SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-22T23:14:31Z.
attacking: indefinite exact-rank-three hub-square geometry with arbitrary hub curvature, plus a minority-sign Schur pivot estimate.

# fleet01/B11 QFORM r11 — minority-sign Schur smoothing and arbitrary hub-curvature closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: indefinite signatures `(+,+,-)` and `(+,-,-)`  
Outcome: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

## 1. Compact conditional end-to-end argument

The exact-rank-three indefinite obstruction has two qualitatively different local mechanisms.

* If an ORIGINAL-coordinate scalar pivot has the minority sign, its Schur complement is rank-two definite. The rank-two definite pushforward has a bounded density by the two-dimensional projection theorem, and the remaining scalar square contributes only a half-Riesz kernel. This gives a determinant-exact bound with only a fourth-root loss in the pivot strength.
* In the orthogonal hub-square geometry, if every leaf row is diffuse, the completed fleet02/B11 hub-Fresnel theorem gives an integrable `|t|^{-3/2}` envelope. If one row is heavy, either a physical scalar diagonal is already quantitative or the hub-heavy-row principal pair is quantitatively indefinite. The existing scalar-pivot or pair theorem then closes the branch.

The first item is proved in Section 3. The second item is proved in Section 4 and is a strict extension of the assigned partner's full hub-square theorem: **arbitrary hub scalar curvature is now allowed without changing the universal constant 256**, under the exact target spectral normalization.

The full target remains open because an arbitrary exact-rank-three form need not admit this orthogonal hub-square representation in original coordinates, and arbitrary extra dense leaf self-coupling is not paid by this argument.

## 2. Source-pinned inputs and corrections

### 2.1 Assigned partner fleet02/B11 r16

Completed partner report:

`yspennstate/math-open-problems@a93d62ee254b5d17d8608a39f25aa3a5d87628f4`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260922T221830Z-fleet02-B11-QFORM-r16/REPORT.md`.

Its theorem `QFORM-DIFFUSE-HUB-FRESNEL-BL-v1` says that, for one genuine original-coordinate hub and rank-one leaf square with orthonormal coefficient vectors `b,d`, if

`b_j^2+d_j^2 <= 1/2` for every leaf coordinate `j`,

then, allowing arbitrary hub scalar curvature and affine terms,

`||p_Q||_infinity <= 3 e^(2/3) |kappa|^(-2/3)|lambda|^(-1/3)`.

The same report proves the full orthogonal hub-square family with zero hub scalar curvature by combining the diffuse branch with scalar-pivot and physical-pair exits. Section 4 below removes the zero-hub-curvature restriction.

### 2.2 Physical-pair compiler

Completed fleet03/B11 r17:

`yspennstate/math-open-problems@c869a82e52e46664d5bf299c3b210de02a02fc50`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260922T215136Z-fleet03-B11-QFORM-r17/REPORT.md`.

If `s_3(A)>=s>0` and an ORIGINAL-coordinate principal pair `B` is invertible indefinite, with

`D=|det B|`, `kappa_B=sigma_min(B)`,

then

`||p_Q||_infinity <= 3*400^(1/3) (D^2 kappa_B s)^(-1/6)`.

Equivalently, if `(D^2 kappa_B)^(1/5)>=delta s`, then

`||p_Q||_infinity <=3*400^(1/3) delta^(-5/6)s^(-1)`.

This branch supplies essential boundedness; continuity is not asserted.

### 2.3 Rank-two definite projection bound

Source package:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

For a rank-two positive semidefinite quadratic form with positive eigenvalues `mu_1,mu_2`, the two-dimensional product-projection density cap gives

`||p||_infinity <= 2*pi/sqrt(mu_1 mu_2)`.

The same bound applies after changing the sign of a negative semidefinite rank-two form.

### 2.4 Exact-rank-three scalar pivot

The completed rank-two-fusion source used by the partner is

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For an exact-rank-three target with all nonzero eigenvalues of magnitude at least one, every nonzero ORIGINAL-coordinate diagonal `A_ii` gives

