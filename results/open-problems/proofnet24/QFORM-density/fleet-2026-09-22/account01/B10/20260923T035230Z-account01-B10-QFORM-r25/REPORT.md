SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B10, 2026-09-23T03:52:30Z.
attacking: rank-three positive-regression-residual collar; extract a disjoint original-product residual/transverse packet and use exact deletion to reach the partner exact-graph theorem on a quantitative subbranch.

# account01/B10 r25 — orthogonal-regression split and exact deletion bridge

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: arbitrary exact-rank-three coupled case  
Status: `ESSENTIAL_STEP_APPLIED / NEW_EXACT_STRUCTURAL_IDENTITY / TARGET_SUBBRANCH_CLOSED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full target remains OPEN. This report proves a product-preserving structural theorem for the small positive regression-residual collar left by account02/B10, and closes one new quantitative subbranch by applying that partner's completed exact-graph theorem at an actual density inequality. It does not assume post-rotation independence, moments, bounded support, log-concavity, or a uniform pointwise oscillatory estimate. No new continuity statement is claimed for the branch closed here.

## 1. Fresh source boundary and completed dependencies


The designated partner actually applied is account02/B10, run `20260923T014801Z-account02-B10-QFORM-auto11`, canonical proof

`yspennstate/math-open-problems@e00458111ae6c54afa30331726a6335fc838557f`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260923T014801Z-account02-B10-QFORM-auto11/REPORT.md`.

Its exact-graph theorem says the following. In an exact-rank-three representation `A=RMR^T`, let a heavy physical row be `sqrt(c)u`, and let a disjoint original-coordinate bank have rows

`r_j=(w dot p_j)u+p_j`, `p_j in u^perp`,

with `G=sum p_jp_j^T >= kappa I_2`, `h=det G`, `q=u^TMu`, `D=|det M|`, `sigma_min(M)>=s`. If

`eta=(|q|/s)(1+(1-c)/kappa)<1`,

then

`||p_Q||_infinity <= C_CT 2^(2/3) h^(-1/3)(cD)^(-1/3)(1-eta)^(-1/6)`,

where `C_CT=103680^(1/3)`. Its complementary nonnull rank-one-bank theorem gives

`||p_Q||_infinity <=128 sqrt(2) c^(-1/2)D^(-1/4)|q|^(-1/4)`.

For the live one-heavy/two-bank reduction the partner records

`c>3/10`, `kappa_0=7/800`, `s=1`, `D>=1`.

The exact-graph endpoint `rho=0` is therefore already paid for every scalar pivot. The first unpaid state is a bank with small positive longitudinal regression residual `rho`.

The projection-density fact used only for the provenance corollary below is `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, account02/B06,

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,

which gives `exp(k/2)` as a dimension-free density cap for a normalized `k`-dimensional product projection. The partner's cross-transverse input was also checked at its canonical source `yspennstate/math-open-problems@7140ff63d4ff7c092cdc18ce7ad8a95e4e03e388`.

## 2. Regression coordinates for one light bank

Fix the heavy spectral direction `u`. For one disjoint light bank `B`, write its spectral rows as

`r_i=t_i u+p_i`, `p_i in u^perp`.

Assume its transverse Gram is positive definite,

`G=sum_i p_i p_i^T >0`.

Let

`b=sum_i t_i p_i`, `w=G^(-1)b`,
`e_i=t_i-w dot p_i`, `rho=sum_i e_i^2`.

Then

`sum_i e_i p_i=0`.

The full bank Gram, in `R u direct_sum u^perp`, is

`S_B=[[w^TGw+rho,(Gw)^T],[Gw,G]]`,

so the familiar Schur identity is

`det S_B=rho det G`.

Assume for the rest of Sections 2--5 that `rho>0`; `rho=0` is exactly the partner's paid graph endpoint.

Whiten only the deterministic coefficient geometry:

`a_i=e_i/sqrt(rho)`,
`q_i=G^(-1/2)p_i in R^2`.

Then the three columns of the row matrix

`z_i=(a_i,q_i) in R^3`

are orthonormal:

`sum_i a_i^2=1`,
`sum_i q_iq_i^T=I_2`,
`sum_i a_i q_i=0`.

Put

`alpha_i=a_i^2`, `beta_i=||q_i||^2`, `ell_i=alpha_i+beta_i`.

Because `sum_i z_i z_i^T=I_3`, every row leverage obeys

`0<=ell_i<=1`,

and

`sum_i ell_i=3`, `sum_i alpha_i=1`, `sum_i beta_i=2`.

No random-variable change of basis has occurred here; these are coefficient identities only.

## 3. A sharp residual-versus-transverse determinant identity

### Theorem 3.1 — `QFORM-ORTHOGONAL-REGRESSION-MIXED-VOLUME-v1`

With the notation above,

`boxed:
 sum_i e_i^2 det(G-p_i p_i^T)
 =rho det G [1-sum_i alpha_i beta_i]
 >=(1/3) rho det G.
