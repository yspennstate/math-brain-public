SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B01, 2026-09-24T00:33:08Z.
attacking: the global latent-rank-one exact-W2 survivor; force a strong ORIGINAL indefinite physical pair in the low-diagonal chamber, and combine it with the newest account03/B01 scalar-pivot closure in the complementary high-diagonal chamber.

# account02/B01 — global latent-rank-one survivor paid

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T003308Z-account02-B01-QFORM-auto11-latentrank1`  
Role: oscillatory replacement / complementary constructions and source-valid obstructions  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING TARGET-LEVEL THEOREM / GLOBAL LATENT-RANK-ONE BRANCH PAID / FULL QFORM OPEN**

The unrestricted owner target remains OPEN. No Gaussianity, log-concavity, moments, support regularity, spectral-coordinate independence, or post-rotation product assumption is used. The phase-aligned-density obstruction to law-uniform scalar quadratic-phase decay is preserved; the proof below uses only literal ORIGINAL-coordinate pivots and an already proved arbitrary-rank physical-pair averaged-frequency/small-ball receiver.

## 1. Fresh source/control boundary


The required compatible decoupling/Brascamp--Lieb source was read at the exact pin

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

The arbitrary-rank physical indefinite-pair theorem used below is source-pinned at

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.

It proves that if `s_3(A)>=s>0` and an ORIGINAL physical `2x2` principal block `B` is invertible indefinite, with

`D_B=|det B|`, `kappa=sigma_min(B)`,

then for every cap-one product input and arbitrary affine terms,

`||p_Q||_infinity <= C_pair (D_B^2 kappa s)^(-1/6)`,            (1.1)

where

`C_pair = 3*400^(1/3) = 22.1041889918423... .`                  (1.2)

The newest designated partner account03/B01 report consumed in this run is

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T233049Z-auto11/REPORT.md`

on the current compatible open-problems state. Its completed theorem `QFORM-SCALARPIVOT-COMPOUND-OPERATOR-CLOSURE-v1` gives, whenever `s_3(A)>=1` and one ORIGINAL physical diagonal `a=A_ii` is nonzero,

`||p_Q||_infinity < 137 |a|^(-1/2).`                            (1.3)

This report applies (1.3) at a quantitative threshold rather than merely citing it.

## 2. First unpaid implication attacked: global latent rank one

The preceding B01 exact-`W_2` work showed that one surviving exact-zero-overlap geometry is a diagonal-plus-global-rank-one coefficient matrix. We now pay that entire structural class, without assuming exact `W_2` in the theorem itself.

### Theorem 2.1 — `QFORM-LATENT-RANK1-GLOBAL-COMPILER-v1`

Let `A` be real symmetric with

`s_3(A)>=1`,                                                     (2.1)

and suppose

`A = D + R`,                                                     (2.2)