`||p_Q||_infinity <=128/sqrt(|A_ii|)`.

### 2.5 Binding corrections honored

No step below assumes independence after a spectral rotation. No pointwise law-uniform van-der-Corput estimate is used. A bounded spectral projection density is used only for the **definite rank-two Schur remainder**, where polar coarea is valid; it is not used to bound an indefinite pushforward. No conditional-density cap is substituted for independence. No support, moment, log-concavity or connectedness assumption appears. No coefficient is deleted perturbatively.

## 3. Minority-sign scalar pivot theorem

Let

`A=R M R^T`, `R^T R=I_3`,

be exact rank three. Write the `i`th spectral row as `r in R^3`, let

`c=||r||^2`, `a=A_ii=r^T M r`,

and assume `a!=0` has the **minority sign** of the inertia of `M`: `a<0` for inertia `(2,1)`, and `a>0` for inertia `(1,2)`.

### Theorem 3.1 — `QFORM-MINORITY-SCHUR-HALF-RIESZ-v1`

For independent cap-one original coordinates,

`||p_{X^T A X}||_infinity <= 4 sqrt(pi) [c |a| |det M|]^(-1/4).`      (3.1)

This is an essential-boundedness theorem. No continuity assertion is made.

### Proof

Write `X=(X_i,Y)` and block-decompose

`A=[[a,b^T],[b,C]]`.

Completing the ORIGINAL coordinate `X_i` gives

`Q=a (X_i+a^(-1)b^T Y)^2 + Y^T S Y`,

where

`S=C-bb^T/a`.                                                    (3.2)

By Sylvester inertia additivity, because `a` has the minority sign, `S` is rank-two semidefinite of the opposite sign. For inertia `(2,1)` with `a<0`, `S` is positive semidefinite rank two; the other case follows after multiplying the form by `-1`.

The key exact determinant identity is

`pdet(S)= c |det M|/|a|`.                                       (3.3)

To verify it, rotate only the three-dimensional **coefficient space**, not the random variables, so that `r=sqrt(c)e_1`. In this coefficient basis write

`M=[[m,u^T],[u,D]]`, so `a=c m`.

The coefficient-space Schur matrix is

`K=M-M r r^T M/a`
` = [[0,0],[0,D-u u^T/m]]`.

Its nonzero determinant is

`det(D-u u^T/m)=det(M)/m=c det(M)/a`.                            (3.4)

The remaining original-coordinate frame satisfies

`R_-^T R_-=I-r r^T`.

Because `K r=0`, `range(K)=r^perp`; on `r^perp`, `I-r r^T` is the identity. Therefore multiplication by `R_-` is isometric on the nonzero range of `K`, so the two nonzero eigenvalues of `S=R_- K R_-^T` are exactly those of `K|_{r^perp}`. This proves (3.3).

Let

`T=Y^T S Y`.

The rank-two definite projection theorem and (3.3) give a density `g_T` with

`||g_T||_infinity <= B := 2*pi / sqrt(pdet(S))`.                (3.5)

Conditional on `Y`, the map in `X_i` is a translated square. Since the density of `X_i` is at most one, the conditional density is bounded by

`|a|^(-1/2) |s-T|^(-1/2)`                                      (3.6)

(the two roots together contribute exactly at most this amount). Hence

`p_Q(s) <= |a|^(-1/2) int |s-t|^(-1/2) g_T(t) dt`.             (3.7)

For every probability density `g<=B`, the one-dimensional bathtub principle gives

`sup_s int |s-t|^(-1/2) g(t)dt`
` <= B int_{-1/(2B)}^{1/(2B)} |u|^(-1/2)du`
` =2 sqrt(2B).`                                                 (3.8)

Insert (3.5):

`2 sqrt(2B)=4 sqrt(pi) pdet(S)^(-1/4)`.                         (3.9)

Combining (3.7), (3.9) and (3.3) yields

`||p_Q||_infinity`
` <=4 sqrt(pi)|a|^(-1/2)(c|det M|/|a|)^(-1/4)`
` =4 sqrt(pi)[c|a||det M|]^(-1/4).`                            (3.10)

