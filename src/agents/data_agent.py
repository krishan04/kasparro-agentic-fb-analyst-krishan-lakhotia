from src.utils.helpers import load_and_clean, month_period
import pandas as pd

class DataAgent:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None

    def load(self):
        self.df = load_and_clean(self.data_path)
        self.df = month_period(self.df)
        return self.df

    def summarize_by_campaign(self):
        df = self.df
        camp = df.groupby('campaign_name').agg(
            total_spend=('spend','sum'),
            total_impressions=('impressions','sum'),
            total_clicks=('clicks','sum'),
            avg_ctr=('ctr','mean'),
            avg_roas=('roas','mean'),
            unique_creatives=('creative_message','nunique'),
            rows=('campaign_name','count')
        ).reset_index()
        return camp