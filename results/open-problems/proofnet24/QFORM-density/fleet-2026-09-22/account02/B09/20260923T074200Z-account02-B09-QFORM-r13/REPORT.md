SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-23T07:42:00Z.
attacking: an original-coordinate hub/star with arbitrary within-bank quadratic curvature, by splitting off genuine disjoint five-volume and then exactly completing the zero-volume survivor to diagonal plus rank at most four before mixed-hub smoothing.

# account02/B09 r13 — arbitrary leaf curvature: disjoint-volume exit + exact low-rank completion

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / complementary constructions and source-valid counterexamples  
Status: **ESSENTIAL_STEP_APPLIED / NEW STRUCTURAL CLASSIFICATION + NEW ONE-HUB SMOOTHER / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains **OPEN**. This run handles a genuinely arbitrary same-side leaf matrix at an exact algebraic level: either it has positive disjoint five-volume, in which case the completed `D_5` Fourier theorem gives a direct linear interval bound, or its disjoint five-volume is zero, in which case conditioning at most eight literal leaf coordinates makes the remaining leaf block exactly `diagonal + rank <=4`. On that exact survivor a new determinant-balanced one-hub theorem applies whenever the source-coordinate star is transverse to the low-rank curvature packet.

No moment, bounded-support, connected-support, log-concavity, Gaussianity, diagonal-basis, or post-rotation independence assumption is used. No small matrix coefficient is discarded as a small random quadratic error. Every partition below is a partition of the original independent coordinates. The final probability bounds are `O(|L|)`; no square-root small-ball loss is introduced.

## 1. First unpaid implication

The preceding account02/B09 run left

`QFORM-TWOHUB-HIGHRANK-OR-LOCALIZED-LEAF-ROUTING-v1`:

> Given a quantitative hub/star resource and arbitrary within-bank curvature, either expose a paid genuinely high-rank packet, reduce the curvature to an exact determinant-balanced low-rank-plus-diagonal packet, or retain a bounded physical core without conditioning away the third target direction.

This run proves an exact version of the high-rank-versus-low-diagonal-rank split and sharpens the remaining quantitative debt to

`QFORM-STAR-DISJOINT5-STABILITY-OR-ALIGNED-THIRD-DIRECTION-v1`:

> In the surviving star geometry, if the arbitrary leaf matrix has only tiny (rather than exactly zero) disjoint five-volume, either convert that near-vanishing into a source-valid mixed-hub packet with a quantitative transverse resource, or route the resulting finite pivot/alignment to an already-paid external third direction. The tiny residual may not be deleted on arbitrary unbounded product laws.

The exact zero-disjoint-volume endpoint is paid below except for the explicitly aligned/diagonal star endpoint.

## 2. Source-pinned completed inputs actually used

### 2.1 Required newest-Claude package

I read, at the owner-pinned compatible snapshot

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

all of

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`,
`FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Two pieces are used here.

1. The completed mixed-hub Fresnel reduction (Theorem H, before its final raw-leverage Brascamp--Lieb gate): for a literal hub set and a leaf block `D+sum lambda_k v_kv_k^T`, all hub self-terms, hub/outside couplings and outside quadratic terms are retained; the hub variables produce full `|t|^{-1}` factors and the displayed same-side squares produce `|t|^{-1/2}` factors.

2. The completed unconditional `D_5` cross-block theorem: for a disjoint original-coordinate split with cross block `M`,

`Z_5=e_5(M^T M)`,

one has

`||p_Q||_infinity <= 5 sqrt(2e) Z_5^(-1/10)`,                     (2.1)

with arbitrary self blocks, outside couplings and affine terms. This is a direct density estimate, hence the same coefficient multiplies every interval length.

### 2.2 Determinant-weighted entropy Brascamp--Lieb

I also read the full proof of account02/B07

`QFORM-PLUCKER-ENTROPY-BL-v1`,

canonical source

