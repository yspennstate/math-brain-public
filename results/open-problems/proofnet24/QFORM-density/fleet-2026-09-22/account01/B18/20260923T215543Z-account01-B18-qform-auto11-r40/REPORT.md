SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-23T21:55:43Z.
attacking: literature-to-proof transfer plus an asymmetric original-coordinate cut that enlarges the exact-rank-three diffuse branch, followed by a literal application of the completed account02/B18 private-bank theorem.

# account01/B18 r40 — asymmetric 3-volume cut through leverage 3/16

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: account01/B18 — Literature-to-proof transfer  
Outcome: **NEW SUPPORTING TARGET-LEVEL THEOREM + COMPLETED PARTNER INEQUALITY / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: proved on the new diffuse principal-core branch and on the partner private-bank subbranch below; full-target continuity remains open.


## 1. Sources used at literal hypotheses

### 1.1 Primary bounded-product marginal theorem

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), Theorem 1.1, arXiv:1507.07949, proves for a genuine product probability density

`f(x)=prod_i f_i(x_i)`, `||f_i||_1=1`,

that every `k`-dimensional orthogonal marginal has density bounded by

`2^(k/2) prod_i ||f_i||_infinity^(gamma_i)`

for suitable `gamma_i in [0,1]`, `sum gamma_i=k`. Therefore in the present cap-one class,

`||p_(P_E X)||_infinity <=2^(k/2)`.                                  (1.1)

In particular, for every nonzero coefficient vector `g`, whitening the one-dimensional image gives

`boxed: ||p_(g dot X)||_infinity <=sqrt(2)/||g||_2.`                 (1.2)

No iid, moment, support, log-concavity, centering, symmetry, or smoothness assumption is introduced. Equation (1.1) is a density statement for a projected random vector; it is not an independence statement for its coordinates.

### 1.2 Internal Fourier receiver, source pinned

The reviewed owner-pinned Fourier report

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`

proves Theorem D'. For a literal ORIGINAL-coordinate cut `I sqcup J` and cross block `M=A[I,J]`, write

`Z=e_3(M^T M)=sum_{|R|=|C|=3} det(M[R,C])^2`,                       (1.3)

and let `alpha_i` be the I-side row marginal of the natural probability law proportional to `det(M[R,C])^2`. If

`max_i alpha_i <= h <3/4`,                                          (1.4)

then, uniformly in all same-side quadratic blocks, all affine terms, and all conditioned outside coordinates,

`boxed:
 ||p_Q||_infinity
 <=6 sqrt(e) (2h)^(-1/2)(3-4h)^(-1) Z^(-1/6).`                     (1.5)

The proof gives an integrable characteristic-function envelope, hence a continuous `C_0` density.

### 1.3 Designated completed partner, source pinned

The completed account02/B18 report is pinned at

`math-open-problems@5bb8c5faaf65393ba42f440dce575d8ffdaf1f52`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T203819Z-account02-B18-QFORM-auto11/REPORT.md`.

Its theorem `QFORM-NULLHUB-DIFFUSE-PRIVATE-BANK-v1` treats

`Q=2(X_0+ell dot X_L)(g dot X_L)+d(beta dot X_L)^2`,                (1.6)

with a literal source split `L=J sqcup K`, `g_K=0`, private-square mass `rho=||beta_K||>0`, and private nonaligned twist `eta>0`. If the normalized private two-frame is coordinatewise diffuse,

`b_k^2+v_k^2<=1/2`,                                                 (1.7)

then with `G=g_J dot X_J`, `M_G=||p_G||_infinity`,

`||p_Q||_infinity
 <=3*2^(4/3) M_G^(2/3)(rho^2 eta^2 |d|)^(-1/3)`.                  (1.8)

It proves a continuous `C_0` density. This theorem keeps the actual product source bank and never declares the two projected private coordinates independent.

## 2. New deterministic-probabilistic compiler

### Theorem 2.1 — `QFORM-ASYMMETRIC-CUT-3OVER16-v1`

Let `B` be a real symmetric ORIGINAL-coordinate principal block of exact rank three,

`B=U Lambda U^T`, `U^T U=I_3`,                                     (2.1)

and assume its three nonzero eigenvalues satisfy

`|lambda_j|>=s>0`.                                                   (2.2)

Write the physical rows of `U` as `u_i^T` and their range leverage as

`c_i=||u_i||_2^2`, `kappa=max_i c_i`.                              (2.3)

If

`boxed: kappa<=3/16,`                                               (2.4)

then for arbitrary independent cap-one coordinate densities and arbitrary affine perturbations, the quadratic polynomial with quadratic matrix `B` has a continuous `C_0` density satisfying

`boxed:
 ||p_Q||_infinity
 <= [32(20-3sqrt(15))sqrt(e)]/[9(4-sqrt(15))^(3/2)] * s^(-1)
 <1086/s.`                                                          (2.5)

The same bound holds for a full ambient quadratic form after conditioning all original coordinates outside this principal block.

This improves the clean random-cut leverage threshold obtainable from a symmetric half-cut. The improvement is not from a probabilistic rotation: the cut is always a cut of ORIGINAL coordinates.

