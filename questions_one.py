"""
    Posible questions
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'date':[],
    'phone_source':[],
    'phone_destination':[],
    'duration':[],
})

names = pd.read_csv('raw_names.csv')
pass