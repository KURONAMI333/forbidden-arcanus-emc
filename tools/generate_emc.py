"""Generate data/forbidden_arcanus/pe_custom_conversions/forbidden_arcanus_emc.json.

Forbidden Arcanus: most content is craftable via vanilla recipe types, so we seed
the worldgen/mob-drop primitives and let ProjectE auto-derive the rest. The few
fully-custom outputs (clibano obsidiansteel, hephaestus ritual results) are deferred
to a later pass. All item IDs below were verified present in the 2.6.1 jar's lang.

ProjectE NSS schema (1.21.1): values.before = list of {type,emc_value,id}. See PROJECTE_EMC_NOTES.md.
"""

import json
import os

OUT = os.path.join(
    os.path.dirname(__file__),
    "..",
    "src",
    "main",
    "resources",
    "data",
    "forbidden_arcanus",
    "pe_custom_conversions",
    "forbidden_arcanus_emc.json",
)

# Hand-set EMC for primitives (P2; ProjectE anchors: stone 1, log 32, leaves 1,
# iron 256, gold 2048, diamond 8192, ender_pearl 1024). deorum_ingot is craftable
# -> left to auto-derivation.
BEFORE = {
    # worldgen ores / stone (drops)
    "arcane_crystal": 256,  # arcane crystal ore drop (stone-tier)
    "rune": 256,  # runic stone ore drop
    "darkstone": 4,  # stone variant blob
    # stella_arcanum（鉱石ブロック本体）は c:ores に属し、ProjectE の OreBlacklistMapper が
    # 実行時に 0 を強制する。落とし物側 stellarite_piece（1ブロック=1個）へ同じ値を置く。
    # piece は block との 9:1 往復しか作る経路が無く自動導出では 0 のままになるため手付けが要る。
    "stellarite_piece": 8192,  # rare deep ore drop (high tier)
    # trees / plants (gathered)
    "edelwood_log": 32,
    "aurum_log": 32,
    "aurum_leaves": 1,
    "aurum_sapling": 32,
    "fungyss": 32,
    "yellow_orchid": 16,
    "soulless_sand": 4,
    # mob drops
    "bat_wing": 32,
    "dragon_scale": 1024,  # ender dragon drop
    "tentacle": 64,
    "soul": 128,  # lost soul drops
    "corrupt_soul": 256,
    "enchanted_soul": 512,
    # ritual primitive
    "xpetrified_orb": 2048,
}


def main() -> None:
    doc = {
        "replace": False,
        "comment": (
            "Forbidden Arcanus EMC integration for ProjectE (KURONAMI). Worldgen / mob-drop "
            "primitives seeded; vanilla recipes derive the rest. Tools/armor/aureal-charge/"
            "quantum-catcher items intentionally have no EMC. Clibano & hephaestus ritual "
            "outputs deferred to a later pass."
        ),
        "values": {
            "before": [
                {
                    "type": "projecte:item",
                    "emc_value": v,
                    "id": f"forbidden_arcanus:{k}",
                }
                for k, v in BEFORE.items()
            ]
        },
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(doc, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"primitives={len(BEFORE)} -> {os.path.normpath(OUT)}")


if __name__ == "__main__":
    main()
