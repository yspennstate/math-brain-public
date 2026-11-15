VERDICT: PARTIAL a sharper asymptotic interaction-energy bound for the exact planar TSP

The variance-limit conjecture remains open. The earlier reduction checks
out. This session sharpens its asymptotic constant by more than a factor
of two, without a localization assumption for optimal tours.

With the earlier notation V_{n,j} for the order-j Hoeffding energies, put
E_n=sum_{j>=1}j V_{n,j}. The new result is

\[
 \limsup_{n\to\infty} E_n\le\kappa<\frac2\pi,
 \qquad
 \kappa=\min_{c\ge0}\left\{
 c^2+\frac4\pi e^{-\pi c^2}
 -2c\operatorname{erfc}(\sqrt\pi c)\right\}.
\]

The previous report gave 4/pi. The minimizer c_* is unique and satisfies

\[
 c_*=2c_*e^{-\pi c_*^2}+\operatorname{erfc}(\sqrt\pi c_*).
\]

Consequently the earlier reduction has the sharper errors

\[
 \limsup_n\sum_{j>m}V_{n,j}\le\frac\kappa{m+1},\qquad
 \limsup_n\bigl(\operatorname{Var}(L_n)-C_n(\rho)\bigr)
 \le\kappa(1-\rho).
\]

In particular limsup Var(L_n)<=kappa. These are bounds for the exact
optimal closed tour through uniform points in the fixed unit square.
Kappa is not a candidate value for the conjectured limiting variance.
No comparison with the best published variance upper bound is claimed.

The proof uses the insertion interval 0<=d<=2R, where R is the nearest
base-point distance. Conditional variance permits centering sqrt(n)d
at any constant c. The squared error is bounded by the larger of the
two endpoint errors. Since sqrt(n)R converges to a variable Z with
P(Z>z)=exp(-pi z^2), with a uniform Gaussian tail controlling moments,
the endpoint envelope has the expectation displayed above. This handles
the square's boundary explicitly. Taking c=1/sqrt(pi) proves the strict
bound kappa<2/pi by elementary integral inequalities; no decimal
approximation or numerical optimization is used.

PROOF.md supplies every step. It also proves that kappa is the exact
largest possible Var(Y) among scalar couplings satisfying 0<=Y<=2Z
with this marginal law of Z. The extremizer is
Y=2Z 1_{Z>c_*}. This is a limitation of the scalar-envelope argument,
not a realizable TSP insertion law asserted by the proof.

AUDIT.md independently checks the energy by replacement pairs, recomputes
the constant from exponential truncated moments, checks the derivatives
through threshold integrals, and tests boundary and singleton cases.
An oscillating product-space example shows why even the sharper bound
does not force variance convergence. No error in the earlier result or
the new bound was found. All checks are exact analytic calculations;
there is no simulation, generated dataset, or numerical script.

The bounded literature check found no closing theorem. The source actually
opened was Sourav Chatterjee, *A general method for lower bounds on
fluctuations of random variables*, arXiv:1706.04290, whose Section 3,
problem (2), states this conjecture:
https://arxiv.org/html/1706.04290v3.
This was a short update check, not an exhaustive review. No
SOLVED_ELSEWHERE.md was warranted.

Reproduce the artifact checks with:

```sh
env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '
cat PROOF.md AUDIT.md
head -n 1 REPORT.md
wc -l LOG.md PROOF.md AUDIT.md REPORT.md
'
```

LOG.md records the reads, web queries, decisions and audit calculations.
The sandbox prints `nice: setpriority: Operation not permitted`; no
successful priority adjustment is claimed. Only short file reads were
run. All writes stay in this folder; no git or subagents were used.

What failed or remains uncertain: no fixed-order energy convergence,
fixed-noise covariance convergence, add-one stabilization, variance limit,
or limiting constant is proved. The scalar sharpness result shows that
another improvement needs information beyond the interval 0<=d<=2R
and the marginal nearest-distance limit. Novelty relative to the full
literature has not been established.

Next worker: return to V_{n,1}=n Var(E[L_n|X_1]), including the boundary,
or a fixed-noise covariance limit. Further geometry is needed; a local
insertion competitor does not prove that the optimal tour rearranges
locally. The sharper truncation errors are available once a geometric
limit is established.

Task: "take the NEXT checkable step on this problem, building on that work"
— T222, 2026-11-15 approximately 01:40 Asia/Tbilisi (recorded task time).