### Proof

Set

`p=5/8`.                                                            (2.6)

Independently select every original row into `I` with probability `p`, and put `J=I^c`. Define

`G_I=sum_{i in I} u_i u_i^T`.                                      (2.7)

Since `sum_i u_i u_i^T=I_3`,

`E G_I=p I_3`.                                                      (2.8)

The centered rank-one summands are independent, so

`E ||G_I-pI_3||_F^2
 =p(1-p) sum_i ||u_i u_i^T||_F^2
 =p(1-p) sum_i c_i^2
 <=3p(1-p)kappa.`                                                   (2.9)

Under (2.4),

`3p(1-p)kappa
 <=3*(5/8)*(3/8)*(3/16)
 =135/1024`.                                                        (2.10)

Hence some deterministic original-coordinate cut satisfies

`||G_I-pI_3||_op
 <=||G_I-pI_3||_F
 <=epsilon:=3sqrt(15)/32`.                                         (2.11)

Put

`a_0=p-epsilon=(20-3sqrt(15))/32`,
`b_0=1-p-epsilon=(12-3sqrt(15))/32`.                               (2.12)

Both are positive. Therefore

`G_I>=a_0 I_3`, `G_J:=I_3-G_I>=b_0 I_3`.                           (2.13)

In particular both sides see all three spectral directions.

Now use the literal physical cross block

`M=B[I,J]=U_I Lambda U_J^T`.                                       (2.14)

By Cauchy--Binet, because the rank is exactly three,

`Z=e_3(M^T M)
 =det(Lambda)^2 det(G_I)det(G_J)
 >=s^6(a_0 b_0)^3.`                                                (2.15)

The same factorization gives the natural squared-minor I-row marginal

`alpha_i=u_i^T G_I^(-1)u_i`.                                      (2.16)

Thus

`alpha_i<=c_i/a_0<=h_0`,                                           (2.17)

where

`h_0=(3/16)/a_0=6/(20-3sqrt(15))
 =0.715900755591447...<3/4`.                                       (2.18)

The strict inequality is equivalent to `sqrt(15)<4`.

Apply Theorem D' with `h=h_0` and (2.15):

`||p_Q||_infinity
 <=6sqrt(e)(2h_0)^(-1/2)(3-4h_0)^(-1)
    s^(-1)(a_0b_0)^(-1/2).`                                       (2.19)

Exact simplification yields

`6sqrt(e)(2h_0)^(-1/2)(3-4h_0)^(-1)(a_0b_0)^(-1/2)
 =32(20-3sqrt(15))sqrt(e)/[9(4-sqrt(15))^(3/2)]
 =1085.3308269959426...<1086.`                                     (2.20)

This proves (2.5). The exact identities and inequalities in (2.10)--(2.20) are regression-checked in this run's `VERIFY.py`.

### Ambient lift and continuity

Let the full symmetric ambient matrix be `A`, and suppose `B=A[S,S]` is a principal block meeting Theorem 2.1. Condition on all original coordinates `X_{S^c}=y`. The retained variables remain independent with the same cap-one densities, while

`Q_y(X_S)=X_S^T B X_S+b(y)^T X_S+c(y)`.                             (2.21)

The D' estimate is uniform in `b(y),c(y)`. More strongly, the proof supplies an integrable envelope `F(t)` independent of `y` such that the conditional characteristic functions obey

`|phi_y(t)|<=F(t)`, `F in L^1(R)`.                                 (2.22)

Averaging gives `|phi_Q(t)|<=F(t)`. Hence Fourier inversion gives a continuous `C_0` density for the full ambient output and the same bound (2.5). No extra spectrum or outside coupling was deleted.

## 3. How far the asymmetric second-moment method can go

The choice `p=5/8` was made to give a clean rational leverage statement. The same argument can be optimized.

For a target leverage `kappa`, define

`epsilon(p,kappa)=sqrt(3p(1-p)kappa)`.                              (3.1)

The two requirements are

`1-p-epsilon>0`                                                     (3.2)

so that the complementary side has three-dimensional volume, and

`kappa/(p-epsilon)<3/4`                                             (3.3)

so that D' is integrable. At the limiting simultaneous equality one has

`p=1/(1+3kappa)`                                                    (3.4)

and

`12kappa^2+13kappa-3=0`.                                           (3.5)

Thus the method's open limiting threshold is

`kappa_*=(sqrt(313)-13)/24
 =0.195491917206422...`.                                            (3.6)

For every fixed `kappa<kappa_*`, a nearby admissible `p` gives a finite continuous bound depending only on that fixed leverage threshold and `s`. I do not use the endpoint itself because D' requires a strict `h<3/4` and the complementary Gram lower bound must stay positive. The clean theorem (2.5) stays safely inside this limit at `3/16=0.1875`.

## 4. Required application of the completed account02/B18 result

Apply the primary LPP theorem (1.2) literally to the complementary original-coordinate projection in account02/B18's completed private-bank theorem:

`G=g_J dot X_J`, `gamma=||g||_2=||g_J||_2`.                        (4.1)

