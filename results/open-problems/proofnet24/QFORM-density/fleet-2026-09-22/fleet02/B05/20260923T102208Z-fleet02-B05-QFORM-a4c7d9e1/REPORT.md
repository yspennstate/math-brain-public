SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B05, 2026-09-23T10:22:08.593825Z.
attacking: the residual-diffuse heavy-null two-sheet branch; quantify the longitudinal leakage left after two transverse product banks and pay both the nonzero cross-volume collar and the exact zero endpoint without a curved-fiber supremum.

# fleet02/B05 — two-bank longitudinal innovation collar and exact zero endpoint

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Quadratic coarea bound / complementary constructions and source-valid counterexamples  
**Run:** `20260923T102208Z-fleet02-B05-QFORM-a4c7d9e1`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / PRECISE_MISSING_FACTOR_SHARPENED / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** continuous on the positive-innovation cross-block branch; only essential boundedness is asserted at the exact zero-innovation endpoint.

The full conjecture remains OPEN. Nothing below assumes moments, bounded support, connected support, log-concavity, identical laws, a diagonal independent basis, or independence after spectral rotation.

## 1. First unpaid implication, stated before the calculation

The ruled one-sheet half-line is already paid at rough interval level. The current exact-rank-three two-sheet survivor can be taken to have a heavy physical row with zero quadratic pivot, while every complementary row is diffuse in the residual transverse two-plane. A completed structural theorem then splits the transverse plane into two genuinely independent original-coordinate banks, each quantitatively nondegenerate.

The missing quantity inside those two banks is not another determinant atom. It is the component of the **longitudinal coefficient row which is orthogonal to the transverse two-row span inside each bank**.

This report introduces the exact bank innovations `tau_J,tau_K` and proves:

1. if `tau_J tau_K>0`, the physical `J|K` cross block has exact rank three with singular-volume

   `Gamma >= tau_J tau_K/640`,

   so the completed exact-rank-three cross-block Fourier theorem gives

   `||p_Q||_infinity <51.707 (tau_J tau_K)^(-1/3)`;

2. if either innovation is exactly zero, condition on the other original-coordinate bank and use the completed dependence-safe null-scalar/dependent-pair theorem to get the **uniform endpoint bound**

   `||p_Q||_infinity <100.711`.

Thus both the positive collar away from zero and the exact zero endpoint are paid. The remaining problem is genuinely **punctured**: obtain a bound uniform as `0<min(tau_J,tau_K)->0` without deleting that small coefficient as a random perturbation and without turning the same-bank dependent projection into fictitious independent coordinates.

That is the first unpaid implication after this run:

**`QFORM-NULLROW-PUNCTURED-INNOVATION-BRIDGE-v1`.**

## 2. Source inputs actually used

### 2.1 Required newest-Claude source

I read all three required files at the owner-pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`:

- `RESULTS.md`, including Theorem F (Fresnel--Brascamp--Lieb), Theorem H and Theorem D;
- `FOURIER_ROUTE_REPORT.md`, including the audited Theorem F/D statements and relaxed cross-volume variants;
- `COUNTEREXAMPLE_SEARCH.md`, including the ruled one-sheet theorem and the explicit statement that the convex/two-sheet side remains the rank-three geometric difficulty.

Theorem F is applied quantitatively in Section 8 below to remove the deletion-diffuse collar; this is a real inequality, not a citation-only mention.

### 2.2 Prior B05 result

The preceding fleet02/B05 report

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260923T092247Z-fleet02-B05-QFORM-r19/REPORT.md`

proved the pivot-free leave-one-out Fresnel theorem and established the exact high-leverage null-pivot normal form used below. In particular it preserved the original-coordinate product provenance of the residual three-dimensional projection.

### 2.3 Residual-diffuse transverse split

Fleet03/B19 proved

`QFORM-DIFFUSE-2D-TWO-BANK-PARTITION-v1`

