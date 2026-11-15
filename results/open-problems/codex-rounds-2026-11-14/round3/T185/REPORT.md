VERDICT: PARTIAL obstruction to smooth homogeneous workload Lyapunov functions

The earlier linear-workload result holds under its stated Poisson
assumptions. It was rederived independently through a link-slack argument
and a scalar busy-period comparison. T185 remains unresolved.

New beyond the earlier report: in its same two-link network, with loads
(1/5,1/2,1/2), deterministic unit files, arbitrary alpha>0 and positive
fairness weights, no function V=F(W) in the following class has uniformly
strictly negative pointwise generator drift outside a finite V-sublevel:
F is positively homogeneous of any degree d>0, is C^1 away from zero
including the orthant boundary, and satisfies F(e_0)>0. This extends the
earlier obstruction from positive linear functions to a class of nonlinear
functions, without convexity or coordinate monotonicity assumptions.

For each such F, PROOF.md constructs states with V tending to infinity and

\[
 \lim_{N\to\infty}N^{1-d}\mathcal GV(x_N)
 \ge dF(e_0)/5>0.
\]

There are N through-route files and N^3 nearly completed files on one local
route. The normalized workloads approach e_0, while service approaches
either e_1 or e_2. The two limiting drifts average to dF(e_0)/5. A separate
Poisson event reaches nearby obstructing states from empty with strictly
positive probability; the theorem does not rely on hitting equal-residual
states exactly. Each link has load 7/10, so the example is strictly
subcritical. Positive instantaneous drift does not imply instability:
the almost completed local files clear on a time scale tending to zero.

The literature update found no unrestricted later stochastic stability
theorem. Opened primary sources were Yingjia Fu and Ruth J. Williams's
[2020 publisher page](https://pubsonline.informs.org/doi/10.1287/stsy.2019.0058)
and [2022 paper](https://mathweb.ucsd.edu/~williams/bandwidth/AAP1723forposting.pdf),
and Maria Vlasiou, Jiheng Zhang and Bert Zwart's
[arXiv:1411.4841](https://arxiv.org/abs/1411.4841).
The 2022 paper discusses a distributionally conditional bridge through
Lee's work. The arXiv abstract concerns heavy traffic. This brief search
does not certify that the problem is open, or establish novelty of the
obstruction. The publisher confirms DOI 10.1287/stsy.2019.0058; an initial
contrary bibliographic note in LOG.md is corrected later in that log.

Reproduce the exact checks from this folder:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 check_obstruction.py
```

Output: `all exact checks passed`; 216 earlier coefficient witnesses;
120 exact KKT checks; direct generator evaluations equal independent
Laurent expansions for five polynomial functions and both service
branches. Their respective limiting drift pairs are (1/5,1/5),
(2/5,2/5), (4/5,4/5), (21/10,-9/10), and (14/5,-6/5).
The general theorem is symbolic, not inferred from these finite checks.
Full output is obstruction_checks.json. The successful run took 0.0099
seconds and peaked at 15,843,328 bytes RSS, with actual process nice 20.

What failed: a smooth homogeneous nonlinear workload replacement cannot
repair the earlier pointwise drift method. Three initial script attempts
stopped before mathematical checks because macOS rejected RLIMIT_DATA
settings. The final script reports that restriction, caps CPU time, and
records and checks its tiny measured RSS. The nice wrapper warns, but a
direct priority query confirms the process already runs at nice 20.

AUDIT.md independently checks the earlier certificate, the new drift
constant, all positive real degrees, accessibility, the boundary derivative
assumption, unequal weights, and the order of limits. No mistake in the
earlier mathematical result or counterexample to stability was found.

Unresolved: nonsmooth or nonhomogeneous workload functions, residual-profile
functions, and drift sampled over time. The result requires C^1 behavior
at the through-route axis; interior differentiability alone is insufficient.
It proves no additional stochastic recurrence region and no renewal-arrival
extension.

Next worker: retain this example as an adversarial test for a sampled-drift
argument. A concrete next lemma would estimate the expected change of the
maximum link workload over a fixed sufficiently long interval, uniformly
over the two hostile state sequences here. Such a lemma must retain actual
unit arrival jumps and control newly arriving local files after the original
tiny residuals clear. A negative result for pointwise drift cannot be
substituted for that interval calculation. For a general fluid bridge,
compare Lee's exact distributional hypotheses before invoking it.

Task: “take the NEXT checkable step on this problem, building on that work.”
First recorded task time: 15 November 2026, 01:38:59 Asia/Tbilisi;
completion resumed at 03:30 Asia/Tbilisi. Exact receipt time is unavailable.