Because `X_J` is a genuine subvector of the original product input,

`M_G=||p_G||_infinity<=sqrt(2)/gamma`.                              (4.2)

Substitution into (1.8) gives exactly the partner's source-valid corollary

`boxed:
 ||p_Q||_infinity
 <=3*2^(5/3)
   [|d| gamma^2 rho^2 eta^2]^(-1/3).`                              (4.3)

Now spend this at a concrete threshold. If

`|d| gamma^2>=1`, `rho eta>=1/4`,                                  (4.4)

then

`|d|gamma^2 rho^2 eta^2>=1/16`.                                   (4.5)

Therefore

`||p_Q||_infinity
 <=3*2^(5/3)*16^(1/3)
 =boxed: 24.`                                                       (4.6)

The completed partner theorem supplies a continuous `C_0` density on this subbranch. This is an actual target-level inequality, not a citation-only handoff.

For the partner's literal target family

`Q_(m,eta)=2(X_0+eta V)G+B^2`                                      (4.7)

with the diffuse private two-frame, one has `d=gamma=rho=1` and physical nonzero spectrum

`{-sqrt(1+eta^2),1,+sqrt(1+eta^2)}`.                               (4.8)

Thus every `eta>=1/4` satisfies the owner spectral hypothesis and (4.6) gives the whole-line continuous bound

`boxed: ||p_(Q_(m,eta))||_infinity<=24}`                            (4.9)

uniformly in the number of private coordinates and in every allowed cap-one product law. This does not claim novelty for the family or for the partner theorem; it is the requested source-to-proof transfer at an explicit inequality.

## 5. Primary quadratic/bilinear literature audit

I also checked two primary/near-primary quadratic-form regularity routes for an exact prior solution.

1. Banks--Garza-Vargas--Kulkarni--Srivastava, *Overlaps, Eigenvalue Gaps, and Pseudospectrum under real Ginibre and Absolutely Continuous Perturbations*, arXiv:2005.08930, Section 2, proves density estimates for bilinear/quadratic maps made from two genuinely independent bounded-entry-density banks. Its `k=1` Corollary 2.4 controls a scalar form of the type `X^T ZY+X^T U+V^T Y+W` through singular values of `Z`. This is a real overlap with the fleet's pure two-bank bilinear branch, so no novelty claim should be made there. It does **not** cover an arbitrary same-bank quadratic term `H(X)` or the full arbitrary symmetric QFORM target, so it cannot be substituted for the present whole theorem.

2. Herry--Malicet--Poly, *Regularity of laws via Dirichlet forms -- Application to quadratic forms in independent and identically distributed random variables*, arXiv:2303.09488, works with iid inputs whose one-dimensional law is a sufficiently smooth function of a Gaussian field and imposes further normalization/spectral hypotheses for its principal applications. Those hypotheses do not match arbitrary non-iid cap-one rough densities.

I found no exact prior theorem in this targeted audit matching all owner quantifiers. This is only a hypothesis-scope statement, not a novelty claim.

## 6. Correction-safe interpretation and remaining debt

The new theorem genuinely enlarges a clean exact-rank-three diffuse principal-core branch from the usual symmetric-cut scale to `kappa<=3/16`, close to the intrinsic `kappa_*≈0.195492` ceiling of this simple asymmetric second-moment + D' mechanism. It does not solve the global structural problem: the owner spectral hypothesis alone still does not force an exact-rank-three principal block with row leverage at most `3/16` and unit-scale nonzero eigenvalues.

The completed account02/B18 private-bank theorem, after the primary LPP transfer, pays the explicit currency region

`|d|gamma^2>=1`, `rho eta>=1/4`                                    (6.1)

by the continuous universal constant `24`. Its live debt remains the private-bank heavy/near-aligned regime in which the normalized private two-frame is not diffuse or `rho eta` is small, together with the separate global descent problem from an arbitrary ambient `A` with extra spectrum.

No step in this report uses post-rotation independence, arbitrary-joint three-dimensional coarea, conditional density cap as independence, deletion of a small nonzero edge or quadratic remainder, a law-uniform pointwise Fresnel estimate, a worst-fiber bound, or a claim that aggregate determinant mass yields one universally good predetermined physical minor.

### Status

- full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**;
- new theorem: `QFORM-ASYMMETRIC-CUT-3OVER16-v1`, continuous bound `<1086/s` for any exact-rank-three principal core with max range leverage at most `3/16`;
- method ceiling: every fixed `kappa<(sqrt(313)-13)/24` is in principle payable by the same asymmetric second-moment + D' construction, with constants deteriorating at the endpoint;
- designated partner application: source-valid continuous bound `<=24` under (4.4), including the target-valid family (4.7) for `eta>=1/4`;
- full-target continuity: **OPEN**.

First useful next edge: prove a structural routing theorem that sends every remaining exact-rank-three heavy state (`kappa>3/16`) into one of the already-paid physical-pivot/private-bank/grouped-cross packets, while keeping all extra ambient spectrum; or find a stronger product-coordinate paving/volume argument that crosses the `kappa_*` barrier without violating the D' marginal gate.
