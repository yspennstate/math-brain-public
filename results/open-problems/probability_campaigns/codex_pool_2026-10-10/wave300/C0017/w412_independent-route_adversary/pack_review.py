"""Prepare reviewed-by-human-ready draft additions; writes only under w412."""
import difflib
import json
from pathlib import Path

BASE = Path("~/brain_workers/w412").resolve()

def write_local(relative, text):
    path = (BASE / relative).resolve()
    if not path.is_relative_to(BASE):
        raise ValueError("Output escaped worker folder")
    path.parent.mkdir(parents=True, exist_ok=True)
    if relative.startswith("brain_drafts/"):
        part = path.with_suffix(path.suffix+".part").resolve()
        if not part.is_relative_to(BASE):
            raise ValueError("Part output escaped worker folder")
        part.write_text(text, encoding="utf-8")
        part.replace(path)
    else:
        path.write_text(text, encoding="utf-8")
    return path

def own_source(slug, filename):
    return {
        "source_id": "owner-own-work:w412:"+slug,
        "url": "file:///~/brain_workers/w412/"+filename,
        "revision": "draft-peer-math-keep-integration-pending-2026-10-10",
        "license": "owner-own-work",
        "excerpt": None
    }

def entry(key, logical, kind, title, statement, assumptions, filename="ATTEMPT.md"):
    return {
        "key": key, "namespace": "probability.percolation", "logical_name": logical,
        "kind": kind, "title": title, "statement": statement, "proof_text": None,
        "assumptions": assumptions, "domain": "probability theory",
        "source": own_source(logical, filename)
    }

bundle = {
    "spec": "mathbrain-draft-v1", "author_agent": "w412",
    "bundle_slug": "c0017-conditional-cardy-route-w412-001",
    "entries": [
        entry("cardy-function", "cardy-beta-integral-crossing-function", "definition", "Normalized Cardy crossing function",
              "For 0<=u<=1, define C(u)=B(1/3,1/3)^(-1) times the integral from 0 to u of [s(1-s)]^(-2/3) ds, where B(1/3,1/3) is the same integral over [0,1]. This defines a function; invoking it as a square-lattice crossing limit requires a separate convergence theorem.", ["u in [0,1]."]),
        entry("two-cardy-driver", "draft-two-cardy-martingales-identify-chordal-sle-six-driver", "concept", "DRAFT: two Cardy martingales identify a local SLE(6) driver",
              "DRAFT conditional derivation, kept mathematically by independent referee w413 in REVIEW_PACKET.md on 2026-10-10; integration's served-model/different-model gate remains unestablished. This is not a square-bond percolation proof. Let W be a continuous adapted real driver with deterministic W(0) for chordal Loewner dg_t(z)=2/(g_t(z)-W_t)dt in a usual filtration. Choose W(0)<x1<x2<x3, with 0<X1<X2<X3 before swallowing, Xi=g_t(xi)-W_t. If BOTH C(X1/X2) and C(X1/X3) are continuous local martingales in the SAME filtration throughout a locally stopped lifetime, then W-W(0) is a continuous local martingale with quadratic variation 6t over that lifetime. Invert the first observable to make W a semimartingale; Ito gives dA=(1/Xi+1/Xj)(2dt-dV/3), where A is the driver drift measure and V its local-martingale quadratic variation. Subtract the two identities to force dV=6dt and dA=0. Square-lattice conditional Cardy limits and trace convergence remain unproved here; retain concept/draft status until the remaining promotion gate passes.",
              ["Usual filtration and a continuous adapted Loewner driver.", "Capacity convention dg=2/(g-W)dt.", "Three ordered, positive, surviving boundary distances.", "Both specified Cardy observables are local martingales in the same filtration.", "Conclusion only over a lifetime covered by localized observable hypotheses."]),
        entry("one-cardy-counterexample", "draft-single-cardy-martingale-does-not-identify-sle-six", "concept", "DRAFT: one Cardy martingale admits a deterministic driver",
              "DRAFT explicit obstruction kept mathematically by independent referee w413 on 2026-10-10; integration's served-model/different-model gate remains unestablished. This is a counterexample to a general inference, not to the percolation conjecture. For 0<=t<1/2, set Y=sqrt(4-8t), W=3-3Y/2, g_t(1)=3-Y and g_t(2)=3-Y/2. The real Loewner equations hold: g_t(1)'=2/(Y/2) and g_t(2)'=2/Y. Their distances from W have ratio 1/2, so the single Cardy observable C((g_t(1)-W)/(g_t(2)-W)) is the constant martingale 1/2. W is nonconstant deterministic finite variation with zero quadratic variation, so one such observable cannot identify a Brownian driver without further premises. For a third mark starting at 3, the initial ratio derivative is -2/27, and its Cardy observable is not a martingale.",
              ["Capacity convention 2; deterministic filtration.", "Times strictly below 1/2, before swallowing.", "C is the normalized beta-integral crossing function."]),
        entry("conditional-gap", "square-bond-percolation-conditional-cardy-identification-gap", "concept", "Square-bond percolation: conditional observable identification gap",
              "The unproved input in the w412 Cardy-martingale route is identification of TWO actual discrete crossing or boundary-order Doob martingales, including their induced primal/dual boundary conditions after exploration, with joint limits C(X1/X2) and C(X1/X3) in the SAME limiting exploration filtration on random slit domains. Exact discrete martingale identities alone do not identify their limiting functions. Fixed-domain crossing estimates, RSW tightness and large-scale rotational invariance do not alone supply this stated input. Joint convergence must retain the past-versus-future martingale identities; an enlarged filtration and discontinuous boundary stopping times require their own checks. No square-lattice conformal-invariance result is asserted by this draft.",
              ["Application under discussion is critical independent square-lattice bond percolation at p=1/2.", "This is a proof-gap record for the specific conditional-observable route, not a claim that it is the only possible route."]),
        entry("source-status-guard", "c0017-historical-source-and-unknown-current-proof-status", "concept", "C0017: historical source and unverified current proof claims",
              "C0017 asks for Cardy crossing limits and SLE(6) exploration limits for critical independent bond percolation on the square lattice at p=1/2. Garban-Steif arXiv:1102.5761v3, Chapter II section 4, printed p.24 / PDF page 26, calls its conformal invariance an open problem in 2012; the adjacent established Theorem II.2 concerns triangular-lattice site percolation. A bounded 2026-10-10 primary search also found square-bond proof claims arXiv:1112.2017v5 and arXiv:2409.03235v6, without independently checking their mathematics. Thus the task records current openness as UNKNOWN and makes no novelty claim. Historical source wording, an arXiv abstract, a source hash, or an ingestion receipt is not an independent mathematical proof certificate.",
              ["Status date 2026-10-10.", "Bounded search and source-recovery evidence only; no soundness judgment of the claimed square-bond proofs."], "SOURCE_STATUS.json")
    ],
    "relations": [
        {"from_key": "two-cardy-driver", "to_key": "cardy-function", "kind": "depends_on", "rationale": "The conditional driving-process derivation uses precisely this C(u)."},
        {"from_key": "one-cardy-counterexample", "to_key": "cardy-function", "kind": "depends_on", "rationale": "The counterexample uses C(1/2)=1/2 by symmetry of this defining integral."},
        {"from_key": "conditional-gap", "to_key": "two-cardy-driver", "kind": "semantic_association", "rationale": "Names the missing lattice input for the explicitly conditional draft reduction; does not claim to prove it."},
        {"from_key": "source-status-guard", "to_existing_logical": "math:probability.percolation:open-problem-c0017-conformal-invariance-of-critical-bond-percolation-on-the-square-lattic", "kind": "cites", "rationale": "The exact C0017 intake target is present in exported card claim_91f295e6d2a67634c0b90a5ee4130c1feed72dc0fe16086a679021c90c8917cb. Current live-store resolution remains for the integrator."}
    ]
}

