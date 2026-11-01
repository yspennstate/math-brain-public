SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B16, 2026-09-23T08:10:22Z.
attacking: overlapping projection-product interactions by retaining two genuinely independent original scalar noises until after the dependent two-dimensional slope projection is paid.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN. This checkpoint records a proved calculation before the final report.

## Two-noise random-slope calculation

Let `Z` be arbitrary. Let `(A,B,R)` be measurable functions of `Z`, and suppose `(A,B)` has a joint density `h` satisfying `||h||_infinity<=M`. Let `U,V` be independent real random variables, independent of `Z`, with probability densities bounded by one. For nonzero constants `c,d`, put

`Q = R + c A U + d B V`.

Conditional on `Z`, the two random terms have density caps `1/(|cA|)` and `1/(|dB|)`. Their convolution therefore has cap

`k(A,B)=1/max(|cA|,|dB|)`

for almost every `(A,B)`. Hence `||p_Q||_infinity <= E k(A,B)`. For `s>0`,

`{k>s} subset {|A|<1/(|c|s), |B|<1/(|d|s)}`,

whose planar Lebesgue measure is `4/(|cd|s^2)`. Thus

`P(k>s) <= min(1, 4M/(|cd|s^2))`,

and layer cake gives

`E k <= int_0^infinity min(1,4M/(|cd|s^2)) ds
       = 4 sqrt(M/|cd|)`.

Therefore

`||p_Q||_infinity <= 4 sqrt(M/|cd|)`.

The same argument yields a continuous density: for `AB!=0` the conditional density is a convolution of two `L1` densities and is continuous; the displayed integrable random cap gives dominated convergence. The axes have zero `(A,B)`-probability.

## Physical zero-pair corollary

For a symmetric full ambient matrix `H`, choose distinct original coordinates `i,j` satisfying

`H_ii=H_jj=H_ij=0`.

Write the remaining-coordinate slope rows as `b_i=H_{i,K}`, `b_j=H_{j,K}`, and set

`G=[[||b_i||^2,<b_i,b_j>],[<b_i,b_j>,||b_j||^2]]`.

If `det G>0`, the actual two-dimensional bounded-density projection theorem gives the slope pair `(b_i X_K,b_j X_K)` joint density cap

`M <= 2/sqrt(det G)`.

Taking `c=d=2`, `U=X_i`, `V=X_j` yields the full-ambient bound

`||p_(X^T H X)||_infinity <= 2 sqrt(2) (det G)^(-1/4)`.

All quadratic curvature on `K`, and all dependence between the two slopes, are retained. This branch also has a continuous density.

## Designated-partner family application

Apply the newest completed fleet02/B16 r27 stress construction

`Q_eps = 2 X_h(L+Y0) + 2 V Y1 + 2 eps T Y2`,

where `X_h,Y0,Y1,Y2` are independent cap-one scalars and `(L,V,T)` is the stated orthogonal projection of four iid `Unif[-1/2,1/2]` sources. Condition on `(X_h,L,V,T,Y2)` and use the fresh noises `Y0,Y1`. The slope pair is `(X_h,V)`. The actual one-dimensional projection theorem gives `||p_V||_infinity<=sqrt(2)`, so independence of `X_h` and `V` yields `M<=sqrt(2)`. Therefore

`||p_(Q_eps)||_infinity <= 2 sqrt(sqrt(2)) = 2^(5/4) = 2.3784142300...`

uniformly in `eps`. In particular this is a uniform bound on the partner's target-valid `0<eps<=1` family whose nonzero spectrum is `{sqrt(2),-sqrt(2),1,-1,eps,-eps}`. Thus the partner's infinite slice-Wiener quantity is a proof-interface obstruction, not an output-density obstruction.

Correction boundary: no independence after spectral rotation, arbitrary-joint coarea, conditional projection-density cap, pointwise law-uniform Fresnel decay, or small-random-error step is used. The remaining global debt is structural: the bare three-large-eigenvalue hypothesis does not automatically furnish two clean zero-pivot scalar noises with a quantitatively nondegenerate slope Gram determinant.
