SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-23T16:51:24Z.
attacking: remove the one-hub projected-crossing row-marginal gate by heavy-row peeling, while retaining a dependence-safe whole-copy time integral.

# account01/B03 r29 — row-marginal-free one-hub two-volume compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.
Assignment: decoupled time integral.
Status: `NEW SUPPORTING THEOREM / ROW-MARGINAL GATE REMOVED IN ONE-HUB-PLUS-2VOLUME PACKET / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture remains OPEN. This report proves an analytic compiler for one original hub plus a projected two-volume crossing. It removes the `alpha_i<=1/2` volume-row-marginal gate by recursively promoting heavy physical rows into the grouped hub/selector bank. No rotation of the input law is used. The theorem also gives a whole-copy independent-copy time integral and a continuous density in its stated packet.

## 1. Source boundary


Primary completed analytic source:

- `math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`,
  `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.
  I use its grouped-hub projected-crossing theorem (GC), including the exact `k=1, ell=2` and `k=2, ell=1` constants and its allowance of arbitrary internal hub functions and arbitrary internal light curvature.

Designated partner actually applied:

- account02/B03, `math-open-problems@c3bba054c20287883c43303711eec7eefc05d46e`,
  `proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260923T131311Z-account02-B03-QFORM-r11/REPORT.md`.
  Its theorem `QFORM-JOINT-SELECTOR-PHASE-LP-PLANCHEREL-v1`, at `p=infinity,k=3`, gives for three genuine physical selectors with arbitrary selector self-curvature and full-row-rank cross matrix `M`

  `||p_Q||_infinity <= 3 sqrt(e) Delta_3^(-1/3)`,

  where `Delta_3=sqrt(det(MM^T))`, and proves a continuous `C_0` density together with the whole-copy weighted integral.

Corrections retained: no law-uniform pointwise quadratic-phase decay; no independence after rotation; no conditional density cap for conjugate sum/difference variables; no arbitrary-joint rank-three coarea cap; no fixed uniformly good physical minor; no perturbative deletion of small coefficients under arbitrary fragmented unbounded input support.

## 2. Geometric packet

Let the original-coordinate indices be split as

`{h} union I union J`,

and let all coordinates be independent with probability densities bounded by one. Allow an arbitrary quadratic polynomial

`Q(X)=X^T A X+b^T X+c`;

the affine terms are included because conditioning elsewhere in the full problem creates them.

Write the physical hub-to-`J` row

`m=A_{h,J}`

and assume `m!=0`. For every `i in I`, write

`a_i=A_{i,J}`

and project away the hub row,

`c_i=a_i(I-P_m)`,

where `P_m` is orthogonal projection onto `span(m)` in the Euclidean coordinate space indexed by `J`.

Define the aggregate projected two-volume

`Z_2 = sum_{i<j, i,j in I} |c_i wedge c_j|^2`.

Assume `Z_2>0`. Put

`V_3 := ||m||^2 Z_2`.

Equivalently,

`V_3 = sum_{i<j} |m wedge a_i wedge a_j|^2`.

Indeed orthogonal projection away from `m` preserves each three-volume after factoring out `||m||`:

`|m wedge a_i wedge a_j|^2 = ||m||^2 |c_i wedge c_j|^2`.

Thus `V_3` is an aggregate physical three-volume on one fixed column bank `J`; no reciprocal single-minor selection has occurred.

## 3. Main theorem

### Theorem `QFORM-ONE-HUB-ROW-MARGINAL-FREE-2VOLUME-v1`

Under the packet above, if `V_3>0`, then `Q` has a continuous `C_0` density and

`||p_Q||_infinity
 <= C_* V_3^(-1/6)`,

where

`C_* = 3*2^(7/6)*exp(1/3)
     = 9.39913188784886...`.

Consequently every interval `K` satisfies the genuine linear small-ball estimate

`P(Q in K) <= C_* V_3^(-1/6) |K|`.

No volume-row-marginal assumption is required.

### Proof

For `Z_2>0`, define the two-volume row marginals

`alpha_i = Z_2^(-1) sum_{j!=i}|c_i wedge c_j|^2`.

They obey `0<=alpha_i<=1` and `sum_i alpha_i=2`.

#### Case 1: every `alpha_i<=1/2`

This is exactly the completed one-original-hub, `ell=2` consequence of (GC). The hub projection is the single original coordinate `X_h`, whose density is at most one, the hub crossing singular product is `S=||m||`, and the projected crossing two-volume is `Z_2`. Therefore

