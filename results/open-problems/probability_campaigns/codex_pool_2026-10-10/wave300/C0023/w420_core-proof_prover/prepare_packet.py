"""Finish this worker's C0023 draft artifacts; never write the live brain store."""
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import time
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w420")
MESH = "~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py"
STATE = Path("~/.claude/compute/compute_state.json")


def save(name, data):
    (ROOT/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")


def source_snapshots():
    folder = ROOT/"sources"
    folder.mkdir(exist_ok=True)
    rows = []
    for name, url in (
        ("CriticalZ3.lean", "https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/CriticalZ3.lean"),
        ("CriticalPercolation.lean", "https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/CriticalPercolation.lean"),
        ("formal-math-README.md", "https://raw.githubusercontent.com/anthropics/formal-math/main/README.md"),
    ):
        row = {"url": url, "retrieved_at": datetime.now().astimezone().isoformat()}
        try:
            with urlopen(Request(url, headers={"User-Agent": "C0023-source-status-audit"}), timeout=15) as response:
                data = response.read(100001)
                if len(data)>100000:
                    raise ValueError("unexpectedly large source; do not read further")
                row["http_status"] = response.status
            (folder/name).write_bytes(data)
            txt = data.decode("utf-8")
            row.update({"snapshot": str(folder/name), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                        "admitted_placeholder_lines": [i for i,line in enumerate(txt.splitlines(),1) if line.strip()=="sorry"]})
        except Exception as exc:
            row["error"] = f"{type(exc).__name__}: {exc}"
            row["fallback"] = "Primary web inspection already recorded in CLAIMS.jsonl S1; no local hash claim for a failed fetch"
        rows.append(row)
    save("SOURCE_SNAPSHOT_REPORT.json", rows)
    return rows


def canonical_record():
    uri = "file:~/math-brain-build/local/population/brain.sqlite3?mode=ro"
    with sqlite3.connect(uri, uri=True) as connection:
        rows = connection.execute(
            "SELECT id,kind,title,body,metadata_json FROM nodes WHERE id=? OR title LIKE ? LIMIT 4",
            ("math:probability.percolation:open-problem-c0023-no-percolation-at-criticality-on-z-d-for-3-d-10", "%No percolation at criticality%")
        ).fetchall()
    receipt = {"uri": uri, "read_only": True, "rows": [dict(zip(("id","kind","title","body","metadata_json"),row)) for row in rows]}
    save("CANONICAL_RECORD_REPORT.json", receipt)
    return receipt


def fresh_gate():
    # Read only local pressure fields, not the remote/trading telemetry.
    state = json.loads(STATE.read_text(encoding="utf-8-sig"))
    keys = ("ts","host","status","mode","reasons","cpu_pct","mem_avail_mb","commit_avail_mb",
            "commit_used_pct","disk_queue","disk_free_gb","hung_windows")
    sample = {key:state.get(key) for key in keys}
    now = datetime.now().astimezone()
    stamp = datetime.fromisoformat(str(sample["ts"]))
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=now.tzinfo)
    age = (now-stamp).total_seconds()
    def finite_number(key):
        value = sample[key]
        if not isinstance(value,(int,float)):
            raise ValueError(f"missing local numeric pressure field {key}")
        return value
    reasons = []
    if not 0 <= age <= 60:
        reasons.append(f"local governor sample age {age:.1f}s outside [0,60]")
    if str(sample["status"]).lower() in ("distress","critical","stop"):
        reasons.append(f"local status {sample['status']}")
    if sample["mode"] not in ("owner_away_open","owner_present_polite","open","throttle"):
        reasons.append(f"unrecognized or paused mode {sample['mode']}")
    if finite_number("cpu_pct") >= 95:
        reasons.append("CPU at least 95 percent")
    if finite_number("mem_avail_mb") <= 4096 or finite_number("commit_avail_mb") <= 8192 or finite_number("commit_used_pct") >= 90:
        reasons.append("critical physical or commit memory pressure")
    if finite_number("disk_free_gb") < 2 or finite_number("disk_queue") >= 100:
        reasons.append("critical disk headroom or queue")
    if sample["hung_windows"]:
        reasons.append("hung-window signal")
    receipt = {"source": str(STATE), "sample": sample, "age_seconds": age, "allowed": not reasons,
               "hold_reasons": reasons, "finished_epoch": time.time(),
               "workload": "One serial pure-Python finite proof check, 256 masks plus three boundary cases, 16 domino states, no GPU/model/sweep",
               "throttle_response": "parallelism fixed at one; no extra worker or background process; bounded tiny batch"}
    save("COMPUTE_GATE_REPORT.json", receipt)
    return receipt


