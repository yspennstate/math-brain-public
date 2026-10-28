SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-22T20:02:07Z.
attacking: the integrated-Fourier route's first unpaid dense/localized split, then a correction-safe repair of the localized physical-3x3 branch without the false arbitrary-joint coarea lemma.

# account03/B02 — corrected localized 3x3 theorem

Run: `20260922T200207Z-account03-B02-qform-r14`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `PROVED_SUPPORTING_SYNTHESIS / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and why this run changed mechanism

The parent target is unchanged. For every dimension, every vector of independent real coordinates whose one-dimensional densities are bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has an essentially bounded density with one universal constant, or give a valid counterexample. Continuity is a separate desired conclusion.

B02's primary assignment is the integrated Fourier estimate. I tested the current revision-15 decoupling route against the latest correction state. The exact independent-copy identity is still valid, but the straightforward conditional `L^3` implementation is not a uniform closure: account03/B01's completed `QFORM-TRANSLATED-FRESNEL-LP-v1` addendum gives the exact target-valid family `f_R(x)=1_[1,R](x)/(x log R)` for which the normalized conditional absolute-value cost grows logarithmically even for `A=I_3`. This does not refute the desired unweighted `int |phi_Q|`; it refutes that particular absolute conditional-normalization step. I found no source-valid exact-target counterexample to the unweighted `L^1` characteristic-function criterion in this run, so I do not claim one.

The live proof-first instructions say to continue bounded density when an integrated route stalls and to attack the first actual unpaid implication. A major live inconsistency is that the old owner prose calls the localized physical-3x3 branch proved using an arbitrary-joint coarea lemma, while `CURRENT_RESEARCH.md` correctly records that arbitrary-joint coarea lemma as false. The theorem below repairs that branch using only product-coordinate results that survive the correction inbox.

## 2. Dependencies actually checked and used

### 2.1 Designated partner account04/B02

Completed designated-partner theorem:

`QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`,

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`.

If a physical principal `3x3` block `B` is nonsingular and has a zero diagonal entry, then the full ambient quadratic form, with arbitrary outside terms and couplings, has a continuous density and

`||p_Q||_infinity <= 3*2^(2/3)*|det B|^(-1/3)`.              (2.1)

This partner result is applied below to an actual inequality, not merely cited.

### 2.2 Orientation-free rank-two half-Riesz theorem

Completed supporting theorem:

`QFORM-RANK2-AFFINE-HALF-RIESZ-v1`,

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For independent cap-one coordinates `Y`, every rank-two quadratic form with nonzero eigenvalues represented by an invertible symmetric `2x2` matrix `S`, and every affine term,

`sup_t E |Y^T S Y + ell^T Y + c - t|^(-1/2)
 <= 128 |det S|^(-1/4)`.                                     (2.2)

The theorem is orientation-free; in the application below the two remaining variables are themselves original independent coordinates, so no rotation of the input product law is needed.

### 2.3 Full-matrix indefinite-pair theorem

Completed supporting theorem:

`QFORM-FULL-MATRIX-INDEFINITE-PAIR-LOG-v1`,

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`,

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.

If a symmetric matrix `M` has third singular value at least `s>0` and contains an invertible indefinite original-coordinate principal pair `P`, with

`D=|det P|`, `kappa=sigma_min(P)`,

then for arbitrary affine terms and independent cap-one coordinates

`||p||_infinity
 <= 3*400^(1/3)*(D^2*kappa*s)^(-1/6)`.                       (2.3)

This theorem keeps the full remaining spectrum and all affine terms. It does not require a zero diagonal.

## 3. New theorem

### Theorem — `QFORM-LOCALIZED-PRINCIPAL-3X3-REPAIRED-v1`

Let `X=(X_1,...,X_n)` have independent real coordinates with densities `0<=f_i<=1`. Let `A` be an arbitrary real symmetric `n x n` matrix. Suppose there is a set `I` of three ORIGINAL coordinates for which the physical principal block

`B=A[I,I]`

satisfies

`sigma_min(B) >= c > 0`.                                      (3.1)

Then `Q=X^T A X` has an essentially bounded density and

`||p_Q||_infinity <= 128*2^(1/4)/c < 152.219/c`.              (3.2)

No sign condition, moment condition, smoothness, compact support, connected support, or restriction on the spectrum/couplings outside `I` is imposed.

If one diagonal entry of `B` is exactly zero, the designated partner improves (3.2) to the continuous-density bound

`||p_Q||_infinity <= 3*2^(2/3)/c < 4.763/c`.                 (3.3)

The main theorem asserts essential boundedness only. Continuity outside the exact-zero-diagonal subbranch is not claimed here.

This theorem repairs the localized physical-3x3 branch without using the refuted arbitrary-joint coarea statement.

## 4. Reduction to a three-variable quadratic-plus-linear form

Condition on every original coordinate outside `I`. Because the inputs are independent, the three selected coordinates remain independent with exactly their original cap-one densities. For almost every outside configuration, the conditional polynomial is

`q(x)=x^T B x + ell^T x + d`,                                 (4.1)

where only `ell,d` depend on the conditioning. The matrix `B` is unchanged.

It therefore suffices to prove a density bound uniform in arbitrary `ell,d` for three independent cap-one variables. Averaging the conditional densities then preserves the same essential-supremum bound.

Since every singular value of `B` is at least `c`,

`|det B| >= c^3`,                                             (4.2)

and every row has Euclidean norm at least `c`:

`sum_j B_ij^2 = ||B e_i||_2^2 >= c^2`.                       (4.3)

We split according to the physical diagonals.

## 5. Exact-zero diagonal: designated partner branch

If some `B_ii=0`, then `B` is nonsingular by (3.1), so the designated account04/B02 theorem applies directly to the full ambient conditional polynomial and, in fact, before conditioning to the full ambient form. Using (4.2),

`||p_Q||_infinity
 <= 3*2^(2/3)|det B|^(-1/3)
 <= 3*2^(2/3)c^(-1)`.                                        (5.1)

This is (3.3), and the partner theorem supplies a continuous representative. This is the required direct application of the completed designated-partner result.

For the rest of the proof assume every diagonal is nonzero.

## 6. A large physical diagonal: square pivot plus rank-two half-Riesz

Assume for some `i`

`|a|:=|B_ii| >= c/2`.                                        (6.1)

Reorder the three variables so this is the first coordinate and write

`B = [[a, r^T], [r, C]]`.

Because `a!=0`, complete the physical square in the first ORIGINAL coordinate. The conditional polynomial (4.1) takes the form

`q = a (X_i + h(Y))^2 + R(Y)`,                               (6.2)

where `Y` denotes the other two original coordinates and the quadratic matrix of `R` is the Schur complement

`S=C-r r^T/a`.                                                (6.3)

Since `B` is invertible,

`det B = a det S`,                                            (6.4)

so `S` is an invertible symmetric `2x2` matrix. All affine terms induced by completing the square are allowed by (2.2).

For fixed `Y`, the pushforward of the cap-one density of `X_i` through `x -> a(x+h(Y))^2+R(Y)` has density bounded pointwise by

`|a|^(-1/2) |s-R(Y)|^(-1/2)`.                                (6.5)

Indeed, away from the vertex there are at most two inverse branches, each contributing `f(x)/(2 sqrt(|a| |s-R|))`, and `f<=1`; the support-side indicator can only decrease the expression.

Average (6.5) over `Y` and invoke (2.2):

`||p_q||_infinity
 <= 128 |a|^(-1/2)|det S|^(-1/4)
 = 128 |a|^(-1/4)|det B|^(-1/4)`.                            (6.6)

Using (6.1) and (4.2),

`|a| |det B| >= (c/2)c^3 = c^4/2`,

hence

`||p_q||_infinity <= 128*2^(1/4)c^(-1)`.                     (6.7)

The bound is uniform in the outside conditioning.

## 7. All physical diagonals small: a quantitatively indefinite pair is forced

It remains to treat

`0 < |B_11|,|B_22|,|B_33| < c/2`.                            (7.1)

Choose any row, say row `i`. By (4.3),

`sum_(j!=i) B_ij^2
 >= c^2 - B_ii^2
 > 3c^2/4`.                                                   (7.2)

There are only two off-diagonal entries in that sum, so for some `j!=i`, with `b=B_ij`,

`|b| >= sqrt(3/8)c`.                                         (7.3)

Consider the physical principal pair

`P=[[B_ii,b],[b,B_jj]]`.                                     (7.4)

Because both diagonal magnitudes are below `c/2`,

`det P = B_ii B_jj-b^2
 <= c^2/4-3c^2/8
 = -c^2/8`.                                                   (7.5)

Thus `P` is invertible and indefinite, and

`D:=|det P| >= c^2/8`.                                       (7.6)

For its least singular value, compare `P` with `[[0,b],[b,0]]`. The latter has both singular values `|b|`, while the diagonal perturbation has operator norm at most `c/2`. Weyl's singular-value inequality gives

`kappa:=sigma_min(P)
 >= |b|-c/2
 >= (sqrt(3/8)-1/2)c`.                                      (7.7)

The three-by-three matrix `B` itself has third singular value at least `c`, so the arbitrary-rank physical-pair theorem (2.3), applied to the conditional three-variable polynomial including its arbitrary affine terms, yields

`||p_q||_infinity
 <= 3*400^(1/3)*(D^2*kappa*c)^(-1/6)`
` <= C_pair/c`,                                               (7.8)

where

`C_pair
 =3*400^(1/3)*[64/(sqrt(3/8)-1/2)]^(1/6)
 =63.6396743166...`.                                         (7.9)

In particular,

`C_pair < 128*2^(1/4)=152.218510720...`.                     (7.10)

So the pair branch is strictly below the constant already obtained in the scalar-pivot branch.

## 8. Remove the outside conditioning

For almost every outside configuration, Sections 5--7 give a conditional density bounded by

`M=128*2^(1/4)/c`,                                           (8.1)

independently of every induced affine coefficient and constant. For any Borel interval `J`,

`P(Q in J | X_(I^c)) <= M |J|`                               (8.2)

almost surely. Averaging gives

`P(Q in J) <= M |J|`.                                        (8.3)

By the Radon--Nikodym characterization, the unconditional law is absolutely continuous with an essentially bounded density satisfying (3.2).

This step never conditions on eigen-coordinates and never rotates the product law.

## 9. What was paid, and what remains open

This theorem is not the full conjecture. The bare hypothesis `s_3(A)>=1` does NOT force a physical principal 3x3 block with `sigma_min` bounded below by a universal constant. The known singleton-plus-two-banks and diffuse examples can make every fixed physical triple poorly conditioned. Therefore (3.2) repairs the localized branch but does not close the diffuse/grouped-coordinate branch.

It does, however, remove a specific logical hole in the old control prose. The previously advertised localized argument depended on the now-refuted statement that an arbitrary bounded three-dimensional joint density has a uniformly bounded quadratic pushforward. The proof above uses only original-coordinate independence and two correction-safe product-coordinate theorems, plus the designated partner's exact-zero theorem.

The first unpaid implication after this repair is genuinely structural:

> Under only `s_3(A)>=1`, aggregate original-coordinate mass before paying reciprocal fixed-minor costs, and prove that either a block satisfying (3.1) appears at a controlled scale, or one of the completed diffuse/ridge/grouped-hyperbolic certificates fires with a universal constant.

The current integrated-Fourier programme remains viable in principle, but the normalized conditional-L3 averaging step is known to incur a logarithmic loss. A successful Fourier proof must retain the unnormalized overlap kernels jointly in displacement and frequency, or use a stronger grouped-coordinate extraction.

## 10. Fourier status

No exact-target counterexample to

`sup_(A,f_i) int_R |E exp(i t X^T A X)| dt < infinity`        (10.1)

was established here, so this report does not mark (10.1) false. The current source-valid obstruction is narrower: absolute normalized conditional `L^3` decoupling produces a logarithmically divergent majorant on a valid diagonal family even though the true unsymmetrized characteristic function is uniformly `L^1` there.

On the exact-zero-diagonal branch, the designated partner additionally supplies the genuine integrated estimate

`int |phi_Q(t)|^2 dt
 <= 6*pi*2^(2/3)|det B|^(-1/3)
 <= 6*pi*2^(2/3)c^(-1)`.                                    (10.2)

This is `L^2`, not the target-wide `L^1` estimate.

## 11. Quantifier and correction audit

Used: independent original-coordinate densities bounded by one; arbitrary dimension; arbitrary outside quadratic spectrum/couplings; arbitrary affine terms induced by conditioning; all signatures of the 3x3 block; no moments or support restrictions.

Not used: post-rotation independence, Gaussian/log-concave hypotheses, compact/connected support, arbitrary-joint coarea, positive conditional projection-height moments, law-uniform pointwise Fresnel decay, fixed-good-minor extraction from the bare spectral hypothesis, or Monte Carlo evidence.

Continuity: proved only in the exact-zero-diagonal partner subbranch. The repaired localized theorem as a whole establishes essential boundedness only.
