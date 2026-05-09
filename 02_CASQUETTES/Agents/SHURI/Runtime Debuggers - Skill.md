---
name: runtime-debuggers
description: "Debug live processes: Python (pdb/debugpy/remote-pdb), Node.js (--inspect/CDP), and Hermes TUI slash commands (Python↔gateway↔Ink layers)."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [debugging, python, pdb, debugpy, nodejs, node-inspect, cdp, hermes-agent, tui, slash-commands, breakpoints, dap, post-mortem]
    related_skills: [systematic-debugging, hermes-agent-skill-authoring]
---

# Runtime Debuggers

Three debugger families in one place — choose by language/runtime:

| Section | Use when |
|---|---|
| **Python** | Test fails, async handler deadlocks, gateway/daemon misbehaves, exception in prod |
| **Node.js** | ui-tui crashes, Ink state wrong, tui_gateway child process misbehaves |
| **Hermes TUI commands** | Slash command missing from autocomplete, works in CLI but not TUI, config persists but UI doesn't update |

---

## Python (pdb + debugpy + remote-pdb)

Full reference: [references/python-debugpy.md](references/python-debugpy.md)

### Three tools, pick one

| Tool | When |
|---|---|
| `breakpoint()` + pdb | Local, interactive, simplest. Add `breakpoint()` in source, run normally. |
| `python -m pdb` | Launch script under pdb with no source edits. |
| `debugpy` | Remote / headless / attach to already-running process. Talks DAP. |
| `remote-pdb` | Best agent-friendly choice for long-lived processes: `nc 127.0.0.1 4444` gives a pdb REPL. |

### pdb Quick Reference

| Command | Action |
|---|---|
| `n` | next (step over) |
| `s` | step into |
| `r` | return from current function |
| `c` | continue |
| `w` | where (stack trace) |
| `u` / `d` | up / down in stack |
| `p expr` | print expression |
| `interact` | full Python REPL in current scope (Ctrl+D to exit) |
| `b file:line` | set breakpoint |
| `q` | quit |

### Key Recipes

**Local breakpoint:**
```python
def compute(x, y):
    result = some_helper(x)
    breakpoint()   # drops into pdb
    return result + y
```

**Debug a pytest test (pdb under xdist DOES NOT WORK — always add `-p no:xdist`):**
```bash
scripts/run_tests.sh tests/path/test.py::test_name --pdb -p no:xdist
```

**Remote attach with remote-pdb (best for gateway, tui_gateway):**
```python
from remote_pdb import set_trace
set_trace(host="127.0.0.1", port=4444)
```
Then: `nc 127.0.0.1 4444`

**Post-mortem:**
```bash
python -m pdb -c continue script.py
# On crash, pdb lands at the frame of the exception
```

### Hermes-specific processes

- **Tests:** `scripts/run_tests.sh ... --pdb -p no:xdist` (xdist silently swallows pdb prompts)
- **tui_gateway subprocess:** add `remote_pdb.set_trace()` at the RPC handler; trigger the slash command; `nc` in another terminal
- **`_SlashWorker`:** same pattern — `set_trace()` in `exec` path, first trigger blocks, subsequent pass through
- **CLI one-shot:** add `breakpoint()` near the suspect line, run `hermes` normally

### Common pitfalls

1. **pdb under pytest-xdist silently hangs.** Always use `-p no:xdist` or `-n 0`.
2. **`PYTHONBREAKPOINT=0`** disables all `breakpoint()` calls. Check the env.
3. **`debugpy.listen` blocks only if you also call `wait_for_client()`.** Without it, execution races past your breakpoints.
4. **Threads:** pdb only debugs the current thread. Use `debugpy` for multithreaded code.
5. **`asyncio`:** `await` inside pdb requires Python 3.13+ or `interact` mode workaround.

---

## Node.js (--inspect + CDP)

Full reference: [references/node-inspect-debugger.md](references/node-inspect-debugger.md)

### Two tools, pick one

- **`node inspect`** — built-in, zero install, CLI REPL. Best for quick poking.
- **CDP via `chrome-remote-interface`** — scriptable; best for automation, many breakpoints, non-interactive debugging.

**Prefer `node inspect` first.**

### `node inspect` Quick Reference

```bash
node inspect path/to/script.js
# or TypeScript via tsx:
node --inspect-brk --import tsx script.ts
```

| Command | Action |
|---|---|
| `c` / `cont` | continue |
| `n` / `next` | step over |
| `s` / `step` | step into |
| `o` / `out` | step out |
| `sb('file.js', 42)` | set breakpoint |
| `sb('functionName')` | break when function is called |
| `bt` | backtrace |
| `repl` | REPL in current scope (Ctrl+C to exit) |
| `exec expr` | evaluate expression once |
| `.exit` | quit |

### Attach to running process

```bash
kill -SIGUSR1 <pid>           # enable inspector on existing process
node inspect -p <pid>         # attach
curl -s http://127.0.0.1:9229/json/list  # find WS URL
```

### Debugging Hermes ui-tui

```bash
# Attach to hermes --tui's Node process
hermes --tui &
TUI_PID=$(pgrep -f 'ui-tui/dist/entry' | head -1)
kill -SIGUSR1 "$TUI_PID"
node inspect -p "$TUI_PID"
```

