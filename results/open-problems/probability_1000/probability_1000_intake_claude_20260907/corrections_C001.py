"""Corrections to the Claude intake ledger from the Codex holder's four review messages (10:53, 11:15, 12:02, 12:12
his clock, 2026-09-07), each checked by the Fable agent before landing. Appends superseding attempt rows (A002) and
marks the superseded A001 rows in place; flips two problems to resolved/refuted status in place with resolved_by."""
import json
from intake_tools import append, now, HERE

P = HERE / "problems.jsonl"; A = HERE / "attempts.jsonl"
CORR = {
 "C0002": ("Codex review 10:53: the Gaussian tail carries a 1/sqrt(log N) factor.",
  "CORRECTION of C0002-A001. With Var h_x = g log N + O(1) and threshold 2 sqrt(g) lambda log N, P(h_x >= threshold) = exp(-2 lambda^2 log N)/(sqrt(2 pi) 2 lambda sqrt(log N)) (1 + o(1)), so the mean size of the intermediate level set is of order N^{2 - 2 lambda^2}/sqrt(log N), not a constant times N^{2(1 - lambda^2)} as A001 wrote; the (log N)^{-1/2} is the leading normalisation, not a correction term. The rest of A001 (variance dominated by mesoscopic pairs, mixing-measure identification open) stands with this normalisation.",
  "E|level set| = c N^{2-2 lambda^2} (log N)^{-1/2} (1+o(1)) with c = 1/(2 sqrt(2 pi) lambda) times the boundary-correction factor."),
 "C0004": ("Codex review 10:53: ratio-of-expectations equality does not need a constant total mass.",
  "CORRECTION of C0004-A001. The sentence 'the naive guess rho^D proportional to r_D(x)^2 fails unless Z^D(D) is a.s. constant' is too strong: if Z^D = xi mu with xi a random scalar and mu deterministic, then Z^D(dx)/Z^D(D) = mu(dx)/mu(D) is deterministic and E[Z^D(dx)/Z^D(D)] = E Z^D(dx)/E Z^D(D) although Z^D(D) is random. The correct statement: rho^D differs from the normalised intensity E Z^D(dx)/E Z^D(D) exactly when the total mass Z^D(D) is not independent of the normalised measure Z^D(dx)/Z^D(D); for the DGFF extremal measure this independence fails (the mass and the shape are coupled through the Gibbs-Markov structure), so rho^D is not r_D(x)^2 dx normalised, but the argument in A001 does not prove that and the question stands.",
  "rho^D = E[Z(dx)/Z(D)] equals E Z(dx)/E Z(D) iff the total mass is independent of the normalised measure (sufficient direction), not iff the mass is constant."),
 "C0033": ("Codex review 11:15: finite-kernel concavity implies stationary entropy concavity; it is not an equivalence.",
  "CORRECTION of C0033-A001 and of the problem statement's 'equivalently': Lyons's Conjecture 2.6 (finite positive contractions) implies Conjecture 5.3 (stationary processes on Z, concavity of the entropy rate in the symbol) by taking limits of finite restrictions, but the converse is not claimed and is not known; the two are recorded as implication, not equivalence. The numerical evidence (1440 random pairs, no violation) is for Conjecture 2.6 only.",
  "Conjecture 2.6 (finite) => Conjecture 5.3 (stationary), by finite-restriction limits; converse open."),
 "C0034": ("Codex review 11:15: floating-point LP feasibility is not an exact certificate.",
  "CORRECTION of C0034-A001's wording. HiGHS reported minimum total violation 0.0 on every instance in double precision; that is numerical evidence, not an exact feasibility certificate. An exact certificate would need rational LP (or a feasible point verified in exact arithmetic) on rational-kernel instances; not done. The observation that the naive conditional splitting fails stands (it is a direct computation).",
  "Feasibility asserted to solver tolerance only; exact rational verification is the next step."),
 "C0035": ("Codex review 11:15: the sublattice reduction needs the reduced-degree case, so it settles only degrees that reduce to a proved case.",
  "CORRECTION of C0035-A001's last claim. The sublattice lemma (symbol g(k theta) = interleaving of k independent copies of P_g) reduces degree m to degree m/k; it settles the question only when the reduced degree is a proved case, i.e. m/k = 1 (degree-1 symbols are 2-block factors by the known result). So the positive answer covers symbols f(theta) = g(m theta) with g of degree 1, not all even degrees: for m = 4 the reduction gives degree 2, which is itself open. The 'induction' in A001 has no base beyond degree 1.",
  "Settled cases: f(theta) = a + b cos(m theta) for any m (block factor with window m + 1); open: every symbol whose reduced degree exceeds 1."),
 "C0036": ("Codex review 10:53: the key identity conflated the Schur complement s with the probability s/(1+s).",
  "CORRECTION of C0036-A001's key_identity line only. Correct chain: s_B = det J_{B+e}/det J_B is nonincreasing in B; s_min = 1/(J^{-1})_ee = 1/((Q^{-1})_ee - 1) = HM/(1 - HM); the minimal conditional probability of presence is s_min/(1 + s_min) = 1/(Q^{-1})_ee = HM(Q). The A001 key_identity wrote 'min P(e | rest) = 1/(J^{-1})_ee = HM', which equates the odds with the probability; the proof text in the math-brain node (harmonic-mean lemma) already has the correct chain. Conclusion (domination by Bernoulli(HM)) unchanged.",
  "min_B P(e in X | X minus e = B) = 1/(Q^{-1})_ee = HM(spec Q); the Schur complement s_min = HM/(1-HM) is the odds, not the probability."),
 "C0040": ("Codex review 12:02: the forward implication is Drewitz-Ramirez Corollary 2.15.",
  "CORRECTION of C0040-A001. The direction 'invariant absolutely continuous probability measure for the environment process + transience in direction l implies ballisticity in direction l' is not open: it is Corollary 2.15 of the source (Drewitz-Ramirez, PDF pages 20-21), so A001's reduction of that direction to strict positivity of the velocity was solving a solved half. Only the converse (ballistic implies existence of an invariant a.c. measure under (ERG)+(E)) is the open content of Open question 2.19; A001's remarks on the converse (regenerations unavailable under (ERG)) stand.",
  "Open content = converse only: ballistic under (ERG)+(E) implies an invariant absolutely continuous environment measure?"),
 "C0042": ("Codex review 12:02: source has a site-index typo and the corrected two-site criterion is refuted by Fribergh-Kious.",
  "CORRECTION and STATUS CHANGE for C0042. The displayed moment condition in the source uses omega(0,e) omega(0,-e) at a single site, which is at most 1/4 automatically, making the displayed hypothesis vacuous; the intended quantity is the two-site back-and-forth product omega(0,e) omega(e,-e). With that reading, Fribergh and Kious (arXiv 1404.2060v2, Proposition 4.4, PDF pages 24-25) exhibit a directionally transient RWRE in d >= 3 with zero speed while the edge escape probability is uniformly positive, so the corrected two-site criterion does NOT imply ballisticity. The problem is recorded as refuted in the literature; A001's remark that the two-site condition controls only two-site traps was pointing the right way.",
  "Refuted: Fribergh-Kious Prop. 4.4 gives transient, zero-speed, uniformly-escaping counterexamples in d >= 3."),
 "C0044": ("Codex review 12:02: A_l and A_{-l} are disjoint by definition; the content of Zerner-Merkl is the 0-1 law for A_l.",
  "CORRECTION of C0044-A001's first sentence. The events {X_n . l -> +infinity} and {X_n . l -> -infinity} are disjoint by definition, so 'Zerner-Merkl show P(A_l intersect A_{-l}) = 0' is empty; what Zerner-Merkl prove in d = 2 is P_0(A_l) in {0,1}, using planarity to show two walks in the same environment intersect, which is what A001 then describes. The reduction (planarity essential; no d >= 3 substitute; no finite-region measurability for the natural martingale) stands.",
  "Zerner-Merkl (d=2): P_0(A_l) in {0,1}; Kalikow (all d): P_0(A_l union A_{-l}) in {0,1}; d >= 3 directional law open."),
 "C0045": ("Codex review 12:02: the claimed equivalence of (P)_M with arbitrary regeneration-moment bounds is unsupported.",
  "CORRECTION of C0045-A001. A001 asserted '(P)_M for large M <=> E[tau_1^{M'}] < infinity for some M' growing with M'. Only one direction is supported by the source's slab decomposition: (P)_M gives polynomial tails for exit probabilities, hence moment bounds on tau_1 of order growing with M. The converse (high moments of tau_1 imply (P)_M) is not established and A001 should not have written an equivalence. The question 'does positive velocity imply (P)_M' stands as a self-improvement question in one direction only.",
  "(P)_M => moment bounds on tau_1 (source); moments => (P)_M unsupported."),
}
RESOLVED = {
 "C0007": ("Biskup, Gufler and Louidor, arXiv 2010.13939v3, Theorem 2.3 (journal version 2024): the near-extremal profile of Conjecture 16.7 is proved. Identified by the Codex holder on 2026-09-07 11:15 his clock; source PDF read and archived on its side.", "resolved_in_literature"),
 "C0042": ("Refuted as a criterion: Fribergh and Kious, arXiv 1404.2060v2, Proposition 4.4 (directionally transient, zero-speed RWRE in d >= 3 with uniformly positive edge escape); the source's displayed condition also carries a site-index typo. Identified by the Codex holder 12:02 his clock.", "resolved_in_literature"),
}
rows = [json.loads(l) for l in open(A, encoding="utf-8") if l.strip()]
for r in rows:
    if r["attempt_id"] == r["problem_id"] + "-A001" and r["problem_id"] in CORR and not r.get("superseded_by"):
        r["superseded_by"] = r["problem_id"] + "-A002"; r["correction_note"] = CORR[r["problem_id"]][0]
