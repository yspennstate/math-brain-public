SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-23T19:16:31Z.
attacking: a four-original-coordinate zero-diagonal rank-three core; close the small-range-leverage endpoint by a sharp codimension-one compression lemma, splice the cofactor receiver for the complementary endpoint, and apply account04/B18 at the exact leaf-kernel endpoint.

# account03/B18 r33 — uniform zero-diagonal four-core closure

Programme: `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`, owner-control revision `2026-09-22.15`.

Status: **PROVED SUPPORTING TARGET-LEVEL IMPLICATION / DESIGNATED PARTNER APPLIED / FULL UNRESTRICTED QFORM OPEN.**

Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Main result

### Theorem A — `QFORM-4COORD-ZERODIAG-COMPRESSION-COFACTOR-v1`

Let `A` be an arbitrary real symmetric `n x n` matrix and let the original coordinates `X_1,...,X_n` be independent with probability densities bounded by one. Suppose there is an ORIGINAL-coordinate four-set `I={0,1,2,3}` such that the principal block

`B=A[I,I]`

has rank exactly three, satisfies the physical zero diagonal condition

`B_00=0`,

and its three nonzero eigenvalues obey

`|mu_1|,|mu_2|,|mu_3| >= s > 0`.

Then the full ambient quadratic form `Q=X^T A X` has an essentially bounded density and

`||p_Q||_infinity <= C_4/s`,

where one may take the explicit universal constant

`C_4 = 148/(1-576/148^3)
     = 148*50653/50644
     = 148.02630124002843... .`                                  (1.1)

Thus, in the target normalization `s>=1`, every ambient matrix containing such a four-coordinate core has

`||p_Q||_infinity < 148.027`.                                    (1.2)

The ambient matrix outside `I` is completely arbitrary: it may have extra eigenvalues of either sign and arbitrary cross couplings to the four active coordinates. These become affine terms after conditioning on the outside ORIGINAL coordinates.

Continuity is **not** proved by Theorem A in general. Section 6 proves a continuous-density bound on the exact endpoint where the hub coordinate is entirely in the range of `B`, using the designated account04/B18 theorem.

The full owner conjecture remains OPEN because `s_3(A)>=1` does not force the existence of a four-coordinate exact-rank-three principal block satisfying `B_00=0`.

## 2. New deterministic lemma: a sharp codimension-one principal compression bound

### Lemma B — `QFORM-CODIM1-PRINCIPAL-COMPRESSION-v1`

Let `B` be any real symmetric `m x m` matrix of rank `m-1`. Let `z` be a unit vector spanning `ker B`, and suppose every nonzero singular value of `B` is at least `s>0`. Delete coordinate `0` and let `C` be the resulting `(m-1)x(m-1)` principal submatrix. Then

`boxed: sigma_min(C) >= s z_0^2.`                                 (2.1)

The inequality is sharp for every possible value of `z_0`: equality occurs for

`B=s(I-zz^T)`.

#### Proof

If `z_0=0`, the right side of (2.1) is zero and the assertion is trivial. Assume `z_0!=0`.

First, `C` is invertible. Indeed, if `Cy=0` and `tilde y=(0,y)`, then

`B tilde y=(alpha,0)`

for some `alpha`. Since `range(B)=z^perp`, we have `z_0 alpha=0`, hence `alpha=0`. Thus `tilde y in ker B=span{z}`. Its zeroth coordinate is zero while `z_0!=0`, so `tilde y=0` and `y=0`.

Now fix `x in R^(m-1)` and put `y=C^{-1}x`, `tilde y=(0,y)`. Write

`B tilde y = w=(alpha,x)`.

Again `w in z^perp`, so

`alpha = - <z_-,x>/z_0`.

Consequently

`||w||^2
 = ||x||^2 + |<z_-,x>|^2/z_0^2
 <= ||x||^2 [1+(1-z_0^2)/z_0^2]
 = ||x||^2/z_0^2`,

hence

