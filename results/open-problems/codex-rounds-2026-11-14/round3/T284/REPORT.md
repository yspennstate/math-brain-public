VERDICT: PARTIAL subpolynomial success amplifies to high probability with vanishing density loss

The earlier amplification result holds. Its main bound was re-derived independently and its verifier rerun unchanged from this directory; all checks passed.

New beyond that report: let d>0 be fixed rational and k_n/n->a>0 be a polynomial-time computable target. If an arbitrary randomized polynomial-time solver succeeds in G(n,d/n) with probability v_n=n^(-o(1)), a polynomial-time transformation finds an independent set of size k_n-o(n) with probability tending to one. It makes n^2 ceil(log_2 n) solver calls and does not need to know v_n or its convergence rate. For constant starting success, the loss is O(n log log n/log n), with failure O((log n)^(-K)) for any fixed K>0. PROOF.md gives the exact loss and finite-n probability bound. This removes fixed density slack for a narrower success hypothesis than the earlier theorem; it does not remove all vertex loss.

The construction tries dyadic edge-refresh rates, repairs each solver output by deleting endpoints of original internal edges, and returns the largest valid result. The analytic input is the same as before: Corollary 1.11 of Elchanan Mossel, Krzysztof Oleszkiewicz, and Arnab Sen, *On reverse hypercontractivity*, arXiv:1108.1210v5, https://arxiv.org/pdf/1108.1210 . No novelty claim is made for the underlying amplification method.

Commands, run in this folder:

    env OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114/briefs/T284/verify.py
    env OMP_NUM_THREADS=1 nice -n 15 python3 verify_extension.py

Both pass. The new verifier checks 90 exact latent-variable posterior identities, 396 independent count-based posterior identities, 6120 numerical negative-moment inequalities, 111 exact binomial tails compared numerically with the bound, 369 scale/loss cases, 8 complete sampling-error budgets, and 19482 rounding identities. It tests symbolic integers up to n=2^8192 without allocating n-sized objects. Runtime was 1.5033 seconds; peak resident memory was 16482304 bytes. OMP_NUM_THREADS=1 and inherited nice=20 were verified; the sandbox refused raising priority to the requested 15. Full output is in LOG.md; data are in verification.json and extension_verification.json.

What failed or changed: the first new verifier run included small n outside the proof's eventual scale-existence hypothesis. Its test domain was corrected and four such cases are explicitly counted. An audit found that the overlap-scale corollary needed polynomial-time computability of its target constant, rather than mere computability; the corrected corollary uses integer d and rational epsilon, with an explicit approximation argument for log d. No contradiction to either amplification theorem was found.

Unresolved and uncertain: T284 remains open here. There is no named average-case hardness reduction, no all-polynomial-time obstruction, and no algorithm that crosses the barrier. The new theorem does not give exactly k_n vertices, vanishing loss from arbitrary inverse-polynomial starting success, or polynomially small failure with vanishing loss. The imported analytic inequality is checked in the primary paper and used as a theorem; finite numerical checks do not reprove it. The bounded literature check found no settlement and is not exhaustive. AUDIT.md records the attempts to break the result and the limits of the argument.

Next worker: the concrete remaining amplification question is whether constant-success search can be amplified with O(n/log n) loss, rather than the present O(n log log n/log n), or whether a counterexample to such a general transformation can be proved. The present negative-moment estimate alone stops at constant failure when delta log n stays bounded. A more central advance on T284 still needs a distribution-preserving reduction from a separate, explicitly named average-case assumption, or a barrier-crossing algorithm; these amplification lemmas supply neither.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 03:44 +04 (Asia/Tbilisi).
