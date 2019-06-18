"""
This script will create a large dataset about Pymarket
"""
import pandas as pd
import numpy as np

df_short = pd.DataFrame({
    'Tom': [122.49,34.22,123.0],
    'Joe': [13.49,12.22,577.0],
    'Charlie': [741.49,0,0],
})

df_short.to_csv("pymarket.csv")

def generate_pymarket():
    total_records = 1000
    cols = ['Tom','Joe','Charlie']
    data = np.round(np.random.uniform(0,500,size=(total_records,len(cols))),decimals=2)
    df = pd.DataFrame(columns=cols,data=data)
    pass

if __name__ == '__main__':
    generate_pymarket()
    print("PyMarket generated")
    pass
# np.round(np.random.uniform(0,500,size=(3,3)),decimals=2)