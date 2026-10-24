SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T00:50:18Z.
attacking: diffuse rank-one bilinear half-Riesz smoothing with arbitrary opposite-bank curvature, then an external square; apply it to a genuine N3 family and close the explicit spike/dust route-counterexample family.

# account01/B09 r20 — diffuse rank-one fractional endpoint and external-square closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `B09-20260923T005018Z-r20`  
Assignment: Bilinear block mechanism  
Method emphasis: analytic derivation / exact structural identities  
Status: **ESSENTIAL_STEP_APPLIED / NEW_SUPPORTING_THEOREM / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. This report proves a new rank-one *fractional* endpoint of the previously proved diffuse separable-phase bilinear estimate, and then turns it into a genuine `L^infinity` density bound by a disjoint square smoother. It also observes that the explicit Hadamard spike/dust family recently introduced as an obstruction to robust second-singular-value extraction is itself already paid by a source-matched arbitrary-rank half-Riesz theorem. Neither statement is a proof of the full conjecture.

Fresh owner control immediately before publication remained QFORM-only at OWNER CONTROL revision `2026-09-22.15`. The live correction ledger was reread. In particular this proof does not use law-uniform pointwise van der Corput decay, post-rotation independence, a conditional spectral-density cap, an arbitrary-joint rank-three coarea estimate, a single good local minor, or the false one-heavy-row-plus-own-square absorption rule.

## 1. Source pins and duplicate-work audit

The main analytic source is my earlier B09 theorem `QFORM-ONE-SIDED-SEPARABLE-CROSS-DIFFUSE-v1`, canonical

`yspennstate/math-open-problems@3e5068e27a41e88ec5a59311b64e9b95ee4babd6`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/B09-20260922T184627Z-r15/REPORT.md`.

Its proof established, for rank `r>=2`, the characteristic-function estimate

`|phi_T(t)| <= min(1, ((sqrt(2) pi)^r B_U)/(D |t|^r))`,               (1.1)

where `D=prod s_l(B)` and `B_U=prod_i(1-c_i)^(-(1-c_i)/2)` for the left singular-frame leverages `c_i`. The derivation of (1.1) itself is valid already for `r=1`; only the final density inversion in that report required `r>=2`.

The underlying complex-amplitude Brascamp--Lieb/Hausdorff--Young input is

`QFORM-DIFFUSE-SEPARABLE-PHASE-v1`,
`yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`,
`proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`.

I checked nearby fractional results before claiming a new scope:

* account01/B14 `QFORM-RANK2-DIFFUSE-SEPARABLE-HALF-RIESZ-v1` treats rank-two *quadratic projected curvature* with coordinatewise perturbations, not the rank-one bilinear geometry below;
* account02/B18 `QFORM-ONE-SIDED-CROSS-HALF-RIESZ-v1` treats arbitrary-rank bilinear cross matrices and even gives a rank-one endpoint, but requires zero self-quadratic term on one cross bank; its coefficient-side function can be arbitrary;
* my B09 r16 `QFORM-HALFRIESZ-ZEROPIVOT-ONECROSS-v1` treats one physical scalar with zero square coefficient crossing an arbitrary opposite-bank function, but does not aggregate a diffuse multi-coordinate coefficient bank carrying arbitrary coordinate-separable curvature.

Thus the exact theorem below is not a duplicate of those scopes: it allows a **rank-one bilinear cross**, arbitrary measurable curvature on the entire opposite bank, and arbitrary coordinate-by-coordinate measurable curvature on the diffuse coefficient bank.

A second source-matched input used in Section 6 is account02/B18:

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260922T181504Z-account02-B18-QFORM-r12/REPORT.md`,
claim `QFORM-ONE-SIDED-CROSS-HALF-RIESZ-v1`.

The newest designated partner account02/B09 result was also read in full:

`yspennstate/math-open-problems@74484a59609ced9b80417aab0f22095d307e2174`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T004108Z-account02-B09-QFORM-auto11/REPORT.md`,
claim `QFORM-ONE-HUB-RANKR-MIXEDFRAME-v1`. It is applied quantitatively in Section 7.

## 2. First essential missing implication attacked

The latest N3/no-pivot structural work leaves two difficult types of geometry: mixed source-coordinate hubs with overlapping same-bank curvature, and a high-dimensional spike/dust cross block in which a robust second singular direction may be arbitrarily small.

A natural analytic question is whether rank-one cross geometry is truly lost once both sides carry curvature. The answer is **no** if one side's curvature is coordinate-separable and its rank-one cross direction is diffuse. The density itself remains at the logarithmic Fourier endpoint, but its half-Riesz potential is uniformly bounded. A genuinely disjoint square then supplies exactly the missing half derivative, giving a linear interval bound without probability squaring.

## 3. Main theorem — diffuse rank-one bilinear half-Riesz with arbitrary opposite-bank curvature

Let `X=(X_i)_(i in I)` and `Y=(Y_j)_(j in J)` be disjoint original-coordinate banks. All coordinates are mutually independent and have probability densities bounded by one. Let

`B = sigma u v^T`, `sigma>0`, `||u||_2=||v||_2=1`,                    (3.1)

be rank one. Assume the left direction is diffuse:

`c_i=u_i^2 <=1/2` for every `i`.                                    (3.2)

Let `W_i:R->R` and `H:R^J->R` be arbitrary measurable functions finite almost surely. Put

`T = sum_i W_i(X_i) + 2 X^T B Y + H(Y)`.                             (3.3)

Define

`B(u)=prod_(i:c_i>0) (1-c_i)^(-(1-c_i)/2)`.                          (3.4)

Because `sum_i c_i=1` and `-(1-c)log(1-c)<=c`,

`B(u)<=e^(1/2)`.                                                       (3.5)

### Theorem 3.1 — `QFORM-DIFFUSE-RANK1-SEPARABLE-BILINEAR-HALFRIESZ-v1`

For every real `w`,

`boxed: E |T-w|^(-1/2)
 <= 2^(11/4) B(u)^(1/2) sigma^(-1/2)
 <= 2^(11/4) e^(1/4) sigma^(-1/2)
 < 8.638 sigma^(-1/2).`                                               (3.6)

No moment, support, smoothness, centering, sign, connected-support, or identical-law assumption is used. In particular `H(Y)` may contain an arbitrary quadratic form on the whole opposite bank, including indefinite and dense curvature. The only self-structure assumption is that the `X`-bank contribution outside the cross term is coordinate-separable.

### Proof

For frequency `t`, put

`h_(i,t)(x)=f_i(x) exp(i t W_i(x))`.                                  (3.7)

Conditioning on `Y=y` and using product structure of the original `X_i`,

`E_X exp[i t(sum_i W_i(X_i)+2X^TBy)]
 = prod_i hat h_(i,t)(-2t sigma u_i <v,y>)`.                          (3.8)

Take absolute values only after the product has formed. Set

`Z=<v,Y>`.

This is a genuine one-dimensional orthogonal marginal of an original product bank, so the Livshyts--Paouris--Pivovarov product-marginal theorem gives a density `rho_Z` with

`||rho_Z||_infinity <= sqrt(2)`.                                      (3.9)

The arbitrary phase `exp(itH(Y))` has modulus one, hence

`|phi_T(t)|
 <= sqrt(2) int_R prod_i |hat h_(i,t)(2t sigma u_i z)| dz`.            (3.10)

For `t!=0`, set `xi=2t sigma z`. Then

`|phi_T(t)|
 <= [sqrt(2)/(2|t|sigma)]
    int_R prod_i |hat h_(i,t)(u_i xi)| dxi`.                          (3.11)

The one-dimensional specialization of the source-pinned separable-phase Brascamp--Lieb/Hausdorff--Young theorem gives

`int_R prod_i |hat h_(i,t)(u_i xi)| dxi <= 2 pi B(u)`.                (3.12)

Therefore

`boxed: |phi_T(t)| <= min(1, K/|t|),
        K = sqrt(2) pi B(u)/sigma.}`                                  (3.13)

This is not a forbidden one-dimensional van-der-Corput estimate. The `|t|^-1` appears only after aggregating the **entire original product X-bank** by geometric Brascamp--Lieb and the genuine product marginal `v^T Y`; arbitrary coordinatewise phases remain inside the complex amplitudes.

Use the standard Riesz-kernel identity, justified by Abel/Gaussian regularization,

`widehat(|x|^(-1/2))(t)=sqrt(2pi)|t|^(-1/2)`.                         (3.14)

Because the majorant below is integrable, Fourier inversion gives uniformly in `w`

`E|T-w|^(-1/2)
 <= (2pi)^(-1/2) int_R |t|^(-1/2)|phi_T(t)| dt`.                      (3.15)

With (3.13),

`int_R |t|^(-1/2) min(1,K/|t|) dt
 = 2[ int_0^K t^(-1/2)dt + K int_K^infinity t^(-3/2)dt ]
 = 8 sqrt(K).`                                                        (3.16)

Substituting `K=sqrt(2)pi B(u)/sigma` into (3.15) gives

`(8/sqrt(2pi)) sqrt(sqrt(2)pi B(u)/sigma)
 = 2^(11/4) B(u)^(1/2) sigma^(-1/2)`,                                 (3.17)

which proves (3.6). QED.

### Why this is exactly the fractional endpoint

The characteristic envelope `|t|^-1` is not integrable and therefore does **not** prove an `L^infinity` density for `T`. After multiplication by the half-Riesz weight `|t|^-1/2`, it becomes `|t|^-3/2`, which is integrable. Thus the theorem asks for exactly the amount of regularity that one further independent square can convert into a bounded density.

## 4. External-square transducer and the direct `O(|I|)` bound

Let `Z` be a random variable coming from a third disjoint original-coordinate bank, independent of `(X,Y)`, with density cap `K_Z`. Let `m(X,Y)` be arbitrary measurable and let `a!=0`. Define

`Q = T + a (Z+m(X,Y))^2`.                                             (4.1)

Conditionally on the base variables, and hence also conditionally on `T=r`, the shifted variable `Z+m(X,Y)` is a mixture of translations of the law of `Z`; its conditional density remains at most `K_Z`. The dependence-safe square transducer from account02/B18 therefore gives

`||p_Q||_infinity
 <= K_Z |a|^(-1/2) sup_w E|T-w|^(-1/2).`                             (4.2)

Combining with Theorem 3.1 yields the new density endpoint

### Corollary 4.1 — `QFORM-DIFFUSE-RANK1-SEPARABLE-EXTERNAL-SQUARE-v1`

`boxed: ||p_Q||_infinity
 <= 2^(11/4) K_Z B(u)^(1/2) (|a| sigma)^(-1/2)
 <= 2^(11/4) e^(1/4) K_Z (|a|sigma)^(-1/2).}`                        (4.3)

Hence every interval `L` satisfies

`boxed: P{Q in L}
 <= 2^(11/4) e^(1/4) K_Z (|a|sigma)^(-1/2) |L|.`                     (4.4)

For one genuine physical scalar coordinate, `K_Z<=1`. For a unit linear projection of a disjoint product bank, LPP gives `K_Z<=sqrt(2)`. The scaling is correct: under simultaneous coefficient scaling by `lambda`, the product `|a|sigma` scales as `lambda^2`, so the right side scales as `|lambda|^-1`.

This proves an essentially bounded density. **Continuity is not claimed** from the transducer under merely measurable input densities.

## 5. A genuine N3 target family with opposite-bank curvature

Take three disjoint physical banks `I,J,K`, each of size `m`, and flat unit vectors

`u=v=w=m^(-1/2)(1,...,1)`

on the respective banks. Set

`U=<u,X_I>`, `V=<v,X_J>`, `W=<w,X_K>`,

and define

`Q_m = 4 U V + V^2 + W^2.`                                           (5.1)

In the scalar basis `(U,V,W)`, the quadratic coefficient matrix is

`G=[[0,2,0],[2,1,0],[0,0,1]]`.                                       (5.2)

Its eigenvalues are

`(1+sqrt(17))/2`, `(1-sqrt(17))/2`, `1`,                             (5.3)

so all three have modulus at least one. This is an exact full-target family.

At physical-coordinate level, the only nonzero coefficients have magnitude at most `2/m`; every physical diagonal has magnitude at most `1/m`; and every physical `2x2` principal determinant has magnitude at most `4/m^2`. Therefore for `m>=129`,

`Q_m` lies strictly in the sufficient no-pivot class `N3(1/128)`.      (5.4)

Apply Corollary 4.1 with rank-one cross singular value `sigma=2`, arbitrary opposite-bank term `H(Y)=V^2`, no `X`-side self term, square coefficient `a=1`, and external bank projection `W`, whose density cap is at most `sqrt(2)`. For the flat vector,

`B(u)=(1-1/m)^(-(m-1)/2)<e^(1/2)`.                                   (5.5)

Thus

`boxed: ||p_(Q_m)||_infinity
 <= 2^(11/4) B(u)^(1/2)
 < 2^(11/4)e^(1/4)
 < 8.638,}`                                                           (5.6)

and

`boxed: P{Q_m in L}<8.638 |L|.}`                                     (5.7)

The point is not the constant. The third large direction is stored in a **dense grouped square**, the cross direction is rank one, and the opposite cross bank already carries nonzero same-bank curvature. All fixed physical coefficients vanish as `m` grows, yet the aggregate product-preserving estimate stays dimension free.

## 6. The explicit spike/dust route-counterexample family is analytically paid

The latest account02/B20 report introduced a target-valid Hadamard family to refute the structural shortcut `E_2(D)>c, E_3(D) small => sigma_1(D)sigma_2(D)>c'`. Its cross block has singular values

