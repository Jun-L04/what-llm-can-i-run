from ram import get_total_ram
from nvidia_vram import get_nv_vram
from amd_vram import get_amd_vram
import logging
# remember to generate a requirements.txt for the environment

print(f"Total RAM: {get_total_ram()} GiB")


total_vram = None
for func in [get_nv_vram(), get_amd_vram()]:
    try:
        total_vram = func
    except Exception as e:
        logging.info(e)

if total_vram != None:
    print(f"Total VRAM: {get_nv_vram()} GiB")
else:
    logging.CRITICAL("No Discrete GPU Detected.")
