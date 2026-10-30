# Addendum — balanced-hub near-coloop optimization

Run: `20260923T074642Z-fleet01-B04-QFORM-auto15`.

This addendum sharpens `QFORM-SINGLE-HUB-BERNOULLI-TILT-v1` from `REPORT.md`. Full QFORM remains open. The square-peel conclusion below is an essentially bounded density statement; continuity is not claimed.

## 1. Logarithmic-cost tilt near a canonical coloop

Retain the notation of the report. The canonical squared-`2x2`-minor law has hub inclusion probability

`p=1-epsilon`, `0<epsilon<1`,

and conditional leaf frequencies `u_k=P(k in S|h in S)`, `v_k=P(k in S|h notin S)`. Assume the balanced-neighborhood condition

`u_k+v_k<=1` for every `k!=h`.

For a Bernoulli tilt with hub mass `theta>=1/2`, every nonhub row marginal is

`alpha_k(theta)=theta u_k+(1-theta)v_k <= theta(u_k+v_k) <= theta`,

because `theta>=1-theta`. Therefore the fleet02/B04 entropy-weighted rank-two half-Riesz theorem applies with

`q=2 theta <2`.

Suppose now `0<epsilon<=e^(-2)`. Put

`L_epsilon=log(1/epsilon)`, `delta=1/L_epsilon`, `theta=1-delta`.

Then `0<delta<=1/2` and `delta>=epsilon` (equivalently `e^{L_epsilon}>=L_epsilon`). The Bernoulli entropy cost is

`D=D_Ber(1-delta || 1-epsilon)`

`=(1-delta) log[(1-delta)/(1-epsilon)] + delta log(delta/epsilon)`.

Since `delta>=epsilon`, the first term is nonpositive, while

`delta log(delta/epsilon)=delta[L_epsilon+log delta]=1+delta log delta<=1`.

Hence

`D<=1`.

The exact Gibbs identity from the report gives

`G_2=Z_2 exp(-D) >= e^(-1) Z_2`.

Moreover `q=2(1-delta)>=1` and `2-q=2delta`, so the partner constant satisfies

`C(q)=4 sqrt(2e) q^(-1/4)/(2-q)
      <=2 sqrt(2e) delta^(-1)`.

Therefore:

### `QFORM-BALANCED-HUB-NEARCOLOOP-LOG-v1`

Under the assumptions above,

`sup_s E|R-s|^(-1/2)
 <= 2 sqrt(2e) e^(1/8) log(1/epsilon) Z_2^(-1/8)`.

Numerically the leading constant is

`2 sqrt(2e) e^(1/8)=5.284197541698714...`.

If an untouched original coordinate gives `Q=a[Z+m]^2+R`, `a!=0`, then

`||p_Q||_infinity
 <=5.284197541698714... |a|^(-1/2)
   log(1/epsilon) Z_2^(-1/8)`.

This shows that in the balanced-neighborhood regime a canonical hub marginal tending to one costs only a logarithm when one optimizes the tilt instead of fixing `theta=1/2`.

## 2. Application to the rotated family in REPORT.md

For the report family `M_L`,

`epsilon=1-p=2/(L^2+2)`,
`Z_2=2(L^2+2)`,
`u_k+v_k=3/4`.

Whenever `2/(L^2+2)<=e^(-2)`, the optimized branch gives

`||p_(Q_L)||_infinity
 <=5.284197541698714...
   log[(L^2+2)/2]
   [2(L^2+2)]^(-1/8)`.

Together with the half-tilt estimate from the report,

`4 sqrt(2e)(4 sqrt(2)L)^(-1/8)`,

one may take the minimum of the two explicit bounds. The optimized branch has asymptotic order `O(L^(-1/4) log L)`, whereas the fixed half-tilt has order `O(L^(-1/8))`.

## 3. Exact-coloop endpoint in the quadratically-clean-bank scope

There is a clean endpoint application of the newest completed fleet02/B04 theorem.

If the canonical `E_2` row law has `p=1`, then every nonzero physical `2x2` row minor contains the hub row `h`. Therefore every `2x2` minor of the row-deleted block `M_{-h}` vanishes, so

`rank(M_{-h})<=1`.

Since `Z_2=e_2(M^T M)>0`, `rank(M)>=2`; adding one row to a rank-at-most-one matrix raises rank by at most one, hence in fact

`rank(M)=2`.

In the quadratically clean `J`-bank setting of fleet02/B04's completed theorem `QFORM-COEFFICIENT-PROJECTED-ROWSTAR-CLEANBANK-v1`, take the deterministic coefficient projection `P=I`. Its hypotheses are then exactly met and one gets

`||p_Q||_infinity <=2^(3/4) sqrt(pi) E_2(M)^(-1/4)`.

Source: `yspennstate/math-open-problems@c7fbb4f97fef82c9e6920e17bc01fa3efc0da85e`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260923T071501Z-fleet02-B04-QFORM-r11/REPORT.md`.

This closes the strict-coloop endpoint only in that clean-bank scope. It does **not** close the arbitrary two-sided-curvature endpoint of the full QFORM problem.