in

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260922T203112Z-fleet03-B19-QFORM/REPORT.md`.

For a two-dimensional Parseval frame with every row norm squared at most `1/2`, it produces an original-coordinate partition `J disjoint K` such that both bank frame matrices have determinant and smallest eigenvalue at least `1/640`. The corresponding two-dimensional bank projections are genuinely independent across the two banks and each has joint density cap at most `e sqrt(640)`.

### 2.4 Nested-heavy exit

Fleet02/B10 proved

`QFORM-NULL-ROW-NESTED-HEAVY-CLOSURE-v1`

in

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T193653Z-fleet02-B10-QFORM-r15/REPORT.md`.

Therefore, in the exact-rank-three heavy-null state, any complementary row with transverse leverage greater than `1/2` is already paid by a physical scalar pivot or a uniformly indefinite physical pair. The survivor addressed here indeed has every transverse row norm squared at most `1/2`.

### 2.5 Cross-block receiver

Fleet03/B02 proved

`QFORM-EXACT-RANK3-CROSSBLOCK-FOURIER-v1`

at canonical commit

`yspennstate/math-open-problems@484c89f85cda352b2c4318364a6206ebc4154950`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T230126Z-fleet03-B02-QFORM-r17/REPORT.md`.

If an ORIGINAL-coordinate physical cross block has exact rank three and nonzero singular-value product `Gamma`, then, with arbitrary same-bank quadratic terms, outside couplings and affine terms,

`|phi_Q(t)| <= min(1,(2*pi)^(3/2)Gamma^(-1/2)|t|^(-3/2))`,

`||p_Q||_infinity <=6 Gamma^(-1/3)`.

This is the main quantitative receiver for the positive-innovation branch.

### 2.6 Dependence-safe null-scalar receiver

Fleet01/B11 proved the dependence-safe null-scalar theorem in

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/QFORM-B11-20260922T211147Z/REPORT.md`.

If a scalar `Z` with density cap `L` is genuinely independent of a two-dimensional pair `Y` with joint density cap `M`, and the `3x3` homogeneous quadratic matrix `H` in `(Z,Y)` is invertible with zero `Z^2` coefficient, then

`||p||_infinity <=3*2^(2/3)(LM)^(2/3)|det H|^(-1/3)`.

No independence inside the pair is required. This receiver pays the exact zero-innovation endpoint below.

### 2.7 Designated partner fleet03/B05

