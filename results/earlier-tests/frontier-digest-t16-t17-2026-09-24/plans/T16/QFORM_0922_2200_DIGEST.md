# QFORM research plan

## What is known

The separable case is proved with C = π: among three eigenvalues of modulus at least 1 two share a sign, the ellipse coarea bound gives π for that pair, and the independent remainder only convolves. Three is sharp, since an opposite-sign pair gives a logarithmic singularity. A rank-three theorem with a universal constant is claimed (20:45) and unchecked. The 19:54 correction (the constant is not π in general) is consistent with Ball's slicing bound: a two-dimensional marginal of a product of densities at most 1 can have density 2 (Livshyts-Paouris-Pivovarov), so a rotated definite pair only gives 2π. The 09-07 and 09-12 entries are off-topic.

## The gap

Non-separability. The core pair Y = (<X,r_a>, <X,r_b>) depends on the rest of the form, and its conditional density given the orthogonal projection is unbounded (cube sections near the boundary of its projection are tiny). Any step bounding the core conditionally on the remainder is false.

## First concrete step

Read claims e0cc72a6 (rank three), 9d240315 (correction), b75770a2 (coarea) and aa29dd22 (literature) in full. Check the rank-three proof at three places: the (2,1) signature, where the level set is a hyperboloid on which 1/|grad F| is not integrable, so the marginal bound 2√2 alone cannot suffice; heavy tails, since density at most 1 gives no moments; and delocalized r_j, where coordinate pairs have 2x2 blocks of size O(1/n). Then state the one inequality about three-dimensional marginals it really uses.

## Quick reductions

1. Q(X) = F(PX), with P the projection onto the range of A.
2. Linear terms cost nothing: complete the square in the range; for a kernel term add η(b·x)², which keeps the large eigenvalues, and let η → 0 (weak limits keep a density bound).
3. Heredity. Conditioning on X_J leaves a quadratic polynomial in X_I with Hessian A_II, so a principal block with three eigenvalues of modulus at least c gives C/c.
4. Interlacing. Deleting a coordinate loses at most one eigenvalue ≥ 1 and one ≤ -1, so by induction on n it suffices to treat large-eigenvalue signatures (3,0), (2,1), (3,1), (2,2) up to sign, with any number of eigenvalues in (-1,1).
5. Extreme points. The window probability is multilinear in the f_i, so each f_i may be an indicator of a set of measure one, combs included.

After 4, the difficulty sits entirely in the many small eigenvalues.

## Main line

(a) Extend the rank-three argument to rank r with a constant C(r). With heredity this settles every A having a bounded principal block with three eigenvalues of modulus at least c. Pairs are not enough: [[1,1,-1],[1,1,1],[-1,1,1]] has eigenvalues 2, 2, -1 and every 2x2 principal minor zero. Where a nondegenerate indefinite pair exists there is a fallback: its log singularity sits at a Schur-complement quadratic in the other coordinates, and any polynomial small-ball bound (Carbery-Wright, decoupling) integrates it.

(b) What remains is the delocalized regime, where Y should be nearly Gaussian. There are no moments and the extreme densities are combs, so the needed statement is a local limit bound valid at every scale. I expect the real difficulty here.

(c) In parallel, a few minutes of Monte Carlo to break the conjecture: cube coordinates with delocalized (2,1) forms; the off-diagonal part of a delocalized rank-three form, where small eigenvalues cancel the diagonal and its smoothing (with one large eigenvalue this family should grow like n^{1/4}, a positive control); Ball's pair structures; combs tuned to the form. Growth in n would change the plan.

## To avoid

Pointwise Fourier decay: a comb makes |E exp(isX²)| close to 1 at a chosen s. Fourier with decoupling: each Cauchy-Schwarz costs a square root, and by my count k effective dimensions give |φ(s)| ≲ |s|^{-k/4}, so k ≥ 5 is needed, as in Götze's lattice-point work, while the hard case has three or four. Rogozin rearrangement to the cube: the bathtub principle gives sets of measure one, not intervals. Needle localization: it reduces to one-dimensional quadratics, where the claim is false. The best constant: any universal C will do.

Each verified piece goes to the math memory as its own note.
