# account03/B01 auto12 — fractional rank-two volume smoothing and high-leverage localization

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `account03-B01-20260922T223030Z-auto12`  
**Assignment:** Oscillatory replacement  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `ESSENTIAL_STEP_APPLIED / FRACTIONAL-E2-BL BRANCH PAID / FULL_TARGET_OPEN`  
**Continuity:** the new outer-pivot theorem proves essential boundedness; continuity is not asserted.

## 1. Exact target and correction boundary

The target is unchanged: for every finite `n`, every product input `X=(X_1,...,X_n)` with independent real coordinates and probability densities `0<=f_i<=1`, and every real symmetric matrix `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density bounded by one universal finite constant, or give a valid target counterexample.

No Gaussian, moment, iid, compact-support, connected-support, log-concavity, spectral-coordinate independence, or regularity hypothesis is added. The scalar law-uniform pointwise Fresnel estimate remains false for fragmented phase-aligned cap-one densities. The argument below does not use it. It also does not use the false arbitrary-joint rank-three coarea statement, a worst conditional projection-density cap, a fixed-good-minor extraction, or a fiber supremum.

The mechanism is an averaged-frequency one: Weyl differencing removes both same-side quadratic phases, a fractional volume-sampling Brascamp--Lieb estimate controls the resulting product Fourier integral, and only then is finite-`p` Fourier regularity converted into a target density bound through a genuine original-coordinate scalar square.

## 2. Fresh source inputs actually used

### 2.1 Fractional volume-sampling template

The fresh account01/B20 report

`yspennstate/math-open-problems@e8dbbf2d994e8a3878110b6eb405cdce0bc3e5e4`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260922T222136Z-account01-B20-QFORM-r21/REPORT.md`

proves a fractional volume-sampling Brascamp--Lieb theorem for **third** cross-volume `e_3`, using exponents `c_i=theta alpha_i`, `d_j=1-theta beta_j` and the determinant interpolation

`1+u >= K_theta u^theta`,

where

`K_theta=theta^(-theta)(1-theta)^(-(1-theta))`.

The theorem below performs the rank-two version but stops at the correct finite-`p` regularity scale instead of demanding an `L^1` characteristic function. This is the key difference: at second cross-volume the natural pointwise tail is `|t|^{-theta}`, which cannot be absolutely integrated for `theta<1`, but its `L^{3/2}` norm is finite as soon as `theta>2/3` and that is exactly what a third physical square can spend.

### 2.2 Current balanced-hub packet to which the theorem is applied

The source-valid balanced packet is recorded in account01/B20