`||p_Q||_infinity
 <= 3*2^(7/6)*exp(1/3)(||m||^2 Z_2)^(-1/6)
 = C_* V_3^(-1/6)`.

The source proof gives the pointwise characteristic-function envelope

`|phi_Q(t)|
 <= min(1,
    K_* V_3^(-1/4)|t|^(-3/2))`,

with

`K_* = 2^(7/4) pi^(3/2) exp(1/2)`.

Hence the density is continuous and vanishes at infinity.

#### Case 2: some `alpha_i>1/2`

Fix such an `i`. Let

`d_j=P_{c_i^perp}c_j`, `j!=i`,

and

`F_i^2=sum_{j!=i}||d_j||^2`.

The exact exterior-algebra identity is

`||c_i||^2 F_i^2
 = sum_{j!=i}|c_i wedge c_j|^2
 = alpha_i Z_2`.                                              (3.1)

In particular `c_i!=0` and `F_i>0`.

Promote the physical coordinate `i` into the hub group. The two grouped physical hub coordinates are now `(X_h,X_i)`, whose joint density is at most one. Their crossing matrix to `J` has rows `m,a_i`. Subtracting the `m`-component of `a_i` is a determinant-one row operation, so its singular-value product is exactly

`S_i=sqrt(det([m;a_i][m;a_i]^T))
    =||m|| ||c_i||`.                                         (3.2)

For every remaining `j in I\{i}`, projection away from the enlarged crossing row space `span(m,a_i)=span(m,c_i)` gives exactly `d_j`. Thus the new projected one-volume is

`Z_1'=F_i^2`.                                                (3.3)

Define its row marginals

`beta_j=||d_j||^2/F_i^2`.

##### Case 2a: every `beta_j<=1/2`

Apply (GC) with `k=2, ell=1`. Since the grouped hub consists of two genuine original coordinates, its joint density cap is one. For `ell=1` the exponential entropy factor is absent. Therefore

`||p_Q||_infinity
 <=3*2^(5/6)(S_i F_i)^(-1/3)`

`=3*2^(5/6)(||m|| sqrt(alpha_i Z_2))^(-1/3)` by (3.1)-(3.2). Since `alpha_i>1/2`,

`||p_Q||_infinity
 < 6 (||m|| sqrt(Z_2))^(-1/3)
 = 6 V_3^(-1/6)`.                                          (3.4)

This is strictly better than `C_* V_3^(-1/6)`.

The source characteristic-function envelope in this branch is

`|phi_Q(t)|
 <=min(1,
   2^(5/4)pi^(3/2)(S_iF_i)^(-1/2)|t|^(-3/2))`.

Using `alpha_i>1/2`, its coefficient is at most

`2^(3/2)pi^(3/2)V_3^(-1/4)`,

again smaller than the Case-1 coefficient `K_* V_3^(-1/4)`.

##### Case 2b: some `beta_j>1/2`

Choose such a `j`. Promote `j` as a third genuine physical selector. The `J`-restriction of the three-row cross matrix has rows `m,a_i,a_j`. Determinant-one row elimination sends these rows to the mutually orthogonal triangular system

`m, c_i, d_j`.

Hence its three-volume is exactly

`Delta_J
 =sqrt(det([m;a_i;a_j][m;a_i;a_j]^T))
 =||m|| ||c_i|| ||d_j||`.                                  (3.5)

Since `beta_j>1/2`,

`||d_j||>F_i/sqrt(2)`.

Combining with (3.1) and `alpha_i>1/2` gives

`Delta_J
 > ||m|| sqrt(alpha_i Z_2/2)
 > (1/2)||m|| sqrt(Z_2)
 = (1/2)V_3^(1/2)`.                                         (3.6)

Now take the full cross matrix `M_full` from the three physical selectors `(h,i,j)` to all remaining original coordinates. Its Gram matrix is the sum of the positive-definite `J`-restriction Gram matrix and a positive-semidefinite contribution from all other background columns, so

`Delta_3=sqrt(det(M_full M_full^T)) >= Delta_J`.             (3.7)

This is the promised actual application of the designated account02/B03 theorem. Its `k=3,p=infinity` quadratic cross-block consequence allows arbitrary symmetric curvature inside the three-selector principal block and arbitrary quadratic curvature in the background, and gives

`||p_Q||_infinity
 <=3 sqrt(e) Delta_3^(-1/3)`

`<3 sqrt(e) 2^(1/3) V_3^(-1/6)`

