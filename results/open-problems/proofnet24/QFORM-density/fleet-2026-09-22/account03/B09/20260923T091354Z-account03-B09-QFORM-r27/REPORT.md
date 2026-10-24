SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-23T09:13:54Z.
attacking: the small-disjointness/high-leverage survivor: first remove the artificial null-self-coefficient restriction from the rank-two cross-bank pivot theorem by an L2 chirp argument, then convert small two-frame Pluecker disjointness into a quantitative weighted star-or-triangle localization certificate.

# account03/B09 r27 — chirp-stable pivot smoothing and weighted two-frame EKR stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: bilinear block mechanism  
Status: **NEW SUPPORTING ANALYTIC THEOREM / NEW STRUCTURAL STABILITY LEMMA / PEER THEOREM APPLIED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains **OPEN**. This run advances the exact small-disjointness/high-leverage branch left by r26 in two ways.

1. The earlier account03/B09 rank-two cross-bank theorem required the promoted physical pivot to be a *null* quadratic pivot. That restriction is unnecessary. The same Plancherel argument is stable under an arbitrary measurable one-variable phase on the pivot, hence in the quadratic-form problem it allows an arbitrary pivot diagonal coefficient and all conditioning-generated linear terms. This is important when a high-leverage physical leaf is promoted to a pivot: one no longer needs `A_ii=0`.
2. For the remaining determinant-balanced two-hub cross frame, small Pluecker disjointness is sharpened from the weak statement “one leverage exceeds about one half” to a quantitative weighted Erdős--Ko--Rado stability dichotomy: the two-frame basis law is either almost a physical star or almost supported on the three edges of one physical triangle. At a concrete threshold `rho<1/512`, one gets either a physical row of leverage `>0.8988` or a physical triple carrying `>0.8879` of the total two-volume.

Both results preserve original-coordinate product provenance. No random coordinate rotation is declared independent. No moment, compact-support, connected-support, log-concavity, Gaussian, diagonal-basis, arbitrary-joint coarea, conditional-density supremum, or law-uniform pointwise van-der-Corput estimate is used. No probability squaring occurs, and every positive density conclusion below is a genuine `O(|L|)` interval bound.

## 1. Fresh controls, corrections, and dependencies

Fresh control was read from `yspennstate/math-research-brain` main; OWNER CONTROL remains revision `2026-09-22.15` under programme `QFORM-DENSITY-3EIG-20260922`, with no B09 stop or pause observed.

The live correction set was reread. In particular this run does **not** use any of the following refuted interfaces:

- law-uniform pointwise quadratic-phase decay;
- arbitrary-joint rank-three coarea from an `L^infinity` joint-density cap;
- post-rotation independence;
- a worst conditional spectral-fiber density cap;
- a guaranteed good fixed physical minor from the three-large-eigenvalue hypothesis.

The direct predecessor is account03/B09 r26,

`yspennstate/math-open-problems@5368af077ca929e49b8dc8adeb3e0cefad85f827`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T074252Z-account03-B09-qform-nearnull-r26/REPORT.md`.

It proved the exact two-frame identity

`rho = 1-sum_i ell_i^2 + sum_(i<j) w_ij^2`,

and showed by an explicit strict-N3 target family that a selected rank-one physical-core resource cannot be forced uniformly from an aggregate cross wedge alone. Its correct next direction was determinant-balanced smoothing followed by source-coordinate localization when disjointness is small.

The completed peer theorem applied below is account02/B09

`QFORM-TWOHUB-PLUCKER-SMOOTHING-v1`,

source

`yspennstate/math-open-problems@bc348aa1a3631b0a0a3a9939cbb6b023578e9abc`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T064043Z-account02-B09-QFORM-r13/REPORT.md`.

For a two-physical-hub / diagonal-leaf packet with cross Gram `G>0` and two-frame disjoint-basis probability `rho>0`, it gives

`||p_Q||_infinity <= 2 sqrt(e) [rho det G]^(-1/4)`              (1.1)

