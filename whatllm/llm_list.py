from datasets import load_dataset
#from vram import get_machine_spec
from huggingface_hub import list_models
import pandas as pd
import re

# TODO: filter df based on 'fp16' or 'bf16'
# TODO: check if architecture allows for quantization
# TODO: install the model via cli

# run once or something
def list_to_excel():
    # should be all of the models listed in the leaderboard
    dataset = load_dataset("open-llm-leaderboard/contents", split="train")

    # conversion into a pandas DataFrame
    df = dataset.to_pandas()

    # let's review it in excel real quick
    df.to_excel("leaderboard.xlsx")


def get_llm_list(precision: str, capacity: float) -> pd.DataFrame:
    """ Depending on user input, prolly, give us the appropriate list of llms
    """
    precision = float("".join(re.findall(r'\d+', precision))) # parse precision into float
    max_param = precision / 8.0 * capacity # unit memory usage per 1B params * total capacity = max param we can store
    llm_list = pd.DataFrame(columns=['Model Name', 'Average Score', 'Architecture'])
    param = '#Params (B)'

    df = pd.read_excel("leaderboard.xlsx")

    filtered_df = df[df[param] <= max_param]  # filter by model parameters
    sorted_df = filtered_df.sort_values(by='Average ⬆️', ascending=False).reset_index(drop=True)  # sort by average score in descending order and get natural indexing
    #sorted_df.to_excel("sorted_leaderboard.xlsx")

    for idx in range(5): # top 5 performing models
        model_name = sorted_df['fullname'][idx]
        model_average = sorted_df['Average ⬆️'][idx]
        model_architecture = sorted_df['Architecture'][idx]

        llm_list.loc[len(llm_list)] = [model_name, model_average, model_architecture]

    llm_list.index = llm_list.index + 1 # looks nicer when printed

    return llm_list

def test():
    df = pd.read_excel("leaderboard.xlsx")
    archi = set()
    for idx in range(len(df)):
        archi.add(df['Architecture'][idx])

    print(archi)








