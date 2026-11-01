"""Atomic source-status addendum and artifact validation; no numerical experiment."""
import ast
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w420")
PEER = Path("~/brain_workers/w422")
MESH = "~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py"


def save(name, value):
    (ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")


def main():
    peer = json.loads((PEER/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
    reports = peer.get("new_primary_evidence",[])
    quasi = next(row for row in reports if "quasi-transitive-graphs" in row.get("url",""))
    status = json.loads((ROOT/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
    status["reported_resolution_status"] = "REPORTED_SOLVED_IN_SEPTEMBER_24_PRIMARY_PREPRINTS__INDEPENDENT_PROOF_AUDIT_PENDING"
    status["new_primary_reports"] = [{"source":row["source"],"url":row["url"],"scope":row["scope"],
        "evidence_origin":"w422/SOURCE_STATUS.json primary-text extraction; no proof audit inferred"} for row in reports]
    status["current_openness"] = "UNKNOWN"
    status["unknown_reason"] = "A new primary manuscript reports the full target solved. Its mathematical validity and actual solution trusted axioms have not been independently verified by w420; no original solved credit is allowed."
    status["new_primary_direct_check"] = {"web_raw_pdf":"Fetch failed: application/octet-stream unsupported; source report remains explicitly attributed to w422"}
    pdf_candidates = [PEER/"sources"/"openai_quasi_transitive_20260924.pdf",PEER/"openai_quasi_transitive_20260924.pdf"]
    pdf = next((path for path in pdf_candidates if path.exists()),None)
    if pdf is not None:
        try:
            from pypdf import PdfReader
            reader = PdfReader(str(pdf))
            txt = "\n\n".join(reader.pages[i].extract_text() or "" for i in range(min(2,len(reader.pages))))
            (ROOT/"PRIMARY_PREPRINT_FIRST_PAGES_REPORT.txt").write_text(txt,encoding="utf-8")
            status["new_primary_direct_check"].update({"local_public_pdf":str(pdf),"pages_extracted":[1,2],
                "page_count":len(reader.pages),"extracted_report":"PRIMARY_PREPRINT_FIRST_PAGES_REPORT.txt",
                "scope_inspection_only":True,"mathematical_proof_verified":False})
        except Exception as exc:
            status["new_primary_direct_check"]["local_extraction_error"] = f"{type(exc).__name__}: {exc}"

    oldrows = [json.loads(line) for line in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    snapshots = json.loads((ROOT/"SOURCE_SNAPSHOT_REPORT.json").read_text(encoding="utf-8"))
    for row in oldrows:
        if row["id"]=="C0023-w420-S1":
            row["source"]["quotes"] = ["CriticalZ3.lean line 59: sorry","CriticalPercolation.lean line 58: sorry"]
            row["source"]["snapshot_report"] = "SOURCE_SNAPSHOT_REPORT.json (current source hashes and line numbers; earlier web extraction had different line offsets)"
    newclaim = {"id":"C0023-w420-S2","status":"sketch",
        "statement":"A September 24, 2026 primary preprint reports critical Bernoulli bond nonpercolation for every infinite connected locally finite quasi-transitive undirected graph G with p_c(G)<1, which covers all assigned lattice dimensions. This is a reported resolution with mathematical proof audit pending, not a verified theorem of this worker.",
        "assumptions":["Source-status claim only; the manuscript's mathematical proof has not been audited here","Nearest-neighbor Z^d, d>=2, is in the reported scope","No original solved credit or formal-proof receipt"],
        "source":{"url":quasi["url"],"date":"2026-09-24","locator":"Theorem 1.1","primary_extraction_report":"~/brain_workers/w422/SOURCE_STATUS.json"},
        "proof":"Not a mathematical proof. The named referee records the exact primary statement and its scope; source existence and scope must remain separate from independent proof verification.",
        "independent_reviewer":"w422 source inspector; no full theorem proof audit by w420 or w422 claimed",
        "remaining_gap":"Independent audit of the reported primary proof; our own route still stops at G.","novelty_claim":False}
    if not any(row["id"]==newclaim["id"] for row in oldrows):
        oldrows.append(newclaim)
    (ROOT/"CLAIMS.jsonl").write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in oldrows),encoding="utf-8")

    note = ("New primary evidence reports a solution of the entire assigned target. OpenAI's September 24, 2026 manuscript, No percolation at criticality on quasi-transitive graphs, reports zero probability of an infinite open cluster at p_c(G) for every infinite connected locally finite quasi-transitive undirected graph with p_c(G)<1. This covers nearest-neighbor bond percolation on Z^d for all d>=2.\n\n"
        "Evidence: "+quasi["url"]+" (Theorem 1.1), recorded by w422 in SOURCE_STATUS.json. The cubic-lattice companion manuscript separately reports bond and site critical nonpercolation for d=3. The raw-PDF web reader failed on its content type; any available local first-page extraction is recorded separately.\n\n"
        "Reported solved status is distinct from independently verified mathematical validity. No primary proof or actual formal solution has been independently audited by this worker. Our six supporting draft lemmas and missing estimate G remain a proof-route/audit packet, with no original C0023 solved credit. The comparator sorry finding covers only those statement files and does not refute an unseen solution or the manuscript.\n\n"
        "NEXT: Referee the supporting lemmas and compare the dependence-matched estimate G with the reported primary proof; do not seek novelty credit from the historical ranking.\n")
    (ROOT/"PRIMARY_STATUS_ADDENDUM.md").write_text(note,encoding="utf-8")

    entry = {"key":"reported-resolution","namespace":"probability.percolation",
        "logical_name":"draft-reported-critical-percolation-resolution-20260924","kind":"concept",
        "title":"Draft source status: reported critical-percolation resolution, audit pending",
        "statement":"DRAFT source-status record, not a verified theorem. A September 24, 2026 OpenAI primary manuscript, No percolation at criticality on quasi-transitive graphs, reports that independent Bernoulli bond percolation on every infinite connected locally finite quasi-transitive undirected graph G with p_c(G)<1 has probability zero of any infinite open cluster at p_c(G). Its reported scope includes nearest-neighbor bond percolation on Z^d for every d>=2 and hence C0023's assigned dimensions 3 through 10. The manuscript's proof and actual formal solution have not been independently audited in this record. The separate public comparator statement files contain sorry and cannot by themselves certify a proof. No original C0023 solved credit is claimed.",
        "proof_text":None,"assumptions":["Source scope recorded from w422's primary-text extraction","Independent mathematical and trusted-axiom audits pending","Historical September 7 ranking cannot establish current openness"],
        "domain":"probability theory","source":{"source_id":"owner-source-audit:w420:c0023-reported-resolution-20261010",
            "url":quasi["url"],"revision":"scoped-source-report-20261010; proof audit pending",
            "license":"owner-own-work (attributed, not reproduced)","excerpt":None}}
    payload = {"spec":"mathbrain-draft-v1","author_agent":"w420","bundle_slug":"c0023-reported-resolution-status-20261010",
        "review_status":"pending; concept only; no theorem promotion","entries":[entry],"relations":[]}
    asserted = subprocess.run([sys.executable,"-X","utf8",MESH,"assert","--agent","w420","--resource",str(INBOX)],
        capture_output=True,text=True,encoding="utf-8",timeout=60)
    save("INBOX_ADDENDUM_LEASE_REPORT.json",{"returncode":asserted.returncode,"stdout":asserted.stdout,"stderr":asserted.stderr})
    if asserted.returncode:
        raise RuntimeError("Source-addendum inbox lease not asserted")
    data = json.dumps(payload,ensure_ascii=False,indent=2)+"\n"
    path = INBOX/"bundle_002.json"
    if path.exists() and path.read_text(encoding="utf-8")!=data:
        raise RuntimeError("Existing different addendum preserved")
    if not path.exists():
        part = INBOX/"bundle_002.part"
        part.write_text(data,encoding="utf-8")
        part.rename(path)
    (ROOT/"BUNDLE_SOURCE_ADDENDUM_REVIEW_COPY.json").write_text(data,encoding="utf-8")
    status["brain_pipeline"]["submitted"]["addendum_path"] = str(path)
    save("SOURCE_STATUS.json",status)

    with (ROOT/"ATTEMPT.md").open("a",encoding="utf-8") as handle:
        handle.write("\n## New primary-source status addendum\n\nA September 24 primary preprint reports the full target solved on quasi-transitive graphs. See PRIMARY_STATUS_ADDENDUM.md for exact reported scope and audit limits. This packet claims no original solved credit and does not independently verify that proof. The supporting lemmas and the remaining input G describe our own route, not the status of unseen proofs.\n")
    with (ROOT/"REVIEW_PACKET.md").open("a",encoding="utf-8") as handle:
        handle.write("\nRead PRIMARY_STATUS_ADDENDUM.md before assessing novelty or retirement. MEASUREMENTS.json records NOT RUN: the fresh local gate measured 93.9 percent commit use, 6.4 GB commit headroom and 2.9 GB physical headroom. The finite-check script is supplied for a later healthy gate; no numerical run is claimed.\n")

    allowed = {"conjecture","numerical evidence","sketch","proved special case","independently checked proof"}
    assert all(row["status"] in allowed for row in oldrows)
    assert len({row["id"] for row in oldrows})==len(oldrows)
    allbundles = [json.loads((ROOT/"BUNDLE_REVIEW_COPY.json").read_text(encoding="utf-8")),payload]
    for draft in allbundles:
        assert draft["spec"]=="mathbrain-draft-v1"
        keys = {e["key"] for e in draft["entries"]}
        assert all(e["kind"]=="concept" and e["proof_text"] is None and e["source"]["license"].startswith("owner-own-work") for e in draft["entries"])
        assert all(r["from_key"] in keys and r["to_key"] in keys for r in draft["relations"])
    for name in ("proof_checks.py","prepare_packet.py","finalize_metadata.py"):
        ast.parse((ROOT/name).read_text(encoding="utf-8"),filename=name)
    hashes_ok = all(hashlib.sha256(Path(row["snapshot"]).read_bytes()).hexdigest()==row["sha256"] for row in snapshots if "snapshot" in row)
    assert hashes_ok
    validation = {"scope":"Static artifact/schema/source validation only; no finite mathematical experiment or formal proof",
        "passed":True,"claim_rows":len(oldrows),"supporting_lemmas":6,"single_mathematical_route_gap":"G",
        "draft_bundles":2,"draft_concept_entries":sum(len(b["entries"]) for b in allbundles),
        "internal_relations":sum(len(b["relations"]) for b in allbundles),"source_snapshots_hash_verified":len(snapshots),
        "admitted_comparator_bodies":sum(bool(row.get("admitted_placeholder_lines")) for row in snapshots),
        "unreviewed_theorem_entries":0,"formal_proof_receipts":0,"numerical_checks_run":False}
    save("ARTIFACT_VALIDATION_REPORT.json",validation)
    report = ("Saved a C0023 dependence-aware proof-route draft: six supporting handwritten lemmas and the single unproved critical estimate G. A newly located September 24 primary preprint reports the full target solved on quasi-transitive graphs; its proof has not been independently audited here. No original solved credit is claimed.\n\n"
        f"Measurements from runs: 3 public source snapshots match their saved SHA-256 hashes; both inspected comparator headline bodies contain sorry. Static validation passes for {len(oldrows)} claim rows, 7 concept entries in 2 DRAFT bundles, 4 internal relations, and zero unreviewed theorem entries. Commands: python -X utf8 -B prepare_packet.py; python -X utf8 -B finalize_metadata.py. Ordinary file fingerprints are in REVIEW_FILE_HASHES.json; they are not proof receipts or canonical store digests.\n\n"
        "Numerical checks were NOT RUN. The fresh local gate held them at 93.9 percent commit use, 6.4 GB commit headroom and 2.9 GB physical headroom. The exact-check script is supplied for a later healthy gate. This is a mathematical draft proposal for the brain; no measured recall improvement or solved-problem-rate improvement is claimed.\n\n"
        "Submitted: ~/math-brain-inbox/w420/bundle_001.json and bundle_002.json. Every entry remains concept/draft material. Review, ingestion and retrievability have no verified receipts. The live store and global controls were not changed.\n\n"
        "Main mathematical review risks are L2's general exterior-boundary tracing, L3's compatible anchors/support separation, and L4's iterated-limit quantifiers. G is unproved. The primary preprint's reported proof needs its own independent audit; comparator admission does not refute that manuscript. Author/referee served-model evidence is unverified/pending.\n\n"
        "Apply: the validating coordinator reviews both BUNDLE_*_REVIEW_COPY.json files and submits them to the existing integrator only after the relevant review gates. The reviewer may apply patches/01_critical_proof_status_hook.diff from ~ or copy the staged HOOK_PROPOSAL.jsonl to its named proposal path. No live hook was edited. PROGRESS_EVENT.txt stages the progress command required outside this worker's allowed write scope.\n\n"
        "NEXT: w422 referee L0--L5 and compare the dependence-matched estimate G with the reported primary proof; retain no-novelty status and do not substitute the iterated limit for G.\n")
    (ROOT/"REPORT.md").write_text(report,encoding="utf-8")
    (ROOT/"STATUS.md").write_text("STATE: NEEDS_REVIEW\nNEXT: w422 referee L0--L5 and compare G with the reported primary proof; coordinator review the two concept DRAFTs, with no original solved credit.\n\n"
        "2026-10-10: Saved six supporting draft lemmas and one unproved critical estimate G. Exact historical target recovered; two public comparator headline bodies contain sorry.\n"
        "2026-10-10: New September 24 primary preprints report the full target solved; proof validity unverified here. Source addendum saved without overwriting the first submission.\n"
        f"2026-10-10: Static artifact validation passes: {len(oldrows)} claims, 7 concept entries, 4 relations, 3 matching source hashes, 2 admitted comparator bodies. Numerical tests held by fresh critical memory gate; no test pass claimed.\n"
        "2026-10-10: Statement delivered to w421 (msg-bbb85bdc32); proof packet delivered to w422 (msg-5eae20f1d4). Two DRAFTs submitted; review/ingestion/retrievability have no verified receipts. Served-model evidence unverified.\n",encoding="utf-8")
    names = ("ATTEMPT.md","CLAIMS.jsonl","SOURCE_STATUS.json","REVIEW_PACKET.md","PRIMARY_STATUS_ADDENDUM.md","REPORT.md","MEASUREMENTS.json","ARTIFACT_VALIDATION_REPORT.json","STATUS.md")
    fingerprints = {name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in names}
    save("REVIEW_FILE_HASHES.json",fingerprints)

    body = ("C0023 review-ready drafts; full target not proved by w420, Sept24 preprint reports solved/audit pending. "
        "Packet ~/brain_workers/w420/REVIEW_PACKET.md; ATTEMPT sha256 "+fingerprints["ATTEMPT.md"]+"; "
        "hashes REVIEW_FILE_HASHES.json; inbox w420/bundle_001.json + bundle_002.json (7 concepts, 4 relations). "
        "KEEP none received; author/referee served identity UNVERIFIED/pending. G unproved; finite tests held by critical memory gate.")
    result = subprocess.run([sys.executable,"-X","utf8",MESH,"send","--agent","w420","--to","codex-01a12190",
        "--topic","probability300-integration","--kind","message","--body",body],capture_output=True,text=True,encoding="utf-8",timeout=60)
    save("INTEGRATION_HANDOFF_REPORT.json",{"returncode":result.returncode,"stdout":result.stdout,"stderr":result.stderr,"body":body})
    print(json.dumps({"state":"NEEDS_REVIEW","validation":validation,"integration_handoff_returncode":result.returncode,
        "reported_primary_resolution":True,"mathematical_proof_audited":False},ensure_ascii=False))


if __name__=="__main__":
    main()
