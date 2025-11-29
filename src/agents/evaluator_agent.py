import numpy as np
from scipy import stats

class EvaluatorAgent:
    def __init__(self):
        pass

    def validate(self, df, hypotheses):
        validated = []
        for h in hypotheses:
            camp = h['campaign']
            cdf = df[df['campaign_name']==camp].sort_values('date')
            half = len(cdf)//2
            first = cdf.iloc[:half]
            last = cdf.iloc[half:]
            evidence = {}
            evidence['first_roas'] = float(first['roas'].mean()) if not first['roas'].isna().all() else None
            evidence['last_roas'] = float(last['roas'].mean()) if not last['roas'].isna().all() else None
            evidence['ctr_change'] = float(last['ctr'].mean() - first['ctr'].mean()) if 'ctr' in df.columns else None
            # simple t-test for clicks if enough samples
            try:
                tstat, pval = stats.ttest_ind(first['ctr'].dropna(), last['ctr'].dropna(), equal_var=False)
            except Exception:
                tstat, pval = None, None
            validated.append({'campaign': camp, 'evidence': evidence, 't_pval': pval})
        return validated