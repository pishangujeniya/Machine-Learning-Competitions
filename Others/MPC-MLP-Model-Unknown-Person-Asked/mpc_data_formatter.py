import pandas as pd
import numpy as np
import csv

df = pd.read_csv("./mpc_data_1.csv")
print(df.describe())

df.to_csv(path_or_buf="./mpc_data_1_formatted.csv", index=False, quotechar='"',float_format='%.15f', quoting=csv.QUOTE_NONNUMERIC, encoding='utf-8')
