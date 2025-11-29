import json
from src.agents.data_agent import DataAgent
from src.agents.insight_agent import InsightAgent
from src.agents.evaluator_agent import EvaluatorAgent
from src.agents.creative_agent import CreativeAgent
from src.agents.planner import PlannerAgent
import yaml
from pathlib import Path

class Orchestrator:
    def __init__(self, config_path='config/config.yaml', data_path='data/synthetic_fb_ads_undergarments.csv', out_dir='reports/'):
        self.config = yaml.safe_load(Path(config_path).read_text())
        self.data_path = data_path
        self.out_dir = Path(out_dir)
        self.out_dir.mkdir(parents=True, exist_ok=True)
        self.data_agent = DataAgent(self.data_path)
        self.insight_agent = InsightAgent()
        self.evaluator_agent = EvaluatorAgent()
        self.creative_agent = CreativeAgent()
        self.planner = PlannerAgent()

    def run(self, command):
        plan = self.planner.decompose(command)
        df = self.data_agent.load()
        summary = self.data_agent.summarize_by_campaign()
        hypotheses = self.insight_agent.generate_hypotheses(df, min_rows=self.config.get('min_rows_for_analysis',4))
        validated = self.evaluator_agent.validate(df, hypotheses)
        low_ctr_thresh = summary['avg_ctr'].mean() - self.config.get('low_ctr_std_multiplier',0.5)*summary['avg_ctr'].std()
        low_ctr_campaigns = summary[summary['avg_ctr'] < low_ctr_thresh]['campaign_name'].tolist()
        creatives = self.creative_agent.generate(df, low_ctr_campaigns, n=3)
        # Save outputs
        Path(self.out_dir / 'insights.json').write_text(json.dumps(validated, indent=2))
        Path(self.out_dir / 'creatives.json').write_text(json.dumps(creatives, indent=2))
        # basic report
        report = {
            'command': command,
            'total_campaigns': int(summary.shape[0]),
            'num_low_ctr': len(low_ctr_campaigns)
        }
        Path(self.out_dir / 'report.md').write_text("# Report\n\n" + json.dumps(report, indent=2))
        return {'summary': summary, 'hypotheses': hypotheses, 'validated': validated, 'creatives': creatives}