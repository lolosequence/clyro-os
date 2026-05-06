# Tracking des Cout des Taches Clyro OS

> Date de creation: 2026-05-06
> Dernière mise à jour: 2026-05-06

---

## Methodologie

Les sessions Hermes ne stockent pas les compteurs de tokens OpenRouter natifs. Les couts sont **estimes** avec la formule :
- `1 token ≈ 4 caracteres` (standard pour FR/EN)
- Cout input : tokens d'entree (system prompt + user prompt + tool outputs)
- Cout output : tokens de sortie (reponses assistant)

Les chiffres sont des **ordres de grandeur fiables** mais pas exacts au centime.

---

## Tableaux des prix des modeles (OpenRouter USD / 1M tokens)

| Model | Input ($/1M) | Output ($/1M) | Ratio input/output |
|-------|-------------:|--------------:|-------------------:|
| **qwen/qwen3.6-plus** | $0.10 | $0.40 | 1:4 |
| openai/gpt-4o-mini | $0.15 | $0.60 | 1:4 |
| google/gemini-2.5-flash | $0.15 | $0.60 | 1:4 |
| meta-llama/llama-4-maverick | $0.20 | $0.80 | 1:4 |
| openai/gpt-4o | $2.50 | $10.00 | 1:4 |
| google/gemini-2.5-pro | $1.25 | $5.00 | 1:4 |
| anthropic/claude-sonnet-4 | $3.00 | $15.00 | 1:5 |
| anthropic/claude-opus-4 | $15.00 | $75.00 | 1:5 |

---

## Cronjobs Actifs

### 1. FURY — Monitorage Concurrentiel Quotidien (09h)

| Detail | Valeur |
|--------|-------|
| **Job ID** | `521ac76240c7` |
| **Schedule** | `0 9 * * *` (quotidien 09h UTC) |
| **Model** | qwen/qwen3.6-plus |
| **Toolsets** | web, terminal, file, delegation |
| **Tool calls/run** | ~3 |
| **Skill charge** | Aucun (prompt seul) |

**Breakdown des tokens (estimation):**

| Composante | Chars | Tokens approx |
|------------|------:|-------------:|
| System prompt Hermes | 1,188 | 297 |
| Prompt cron (FURY) | ~2,200 | 550 |
| User + system total input | ~14,156 | 3,539 |
| Assistant output | ~2,332 | 583 |

**Cout par run :**

| Model | Input | Output | Total/run | Total/mois (30 runs) |
|-------|------:|-------:|----------:|---------------------:|
| **qwen3.6-plus (actuel)** | $0.000354 | $0.000233 | **$0.000587** | **$0.0176** |
| GPT-4o Mini | $0.000531 | $0.000350 | $0.000881 | $0.0264 |
| Gemini 2.5 Flash | $0.000531 | $0.000350 | $0.000881 | $0.0264 |
| GPT-4o | $0.008848 | $0.005830 | $0.014677 | $0.4403 |
| Claude Sonnet 4 | $0.010617 | $0.008745 | $0.019362 | $0.5809 |
| Claude Opus 4 | $0.053085 | $0.043725 | $0.096810 | $2.9043 |

---

### 2. COULSON — Maintenance Vault Quotidienne (09h30)

| Detail | Valeur |
|--------|-------|
| **Job ID** | `93267ed7b74b` |
| **Schedule** | `0 9 * * *` (quotidien 09h UTC) |
| **Model** | qwen/qwen3.6-plus |
| **Toolsets** | terminal, file, delegation |
| **Tool calls/run** | ~18 |
| **Skill charge** | Aucun (prompt seul) |

**Breakdown des tokens (estimation):**

| Composante | Chars | Tokens approx |
|------------|------:|-------------:|
| System prompt Hermes | 1,188 | 297 |
| Prompt cron (COULSON) | ~1,400 | 350 |
| User + system total input | ~18,792 | 4,698 |
| Assistant output | ~1,320 | 330 |

**Cout par run :**

