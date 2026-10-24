# Independent verification log (lead/Claude)

A running record of results I re-derived from scratch and checked against the manuscript.
"PASS" = independently reproduced; errors found are noted with the fix. This is a second,
independent pass on top of the per-round audit agents.

## Constants / exponents re-derived — PASS
- **k-th singular value exponent** `e_k = d_F k^2` (geometric.tex). Re-derived via the bottom-k
  Laguerre block: Vandermonde `beta*C(k,2)` + weight `k(beta/2-1)` + measure `k` = `beta k^2/2` in
  lambda, doubled by `sigma=sqrt(lambda)` => `d_F k^2`. Checked `k=1 -> d_F`, `k=2 -> 4 d_F`. PASS.
- **One-matrix lower tail** `P{smin(G)<=t} >= c_F t^{d_F}` (ldp.tex). `smin(G) <= d_i = |<R_i,u>|`,
  `u` unit normal to other rows; `<R_i,u>` is a standard scalar Gaussian. PASS.
- **III.D endpoint asymptotics** (geometric.tex). `h(1+delta)= (1+delta)log(1+delta) - delta log delta
  = delta log(1/delta) + delta + O(delta^2)` (used `(1+d)log(1+d)=d+d^2/2+O(d^3)`); and
  `h(gamma)=log gamma + 1 - 1/(2 gamma) + O(gamma^{-2})` as `gamma->inf` (expanded `(gamma-1)log(gamma-1)`).
  Both PASS.
- **II.A-fin-row budget** (universality.tex). `sum_{|T|=m} sum_{i in T} K_{m,i} = binom(N-1,m-1) sum_i K_{m,i}`
  (each i lies in `binom(N-1,m-1)` of the m-subsets); per-T tail `<= C m^{d_F} t^{d_F} sum_{i in T} K_{m,i}`
  via the distance + density argument. PASS.
- **III.A-het-row / III.A-het-entry budgets** (geometric.tex lines ~221-340). Column negative-second-moment
  forces a column distance `<= sqrt(m) t`; orthocomplement dim `>= p=r+1`; Cauchy-Binet gives a p-row block
  with projected density `<= (prod_{a in S} K_{m,a,q}) binom(m+r,p)^{d_F/2}`; m-powers reconcile:
  `binom(m+r,p)^{d_F/2} * m^{d_F p/2} = m^{d_F p}`, and het-entry reduces to het-row under column-uniformity
  (`sum_q kappa_{T,q} = m kappa_T`), het-row to III.A-fin under full uniformity. Internally consistent. PASS.

## Lemmas re-derived / verified — PASS (with fixes applied)
- **2D bounded-density anti-concentration** (`lem:two-proj`, notes/IIB_lemma_2D.md). Char-function bound
  (variance => small-theta, Riemann-Lebesgue+L^2 => large-theta), local-CLT constant
  `(1-|rho|^2)^{-d_F/2}`, far-tail via transverse-pair Cauchy-Schwarz. Adversarial verify: SOUND.
  FIX APPLIED: the `(1+o(1))` constant holds for `t_m -> 0`, not all `0<t<=1` (at fixed t the constant
  degrades). Corrected in the .tex.
- **small/intermediate-D negligibility** (`prop:small-D-negligible`, notes/IIB_overlap_smallD.md).
  Hypergeometric overlap rarity `P{2<=D<=eps m} = o(e^{-d_F s m})` via the LD rate `R(beta')`. PASS.
- **Quaternion overlap moment** (notes/quaternion_base.tex). `|rho|^2 ~ Beta(2,2(D-1))`,
  `E[(1-|rho|^2)^{-2}|D] = (2D-1)(2D-2)/((2D-3)(2D-4))`. FIX APPLIED: this is `1+2/D+O(D^{-2})`, NOT
  `1+4/D` (my first draft). Unified pattern `1+d_F/(2D)` (R:1/(2D) via Beta(1/2,(D-1)/2); C:1/D via
  Beta(1,D-1); H:2/D via Beta(2,2(D-1))). PASS after fix.
