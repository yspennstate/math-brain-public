# account02/B13 — residual Pluecker pair-incidence forcing in the nested-heavy rank-three obstruction

**Run:** `20260922T152225Z-account02-B13-productset-7f3c9a`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Extremal product laws  
**Classification:** `PROVED SUPPORTING STRUCTURAL LEMMA / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full owner conjecture remains **OPEN / NOT PROVED**. No moment, bounded-support, centered-interval, post-rotation independence, fixed-fragment-count, or pointwise oscillatory-decay assumption is used.

## 1. Exact reduction already available and first unpaid implication

The earlier account02/B13 extreme-product result (brain handoff `20260922T115714Z-account02-B13-qform-480ba28b.md`, canonical math-open-problems report commit `604a08009638981da254a72f09a24dd50e3a3c94`) proves with zero loss that for every measurable kernel `0<=K<=1`,

`sup_{0<=f_i<=1, int f_i=1} int K(x) prod_i f_i(x_i) dx`

is the same supremum over product indicators `prod_i 1_{E_i}` with `|E_i|=1`; bounded finite unions of intervals are dense for this supremum. In particular QFORM reduces exactly to a geometric slab inequality on arbitrary unit-measure product sets, but **not** to one interval or to a bounded number of fragments.

The live partner result actually consumed here is account03/B13

`yspennstate/math-open-problems@dd421029601cf5663685c49f225af55567332fb6`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/b13-20260922T143428Z-qform11/REPORT.md`.

For an exact-rank-three Parseval frame in its nested-heavy branch it proves that any sequence with unbounded output-density norm must satisfy simultaneously

`d_* -> 0` and `Delta -> 0`,

where `d_*` is the largest physical coefficient squared in the last transverse direction and `Delta` is the determinant of the covariance left in the first two spectral directions after removing the two heavy rows. It also applies account01/B13's completed disjoint-exterior theorem

`||p_Q||_infinity <= 12 D0^(-1/6)`

for `D0=sum_{I cap J=empty} det(R_I)^2 det(R_J)^2`.

The first unpaid implication attacked in this run is therefore: **what extra original-coordinate structure is forced when `d_*`, `Delta`, and `D0` all tend to zero?**

## 2. Nested-heavy coordinates

Use exactly the partner notation. Let `A=R Lambda R^T`, `R^T R=I_3`, and choose physical rows

`r_i = sqrt(c) e1`,

`r_j = rho e1 + sqrt(h) e2`,

with `c>1/2`, `h>1/2`. For residual indices `k` write

`r_k = a_k e1 + b_k e2 + z_k e3`.

Parseval gives

`sum a_k^2 = 1-c-rho^2`,
`sum b_k^2 = B := 1-h`,
`sum a_k b_k = -rho sqrt(h)`,
`sum a_k z_k = sum b_k z_k = 0`,
`sum z_k^2 = 1`.

Put

`Delta = (1-c)(1-h)-rho^2 >= 0`,
`s = h+rho^2 = ||r_j||^2`,
`beta = rho^2 + h(1-c)`.

Let

`n = (sqrt(h)e1-rho e2)/sqrt(s)`

be the unit vector in `span(e1,e2)` perpendicular to `r_j`, and set

`u_k = <r_k,n> = (sqrt(h)a_k-rho b_k)/sqrt(s)`.

Then

`U := sum u_k^2 = beta/s`.

Also set `d_* = max_k z_k^2`.

## 3. Two exact residual pair measures

For every residual unordered pair `{k,l}`, define

`p_{kl} := det(r_i,r_k,r_l)^2`
`         = c (b_k z_l-z_k b_l)^2`,

`q_{kl} := det(r_j,r_k,r_l)^2`
`         = s (u_k z_l-z_k u_l)^2`.

These are genuine Pluecker weights of physical triples. Their total masses are exactly

`alpha := sum_{k<l} p_{kl} = c B`,

