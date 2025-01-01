import pyopencl as cl


def get_intel_vram() -> float:
    platforms = cl.get_platforms()
    print(platforms)
    gibi = 1073741824
    total_vram = 0.0

    for platform in platforms:
        # opencl is for heterogenous computing 
        # Intel GPU will be on Intel platform 
        if "Intel" in platform.name:
            devices = platform.get_devices(device_type=cl.device_type.GPU) # includes integrated and discrete
            for device in devices:
                # global_mem_size is in bytes
                total_vram += round(device.global_mem_size / gibi, 2)
                intel_gpu = device.name # log this for later

    if total_vram != 0.0:
        return total_vram
    else:
        return NameError # some other error here

get_intel_vram()