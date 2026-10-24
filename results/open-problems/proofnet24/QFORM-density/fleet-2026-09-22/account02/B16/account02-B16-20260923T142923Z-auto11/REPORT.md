SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-23T14:29:23Z.
attacking: the superdiffuse-bank same-side-curvature debt by replacing two physical hubs with one genuinely dependent two-dimensional product projection, and paying a rank-two cross block before any projected-independence or conditional-cap step.

# account02/B16 — projected two-hub / rank-two diagonal-side compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SUPPORTING THEOREM / PINNED RESULT APPLIED / PARTNER r29 SHARPENED / FULL QFORM OPEN`  
**Regularity:** continuity is proved on Theorem A below; the sharper null-side Theorem B proves essential boundedness, with continuity not claimed there.

## 1. First unpaid implication

The latest compatible designated partner actually used here is account03/B16 r29,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T132339Z-account03-B16-QFORM-r29/REPORT.md`.

After its paid physical-diagonal and physical-pair exits, the exact-rank-three near-coloop survivor has hub leverage `c>63/64`, all normalized hub-star atoms `<1/251`, and at least 80 disjoint original-coordinate source banks whose normalized star aggregates have scalar density cap `sqrt(2)`. Its explicit unpaid implication is to retain the same-side curvature jointly with those banks, without conditioning to a worst projected slice.

This run pays a clean rank-two cut whenever the bank on the curved side is diagonal in ORIGINAL coordinates. It also proves that the still easier null-side version cannot be the missing exact-rank-three endpoint: a null side with rank-two cross interaction already forces matrix rank at least four. Thus genuine same-side curvature in the partner survivor is algebraically necessary, not merely an artifact of the current proof.

## 2. Pinned source used at an equation

Required source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

Two completed facts are used, in their exact product-law scope.

1. Every two-dimensional orthonormal projection `Z=U^T X` of independent cap-one coordinates has joint density

`||p_Z||_infinity <= 2`.

This is the two-dimensional marginal input used in the pinned ruled theorem. It does **not** make the two coordinates of `Z` independent.

2. For `g` with `|g|<=f<=1`, the pinned Lemma 1 gives

`integral |g_hat|^p <= 4 pi / sqrt(p)`, `p>=2`.

In particular the same bound holds for the quadratic twists `g_j(x)=exp(i t d_j x^2)f_j(x)`. Combined with geometric Brascamp-Lieb, this pays a diagonal leaf bank after the dependent projected pair has been integrated as one joint object.

The pinned volume theorem D is also checked on the stress family below: its three-volume is exactly zero, so it supplies no certificate there. That is a real obstruction to a rank-three-volume-only route, not a contradiction to theorem D.

## 3. Theorem A: a dependent projected pair may replace two physical hubs

### `QFORM-PROJECTED-2HUB-RANK2-DIAGONAL-SIDE-v1`

Let the original coordinates be partitioned as `I union J union K`. Condition on `X_K`. Assume:

* `A_JJ=D` is diagonal in the original `J` coordinates;
* the physical cross block `M=A_IJ` has **exact rank two**, with singular values `s_1>=s_2>0`;
* if `M=U Sigma V^T`, `Sigma=diag(s_1,s_2)`, then every row of the right singular frame satisfies

`||V_{j,*}||_2^2 <= 1/2`, `j in J`.

No restriction is placed on `A_II`, on the conditioned blocks involving `K`, or on affine terms. Then the full quadratic polynomial has a continuous density and

`boxed: ||p_Q||_infinity <= 4 sqrt(2) (s_1 s_2)^(-1/2).`          (3.1)

The two coordinates of `U^T X_I` may be arbitrarily dependent.

### Proof

After conditioning `X_K=x_K`, absorb every term not involving `X_J` into an arbitrary real function `R(X_I)`, and every fixed linear `J` term into `b in R^J`. Thus

`Q=R(X_I)+sum_(j in J) d_j X_j^2 + 2 X_I^T M X_J + b^T X_J`.       (3.2)

Put

`Z=U^T X_I in R^2`.

The `I` and `J` source banks are genuinely independent, while the two coordinates of `Z` are not asserted independent. By the completed two-dimensional product-marginal theorem,

`p_Z(z)<=2` a.e.                                                       (3.3)

Disintegrate the `I` bank over `Z`. For each `t`, the conditional factor coming from `R(X_I)` has modulus at most one, so

`|phi_Q(t)| <= 2 integral_(R^2) |Phi_J(t,z)| dz`,                    (3.4)

where

`Phi_J(t,z)=prod_(j in J) ghat_j( 2t <V_{j,*},Sigma z> + t b_j )`,
`g_j(x)=exp(i t d_j x^2) f_j(x)`.                                  (3.5)

For `t!=0`, substitute `y=2tz`. Let

`rho_j=Sigma V_{j,*}^T in R^2`,
`G=sum_j rho_j rho_j^T=Sigma^2`,
`c_j=rho_j^T G^(-1) rho_j=||V_{j,*}||_2^2`.                         (3.6)

Then `sum c_j=2` and every `c_j<=1/2`. The geometric Brascamp-Lieb inequality, with its translation invariance in every one-dimensional argument, and the pinned twisted `L^p` lemma give

`integral_(R^2) prod_j |ghat_j(<rho_j,y>+t b_j)| dy
 <= det(G)^(-1/2) prod_j [c_j^(-1/2) integral |ghat_j|^(1/c_j)]^(c_j)
 <= (4 pi)^2 (s_1 s_2)^(-1)`.                                     (3.7)

The case `c_j=0` is dropped, since its factor is at most one. Combining (3.4)-(3.7),

`|phi_Q(t)| <= 8 pi^2 (s_1 s_2)^(-1) |t|^(-2)`.                    (3.8)

Together with `|phi_Q|<=1`, if

`B=8 pi^2/(s_1 s_2)`,

then

`integral_R min(1,B/t^2) dt = 4 sqrt(B)`.                           (3.9)

Fourier inversion therefore yields

`||p_Q||_infinity <= (2 pi)^(-1) 4 sqrt(B)
 =4 sqrt(2) (s_1 s_2)^(-1/2)`.                                    (3.10)

The majorant in (3.8) is integrable, so the conditional density is continuous. The bound is uniform in the conditioned value `x_K`; averaging the conditional continuous densities and using dominated convergence gives a continuous density for the full `Q`. QED.

### What was and was not used

The product theorem was used only as the joint cap (3.3). No independence of the two projected coordinates, no conditional density cap for one projected coordinate given the other, and no post-rotation product structure were used. The `J`-side factorisation occurs only because `D=A_JJ` is diagonal in ORIGINAL coordinates.

## 4. Theorem B: null-side sharpening with no right-leverage gate

When `A_JJ=0`, the diagonal-twist Fourier step can be replaced by direct source conditioning, removing the right-singular leverage assumption and improving the constant.

### `QFORM-NULL-SIDE-CROSS2-PROJECTION-v1`

Let `I,J,K` be disjoint original-coordinate sets, condition on `K`, and suppose `A_JJ=0`. If `M=A_IJ` has at least two nonzero singular values `s_1>=s_2>0`, then, with all other blocks and affine terms arbitrary,

`boxed: ||p_Q||_infinity <= 2 sqrt(pi) (s_1 s_2)^(-1/2).`           (4.1)

Essential boundedness is asserted; this proof does not claim continuity.

### Proof

Condition further on `X_I=x`. As a function of the independent original `J` coordinates, `Q` is affine with coefficient

`ell(x)=2 M^T x+d`,                                                 (4.2)

where `d` contains all terms fixed by the conditioning. The one-dimensional bounded-density projection theorem gives the conditional density cap

`sqrt(2)/||ell(x)||_2`.                                             (4.3)

Let `u_1,u_2` and `v_1,v_2` be the first two left/right singular vectors of `M`, and put

`Z=(<u_1,X_I>,<u_2,X_I>)`, `Sigma_2=diag(s_1,s_2)`.

Projecting (4.2) onto `span(v_1,v_2)` gives, for a fixed translation `z_0`,

`||ell(X_I)||_2 >= 2 ||Sigma_2 (Z-z_0)||_2`.                        (4.4)

Again `p_Z<=2`; hence `Y=Sigma_2(Z-z_0)` has density cap

`||p_Y||_infinity <= 2/(s_1 s_2)`.                                 (4.5)

For any planar probability density bounded by `M_0`, layer cake gives the exact elementary estimate

`E |Y|^(-1)
 = integral_0^infinity P(|Y|<1/u) du
 <= integral_0^infinity min(1, pi M_0/u^2) du
 =2 sqrt(pi M_0)`.                                                  (4.6)

Using `M_0=2/(s_1s_2)` in (4.3)-(4.6) gives

`E[sqrt(2)/||ell||]
 <= (1/sqrt(2)) E |Y|^(-1)
 <=2 sqrt(pi)(s_1s_2)^(-1/2)`.                                     (4.7)

Averaging the conditional interval estimates proves (4.1). QED.

This is the precise curved-integral interface sought by B16: the singular kernel is `1/|y|`, which is locally integrable in two dimensions. A bounded two-dimensional projection density is sufficient **here** because it is inserted against that integrable kernel; it would not be sufficient against an arbitrary indefinite quadratic trace.

## 5. Target-valid diffuse stress family: aggregation beats every physical pair

Let `m>=4` be even. Choose balanced signs `eps_i,tau_j in {+1,-1}` and define `m x 2` matrices

`C_i=(1,eps_i)/sqrt(m)`, `D_j=(1,tau_j)/sqrt(m)`.

Then

`C^T C=D^T D=I_2`.                                                  (5.1)

For two disjoint original-coordinate banks `X in R^m`, `Y in R^m`, set

`A_m = [[0, C D^T], [D C^T, 0]]`.                                  (5.2)

Its nonzero spectrum is exactly

`boxed: {1,1,-1,-1}`.                                               (5.3)

Thus it is a strict instance of the user's full `>=3`-large-eigenvalue target. Writing

`Z=C^T X`, `W=D^T Y`,

we have

`Q=2 Z^T W`.                                                        (5.4)

The coordinates inside `Z` and inside `W` need not be independent. The two vectors `Z` and `W` are genuinely independent because they use disjoint original source banks.

Theorem B sees `s_1=s_2=1` and gives the dimension-free all-law bound

`boxed: ||p_Q||_infinity <= 2 sqrt(pi)=3.5449077018...`.            (5.5)

Theorem A independently gives `4sqrt(2)` and remains valid if an arbitrary original-coordinate diagonal quadratic twist is added on the `Y` bank.

In physical coordinates every diagonal is zero and

`(C D^T)_{ij}=(1+eps_i tau_j)/m in {0,2/m}`.                        (5.6)

Hence every physical `2x2` principal determinant has magnitude at most `4/m^2`. On a nonzero physical pair the completed pair-log certificate from the current proof map is only

`8 sqrt(5) [(4/m^2)(2/m)]^(-1/4)
 = (8 sqrt(5)/8^(1/4)) m^(3/4)
 =10.63659179... m^(3/4)`,                                         (5.7)

which diverges, while (5.5) is constant. This is a genuine **aggregation-before-reciprocal-payment obstruction**.

The required pinned theorem D also has

`e_3((C D^T)^T(C D^T))=0`                                         (5.8)

because the cross block has rank two; its `D_5` extension is likewise zero. Thus the family is invisible to every three/five-volume cross certificate in the pinned source but is paid by the product-projection curved integral above. This does not refute those theorems; it identifies a complementary rank-two aggregate mechanism.

## 6. Application to account03/B16 r29

The partner r29 survivor is exact rank three. Theorem B cannot be the missing endpoint for a structural reason.

If a symmetric principal block has the form

`[[P,M],[M^T,0]]`                                                   (6.1)

and `rank M=r`, choose an invertible physical `r x r` minor `M_0`. The corresponding `2r x 2r` principal submatrix has determinant

`det [[P_0,M_0],[M_0^T,0]] = (-1)^r det(M_0)^2 !=0`.                (6.2)

Therefore

`rank [[P,M],[M^T,0]] >=2r`.                                       (6.3)

For an exact-rank-three matrix, a null original-coordinate bank can consequently have cross rank at most one. So the partner's same-side-curvature debt is **algebraically unavoidable** as soon as two cross directions are needed.

Theorem A nevertheless removes a genuine subbranch of the r29 debt. For any union `J` of its original-coordinate banks for which

1. `A_JJ` is diagonal in those original coordinates,
2. `rank A_IJ=2`,
3. `s_1(A_IJ)s_2(A_IJ)>=kappa>0`, and
4. the right singular two-plane has row leverage at most `1/2`,

we obtain immediately

`boxed: ||p_Q||_infinity <=4 sqrt(2) kappa^(-1/2).`                 (6.4)

Thus the true exact-rank-three B16 survivor can be narrowed further: every useful diffuse rank-two cut must fail at least one of (i) diagonal same-side curvature, (ii) quantitative second cross singular value, or (iii) right-side two-plane diffuseness. In particular, a proof can no longer treat “same-bank dependence” alone as the obstruction; after this theorem the unpaid phenomenon is specifically **non-diagonal same-side curvature or a quantitative rank/leverage collapse on every useful bank cut**.

## 7. Remaining implication

The next unpaid B16 implication is

**`QFORM-SUPERDIFFUSE-BANK-DIAGONALIZE-OR-PAY-CURVATURE-v1`.**

Starting from the partner r29 eighty-bank survivor, either:

* extract a union of original-coordinate banks satisfying the four hypotheses of (6.4), or
* use the non-diagonal same-side curvature that prevents such a cut as a new source-preserving Fresnel resource.

The latter step must retain each bank's original product factors until the curvature is paid; it may not condition on a projected coordinate, infer projected independence, or delete a small coefficient on unbounded inputs.

Arbitrary additional spectrum is partly covered by Theorems A/B because their proofs allow arbitrary `A_II` and arbitrary conditioned outside blocks, but no claim is made that every full target matrix contains such a cut. The unrestricted QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED.
