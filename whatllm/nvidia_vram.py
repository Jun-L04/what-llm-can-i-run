import GPUtil
import logging

def get_nv_vram() -> float:
    try:
        gpus = GPUtil.getGPUs()
        total_vram = 0.0
        for gpu in gpus:
            # memoryTotal is in MiB
            total_vram += gpu.memoryTotal / 1024
    except Exception as e:
        logging.info(e)

    return total_vram