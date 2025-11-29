# kasparro-agentic-fb-analyst-krishan-lakhotia

Agentic Facebook Ads Performance Analyst — assignment submission.

## Quick start

1. Install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Run the CLI (sample):
```bash
python run.py "Analyze ROAS drop" --data data/synthetic_fb_ads_undergarments.csv --out reports/
```

3. Outputs will be saved to `reports/` and logs to `logs/`.

This repo includes:
- `src/agents/` — implementations for planner, data_agent, insight_agent, evaluator_agent, creative_agent
- `src/orchestrator/orchestrator.py` — main Orchestrator class used by `run.py`
- `prompts/` — prompt templates for each agent
- `reports/` — generated artifacts (report.md, insights.json, creatives.json)
- `tests/` — simple unit test for evaluator

Repo generated automatically inside the execution environment. Replace sample dataset with full dataset if needed.