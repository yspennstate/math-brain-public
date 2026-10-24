# account01/B10 — residual-isotropic heavy-row L3 bridge

**Run:** `20260922T135338Z-account01-B10-QFORM-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** rank-three coupled case  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and compact end-to-end route

The exact rank-three target is: let `X_1,...,X_n` be independent real random variables with densities at most one and let

`A=U Lambda U^T`, `U^T U=I_3`,

with real symmetric invertible `Lambda` and all three eigenvalues of modulus at least one. Prove a universal `L^infinity` density bound for `Q=X^TAX`, with arbitrary orientation and without treating projected coordinates as independent.

Current route:

1. Fully diffuse three-frame: already paid by the diffuse rank-three theorem.
2. Heavy physical row `v=r_i`, scalar pivot `a=v^T Lambda v !=0`: complete the square in the original independent coordinate `X_i`. The Schur residual is an exact rank-two projected quadratic with determinant identity

   `det B = ell det Lambda / a`, where `ell=|v|^2`.
3. If the residual two-frame is diffuse, account03/B16 and account01/B18 already give the sign-free closure.
4. If the residual frame contains a heavy row, the remaining hard case is a finite localized core. This report pays the important subcase where that heavy residual row is **isotropic for the residual Schur form**. This is exactly where a second scalar-square pivot is unavailable and a hyperbolic mechanism is required.

The parent rank-three theorem remains open because a heavy residual row can have a nonzero Schur Rayleigh quotient, and the outer physical pivot can itself approach the light cone.

## 2. A shift-robust affine-mixture `L^3` lemma

### Lemma 2.1 (`QFORM-AFFINE-MIXTURE-L3-v1`)

Let `L` be a real random variable with density `g` satisfying `||g||_infinity<=H`. Let `X` be independent of a sigma-field `G` containing `L`, with probability density `f_X<=1`. Let `F` be any real `G`-measurable random variable and let `c!=0`. Then

`Y = c L X + F`

has an `L^3` density and

`||p_Y||_3 <= 66^(1/3) (H/|c|)^(2/3)`.          (2.1)

No independence between `F` and `L` is assumed.

### Proof

Condition on `L=l` and the rest of `G`. For `l!=0`, the conditional law of `Y` is a translate and rescaling of `X`, hence is a probability density with essential supremum at most

`K/|l|`, where `K=1/|c|`.

After averaging the other `G`-variables conditional on `L=l`, write that conditional density as `h_l`. It still satisfies

`int h_l=1`, `||h_l||_infinity<=K/|l|`.

Thus for every measurable set `E` of Lebesgue measure `m`,

`P(Y in E) <= int g(l) min(1,mK/|l|) dl`.        (2.2)

The function `l -> min(1,mK/|l|)` is symmetric decreasing. Under the constraints `0<=g<=H` and `int g=1`, the bathtub principle therefore gives the sharp worst placement `g=H 1_{[-R,R]}` with `R=1/(2H)`. Hence, if `a=mK<=R`,

`P(Y in E) <= 2Ha [1+log(R/a)]`,                 (2.3)

whereas if `a>=R`, the bound is at most one.

Let `p_Y^*` be the decreasing rearrangement. Since

`m p_Y^*(m) <= sup_{|E|=m} int_E p_Y`,

with `m_0=1/(2HK)` we obtain

`p_Y^*(m) <= 2HK[1+log(m_0/m)]`, `0<m<=m_0`,

and

`p_Y^*(m) <= 1/m`, `m>=m_0`.                    (2.4)

Therefore

`||p_Y||_3^3 = int_0^infinity p_Y^*(m)^3 dm`

`<= (2HK)^3 m_0 int_0^1 [1+log(1/u)]^3 du + int_{m_0}^infinity m^(-3) dm`.

Using

`int_0^1 [1+log(1/u)]^3 du = 16`

and `m_0=(2HK)^(-1)`, the right side is

`64 H^2K^2 + 2H^2K^2 = 66H^2K^2`.

Taking cube roots proves (2.1). QED.

The point is that arbitrary `G`-measurable shifts are harmless: the proof uses only genuine independence of the original scalar coordinate `X`, not any conditional cap obtained by rotating or conditioning product coordinates.

## 3. A dimension-free one-dimensional bank cap from the existing two-dimensional projection theorem

Let `L=sum_k c_k X_k` with `sum c_k^2=1`, where the `X_k` are independent and each density is at most one. The source-valid two-dimensional product projection theorem used by account02/B10 gives joint density cap two for every orthonormal two-frame.

Introduce an independent dummy `U~Unif[0,1]` and the orthonormal two-frame whose projected coordinates are `(L,U)`. Their joint density is exactly `p_L(l) 1_[0,1](u)`, so the two-dimensional cap gives

`||p_L||_infinity <= 2`.                            (3.1)

This avoids any dimension-dependent `1/max |c_k|` estimate and is the bank aggregation used below.

## 4. Main theorem: a heavy residual row on the Schur light cone is paid

### Theorem 4.1 (`QFORM-RANK3-RESIDUAL-ISOTROPIC-HEAVY-v1`)

Let `A=U Lambda U^T` have exact rank three, with `U^TU=I_3` and `Lambda` real symmetric invertible. Choose a physical row `v=r_i` with

`ell=|v|^2>0`, `a=v^T Lambda v=A_ii !=0`.

Complete the square in the original independent coordinate `X_i`. Let `W` be the resulting residual orthonormal two-frame and `B` its invertible symmetric `2x2` Schur coefficient matrix, so

`|det B| = ell |det Lambda|/|a|`.                  (4.1)

Suppose a residual physical row `w=r_j^res` has leverage

`h=|w|^2>0`

and is isotropic for the residual Schur form:

`w^T B w =0`.                                      (4.2)

Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= 4*66^(1/4) [h ell |det Lambda| |a|]^(-1/4)`.   (4.3)

