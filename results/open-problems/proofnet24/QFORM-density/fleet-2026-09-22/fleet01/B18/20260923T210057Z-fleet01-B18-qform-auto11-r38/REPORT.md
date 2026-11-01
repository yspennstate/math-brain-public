SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B18, 2026-09-23T21:00:57Z.
attacking: physical-block transfer of the completed fleet02/B18 diffuse-private-bank theorem, then a finite-ray extension of the low-hub equal-spectrum source-bank closure.

# fleet01/B18 — physical private-bank currency and finite-ray low-hub closure

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Run: `20260923T210057Z-fleet01-B18-qform-auto11-r38`.  
Status: **PROVED SUPPORTING TARGET-LEVEL IMPLICATIONS / DESIGNATED PARTNER APPLIED; FULL QFORM OPEN**.  
Continuity: proved only for Theorem A below; not claimed for Theorem B.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-pinned completed partner results consumed

The newest completed designated partner result is fleet02/B18
`QFORM-NULLHUB-DIFFUSE-PRIVATE-BANK-v1`, canonical source

- `yspennstate/math-open-problems@529be48498963ede3243fd4a2b00a0104442fc05`;
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/20260923T203819Z-fleet02-B18-QFORM-auto11/REPORT.md`.

In the exact null-hub normal form

`Q = 2 (X_0 + ell.X_L)(g.X_L) + d (beta.X_L)^2`,                    (1.1)

with `||beta||=1`, `beta.g=0`, `gamma=||g||>0`, `d!=0`, suppose
`L=J disjoint_union K`, `g_K=0`, `rho=||beta_K||>0`, and

`ell_K = a beta_K + r`, `r perp beta_K`, `eta=||r||>0`.             (1.2)

Put `b=beta_K/rho`, `v=r/eta`.  If

`b_k^2+v_k^2 <= 1/2` for every `k in K`,                            (1.3)

then, writing `G=g_J.X_J` and `M_G=||p_G||_infinity`, the completed partner theorem gives a continuous `C_0` density and

`||p_Q||_infinity
 <= 3*2^(4/3) M_G^(2/3) (rho^2 eta^2 |d|)^(-1/3).`                 (1.4)

Its source-valid Livshyts--Paouris--Pivovarov specialization gives

`||p_Q||_infinity
 <= 3*2^(5/3) [|d| gamma^2 rho^2 eta^2]^(-1/3).`                   (1.5)

I also use the earlier completed fleet02/B18 receiver
`QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`, canonical source

- `yspennstate/math-open-problems@ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`;
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/20260923T013147Z-bf13c29b/REPORT.md`.

If a scalar of density cap `K_0` is genuinely independent of a possibly dependent pair of joint density cap `M`, and the retained symmetric three-variable quadratic matrix has zero scalar pivot and determinant `Delta!=0`, then

`||p_Q||_infinity <= 3(2 M K_0)^(2/3)|Delta|^(-1/3).`               (1.6)

The pair coordinates are not required to be independent.

Finally, the low-hub equal-spectrum geometry is the completed fleet02/B18 source

