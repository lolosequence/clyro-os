# 08 — Tailles et REM

> **Source :** [finsweet.com/client-first/fr/tailles-et-rem](https://finsweet.com/client-first/fr/tailles-et-rem)

---

## Pourquoi REM ?

Webflow utilise `px` par défaut. **Client-First utilise `rem`.**

| Unité | Base | Exemple |
|---|---|---|
| **px** | Absolue | `16px` = toujours 16 pixels |
| **rem** | Relative à la taille de police de `<html>` | `1rem` = 16px (par défaut navigateur) |

---

## La règle de conversion

> 🧮 **1rem = 16px** (taille de police par défaut du navigateur)

```
px → rem : diviser par 16
rem → px : multiplier par 16
```

| px | rem |
|---|---|
| 8px | 0.5rem |
| 16px | 1rem |
| 24px | 1.5rem |
| 32px | 2rem |
| 40px | 2.5rem |
| 48px | 3rem |
| 64px | 4rem |
| 80px | 5rem |
| 128px | 8rem |

---

## Valeurs approuvées Client-First

Client-First recommande d'utiliser des **multiples de 0.5rem** :

```
0.5rem, 1rem, 1.5rem, 2rem, 2.5rem, 3rem, 3.5rem, 4rem,
5rem, 6rem, 7rem, 8rem, 10rem, 12rem
```

---

## Avantages du REM

| Avantage | Explication |
|---|---|
| ♿ **Accessibilité** | Respecte les préférences de zoom du navigateur |
| 📱 **Responsive** | S'adapte automatiquement à la taille de police du device |
| 🔄 **Maintenable** | Changer la taille de base `html` change tout le site |
| 🎯 **Précis** | Évite les décimales à rallonge des `em` imbriqués |

---

## REM vs EM

| | REM | EM |
|---|---|---|
| **Base** | Racine `<html>` | Parent direct |
| **Cascade** | Non (stable) | Oui (effet boule de neige) |
| **Prévisibilité** | ✅ Élevée | ❌ Faible |
| **Usage Client-First** | ✅ Partout | ❌ Éviter |

---

## Dans Webflow

1. Sélectionner `REM` dans la liste déroulante des unités
2. Ou taper `2.5rem` directement dans le champ
3. **Ne plus utiliser `px`** sauf cas exceptionnel (bordures, ombres)