The latest compatible designated partner actually present at source refresh is fleet03/B05 r22,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260923T063932Z-fleet03-B05-QFORM-r22/REPORT.md`.

Its theorem `QFORM-RATIOPACKET-SIGMAFREE-PAIRLOG-v1` gives

`||p_Q||_infinity <=8*2^(3/4)*sqrt(5) (mu*kappa*m)^(-1/4)`

for its one-product-packet/two-disjoint-scalar-bank normal form, with no loss in the packet residual parameter `sigma`. Its exact double-zero theorem supplies a second `kappa`-free receiver when the residual coupling ratio is bounded below. Section 9 records the exact branch this closes and the exact independence interface that prevents silently applying it to the new punctured-innovation survivor.

## 3. Exact heavy-null normal form

Let

`A=R M R^T`, `R^T R=I_3`,

be an **exact-rank-three** target form, so every eigenvalue of the real symmetric `3x3` matrix `M` has modulus at least one. Suppose original coordinate `i` has leverage

`c=||r_i||^2>1/2`

and exact physical null pivot

`A_ii=r_i^T M r_i=0`.

Rotate only the deterministic three-dimensional spectral coefficient basis. No random variable is rotated. We may write

`r_i=sqrt(c)e_1`,                                                     (3.1)

and, after a further deterministic rotation in `e_1^perp`,

`M=[[0,b,0],
    [b,alpha,delta],
    [0,delta,gamma]].`                                                (3.2)

Because `sigma_min(M)>=1`,

`|b|=||M e_1||>=1`.                                                   (3.3)

Also direct inversion gives `(M^(-1))_33=1/gamma`; since `||M^(-1)||op<=1`,

`|gamma|>=1`.                                                        (3.4)

For each residual original coordinate `j!=i`, write its spectral row as

`r_j=(u_j,v_j,w_j)`.                                                  (3.5)

Parseval gives

`sum_(j!=i) u_j^2 = rho :=1-c`,
`sum v_j^2=sum w_j^2=1`,
`sum u_jv_j=sum u_jw_j=sum v_jw_j=0`.                                (3.6)

In random-variable notation,

`U=sum u_j X_j`, `V=sum v_j X_j`, `W=sum w_j X_j`,                    (3.7)

and the quadratic form is

`Q=2b(sqrt(c)X_i+U)V + alpha V^2+2delta V W+gamma W^2`.              (3.8)

Here `X_i` is genuinely independent of the entire residual original-coordinate product source. The projected coordinates `(U,V,W)` are generally dependent; no independence is asserted among them.

By the completed nested-heavy theorem, the survivor may be restricted to

`v_j^2+w_j^2<=1/2` for every `j!=i`.                                  (3.9)

Put

`z_j=(v_j,w_j) in R^2`.

Then

`sum z_j z_j^T=I_2`.                                                  (3.10)

## 4. Two transverse product banks and the innovation invariant

Apply `QFORM-DIFFUSE-2D-TWO-BANK-PARTITION-v1` to the frame `(z_j)`. There is a partition of the residual original coordinates into disjoint banks `J,K` such that

`S_G := sum_(j in G) z_j z_j^T`, `G=J,K`,                            (4.1)

satisfies

`S_J+S_K=I_2`,
`det S_G>=1/640`,
`lambda_min(S_G)>=1/640`.                                            (4.2)

For a bank `G`, regard

`u_G=(u_j)_(j in G)`

as a vector in `l^2(G)` and let `Z_G` be the `|G| x2` matrix with columns `v_G,w_G`. Then

`Z_G^T Z_G=S_G`.                                                       (4.3)

Define the regression vector

`h_G:=Z_G^T u_G in R^2`,                                              (4.4)

and the **longitudinal innovation**

`tau_G^2 := ||u_G||_2^2-h_G^T S_G^(-1)h_G.`                          (4.5)

Because `S_G` is positive definite, (4.5) is exactly

`tau_G=dist(u_G,span(v_G,w_G))`.                                      (4.6)

Thus `tau_G=0` if and only if there exist real coefficients `a_G,d_G` such that, coefficientwise on the whole bank,

`u_j=a_G v_j+d_G w_j`, `j in G`.                                     (4.7)

This is the exact variable that measures whether the longitudinal leakage contains a genuinely third physical coefficient direction inside the bank.

### 4.1 Exact bank Gram determinant

Let `R_G` denote the `|G| x3` matrix whose columns are `u_G,v_G,w_G`. Its Gram matrix is

`G_G=R_G^T R_G`
`   =[[||u_G||^2,h_G^T],
`     [h_G,S_G]].`                                                     (4.8)

Schur complement gives the exact identity

`det G_G = det(S_G) tau_G^2.`                                        (4.9)

No estimate has entered yet.

### 4.2 Global overlap identity

From the global orthogonality in (3.6),

`h_J+h_K=0`.                                                          (4.10)

Put `h=h_J=-h_K`. Expanding (4.5) on both banks gives

`rho=tau_J^2+tau_K^2
     +h^T(S_J^(-1)+S_K^(-1))h.`                                      (4.11)

Since `S_K=I-S_J`, the two matrices commute and every eigenvalue of

`S_J^(-1)+S_K^(-1)`

is of the form `1/s+1/(1-s)>=4`. Hence

`4||h||^2 <= rho-tau_J^2-tau_K^2`.                                  (4.12)

Thus in the ultrahigh-leverage regime `rho=1-c ->0`, both the true innovations and the opposing transverse regression correlation become small. This does **not** allow us to delete them as random perturbations: the inputs have no support or moment bound. Equation (4.11) is instead a precise bookkeeping identity for the overlap resource.

## 5. Positive innovations create an exact rank-three physical cross block

Consider the ORIGINAL-coordinate physical cross block

`C=A[J,K]=R_J M R_K^T`.                                               (5.1)

Assume first

`tau_J tau_K>0`.                                                      (5.2)

By (4.9), both `R_J` and `R_K` have full column rank three. Since `M` is invertible, `C` has exact rank three.

Let `Gamma` be the product of its three nonzero singular values. The nonzero squared singular values are the eigenvalues of the `3x3` positive matrix obtained after compressing through the two full-column-rank factors. Taking determinants yields

`Gamma^2
 =det(R_J^T R_J) det(M)^2 det(R_K^T R_K).`                           (5.3)

Using (4.9),

`Gamma
 =|det M| sqrt(det S_J det S_K) tau_J tau_K.`                        (5.4)

For the target normalization,

`|det M|>=1`,
`sqrt(det S_J det S_K)>=1/640`,                                      (5.5)

so

`Gamma >= tau_J tau_K/640.`                                          (5.6)

This is the exact dimension-free geometric inequality supplied by the present run. It does not select one physical triple and it does not take a fiber supremum; it aggregates the entire original-coordinate banks before paying reciprocal volume.

### Theorem 5.1 — `QFORM-NULLROW-TWOBANK-INNOVATION-COLLAR-v1`, positive branch

Under the hypotheses above and `tau_J tau_K>0`,

`||p_Q||_infinity
 <=6 Gamma^(-1/3)
 <=6*640^(1/3)(tau_J tau_K)^(-1/3)
 <51.707 (tau_J tau_K)^(-1/3).`                                      (5.7)

The density is continuous and vanishes at infinity.

#### Proof

Apply `QFORM-EXACT-RANK3-CROSSBLOCK-FOURIER-v1` directly to the physical cut `J|K`, placing `X_i` in the outside bank. Its theorem permits arbitrary same-bank quadratic terms and arbitrary couplings to outside conditioned coordinates. Formula (5.6) then gives (5.7). Its `L^1` characteristic-function proof supplies continuity. QED.

### Corollary 5.2

For every fixed `eta>0`, the entire subbranch

`min(tau_J,tau_K)>=eta`

has

`||p_Q||_infinity <51.707 eta^(-2/3)`.                               (5.8)

Thus the only possible failure of this receiver occurs when at least one bank innovation tends to zero.

## 6. The exact zero-innovation endpoint is uniformly paid

Assume now

`tau_J=0`.                                                           (6.1)

By (4.7), there are real `a,d` such that on bank `J`,

`U_J=a V_J+d W_J`                                                     (6.2)

**as an exact identity of random variables**, because it is already an identity of their original-coordinate coefficient rows.

Condition on every original coordinate in bank `K`. This is genuine product conditioning. All `K`-variables become fixed constants. The remaining random objects are:

- the heavy original scalar `X_i`, density cap one;
- the two-dimensional bank projection `(V_J,W_J)`, independent of `X_i` because bank `J` is disjoint from coordinate `i`.

The normalized pair

`Y_J^*=S_J^(-1/2)(V_J,W_J)^T`

is an orthonormal two-dimensional projection of the original product law on bank `J`, hence has joint density cap at most `e`. Equivalently, the unnormalized pair has cap

`M_J<=e/sqrt(det S_J)<=e sqrt(640)`.                                 (6.3)

After the conditioning, every term involving bank `K` is affine in `(X_i,V_J,W_J)`. The homogeneous conditional quadratic matrix in the unnormalized variables `(X_i,V_J,W_J)` is

`H_J=
 [[0,          b sqrt(c),             0],
  [b sqrt(c), alpha+2ba,       delta+bd],
  [0,         delta+bd,             gamma]].`                        (6.4)

Its determinant is independent of the regression coefficients `a,d`:

`det H_J=-c b^2 gamma.`                                              (6.5)

By (3.3)-(3.4),

`|det H_J|>=c>1/2`.                                                   (6.6)

Apply the dependence-safe null-scalar/dependent-pair theorem with `L=1`, `M=M_J`. It gives

`||p_(Q|X_K)||_infinity
 <=3*2^(2/3) M_J^(2/3) |det H_J|^(-1/3)`
` <=3*2^(2/3)(e sqrt(640))^(2/3)c^(-1/3).`                           (6.7)

Using `c>1/2`,

`||p_(Q|X_K)||_infinity
 <6 e^(2/3) 640^(1/3)
 =100.7103788401... .`                                               (6.8)

The bound is uniform in the conditioned bank `K`, so averaging yields the same bound for `Q` itself.

The argument is symmetric if `tau_K=0`.

### Theorem 6.1 — exact endpoint

If

`min(tau_J,tau_K)=0`,

then

`||p_Q||_infinity<100.711.`                                          (6.9)

Essential boundedness is proved. This null-scalar route does not by itself prove a continuous representative.

### Why this endpoint is genuinely dependence-safe

No conditional density of one projected coordinate given another is used. After conditioning the **other original-coordinate bank**, `X_i` remains genuinely independent of the entire dependent pair `(V_J,W_J)`. The pair is kept intact and paid by its joint projection-density cap. This is exactly the interface permitted by the live `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` correction.

## 7. What the two endpoint theorems leave open

Sections 5 and 6 together give a nonuniform collar plus its exact endpoint:

- `tau_J tau_K>0`: bounded by `51.707(tau_J tau_K)^(-1/3)`;
- `tau_J tau_K=0`: bounded uniformly by `100.711`.

The estimates do not interpolate uniformly as one positive innovation tends to zero. That failure is not cosmetic. A small coefficient vector is not a small random variable under arbitrary unbounded supports, so there is no permitted perturbative step from `tau>0` to `tau=0`.

The first new unpaid implication is therefore exactly

**`QFORM-NULLROW-PUNCTURED-INNOVATION-BRIDGE-v1`:**

> In the setup of Sections 3--4, prove one universal essential density bound in the punctured regime `0<min(tau_J,tau_K)<<1`, retaining the original product coordinates and the dependence of the innovation projection on the transverse pair inside its own bank.

The missing mechanism may be viewed as a product-sensitive stability theorem for the null-scalar curved trace under a same-bank orthogonal linear innovation. It cannot be replaced by an unrestricted trace supremum: the live two-sheet and fiberwise-trace counterexamples rule out exactly that substitution.

Equation (4.11) further says that this punctured state is the only place where the near-coloop limit can hide: when `rho=1-c` is tiny, both innovation norms and the opposing regression correlation are tiny in coefficient geometry, even though none may be discarded probabilistically.

## 8. Required newest-Claude theorem applied at an actual inequality

The required e5f source Theorem F supplies a separate deletion-diffuse exit which is used to narrow the survivor before the innovation bridge.

For the heavy row `r_i`, let

`H_i=I_3-r_i r_i^T`.

Then

`det H_i=1-c`.                                                        (8.1)

For a residual row `r_j`, define the deletion-normalized leverage

`ell_j^(-i)=r_j^T H_i^(-1)r_j`.                                      (8.2)

If every `ell_j^(-i)<=1/2`, apply Theorem F with the heavy coordinate on the conditioned side and the residual original coordinates in the Brascamp--Lieb block. Since the rank-three part is the exact form and the residual quadratic error is zero, the theorem gives

`||p_Q||_infinity
 <=12 [|det M|(1-c)]^(-1/3).`                                       (8.3)

Thus, in the target `|det M|>=1`, whenever

`1-c>=1/128`,

`||p_Q||_infinity
 <=12*128^(1/3)
 =60.4762103949... .`                                                (8.4)

This is an actual application of the newest-Claude result. Consequently a survivor with `1-c>=1/128` must violate the deletion-normalized leverage gate. Since the normalized residual rows form a three-dimensional Parseval frame,

`sum_(j!=i) ell_j^(-i)=3`,                                            (8.5)

so at most five rows can have `ell_j^(-i)>1/2`.

Combining (8.3) with the innovation theorem means the unresolved punctured state can be concentrated still further: either `c>127/128`, or there is a finite set of at most five deletion-normalized-heavy leaves, while every transverse row remains at most `1/2` by the nested-heavy closure.

## 9. Designated partner fleet03/B05 applied and its exact compatibility boundary

The latest fleet03/B05 r22 sigma-free pair-log theorem states, in its ratio-packet normal form,

`||p_Q||_infinity
 <=8*2^(3/4)*sqrt(5)(mu*kappa*m)^(-1/4).`                            (9.1)

The packet extraction used by that line of work gives `m>=3/20`. Therefore the concrete branch

`mu>=1`, `kappa>=1/4`

is paid by

`||p_Q||_infinity
 <=8*2^(3/4)*sqrt(5)((3/20)(1/4))^(-1/4)
 =68.3659210234... .`                                                (9.2)

The partner's exact double-zero theorem supplies a second `kappa`-free exit when its normalized residual coupling `eta_R/|c_pair|` is bounded below.

Those are genuine exits from the current two-sheet proof map. The partner theorem also explains why the new `tau` factor should not automatically be blamed as a geometric curvature loss: in its **compatible** packet geometry, the analogous residual parameter costs nothing.

However, applying (9.1) to the present punctured-innovation bank without further work would be invalid. The partner normal form has two scalar pair variables carried by **genuinely disjoint original-coordinate scalar banks**. Here B19 supplies, on each side, one dependent **two-dimensional** transverse product projection, and the innovation variable lives in that same original bank. Splitting one projected pair by conditioning would invoke the refuted conditional-cap-as-independence interface. Therefore the exact missing bridge is a dependence-safe analogue of the partner's sigma-free mechanism for a scalar plus a dependent pair, not another lower bound on matrix curvature.

This is an exact incompatibility statement, not a reason to weaken the partner theorem.

## 10. Relation to the rough ruled/coarea programme

The rough one-sheet interval theorem proved earlier by this slot avoids evaluating an a.e. density representative on a selected curve: it mollifies first, uses the exact ruling Jacobian, and passes to the original rough law in `L^1`. That half-line is paid.

The present theorem attacks the opposite two-sheet side without replacing curved fibers by unrestricted fiber suprema. The positive-innovation branch converts the unresolved curved geometry into an exact rank-three **physical cross volume** and then uses integrated Fourier/Plancherel on the original product banks. The zero endpoint conditions only a disjoint original bank and invokes a scalar-versus-dependent-pair coarea estimate. Both moves preserve product provenance.

The remaining punctured bridge is therefore a sharply formulated curved/product stability problem, not the already-refuted claim that bounded straight-line X-rays control a two-sheet trace for an arbitrary three-dimensional density.

## 11. Computation and exact checks

`CHECK_RESULTS.txt` records the actual finite algebra checks performed in this invocation.

Exact symbolic calculation returned

`det H_J=-b^2 c gamma`.

A seeded random regression on twenty full-column-rank triples verified

`Gamma=|det M| sqrt(det(R_J^T R_J)det(R_K^T R_K))`

with maximum relative floating-point error `1.54e-15`. This is diagnostic only; equation (5.3) is an exact determinant identity.

The same live calculation recomputed

`6*640^(1/3)=51.7064325607652`,

`6*e^(2/3)*640^(1/3)=100.71037884010028`,

`12*128^(1/3)=60.4762103949539`,

and the partner branch constant in (9.2), `68.36592102339745`.

## 12. Correction boundary and status

The proof above never uses:

- independence after spectral rotation;
- the false arbitrary-joint rank-three coarea inequality;
- an unrestricted curved-fiber or spectral-fiber supremum;
- positive moments of worst conditional projection-density caps;
- conditional density cap as a substitute for independence;
- a uniformly good physical triple;
- or deletion of a small coefficient as a small random error.

No target-valid counterexample was found. The result is a supporting exact-rank-three theorem and a sharper obstruction, not a proof of the unrestricted full-matrix conjecture.

**First next mathematical step:** prove `QFORM-NULLROW-PUNCTURED-INNOVATION-BRIDGE-v1`, preferably by a product-sensitive coarea or mixed-Fresnel estimate that is uniform as a same-bank innovation coefficient tends to zero and reduces continuously to the dependence-safe null-scalar theorem at the endpoint. A valid argument must retain the whole bank rather than condition on one coordinate of its dependent transverse projection.