| Model | Input | Output | Total/run | Total/mois (30 runs) |
|-------|------:|-------:|----------:|---------------------:|
| **qwen3.6-plus (actuel)** | $0.000470 | $0.000132 | **$0.000602** | **$0.0181** |
| GPT-4o Mini | $0.000705 | $0.000198 | $0.000903 | $0.0271 |
| Gemini 2.5 Flash | $0.000705 | $0.000198 | $0.000903 | $0.0271 |
| GPT-4o | $0.011745 | $0.008300 | $0.015045 | $0.4514 |
| Claude Sonnet 4 | $0.014094 | $0.004950 | $0.019044 | $0.5713 |
| Claude Opus 4 | $0.070470 | $0.024750 | $0.095220 | $2.8566 |

---

## Resume Global — Cout Mensuel

### Cout total actuel (2 cronjobs, qwen3.6-plus)

| Tache | Cout/run USD | Runs/mois | Cout/mois USD | Cout/mois EUR |
|-------|-------------:|----------:|--------------:|--------------:|
| FURY | $0.000587 | 30 | $0.0176 | €0.016 |
| COULSON | $0.000602 | 30 | $0.0181 | €0.017 |
| **TOTAL** | | | **$0.0357** | **€0.032** |

### Si on passait a Claude Sonnet 4

| Tache | Cout/run USD | Runs/mois | Cout/mois USD | Cout/mois EUR |
|-------|-------------:|----------:|--------------:|--------------:|
| FURY | $0.019362 | 30 | $0.5809 | €0.53 |
| COULSON | $0.019044 | 30 | $0.5713 | €0.53 |
| **TOTAL** | | | **$1.15** | **€1.06** |

### Comparaison de couts mensuels par model

| Model | Mensuel USD | Mensuel EUR |
|-------|------------:|------------:|
| **qwen3.6-plus** | $0.036 | €0.033 |
| GPT-4o Mini | $0.054 | €0.050 |
| Gemini 2.5 Flash | $0.054 | €0.050 |
| GPT-4o | $0.892 | €0.821 |
| Gemini 2.5 Pro | $0.401 | €0.369 |
| Claude Sonnet 4 | $1.152 | €1.060 |
| Claude Opus 4 | $5.761 | €5.300 |

---

## Taches Manuelles (chat interactif)

Les couts varient enormement selon la complexite de la conversation. Les interactions manuelles en Telegram typiques :

| Type de tache | Tokens input | Tokens output | Cout (qwen3.6+) | Cout (Sonnet 4) |
|---------------|-------------:|--------------:|----------------:|----------------:|
| Question simple | ~500 | ~200 | $0.0001 | $0.0045 |
| Creation fichier Obsidian | ~2,000 | ~500 | $0.0004 | $0.0135 |
| Config/setup complexe | ~8,000 | ~3,000 | $0.0020 | $0.0690 |
| Debug long | ~15,000 | ~5,000 | $0.0035 | $0.1200 |
| Session complete (100 messages) | ~50,000 | ~20,000 | $0.0130 | $0.4500 |

---

## Recommendations

1. **Model actuel optimal**: qwen/qwen3.6-plus est parfait pour les cronjobs — cout negligeable ($0.036/mois).
2. **Upgrade pour taches critiques**: Pour les sessions interactives complexes (config, debug, creation de skills), Claude Sonnet 4 vaut le cout supplementaire (10-30x plus cher mais bien meilleur raisonnement).
3. **A eviter**: Claude Opus 4 est 160x plus cher que Qwen — a reserver uniquement pour les taches ultra-critiques.
4. **Skills = tokens**: Les skills charges dans un cron ou conversation ajoutent leurs SKILL.md au context. C'est pourquoi la reduction de 103 a 42 skills economise des tokens sur chaque appel.

---

## Historique des changements

| Date | Changement | Impact cout |
|------|-----------|-------------|
| 2026-05-06 | Suppression 61 skills (103→42) | -20-30% tokens system prompt par appel |
| 2026-05-02 | FURY: 4→3 concurrents scrapes | Legere reduction cout FURY |
| 2026-05-01 | Creation cronjobs FURY + COULSON | Base |