`||w|| <= ||x||/|z_0|`.                                          (2.2)

Let `v=P_(z^perp) tilde y`. Since `Bz=0`,

`Bv=B tilde y=w`.

On `z^perp`, the inverse of `B` has operator norm at most `1/s`, hence by (2.2)

`||v|| <= ||x||/(s |z_0|)`.                                      (2.3)

Write the orthogonal decomposition

`tilde y=v+t z`.

The zeroth coordinate of `tilde y` is zero, so `t=-v_0/z_0`. Because `v perp z`,

`|v_0|=|<v,e_0-z_0 z>| <= sqrt(1-z_0^2)||v||`.

Therefore

`||tilde y||^2
 = ||v||^2+t^2
 <= ||v||^2 [1+(1-z_0^2)/z_0^2]
 = ||v||^2/z_0^2
 <= ||x||^2/(s^2 z_0^4)`.

Thus

`||C^{-1}|| <= 1/(s z_0^2)`,

which is equivalent to (2.1).

For sharpness, take `B=s(I-zz^T)`. The deleted principal block is

`C=s(I-z_-z_-^T)`,

whose eigenvalues are `s` with multiplicity `m-2` and `s z_0^2`. QED.

This lemma is purely deterministic, sign-free, and uses no probabilistic rotation.

## 3. Small-range-leverage branch: condition on the physical hub

Return to Theorem A and let `z` be a unit kernel vector of `B`. Define the range leverage of the physical zero-diagonal coordinate

`h = ||P_(range B)e_0||^2 = 1-z_0^2`.                             (3.1)

Let

`C=B[{1,2,3},{1,2,3}]`.

Lemma B gives

`boxed: sigma_min(C) >= s(1-h).`                                  (3.2)

Now condition on every outside original coordinate and also on the physical coordinate `X_0`. The three remaining variables `X_1,X_2,X_3` are still genuinely independent and retain their original density caps. Their conditional polynomial is

`X_-^T C X_- + b^T X_- + c`,                                     (3.3)

where `b,c` can depend arbitrarily on the conditioned values.

Use the already completed account03/B18 cap-one three-variable theorem

`QFORM-THREE-DISJOINT-BANKS-ALLPIVOTS-v1`,

source

`yspennstate/math-open-problems@602d508c11f3bb5848b65581a750b4497708bd5f`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260923T112422Z-account03-B18-QFORM-r27/REPORT.md`.

Its internal Lemma B states that for three independent cap-one variables, a symmetric `3x3` quadratic matrix with `sigma_min>=tau` and an arbitrary affine term has density cap `<148/tau`. Applying it to (3.2)-(3.3) yields, for `h<1`,

`boxed: ||p_Q||_infinity < 148/[s(1-h)].`                          (3.4)

The estimate is uniform in all conditioning variables, so averaging preserves the same essential-density cap. No conditional-density cap is substituted for independence: the active variables are three ORIGINAL independent coordinates.

## 4. Complementary cofactor branch

The complementary completed theorem is account01/B18

`QFORM-4COORD-NULLHUB-COFACTOR-v1`,

read at

`yspennstate/math-open-problems@8103579cff840cf3e09607ac05841bd156fa8744`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260923T185527Z-account01-B18-qform-auto11-r36/REPORT.md`.

Under exactly the present physical hypotheses `rank(B)=3`, `B_00=0`, `|mu_j|>=s`, it proves, for every `h>0` and arbitrary affine terms,

`boxed: ||p_Q||_infinity
 <= 576^(1/3) s^(-1) h^(-1/3).`                                  (4.1)

Its proof uses the physical adjugate identity and a completed planar-twist receiver; no fixed minor is asserted from the global three-eigenvalue hypothesis.

The value of (4.1) diverges only at `h -> 0`, precisely where the new compression estimate (3.4) is strongest.

## 5. Exact splice and constant

Put

`a=576^(1/3)`

and choose the exact threshold

