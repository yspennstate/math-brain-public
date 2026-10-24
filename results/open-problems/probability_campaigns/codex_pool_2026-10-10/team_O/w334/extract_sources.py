"""Extract only the ten assigned problem records and their cited sources."""
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = Path("~/<private-repo>/06_math_research")
INTAKE = ROOT / "probability_1000_intake_claude_20260907"
IDS = {"P0193", "P0411", "C0113", "P0039", "P0245", "C0012", "C0072", "C0108", "C0155", "P0026"}
out = {"problems": [], "attempts": [], "sources": [], "cache_names": []}
for filename, key in [("problems.jsonl", "problems"), ("attempts.jsonl", "attempts")]:
    with (INTAKE / filename).open(encoding="utf-8-sig") as handle:
        for number, line in enumerate(handle, 1):
            if not any(pid.lower() in line.lower() for pid in IDS):
                continue
            value = json.loads(line)
            if value.get("problem_id") in IDS:
                value["local_path"] = str(INTAKE / filename)
                value["local_line"] = number
                out[key].append(value)
                print(key, json.dumps(value, ensure_ascii=False))
source_ids = {v.get("source_id") for v in out["problems"]}
with (INTAKE / "sources.jsonl").open(encoding="utf-8-sig") as handle:
    for number, line in enumerate(handle, 1):
        if not any(source and source in line for source in source_ids):
            continue
        value = json.loads(line)
        value["local_line"] = number
        out["sources"].append(value)
        print("source", json.dumps(value, ensure_ascii=False))
for path in (INTAKE / "raw").iterdir():
    if any(term in path.name.lower() for term in ["biskup", "heydenreich", "littlewood", "tao_vu", "poisson", "rough", "hasebe", "spanning", "forest", "benjamini", "grimmett"]):
        out["cache_names"].append(str(path))
print("cache_names", json.dumps(out["cache_names"]))
(HERE / "source_records.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
ORIGINAL = Path("~/Downloads/Probability_1000_20h_20260906")
for filename, key in [("problems.jsonl", "problems"), ("attempts.jsonl", "attempts")]:
    with (ORIGINAL / filename).open(encoding="utf-8-sig") as handle:
        for number, line in enumerate(handle, 1):
            if not any(pid.lower() in line.lower() for pid in IDS):
                continue
            value=json.loads(line)
            if value.get("problem_id") in IDS:
                value["local_path"]=str(ORIGINAL / filename)
                value["local_line"]=number
                out[key].append(value)
                if key=="problems":
                    print("original_problem",json.dumps(value,ensure_ascii=False))
source_ids={v.get("source_id") for v in out["problems"] if v.get("source_id")}
with (ORIGINAL / "sources.jsonl").open(encoding="utf-8-sig") as handle:
    for number,line in enumerate(handle,1):
        if any(source in line for source in source_ids):
            value=json.loads(line)
            value["local_line"]=number
            out["sources"].append(value)
            print("original_source",json.dumps(value,ensure_ascii=False))
(HERE / "source_records.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
cards = json.loads((HERE / "store_cards.json").read_text(encoding="utf-8"))
for card in cards:
    if card["query"] not in {"P0193", "C0012", "C0072", "C0108", "P0026"}:
        metadata = json.loads(card["metadata_json"])
        print("card", json.dumps({"query": card["query"], "logical": metadata["logical_id"], "body": card["body"]}, ensure_ascii=False))
