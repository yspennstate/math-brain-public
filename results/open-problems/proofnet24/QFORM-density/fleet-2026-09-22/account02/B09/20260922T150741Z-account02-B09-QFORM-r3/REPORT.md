# account02/B09 — diffuse-bank bilinear absorption before local pivot payment

**Run:** `20260922T150741Z-account02-B09-QFORM-r3`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, OWNER CONTROL revision `2026-09-22.5`  
**Assignment:** Bilinear block mechanism  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target, corrections, and first unpaid implication

The sole target remains the full arbitrary-product-law statement: for every dimension, independent real coordinates `X_i` with probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound on the density of `X^T A X`, or give a valid counterexample. No moment, support, sign, or post-rotation independence assumption is permitted.

Live corrections consumed before this report include the failures of law-uniform pointwise Fresnel decay, naive spectral-fiber suprema, a rank-two cross block alone at `L^infinity`, transformed conditional density caps, a universal physical scalar-pivot/rank-two-Schur extraction, and a local-principal-block/rank-three-cross-cut dichotomy.

The previous B09 result `QFORM-RANK2-SCHUR-PIVOT-v1` pays a rank-two Schur cross once one useful *physical scalar pivot* has already been found, but the source-valid family recorded in `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` shows that the three-large-eigenvalue hypothesis does not force such a pivot. Thus the first unpaid implication at the start of this run was:

> `QFORM-SCHUR-CROSS-OR-DIFFUSE-AGGREGATION-v2`: aggregate the third spectral resource before paying a reciprocal physical-coordinate pivot cost, while retaining a disjoint original-coordinate product decomposition and a direct `O(|I|)` interval bound.

This run makes that step concrete: it replaces the physical scalar pivot by a **diffuse scalar bank projection**, and it also proves a one-cross-plus-square absorption theorem allowing arbitrary same-bank quadratic structure on the coefficient side.

## 2. Source-pinned completed results actually used

### Named partner: account03/B09

Latest completed partner report observed before publication:

- repository `yspennstate/math-open-problems`;
- commit `fb2f074c2fe11dc9343397ae0a06f20bcc971f65`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/account03-B09-20260922T144807Z-qform11/REPORT.md`.

It proves `QFORM-CROSS-SQUARE-CAPS-v1`: for independent scalar `U,V,W` with density caps `M_U,M_V,M_W`,

`T=2 beta U V + gamma W^2 + affine`,

has

`||p_T||_infinity <= 4 sqrt(2) M_W sqrt(M_U M_V)/sqrt(|beta gamma|)`,

and its Lemma 2.1 gives the sharp-enough half-potential inequality

`sup_s E |s-Y|^(-1/2) <= 2 sqrt(2M)` whenever `||p_Y||_infinity<=M`.

The same report applies the Livshyts--Paouris--Pivovarov product-marginal theorem: a `k`-dimensional orthogonal marginal of a cap-one product density has density at most `2^(k/2)`.

I apply the partner half-potential inequality twice in Theorem 3.1 below, and its LPP bank caps in Theorem 4.1. These are actual inequalities in the proof, not background citations.

### Dependent-square smoothing

Account01/B11, canonical report commit `2279571f59ade7a9ec478af1e4818f6c117ac224`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/QFORM-B11-20260922T121344Z/REPORT.md`, proves `QFORM-DEPENDENT-SQUARE-L3-SMOOTHING-v1`:

if `R` has density with `||p_R||_3=M` and, conditionally on `R=r`, `V` has density cap one, then

`||p_{R+dV^2}||_infinity <= 4 |d|^(-1/2) M^(3/4)`.

By scaling, if the conditional cap is `M_V`, the right side becomes

`4 M_V |d|^(-1/2) M^(3/4)`.

### Previous B09 rank-two cross ladder