In particular, if the row is residual-heavy (`h>1/2`), this removes the residual-light-cone subbranch of the nested-heavy obstruction without paying any reciprocal physical `3x3` minor.

### Proof

Choose an orthonormal basis `(e_1,e_2)` of the residual spectral plane with

`w=sqrt(h)e_1`.

By (4.2), in this basis

`B = [[0,gamma],[gamma,delta]]`.

Since `B` is invertible,

`det B=-gamma^2`, so `|gamma|=sqrt(|det B|)`.       (4.4)

For the remaining original coordinates `k!=i,j`, write their residual-frame rows as `(t_k,l_k)`. Frame orthonormality and the fact that the selected row has second component zero give

`sum_{k!=i,j} l_k^2=1`.                            (4.5)

Define

`T=sum_{k!=i,j} t_k X_k`, `L=sum_{k!=i,j} l_k X_k`.

Then the residual quadratic is exactly

`D = 2 gamma (sqrt(h) X_j + T)L + delta L^2`

`  = 2 gamma sqrt(h) L X_j + F`,                  (4.6)

where `F=2gamma TL+delta L^2` is measurable with respect to the sigma-field generated by all residual variables except `X_j`.

By (4.5) and the bank cap (3.1),

`||p_L||_infinity<=2`.                             (4.7)

Apply Lemma 2.1 to (4.6) with

`H=2`, `c=2gamma sqrt(h)`.

This yields

`||p_D||_3 <=66^(1/3) (1/(|gamma|sqrt(h)))^(2/3)`

`             =66^(1/3) h^(-1/3)|det B|^(-1/3)`.  (4.8)

Now return to the first physical pivot. Completing the square in `X_i` has the form

`Q=a(X_i+m(R))^2+D(R)`,                            (4.9)

where `R` denotes the remaining coordinates. Because `X_i` is genuinely independent of `R`, conditioning on `D` leaves the translated variable `X_i+m(R)` with conditional density at most one. Apply the completed dependent `L^3` square-smoothing lemma of account01/B11:

`||p_Q||_infinity <=4 |a|^(-1/2) ||p_D||_3^(3/4)`. (4.10)

Using (4.8),

`||p_Q||_infinity <=4*66^(1/4)|a|^(-1/2)h^(-1/4)|det B|^(-1/4)`.

Finally substitute (4.1):

`|a|^(-1/2)|det B|^(-1/4)`

`=|a|^(-1/2)(ell|det Lambda|/|a|)^(-1/4)`

`=(ell|det Lambda||a|)^(-1/4)`.

This is exactly (4.3). QED.

Numerically, `4*66^(1/4)=11.4010795311...`.

## 5. Why this is genuinely a bank result

The coordinate `L` may involve arbitrarily many original variables and no single coefficient `l_k` need be bounded below. The only input is the exact frame identity `sum l_k^2=1`; the density cap (3.1) aggregates the whole bank before any reciprocal local coefficient is paid.

This directly respects `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`: the theorem does not select a uniformly good principal triple or a rank-three cross cut. It also respects `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`: the proof never replaces original-coordinate independence by a cap on a rotated conditional law. The independent variable in Lemma 2.1 is exactly the physical coordinate `X_j`.

## 6. Named partner result actually applied

The designated partner `account02/B10` has a completed branch theorem at

`yspennstate/math-open-problems@11c9ae19edfd07e3a0bd4053a910667c20e721ab`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260922T130225Z-b10-qform-r11/REPORT.md`.

Its Theorem 3.1 proves that in the heavy-isotropic normal form, if the leakage `T` is genuinely independent of the transverse pair `(Y,Z)`, then

`||p_Q||_infinity <=3*2^(4/3)c^(-1/3)<3*2^(5/3)<9.525`           (6.1)

for `c>1/2`.

I use (6.1) as an actual inequality in the conditional route: the support-disjoint/independent-leakage heavy-isotropic subbranch is therefore already paid and must not be mixed into the remaining dependent nested-heavy case. The partner's exact falsifier in the same report also blocks the invalid shortcut of replacing that independence by only a pair density cap plus a conditional scalar cap.

## 7. First remaining implication

The new theorem removes the **residual isotropic heavy row** case after a nonzero outer physical pivot. The next unpaid rank-three implication is now more specific:

`QFORM-RANK3-NESTED-HEAVY-NONISOTROPIC-v1`:

> after a nonzero physical pivot, suppose the residual two-frame has a row of leverage `>1/2` but every such heavy residual row has nonzero Schur Rayleigh quotient. Prove a determinant-level `L^3` bound for that residual indefinite quadratic by aggregating the remaining one-dimensional bank before paying the heavy row's scalar square coefficient; alternatively show that one can move to another physical pivot or a hyperbolic bank with a well-conditioned invariant.

A second surviving obstruction is the outer light-cone regime `|a| ->0`; (4.3) still carries the correct explicit `|a|^(-1/4)` debt and does not claim to remove it.

A plausible next mechanism is a two-regime theorem for

`beta(sqrt(h)X+T)^2 + 2gamma(sqrt(h)X+T)L + delta L^2`

with `X` a genuine independent physical coordinate, `L` a normalized original-coordinate bank with density cap two, and `T` arbitrarily dependent on `L`. The exact `beta=0` endpoint is Theorem 4.1; any extension must retain the normalization of the conditional scalar sections and cannot collapse to a generic two-dimensional density cap.

## 8. Status and regularity

- `QFORM-AFFINE-MIXTURE-L3-v1`: **PROVED**.
- `QFORM-RANK3-RESIDUAL-ISOTROPIC-HEAVY-v1`: **PROVED SUPPORTING THEOREM**.
- arbitrary exact-rank-three orientation: **OPEN**.
- full owner conjecture with additional spectrum: **OPEN**.
- The theorem proves existence of an essentially bounded density in its scope. **Continuity is not proved here.**

No Gaussianity, moments, log-concavity, compact support, connected support, diagonal-basis independence, pointwise van-der-Corput decay, or Monte Carlo evidence is used.
