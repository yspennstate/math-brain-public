SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B18, 2026-09-23T13:06:19Z.
attacking: literature-to-proof transfer for the Schur-isotropic survivor; close the circular two-sheet stress family with the newest account03/B18 null-hub transverse compiler, then identify the exact determinant currency of the surviving heavy-transverse branch.

# account02/B18 r29 — circular two-sheet closure and the null-hub triple-minor ledger

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: literature-to-proof transfer / complementary source-valid constructions  
Status: `NEW TARGET-VALID STRESS-FAMILY CLOSURE + NEW STRUCTURAL LEDGER / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The new results below do not use moments, bounded support, log-concavity, iid laws, a diagonal random basis, post-rotation independence, arbitrary-joint coarea, conditional projection-density caps, or a law-uniform pointwise quadratic-phase decay estimate.

## 1. Entry debt and sources actually used

The previous B18 run left one explicit source-valid stress obstruction:

`QFORM-CIRCULAR-THREEDIM-PROVENANCE-TWOSHEET-v1`.

The family is

`v_j=m^(-1/2)(1,sqrt(2) cos(2 pi j/m),sqrt(2) sin(2 pi j/m))`,

`u_0=m e_1`,

`D_m=[[0,(1+m^2)^(-1/2),0],[(1+m^2)^(-1/2),0,0],[0,0,1]]`,

`A_m=U D_m U^T`,

where the residual rows `v_j` form a Parseval frame in `R^3`. One has exactly

`spec_nonzero(A_m)={-1,1,1}`,

and

`Q_m=2/sqrt(1+m^2) (Y_1+m X_0)Y_2+Y_3^2`.

Earlier exact scalar-bank, exact planar-bank, one-cut and one-pivot compilers all lose dimension on this family, while the pinned ruled-surface theorem only paid the one-sheet side. The first unpaid implication was the negative/two-sheet half-line while preserving the true original product provenance of the three-dimensional residual projection.

### 1.1 Designated partner actually applied

The latest compatible completed designated-partner theorem consumed here is account03/B18 r28:

`yspennstate/math-open-problems@43b16ba3992035298289170540682e8aa62a9ad4`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260923T120257Z-account03-B18-QFORM-r28/REPORT.md`.

Its theorem `QFORM-SCHUR-NULLHUB-TRANSVERSE-COMPILER-v1` treats the exact-rank-three Schur-isotropic packet

`Q=(Y+r n X_0)^T D(Y+r n X_0)`, `Y=V^T X_res`, `V^T V=I_3`, `n^T D n=0`.

Put

`q_j=||P_(n^perp)v_j||^2`.

If `max_j q_j<=1/2`, then for arbitrary independent original-coordinate cap-one input laws,

`||p_Q||_infinity <=3*2^(4/3)[r^2 |det D|]^(-1/3)`,                 (1.1)

and the density is continuous and vanishes at infinity. If the physical nonzero eigenvalues have modulus at least `s`, the exact pseudodeterminant identity

`(1+r^2)|det D|=|pdet A|>=s^3`                                    (1.2)

gives

`||p_Q||_infinity <=3*2^(4/3) s^(-1) (1+r^(-2))^(1/3)`.           (1.3)

This result is source-compatible with the owner class because its proof uses a joint original-product mixed-Fresnel estimate. It does not diagonalize the random vector and then declare the rotated coordinates independent.

The partner in turn consumes the exact-null mixed-Fresnel theorem account03/B10 r24:

`yspennstate/math-open-problems@c0d7e627b3b877fcecc3004a58335658f6541d64`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260923T114517Z-account03-B10-QFORM-r24/REPORT.md`.

That theorem identifies the transverse leverage gate exactly with the two-dimensional augmented original-product Fourier frame; no projection-density-to-independence conversion occurs.

### 1.2 Pinned e5f result applied at a real inequality

The required source bundle

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

contains the proved ruled one-sheet estimate. For an exact rank-three signature `(2+,1-)` with all three magnitudes at least one,

`p_Q(t)<=pi sqrt(2)` for a.e. `t>=0`.                              (1.4)

Applying it to `A_m`, after choosing the sign so the two positive eigenvalues are the majority, gives

`p_(Q_m)(t)<=pi sqrt(2)` for a.e. `t>=0`.                          (1.5)

This is a literal inequality on the same target-valid circular family. The new partner transfer below is what additionally closes the formerly unpaid negative side.

### 1.3 Primary literature check for the projection input in (1.4)

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949 / Israel J. Math. 216 (2016), Theorem 1.1, assumes

`f(x)=prod_i f_i(x_i)`, each `f_i>=0`, `||f_i||_1=1`, `||f_i||_infinity<infinity`,

and proves for every `k`-dimensional orthogonal marginal

`||pi_E f||_infinity <= min((n/(n-k))^((n-k)/2),2^(k/2)) prod_i ||f_i||_infinity^(gamma_i)`,

with `gamma_i in [0,1]` and `sum gamma_i=k`. Thus the owner cap-one class has every two-dimensional orthogonal marginal bounded by exactly `2`. There are no moment, compact-support, log-concavity, smoothness, centering, symmetry or iid assumptions. The theorem controls a projected joint density; it does not assert independence of the projected coordinates.

A tempting alternative literature route remains non-source-matching. Glazer--Mikulincer, arXiv:2108.04268, derive their dimension-free polynomial van-der-Corput/Fourier-decay statement for isotropic log-concave product measures. Their Section 5 explicitly assumes an isotropic log-concave one-dimensional law and then an isotropic log-concave product measure. The owner target allows arbitrary fragmented cap-one laws and already contains phase-aligned counterexamples to a law-uniform pointwise quadratic-phase decay claim. I therefore do not transfer that theorem to QFORM.

## 2. The circular two-sheet obstruction is closed

In the circular family the Schur null direction is simply

`n=e_1`, `r=m`.

For every residual row,

`P_(n^perp)v_j=m^(-1/2)(0,sqrt(2)cos(2 pi j/m),sqrt(2)sin(2 pi j/m))`,

hence exactly

`q_j=2/m`.                                                         (2.1)

Therefore for every `m>=4`,

`max_j q_j<=1/2`,                                                  (2.2)

so every hypothesis of the designated-partner theorem holds in original coordinates. Also

`|det D_m|=1/(1+m^2)`.                                             (2.3)

Substituting `r=m` and (2.3) into (1.1) gives the whole-line bound

`boxed: ||p_(Q_m)||_infinity
 <=3*2^(4/3)(1+m^(-2))^(1/3),  m>=4.`                              (2.4)

The right side is decreasing in `m`; therefore

`boxed: sup_(m>=4) ||p_(Q_m)||_infinity
 <=3*2^(4/3)(17/16)^(1/3)
 =7.713844771974705... .`                                         (2.5)

As `m->infinity`, the certificate tends to

`3*2^(4/3)=7.559526299369239...`.                                 (2.6)

The partner theorem also gives a continuous `C_0` density. Thus the exact family previously constructed as the live nonplanar, non-source-separated two-sheet stress test is no longer an obstruction: its negative side is now paid as well as its one-sheet side. This is a genuine closure, not a subclass theorem mislabeled as the full target.

## 3. New exact determinant ledger for every null-hub packet

The partner theorem leaves, for moderate/high shear, only failure of the transverse-diffuse gate. The same exact algebra gives a useful stronger structural invariant.

### Theorem — `QFORM-NULLHUB-TRIPLE-MINOR-LEDGER-v1`

Consider the exact-rank-three Schur-isotropic packet of Section 1.1. In the account03/B18 whitening, write the physical spectral frame as

`A=R M R^T`, `R^T R=I_3`,

with original physical hub row

`u_0=sqrt(h) n`, `n^T M n=0`,

where

`h=r^2/(1+r^2)`, `|det M|=(1+r^2)|det D|`.                         (3.1)

Use the exact account03/B10 null-hub normal form. Put `s=||Mn||`; since `n^T M n=0`, choose an orthonormal basis `(n,v,w)` in spectral space in which

`M=[[0,s,0],[s,b,c],[0,c,d]]`.                                    (3.2)

Write each residual physical spectral row as

`u_j=t_j n+alpha_j v+beta_j w`.                                   (3.3)

Parseval gives

`sum_j alpha_j^2=sum_j beta_j^2=1`,
`sum_j alpha_j beta_j=0`,                                         (3.4)

and the transverse leverage is exactly

`q_j=alpha_j^2+beta_j^2`.                                        (3.5)

The hub-leaf coupling is

`g_j=A_0j=sqrt(h)s alpha_j`,                                      (3.6)

and the full form admits the exact original-coordinate shear

`Q=2(X_0+ell.X_L)(g.X_L)+d(beta.X_L)^2`.                          (3.7)

For two distinct residual indices `i,j`, restrict (3.7) to the physical principal block `{0,i,j}`. The local change `X_0'=X_0+ell_i X_i+ell_j X_j` is only a determinant-one congruence used to compute the matrix determinant; it is not a probabilistic change of independent variables. It reduces that principal matrix to