with a continuous density and the same coefficient times interval length. The physical `2 x 2` hub core is arbitrary.

The scalar/vector projection cap used in Section 3 is the completed account02/B06 affine-fiber Brascamp--Lieb theorem,

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,

which gives in particular a two-dimensional projection density cap `<=e` for an original-coordinate cap-one product source.

The designated `account04/B09` current-QFORM memory/handoff remained absent at the final fresh lookup, so no designated-partner result is fabricated or awaited.

## 2. Chirp-stable rank-two cross-bank pivot theorem

The first missing implication is analytic and can be removed completely.

Let `X0`, `U=(U_i)_(i in I)`, and `V=(V_j)_(j in J)` be mutually independent original-coordinate blocks with scalar coordinate density caps one. Let `B` be a real `|I| x |J|` matrix of rank `r>=2`, with nonzero singular values `sigma_1,...,sigma_r` and

`Delta_r(B)=prod_(k=1)^r sigma_k`.

Let `p in R^I` be nonzero and `a!=0`. Let `H0:R->R`, `F:R^I->R`, and `G0:R^J->R` be arbitrary measurable real functions, finite almost surely. Put

`T = H0(X0)+F(U)+G0(V)+2 U^T B V+2 a X0(p^T U+d).`             (2.1)

Write `E=range(B)` and `Fsp=range(B^T)`. Suppose the corresponding projection densities obey

`||rho_(P_E U)||_infinity <= M`,
`||rho_(P_Fsp V)||_infinity <= N`,
`||rho_(p^T U)||_infinity <= L`.                               (2.2)

### Theorem `QFORM-CHIRPED-PIVOT-CROSSBANK-LINF-v1`

The random variable `T` has a bounded continuous density and

`boxed:
||p_T||_infinity
 <= [(r+1)/(r-1)] [M N L/(|a| Delta_r(B))]^(1/(r+1)).`        (2.3)

Therefore every interval `L0` satisfies

`boxed:
P{T in L0}
 <= [(r+1)/(r-1)] [M N L/(|a| Delta_r(B))]^(1/(r+1)) |L0|.`   (2.4)

The novelty relative to r20 is that the pivot self-phase `H0(X0)` is completely arbitrary. In particular the physical quadratic coefficient of `X0^2` need not vanish.

### Proof

Take a thin SVD

`B=P Sigma R^T`,

with `P,R` having `r` orthonormal columns, and set

`Y=P^T U`, `Z=R^T V`.

For fixed `t`, define the **chirped pivot Fourier transform**

`Psi_t(s)=int_R f_0(x) exp(i t H0(x)) exp(2 i a t s x) dx`.     (2.5)

The key point is the exact `L^2` identity. Since multiplication by the unimodular chirp `exp(i t H0(x))` does not change modulus, Plancherel gives

`int_R |Psi_t(s)|^2 ds
 = [1/(2|a t|)] int_R |hat g_t(xi)|^2 dxi
 = [pi/(|a t|)] int_R f_0(x)^2 dx
 <= pi/(|a t|),`                                               (2.6)

where `g_t(x)=f_0(x) exp(i t H0(x))` and `int f_0^2<=int f_0=1`.

Now define the complex amplitudes

`A_t(y)=rho_Y(y) E[exp(i t F(U)) Psi_t(p^T U+d) | Y=y]`,
`C_t(z)=rho_Z(z) E[exp(i t G0(V)) | Z=z].`                     (2.7)

No independence among coordinates of `Y` or `Z` is asserted. Jensen on the conditional probability measure and the cap `rho_Y<=M` give

`|A_t(y)|^2
 <= M rho_Y(y) E[|Psi_t(p^T U+d)|^2 | Y=y].`                  (2.8)

Integrating and using the scalar density cap `L`,

`||A_t||_2^2
 <= M E|Psi_t(p^T U+d)|^2
 <= M L int_R |Psi_t(s)|^2 ds
 <= M L pi/(|a t|).`                                           (2.9)

