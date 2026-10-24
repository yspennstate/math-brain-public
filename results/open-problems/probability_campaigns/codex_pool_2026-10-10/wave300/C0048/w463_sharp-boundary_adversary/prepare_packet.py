"""Prepare immutable mathematical deliverables locally; no live integration."""
from pathlib import Path
import difflib
import hashlib
import json

root = Path(__file__).resolve().parent


def write_json(name, obj):
    (root/name).write_text(json.dumps(obj, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")


primary = "https://www.math.ucla.edu/~lchayes/lchayes_website_folder/old_publications_folder/bc_mft.pdf"
source_status = {
    "candidate_id": "C0048", "checked_date": "2026-10-10", "current_openness": "UNKNOWN", "novelty_claim": False,
    "exact_statement": "For every integer q>=3 and integer d>=3, the standard zero-field nearest-neighbor ferromagnetic Potts model on Z^d has positive color-boundary spontaneous magnetization at its first critical inverse temperature.",
    "convention": "Weight exp(beta sum_edges 1{sigma_x=sigma_y}); M(beta)=(q*mu_beta^1(sigma_0=1)-1)/(q-1), beta_c=inf{beta:M(beta)>0}. The target is M(beta_c)>0, equivalently phi^wired_{p_c,q}(0 connected by ordinary edges to infinity)>0, with p=1-exp(-beta).",
    "normalization_warning": "Biskup-Chayes use J=2*d*beta in the delta-spin convention and their rescaled spin inner product has kappa=(q-1)/q. This packet uses their probability-vector F_J. Lecture unit-spin conventions rescale beta.",
    "primary_sources": [
        {"source_id": "duminil_copin_ising_potts_2017", "url": "https://arxiv.org/abs/1707.00520", "read_url": "https://www.ihes.fr/~duminil/publi/2017PIMS.pdf", "locator": "Conjecture 2, printed p.93; critical magnetization definition, printed p.5", "historical_status": "source calls it a conjecture", "intake_reported_pdf_sha256": "cc442344d0cc21c5d57163719b06dfaf1d243dee8731716bf89d21c593f98a5b", "hash_verification": "intake-reported only; not a new source-hash check"},
        {"source_id": "biskup_chayes_2003", "url": primary, "arxiv": "https://arxiv.org/abs/math/0207242", "doi": "10.1007/s00220-003-0828-2", "locators": ["Main Theorem (1.12)-(1.13)", "Potts normalization (2.3),(2.7)", "Theorem 2.1 and following paragraph", "proof of Theorem 2.1: delta_d=(q-1)^2 I_d/(2q)"], "scope": "fixed integer q>=3, sufficiently large d; cited theorem alone does not identify J_t=J_c"},
        {"url": "https://journals.aps.org/prb/abstract/10.1103/x1qn-x6xb", "date": "2025-07-24", "role": "recent primary finite-size/fuzzy-sphere evidence; different quantum regularization, not a proof of the classical nearest-neighbor universal target"}
    ],
    "prior_work": {"recovered": "C0048-A001 in probability_1000_intake_claude_20260907/attempts.jsonl line 38; no result", "targeted_negative_searches": ["probability_1000_attempts_H_20260912", "probability_1000_attempts_I_20260914", "prob1000_lean_20260908", "intake_H_20260914", "intake_I_20260914", "named Potts/C0048 filenames in Big Open problem in probability theory"], "team_O": "targeted board search found no C0048 lane", "retirement_certificate": "NOT established; no owner-wide search performed"},
    "store_check": {"receipt": str(root/"STORE_SOURCE_REPORT.json"), "read_only": True, "matching_ids": ["claim_38c945c83e6d9f9dc77b20f936b660e811e528c284f76bd513990e6ed06ecc6a", "claim_9830d2b5c32b82afa88de780611e6b0fe5e81b7d425ff5fabff71dad19cc6930"], "interpretation": "matching problem and prior-attempt nodes, not a proof or exhaustive solved/retired certificate"},
    "status_search_limits": "Targeted public primary searches did not locate a rigorous full-target solution; a search miss cannot certify current openness.",
    "brain_scar": "perceptron_proof_open_gaps_fleet_2026_07_12", "recall_receipt": str(root/"RECALL_REPORT.json"),
}
write_json("SOURCE_STATUS.json", source_status)

peer = Path("~/brain_workers/w462/ATTEMPT.md")
peer_bytes = peer.read_bytes()
peer_hash = hashlib.sha256(peer_bytes).hexdigest()
(root/"review").mkdir(exist_ok=True)
(root/"review/w462_ATTEMPT_reviewed.md").write_bytes(peer_bytes)
audits = [
    {"id": "w463-audit-w462-L1", "verdict": "KEEP", "status": "independently checked proof", "statement": "For finite FK with arbitrary boundary partition, 0<p<1, q>=1 and pairwise disjoint nonempty edge sets C_i, P(all C_i have an open edge)<=product_i[1-(1-p)^|C_i|].", "assumptions": ["q>=1", "pairwise disjoint C_i", "finite graph", "uniform full-conditional closed-edge lower bound"], "source_quote": "The same bound holds after conditioning on any positive-probability event measurable without e", "why": "Independently rederived the full conditional formula p or p/(p+q(1-p)); tower conditioning preserves closed>=1-p. Every prefix event is measurable outside the next C_i, so the chain rule is valid. No independence is used. Exact controls below show the assumptions matter.", "remaining_gap": "None identified in this scoped inequality; this is not the parent critical-ordering lower bound."},
    {"id": "w463-audit-w462-L2", "verdict": "KEEP", "status": "independently checked proof", "statement": "For G=Z Cartesian-product H with finite connected H of m vertices, q>=1 and p<1, ordinary crossing probabilities are bounded by [1-(1-p)^m]^n; all ordinary infinite clusters are absent. Integer-q color-boundary magnetization vanishes at every finite beta.", "assumptions": ["finite cross-section H", "ordinary open paths", "cuts contained in the finite volume", "q>=1", "integer q>=2 for Potts coloring"], "source_quote": "all ordinary open clusters are finite for every p<1", "why": "Each physical path must cross every longitudinal cut; the pairwise disjoint cutsets permit L1. An infinite cluster leaves each finite interval, giving the two-end union bound. Wired identifications do not create an ordinary crossing. Edwards-Sokal boundary connection is an ordinary path to at least one physical end.", "remaining_gap": "No claim of free-energy analyticity or of behavior on Z^3 is being audited."},
    {"id": "w463-audit-w462-L3", "verdict": "KEEP", "status": "independently checked proof", "statement": "Z Cartesian-product K5 is simple, connected, transitive, six-regular and amenable, but its q=3 Potts model has no finite-temperature spontaneous magnetization.", "assumptions": ["the graph is Z x K5, not Z^3", "standard finite-coupling ferromagnetic Potts model"], "source_quote": "This refutes the stronger hypothetical bridge", "why": "Degree is 2+4=6; interval fibers have 5(2n+1) vertices and 10 outgoing edges. L2 applies. The example fails pc<1 and has linear growth, so it does not refute bridges with those additional hypotheses or the original target.", "remaining_gap": "Critical wired ordering on the actual Z^3 lattice remains unproved."}
]
with (root/"PEER_AUDIT.jsonl").open("w", encoding="utf-8") as stream:
    for audit in audits:
        audit.update({"author": "w462", "independent_reviewer": "w463", "source": str(peer), "source_snapshot": str(root/"review/w462_ATTEMPT_reviewed.md"), "scoped_sections": ["L1", "L2", "L3"], "source_sha256": peer_hash, "review_gate": "mathematical KEEP only; account and served-model independence not established; w464 review still required"})
        stream.write(json.dumps(audit, ensure_ascii=False)+"\n")

audit_text = f"""# Independent audit of w462's C0048 packet

Auditor w463; 2026-10-10. Audited author proof: {peer}. SHA-256 at review: {peer_hash}. The independent minimax derivation in this worker's ATTEMPT.md was saved before the paired proof was opened. This reviews the author's proof, not a review of it.

KEEP L1, L2 and L3 with exactly their saved assumptions. L1 correctly conditions each factor on earlier events. Uniform conditional closure survives partial conditioning by the tower property; disjointness makes the prefix measurable outside the next block. The finite-volume inequality is uniform in boundary partition and passes to finite cylinder events in a weak limit. L2 uses ordinary physical paths and a finite-width cross-section. Boundary coloring only needs an ordinary path to either physical end, even when those ends are wired together. L3 checks degree, transitivity and the explicit amenability ratio and clearly distinguishes the strip from Z^3.

Three necessary qualifiers have exact failure controls, checked by python -X utf8 check_peer_bound.py:

* Disjointness: at q=1,p=1/2, counting the same one-edge set twice gives actual intersection 1/2 but the proposed product 1/4.
* q>=1: on a free one-edge graph at q=p=1/2 the open probability is 2/3, above the putative upper bound p=1/2.
* Ordinary paths: on -1--0--1--2 with end vertices wired, at q=3,p=1/2 the ordinary right-crossing probability is 1/11, while wired connectivity to the right end is 7/22>1/4. The ordinary two-cut upper bound is 1/4. A proof silently replacing ordinary crossing by wired connectivity would fail.

The same eight-state q=3 calculation gives P(A1 intersection A2)=3/22>P(A1)P(A2)=15/121 for A1=left edge open and A2=at least one right edge open. Thus multiplying unconditioned marginal upper bounds really fails, while w462's uniform conditional bound, 3/8, remains valid. At q=1 the disjoint-block bound is attained exactly.

These controls do not refute any of w462's properly scoped lemmas. They delimit what can safely enter the brain. The hardest remaining gap is theta^wired(pc,3)>0 on Z^3; none of these upper bounds supplies it. This mathematical KEEP is separate from account/served-model/different-model admission gates, for which response-side evidence is unavailable here. No formal proof receipt is claimed.

NEXT: w464 independently check w463's exact full-simplex barrier and the source normalization; retain the ordinary-path and disjointness qualifiers in every recall card.
"""
(root/"PEER_AUDIT.md").write_text(audit_text, encoding="utf-8")

namespace = "probability.statistical-mechanics"
entries = []
definitions = [
    ("minimax", "potts-three-state-mean-field-minimax-barrier-draft", "Draft: exact three-state mean-field minimax barrier", "AUTHOR PROOF; INDEPENDENT REVIEW PENDING. For S={x_i>=0,sum x_i=1}, F_J(x)=sum x_i log x_i-(J/2)sum x_i^2 (0 log 0=0), and J0=4 log 2, the global minimizers are u=(1/3,1/3,1/3) and permutations of v=(2/3,1/6,1/6). The infimum over continuous paths u to v of their maximum F_J0 excess above the global minimum is exactly Delta=log 3-(19/12)log 2>0, attained via (1/2,1/4,1/4). This is a mean-field auxiliary result; C0048 and novelty remain unverified.", ["q=3 mean-field simplex", "natural logarithms", "continuous full-simplex paths"]),
    ("interpolation", "potts-approximate-minimizer-continuous-interpolation-draft", "Draft: sharp obstruction to an approximation-only jump bridge", "AUTHOR PROOF; INDEPENDENT REVIEW PENDING. Let S={x_i>=0,sum_{i=1}^3 x_i=1}, F_J(x)=sum x_i log x_i-(J/2)sum x_i^2 with 0 log 0=0, J0=4 log 2, u=(1/3,1/3,1/3), v=(2/3,1/6,1/6), and Delta=log 3-(19/12)log 2. The sublevel {F_J0<=min_S F_J0+epsilon} contains a continuous path u to v iff epsilon>=Delta. For every epsilon>Delta, choose 0<h<min(J0,3(epsilon-Delta)); x(m)=((1+2m)/3,(1-m)/3,(1-m)/3) with m(J) linear from 0 to 1/2 across [J0-h,J0+h] obeys F_J(x(m(J)))-min_S F_J<=Delta+|J-J0|/3<epsilon continuously. This inequality alone cannot force a jump. The selector is not asserted to be a lattice Gibbs magnetization.", ["q=3 mean-field simplex", "natural logarithms", "epsilon>Delta for interval interpolation"]),
    ("allowance", "potts-biskup-chayes-coarse-error-barrier-gate-draft", "Draft: normalized error obstruction for the q=3 mean-field route", "AUTHOR DERIVATION; INDEPENDENT REVIEW PENDING. In Biskup-Chayes Main Theorem (1.12), the q=3 rescaled Potts inner product gives n=2,kappa=2/3 and allowance E_d(J0)=(2J0/3)I_d, where J0=4 log 2, a(k)=d^(-1)sum cos(k_j), and I_d=integral a^2/(1-a) under normalized torus measure. For integer d>=3, symmetry gives I_d>=1/(2d). Hence E_3(J0)>=4 log 2/9, more than 272.8 times Delta=log 3-(19/12)log 2. E_d(J0)<Delta is impossible for d<=818; d=819 passing this necessary lower-bound test is not sufficient. This bounds a theorem allowance, not actual Gibbs error or the lattice dimension at which discontinuity begins.", ["integer d>=3", "q=3", "unmodified Main Theorem allowance", "probability-vector normalization F_J=sum x_i log x_i-(J/2)sum x_i^2"]),
    ("critical-scope", "potts-mean-field-jump-first-critical-point-premise-draft", "Draft: a jump location needs identification with the first critical point", "SOURCE-SCOPE DRAFT; INDEPENDENT REVIEW PENDING. C0048 asks for positive color-boundary spontaneous magnetization at the first critical point of the standard nearest-neighbor zero-field Potts model on Z^d for every integer q>=3,d>=3. The cited Biskup-Chayes Theorem 2.1 proves a jump at J_t near J_MF in sufficiently large d, while its following paragraph explicitly does not establish m_*(J)=0 for every J<J_t. Invoking that theorem alone requires an additional argument identifying J_t=J_c to obtain the first-critical-point claim. This does not assess other large-d results; current C0048 openness is UNKNOWN.", ["exact conclusion of Biskup-Chayes Theorem 2.1", "C0048 uses critical spontaneous magnetization, not arbitrary secondary jumps"]),
]
for key, logical, title, statement, assumptions in definitions:
    entries.append({"key": key, "namespace": namespace, "logical_name": logical, "kind": "concept", "title": title, "statement": statement, "proof_text": None, "assumptions": assumptions, "domain": "probability theory", "source": {"source_id": "owner-own-work:w463:C0048-"+key+"-20261010", "url": (root/"ATTEMPT.md").as_uri(), "revision": "author-draft-2026-10-10; w464 review pending", "license": "owner-own-work (campaign proof and route audit; primary sources attributed in SOURCE_STATUS.json)", "excerpt": None}})
relations = [
    {"from_key": "interpolation", "to_key": "minimax", "kind": "depends_on", "rationale": "The exact minimax barrier proves both the absence below Delta and the explicit connecting path at Delta."},
    {"from_key": "allowance", "to_key": "minimax", "kind": "depends_on", "rationale": "The normalized Biskup-Chayes allowance is compared with the exact Delta separating the three-state mean-field minima."},
    {"from_key": "critical-scope", "to_key": "allowance", "kind": "semantic_association", "rationale": "Both delimit what the same mean-field theorem can certify: error size and identification of the jump with first criticality are separate missing inputs."},
]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w463", "bundle_slug": "c0048-three-state-minimax-route-boundary-draft-20261010", "entries": entries, "relations": relations}
(root/"drafts").mkdir(exist_ok=True)
write_json("drafts/bundle_001.json", bundle)
with (root/"RELATIONS_EVIDENCE.jsonl").open("w", encoding="utf-8") as stream:
    keyed = {entry["key"]: entry for entry in entries}
    for relation in relations:
        stream.write(json.dumps({**relation, "from_statement_quote": keyed[relation["from_key"]]["statement"], "to_statement_quote": keyed[relation["to_key"]]["statement"], "status": "draft; review pending"}, ensure_ascii=False)+"\n")

(root/"hooks").mkdir(exist_ok=True)
hook = {"id": "c0048-w463-01", "area": "math", "event": "stage-start", "cue": "A nearest-neighbor Potts proof transfers a mean-field jump to q=3,d=3 using an approximate-minimizer allowance.", "fire_when": "A proposed q=3 lattice jump uses the Biskup-Chayes error bound without comparing it with a separating barrier in the same spin normalization.", "silent_when": "The text reports only a mean-field special case, or explicitly verifies a smaller allowance and supplies the critical-point identification.", "text": "Mean-field jump transfer needs an error smaller than its separating barrier, in the same normalization. For q=3, Delta=log(3)-19log(2)/12 is tiny; the coarse d=3 allowance is >272.8 Delta. A jump at Jt also needs Jt=Jc for C0048.", "evidence": "~/brain_workers/w463/ATTEMPT.md Claims A/B and normalized allowance; MEASUREMENTS.json", "proposer": "w463"}
assert len(hook["text"]) <= 300
(root/"hooks/c0048-w463.jsonl").write_text(json.dumps(hook)+"\n", encoding="utf-8")

(root/"patches").mkdir(exist_ok=True)
live_relative = "06_math_research/C0048_sharp_mean_field_barrier_w463_20261010.md"
note = (root/"ATTEMPT.md").read_text(encoding="utf-8")
patch = "".join(difflib.unified_diff([], note.splitlines(keepends=True), fromfile="a/"+live_relative, tofile="b/"+live_relative))
(root/"patches/01_C0048_minimax_note.diff").write_text(patch, encoding="utf-8", newline="\n")
(root/"patch_check").mkdir(exist_ok=True)
write_json("DRAFT_LIFECYCLE.json", {"prepared": True, "submitted": False, "reviewed": False, "ingested": "not observed", "retrievable": "not verified", "coordinator": "codex-01a12190", "independent_referee": "w464", "draft_path": str(root/"drafts/bundle_001.json"), "promotion": "concept/draft only until proof and independent review gates pass"})

report = """C0048 is review-ready as a bounded mathematical contribution. Its exact target is positive critical magnetization for every integer q>=3,d>=3 on the standard nearest-neighbor lattice. Current openness and novelty remain UNKNOWN. The old C0048-A001 attempt supplied a qualitative contour obstruction; this packet supplies an exact sharp mean-field error threshold, without a parent-problem solved claim.

The independent proof gives Delta=log(3)-19log(2)/12=0.001129252781529618... as the full-simplex minimax barrier at J0=4log(2). Continuous approximate minimizers exist at or above that barrier. With the primary theorem's actual n=2,kappa=2/3 normalization, its d=3 allowance is at least 0.3080654135821979, or 272.8046533 times Delta. Exact integer arithmetic excludes d<=818 for this particular coarse-error criterion; 819 is a necessary-condition cutoff, not a sufficient dimension or a lattice phase threshold. The source audit separately identifies the missing J_t=J_c premise in invoking Theorem 2.1 alone.

Validation: python -X utf8 check_barrier.py passed 2001 path and 2001 separating-section arithmetic checks plus the exact integer comparisons. The analytic proof, rather than sampling, establishes the general minimax statement. python -X utf8 check_peer_bound.py checked 16 finite FK configurations exactly with fractions and produced overlap, q<1 and wired-path failure controls. w462's L1/L2/L3 received scoped mathematical KEEP; their uniform conditioning is sound. Review and served-model/account admission gates remain distinct and pending. Source and store checks were targeted; SQLite was read-only.

The draft holds four review-pending concept cards and three supported relations. No live store or recall control was changed, and no recall-performance gain is claimed. A wrong spin normalization, treating an allowance as actual error, or promoting a secondary jump to critical ordering would invalidate the intended inference. w464 should check the full-simplex lower bound, norm perturbation and normalized source allowance before promotion.

Reviewer application of the optional knowledge-note diff: git -C ~/<private-repo> apply ~/brain_workers/w463/patches/01_C0048_minimax_note.diff . The live target is 06_math_research/C0048_sharp_mean_field_barrier_w463_20261010.md. Alternatively integrate only the concept draft through the validating coordinator; do not run live integration from this worker. The hook and progress event are prepared locally under the worker-folder restriction.

NEXT: w464 independently review Claims A/B/C and the critical-point source qualifier; keep the parent Z^3,q=3 ordering gap explicit.
"""
(root/"REPORT.md").write_text(report, encoding="utf-8")
write_json("PROGRESS_EVENT.json", {"agent": "w463", "row": "S1.C0048", "event": "C0048: exact q=3 mean-field minimax barrier and normalized 272.8x error obstruction saved; scoped KEEP on w462 cutset/strip proof; review pending", "evidence": str(root/"REPORT.md"), "publication": "prepared locally; coordinator may post under worker-folder restriction"})
print(json.dumps({"prepared_entries": len(entries), "supported_relations": len(relations), "peer_math_KEEPS": len(audits), "peer_sha256": peer_hash, "report": str(root/"REPORT.md")}, indent=2))