`=6.231775903093545... V_3^(-1/6)`.                          (3.8)

This is again strictly below `C_* V_3^(-1/6)`. The same partner theorem gives an integrable `|t|^(-3/2)` envelope, hence a continuous `C_0` density.

Cases 1, 2a and 2b are exhaustive, proving the theorem. QED.

## 4. Dependence-safe whole-copy time integral

The proof never splits a copy difference into conjugate coordinate sums and differences. For an independent copy `Q'`, retain the scalar identity as a whole:

`|phi_Q(t)|^2 = E exp(it(Q-Q'))`.                              (4.1)

Across all three cases above, the Case-1 envelope dominates the branchwise envelopes:

`|phi_Q(t)|
 <= min(1, K_* V_3^(-1/4)|t|^(-3/2))`,                        (4.2)

where

`K_*=2^(7/4)pi^(3/2)exp(1/2)
    =30.87980451778735...`.

Indeed Case 2a has the smaller coefficient `<=2^(3/2)pi^(3/2)V_3^(-1/4)`, while the account02/B03 `k=3` envelope in Case 2b is also smaller after (3.6).

Squaring (4.2) and splitting at

`T=(K_*^2 V_3^(-1/2))^(1/3)=K_*^(2/3)V_3^(-1/6)`

gives the exact weighted bound

`int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <= (24/5)K_*^(1/3)V_3^(-1/12)`

`= (24/5)2^(7/12)sqrt(pi)exp(1/6)V_3^(-1/12)`

`=15.05911390259813... V_3^(-1/12)`.                           (4.3)

By the regularized Riesz identity

`int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 =sqrt(2pi) E|Q-Q'|^(-1/2)`,                                  (4.4)

so also

`E|Q-Q'|^(-1/2)
 <=6.007717241127417... V_3^(-1/12)`.                          (4.5)

The linear small-ball scaling does not rely on pretending (4.3) alone is an `L^infinity` criterion; it comes from the stronger `L^1_t` envelopes in the three exhaustive branches.

## 5. Target-level corollary

Let `s=s_3(A)` be the third largest singular value of the symmetric coefficient matrix (equivalently the third largest eigenvalue magnitude). If a physical partition `{h} union I union J` satisfies

`V_3 = ||A_{h,J}||^2
       * sum_{i<j in I}|A_{i,J}(I-P_{A_{h,J}}) wedge A_{j,J}(I-P_{A_{h,J}})|^2
     >= eta s^6`

for some `eta>0`, then

`||p_Q||_infinity <= C_* eta^(-1/6) s^(-1)`,                   (5.1)

with a continuous `C_0` density, and

`int |t|^(-1/2)|phi_Q(t)|^2dt
 <=15.0591139026 eta^(-1/12) s^(-1/2)`.                       (5.2)

Thus the analytic debt for this packet is now only aggregate extraction of a positive-scale `V_3`; no volume-row-marginal regularity is needed.

Exact target-valid control: for

`A_0=[[0,I_3],[I_3,0]]`

with the split `h=1`, `I={2,3}`, `J={4,5,6}`, one has `||m||=1`, `Z_2=1`, hence `V_3=1`. The spectrum of `A_0` is `+1` and `-1`, each with multiplicity three. The theorem gives

`||p_{X^T A_0 X}||_infinity <=9.3991318879`

and a continuous density for every cap-one product input law. The partner theorem gives a sharper constant on this special exact-rank-three crossing; the point here is the row-marginal-free aggregate compiler.

## 6. What remains open

This theorem does NOT prove that the bare hypothesis `s_3(A)>=1` forces a partition with `V_3` bounded below by a universal positive constant. Diagonal and near-diagonal forms can have zero disjoint crossing volume and are paid by other branches; concentrated low-rank/grouped-hub forms may require a different partition or a separate grouped-source exit. Therefore full QFORM remains OPEN.

The next useful structural implication is:

`QFORM-AGGREGATE-3VOLUME-OR-PAID-EXIT-v1`:

from `s_3(A)>=1`, prove either (i) a physical partition with `V_3>=eta_0` for a universal `eta_0>0`, so (5.1) applies, or (ii) route to an already proved diagonal/pivot/ridge/grouped-hub/exact-coloop packet. The extraction must aggregate before reciprocal minor selection and must not treat a small operator coefficient as a small random perturbation.

Within the theorem's scope, both essential boundedness and continuity are proved. Unrestricted full-target continuity remains OPEN.
