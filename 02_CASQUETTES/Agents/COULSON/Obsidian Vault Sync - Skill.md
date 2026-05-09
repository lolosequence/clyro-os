---
name: obsidian-vault-sync
description: Setup and maintain Git-based sync between Obsidian vault on this server and the local PC. Covers HTTPS PAT auth, repo init, push/pull, Obsidian Git config, and common troubleshooting.
---

# Obsidian Vault Git Sync

Syncs the Obsidian vault between this server (`/root/Documents/Obsidian Vault/Clyro OS`) and Laurent's PC Windows (`C:\Users\laure\clyro-os`).

**GitHub repo:** https://github.com/lolosequence/clyro-os.git
**GitHub user:** lolosequence
**Auth method:** HTTPS with Personal Access Token (PAT) — stored via git credential store
**Vault path on server:** `/root/Documents/Obsidian Vault/Clyro OS`

## Initial Setup (one-time)

### 1. Server-side Git setup (already done)

The server uses HTTPS PAT auth, not SSH. Credentials are stored via `git credential store` in `~/.git-credentials`.

```bash
cd "/root/Documents/Obsidian Vault/Clyro OS"
git status          # verify repo exists
git remote -v       # should show HTTPS origin with PAT
git log --oneline   # verify commits
```

### 2. On Windows PC (user does this)

**DO NOT use `git init` + `git fetch`** — it fails with "fatal: not a git repository" errors and is confusing. Instead, **re-clone cleanly**:

```powershell
cd C:\Users\laure
# If folder exists and is broken:
rm -Recurse -Force clyro-os
git clone https://github.com/lolosequence/clyro-os.git
cd clyro-os
git log --oneline -3
```

Then open `C:\Users\laure\clyro-os` as a vault in Obsidian.

### 3. Configure Obsidian Git plugin (PC side)

In Obsidian → Settings → Obsidian Git (by Vinzent03):

- **Git Pull on refresh** → ON
- **Auto backup interval** → 5 or 10 minutes (auto commit + push)
- **Auto backup on file change** → ON (immediate commit on note changes)
- **Push on backup** → ON (send to GitHub after each commit)
- **Commit message** → default is fine, or `Update: {{date}}`

## Daily sync commands

### Push from server
```bash
cd "/root/Documents/Obsidian Vault/Clyro OS"
git add .
git commit -m "Auto-sync $(date +%Y-%m-%d)"
git push
```

### Pull on server (get changes from PC)
```bash
cd "/root/Documents/Obsidian Vault/Clyro OS"
git pull --rebase
```

### Force pull (overwrites local changes)
```bash
cd "/root/Documents/Obsidian Vault/Clyro OS"
git fetch origin
git reset --hard origin/master
```

## Pitfall: Rename/Rename Conflicts with COULSON Auto-Maintenance

COULSON runs daily cron maintenance (09h) that moves/renames vault files (e.g., `00_Inbox/` → `02_CASQUETTES/` or `50_Knowledge/`). If you make a commit while COULSON also commits renames, `git pull --rebase` WILL hit a `CONFLICT (rename/rename)` error:

```
CONFLICT (rename/rename): file.md renamed to path/A in HEAD and to path/B in COMMIT
```

Both `git pull --rebase --autostash` and `git merge` will fail. Standard resolution:

```bash
# 1. Abort whatever is stuck (rebase or merge)
git rebase --abort   # or: git merge --abort

# 2. Reset cleanly to remote state
git reset --hard origin/main   # requires approval — note uncommitted files first!

# 3. Re-apply your changes on top of the clean state
# Then commit and push normally
git add . && git commit -m "..." && git push
```

**Prevention**: Before committing new files on the server, always `git pull --rebase` first to catch any COULSON changes. If COULSON cron just ran (around 09h UTC), wait a minute for it to finish before pushing.

## Troubleshooting

### Not a git repository on PC
- Folder exists but has no `.git` — re-clone: `rm -Recurse -Force clyro-os && git clone https://github.com/lolosequence/clyro-os.git`

### PAT expired
- Generate a new PAT at https://github.com/settings/tokens (repo scope)
- Update: `git remote set-url origin https://lolosequence:NEW_TOKEN@github.com/lolosequence/clyro-os.git`
- Then re-authenticate on PC

### Conflicts on push
- Pull with rebase first: `git pull --rebase`
- Resolve any conflicts, then push

### Files created on server not visible in Obsidian PC
- Ensure Git push succeeded on server: `git push` + check exit code
- Ensure Git pull succeeded on PC: `git pull`
- Check both are using the same branch (master)
- Verify path on PC is correct: `C:\Users\laure\clyro-os`

### Obsidian Git plugin not pushing
- Check plugin is enabled in Obsidian settings
- Check git is installed and in PATH on PC
- Verify the vault was opened as a Git repo (should show Git icon or sync status)
- Try "Create backup" manually from the Git ribbon

## Branch setup

- **Always use `main` on the server** — GitHub defaults to `main`, and PC clones will also use `main`.
- If the server is on `master`, switch:
```bash
cd "/root/Documents/Obsidian Vault/Clyro OS"
git checkout -b main      # create main tracking origin/main if needed
git branch -D master      # remove old branch
```

## Obsidian Git plugin: push not happening

- Check Git icon in Obsidian sidebar (bottom-left) for error status
- On Windows PC, verify git credentials are configured:
```powershell
git config --global credential.helper manager
git pull   # triggers credential prompt, enters username/PAT once
```
- Can manually trigger: Git ribbon → "Create Backup and Push"
- If push fails with "Permission denied", the Windows git may need PAT auth — re-clone with credentials embedded:
```powershell
git clone https://lolosequence:YOUR_PAT@github.com/lolosequence/clyro-os.git
```

## Notes
- The vault is NOT managed by Obsidian Sync on the server side (no Obsidian desktop app installed here)
- Obsidian Sync may still be active on the PC for mobile/other device sync
- Git is the server ↔ PC bridge
- `.obsidian/` folder is created by Obsidian on first open — include it in the vault so plugin settings sync
- The server-side branch is **master** (not main) — this is important for any git commands referencing the branch
