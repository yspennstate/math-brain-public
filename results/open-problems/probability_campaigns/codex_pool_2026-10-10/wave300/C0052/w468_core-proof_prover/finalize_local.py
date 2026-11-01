from pathlib import Path
import hashlib
import json
import subprocess

root = Path(__file__).resolve().parent
lookup = json.loads((root/"SOURCE_LOOKUP_REPORT.json").read_text(encoding="utf-8"))
ids = {"claim_db355f188daf0592950298d6e3b23e5f2b7e6eb0f3a21694083ad47fdadd0048",
       "claim_93dc043f691fa62549866c90e84e26aa836d69164fd798c69ba9c0dc431b1fc0"}
matches = [dict(m,store=s["store"]) for s in lookup["stores"] for m in s["matches"] if m.get("id") in ids]
assert len(matches)==2
(root/"SOURCE_C0052_ONLY_REPORT.json").write_text(json.dumps({"exact_C0052_cards":matches,"current_openness":"UNKNOWN",
     "scope":"Only these two exact IDs support this report; broad substring discovery had unrelated matches. Neither card certifies a current resolution."},indent=2),encoding="utf-8")
old = next(m for m in matches if m["id"].startswith("claim_db355"))
quote = "non-triviality (nonvanishing renormalised coupling) is equivalent to inf over scales L of P(two independent random-current clusters at scale L intersect) > 0."
assert quote in old["body_excerpt"]
correction = {"id":"w468-C0052-S2","target_node_id":old["id"],"target_title":old["title"],"action":"proposed annotation; preserve the historical author-only reduction",
     "source_quote":quote,
     "statement":"The cited primary source defines non-triviality as signed g(beta) not tending to zero. For lambda=-g>=0 this is a nonzero limsup criterion; a uniform-inf current-overlap bound is a stronger sufficient route whose equivalence has not been established by this packet or the cited definition. Use the original source normalization and endpoint-weighted current law explicitly, and retain the first/joint occupation gaps as unproved inputs.",
     "assumptions":["No added limit-existence, finite-size scaling or current-law comparison theorem","Primary Conjecture 6 and eqs.(7.1)-(7.2) as verified in STATEMENT.md"],
     "source":"Read-only population node above; primary arXiv:1707.00520v1, printed p94; ATTEMPT.md L3-L5",
     "proof_or_counterexample":"The source definition yields the nonzero limsup criterion. ATTEMPT.md derives an exact susceptibility-weighted current average and only a sufficient moment bound. The finite-tree calculations refute two graph-uniform comparison shortcuts, not any proposed model-specific Ising equivalence.",
     "independent_reviewer":"w470 pending; this annotation is not a new theorem claim",
     "remaining_gap":"A model-specific equivalence or uniform original-current estimate would require an actual proof; current openness remains UNKNOWN.",
     "status":"sketch","kind":"source-and-quantifier-annotation"}
(root/"STORE_CORRECTION_REPORT.jsonl").write_text(json.dumps(correction,ensure_ascii=False)+"\n",encoding="utf-8")
with (root/"CLAIMS.jsonl").open("a",encoding="utf-8") as stream:
    stream.write(json.dumps(correction,ensure_ascii=False)+"\n")
status = json.loads((root/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
status["bounded_store_check"] = {"receipt":"SOURCE_C0052_ONLY_REPORT.json","exact_population_card_ids":sorted(ids),
     "canonical_location":"Only accessible local audit snapshots were located; they had no C0052 match. A current canonical-store status certificate is unavailable.",
     "verified_current_resolution":False,"current_openness":"UNKNOWN"}
status["independent_review"] = {"w469":"scoped KEEP of tree L1-L2","w470":"full packet delivered; verdict pending","served_model_evidence":"unavailable"}
(root/"SOURCE_STATUS.json").write_text(json.dumps(status,indent=2),encoding="utf-8")
report = (root/"REPORT.md").read_text(encoding="utf-8")
report += "\nRead-only source check: the population's exact C0052 open card and PRIVATE REDUCTION card were found. STORE_CORRECTION_REPORT.jsonl proposes an annotation to the latter's unproved uniform-inf equivalence, preserving its historical record. This quote remains only in this worker's reports. Current canonical-store status could not be certified; current openness stays UNKNOWN.\n"
# Keep the requested one-line NEXT last after adding the source-check result.
lines = report.splitlines()
next_line = next(line for line in lines if line.startswith("NEXT:"))
report = "\n".join(line for line in lines if not line.startswith("NEXT:")).rstrip()+"\n\n"+next_line+"\n"
(root/"REPORT.md").write_text(report,encoding="utf-8")

check_root = root/"patch_check_root"
check_root.mkdir(exist_ok=True)
patch_receipts = []
for name in ["01_c0052_current_law_note.diff","02_current_law_hook.diff"]:
    process = subprocess.run(["git","apply","--check",str(root/"patches"/name)],cwd=check_root,capture_output=True,text=True,encoding="utf-8")
    patch_receipts.append({"patch":name,"exit_code":process.returncode,"stdout":process.stdout,"stderr":process.stderr})
    assert process.returncode==0,patch_receipts[-1]
(root/"patch_validation.json").write_text(json.dumps({"command":"python -X utf8 finalize_local.py (git apply --check in private patch_check_root)",
      "status":"PASS","checks":patch_receipts,"scope":"Syntax and addition-path check only; no live patch application."},indent=2),encoding="utf-8")
manifest = json.loads((root/"REVIEW_CHECKSUMS.json").read_text(encoding="utf-8"))
names = set(manifest["files"]) | {"SOURCE_STATUS.json","STORE_CORRECTION_REPORT.jsonl","SOURCE_C0052_ONLY_REPORT.json","patch_validation.json"}
manifest["files"] = {name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in sorted(names)}
(root/"REVIEW_CHECKSUMS.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
print(json.dumps({"status":"PASS","patch_checks":len(patch_receipts),"claims":sum(1 for line in (root/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()),
      "packet_sha256":manifest["files"]["REVIEW_PACKET.md"],"attempt_sha256":manifest["files"]["ATTEMPT.md"],
      "correction_target":old["id"],"current_openness":"UNKNOWN"},indent=2))
