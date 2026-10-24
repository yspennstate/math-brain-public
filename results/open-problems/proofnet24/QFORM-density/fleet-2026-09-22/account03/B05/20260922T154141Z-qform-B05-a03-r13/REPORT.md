# account03/B05 — pair-Pluecker collision classification and a star-endpoint double-Wiener coarea closure

**Run:** `20260922T154141Z-qform-B05-a03-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Quadratic coarea bound  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Scope, corrections, and exact starting debt

The owner target remains the full arbitrary-dimensional statement: independent real physical coordinates `X_i` with probability densities `0<=f_i<=1`, and a real symmetric `A` with at least three eigenvalues of modulus at least one. The goal is one universal bound for the essential density of `Q=X^TAX`; continuity is tracked separately. This report does **not** claim the full target.

The previous B05 report

`yspennstate/math-open-problems@332f29e335274f2b3f81ccf92d62443b928c66cd`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260922T144946Z-qform-B05-a03-r12/REPORT.md`

proved the local pair-sectional coarea estimate in the exact-rank-three heavy-isotropic branch. If the transverse two-frame has Pluecker coordinate

`Delta_jk = y_j z_k-y_k z_j !=0`,

then one obtains a valid bound proportional to `|Delta_jk|^(-2/3)`. Since

`sum_{j<k} Delta_jk^2=1`,

but the largest individual minor may vanish with dimension, the first unpaid step was `QFORM-PAIR-PLUCKER-AGGREGATION-v1`: aggregate before paying a reciprocal local minor.

The live corrections forbid replacing this by a generic conditional-density cap, a post-rotation independence assertion, an unrestricted fiber supremum, or a single uniformly good physical minor. Those invalid mechanisms are not used below.

The exact assigned partner is `account04/B05`. Fresh source checks found no completed current-QFORM report or handoff for that slot, so no partner result is fabricated. Compatible completed sources actually used are:

1. account01/B06 `QFORM-WEIGHTED-2D-PROJECTION-v1`, canonical mathematics
   `yspennstate/math-open-problems@0b523077616e4d1a2c959ddca036cfd895067460:proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260922T130334Z-qform-r11/REPORT.md`, especially its diffuse two-dimensional Fourier-Wiener bound;
2. account01/B06 `QFORM-MODULATED-1D-WIENER-BANK-v1`, canonical mathematics
   `yspennstate/math-open-problems@1c155008146adf84eb705047eea1c46c312b3927:proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260922T140612Z-qform-r12/REPORT.md`;
3. account01/B10 `QFORM-ZERO-DIAGONAL-TRIPLE-v1`, canonical mathematics
   `yspennstate/math-open-problems@3be6045911d80a0881d7a1c3631871643f52434c:proofnet24/QFORM-density/fleet-2026-09-22/account01/B10/20260922T131954Z-account01-B10-QFORM-r12/REPORT.md`;
4. account02/B10 scaled dependent-pair hyperbolic-square theorem,
   `yspennstate/math-open-problems@11c9ae19edfd07e3a0bd4053a910667c20e721ab:proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260922T130225Z-b10-qform-r11/REPORT.md`;
5. compatible account04 mathematics actually applied in Section 7: account04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`,
   `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3:proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

## 1. The pair-Pluecker graph has an exact collision statistic

Let `(y_j,z_j)` be a Parseval two-frame:

`sum_j [[y_j],[z_j]] [y_j,z_j] = I_2`.

Put

`w_jk = Delta_jk^2`,  `Delta_jk=y_jz_k-y_kz_j`,

and

`d_j = sum_{k!=j} w_jk = y_j^2+z_j^2`.

Cauchy--Binet gives `sum_{j<k}w_jk=1`, so the `w_jk` are a probability law on unordered physical pairs. Let `P,Q` be independent pairs sampled from this law and define the ordered disjoint collision mass

`R_2 = P(P cap Q = empty)`.

### Theorem 1.1 — `QFORM-PAIR-PLUCKER-COLLISION-IDENTITY-v1`

