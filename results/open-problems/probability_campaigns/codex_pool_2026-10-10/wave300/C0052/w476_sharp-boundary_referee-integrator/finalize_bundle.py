"""Produce the nonduplicative, concept-only C0052 draft from local reviewed rows."""

import json
from pathlib import Path


root = Path(__file__).resolve().parent
path = root / "bundle_001.json"
bundle = json.loads(path.read_text(encoding="utf-8"))
source = bundle["entries"][0]
source["title"] = "DRAFT: exact source quantifiers for C0052"
source["statement"] = (
    "DRAFT source correction, not a solution. For zero-field nearest-neighbor ferromagnetic "
    "Ising on Z^3, Duminil-Copin's Conjecture 6 defines g_3(beta)="
    "sum_{x2,x3,x4} U4(0,x2,x3,x4)/(chi(beta)^2 xi(beta)^3) using the "
    "subcritical free infinite-volume state. It calls the model nontrivial when g_3(beta) "
    "does not tend to zero as beta increases to beta_c. Since U4<=0, this asks for a "
    "sequence beta_n increasing to beta_c with -g_3(beta_n)>=epsilon for some epsilon>0. "
    "A positive full liminf or non-Gaussianity of every subsequential scaling field is a "
    "stronger quantified route. Current 2026 openness is UNKNOWN in this packet."
)
sign_boundary = {
    "key": "associated-sign-gaussian-boundary",
    "namespace": "probability.statmech",
    "logical_name": "associated-gaussian-sign-field-with-gaussian-power-law-limit",
    "kind": "concept",
    "title": "DRAFT: associated spin field with anomalous power-law covariance and Gaussian limit",
    "statement": (
        "DRAFT scoped boundary result; written proof independently checked by w476, "
        "served-model diversity gate pending. For each 0<gamma<3, take a stationary unit-variance "
        "Gaussian field G on Z^3 with covariance R_gamma(z)=(1+|z|^2)^(-gamma/2), and "
        "set sigma_x=sign(G_x). The bounded spin field is stationary, spin-flip symmetric, "
        "positively associated, has two-point covariance (2/pi)arcsin R_gamma(z) "
        "asymptotic to (2/pi)|z|^(-gamma), and has on-site fourth cumulant -2. Yet for "
        "each finite list of compactly supported smooth tests f, the normalized sums "
        "N^(-3+gamma/2) sum_x f(x/N)sigma_x converge jointly to a centered Gaussian vector "
        "with covariance (2/pi) double_integral f(u)h(v)|u-v|^(-gamma) du dv. "
        "This refutes only a proposed implication from association, anomalous two-point "
        "decay and a local fourth cumulant to non-Gaussian smeared limits. The field is "
        "not shown to be a nearest-neighbor Ising Gibbs state or to satisfy random-current identities."
    ),
    "proof_text": None,
    "assumptions": [
        "fixed gamma in (0,3)",
        "specified sign-Gaussian construction",
        "finite list of fixed compactly supported smooth tests",
        "finite-dimensional smeared convergence only"
    ],
    "domain": "probability theory; statistical mechanics",
    "source": {
        "source_id": "owner-own-work:w474:C0052-boundary-2026-10-10; referee w476.R7-R8",
        "url": "file:///~/brain_workers/w474/ATTEMPT.md",
        "revision": "author proof 2026-10-10; independent mathematical check ~/brain_workers/w476/REVIEW.jsonl; model gate pending",
        "license": "owner-own-work",
        "excerpt": None
    }
}
bundle["entries"] = [source, sign_boundary]
bundle["relations"] = [
    {
        "from_key": "c0052-source-target",
        "to_existing_logical": "math:probability.statmech:open-problem-c0052-non-triviality-of-the-scaling-limit-of-the-three-dimensional-ising-mod",
        "kind": "semantic_association",
        "rationale": "This concept records the primary source's precise signed-coupling quantifiers for the existing C0052 open-problem card, without a solved claim."
    },
    {
        "from_key": "associated-sign-gaussian-boundary",
        "to_key": "c0052-source-target",
        "kind": "semantic_association",
        "rationale": "The associated sign field blocks a broader proposed Gaussianity implication, while lacking the nearest-neighbor Ising and random-current assumptions of C0052."
    }
]
path.write_text(json.dumps(bundle, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"entries={len(bundle['entries'])} relations={len(bundle['relations'])}")
