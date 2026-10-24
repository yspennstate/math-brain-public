# account01/B16 — translated projection-bank smoothing over an indefinite Frostman base

**Run:** `account01-B16-20260922T161036Z-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Projection-product interaction  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction-aware gap

The full target remains open: for every dimension, every independent real coordinates `X_i` with densities bounded by one, and every real symmetric matrix `A` having at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has an essentially bounded density with one universal finite constant. Continuity is a separate desired conclusion and is not proved here.

Fresh controls were read from `yspennstate/math-research-brain`; the initial coherent source commit was `521cf8717db5349bf94ddcf200e4d91f0a742e7d`, and the pre-publication refresh was `3849060b24ff77ba6dc6dcc1c9d4bc1e99cc1aeb`. The latter still carries owner revision `2026-09-22.5`. The fresh correction inbox blob is `7f181e495e359f3ec5037c4e40fa5bd5e6d3a21b`.

The proof below explicitly respects the live corrections: a bounded low-dimensional projection density by itself does not control an indefinite quadratic trace; conditioning after a sum/difference or general projection need not preserve density caps; one uniformly good physical minor need not exist; and the singleton-plus-two-banks family defeats local reciprocal-minor selection. The mechanism here therefore uses an **independent original-coordinate projection bank before the nonlinear trace**, while allowing its translation to depend arbitrarily on the base variables.

## 2. Completed designated partner result actually applied

The designated partner result is account02/B16 run `20260922T153609Z-account02-B16-QFORM-auto11`, canonical report

`yspennstate/math-open-problems@85c527c3172670ca9e6200138e1364be554413ac`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260922T153609Z-account02-B16-QFORM-auto11/REPORT.md`,

report blob `e919e8c6811b687ad32a6e73a7c32962248ccac0`.

Its theorem `QFORM-INDEFINITE-BINARY-FROSTMAN-v1` implies the following inverse-square-root potential estimate. If independent cap-one `Y,W` enter

`R=aY^2+2bYW+cW^2+linear+constant`,

with `D=ac-b^2<0`, `d=|D|`, then

`sup_t int |t-r|^(-1/2) dmu_R(r) <= C_ind d^(-1/4)`,              (2.1)

where

`C_ind = 8*3^(3/4)*5^(1/4)/sqrt(e)
       = 16.53964516612327... .`                                  (2.2)

The estimate is uniform over all linear and constant terms.

We also use the source-transferred Rudelson--Vershynin one-dimensional projection theorem recorded by account02/B18: if `L=sum c_i X_i`, `sum c_i^2=1`, and the independent `X_i` have densities at most one, then

`||p_L||_infinity <= sqrt(2)`.                                    (2.3)

No independence after spectral rotation is asserted.

## 3. Scaling the partner theorem to arbitrary density caps

### Lemma 3.1 — cap-scaled binary Frostman potential

Let `Y,W` be independent and have densities bounded by `K_1,K_2`, respectively. Let

`R=aY^2+2bYW+cW^2+ell_1Y+ell_2W+ell_0`,

with `D=ac-b^2<0`, `d=|D|`. Then

`boxed(
 sup_t int |t-r|^(-1/2) dmu_R(r)
 <= C_ind sqrt(K_1 K_2) d^(-1/4).
 )`                                                               (3.1)

### Proof

Set `Y'=K_1Y`, `W'=K_2W`. Their densities are at most one. In `(Y',W')` variables the quadratic determinant is

`D'=D/(K_1^2 K_2^2)`.

Apply (2.1) to the transformed polynomial. Since

`|D'|^(-1/4)=sqrt(K_1K_2)d^(-1/4)`,

(3.1) follows. The transformed linear terms remain arbitrary, which is within the partner theorem's scope. QED.

The same estimate survives arbitrary mixing of the linear and constant terms: if a nuisance parameter `Theta` is independent of `(Y,W)` and only `ell_1,ell_2,ell_0` depend measurably on `Theta`, apply (3.1) conditionally on `Theta` and average.

## 4. A conditional square kernel needs only a capped independent innovation

### Lemma 4.1 — translated-bank square smoothing

Let `(R,V)` be any pair of real random variables such that, for almost every `r`, the conditional law of `V|R=r` has a density bounded by `K_3`. For `gamma!=0`, put

`Q=R+gamma V^2`.

Then whenever the right side is finite,

`boxed(
 ||p_Q||_infinity
 <= K_3 |gamma|^(-1/2)
    sup_t int |t-r|^(-1/2) dmu_R(r).
 )`                                                               (4.1)

### Proof

For fixed `R=r`, the density of `gamma V^2` at a point `u` of the correct sign is

`[h_r(sqrt(|u/gamma|))+h_r(-sqrt(|u/gamma|))]
 /(2 sqrt(|gamma| |u|))`,

