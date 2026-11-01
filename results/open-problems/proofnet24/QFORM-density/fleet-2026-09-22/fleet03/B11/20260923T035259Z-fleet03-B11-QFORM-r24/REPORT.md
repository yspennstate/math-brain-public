SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B11, 2026-09-23T03:52:59Z.
attacking: minority-sign physical scalar completion: turn the third coordinate into an elliptic discriminant trace, then splice with the partner sign-frustrated triangle branch.

# fleet03/B11 r24 — minority-scalar elliptic discriminant compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** indefinite signatures `(2,1)` and `(1,2)`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING TARGET-LEVEL THEOREM / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** the new theorem proves existence of an essentially bounded density in its scope. A continuous representative is **not** proved here.

## 1. Exact target and correction boundary

The owner target remains the unrestricted statement: for arbitrary dimension, arbitrary independent real coordinates whose one-dimensional probability densities are bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential bound on the density of `Q=X^T A X`, or produce a genuine counterexample. The full theorem remains open.

This run attacks a remaining opposite-sign physical branch and uses only original-coordinate independence. It does **not** assume independence after spectral rotation, a law-uniform pointwise quadratic-phase decay estimate, the refuted arbitrary-joint rank-three coarea bound, a positive moment of a worst conditional projection density, a fibre-supremum bound, moments, compact support, connected support, log-concavity, Gaussianity, or perturbative deletion of small coefficients.

The preceding fleet03/B11 physical-triangle compiler is pinned at

`yspennstate/math-open-problems@a64123b3154f1f9ee0e37ef043ee591bf5b0ddbf`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260923T031429Z-fleet03-B11-QFORM-r23/REPORT.md`.

It pays all fixed-scale sign-frustrated pair-PSD physical triangles and shows that the all-majority balanced-sign chamber can deteriorate only as its normalized determinant tends to zero. The new result below closes a different branch that r23 did not isolate cleanly: a physical triple in which the **minority spectral sign is already visible on one original-coordinate diagonal**.

The completed designated partner fleet04/B11 theorem actually used again below is

`yspennstate/math-open-problems@572f6cd066c9cdef7b5a509917b4dcd79cea2fda`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260923T021512Z-fleet04-B11-sign-frustrated-triangle-r4/REPORT.md`.

For a sign-frustrated physical triple with positive diagonals `a_r`, normalized off-diagonals within `eta<1/2` of a frustrated sign pattern, and `m=min a_r`, it gives the full conditional density estimate

`||p||_infinity <= 6 sqrt(pi)/[m(1-2 eta)]`,                       (1.1)

with arbitrary affine terms and arbitrary conditioned outside coordinates. Its one-sheet ruled estimate is paid separately from its two-sheet Schur estimate, so (1.1) is a genuine full density bound in its exact scope.

## 2. New theorem: minority scalar + arbitrary dependent pair

The theorem is deliberately formulated one level more generally than the QFORM product fibre, because the proof only needs one genuinely independent scalar and a bounded two-dimensional joint density for the other variables.

### Theorem 2.1 — `QFORM-MINORITY-SCALAR-ELLIPTIC-DISCRIMINANT-v1`

Let `X` be a real random variable with probability density `f` satisfying `0<=f<=1`. Let `Y=(Y_1,Y_2)` be independent of `X` and have an arbitrary joint probability density `g` with

`||g||_infinity <= M`.                                             (2.1)

Let

`H = [[a,b^T],[b,C]]`                                               (2.2)

be a real invertible symmetric `3 x 3` matrix of inertia `(2,1)` or `(1,2)`, with `a!=0`. Assume the scalar pivot `a` carries the **minority inertia sign**. Equivalently,

`a det H > 0`.                                                      (2.3)

For arbitrary `r in R`, `d in R^2`, `c in R`, define

`Q = a X^2 + 2X(b^T Y+r) + Y^T C Y + 2 d^T Y + c`.               (2.4)

Then `Q` has an absolutely continuous law and

`boxed:
 ||p_Q||_infinity <= 2 sqrt(pi M) (a det H)^(-1/4).`                (2.5)

No independence between `Y_1` and `Y_2` is required.

The estimate is translation-uniform: the arbitrary affine parameters `r,d,c` do not enter the constant.

### Proof

Fix `y` and a target value `t`. Put

`L(y)=b^T y+r`,
`R(y)=y^T C y+2d^T y+c`.                                           (2.6)

