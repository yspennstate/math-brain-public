"""Prepare and validate owned draft artifacts; never integrate a live store."""
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w534")
NOW = datetime.now(timezone.utc).isoformat()
VERIFICATION = json.loads((ROOT / "VERIFICATION.json").read_text(encoding="utf-8"))
assert VERIFICATION["outcome"] == "passed"
PASSED = sum(bool(row.get("passed")) for row in VERIFICATION["rows"])
assert PASSED == 12
REVIEW = Path("~/brain_workers/w536/AUDITS_w534.jsonl")
audits = [json.loads(line) for line in REVIEW.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
keeps = {row["target"]: row["verdict"] for row in audits}
assert keeps["S1.w534.C2"] == "KEEP"
assert keeps["S1.w534.C3"] == "KEEP"
assert keeps["S1.w534.C4"] == "KEEP_SCOPED"


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def complete_new_json(path, value):
    """Complete a .part then rename; preserve any different existing artifact."""
    content = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_text(encoding="utf-8") != content:
            raise FileExistsError(f"Preserving existing different artifact: {path}")
        return
    for attempt in range(10):
        part = path.with_name(f"{path.stem}.{attempt}.part")
        if not part.exists():
            with part.open("x", encoding="utf-8") as stream:
                stream.write(content)
            assert json.loads(part.read_text(encoding="utf-8")) == value
            part.rename(path)
            return
    raise FileExistsError("No unused .part name; preserve all files and choose a new bundle number.")


def entry(key, logical, title, statement, assumptions, proof=None, claim=None):
    return {
        "key": key, "namespace": "probability.riesz", "logical_name": logical,
        "kind": "lemma" if proof else "concept", "title": title,
        "statement": statement, "proof_text": proof, "assumptions": assumptions,
        "domain": "probability theory and classical equilibrium statistical mechanics",
        "source": {"source_id": f"owner-p0309-w534-20261010:{claim or key}",
                   "url": f"urn:owner-own-work:w534:P0309:2026-10-10:{claim or key}",
                   "revision": "independently-reviewed-w536-20261010-scoped-v1",
                   "license": "owner-own-work", "excerpt": None}
    }


entries = [
    entry("heat-relative", "alternating-plane-riesz-relative-heat-integral",
          "Alternating-plane Riesz heat difference (specified integral only)",
          "For s>0 and real a define Theta(t,a)=sum_{m in Z} exp(-t(m+a)^2), O(t)=sum_{n odd} exp(-t n^2), and D_s(a)=(2 Gamma(s/2))^{-1} integral_0^infinity t^{s/2-1} Theta(t,0) O(t) [Theta(t,a)-Theta(t,0)] dt. This integral is finite; D_s(a)<0 for a not in Z, D_s(a)=0 exactly for a in Z, and D_s''(0)<0. This statement concerns the displayed integral alone, with no physical long-range DLR energy identification. Independent referee w536 kept precisely this scope; novelty UNKNOWN.",
          ["s>0", "The displayed integral is the definition of D_s", "No identification with an unspecified Coulomb or long-range Gibbs energy"],
          "Gaussian Fourier coefficients give Theta(t,a)-Theta(t,0)=2 sqrt(pi/t) sum_{k>=1} exp(-pi^2 k^2/t)(cos(2 pi k a)-1). Every term is nonpositive; k=1 is strictly negative for nonintegral a. Multiply by positive Theta(t,0)O(t)t^{s/2-1}/(2 Gamma(s/2)) and integrate. At t near zero the nonzero Fourier modes and their first two a-derivatives have exponential exp(-pi^2/t) decay; Theta(t,0)O(t)=O(t^-1). At infinity O(t)=O(exp(-t)) while the other factors and derivatives grow at most polynomially on a bounded period interval. Thus the integral and two derivatives converge. Theta_aa(t,0)=-8 pi^2 sqrt(pi/t) sum_{k>=1} k^2 exp(-pi^2 k^2/t)<0, proving D_s''(0)<0. Full bounds: ATTEMPT.md Lemma C; independent review: w536 REVIEW_w534.md C4.", "C4"),
    entry("sc-periodic", "simple-cubic-riesz-alternating-plane-instability",
          "Simple cubic Riesz instability under alternating-plane slides",
          "For s>3 set X_a={(m+a(n mod 2),l,n):m,l,n in Z}, with two particles per rectangular cell of volume two. Let E_s(a) be its mean per-particle Riesz pair energy with unordered pairs counted once. Then E_s(a)<E_s(0) for every nonintegral a, equality holds exactly for integral a, and E_s''(0)<0. Dilation to intensity rho>0 multiplies the energy by rho^{s/3}. This is a periodic energy result, not a positive-temperature crystalline Gibbs phase theorem. Independent referee w536 kept this statement; novelty UNKNOWN.",
          ["Repulsive potential |r|^{-s}", "s>3", "Density one before dilation", "Mean unordered-pair energy includes factor 1/2"],
          "Raw lattice pair sums converge absolutely for s>3. Even- and odd-plane particles see offsets m+a and m-a, which have equal sums after m->-m; same-parity pairs are unchanged. Therefore E_s(a)-E_s(0)=(1/2) sum_{n odd,m,l in Z}[((m+a)^2+l^2+n^2)^(-s/2)-(m^2+l^2+n^2)^(-s/2)]. The gamma integral identifies this difference with D_s(a) in the heat-relative entry. Its strict sign and equality condition follow from positive Gaussian Fourier coefficients. Differentiation gives E_s''(0)=-4 pi^2 sqrt(pi)/Gamma(s/2) integral_0^infinity t^{s/2-3/2}Theta(t,0)O(t)sum_{k>=1}k^2 exp(-pi^2 k^2/t)dt<0, with convergence as in that entry. Full proof: ATTEMPT.md Lemma A; independent review: w536 REVIEW_w534.md C2.", "C2"),
    entry("sc-compact", "force-balanced-simple-cubic-riesz-finite-support-instability",
          "Force-balanced simple cubic Riesz lattice has a finite-support instability",
          "For every s>3, the density-one simple cubic lattice Z^3 is stationary for repulsive v_s(r)=|r|^{-s} under every finitely supported displacement, yet it admits a finitely supported negative second-variation direction and arbitrarily small finite-support perturbations lowering relative unordered-pair energy while all exterior particles stay fixed. Independent referee w536 kept this result; novelty UNKNOWN. It does not prove or refute P0309's crystalline Gibbs phase target.",
          ["s>3", "Repulsive |r|^{-s}", "Relative pair energy with a fixed infinite exterior", "Displacements restricted to magnitude at most 1/4"],
          "The absolutely convergent force sum vanishes by r->-r. Put p_x=1_{x in Q_L}1_{x_3 odd}, Q_L={-L,...,L}^3, and displace x by a p_x e_1. Far-field relative energy and its Hessian converge absolutely. If h_s(r)=s[(s+2)r_1^2-|r|^2]|r|^{-s-4}, the second derivative is K_L=(1/2)sum_{r!=0}h_s(r)sum_x(p_{x+r}-p_x)^2. After division by |Q_L|, for fixed r the inner sum tends to 1 when r_3 is odd and 0 otherwise and is bounded by 2. Since sum_r |h_s(r)| is finite, dominated convergence gives K_L/|Q_L| -> (1/2)sum_{r_3 odd}h_s(r)=E_s''(0)<0 from sc-periodic. For a sufficiently large finite L, stationarity and Taylor expansion supply arbitrarily small energy-lowering finite-support displacements. Full proof: ATTEMPT.md Lemma B; independent review: w536 REVIEW_w534.md C3.", "C3"),
    entry("false-bridge", "refuted-force-balance-implies-riesz-hessian-positivity",
          "Refuted auxiliary bridge: force balance implies Hessian positivity",
          "REFUTED AUXILIARY CLAIM: every density-one periodic force-balanced configuration for the repulsive three-dimensional Riesz potential |r|^{-s}, s>3, has nonnegative second variation under every finitely supported displacement. The sc-compact entry is a counterexample: Z^3 is force balanced and has a finite-support negative second variation. This false universal bridge is distinct from P0309 and from a properly conditional harmonic calculation.",
          ["This entry records a false auxiliary statement with its counterexample", "It must not be used as a theorem"]),
    entry("stability-guard", "riesz-crystal-harmonic-stability-prerequisite",
          "Stability prerequisite for a Riesz crystal harmonic expansion",
          "Before a harmonic fluctuation calculation can support a low-temperature Riesz crystal argument, the chosen lattice must have a nonnegative displacement Hessian in the relevant directions. Force balance alone is insufficient, as the density-one simple cubic lattice has a finite-support negative second variation for every s>3. Even a valid finite infrared fluctuation integral in dimension three leaves the nonlinear control of defects, competing phases and a symmetry-breaking infinite-volume Gibbs limit open. This is a proof-route guard, not a solution of P0309.",
          ["Classical three-dimensional continuum Riesz crystal proof route", "Reference to the counterexample at s>3 only"])
]
relations = [
    {"from_key": "sc-periodic", "to_key": "heat-relative", "kind": "depends_on",
     "rationale": "The periodic entry says 'E_s(a)-E_s(0)' equals the displayed 'D_s(a)' for s>3 by absolute convergence and the gamma integral; the heat-relative entry provides strict sign and curvature for that exact integral."},
    {"from_key": "sc-compact", "to_key": "sc-periodic", "kind": "depends_on",
     "rationale": "The compact entry's 'K_L/|Q_L| -> E_s''(0)<0' uses the periodic entry's exact 'E_s''(0)<0'; its proof separately supplies force cancellation and the finite-support limit."},
    {"from_key": "sc-compact", "to_key": "false-bridge", "kind": "refutes",
     "rationale": "The bridge asserts that 'every density-one periodic force-balanced configuration ... has nonnegative second variation'; the compact entry proves that 'Z^3 is stationary ... yet it admits a finitely supported negative second-variation direction' under those same s>3 assumptions."},
    {"from_key": "stability-guard", "to_key": "sc-compact", "kind": "depends_on",
     "rationale": "The guard says 'Force balance alone is insufficient'; the compact entry supplies the exact force-balanced Z^3 counterexample with a finite-support negative second variation."},
    {"from_key": "stability-guard", "to_existing_logical": "math:probability.core:attempt-p0309-positive-temperature-crystalline-gibbs-phases-for-three-dimensional-ri", "kind": "cites",
     "rationale": "The observed canonical prior-attempt card states 'This only checks the Gaussian approximation conditional on a lattice'; the guard supplies the distinct stability prerequisite and preserves that conditional scope."},
    {"from_key": "stability-guard", "to_existing_logical": "math:probability.core:open-problem-p0309-positive-temperature-crystalline-gibbs-phases-for-three-dimensional-ri", "kind": "cites",
     "rationale": "The observed target card asks for 'existence of a crystalline Gibbs phase at sufficiently low positive temperature'; the guard explicitly leaves the symmetry-breaking infinite-volume Gibbs limit open. No refutes/proves edge to P0309 is asserted."}
]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w534",
          "bundle_slug": "p0309-simple-cubic-stability-obstruction-w534-001",
          "entries": entries, "relations": relations}