`yspennstate/math-open-problems@e8dbbf2d994e8a3878110b6eb405cdce0bc3e5e4`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260922T202251Z-account01-B20-QFORM-r12/REPORT.md`.

It has an original physical outer pivot `a` with

`|a|>=m:=3501/8000`,

an exact Schur residual `S`, a physical residual hub `p`, and disjoint physical banks `U,V`. Put

`c_U=S[U,p]`, `c_V=S[p,V]`, `M=S[U,V]`,

`r_U=||c_U||_2`, `r_V=||c_V||_2`,

with

`r_U,r_V>g:=1/(8 sqrt(2))`.

For the augmented physical cross bank

`N_U=S[U,{p} union V]=[c_U,M]`,

and `u=c_U/r_U`, define

`D_U=||(I-uu^T)M||_F`.

That report proves the exact wedge inequality

`E_2(N_U):=e_2(N_U N_U^T) >= r_U^2 D_U^2`.

The previous analytic payment used a selected-side **range leverage** gate at `1/2`. The new theorem below instead uses the actual squared-minor volume marginals and pays a strictly larger diffuse range.

### 2.3 Designated partner account04/B01

The designated partner result is `QFORM-SIGNED-FEJER-EQUIVALENCE-v1`, canonical source

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

For every probability measure `mu`, with

`D_T mu(y)=(1/(2pi)) int_{-T}^T (1-|t|/T) Re(e^{-ity} phi_mu(t)) dt`,

it proves

`||p_mu||_infinity = sup_{T>0,y} D_T mu(y)`

with value `+infinity` if there is no bounded density. Section 7 applies this exact partner identity to the new inequality.

## 3. Rank-two volume notation

Let `I,J` be disjoint sets of original physical coordinates and let

`M=A[I,J]`.

Assume

`E:=e_2(M^T M)>0`.

By Cauchy--Binet,

`E = sum_{|S|=|T|=2} det(M[S,T])^2`.

Define the exact squared-minor volume distribution

`w_ST = det(M[S,T])^2/E`

on nonzero physical `2 x 2` cross minors, and inclusion marginals

`alpha_i=P_w(i in S)`,  `beta_j=P_w(j in T)`.

Then

`sum_i alpha_i=sum_j beta_j=2`,

and all `alpha_i,beta_j` lie in `[0,1]`.

For `0<theta<1`, set

`K_theta=theta^(-theta)(1-theta)^(-(1-theta))`.

## 4. Main averaged-frequency theorem — fractional rank-two volume BL

### Theorem 4.1 — `QFORM-FRACTIONAL-E2-BL-L3-v1`

Let `R` be an arbitrary quadratic-affine form in independent cap-one original coordinates, and suppose one original-coordinate cut `I|J` has cross block `M` as above. Fix

`2/3 < theta <1`

and assume

`theta alpha_i <=1/2` for every row `i in I`.                     (4.1)

No condition is imposed on either same-side quadratic block, on signs, on outside coordinates/couplings, or on the column marginals `beta_j`.

Then `R` has a density in `L^3(R)` and

`boxed(
 ||p_R||_3
 <= [ e * (3 theta/(3 theta-2))
        * K_theta^(-1/(4 theta)) ]^(2/3)
      E^(-1/6).
)`                                                               (4.2)

The same theorem may be applied to `M^T`, exchanging `alpha` and `beta`.

#### Proof

The source-valid Weyl-differencing step used in the reviewed volume-sampling theorem applies verbatim at second cross volume. After conditioning any outside original coordinates, it gives

`|phi_R(t)|^2
 <= int_{R^J} prod_i |psi_i(2t <a_i,w>)|
                    prod_j g_j(w_j) dw`,                          (4.3)

where `a_i` are the physical rows of `M`, `psi_i` are characteristic functions of the original physical inputs on the row side, and `g_j=f_j*f_j_tilde` are probability densities satisfying `0<=g_j<=1`. Both same-side quadratic phases cancel in the difference; no spectral rotation of the source occurs.

Set

`c_i=theta alpha_i`,  `d_j=1-theta beta_j`.                       (4.4)

Then

`sum_i c_i=2theta`,
`sum_j d_j=|J|-2theta`,
`sum_i c_i+sum_j d_j=|J|`.                                      (4.5)

By (4.1), `0<=c_i<=1/2`; because `theta<1`, every `d_j` is positive.

For positive Gaussian parameters let

`D_I=diag(x_i)`, `D_J=diag(y_j)`.

Cauchy--Binet and weighted AM--GM with the exact weights `w_ST` give

`det(D_J+M^T D_I M)`
` =det(D_J) det(I+N^T N)`
` >=det(D_J)[1+e_2(N^T N)]`,                                   (4.6)

and

`e_2(N^T N)
 >= E prod_i x_i^(alpha_i) prod_j y_j^(-beta_j)`.                (4.7)

For every `u>0`,

`1+u >=K_theta u^theta`.                                        (4.8)

Combining (4.6)--(4.8),

`det(D_J+M^T D_I M)
 >=K_theta E^theta prod_i x_i^(c_i) prod_j y_j^(d_j)`.           (4.9)

Hence Lieb's Gaussian characterization of the Brascamp--Lieb constant yields

`BL <= K_theta^(-1/2) E^(-theta/2)
       prod_i c_i^(-c_i/2) prod_j d_j^(-d_j/2)`.                 (4.10)

Apply Brascamp--Lieb to (4.3). Since `c_i<=1/2`, the exponent `1/c_i>=2`, and the same sharp one-dimensional Hausdorff--Young estimate used in the fresh rank-three theorem gives

`[int |psi_i(2ts)|^(1/c_i) ds]^(c_i)
 <=(pi/|t|)^(c_i)
   (1-c_i)^(-(1-c_i)/2)c_i^(c_i/2)`.                            (4.11)

The `c_i` powers cancel (4.10). Since `0<=g_j<=1` and `int g_j=1`,

`[int g_j^(1/d_j)]^(d_j)<=1`.                                   (4.12)

Write

`R_theta=prod_i(1-c_i)^(-(1-c_i)/2)`,
`D_theta=prod_j d_j^(-d_j/2)`.

Using `-(1-x)log(1-x)<=x`,

`log R_theta<=theta`, `log D_theta<=theta`,

so `R_theta D_theta<=e^(2theta)`. Thus (4.3) implies

`|phi_R(t)|
 <=min{1, A_theta |t|^(-theta)}`,                               (4.13)

where

`A_theta=K_theta^(-1/4)e^theta E^(-theta/4) pi^theta`.           (4.14)

Now put `q=3/2`. Since `theta>2/3`, `theta q>1`, and exact integration at the crossover `T=A_theta^(1/theta)` gives

`||phi_R||_q^q
 <=2 A_theta^(1/theta) * (3theta/(3theta-2)).`                  (4.15)

Inverse Hausdorff--Young, in the convention `hat f(t)=int e^{itx}f(x)dx`, gives

`||p_R||_3 <=(2pi)^(-2/3)||phi_R||_(3/2)`.                      (4.16)

Since

`A_theta^(1/theta)
 = pi e K_theta^(-1/(4theta)) E^(-1/4)`,                        (4.17)

substitution of (4.15)--(4.17) is exactly (4.2). This proves the theorem. QED.

### Why the exponent threshold is exact for this mechanism

At `theta=2/3`, the tail in (4.13) is `|t|^(-2/3)`, whose `3/2` power is the logarithmic endpoint `|t|^-1`. Thus this route cannot reach the `L^3` density needed by the outer square at the endpoint without a genuinely new cancellation input. For every fixed `theta>2/3`, however, the constant is finite.

## 5. Target-level square absorption

### Theorem 5.1 — `QFORM-FRACTIONAL-E2-BL-SQUARE-v1`

Let a full quadratic form have a nonzero **original-coordinate** scalar pivot `a`. After exact physical Schur completion write

`Q=a(X+h(Y))^2+R(Y)`,                                           (5.1)

where `X` is the original independent cap-one coordinate and `R` is the exact Schur residual. Suppose `R` has an original-coordinate cross block `M` with second volume `E=e_2(M^TM)>0`, and its volume row marginals satisfy (4.1) for some fixed `theta in (2/3,1)`.

Then the full ambient form has an essentially bounded density satisfying

`boxed(
 ||p_Q||_infinity
 <= 4 [ e * (3theta/(3theta-2)) ]^(1/2)
       K_theta^(-1/(8theta))
       |a|^(-1/2) E^(-1/8).
)`                                                               (5.2)

All residual same-side curvature and all outside couplings are retained. Continuity is not asserted by this dependent-square step.

#### Proof

Theorem 4.1 gives the `L^3` density estimate for `R`. Conditional on `R=r`, the shifted variable `X+h(Y)` is a mixture of translates of the original cap-one law of `X`, hence has conditional density cap at most one. The completed dependence-safe square theorem therefore gives

`||p_Q||_infinity <=4|a|^(-1/2)||p_R||_3^(3/4)`.               (5.3)

Insert (4.2); the exponent `(2/3)(3/4)=1/2` on the bracket and `(-1/6)(3/4)=-1/8` on `E`, yielding exactly (5.2). QED.

### Concrete gate `theta=3/4`

For `theta=3/4`, the volume-marginal hypothesis becomes

`max_i alpha_i<=2/3`.                                           (5.4)

Here

`K_(3/4)=4/3^(3/4)`,

and (5.2) becomes

`boxed(
 ||p_Q||_infinity
 <= C_(2,3/4) |a|^(-1/2) E^(-1/8),
 C_(2,3/4)
 =12 sqrt(e) (3^(3/4)/4)^(1/6)
 =18.0146285612... .
)`                                                               (5.5)

This enlarges the analytically paid second-volume range beyond the former `1/2` leverage-style gate: a second-compound volume marginal may lie anywhere up to `2/3` and still be absorbed by the third physical square.

More generally, since (5.2) is valid for every fixed `theta>2/3`, any fixed volume-marginal threshold strictly below `3/4` can be paid, with a finite constant depending only on that chosen threshold. No claim is made at the endpoint `3/4`.

## 6. Actual application to the current balanced-hub high-leverage frontier

Return to the source packet in Section 2.2. Set

`xi:=1/64`.

If

`D_U>=xi`,

then the physical wedge identity gives

`E_2(N_U)>=r_U^2 D_U^2 >g^2 xi^2`.                              (6.1)

Apply Theorem 5.1 at `theta=3/4` to the actual outer physical pivot `|a|>=m`. If the `e_2` volume row marginals of `N_U` obey

`max alpha_i<=2/3`,                                               (6.2)

then

`||p_Q||_infinity
 <18.014629 m^(-1/2)(g xi)^(-1/4)
 <141.261`.                                                       (6.3)

The same conclusion holds if the **column** volume marginals are all at most `2/3`, by applying the theorem to `N_U^T`.

Thus an unpaid state with `D_U>=1/64` must now have genuine physical volume anchors on **both** sides:

there exist `i in U` and `j in {p} union V` with

`alpha_i>2/3`, `beta_j>2/3`.                                    (6.4)

By the union bound under the exact squared-minor volume law,

`P_w(i in S and j in T)
 >=alpha_i+beta_j-1>1/3`.                                       (6.5)

Therefore the actual anchored squared-minor mass satisfies

`boxed(
 sum_{S contains i, T contains j}
 det(N_U[S,T])^2
 > (1/3) E_2(N_U)
 > g^2 xi^2/3
 =1/1572864.
)`                                                               (6.6)

This is a source-coordinate localization, not a rotated leverage statement. Every minor in (6.6) contains the same genuine physical row `i` and genuine physical column `j`.

Consequently the old unresolved alternative

`range leverage >1/2`

can be sharpened on every wedge-active side to the following source-valid alternative:

- either the form is paid by (6.3);
- or the wedge deviation is already small, `D_U<1/64`;
- or there is a **two-sided physical second-compound anchor** carrying more than one third of the total `e_2` mass and at least `1/1572864` absolute squared-minor mass.

The identical statement holds with `U,V` interchanged.

This does not finish the balanced-hub or pivot-star branch. It moves the first unpaid analytic implication from generic `>1/2` high leverage to an anchored physical minor bank. The next source-preserving step is to spend (6.6) before selecting one reciprocal minor: separate the cases `j=p` (hub-column anchored wedge mass) and `j in V` (interbank two-anchor mass), and force a quantitative second Schur pivot / grouped-star / already-paid pair packet.

## 7. Designated partner account04/B01 applied to the new inequality

Apply `QFORM-SIGNED-FEJER-EQUIVALENCE-v1` to Theorem 5.1. For every form satisfying its hypotheses,

`boxed(
 sup_{T>0,y} D_T law(Q)(y)
 <=4 [ e * (3theta/(3theta-2)) ]^(1/2)
      K_theta^(-1/(8theta))
      |a|^(-1/2) E^(-1/8).
)`                                                               (7.1)

At `theta=3/4` this is

`sup_{T,y}D_T law(Q)(y)
 <=18.014629 |a|^(-1/2)E^(-1/8)`.                               (7.2)

On the balanced-hub application (6.1), the same exact averaged-frequency quantity is `<141.261` whenever (6.2) holds.

This is an actual application of the designated partner theorem to the new target-level inequality. It also makes the oscillatory interpretation explicit: the proof never asks for false law-uniform scalar pointwise Fresnel decay. The phase-aligned fragmented-support counterexample remains intact. What replaces it is a source-valid **fractional cross-volume averaged-frequency budget**, followed by the exact Fejer density-height interface.

## 8. Quantitative checks

The constants used above are

`m=3501/8000=0.437625`,

`g=1/(8sqrt(2))=0.0883883476483184...`,

`xi=1/64`,

`K_(3/4)=4/3^(3/4)`,

`C_(2,3/4)=12 sqrt(e)(3^(3/4)/4)^(1/6)
           =18.0146285612781...`,

and

`C_(2,3/4)m^(-1/2)(g xi)^(-1/4)
 =141.260418891275... <141.261`.

Also

`g^2 xi^2/3=(1/128)(1/4096)/3=1/1572864`.

These computations only verify displayed constants. The proof is the analytic argument in Sections 4--7.

## 9. Status and first unpaid implication

**Proved in this run:**

1. `QFORM-FRACTIONAL-E2-BL-L3-v1`: a rank-two fractional volume-sampling theorem producing a dimension-free `L^3` density with arbitrary same-side quadratic curvature;
2. `QFORM-FRACTIONAL-E2-BL-SQUARE-v1`: one genuine original physical square upgrades that finite-`p` estimate to an `L^infinity` density bound;
3. the concrete `theta=3/4` gate pays all second-volume packets with maximum volume marginal at most `2/3`;
4. applied to the current balanced-hub wedge packet, every still-unpaid wedge-active side now carries a two-sided physical anchored second-compound mass (6.6);
5. the designated account04/B01 signed-Fejer result converts the new density theorem to the exact averaged-frequency bound (7.1) without constant loss.

**Not proved:** the unrestricted QFORM conjecture; the endpoint `theta=2/3` or volume threshold `3/4`; universal continuity; the final anchored-bank structural payment.

The immediate next implication for this B01 mechanism is:

`QFORM-ANCHORED-E2-FEJER-PAYMENT-v1` (OPEN): use the physical anchored mass (6.6) directly in a signed-Fejer / conditional-product argument, before reciprocal selection of one `2 x 2` minor, to force either a quantitative second Schur pivot or an already-paid grouped-star/rank-two-cross packet.
