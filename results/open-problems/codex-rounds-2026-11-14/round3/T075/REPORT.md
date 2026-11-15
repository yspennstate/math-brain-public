VERDICT: PARTIAL proved a finite-prefix concentration criterion with a conditional explicit L^p exponent; T075 remains open

The earlier result holds. Samuel Kittle and Constantin Kogler's [arXiv:2611.17277v1](https://arxiv.org/html/2611.17277v1), Theorem 1.1, assumes absolute continuity and concludes higher integrability. The bounded literature update found no subsequent solution of T075. The earlier folder has no PROOF.md or scripts.

The extension is in PROOF.md. Let f_n be the density of the n-sign prefix plus an independent uniform variable on the exact remaining tail interval, and let A_n(delta) be its largest mass on any set of Lebesgue measure at most delta. For every 0<lambda<1,

    nu_lambda is absolutely continuous
    iff liminf_n A_n(delta)<1 for some delta>0.

If nu_lambda is singular, A_n(delta) tends to one for every delta>0. If it is absolutely continuous, sup_n A_n(delta) tends to zero as delta decreases to zero. The proof derives pure type and establishes the useful uniform comparison A_n(delta)<=2 omega_nu(delta), where omega_nu is the small-set mass modulus.

Under the stronger, unproved hypothesis

    liminf_n A_n(delta)<theta<1/18,  0<delta<=D=2/(1-lambda),

the density belongs to L^p for

    p = 1 + log(1/(18 theta))/log(72D/(delta lambda)).

This uses the cited paper's Lemma 2.1 after proving absolute continuity. It does not assume a density in the sufficiency direction. These are elementary reductions beyond the earlier literature-only report; no claim of priority over existing criteria is made.

The exact-rational script computes A_n by sorting the overlaps of prefix intervals. Run:

~~~sh
OMP_NUM_THREADS=1 nice -n 15 python3 prefix_concentration.py > computation.txt 2>&1
~~~

It passed 72 independent midpoint/convex-dual comparisons and 112 comparisons with exact formulas at lambda=1/2 and lambda=1/3. Runtime was 1.180 seconds; peak RSS was 28,082,176 bytes; actual priority was 20 and OMP_NUM_THREADS was 1. Full output and the commands are in computation.txt and LOG.md.

What failed: the finite-depth calculations do not establish any infinite-subsequence bound for lambda=2/3 or any transcendental parameter. The singular control lambda=1/3 passes the threshold theta=1/36 at depth 4 but reaches A_14(1/64)=1. A finite favorable value therefore cannot replace the hypothesis. This control lies outside (1/2,1).

Uncertainty: the conditional regularity exponent uses a new preprint's analytic lemma; its level-set constants were independently checked, but no Lean verification or exhaustive literature review was performed. No specified transcendental Bernoulli convolution is newly proved absolutely continuous.

Next worker: prove a bound A_{n_j}(delta)<=theta<1 along an unbounded sequence for one specified transcendental lambda. A bound theta<1/18 also gives the displayed exponent. The exact sweep provides a verification target, but additional finite depths alone will not close the gap. A promising lemma would propagate such a bound to arbitrarily large depths; no such propagation is proved here.

Task: “take the NEXT checkable step on this problem, building on that work.” — 2026-11-15, first recorded local clock 01:10:23 +04:00.
