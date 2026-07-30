# 06 — Stratégie Typographique

> **Source :** [finsweet.com/client-first/fr/strategie-typographique](https://finsweet.com/client-first/fr/strategie-typographique)

---

## Les balises HTML sont les valeurs par défaut

Dans un monde parfait, on n'aurait jamais besoin de mettre une classe sur un `<h1>` ou un `<p>`. Les balises HTML natives suffisent. En pratique, les designs demandent des variations → on utilise des **classes utilitaires**.

---

## Système de classes typographiques

Client-First utilise deux préfixes pour la typographie :

### `text-*` (corps de texte, paragraphes)

| Classe | Usage typique |
|---|---|
| `text-size-small` | Texte secondaire, légendes |
| `text-size-regular` | Texte de corps par défaut |
| `text-size-medium` | Texte accentué |
| `text-size-large` | Grand texte, citations |
| `text-color-white` | Texte blanc |
| `text-color-primary` | Couleur de marque |
| `text-weight-bold` | Gras |
| `text-weight-xbold` | Extra-gras |
| `text-align-center` | Centré |
| `text-align-right` | Aligné à droite |
| `text-style-italic` | Italique |
| `text-style-uppercase` | Majuscules |

### `heading-*` (titres)

| Classe | Usage typique |
|---|---|
| `heading-style-h1` | Même style que H1 |
| `heading-style-h2` | Même style que H2 |
| `heading-style-h3` | Même style que H3 |
| `heading-size-xlarge` | Très grand titre |
| `heading-size-large` | Grand titre |
| `heading-size-medium` | Titre moyen |

---

## Avantages du système

| Bénéfice | Explication |
|---|---|
| 🌐 **Gestion globale** | Changer `text-size-large` met à jour TOUS les textes l'utilisant |
| 🚫 **Évite les classes inutiles** | Pas besoin de `paragraph-about-page-size-18` |
| 🎯 **Sémantique préservée** | On garde les balises HTML natives (`<h1>`, `<p>`) |
| 📐 **Design system cohérent** | Tailles et styles unifiés sur tout le site |
| ♿ **Accessibilité** | Hiérarchie de titres respectée |

---

## Règles d'usage

1. ✅ Les balises HTML (`h1`–`h6`, `p`) portent les styles par défaut
2. ✅ On ajoute une classe utilitaire **uniquement pour une variation**
3. ✅ `text-size-*` ≠ balise `h*` — on peut avoir un `h2` avec `text-size-small`
4. ❌ Ne pas créer `hero_title_font_size_v2` — utiliser les utilitaires existants

---

## Exemple

```html
<!-- Style par défaut du H1 -->
<h1>Mon titre principal</h1>

<!-- H2 avec taille personnalisée via utilitaire -->
<h2 class="heading-size-medium text-color-primary">
  Sous-titre accentué
</h2>

<!-- Paragraphe avec variation -->
<p class="text-size-small text-color-grey">
  Texte secondaire
</p>
```