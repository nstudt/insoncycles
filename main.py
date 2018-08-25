import pandas as pd
import numpy as np
import csv_inv as ci


if __name__ == "__main__":
    df1 = ci.createDf('data/insonFactora.csv')
    df2 = ci.createDf('data/insonprods.csv')
    print(df1)
    print(df2)