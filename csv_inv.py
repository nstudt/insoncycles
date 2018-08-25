"""

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#creat dataframes
def createDf(*args):
    df = (pd.read_csv(*args))
    df['UnitCost']=df['UnitCost'].apply(int)
    df['Code']=df['Code'].apply(int)
    df['Inventory_Dapa']=df['Inventory_Dapa'].apply(float)
    return(df)

if __name__ == "__main__":
    main()

def main():
    pass