For fixed `Y=y`, the equation `Q=t` is

`a x^2+2L(y)x+R(y)-t=0`,                                           (2.7)

with scalar discriminant

`D_t(y)=L(y)^2-a(R(y)-t)`.                                         (2.8)

On each of the two monotone branches of the quadratic map in `x`, the ordinary one-dimensional change-of-variables formula applies. At a real root `x_*`,

`|dQ/dx| = |2a x_*+2L(y)| = 2 sqrt(D_t(y))`.                       (2.9)

There are at most two roots, and `f<=1`. Hence for almost every `t`,

`p_{Q|Y=y}(t)
 <= 1_{D_t(y)>0}/sqrt(D_t(y)).`                                   (2.10)

The critical point is that the discriminant is an **elliptic quadratic form in the remaining two variables**. Define

`K := b b^T-a C`.                                                   (2.11)

Let

`S:=C-bb^T/a`                                                       (2.12)

be the Schur complement of the scalar pivot. Sylvester inertia additivity gives

`inertia(H)=inertia(a)+inertia(S)`.                                (2.13)

If `H` has inertia `(2,1)` and `a<0`, then `S>0`; if `H` has inertia `(1,2)` and `a>0`, then `S<0`. These are exactly the two cases encoded by the minority-sign condition (2.3). Since

`K=-aS`,                                                            (2.14)

both cases give

`K>0`.                                                              (2.15)

Moreover

`det H = a det S`,
`det K = (-a)^2 det S = a det H >0`.                               (2.16)

Expanding (2.8),

`D_t(y)
 = y^T K y + 2(r b-a d)^T y + r^2-a(c-t)`.                        (2.17)

Because `K>0`, complete the square:

`D_t(y)=(y-y_0)^T K(y-y_0)+beta_t`                                 (2.18)

for some deterministic `y_0` and scalar `beta_t`.

For `s>0`, the superlevel set of the reciprocal-square-root kernel is

`E_s(t):={y:0<D_t(y)<s^(-2)}`.                                    (2.19)

Under the affine change `z=K^(1/2)(y-y_0)`, this is an annulus, disk, or empty set cut out by

`0<|z|^2+beta_t<s^(-2)`.                                          (2.20)

Since the area of `{z:|z|^2<R}` is `pi R`, the width in the radial-square variable is at most `s^(-2)`. Therefore, uniformly in `t` and every affine term,

`|E_s(t)| <= pi s^(-2)/sqrt(det K)`.                              (2.21)

Average (2.10) against `g`. By layer cake, the probability normalization of `g`, and its density cap,

`p_Q(t)
 <= integral g(y) D_t(y)_+^(-1/2) dy`
` =  integral_0^infinity P_g(E_s(t)) ds`
` <= integral_0^infinity
       min{1, M pi det(K)^(-1/2) s^(-2)} ds`.                      (2.22)

For every `A>0`,

`integral_0^infinity min(1,A s^(-2)) ds = 2 sqrt(A)`.             (2.23)

Using (2.16) gives exactly

`p_Q(t)
 <= 2 sqrt(pi M) det(K)^(-1/4)
 =  2 sqrt(pi M) (a det H)^(-1/4)`.                               (2.24)

The conditional quadratic pushforward is absolutely continuous for almost every `y`; Tonelli applied to its nonnegative conditional densities shows that their mixture is a density for `Q`. This proves (2.5). QED.

## 3. Full-ambient original-coordinate corollary

The preceding theorem becomes a target-level local compiler because outside conditioning preserves the required scalar/pair independence.

### Corollary 3.1 — `QFORM-MINORITY-PHYSICAL-PIVOT-v1`

Let `A` be any real symmetric `n x n` matrix. Suppose an ORIGINAL-coordinate principal triple `S={i,j,k}` has invertible block

`H=A[S,S]`                                                         (3.1)

of inertia `(2,1)` or `(1,2)`. If for one `i in S`

`A_ii det H >0`,                                                   (3.2)

then for every independent cap-one input family,

`boxed:
 ||p_{X^T A X}||_infinity
 <= 2 sqrt(pi) [A_ii det H]^(-1/4).`                              (3.3)

All spectrum, self-couplings and cross-couplings outside `S` are arbitrary.

### Proof

