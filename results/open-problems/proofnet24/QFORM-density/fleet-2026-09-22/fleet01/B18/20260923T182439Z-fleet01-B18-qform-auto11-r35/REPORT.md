SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B18, 2026-09-23T18:24:39Z.
attacking: literature-to-proof transfer for the remaining rough-input near-null/overlapping-source collar; isolate an original-coordinate two-leaf packet and pay it with the completed fleet02/B18 scalar/dependent-pair theorem.

# fleet01/B18 r35 — local-area conditioning compiler for the exact-null hub

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `PROVED SUPPORTING TARGET-LEVEL BRANCH / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Continuity:** essential boundedness only from the new argument; continuity is not claimed.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN: arbitrary independent real coordinates with one-dimensional densities bounded by one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, no moments, iid, smoothness, log-concavity, connected support, bounded support, centering, or post-rotation independence.

This run proves a new conditioning compiler for the exact-null-hub normal form and applies it at a literal inequality to the completed fleet02/B18 result. It closes the **concentrated anchored determinant** part of the remaining punctured tiny-edge collar. It does not force such a concentrated determinant from the bare spectral hypothesis.

## 1. Fresh state and corrections consumed


The live corrections retained here include, in particular:

* no independence after rotating spectral coordinates;
* arbitrary bounded joint density does not imply the false indefinite rank-three coarea bound;
* a bounded conditional density is not a substitute for genuine independence;
* no universal positive moment of conditional projection density is available;
* a small nonzero coefficient cannot be deleted for arbitrary rough/unbounded inputs;
* the three-large-eigenvalue hypothesis does not force one uniformly good physical minor.

The proof below conditions only on ORIGINAL coordinates. No random variable is spectrally rotated.

## 2. Primary literature audit

### 2.1 Livshyts--Paouris--Pivovarov: exact marginal theorem used

Primary source:

G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889; arXiv:1507.07949, Theorem 1.1.

Their literal hypotheses are a product probability density

`f(x)=prod_i f_i(x_i)`, `f_i>=0`, `||f_i||_1=1`, each `f_i` bounded,

and an orthogonal `k`-dimensional marginal. Theorem 1.1 gives weights `gamma_i in [0,1]`, `sum gamma_i=k`, and

`||pi_E f||_infinity <= min((n/(n-k))^((n-k)/2),2^(k/2)) prod_i ||f_i||_infinity^(gamma_i)`.

Hence for the owner cap-one class every two-dimensional orthogonal projection has joint density cap at most `2`. There is no moment, iid, smoothness, support, log-concavity, centering, or symmetry assumption. The theorem is a marginal-density bound only; it does NOT make projected coordinates independent.

For a full-row-rank `2 x m` linear map `L`, factor `L=T P` with `P` an orthogonal two-dimensional projection and `|det T|=sqrt(det(LL^T))`. Therefore

`boxed: ||p_(LX)||_infinity <= 2/sqrt(det(LL^T)).`                 (2.1)

When `m=2`, the direct change-of-variables formula for the two ORIGINAL independent coordinates is sharper:

`boxed: ||p_(LX)||_infinity <= 1/|det L|.`                         (2.2)

### 2.2 Quadratic-form regularity literature checked, but not imported beyond scope

R. Herry, D. Malicet, G. Poly, *Regularity of laws via Dirichlet forms -- Application to quadratic forms in independent and identically distributed random variables* (PTRF 2025; arXiv:2303.09488), assumes iid inputs in a regular class representable as sufficiently smooth functions of a Gaussian field and studies regularity/strong convergence under additional normalization/spectral hypotheses. These hypotheses do not match arbitrary non-iid fragmented cap-one laws. I therefore do not use that paper as an unrestricted QFORM solution. This is a hypothesis comparison, not a novelty claim.

The newer interactive Gaussian-mixture theorem was also checked: it proves the full matrix statement with constant `<3` for independent Gaussian component mixtures satisfying `E T_i^(-1/2)<=sqrt(2*pi)`, but the cap-one condition alone does not imply that component-moment condition for random separated centers. No mixture-approximation shortcut is used here.

## 3. Completed designated-partner theorem actually applied

Pinned completed fleet02/B18 theorem:

`QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`,
`math-open-problems@ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/20260923T013147Z-bf13c29b/REPORT.md`.

It states: if `S` is a real scalar with density cap `K`, `(C,D)` is genuinely independent of `S` and has arbitrary joint density cap `M`, and `beta,gamma_0` are nonzero, then

`T=2 beta S C + alpha C^2 + 2 delta C D + gamma_0 D^2`

has an essentially bounded density satisfying

`boxed: ||p_T||_infinity <= 3(2 M K)^(2/3)|beta^2 gamma_0|^(-1/3).`   (3.1)

The pair `(C,D)` need not have independent components. This exact theorem, not an unverified conditional-cap replacement, is the analytic receiver below.

The latest completed fleet02/B18 exact-null normal form used as structural input is

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/20260923T170538Z-fleet02-B18-auto11/REPORT.md`.

