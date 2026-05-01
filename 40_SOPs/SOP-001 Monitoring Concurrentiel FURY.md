# SOP-001: Monitoring Concurrentiel FURY

**Statut :** ✅ Actif
**Créé :** 2026-05-01
**Mis à jour :** 2026-05-01
**Responsable :** FURY (Worker Veille Concurrentielle)

## Contexte
FURY effectue un scraping quotidien de 3 concurrents de Clyro pour détecter changements d'offres, de prix, de design et de positionnement.

## Pré-requis
- [ ] Script `fury_monitor.sh` présent dans `/opt/data/skills/autonomous-ai-agents/fury-competitor-monitor/scripts/`
- [ ] Cron FURY actif (09:00 UTC)
- [ ] Accès internet fonctionnel

## Étapes

### 1. Exécution automatique (Cron)
Le cron `FURY - Monitorage Concurrentiel Quotidien (09h)` se déclenche automatiquement à 09:00 UTC.

### 2. Scraping des sites
FURY scrape les 3 concurrents simultanément et extrait le texte brut.

### 3. Extraction de signaux
Les patterns regex détectent : CTAs, tarifs, services, éléments de confiance.

### 4. Génération du brief
Un brief consolidé est généré dans `/opt/data/fury_monitor/daily_brief.md`.

### 5. Archivage (COULSON)
Le brief est copié dans `30_Concurrents/` et référencé dans `30_Concurrents/Briefs FURY.md`.

## Checklist de sortie
- [ ] Brief FURY généré et livrable à Laurent
- [ ] Signaux extraits et catégorisés
- [ ] Brief archivé dans le vault Obsidian

## Notes & Pièges à éviter
- ⚠️ Les sites avec JavaScript dynamique ne sont pas scrapés → utiliser Playwright si besoin
- ⚠️ Captchas ou Cloudflare → fallback vers cache
- 💡 Ajouter des concurrents en éditant la skill `fury-competitor-monitor`

## Liens connexes
- [[Briefs FURY]]
- [[Fury Competitor Monitor Skill]]