- `yspennstate/math-open-problems@c99a85972a70c210b19dd41128300ad55a9b8cb4`;
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/b18-20260923T191130Z-20b2aab6/REPORT.md`.

It gives an exact target family with nonzero spectrum `{-1,1,1}` and the low-hub distinguished row used in Theorem B.

## 2. Primary literature hypothesis audit

The external theorem actually used is G. Livshyts, G. Paouris and P. Pivovarov,
*On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), Theorem 1.1, arXiv:1507.07949.  Its hypothesis is a genuine product probability density `prod_i f_i` with one-dimensional caps `||f_i||_infinity<=1`; every `k`-dimensional orthogonal marginal has density cap at most `2^(k/2)`.  No moment, iid, support, log-concavity, centering, symmetry or smoothness hypothesis is present.  In particular

`||p_(a.X)||_infinity <= sqrt(2)/||a||_2`                           (2.1)

for every nonzero deterministic coefficient vector `a`, and every two-dimensional orthogonal product projection has joint density cap at most `2`.

I use (2.1) only on genuine original-coordinate product blocks.  It is never interpreted as independence after rotation.

For comparison, Juškevičius--Lee's sharp Rogozin/rearrangement theorem controls sums of genuinely independent bounded-density random vectors, but it does not turn the dependent spectral coordinates of a rotated quadratic form into independent variables.  Herry--Malicet--Poly's quadratic-form regularity theorem assumes iid inputs representable as sufficiently smooth functions of a Gaussian field.  The 2026 Choudhary--Kuchibhotla concentration theorem treats Gaussian quadratic forms.  None of those hypotheses equals the owner's arbitrary non-iid rough cap-one class.  I found no exact published theorem in this targeted audit that closes all owner quantifiers; this is a hypothesis comparison, not a novelty claim.

## 3. Theorem A — physical-block form of the latest partner currency

### `QFORM-NULLHUB-PRIVATE-BANK-PHYSICAL-v1`

Assume the completed exact null-hub normal form (1.1).  Let `L=J disjoint_union K` be a literal ORIGINAL-coordinate split satisfying

`A_(0,K)=0`.                                                        (3.1)

Since the physical hub row in (1.1) is `g`, (3.1) is exactly `g_K=0`.
Assume the private square block is nonzero.  Let

`T_K := A_(K,K)`,                                                    (3.2)

let `tau` be its unique nonzero eigenvalue, and let `b` be a corresponding unit eigenvector.  Put

`P = I_K - b b^T`,
`C = A_(J,K) P`.                                                     (3.3)

Assume `C!=0`.  In this null-hub normal form `C` has rank one; let

`sigma = ||C||_HS = ||C||_op`,                                     (3.4)

and let `v` be a unit right singular vector of `C`.  If the physical two-plane `span{b,v}` is coordinate-diffuse,

`b_k^2+v_k^2 <= 1/2` for every `k in K`,                            (3.5)

then `Q` has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= 3*2^(5/3) (|tau| sigma^2)^(-1/3).`                             (3.6)

More precisely, with `gamma=||A_(0,J)||_2` and
`M_G=||p_(A_(0,J).X_J)||_infinity`,

`boxed:
 ||p_Q||_infinity
 <= 3*2^(4/3) (gamma M_G)^(2/3)
    (|tau| sigma^2)^(-1/3).`                                       (3.7)

LPP gives `gamma M_G<=sqrt(2)`, reducing (3.7) to (3.6).

### Proof

Because `g_K=0`, the physical blocks of the matrix in (1.1) are

`A_(K,K) = d beta_K beta_K^T`,                                     (3.8)

`A_(J,K) = g_J ell_K^T + d beta_J beta_K^T`.                       (3.9)

Write `rho=||beta_K||>0`.  Up to sign,

`b=beta_K/rho`, `tau=d rho^2`.                                     (3.10)

Let

`r=P ell_K`, `eta=||r||>0`.                                        (3.11)

Since `beta_K^T P=0`, (3.9) gives the exact physical identity

`C=A_(J,K)P = g_J r^T`.                                             (3.12)

Thus its only singular value is

`sigma=||g_J|| eta=gamma eta`,                                     (3.13)

and its right singular direction is `v=r/eta`.  Therefore the partner's analytic currency is exactly

`|d| gamma^2 rho^2 eta^2
 = |tau| sigma^2`.                                                   (3.14)

The physical leverage gate (3.5) is exactly the partner gate (1.3).  Substituting

`rho^2 eta^2 |d| = |tau| sigma^2/gamma^2`                           (3.15)

into the completed partner estimate (1.4) proves (3.7).  The primary LPP theorem gives
`M_G<=sqrt(2)/gamma`, so (3.6) follows.  Continuity is inherited from the partner proof because it proves an integrable characteristic function, not merely an essential-density estimate.  QED.

### Concrete payoff

If the entirely physical currency satisfies

`|tau| sigma^2 >= kappa`,                                          (3.16)

then

`||p_Q||_infinity <= 9.52440631181 kappa^(-1/3).`                  (3.17)

In particular,

`|tau| sigma^2 >= 1/64`

pays the whole branch at

`boxed: ||p_Q||_infinity <= 38.0976252473,`                         (3.18)

with a continuous `C_0` density.  This converts the newest partner theorem from hidden `(d,g,beta,ell)` variables into a directly checkable physical-block inequality.

For the partner's strict target family

`Q_(m,eta)=2(X_0+eta v.X_K)G+(b.X_K)^2`, `m>=8`,                    (3.19)

one has `tau=1`, `sigma=eta` and

`max_k(b_k^2+v_k^2)=(4m-2)/(m(m+1))<=1/2`.                         (3.20)

Hence (3.6) gives the literal target inequality

`||p_(Q_(m,eta))||_infinity <= 9.52440631181 eta^(-2/3)`.           (3.21)

Since here `G` itself is one original cap-one coordinate, `gamma M_G<=1`, and the sharper partner formula (3.7) gives

