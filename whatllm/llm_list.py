from datasets import load_dataset
#from vram import get_machine_spec
from huggingface_hub import list_models
import pandas as pd
from typing import Dict, List
import re


# run once or something
def list_to_excel():
    # should be all of the models listed in the leaderboard
    dataset = load_dataset("open-llm-leaderboard/contents", split="train")

    # conversion into a pandas DataFrame
    df = dataset.to_pandas()

    # let's review it in excel real quick
    df.to_excel("leaderboard.xlsx")


def get_llm_list(precision: str, capacity: float) -> Dict[str, List]:
    """ Depending on user input, prolly, give us the appropriate list of llms
    """
    precision = float("".join(re.findall(r'\d+', precision))) # parse precision into float
    max_param = precision / 8.0 * capacity # unit memory usage per 1B params * total capacity = max param we can store
    llm_list = {}
    llm_attributes = []
    df = pd.read_excel("leaderboard.xlsx")

    param = '#Params (B)'

    count = 0
    highestAvg = float('-inf')
    best_model = ''

    for idx in range(len(df[param])):
        if df[param][idx] < max_param:
            score = df['Average ⬆️'][idx]  # thank god pandas work with emojis
            if score > highestAvg:
                highestAvg = score
                best_model = df['fullname'][idx]
            #print(df['fullname'][idx])
            count += 1
    llm_attributes = [count, best_model, highestAvg]
    llm_list[best_model] = llm_attributes

    return llm_list
    print(f'Total of {count} models given our constraints.')
    print(f'Best model; {best_model}, with avg. of {highestAvg}.')








