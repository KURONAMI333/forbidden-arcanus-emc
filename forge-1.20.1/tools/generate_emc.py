"""Generate data/forbidden_arcanus/pe_custom_conversions/forbidden_arcanus_emc.json
for ProjectE on Minecraft 1.20.1 (PE1.0.1).

Same EMC content as the 1.21.1 sibling, emitted in ProjectE 1.20.1's map shape
(`values.before` = {id: emc}), grounded on PE1.0.1's bundled defaults.json.
All ids below were confirmed present in forbidden_arcanus-1.20.1-2.2.6 (lang en_us.json).

Usage: python tools/generate_emc.py
"""

import json
import os

OUT = os.path.join(
    os.path.dirname(__file__),
    "..",
    "src",
    "data",
    "forbidden_arcanus",
    "pe_custom_conversions",
    "forbidden_arcanus_emc.json",
)

# Hand-set EMC for primitives (P2; ProjectE anchors: stone 1, log 32, leaves 1,
# iron 256, gold 2048, diamond 8192, ender_pearl 1024). deorum_ingot / stellarite_piece
# are craftable -> left to auto-derivation.
BEFORE = {
    "arcane_crystal": 256,
    "rune": 256,
    "darkstone": 4,
    "stella_arcanum": 8192,
    "edelwood_log": 32,
    "aurum_log": 32,
    "aurum_leaves": 1,
    "aurum_sapling": 32,
    "fungyss": 32,
    "yellow_orchid": 16,
    "soulless_sand": 4,
    "bat_wing": 32,
    "dragon_scale": 1024,
    "tentacle": 64,
    "soul": 128,
    "corrupt_soul": 256,
    "enchanted_soul": 512,
    "xpetrified_orb": 2048,
}


def main() -> None:
    doc = {
        "comment": (
            "Forbidden Arcanus EMC integration for ProjectE (KURONAMI). "
            "Worldgen / mob-drop primitives seeded; vanilla recipes derive the rest. "
            "Tools/armor/aureal-charge/quantum-catcher items intentionally have no EMC."
        ),
        "values": {
            "before": {f"forbidden_arcanus:{k}": v for k, v in BEFORE.items()},
        },
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    print(f"primitives={len(BEFORE)} -> {os.path.normpath(OUT)}")


if __name__ == "__main__":
    main()
