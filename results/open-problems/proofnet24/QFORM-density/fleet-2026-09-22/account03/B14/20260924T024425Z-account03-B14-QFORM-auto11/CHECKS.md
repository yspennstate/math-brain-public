# Checks for QFORM-GENERIC-MATRIX-ZERO-LOSS-CLOSURE-v1

Run `20260924T024425Z-account03-B14-QFORM-auto11`.

## Algebraic-genericity check

For fixed `n`, the bad conditions used in the report are zero sets of finitely many nonzero polynomials in the independent upper-triangular entries of a symmetric matrix:

- each principal determinant `det G_{S,S}`;
- the characteristic-polynomial discriminant;
- each off-diagonal coordinate `G_ij`.

Their product is a nonzero polynomial because the coordinate ring over `R` is an integral domain. Hence its nonvanishing set is open dense. This proves existence of generic approximants in every operator-norm neighborhood; equivalence of Euclidean/Frobenius/operator topologies in fixed finite dimension is enough.

## Spectral-margin check

For symmetric `A`, the singular values are absolute eigenvalues. Weyl's singular-value perturbation inequality gives

`|s_3(G)-s_3(H)| <= ||G-H||_op`.

Thus if `s_3(A)>=1`, then `s_3((1+eta)A)>=1+eta`; any generic `G` with `||G-(1+eta)A||_op<eta/2` satisfies `s_3(G)>1`.

## No-moment convergence check

For every fixed sample `x in R^n`,

`|x^T(G_k-H)x| <= ||G_k-H||_op ||x||_2^2`.

Because each random coordinate is real-valued almost surely and `n` is finite, `||X||_2^2<infinity` almost surely. Therefore `X^T G_k X -> X^T H X` almost surely without using `E||X||^2` or any other moment.

## Buffered-interval check

If `Y_k->Y` almost surely and `I=[a,b]`, then for every `delta>0`, on `{Y in I}` one has eventually `Y_k in (a-delta,b+delta)`. Therefore

`1_{Y in I} <= liminf_k 1_{Y_k in I^delta}`,

and Fatou gives

`P(Y in I) <= liminf_k P(Y_k in I^delta)`.

If the right side is bounded by `C(|I|+2delta)`, letting `delta downarrow0` preserves exactly `C`.

## Source-law approximation check

With `delta_R=int_{|x|>R} f`,

`f_R=f 1_{[-R,R]} + 1_[R+1,R+1+delta_R]`

has mass `(1-delta_R)+delta_R=1`, cap at most one, and

`||f_R-f||_1 <= int_{|x|>R}f + delta_R =2delta_R`.

Convolution with a nonnegative unit-mass mollifier preserves the `L^infinity` cap. Mixing with a broad cap-`<1` connected-support bump by `(1-epsilon)g+epsilon q` gives strict cap `<1`, one connected compact support interval, and `L^1` error at most `2epsilon`.

For product laws, total variation telescopes:

`d_TV(otimes_i mu_i,otimes_i nu_i) <= sum_i d_TV(mu_i,nu_i)`.

Pushforward cannot increase total variation, so every interval probability passes with no constant loss.

## Partner numerical check

Account04/B14 r10 uses `6 sqrt(pi)/sigma`. At unit scale,

`6 sqrt(pi) = 10.634723105433096...`.

For generic approximants of `(1+eta)A`, the selected physical-block scale satisfies `sigma_k -> (1+eta)sigma`; after the output rescaling by `(1+eta)`, the factors cancel exactly and recover `6 sqrt(pi)/sigma`.

## Scope guard

This is not a proof of full QFORM. Genericization removes exact algebraic degeneracies but supplies no positive uniform lower bound on the nonzero pivots/minors. Any analytic estimate that blows up as those quantities tend to zero remains insufficient. Continuity of the full limiting density is also not established.