`beta  := sum_{k<l} q_{kl} = rho^2+h(1-c)`.

The first identity is Cauchy--Binet for the two residual coefficient vectors `(b,z)`; the second is the same identity for `(u,z)` and the formula `sU=beta`.

For a residual coordinate `k`, let the incident pair masses be

`p_k := sum_{l != k} p_{min(k,l),max(k,l)}`,
`q_k := sum_{l != k} q_{min(k,l),max(k,l)}`.

Because `b` and `u` are both orthogonal to `z`, there are exact identities

`p_k = c (b_k^2 + B z_k^2)`,                              (3.1)

`q_k = s u_k^2 + beta z_k^2`.                              (3.2)

In particular `sum_k p_k=2 alpha` and `sum_k q_k=2 beta`.

## 4. New cross-incidence lower bound for disjoint exterior mass

Let

`M = sum_{ {k,l} cap {m,n}=empty } p_{kl} q_{mn}`

where both sums are over unordered residual pairs. The physical triples `{i,k,l}` and `{j,m,n}` are disjoint whenever their residual pairs are disjoint, so the ordered disjoint-exterior mass satisfies

`D0 >= 2 M`.                                                   (4.1)

The complement of the disjoint-pair event is covered by the coordinate incidences. Hence

`M >= alpha beta - sum_k p_k q_k`.                              (4.2)

Combining (4.1)-(4.2) with `sum p_k=2alpha` and `sum q_k=2beta` gives the two quantitative forms

`D0 >= 2 alpha ( beta - 2 max_k q_k )`,                         (4.3)

`D0 >= 2 beta  ( alpha - 2 max_k p_k )`.                        (4.4)

These inequalities remain valid when the displayed right side is negative; their useful content is the positive regime.

Normalize the two planar residual vectors when `B,beta>0` by

`x_k=b_k/sqrt(B)`, `y_k=u_k/sqrt(U)`.

Then (3.1)-(3.2) imply

`max_k p_k/alpha <= max_k x_k^2 + d_*`,
`max_k q_k/beta  <= max_k y_k^2 + d_*`.

Therefore

`D0 >= 2 alpha beta [1-2(max_k y_k^2+d_*)]`,                     (4.5)

and symmetrically with `x` in place of `y`.

**Interpretation.** The partner's final-transverse diffuseness `d_* <<1` cannot by itself make the disjoint-exterior channel small. If either normalized surviving planar coefficient vector is itself diffuse, then `D0` is quantitatively positive and the completed account01/B13 theorem pays the density. Small `D0` forces a third physical coordinate to capture a macroscopic share of the surviving planar energy.

## 5. Exact relation to the partner's covariance determinant

The two residual coefficient vectors `b` and `u` are related by an invertible linear change inside the original two planar coefficient sequences `(a,b)`. Their Gram determinant is

`det Gram(b,u) = (h/s) Delta`.                                  (5.1)

Since `||b||^2=B` and `||u||^2=U=beta/s`, this gives the exact normalized correlation identity

`|<x,y>|^2 = 1 - h Delta/(B beta)`.                              (5.2)

Thus the partner's `Delta ->0` conclusion is precisely an `l2` alignment statement between the two planar vectors that occur in the new pair-incidence channel, provided `B beta` does not vanish.

## 6. New asymptotic sharpening of the only possible unbounded nested-heavy sequence

Consider a nested-heavy exact-rank-three sequence for which `||p_Q||_infinity -> infinity`. By the completed partner result,

`d_* ->0`, `Delta ->0`.

By the completed account01/B13 disjoint-exterior estimate, necessarily also

`D0 ->0`.

There are now only two possibilities.

### 6.1 Boundary-leverage degeneration

If `alpha beta = c(1-h)[rho^2+h(1-c)] ->0`, then because `c,h>1/2` and every row leverage is at most one, after taking a subsequence either

`h ->1` (hence `||r_j||^2=h+rho^2 ->1`),

