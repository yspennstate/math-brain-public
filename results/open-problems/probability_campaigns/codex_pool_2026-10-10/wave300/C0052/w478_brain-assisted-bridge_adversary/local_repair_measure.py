"""A bounded local lexical control; no live recall changes or model runs."""
import json
import re
import time
from fractions import Fraction
from pathlib import Path

root=Path(__file__).resolve().parent
started=time.perf_counter()
receipt=json.loads((root/"store_retrieval.json").read_text(encoding="utf-8"))
rows=receipt["safe_source_headers"]
def whole_token_card(title):
    return bool(re.search(r"\bising\b|\brandom currents?\b",title,re.I))
false_substrings=[x for x in rows if not whole_token_card(x["title"])]
kept=[x for x in rows if whole_token_card(x["title"])]
controls={"Ising model":True,"critical random currents":True,
          "raising a weight":False,"arising at criticality":False}
checks={s:whole_token_card(s)==want for s,want in controls.items()}
assert all(checks.values())
counter=[]
for n in (2,10,100,1000000):
    p=Fraction(1,n)
    mean=p*n*n
    second=p*n**4
    cs=mean**2/second
    assert mean==n and cs==p
    counter.append({"n":n,"mean":str(mean),"intersection_probability":str(p),
                    "second_moment_ratio":str(second/mean**2)})
result={"scope":"fixed local saved header sample, not a general recall benchmark",
 "candidate_headers":len(rows),"before_lexical_false_matches":len(false_substrings),
 "after_lexical_false_matches":0,"valid_whole_token_headers_retained":len(kept),
 "discarded_ids":[x["id"] for x in false_substrings],"control_passes":sum(checks.values()),
 "control_count":len(checks),"counterexample_arithmetic":counter,
 "elapsed_seconds":time.perf_counter()-started,
 "repair_status":"local demonstration only; global repair PROPOSED, not deployed",
 "no_ising_simulation":True,"no_store_writes":True}
(root/"MEASUREMENTS.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(result,ensure_ascii=False))
