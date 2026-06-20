# Forbidden Arcanus ProjectE EMC — Forge 1.20.1

The Minecraft **1.20.1 Forge** build of the EMC addon (the repo root is the 1.21.1 NeoForge build).

Same EMC content as the 1.21.1 sibling, re-emitted in ProjectE 1.20.1 (PE1.0.1)'s
`values.before` **map** shape and shipped as a **lowcodefml** data jar (no compilation).
Targets Forbidden & Arcanus 1.20.1-2.2.6 (all 18 seeded items present; FA itself needs
Valhelsia Core).

## Build (no Gradle / JDK)

```bash
python tools/generate_emc.py   # regenerate src/data/.../forbidden_arcanus_emc.json
python tools/build_jar.py       # -> build/forbidden_arcanus_emc-0.1.0-forge-1.20.1.jar
```

## Verify

Same as the 042 sibling — load with ProjectE 1.20.1 + Forbidden & Arcanus (+ Valhelsia Core)
on a Forge 1.20.1 server and confirm `mo.pr.PECore` parses the file with 0 errors.
Canon: `kuronami-mods/knowledge/PROJECTE_EMC_NOTES.md` → 1.20.1 Forge 展開.

Status: v0.1.0 — built; ProjectE 1.20.1 parse verified (0 errors) on a Forge 1.20.1 server.