QED.

### Interpretation

A rank-two opposite-sign saddle can have a logarithmically divergent density. A minority-sign scalar pivot reverses the geometry of the Schur remainder: the remaining rank-two form is definite, hence has a bounded density. The scalar square then costs only the integrable half-Riesz potential in (3.8). This is one exact way the third direction removes the rank-two singularity.

The theorem is not a full proof because an indefinite matrix can have no minority-sign physical diagonal at all; diffuse Hadamard-type frames are a standard example.

## 4. Arbitrary hub curvature: a full exact-rank-three subclass

Let `b,d in R^m` be orthonormal. Let `X_0,X_1,...,X_m` be independent with densities bounded by one. Consider

`Q = a X_0^2 + 2 kappa X_0 <b,X> + lambda <d,X>^2`,             (4.1)

with arbitrary real `a`, nonzero `kappa,lambda`, and arbitrary affine terms allowed. In the orthonormal aggregate coordinates `(X_0,B,D)`, `B=<b,X>`, `D=<d,X>`, the spectral matrix is

`H=[[a,kappa,0],[kappa,0,0],[0,0,lambda]]`.                     (4.2)

Its determinant is

`det H=-kappa^2 lambda`.                                        (4.3)

Assume the three eigenvalues of `H` all have absolute value at least one. Then automatically

`|lambda|>=1`, `|kappa|>=1`: `lambda` is one eigenvalue, while the other two have product `-kappa^2` and both have modulus at least one.

### Theorem 4.1 — `QFORM-ORTHOGONAL-HUB-SQUARE-HUBCURV-FULL-v1`

Under the preceding assumptions,

`||p_Q||_infinity <=256`.                                      (4.4)

For `lambda>0` the signature is `(+,+,-)`; for `lambda<0` it is `(+,-,-)`. Thus this is a genuinely indefinite exact-rank-three target subclass. The theorem proves essential boundedness; continuity is proved only in the diffuse branch below, not uniformly for all branches of the proof.

### Proof

#### Branch D: all leaf rows diffuse

Assume

`b_j^2+d_j^2 <=1/2` for every `j`.                              (4.5)

Apply the completed assigned-partner theorem fleet02/B11 r16 with `r=1`. Its Gram matrix is exactly the identity because `b,d` are orthonormal, and it expressly permits arbitrary hub scalar curvature `a`. Therefore

`||p_Q||_infinity`
` <=3e^(2/3)|kappa|^(-2/3)|lambda|^(-1/3)`
` =3e^(2/3)|det H|^(-1/3)`
` <=3e^(2/3)<5.844.`                                           (4.6)

This is an actual inequality application of the assigned partner result. This branch has a continuous `C_0` density.

#### Branch H: a heavy leaf row

Otherwise choose `j` with

`b_j^2+d_j^2>1/2`.                                              (4.7)

Put

`q=lambda d_j^2`, `p=kappa b_j`.

If `|q|>=1/4`, the ORIGINAL diagonal entry `A_jj=q` and the exact-rank-three scalar-pivot theorem gives

`||p_Q||_infinity <=128/sqrt(|q|)<=256`.                        (4.8)

Assume now `|q|<1/4`. Since `|lambda|>=1`, this forces `d_j^2<1/4`; by (4.7),

`b_j^2>1/4`, hence `|p|>1/2`.                                  (4.9)

If `|a|>=1/4`, the hub ORIGINAL diagonal is `A_00=a`, and again

`||p_Q||_infinity <=128/sqrt(|a|)<=256`.                        (4.10)

It remains to treat

`|a|<1/4`, `|q|<1/4`, `|p|>1/2`.                               (4.11)

The ORIGINAL principal pair on coordinates `{0,j}` is

`B_j=[[a,p],[p,q]]`.                                            (4.12)

Its determinant is negative, because

`D:=|det B_j|=|p^2-aq| >=p^2-|a q| >1/4-1/16=3/16`.            (4.13)

Thus the pair is invertible indefinite. Its two eigenvalues have opposite signs. Writing their discriminant as