- **Spherical two-slab constant** (notes/rotinv_universality.tex, superseded by user's pathwise version).
  FIX APPLIED: mixture constant is `E[Sigma^{-2d_F}]/(E[Sigma^{-d_F}])^2` (a 2-D density needs the
  `2d_F` exponent), not the halved version. (Now moot: user's pathwise approach handles mixtures.)
- **Gumbel intensity** (notes/gumbel_partial.tex). `E[Z_x] = binom(N,m) P{smin<=e^{x-b_m}} -> e^{d_F x}`
  using the power-law hard edge and the defining equation for `b_m`; one-sided Markov bound; reduction of
  full law to factorial moments = the same bulk overlap moment as prob:pc. PASS.

## Structural facts checked
- **Deterministic sign-frame failure** (`prop:sign-critical`, VI.B). Two-COLUMN pigeonhole (not antipodal-row):
  among 2m-1 rows, cols 1,2 agree or disagree on >= m rows; on those rows the two columns are equal/opposite
  => any m of them give a singular minor. Valid for ALL m>=2. PASS. (I initially mis-checked with the wrong
  pigeonhole; the column argument is correct.)
- **Universality-upper and Gumbel are the same obstruction**: both close iff
  `E[(1-|rho|^2)^{-d_F/2}; D>=eps m] <= 1+o(1)` (bulk overlap moment). Verified the reduction in both directions.

## More checks (session 7) — PASS
- **III.B-lower** (k-th singular value lower side). Independently re-derived (notes/kth_singular_lower.tex):
  one-matrix tail `P{sigma_{m-k+1}(G)<=t} <= C_{m,k} t^{d_F k^2}` from the bottom-k Laguerre block
  (`beta C(k,2)+k(beta/2-1)+k = beta k^2/2` in lambda, doubled), then union bound => lower side
  `>= -h(gamma)/(d_F k^2)`. Matches the user's `III.B-lower` row. PASS.
- **II.A-fin-dir** (directional anti-concentration => log-concave lower side). If
  `P{|<R_i,u>-z|<=r} <= L_{m,i} r^{d_F}` uniformly, then `d_i=|<R_i,u>|` has small-ball
  `<= L_{m,i} m^{d_F/2} t^{d_F}`, budget `binom(N-1,m-1) sum_i L_{m,i}` (each i in `binom(N-1,m-1)`
  m-subsets), threshold `(log binom(N-1,m-1)+log sum L_i + (d_F/2)log m)/d_F`. For isotropic log-concave
  rows `L_{m,i}=C` (bounded 1-D marginal density), base `h(gamma)/d_F`. Resolves the LOWER side of
  `prob:logconcave`. PASS.

## Net / publishability assessment (lead view, session 7)
No mathematical errors found in the user's PROVEN formulas on independent re-derivation; all fixes were to
my own draft notes pre-integration. The proven core is now broad and verified: the principle; universal
lower side in ~10 forms (bounded-density, density-rate, finite-entropy, row/entry/directional heterogeneous,
log-concave, random-count); spherical universality over R,C (pathwise) + quaternion base h/4 (all division
algebras); LDP sandwich; deterministic critical sign-frame failure; row/column conditioning transfers;
k-th-singular lower side; and a partial Gumbel law (intensity + explicit limit + one-sided bound).

A referee's likely verdict: PUBLISHABLE as a framework + verified proven core + a sharply-isolated central
open problem, PROVIDED the abstract/intro lead with the PROVEN results and present the conditional flagship
honestly as one named estimate. Minimal path to "every headline result proven": close the bulk overlap
moment `E[(1-|rho|^2)^{-d_F/2}; D>=eps m] <= 1+o(1)` (a no-gaps-delocalization sub-lemma; Rudelson 2016),
which by the Gumbel reduction ALSO upgrades FLU. That single estimate is the paper's center of gravity and
is itself a clean, citable open problem. Recommend: (1) abstract leads with proven core; (2) state the
"universality-upper = Gumbel = one overlap moment" unification prominently; (3) keep conditional/partial
labels exactly as is (honest, referee-friendly).