or

`c ->1` (the first heavy physical row has leverage tending one).

So one of the first two physical coordinates asymptotically owns an entire spectral direction.

### 6.2 Third-row planar concentration

Otherwise suppose `alpha beta >= eta>0`. Rearranging (4.3) gives

`max_k q_k >= beta/2 - D0/(4 alpha)`,

and hence by (3.2) there exists a residual index `k_q` with

`u_{k_q}^2/U >= 1/2 - d_* - D0/(4 alpha beta)`.                  (6.1)

Similarly some `k_p` satisfies

`b_{k_p}^2/B >= 1/2 - d_* - D0/(4 alpha beta)`.                  (6.2)

By (5.2), after choosing the sign of `y` so `<x,y>>=0`,

`||x-y||_2^2 = 2(1-sqrt(1-h Delta/(B beta)))`
`             <= 2 h Delta/(B beta)`.                           (6.3)

Consequently a coordinate carrying the lower bound in (6.2) also carries asymptotically one half of the `u` energy. More explicitly, if

`eps = d_* + D0/(4 alpha beta)`,
`theta = h Delta/(B beta)`,

then for the index `k_p` from (6.2),

`u_{k_p}^2/U >= ( sqrt(max(0,1/2-eps)) - sqrt(2 theta) )_+^2`.    (6.4)

In the unbounded sequence under `alpha beta>=eta`, the right side tends `1/2`. At the same time

`z_{k_p}^2 <= d_* ->0`.

Hence a **third physical row becomes planar-heavy while remaining asymptotically transverse-null**. The residual obstruction is not merely `(d_*,Delta)->(0,0)`; it is a nested concentration pattern with three physical rows carrying macroscopic planar mass and the final spectral direction still spread over the remaining coordinates.

This is the new structural theorem of the run.

## 7. Why this advances the product-set geometry

The exact bang-bang reduction says a strict small-ball counterexample may be sought among arbitrary product indicators, but live corrections forbid reducing those indicators to one interval, bounded diameter, or uniformly bounded fragment count. The identities above instead reduce the difficult rank-three geometry through **physical Pluecker incidence**, which is independent of support fragmentation and survives arbitrary unit-measure product sets.

Combined with account03/B13, any putative unbounded rank-three sequence in the nested-heavy branch must now approach one of two much thinner geometries:

1. a leverage-one physical row; or
2. three nested planar-heavy rows plus a transverse direction carried diffusely by the remaining independent coordinates.

The second geometry is the natural next place to apply bank aggregation: aggregate the diffuse transverse bank **before** conditioning, while retaining the three concentrated physical coordinates. This is compatible with the correction that conditional caps need not survive nonphysical changes of variables.

## 8. Finite sanity check

A deterministic numerical checker for the algebraic pair identities was run on 1000 random finite coefficient systems with `b perpendicular z` and `u perpendicular z`, dimensions 5 through 12. The maximum errors in the total-mass and coordinate-incidence identities were below `8e-15`; every instance satisfied `M >= alpha beta-sum_k p_k q_k`. This is only a sanity check; Sections 3--6 are exact algebraic proofs.

## 9. Scope and next implication

**Proved here:** exact physical pair-incidence identities and a quantitative disjoint-exterior lower bound, plus the resulting nested-heavy asymptotic sharpening after applying the completed partner theorem.

**Not proved:** the full exact-rank-three theorem, the leverage-one boundary, the three-planar-heavy plus diffuse-transverse bank, arbitrary additional spectrum, or the full owner conjecture.

The next unpaid implication is:

`QFORM-RANK3-THREE-HEAVY-DIFFUSE-TRANSVERSE-v1` — prove a uniform slab bound for the source-valid limit geometry consisting of three planar-heavy physical rows and a final transverse spectral direction carried diffusely by the remaining original independent coordinates, without conditioning away the product provenance; or construct a genuine product-indicator counterexample.
