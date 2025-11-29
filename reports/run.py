#!/usr/bin/env python3
"""
kasparro-agentic-fb-analyst - run.py
Usage:
    python run.py "Analyze ROAS drop" --data ./data/synthetic_fb_ads_undergarments.csv
"""
import argparse
import json
from src.orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser(description="Kasparro Agentic FB Analyst CLI")
    parser.add_argument("command", type=str, help="High-level instruction (e.g., 'Analyze ROAS drop')")
    parser.add_argument("--data", type=str, default="data/synthetic_fb_ads_undergarments.csv")
    parser.add_argument("--out", type=str, default="reports/")
    args = parser.parse_args()
    orch = Orchestrator(data_path=args.data, out_dir=args.out)
    orch.run(args.command)

if __name__ == "__main__":
    main()
