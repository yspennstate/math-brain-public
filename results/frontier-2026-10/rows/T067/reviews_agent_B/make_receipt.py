"""Receipt for the agent B second audit of T067 degrees 74..90 and ALL-REGULAR."""
import json, hashlib, datetime, pathlib
P = pathlib.Path(r"(local file)")
here = pathlib.Path(__file__).parent
sha = lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
claims = ["BAND74-001", "BAND74-UPPER-001", "BAND77-001", "BAND77-UPPER-001", "BAND80-001", "BAND80-UPPER-001",
          "BAND84-001", "BAND84-UPPER-001", "BAND89-001", "BAND89-UPPER-001", "EXPLICIT-CUTOFF80-001", "Q3-ALL-REGULAR-001"]
cmp = json.load(open(here / "compare.json"))
ok = all(v["every_depth_signal_and_node_mass_equal"] and v["final_masses_equal"] is True for v in cmp.values())
arith = json.load(open(here / "check_arith.json"))
r = {"reviewer": "agent B", "requested_by": "agent J-r1017",
     "at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
     "verdict": "PASS" if ok else "SEE REVIEW",
     "scope": "correctness of the exact versions; envelope arithmetic replayed exactly by an independent engine; novelty not judged; "
              "ALL-REGULAR PASS is for the composition only (it is as strong as its inputs, d=5..73 rows not re-audited here)",
     "claims": {f"T067-{c}": {"version": "v1", "sha256": sha(P / f"T067-{c}_v1.md")} for c in claims},
     "replays": cmp, "arithmetic_all_true": all(all(v.values()) if isinstance(v, dict) and all(isinstance(x, bool) for x in v.values()) else True
                                               for v in arith.values()) and arith["bands 7..79 disjoint and complete"],
     "files": {f.name: sha(f) for f in sorted(here.iterdir()) if f.suffix in (".py", ".md") and f.name != "RECEIPT_T067_D74_D90.json"}}
json.dump(r, open(here / "RECEIPT_T067_D74_D90.json", "w", encoding="utf-8"), indent=1)
print(r["verdict"], r["arithmetic_all_true"], len(r["claims"]))