hence it is at most

`K_3/(sqrt(|gamma| |u|))`.

Average this conditional density at `u=t-r` over `mu_R`. QED.

The point is that no independence between `R` and `V` is required.

### Lemma 4.2 — how original product structure supplies the conditional cap

Let `Z` be arbitrary, let `L` be independent of `Z` with density bounded by `K_3`, and let `s(Z)` be any measurable function. Set

`R=F(Z)`, `V=L+s(Z)`.

Then the conditional density of `V|R=r` is bounded by `K_3` for almost every `r`.

Indeed, conditional on `Z=z`, `V` is merely a translate of `L`. Conditioning only on the coarser sigma-field generated by `R=F(Z)` forms a mixture of these translates, and a mixture of densities each bounded by `K_3` retains the same bound.

This is the dependence-retaining interface missing from a bare projected-density argument: the projection bank is spent as an **independent innovation**, while its center may depend arbitrarily on all variables that determine the indefinite residual.

## 5. Main theorem: indefinite base plus translated projection bank

### Theorem 5.1 — `QFORM-TRANSLATED-BANK-FROSTMAN-SMOOTHER-v1`

Let `Theta,Y,W,L` be such that:

1. `Y,W,Theta` are mutually independent, and `Y,W` have densities bounded by `K_1,K_2`;
2. `L` is independent of `(Theta,Y,W)` and has density bounded by `K_3`;
3. `D=ac-b^2<0`, `d=|D|`;
4. `A(Theta),B(Theta),C(Theta)` and `s(Theta,Y,W)` are arbitrary measurable functions;
5. `gamma!=0`.

Define

`R=aY^2+2bYW+cW^2+A(Theta)Y+B(Theta)W+C(Theta)`,

`Q=R+gamma [L+s(Theta,Y,W)]^2`.

Then `Q` has an essentially bounded density and

`boxed(
 ||p_Q||_infinity
 <= C_ind K_3 sqrt(K_1K_2)
    |gamma|^(-1/2) d^(-1/4).
 )`                                                               (5.1)

### Proof

Condition on `Theta`. Lemma 3.1 applies with the same quadratic determinant `D`, independently of the realized linear/constant terms. Averaging gives

`sup_t int |t-r|^(-1/2)dmu_R(r)
 <= C_ind sqrt(K_1K_2)d^(-1/4)`.                                  (5.2)

Put `Z=(Theta,Y,W)` and `V=L+s(Z)`. Lemma 4.2 gives

`||p_{V|R=r}||_infinity<=K_3`

for almost every `r`. Lemma 4.1 now gives exactly (5.1). QED.

This theorem is nonlinear and genuinely keeps dependence: the translation of the final square may be an arbitrary function of the variables producing the indefinite residual. The only independence spent is the original-coordinate innovation bank `L`, before the curved square map.

## 6. Actual use of the bounded-density projection theorem

Let `T` be a set of original physical coordinates, disjoint from all coordinates in `Z=(Theta,Y,W)`, and let

`L=sum_{k in T} l_k X_k`, `sum_{k in T}l_k^2=1`.

By the Rudelson--Vershynin projection theorem (2.3),

`K_3=sqrt(2)`                                                     (6.1)

is valid. Therefore Theorem 5.1 gives the concrete projection-product inequality

`boxed(
 ||p_Q||_infinity
 <= sqrt(2) C_ind sqrt(K_1K_2)
    |gamma|^(-1/2)d^(-1/4).
 )`                                                               (6.2)

If `Y,W` are themselves original physical coordinates, `K_1=K_2=1`, so

`||p_Q||_infinity
 <= sqrt(2) C_ind |gamma|^(-1/2)d^(-1/4)
 =23.3905915... |gamma|^(-1/2)d^(-1/4).`                          (6.3)

Thus an independent normalized transverse projection bank may be completely diffuse over arbitrarily many coordinates without any reciprocal-minor loss.

## 7. Three disjoint diffuse spectral banks

The preceding theorem yields a clean target-valid branch that includes the live singleton-plus-two-banks obstruction.

Let the physical coordinate set be partitioned into three disjoint sets `T_1,T_2,T_3` (and optionally a fourth disjoint set carrying an independent remainder). Let

`L_j=sum_{k in T_j} u_{jk}X_k`, `sum_{k in T_j}u_{jk}^2=1`.

The `L_j` are independent and, by (2.3), each has density at most `sqrt(2)`. Consider

`Q_3=lambda_1 L_1^2+lambda_2 L_2^2+lambda_3 L_3^2`,

with `|lambda_j|>=1`.

### Corollary 7.1 — `QFORM-DISJOINT-THREE-BANK-v1`