where `D` is diagonal and `rank R<=1`. Then for every independent real input with densities bounded by one, `Q=X^T A X` has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity < C_* < 195.01`,                       (2.3)

where

`C_* = sqrt( 2*137^2 + C_pair^2 )
     = 195.004090139122... .`                                   (2.4)

No continuity claim is made.

#### Proof

If `R=0`, then `A=D`; since `s_3(A)>=1`, at least one physical diagonal has modulus at least one, so the partner scalar-pivot bound (1.3) already applies. Hence assume `rank R=1` and write

`R = sigma u u^T`, `sigma!=0`.                                  (2.5)

Fix a threshold `0<epsilon<1/2`.

**High-diagonal branch.** If

`max_i |A_ii| >= epsilon`,                                      (2.6)

choose `i` attaining this threshold. The newest account03/B01 theorem (1.3) gives the actual inequality

`||p_Q||_infinity < 137 epsilon^(-1/2).`                        (2.7)

**Low-diagonal branch.** Assume instead

`max_i |A_ii| < epsilon`.                                       (2.8)

Because `rank R<=1`, the singular-value rank-one perturbation inequality gives

`s_3(D+R) <= s_2(D)`.                                           (2.9)

Together with (2.1), this implies `s_2(D)>=1`. Therefore there are distinct ORIGINAL coordinates `i,j` such that

`|d_i|>=1`, `|d_j|>=1`.                                        (2.10)

For each of them,

`|sigma| u_i^2 = |A_ii-d_i| >= |d_i|-|A_ii| > 1-epsilon`,      (2.11)

and similarly for `j`. Thus the physical off-diagonal entry obeys

`|A_ij| = |sigma u_i u_j|
        = sqrt((|sigma|u_i^2)(|sigma|u_j^2))
        > 1-epsilon`.                                           (2.12)

Consider the ORIGINAL physical principal pair

`B = [[A_ii,A_ij],[A_ij,A_jj]].`                                (2.13)

Its determinant satisfies

`det B = A_ii A_jj - A_ij^2
       < epsilon^2-(1-epsilon)^2
       = -(1-2epsilon) <0`.                                     (2.14)

Hence `B` is invertible indefinite and

`D_B=|det B| > 1-2epsilon`.                                    (2.15)

Moreover compare `B` with `[[0,A_ij],[A_ij,0]]`. Their difference is diagonal of operator norm `<epsilon`, so singular-value Lipschitz continuity gives

`kappa=sigma_min(B) > |A_ij|-epsilon > 1-2epsilon`.             (2.16)

Apply the source-pinned arbitrary-rank pair theorem (1.1) with `s=1`:

`||p_Q||_infinity
 <= C_pair (D_B^2 kappa)^(-1/6)
 <  C_pair (1-2epsilon)^(-1/2).`                                (2.17)

Combining (2.7) and (2.17), optimize the worst branch. Equality of the two envelopes occurs at

`epsilon_* = 137^2/(2*137^2+C_pair^2)
            =0.4935756124261177... <1/2`.                       (2.18)

At this value both bounds equal

`sqrt(2*137^2+C_pair^2)=195.004090139122...`,                   (2.19)

which proves (2.3). QED.

The proof is entirely in the physical coordinate system. In particular, the rank-one representation (2.5) is only deterministic matrix algebra; no random variable is rotated and no independence is claimed for latent coordinates.

## 3. Required 20260922T211500Z source applied to a concrete obstruction

The newest required decoupling/Brascamp--Lieb report supplies rank-three and rank-five cross-volume receivers in terms of

`Z_3=e_3(M^T M)`, `Z_5=e_5(M^T M)`

for ORIGINAL-coordinate cross blocks `M=A[I,J]`.

In the entire class (2.2), every disjoint physical cut satisfies

`A[I,J] = R[I,J] = sigma u_I u_J^T`,                            (3.1)

because the diagonal matrix contributes nothing across a cut. Therefore

`rank A[I,J] <=1`,                                              (3.2)

and concretely

`boxed: Z_3=Z_5=0 on every ORIGINAL-coordinate cut.`            (3.3)

Thus the required source's Theorem D/D' and D5 volume currencies are identically zero throughout this survivor. This is a concrete obstruction, not a summary: the branch cannot be paid by rank-three/five cross-volume regardless of how one partitions the original coordinates. The physical-pair mechanism above is therefore genuinely complementary to the newest averaged-frequency volume route.

A minimal target example is

`A_0 = I_3 - 1 1^T
    = [[0,-1,-1],[-1,0,-1],[-1,-1,0]].`                         (3.4)

Its eigenvalues are `{1,1,-2}`, so it exactly meets the owner target, every physical diagonal vanishes, and every cross cut has rank one and hence `Z_3=Z_5=0`. Yet every physical pair is the hyperbolic block `[[0,-1],[-1,0]]`, so (1.1) gives

`||p_{X^T A_0 X}||_infinity <= C_pair <22.105`.                 (3.5)

This explicit example demonstrates the mechanism switch: volume smoothing is structurally unavailable, while an ORIGINAL indefinite pair pays the law uniformly.

## 4. Consequence for the exact-W2 finite-leak programme

The earlier B01 exact-`W_2` identity showed that `W_2=0` for an invertible physical pair forces a diagonal-plus-rank-at-most-two global structure, and the subsequent latent-wedge theorem reduced the exact-rank-one crossing zero-wedge survivor to several finite-leak alternatives. Theorem 2.1 eliminates one of those alternatives completely:

`global latent rank <=1  =>  ||p_Q||_infinity <195.01`.         (4.1)

So no further `W_2`, Schur, near-null, or tiny-determinant payment is needed in the global latent-rank-one state.

The remaining first unpaid implication is now

`QFORM-W2ZERO-RANK2-FINITELEAK-ROUTING-v1`:

> In the diagonal-plus-rank-two exact-`W_2` survivor, after the nonzero transverse-wedge recut is paid and the global latent-rank-one alternative is removed by Theorem 2.1, route the genuinely rank-two zero-wedge states. These are the states in which both relevant bank restrictions are latent rank one, or an invertible latent rank-two representation has its transverse direction supported on at most two literal physical coordinates. The next mechanism should exploit that finite physical support through an ORIGINAL low-dimensional pair/three-coordinate receiver, without rotating the product law or deleting small same-bank curvature.

This is strictly narrower than the predecessor unpaid state.

## 5. Pointwise-decay correction preserved

Nothing above asserts a law-uniform pointwise estimate of the form

`|E exp(it X^2)| <= C |t|^-1/2`.

The phase-aligned-density counterexample remains valid: for a fixed nonzero frequency one can choose a cap-one probability density supported on sufficiently many phase-aligned fragments so that the scalar quadratic characteristic function is arbitrarily close to unit modulus at that frequency. The proof here instead consumes the already completed physical-pair theorem, whose analytic engine is decoupling/regularized-determinant small-ball control and logarithmic averaging.

## 6. Status and telemetry

Full QFORM is **OPEN / NOT PROVED / NOT DISPROVED**. The new result is a source-valid supporting theorem for one structural branch. There are not two independent end-to-end reviews of the owner target.

Model self-report: `GPT-5.6 Sol`. Configured/self-reported thinking level: `UNKNOWN`. Provider reasoning-token count and provider thinking time: `null/not exposed`. Authenticated repository retrieval was used. No usable native receiver-memory state entered this proof, so execution remains `WITHOUT_VERIFIED_BRAIN`. Elapsed execution time is recorded separately in the finish artifact and includes tool/repository/validation/publication overhead; it is not pure thinking.