`sigma_1(D_M)=sqrt(M)`,
`sigma_2(D_M)=1/(4 sqrt(2) M^(3/2))` in the displayed construction,     (6.1)

so `sigma_1 sigma_2=1/(4sqrt(2)M)->0`. The full target matrix is

`A_M=[[0,D_M,0],[D_M^T,0,0],[0,0,w w^T]]`,                           (6.2)

where the last bank has 256 coordinates and `w=(1/16,...,1/16)`, hence `||w||=1`. The family lies in `N3(1/128)` for `M>=128` and has at least the eigenvalues `+sqrt(M),-sqrt(M),+1`.

This family is **not** an analytic obstruction. Apply the already completed account02/B18 theorem `QFORM-ONE-SIDED-CROSS-HALF-RIESZ-v1` to

`R=2 X_L^T D_M X_R`.

Its `j=1` endpoint gives

`sup_t E|R-t|^(-1/2)
 <=8 sigma_1(D_M)^(-1/2)
 =8 M^(-1/4).`                                                        (6.3)

The external projection `W=<w,X_W>` is independent of `R` and has density cap at most `sqrt(2)`. Applying the same square transducer gives

`boxed: ||p_(X^T A_M X)||_infinity
 <=8 sqrt(2) M^(-1/4).}`                                              (6.4)