`

The constant `1/3` is sharp at the level of this coefficient inequality.

### Proof

The matrix determinant lemma gives

`det(G-p_i p_i^T)=det G (1-p_i^TG^(-1)p_i)=det G(1-beta_i)`.

Hence

`sum_i e_i^2 det(G-p_i p_i^T)
 =rho det G sum_i alpha_i(1-beta_i)
 =rho det G [1-sum_i alpha_i beta_i]`.

It remains to show

`sum_i alpha_i beta_i<=2/3`.

For rows with `ell_i>0`, put `x_i=alpha_i/ell_i in[0,1]`; rows of zero leverage may be ignored. Then

`alpha_i beta_i=ell_i^2 x_i(1-x_i)<=ell_i x_i(1-x_i)`

because `ell_i<=1`. Introduce probability weights `mu_i=ell_i/3`. Since

`sum_i mu_i x_i=(1/3)sum_i alpha_i=1/3`,

concavity of `x(1-x)` gives

`sum_i alpha_i beta_i
 <=3 sum_i mu_i x_i(1-x_i)
 <=3*(1/3)*(2/3)=2/3`.

This proves the inequality.

For sharpness, take three rows forming an orthogonal `3x3` matrix whose first column is `(1,1,1)/sqrt(3)`. Then every row has `ell_i=1`, `alpha_i=1/3`, `beta_i=2/3`, so `sum alpha_i beta_i=2/3` and equality holds. QED.

The theorem says the positive Schur defect `rho det G` cannot hide entirely in coordinates that simultaneously exhaust the transverse two-dimensional leverage.

## 4. Product-preserving disjoint split

### Theorem 4.1 — `QFORM-REGRESSION-RESIDUAL-TRANSVERSE-SPLIT-v1`

There is a partition of the ORIGINAL bank indices

`B=S disjoint_union T`

such that, with

`rho_S=sum_(i in S)e_i^2`,
`G_T=sum_(j in T)p_jp_j^T`,

one has

`boxed: rho_S det G_T >= (rho det G)/24.`

Consequently the residual scalar

`E_S=sum_(i in S)e_iX_i`

is genuinely independent of the transverse vector

`Z_T=sum_(j in T)p_jX_j`,

because the two aggregates use disjoint original coordinates.

### Proof

Choose a random Bernoulli partition, independently placing every index into `S` or `T` with probability `1/2`. By two-dimensional Cauchy--Binet,

`det G_T=sum_(j<k; j,k in T) det(p_j,p_k)^2`.

Therefore

`E[rho_S det G_T]
 =sum_i sum_(j<k; i,j,k distinct)
   e_i^2 det(p_j,p_k)^2 P(i in S,j,k in T)`
` =(1/8) sum_i e_i^2
   sum_(j<k; j,k !=i) det(p_j,p_k)^2`
` =(1/8) sum_i e_i^2 det(G-p_i p_i^T)`.

Theorem 3.1 now gives

`E[rho_S det G_T]>=(rho det G)/24`.

At least one deterministic partition attains at least its expectation. QED.

This is a strict product-provenance statement, not a marginal-density or conditional-density surrogate. Applying the completed weighted affine-fiber Brascamp--Lieb theorem to the normalized disjoint aggregates gives

`||p_(E_S/sqrt(rho_S))||_infinity<=sqrt(e)`,

and, after whitening `Z_T`, a two-dimensional density cap at most `e`. Thus the split produces a genuine independent scalar/vector source with coefficient-volume packet at least `(rho det G)/24`. This does not yet by itself bound the quadratic pushforward, because the remaining projections carried by the same `S` and `T` source coordinates still enter the quadratic polynomial. The theorem is therefore a structural bridge, not a declaration of full closure.

For the live quantitative bank `G>=kappa_0 I_2`,

`boxed: rho_S det G_T >= rho kappa_0^2/24
       = (49/15360000) rho.`

## 5. Exact delete-one formula

The same orthonormal-row geometry gives an exact recursion that identifies when a positive-residual bank becomes an exact graph after conditioning one original coordinate.

### Lemma 5.1 — `QFORM-REGRESSION-DELETE-ONE-v1`

Fix `i` with `beta_i<1` and remove coordinate `i` from the bank. Let

`G_i=G-p_i p_i^T`

and let `rho_i` be the least-squares longitudinal regression residual of the remaining coefficients `{t_j:j!=i}` against `{p_j:j!=i}`. Then

`boxed:
 det G_i=det G(1-beta_i),
 rho_i=rho (1-ell_i)/(1-beta_i).
}`

### Proof

Apply the deterministic regression shear that sends the full bank coefficient row `(t_i,p_i)` to `(e_i,p_i)`. The total sheared Gram is `diag(rho,G)`. Whitening it sends row `i` to `z_i=(a_i,q_i)`. Deleting this row therefore changes the full Gram determinant, by the matrix determinant lemma, to

`rho det G (1-||z_i||^2)=rho det G(1-ell_i)`.

The transverse determinant after deletion is separately

`det G_i=det G(1-beta_i)`.

The Schur complement identity for the remaining bank says its full Gram determinant is `rho_i det G_i`; division gives the stated formula. QED.

In particular, if

`ell_i=1`, `alpha_i>0`,

then deleting coordinate `i` makes the remaining bank an exact graph:

`rho_i=0`,

while

`det G_i=alpha_i det G`.

This is an exact algebraic endpoint, not a small-perturbation argument.

## 6. Actual application of account02/B10: a new paid leverage-one subbranch

Return to the partner's live one-heavy/two-bank reduction:

`c>3/10`, `G>=kappa_0 I_2`, `kappa_0=7/800`, `s=1`, `D>=1`.

Assume one positive-residual light bank contains a row `i` satisfying

`ell_i=1`, `alpha_i>=1/4`.

Condition on the original coordinate `X_i` together with all coordinates outside the heavy scalar and the remaining bank. This is product-safe conditioning. By Lemma 5.1 the remaining bank has zero regression residual, so it is an exact graph and the designated account02/B10 theorem applies, including arbitrary induced affine terms.

Moreover

`h_i:=det G_i=alpha_i det G>=kappa_0^2/4`.

Because the transverse Gram of any subbank is bounded above by `I_2` in the Parseval frame,

`lambda_min(G_i)>=det G_i>=kappa_1`,

where

`kappa_1:=kappa_0^2/4=49/2560000`.

Set

`q_0=kappa_1/4=49/10240000`.

### Near-null pivot: `|q|<=q_0`

For the partner exact-graph theorem,

`eta<=q_0(1+(1-c)/kappa_1)
 < kappa_1/4+7/40<1/5`.

Hence `1-eta>4/5`, and using `h_i>=kappa_1`, `c>3/10`, `D>=1`,

`||p_Q||_infinity
 <=C_CT 2^(2/3) kappa_1^(-1/3)(3/10)^(-1/3)(4/5)^(-1/6)
 <4323.`

### Nonnull pivot: `|q|>=q_0`

Apply the completed rank-one-bank theorem quoted and used in the account02/B10 partner report to the heavy original coordinate itself, whose ray mass is `m=c`:

`||p_Q||_infinity
 <=128 sqrt(2)c^(-1/2)D^(-1/4)|q|^(-1/4)`
` <=128 sqrt(2)(3/10)^(-1/2)q_0^(-1/4)`
` <7067.`

Thus the two ranges overlap and prove the new target-level branch

`boxed: ||p_Q||_infinity<7067`

whenever a live positive-residual quantitative bank contains a normalized regression/transverse row with `ell_i=1` and `alpha_i>=1/4`.

This is the required actual partner application: account02/B10's exact-graph interpolation is invoked after the exact delete-one identity, with the new quantitative lower bound `h_i>=kappa_0^2/4` inserted into its density inequality.

Essential boundedness is proved in this subbranch. Continuity is not claimed here because the invoked all-pivot splice includes an essential-density theorem for which a continuous representative is not part of the stated source result.

## 7. What is now genuinely left

The positive-residual collar can no longer be described as lacking disjoint product provenance. Every such bank has the sharp mixed-volume certificate of Theorem 3.1 and a disjoint original-coordinate residual/transverse packet of Theorem 4.1. The exact graph boundary `rho=0` is paid by account02/B10, and the leverage-one/high-residual-share deletion branch above is also paid.

The first unpaid implication is therefore

`QFORM-DISJOINT-RESIDUAL-TRANSVERSE-MIXED-CURVATURE-RECEIVER-v1`.

In the concrete surviving collar one may take `0<rho<1/100` and small heavy Rayleigh quotient `|q|`, with no usable leverage-one deletion as above. One must convert

`rho_S det G_T >= rho det G/24`

into a density payment while retaining the same-bank transverse contamination attached to `E_S` and the same-bank longitudinal contamination attached to `Z_T`. Taking a conditional density supremum is forbidden by the live correction; treating `sqrt(rho)E` as a small random perturbation is also invalid without moment/support assumptions. The appropriate next receiver must act on the two disjoint ORIGINAL product banks before collapsing them to dependent projections.

The arbitrary exact-rank-three theorem remains OPEN / NOT PROVED / NOT DISPROVED, and so does the owner's full three-large-eigenvalue conjecture. No counterexample to the conjecture is produced here.
