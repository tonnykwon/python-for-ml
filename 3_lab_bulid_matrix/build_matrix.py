import numpy as np
import pandas as pd


def get_rating_matrix(filename, dtype=np.float32):
    data = pd.read_csv(filename)
    return data.pivot_table(["rating"],index = data["source"], columns = data["target"], fill_value = 0)
    




def get_frequent_matrix(filename, dtype=np.float32):
    data = pd.read_csv(filename)
    data["count"] = 1
    return data.pivot_table(["count"], index = data["source"], columns = data["target"], aggfunc = "sum")