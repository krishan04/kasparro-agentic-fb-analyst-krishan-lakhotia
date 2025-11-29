.PHONY: install run test

install:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

run:
	python run.py "Analyze ROAS drop" --data data/synthetic_fb_ads_undergarments.csv --out reports/

test:
	pytest -q