serialized = json.dumps(bundle, ensure_ascii=False, indent=2)+"\n"
draft_path = write_local("brain_drafts/bundle_001.json", serialized)
live_bundle = "~/math-brain-inbox/w412/bundle_001.json"
patch = "".join(difflib.unified_diff([], serialized.splitlines(keepends=True), fromfile="a/"+live_bundle, tofile="b/"+live_bundle))
write_local("patches/01_C0017_draft_bundle.diff", patch)

hook = {
    "id": "conditional-cardy-w412-01", "area": "math", "event": "PostToolUse",
    "cue": "A proof infers a Brownian Loewner driver solely from one Cardy-ratio martingale, or replaces an unproved conditional Cardy limit with a raw discrete Doob identity.",
    "fire_when": "One Cardy-ratio observable is constant for the deterministic Loewner driver in w412-C0017-X1, yet a Brownian driver is inferred.",
    "silent_when": "Brownian or zero-drift driver structure is independently justified and one observable only determines its variance; or two limiting Cardy martingales are proved in one filtration with localization; or the identification remains explicitly a gap.",
    "text": "An exact Doob identity does not identify a limiting Cardy function. One Cardy observable does not by itself make a Loewner driver Brownian. Check the conditional limit, filtration and boundary conditions before identifying SLE(6).",
    "evidence": "~/brain_workers/w412/ATTEMPT.md, w412-C0017-X1; MEASUREMENTS.json: 639 exact controls, zero failures; scar proof_steps_need_derived_joint_structure_2026_09_09.",
    "proposer": "w412"
}
hook_text = json.dumps(hook, ensure_ascii=False)+"\n"
write_local("hooks1000/proposals/math-w412.jsonl", hook_text)
live_hook = "~/primary_directive/hooks1000/proposals/math-w412.jsonl"
write_local("patches/02_C0017_hook_proposal.diff", "".join(difflib.unified_diff([], hook_text.splitlines(keepends=True), fromfile="a/"+live_hook, tofile="b/"+live_hook)))

keys = {e["key"] for e in bundle["entries"]}
allowed_relations = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
checks = 0
def require(condition):
    global checks
    checks += 1
    if not condition:
        raise AssertionError("draft validation failed at check "+str(checks))
