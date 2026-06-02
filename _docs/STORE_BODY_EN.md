<!-- Modrinth/CurseForge description source of truth. Paste verbatim into Modrinth;
     paste into CurseForge in MARKDOWN mode. Title/summary below are the search-indexed fields. -->

<!-- TITLE (<=64 chars): Forbidden Arcanus ProjectE EMC -->
<!-- SUMMARY (search-indexed, plain text): ProjectE EMC for Forbidden Arcanus: adds EMC to its arcane crystal, runes, darkstone, trees and mob drops so you can transmute them. -->

# Forbidden Arcanus ProjectE EMC

Play [Forbidden Arcanus](https://www.curseforge.com/minecraft/mc-mods/forbidden-arcanus) with [ProjectE](https://modrinth.com/mod/projecte) and find its content has no EMC value? This add-on fixes that.

## What it does

A small, **data-only** add-on that teaches ProjectE about Forbidden Arcanus:

- **Hand-tuned EMC** for the mod's gathered resources — Arcane Crystal, Runes, Darkstone, Stella Arcanum, the Edelwood / Aurum / Fungyss trees, and mob drops (Dragon Scale, Souls, Tentacle, Bat Wing).
- Most crafted content — Deorum, building blocks, decoration — **derives its EMC automatically** from the mod's vanilla-style recipes.
- **Endgame Stella Arcanum is priced high** to keep its rarity meaningful.
- **Stateful items have no EMC by design**: tools, armor, the Aureal-storing bottles/tanks, Obsidian Skulls and Quantum Catchers all carry durability or stored charge/entity state.

It adds **no items, blocks or recipes** — only EMC data.

## Compatibility

| | 1.21.1 |
|---|---|
| NeoForge | ✅ |

Requires **ProjectE** and **Forbidden Arcanus** (NeoForge 1.21.1).

## Install

Drop the jar into your `mods` folder alongside ProjectE and Forbidden Arcanus. EMC values apply on world load — open a Transmutation Table to see them.

## Dependencies

- **ProjectE** — required
- **Forbidden Arcanus** — required

## Scope & limitations

- NeoForge 1.21.1 only.
- EMC values are a considered first pass; balance feedback is welcome via the issue tracker.
- Clibano furnace alloys and Hephaestus Forge ritual outputs are not valued in this first version.
- Tools, armor, aureal/charge items and quantum catchers intentionally carry no EMC (see above).

## License & credits

MIT. Forbidden Arcanus is by the Forbidden Arcanus team; ProjectE by sinkillerj & contributors. This add-on is an independent integration and is not affiliated with either.