required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
keys = {item["key"] for item in entries}
assert len(keys) == len(entries)
allowed = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
for item in entries:
    assert required <= item.keys()
    assert item["source"]["license"].startswith("owner-own-work")
    assert bool(item["proof_text"]) == (item["kind"] == "lemma")
    assert len(item["statement"]) > 100
dependencies = {key: [] for key in keys}
for relation in relations:
    assert relation["from_key"] in keys and relation["kind"] in allowed
    if "to_key" in relation:
        assert relation["to_key"] in keys
        if relation["kind"] == "depends_on":
            dependencies[relation["from_key"]].append(relation["to_key"])
    else:
        assert relation["kind"] == "cites"
        assert relation["to_existing_logical"].startswith("math:probability.core:")


def visit(key, active):
    assert key not in active, "Cyclic dependency"
    for target in dependencies[key]:
        visit(target, active | {key})


for key in keys:
    visit(key, set())
complete_new_json(ROOT / "drafts/bundle_001.json", bundle)
complete_new_json(INBOX / "bundle_001.json", bundle)
assert json.loads((INBOX / "bundle_001.json").read_text(encoding="utf-8")) == bundle

hook = {
    "id": "riesz-stability-w534-01", "area": "math", "event": "PreToolUse",
    "cue": r"(?is)(?=.*(?:P0309|Riesz))(?=.*(?:force.balance|stationar))(?=.*(?:harmonic|Hessian|phonon))(?!.*(?:Hessian (?:positivity|nonnegativity|coercivity) (?:proved|verified)|independently (?:proved|verified) nonnegative Hessian))",
    "fire_when": "For a force-balanced Riesz lattice, infer a positive phonon Hessian before a harmonic crystal expansion.",
    "silent_when": "For a force-balanced Riesz lattice, Hessian positivity proved; proceed to nonlinear defect control.",
    "text": "Before treating a force-balanced Riesz lattice as a harmonic crystal, check its displacement Hessian. Force balance alone fails: simple cubic has a finite-support negative second variation for every s>3. Use w534 C3 as a boundary test.",
    "evidence": "S1.w534.C3; ATTEMPT.md Lemma B; w536/AUDITS_w534.jsonl KEEP; VERIFICATION.json rational_hessian_enclosure",
    "proposer": "w534"
}
assert len(hook["text"]) <= 300
assert re.search(hook["cue"], hook["fire_when"])
assert not re.search(hook["cue"], hook["silent_when"])
hook_text = json.dumps(hook, ensure_ascii=False) + "\n"
(ROOT / "hooks").mkdir(exist_ok=True)
(ROOT / "hooks/math-w534.jsonl").write_text(hook_text, encoding="utf-8")
(ROOT / "patches").mkdir(exist_ok=True)
(ROOT / "patches/01_riesz_stability_hook.diff").write_text(
    "--- a/~/primary_directive/hooks1000/proposals/math-w534.jsonl\n"
    "+++ b/~/primary_directive/hooks1000/proposals/math-w534.jsonl\n"
    "@@ -0,0 +1 @@\n+" + hook_text, encoding="utf-8")

