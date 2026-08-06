# 🔍 Analyse SEO — Douces Émotions

> **Date :** 2026-07-03
> **Site :** [douces-emotions.fr](https://douces-emotions.fr)
> **Client :** Lia Obscur
> **CMS :** WordPress + Elementor

---

## 📊 Score Global

| Catégorie | Note | Statut |
|---|---|---|
| Technique | 3/10 | 🔴 Critique |
| Contenu | 6/10 | 🟡 Moyen |
| On-page SEO | 2/10 | 🔴 Très faible |
| SEO Local | 5/10 | 🟡 À améliorer |
| Réseaux Sociaux | 6/10 | 🟡 Correct |
| **Global** | **4,4/10** | 🔴 |

---

## 🔴 PROBLÈMES CRITIQUES

### 1. ❌ Pas de balise H1
**Aucune page n'a de H1.** C'est le problème le plus grave. Le H1 est le titre principal que Google utilise pour comprendre le sujet de la page.

**Correction :** Ajouter un H1 unique sur chaque page :
- Accueil : `Photographe mariage & portrait à Beaumont de Lomagne`
- Mariage : `Photographe de mariage à Beaumont de Lomagne — Douces Émotions`
- Prestations : `Tarifs photographe — Prestations & Forfaits`

### 2. ❌ Pas de Meta Description
Aucune meta description sur l'ensemble du site. Google affiche un extrait aléatoire du contenu.

**Correction :** Ajouter une meta description engageante :
```
<meta name="description" content="Photographe professionnelle à Beaumont de Lomagne (82), 
je capture vos moments précieux : mariage, portrait, grossesse, boudoir. 
Une approche douce et artistique pour des souvenirs inoubliables.">
```

### 3. ❌ Pas de balises Open Graph
Aucun aperçu sur les réseaux sociaux (Facebook, LinkedIn, WhatsApp). Les partages affichent un lien brut.

**Correction :** Ajouter les balises OG :
```html
<meta property="og:title" content="Douces Émotions — Photographe Beaumont de Lomagne">
<meta property="og:description" content="Mariage, portrait, famille…">
<meta property="og:image" content="https://douces-emotions.fr/wp-content/uploads/2024/07/..."
<meta property="og:url" content="https://douces-emotions.fr/">
<meta property="og:type" content="website">
```

### 4. ❌ Pas de données structurées (Schema.org)
Aucun balisage JSON-LD. Pas de rich snippets possibles dans Google.

**Correction :** Ajouter :
- `LocalBusiness` + `Photographer` (obligatoire pour le SEO local)
- `BreadcrumbList` (fil d'Ariane)
- `FAQ` sur la page prestations
- `Review` pour les témoignages

---

## 🟡 PROBLÈMES MODÉRÉS

### 5. Balise Title trop longue
`Photographe Beaumont de Lomagne – Famille – mariage…` → tronquée dans Google (≈55-60 caractères visibles).

**Correction :** 
- Accueil : `Douces Émotions | Photographe Mariage & Portrait — Beaumont de Lomagne (82)`
- Garder le mot-clé principal en premier, max 60 caractères utiles.

### 6. Images sans attribut ALT
Sur 12 images de la homepage, seulement 4 ont un alt descriptif. Les autres ont `alt="Image hover effect image"` (générique) ou pas d'alt du tout.

**Correction :** Chaque image doit avoir un alt descriptif + mot-clé :
- `alt="Photographe mariage Beaumont de Lomagne — Mariés dans un champ"`
- `alt="Séance photo future maman en robe rose — Douces Émotions"`

### 7. Page Mariage : galerie sans contenu texte
La page `/mariage/` est une galerie de 50+ images sans aucun texte. Google ne peut pas comprendre le contenu (pas de H1, pas de texte).

**Correction :** Ajouter un texte d'introduction, des légendes sur les photos, et un appel à l'action vers la réservation.

### 8. Pas de blog / actualités
Aucun contenu frais indexable. Le site est statique.

**Correction :** Créer un blog avec 2 articles/mois minimum :
- "Les 10 plus beaux lieux de mariage dans le Tarn-et-Garonne"
- "Comment choisir son photographe de mariage ?"
- "Séance photo future maman : quand et comment ?"

---

## 🟢 POINTS POSITIFS

- ✅ **HTTPS** activé
- ✅ **Sitemap XML** présent (`/wp-sitemap.xml`)
- ✅ **robots.txt** fonctionnel
- ✅ **lang="fr-FR"** correct
- ✅ **URL propres** (pas de `?p=123`)
- ✅ **Navigation claire** (Galerie, Prestations, Réservation, Accès Clients)
- ✅ **Liens réseaux sociaux** (Facebook + Instagram)
- ✅ **Page Réservation** présente
- ✅ **Mentions légales** présentes
- ✅ **Témoignages clients** sur la homepage (bon pour la confiance)
- ✅ **Ancrage local** : Beaumont de Lomagne (82) dans le title

---

## 📍 SEO Local — Plan d'action

| Action | Priorité |
|---|---|
| Créer une fiche Google Business Profile | 🔴 Immédiat |
| Ajouter schema `LocalBusiness` | 🔴 Immédiat |
| Obtenir des avis Google | 🟡 Court terme |
| S'inscrire sur PagesJaunes, Mappy | 🟡 Court terme |
| Créer une page "Photographe Beaumont de Lomagne" | 🟡 Court terme |
| Ajouter l'adresse exacte dans le footer | 🟢 Moyen terme |
| S'inscrire sur Mariages.net | 🟢 Moyen terme |

---

## ⚡ Performance (WordPress + Elementor)

**Problèmes probables (sans audit PageSpeed) :**
- Elementor génère un DOM lourd et du CSS/JS inline
- Images probablement non optimisées (pas de WebP, pas de lazy loading natif)
- Pas de cache visible dans les headers

**Corrections recommandées :**
- Installer un plugin de cache (WP Rocket ou LiteSpeed Cache)
- Convertir les images en WebP
- Activer le lazy loading natif WordPress
- Minifier CSS/JS

---

## 📋 Plan d'action prioritaire

| # | Action | Impact | Difficulté |
|---|---|---|---|
| 1 | Ajouter les balises H1 sur toutes les pages | 🔴 Critique | Facile |
| 2 | Ajouter les meta descriptions | 🔴 Critique | Facile |
| 3 | Ajouter les balises Open Graph | 🔴 Critique | Facile |
| 4 | Ajouter les données structurées Schema.org | 🔴 Critique | Moyen |
| 5 | Optimiser les balises Title | 🟡 Important | Facile |
| 6 | Renommer les attributs ALT des images | 🟡 Important | Moyen |
| 7 | Ajouter du contenu texte sur les pages galerie | 🟡 Important | Moyen |
| 8 | Créer un blog (2 articles/mois) | 🟢 Secondaire | Moyen |
| 9 | Installer plugin cache + optimiser images | 🟡 Important | Facile |
| 10 | Créer Google Business Profile | 🔴 Critique | Facile |

---

## ⚙️ Détails techniques

| Élément | Valeur |
|---|---|
| Serveur | Apache |
| PHP | 8.1.34 |
| CMS | WordPress |
| Builder | Elementor |
| Sitemap | `/wp-sitemap.xml` |
| Robots | `Disallow: /wp-admin/` |
| Nombre de pages indexables | ~15-20 |
| Langue | fr-FR |
| SSL | Oui |
| Réseaux sociaux | Facebook + Instagram |
| Page de réservation | Oui |

---

> **Résumé :** Le site a une bonne base (navigation claire, HTTPS, témoignages) mais souffre de graves lacunes techniques SEO : pas de H1, pas de meta description, pas d'Open Graph, pas de Schema.org. Ces corrections sont **simples à mettre en place** et auront un impact immédiat sur le référencement. L'absence de fiche Google Business Profile est également critique pour une photographe locale.