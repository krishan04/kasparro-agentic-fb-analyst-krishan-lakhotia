# Agent Graph — Kasparro Agentic FB Analyst

## Overview
This multi-agent system contains five primary agents:
- Planner Agent: Receives user instruction (e.g., "Analyze ROAS drop") and decomposes into subtasks (load data, summarize, generate hypotheses, validate, produce creatives).
- Data Agent: Loads dataset, cleans, summarizes, and provides aggregated data views (by campaign, adset, date).
- Insight Agent: Produces human-readable hypotheses explaining observed patterns (e.g., ROAS drop, CTR fall), with initial confidence scores.
- Evaluator Agent: Runs quantitative checks (pre/post comparisons, correlation, significance heuristics) and assigns evidence-backed confidence adjustments.
- Creative Improvement Generator: Uses existing creative messaging to propose new headlines/body/CTAs for low-CTR campaigns with reasoning.

## Data Flow
User CLI -> Planner -> Data Agent (returns summaries) -> Planner delegates to Insight Agent -> Evaluator validates hypotheses -> Planner asks Creative Generator for low-CTR campaigns -> Outputs: insights.json, creatives.json, report.md, logs/.

## Reflection & Retry
- Each agent returns a confidence score.
- Planner triggers a retry if overall confidence < 0.6: re-run with different aggregation (weekly/monthly) or request more data slices (audience, country).