Then in `debug>`:
```
sb('dist/app.js', 220)
cont
```

### Running Vitest under the debugger

```bash
cd /home/bb/hermes-agent/ui-tui
node --inspect-brk ./node_modules/vitest/vitest.mjs run --no-file-parallelism src/app/foo.test.tsx
# In another terminal: node inspect -p <pid>
```

### Common pitfalls

1. **Wrong line numbers in TS source.** Break in built `dist/*.js`, or enable `--enable-source-maps` with a CDP client.
2. **`--inspect` vs `--inspect-brk`.** Use `--inspect-brk` to pause before any code runs; `--inspect` races.
3. **Port collisions.** Default is `9229`. Use `--inspect=0` for random port; check `/json/list`.
4. **Child processes.** `--inspect` on parent does NOT inspect children. Use `NODE_OPTIONS='--inspect'`.
5. **Hermes terminal:** use `terminal(pty=true)` for interactive stepping.

---

## Hermes TUI Slash Commands

Full reference: [references/hermes-tui-commands.md](references/hermes-tui-commands.md)

### Architecture

```
Python backend (hermes_cli/commands.py)   ← canonical COMMAND_REGISTRY
       │
tui_gateway (tui_gateway/server.py)       ← slash.exec / command.dispatch
       │
TUI frontend (ui-tui/src/app/slash/)      ← local handlers + fallthrough
```

**Python `COMMAND_REGISTRY` is the source of truth** for: CLI dispatch, gateway help, autocomplete data shipped to Ink, Telegram BotCommand menu, Slack subcommand map.

### Fix: Missing autocomplete

Add a `CommandDef` entry to `COMMAND_REGISTRY` in `hermes_cli/commands.py`:

```python
CommandDef("commandname", "Description", "Session",
           cli_only=True, aliases=("alias",),
           args_hint="[arg1|arg2|arg3]",
           subcommands=("arg1", "arg2", "arg3")),
```

### Common failure modes

1. **Command in TUI but not autocomplete.** Missing from `COMMAND_REGISTRY`. Autocomplete data ships from Python.
2. **Command in autocomplete but doesn't work.** Check handler in `tui_gateway/server.py` and frontend in `createSlashHandler.ts`.
3. **Behavior differs between CLI and TUI.** Different implementations. Check `cli.py::process_command` vs local TUI handler.
4. **Config persists but UI doesn't update.** Also patch the relevant nanostore state immediately (`patchUiState(...)`).
5. **Gateway silently ignores the command.** Check `GATEWAY_KNOWN_COMMANDS` includes the canonical name.

### Verification

```bash
cd /home/bb/hermes-agent && npm --prefix ui-tui run build
hermes --tui
# Type / and verify autocomplete, execute, check config
```

For gateway-available commands:
```bash
scripts/run_tests.sh tests/gateway/
```

### Detailed Investigation Steps (from absorbed debugging-hermes-tui-commands)

When surface-level inspection doesn't reveal the bug, follow these steps:

1. **Check if the command exists in the TUI frontend:**
   ```
   search_files --pattern "/commandname" --file_glob "*.ts" --path ui-tui/
   ```
2. **Check if it exists in the Python backend:**
   ```
   search_files --pattern "CommandDef" --file_glob "*.py" --path hermes_cli/
   ```
3. **Check the gateway:**
   ```
   search_files --pattern "slash.exec|command.dispatch" --path tui_gateway/
   ```

**Pick `cli_only` vs gateway availability carefully:**
- `cli_only=True` — only in the interactive CLI/TUI
- `gateway_only=True` — only in messaging platforms
- neither — available everywhere
- `gateway_config_gate="display.foo"` — config-gated availability

**After adding live UI state**, search every consumer of the old prop/helper and thread the new state through all render paths, not just the active streaming path. TUI detail rendering has at least two paths: live `StreamingAssistant`/`ToolTrail` and transcript/pending `MessageLine` rows.

For deeper debugging of the Python side, use the Python (pdb/debugpy) section above. For the Ink/Node side, use the Node.js section above.

---

## Verification Checklist

**Python:**
- [ ] `python -c "import debugpy; print(debugpy.__version__)"` if using debugpy
- [ ] `ss -tlnp | grep 5678` confirms port is listening for remote debug
- [ ] First breakpoint actually hits (`PYTHONBREAKPOINT=0`? xdist? execution finished before attach?)
- [ ] Post-debug: no stray `breakpoint()` / `set_trace()` in committed code: `rg -n 'breakpoint\(\)|set_trace\(' --type py`

**Node.js:**
- [ ] `curl -s http://127.0.0.1:9229/json/list` returns the expected target
- [ ] First breakpoint actually hits (missed `--inspect-brk`? attached after execution?)
- [ ] `exec process.pid` in repl returns the PID you meant to attach to

**Hermes TUI:**
- [ ] Rebuild TUI before testing: `npm --prefix ui-tui run build`
- [ ] Command appears in autocomplete with expected description and args hint
- [ ] Expected behavior fires; persisted config updates correctly; live UI state reflects change immediately