source_status = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
source_status.update({
    "checked_utc": NOW, "primary_context_recovered": True,
    "exact_primary_statement_recovered": False,
    "exact_primary_statement_note": "The exact intake statement is recovered. The cited primary passage gives qualitative/numerical phase regimes, not a numbered fully quantified P0309 theorem; ATTEMPT.md labels its precise s>3 working specialization as a formalization.",
    "primary_source": {"author": "Mathieu Lewin", "title": "Coulomb and Riesz gases: The known and the unknown",
        "url": "https://arxiv.org/pdf/2202.09240v2", "version": "v2", "section": "VI",
        "printed_pages": "59-61,66-67", "pdf_zero_based_pages": "58-60,65-66",
        "phase_diagram_quote": "Existing results on the shape of the phase diagram are essentially numerical.",
        "scope": "Periodic probability laws and conjectural/numerical FCC/BCC regimes; not exact-lattice sample support."},
    "prior_attempt": {"path": "~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/brain_bundle_C006a05.json",
        "key": "at-p0309", "line": 2112, "scope": "Conditional harmonic infrared calculation; stable lattice, defects and Gibbs limit are not established."},
    "owner_solved_retired_check": {"population_store": "~/math-brain-build/local/population/brain.sqlite3",
        "mode": "sqlite read-only URI", "target_rows_found": 2,
        "truth_status": "unverified", "logical_ids": [
        "math:probability.core:open-problem-p0309-positive-temperature-crystalline-gibbs-phases-for-three-dimensional-ri",
        "math:probability.core:attempt-p0309-positive-temperature-crystalline-gibbs-phases-for-three-dimensional-ri"],
        "conclusion": "The two located canonical population cards are historical and unverified; no claim of a current solution or exhaustive retirement check."},
    "recent_primary_search": {"queries": ["site:arxiv.org Riesz gas crystallization three dimensional 2025 2026 positive temperature", "site:arxiv.org simple cubic Riesz alternating planes instability theta"],
        "conclusion": "No checked source established current resolution; a bounded negative search is not evidence of openness or novelty."},
    "independent_review": {"reviewer": "w536", "C2": "KEEP", "C3": "KEEP", "C4": "KEEP_SCOPED",
        "path": str(REVIEW), "cross_login_identity_verified": False},
    "brain_delivery_state": "submitted DRAFT; mathematics reviewed by w536; not ingested; not verified retrievable",
    "no_formal_check": True
})
write_json(ROOT / "SOURCE_STATUS.json", source_status)
write_json(ROOT / "REVIEW_RECEIPT.json", {"recorded_utc": NOW, "reviewer": "w536",
    "source": str(REVIEW), "verdicts": keeps,
    "accepted_scope_correction": "Removed common-counterterm language; C4 is the specified integral only.",
    "formal_theorem_receipt": None, "served_model_or_login_verified": False})