`[[0,g_i,g_j],
  [g_i,d beta_i^2,d beta_i beta_j],
  [g_j,d beta_i beta_j,d beta_j^2]]`.

Hence

`det A[{0,i,j}]=-d(g_i beta_j-g_j beta_i)^2`.                      (3.8)

Since `det M=-s^2 d`, equations (3.1),(3.6) give

`boxed: |det A[{0,i,j}]|
 =h|det M|(alpha_i beta_j-alpha_j beta_i)^2
 =r^2|det D|(alpha_i beta_j-alpha_j beta_i)^2.`                    (3.9)

Define

`w_ij=(alpha_i beta_j-alpha_j beta_i)^2`, `i<j`.                   (3.10)

By Cauchy--Binet applied to the two orthonormal columns `alpha,beta`,

`sum_(i<j) w_ij=1`.                                                (3.11)

Moreover its vertex marginal is exactly the transverse leverage:

`sum_(j!=i) w_ij
 =alpha_i^2 sum_j beta_j^2+beta_i^2 sum_j alpha_j^2
  -2 alpha_i beta_i sum_j alpha_j beta_j
 =q_i`.                                                            (3.12)

Consequently the physical hub-triple determinants obey the two exact ledger identities

`boxed: sum_(i<j)|det A[{0,i,j}]|=r^2|det D|,}`                   (3.13)

`boxed: sum_(j!=i)|det A[{0,i,j}]|=r^2|det D| q_i.}`              (3.14)

Thus the partner's transverse leverage `q_i` is literally the marginal of the normalized absolute hub-triple determinant-volume measure. This is stronger than merely knowing that some aggregate curvature exists.

### Target-normalized consequence

If the three nonzero physical eigenvalues have modulus at least `s`, then

`|pdet A|=(1+r^2)|det D|>=s^3`,                                   (3.15)

so

`r^2|det D| >= [r^2/(1+r^2)]s^3`.                                (3.16)

For `r>=1/2`, the factor on the right is at least `1/5`. Therefore

`sum_(i<j)|det A[{0,i,j}]| >=s^3/5`.                              (3.17)

If the designated-partner gate fails at an index `i`, so `q_i>1/2`, then that single original coordinate captures more than half of this determinant-volume:

`boxed: sum_(j!=i)|det A[{0,i,j}]| >s^3/10.}`                     (3.18)

In the owner normalization `s=1`, the lower bounds are `1/5` globally and `>1/10` on a heavy anchor.

This does **not** imply one uniformly large physical `3x3` minor: the mass in (3.18) may be spread over arbitrarily many leaves. It therefore respects the live corrections refuting fixed-good-minor reductions.

## 4. A clean moderate/high-shear dichotomy