def bundle():
    source = {"source_id":"owner-work:w420:c0023-anchor-certificate-20261010",
              "url":"urn:owner-work:w420:c0023-anchor-certificate:2026-10-10",
              "revision":"author-checked-draft-20261010; independent review pending",
              "license":"owner-own-work; DRAFT supporting reductions, no parent-problem solved claim", "excerpt":None}
    def entry(key, logical, title, statement, assumptions):
        return {"key":key,"namespace":"probability.percolation","logical_name":logical,
                "kind":"concept","title":title,"statement":statement,"proof_text":None,
                "assumptions":assumptions,"domain":"probability theory","source":source}
    entries = [
        entry("color", "draft-finite-dependent-bad-site-coloring-bound", "Draft: dependence-aware bad-site bound",
              "DRAFT author-checked supporting bound, independent audit pending. For a binary field on Z^2 with independence of sigma-fields on index sets at infinity-norm distance greater than integer R>=0, and each bad-site probability <=q in [0,1], the probability that m>=1 distinct specified sites are all bad is <=q^ceil(m/(R+1)^2). Both coordinate residues modulo R+1 supply a jointly independent subfamily. Pairwise independence alone is insufficient.",
              ["Strong R-dependence, not only pairwise independence", "Uniform bad-site probability bound", "No novelty claim"]),
        entry("peierls", "draft-explicit-finite-dependent-good-site-threshold", "Draft: explicit finite-dependent block threshold",
              "DRAFT author-checked supporting estimate, independent audit pending. For the strongly R-dependent binary field on Z^2 with bad probability <=q, put K=(R+1)^2 and t=8*q^(1/K). If t<1, the probability that 0 belongs to an infinite nearest-neighbor good component is at least 1-q-9*t*(1+t)/(1-t)^3. In particular q<=800^(-K) yields probability >9/10. The proof uses enclosing bad star-cycles and multiplies probabilities only for an independent color subfamily.",
              ["Strong infinity-norm R-dependence", "Bad probabilities uniformly <=q in [0,1]", "Nearest-neighbor good components and star-neighbor bad cycles", "General boundary proof awaits referee"]),
        entry("anchor", "draft-compatible-local-anchor-openness-certificate", "Draft: local anchor certificate and critical lower bound",
              "DRAFT author-checked conditional reduction, independent audit pending. For independent nearest-neighbor bond percolation on Z^d, d>=2, take plane block centers c_z=L*(z_1,z_2,0,...,0), seed boxes S_z=c_z+[-L,L]^d, and outer boxes D_z(M)=c_z+[-M,M]^d, integers M>=L>=1. Select h_z as the first vertex in S_z reaching the boundary of D_z(M) internally. G_z requires h_z and its four neighboring anchors to exist and h_z to connect to each inside D_z(M+L). Put R=floor(2*(M+L)/L). If p0>0 and P_p0(G_0^c)<800^(-(R+1)^2), finite-product continuity preserves the strict margin at some p1<p0 and compatible anchors give theta_d(p1)>0. Hence the critical failure probability for every fixed pair is at least this threshold. This does not prove critical nonpercolation.",
              ["Same deterministic finite anchor rule in all neighboring events", "Product measure on bonds", "Supporting box contains every test and connection", "Strict threshold margin for lowering p"]),
        entry("gap", "draft-critical-anchor-dependence-matched-estimate-gap", "Unproved: critical dependence-matched anchor estimate",
              "UNPROVED INPUT, no theorem or solved claim. On independent nearest-neighbor bond percolation on Z^d, take centers c_z=L*(z_1,z_2,0,...,0), seeds S_z=c_z+[-L,L]^d, and D_z(M)=c_z+[-M,M]^d, integers M>=L>=1. Let h_z be the first seed vertex reaching the boundary of D_z(M) internally, using one fixed offset order. G_z requires h_z and its four neighboring anchors to exist and h_z to connect to each inside D_z(M+L). A proof route to theta_d(p_c)=0 for a fixed d in {3,...,10} would need to derive from hypothetical theta_d(p_c)>0 a finite pair with P_pc(G_0^c)<800^(-(floor(2*(M+L)/L)+1)^2). Unique infinite-cluster stabilization supplies only lim_L lim_M P_pc(G_0^c)=0. It supplies no estimate matching the increasing dependence range. A uniform fixed-aspect-ratio high-probability connection estimate would suffice, but remains unproved in this packet. Current openness of the full target is UNKNOWN.",
              ["Hypothetical positive critical percolation probability", "Compatible local anchor construction", "Iterated limit is not a joint-scale rate"]),
        entry("quantifiers", "draft-two-scale-limit-dependence-threshold-obstruction", "Draft: counterexample to a scale-selection inference",
              "DRAFT author-checked numerical-family counterexample to a logical inference, independent audit pending. For integers M>=L>=1, let q_fake(L,M)=1 when M<L*2^L and q_fake(L,M)=2^(-L) otherwise. This is nonincreasing in M for each fixed L and lim_L lim_M q_fake=0. Nevertheless q_fake(L,M)>800^(-(floor(2*(M+L)/L)+1)^2) for every finite pair. Thus an iterated vanishing failure limit alone cannot supply a dependence-matched block certificate. No percolation realization of q_fake is asserted.",
              ["Logical counterexample only", "No percolation counterexample or novelty claim"]),
        entry("formal-status", "draft-critical-percolation-comparator-placeholder-audit", "Source audit: comparator statements do not certify a proof",
              "SOURCE-STATUS DRAFT, not a mathematical proof. The public openai/math files lean/ComparatorChallenges/CriticalZ3.lean and CriticalPercolation.lean inspected on 2026-10-10 end their headline critical_no_infinite and no_percolation_at_criticality statements with sorry. These inspected statement files do not certify admitted-free proofs. This says nothing about unseen solution artifacts. Current openness of C0023 remains UNKNOWN; retirement requires the actual theorem, its intended definitions and assumptions, and a trusted-axiom receipt from the actual solution.",
              ["Only the inspected public raw statements are covered", "No inference from documentation prose to a checked proof"]),
    ]
    relations = [
        {"from_key":"peierls","to_key":"color","kind":"depends_on","rationale":"The contour sum uses only the independently colored subfamily bound."},
        {"from_key":"anchor","to_key":"peierls","kind":"depends_on","rationale":"The anchor certificate percolates its finite-dependent coarse field through the explicit good-site threshold."},
        {"from_key":"gap","to_key":"anchor","kind":"depends_on","rationale":"The unproved critical estimate would contradict the proved conditional openness certificate."},
        {"from_key":"quantifiers","to_key":"gap","kind":"semantic_association","rationale":"The numerical family explains why the iterated limit cannot discharge the dependence-matched gap."},
    ]
    return {"spec":"mathbrain-draft-v1","author_agent":"w420","bundle_slug":"c0023-quantified-anchor-obstruction-20261010",
            "review_status":"pending; all entries remain concept/draft material", "entries":entries,"relations":relations}


