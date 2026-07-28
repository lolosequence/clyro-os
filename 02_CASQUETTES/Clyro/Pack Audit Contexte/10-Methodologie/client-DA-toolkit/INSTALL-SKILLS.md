# Skills DA — Installation dans Open Design & Hermes

> Guide d'installation et d'utilisation des skills DA Clyro

---

## Pour Hermes

Copier les fichiers dans `~/.local/share/hermes/skills/` ou le chemin skills configuré dans ta config Hermes :

```bash
# Créer le dossier des skills DA
mkdir -p ~/.local/share/hermes/skills/da-clyro

# Copier les skills
cp SKILL-da-brief-extractor.md ~/.local/share/hermes/skills/da-clyro/SKILL.md
# (faire de même pour chaque skill dans son propre sous-dossier)
```

Structure attendue par Hermes :
```
~/.local/share/hermes/skills/
├── da-brief-extractor/
│   └── SKILL.md
├── da-color-system/
│   └── SKILL.md
├── da-typography-selector/
│   └── SKILL.md
├── da-moodboard-curator/
│   └── SKILL.md
└── da-livrable-generator/
    └── SKILL.md
```

Pour le soul STARK :
```bash
cp SOUL-stark-agent-da.md ~/.local/share/hermes/SOUL.md
```

---

## Pour Open Design

Dans le dossier du repo Open Design cloné :

```bash
# Créer les dossiers skills
mkdir -p open-design/skills/da-brief-extractor
mkdir -p open-design/skills/da-color-system
mkdir -p open-design/skills/da-typography-selector
mkdir -p open-design/skills/da-moodboard-curator
mkdir -p open-design/skills/da-livrable-generator

# Copier chaque skill
cp SKILL-da-brief-extractor.md open-design/skills/da-brief-extractor/SKILL.md
cp SKILL-da-color-system.md open-design/skills/da-color-system/SKILL.md
cp SKILL-da-typography-selector.md open-design/skills/da-typography-selector/SKILL.md
cp SKILL-da-moodboard-curator.md open-design/skills/da-moodboard-curator/SKILL.md
cp SKILL-da-livrable-generator.md open-design/skills/da-livrable-generator/SKILL.md
```

Redémarrer le daemon Open Design pour que les skills apparaissent dans le picker.

---

## Ordre d'utilisation recommandé

1. `da-brief-extractor` → colle le brief brut du client
2. `da-moodboard-curator` → génère 3 directions
3. `da-color-system` → sur la direction validée
4. `da-typography-selector` → en parallèle ou après les couleurs
5. `da-livrable-generator` → consolide tout en Brand Kit client

---

## Soul STARK

Le soul STARK est l'identité de l'agent DA Clyro.
Il doit être chargé comme soul actif dans Hermes avant de lancer les skills DA :

```bash
hermes soul load SOUL-stark-agent-da.md
```

Ou copier son contenu dans `~/.local/share/hermes/SOUL.md`.

