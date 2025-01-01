import rocm_smi as rsmi
import logging

def get_amd_vram() -> float:
    total_vram = 0.0
    
    try:
        all_devices = rsmi.listDevices()
        print(all_devices)
        

        for idx in range(all_devices):
            total_vram += rsmi.getMemInfo(idx, "vram")[1] / 1024
    except Exception as e:
        logging.info(e)

    return total_vram