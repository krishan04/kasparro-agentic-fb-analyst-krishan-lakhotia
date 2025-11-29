from src.agents.evaluator_agent import EvaluatorAgent
import pandas as pd
from io import StringIO

def test_evaluator_runs():
    csv = \'\'
date,campaign_name,ctr,roas,impressions,clicks,purchases
2025-01-01,TestCamp,0.02,1.0,1000,20,2
2025-01-02,TestCamp,0.015,0.8,900,14,1
2025-01-03,TestCamp,0.01,0.6,800,8,1
2025-01-04,TestCamp,0.005,0.4,700,4,0
\'\'
    df = pd.read_csv(StringIO(csv), parse_dates=['date'])
    hypotheses = [{'campaign':'TestCamp','reasons':['ROAS drop >25%']}]
    ev = EvaluatorAgent()
    out = ev.validate(df, hypotheses)
    assert isinstance(out, list)
    assert out[0]['campaign'] == 'TestCamp'