Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-04 idea before code — stop the rescue aggregates from escaping by charging their entropy deviation

This continues only the scoped cluster-aware Díaz weighted-counting route in `operations/claims/PROB10-04.md`.  It does not audit or duplicate NM13-13's interpolation candidate or NM13-06's constructive lower-bound route.

## Inherited obstruction

Run 9 proved a correct conditional dual after fixing six outer scalars

\[
(u,v,w,q,\beta,e)
=(\ell_{ps},\ell_{ns1},\ell_{ns2},Q/u,B/N,E/v),
\qquad N=\lambda_n-v-w.
\]

The rescue factor is

\[
\prod_{i=1}^{M}
\left(1-\frac12\frac BN\left(\frac Qu\right)^i\frac Ev\right)^{t_{i,1}n+o(n)}.
\]

The simple six-dimensional outer relaxation is too loose for endpoint work because it permits `Q=0`, `B=0`, or `E=0`, which switches the rescue penalty off.  A deterministic positive lower bound on all three aggregates is false: in particular, even at the rounded Díaz copy macrostate the exact 16-clause-type LP permits `B=0` while preserving the syntactic clause masses and the three copy masses.  Therefore the next step cannot be another structural floor for `B`.

## New idea

Do **not** force `Q,B,E` away from zero by feasibility.  Instead, compare every variable/clause type distribution with the unrescued Gibbs distribution selected by fixed positive Díaz multipliers.  The log-sum inequalities used in the source proof have exact relative-entropy remainders.  Pinsker plus Cauchy turns these remainders into quadratic costs for moving the rescue aggregates away from their Gibbs values.

For the `j=1` variable blocks, with

\[
D_1=\sum_{i=1}^{M}\widehat\delta_{i,1},
\qquad E=\sum_i f_{i,1,1},
\]

and Gibbs value `E_*`, the exact KL remainder gives the universal cost

\[
K_{var}\ge \frac{2(E-E_*)^2}{D_1}.
\]

For the clause blocks let `B` be the canonical-blocker statistic and `Q` the safe-`ps` statistic.  Splitting the clause KL remainder in half and applying Pinsker separately to the two bounded statistics should give

\[
K_{clause}
\ge \frac{(B-B_*)^2}{G_B}
+\frac{(Q-Q_*)^2}{G_Q},
\]

where, for 3-SAT,

\[
G_B=\widehat\gamma_0+\widehat\gamma_1,
\qquad
G_Q=\widehat\gamma_1+4\widehat\gamma_2+9\widehat\gamma_3.
\]

The coefficients come from the exact within-syntactic-class ranges of the two clause statistics: `B` has ranges `(1,1,0,0)` for `k=0,1,2,3`, while `Q` has ranges `(0,1,2,3)`.

The rescue factor itself can be linearized in the correct direction:

\[
\log(1-x)\le -x.
\]

The only remaining difficulty is to lower-bound the weighted true-center mass

\[
A(q,f)=\sum_i t_{i,1}q^i,
\qquad q=Q/u,
\]

using only `q` and the total false-leaf mass `E`.  Since `t_i+f_i=\delta_i` and `\sum f_i=E`, this is a finite fractional-knapsack problem.  Because `q^i` decreases with `i` for `0\le q\le1`, the adversary minimizes `A` by placing false mass first in the smallest degrees.  Thus define exactly

\[
A_{\min}(q,E)
=\sum_{i=1}^{M}\delta_iq^i
-\max\left\{\sum_i f_iq^i:
0\le f_i\le\delta_i,\ \sum_i f_i=E\right\},
\]

whose optimizer greedily fills `i=1,2,...`.

If the three entropy inequalities are correct, then at every fixed copy macrostate `(u,v,w)` and for every feasible type,

\[
\log F_R
\le D_0(u,v,w;\nu,\mu)
-\mathcal P(Q,B,E),
\]

with

\[
\boxed{
\mathcal P(Q,B,E)=
\frac{2(E-E_*)^2}{D_1}
+\frac{(B-B_*)^2}{G_B}
+\frac{(Q-Q_*)^2}{G_Q}
+\frac{BE}{2Nv}A_{\min}(Q/u,E).
}
\]

Here `D_0` is the ordinary unrescued conditional Díaz dual at the fixed copy macrostate.  This would convert the previous six-outer-scalar obstruction into a **three-copy-mass outer problem plus an explicit three-variable nonnegative defect**.  More importantly, the defect stays strictly positive even though feasibility alone permits one rescue aggregate to vanish: making it vanish incurs a KL price.

## Three different attacks in this run

1. **Deterministic clause-capacity floors.**  Derive exact lower bounds such as
   \[
   Q\ge \frac{[3u+3v+w-3\gamma_b]_+}{2}.
   \]
   This succeeds for `Q` but fails fundamentally for `B`; a feasible clause LP can have `B=0` at the rounded source copy macrostate.

2. **Entropy-stabilized aggregates (main route).**  Keep `Q,B,E` variable but prove the quadratic KL costs above, then combine them with the rescue factor and the fractional-knapsack lower envelope `A_min`.  This is the route to prove on the page.

3. **Pure variable-side floor for `E`.**  Try to force `E>0` from copy conservation alone.  The coarse inequalities only give a bound of the form
   \[
   E\ge [v-h_{ns}-\sum_{i,j\ge2}j\widehat\delta_{i,j}]_+,
   \]
   which can be zero in the relevant region.  So `E` must also be stabilized entropically rather than by feasibility.

## Exact missing lemma for this run

Prove the displayed entropy-stabilized defect inequality with all constants and boundary conventions.  Then test only the **rounded source saddle as a diagnostic**, not as an endpoint theorem: the question is whether the defect remains of order `10^{-7}` after allowing arbitrary inner reallocation of `Q,B,E`, rather than merely evaluating the rescue at the old saddle point.

No threshold endpoint is to move unless the final outer `(u,v,w)` optimization is rigorously certified for a density below `4.4898`.