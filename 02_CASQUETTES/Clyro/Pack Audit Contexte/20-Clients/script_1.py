
import zipfile, os

zip_path = "output/clyro-DA-toolkit.zip"

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    # Skills + Soul + Brief CNT
    for fname in [
        "SKILL-da-brief-extractor.md",
        "SKILL-da-color-system.md",
        "SKILL-da-typography-selector.md",
        "SKILL-da-moodboard-curator.md",
        "SKILL-da-livrable-generator.md",
        "SOUL-stark-agent-da.md",
        "BRIEF-CNT-Patrimoine.md",
        "INSTALL-SKILLS.md",
    ]:
        zf.write(f"output/{fname}", fname)

    # Template dossier client
    for fname in [
        "00-README.md",
        "01-BRIEF.md",
        "02-BENCHMARK.md",
        "03-MOODBOARDS.md",
        "04-DIRECTION-RETENUE.md",
        "05-COLOR-SYSTEM.md",
        "06-TYPOGRAPHY.md",
        "08-BRAND-KIT.md",
        "09-VOICE-EDITORIAL.md",
        "10-CHANGELOG.md",
    ]:
        zf.write(f"output/template-DA/{fname}", f"template-DA/{fname}")

print(f"ZIP créé : {zip_path} ({os.path.getsize(zip_path) / 1024:.1f} Ko)")
print(f"Contenu : {len(zf.namelist())} fichiers")
