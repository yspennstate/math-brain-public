# QFORM B20 — convex-chain payment inside the anchored O3 graph

Run: 20260923T051451Z-fleet04-B20-QFORM-r6

Status: ESSENTIAL_STEP_APPLIED. The unrestricted QFORM conjecture remains OPEN. Global continuity remains separate.

Source snapshot: brain main c6450eeb9b45d5505db5ecee471d04d7b336fa3f; owner correction revision 2026-09-22.15. Claude starting source e5f71d79eff325201dd0274053d20268ce65b837, with later Claude-review corrections retained. The completed fleet01/B20 input used below is f64266f079e502403ff19ff5ca9739a79c65ebcc.

No post-rotation independence, moment hypothesis, support restriction, conditional projection cap, arbitrary-joint coarea, or one-minor extraction is used.

## 1. New theorem: a convex residual chain is paid globally

Let X,Y,Z be independent real random variables with probability densities bounded by one. Let a,b be nonzero, and c,d be arbitrary reals. For arbitrary affine coefficients, put

    Q = 2aXY + cY^2 + 2dYZ + bZ^2 + alpha X + beta Y + gamma Z + kappa.

Then Q has a continuous density and

    ||p_Q||_infinity <= 4 / sqrt(|a b|).                 (1)

This includes the convex-residual case where the 2 by 2 matrix [[c,d],[d,b]] is positive definite. Thus (1) is a genuine two-sheet/convex-side payment, although only for the physical chain pattern

    K = [[0,a,0],[a,c,d],[0,d,b]].                       (2)

### Proof

Translate Y by alpha/(2a). Translations preserve independence and the density cap, and after absorbing new affine and constant terms it suffices to treat alpha=0.

Condition on the original coordinate Y=y. Complete the Z-square:

    b Z^2 + (2dy+gamma) Z
      = b (Z + (2dy+gamma)/(2b))^2 - (2dy+gamma)^2/(4b).

For fixed y, the translated Z is still independent of X and has density cap one. If W=b Z_y^2, its density satisfies, on the appropriate half-line,

    k_b(w) <= 1 / sqrt(|b w|).                           (3)

The remaining y-dependent terms only translate the output. Hence the same one-dimensional bathtub calculation as for a null pair plus a square gives, uniformly in the output level,

    p_(Q | Y=y)(s) <= sqrt(2) |y|^(-1/2) / sqrt(|a b|). (4)

Indeed, after writing s-2ayx = 2|ay|(t-x), the cap-one density of X gives

    integral f_X(x) (t-x)_+^(-1/2) dx <= integral_0^1 u^(-1/2) du = 2.

A second bathtub inequality gives

    integral f_Y(y) |y|^(-1/2) dy
      <= integral_(-1/2)^(1/2) |y|^(-1/2) dy = 2 sqrt(2). (5)

Averaging (4) and using (5) proves (1). For each y not equal to zero, the conditional density is a convolution of two L1 densities and is continuous. Equations (4)-(5) give an integrable, output-independent majorant, so dominated convergence proves continuity.

Conditioning on all outside original coordinates only adds affine terms to the three coordinates in (2). Thus (1) also holds for an ambient quadratic form whenever it contains this physical principal block, with arbitrary outside curvature and couplings.

## 2. Exact target-admissible convex-chain matrix

Take

    K0 = 3 [[0,1,0],[1,2,1],[0,1,2]].                   (6)

Its residual Y,Z block is 3 [[2,1],[1,2]], which is positive definite. The characteristic polynomial of the unscaled matrix is

    p(lambda) = lambda^3 - 4 lambda^2 + 2 lambda + 2.

On [-1/3,1/3], the sole critical point is the local maximum (4-sqrt(10))/3. Moreover,

    p(-1/3)=23/27,    p(1/3)=61/27.

Therefore p has no root in that interval. Since the matrix is symmetric, all its eigenvalues are real, so every eigenvalue of K0 has magnitude greater than one. Thus (6) is target-admissible, indefinite, zero-pivot, and has genuine convex residual curvature.

For

    Q = 6XY + 6Y^2 + 6YZ + 6Z^2,

the theorem has a=3 and b=6, hence

    ||p_Q||_infinity <= 4/(3 sqrt(2)) = 0.942809... .    (7)

This holds for all independent cap-one laws, not merely uniforms or Gaussian completions.

## 3. Actual use of fleet01/B20

Fleet01/B20 proved that its O3 star survivor has anchored exterior reserve

    W_i = sum_(j != i) ||r_i wedge r_j||^2 > 1/41472,   (8)

and decomposes into principal, one-overlap, and disjoint physical channels.

For (6), at the zero-pivot coordinate i=1,

    r_1=(0,3,0), r_2=(3,6,3), r_3=(0,3,6),

so

    W_1 = ||r_1 wedge r_2||^2 + ||r_1 wedge r_3||^2
        = 162 + 324 = 486 > 1/41472.                    (9)

Thus this concrete convex-chain matrix lies inside the anchored-compound geometry detected by the completed fleet01/B20 theorem. Equation (7) pays it at L-infinity, upgrading the generic 2/3-small-ball receiver on this exact chain.

The transfer is scoped: (8) alone does not force the sparse chain pattern (2), and (1) does not pay diffuse aggregate principal/overlap mass.

## 4. Compact noncircular proof graph

1. Physical-pivot, diffuse determinant/ridge, ruled one-sheet, null-pair, balanced-bank, and several finite-dimensional branches are already paid in their stated scopes.
2. The O3 survivor yields the anchored reserve (8) and the exact principal/overlap/disjoint ledger from fleet01/B20.
3. The present theorem pays the convex two-sheet node when that reserve is realized by one physical three-coordinate chain (2), including arbitrary ambient affine terms after conditioning.
4. The disjoint concentrated node has only a 2/3-small-ball/half-Riesz payment; it is not silently upgraded to L-infinity.
5. Still open: diffuse aggregate principal/overlap payment, diffuse disjoint e2 payment, the general near-null convex collar without chain sparsity, and interaction with arbitrary additional spectrum.

There is no full candidate to send for two end-to-end reviews. Under the stated review gate, none are fabricated or counted. The unrestricted conjecture and full continuity remain open.