One has the exact identity

`boxed( R_2 = 1 - sum_j d_j^2 + sum_{j<k} w_jk^2. )`                 (1.1)

#### Proof

Let `A_j={j in P cap Q}`. Then `P(A_j)=d_j^2`. If `j!=k`, the event `A_j cap A_k` occurs exactly when `P=Q={j,k}`, and therefore has probability `w_jk^2`. No three distinct events `A_j` can occur simultaneously because both `P` and `Q` have cardinality two. Inclusion-exclusion is therefore exact:

`P(P cap Q != empty)=sum_j d_j^2-sum_{j<k}w_jk^2`.

Subtract from one. QED.

This identifies a missing factor that total Pluecker mass alone cannot see: **matching/disjointness mass**. A star can have `sum w=1` while `R_2=0`.

## 2. Exact zero-disjointness classification: only star or triangle

Ignore zero transverse rows. Declare two nonzero rows equivalent when they are parallel. Since `Delta_jk!=0` exactly when the two rows are nonparallel, the support graph

`G={ {j,k}: w_jk>0 }`

is a complete multipartite graph on the parallelism classes.

### Theorem 2.1 — `QFORM-PAIR-PLUCKER-ZERO-MATCHING-CLASSIFICATION-v1`

If `R_2=0`, then `G` is one of the following:

1. a **star**: exactly two parallelism classes occur and one class consists of a single physical row; or
2. a **triangle**: exactly three nonzero rows occur, in three distinct parallelism classes.

#### Proof

`R_2=0` means no two positive-weight edges are disjoint, so `G` has matching number one. For a complete bipartite graph `K_{a,b}`, matching number one forces `min(a,b)=1`, hence a star. If there are at least three parts and at least four vertices, then two disjoint edges exist: with four singleton parts use edges between parts `(1,2)` and `(3,4)`; with three parts and at least four vertices, one part contains two vertices, and those two can be paired with vertices from the other two parts. Hence the only multipartite possibility with at least three parts is three singleton parts, namely a triangle. QED.

So the worst possible failure of disjoint pair aggregation has rigid projective geometry; it is not an arbitrary diffuse frame.

## 3. Triangle endpoint closes immediately

Return to the exact-rank-three heavy-isotropic state

`A=U Lambda U^T`, `U^TU=I_3`, `u_i=sqrt(c)e`, `c>1/2`,
`e^T Lambda e=0`, `|det Lambda|>=1`.

In the orthogonal transverse plane write residual rows as

`u_j=s_j e+y_j f+z_j g`.

Account01/B06 proves for every residual pair

`|det A[{i,j,k},{i,j,k}]|
 = c |det Lambda| Delta_jk^2
 = c |det Lambda| w_jk`.                                              (3.1)

If the zero-disjointness support is a triangle, its three edge weights sum to one, so some `w_jk>=1/3`. Therefore

`|det A[{i,j,k}]| >= c|det Lambda|/3 >1/6`.

The selected physical triple has `A_ii=0`. Applying the completed account01/B10 zero-diagonal-triple theorem gives

`boxed(
 ||p_Q||_infinity
 < 3*2^(2/3)*6^(1/3)
 = 8.6534974218... .
)`                                                                    (3.2)

Thus the triangle endpoint of `R_2=0` is fully paid, with arbitrary outside couplings. Continuity is not asserted by this local theorem.

## 4. Star geometry forces an original-coordinate transverse singleton

Suppose instead the zero-disjointness support is a star. Let the singleton parallelism class be row `j`. Because the transverse frame is Parseval, the star is more rigid than the graph statement alone.

### Lemma 4.1 — `QFORM-PAIR-PLUCKER-STAR-NORMAL-FORM-v1`

After an orthogonal change of basis **only in the two-dimensional spectral bookkeeping plane**, one has

`(y_j,z_j)=(1,0)`,

and for every `k!=i,j`,

`(y_k,z_k)=(0,z_k)`,  `sum_k z_k^2=1`.                               (4.1)

