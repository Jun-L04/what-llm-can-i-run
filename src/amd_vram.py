import rocm_smi as rsmi
import logging

def get_amd_vram() -> float:
    try:
        rsmi.rsmi_init(0)
        total_device = rsmi.rsmi_num_monitor_devices()
        total_vram = 0

        for idx in range(total_device):
            total_vram += rsmi.rsmi_dev_memory_total_get(idx) / 1024
    except Exception as e:
        logging.info(e)
    finally:
        rsmi.rsmi_shut_down()

    return total_vram