Condition on every original coordinate outside `S`. The conditional polynomial in `(X_i,X_j,X_k)` has quadratic block exactly `H`; outside terms produce only an arbitrary affine term and scalar shift. The physical coordinate `X_i` remains independent of the original-coordinate pair `(X_j,X_k)`, whose joint density is

`f_j(x_j)f_k(x_k)<=1`.                                             (3.4)

Apply Theorem 2.1 with `M=1`, uniformly in the conditioning. Averaging the resulting conditional interval probabilities gives (3.3). QED.

Condition (3.2) has a clean signature meaning. For inertia `(2,1)`, `det H<0`, so (3.2) says `A_ii<0`: a negative physical diagonal visibly carries the unique minority sign. For inertia `(1,2)`, `det H>0`, so it says `A_ii>0`: a positive physical diagonal visibly carries the unique minority sign. Thus every mixed-sign physical diagonal pattern contains an immediately usable minority pivot.

## 4. Exact rank-two control and why the third direction removes the logarithm

The proof itself explains the dimension threshold without hiding the known rank-two singularity.

For a two-variable indefinite quadratic, the same scalar-root calculation leaves only **one** residual variable `y`. When its discriminant is positive definite in that one variable, a kernel superlevel has length of order

`s^(-1)`                                                         (4.1)

rather than area of order `s^(-2)`. The corresponding cap-plus-mass layer-cake majorant is

`integral_0^infinity min(1,C/s) ds=infinity`.                     (4.2)

This is exactly the logarithmic endpoint, not a weakness of the estimate. For the canonical control with independent

`X,Y ~ Uniform[-1/2,1/2]`,

`T=2XY`,                                                          (4.3)

one computes for `0<|t|<1/2`

`p_T(t)=log(1/(2|t|))`.                                           (4.4)

In rank three with a minority scalar pivot, the remaining discriminant lives in a **two-dimensional** pair. Its shell area is `O(s^(-2))`; (2.23) becomes finite. This is a direct quantitative explanation of how the third direction removes the opposite-sign rank-two logarithm in the present branch.

The cancellation is structural: after scalar completion, the Schur complement on the other two directions is definite. The third direction therefore converts the hyperbolic endpoint into an elliptic two-dimensional discriminant trace. No spectral-coordinate independence is required.

## 5. Genuine rotated target example

The theorem is not a diagonal-basis argument. Let

`O=(1/3)[[1,2,2],[2,1,-2],[-2,2,-1]]`,                            (5.1)

so `O^T O=I`, and let

`Lambda=diag(-3,1,2)`.                                             (5.2)

Then

`H=O Lambda O^T
 =[[1,-4/3,2/3],
   [-4/3,-1/3,2],
   [2/3,2,-2/3]].`                                                (5.3)

Every off-diagonal entry is nonzero, and the eigenvalues are exactly

`{-3,1,2}`.                                                       (5.4)

Thus this is a genuinely rotated target signature `(2,1)`, not diagonal in the independent coordinates. Also

`det H=-6`,
`H_33=-2/3`,
`H_33 det H=4`.                                                    (5.5)

Corollary 3.1 therefore gives, for **arbitrary** independent input densities bounded by one,

`boxed:
 ||p_{X^T H X}||_infinity <= sqrt(2 pi)=2.5066282746... .`         (5.6)

The same estimate remains valid if (5.3) occurs as a principal physical triple inside a larger ambient form with arbitrary outside coefficients, by the conditioning argument of Section 3.

Negating the example gives a genuinely rotated `(1,2)` target with the same bound.

## 6. Designated-partner application and the local sign compiler

The new theorem pays the case where the minority signature is **visible on a physical diagonal**. The designated fleet04/B11 theorem pays a complementary case where every physical diagonal has the majority sign but the near-null edge signs cannot be globally balanced.

Take an original-coordinate triple with positive diagonals `a_i,a_j,a_k`, put `m=min a_r`, assume its pair determinants are nonnegative, and write

`rho_rs=A_rs/sqrt(a_r a_s)`.                                      (6.1)

Suppose the edge-sign product is negative. If every pair defect

`d_rs=1-rho_rs^2`                                                  (6.2)

is `<1/16`, then

`|rho_rs|>sqrt(15)/4`.                                            (6.3)

With `epsilon_rs=sign(rho_rs)`, this gives the partner hypothesis

`|rho_rs-epsilon_rs|
 < eta_0:=1-sqrt(15)/4`,                                         (6.4)