The preceding account02/B09 report, commit `a47c679eb9f7788b5c3c2a900ce516ec11de8d9b`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260922T124417Z-account02-B09-QFORM-r2/REPORT.md`, proves finite-`p` smoothing for an original-coordinate rank-two cross block. The new bank theorem below is its low-dimensional marginal analogue and reduces exactly to the same `L^3` constant under the LPP caps.

## 3. Arbitrary coefficient-side structure survives cross-square smoothing

### Theorem 3.1 — `QFORM-CROSS-SQUARE-COEFFICIENT-SIDE-ABSORPTION-v1`

Let three pairwise disjoint original-coordinate banks generate independent random objects `Z`, `V`, `W`. Let

`U=u(Z)`

be a real linear projection of the first bank, with density cap `M_U`; let `V,W` have scalar density caps `M_V,M_W`. Let `H(Z)` be **arbitrary measurable**, possibly a quadratic form in all coordinates of the first bank and therefore possibly dependent on `U`. Let `beta,gamma` be nonzero. Then for arbitrary real affine coefficients,

`T = H(Z) + 2 beta U V + gamma W^2 + r U + s V + t W + q`

has an essentially bounded density satisfying

`boxed(
 ||p_T||_infinity
 <= 4 sqrt(2) M_W sqrt(M_U M_V)/sqrt(|beta gamma|).
)`                                                               (3.1)

Moreover `T` has a continuous density.

#### Proof

Translate `U,V,W` to absorb the affine terms `rU+sV+tW`; translations preserve the relevant density caps. The arbitrary first-bank term remains an arbitrary measurable function of `Z`, so it suffices to treat

`T=H(Z)+2 beta U V+gamma W^2`.

The square transform obeys, for either sign of `gamma`, the pointwise density majorant

`p_{gamma W^2}(y) <= M_W |gamma|^(-1/2)|y|^(-1/2)`

on the appropriate half-line. Hence

`p_T(x)
 <= M_W |gamma|^(-1/2)
    E |x-H(Z)-2 beta U V|^(-1/2)`.                               (3.2)

Condition on the whole first bank `Z=z`, so `H` and `U=u` are fixed. When `u!=0`, the variable `2 beta u V` has density cap

`M_V/(2|beta u|)`.

Applying the named partner's half-potential inequality gives, uniformly in the translated center,

`E_V |x-H(z)-2 beta u V|^(-1/2)
 <= 2 sqrt(M_V/(|beta u|)).`                                      (3.3)

The exceptional event `U=0` has probability zero because `U` has a density. Averaging (3.3) in `Z` and applying the same partner half-potential inequality to `U` at center zero gives

`E |U|^(-1/2) <= 2 sqrt(2M_U)`.                                  (3.4)

Combining (3.2)--(3.4) proves (3.1).

For continuity, the residual `H(Z)+2 beta U V` has an `L^1` density: condition on `Z`; except on the null event where the coefficient of `V` vanishes, it is a translate/scale of the density of `V`, and mixing preserves absolute continuity and total mass one. It is independent of `W`. The square term `gamma W^2` also has an `L^1` density. Their convolution belongs to `C_0(R)`. QED.

### Disjoint-bank consequence

If `U,V,W` are unit linear projections of three disjoint cap-one product banks, LPP gives

`M_U,M_V,M_W <= sqrt(2)`.

Therefore

`boxed(
 ||p_T||_infinity <= 8 sqrt(2)/sqrt(|beta gamma|).
)`                                                               (3.5)

The point of (3.5) is not its constant: unlike the partner's exact cross-square normal form, the entire coefficient-side bank may carry an arbitrary quadratic `H(Z)` correlated with `U`.

### Target-level diffuse family outside the literal partner normal form

Let `m` be even. On a physical bank `I` of size `m`, choose two orthonormal dense vectors `a,b`; on disjoint banks `J,K`, choose unit dense vectors `c,e`. Put

`U_1=<a,X_I>`, `U_2=<b,X_I>`, `V=<c,X_J>`, `W=<e,X_K>`

and

`Q_m = -U_2^2 + 2 U_1 V + W^2`.                                  (3.6)

The effective quadratic matrix on `(U_1,U_2,V,W)` has spectrum

`{1,-1,-1,1}`.

Thus every `Q_m` lies in the owner's target class. Taking all vector coordinates of magnitude `m^(-1/2)` makes every physical matrix coefficient `O(1/m)`, so no fixed local coefficient carries the resource. Equation (3.5), with `H=-U_2^2`, nevertheless gives

`boxed( ||p_{Q_m}||_infinity <= 8 sqrt(2) )`                      (3.7)

for every `m` and every allowed input law. Here `U_1,U_2` may be dependent because they come from the same physical bank; Theorem 3.1 was designed to retain exactly that dependence.

## 4. A diffuse bank can replace the physical scalar pivot

The previous physical-pivot theorem becomes dimensionally expensive when the third direction is spread across many coordinates. The next theorem aggregates that direction first.

### Lemma 4.1 — rank-two cross `L^p` ladder for bounded two-dimensional bank marginals

Let `U,V in R^2` be independent random vectors with probability densities bounded by `M_U,M_V`. Let `N` be an invertible `2 x 2` matrix. Allow arbitrary measurable quadratic-affine phases on each side:

`R=q_U(U)+2U^T N V+q_V(V)`.

Then for every `2<=p<infinity`,

`boxed(
 ||p_R||_p
 <= p^(1-1/p)
    (M_U M_V)^((1-1/p)/2)
    |det N|^(-(1-1/p)/2).
)`                                                               (4.1)

In particular,

`boxed(
 ||p_R||_3
 <= 3^(2/3)(M_U M_V)^(1/3)|det N|^(-1/3).
)`                                                               (4.2)

#### Proof

Put complex amplitudes `a_t(u)=p_U(u)e^{itq_U(u)}` and `b_t(v)=p_V(v)e^{itq_V(v)}`. Two-dimensional Plancherel gives

`|phi_R(t)|
 <= pi sqrt(M_U M_V)/(|t| sqrt(|det N|))`.                        (4.3)

Indeed `||a_t||_2<=sqrt(M_U)`, `||b_t||_2<=sqrt(M_V)`, and the change of variables `xi=2tNv` has Jacobian `4t^2|det N|`. With the trivial `|phi_R|<=1`, set

`C=pi sqrt(M_U M_V)/sqrt(|det N|)`.

For `q=p/(p-1)`,

`||phi_R||_q^q <= 2Cp`.

Inverse Hausdorff--Young in the convention `hat f(t)=int e^{itx}f(x)dx` gives

`||p_R||_p <= (2pi)^(-1/q)||phi_R||_q`,

which simplifies exactly to (4.1). QED.

### Theorem 4.2 — `QFORM-DIFFUSE-BANK-SCHUR-PIVOT-v1`

Let the original physical coordinates be split into four disjoint groups `I,J,K,R`. Condition on the outside block `R`. From `I` and `J` take orthonormal two-dimensional linear projections

`U in R^2`, `V in R^2`,

and from `K` take a unit scalar projection `W`. Assume all dependence of the selected quadratic form on the three selected banks factors through `(U,V,W)`. After outside conditioning write its quadratic matrix as

`[[B,   M, r],
  [M^T, C, s],
  [r^T, s^T,d]]`,                                                (4.4)

where `B,C` are symmetric `2 x 2`, `M` is `2 x 2`, `r,s in R^2`, and `d!=0`. Define the scalar-bank Schur cross

`N=M-rs^T/d`.                                                     (4.5)

If `det N !=0`, then the full quadratic form has an essentially bounded density and

`boxed(
 ||p_Q||_infinity
 <= 8 sqrt(3) |d|^(-1/2)|det N|^(-1/4).
)`                                                               (4.6)

The estimate is uniform in all outside conditioning and hence holds unconditionally.

#### Proof

The original coordinate banks are disjoint, so before any internal orthogonal projection the three bank random vectors are independent. LPP gives their selected marginal caps

`M_U<=2`, `M_V<=2`, `M_W<=sqrt(2)`.                              (4.7)

Complete the square in the scalar bank projection `W`:

`Q=d(W+theta(U,V))^2+R_0(U,V)`,                                  (4.8)

where `theta` is affine and the cross block of `R_0` is precisely `N` in (4.5). Lemma 4.1 and (4.7) give

`||p_{R_0}||_3
 <= 3^(2/3) 4^(1/3)|det N|^(-1/3)
 = 6^(2/3)|det N|^(-1/3).`                                       (4.9)

Set `W'=W+theta(U,V)`. Conditional on `R_0=rho`, the density of `W'` is a mixture of translates of the original density of `W`, so its conditional cap is still at most `sqrt(2)`. Apply the scaled account01/B11 dependent-square lemma:

`||p_Q||_infinity
 <=4 sqrt(2)|d|^(-1/2)
      [6^(2/3)|det N|^(-1/3)]^(3/4)
 =8 sqrt(3)|d|^(-1/2)|det N|^(-1/4).`

This is (4.6). No rotation of the *whole* product law and no independence claim between coordinates inside one bank is used. QED.

If `K` is a physical singleton rather than a diffuse bank, `M_W<=1` and (4.6) improves to the previous physical-pivot constant `4 sqrt(6)|d|^(-1/2)|det N|^(-1/4)`.

The theorem proves an `O(|L|)` interval estimate directly. Continuity is not claimed in the fully coupled case because the completed-square shift may depend on `(U,V)`; the cited dependent-square theorem supplies `L^infinity`, not an `L^1` characteristic-function conclusion.

## 5. Decisive diffuse-pivot stress family

Let `m` be even and take three disjoint physical banks `I,J,K`, each of size `m`. Choose orthonormal dense vectors `a,b` on `I`, orthonormal dense vectors `c,d` on `J`, and a unit dense vector `e` on `K`; for example use normalized sign vectors with all coordinates of modulus `m^(-1/2)`. Define

`U_1=<a,X_I>`, `U_2=<b,X_I>`,
`V_1=<c,X_J>`, `V_2=<d,X_J>`,
`W=<e,X_K>`,

and

`Q_m=(U_1+V_1)^2-(U_2+V_2)^2+W^2`.                              (5.1)

The physical quadratic matrix is

`A_m=(a+c)(a+c)^T-(b+d)(b+d)^T+ee^T`,                            (5.2)

with the vectors extended by zero outside their banks. They are mutually orthogonal, with squared norms `2,2,1`. Consequently

`spec(A_m)={2,-2,1,0,...,0}`.                                    (5.3)

So this is a genuine target family for all `m`.

In the bank coordinates of Theorem 4.2,

`B=C=M=diag(1,-1)`, `r=s=0`, `d=1`,

hence `N=M`, `|det N|=1`, and

`boxed( ||p_{Q_m}||_infinity <= 8 sqrt(3) )`                     (5.4)

uniformly in `m` and in every admissible product input law.

This family shows exactly what the new theorem buys over a local physical pivot. All physical diagonal entries on `I` and `J` vanish because `a_i^2=b_i^2` and `c_j^2=d_j^2`; the only nonzero physical scalar pivots are on `K`, each of size `1/m`. Pivoting one such coordinate removes the remaining rank-one `K` square and leaves the two-direction saddle. The natural `I|J` Schur cross has singular values `1,1`, so the previous physical-pivot estimate scales only as

`4 sqrt(6m)`,                                                     (5.5)

whereas aggregating `K` to the unit projection `W` **before** paying the square direction gives the dimension-free (5.4). Every physical matrix entry is at most `2/m`, so this is not a disguised local-minor example.

This is not a counterexample to the previous theorem; it is a counterexample to the proof strategy that insists on paying the third direction through one physical diagonal pivot before bank aggregation.

## 6. Conditional end-to-end route after this run

The bilinear pathway now has a product-preserving hierarchy:

1. rank-two cross alone gives every finite `L^p` but not `L^infinity`;
2. a physical third pivot pays it by `L^3 -> L^infinity`;
3. a **diffuse scalar bank pivot** now pays it with no dimension loss (Theorem 4.2);
4. a rank-one scalar cross plus a square bank remains bounded even with arbitrary same-bank coefficient-side quadratic structure (Theorem 3.1);
5. account03/B09 already pays the exact three-bank cross-square normal form, while account01/B18 pays definite two-bank compressions.

The first surviving structural obligation is therefore narrower:

> **`QFORM-DIFFUSE-PIVOT-OR-NONSEPARABLE-RESIDUAL-v1` (OPEN).** From only `s_3(A)>=1`, aggregate original coordinates before reciprocal minor payment and force one of the already-paid certificates: a regularized diffuse determinant branch, a definite two-bank compression, a three-bank rank-one cross-square/absorption branch, or a two-by-two bank Schur cross plus scalar bank square as in Theorem 4.2. If none exists, identify the exact genuinely nonseparable residual and prove a new product-preserving estimate there, or construct a full target-valid counterexample.

The new family (5.1) is a mandatory regression test: any proposed extraction lemma that localizes the square direction to one coordinate before aggregation pays a spurious factor `sqrt(m)`.

## 7. Status

`ESSENTIAL_STEP_APPLIED`.

Proved here:

1. `QFORM-CROSS-SQUARE-COEFFICIENT-SIDE-ABSORPTION-v1`, extending the named partner half-potential mechanism to arbitrary same-bank coefficient-side structure;
2. the exact two-dimensional bank-marginal rank-two `L^p` ladder (4.1);
3. `QFORM-DIFFUSE-BANK-SCHUR-PIVOT-v1`, replacing a physical scalar pivot by a diffuse scalar bank while preserving original-coordinate product provenance and a linear small-ball exponent;
4. a fully diffuse target family with spectrum `{2,-2,1}` whose local physical-pivot bound grows like `sqrt(m)` but whose bank-first bound is the universal `8 sqrt(3)`.

The full conjecture remains OPEN. No numerical computation is used as mathematical evidence in this report.