`yspennstate/math-open-problems@32c257209b588141fb60af698f478f1d0ad20b8a`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260922T123512Z-b07-qform-minors-11/REPORT.md`.

For an `N x d` matrix `U` with orthonormal columns, Pluecker weights `w_S=det(U_S)^2`, and a basis law with coordinate marginals at most `1/2`, its Fourier integral is bounded by

`exp(D(pi||w)/2) (2pi)^d e^(d/2)`.                              (2.2)

If two iid Pluecker bases are conditioned to be disjoint and their disjointness probability is `rho>0`, then the resulting marginal has the required `<=1/2` coordinate marginals and entropy cost at most `log(1/rho)`.

### 2.3 Latest designated partner

The newest completed account03/B09 result available at the fresh check was r25,

`QFORM-RANKONE-HUBPAIR-RANDOM-SLOPE-v1`,

canonical proof

`yspennstate/math-open-problems@195447da931f086720afaa12ac902ed7d33dd32e`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T061516Z-account03-B09-QFORM-r25/REPORT.md`.

For a rank-one physical two-coordinate core `[[a,b],[b,c]]`, with `a!=0` and complementary rows `u,v`, its source-coordinate square/random-slope argument gives

`||p_Q||_infinity <=4 sqrt(2)e^(1/4)
 (|a| ||v-(b/a)u||_2)^(-1/2)`.                                 (2.3)

An actual application appears in Section 8.

## 3. New exact algebraic lemma: maximal disjoint pivot completes the remainder

Let `B` be an arbitrary real symmetric matrix indexed by a leaf bank `T`. Define its **disjoint rank**

`dr(B)=max{k: there exist S,R subset T,
                 S cap R=empty, |S|=|R|=k,
                 det B[S,R] !=0}.`                              (3.1)

For `dr(B)=0`, every off-diagonal entry of `B` is zero, so `B` is diagonal. Assume henceforth `k=dr(B)>=1`. Choose disjoint `S,R` attaining `k`, put

`P=B[S,R]`, `L=T\(S union R)`.                                  (3.2)

### Theorem `QFORM-DISJOINT-PIVOT-DIAGONAL-RANK-COMPLETION-v1`

There is a symmetric matrix `C` on `L`, of rank at most `k`, and a diagonal matrix `D` such that

`boxed: B[L,L]=D+C.`                                            (3.3)

In fact one may take

`C=B[L,R] P^{-1} B[S,L]`.                                      (3.4)

#### Proof

Fix distinct `i,j in L`. The row set `S union {i}` and column set `R union {j}` are disjoint. By maximality of `k`, the corresponding `(k+1)x(k+1)` determinant vanishes. Schur expansion around the invertible pivot `P` gives

`0=det [[P,B[S,j]],[B[i,R],B[i,j]]]
  =det(P) [B[i,j]-B[i,R]P^{-1}B[S,j]].`                         (3.5)

Hence for every `i!=j` in `L`,

`B[i,j]=C[i,j]`.                                                (3.6)

Because `B[L,L]` is symmetric, (3.6) implies `C[i,j]=C[j,i]` off the diagonal; diagonal entries are tautologically symmetric, so `C=C^T`. Formula (3.4) gives `rank(C)<=k`. Therefore `D=B[L,L]-C` has zero off-diagonal entries and is diagonal. QED.

This is an exact original-coordinate statement. The pivot coordinates `S union R` are not rotated; if they are conditioned later, they create only affine terms on `L`.

## 4. Arbitrary curvature: disjoint five-volume either pays or reduces to rank <=4

Define the intrinsic disjoint five-volume

`Omega_5(B)=
 sum_{S cap R=empty, |S|=|R|=5} det(B[S,R])^2`.                 (4.1)

### Theorem `QFORM-LEAF-DISJOINT5-EXTRACTION-v1`

Consider any full quadratic form with a leaf bank `T` having exact same-side principal block `B=A[T,T]`. All other coordinates may include literal hubs, arbitrary hub self-curvature, arbitrary star coefficients, arbitrary outside quadratic terms and arbitrary affine terms.

If `Omega_5(B)>0`, then

`boxed:
 ||p_Q||_infinity <=10 sqrt(2e) Omega_5(B)^(-1/10).`            (4.2)

Consequently

`boxed:
 P{Q in I} <=10 sqrt(2e) Omega_5(B)^(-1/10) |I|`               (4.3)

for every interval `I`.

If `Omega_5(B)=0`, then after conditioning at most eight literal coordinates from `T`, the remaining leaf principal block is exactly diagonal plus symmetric rank at most four.

#### Proof of the positive-volume branch

Randomly assign every coordinate of `T` independently to `I` or `J` with probability `1/2`. For the cross block `M=B[I,J]`, Cauchy--Binet gives

