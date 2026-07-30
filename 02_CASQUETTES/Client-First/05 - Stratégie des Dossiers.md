# 05 — Stratégie des Dossiers (Folders)

> **Source :** [finsweet.com/client-first/fr/strategie-des-dossiers](https://finsweet.com/client-first/fr/strategie-des-dossiers)

---

## Philosophie

> 💡 **"Une convention de nomination unique pour chaque projet"**

Il n'y a pas de structure unique. La flexibilité est essentielle pour s'adapter à chaque projet. Il n'y a pas de « bon » ou « mauvais » choix — seulement des nominations plus ou moins efficaces.

---

## Modèles d'organisation

### Modèle A — Par type de composant

```
Classes Client-First/
├── Utility/
│   ├── Typography/
│   ├── Spacing/
│   └── Colors/
├── Sections/
│   ├── section_hero
│   └── section_features
├── Components/
│   ├── component_card
│   └── component_nav
└── Layout/
    ├── layout_grid
    └── layout_flex
```

### Modèle B — Par page

```
Classes Client-First/
├── Global/
│   └── Utility/
├── Homepage/
│   ├── section_home_hero
│   └── section_home_team
├── About/
│   └── section_about_story
└── Blog/
    └── component_blog_card
```

### Modèle C — Minimaliste

```
Classes Client-First/
├── Utility/
└── Custom/
    ├── Sections/
    └── Components/
```

---

## Règles de nommage

| Règle | Exemple |
|---|---|
| Noms **descriptifs** | `Typography` pas `Type` |
| Grouper par **fonction** | `Buttons` pas `Blue Elements` |
| Max **2-3 niveaux** | Pas de `A/B/C/D/E/ma_classe` |
| Utilitaires **en premier** | `Utility/` avant `Custom/` |

---

## ⚠️ Pièges

| ❌ Éviter | ✅ Privilégier |
|---|---|
| Dossiers par couleur | Dossiers par fonction |
| Trop de niveaux | Max 2-3 niveaux |
| Mélanger utilitaire/perso | Séparation claire |
| Noms vagues (`truc`) | Noms explicites (`Sections`) |