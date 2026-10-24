# The adapted-hub statement: a Gaussian theorem and an obstruction to cap-only proofs

Date: 2026-09-23. These are mathematical deductions for the conditional-hub research branch. No claim below settles SP for arbitrary independent bounded-density inputs.

## 1. Statement studied

Let `L = w·X`, `V = v·X`, `P = p·X`, where `w,v,p` are orthonormal. In the full proposed statement, the coordinates of `X` are independent with densities at most one and each coordinate satisfies `w_i^2+v_i^2+p_i^2 <= 1/2`. Given `X`, let `Y` have conditional density `g(y|P)`, where `0 <= g <= 1` and `integral g(y|P) dy = 1`. The proposed adapted-hub estimate (SP) is a universal upper bound on the density of

`Q = 2 Y L + V^2`.

The conditioning restriction is essential: `Y` may see `P`, but it may not see arbitrary additional information about `L,V`.

## 2. Rigorous positive result: SP holds with constant 3 for Gaussian-smoothed inputs

**Theorem.** Suppose `X = Z + G`, where `Z` is an arbitrary random vector and `G` is an independent centered Gaussian vector with covariance `D >= (1/(2 pi)) I`. No independence assumption on the coordinates of `Z` is required. Assume the conditional distribution of `Y` given `(Z,G)` is `g(y|p·(Z+G)) dy`, with `0 <= g <= 1` and unit integral in `y`. Then, for every orthonormal triple `w,v,p`,

`||p_{2 Y L + V^2}||_infinity <= 3`.

The coordinate spread condition is unnecessary for this theorem. In particular it applies to independent Gaussian coordinate laws with densities at most one. It also applies when independent inputs have independent Gaussian summands of variance at least `1/(2 pi)`.

**Extension.** The same bound holds for

`Q = 2 Y L + lambda V^2 + B(Y,P) V + C(Y,P)`

when `|lambda|>=1` and `B,C` are arbitrary finite real measurable functions. In particular, an arbitrary hub diagonal `a(P)Y^2` is allowed. Moreover, `P` may be replaced throughout by the full orthogonal projection `U` of `X` onto the orthogonal complement of `span(w,v)`, so the adapted hub may observe all these orthogonal directions.

For this extension, condition on `(Z,U)` and use the same Schur-complement bound for the residual two-dimensional Gaussian covariance. The extra terms change only a linear Gaussian phase and a scalar phase once `Y,Z,U` are fixed. The determinant factor becomes `(1+4 lambda^2 c^2 t^2)^(-1/4)`, bounded by the factor used below.

### Proof

Condition on `Z=z` and `P=p0`. The conditional law of `(L,V)` is Gaussian. Its covariance matrix `K` satisfies

`K >= c I_2`, where `c=1/(2 pi)`.

To see this, the covariance of `(L,V,P)` before conditioning is `C = R D R^T >= c I_3`, where the rows of `R` are `w,v,p`. The conditional covariance is the Schur complement of the `P` entry. For each `a in R^2`,

`a^T K a = inf_b (a,b)^T C (a,b) >= c |a|^2`.

Write the conditional Gaussian regression as

`L = mu + alpha V + W`,

where `W` is independent of `V` and has variance `r >= c`, while `V` has variance `q >= c`. The lower bound on `r` follows again from the Schur-complement inequality for `K >= c I_2`. Conditional on `(z,p0)`, the variable `Y` is independent of the Gaussian residual variables because its conditional kernel is the fixed function `g(y|p0)`.

For fixed `Y=y`, the characteristic function of `2yL+V^2` therefore satisfies

`|phi_y(t)| <= exp(-2 c y^2 t^2) (1 + 4 c^2 t^2)^(-1/4)`.

Indeed the independent Gaussian `W` gives the exponential factor. Completing the square in the Gaussian integral for `V^2+2 alpha y V` gives the displayed determinant factor; the remaining modulus is at most one, for arbitrary means and regression coefficients.

Integrating in `y` and using both `g<=1` and its unit mass gives

`|phi_Q(t)| <= (1 + t^2/pi^2)^(-1/4) min(1, pi/|t|)`.

The right side is integrable. Fourier inversion and `u=t/pi` yield

`||p_Q||_infinity <= integral_0^infinity (1+u^2)^(-1/4) min(1,1/u) du`.

On `0<u<1`, the integrand is at most one; on `u>=1`, it is at most `u^(-3/2)`. Consequently the integral is at most `1+2=3`. This bound is uniform in the conditioned variables, so averaging completes the proof.

### Smaller Gaussian smoothing scales

The same proof gives, when `D >= sigma^2 I` and `a=sqrt(2 pi) sigma <= 1`,

