"""Prepare reviewable draft concepts and diffs; optional scoped inbox submission."""
import argparse
import difflib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

base = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--submit", action="store_true", help="write only the explicitly assigned w354 draft inbox file")
args = parser.parse_args()
source = {"source_id": "owner-probability-campaign-20261010:w354-p0017-simplex-fibers", "url": "urn:probability-research:20261010:w354:p0017-simplex-fibers", "revision": "independently-checked-special-cases-20261010-v2", "license": "owner-own-work; campaign boundary proof, no novelty claim", "excerpt": None}
namespace = "probability.functional-inequalities"

def entry(key, logical, title, statement, assumptions):
    return {"key": key, "namespace": namespace, "logical_name": logical, "kind": "concept", "title": title, "statement": statement, "proof_text": None, "assumptions": assumptions, "domain": "probability theory", "source": dict(source)}

construction = "Let d>=2, K=(d+1)(d+2), X be uniform on Delta_d={x_i>=0,sum_i x_i<=1}, m=(1,...,1)/(d+1), Sigma=(I-J/(d+1))/K with J the all-ones matrix, A=Sigma^(-1/2), Y=A(X-m), a=sqrt(2K), and v=Ae_1/a. Put Z=Proj_(v-perp)Y, T=<v,Y> and S=sum_(j=2)^d X_j. "
draft = "DRAFT: author-proved special case, independent mathematical audit pending; no novelty claim. "
entries = [
    entry("p0017-source-context", "p0017-kls-primary-proof-claims-october-2026", "P0017: October primary proof claims supersede dated openness evidence", "DRAFT source annotation; mathematical validity of the cited proofs is not audited here. P0017 asks for an absolute positive Euclidean Cheeger lower bound for every isotropic log-concave probability in every dimension, equivalently an absolute upper bound on its Euclidean Poincare constant. The cited intake source is arXiv:2603.29571v1, Entry 13, Conjecture 30. Bizeul, Klartag and Lehec, arXiv:2610.05474v1 (4 October 2026), Theorem 1.1, claims the complete target. Balasubramanian and Kasiviswanathan, arXiv:2610.07728v2 (8 October), claims C_P<=25. These primary proof claims prevent treating the 7 September campaign ranking as certification of current openness. This worker records current openness UNKNOWN and claims no new solution.", ["Source status checked 10 October 2026", "Poincare uses the full Euclidean gradient", "Historical openness and independent proof validation are distinct"]),
    entry("uniform-fiber-proposal", "isotropic-log-concave-uniform-fiber-bound-invalid-proposal", "Rejected auxiliary proposal: dimension-free constants on all isotropic fibers", "REJECTED AUXILIARY PROPOSAL, not a theorem: isotropy and log-concavity alone might seem to imply a universal M such that, for every dimension d, every isotropic log-concave Y and every unit v, ess sup_z C_P(Law(<v,Y>|Proj_(v-perp)Y=z))<=M. The isotropic uniform-simplex construction refutes this stronger assertion, with essential supremum 2(d+1)(d+2)/pi^2. Its failure does not refute the KLS inequality with the full gradient.", ["Scalar fiber coordinates use the intrinsic Euclidean metric", "Essential supremum is relative to the projection marginal", "Independent audit of the supplied counterexample pending"]),
    entry("mean-fiber-proposal", "conditional-poincare-arithmetic-averaging-invalid-proposal", "Rejected auxiliary proposal: separate mean fiber constant from energy", "REJECTED AUXILIARY PROPOSAL, not a theorem: for T=<v,Y> and Z=Proj_(v-perp)Y, replacing the valid weighted fiber inequality by E Var(f(Y)|Z)<=E[C_P(T|Z)] E|partial_v f(Y)|^2 is unjustified for general dependent log-concave laws. A smooth polynomial on the isotropic uniform triangle refutes it. The valid first step is E Var(f|Z)<=E[C_P(T|Z) E(|partial_v f|^2|Z)]. Any separation requires a proved decorrelation estimate or additional structure.", ["Y is isotropic and log-concave", "v is a unit vector", "f is locally Lipschitz with finite energies", "Independent audit of the supplied counterexample pending"]),
    entry("simplex-fibers", "isotropic-simplex-orthogonal-fiber-constants", "Isotropic simplex: exact conditional Poincare and Cheeger constants", draft + construction + "Then Y is centered and isotropic, and conditioning on Z fixes X_2,...,X_d. T|Z is uniform on [-a(1-S)/2,a(1-S)/2], where S has Beta(d-1,2) distribution. Therefore ess sup C_P(T|Z)=2K/pi^2, E C_P(T|Z)=12/pi^2, and ess inf h(T|Z)=sqrt(2/K), with h defined using the outer Euclidean Minkowski perimeter divided by min mass. With probability (d+1)/2^d the conditional Poincare constant is at least K/(2 pi^2). These are genuine positive-probability fiber neighborhoods, not a claim based only on a zero-probability edge.", ["Integer d>=2", "Uniform full-dimensional simplex", "Orthogonal projection after whitening", "Essential extrema relative to Law(Z)"]),
    entry("optimal-directional", "isotropic-simplex-optimal-directional-conditional-poincare", "Isotropic simplex: optimal directional conditional inequality", draft + construction + "The least constant C such that E Var(f(Y)|Z)<=C E|partial_v f(Y)|^2 for every locally Lipschitz f with finite full and directional energies is exactly 2K/pi^2. The upper bound uses the essential supremum of the fiber constants. Localized first Neumann sine modes on fibers with 0<S<epsilon attain the bound in the limit epsilon to zero. The optimal constant exceeds the arithmetic mean of the fiber constants by K/6. Orthogonal gradient energy is present in the full KLS inequality and cannot be omitted.", ["Integer d>=2", "Scalar directional derivative along unit v", "Each test has finite full energy; no uniform bound on its orthogonal energy is asserted"]),
    entry("triangle-polynomial", "isotropic-triangle-polynomial-refutes-mean-fiber-poincare", "Smooth triangle witness to false mean fiber averaging", draft + "Let X be uniform on {x_1,x_2>=0,x_1+x_2<=1}, m=(1/3,1/3), Sigma=[[1/18,-1/36],[-1/36,1/18]], A=Sigma^(-1/2), Y=A(X-m), a=sqrt(24), v=Ae_1/a, Z=Proj_(v-perp)Y, S=X_2 and T=<v,Y>=a(X_1-(1-S)/2). The polynomial f(Y)=T(1-S)^2 has mean zero, E Var(f|Z)=1/2, E|partial_v f|^2=1/3, and E|grad f|^2=13/27. Since E C_P(T|Z)=12/pi^2, arithmetic averaging would require 1/2<=4/pi^2, which is false. The full-gradient quotient is 27/26, so this example is not a KLS counterexample.", ["Uniform isotropic triangle after the specified whitening", "Full Euclidean gradient in the last energy", "Independent exact rational monomial check saved separately"])
]
existing_target = "math:probability.core:open-problem-p0017-dimension-free-log-concave-poincare-or-cheeger-constant"
existing_attempt = "math:probability.core:attempt-p0017-dimension-free-log-concave-poincare-or-cheeger-constant"
relations = [
    {"from_key": "p0017-source-context", "to_existing_logical": existing_target, "kind": "cites", "rationale": "The September target card states the isotropic Cheeger question and honestly labels its current status unverified; this annotation adds the October primary proof claims."},
    {"from_key": "simplex-fibers", "to_existing_logical": existing_target, "kind": "semantic_association", "rationale": "The isotropic simplex is within the target's log-concave class, but its conditional constants address a stronger auxiliary fiber statement."},
    {"from_key": "simplex-fibers", "to_existing_logical": existing_attempt, "kind": "semantic_association", "rationale": "The previous attempt uses the Gaussian Hermite generator; the dependent simplex tests a distinct conditional route without that generator."},
    {"from_key": "simplex-fibers", "to_key": "uniform-fiber-proposal", "kind": "refutes", "rationale": "The essential supremum equals 2(d+1)(d+2)/pi^2 and is unbounded with dimension on positive-probability neighborhoods."},
    {"from_key": "optimal-directional", "to_key": "simplex-fibers", "kind": "depends_on", "rationale": "Uses the exact orthogonal fiber distribution and constants of the whitened simplex."},
    {"from_key": "optimal-directional", "to_key": "mean-fiber-proposal", "kind": "refutes", "rationale": "The optimal directional constant is the fiber essential supremum, K/6 times its arithmetic mean."},
    {"from_key": "triangle-polynomial", "to_key": "simplex-fibers", "kind": "specializes", "rationale": "Dimension two, with all whitening and scalar fiber variables explicitly specified."},
    {"from_key": "triangle-polynomial", "to_key": "mean-fiber-proposal", "kind": "refutes", "rationale": "Variance 1/2 exceeds the proposed right side 4/pi^2 while full energy is accounted for as 13/27."}
]
full_pre_dedup = {"spec": "mathbrain-draft-v1", "author_agent": "w354", "bundle_slug": "p0017-simplex-fiber-boundary-w354-001", "entries": entries, "relations": relations}
archive = base / "drafts" / "bundle_001.full_pre_dedup.json"
archive.parent.mkdir(exist_ok=True)
if not archive.exists():
    archive.write_text(json.dumps(full_pre_dedup, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# The peer drafts already supply the common theorem, status and triangle cards.
# Keep distinct proof-method and full polynomial-family cards in this draft.
entries = [
    entry("localized-neumann", "isotropic-simplex-localized-neumann-sine-test-family", "Isotropic simplex: localized admissible Neumann modes attain the sharp directional bound", "DRAFT proof-method concept; this special-case argument was independently checked by w355 and assigned referee w356. No novelty or full KLS claim. " + construction + "Given 0<epsilon<1, choose a nonzero smooth eta supported in (epsilon/4,epsilon/2) and put f(Y)=eta(S) sin(pi T/(a(1-S))). Each such f has finite full energy, E[f|Z]=0, E Var(f|Z)=E eta(S)^2/2 and E|partial_v f|^2=(pi^2/(2a^2)) E[eta(S)^2/(1-S)^2]. Its directional quotient is at least (2K/pi^2)(1-epsilon)^2, and the support has positive probability. Letting epsilon go to zero proves that the optimal directional conditional coefficient is 2K/pi^2. This card records the localized admissible witness method, rather than duplicating the common simplex-constants card. It does not bound the full-gradient KLS constant.", ["Integer d>=2", "eta is nonzero smooth with the indicated support", "Each fixed-epsilon full gradient energy is finite", "Independent KEEP receipts are in w354 REFEREE_VERDICTS.json and w355 W354_AUDIT.md"]),
    entry("polynomial-family", "isotropic-simplex-polynomial-directional-and-full-gradient-energy-family", "Isotropic simplex: exact directional and full energies of the polynomial family", "DRAFT independently checked special-case formula: w355's full-packet audit checked Section 5; w356 kept its d=2,k=2 specialization. No novelty or full KLS claim. " + construction + "For every integer k>=1 put t=1-S, f(Y)=T t^k and M_p=(p+1)! d!/(d+p)!. Then E[f|Z]=0, E Var(f|Z)=(K/6) M_(2k+2), E|partial_v f|^2=M_(2k), and E|grad f|^2=[1+k^2(d-1)/(3(d+1))] M_(2k). Thus the exact directional quotient is R_(d,k)=(K/6)(2k+2)(2k+3)/[(d+2k+1)(d+2k+2)], while the full-gradient quotient is R_(d,k)/[1+k^2(d-1)/(3(d+1))]. The extra factor is the transverse gradient cost: grad_Y S is perpendicular to v and has squared norm 2(d-1)/((d+1)K). For d=2,k=2 these give variance 1/2, directional energy 1/3 and full energy 13/27. The family generalizes the separately submitted triangle witness and explicitly preserves all gradient terms.", ["Integer d>=2 and integer k>=1", "Inherited Euclidean metric after whitening", "All functions are polynomials on a compact simplex and have finite full energy", "General-family formula checked in w355's independent Section 5 audit; assigned referee's separate exact general-family row requested"])
]
relations = [
    {"from_key": "localized-neumann", "to_existing_logical": existing_target, "kind": "semantic_association", "rationale": "An admissible test family exposes the sharp coefficient of a stronger directional conditional route within the KLS class; no conclusion refutes the full-gradient target."},
    {"from_key": "polynomial-family", "to_existing_logical": existing_target, "kind": "semantic_association", "rationale": "Exact transverse-energy accounting stress-tests conditional routes to the covariance-normalized target."},
    {"from_key": "polynomial-family", "to_key": "localized-neumann", "kind": "analogous_to", "rationale": "Both are explicit mean-zero fiber test families, but the polynomial family also records its full transverse energy exactly."}
]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w354", "bundle_slug": "p0017-simplex-fiber-boundary-w354-001", "entries": entries, "relations": relations}
text = json.dumps(bundle, indent=2, ensure_ascii=False) + "\n"
local_bundle = base / "drafts" / "bundle_001.json"
local_bundle.parent.mkdir(exist_ok=True)
local_bundle.write_text(text, encoding="utf-8")
patches = base / "patches"
patches.mkdir(exist_ok=True)
inbox_target = Path("~/math-brain-inbox/w354/bundle_001.json")

def patch(old, new, target, name):
    normalized = target.as_posix()
    preamble = f"diff --git a/{normalized} b/{normalized}\n"
    if not old:
        preamble += "new file mode 100644\n"
    body = "".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile=("a/" + normalized if old else "/dev/null"), tofile="b/" + normalized))
    (patches / name).write_text(preamble + body, encoding="utf-8")

