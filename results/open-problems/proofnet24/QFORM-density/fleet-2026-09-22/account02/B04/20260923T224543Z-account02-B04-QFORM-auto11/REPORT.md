SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-23T22:45:43Z.
attacking: the unpaid zero-pivot C1 star factor with rough residual curvature; first pay exact rank-two zero-diagonal Z-curvature by a physical bipartition and grouped product rearrangement, then compare globally optimized volume weights and ridge on the same weak-third-direction matrix.

# account02/B04 — exact rank-two rough-curvature receiver in the zero-pivot C1 branch

Programme: `QFORM-DENSITY-3EIG-20260922`.
Role: Product Fourier rearrangement / complementary constructions and source-valid counterexamples.
Status: `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / SAME-MATRIX GLOBAL VOLUME OPTIMIZATION / FULL TARGET OPEN`.
Execution context: `WITHOUT_VERIFIED_BRAIN`.
Continuity: the new receiver proves essential boundedness; continuity remains separate. The pinned e5 Fourier theorem does supply a continuous `C_0` density on the explicit epsilon-stress family below, with a deteriorating epsilon-dependent bound.

The unrestricted conjecture remains **OPEN**. All random variables below are original physical product coordinates. Coefficient-space singular vectors are used only inside deterministic Euclidean norm / exterior-product inequalities. No post-rotation independence, moments, support restriction, log-concavity, arbitrary-joint coarea, worst-fibre supremum, or law-uniform pointwise quadratic-phase decay is used.

## 0. First unpaid implication and mechanism change

Fresh slot memory showed that the immediately preceding B04 run had already proved the clean-bank top-two theorem and paid the `E_ZZ=0` zero-anchor C1 subbranch. The early calculation saved at the beginning of this invocation re-derived that theorem before the memory read; it is therefore preserved but **not counted as new progress**. In accordance with the owner instruction to change mechanism rather than repeat an unchanged attempt, the run pivoted to the first genuinely unpaid case `E_ZZ!=0`.

The first unpaid implication after the present theorem is now

`QFORM-C1-ZCURVATURE-RANKGE3-VOLUME-OR-CLEAN-SUBBANK-v1`:

> In the account03/B04 zero-anchor C1 star factorization, rank-zero residual `E_ZZ` is paid by the preceding clean-bank theorem and exact rank-two residual `E_ZZ` is paid below. For `rank(E_ZZ)>=3`, prove that either the residual curvature itself forces a target-scale completed third/fifth-volume, projected-crossing, ridge, pair, or grouped-hub certificate, or extract a physical curvature-free subbank `S subset Z` whose grouped crossing with the anchor retains target-scale top-two coefficient area. Do this before selecting/inverting a vanishing local coefficient.

This narrows the rough-curvature branch from arbitrary nonzero `E_ZZ` to rank at least three.

## 1. Fresh sources and completed inputs

Fresh owner control remained revision `2026-09-22.15`, QFORM-only, with no applicable pause or stop. The current continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` and the live correction discipline were re-read before publication.

The exact structural input is account03/B04 r41,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260923T204706Z-account03-B04-auto11-r41/REPORT.md`,

which proves the following zero-anchor factorization. Let `A_hh=0`, write `b_i=A_hi`, let `N={i:b_i!=0}`, `Z={i:b_i=0}`, and assume every physical principal triangle through `h` is singular. Then

`C=bp^T+pb^T+E`,

`E_NN=0`, `E_ii=0` for every residual physical coordinate, and

`2X_h b^T Y+Y^T C Y
 =2(b^T Y)(X_h+p^T Y)+Y^T E Y`.                                  (1.1)

The preceding account02/B04 run at commit

`dfe442ee899867f5677e5ced85a196eca922fe64`

proved `QFORM-CLEANBANK-TOPTWO-REARRANGEMENT-v1`: for disjoint original-coordinate banks `X,Y`, cap-one scalar densities, a physical crossing `M` with top singular values `s1>=s2>0`, arbitrary same-bank function `F(X)`, and no `Y-Y` quadratic term,

`Q=F(X)+2X^T M Y+l^T Y+c`

satisfies

`||p_Q||_infinity <=2 sqrt(pi) (s1 s2)^(-1/2).`                    (1.2)