Moreover the leakage coefficients satisfy

`s_j=0`,  `sum_k s_k z_k=0`,  `sum_k s_k^2=1-c`.                     (4.2)

Hence

`Y=X_j`, `T=sum_k s_kX_k`, `Z=sum_k z_kX_k`,

and the bank `(T,Z)` uses physical coordinates disjoint from both `X_i` and `X_j`.

#### Proof

The nonzero transverse rows lie on exactly two lines. Write their total squared masses as `alpha,beta` and the angle between the unit line directions as `theta`. Parseval gives

`alpha uu^T+beta vv^T=I_2`.

Taking trace and determinant yields

`alpha+beta=2`, `alpha beta sin^2(theta)=1`.

But `alpha beta<=1` by AM-GM and `sin^2(theta)<=1`; equality in their product forces `alpha=beta=1` and orthogonal line directions. Since one class is the singleton row `j`, its row has norm one, giving (4.1). The full Parseval orthogonality identities `sum s_ky_k=0`, `sum s_kz_k=0`, `sum s_k^2=1-c` then give (4.2). QED.

Write `delta=1-c`. In this star normal form the heavy-isotropic quadratic is

`Q = 2B(sqrt(c)X_i+T)X_j + rX_j^2 +2 sigma X_j Z + tau Z^2`,           (4.3)

with

`B^2|tau|=|det Lambda|>=1`.                                          (4.4)

This is the exact zero-matching obstruction left by total pair-Pluecker aggregation.

## 5. A double-Wiener Fresnel profile for a diffuse leakage-square bank

Assume first `0<delta<1/2`. Normalize

`S=T/sqrt(delta)`.

Then the coefficient vectors of `(S,Z)` form an orthonormal two-frame. Assume the normalized bank is diffuse:

`boxed( s_k^2/delta + z_k^2 <=1/2  for every bank coordinate k. )`    (5.1)

Let `p(s,z)` be the density of `(S,Z)` and

`Phi(xi,eta)=E exp(i xi S+i eta Z)`.

The completed account01/B06 two-dimensional Wiener theorem gives

`int_R2 |Phi(xi,eta)| dxi deta <= (2pi)^2 e`.                         (5.2)

The completed modulated one-dimensional bank theorem gives, because `z_k^2<=1/2`,

`sup_xi int_R |Phi(xi,eta+kappa xi)| deta <=2pi sqrt(e)`              (5.3)

for every fixed real shear `kappa`; this is simply its arbitrary-frequency-shift conclusion applied coordinatewise.

For `t!=0` define

`F_t(xi)
 = E exp( i xi(S+kappa Z) + i t tau Z^2 )`.                           (5.4)

### Lemma 5.1 — `QFORM-DOUBLE-WIENER-FRESNEL-PROFILE-v1`

Under (5.1), for every `kappa` and `t!=0`,

`||F_t||_infinity <= sqrt(pi e) |tau t|^(-1/2)`,                     (5.5)

`||F_t||_1 <= 2 pi^(3/2) e |tau t|^(-1/2)`,                          (5.6)

and therefore

`boxed(
 ||F_t||_2 <= sqrt(2) pi e^(3/4) |tau t|^(-1/2).
)`                                                                    (5.7)

#### Proof

For fixed `xi`, let

`g_xi(z)=int p(s,z) exp(i xi(s+kappa z)) ds`.

Its Fourier transform in `z` is `Phi(xi,eta+kappa xi)`. Pairing `g_xi` with the chirp `exp(i t tau z^2)` and using

`| Fourier[exp(i t tau z^2)](eta) |=sqrt(pi/|tau t|)`

(with standard Gaussian regularization if desired) gives (5.5) from (5.3).

Integrating the same inequality before taking the `xi` supremum and using the shear-invariant full Wiener norm (5.2) gives (5.6). Finally

`||F_t||_2^2 <= ||F_t||_infinity ||F_t||_1`

