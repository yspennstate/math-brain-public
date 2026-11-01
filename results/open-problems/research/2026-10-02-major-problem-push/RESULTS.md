# Results and scope, 2026-10-02

The strongest completed result is a full counterexample to the mathematical assertion in Whitt's 1983 Conjecture 1.1: increasing iid service times in convex order can decrease the stationary waiting-time tail in a two-server FCFS Poisson queue. Both service means are unchanged. This is a longstanding queueing comparison; historical novelty and present literature status are unverified, and no external expert review has occurred.

## Full queueing proofs

`proofnet24/whitt-stochastic-comparison/2026-10-02/whitt_README.md` links the complete proof chain and run commands.

- A nine-state integer certificate gives a hand-checkable explicit counterexample at arrival rate 1/10, using S=.5E with probability 2/3 or 2E with probability 1/3, and U=0 or 2E with probability 1/2 each. The exact delay gap is at least 1879/2199357510. The finite chain supplies only a pathwise lower bound; the comparison concerns actual infinite queues.
- A general analytic cubic light-traffic theorem proves a family of counterexamples for every nondegenerate finite hyperexponential starting law. Exchangeability and AM-GM make the excess cubic coefficient strictly positive. The convex-order larger target may be chosen with strictly positive service times.
- At arrival rate 11/10, an explicit strictly positive two-exponential pair has exact certified delay-probability reversal greater than 1/400, and a positive waiting threshold 1/100000 has reversal greater than .0024.
- The original pair is preserved with both a rational matrix-geometric certificate and an independent killed-chain occupation calculation. Mathematical audits, exact outputs and exploratory code are archived.

## Major conjectures: subsidiary results only

The FEI split identity, monotone maximum-influence and approximate-maximum obstructions, full constructions and three further attack routes are in `proofnet24/P03-fei/continuations/2026-10-02-selection-obstructions/`. The full FEI conjecture remains open in this work. These results rule out coordinate-selection proof rules, not FEI itself.

Exact forest transfer coefficients and independent direct enumeration audits establish all edge-pair negative correlations for homogeneous K_(m,s), 2<=m<=8, every s>=2 and all common positive activities. An exceptional twin-matching family is also proved. Full reports are in `proofnet24/P14-probability-correlation/continuations/2026-10-02-forest-families/`. The full forest and q<1 random-cluster conjectures remain open. Prior-art checks are bounded and novelty is unverified.

The Sidorenko Mobius-ladder derivations, regular graphon searches and unresolved operator gap are checkpointed under `research/2026-10-02-major-problem-push/runs/initial/sidorenko/`. The K-theory/nonsofic direct-finiteness attempts and exact remaining gaps are checkpointed in the same run's `k-theory/` folder. Neither full target was solved.

The earlier two proved MMPP counterexamples, PDF, source and exact certificates are already in `proofnet24/mmpp-counterexamples/2026-10-02/`. They concern specialized published questions rather than famous major conjectures.

Hourly continuation was created for the user's authorized ten-hour window, ending 2026-10-03T05:51:21Z. This is scheduled follow-up work, not a claim of uninterrupted execution. Existing unrelated schedules were not changed.
