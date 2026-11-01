"""Prepare and validate a task-authorized DRAFT; never invoke the live integrator."""
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

folder = Path(__file__).resolve().parent
claims = [json.loads(x) for x in (folder / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if x]
names = {
    "C1": ("translation-obstruction", "fixed-lattice-defect-coercivity-translation-obstruction", "Translation obstructs a fixed-lattice defect penalty"),
    "C2": ("acoustic-obstruction", "mean-zero-acoustic-mode-coercivity-obstruction", "Mean-zero acoustic modes have no volume-uniform displacement gap"),
    "C3": ("fourier-reduction", "lattice-matching-displacement-fourier-order-reduction", "Matching and displacement bounds imply finite-volume Fourier order"),
    "C4": ("vacancy-obstruction", "soft-short-range-riesz-dlr-vacancy-bound", "Soft short-range Gibbs laws allow vacancies in every bounded region"),
    "C5": ("harmonic-control", "three-dimensional-discrete-harmonic-displacement-bound", "Uniform displacement variance in cubic harmonic elasticity"),
    "C6": ("entropy-obstruction", "extensive-energy-gap-defect-entropy-counterexample", "An extensive energy gap alone does not suppress Gibbs defects"),
    "C7": ("repair-comparison", "continuum-defect-repair-energy-jacobian-comparison", "A continuum defect comparison needs energy and measure control"),
    "C8": ("rigid-repair-obstruction", "rigid-template-continuum-repair-null-image-obstruction", "Exact rigid repairs collapse continuum configuration volume")
}

def source(logical):
    return {"source_id": "owner-own-work:" + logical, "url": "urn:mathbrain:owner-own-work:" + logical,
            "revision": "draft-2026-10-10-v1", "license": "owner-own-work", "excerpt": None}

entries = []
for row in claims:
    suffix = row["claim_id"].rsplit("-", 1)[-1]
    key, logical, title = names[suffix]
    checked = row["status"] == "independently checked proof"
    statement = row["exact_statement"]
    if not checked:
        statement = "DRAFT concept; independent review pending. " + statement
    statement += " Scope: " + row["remaining_gap"]
    entries.append({"key": key, "namespace": "probability.gibbs", "logical_name": logical,
        "kind": "lemma" if checked else "concept", "title": title if checked else "Draft: " + title,
        "statement": statement, "proof_text": row["proof_or_counterexample"] if checked else None,
        "assumptions": row["assumptions"], "domain": "probability and mathematical statistical mechanics",
        "source": source(logical)})

logical = "unrestricted-riesz-crystal-reconstruction-proof-obligation"
entries.append({"key": "reconstruction-obligation", "namespace": "probability.gibbs", "logical_name": logical,
    "kind": "concept", "title": "Draft: unrestricted crystalline reconstruction for neutral Riesz gas",
    "statement": "UNPROVED INPUT for a chosen contour route. In dimension three fix 0<s<3, density rho>0, finite inverse temperature beta>0 and a neutral canonical Riesz jellium container with N=rho times its volume. To extend a phase-selected lattice calculation to the unrestricted gas, construct admissible same-N continuum defect repairs with volume-uniform positive energy gain per contour size and an exponential bound on the repaired reference-measure density. Include the actual exterior/background energy and dipole sector; retain full-dimensional configuration volume. Separately derive small phase-fitted mismatch/displacement moments, an unperturbed infinite-volume Gibbs limit, and a stated positional-order criterion. Compact dipole-free interaction estimates and harmonic variance bounds do not establish these inputs. No solution or novelty is claimed.",
    "proof_text": None,
    "assumptions": ["Chosen long-range neutral canonical subtarget, not a fully quantified interpretation of every Riesz exponent", "Unrestricted continuum configurations", "No proved reconstruction premise is supplied"],
    "domain": "probability and mathematical statistical mechanics", "source": source(logical)})

relations = [
    {"from_key": "reconstruction-obligation", "to_key": "repair-comparison", "kind": "depends_on", "rationale": "The chosen contour route requires a valid energy and reference-measure comparison; C7 gives one sufficient conditional form."},
    {"from_key": "reconstruction-obligation", "to_key": "fourier-reduction", "kind": "depends_on", "rationale": "This route uses an explicit matching/displacement-to-Fourier implication after deriving its hypotheses; the Gibbs limit and full phase periodicity remain separate."},
    {"from_key": "harmonic-control", "to_key": "reconstruction-obligation", "kind": "analogous_to", "rationale": "The exactly quadratic displacement bound illustrates the desired phonon control but proves none of the unrestricted Riesz defect hypotheses."},
    {"from_key": "acoustic-obstruction", "to_key": "harmonic-control", "kind": "semantic_association", "rationale": "Both concern the same cubic harmonic operator: its smallest nonzero eigenvalue vanishes while its normalized inverse trace stays bounded."},
    {"from_key": "entropy-obstruction", "to_key": "repair-comparison", "kind": "semantic_association", "rationale": "The two-sector counterexample demonstrates why energy control alone cannot replace multiplicity/Jacobian or equivalent reference-measure control."},
    {"from_key": "rigid-repair-obstruction", "to_key": "repair-comparison", "kind": "semantic_association", "rationale": "An exact rigid-template map has null image and cannot satisfy the comparison's positive Jacobian premise on a positive-volume domain."},
    {"from_key": "translation-obstruction", "to_key": "fourier-reduction", "kind": "semantic_association", "rationale": "A global phase must be accounted for before counting absolute lattice deviations; the Fourier reduction explicitly registers this phase."}
]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w529", "bundle_slug": "riesz-crystal-repair-entropy-audit-20261010", "entries": entries, "relations": relations}

allowed_kinds = {"definition", "lemma", "theorem", "concept"}
allowed_relations = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
keys = {e["key"] for e in entries}
assert len(entries) <= 200 and len(keys) == len(entries)
for entry in entries:
    assert entry["kind"] in allowed_kinds
    assert entry["source"]["license"].startswith("owner-own-work")
    assert (bool(entry["proof_text"]) if entry["kind"] in {"lemma", "theorem"} else entry["proof_text"] is None)
    assert not any(bad in entry["statement"] for bad in ("C:/", "C:\\", "w529", "owner-probability-campaign", "private campaign"))
for relation in relations:
    assert relation["from_key"] in keys and relation["to_key"] in keys
    assert relation["kind"] in allowed_relations and relation["rationale"]
graph = {k: [] for k in keys}
for relation in relations:
    if relation["kind"] == "depends_on":
        graph[relation["from_key"]].append(relation["to_key"])
def visit(key, active, finished):
    assert key not in active, "cyclic depends_on relation"
    if key in finished:
        return
    active.add(key)
    for target in graph[key]:
        visit(target, active, finished)
    active.remove(key)
    finished.add(key)
finished = set()
for key in keys:
    visit(key, set(), finished)

payload = json.dumps(bundle, ensure_ascii=False, indent=2) + "\n"
json.loads(payload)
(folder / "bundle_001.json").write_text(payload, encoding="utf-8")
inbox = Path("~/math-brain-inbox/w529")
number = 1
while (inbox / f"bundle_{number:03}.json").exists() or (inbox / f"bundle_{number:03}.part").exists():
    number += 1
dest = inbox / f"bundle_{number:03}.json"
claim_args = ["python", "-X", "utf8", "~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py", "claim", "--agent", "w529", "--resource", "file:" + dest.as_posix(), "--mode", "write", "--purpose", "P0309 DRAFT reconstruction audit, this worker bundle only", "--ttl", "45m"]
claim = subprocess.run(claim_args, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
(folder / "BUNDLE_CLAIM_RECEIPT.json").write_text(json.dumps({"returncode": claim.returncode, "stdout": claim.stdout, "stderr": claim.stderr}, indent=2), encoding="utf-8")
if claim.returncode != 0:
    raise RuntimeError("Narrow bundle claim failed; local validated bundle preserved; no inbox mutation")
inbox.mkdir(parents=True, exist_ok=True)
part = dest.with_suffix(".part")
with part.open("x", encoding="utf-8") as stream:
    stream.write(payload)
part.rename(dest)
receipt = {"spec": "mathbrain-draft-v1", "entries": len(entries), "relations": len(relations), "lemmas": sum(e["kind"] == "lemma" for e in entries), "draft_concepts": sum(e["kind"] == "concept" for e in entries), "local_validation": "passed", "source_tag": "owner-own-work", "dependency_graph": "acyclic", "submitted": {"state": True, "path": str(dest), "timestamp_utc": datetime.now(timezone.utc).isoformat()}, "reviewed": {"complete": False, "checked_claims": [r["claim_id"] for r in claims if r["status"] == "independently checked proof"]}, "ingested": {"state": False, "reason": "Coordinator only; no live integrator invoked"}, "retrievable": {"state": False, "reason": "Not ingested or queried from the live store"}, "formal_check": None, "live_brain_improvement_measured": False}
(folder / "BUNDLE_STATE.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))