`h_0=(a/148)^3=576/148^3=9/50653`.                               (5.1)

If `0<=h<=h_0`, then (3.4) gives

`||p_Q||_infinity
 < 148/[s(1-h_0)]
 = [148*50653/50644]/s
 = 148.02630124002843.../s.`                                     (5.2)

If `h>=h_0`, then (4.1) gives

`||p_Q||_infinity
 <= a s^(-1) h_0^(-1/3)
 =148/s.`                                                        (5.3)

Equations (5.2)-(5.3) prove Theorem A. The threshold (5.1) is chosen for a clean exact proof, not as the numerically optimal crossing; no numerical experiment enters the theorem.

This splice completely removes the `h^(-1/3)` blow-up for the stated four-coordinate zero-diagonal core.

## 6. Required account04/B18 application: exact leaf-kernel endpoint and continuity

This section applies a completed **account04/B18** theorem at an actual inequality.

Assume the endpoint

`h=1`, equivalently `z_0=0`.                                     (6.1)

Write the four-coordinate block as

`B=[[0,g^T],[g,C]]`.

Since `h>0`, `g!=0`. Put `gamma=||g||` and `u=g/gamma`. The algebraic null-hub decomposition in the account01/B18 report gives

`C = g ell^T + ell g^T + d beta beta^T`,                          (6.2)

where `beta perp g`, `||beta||=1`, and `d!=0`.

At (6.1), the kernel vector is `z=(0,z_L)`. From `Bz=0` we have `g·z_L=0` and `Cz_L=0`. Substituting (6.2),

`0=Cz_L=g(ell·z_L)+d beta(beta·z_L)`.

The two vectors `g` and `beta` are orthogonal and nonzero, so

`ell·z_L=0`, `beta·z_L=0`.                                       (6.3)

Thus the three leaf vectors `u,beta,z_L` form an orthonormal basis and

`ell = alpha u + b beta`                                         (6.4)

for some real `alpha,b`.

Define the two overlapping leaf projections

`S=u·X_L`, `T=beta·X_L`.

The primary theorem of Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures* (Israel J. Math. 216 (2016), arXiv:1507.07949), applies literally: `(S,T)` is a two-dimensional orthogonal marginal of the genuine three-coordinate product law, hence it has a joint density with

`||p_(S,T)||_infinity <= 2`.                                     (6.5)

No independence between `S` and `T` is asserted. The original scalar `X_0` is genuinely independent of the entire leaf block and hence of `(S,T)`.

By (6.2)-(6.4), the active form is

`2 gamma X_0 S + 2 alpha gamma S^2 + 2 b gamma ST + d T^2`,

with effective matrix

`K=[[0,gamma,0],
    [gamma,2 alpha gamma,b gamma],
    [0,b gamma,d]]`,                                             (6.6)

and

`det K=-d gamma^2`.                                               (6.7)

Now apply the completed account04/B18 zero-pivot theorem from

`yspennstate/math-open-problems@f852e87a4002c603ac47039f22a1921061b19f2d`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

It states that a cap-one scalar genuinely independent of a two-dimensional vector of joint density cap `M`, under a nonsingular symmetric `3x3` matrix with a zero scalar pivot, has a **continuous density** satisfying

`||p||_infinity <= 6 M^(2/3)|det K|^(-1/3).`                    (6.8)

Use `M=2` from (6.5). Since in the orthonormal basis `(e_0,u,beta,z_L)` the physical block is `K direct_sum [0]`,

`|det K|=|pdet B|=|mu_1 mu_2 mu_3| >= s^3`.                     (6.9)

Therefore

`boxed: ||p_Q||_infinity
 <= 6*2^(2/3)/s
 = 9.524406311809197.../s,`                                      (6.10)

and the density is continuous.

Equation (6.10) is the required designated-partner application. It also illustrates the correct role of the LPP projection theorem: the bounded two-dimensional projection density is passed into a proved nonlinear zero-pivot receiver; it is **not** treated as a standalone theorem about an indefinite quadratic pushforward.