Its active packet is

`Q=2(X_0+ell dot X_L)(g dot X_L)+d(beta dot X_L)^2`,               (3.2)

where all displayed `X` are ORIGINAL independent coordinates, and in the target-normalized moderate/high-shear compiler

`||beta||_2=1`, `beta dot g=0`, `gamma=||g||_2>0`,
`|d| gamma^2=hD`, `h>=1/5`, `D=|pdet A|>=1`.                       (3.3)

For leaf `i`,

`q_i=beta_i^2+g_i^2/gamma^2`.                                    (3.4)

The same completed partner report leaves, after its diffuse/large-edge/zero-edge/source-separated exits, a punctured source-entangled heavy state `q_i>1/2`, `0<|g_i|<1/64`.

## 4. New theorem: local-area conditioning compiler

### `QFORM-NULLHUB-LOCAL-AREA-CONDITIONING-v1`

Consider (3.2), with arbitrary independent original cap-one inputs. Let `J` be a subset of leaf indices and `K=L\J`. Define

`Omega_J = ||g_J||_2^2 ||beta_J||_2^2 - <g_J,beta_J>^2`.            (4.1)

Assume

`Omega_J>0`,                                                       (4.2)

and assume the restriction of the twist to `J` lies in the two-row span,

`ell_J=a g_J+b beta_J`                                            (4.3)

for some real `a,b`. No condition is imposed on `g_K,beta_K,ell_K`.

Then

`boxed: ||p_Q||_infinity <= 3*4^(2/3) (|d| Omega_J)^(-1/3).`        (4.4)

This strictly relaxes the source-separated theorem in the completed fleet02/B18 report: active `g` and `beta` coefficients on the conditioned complement `K` are allowed arbitrarily.

### Proof

Condition on the complete ORIGINAL coordinate block `X_K=x_K`. Set the deterministic constants

`G=g_K dot x_K`, `B=beta_K dot x_K`, `L0=ell_K dot x_K`.            (4.5)

Define

`C=g_J dot X_J+G`,
`D0=beta_J dot X_J+B`,
`S=X_0+L0-aG-bB`.                                                  (4.6)

Then `S` is only a deterministic translate of the original scalar `X_0`, so

`||p_S||_infinity<=1`.                                             (4.7)

Moreover `S` is genuinely independent of `(C,D0)`, because after conditioning on `K`, the scalar uses original coordinate `0` and the pair uses only the disjoint original block `J`.

By (4.3),

`X_0+ell dot X_L = S+aC+bD0`.                                     (4.8)

Therefore the conditional polynomial is EXACTLY

`Q=2 S C+2a C^2+2b C D0+d D0^2`.                                 (4.9)

No affine remainder and no perturbative deletion remain.

The coefficient map from `X_J` to the unshifted pair `(g_J dot X_J,beta_J dot X_J)` is the `2 x |J|` matrix with row Gram determinant `Omega_J`. By (2.1),

`||p_(C,D0)||_infinity <=2/sqrt(Omega_J)`.                         (4.10)

Apply the completed partner theorem (3.1) with

`K=1`, `M=2/sqrt(Omega_J)`, `beta=1`, `gamma_0=d`.                 (4.11)

This yields

`||p_(Q|X_K=x_K)||_infinity
 <=3(4/sqrt(Omega_J))^(2/3)|d|^(-1/3)
 =3*4^(2/3)(|d|Omega_J)^(-1/3)`.                                  (4.12)

The bound is uniform in the conditioned value. Averaging the conditional laws proves (4.4). QED.

## 5. Two-leaf corollary: arbitrary twist disappears

Take `J={i,j}`. If

`w_ij=g_i beta_j-g_j beta_i !=0`,                                 (5.1)

then `g_J,beta_J` form a basis of `R^2`, so (4.3) is AUTOMATIC for every possible `ell_J`. Further,

`Omega_J=w_ij^2`.                                                  (5.2)

Because `J` consists of exactly two original independent cap-one coordinates, use the sharper direct Jacobian cap (2.2),

`M<=1/|w_ij|`,                                                     (5.3)

rather than the generic LPP constant. The designated-partner inequality (3.1) now gives

`boxed: ||p_Q||_infinity
 <=3*2^(2/3) (|d| w_ij^2)^(-1/3).}`                               (5.4)