open(A, "w", encoding="utf-8", newline="\n").write("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows))
for pid, (method, result, key) in CORR.items():
    append(A, {"schema": "probability-attempt.v1", "attempt_id": pid + "-A002", "problem_id": pid, "recorded_at": now(), "substantive": True,
               "method": method, "result": result, "key_identity": key, "independent_check": "Correction checked line by line against the source and the holder's message by the Fable agent; the holder's claim was taken as a lead, not as authority.",
               "obstruction": "see A001 for the standing obstruction", "author": "claude-probability-1000-continue-0907", "supersedes": pid + "-A001"})
prows = [json.loads(l) for l in open(P, encoding="utf-8") if l.strip()]
for r in prows:
    if r["problem_id"] in RESOLVED:
        note, status = RESOLVED[r["problem_id"]]
        r["current_status"] = status; r["admitted"] = False; r["resolved_by"] = note; r["result_status"] = "not_attempted_resolved"
        r["status_search"] = (r.get("status_search", "") + " | " + note).strip(" |")
    if r["problem_id"] == "C0033":
        r["statement"] = r["statement"].replace("equivalently (Conjecture 5.3) the entropy H(P_f) of stationary determinantal processes is concave in f", "which implies (Conjecture 5.3, by finite restrictions) concavity of the entropy rate H(P_f) of stationary determinantal processes in the symbol f; the converse is not claimed")
open(P, "w", encoding="utf-8", newline="\n").write("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in prows))
print("corrections landed:", len(CORR), "attempt rows;", len(RESOLVED), "problems re-statused")
