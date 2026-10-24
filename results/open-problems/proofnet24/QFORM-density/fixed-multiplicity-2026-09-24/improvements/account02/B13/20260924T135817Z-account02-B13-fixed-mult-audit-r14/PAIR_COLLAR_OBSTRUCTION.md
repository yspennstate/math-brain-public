# account02/B13 — pair-collar obstruction at the multiplicity-eight frontier

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Baseline manuscript pin: commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Result

The definite-pair and hyperbolic-pair lemmas are genuinely determinant-gated, not minimum-singular-value gated. They therefore cannot close the current multiplicity-eight two-sided collar merely by extracting the common physical pair. There is an explicit local no-pivot collar at exactly the guaranteed `Xi_2` scale.

Let `S,H,T` be pairwise disjoint two-coordinate banks and set

\[
A_c=\begin{pmatrix}
0&cI_2&0\\
cI_2&0&cI_2\\
0&cI_2&0
\end{pmatrix},
\qquad 0<c<1/10.
\]

Every diagonal entry is zero. Every principal `2x2` determinant is either zero or `-c^2`, hence has modulus `<eta=1/100`; there is no scalar or pair `eta`-pivot anywhere in this six-coordinate packet. In particular the common middle pair has

\[
A_c[H,H]=0.
\]

Nevertheless

\[
\det A_c[S,H]=c^2,
\qquad
\det A_c[H,T]=c^2,
\]

so the ordered collar triple `(S,H,T)` contributes

\[
\det(A_c[S,H])^2\det(A_c[H,T])^2=c^8
\]

to the current `Xi_2` currency.

For the threshold-eight structural theorem, the guaranteed scale is

\[
\xi_*=(\delta_*^2/2)\kappa^2
      =8.909772116276907\ldots\times10^{-9},
\]

where `kappa=1/6400` and `delta_*=0.854335140191...`. Its eighth root is

\[
\xi_*^{1/8}=0.0985674053572\ldots<0.1.
\]

Thus choosing `c=xi_*^{1/8}` gives a **single two-sided collar term already at the guaranteed global lower-bound scale while the entire local six-coordinate packet remains below the manuscript's principal-pair pivot threshold and the common pair matrix is exactly zero**.

This is not an `s_8` counterexample and does not contradict the structural collar theorem. It is a counterexample to the tempting deterministic shortcut

`two-sided collar mass => usable principal pair pivot`.

Therefore the remaining multiplicity-eight implication really must be an overlapping product-law receiver (or an equivalent aggregate argument). It cannot legitimately divide by the common diagonal, assume a minimum singular value for the middle pair, or replace the collar by the manuscript's definite/hyperbolic principal-pair branch.

## Pair-proof boundary

For an actual principal pair `B` with `D=|det B|>0`, the audited manuscript gives:

- definite `B`: `||p||_infinity <= pi/sqrt(D)` after conditioning;
- indefinite `B`: the conditional rough-law envelope

\[
p(z)\le D^{-1/2}\left(6+\log_+\frac{16\sqrt D}{|z-v|}\right),
\]

and a surviving Schur spectral direction pays the logarithm.

Both statements remain valid for fragmented/unbounded cap-one inputs and use only original-coordinate conditioning. The obstruction above shows exactly why those correct pair lemmas do not by themselves spend the zero-diagonal overlap collar.

Next obligation: `QFORM-EIGHT-OVERLAP1-TWOSIDED-COLLAR-RECEIVER-v1`.
