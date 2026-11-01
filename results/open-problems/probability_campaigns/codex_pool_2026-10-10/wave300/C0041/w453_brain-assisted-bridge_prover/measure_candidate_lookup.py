"""Bounded comparison: substring metadata lookup versus an exact semantic ID."""
import json
import re
import sqlite3
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
def lookup_candidate(database, candidate_id):
    if not re.fullmatch(r"[CP][0-9]{4}",candidate_id):
        raise ValueError("candidate ID must be Cdddd or Pdddd")
    con=sqlite3.connect(f"file:{Path(database).as_posix()}?mode=ro",uri=True,timeout=5)
    con.execute("PRAGMA query_only=ON")
    try:
        return con.execute("SELECT id,title FROM nodes WHERE lower(json_extract(metadata_json,'$.bundle_entry_key'))=? LIMIT 8",("op-"+candidate_id.casefold(),)).fetchall()
    finally:
        con.close()

database="~/math-brain-build/local/population/brain.sqlite3"
start=time.perf_counter()
con=sqlite3.connect(f"file:{database}?mode=ro",uri=True,timeout=5)
con.execute("PRAGMA query_only=ON")
baseline=con.execute("SELECT id,title FROM nodes WHERE body LIKE ? OR metadata_json LIKE ? LIMIT 8",("%C0041%","%C0041%")).fetchall()
con.close()
repaired=lookup_candidate(database,"C0041")
expected=[r["id"] for group in json.loads(ROOT.joinpath("math_cards.json").read_text(encoding="utf-8"))["queries"] for r in group["rows"] if r["metadata"].get("bundle_entry_key")=="op-c0041"]
expected=set(expected)
assert expected,"no independently identified exact target in bounded saved lookup"
assert {r[0] for r in repaired}==expected
for malformed in ("C0041%","C0041'","C41","c0041","C0041 OR 1=1"):
    try:
        lookup_candidate(database,malformed)
    except ValueError:
        pass
    else:
        raise AssertionError("malformed identifier accepted")
result={"command":"python -B -X utf8 measure_candidate_lookup.py","baseline":{"returned":len(baseline),"target_hits":sum(r[0] in expected for r in baseline),"false_positives":sum(r[0] not in expected for r in baseline),"rows":baseline},"repaired":{"returned":len(repaired),"target_hits":sum(r[0] in expected for r in repaired),"false_positives":sum(r[0] not in expected for r in repaired),"rows":repaired},"malformed_ids_rejected":5,"elapsed_seconds":round(time.perf_counter()-start,6),"scope":"One exact-ID fixture on the current store; not a general recall@k benchmark or deployed improvement. Do not fall back to raw metadata substring, which matches hash bytes and bibliography references."}
ROOT.joinpath("candidate_lookup_measurement.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result))
