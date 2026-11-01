"""Checkpoint review artifacts and a claimed draft; never integrate a store."""
from __future__ import annotations
import difflib
import hashlib
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w408")


def write(name, value):
    p = ROOT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(value if isinstance(value, str) else json.dumps(value, indent=2)+"\n", encoding="utf-8")


def entry(key, name, title, statement, kind="concept", assumptions=None):
    return {
        "key": key, "namespace":"probability.percolation", "logical_name":name,
        "kind":kind, "title":title, "statement":statement, "proof_text":None,
        "assumptions":assumptions or [], "domain":"planar probability and Loewner evolution",
        "source":{"source_id":"owner-own-work:w408:C0017-20261010", "url":None,
                  "revision":"2026-10-10-draft", "license":"owner-own-work (campaign derivations; independent review pending)", "excerpt":None},
    }


def main():
    # Persist each new claim as a row, retaining the existing first result rows.
    rows = [json.loads(s) for s in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
    seen = {r["id"] for r in rows}
    with (ROOT / "CLAIMS.jsonl").open("a", encoding="utf-8") as stream:
        extra_text = (ROOT / "ADDITIONAL_CLAIMS.jsonl").read_text(encoding="utf-8") + (ROOT / "GLOBAL_CLAIM.jsonl").read_text(encoding="utf-8")
        for line in extra_text.splitlines():
            r = json.loads(line)
            if r["id"] not in seen:
                stream.write(json.dumps(r, ensure_ascii=False)+"\n")
                stream.flush()
                rows.append(r)
                seen.add(r["id"])
    verdicts = [json.loads(s) for s in (ROOT/"review/w410_verdicts.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
    verdicts = [v for v in verdicts if str(v.get("item","")).startswith("w408")]
    keeps = [v for v in verdicts if v["verdict"]=="KEEP"]
    fixes = [v for v in verdicts if v["verdict"]=="FIX"]
    for r in rows:
        if r["id"]=="w408-S1.2":
            r["independent_review"]={"local":"KEEP by w410","global":"FIX revised explicitly in GLOBAL_EXHAUSTION.md; w413 pending"}
        if r["id"] in {"w408-S1.1","w408-S1.3","w408-S1.4","w408-S1.5","w408-S1.7","w408-S1.8"}:
            r["independent_review"]="Scoped mathematical KEEP by w410; see review/w410_verdicts.jsonl; served-model evidence unavailable"
    write("CLAIMS.jsonl","".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows))
    measurement = json.loads((ROOT / "MEASUREMENTS.json").read_text(encoding="utf-8"))
    stored = json.loads((ROOT / "STORE_TARGET_ROWS.json").read_text(encoding="utf-8"))
    target = next(r for r in stored if r[1].startswith("Open problem: Conformal invariance"))
    attempt = next(r for r in stored if r[1].startswith("Attempt on Conformal invariance"))
    target_logical = json.loads(target[3])["logical_id"]
    attempt_logical = json.loads(attempt[3])["logical_id"]
    nodes = [
        entry("cardy-function", "normalized-cardy-boundary-crossing-function", "Normalized Cardy crossing function",
              "For 0<u<1 define C(u)=B(1/3,1/3)^(-1) integral_0^u [v(1-v)]^(-2/3)dv, where B(1/3,1/3) is the same integral from 0 to 1. Thus C(0)=0, C(1)=1, C'>0 and C''/C'=2(2u-1)/(3u(1-u)). This definition alone is not a claim that square-lattice crossing probabilities converge to C.", "definition"),
        entry("two-martingales", "two-cardy-martingales-identify-sle-six-driver", "DRAFT: two Cardy martingales identify the SLE 6 driver",
              "Conditional reduction, independent review pending: let W be a continuous adapted real chordal Loewner driver, W_0=0, with dg_t(z)=2/(g_t(z)-W_t)dt in one usual filtration. For three real marks 0<a<b<c put X=g_t(a)-W_t and Y_i=g_t(b_i)-W_t, b_1=b,b_2=c. On each stopped compact localization with 0<X<Y_1<Y_2 and positive separations, assume BOTH C(X/Y_i) are local martingales, where C(u)=B(1/3,1/3)^(-1) integral_0^u [v(1-v)]^(-2/3)dv. Smooth inversion of the first makes W a semimartingale; the two Ito signed-measure equations force zero finite variation part and local martingale bracket 6dt. If the assumption holds for a countable mark/localization family covering every finite time, W/sqrt(6) is Brownian motion. The square-lattice martingale approximation needed to apply this reduction is unproved in this draft.",
              assumptions=["usual filtration; continuous adapted W", "capacity normalization 2", "both Cardy local martingales in the same filtration", "nondegenerate stopped mark separation", "covering family only for the global conclusion"]),
        entry("one-test-counterexample", "one-cardy-martingale-does-not-select-sle-six", "DRAFT: one Cardy martingale admits the wrong diffusion",
              "Conditional counterexample, independent review pending: for kappa>=0, kappa!=6, fix 0<a<b<c and stop in 0<X<Y<Z. Solve locally dX=[2/X-beta]dt-sqrt(kappa)dB and dY=[2/Y-beta]dt-sqrt(kappa)dB with beta=(6-kappa)(1/X+1/Y)/3, X_0=a,Y_0=b. Set W=integral beta dt+sqrt(kappa)B and Z=g_t(c)-W. These X,Y are real Loewner marks for W. For C(u)=B(1/3,1/3)^(-1) integral_0^u [v(1-v)]^(-2/3)dv, C(X/Y) is a local martingale, although W has bracket kappa dt and nonzero drift. The second Cardy observable C(X/Z) has normalized drift (6-kappa)(1/Z-1/Y)/3, which is nonzero. This refutes only one-observable identification, not percolation conformal invariance.",
              assumptions=["Brownian B", "smooth locally Lipschitz SDE stopped before mark collision", "Loewner capacity normalization 2"]),
        entry("square-cardy-gap", "square-bond-stopped-cardy-martingale-approximation-gap", "UNPROVED: stopped square bond Cardy approximation",
              "Unproved model-specific input for square-lattice bond percolation at p=1/2 with precisely fixed Dobrushin exploration and boundary crossing events: on each positive-separation localization of marked Loewner coordinates 0<X_delta<Y_delta,1<Y_delta,2, the correctly oriented bounded conditional crossing martingales P_delta,i should satisfy E sup_{t<=T wedge tau_delta}|P_delta,i(t)-C(X_delta,t/Y_delta,i,t)| -> 0 as delta -> 0. Here C(u)=B(1/3,1/3)^(-1) integral_0^u [v(1-v)]^(-2/3)dv. Compatible joint driver/mark convergence and limiting filtration are also required. This draft provides no proof of this estimate; rotational symmetry, self-duality and a local parafermion equation do not by themselves establish it. No C0017 solution or novelty is claimed."),
        entry("spin-convention", "standard-q-one-edge-parafermion-spin-one-third", "Standard q 1 edge parafermion spin convention",
              "Under the standard signed-radian edge parafermion convention F(e)=E[exp(i sigma W(e,e_b))1_{e in gamma}] with sigma in [0,1] satisfying sin(pi sigma/2)=sqrt(q)/2, q=1 gives sigma=1/3, since sin(pi/6)=1/2 and the sine is injective on that branch. The alternative exponent sigma-1 is -2/3. A positive spin 2/3 is not the standard branch; a different winding or conjugation convention must be stated explicitly. This elementary convention correction adds no missing analyticity estimate. Primary support is Definition 3 of Duminil-Copin, arXiv:1208.3787, and equation (1) of Zhou, arXiv:2409.03235v6."),
    ]
    relations = [
        {"from_key":"two-martingales","to_key":"cardy-function","kind":"depends_on","rationale":"The two driver tests use the normalized Cardy function and its positive derivative."},
        {"from_key":"one-test-counterexample","to_key":"cardy-function","kind":"depends_on","rationale":"The explicit incorrect diffusion preserves one test of this exact function."},
        {"from_key":"square-cardy-gap","to_key":"cardy-function","kind":"depends_on","rationale":"The unproved lattice estimate compares its martingales to this function."},
        {"from_key":"one-test-counterexample","to_key":"two-martingales","kind":"semantic_association","rationale":"The wrong-kappa construction explains why the identification criterion uses two distinct boundary tests."},
        {"from_key":"square-cardy-gap","to_key":"two-martingales","kind":"semantic_association","rationale":"If proved with compatible joint convergence, the lattice estimate would supply the two martingales assumed by the conditional criterion."},
        {"from_key":"square-cardy-gap","to_existing_logical":target_logical,"kind":"semantic_association","rationale":"This explicitly unproved input concerns identification of the square-bond exploration scaling limit in C0017."},
        {"from_key":"spin-convention","to_existing_logical":attempt_logical,"kind":"semantic_association","rationale":"The standard-branch convention is needed when using the historical C0017 parafermion attempt; its unqualified positive 2/3 spin requires correction or an explicit alternative convention."},
    ]
    bundle = {"spec":"mathbrain-draft-v1","author_agent":"w408","bundle_slug":"c0017-two-cardy-identification-w408-20261010","entries":nodes,"relations":relations}
    # Local shape checks only. Do not invoke the live integrator or source/store sealing.
    required = {"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
    keys = {e["key"] for e in nodes}
    assert len(keys)==len(nodes)
    for e in nodes:
        assert required <= e.keys() and e["kind"] in {"definition","concept"}
        assert e["proof_text"] is None and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",e["logical_name"])
        assert e["source"]["license"].startswith("owner-own-work")
    for r in relations:
        assert r["from_key"] in keys
        assert r.get("to_key") in keys or r.get("to_existing_logical") in {target_logical,attempt_logical}
        assert r["kind"] in {"depends_on","semantic_association"}
    INBOX.mkdir(parents=True, exist_ok=True)
    out = INBOX / "bundle_001.json"
    part = INBOX / "bundle_001.part"
    payload = json.dumps(bundle, indent=2)+"\n"
    write("drafts/bundle_001.json",payload)
    if not out.exists():
        if part.exists():
            raise RuntimeError("Existing part is preserved; choose a new bundle number")
        part.write_text(payload,encoding="utf-8")
        os.rename(part,out)
    elif out.read_text(encoding="utf-8") != payload:
        raise RuntimeError("Existing submitted bundle differs; preserve it")
    patch = "".join(difflib.unified_diff([],payload.splitlines(True),
                      fromfile="a/~/math-brain-inbox/w408/bundle_001.json",
                      tofile="b/~/math-brain-inbox/w408/bundle_001.json"))
    write("patches/01_c0017_draft.diff",patch)
    relation_evidence = []
    for r in relations:
        left = next(e for e in nodes if e["key"]==r["from_key"])
        if "to_key" in r:
            right = next(e for e in nodes if e["key"]==r["to_key"])
            endpoint = {"key":right["key"],"quote":right["statement"]}
        else:
            old = target if r["to_existing_logical"]==target_logical else attempt
            endpoint = {"logical_id":r["to_existing_logical"],"node_id":old[0],"quote":old[2]}
        relation_evidence.append({"from_key":left["key"],"from_quote":left["statement"],"to":endpoint,"kind":r["kind"],"rationale":r["rationale"],"review":"pending"})
    write("RELATION_EVIDENCE.jsonl","".join(json.dumps(r,ensure_ascii=False)+"\n" for r in relation_evidence))
    write("STORE_CORRECTION.md",f"# Proposed source-convention correction\n\nCanonical node: {attempt[0]}\nLogical ID: {attempt_logical}\n\nThe live attempt contains the unqualified phrase 'spin sigma = 2/3'. Definition 3 of arXiv:1208.3787 and Zhou v6 equation (1) use the standard positive branch 1/3. Preserve the historical attempt and its author-checked status; have the validating coordinator attach the convention correction or make a reviewed revision that identifies the convention. No write to the store was made. This is a source correction, not a new proof of conformal invariance.\n\nEvidence: STORE_TARGET_ROWS.json, SOURCE_STATUS.json, claim w408-S1.6, draft entry spin-convention.\n")
    write("INTEGRATION_STATE.json",{
        "target":"C0017","submitted":{"state":"COMPLETE_DRAFT_WRITTEN","path":str(out),"claim_id":"clm-f10f7c6c47"},
        "local_format_validation":{"state":"PASS","entries":len(nodes),"relations":len(relations),"theorem_or_lemma_promotions":0},
        "reviewed":{"state":"PARTIAL_KEEP_GLOBAL_FIX_REVISED","referee":"w410","request":"msg-13dae86ab1","scoped_keeps":keeps,"fixes":fixes,"global_revision":"GLOBAL_EXHAUSTION.md","global_revision_independent_review":"PENDING_W413"},
        "ingested":{"state":"NOT_OBSERVED","live_integrator_run_by_author":False},
        "retrievable":{"state":"NOT_CHECKED"},
        "author_response_served_model":"UNAVAILABLE","referee_response_served_model":"UNAVAILABLE",
        "different_model_review_gate":"NOT_PASSED","full_target_solved":False,
        "integration_contact":"codex-01a12190","measurement":measurement,
    })
    hooks = [
        {"id":"C0017-w408-01","area":"math","event":"PreToolUse","cue":"q=1 edge parafermion with positive sigma=2/3 and standard sine branch","fire_when":"Recalling the C0017 attempt's positive 2/3 as standard spin","silent_when":"An explicitly stated sigma-1=-2/3 or conjugated winding convention","text":"Check the winding convention: sin(pi sigma/2)=sqrt(q)/2 with sigma in [0,1] gives q=1 sigma=1/3. The sigma-1 variant is -2/3. This correction supplies no missing analyticity relation.","evidence":"w408-S1.6; STORE_TARGET_ROWS.json; primary Definition 3 arXiv:1208.3787","proposer":"w408"},
        {"id":"C0017-w408-02","area":"math","event":"Stop","cue":"C0017 is called solved after a driver algebra check while the lattice Cardy input is unproved","fire_when":"L1 passed locally but w408-S1.9 remains conjecture","silent_when":"Only the conditional identification lemma is claimed, with its input labeled unproved","text":"A two-Cardy-martingale criterion identifies the driver only under its hypotheses. Check the square-lattice stopped Cardy approximation, event convention and filtration limit before promoting C0017 to solved.","evidence":"w408-S1.9; ATTEMPT.md; memory slug perceptron_proof_open_gaps_fleet_2026_07_12","proposer":"w408"},
    ]
    assert all(len(h["text"])<=300 for h in hooks)
    write("HOOK_PROPOSALS.jsonl","".join(json.dumps(h)+"\n" for h in hooks))
    metric_text = (
        f"Exact checks passed on {measurement['state_triples']} distinct mark triples. With wrong kappa controls, one equation accepted {measurement['single_equation_incorrect_accepts']} and two accepted {measurement['two_equation_incorrect_accepts']}; the correct kappa=6 passed {measurement['valid_kappa6_states']}. CPU time {measurement['cpu_seconds']:.4f}s."
        if measurement["status"]=="PASS" else
        f"The exact-arithmetic check was HELD by the fresh resource gate: {measurement['reason']}. No algebra improvement measurement is claimed."
    )
    write("REPORT.md",f"The conditional local two-martingale identification and the one-martingale counterexample received scoped KEEP from w410. The square-lattice stopped Cardy approximation remains the single hardest unproved input; C0017 is not solved and current openness is UNKNOWN.\n\nThe standard positive parafermion spin is 1/3; one canonical target-attempt row currently serves unqualified 2/3. Primary source checks and a proposed convention correction are saved.\n\n{metric_text} Command: python -X utf8 ~/brain_workers/w408/verify_reduction.py. These checks, when run, concern finite algebra, not percolation universality or a formal stochastic theorem.\n\nSaved {len(rows)} claim rows and submitted a locally shape-checked DRAFT with {len(nodes)} entries and {len(relations)} relations; zero theorem promotions, no live store writes. w410 returned {len(keeps)} scoped KEEP verdicts and {len(fixes)} FIX. The global exhaustion FIX is addressed explicitly in GLOBAL_EXHAUSTION.md and awaits w413 review. Author/referee served-model evidence is unavailable; no different-model gate is claimed.\n\nApply: coordinator codex-01a12190 reviews the submitted bundle at {out.as_posix()} (review diff patches/01_c0017_draft.diff) and performs any validated integration or canonical correction after the relevant KEEP. The author does not run the live integrator. Hook proposals and the progress line are staged in this folder because global writes are outside this brief's allowed paths.\n\nRisks: boundary-event convention, joint stopped convergence and a valid capacity-time martingale embedding remain explicit prerequisites; the event candidate is now specified in ATTEMPT.md. Source hashes and numerical identities cannot fill those gaps. The owner-work search was bounded and does not certify novelty.\n\nNEXT: w413 audit the explicit global localization; prove the square-bond stopped Cardy defect estimate before any C0017 solution claim.\n")
    write("PROGRESS_EVENT.txt","w408 saved C0017 conditional two-Cardy-martingale proof, wrong-kappa counterexample and canonical spin correction; 5-entry DRAFT submitted, hardest square-bond input unproved; evidence REPORT.md, row S1.2.\n")
    # These identify ordinary review-file bytes, not source/store seals or proof receipts.
    names = ["ATTEMPT.md","GLOBAL_EXHAUSTION.md","COUNTEREXAMPLES.md","CLAIMS.jsonl","SOURCE_STATUS.json","REPORT.md","MEASUREMENTS.json","REVIEW_PACKET.md","review/w410_verdicts.jsonl"]
    write("ARTIFACT_FINGERPRINTS.json",{
        "purpose":"review artifact byte identity only; not a proof/served-model/store-seal receipt",
        "sha256":{n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in names},
    })
    print(json.dumps({"status":"REVIEW_PACKET_SAVED","claims":len(rows),"draft_entries":len(nodes),"draft_relations":len(relations),"submitted_path":str(out),"algebra_gate":measurement["status"],"parent_solved":False}))


if __name__=="__main__":
    main()