Hence

`||A_t||_2 <= [M L pi/(|a t|)]^(1/2).`                         (2.10)

Likewise `||C_t||_2<=N^(1/2)`.

The exact bilinear representation is

`phi_T(t)=int int A_t(y) C_t(z) exp(2 i t y^T Sigma z) dy dz`.  (2.11)

Rank-`r` bilinear Plancherel therefore yields

`|phi_T(t)|
 <= pi^(r/2)|t|^(-r/2) Delta_r(B)^(-1/2)
    ||A_t||_2 ||C_t||_2`                                      (2.12)

and hence

`|phi_T(t)|
 <= pi^((r+1)/2)
    [M N L/(|a|Delta_r(B))]^(1/2)
    |t|^(-(r+1)/2).`                                           (2.13)

Because `r>=2`, the exponent `(r+1)/2>1`. Combining (2.13) with `|phi_T(t)|<=1` and integrating the envelope exactly gives

`int_R |phi_T(t)| dt
 <= 2[(r+1)/(r-1)] pi
    [M N L/(|a|Delta_r(B))]^(1/(r+1)).`                        (2.14)

Fourier inversion gives (2.3), integrability gives continuity, and integrating the density over an interval gives (2.4). QED.

This proof is *not* pointwise stationary phase in `X0`; the entire pivot phase can be adversarial. Only the `L^2` norm of a Fourier transform is used, so the phase-aligned fragmented-support correction is fully respected.

## 3. Physical corollary: the pivot diagonal is free

Partition original coordinates as

`{0} union I union J union O`.

Assume only

`p=A_(0,I) !=0`,
`A_(0,J)=0`,
`rank A_(I,J)=r>=2`.                                           (3.1)

There is **no condition on `A_00`**. There is also no condition on `A_II,A_JJ,A_OO` or on couplings involving `O`.

Condition on `X_O`. All terms depending only on `X_0` become an allowed one-variable phase

`H0(x_0)=A_00 x_0^2 + (conditioning-generated linear term)*x_0`,

while the active cross terms are exactly of the form (2.1). Thus Theorem 2 applies uniformly in the conditioning.

### Corollary `QFORM-QUADRATIC-PIVOT-RANK2-CROSS-v1`

At rank two,

`boxed:
||p_(X^T A X)||_infinity
 <= 3 [M N L/(sigma_1(A_IJ)sigma_2(A_IJ))]^(1/3),`             (3.2)

with the same coefficient times interval length, and with continuity on this branch.

This strictly extends the r20 “null pivot” corollary: a nonzero or arbitrarily large physical pivot diagonal does not cost anything.

### Promoted physical leaf corollary

Now let the active coordinates consist of two literal physical hubs `H={h_1,h_2}` and a leaf bank with cross rows `c_j in R^2`. Let

`C` be the leaf-by-two cross matrix,
`G=C^T C>0`.

Pick a physical leaf `i` which has **no off-diagonal coupling to the remaining active leaf bank** (this holds, in particular, when the leaf principal block is diagonal). Promote `X_i` to `X0`; take the two physical hubs as `U` and the remaining leaves as `V`. Put

`ell_i=c_i^T G^(-1)c_i`.                                      (3.3)

If the residual cross block has rank two, then

`Delta_2(A_(H,leaf\{i}))
 = sqrt(det(G-c_i c_i^T))
 = sqrt(det G * (1-ell_i)),`                                  (3.4)

by the matrix determinant lemma.

For the two physical hubs, the joint density cap is exactly `M<=1`. The completed account02/B06 theorem gives `N<=e` for the rank-two projection of the remaining product leaf bank. Finally, the elementary two-coordinate conditioning bound gives

`L=||p_(c_i^T X_H)||_infinity <= sqrt(2)/||c_i||_2`:           (3.5)