For arbitrary independent cap-one physical inputs,

`boxed(||p_{Q_3}||_infinity <= 2 C_ind <33.08.)`                  (7.1)

The same bound holds after adding any independent random variable, in particular an arbitrary quadratic form on a fourth disjoint physical block.

### Proof

If all three `lambda_j` have the same sign, the square of a variable with density cap `K` has the standard one-sided envelope `K/(sqrt(|lambda|y))`. Convolving the first two same-sign squares gives

`||p||_infinity<=K_1K_2 pi/sqrt(|lambda_1lambda_2|)
 <=2pi<2C_ind`,                                                   (7.2)

and convolution with the third independent term cannot increase `L^infinity`.

Otherwise choose two coefficients of opposite signs, say `lambda_1lambda_2<0`. Apply Theorem 5.1 with no nuisance parameter and no translation, with

`Y=L_1`, `W=L_2`, `L=L_3`,
`K_1=K_2=K_3=sqrt(2)`,
`d=|lambda_1lambda_2|`, `gamma=lambda_3`.

Then

`||p_{Q_3}||_infinity
 <= C_ind * sqrt(2) * sqrt(2) *
    |lambda_3|^(-1/2)|lambda_1lambda_2|^(-1/4)
 <=2C_ind`.                                                       (7.3)

Finally, convolution with an independent remainder preserves the bound. QED.

### Live stress family

For

`A_m=[1] direct_sum (J_m/m) direct_sum (-J_m/m)`,

write the two rank-one bank coordinates as

`L_+=(1/sqrt(m))sum_{j=1}^m X_j`,
`L_-=(1/sqrt(m))sum_{j=m+1}^{2m} X_j`.

The three nonzero eigenvalues are `{1,1,-1}`, and the three active variables are the singleton physical coordinate together with the two disjoint normalized banks. Corollary 7.1 gives a dimension-free bound immediately; more sharply, pairing the two diffuse opposite-sign banks in the partner Frostman estimate and using the singleton as the final square gives

`||p_Q||_infinity <= 2 C_ind =33.07929033224653...`,              (7.4)

uniformly in `m` and in all cap-one input laws.

This pays the exact structural family that defeats every strategy selecting one uniformly good physical triple. No physical determinant is inverted.

## 8. Relation to the previous B16 cubic ledger

The preceding B16 run proved that, in an exact-rank-three factorization, the normalized transverse projection weights through a fixed physical pair are exactly the normalized third-principal-minor weights. Its remaining debt was a nonlinear diffuse-bank aggregation theorem. The present result proves such aggregation **when the transverse bank is an original-coordinate innovation independent of the variables generating the binary indefinite base**, even though the center of the square is allowed to depend arbitrarily on that base.

This is a strict extension beyond choosing a heavy bank atom: all coefficients of the transverse bank may be of size `m^(-1/2)` and the bound is unchanged. It also explains why the generic projected-density/X-ray correction does not apply: the proof uses the independent innovation representation before the nonlinear map, not merely the marginal density of a dependent spectral projection.

## 9. Exact remaining implication

The new first unpaid step is an **innovation-extraction/weighted-conditioning bridge**:

> Given an arbitrary rank-three (or higher-rank) spectral frame whose physical rows mix all three spectral directions, either extract a coordinate-disjoint normalized bank that remains a capped innovation after the two-dimensional indefinite residual is formed, or prove a replacement for Lemma 4.2 that uses the full original product provenance without requiring support-disjointness. This must survive the Hadamard/diffuse frames and arbitrary additional spectral components.

A bare joint projection-density bound is insufficient by the live two-sheet and fiberwise-trace counterexamples. A single local minor is also insufficient. The current theorem closes the disjoint-bank obstruction but not the overlapping-frame case.

The ridge-window theorem supplies a complementary complete branch when the high-spectral projection has maximum coordinate leverage at most `1/32`; the unresolved geometry is therefore concentrated in high-leverage/overlapping frames outside that branch.

## 10. Status

Proved here:

1. cap-scaled version (3.1) of the completed account02/B16 inverse-square-root Frostman potential;
2. translated conditional-bank square smoother (4.1)--(4.2);
3. `QFORM-TRANSLATED-BANK-FROSTMAN-SMOOTHER-v1`, equation (5.1);
4. a direct application of the actual product-projection density theorem, equation (6.2);
5. `QFORM-DISJOINT-THREE-BANK-v1`, equation (7.1), closing the singleton-plus-two-banks stress family without local-minor selection.

Not proved: an innovation extraction for arbitrary overlapping spectral frames, arbitrary additional correlated spectral components, the full conjecture, or continuity in the full target.

**Full QFORM conjecture: OPEN / NOT PROVED.**
