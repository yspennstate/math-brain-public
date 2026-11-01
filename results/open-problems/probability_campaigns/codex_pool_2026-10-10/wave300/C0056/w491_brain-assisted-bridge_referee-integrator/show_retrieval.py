import json
from pathlib import Path

d = json.loads(Path("retrieval_measure.json").read_text(encoding="utf-8"))
for q in d["queries"]:
    for c in q["cards"]:
        if c["title"] in {
            "Open problem: Extended states for the three-dimensional Anderson model at weak disorder",
            "Attempt on Extended states for the three-dimensional Anderson model at weak disorder",
            "Approximate Identity (Good Kernels)",
            "Lebesgue decomposition into absolutely continuous and singular parts",
        }:
            print("\nCARD", q["name"], c["id"], c["title"])
            print(c["body"])
