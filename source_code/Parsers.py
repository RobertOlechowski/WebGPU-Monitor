from source_code.gpu.GpuInfoParser import GpuInfoParser

parsersss = [
            GpuInfoParser("timestamp"),
            GpuInfoParser("index"),
            GpuInfoParser("count"),

            GpuInfoParser("name"),
            GpuInfoParser("uuid"),
            GpuInfoParser("serial"),

            GpuInfoParser("display_mode"),
            GpuInfoParser("display_active"),
            GpuInfoParser("persistence_mode"),
            GpuInfoParser("compute_mode"),
            GpuInfoParser("compute_cap"),
            # GpuInfoParser("cuda_version"),

            GpuInfoParser("pci.bus_id"),
            GpuInfoParser("pci.domain"),
            GpuInfoParser("pci.bus"),
            GpuInfoParser("pci.device"),
            GpuInfoParser("pci.device_id"),
            GpuInfoParser("pci.sub_device_id"),


            GpuInfoParser("vgpu_driver_capability.heterogenous_multivGPU"),
            GpuInfoParser("vgpu_device_capability.fractional_multiVgpu"),
            GpuInfoParser("vgpu_device_capability.heterogeneous_timeSlice_profile"),
            GpuInfoParser("vgpu_device_capability.heterogeneous_timeSlice_sizes"),

            GpuInfoParser("pcie.link.gen.max"),
            GpuInfoParser("pcie.link.gen.current"),
            GpuInfoParser("pcie.link.gen.gpucurrent"),
            GpuInfoParser("pcie.link.gen.gpumax"),
            GpuInfoParser("pcie.link.gen.hostmax"),
            GpuInfoParser("pcie.link.width.current"),
            GpuInfoParser("pcie.link.width.max"),

            GpuInfoParser("vbios_version"),
            GpuInfoParser("pstate"),
            GpuInfoParser("fan.speed"),


            GpuInfoParser("driver_version"),

            GpuInfoParser("clocks_throttle_reasons.supported"),
            GpuInfoParser("clocks_throttle_reasons.active"),
            GpuInfoParser("clocks_throttle_reasons.gpu_idle"),
            GpuInfoParser("clocks_throttle_reasons.applications_clocks_setting"),
            GpuInfoParser("clocks_throttle_reasons.sw_power_cap"),
            GpuInfoParser("clocks_throttle_reasons.hw_slowdown"),
            GpuInfoParser("clocks_throttle_reasons.hw_thermal_slowdown"),
            GpuInfoParser("clocks_throttle_reasons.hw_power_brake_slowdown"),
            GpuInfoParser("clocks_throttle_reasons.sw_thermal_slowdown"),
            GpuInfoParser("clocks_throttle_reasons.sync_boost"),
            #GpuInfoParser(""),



            GpuInfoParser("temperature.gpu"),
            GpuInfoParser("temperature.memory"),

            GpuInfoParser("memory.total"),
            GpuInfoParser("memory.reserved"),
            GpuInfoParser("memory.used"),
            GpuInfoParser("memory.free"),

            GpuInfoParser("utilization.gpu"),
            GpuInfoParser("utilization.memory"),

            GpuInfoParser("power.management"),
            GpuInfoParser("power.draw"),
            GpuInfoParser("power.limit"),
            GpuInfoParser("power.default_limit"),
            GpuInfoParser("enforced.power.limit"),
            GpuInfoParser("power.min_limit"),
            GpuInfoParser("power.max_limit"),

            GpuInfoParser("clocks.current.graphics"),
            GpuInfoParser("clocks.current.sm"),
            GpuInfoParser("clocks.current.memory"),
            GpuInfoParser("clocks.current.video"),
            GpuInfoParser("clocks.applications.graphics"),
            GpuInfoParser("clocks.applications.memory"),

            GpuInfoParser("mig.mode.current"),
            GpuInfoParser("mig.mode.pending"),
            GpuInfoParser("fabric.state"),
            GpuInfoParser("fabric.status"),
        ]