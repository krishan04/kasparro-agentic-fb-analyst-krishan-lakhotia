import re
from collections import Counter

class CreativeAgent:
    def __init__(self):
        pass

    def generate(self, df, campaigns, n=3):
        out = []
        for camp in campaigns:
            examples = df[df['campaign_name']==camp]['creative_message'].dropna().astype(str)
            text = " ".join(examples.values)
            words = re.findall(r"\w{4,}", text.lower())
            common = [w for w,_ in Counter(words).most_common(6)]
            keywords = ", ".join(common[:3]) if common else "comfortable, fit"
            for i in range(n):
                if i==0:
                    headline = f"Upgrade to {common[0].capitalize() if common else 'Comfort'} — Feel the difference"
                    body = f"Experience {keywords}. Soft, supportive, and designed for all-day comfort. Try now with free returns."
                    cta = "Shop Comfortable Fit"
                elif i==1:
                    headline = "Limited time: 20% off our best-sellers"
                    body = f"Customers love the {common[0] if common else 'fit'}. Grab yours before stock runs out — comfortable, breathable, reliable."
                    cta = "Claim 20% Off"
                else:
                    headline = "Loved by thousands — Rated 4.5★"
                    body = f"Join satisfied customers enjoying {keywords}. Free shipping over ₹999. Easy returns."
                    cta = "See Why People Love It"
                out.append({
                    'campaign': camp,
                    'headline': headline,
                    'body': body,
                    'cta': cta,
                    'rationale': 'keyword-based variants'
                })
        return out