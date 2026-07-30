# 03 — Stratégie des Classes

> **Source :** [finsweet.com/client-first/fr/strategie-classes-partie-1](https://finsweet.com/client-first/fr/strategie-classes-partie-1)

---

## Deux types de classes

### 1. Classes utilitaires (Utility Classes)

Classe avec une combinaison **spécifique de propriétés CSS** appliquée globalement à différents éléments.

**Caractéristiques :**
- Toujours **globales** par nature
- Utilisent un **tiret simple** `-` (pas de `_`)
- Réutilisables sur n'importe quel élément
- Appliquent **une seule responsabilité CSS**

**Exemples :**
```
background-color-gray
font-size-large
text-color-white
padding-global
margin-bottom-medium
```

### 2. Classes personnalisées (Custom Classes)

Classe créée pour un **composant, une page, un groupe ou un élément unique**.

**Caractéristiques :**
- Créées quand les classes utilitaires ne suffisent pas
- Utilisent un **underscore** `_` comme séparateur
- Spécifiques à un élément/composant

**Exemples :**
```
hero_component
nav_menu
card_wrapper
footer_link
```

---

## Conventions de nommage

### Structure du nom

```
[categorie]_[élément]
```

### Préfixes par catégorie

| Préfixe | Usage | Exemple |
|---|---|---|
| Pas de préfixe | Classes utilitaires globales | `padding-global` |
| `section_` | Sections de page | `section_hero` |
| `component_` | Composants réutilisables | `component_card` |
| `layout_` | Éléments de mise en page | `layout_grid` |
| `nav_` | Navigation | `nav_link` |
| `footer_` | Pied de page | `footer_social` |

---

## Règle d'or

> 🎯 **Toujours privilégier les classes utilitaires avant de créer une classe personnalisée.**

Si un style peut être obtenu avec des classes utilitaires existantes, **ne pas créer de nouvelle classe**.

---

## Comparaison rapide

| | Utility Class | Custom Class |
|---|---|---|
| **Symbole** | `-` (tiret) | `_` (underscore) |
| **Portée** | Globale | Locale / composant |
| **Réutilisation** | Partout | Spécifique |
| **Exemple** | `text-size-large` | `hero_title` |
| **Modification** | Impact global | Impact local |