Therefore for every `M>=128`,

`boxed: ||p_(X^T A_M X)||_infinity <3.364,}`                          (6.5)

and every interval satisfies the same coefficient times its length.

So the Hadamard spike/dust family remains a valid **counterexample to robust second-singular-direction extraction**, but it is now explicitly closed as a density branch. The genuinely hard spike/dust survivor must entangle its third spectral resource with the spike/dust banks or retain nonseparable self-curvature on both sides; a disjoint grouped square already pays it.

## 7. Newest designated partner account02/B09 applied to an actual inequality

The newest partner theorem `QFORM-ONE-HUB-RANKR-MIXEDFRAME-v1` states, for one physical hub and a leaf block

`A_II=D+sum_(k=1)^r lambda_k v_kv_k^T`,

that if the mixed Gram `G=sum_i rho_i rho_i^T` is positive definite and every mixed row leverage is at most `1/2`, then

`||p_Q||_infinity
 <= C_r [det(G) prod_k|lambda_k|]^(-1/(r+2)).`                        (7.1)

For `r=1`,

`C_1=3*2^(4/3)<7.560`,
`det G=||v wedge c||^2`, where `c=A_Ih`.                              (7.2)

Apply this to the partner's explicit target family with even `m>=129`,

`Q_m^hub=2X_h<c,X_I>+<v,X_I>^2`,                                    (7.3)

