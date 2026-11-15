VERDICT: PROVED TW1 with deterministic finite-size centering for spherical inputs and a strictly subcritical quadratic Hermite component

The round 3 result holds on independent rechecking. This session extends it
from a_0=a_1=a_2=0 to a_0=a_1=0, allowing q=a_2^2>0 under the explicit strict
condition

    q alpha sqrt(b)<v,
    alpha=lim N/d,    b=lim m/N !=1,    v=E sigma(Z)^2>0.

The other hypotheses remain: independent spherical input columns of radius
sqrt(d), independent standard Gaussian W, a fixed Lipschitz activation, and
positive finite proportional limits. For K=YY^T/N and b_N=m/N,

    [b_N^(1/6)/(v(1+sqrt(b_N))^(4/3))] N^(2/3)
      [lambda_max(K)-v(1+sqrt(b_N))^2] => TW_1.

Thus the largest eigenvalue converges in probability to v(1+sqrt(b))^2.
This is a further special case of T248. The full problem remains open.

The complete proof is in [PROOF.md](PROOF.md). Its new covariance decomposition is

    Sigma=(v-q/d)I+(q/d)11^T+qB+R,
    B_jk=rho_jk^2-1/d (j!=k),    B_jj=0,
    ||B||_op=O_p(d^-1/4),    ||R||_F=O_p(d^-1/2).

The operator-norm bound follows from an exact fourth-trace identity proved
by centered traceless tensor contractions and closed-walk counting. It
isolates one population eigenvalue v+q alpha+o_p(1). The condition above is
exactly positive separation of its pole from the scalar MP stationary point.
A strengthened deterministic edge lemma allows this nonvanishing subcritical
population spike. Exact trace cancellation and E Tr((Sigma-vI)^2)=O(1) give
an O_p(N^-1) conditional edge shift, negligible at the TW scale.

The universality input remains Corollary 1.4 of Guangchen Chen and Xing Lyu,
*Tracy–Widom law for sample covariance matrices under quadratic form
concentration*, [arXiv:2610.41416v2](https://arxiv.org/html/2610.41416v2).
Its hypotheses are verified conditionally, with uniform constants. The theorem
is used as stated, not independently reproved. The five-minute literature
check found no newer full solution; no SOLVED_ELSEWHERE.md was created.

Independent verification is in [verify_subcritical.py](verify_subcritical.py),
with the command and complete relevant output in [LOG.md](LOG.md):

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B verify_subcritical.py
```

All checks passed. Coordinate-polynomial integration independently reproduced
the pair, star and cycle expectations exactly at d=2,3; exhaustive enumeration
verified all fourth-trace walk counts for N=2,...,7. The two covariance-edge
solvers agreed within 1.776e-15. The script also checked the predecessor's
rational trace cancellation, spherical moments, the threshold on both sides
of criticality, first-order finite-rank edge shifts, and normalization in both
rectangular orientations. These are algebra checks, not numerical TW evidence.
The scalar script used the standard library and finished in 0.018 seconds.

The launcher printed a priority-adjustment warning, but the script's effective
priority guard passed. A separate diagnostic measured nice value 20, already
at least the required 15. No computation ran at an unverified higher priority.
All task writes stayed in this folder; no git, subagents or external writes.

What fails or remains uncertain: covariance closeness to vI alone fails for
q>0, which is why the spike was separated. At criticality pole separation
vanishes, and above it the scalar MP stationary point is across the pole;
the cited regular-rightmost-edge theorem does not supply the desired bulk-edge
fluctuation result there. No sample outlier fluctuation law or law for the
next eigenvalue below an outlier is proved. Linear components, random column
norms, non-Lipschitz polynomials and b=1 remain outside this result. Replacing
the exact finite aspect ratio by its limit still requires an extra rate.

Next worker: use the same decomposition to prove TW1 for the explicitly
projected kernel Y(I-ee^T)Y^T/N, e=(1,...,1)^T/sqrt(N), even when q is supercritical.
Then identify the additional comparison needed to transfer that result to
the second eigenvalue of the original kernel. Interlacing alone does not
identify its fluctuations, so do not equate these two conclusions.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, first clock reading 05:13:02 +04.
