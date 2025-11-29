Planner Agent Prompt Template

Think:
- Break the high-level task into subtasks.
Analyze:
- Request summary statistics from Data Agent.
- Request candidate hypotheses from Insight Agent.
Conclude:
- Assemble plan, confidence thresholds, and reflection actions.

Output schema:
{
  "tasks": ["load_data","summarize","generate_hypotheses","validate","generate_creatives"],
  "params": {...},
  "reflection_if_confidence_low": "re-aggregate by week/month"
}