import pandas as pd
class InsightAgent:
    def __init__(self):
        pass

    def generate_hypotheses(self, df, min_rows=4):
        results = []
        for camp in df['campaign_name'].unique():
            cdf = df[df['campaign_name']==camp].sort_values('date')
            if len(cdf) < min_rows:
                continue
            half = len(cdf)//2
            first = cdf.iloc[:half]
            last = cdf.iloc[half:]
            first_roas = first['roas'].mean()
            last_roas = last['roas'].mean()
            reasons = []
            if pd.notna(first_roas) and pd.notna(last_roas) and first_roas != 0:
                change = (last_roas - first_roas)/abs(first_roas)
                if change < -0.25:
                    reasons.append('ROAS drop >25%')
            if last['ctr'].mean() < first['ctr'].mean():
                reasons.append('CTR decreased')
            if last['impressions'].sum() < first['impressions'].sum():
                reasons.append('Impressions decreased')
            if cdf['creative_message'].nunique() <= 2:
                reasons.append('Low creative variety')
            if reasons:
                results.append({
                    'campaign': camp,
                    'reasons': reasons
                })
        return results