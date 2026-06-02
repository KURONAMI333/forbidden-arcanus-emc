package com.kuronami.forbiddenarcanusemc;

import com.mojang.logging.LogUtils;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.common.Mod;
import org.slf4j.Logger;

/**
 * Forbidden Arcanus ProjectE EMC — data-only integration. EMC values live in
 * {@code data/forbidden_arcanus/pe_custom_conversions/} (loaded by ProjectE via
 * datapack reload); this class only provides the {@code @Mod} entry point.
 */
@Mod(ForbiddenArcanusEMC.MODID)
public final class ForbiddenArcanusEMC {
    public static final String MODID = "forbidden_arcanus_emc";
    public static final String VERSION = "0.1.0";
    private static final Logger LOGGER = LogUtils.getLogger();

    public ForbiddenArcanusEMC(IEventBus modBus) {
        LOGGER.info("Forbidden Arcanus ProjectE EMC v{} loading — EMC via data/forbidden_arcanus/pe_custom_conversions", VERSION);
    }
}