`e_5(M^T M)
 =sum_{S subset I,R subset J, |S|=|R|=5} det(B[S,R])^2.`       (4.4)

For each ordered disjoint pair `(S,R)` in (4.1), the event `S subset I, R subset J` has probability `2^{-10}`. Therefore

`E e_5(M^TM)=2^{-10} Omega_5(B)`.                              (4.5)

Some deterministic original-coordinate bipartition has

`Z_5=e_5(M^TM)>=2^{-10}Omega_5(B)`.                            (4.6)

Apply the completed `D_5` theorem (2.1) to that split, conditioning every other original coordinate. Since `(2^{-10})^{-1/10}=2`, (4.2) follows. Averaging over the conditioned variables preserves the same density bound. QED.

If `Omega_5(B)=0`, no nonzero disjoint `5x5` minor exists. A nonzero disjoint `k x k` minor with `k>5` would contain a nonzero `5x5` subminor, so `dr(B)<=4`. Apply Theorem 3 and condition the at most `2dr(B)<=8` pivot coordinates. QED.

The `D_5` proof does use a characteristic-function differencing step, but it ends in an integrable Fourier envelope and the density estimate (2.1). It does **not** convert a linear small-ball estimate into a square root of interval length.

## 5. New analytic theorem: determinant-balanced one-hub smoothing

We now pay the exact low-disjoint-rank branch when the source-coordinate star is transverse to the completed low-rank curvature.

Split the independent original coordinates as one literal hub `{h}`, active leaves `L`, and an arbitrary conditioned outside bank `J`. Assume

`A[L,L]=D+sum_(a=1)^r lambda_a v_a v_a^T`,                     (5.1)

where `D` is diagonal, `r>=1`, and every `lambda_a!=0`. Put the actual hub-to-leaf star

`c=A[L,h]`,                                                     (5.2)

and

`W=[v_1,...,v_r,c]`, `G=W^T W`, `d=r+1`.                       (5.3)

Assume `G>0`. Whiten only this deterministic coefficient frame,

`U=W G^{-1/2}`,                                                 (5.4)

so `U^TU=I_d`. Let `w_S=det(U_S)^2` be the Pluecker basis law and let

`rho=P(S cap R=empty)`                                         (5.5)

for two iid bases `S,R~w`.

### Theorem `QFORM-ONEHUB-PLUCKER-SMOOTHING-v1`

If `rho>0`, then the full quadratic form has a continuous density and

`boxed:
 ||p_Q||_infinity
 <= ((r+2)/r) exp((r+1)/(r+2))
    [rho det(G) prod_a |lambda_a|]^(-1/(r+2)).`                (5.6)

The same right side times `|I|` bounds every interval probability. The hub diagonal entry, all hub/outside couplings, the entire outside quadratic block, and all affine terms are arbitrary.

#### Proof

Condition only on the original outside coordinates `X_J`. For a fixed hub value `x_h`, all hub-only quadratic and affine terms have modulus one in the characteristic function. Taking absolute values after the leaf expectation and substituting the linear star frequency

`y=2t x_h`                                                     (5.7)

gives the exact hub Jacobian `(2|t|)^{-1}` because the physical hub density is at most one.

Fresnel-linearise the `r` displayed squares in (5.1). This contributes

`prod_a (4pi |t lambda_a|)^(-1/2)`                             (5.8)

and leaves a `d=r+1` dimensional Fourier integral over the augmented rows of `W`; the diagonal `D` and every conditioning-generated linear term are one-coordinate phases.

After `z'=G^(1/2)z`, apply the determinant-entropy theorem (2.2) to the first marginal of two iid Pluecker bases conditioned to be disjoint. Its coordinate marginals are at most `1/2` and its entropy cost is at most `log(1/rho)`. Thus the residual Fourier integral is at most

`det(G)^(-1/2)(2pi)^d e^(d/2) rho^(-1/2)`.                    (5.9)

The constants combine exactly:

`2^(-1)(4pi)^(-r/2)(2pi)^(r+1)=pi^((r+2)/2).`                 (5.10)

Writing `alpha=(r+2)/2>1`,

`|phi_Q(t)| <= min(1,A |t|^(-alpha))`,                         (5.11)

with

`A=pi^alpha e^((r+1)/2)
   [rho det(G) prod_a|lambda_a|]^(-1/2).`                      (5.12)

Hence

`int_R |phi_Q(t)|dt
 <=2 alpha/(alpha-1) A^(1/alpha)`.                             (5.13)