`||p_Q||_infinity <= (3 + log(1/a))/a`.

Thus smoothing gives an explicit bound of order `sigma^(-1) log(1/sigma)`. This diverges when the smoothing scale vanishes and does not resolve the rough-law endpoint.

## 3. Rigorous negative result: all pointwise joint and coordinate marginal caps are insufficient

**Proposition.** For every sufficiently large integer `m`, there exists a joint law `(L,V,P)` such that its three-dimensional density and every coordinate marginal density are at most one, but there is a conditional hub density `g(y|P)<=1` of unit mass for which

`p_{2 Y L + V^2}(0) >= (1/4) log m - O(1)`.

This is **not** an admissible counterexample to SP: the constructed joint law has not been represented as orthogonal linear projections of independent cap-one coordinate laws. It proves that a proof which retains only pointwise Brascamp-Lieb projection-density caps cannot establish SP.

### Construction and proof

Put `delta=1/m`. Take `L` uniform on `[0,1]` and `V` independently uniform on `[1,2]`. Partition this rectangle into `m^2` squares

`C_jk = [j delta,(j+1)delta] x [1+k delta,1+(k+1)delta]`,

for `0<=j,k<m`. Assign every square a distinct unit interval `I_jk` on the `P` axis, with the intervals pairwise disjoint. Conditional on `(L,V)` lying in `C_jk`, take `P` uniform on `I_jk`.

Equivalently, the joint density is exactly one on the union of the boxes `C_jk x I_jk` and zero elsewhere. The total volume is `m^2 delta^2=1`. The `(L,V)` marginal density is one on the rectangle; the `(L,P)` and `(V,P)` marginal densities are `delta` on their supports; the `P` marginal density is `delta^2`; and the `L,V` marginal densities are each one. Thus all the asserted density caps hold.

Let `(ell_j,v_k)` be the center of `C_jk`. For `P in I_jk`, choose `Y` uniform on the unit interval centered at

`y_jk = -v_k^2/(2 ell_j)`.

This is allowed to depend only on `P`, and its conditional density is at most one.

For cells whose lower `L` endpoint is at least `8 sqrt(delta)`, all roots

`y_*(l,v) = -v^2/(2l)`

belong to that unit hub interval. For example the mean-value theorem, with `v<=2`, bounds the displacement from the cell-center root by

`delta/l_min + delta/l_min^2 <= sqrt(delta)/8 + 1/64 < 1/2`.

For these cells the coarea formula in `Y` gives the exact contribution `1/(2l)` after integrating in `P`. If `b_m` is the first grid boundary at least `8 sqrt(delta)`, then `b_m <= 9 sqrt(delta)` for large `m`. Hence

`p_Q(0) >= integral_{b_m}^1 integral_1^2 (1/(2l)) dv dl`

`= (1/2) log(1/b_m) >= (1/4) log m - (1/2) log 9`.

This proves the proposition.

The divergence concerns the essential supremum of the density, not an arbitrary choice of its value at a single point. The same cells and hub intervals also contain `(s-v^2)/(2l)` whenever `|s|<=sqrt(delta)`, since the extra root displacement is at most `1/16`. Hence the displayed logarithmic lower bound holds throughout this nonempty interval of levels.

### What the example isolates

The failure is entirely in conditional information: `P` identifies a tiny `(L,V)` cell, so the hub can choose a different center for every cell. Each scale `l` between `m^(-1/2)` and one contributes comparable mass after weighting by `1/l`. Uniform caps on all coordinate projection densities do not prevent this fine encoding.

The independent-coordinate and linear-projection structure of SP must therefore enter any successful proof quantitatively. Merely reapplying density caps after conditioning on `P` cannot suffice.

## 4. Why straightforward admissible comb coding has not produced a counterexample

For a one-dimensional cap-one density supported on `N` equal-mass teeth, every tooth carrying mass `1/N` needs width at least `1/N`. To decode a full discrete configuration from `P`, the corresponding projected tooth centers must be separated by more than the projected within-tooth noise, generally of order `1/N`.

If both `L,V` stay in bounded ranges, a bounded-range `P` has only order `N` separated code positions, while recovering their two-dimensional cell locations to accuracy `1/N` requires order `N^2` positions. Increasing the support range in `P` is possible, but orthogonality means the same independent coordinate directions typically also inflate `L` or `V`; the density contribution then pays the factor `1/|L|`, or the root fluctuates too much inside a tooth.