Its proof conditions only original coordinates, uses the cap-two density of a two-dimensional product projection, and finishes by planar decreasing rearrangement against `|z|^(-1)`.

The required pinned Claude/e5 source was re-read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. The completed result used at an actual inequality below is Theorem D with arbitrary supported minor weights:

`||p_Q||_infinity <=6 sqrt(e) G(w)^(-1/6)`                          (1.3)

when the physical third-minor row marginals are at most `1/2`, where

`G(w)=exp(E_w log det(M_ST)^2+H(w))`.

The newest compatible designated partner account03/B04 r42 is

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260923T215155Z-account03-B04-QFORM-auto11-r42/REPORT.md`.

It proves the marginal-free E3 compiler

`||p_Q||_infinity <= C_* E_3(M)^(-1/6)`,

`C_*=8.4530212255281768747...`,                                     (1.4)

and records the sharper diffuse branch

`D(h)=3e/[sqrt(2h)(3-4h)]`                                         (1.5)

when the natural third-volume row marginals are bounded by `h`. It also proves the fixed-row incident receiver

`||p_Q||_infinity <=3*2^(4/3) J_i^(-1/6)`.                         (1.6)

For ridge comparison I use only the completed `q=1` theorem checked in account03/B04 r24: for

`K_gamma=MM^T(gamma^2 I+MM^T)^(-1)`, `theta=tr K_gamma`,

if `max_i(K_gamma)_ii<=1/2` and `theta>2`, then

`||p_Q||_infinity <= sqrt(e)/(sqrt(2)gamma) * theta/(theta-2)`.     (1.7)

## 2. Algebraic lemma: every nonzero rank-two zero-diagonal curvature is physically bipartite

### Lemma 2.1 — `QFORM-RANK2-ZERODIAG-BIPARTITION-v1`

Let `E=E^T` be a real finite matrix with

`diag(E)=0`, `rank(E)=2`, `E!=0`.

Then there is a partition of its active physical coordinates

`Z=P disjoint-union Q`

and unit vectors `a` on `P`, `c` on `Q` such that, after the corresponding physical reordering,

`boxed:
 E=[[0, lambda a c^T],
    [lambda c a^T,0]],
 lambda=||E||op>0.`                                                (2.1)

In particular both diagonal physical subblocks vanish and the cross block has rank one and singular value `lambda`.

### Proof

Because the diagonal is zero, `tr E=0`. Rank two and `E!=0` therefore imply that the two nonzero eigenvalues are `lambda,-lambda` for some `lambda>0`. With orthonormal eigenvectors `r,s`,

`E=lambda(rr^T-ss^T)`.                                             (2.2)

The zero diagonal gives `r_i^2=s_i^2` for every physical index. On active coordinates write

`s_i=epsilon_i r_i`, `epsilon_i in {+1,-1}`.                       (2.3)

Since `r perpendicular s`,

`sum_i epsilon_i r_i^2=0`.

Together with `sum_i r_i^2=1`, this yields

`sum_{epsilon_i=+1}r_i^2=sum_{epsilon_i=-1}r_i^2=1/2`.             (2.4)

Take `P={epsilon_i=+1}`, `Q={epsilon_i=-1}`, set

`a=sqrt(2) r_P`, `c=sqrt(2) r_Q`.

Then `||a||=||c||=1`. If two indices have the same sign, (2.2) gives `E_ij=0`; if they have opposite signs, it gives the cross coefficient `2lambda r_i r_j`. Hence (2.1) follows. QED.

A useful side fact is immediate: a symmetric zero-diagonal matrix can never have nonzero rank one. Thus after the rank-zero branch, rank two is the first possible rough-curvature case.

## 3. New receiver: exact rank-two rough `Z-Z` curvature

### Theorem 3.1 — `QFORM-C1-RANK2-ZCURVATURE-BIPARTITE-RECEIVER-v1`

Assume the account03/B04 r41 zero-anchor factorization (1.1), with `N` nonempty, and suppose

`rank(E_ZZ)=2`.

Put

`lambda=||E_ZZ||op>0`.

Then, after arbitrary conditioning on outside original physical coordinates and with arbitrary affine terms generated by that conditioning,

`boxed:
 ||p_Q||_infinity
 <=2 sqrt(pi) (||b||_2 lambda)^(-1/2).`                            (3.1)

No individual entry of `b`, `E_NZ`, or `E_ZZ` is selected or inverted.

### Proof

Apply Lemma 2.1 to the physical `Z` coordinates. Thus `Z=P disjoint-union Q`,

`E_PP=E_QQ=0`,
`E_QP=lambda c a^T`,                                               (3.2)

with unit `a,c`.

Use as the **curved original-coordinate bank**

`X=(Y_N,Y_Q)`

and as the **clean original-coordinate bank**

`Y=(X_h,Y_P)`.

The clean bank has no internal quadratic term: `A_hh=0`, the definition of `Z` gives no `h-P` coupling, and (3.2) gives `E_PP=0`. Every remaining term of (1.1), including `2(b^T Y_N)(p^T Y_N)`, the `N-Q` part of `E_NZ`, and arbitrary conditioned affine terms, is allowed inside the curved-bank function in (1.2).

The physical crossing from the curved bank to the clean bank is

`M=
 [[b, E_NP],
  [0, lambda c a^T]].`                                            (3.3)

Let `e_h` denote the unit coefficient vector of the physical clean coordinate `h`; regard `a` as the unit vector in the `P` columns. These are orthogonal coefficient-domain vectors. Their images are

`M e_h=(b,0)`,
`M a=(E_NP a,lambda c)`.                                          (3.4)

Their squared Euclidean area is

`||b||^2 lambda^2
 +||b||^2 ||E_NP a||^2
 -<b,E_NP a>^2
 >=||b||^2 lambda^2`.                                             (3.5)

But `s1(M)s2(M)=||wedge^2 M||op`, and the exterior operator norm is at least the area of the images of any orthonormal pair. Therefore

`boxed: s1(M)s2(M)>=||b|| lambda.`                                (3.6)

Apply the already proved clean-bank rearrangement theorem (1.2) to (3.3) and use (3.6). This gives (3.1). QED.

The point of (3.5) is that arbitrary `E_NP` can only add nonnegative transverse area after the `Q`-row component `lambda c` has already separated the two coefficient directions. No cancellation can destroy the aggregate rank-two curvature packet.

## 4. Why this is genuinely stronger than selecting one physical `z`

For a single physical `z in P`, using only the clean pair `{h,z}` would expose a two-column crossing whose second-column transverse norm can be as small as `lambda |a_z|`. If `a` is flat on `m` coordinates, this is `lambda/sqrt(m)`, producing an artificial `m^(1/4)` loss in a local two-coordinate density estimate.

Theorem 3.1 groups the entire physical `P` bank first. The vector `a` is then spent as one coefficient-space direction of norm one, so the bound depends on `lambda` itself and has **no dimension loss**. This is the same aggregate-before-inversion principle as the preceding clean-bank result, now with genuinely nonzero rough `Z-Z` curvature.

## 5. Same-matrix stress family with a weak third cross direction

Fix `m>=2` and `0<epsilon<=1`. Use disjoint original-coordinate groups

`N={n_1,n_2}`, `P={p_1,...,p_m}`, `Q={q_1,...,q_m}`,
`R={r_1,r_2}`, `S={s_1,s_2}`,

plus one physical anchor `h`. Put

`b=(sqrt(2),sqrt(2))`,
`u=v=m^(-1/2)(1,...,1)`,
`a=c=2^(-1/2)(1,1)`.                                               (5.1)

On the physical cut

`I=N union Q union R`,
`J={h} union P union S`,                                           (5.2)

define the crossing matrix

`M_epsilon=diag_block(b, 2 v u^T, epsilon a c^T)`.                 (5.3)

Equivalently the full symmetric physical matrix is

`A_epsilon=[[0,M_epsilon],[M_epsilon^T,0]]`.                       (5.4)

The three nonzero singular values of `M_epsilon` are exactly

`2,2,epsilon`,                                                     (5.5)

hence

`spec(A_epsilon)
 ={2,2,epsilon,-epsilon,-2,-2,0^(2m+1)}`.                          (5.6)

Thus **for every epsilon>0**, even as `epsilon` tends to zero, `A_epsilon` is indefinite, non-diagonal in the original product coordinates, and has four eigenvalues of modulus two. It satisfies the owner's exact target without using the weak third singular direction at all.

The first two components form the rough-curvature core

`Q_core=2X_h b^T X_N + 2 X_Q^T(2vu^T)X_P`.                         (5.7)

Relative to the zero anchor `h`, the strong `P-Q` residual block is precisely a rank-two zero-diagonal curvature with operator norm `lambda=2`, while `||b||=2`. Theorem 3.1 therefore gives

`boxed:
 ||p_Qcore||_infinity <=sqrt(pi)
 =1.772453850905516... .}`                                        (5.8)

The weak `R-S` quadratic component uses disjoint original coordinates and is independent of the core. Convolution with an arbitrary probability law cannot raise an `L^infinity` density norm, so the **full** target-valid form satisfies

`boxed:
 ||p_(X^T A_epsilon X)||_infinity <=sqrt(pi)`                       (5.9)

uniformly in both `m` and `epsilon`.

For comparison, if one selected one `p_j` before grouping the rough `P` bank, the transverse strong-curvature column has norm `2/sqrt(m)` and the corresponding local two-coordinate route deteriorates like `sqrt(pi/2) m^(1/4)`. Equation (5.9) removes that loss.

## 6. Global optimization of all admissible third-volume weights on this same cut

Every nonzero physical `3x3` minor of (5.3) chooses

- one row from `N`, one from `Q`, one from `R`;
- the unique column `h`, one column from `P`, one from `S`.

There are exactly

`8m^2`                                                             (6.1)

such minors, and every one has squared determinant

`2 epsilon^2/m^2`.                                                 (6.2)

Therefore

`Z=E_3(M_epsilon)=16 epsilon^2`.                                   (6.3)

The canonical squared-minor law is uniform. Its constrained-side physical row marginals are

`1/2` on each `N` row,
`1/m` on each `Q` row,
`1/2` on each `R` row.                                             (6.4)

Hence it is admissible for the pinned e5 Theorem D.

This law is also the **global optimum over every supported physical minor weight**. Indeed, if `w` is any probability on the supported minors, then because all determinant squares equal the common value `a_0=2epsilon^2/m^2`,

`G(w)=a_0 exp(H(w))
 <=a_0(8m^2)
 =16epsilon^2`,                                                    (6.5)

with equality only for the uniform law. Moreover every supported minor contains exactly one `N` row, so the two `N` marginals sum to one; no threshold below `1/2` can be feasible. The same statement holds for the two `R` rows. Thus the exact optimum over **all supported weights and all proved D/D' thresholds** occurs at the uniform law and `h=1/2`.

Applying the required pinned e5 theorem at the actual inequality gives

`boxed:
 ||p_(X^T A_epsilon X)||_infinity
 <=6 sqrt(e) (16epsilon^2)^(-1/6)
 =6 sqrt(e) 2^(-2/3) epsilon^(-1/3)
 =6.231775903093545... epsilon^(-1/3).}`                            (6.6)

This source-complete Fourier certificate also gives a continuous `C_0` density for every fixed `epsilon>0`. The uniform rearrangement bound (5.9) is much stronger in height but is not promoted here as a continuity theorem.

The pinned fifth-volume theorem has no currency on this natural cut because `rank(M_epsilon)=3`, hence `E_5(M_epsilon)=0`.

## 7. Actual application of the newest designated partner account03/B04 r42

The r42 marginal-free compiler (1.4), applied to the exact same physical crossing (6.3), gives

`boxed:
 ||p||_infinity
 <= C_* 2^(-2/3) epsilon^(-1/3)
 =5.325069688625554... epsilon^(-1/3).}`                            (7.1)

Because this matrix has the stronger exact marginal information (6.4), the diffuse constituent (1.5) may be used at `h=1/2`, yielding the sharper partner certificate

`boxed:
 ||p||_infinity
 <=3e 2^(-2/3) epsilon^(-1/3)
 =5.137230742833414... epsilon^(-1/3).}`                            (7.2)

For completeness, any `N` or `R` row carries incident third volume

`J_i=Z/2=8epsilon^2`,                                               (7.3)

so the r42 incident receiver (1.6) gives

`3*2^(5/6) epsilon^(-1/3)
 =5.345392308842036... epsilon^(-1/3)`.                             (7.4)

Thus the latest partner result is applied at an actual inequality. Its E3 mechanism correctly improves the pinned e5 constant but still necessarily pays the deliberately irrelevant weak third cross direction. The new rough-curvature receiver does not.

## 8. Direct ridge comparison on the identical physical cut

Let `g=gamma^2` and set

`k=4/(4+g)`,
`h_e=epsilon^2/(epsilon^2+g)`.                                     (8.1)

Then

`theta=2k+h_e`.                                                     (8.2)

The physical ridge leverages are

`k/2` on the two `N` rows,
`k/m` on the `Q` rows,
`h_e/2` on the two `R` rows.                                       (8.3)

For `m>=2` the completed `q=1` leverage gate is therefore automatically satisfied for every `gamma>0`. Whenever its trace gate `theta>2` holds,

`theta-2
 =h_e-2(1-k)
 <=h_e`.                                                           (8.4)

Consequently the completed simplified ridge certificate (1.7) satisfies

`R_epsilon(gamma)
 >=sqrt(2e)/(gamma h_e)
 =sqrt(2e)(epsilon^2+gamma^2)/(gamma epsilon^2)
 >=2sqrt(2e) epsilon^(-1).`                                        (8.5)

Thus **every valid certificate in this completed q=1 simplified ridge family** costs at least

`4.663287963194248... epsilon^(-1)`.                               (8.6)

The concrete choice

`gamma=sqrt(3/2) epsilon`                                          (8.7)

is valid for small `epsilon` and gives

`R_epsilon(gamma)
 =(2sqrt(3e)+o(1))epsilon^(-1)
 =5.711338016744285... epsilon^(-1)(1+o(1)).`                      (8.8)

No claim is made here about every later determinant-retaining or square-assisted ridge variant; (8.5) is an exact obstruction to the completed simplified q=1 certificate being compared.

## 9. Same-matrix hierarchy and interpretation

At `epsilon=10^(-6)`, for the identical physical matrix family,

`1.772454` — grouped rank-two rough-curvature rearrangement;

`513.7231` — latest partner r42 diffuse E3 certificate;

`623.1776` — globally optimized pinned e5 D/D' certificate;

`>=4.6633*10^6` — every valid simplified q=1 ridge certificate.               (9.1)

The important structural point is not the numerical gap. It is that **three large eigenvalues do not mean one must pay three cross singular directions**. A physical rank-two bipartite packet already contributes the symmetric eigenvalue pairs `+s1,+s2,-s2,-s1`; in the stress family the two strong cross directions alone give four target-scale eigenvalues. A third cross singular value may therefore be arbitrarily small while being completely irrelevant to the target-level smoothing mechanism.

The correct product-space move in this rough C1 branch is to identify the physical bipartition hidden inside exact rank-two zero-diagonal curvature and spend its aggregate singular direction together with the anchor star before any local coefficient or third volume is inverted.

## 10. Remaining gap

The new theorem closes `rank(E_ZZ)=2` exactly, including arbitrary `E_NZ` and arbitrary star term `p`. Rank zero was already closed by the preceding clean-bank theorem; nonzero rank one is impossible. The first genuinely unpaid rough-curvature regime is therefore

`rank(E_ZZ)>=3`.

A useful next proof should combine the zero diagonal, the C1 compound mass retained by the r41 star subtraction, and the higher-rank curvature spectrum to force one of two outcomes:

1. a physical curvature-free subbank whose anchor-plus-subbank crossing has target-scale top-two exterior norm, allowing the same grouped rearrangement; or
2. a target-scale completed E3/E5/projected-crossing/ridge/pair/grouped-hub certificate supplied by the curvature itself.

A small operator-norm remainder is not a small random quadratic perturbation for arbitrary unbounded cap-one laws, so perturbatively deleting the rank-at-least-three curvature remains forbidden.

## 11. Audit / provenance

The exact rank-two spectral classification, exterior-area inequality, target spectrum, minor count, global entropy optimizer, row marginals, and ridge inequalities are independently recorded in `CHECKS.md` in this run directory. The initial `EARLY_CALC.md` is preserved as required; after fresh memory showed its clean-bank result was already present in the previous B04 run, it was superseded by Sections 2-10 above rather than silently overwritten.

No scheduler/task identity, cadence, enabled/quiet state, email, notification, permission, cross-account authentication, paid call, public release, FEI work, installation, benchmark, gold data, or unrelated data was changed. Repository retrieval and writes were authenticated, but no native learned-memory receiver/ingestion was observed, so the execution label remains `WITHOUT_VERIFIED_BRAIN`.