This conclusion allows a completely dense, source-entangled, non-aligned global twist `ell`.

### Exact physical-minor identity

The physical three-coordinate principal matrix on `{0,i,j}` is

`[[0,g_i,g_j],
  [g_i,2 ell_i g_i+d beta_i^2,
       ell_i g_j+ell_j g_i+d beta_i beta_j],
  [g_j,ell_i g_j+ell_j g_i+d beta_i beta_j,
       2 ell_j g_j+d beta_j^2]]`.

Direct expansion cancels every `ell` term and gives

`boxed: det A[{0,i,j}] = -d (g_i beta_j-g_j beta_i)^2.`            (5.5)

Consequently (5.4) can be written in the invariant physical form

`boxed: ||p_Q||_infinity
 <=3*2^(2/3) |det A[{0,i,j}]|^(-1/3).}`                           (5.6)

This is a conditional branch theorem; it does NOT assert that the spectral hypothesis forces one uniformly large such principal minor.

## 6. Actual target-level splice into the punctured heavy collar

For the heavy leaf `i` from the completed fleet02/B18 packet, use `||beta||=1`, `g dot beta=0`, `||g||=gamma`. An exact Lagrange identity gives

`sum_(j!=i) (g_i beta_j-g_j beta_i)^2
 =g_i^2+gamma^2 beta_i^2
 =gamma^2 q_i`.                                                    (6.1)

Multiplying by `|d|` and using (5.5),

`boxed: sum_(j!=i) |det A[{0,i,j}]|
       =|d|gamma^2 q_i
       =hD q_i.`                                                   (6.2)

In the target-normalized heavy branch `h>=1/5`, `D>=1`, `q_i>1/2`, hence

`boxed: sum_(j!=i) |det A[{0,i,j}]| >1/10.`                        (6.3)

Therefore the remaining punctured source-entangled collar has the following exact dichotomy.

### Concentrated anchored determinant — CLOSED

If for some `j!=i`,

`|det A[{0,i,j}]| >=1/320`,                                      (6.4)

then (5.6) gives

`boxed: ||p_Q||_infinity
 <=3*2^(2/3)*320^(1/3)
 =32.5730113991... .}`                                            (6.5)

This is a whole-line essential-density bound valid for arbitrary rough cap-one input laws and arbitrary twist.

### What survives

If (6.4) fails for every `j`, then (6.3) forces at least **33 nonzero anchored leaves**. Indeed at most 32 summands, each `<1/320`, would have total `<1/10`.

Thus the first unpaid exact-null punctured state after this run is not merely "small nonzero edge + entangled twist". It is a **high-cardinality diffuse anchored-volume star**:

`q_i>1/2`, `0<|g_i|<1/64`,
`|det A[{0,i,j}]|<1/320 for every j!=i`,
`sum_(j!=i)|det A[{0,i,j}]|>1/10`,                                (6.6)

plus the already-required failure of the diffuse/source-separated exits. This is consistent with the known stress families that spread aggregate determinant mass over many leaves; it does not contradict them.

## 7. Relation to the newest fleet02/B18 obstruction

The current in-progress fleet02/B18 early artifact constructs a rank-two counterexample showing that an arbitrarily small nonzero edge cannot simply be substituted into the exact-zero-edge receiver when the residual quadratic function is arbitrary. That construction has only two nonzero eigenvalues and therefore is not a QFORM counterexample.

The new theorem here does not make that invalid perturbative step. Instead it requires an actual nonzero **two-leaf wedge** and conditions on all other original leaves. The surviving pair is an invertible linear image of two genuinely independent original coordinates, and the partner theorem is applied to that exact pair. In the true target, the aggregate identity (6.2) quantifies how much such wedge mass must exist in total.

## 8. Continuity and exact remaining debt

The new local-area/two-leaf argument proves essential boundedness. I do **not** claim a continuous representative from the partner receiver; continuity remains separate.

The next mathematical debt is now sharper: exploit the diffuse family of at least 33 small anchored minors in (6.6) **collectively**, without selecting a uniformly good single minor and without replacing the source-entangled twist by an independent spectral variable. The weighted-subset/projected-crossing machinery is a plausible receiver only if its row-marginal and projected-volume gates can be verified for an actual partition of this surviving star. The primary LPP theorem alone supplies projection caps, not that structural partition.

No exact prior theorem found in this targeted audit matches all unrestricted owner quantifiers. Herry--Malicet--Poly has materially stronger input-law assumptions; the Gaussian-mixture full theorem has the inverse-half-variance/component-peak hypothesis. This is not a literature-wide novelty claim.