def main():
    snapshots = source_snapshots()
    canonical = canonical_record()
    try:
        gate = fresh_gate()
        if gate["allowed"]:
            import proof_checks
            measurements = proof_checks.run_checks(gate)
        else:
            measurements = {"passed":None,"status":"NOT RUN: current compute gate held numerical checks", "gate_receipt":"COMPUTE_GATE_REPORT.json"}
            save("MEASUREMENTS.json", measurements)
    except Exception as exc:
        save("CHECK_FAILURE_REPORT.json", {"exception":f"{type(exc).__name__}: {exc}"})
        raise

    payload = bundle()
    assert all(e["kind"]=="concept" and e["proof_text"] is None and e["source"]["license"].startswith("owner-own-work") for e in payload["entries"])
    keys = {e["key"] for e in payload["entries"]}
    assert len(keys)==len(payload["entries"])
    assert all(r["from_key"] in keys and r["to_key"] in keys for r in payload["relations"])
    gate_cmd = [sys.executable,"-X","utf8",MESH,"assert","--agent","w420","--resource",str(INBOX)]
    asserted = subprocess.run(gate_cmd,capture_output=True,text=True,encoding="utf-8",timeout=60)
    save("INBOX_LEASE_REPORT.json", {"command":gate_cmd,"returncode":asserted.returncode,"stdout":asserted.stdout,"stderr":asserted.stderr})
    if asserted.returncode:
        raise RuntimeError("inbox write lease not asserted; keep local draft only")
    INBOX.mkdir(exist_ok=True)
    text = json.dumps(payload,ensure_ascii=False,indent=2)+"\n"
    final = INBOX/"bundle_001.json"
    if final.exists() and final.read_text(encoding="utf-8")!=text:
        raise RuntimeError("existing different bundle_001.json preserved; choose a fresh filename")
    if not final.exists():
        part = INBOX/"bundle_001.part"
        part.write_text(text,encoding="utf-8")
        os.rename(part,final)
    (ROOT/"BUNDLE_REVIEW_COPY.json").write_text(text,encoding="utf-8")

    status = json.loads((ROOT/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
    status["model"] = "Independent nearest-neighbor Bernoulli bond percolation on Z^d; exact product measure and target recovered in primary Kozma--Nitzan Section 1"
    status["historical_intake"] = {"record_path":"~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl","line":23,
        "source_id":"garban_steif_noise_2012","primary_url":"https://arxiv.org/abs/1102.5761",
        "locator":"Chapter XI Section 1, p. 136; also cited ICM 2018 Conjecture 1 p. 3 and Ising/Potts 2017 Conjecture 1 p. 37",
        "historic_current_status":"no_resolution_found_in_documented_search as of 2026-09-07; unreviewed",
        "exact_statement":"Prove theta(p_c)=0 for Bernoulli percolation on Z^d for every d>=3; the historical unresolved range was 3<=d<=10."}
    status["prior_attempts"] = {"C0023-A001":"Half-space susceptibility and hyperplane gluing inputs explicitly unproved; not reused",
        "H_I_and_lean_targeted_search":"rg -l C0023 in the named H/I attempts returned no exact candidate file; Lean annotated ranking repeats historical status, not a proof",
        "owner_retirement_check":"Named historical records and the recalled campaign proof-directory audit were checked; no independently verified retirement receipt recovered. This is not an exhaustive nonexistence claim.",
        "team_O":"The named Team O board has no C0023 owner; disjoint quantified-anchor lane claimed on mesh."}
    status["source_snapshots"] = snapshots
    status["canonical_record_matches"] = len(canonical["rows"])
    status["formal_check"] = {"performed":False,"source_statement_inspection_performed":True,"headline_bodies":"Both inspected comparator headline bodies are admitted with sorry","trusted_axioms":None,"no_formal_success_claim":True}
    status["served_model_evidence"] = {"author":"UNVERIFIED; requested model and effort are not served-model evidence","referee":"pending"}
    status["brain_pipeline"] = {"prepared":"complete","submitted":{"state":"complete","path":str(final)},"reviewed":"pending; no receipt","ingested":"unverified; no receipt","retrievable":"unverified; not queried for this new draft"}
    save("SOURCE_STATUS.json",status)

    hook = {"id":"critical-proof-status-w420-01","area":"math","event":"stage-start",
        "cue":"critical-percolation solved/retired claim based only on comparator statements or formalization prose",
        "fire_when":"A critical-nonpercolation success claim cites CriticalZ3.lean or CriticalPercolation.lean while the inspected headline ends in sorry.",
        "silent_when":"The actual solution theorem and intended assumptions have an admitted-free trusted-axiom receipt and a scoped independent mathematical review.",
        "text":"Before retiring a percolation problem from a formal-proof claim, inspect the actual solution theorem, definitions, assumptions and trusted axioms. A comparator statement with sorry supplies a target; documentation or build success alone does not certify the proof.",
        "evidence":"SOURCE_SNAPSHOT_REPORT.json, two admitted headline bodies; memory slug perceptron_proof_open_gaps_fleet_2026_07_12","proposer":"w420"}
    assert len(hook["text"])<=300
    hook_text = json.dumps(hook,ensure_ascii=False)+"\n"
    (ROOT/"HOOK_PROPOSAL.jsonl").write_text(hook_text,encoding="utf-8")
    patches = ROOT/"patches"
    patches.mkdir(exist_ok=True)
    patch = "--- a/primary_directive/hooks1000/proposals/math-w420.jsonl\n+++ b/primary_directive/hooks1000/proposals/math-w420.jsonl\n@@ -0,0 +1 @@\n+"+hook_text
    (patches/"01_critical_proof_status_hook.diff").write_text(patch,encoding="utf-8")

    if measurements.get("passed"):
        m = measurements
        measurement_text = (f"Exact checks passed: {m['boundary_cases']['connected_subsets_of_3x3']} connected 3x3 subsets plus three hole/corner cases, zero contour failures; "
            f"16 domino configurations; {m['quantifier_counterexample_pairs']} scale evaluations. The invalid marginal product 1/256 understates the exact all-bad probability 1/16 by 16x; "
            f"the valid dependence-aware bound is 1/4. The Peierls error bound is {m['peierls_error_float']:.9f}<0.1. "
            f"Checks took {m['checks_seconds']:.4f} seconds under the fresh single-process gate.")
    else:
        measurement_text = "Numerical finite checks were held by the current fresh compute gate; the exact analytic reductions remain draft handwritten proofs. No unrun test or measured recall improvement is claimed."
    report = ("Prepared a dependence-aware C0023 proof route and isolated the one unproved critical anchor estimate. The full critical nonpercolation target remains unproved; current openness is UNKNOWN. "
        "The historical half-space route supplies no accepted gluing proof, and both inspected public comparator headline statements contain sorry.\n\n"
        +measurement_text+" Command: python -X utf8 ~/brain_workers/w420/prepare_packet.py.\n\n"
        "One connected draft bundle was submitted at ~/math-brain-inbox/w420/bundle_001.json: six concept entries, four supported internal relations, all explicitly draft material. "
        "There is no verified review, ingestion or retrievability receipt, no store mutation, and no formal proof receipt.\n\n"
        "Main review risk: the general exterior-boundary tracing in L2, followed by compatible anchors and the exact two-scale quantifiers. Finite checks do not prove the general lemma. "
        "Referee w422 has the proof packet; author served-model evidence is unverified.\n\n"
        "Apply: the validating coordinator reviews BUNDLE_REVIEW_COPY.json and ingests the submitted DRAFT through the existing integrator after its gates pass. "
        "The reviewer may apply patches/01_critical_proof_status_hook.diff from ~, or copy HOOK_PROPOSAL.jsonl to the named live proposal file; live hooks were not edited. "
        "The staged progress command is in PROGRESS_EVENT.txt because this worker's isolation rule forbids other external writes.\n\n"
        "NEXT: Referee L0--L5 and then seek a uniform fixed-aspect-ratio critical anchor estimate that discharges G; an iterated limit alone cannot do it.\n")
    (ROOT/"REPORT.md").write_text(report,encoding="utf-8")
    progress = "python -X utf8 ~/primary_directive/pd_progress.py --event \"w420 saved C0023 quantified anchor criterion, explicit scale gap and DRAFT packet; full target unproved\" --agent w420 --row S1.C0023 --evidence ~/brain_workers/w420/REPORT.md\n"
    (ROOT/"PROGRESS_EVENT.txt").write_text(progress,encoding="utf-8")
    (ROOT/"STATUS.md").write_text("STATE: NEEDS_REVIEW\nNEXT: w422 referee L0--L5; validating coordinator review the DRAFT; subsequent proof work must close G with a uniform finite-volume estimate.\n\n"
        "2026-10-10: Exact target and historical record recovered. Current openness UNKNOWN. Source-status finding: two public comparator bodies contain sorry.\n"
        "2026-10-10: Saved six supporting draft lemmas, one explicit unproved input, claim ledger, gated-check receipt and source snapshots. No target success, formal proof or novelty claimed.\n"
        "2026-10-10: Statement delivered to w421 (msg-bbb85bdc32); proof packet handed to w422. Six concept entries submitted in one DRAFT bundle; review/ingestion/retrievability separately unverified.\n",encoding="utf-8")
    filenames = ("ATTEMPT.md","CLAIMS.jsonl","SOURCE_STATUS.json","REVIEW_PACKET.md","REPORT.md","MEASUREMENTS.json","STATUS.md")
    save("REVIEW_FILE_HASHES.json", {name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in filenames})
    # These are ordinary packet file fingerprints, not canonical store digests/manifests.
    print(json.dumps({"checks":measurements,"bundle":str(final),"entries":len(payload['entries']),"relations":len(payload['relations']),"state":"NEEDS_REVIEW"},ensure_ascii=False))


if __name__=="__main__":
    main()