patch("", text, inbox_target, "01_p0017_draft_bundle.diff")
hook_target = Path("~/primary_directive/hooks1000/proposals/math-w354.jsonl")
old_hook = hook_target.read_text(encoding="utf-8-sig") if hook_target.exists() else ""
new_hook = (base / "hooks" / "math-w354.jsonl").read_text(encoding="utf-8")
(base / "hooks" / "LIVE_BASE.jsonl").write_text(old_hook, encoding="utf-8")
patch(old_hook, old_hook + new_hook, hook_target, "02_conditional_energy_hook.diff")
state_path = base / "BRAIN_DELIVERY.json"
state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
state.update({"prepared": {"complete": True, "at": datetime.now(timezone.utc).isoformat(), "local_file": str(local_bundle), "entries": len(entries), "relations": len(relations)}, "reviewed": {"complete": True, "scope": "claims 001-004: w356 four KEEP verdicts; w355 complete-packet KEEP including the general Section 5 formulas", "reviewers": ["w355", "w356"], "receipt": "REFEREE_VERDICTS.json", "account_distinctness_verified": False, "bundle_relation_admission": "pending validating coordinator"}, "ingested": {"complete": False}, "retrievable": {"complete": False}, "integration_attempted": False, "integration_policy": "validating coordinator integrates; mathematical facts remain concept drafts until admission", "deduplication": "two distinct method/family concepts retained; six common fact/status/proposal cards mapped to peers in DEDUP_MAP.json"})
state.setdefault("submitted", {"complete": False, "file": str(inbox_target)})
if args.submit:
    validation = json.loads((base / "BUNDLE_VALIDATION.json").read_text(encoding="utf-8"))
    if validation.get("errors"):
        raise SystemExit("Refusing submission: local draft parser reported errors")
    if validation.get("file") != str(local_bundle) or validation.get("validated_payload") != bundle:
        raise SystemExit("Refusing submission: validation receipt names a different file")
    if inbox_target.exists():
        if inbox_target.read_text(encoding="utf-8") != text:
            raise SystemExit("Refusing to overwrite an existing different draft")
    else:
        inbox_target.parent.mkdir(parents=True, exist_ok=True)
        part = inbox_target.with_suffix(".json.part")
        if part.exists():
            raise SystemExit("Refusing to overwrite an existing partial draft")
        part.write_text(text, encoding="utf-8")
        os.rename(part, inbox_target)
    state["submitted"] = {"complete": True, "at": datetime.now(timezone.utc).isoformat(), "file": str(inbox_target), "state": "DRAFT method/family concepts; independent special-case reviews attached; coordinator admission pending"}
state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")
print(json.dumps({"entries": len(entries), "relations": len(relations), "submitted": state["submitted"]["complete"], "local_bundle": str(local_bundle)}, indent=2))