`boxed:
 ||p_(Q_(m,eta))||_infinity
 <= 3*2^(4/3) eta^(-2/3)
 =7.55952629937 eta^(-2/3).`                                       (3.22)

This is an actual application of the completed fleet02/B18 theorem, not a post-rotation independence argument.

## 4. Theorem B — finite-ray replacement for the Hadamard source banks

The preceding B18 run closed the fleet02/B18 low-hub stress family for the particular four Walsh/Hadamard source rays.  The equal Walsh weights are not needed.

### Setup

Fix the partner's low-hub parameter `0<eta<1/64`, let

`c=sqrt(1-eta^2)`,
`r=(x,y,-eta)`,
`x=sqrt(1-eta^4-eta^6)-c eta`,
`y=sqrt(2 c eta x)`.                                                (4.1)

The partner identity is

`||r||^2=1-eta^6`.                                                  (4.2)

Set

`H=(I_3-r r^T)^(1/2)`.                                              (4.3)

Then

`H r = eta^3 r`, `det H=eta^3`.                                    (4.4)

Let `W` be **any** real `m x 3` matrix with

`W^T W=I_3`,                                                        (4.5)

and use residual frame rows `W H`.  Since

`(WH)^T(WH)=H^2=I-r r^T`,                                          (4.6)

adjoining the distinguished row `r` again gives three orthonormal frame columns.  Therefore the partner construction with

`p=eta e_0+c e`,
`A=p n^T+n p^T+beta beta^T`                                        (4.7)

still has exact nonzero spectrum `{-1,1,1}`.  No Hadamard assumption is needed for this spectral fact.

Assume the rows of `W` lie in `B` nonzero one-dimensional rays.  Thus the residual ORIGINAL coordinates have a partition

`K = K_1 disjoint_union ... disjoint_union K_B`,                    (4.8)

unit vectors `a_alpha in R^3`, and scalars `c_j` such that

`w_j=c_j a_alpha` for `j in K_alpha`.                               (4.9)

Put

`s_alpha=(sum_(j in K_alpha)c_j^2)^(1/2)`,
`u_alpha=s_alpha a_alpha`,
`Z_alpha=s_alpha^(-1) sum_(j in K_alpha)c_j X_j`.                  (4.10)

Then the `Z_alpha` are mutually independent, each is a norm-one original-coordinate projection, and

`sum_alpha u_alpha u_alpha^T=I_3`.                                 (4.11)

By LPP, each `Z_alpha` has density cap at most `sqrt(2)`, hence every pair `(Z_alpha,Z_beta)` from disjoint banks has joint density cap at most `2`.  If the union contains only two original source coordinates, the direct product/Jacobian estimate is even smaller, so there is no endpoint gap.

### `QFORM-EQUAL-SPECTRUM-LOWHUB-FINITERAY-CLOSURE-v1`