For comparison, the sharp Rogozin/rearrangement theorem of Juskėvicius--Lee (arXiv:1503.09190) controls maximum densities of sums of independent bounded-density variables. It can sharpen one-dimensional bank bounds, but it does not make the overlapping projections `S,T` independent and is therefore not substituted for (6.5)-(6.8).

## 7. Primary-literature scope audit

Three primary sources were checked against the owner's exact quantifiers.

1. **Livshyts--Paouris--Pivovarov (2016).** Exact match for linear orthogonal marginals of arbitrary product densities `prod f_i` with each `||f_i||_infinity<=1`; the `k`-dimensional cap is `2^(k/2)`. No Gaussianity, log-concavity, moments, compact support, connected support, iid, centering, or smoothness is assumed. It is used only in (6.5).

2. **Juskėvicius--Lee (2015).** Exact bounded-density rearrangement/small-ball results for sums of independent random vectors. This is not a theorem for a coupled indefinite quadratic pushforward, so it is not used beyond the stated comparison.

3. **Herry--Malicet--Poly (2023/2024).** Their quadratic-form regularity theory is for iid inputs whose common law is representable as a sufficiently smooth function of a Gaussian field, with additional assumptions in the main strong-density convergence regimes. Those hypotheses do not match arbitrary non-iid fragmented cap-one densities, so the paper does not close the owner target and is not imported as such.

No exact published theorem covering all owner quantifiers was found in this targeted source audit. This is not a novelty claim.

## 8. Correction audit

The proof uses none of the currently refuted interfaces:

- no independence after a general spectral rotation;
- no arbitrary-joint 3D coarea cap;
- no conditional density cap used as independence;
- no positive moment of a worst conditional projection cap;
- no law-uniform pointwise quadratic-phase decay;
- no fixed uniformly good physical minor extracted from `s_3(A)>=1`;
- no deletion or zeroing of a small nonzero quadratic coefficient;
- no fiber-supremum argument with hidden dimension loss;
- no Monte Carlo or interval-extremality claim.

The only conditioning is on ORIGINAL coordinates. The LPP projection bound is used only where the source is a genuine original-coordinate product law, and its output is passed to a completed nonlinear theorem with matching hypotheses.

## 9. Remaining implication

Theorem A now pays **every** value of the range leverage `0<=h<=1` once a qualifying four-coordinate exact-rank-three zero-diagonal principal core exists. The former `h -> 0` cofactor divergence is therefore not a local obstruction anymore.

The full conjecture is still OPEN. The global structural debt is to derive from the bare condition `s_3(A)>=1` either such a principal core or one of the already-paid product-preserving ridge, grouped-source, crossing, hub, or pivot certificates, while retaining arbitrary additional spectrum. Current corrections show that one cannot simply assert a uniformly good fixed minor.

Full-target continuity also remains OPEN. Continuity is proved here only at the endpoint `h=1` through (6.10); Theorem A as a whole establishes essential boundedness.

## 10. Source and execution record

Fresh control immediately before publication: `yspennstate/math-research-brain@12cf271a0a54404d06f9cd54cc0630bc7a0fdc68`, owner control revision `2026-09-22.15`. The live correction inbox at that head had blob `6bdbd9987a4eefeba79d53915cfe7e232263f8ec`.

Fresh math master observed immediately before publication: `yspennstate/math-open-problems@77603276a7d3d218a9db0e60a2700c845b5810dc`.

The same-hour canonical login already existed and was preserved rather than overwritten. No task, schedule, enabled/paused state, notification setting, account binding, repository visibility, remote workflow, paid API/model call, or permission was changed.

A changed-file allowlist review found only this mathematical report and the sibling finite-check record; no credentials, account secrets, unrelated personal material, or signed URLs are included. No native mathematical-brain receiver ingestion was available in this run, so status remains `WITHOUT_VERIFIED_BRAIN`.