if `|c_(i,1)|>=|c_(i,2)|`, condition on the second hub and use the first marginal density cap, then `1/|c_(i,1)|<=sqrt(2)/||c_i||`.

Substitution into (3.2) gives the explicit source-coordinate payment

`boxed:
||p_Q||_infinity
 <= 3 e^(1/3) 2^(1/6)
    [ ||c_i||_2 sqrt(det G(1-ell_i)) ]^(-1/3)
 <4.700 [ ||c_i||_2 sqrt(det G(1-ell_i)) ]^(-1/3).`            (3.6)

Every interval obeys the same coefficient times its length, and the branch has a continuous density.

Thus a high-leverage physical leaf can be promoted without first asking that its diagonal coefficient vanish. The only remaining analytic failure of this promotion is genuine collapse of the residual rank-two cross volume or of the physical coupling scale itself.

## 4. Weighted two-frame EKR stability

The r26 two-frame identity detects high leverage but is quantitatively weak when `rho` is very small. The following elementary stability lemma extracts the exact star/triangle geometry of a nearly intersecting weighted edge law.

Let `mu=(mu_e)` be a probability distribution on the two-element subsets (edges) of an arbitrary finite ground set. Let `E,E'` be iid with law `mu`, and set

`rho=P(E cap E'=empty).`                                       (4.1)

For a vertex `v`, let

`d_v=P(v in E)`                                                (4.2)

be its star mass. For a triangle `S={i,j,k}`, let

`t_S=sum_(e subset S, |e|=2) mu_e`                             (4.3)

be the mass of its three internal edges.

### Theorem `QFORM-WEIGHTED-EKR-2FRAME-STABILITY-v1`

Assume `0<rho<1/4` and put

`tau=(rho/2)^(1/3) <1/2`.                                     (4.4)

Then at least one of the following holds:

`boxed: max_v d_v >= 1-rho-tau,`                              (4.5)

or

`boxed: max_(|S|=3) t_S >= 1-rho-tau/(1-tau).`                (4.6)

So a nearly intersecting weighted two-basis law is quantitatively either star-like or triangle-like.

### Proof

For an edge `e={i,j}`, let

`m(e)=P(E' cap e !=empty)=d_i+d_j-mu_(ij).`                    (4.7)

Averaging over `E`,

`E[m(E)]=P(E cap E' !=empty)=1-rho`.                           (4.8)

Hence some edge `{i,j}` satisfies

`m({i,j})>=1-rho`.                                             (4.9)

Decompose the edge mass relative to this pair as

`a=mu_(ij)`,
`p_k=mu_({i,k})`,
`q_k=mu_({j,k})`,
`P=sum_k p_k`, `Q=sum_k q_k`,                                 (4.10)

where `k` ranges outside `{i,j}`, and let `r` be the mass of edges disjoint from `{i,j}`. Equation (4.9) says

`r<=rho`,
`a+P+Q=1-r`.                                                   (4.11)

Ordered pairs `{i,k}` and `{j,l}` are disjoint exactly when `k!=l`. Therefore their contribution to `rho` gives

`2(PQ-sum_k p_k q_k) <= rho`.                                 (4.12)

If `P<=tau`, then the star at `j` has mass

`d_j=a+Q=1-r-P >=1-rho-tau`,                                  (4.13)

proving (4.5). The case `Q<=tau` is symmetric.

Assume therefore `P,Q>tau`. Normalize

`p'_k=p_k/P`, `q'_k=q_k/Q`.

From (4.12),

`I:=sum_k p'_k q'_k
 >=1-rho/(2PQ)
 >1-rho/(2tau^2)
 =1-tau`,                                                      (4.14)

where `tau^3=rho/2` was used.

Since `I<=max_k p'_k`, choose `k_*` with

`p'_(k_*)>=1-tau`.                                             (4.15)

Also

`I
 <= p'_(k_*) q'_(k_*) + (1-p'_(k_*))
 =1-p'_(k_*)(1-q'_(k_*))`.                                    (4.16)

Combining (4.14)-(4.16),

