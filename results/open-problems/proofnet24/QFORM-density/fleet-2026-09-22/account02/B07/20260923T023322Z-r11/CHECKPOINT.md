SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-23T02:33:22Z.
attacking: bounded-dimensional spectral receiver integrated with determinant-weighted coordinate-core extraction; isolate the genuinely diffuse bi-anchor survivor without selecting one tiny minor.

# Early mathematical checkpoint

The live first unpaid obligation is the partner account03/B07 anchored third-minor packet. I am using two ingredients at their proved scopes: (i) the finite-dimensional spectral receiver `||p_q||_infinity <= 2 sqrt(6 pi d)/sigma` for a `d`-coordinate ORIGINAL-coordinate principal block with three ACTUAL eigenvalues of modulus at least `sigma`; and (ii) the e5 Fresnel/mixed-hub theorem only on matrices satisfying its diagonal-plus-low-rank light-block hypothesis.

## 1. Marginal-tail -> physical-core lemma

Let `R,C` be disjoint original-coordinate banks and let `P>0` be the squared determinant mass of any packet of physical `3x3` minors `A[S,T]`, `S subset R`, `T subset C`. Normalize its determinant weights to a probability law `w(S,T)=det(A[S,T])^2/P`. For chosen coordinate sets `R0 subset R`, `C0 subset C`, write

`delta_R = sum_{i in R\R0} P_w(i in S)`,
`delta_C = sum_{j in C\C0} P_w(j in T)`.

Then the union bound gives

`P_w(S subset R0, T subset C0) >= 1-delta_R-delta_C`.

Hence, with `theta=(1-delta_R-delta_C)_+`,

`Z_3(A[R0,C0]) := sum_{|S|=|T|=3, S subset R0,T subset C0} det(A[S,T])^2 >= theta P`.   (1)

If `r=min(|R0|,|C0|)>=3`, `L=||A[R0,C0]||op`, and `s_3` denotes the third singular value, Cauchy-Binet gives

`Z_3=e_3(s_1^2,...,s_r^2) <= binom(r,3) L^4 s_3^2`,

so

`s_3(A[R0,C0]) >= sqrt(theta P)/(sqrt(binom(r,3)) L^2)`.       (2)

Let `H=R0 union C0`. Since `A[R0,C0]` is a rectangular compression of the symmetric principal block `A[H,H]`, singular-value contraction gives

`s_3(A[H,H]) >= s_3(A[R0,C0])`.                                 (3)

Thus `A[H,H]` has three ACTUAL eigenvalues of modulus at least the right side of (2). Conditioning only on original coordinates outside `H`, the finite-dimensional spectral receiver applies uniformly to the induced affine terms.

In the live no-pivot class `N3(tau)`, `|A_uv|^2 < tau+tau^2` for distinct `u,v` and `|A_uu|<tau`. Hence, if `p=|R0|, q=|C0|`,

`L <= sqrt(p q) sqrt(tau+tau^2)`.

Combining with (2)-(3), for `d=|H|` one obtains the explicit aggregate-before-inversion bound

`||p_Q||_infinity <= 2 sqrt(6 pi d) sqrt(binom(r,3)) p q (tau+tau^2) / sqrt(theta P)`.   (4)

No individual minor is selected. This is the bounded-coordinate spectral receiver needed by B07 in a robust approximate-support form.

## 2. Exact target-class diffuse obstruction to bounded cores

For even `N`, take orthonormal pairs in `R^N`

`v_j=u_j=1/sqrt(N)`, `x_j=y_j=(-1)^j/sqrt(N)`.

Define

`M_N = [[0,u^T],[v,x y^T]]`,
`A_N = [[0,M_N],[M_N^T,0]]`.

In row basis `(e0,v,x)` and column basis `(e0,u,y)`, `M_N` is exactly

`[[0,1,0],[1,0,0],[0,0,1]]`,

so its three nonzero singular values are `1,1,1`; therefore `A_N` has nonzero spectrum `{+1,+1,+1,-1,-1,-1}`. It is a valid full-target family.

Every nonzero physical `3x3` minor of `M_N` contains the anchor row and anchor column, and

`det M_N[{0,j,k},{0,p,q}] = -(v_j x_k-v_k x_j)(u_p y_q-u_q y_p)`.    (5)

The total anchored squared-minor mass is exactly `1`. Its residual row-pair and column-pair laws factor, and each physical residual coordinate has inclusion marginal exactly `2/N`. Thus this is a maximally conditional-diffuse bi-anchor packet. Every fixed-cardinality physical principal core has operator norm tending to zero (all its entries are `O(N^{-1/2})`), so no universal bounded-cardinality spectral-core extraction can pay this branch.

For `N>128`, all diagonal entries vanish and every physical principal-pair determinant has magnitude at most `1/N<1/128`; hence the family lies in the live no-pivot class.

## 3. Required e5 result applied to the obstruction

The preceding family is not a QFORM counterexample. Apply e5 Theorem MF with the two physical anchors as the heavy set `H`. On the remaining `2N` original coordinates,

`A_LL=[[0,xy^T],[yx^T,0]]`

has rank two with eigenvalues `+1,-1`. The two heavy-to-light coupling columns are `(0,u)` and `(v,0)`, orthogonal to the rank-two light eigenspace because `u perp y`, `v perp x`. Consequently the mixed Gram matrix is exactly `Gamma=I_4`, and every generalized physical row leverage is `2/N<=1/2` for `N>=4`.

Theorem MF therefore gives

`|phi_Q(t)| <= 16 pi^3 |t|^-3`.

Integrating `min(1,16 pi^3 |t|^-3)` yields

`||p_Q||_infinity <= 3*2^(1/3) < 3.780`,                         (6)

uniformly in `N` and in all independent cap-one input laws. Thus (5) is a source-valid obstruction only to bounded-core extraction, while the completed mixed-hub Fourier mechanism pays the exact diffuse model.

## Remaining gap after this checkpoint

The actual unpaid branch is now sharper: an anchored packet that escapes (4) must have determinant marginal mass spread over arbitrarily many physical coordinates. The exact model above shows this is possible even in `N3`; its payment uses the very special diagonal-plus-rank-two light block required by Theorem MF. What is still missing is a receiver that combines this determinant-marginal diffusion (and the partner r21/r21b disjoint transverse/motif reserve) with **arbitrary same-side light-bank quadratic curvature**. That curvature cannot be discarded by Theorem MF and cannot be called a small random perturbation.