`Delta=(a-q)^2+4p^2`,

the smaller absolute eigenvalue is

`sigma_min(B_j)=(sqrt(Delta)-|a+q|)/2`
` >= (2|p|-|a+q|)/2`
` > (1-1/2)/2=1/4`.                                            (4.14)

Therefore the pair scale from fleet03/B11 r17 satisfies

`(D^2 sigma_min(B_j))^(1/5)`
` > delta_0 := (9/1024)^(1/5)`
` =0.3879613934788399... .`                                    (4.15)

Since the full exact-rank-three matrix has `s_3(A)>=1`, the physical-pair theorem gives

`||p_Q||_infinity`
` <3*400^(1/3) delta_0^(-5/6)`
` =48.6576159646... <256.`                                     (4.16)

Every case is covered, proving (4.4). QED.

### What changed relative to partner r16

Partner r16's diffuse theorem already allowed arbitrary hub scalar curvature, but its full heavy-row closure was stated only for

`2 kappa X_0<b,X>+lambda<d,X>^2`.

The heavy-row algebra above shows that adding **arbitrary** `aX_0^2` does not open a new gap: either `a` itself is a quantitative scalar pivot or, when `a` is small, the same heavy row forces a uniformly indefinite physical pair. Hence the constant 256 survives unchanged.

## 5. Rank-two logarithmic control and the role of the third direction

Take `a=0`, `b=e_1`, and independent centered unit-uniform `X_0,X_1`. Deleting the `lambda<d,X>^2` term leaves

`2 kappa X_0 X_1`.

For `kappa=1`,

`p_{2X_0X_1}(t)=log(1/(2|t|))`, `0<|t|<1/2`,

so the opposite-sign rank-two density is genuinely unbounded.

The third square removes this singularity in two complementary ways in the present proof. In the diffuse branch, the hub bilinear term contributes the critical Fourier factor `|t|^-1`, and the true third quadratic direction contributes a Fresnel half-power, producing `|t|^-3/2`, which is integrable. In the minority-pivot branch, the third direction changes the Schur remainder from indefinite rank two to definite rank two, and its bounded density makes the half-Riesz kernel integrable. Neither mechanism asserts that rotated eigen-coordinates are independent.

## 6. First essential remaining implication

This run pays arbitrary **hub scalar curvature**, but not arbitrary dense **leaf self-coupling**. The first unpaid B11 implication is therefore

`QFORM-HUB-FRESNEL-DENSE-LEAF-SELFCOUPLING-v2`:

> Starting from the paid hub/Fresnel form, allow an arbitrary symmetric leaf remainder `E` that may have high rank and arbitrarily small individual eigenvalues. Prove that the original-coordinate product law still yields a universal density bound whenever the full matrix has three singular/eigen directions at scale one, or route every failure to an already paid scalar-pivot, indefinite-pair, ridge, or bank-aggregation certificate.

The obstacle is genuine: diagonal leaf phases are harmless to the partner's coordinatewise Fourier factorization, but dense `E` couples leaf variables before the absolute value. Because inputs have no support or moment bounds, `E` cannot be deleted merely because its entries or operator norm are small. A proof must aggregate or linearize it while retaining original-coordinate product provenance.

## 7. Deterministic checks

`VERIFY.py` checks the numerical constants and randomly verifies the exact Schur pseudodeterminant identity (3.3). Its recorded run ends

`QFORM_B11_HUBCURV_CHECK_PASS`.

## 8. Honest status

* Full QFORM conjecture: **OPEN**.
* New proved result: minority-sign exact Schur/half-Riesz bound (3.1).
* New proved target subclass: arbitrary-hub-curvature orthogonal hub-square exact-rank-three forms, universal bound 256.
* Assigned partner actually applied: fleet02/B11 r16, inequality (4.6).
* Continuity: **proved in branch D only** by the partner's integrable Fourier envelope; **not proved for the full theorem 4.1** because the heavy scalar/pair exits used here supply essential boundedness only.
* Rank-two logarithmic control retained exactly.