`q'_(k_*)
 >=1-tau/p'_(k_*)
 >=1-tau/(1-tau).`                                             (4.17)

The triangle `{i,j,k_*}` therefore carries mass

`t_{ijk_*}
 =a+p_(k_*)+q_(k_*)`

`>=a+P(1-tau)+Q(1-tau/(1-tau))`

`>=1-r-rho*0 - tau/(1-tau)(P+Q)`

`>=1-rho-tau/(1-tau),`                                        (4.18)

which is (4.6). QED.

(The harmless `rho*0` in the penultimate display only emphasizes that the entire outside-pair loss has already been isolated as `r<=rho`.)

### Pluecker interpretation

Let `U in R^(N x 2)` have orthonormal columns and use its Pluecker basis law

`mu_({i,j})=w_ij=det(u_i,u_j)^2`.

Then

`d_i=sum_(j!=i) w_ij=||u_i||^2=ell_i`.                        (4.19)

For a physical triple `S`, Cauchy--Binet gives

`t_S=sum_({i,j} subset S) w_ij = det(U_S^T U_S).`              (4.20)

Thus the triangle branch is not merely combinatorial. If `t_S>=beta`, both eigenvalues of `U_S^T U_S` lie in `[beta,1]`, and therefore

`boxed:
I_2-U_S^T U_S <= (1-beta) I_2.`                               (4.21)

So three literal physical rows capture both whitened cross directions up to operator error `1-beta`.

At the concrete threshold

`rho_0=1/512`,
`tau_0=(1/1024)^(1/3)=0.099212565748...`,                       (4.22)

the small-disjointness branch `rho<rho_0` yields either

`boxed: ell_i>0.8988343092`                                   (4.23)

for one physical row, or a physical triple `S` with

`boxed: det(U_S^T U_S)>0.8879070551,`
`boxed: I_2-U_S^T U_S <0.1120929449 I_2.`                      (4.24)

This is a much sharper source-coordinate localization certificate than the previous generic `ell_i>(1-rho)/2` consequence.

## 5. Apply the completed two-hub theorem at an actual inequality

Return to a two-physical-hub / diagonal-leaf packet with cross Gram `G>0`. Apply account02/B09's completed theorem (1.1) with the threshold `rho_0=1/512`.

If

`rho>=1/512`,

then

`boxed:
||p_Q||_infinity
 <=2 sqrt(e) (512/det G)^(1/4)
 <15.686 (det G)^(-1/4).`                                     (5.1)

The density is continuous and every interval `L` satisfies

`P{Q in L}<15.686(det G)^(-1/4)|L|`.                           (5.2)

If instead `rho<1/512`, Theorem 4 gives the explicit star/triangle alternatives (4.23)-(4.24). In the star alternative, because the leaf block is diagonal the high-leverage physical leaf has no coupling to the remaining leaves and can be promoted. Whenever its chirped-pivot resource

`R_i=||c_i|| sqrt(det G(1-ell_i))`                              (5.3)

satisfies `R_i>=kappa>0`, Corollary (3.6) gives

`boxed:
||p_Q||_infinity <4.700 kappa^(-1/3),`                         (5.4)

again with continuity and an `O(|L|)` interval bound.

Thus, in this exact two-hub diagonal-leaf scope, the only small-disjointness states not paid by the combination of the completed peer theorem and the new chirped-pivot theorem are now geometrically explicit:

1. a **near-star** with `ell_i>0.8988` but tiny promoted resource `R_i`; or
2. a **near-triangle** in which three literal physical leaves capture at least `88.79%` of the whitened two-volume in the strong operator sense (4.24).

These are finite/localized structural outputs, not a recurrence of the diffuse small-minor problem.

## 6. Target-valid regression where the old null-pivot theorem did not apply

Take five independent cap-one original coordinates ordered as

`(X0,U1,U2,V1,V2)`

and define

`Q=X0^2+2 X0 U1+2 U1 V1+2 U2 V2`.                              (6.1)

