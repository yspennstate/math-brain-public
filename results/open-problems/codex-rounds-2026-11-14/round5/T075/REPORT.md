VERDICT: PARTIAL proved arbitrarily long small-cap prefixes at singular parameters in (1/2,1); T075 remains open

The earlier conditional L^p result holds. Its multiplier
4c theta/(c-1) was independently re-derived, and its script reproduced
all reported checks. The five-minute literature check found no solution
of T075. Samuel Kittle and Constantin Kogler's
[arXiv:2611.17277v1](https://arxiv.org/html/2611.17277v1) still assumes
absolute continuity in its higher-integrability theorem.

The new result strengthens the earlier finite-depth warning, whose
singular example lambda=1/3 lay outside the target interval. For the
same prefix concentration statistic, PROOF.md establishes

    A_n(delta) <= min(1, delta(1-lambda)/2
                        + n(2lambda-1)(1-lambda)/lambda)
               <= min(1, delta/4+n(2lambda-1)).

The proof computes the exact one-step total variation defect of the
uniform law on the support, then uses Markov contraction and telescoping.

Let beta_k be the root in (1,2) of x^k-x^(k-1)-...-x-1 and put
lambda_k=1/beta_k. A self-contained proof shows that nu_(lambda_k) is
singular and 0<2lambda_k-1<2^(-k). Therefore, for any delta/4<theta<1
and any finite N, choosing N*2^(-k)<theta-delta/4 gives

    A_n(delta)<theta for every 0<=n<=N,
    but A_n(delta)->1 as n->infinity.

For delta=1/64 and theta=1/36, the singular parameter lambda_20 passes
every test through depth 25,031. The certified margin below the threshold
is 1/9,437,184. At k=40 the certified depth is 26,247,022,364. These are
analytic certificates, not enumerations of all prefixes at those depths.

Commands, run from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T075/check_constants.py > earlier_recheck.txt 2>&1
OMP_NUM_THREADS=1 nice -n 15 python3 check_obstruction.py > computation.txt 2>&1
```

Both exited 0. The new script checked 39 exact one-step defects, 72
prefix TV distances, 288 cap inequalities, and 39 rational root brackets
against independent 120-digit Newton calculations. Runtime was 0.717 s;
peak RSS 17,022,976 bytes; one thread; actual priority 20. LOG.md contains
the output and the independent arithmetic and failure-case audit.

What failed: no concentration estimate at unbounded depths for a specified
transcendental parameter was obtained. The construction uses different
algebraic parameters for different finite horizons. It does not refute a
criterion using transcendence or additional arithmetic hypotheses.

Uncertainty: the elementary obstruction is not asserted novel or optimal.
No formal proof verification was run. The literature search was bounded,
and no quantitative time to eventual concentration was established.

Next worker: a propagation lemma must use information beyond a fixed
finite list of small caps uniformly over real parameters. Investigate a
quantitative condition on arithmetic separation across infinitely many
scales that distinguishes a chosen transcendental parameter from these
multinacci controls. The previous conditional L^p theorem remains usable
once its infinite-subsequence hypothesis is proved.

Task: “take the NEXT checkable step on this problem, building on that work.” — 2026-11-15, first recorded clock 07:57:34 +04:00.