write_json(ROOT / "DELIVERY_STATUS.json", {"prepared": True,
    "submitted": {"state": True, "path": str(INBOX / "bundle_001.json"), "utc": NOW},
    "reviewed": {"mathematics": True, "reviewer": "w536", "claims": keeps,
                 "cross_login_admission_gate": "not certified by this worker"},
    "ingested": False, "retrievable": False,
    "entries": len(entries), "relations": len(relations),
    "hook": {"state": "staged locally for reviewer application", "path": str(ROOT / "hooks/math-w534.jsonl"),
             "target": "~/primary_directive/hooks1000/proposals/math-w534.jsonl"},
    "next": "Coordinator checks the draft/admission gate and integrates; retain C4 integral-only scope."})
write_json(ROOT / "DRAFT_VALIDATION.json", {"passed": True, "utc": NOW,
    "command": "python -B -X utf8 build_delivery.py", "entries": len(entries), "relations": len(relations),
    "licenses": "owner-own-work", "dependencies": "acyclic", "review_receipts": keeps,
    "inbox_round_trip": True, "hook_controls_passed": 2,
    "live_store_modified": False, "integration_called": False})
event = {"agent": "w534", "row": "S1.w534.C3", "utc": NOW,
         "event": "P0309 simple-cubic finite-support instability independently kept by w536; 12 scalar groups passed; 5-entry draft submitted, original Gibbs-phase gap open.",
         "evidence": str(ROOT / "REPORT.md"),
         "state": "staged locally because unrelated external writes are forbidden in this worker brief"}
