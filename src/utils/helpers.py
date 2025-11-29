import pandas as pd
import numpy as np
from pathlib import Path

def load_and_clean(path):
    df = pd.read_csv(path, parse_dates=['date'])
    for col in ['ctr','roas','spend','impressions','clicks','purchases','revenue']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def month_period(df):
    df['month'] = df['date'].dt.to_period('M').dt.to_timestamp()
    return df