and (5.5)--(5.6) give (5.7). QED.

The gain over a single Fresnel payment is crucial: both the `L^infinity_xi` and `L^1_xi` profile norms carry the factor `|t|^(-1/2)`, so the profile has an `L^2_xi` payment of the same order rather than only `|t|^(-1/4)`.

## 6. Star-diffuse branch: integrable `|t|^(-3/2)` decay and a continuous density

In (4.3) set

`a=B sqrt(delta)`, `kappa=sigma/a`.

For fixed `u=X_j`, the bank phase is

`2u(BT+sigma Z)+tau Z^2
 =2au(S+kappa Z)+tau Z^2`.

Thus, with `F_t` from Section 5,

`A_t(u):=E_bank exp(i t[2u(BT+sigma Z)+tau Z^2])
       =F_t(2 a t u)`.                                                (6.1)

By scaling (5.7),

`||A_t||_2
 <= pi e^(3/4) |a|^(-1/2)|tau|^(-1/2)|t|^(-1).`                    (6.2)

The full characteristic function is exactly

`phi_Q(t)
 =int f_j(u) exp(i t r u^2)
       hat f_i(2B sqrt(c)t u) A_t(u) du`.                             (6.3)

Because `0<=f_j<=1`, Cauchy--Schwarz and Plancherel give

`|phi_Q(t)|
 <= ||hat f_i(2B sqrt(c)t ·)||_2 ||A_t||_2`

and

`||hat f_i(2B sqrt(c)t ·)||_2
 <= sqrt(pi)|B|^(-1/2)c^(-1/4)|t|^(-1/2)`.                           (6.4)

Combining (6.2)--(6.4) and `a=B sqrt(delta)` proves:

### Theorem 6.1 — `QFORM-PAIR-PLUCKER-STAR-DIFFUSE-CLOSE-v1`

Under the exact-rank-three heavy-isotropic star normal form, with `0<c<1` and the normalized bank diffuseness (5.1),

`boxed(
 |phi_Q(t)|
 <= K |t|^(-3/2),

 K=pi^(3/2)e^(3/4)[c(1-c)]^(-1/4)
   (B^2|tau|)^(-1/2).
)`                                                                    (6.5)

Hence `phi_Q in L^1(R)`, the law of `Q` has a bounded **continuous** density, and

`boxed(
 ||p_Q||_infinity
 <=3 sqrt(e)[c(1-c)]^(-1/6)(B^2|tau|)^(-1/3)
 <=3 sqrt(e)[c(1-c)]^(-1/6).
)`                                                                    (6.6)

#### Proof of the density constant

Use `|phi_Q(t)|<=min(1,K|t|^(-3/2))`. At `T=K^(2/3)`,

`int_R |phi_Q(t)|dt
 <=2T+2K int_T^infinity t^(-3/2)dt
 =6K^(2/3)`.

Fourier inversion gives `||p_Q||_infinity<=3K^(2/3)/pi`, which is exactly (6.6). The same `L^1` characteristic-function bound gives continuity. QED.

This theorem closes a genuine endpoint of the previous pair-Pluecker aggregation failure: even when **every positive pair minor intersects every other one**, no single pair needs to be selected if the remaining normalized leakage-square bank is diffuse.

## 6.5. The leverage-one star endpoint `c=1`

If `c=1`, then `T=0` identically. In the star normal form, `X_i`, `X_j`, and the bank variable `Z` are mutually independent, and the one-dimensional product-marginal theorem gives

`||p_Z||_infinity<=sqrt(2)`.

Complete the square in `Z`:

`Q=2B X_i X_j +(r-sigma^2/tau)X_j^2
  +tau(Z+(sigma/tau)X_j)^2`.

Apply the completed account02/B10 dependent-pair hyperbolic-square theorem with independent scalar `X_i`, pair `(X_j,Z)` of joint density cap at most `sqrt(2)`, `a=B`, and `b=tau`. Since `B^2|tau|>=1`,

`boxed( ||p_Q||_infinity <= 6. )`                                    (6.7)