The coefficient matrix is

`A=[[1,1,0,0,0],
    [1,0,0,1,0],
    [0,0,0,0,1],
    [0,1,0,0,0],
    [0,0,1,0,0]].`                                             (6.2)

Here the pivot has `A_00=1`, so the old r20 null-pivot corollary does not apply. In Theorem 2 take

`H0(x)=x^2`, `p=(1,0)`, `B=I_2`, `a=1`.

Because `U` and `V` are themselves two physical product coordinates,

`M=N=L=1`, `Delta_2(B)=1`.                                    (6.3)

Therefore

`boxed: ||p_Q||_infinity <=3,`
`boxed: P{Q in L}<=3|L|.`                                     (6.4)

The density is continuous.

This is a literal target matrix. The `(U2,V2)` block contributes eigenvalues `{-1,1}`. The remaining `3 x 3` block has characteristic polynomial

`lambda^3-lambda^2-2lambda+1`.                                (6.5)

Its value is positive at `lambda=-1` and negative at `lambda=-2`, so it has one eigenvalue below `-1`; it is negative at `lambda=1` and positive at `lambda=2`, so it has one eigenvalue above `1`. Hence the full matrix has at least four eigenvalues of modulus at least one. Numerically the spectrum is

`{-1.2469796037,-1,0.4450418679,1,1.8019377358}`.              (6.6)

Thus the new chirp-stable theorem closes a target-valid branch genuinely outside the old null-pivot hypothesis.

## 7. What remains

The full conjecture is **not** proved. The new structural debt is narrower than r26:

`QFORM-TWOFRAME-NEARSTAR-OR-NEARTRIANGLE-PAYMENT-v1`.

In the two-hub determinant-balanced branch, after the large-`rho` peer payment and the new chirped-pivot payment, prove one of the following without treating small coefficients as small random errors on unbounded laws:

- **near-star:** if a physical row has leverage `>0.8988` but `R_i` in (5.3) is tiny, convert the nearly rank-one residual cross bank into an existing star/ridge/grouped-square payment, retaining the actual pivot diagonal and all same-bank curvature;
- **near-triangle:** if three physical rows capture `>0.8879` of the whitened two-frame, promote/localize those literal coordinates and route the residual operator-norm tail to an already-paid finite-core, multihub, ridge, or anchored-volume mechanism.

The latest completed account01/B09 `QFORM-MULTIHUB-PLUCKER-SMOOTHING-v1` is compatible with this route when a promoted physical coordinate genuinely contributes a new cross direction; it does not by itself pay the diagonal-leaf near-star because the promoted leaf has no cross column to the remaining leaves.

The unrestricted essential-boundedness conjecture remains **OPEN**. Full-target continuity remains **OPEN**. Continuity is proved on the exact positive theorem branches in Sections 2, 3, 5, and 6.

## 8. Finite checks

`CHECK.py` beside this report verifies:

- the threshold constants in (4.22)-(4.24) and (5.1);
- the promoted-pivot constant `3 e^(1/3)2^(1/6)=4.6995659439...`;
- the determinant-leverage identity `det(G-c c^T)=det(G)(1-c^T G^-1 c)` on random full-rank frames;
- the target regression spectrum (6.6);
- 8,452 concentrated random weighted edge laws with `rho<1/4`, finding no violation of Theorem 4. The random check is regression evidence only; the proof of Theorem 4 is the exact argument above.

## 9. Integrity / privacy note

The changed-file allowlist for this run is confined to this immutable account03/B09 mathematics bundle plus the corresponding short handoff, worker-owned memory snapshot/pointer, login/finish/receipt records. No credentials, personal data, financial/company/client material, benchmark keys, public release, email, notification, schedule, workflow, permission, or cross-account authentication state is touched. No repository-local secret scanner was available through the connector; a narrow manual content review of the changed text/code found only mathematical constants, repository pins, and nonsecret run metadata.
