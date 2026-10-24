# C0052 review packet for w473 and integration

## Scope and artifacts

- Target: source's 3D nontriviality criterion for `g(beta)`, not a claim that a full critical scaling field has been constructed.
- Primary source: Hugo Duminil-Copin, *Lectures on the Ising and Potts models on the hypercubic lattice*, (7.1), (7.2), Conjecture 6, Exercise 34, Exercise 61(1): https://www.ihes.fr/~/duminil/publi/2017PIMS.pdf .
- Local evidence: `SOURCE_STATUS.json`, `ATTEMPT.md`, `CLAIMS.jsonl`; historical `C0052-A001` at `~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl:42`.
- Completed peer verdicts and reproducible finite checks: `REVIEW_PEERS.md`, `verify_peer.py`, `compute_gate.json`.
- Store correction row: `STORE_CORRECTIONS.jsonl` for existing card `claim_db355f...`.
- Own new finite-tree lemma for w473: `ENDPOINT_TREE_OBSTRUCTION.md`, endpoint-averaged bare/augmented ratio tends to zero on degree-three trees.

## Referee request to w473

Independently rederive the conditional weighted-intersection inequality in `ATTEMPT.md` from Exercise 61(1). Try to refute: (1) the normalization by `chi^2 xi^3`, (2) the all-connected event when marked vertices coincide, (3) the infinite-volume passage, and (4) the implication from `liminf q_beta>0` to nontriviality. Return KEEP/FIX/DROP with the narrowest valid statement and the unresolved input. The proof author is w470, so its own check is preliminary only.

## Preliminary verdicts

| Claim | Verdict | Reproduction | Remaining gap |
|---|---|---|---|
| Historical C0052-A001 is a proof | DROP | The row itself states its variance bound was not closed. | Scale-uniform intersection lower bound. |
| Historical C0052-A001 heuristic equivalence | FIX | Source's g is a spatial sum with `chi^2 xi^3` normalization; Exercise 61(1) gives each summand's current event. | Relate any proposed geometric event estimate to the weighted sum. |
| w468-C0052-S0 dated task metadata | KEEP, scoped | The task packet really provides title, tier and dated status only. | Exact source and mathematical work were pending in w468's files when read. |
| w469 finite-volume and finite-tree lemmas | KEEP, scoped | Re-derived `E X_f^4=3-2E_Q p` and `q >= (e/4)r^2` on trees; see `REVIEW_PEERS.md`. | Missing 3D original-current lower bound. |
| w469 finite-cycle parity obstruction | KEEP, scoped | Re-derived the two cycle-parity sectors and `h=tanh(t)^4/(1+tanh(t)^4)`; see `REVIEW_PEERS.md`. | No cyclic-lattice nonlinear comparison is established. |
| w470 conditional reduction | FIX applied after w473 review; conditional algebra KEEP | Full endpoint joint mass is now explicit in `ATTEMPT.md`; w473 rederived the sum and constant. | Infinite-volume passage and missing `liminf q_beta>0`. |

No complete C0052 proof, formal-check receipt, or current-openness certification is claimed.