Fourier inversion gives (5.6). The same uniform envelope survives the conditioning average, so the unconditional characteristic function is in `L^1`; this also gives continuity on this branch. QED.

If the `v_a` are chosen as orthonormal eigenvectors of the completed symmetric rank-`r` matrix `C`, then

`det(G)=dist(c,range(C))^2`,                                   (5.14)

and

`det(G) prod_a|lambda_a|
 = |pdet(C)| dist(c,range(C))^2`.                              (5.15)

Thus the resource is an intrinsic curvature-times-transverse-star quantity; no random vector is spectrally rotated.

## 6. Exact arbitrary-curvature routing for a literal source-coordinate star

Combine Sections 3--5 for a one-hub decomposition

`Q=aX_h^2+2X_h<c,X_T>+X_T^T B X_T + outside/affine terms`.      (6.1)

There are now two exact algebraic routes.

1. **Positive disjoint five-volume.** If `Omega_5(B)>0`, Theorem 4 gives (4.2), retaining the entire arbitrary `B` and the star.

2. **Zero disjoint five-volume.** If `Omega_5(B)=0`, choose a maximal disjoint pivot. After conditioning at most eight leaf coordinates, the surviving active block is

   `B[L,L]=D+C`, `rank(C)=r<=4`.                               (6.2)

   If `r>=1`, `dist(c_L,range(C))>0`, and the augmented Pluecker disjointness mass `rho>0`, Theorem 5 gives

`||p_Q||_infinity
 <=((r+2)/r)e^((r+1)/(r+2))
 [rho |pdet(C)| dist(c_L,range(C))^2]^(-1/(r+2)).`             (6.3)

The exact survivors are now explicit rather than hidden inside the phrase “arbitrary curvature”: `Omega_5` may be positive but quantitatively tiny; at the exact-zero endpoint the completed rank can be zero, the star can lie in `range(C)`, or the determinant-weighted coefficient frame can have `rho=0`. A universal proof must spend a genuine external third direction in those aligned/localized cases.

## 7. Required e5 result applied to a real target-valid high-rank star

Let `Y,Z in R^5` be two disjoint original-coordinate leaf banks and define the dense real orthogonal Householder matrix

`M=I_5-(2/5) 11^T`.                                           (7.1)

Every entry is nonzero: diagonal entries are `3/5`, off-diagonal entries are `-2/5`, and

`M^TM=I_5`, `det M=-1`.                                       (7.2)

For an additional literal hub `X_h`, take **arbitrary** hub self coefficient `a` and arbitrary star vectors `c,d`, and consider

`F=aX_h^2+2X_h(<c,Y>+<d,Z>)+2Y^T M Z`.                        (7.3)

The `10x10` leaf principal block is

`B=[[0,M],[M^T,0]]`,                                           (7.4)

whose spectrum is five `+1` and five `-1`. By principal interlacing, the full `11x11` matrix in (7.3) has at least five eigenvalues `>=1` and at least five eigenvalues `<=-1`, for **every** `a,c,d`; in particular it satisfies the owner target.

Apply the completed e5 `D_5` theorem to the literal `Y|Z` split. Here

`Z_5=e_5(M^TM)=1`,                                             (7.5)

so

`boxed: ||p_F||_infinity <=5sqrt(2e)<11.659`,                  (7.6)

and

`boxed: P{F in I} <=5sqrt(2e)|I|.`                             (7.7)

This is an actual source-coordinate hub/star with a dense same-side leaf operator. The hub may couple densely to both leaf halves, yet no star variable is conditioned away before the high-rank leaf smoother is spent.

## 8. Mixed-hub smoothing applied to a real target-valid dense star

The new one-hub theorem removes the raw `max leverage <=1/2` gate from the e5 Theorem H mechanism when the determinant-weighted disjoint-basis mass remains positive.

Take one hub `X_h` and a leaf bank split only for the purpose of defining two deterministic orthogonal coefficient vectors. Let `v` have squared coordinate weights

`0.6, 0.004, ..., 0.004`                                      (8.1)

with one `0.6` entry and one hundred `0.004` entries, and let `c` be flat on a disjoint set of 256 leaf coordinates. Thus `||v||=||c||=1`, `<v,c>=0`. Consider

`G_*=2X_h<c,Y>+<v,Y>^2`.                                      (8.2)

