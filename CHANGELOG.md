# Changelog

## v0.1.1

- Moved the stellarite anchor from Stella Arcanum to the Stellarite Piece. ProjectE forces every item in the ores tag to zero, so the old value never applied and the stellarite line went unpriced. One Stella Arcanum drops one Stellarite Piece, so the value is unchanged.

## v0.1.0

Initial release.

- ProjectE EMC integration for Forbidden Arcanus (NeoForge 1.21.1).
- Hand-set EMC for worldgen / mob-drop primitives (arcane crystal, runes, darkstone, stella arcanum, edelwood/aurum/fungyss trees, dragon scale, souls, tentacle, bat wing); vanilla recipes derive the rest.
- Stella Arcanum priced high to preserve its endgame rarity.
- Tools / armor / aureal-charge items / quantum catchers intentionally left without EMC (durability or stored state).
- Data-only: adds no items, blocks or recipes. Clibano & Hephaestus ritual outputs deferred to a later pass.
