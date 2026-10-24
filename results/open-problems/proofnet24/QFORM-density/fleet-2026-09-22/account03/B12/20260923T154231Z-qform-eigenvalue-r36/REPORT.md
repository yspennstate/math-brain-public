SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T15:42:31Z.
attacking: sign-resolved matrix-tail stability — arbitrary favorable spectrum is free, while only sign-hostile spectral tails consume matching signed reserve modes.

# account03/B12 r36 — adaptive two-sided spectral-tail compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Additional eigenvalue control  
Status: **PROVED SUPPORTING STABILITY THEOREMS / DESIGNATED account04-B12 RESULT APPLIED / NEWEST VOLUME RESULT APPLIED / FULL QFORM OPEN / NOT INDEPENDENTLY REVIEWED**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope and overlap audit

The owner target remains: for arbitrary independent real cap-one densities and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a dimension-free bound for the density of `X^T A X`, or produce a valid counterexample. Continuity is separate.

The early checkpoint of this run isolated the one-sided observation that positive spectral additions are free when protecting positive eigenvalues, and negative additions are free when protecting negative eigenvalues. A source search then found that this one-sided inertia principle is already present in `account02/B12` r23:

- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T021551Z-account02-B12-qform-r23/REPORT.md`,
- current readback source blob `6fa0d347657b0bbcc4885f9914b75e86a6fbb821`.

Accordingly, the one-sided fact is **not** claimed as new here. The retained result is the quantitative simultaneous two-sided spectral-profile compiler below: it optimizes separate hostile rank budgets for the positive and negative sides, pays only the first unreserved eigenvalue of the corresponding hostile positive/negative part, and then composes this with the designated `account04/B12` complementary-Schur factorization. This allows a first arbitrary signed spectral packet and a second arbitrary signed packet with independent positive/negative tail budgets.

No random quadratic remainder is declared independent or probabilistically small.

## 2. Source-valid dependencies actually used

### Designated partner: account04/B12

Canonical latest completed partner result found at publication time:

- repository `yspennstate/math-open-problems`,
- commit `3948d77b0bde5af1bd37cd7c975d4f540eba901b`,
- path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T081758Z-account04-B12-complementary-schur-shield-r4/REPORT.md`.

Its deterministic factorization is as follows. On an ACTUAL physical block, for

`H0=B+U Theta U^T`,

let `W` span `Ran U`, let `Z` span its physical orthogonal complement, set

`D=Z^T B Z`, `Rsh=(W^T B Z)D^{-1}`, `rho=||Rsh||op`,

and

`ell(rho)=(sqrt(rho^2+4)-rho)/2`.

Then in the orthogonal `[W,Z]` basis

`Hhat0 = L diag(S,D) L^T`, `L=[[I,Rsh],[0,I]]`,

with `sigma_min(L)=ell(rho)`. The partner used this to protect three singular modes of `D` through completely arbitrary symmetric `Theta`.

### Newest volume stability input

- commit `c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
- path `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For an ACTUAL original-coordinate cross block `M=M0+E`, if

`s3(M0)>=a`, `max_i(P_range(M0))_ii<=1/2`, `||E||op<=a/16`,

then the full ambient quadratic-plus-affine form has a continuous `C0` density and

`||p_Q||infinity <= 24 sqrt(3)e/(5a) < 23/a`.

All self blocks and outside couplings are arbitrary.

### Physical finite-core receiver

I use the already-completed finite-dimensional physical-fiber receiver repeatedly used in the current proof map: if an ACTUAL original-coordinate principal block of size `m` has at least three eigenvalues of modulus at least `g>0`, then after conditioning only on outside ORIGINAL coordinates,

`||p_Q||infinity <= 2 sqrt(6 pi m)/g`,

uniformly in the affine terms produced by outside couplings. This branch establishes essential boundedness; no continuity claim is imported unless the source explicitly supplies one.

## 3. Adaptive two-sided spectral-tail theorem

For a symmetric matrix `M`, write ordered eigenvalues

`lambda_1(M)>=...>=lambda_m(M)`.

Let

`H = H0 + R + T`,

where `H0=H0^T`, `T=T^T`, `||T||op<=delta`, and write the spectral positive/negative parts of the completely arbitrary second update as

`R=P-N`, `P=R_+>=0`, `N=R_->=0`.

Let

`n_1>=...>=n_m>=0`

be the eigenvalues of `N`, and

`p_1>=...>=p_m>=0`

those of `P`. Set `n_(m+1)=p_(m+1)=0` for endpoint notation.

Fix desired counts `u,v>=0`. Define

`Gamma_+(u) = max_{0<=r<=m-u} [ lambda_(u+r)(H0) - n_(r+1) ] - delta`,

when `u>0`, and

`Gamma_-(v) = max_{0<=s<=m-v} [ lambda_(v+s)(-H0) - p_(s+1) ] - delta`,

when `v>0`.

### Theorem 3.1 (`QFORM-SIGNED-ADAPTIVE-SPECTRAL-TAIL-COMPILER-v1`)