Combining Section 2's partner theorem with the new ledger gives a compact source-valid compiler.

### `QFORM-NULLHUB-DENSITY-OR-ANCHOR-STAR-v1`

For a target-normalized (`s=1`) exact-rank-three Schur-isotropic null-hub packet with `r>=1/2`, one of the following holds:

1. `max_j q_j<=1/2`, in which case

`||p_Q||_infinity <=3*2^(4/3)*5^(1/3)=12.9266081401913...`,        (4.1)

and `p_Q` is continuous and vanishes at infinity; or

2. some original residual coordinate `i` satisfies

`sum_(j!=i)|det A[{0,i,j}]|>1/10`.                                (4.2)

No spectral/random-coordinate rotation is used in this dichotomy. The heavy branch is now a fixed-two-anchor **aggregate principal-curvature star**, not an amorphous three-dimensional projected-density problem.

This structural statement also explains why the circular stress family disappears: for it `q_j=2/m<=1/2`, so it lies exactly in branch 1 once `m>=4`.

## 5. Why the new anchor-star is not yet a full proof

The first unpaid implication is now

`QFORM-NULLHUB-ANCHOR-STAR-AGGREGATION-v1`:

from original-coordinate product inputs and the fixed-anchor lower bound

`sum_(j!=i)|det A[{0,i,j}]|>1/10`,

obtain a uniform whole-line density estimate without selecting one leaf `j` and paying the reciprocal of an arbitrarily small individual minor.

The exact distribution in (3.10)--(3.12) suggests that the correct next mechanism is a weighted/grouped original-coordinate argument: `w_ij` is already a probability distribution whose anchor marginal is `q_i>1/2`. A proof must spend this mass before conditioning destroys the product provenance. The following shortcuts remain invalid:

- infer independence of `(alpha.X,beta.X)` after projection;
- replace the residual projected law by an arbitrary joint density cap and use indefinite coarea;
- select a single physical `3x3` minor from (4.2);
- use only X-ray bounds on the two-sheet trace;
- treat the hub shear as a probabilistic independent-coordinate change;
- delete a small coefficient as a random perturbation under unbounded inputs.

The pinned e5f Theorem D/D' and the new ledger are analogous in that both use determinant-volume marginals, but Theorem D concerns a disjoint cross block and its 3-volume, whereas (3.10) is a two-dimensional transverse Pluecker measure attached to a physical null hub. No direct theorem transfer between them is claimed.

## 6. Literature boundary

The only external marginal theorem needed for the ruled one-sheet comparison in this run is LPP Theorem 1.1, whose literal hypotheses match the owner product class. It yields a joint density cap, not post-rotation independence.

The Glazer--Mikulincer polynomial Fourier-decay theorem is not usable at owner scope: the relevant decay statement assumes isotropic log-concave product measures. Likewise Carbery--Wright type polynomial small-ball bounds are log-concave/moment-normalized tools and are not silently imported into the arbitrary fragmented cap-one setting.

Search failure is not a novelty claim. The new content here is the exact calculation (3.9)--(3.14), the target-normalized dichotomy (4.1)--(4.2), and the literal application of the completed designated-partner theorem to close the previously constructed circular whole-line stress family.

## 7. Status

- Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Circular nonplanar family `Q_m`, `m>=4`: **WHOLE-LINE ESSENTIAL DENSITY BOUNDED AND CONTINUOUS**, with (2.4)--(2.5).
- Pinned ruled one-sheet estimate: **APPLIED** at (1.5), sharper on `t>=0` but no longer needed to cover the circular negative side.
- New exact hub-triple determinant ledger: **PROVED** at (3.9)--(3.14).
- Moderate/high-shear null-hub branch: reduced to either the completed diffuse theorem or the fixed-anchor aggregate star (4.2).
- Continuity: proved only on the completed partner branch; still open globally.

No task/schedule state, enabled/paused state, notification/email setting, cross-account authentication, permission, public release, paid API/Codex use, remote workflow, installation, or unrelated data was changed.