Let `N=binom(B,2)`.  For arbitrary independent original-coordinate input densities bounded by one, the low-hub target form (4.7) has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= 3*4^(2/3)
    [N/((1-eta^2)(1-eta^6))]^(1/3).`                               (4.12)

Consequently every such completion with **at most four source rays** satisfies

`boxed: ||p_Q||_infinity < 13.738`                                 (4.13)

uniformly in the number of original coordinates and in `0<eta<1/64`.
For at most three rays the corresponding constant is `<10.904`.

This strictly enlarges the earlier four-Walsh-bank family: the ray directions, bank sizes and within-bank coefficients may be arbitrary, subject only to (4.5) and the finite-ray decomposition.

### Proof

Let `T` be the deterministic row-coordinate change from `(n,beta,e)` to `(p,n,beta)` on residual coordinates.  As in the previous exact calculation,

`det T=c`.                                                          (4.14)

The active row multiplying `Z_alpha` is `u_alpha H T`, while the distinguished null-diagonal leaf has active row `rT`.  From (4.4),

`det[rH;u_alpha H;u_beta H]
 = det(H) det[r;u_alpha;u_beta]
 = eta^3 det[r;u_alpha;u_beta]`.                                   (4.15)

But `rH=eta^3 r`, so cancellation gives

`det[r;u_alpha H;u_beta H]
 = det[r;u_alpha;u_beta]`.                                         (4.16)

Therefore

`det[rT;u_alpha H T;u_beta H T]^2
 = c^2 det[r;u_alpha;u_beta]^2`.                                   (4.17)

Now set `U=[u_1 ... u_B]`, so `UU^T=I_3` by (4.11).  Apply Cauchy--Binet first to `U`, then to the augmented matrix `[U r]`:

`det(UU^T)=1`,
`det(UU^T+r r^T)=1+||r||^2`.                                      (4.18)

Subtracting the two Cauchy--Binet expansions yields the exact exterior-frame identity

`sum_(alpha<beta) det[r;u_alpha;u_beta]^2
 = ||r||^2
 = 1-eta^6`.                                                       (4.19)

Hence some pair of source banks obeys

`det[r;u_alpha;u_beta]^2 >= (1-eta^6)/N`.                          (4.20)

The quadratic matrix in active `(p,n,beta)` coordinates is

`D=[[0,1,0],[1,0,0],[0,0,1]]`, `|det D|=1`.                       (4.21)

Thus the retained quadratic matrix on
`(X_*,Z_alpha,Z_beta)` has determinant `Delta` satisfying

`|Delta|
 = det[rT;u_alpha H T;u_beta H T]^2
 >= (1-eta^2)(1-eta^6)/N`.                                         (4.22)

Its `X_*^2` pivot is exactly zero by the partner construction.

Condition the hub and all ORIGINAL coordinates in the unselected banks.  The selected banks enter the rank-three spectral projection only through `Z_alpha,Z_beta`, because their `W` rows are collinear within each bank.  Hence the retained scalar `X_*` is genuinely independent of the selected pair, whose joint density cap is at most `M=2`.  Conditioning produces only deterministic affine terms in the retained triple.  Since (4.22) makes the quadratic block invertible, a deterministic translation removes those affine terms without mixing the scalar and pair or altering their density caps.

Apply the completed fleet02/B18 receiver (1.6) with `K_0=1`, `M<=2` and (4.22):

`||p_Q||_infinity
 <=3*4^(2/3)
   [N/((1-eta^2)(1-eta^6))]^(1/3),`

which is (4.12).  For `B<=4`, `N<=6`; the right side is largest as `eta` approaches `1/64` and equals

`3*4^(2/3)
 [6/((1-1/64^2)(1-1/64^6))]^(1/3)
 =13.7376889776911...`,                                           (4.23)

proving (4.13).  For `B<=3`, replace `6` by `3`, giving
`10.9036109673994...`.  QED.

### Continuity for Theorem B

The scalar/dependent-pair receiver used in (4.12) proves essential boundedness.  I do **not** infer an integrable characteristic function or a continuous representative from that argument.  Continuity remains separate on this branch.

## 5. What changed in the proof map

1. The newest fleet02/B18 diffuse-private-bank theorem now has a purely physical currency:

`|tau| sigma^2
 = |lambda_nonzero(A_KK)|
   ||A_(J,K) P_(ker A_KK)||_HS^2`.                                (5.1)

When its coordinate two-plane leverage is at most `1/2`, (3.6) pays the branch and continuity simultaneously.  The hidden normal-form parameters no longer need to be estimated separately.

2. The previous low-hub Hadamard closure was not a Walsh coincidence.  Any exact residual completion with at most four source rays is uniformly paid by `<13.738`; arbitrary weights and ray directions are allowed.

3. The remaining low-hub obstruction is therefore more precise: **unbounded source-ray complexity / fully source-entangled residual geometry**, or the absence of a substantial exact private `A_(0,K)=0` bank.  Small nonzero hub edges cannot be deleted under the rough-law hypotheses.

## 6. Correction audit and scope boundary

No arbitrary-joint coarea theorem, conditional-density-cap-as-independence step, post-rotation independence, law-uniform pointwise quadratic-phase decay, fixed-good-minor assertion, perturbative deletion of a small coefficient, interval-to-Borel transfer, or small-random-quadratic-error estimate is used.

The fresh correction `QFORM-TWO-BANK-INNOVATION-SLOPE-LOWERBOUND-FALSE-v1` is also preserved: neither theorem above infers an order-one inter-bank slope separation from small innovations.  The finite-ray proof instead spends an exact Cauchy--Binet exterior-volume identity.

Theorem A assumes an exact source-private zero hub block `A_(0,K)=0`; Theorem B assumes the exact equal-spectrum low-hub partner construction and finitely many exact source rays.  Neither implication supplies those structures from the bare three-large-eigenvalue hypothesis.  Arbitrary extra spectrum and fully source-entangled rough-law configurations remain outside these statements.  The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

Privacy/source review of this changed file: mathematical formulas, public bibliographic data, repository-internal nonsecret commit pins and run metadata only; no credentials, signed URLs, personal data, trading/client material, permission changes or public-release action.