write_json(ROOT / "PROGRESS_EVENT.json", event)

s6_hessian = next(row for row in VERIFICATION["rows"] if row.get("s") == 6 and row["kind"] == "rational_hessian_enclosure")
s6_energy = next(row for row in VERIFICATION["rows"] if row.get("s") == 6 and row["kind"] == "rational_energy_difference_enclosure")
s6_quad = next(row for row in VERIFICATION["rows"] if row.get("s") == 6 and row["kind"] == "independent_heat_quadrature")
report = f"""P0309 boundary result: simple cubic is force balanced but unstable for every s>3, even against arbitrarily small finite-support perturbations. The alternating-plane energy drops strictly at every nonintegral slide, with the exact equality case and negative curvature proved. This refutes force balance implying a stable harmonic crystal. P0309 is unresolved by this packet; current openness and novelty are UNKNOWN.

The recovered prior attempt had only the conditional infrared integral. The new deliverable is three boundary lemmas, independently kept by w536 (the s>0 heat-integral statement is kept only at that explicitly defined scope). The full proof, precise assumptions, prior digest and hardest remaining gap are in ATTEMPT.md. Referee evidence is in REVIEW_RECEIPT.json and the named w536 files.

Measured with `python -B -X utf8 verify_boundary.py`: {PASSED} groups passed in {VERIFICATION['cpu_seconds']:.5f} CPU seconds and {VERIFICATION['wall_seconds']:.3f} calculation wall seconds. Raw Hessian/finite-support checks cover s=4,6,12; relative heat checks additionally cover s=0.5,1,3. At s=6, the per-particle curvature is enclosed in [{s6_hessian['periodic_curvature'][0]}, {s6_hessian['periodic_curvature'][1]}], and K_32/|Q_32| in [{s6_hessian['finite_K_L_per_volume']['32'][0]}, {s6_hessian['finite_K_L_per_volume']['32'][1]}]. The independent heat calculation gives Delta_6(1/4)={s6_quad['D_s_a']:.12g}; the raw pair sum and analytic tail enclose it in [{s6_energy['bounds'][0]}, {s6_energy['bounds'][1]}]. Fresh governor gates were read before each numeric unit. The initial run refused an unrecognized permitted mode; its receipt is preserved and the label was corrected against the canonical doctrine.

`python -B -X utf8 build_delivery.py` validated and submitted math-brain-inbox/w534/bundle_001.json: five entries and six relations, all owner-own-work, acyclic dependencies, exact local relation ends, and an inbox round trip. DRAFT_VALIDATION.json also records two passing fire/silent hook controls. Submitted, reviewed, ingested and retrievable are separate in DELIVERY_STATUS.json: ingested=false and retrievable=false. This worker did not call integration or change a live store.

Apply: the validating coordinator admits and integrates the submitted DRAFT after its required checks; append hooks/math-w534.jsonl to the live proposal path named in patches/01_riesz_stability_hook.diff. The progress-page event is staged in PROGRESS_EVENT.json for the reviewer because this brief restricts unrelated external writes. Named peer handoffs used the explicitly authorized local mesh.

The material limit is scope: instability of simple cubic does not imply instability of BCC/FCC or absence of a crystalline Gibbs phase. C4 does not identify a Coulomb/DLR energy. One named referee checked the mathematics; this worker has not certified a cross-login admission gate. The hardest remaining P0309 gap is uniform nonlinear free-energy/order control of a stable phase, its defects and competing configurations through the thermodynamic limit.

NEXT: Coordinator checks the DRAFT/admission gate and integrates the reviewed boundary cards; the next proof route needs a stable BCC/FCC nonlinear free-energy estimate, not another simple-cubic calculation.
"""
(ROOT / "REPORT.md").write_text(report, encoding="utf-8")
print(json.dumps({"bundle_path": str(INBOX / "bundle_001.json"), "entries": len(entries),
                  "relations": len(relations), "numeric_groups_passed": PASSED,
                  "mathematical_review": keeps, "ingested": False, "retrievable": False}, indent=2))
