# B14 improvement: rough conditional-Tonelli compiler and terminal r=4 determinant growth

Source manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
Run: `20260924T120303Z-fleet02-B14-QFORM-audit11`.

## 1. Rough-law conditional domination compiler

Fix bounded Borel representatives of all marginal densities once and for all; this is always possible without changing the laws, and pointwise truncation preserves the stated density caps.

Let `nu` be a positive finite environment measure, `mu_y` a measurable kernel on `R`, and `k(y,z)>=0` jointly Borel. If for `nu`-a.e. `y` and every nonnegative Borel `h`

`int h(z) mu_y(dz) <= int h(z) k(y,z) dz`,

then the mixture `mu(B)=int mu_y(B)nu(dy)` satisfies

`mu(dz) <= K(z) dz`,  `K(z)=int k(y,z)nu(dy)`.

This is immediate by integrating the test-function inequality and applying Tonelli. It avoids choosing conditional-density versions and avoids requiring one output-null set valid for every conditioning value.

It applies verbatim to the manuscript's scalar pivot, definite pair, and hyperbolic pair kernels. Consequently arbitrary translations, conditioning-generated affine terms, countably fragmented/unbounded supports and density representatives cause no additional loss in those branches.

## 2. Terminal r=4 growth lemma under s_16

Assume the normalized no-pivot terminal chamber with `r=4`, `V_5<kappa V_4`, and `s_16(A)>=1`. Let `(S,T)` be the sampled seed supplied by the manuscript, `B=A[S,T]`, `L=[n]\(S union T)`, and

`P=A[:,T] B^{-1} A[S,:]`.

The sampled residual obeys `||E||_F<=5 sqrt(kappa)=1/16`. Since `rank R<=12`, the `s_16` hypothesis forces at least four diagonal entries of `D` with modulus at least `15/16`; choose those indices as `H subset L`, `|H|=4`. Because `A` has no `eta=1/100` pivot,

`|P_ii|=|R_ii| >= 15/16-1/100 = 371/400`,

and for `i!=j` in `H`,

`|P_ij|=|R_ij| <= |A_ij|+|E_ij| < 1/7+1/16 = 23/112`.

Therefore the row and column diagonal-dominance margin is

`delta = 371/400 - 3(23/112) = 109/350`.

For any vector `x`, choosing a coordinate of maximal modulus gives

`||P[H,H] x||_infinity >= delta ||x||_infinity`.

Applying the same argument to the transpose yields

`||P[H,H]^{-1}||_infinity <= delta^{-1}` and `||P[H,H]^{-1}||_1 <= delta^{-1}`.

Hence `||P[H,H]^{-1}||_2<=delta^{-1}`, so

`s_min(P[H,H])>=delta`,  `|det P[H,H]|>=delta^4`.

Now set

`b=|det A[S,T]|`, `c=|det A[H,T]|`, `e=|det A[S,H]|`.

Since

`P[H,H]=A[H,T] B^{-1} A[S,H]`,

all three `4x4` minors are nonsingular and

`c e >= delta^4 b`.

For any disjoint `4x4` cross minor, every entry is off-diagonal, hence has modulus `<1/7`. Hadamard therefore gives

`c,e <= (2/7)^4 = 16/2401`.

It follows separately that

`c >= alpha b`, `e >= alpha b`,

where

`alpha = delta^4/(16/2401) = (109/100)^4 = 1.41158161... >1`.

### Consequence

Every sampled-good terminal `r=4` seed in the attempted `s_16` proof generates two neighboring disjoint four-minors whose determinant magnitudes are larger by the same universal factor `(109/100)^4`.

This does **not** complete the 16-eigenvalue theorem: the two heavier neighboring seeds are not known to inherit the sampled small-residual estimate. The precise remaining implication is now to control the transfer from residual-good seeds to these heavier neighbors (for example by a weighted/global sampling argument), or else give a source-valid obstruction. Merely improving the global `3r` or restricted `r` rank bounds is not enough.