On `span{e_h,c,v}`, its matrix is

`[[0,1,0],[1,0,0],[0,0,1]]`,                                  (8.3)

so its active spectrum is exactly `{-1,1,1}`: this is target-valid. The dense same-side square `vv^T` is retained on the 101-coordinate curvature support.

For the augmented two-frame `[v,c]`, `G=I_2`, but the largest raw leverage is `0.6>1/2`, so the final leverage-gated statement of e5 Theorem H does not apply directly. Its Pluecker basis law chooses one `v`-support row and one `c`-support row. Two iid bases are disjoint with probability

`rho=(1-[0.6^2+100(0.004)^2])(1-1/256)
    =0.63590625`.                                               (8.4)

Theorem 5 with `r=1`, `lambda=1` gives

`boxed:
 ||p_(G_*)||_infinity
 <=3e^(2/3) rho^(-1/3)
 =6.7949543725...<6.795.`                                      (8.5)

Again every interval has probability at most `6.795|I|`. This is the requested mixed-hub smoothing on a literal source-coordinate star while keeping a dense same-side coupling packet; no projected coordinates are declared independent.

## 9. Latest partner result applied to an actual target inequality

Let `z,w` be orthonormal coefficient vectors on an original-coordinate bank `K`, disjoint from two physical coordinates `X,Y`, and set

`Q_*=X^2+2Y<z,Z_K>+<w,Z_K>^2`.                                (9.1)

For the physical pair `(X,Y)`, the core is `diag(1,0)`, so in the partner theorem `a=1,b=0,u=0,v=z`; hence the Schur-transverse slope norm is one. Account03/B09 r25 therefore gives

`boxed:
 ||p_(Q_*)||_infinity <=4sqrt(2)e^(1/4)<7.264.`                (9.2)

The compressed spectrum on `{X,Y,<z,Z>,<w,Z>}` is `{1,1,-1,1}`, so this is itself target-valid. The dense square `<w,Z>^2` remains inside the arbitrary complementary quadratic environment of the partner proof.

## 10. Deterministic checks and regression boundaries

For the explicit Householder example, direct finite-dimensional algebra gives

`||M^TM-I||_F <4e-16`, `det M=-1`,

and the leaf spectrum exactly `{-1 x5, +1 x5}`. A random dense hub extension used only as a sanity check retained ten eigenvalues of modulus at least one, as interlacing already proves symbolically. For the mixed-hub example, (8.4) and (8.5) evaluate to

`rho=0.63590625`, `bound=6.794954372549667`,                    (10.1)

and the compressed spectrum in (8.3) is `{-1,1,1}`.

Two boundaries are important.

* High ordinary matrix rank alone is not the relevant high-rank payment: an arbitrary diagonal leaf matrix can have full rank while `Omega_5=0`. That case is harmless only because diagonal curvature is a one-coordinate phase in the mixed-hub argument; it does not justify a generic “rank>=5 implies D_5” step.
* If `Omega_5` is merely small and nonzero, equations (3.5) give small off-diagonal completion errors relative to a chosen pivot determinant, but those errors cannot be dropped. On unbounded product inputs, a matrix-small quadratic tail need not be a uniformly small random variable. The needed next result is a stability/routing theorem, not a perturbative deletion.

## 11. What changed and what remains

Before this run, “arbitrary within-bank curvature” was an undifferentiated survivor. It is now separated by an exact source-coordinate invariant:

* `Omega_5(B)` quantitatively large -> unconditional `D_5` density exit;
* `Omega_5(B)=0` -> after at most eight conditioned leaf coordinates, exact `diagonal + rank<=4` curvature;
* on that exact low-disjoint-rank branch, a transverse determinant-balanced one-hub frame has the explicit density bound (6.3).

The full conjecture is still not closed because the three-large-eigenvalue condition has not yet been shown to force a universal lower bound on either `Omega_5` or the completed mixed-frame resource. The next mathematically precise debt is `QFORM-STAR-DISJOINT5-STABILITY-OR-ALIGNED-THIRD-DIRECTION-v1` from Section 1.

No law-uniform pointwise Fresnel decay, arbitrary-joint coarea, post-rotation independence, worst conditional projection supremum, fixed-good-minor assertion, or small-random-error step is used. Full-target continuity remains separate and OPEN, although the branches proved by the `L^1` Fourier arguments above are continuous.
