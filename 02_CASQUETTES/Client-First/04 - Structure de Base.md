# 04 — Structure de Base (Core Structure)

> **Source :** [finsweet.com/client-first/fr/strategie-de-structure-de-base](https://finsweet.com/client-first/fr/strategie-de-structure-de-base)

---

## Qu'est-ce que la structure de base ?

Un ensemble de **classes et principes** pour créer une base HTML solide, reconnaissable par tous les utilisateurs de Client-First.

**6 classes** composent la structure de base :

```
page-wrapper          ← Parent suprême de la page
└── main-wrapper      ← Contenu principal
    ├── section_*     ← Sections de la page
    │   ├── padding-global  ← Padding horizontal
    │   ├── container-large/medium/small  ← Conteneur de largeur
    │   └── [contenu]
    └── section_*
```

---

## Détail des 6 classes

### 1. `page-wrapper`
- Parent le plus élevé de tous les éléments
- Englobe TOUT le contenu de la page
- Styles facultatifs, ne pas trop styliser
- **Cas d'usage :** copier/coller toute la page, appliquer `overflow: hidden` global

### 2. `main-wrapper`
- Conteneur du contenu principal
- Sépare le contenu du header/footer si nécessaire
- Entre `page-wrapper` et les sections

### 3. `section_*`
- Chaque section de la page est une `section_`
- Utilise un **underscore** (classe personnalisée)
- Exemples : `section_hero`, `section_features`, `section_cta`

### 4. `padding-global`
- Applique un **padding horizontal uniforme** sur tout le site
- Classe utilitaire globale
- Valeur typique : `padding-left: 2.5rem; padding-right: 2.5rem`

### 5. `container-large` / `container-medium` / `container-small`
- Conteneurs de largeur maximale
- **Centrés** avec `margin: 0 auto`
- Largeurs typiques (en rem) :
  - `container-large` → 80rem (1280px)
  - `container-medium` → 64rem (1024px)
  - `container-small` → 48rem (768px)

### 6. `padding-section-*`
- Espacement vertical entre sections
- `padding-section-large` / `padding-section-medium` / `padding-section-small`
- Exemple : `padding-top: 8rem; padding-bottom: 8rem`

---

## Structure complète type

```html
<div class="page-wrapper">
  <header class="nav_component">...</header>
  
  <main class="main-wrapper">
    <section class="section_hero">
      <div class="padding-global">
        <div class="container-large">
          <!-- contenu hero -->
        </div>
      </div>
    </section>
    
    <section class="section_features">
      <div class="padding-global">
        <div class="container-large">
          <div class="padding-section-large">
            <!-- contenu features -->
          </div>
        </div>
      </div>
    </section>
  </main>
  
  <footer class="footer_component">...</footer>
</div>
```

---

## Principes

1. **Chaque page suit la même structure** — prévisible et maintenable
2. **Les couches s'empilent** — `page-wrapper` > `section` > `padding-global` > `container` > contenu
3. **Jamais de contenu nu** — toujours dans un container
4. **Padding global > padding manuel** — utiliser la classe utilitaire