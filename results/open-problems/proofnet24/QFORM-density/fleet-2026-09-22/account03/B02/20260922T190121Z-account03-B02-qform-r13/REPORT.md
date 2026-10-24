# account03/B02 — overlap-one integrated Fourier aggregation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T190121Z-account03-B02-qform-r13`  
Assignment: Integrated Fourier estimate  
Status: `PROVED_SUPPORTING_THEOREM / ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and live correction state

The full target remains OPEN: for every dimension, every independent real input coordinates with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of absolute value at least one, prove a universal finite essential bound for the density of `Q=X^T A X`, or produce a valid counterexample. Continuity is a separate stronger conclusion.

Fresh control was re-read during this run after the owner revision advanced to `2026-09-22.13`. The owner message's renewed arbitrary-joint three-dimensional coarea claim is not used: `CURRENT_RESEARCH.md` still contains the source-valid correction `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1`, which explicitly invalidates that unrestricted arbitrary-joint lemma and the rank-three conclusion derived from it. This report instead keeps the original-coordinate product structure throughout.

The law-uniform absolute characteristic-function `L^1` target is also not pursued. The live owner message now explicitly records that `phi_Q` need not belong to `L^1` even when the output density is bounded. The Fourier ingredient below is only an `L^{3/2}` estimate for a product-preserving rank-two residual, followed by a physical-square fractional smoothing step.

The designated partner is `account04/B02`. No completed current-QFORM handoff or canonical account04/B02 QFORM report was present at the fresh read, so no partner result is fabricated. Two completed compatible results are applied to actual inequalities instead: account03/B01's sharp dependence-safe square smoothing and account02/B20's source-pinned two-dimensional linear-image density bound.

## 2. Rank-three exterior notation

Let

`A = R Lambda R^T`,  `R^T R=I_3`,

have rank exactly three, where `Lambda` is real symmetric and invertible. Write `r_i^T` for the `i`th row of `R`. For every physical triple `I={i,j,k}` put

`w_I = det(R_I)^2`.

Cauchy--Binet gives

`sum_{|I|=3} w_I = det(R^T R)=1`.                                      (2.1)

Thus the `w_I` form a probability law on three-element bases. Let `I,J` be independent samples from this law. Define the overlap-one mass

`D_1 = P(|I intersect J|=1)
     = sum_{I,J: |I intersect J|=1} w_I w_J`.                           (2.2)

For each physical coordinate `i` set

`c_i = ||r_i||_2^2`.

Projection-DPP marginality, or direct Cauchy--Binet, gives

`c_i = sum_{I: i in I} w_I`,  and  `sum_i c_i=3`.                       (2.3)

When `c_i>0`, put `e_i=r_i/sqrt(c_i)` and choose a `3 x 2` isometry `W_i` whose columns span `e_i^perp`. For `j!=i`, define

`s_j = W_i^T r_j in R^2`.

Then

`sum_{j!=i} s_j s_j^T
 = W_i^T (I-r_i r_i^T) W_i
 = I_2`,                                                               (2.4)

so the `s_j` are an exact two-dimensional Parseval frame. For an unordered pair `P={j,k}` define

`u_P^(i)=det(s_j,s_k)^2`.

The three-dimensional determinant factors through the orthogonal decomposition along `r_i`:

`u_{jk}^(i) = w_{ijk}/c_i`.                                             (2.5)

Consequently `sum_P u_P^(i)=1`.

Let

`d_i = sum_{P,Q: P intersect Q=empty} u_P^(i) u_Q^(i)`.                 (2.6)

This is the probability that two independent residual two-bases, conditioned on containing `i` in the original three-basis law, are disjoint. In particular `0<=d_i<=1`.

## 3. Exact overlap-one identity

### Lemma 3.1 — `QFORM-OVERLAP1-RESIDUAL-IDENTITY-v1`

With the definitions above,

`boxed: D_1 = sum_i c_i^2 d_i.`                                         (3.1)

### Proof

Fix `i`. Ordered pairs of original bases whose intersection is exactly `{i}` are precisely

`I={i} union P`, `J={i} union Q`, `P intersect Q=empty`.

By (2.5), their total weight is

`sum_{P intersect Q=empty} (c_i u_P^(i))(c_i u_Q^(i)) = c_i^2 d_i`.

Every ordered pair with overlap exactly one has a unique common coordinate `i`, so summing in `i` proves (3.1). QED.

Put

`z_i=c_i^2 d_i`.

Because `sqrt(z_i)=c_i sqrt(d_i)<=c_i`, (2.3) gives

`sum_i sqrt(z_i)<=3`.                                                     (3.2)

For any index set `L`, therefore,

`sum_{i in L} z_i
 <= (max_{i in L} sqrt(z_i)) sum_{i in L} sqrt(z_i)
 <=3 max_{i in L} sqrt(z_i)`.                                            (3.3)

Hence

`max_{i in L} z_i >= [sum_{i in L} z_i]^2/9`.                            (3.4)

This elementary square-root selection is the mechanism that avoids paying one arbitrarily tiny local minor before aggregating exterior mass.

## 4. One pivot: exact rank-two Schur geometry

Fix an `i` with `c_i>0` and

`a_i=A_ii=r_i^T Lambda r_i !=0`.

Write `v=r_i`, `c=c_i`, `a=a_i`. Completing the physical square in `X_i` gives

`Q=a [X_i+m(X_{-i})]^2 + R_i`,                                           (4.1)

where `m` is linear in the remaining original coordinates and `R_i=X_{-i}^T T_i X_{-i}`. The residual matrix has rank two.

For completeness, choose an orthonormal basis `[e,W]` of `R^3` with `e=v/sqrt(c)` and `W` spanning `v^perp`. In this basis write

`Lambda = [[alpha,b^T],[b,C]]`,  `alpha=e^T Lambda e=a/c`.

The middle spectral Schur matrix is

`Lambda - Lambda v v^T Lambda/a`,

whose restriction to `v^perp` is

`N_i=C-bb^T/alpha`.                                                       (4.2)

The block determinant formula gives

`det Lambda = alpha det N_i`,

hence the exact conservation identity

`boxed: Delta_i:=|det N_i| = c_i |det Lambda|/|a_i|.`                    (4.3)

Moreover, with the residual Parseval rows `s_j` from Section 2,

`R_i = (sum_{j!=i} s_j X_j)^T N_i (sum_{j!=i} s_j X_j)`.                 (4.4)

No spectral-coordinate independence is asserted here: (4.4) is an algebraic representation of a function of the original independent coordinates.

## 5. Aggregate the residual before paying Fourier decay

Randomly split the complement of `i` into two color classes `G,H`, independently with probability `1/2`. Put

`S_G=sum_{j in G}s_j s_j^T`,  `S_H=sum_{j in H}s_j s_j^T`.

By the two-dimensional Cauchy--Binet formula,

`det S_G=sum_P u_P^(i) 1_{P subset G}`, and similarly for `H`.

Therefore

`E[det S_G det S_H]
 = 2^(-4) sum_{P intersect Q=empty}u_P^(i)u_Q^(i)
 = d_i/16`.                                                             (5.1)

So if `d_i>0`, some deterministic physical partition satisfies

`det S_G det S_H >= d_i/16`.                                             (5.2)

Define the independent two-dimensional original-coordinate aggregates

`Y_G=sum_{j in G}s_jX_j`, `Y_H=sum_{j in H}s_jX_j`.

The completed linear-image theorem used in account02/B20 (ultimately the source-pinned product projection estimate) gives

`M_G:=||p_{Y_G}||_infinity <=2/sqrt(det S_G)`,

`M_H:=||p_{Y_H}||_infinity <=2/sqrt(det S_H)`.                            (5.3)

The independence in (5.3) is genuine: `G` and `H` are disjoint sets of the original independent coordinates.

Let `Z=Y_G+Y_H`, with density `k=g*h`, and write

`R_i=Z^T N_i Z`.

Plancherel and Cauchy--Schwarz give

`||hat k||_1 <= ||hat g||_2||hat h||_2
              <=(2 pi)^2 sqrt(M_G M_H)`.                                 (5.4)

The two-dimensional Fresnel transform of `exp(i t z^T N_i z)` has constant modulus

`pi |t|^(-1) Delta_i^(-1/2)`.

Fourier inversion in the two aggregate variables therefore yields, for `t!=0`,

`|phi_{R_i}(t)|
 <= pi Delta_i^(-1/2) sqrt(M_GM_H) |t|^(-1)`.                            (5.5)

Set

`K_i=pi Delta_i^(-1/2)sqrt(M_GM_H)`.

Together with `|phi|<=1`,

`|phi_{R_i}(t)|<=min(1,K_i/|t|)`.                                        (5.6)

This is not the refuted law-uniform one-coordinate van-der-Corput estimate: the coefficient `K_i` records an actual product-preserving two-bank determinant resource, and the estimate is obtained only after the two-dimensional convolution/Plancherel aggregation.

## 6. Integrated Fourier credit: exactly `L^{3/2}` is enough

The borderline envelope (5.6) is not in `L^1`, but it is in every `L^q`, `q>1`. At the clean exponent `q=3/2`,

`int_R |phi_{R_i}(t)|^(3/2) dt
 <=2[int_0^{K_i}1 dt + int_{K_i}^infinity (K_i/t)^(3/2)dt]
 =6K_i`.                                                                (6.1)

Hausdorff--Young applied to the inverse transform (`L^{3/2}->L^3`) gives

`||p_{R_i}||_3
 <=(2pi)^(-2/3)(6K_i)^(2/3)
 =3^(2/3) Delta_i^(-1/3)(M_GM_H)^(1/3).`                                 (6.2)

This is the assigned integrated-Fourier estimate. It deliberately stops short of absolute `L^1` Fourier inversion.

## 7. Apply the completed square-smoothing theorem

Account03/B01 proved the sharp `p=3` dependence-safe physical-square estimate:

if `R` has density `h in L^3`, the conditional law of a variable `V|R` has density at most one, and `d!=0`, then

`||p_{R+dV^2}||_infinity
 <= [2sqrt(pi)/3^(1/4)] |d|^(-1/2)||h||_3^(3/4)`.                         (7.1)

In (4.1), conditional on every function of `X_{-i}`, the variable

`V=X_i+m(X_{-i})`

is a translation of the original `X_i`, so its conditional density is at most one. Applying (7.1) to (6.2) yields

`||p_Q||_infinity
 <=2sqrt(pi)3^(1/4)|a_i|^(-1/2)
   Delta_i^(-1/4)(M_GM_H)^(1/4)`.                                       (7.2)

From (5.3) and (5.2),

`(M_GM_H)^(1/4)
 <=sqrt(2)(det S_G det S_H)^(-1/8)
 <=2 d_i^(-1/8)`.                                                        (7.3)

Using (4.3) in (7.2) gives the main one-pivot estimate

`boxed:
 ||p_Q||_infinity
 <=4 3^(1/4)sqrt(pi)
   |det Lambda|^(-1/4)|a_i|^(-1/4)(c_i^2d_i)^(-1/8).`                    (7.4)

Numerically the leading constant in (7.4) is

`4*3^(1/4)*sqrt(pi)=9.330720...`.

The theorem establishes an essentially bounded density. This argument does not establish continuity.

## 8. Pay the entire non-isotropic overlap-one channel

For a threshold `tau>0`, define

`E_1(tau)=sum_{i: |A_ii|>=tau} c_i^2 d_i`.                               (8.1)

This is exactly the portion of the overlap-one exterior mass carried by physical pivots of size at least `tau`; by (3.1), `0<=E_1(tau)<=D_1`.

If `E_1(tau)>0`, apply (3.4) to

`L={i:|A_ii|>=tau}`.

There is an `i in L` with

`c_i^2d_i >= E_1(tau)^2/9`.                                              (8.2)

Substitution in (7.4) gives:

### Theorem 8.1 — `QFORM-RANK3-OVERLAP1-INTEGRATED-FOURIER-v1`

For every exact-rank-three form above and every `tau>0` with `E_1(tau)>0`,

`boxed:
 ||p_Q||_infinity
 <=4 sqrt(3pi)
 |det Lambda|^(-1/4)
 tau^(-1/4) E_1(tau)^(-1/4).`                                           (8.3)

The numerical constant is

`4sqrt(3pi)=12.279920495...`.

Under the target normalization `|lambda_j|>=1`, `|det Lambda|>=1`, so the determinant factor can be dropped.

An immediate dichotomy is useful. If `D_1>=eta` and

`E_1(tau)>=D_1/2`, then

`||p_Q||_infinity
 <=4sqrt(3pi)(2/(tau eta))^(1/4)`.                                       (8.4)

Otherwise at least half of the entire overlap-one mass is supported on coordinates satisfying

`|A_ii|<tau`.                                                            (8.5)

Thus the previously unresolved `|I intersect J|=1` exterior channel is fully paid away from an explicitly quantified near-isotropic physical-pivot concentration. No individual three-by-three determinant lower bound is required.

## 9. Relation to current rank-three aggregation results

The completed account01/B13 two-bank theorem pays the disjoint triple channel

`D_0=P(I intersect J=empty)`

before selecting a local minor, giving a universal bound whenever `D_0` has a fixed positive lower bound. Theorem 8.1 does the analogous job for the next overlap channel `D_1`, except for the sharply isolated near-isotropic pivot mass (8.5).

The fresh account03/B14 determinant-localization theorem gives a rigorous product-safe bound once one physical principal triple has a quantitative determinant. It replaces the invalid arbitrary-joint coarea route, but diffuse frames may make every such local determinant small. Theorem 8.1 is complementary: it aggregates many residual Pluecker pairs before paying a reciprocal determinant.

Consequently, in rank exactly three, any sequence that keeps `D_0` small, keeps a positive fraction of `D_1`, and evades the present theorem must force that `D_1` mass onto coordinates with `A_ii` tending to zero. This is exactly the near-isotropic branch highlighted by the proof-first controls, now with a precise exterior-mass formulation.

## 10. What remains unpaid

The full QFORM conjecture is OPEN. This report does not handle:

1. the near-isotropic overlap-one mass in (8.5);
2. overlap-two and overlap-three exterior channels when they dominate;
3. arbitrary extra spectral directions outside exact rank three, except where separate completed diffuse/ridge/principal-block theorems apply.

The first next implication for B02 is therefore:

`QFORM-NEAR-ISOTROPIC-OVERLAP1-OFFDIAGONAL-v1` (OPEN):

> If a fixed amount of exact-rank-three overlap-one mass is concentrated on indices with `|A_ii|<=tau`, convert the identity `||Lambda r_i||^2=A_ii^2+||A_{i,-i}||_2^2` and the residual `d_i` mass into a product-preserving two-bank hyperbolic packet whose density cost remains bounded as `tau->0`.

That route uses the curvature forced into off-diagonal couplings when the scalar pivot is near isotropic, rather than trying to divide by `A_ii`. After that, overlap-two/two-heavy-row geometry is the remaining exact-rank-three exterior channel. The arbitrary-extra-spectrum bridge remains a separate full-target obligation.

## 11. Source pins and integrity

Fresh owner/control repository at the decisive refresh: `yspennstate/math-research-brain@9dd55b53aa85edb8fe7d1d4c9cf0787c877ca092`, OWNER CONTROL revision `2026-09-22.13`. `CURRENT_RESEARCH.md` at that commit continues to mark the arbitrary-joint coarea lemma false and the full conjecture open.

Applied analytic dependency:

- account03/B01, sharp half-integral / dependence-safe square smoothing, visible at `yspennstate/math-open-problems@559e4be19d8f032bdae0392e7394bdcdca681a14:proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/20260922T142626Z-account03-B01-qform-r12/REPORT.md`.

Applied projection-density dependency and aggregate precedent:

- account02/B20, two-dimensional linear-image density bound and zero-pivot aggregate mechanism, visible at `yspennstate/math-open-problems@559e4be19d8f032bdae0392e7394bdcdca681a14:proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260922T115925Z-account02-B20-qform-r11/REPORT.md`.

Comparison results:

- account01/B13 disjoint exterior-mass aggregation, visible at `yspennstate/math-open-problems@559e4be19d8f032bdae0392e7394bdcdca681a14:proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260922T135910Z-account01-B13-qform-r13/REPORT.md`.
- account03/B14 determinant-localization theorem, creation visible in the repository history at `yspennstate/math-open-problems@89e6481f4f7ed7d49a77cfcb989ee93572d5d5cd:proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260922T190524Z-account03-B14-QFORM-r16/REPORT.md`.

A numerical regression using 50 random `7 x 3` Parseval frames checked the identities `u_{jk}^{(i)}=w_{ijk}/c_i` and `D_1=sum_i c_i^2d_i`; the maximum floating-point discrepancies were respectively `6.7e-16` and `1.0e-15`. This is only a regression; Sections 2--8 are the proof.

No Gaussian, moment, log-concavity, support-compactness, support-connectedness, post-rotation independence, law-uniform pointwise quadratic-phase decay, or arbitrary-joint coarea premise is used. No claim of a full solution is made.
