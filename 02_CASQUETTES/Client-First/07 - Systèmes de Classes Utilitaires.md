# 07 — Systèmes de Classes Utilitaires

> **Source :** [finsweet.com/client-first/fr/systemes-classes-utilitaires](https://finsweet.com/client-first/fr/systemes-classes-utilitaires)

---

## Les 3 systèmes principaux

Le clonable Client-First inclut 3 systèmes de classes utilitaires globales :

| Système | Rôle | Exemples |
|---|---|---|
| 🏗️ **Structure** | Base HTML de la page | `page-wrapper`, `section_`, `container-large` |
| ✍️ **Typographie** | Styles de texte | `text-size-large`, `heading-style-h1` |
| 📏 **Espacement** | Marges et paddings | `margin-bottom-medium`, `padding-global` |

---

## Système de structure (rappel)

Voir [[04 - Structure de Base]] pour le détail complet.

---

## Système d'espacement (Spacing)

### Padding global
```
padding-global          → padding-left + padding-right (ex: 2.5rem)
```

### Padding de section
```
padding-section-large   → padding-top + padding-bottom (ex: 8rem)
padding-section-medium  → padding-top + padding-bottom (ex: 5rem)
padding-section-small   → padding-top + padding-bottom (ex: 3rem)
```

### Marges
```
margin-top-large        → margin-top (ex: 4rem)
margin-top-medium       → margin-top (ex: 2rem)
margin-top-small        → margin-top (ex: 1rem)
margin-bottom-large     → margin-bottom (ex: 4rem)
margin-bottom-medium    → margin-bottom (ex: 2rem)
margin-bottom-small     → margin-bottom (ex: 1rem)
margin-vertical-large   → margin-top + margin-bottom (ex: 4rem)
margin-horizontal-medium → margin-left + margin-right (ex: 2rem)
```

---

## Système de couleurs

```
background-color-black
background-color-white
background-color-primary
background-color-secondary
background-color-grey
text-color-black
text-color-white
text-color-primary
text-color-grey
```

---

## Système de visibilité

```
hide                    → display: none
show                    → display: block
hide-mobile             → display: none sur mobile (media query)
show-mobile             → display: block sur mobile (media query)
hide-tablet             → display: none sur tablette
show-tablet             → display: block sur tablette
```

---

## Système Flexbox

```
flex-horizontal         → display: flex; flex-direction: row
flex-vertical           → display: flex; flex-direction: column
flex-align-center       → align-items: center
flex-align-start        → align-items: flex-start
flex-justify-center     → justify-content: center
flex-justify-between    → justify-content: space-between
flex-gap-small          → gap: 1rem
flex-gap-medium         → gap: 2rem
```

---

## Système Grid

```
grid-2-col              → display: grid; grid-template-columns: 1fr 1fr
grid-3-col              → display: grid; grid-template-columns: 1fr 1fr 1fr
grid-4-col              → display: grid; grid-template-columns: repeat(4, 1fr)
```

---

## Système de largeur

```
width-full              → width: 100%
width-max-medium        → max-width: 32rem (512px)
width-max-small         → max-width: 24rem (384px)
```

---

## Règles d'usage

1. **Combiner** les utilitaires : `text-size-large text-color-primary flex-horizontal`
2. **Ne pas modifier** les classes utilitaires pour un élément spécifique
3. **Ne pas dupliquer** — si `margin-bottom-medium` existe, ne pas créer `margin-bottom-32px`
4. **Adapter le système** — ajouter/supprimer des utilitaires selon les besoins du projet