and `epsilon_ij epsilon_jk epsilon_ki=-1`. Applying the **completed fleet04/B11 inequality (1.1)** at this actual parameter gives

`||p_Q||_infinity
 <= 6 sqrt(pi)/[m(1-2 eta_0)]`
` = 6 sqrt(pi)/[m(sqrt(15)/2-1)]`
` = 11.3559184890.../m`
` < 4 pi/m`.                                                      (6.5)

If instead some `d_rs>=1/16`, the definite physical-pair theorem from r23 gives `||p_Q||_infinity<=4pi/m`. Thus the completed partner result and the new minority-pivot theorem together yield the following correction-safe local sign classification:

1. **Visible minority diagonal:** if some physical diagonal has the minority inertia sign, (3.3) pays the triple with determinant currency `[|A_ii det H|]^(-1/4)`.
2. **Hidden minority, sign-frustrated majority diagonals:** after global sign reversal all diagonals are positive; the partner splice (6.5), plus the definite-pair complement, pays the entire pair-PSD sign-frustrated chamber at `4pi/m`.
3. **Hidden minority, balanced majority diagonals:** this is the only pair-PSD local chamber in which the third direction can collapse coherently toward rank one. The preceding r23 identity quantifies it by the normalized determinant `tau`; if `tau` is bounded below, it is already paid, while `tau->0` is the genuine local residual.

This is a useful narrowing: **mixed-sign physical diagonals are no longer part of the balanced near-rank-one obstruction.** The remaining difficult local geometry has all physical diagonals aligned with the majority sign and its near-null edge signs balanced.

As a second direct partner calibration, the exact frustrated matrix

`C_0=[[1,1,1],[1,1,-1],[1,-1,1]]`                                (6.6)

has eigenvalues `{2,2,-1}`. The partner theorem with `eta=0`, `m=1` gives the actual full-fibre bound

`||p||_infinity <=6 sqrt(pi)=10.6347231054...`,                   (6.7)

while the rank-two opposite-sign control remains logarithmically singular. This is the complementary “hidden minority” realization of the same three-direction smoothing phenomenon.

## 7. Relation to the newest aggregate work

The current fleet state has already narrowed an exact-rank-three residual to high-leverage/near-coloop geometries using product-preserving volume and duplicated-slice Fourier compilers. In particular, fleet03/B16 r24 proves a continuous-density exit when its duplicated five-dimensional source leverages are all at most `1/2`, and reduces failure to a near-coloop or a second almost-collinear source atom.

The theorem here should be applied **before** treating such a near-coloop as an analytic singularity whenever the corresponding original physical scalar has the minority sign: no coloop approximation is needed; the actual physical scalar/pair block is already paid by (3.3) if its determinant currency is quantitative.

What remains genuinely unpaid for B11 is therefore more specific:

`QFORM-HIDDEN-MINORITY-BALANCED-NEAR-RANKONE-AGGREGATION-v1`:

> In the no-pivot / high-leverage survivor, all useful physical diagonals may carry the majority sign while normalized near-null edge signs are balanced, and local normalized determinants can tend to zero. Aggregate that coherent defect across original-coordinate banks into a product-preserving cross-volume/ridge/duplicated-slice certificate, or show that some physical triple escapes into one of the paid branches above.

A small coefficient or small operator-norm tail cannot simply be deleted because the input laws have no support or moment bound. Arbitrary additional spectrum remains part of the full-target interface.

## 8. Verification and status

The exact checker accompanying this report verifies:

- `det(bb^T-aC)=a det H` symbolically;
- orthogonality of the rational matrix `O` in (5.1);
- the exact rotated block (5.3), determinant `-6`, eigenvalues `{-3,1,2}`, and minority currency `H_33 det H=4`;
- the bound `2 sqrt(pi) 4^(-1/4)=sqrt(2pi)`;
- determinant and eigenvalues of the partner endpoint matrix (6.6).

`QFORM-MINORITY-SCALAR-ELLIPTIC-DISCRIMINANT-v1`: **PROVED** in its stated independent-scalar / bounded-pair-density scope.

`QFORM-MINORITY-PHYSICAL-PIVOT-v1`: **PROVED TARGET-LEVEL SUBCLASS** with arbitrary outside spectrum/couplings.

Designated partner result: **APPLIED at the explicit inequality (6.5)**, not merely cited.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full universal continuous-density conclusion: **OPEN**.
