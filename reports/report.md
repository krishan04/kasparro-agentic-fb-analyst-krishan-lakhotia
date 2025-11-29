# Kasparro Agentic FB Analyst — Run Report
Generated: 2025-11-29T08:22:02.101949Z

## Executive Summary
- Dataset: synthetic_fb_ads_undergarments.csv
- Total campaigns analyzed: 367
- Low-CTR campaigns (threshold avg_ctr < 0.0105): 117
- Key themes: creative variety, CTR decline, ROAS drops detected in several campaigns.

## Notable Findings
- Campaign **Men ComfortMax Launch**: ROAS change -9.55%, reasons: Impressions decreased (possible budget/audience shrink)., Purchases decreased in later period., confidence 0.3
- Campaign **Men  ComfortMax  Launch**: ROAS change 27.52%, reasons: Impressions decreased (possible budget/audience shrink)., Purchases decreased in later period., confidence 0.3
- Campaign **Men Comfortmax Launch**: ROAS change -1.12%, reasons: Impressions decreased (possible budget/audience shrink)., Purchases decreased in later period., confidence 0.3
- Campaign **men comfortmax launch**: ROAS change 38.26%, reasons: Purchases decreased in later period., confidence 0.15
- Campaign **WOMEN Seamless Everyday**: ROAS change -24.76%, reasons: Impressions decreased (possible budget/audience shrink)., Purchases decreased in later period., confidence 0.3
- Campaign **Women Seamless Everyday**: ROAS change 11.25%, reasons: Impressions decreased (possible budget/audience shrink)., Purchases decreased in later period., confidence 0.3
- Campaign **WOMEN  Seamless  Everyday**: ROAS change 41.32%, reasons: Impressions decreased (possible budget/audience shrink)., Purchases decreased in later period., confidence 0.3
- Campaign **women seamless everyday**: ROAS change -22.95%, reasons: Impressions decreased (possible budget/audience shrink)., Purchases decreased in later period., confidence 0.3
- Campaign **MEN | ATHLEISURE COOLING**: ROAS change -33.85%, reasons: Significant ROAS drop (>25%) between halves., confidence 0.3
- Campaign **Men | Athleisure Cooling**: ROAS change -13.29%, reasons: Impressions decreased (possible budget/audience shrink)., Purchases decreased in later period., confidence 0.3


## Recommendations
1. Rotate creatives for low-variety campaigns — add at least 3 distinct messages and test.
2. Use urgency and social-proof variants for low-CTR groups; test CTAs like 'Shop Comfortable Fit' or 'Claim 20% Off'.
3. Validate targeting: check audience overlap and frequency; if impressions dropped, audit budget/audience settings.
4. Run A/B tests on top 3 creative variants for each low-CTR campaign for 7-14 days.

## Artifacts
- insights.json: hypotheses with evidence and confidence.
- creatives.json: creative recommendations (3 per low-CTR campaign).