Thus the literal leverage-one star endpoint is also paid. Continuity is not asserted by this argument.

## 7. Actual compatible account04 application: one physical square extension

The exact assigned account04/B05 artifact is absent, but a completed compatible account04 theorem can be applied without changing the target or invoking a prohibited route.

Let `R` be any star-diffuse variable from Theorem 6.1, with

`M=3 sqrt(e)[c(1-c)]^(-1/6)(B^2|tau|)^(-1/3)`.

Suppose a larger quadratic form has one additional **original physical coordinate** `V`, with scalar pivot `gamma!=0`, such that after conditioning all other outside coordinates and completing the square only in `V`, its conditional form is

`R + gamma(V+m)^2`,

where `m` is measurable in the non-`V` coordinates. Because `V` is an original independent coordinate with density cap one, the conditional density of `V+m` given the base value is a mixture of translates and remains at most one. Account04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` therefore applies literally and gives

`boxed(
 ||p||_infinity
 <= 2 sqrt(M/|gamma|)
 =2 sqrt(3) e^(1/4)|gamma|^(-1/2)
   [c(1-c)]^(-1/12)(B^2|tau|)^(-1/6).
)`                                                                    (7.1)

This is a source-valid one-extra-square extension of the new coarea closure. It is not claimed to reduce an arbitrary complementary spectrum to this form.

## 8. What the first aggregation debt has become

The original debt `sum Delta_jk^2=1` versus `max Delta_jk ->0` is now sharper.

1. The exact collision statistic (1.1) shows that total pair mass is insufficient; the first additional factor is `R_2`, the disjoint/matching mass.
2. At the extreme `R_2=0`, the support is **only star or triangle**.
3. Triangle is universally closed by a physical zero-diagonal triple.
4. Star is closed at `c=1`, and for `0<c<1` whenever the normalized leakage-square bank `(s/sqrt(1-c),z)` is diffuse.

Therefore the first remaining coarea implication is no longer an unspecified multi-pair average. It is the quantitative stability problem

### `QFORM-PAIR-PLUCKER-MATCHING-STABILITY-v1` — OPEN

When `R_2` is small but nonzero, either convert its disjoint pair mass into a dimension-free paid bank **before** local reciprocal determinants are introduced, or prove that the transverse Parseval frame is quantitatively close to a star/triangle endpoint and stabilize the closures above. In the star collar, the only endpoint not paid by Theorem 6.1 is a **localized normalized leakage-square bank**, i.e. some

`s_k^2/(1-c)+z_k^2>1/2`.

This is consistent with the team's independently observed profile-overlap/four-direction collar. Arbitrary extra spectrum remains a separate interaction debt.

## 9. Status

**PROVED in this run**

- `QFORM-PAIR-PLUCKER-COLLISION-IDENTITY-v1`, exact formula (1.1).
- `QFORM-PAIR-PLUCKER-ZERO-MATCHING-CLASSIFICATION-v1`, star/triangle rigidity.
- triangle endpoint density bound `<8.654`.
- `QFORM-DOUBLE-WIENER-FRESNEL-PROFILE-v1`, simultaneous `L^infinity`, `L^1`, and `L^2` profile payments.
- `QFORM-PAIR-PLUCKER-STAR-DIFFUSE-CLOSE-v1`, continuous density with explicit bound (6.6).
- leverage-one star endpoint bound `<=6`.
- actual account04/B18 one-extra-physical-square consequence (7.1).

**NOT PROVED**

- the full exact-rank-three theorem in all collars;
- the quantitative small-`R_2` stability/aggregation implication;
- the star endpoint with a localized normalized leakage-square bank for arbitrary `c<1`;
- the arbitrary complementary-spectrum implication;
- the full owner QFORM theorem.

No Gaussianity, moments, support diameter, connected support, spectral-coordinate independence, or law-uniform one-dimensional Fresnel decay is used. Every probabilistic independence statement is in original disjoint physical coordinate banks.