require(len(keys) == len(bundle["entries"]) <= 200)
for e in bundle["entries"]:
    require(required <= e.keys())
    require(e["kind"] in {"definition", "concept"} and e["proof_text"] is None)
    require(bool(e["statement"]) and bool(e["logical_name"]))
    require(e["source"]["license"].startswith("owner-own-work"))
    if e["key"] in {"two-cardy-driver", "one-cardy-counterexample"}:
        require(e["statement"].startswith("DRAFT") and "different-model gate remains unestablished" in e["statement"])
edges = []
endpoint_evidence = []
for r in bundle["relations"]:
    require(r["from_key"] in keys and r["kind"] in allowed_relations)
    require(("to_key" in r) != ("to_existing_logical" in r))
    if "to_key" in r:
        require(r["to_key"] in keys)
        if r["kind"] == "depends_on":
            edges.append((r["from_key"], r["to_key"]))
        target = next(e["statement"] for e in bundle["entries"] if e["key"] == r["to_key"])
    else:
        target = "OPEN PROBLEM (source_says_open; current status no_resolution_found_in_documented_search; result status attempted_unsolved). Prove that critical bond percolation on Z^2 at p = 1/2 is conformally invariant in the scaling limit (Cardy's formula and convergence of interfaces to SLE(6)), as is known on the triangular lattice by Smirnov."
    endpoint_evidence.append({"relation": r, "from_statement": next(e["statement"] for e in bundle["entries"] if e["key"] == r["from_key"]), "to_statement": target, "target_evidence": "same draft" if "to_key" in r else "export nodes.jsonl:5279; LIVE_TARGET_RECEIPT.json confirms exact node ID claim_91f295e6d2a67634c0b90a5ee4130c1feed72dc0fe16086a679021c90c8917cb and its logical ID by a read-only population query; proposed edge is not ingested"})
for origin in keys:
    stack = [(origin, set())]
    while stack:
        node, path = stack.pop()
        require(node not in path)
        stack.extend((b, path | {node}) for a, b in edges if a == node)
require(len(hook["text"]) <= 300)
require(set(hook) == {"id", "area", "event", "cue", "fire_when", "silent_when", "text", "evidence", "proposer"})
require(patch.count("@@") == 2)
require("".join(line[1:] for line in patch.splitlines(keepends=True) if line.startswith("+") and not line.startswith("+++")) == serialized)
with (BASE / "CLAIMS.jsonl").open(encoding="utf-8") as f:
    for line in f:
        claim = json.loads(line)
        require(all(k in claim for k in ("statement", "assumptions", "source", "independent_reviewer", "remaining_gap", "status")))

write_local("RELATION_ENDPOINT_EVIDENCE.json", json.dumps(endpoint_evidence, ensure_ascii=False, indent=2)+"\n")
validation = {"command": "python -X utf8 ~/brain_workers/w412/pack_review.py", "checks": checks, "failures": 0, "entries": len(bundle["entries"]), "relations": len(bundle["relations"]), "new_result_kind": "concept/draft only", "unreviewed_theorem_entries": 0, "proof_or_math_certification": False, "draft_path": str(draft_path), "scope": "Local schema, labels, endpoint evidence, acyclicity and additive-patch reconstruction. Referee mathematical KEEP is a separate receipt; the integrator has not run."}
write_local("VALIDATION.json", json.dumps(validation, indent=2)+"\n")
states = {"prepared": True, "submitted": False, "reviewed": True, "review_scope": "w413 kept the conditional lemma, deterministic counterexample and source guard; different-model/served-model gate remains unestablished", "ingested": False, "retrievable": False, "reason": "Local draft and unified additions await coordinator application and remaining integration gates. Never run integrate_drafts.py from this worker.", "intended_inbox_path": live_bundle}
handoff_path = BASE / "HANDOFF_RECEIPT.json"
if handoff_path.exists():
    handoff = json.loads(handoff_path.read_text(encoding="utf-8"))
    states["review_packet_handoff"] = {"recipient": "codex-01a12190", "sent": handoff.get("packet_handoff_sent", False), "receipt": "HANDOFF_RECEIPT.json"}
write_local("SUBMISSION_STATE.json", json.dumps(states, indent=2)+"\n")
write_local("progress_events.jsonl", json.dumps({"event": "w412 C0017: two-martingale conditional reduction and deterministic counterexample saved; 639 exact controls pass; draft packet ready for independent review.", "agent": "w412", "row": "S1.C0017", "evidence": str(BASE / "ATTEMPT.md"), "state": "queued locally, not posted"})+"\n")
write_local("team_notices.jsonl", json.dumps({"to": ["w411", "w413"], "kind": "found", "body": "w412's distinct conditional-Cardy route is in ATTEMPT.md; w413 kept conditional L1 and deterministic X1. ADVERSARY.md keeps w411 L1-L4 at finite scope and fixes the normalization convention. Full C0017 is not proved. Review packet was routed separately to the explicitly requested integration contact, with its receipt retained.", "state": "local notice for peers; integration handoff state is in HANDOFF_RECEIPT.json"})+"\n")
print(json.dumps(validation), flush=True)