For every such decomposition,

`lambda_u(H) >= Gamma_+(u)` for `u>0`,

and

`lambda_v(-H) >= Gamma_-(v)` for `v>0`.

Consequently, if `u+v>=3` and every active `Gamma` is positive, then

`s3(H) >= min(active Gamma_+, active Gamma_-)`.

The first `r` negative eigenmodes of `R` can have arbitrary magnitude when protecting the positive side, while the entire positive part `P` is free. Independently, the first `s` positive eigenmodes can have arbitrary magnitude when protecting the negative side, while the entire negative part `N` is free. The optimizing `r` and `s` need not agree.

### Proof

Fix `r` in the positive-side range and spectrally truncate

`N=N_r+N_tail`, `rank N_r<=r`, `||N_tail||op=n_(r+1)`.

Set

`K=H0+P+T-N_tail`.

Because `P>=0`, Weyl monotonicity and the operator-norm perturbation inequality give

`lambda_(u+r)(K)
 >= lambda_(u+r)(H0)-delta-n_(r+1)`.

Now

`H=K-N_r`.

A symmetric perturbation of rank at most `r` satisfies the rank-interlacing inequality

`lambda_u(K-N_r) >= lambda_(u+r)(K)`.

Therefore

`lambda_u(H)
 >= lambda_(u+r)(H0)-delta-n_(r+1)`.

Maximize over `r`. This proves the positive formula.

For the negative formula write

`-H=(-H0)+N-P-T`

and repeat the same argument, with `N` now favorable and the positive part `P` hostile. QED.

### Why this is stronger than a sign-blind singular-tail estimate

A sign-blind bound pays the `(r+1)`-st singular value of the entire update. Here positive and negative tails are paid separately. A huge full-rank positive update does not enter `Gamma_+` at all, while a huge full-rank negative update does not enter `Gamma_-` at all. The theorem can simultaneously protect, for example, two positive and one negative final modes by different adaptive truncations.

## 4. Product-measure consequence on an ACTUAL physical core

Let `I` be a set of `m` ORIGINAL coordinates and apply Theorem 3.1 to the actual final compression `A[I,I]`. If for some `u+v>=3`

`g=min(active Gamma_+(u), active Gamma_-(v))>0`,

then that actual physical block has at least three eigenvalues of modulus at least `g`. Conditioning only on coordinates outside `I` leaves the coordinates in `I` mutually independent with density cap one; outside cross terms become affine coefficients. Hence

`boxed: ||p_(X^T A X)||infinity <= 2 sqrt(6 pi m)/g.`

All spectrum and couplings outside `I` remain arbitrary.

This is a deterministic matrix-tail stability result followed by original-coordinate conditioning. It is not a convolution or an independence-after-rotation argument.

## 5. Applying the completed account04/B12 factorization at an actual inequality

The partner factorization gives more than an unsigned singular-value shield. Its congruence form preserves signed Rayleigh subspaces quantitatively.

Let the complementary block `D` have positive eigenvalues

`d_1^+>=d_2^+>=...>0`

and negative eigenvalues whose magnitudes are

`d_1^->=d_2^->=...>0`.

Let

`H0=B+U Theta U^T`

with completely arbitrary symmetric `Theta`, under the partner hypotheses, and put `c=ell(rho)^2`.

For every `j` within the positive count of `D`,

`lambda_j(H0) >= c d_j^+`,

and for every `j` within the negative count,

`lambda_j(-H0) >= c d_j^-`.

Indeed, if `E_+` is a `j`-dimensional positive spectral subspace of `D`, then on the `j`-dimensional physical subspace `L^{-T}(0 direct_sum E_+)`, writing `y=L^T x`,

`x^T H0 x = y^T diag(S,D)y >= d_j^+ ||y||^2 >= c d_j^+ ||x||^2`.

The min-max principle gives the positive inequality. The negative inequality is identical for `-H0`.

Now add a SECOND arbitrary signed packet

`R=P-N`

and a dense deterministic matrix tail `T`, `||T||op<=delta`. Substitution into Theorem 3.1 yields the concrete partner-composed inequalities

`boxed:
Gamma_+^Schur(u)
 >= max_r [ c d_(u+r)^+ - n_(r+1) ] - delta,`

`boxed:
Gamma_-^Schur(v)
 >= max_s [ c d_(v+s)^- - p_(s+1) ] - delta.`

This is an equation-level application of `account04/B12@3948d77...`. The first packet `U Theta U^T` has arbitrary rank allowed by `U`, arbitrary signs and arbitrary magnitude. In the second packet, large hostile modes are spent by signed reserve count; favorable spectrum is free; only the first unreserved hostile tail eigenvalue is charged.

### Explicit mixed-sign example

Take an ACTUAL seven-coordinate core split as `W` of dimension two and `Z` of dimension five. Let

`D=diag(4,4,4,-4,-4)`,

and choose the partner cross row so that `rho=1/4`. Then

`ell(1/4)^2 = 0.7793044453656702...`,

so both the three positive and two negative complementary reserves are protected at scale

