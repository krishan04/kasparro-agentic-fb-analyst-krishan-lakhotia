#!/usr/bin/env python3
import argparse
from src.orchestrator.orchestrator import Orchestrator
import yaml

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", type=str, help="High-level instruction")
    parser.add_argument("--data", type=str, default="data/synthetic_fb_ads_undergarments.csv")
    parser.add_argument("--out", type=str, default="reports/")
    parser.add_argument("--config", type=str, default="config/config.yaml")
    args = parser.parse_args()
    orch = Orchestrator(config_path=args.config, data_path=args.data, out_dir=args.out)
    orch.run(args.command)

if __name__ == '__main__':
    main()