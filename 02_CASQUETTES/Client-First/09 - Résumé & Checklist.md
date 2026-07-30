# 09 — Résumé & Checklist Client-First

---

## 🎯 Les 8 commandements

| # | Règle | Pourquoi |
|---|---|---|
| 1 | **Utility classes d'abord** | Limiter les classes personnalisées |
| 2 | **`-` = utilitaire, `_` = personnalisé** | Distinguer visuellement |
| 3 | **Structure identique** sur toutes les pages | Prévisibilité |
| 4 | **Toujours dans un container** | `page-wrapper` > `section_` > `padding-global` > `container-*` |
| 5 | **Tout en REM** | Accessibilité |
| 6 | **Multiples de 0.5rem** | Cohérence visuelle |
| 7 | **Balises HTML = styles par défaut** | Classes seulement pour variations |
| 8 | **Dossiers par fonction** | Pas par page, pas par couleur |

---

## 📋 Checklist de mise en œuvre

### Démarrage
- [ ] Cloner le projet de démarrage Client-First
- [ ] Configurer les couleurs du projet
- [ ] Définir la typographie par défaut (balises HTML)

### Structure
- [ ] `page-wrapper` sur chaque page
- [ ] Structurer en `section_*`
- [ ] `padding-global` dans chaque section
- [ ] `container-large/medium/small` selon le contenu

### Classes
- [ ] Préfixer les sections : `section_`
- [ ] Préfixer les composants : `component_`
- [ ] Utiliser `text-size-*`, `heading-style-*`
- [ ] Utiliser `margin-*`, `padding-*`

### Organisation
- [ ] Dossiers dans le Designer
- [ ] Utilitaires dans `Utility/`
- [ ] Classes personnalisées par catégorie
- [ ] Nettoyer avant livraison

### Qualité
- [ ] Aucun `px` (sauf exceptions)
- [ ] Test responsive
- [ ] Accessibilité (contraste, hiérarchie titres)

---

## 🧰 Ressources

| Ressource | Lien |
|---|---|
| Documentation | [finsweet.com/client-first](https://finsweet.com/client-first) |
| Projet clonable | Via dashboard Finsweet |
| Extension | Finsweet Extension pour Webflow |