`g0 = 4 ell(1/4)^2 = 3.117217781462681...`.

Protect `u=2` positive and `v=1` negative final modes. Spend one hostile mode on each side (`r=s=1`). Allow:

- `Theta` to be an arbitrary real symmetric `2 x 2` matrix, with unbounded eigenvalues of either sign;
- the largest eigenvalue of `N` to be arbitrarily large, but `n_2<=1/4`;
- the largest eigenvalue of `P` to be arbitrarily large, but `p_2<=1/4`;
- a dense arbitrary-rank symmetric tail `T` with `||T||op<=1/4`.

Then

`Gamma_+^Schur(2)>=g0-1/4-1/4`,

`Gamma_-^Schur(1)>=g0-1/4-1/4`,

so

`g>=2.617217781462681...`.

The actual seven-coordinate final block therefore has two positive eigenvalues at least `g` and one negative eigenvalue at most `-g`. In particular it lies in the owner's target spectral class. The physical receiver gives

`boxed: ||p_Q||infinity <= 2 sqrt(42 pi)/g
                          = 8.777881526690145... .`

This example contains TWO arbitrary signed spectral packets, and the density estimate never isolates either packet as an independent random summand.

## 6. Applying the newest volume theorem to a different signed-tail footprint

There is a complementary continuous-density branch. Let `I,J` be original-coordinate banks and let

`M0=a U`, `a>0`,

where `U` has three orthonormal columns and `max_i(P_range U)_ii<=1/2`. Thus `s3(M0)=a`.

Let a signed added matrix have spectral decomposition `R=P-N`. Strip arbitrary top spectral packets `P_top,N_top` and assume only that their **cross footprints vanish** on this cut:

`P_top[I,J]=0`, `N_top[I,J]=0`.

Let the residual positive/negative tails have operator norms

`||P_tail||op<=beta_-`, `||N_tail||op<=beta_+`.

Then for the actual cross perturbation

`E=R[I,J]`

we have the matrix-level inequality

`||E||op
 <= ||P_tail[I,J]||op+||N_tail[I,J]||op
 <= beta_-+beta_+`.

Therefore, whenever

`beta_-+beta_+ <= a/16`,

the newest volume-stability theorem at `c2414ef...` applies to the **final** cross block and gives

`boxed: ||p_Q||infinity <= 24 sqrt(3)e/(5a) < 23/a.`

This branch has a continuous `C0` density. The stripped positive and negative packets may have arbitrarily large eigenvalues; they cost zero because their actual cross footprint on the chosen product-preserving cut is zero. The tails are charged only as a deterministic matrix perturbation to the final cross block, never as a small random quadratic variable.

## 7. Rigorous-computation checks

`CHECK.py` in this run directory performs two finite deterministic sanity suites using only matrix eigenvalue computations.

1. 5,000 random instances of Theorem 3.1, with mixed signs, independent positive/negative hostile budgets, arbitrarily large leading hostile modes, residual full-rank tails and dense symmetric `T`: zero violations. The smallest observed positive-branch and negative-branch margins were respectively

`0.05298600911339424`, `0.08046270382134502`.

2. 5,000 random instances of the partner congruence composition with a `2+5` physical split, three positive and two negative complementary modes, arbitrary active Schur block, random shear up to `rho=1/2`, a second signed packet with one arbitrarily large hostile mode on each side, and a dense tail: zero pre-composition and zero final violations. The smallest observed signed-profile margins before the second packet were

`4.56258206460447e-06`, `4.868006445057915e-06`,

and after the second packet

`0.1186987747555408`, `1.9436903442987972`.

These are consistency checks only. The proofs above are analytic and do not rely on numerical sampling.

## 8. Correction audit

The current live correction inbox was re-read before publication. This argument does not use:

- pointwise law-uniform van-der-Corput decay;
- independence after diagonalizing or rotating `A`;
- arbitrary-joint coarea;
- naive fiber-supremum integration;
- a universal good physical minor or universal rank-three cross cut;
- a claim that small operator norm makes `X^T T X` a small random variable;
- Monte Carlo evidence as proof.

All rotations in Sections 3 and 5 are deterministic matrix algebra only. Probability enters only after an ACTUAL original-coordinate physical/cross certificate has been proved for the final matrix.

## 9. Remaining implication

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.**

The new compiler answers the assigned stability question once a physical signed reserve or a diffuse cross carrier is already present. The bare condition `s3(A)>=1` still has to force one of these product-preserving certificates, or one of the already-paid grouped-bank/hub/ridge/pair mechanisms. In particular, exactly three global large modes need not supply reserve against even one hostile direction on a fixed bounded physical core.

The next B12 step should therefore be structural rather than another tail perturbation estimate: prove a reserve-or-cross-volume-or-grouped-bank alternative that starts only from the bare global three-eigenvalue hypothesis and preserves original-coordinate product structure.

Continuity: proved for the newest-volume branch in Section 6; only essential boundedness is asserted for the signed physical-core/Schur branch in Sections 3-5. Continuity for the unrestricted target remains open.
