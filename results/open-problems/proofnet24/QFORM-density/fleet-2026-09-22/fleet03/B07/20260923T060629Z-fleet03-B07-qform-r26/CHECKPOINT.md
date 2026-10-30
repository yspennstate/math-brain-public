SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T06:06:29Z.
attacking: the nested edge-star-core survivor — split its residual physical core into a paid three-volume branch, an aggregate E2 bank, a genuine rank-one tube, or a two-sided physical heavy core.

# Early substantive checkpoint — fleet03/B07 r26

Let `N` be any nonzero ORIGINAL-coordinate cross block between disjoint banks. Put

`S=||N||_F^2`, `c=||N||_op^2`, and
`rho=min(max_i ||row_i(N)||_2^2, max_j ||col_j(N)||_2^2)`.

The following exhaustive four-way split is immediate but useful because every conclusion stays in physical/product coordinates:

1. If `c>3S/4`, then
   `dist_F(N,{rank<=1})^2=S-c<S/4`, hence the core is in a genuine rank-one Frobenius tube of radius `<||N||_F/2`.
2. If `S/3<=c<=3S/4`, then
   `E2(N)>=c(S-c)>=3S^2/16`.
   The existing physical two-coloring therefore produces four disjoint original-coordinate banks with a matching whose squared Frobenius product is at least `3S^2/256`.
3. If `c<S/3` and `rho<=2S/27`, then the newest third-volume theorem applies directly. Indeed
   `E2>=S(S-c)/2`,
   `Z=E3>=S(S-c)(S-2c)/6>S^3/27`, and its volume-marginal matrix inequality gives
   `alpha_i<=3 rho/(S-2c)<=2/3` on the better physical side. At `q=4/3`,
   `||p_Q||_infinity <=(9sqrt(3)e/2) Z^(-1/6)<(27e/2)||N||_F^(-1)`.
   This is a continuous-density bound for the FULL ambient quadratic-plus-affine form, retaining arbitrary same-bank curvature and outside couplings.
4. Otherwise `c<S/3` and `rho>2S/27`; because `rho` is the minimum of the largest row and column energies, there are an actual physical row and column of `N` with norms both `>sqrt(2/27)||N||_F`.

This checkpoint is the intended receiver for the r25 edge-star-core packet. If r25 gives
`|edge| ||star|| ||N||_F > theta F^3/(36sqrt(2))`, with `F` the parent cross-block Frobenius norm, then `|edge|,||star||<=F` imply
`||N||_F>theta F/(36sqrt(2))`.
Thus branch 3 is paid by
`||p_Q||_infinity <486sqrt(2)e/(theta F)`.
In branch 4 the new physical row/column norms `h_R,h_C` give
`|edge| ||star|| h_R h_C > theta^2 F^4/34992`.

The remaining work in this run is to write the full proof carefully, propagate the E2 packet quantitatively, and apply a completed fleet04 product-projection theorem to the new branch-4 inequality without misusing a projected density as a curved pushforward bound.

Full QFORM remains OPEN. This checkpoint makes no claim about full-target continuity outside branch 3.
