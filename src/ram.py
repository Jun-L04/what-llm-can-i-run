import psutil



def get_total_ram() -> float:
    gibi = 1073741824


    memory = psutil.virtual_memory().total

    memory_gib = round(memory / gibi, 2)

    return memory_gib