These are explanatory observations, not a theorem excluding all comb constructions. Very small `L` obtained by matching independent large tooth labels pays collision probabilities. For simple paired matches of tooth masses `r_j`, expressions such as `sum r_j^2 log(1/r_j)` remain bounded, so that particular mechanism does not diverge. More elaborate additive configurations remain a legitimate target.

## 5. Status

The Gaussian-smoothed theorem above is a rigorous positive result for an entire adapted-hub subclass. The cell-encoding proposition is a rigorous obstruction to a broad class of proof strategies. Neither proves nor disproves SP for arbitrary independent cap-one coordinate laws, and neither closes the original QFORM conjecture.

## 6. A fixed-rank frame partition lemma

The following lemma gives a further genuine endpoint result in Section 7. Its constant is nonexplicit; its dimension is fixed at three in that application.

**Lemma.** For every fixed positive integer `d` there exists `eta_d>0` such that every finite family `r_i in R^d` satisfying

`sum_i r_i r_i^T = I_d`, and `|r_i|^2 <= 1/2`,

has a partition into `A,B` for which

`sum_A r_i r_i^T >= eta_d I_d`, and `sum_B r_i r_i^T >= eta_d I_d`.

The constant is independent of the number of frame vectors.

### Qualitative basis packing

For a subspace `H` of codimension `k`, the energy in `H^perp` is `k`. Every frame vector contributes at most `1/2`, so at least `2k` vectors lie outside `H`. The finite matroid base-packing theorem therefore supplies two disjoint bases. The precise criterion used is `|E\F| >= 2(d-rank(F))` for every subset `F` of the finite vector family.

This is the classical base-packing theorem, not a new assertion of matroid theory: see Jack Edmonds, *Lehman's Switching Game and a Theorem of Tutte and Nash-Williams*, J. Res. Nat. Bur. Standards B 69B (1965), Theorem 2, [original paper](https://nvlpubs.nist.gov/nistpubs/jres/69B/jresv69Bn1-2p73_A1b.pdf).

### Uniformity when the number of vectors varies

Suppose no `eta_d` exists. Choose a sequence of counterexample frames whose best lower bound tends to zero. Sort each frame by decreasing vector norm and pad it with zero vectors. Passing to a diagonal subsequence, its `i`th vector converges to `r_i` for every fixed `i`. The sum of squared norms of each frame is `d`, hence the squared norm of its `(N+1)`st and all subsequent vectors is at most `d/(N+1)`.

The limiting atoms satisfy `sum_i r_i r_i^T <= I`. Put

`S = I - sum_i r_i r_i^T >= 0`, and `K=ker S`.

The projections of the limiting atoms onto `K` form a Parseval frame for `K`, with norms squared at most `1/2`. They contain two disjoint finite bases for `K`. Here is a reduction to the finite base-packing theorem: choose a finite initial segment whose covariance on `K` is at least `(1-epsilon)I_K`, with `epsilon<1/(2d)`. Every codimension-`k` subspace of `K` has outside energy greater than `k-1/2`; since each vector contributes at most `1/2`, the integer number of outside vectors is at least `2k`. The base-packing criterion applies to this finite segment.

Let `A0,B0` be the indices of these disjoint bases (empty if `K={0}`). Both matrices

`H_A = sum_{i in A0} r_i r_i^T + S/2`, and

`H_B = sum_{i in B0} r_i r_i^T + S/2`

are positive definite: a common null vector would lie in `K` and be orthogonal to a basis of `K`. Let `gamma>0` be the smaller of their least eigenvalues.

Choose `N` large enough to contain `A0,B0` and satisfy `d/(2 sqrt(N+1)) < gamma/4`. In each original frame, assign these fixed initial basis vectors to their prescribed sides; assign the other first `N` vectors arbitrarily. Randomly partition the tail by independent fair coin flips. If `T` is the tail covariance and `T_A` its contribution to side A, then

`E ||T_A-T/2||_F^2 = (1/4) sum_tail |r_i|^4 <= d^2/[4(N+1)]`.

Therefore there is a tail partition with operator error at most `d/(2 sqrt(N+1))`. The covariance of its other side has the same error. As the original-frame index tends to infinity, its tail covariance tends to `I - sum_{i<=N} r_i r_i^T`, which is at least `S`. Thus both full partition covariances are, for all sufficiently late frames, at least `gamma/2` times the identity. This contradicts the assumed convergence of their best lower bounds to zero and proves the lemma.

## 7. SP for a full class of Gaussian mixtures, without a Gaussian variance floor

**Theorem.** Let

`X_i = M_i + sqrt(T_i) G_i`, with `T_i>0`,

where the pairs `(M_i,T_i)` are independent across coordinates and the standard normal variables `G_i` are independent of all these pairs. Suppose

