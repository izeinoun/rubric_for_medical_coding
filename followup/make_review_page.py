import json, csv, sys, os
sys.path.insert(0, "followup")
import make_review_sheet as M
rows = list(csv.DictReader(open("followup/review/label_review.csv")))
charts = {c["chart_id"]: c for c in map(json.loads, open("followup/data/charts.jsonl"))}
items = []
for r in rows:
    c = charts[r["chart_id"]]
    why, checks = M.why_for(c["scenario"])
    items.append({"id": c["chart_id"], "family": c["family"], "scenario": c["scenario"], "label": c["label"],
                  "why": why, "checks": checks, "text": c["text"], "noise": "format_stress" in c["flags"]})
data = json.dumps(items).replace("</", "<\\/")
html = open("followup/review/label_review_template.html").read().replace("__DATA__", data)
open("followup/review/label_review.html", "w").write(html)
print(len(items), "charts;", len(html)//1024, "KB")
