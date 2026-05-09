---
name: fury-competitor-monitor
description: FURY — regional competitor intelligence agent for Clyro. Monitors local competitors by city/region, verifies Google Business Profile, social media presence + activity, Google reviews, and websites. Produces a daily brief + structured JSON with confidence levels per signal. Designed for local business prospecting.
version: 2.0.0
metadata:
  hermes:
    tags: [clyro, fury, competitor, monitoring, local, regional, GBP, social, prospection]
    related_skills: ["jarvis-ceo-agent"]
---

# FURY — Competitor Monitoring (CNT Patrimoine)

## Overview

FURY scrapes competitor websites daily for **CNT Patrimoine** (client de Clyro). CNT Patrimoine est un client de l'agence Clyro. Les concurrents surveillés sont ceux de CNT Patrimoine, PAS les concurrents généraux de Clyro.

FURY détecte les changements, extrait les signaux compétitifs, et génère un brief actionnable pour Laurent (Clyro CEO).

## Competitors (CNT Patrimoine)

| # | Name | URL | Niche |
|---|---|---|---|
| 1 | Meilleur Investissement Immobilier | https://meilleur-investissement-immobilier.com/ | Investissement immobilier |
| 2 | Gestion de Patrimoine | https://gestiondepatrimoine.com/ | Gestion de patrimoine |
| 3 | Bertrand Demanes | https://www.bertrand-demanes.fr/ | Conseil patrimoine |

## Script Usage

```bash
# Run full monitoring (scrape + brief generation)
bash /opt/data/skills/autonomous-ai-agents/fury-competitor-monitor/scripts/fury_monitor.sh

# Run with debug mode
bash /opt/data/skills/autonomous-ai-agents/fury-competitor-monitor/scripts/fury_monitor.sh --debug
```

## Output Files

- `/opt/data/fury_monitor/daily_brief.md` — Daily intelligence brief (temp)
- `/opt/data/fury_monitor/signals.json` — Structured signal data
- **Brief FURY vault** → `/root/Documents/Obsidian Vault/Clyro OS/01_PROJETS/Clyro/Clients/CNT Patrimoine/Concurrents_CNT/Brief FURY YYYY-MM-DD.md`
- `/opt/data/fury_monitor/history/` — Historical snapshots (one per day)

## Signals Detected

- **New offers** — New services or products announced
- **Pricing changes** — Price modifications, new fee structures
- **Design changes** — New homepage layout, new hero sections
- **New CTAs** — New call-to-action buttons, new lead magnets
- **Content changes** — New blog posts, new landing pages
- **Trust signals** — New testimonials, new certifications, new partnerships
- **Target changes** — New audience segments mentioned

## Integration

FURY is designed to be called by JARVIS (CEO agent) or via cron job at 09:00 daily.
The cron job reads `daily_brief.md` and delivers a formatted report to Laurent.

## Pitfalls (from actual runs)

### Scripts with spaces in competitor names
Competitor names contain spaces ("Gestion de Patrimoine", etc.). Common traps:
- **Never pass scraped content as shell arguments** — the heredoc `<<< "$raw_content"` breaks on HTML with special chars. Use temp files instead.
- **Never pass file paths via sys.argv** to Python heredoc when paths contain spaces. Use environment variables (`COMPETITOR_NAME`, `CONTENT_FILE`, `SIGNALS_FILE`) instead.
- **Always mkdir -p the per-competitor subdirectory** before writing scraped content. The main script must create these, not assume they exist.
- **Use `mkdir -p "$OUTPUT_DIR/$competitor"` inside the loop**, not once at the top.

### Signal extraction gotchas
- `grep -o` is unreliable for multi-line HTML extraction. Python `re` against cleaned text is much better.
- The HTML text extractor must skip `<script>`, `<style>`, `<nav>`, `<footer>`, `<svg>` — these are noise, not signals.
- Deduplicate signal values case-insensitively (`clean.lower()` check).

## Improvement Path
## Pitfalls

### Competitor names with spaces
Competitor names often contain spaces (e.g. "Gestion de Patrimoine"). This causes two problems:

1. **Directory creation** — Must always `mkdir -p "$OUTPUT_DIR/$competitor"` BEFORE writing scraped content, or the script fails with "No such file or directory".

2. **Heredoc + sys.argv** — Bash heredocs with `python3 << 'PYEOF' "$arg1" "$arg2" "$arg3"` break when arguments contain spaces. The shell splits them incorrectly.

**Fix**: Use environment variables instead of positional arguments:
```bash
COMPETITOR_NAME="$competitor_name" CONTENT_FILE="$content_file" SIGNALS_FILE="$signals_file" python3 << 'PYEOF'
import os
competitor_name = os.environ['COMPETITOR_NAME']
content_file = os.environ['CONTENT_FILE']
signals_file = os.environ['SIGNALS_FILE']
```

### Don't pass HTML content as shell arguments
Passing raw HTML via stdout into a Python heredoc breaks with quotes, special chars, and length. Fix: write HTML to a temp file first, have Python read from that file.

### curl can fail silently
Some sites may block or timeout. Always use `--max-time` and handle failures gracefully. The script uses `|| true` to continue even if one competitor fails.

## Improvement Path

- Add screenshots for visual comparison (diffoscope/Playwright)
- Add RSS feed monitoring
- Add social media monitoring (LinkedIn pages)
- Add Google Ads monitoring (SpyFu, SimilarWeb)
- Add competitor backlink monitoring
- Add change detection (diff against previous scrape with date tracking)

## Pitfalls

### Spaces in competitor names
Competitor names with spaces (e.g. "Gestion de Patrimoine") break both:
- **`mkdir`** — the script must `mkdir -p "$OUTPUT_DIR/$competitor"` BEFORE writing any files
- **Python sys.argv** — shell argument splitting breaks paths with spaces. Use environment variables instead:
  ```bash
  COMPETITOR_NAME="$competitor_name" CONTENT_FILE="$content_file" SIGNALS_FILE="$signals_file" python3 << 'PYEOF'
  import os
  competitor_name = os.environ['COMPETITOR_NAME']
  ...
  ```

### Don't pass HTML content as shell arguments
The initial `scrape_website` passed `curl` stdout as a shell argument to a python heredoc. This breaks with any non-trivial HTML (quotes, special chars, length). Fix: write HTML to a temp file first, have python read from that file.

### Use file-based scraping, not stdout piping
Correct pattern:
```bash
# Step 1: curl to temp file
curl -s -L --max-time 15 "$url" -o "$html_file"
# Step 2: python reads from file, extracts text to output file
python3 ... "$html_file" > "$output_file"
```