`E T_i^(-1/2) <= sqrt(2 pi)` for every `i`.

Let `w,v,p` be an orthonormal triple satisfying the SP spread condition `w_i^2+v_i^2+p_i^2<=1/2`. Then SP holds with a universal constant. One admissible constant is

`4 * 2^(-3/4) * 3^(3/2) * eta_3^(-3/4)`.

The theorem also permits the extra terms `B(Y,P)V+C(Y,P)` described in Section 2, with transverse coefficient `|lambda|>=1`.

The moment hypothesis implies that each marginal density is at most one, because it bounds the average peak of its Gaussian mixture components. For **centered Gaussian scale mixtures** (`M_i` deterministic), this hypothesis is exactly the cap-one condition: the maximum density is attained at `M_i` and equals `(2 pi)^(-1/2) E T_i^(-1/2)`. Thus the theorem proves SP for all cap-one centered Gaussian scale mixtures, including arbitrarily small component variances. It does not cover arbitrary translated narrow-tooth comb mixtures merely because their final marginal densities happen to be bounded by one.

### Proof

Write `r_i=(w_i,v_i,p_i)^T`. By Section 6 choose a partition `A,B` with covariance sums `S_A,S_B >= eta_3 I`. Conditional on the mixture variables, `(L,V,P)` is Gaussian with covariance

`M = sum_i T_i r_i r_i^T = M_A+M_B`.

If `lambda_min(M)=h`, its conditional `(L,V)` covariance given `P` is at least `h I_2`. The Gaussian proof in Section 2, with a direct power upper bound in its Fourier integral, gives

`||p_Q||_infinity <= 4 (2 pi)^(-3/4) h^(-3/4)`

for that conditional mixture. Indeed, with `a=sqrt(2 pi h)`, the relevant Fourier integral is at most

`a^(-2) integral_0^infinity u^(-1/2) min(1,a/u) du = 4 a^(-3/2)`.

It remains to bound the expectation of `h^(-3/4)`.

For side A, normalize `M_A` by `S_A`: if the columns of `R_A` are `S_A^(-1/2) r_i`, then `R_A R_A^T=I_3` and

`M_A = S_A^(1/2) [R_A diag(T_i) R_A^T] S_A^(1/2)`.

The matrix compression inequality

`[R D R^T]^(-1/2) <= R D^(-1/2) R^T`, for `R R^T=I`,

implies

`E lambda_min(M_A)^(-1/2) <= 3 sqrt(2 pi) eta_3^(-1/2)`.

For completeness, the compression inequality follows first for resolvents from the Schur-complement inequality `(RDR^T+sI)^(-1) <= R(D+sI)^(-1)R^T`, and then by integrating the scalar identity `x^(-1/2)=(1/pi) integral_0^infinity s^(-1/2)/(x+s) ds`. Taking traces gives the displayed expected bound because `sum_i |S_A^(-1/2)r_i|^2=3`. The identical bound holds for side B.

Put `a0=lambda_min(M_A)`, `b0=lambda_min(M_B)`. The two variables are independent, and

`h >= a0+b0 >= 2 sqrt(a0 b0)`.

Consequently, by independence and Holder's moment inequality,

`E h^(-3/4) <= 2^(-3/4) [3 sqrt(2 pi) eta_3^(-1/2)]^(3/2)`.

Combining this with the Gaussian density bound gives the stated constant. Averaging first in `P` and then in the mixture variables is legitimate because the conditional bound depends only on those mixture variables.

### Explicit Laplace special case

For independent translated Laplace densities `exp(-2|x-mu_i|)`, take `T_i` exponentially distributed with rate 2. Their characteristic functions agree since `E exp(-t^2 T_i/2)=4/(4+t^2)`. Here one can avoid the nonexplicit partition constant: direct compression with exponent `3/4` gives

`E lambda_min(M)^(-3/4) <= 3 E T_i^(-3/4) = 3 * 2^(3/4) Gamma(1/4)`.

Thus SP holds with the explicit bound

`12 pi^(-3/4) Gamma(1/4) < 19`.

This explicit Laplace result needs no spread condition. The general mixture result does use the spread condition through the two independent frame blocks.

## 8. Updated mathematical status

Sections 6 and 7 give a complete conditional-hub proof for the stated Gaussian mixture class and an independently useful fixed-rank frame partition lemma. The arguments have been checked internally, but no novelty claim is made; independent verification remains appropriate before inserting them into a formal manuscript. The unrestricted SP and QFORM problems remain open in this note. In particular, the proof does not control arbitrary rough cap-one laws whose boundedness comes from separating many narrow components in location.
