import acquire_zillow
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import math

def clean_zillow(df):
    df = df.dropna()
    df[['bedroom', 'square_ft','yearbuilt', 'fips']] = df[['bedroom', 'square_ft','yearbuilt', 'fips']].astype('int')
    
    df = df[df.bedroom <= 6]
    df = df[df.bathroom <= 6]
    df = df[df.house_value < 2000000]
    
    return df

def split_zillow(df):
    
    train_and_validate, test = train_test_split(df, test_size=0.2, random_state=123)
    train, validate = train_test_split(train_and_validate, test_size=0.5, random_state=123)
    
    return train, validate, test

def prep_zillow(df):
    
    df = clean_zillow(df)
    train, validate, test = split_zillow(df)
    
    return train, validate, test