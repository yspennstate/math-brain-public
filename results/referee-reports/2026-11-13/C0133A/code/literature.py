"""Save a reproducible, limited OpenAlex citation search. Standard library only."""
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
ROOT = Path(__file__).resolve().parents[1]
out = ROOT / "sources"
records = {}
for work_id in ["W2962897620", "W2276429711"]:
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode({
        "filter": f"cites:{work_id},from_publication_date:2012-01-01,to_publication_date:2026-11-13",
        "per-page": 200,
    })
    try:
        with urllib.request.urlopen(url, timeout=45) as response:
            data = json.load(response)
        (out / f"openalex-citations-{work_id}.json").write_text(json.dumps(data, indent=2))
        print(work_id, "total", data["meta"]["count"], "returned", len(data["results"]))
        for work in data["results"]:
            records[work["id"]] = work
    except Exception as error:
        print(work_id, type(error).__name__, str(error))
lines = []
for work in sorted(records.values(), key=lambda x: (x["publication_year"], x["display_name"])):
    line = f'{work["publication_year"]}\t{work["display_name"]}\t{work.get("doi")}\t{work["id"]}'
    lines.append(line)
    print(line)
(out / "openalex-citations.tsv").write_text("\n".join(lines) + "\n")