where `c` and `v` are orthogonal flat unit vectors. Then

`G=I_2`, `lambda=1`, and every row leverage is `2/m<=1/2`.            (7.4)

Moreover its physical diagonals and hub-leaf principal determinants equal `0` or `1/m`, so for `m>=129` it lies in `N3(1/128)`. Substituting (7.4) into (7.1) gives the actual partner-paid inequality

`boxed: ||p_(Q_m^hub)||_infinity
 <=3*2^(4/3)<7.560,}`                                                 (7.5)

hence

`boxed: P{Q_m^hub in L}<7.560 |L|.}`                                 (7.6)

This partner exit is complementary to Corollary 4.1. The partner keeps a **nonseparable rank-one square on the same leaf bank** by requiring a transverse mixed wedge; the new theorem keeps **arbitrary opposite-bank curvature** by requiring a diffuse rank-one coefficient bank and spending a genuinely external square.

## 8. What remains unpaid

This run changes the first B09 analytic debt to

`QFORM-N3-OVERLAPPING-SPIKEDUST-NONSEPARABLE-v1`:

within the no-pivot survivor, after the D5/high-volume, physical-pair, ridge, gapped three-bank, mixed-hub-wedge, and disjoint-external-square exits are removed, pay a spike/dust or degree-dropped packet in which the third spectral resource is genuinely **overlapping** and both candidate coefficient banks carry nonseparable curvature. Equivalently, prove a product-provenance fractional-potential estimate that keeps the third direction unconditioned rather than replacing it by a conditional density cap.

The newest B20 structural results make this precise: in the low-`E_3` spike branch the leading singular direction carries a quantitative dust reserve `lambda_1 sum_(j>=3)lambda_j>23/2400`, while the explicit Hadamard model shows that no single robust second singular value can be forced. Section 6 shows that the direct-sum external-square realization of this geometry is already harmless. Thus future work should target the **overlap** between the spike direction, dust, and the third spectral resource, not try again to force `sigma_2`.

## 9. Status

**Proved in this run:**

1. `QFORM-DIFFUSE-RANK1-SEPARABLE-BILINEAR-HALFRIESZ-v1`, equation (3.6).
2. `QFORM-DIFFUSE-RANK1-SEPARABLE-EXTERNAL-SQUARE-v1`, equations (4.3)-(4.4).
3. A target-valid N3 curved family `4UV+V^2+W^2` has universal density bound `<8.638`.
4. The explicit B20 Hadamard spike/dust route-counterexample family is analytically paid by the source-matched arbitrary-rank half-Riesz theorem with bound `8sqrt(2)M^(-1/4)<3.364` for `M>=128`.
5. The newest designated partner account02/B09 mixed-hub result was applied at a real N3 target inequality, giving `<7.560`.

**Not proved:** the full QFORM conjecture; extraction of one of these packets from every N3 matrix; continuity of the densities in the two new square-transducer endpoints.

No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis, post-rotation-independence, Monte Carlo, or worst-fiber hypothesis was introduced.