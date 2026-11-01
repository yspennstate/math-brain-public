# B07 improvement attempt: sharpness of the present minor/interpolation bookkeeping

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T120614Z-fleet01-B07-fixedmult-audit-r11`  
Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **proved method barrier / partial lower-threshold branch; no unconditional threshold reduction claimed.**

The baseline no-pivot argument uses, for a sampled order-`r` seed,

`A = D + R + E`,  `rank R <= 3r`,  `rank R[L,L] <= r`,

with `D=0` on the `2r` seed coordinates. It then needs `4r+1` spectral directions in order to force `r+1` large diagonal entries of `D` inside `L`. A tempting route to lower 17 is to replace the global `3r` by `2r`, or to delete the seed and exploit only the restricted rank `r`. Both shortcuts fail in general, and the losses are sharp already in tiny symmetric examples.

## 1. The global `3r` rank bound is algebraically sharp

Take `r=1`, `S={1}`, `T={2}`, `L={3}`, and

\[
 A=\begin{pmatrix}
 1&1&2\\
 1&1&3\\
 2&3&6
 \end{pmatrix}.
\]

The sampled seed is `B=A_{S,T}=[1]`, hence

\[
 P=A_{\cdot,T}B^{-1}A_{S,\cdot}
 =\begin{pmatrix}1\\1\\3\end{pmatrix}(1,1,2)
 =\begin{pmatrix}
 1&1&2\\
 1&1&2\\
 3&3&6
 \end{pmatrix}.
\]

Since `L` has one coordinate, `off(A_{L,L}-P_{L,L})=0`. Also `A_{33}-P_{33}=0`. Therefore the canonical completion of Lemma `lem:completion` has `E=0`, `D=0`, and `R=A`. Directly,

\[
 \det R=-1,
\]

so

\[
 \boxed{\operatorname{rank}R=3=3r},
 \qquad
 \boxed{\operatorname{rank}R_{L,L}=1=r}.
\]

Thus no universal replacement `rank R<=2r` is possible for this interpolation/completion construction.

This is not an artifact of large pivots. Multiplying the whole matrix by any sufficiently small nonzero scalar `delta` preserves both ranks and the nonsingular seed while making every diagonal entry and every principal two-coordinate determinant smaller than the manuscript's fixed pivot threshold. Hence the **no-pivot hypothesis alone does not improve the algebraic `3r` rank bound.** (The rescaled example is not claimed to satisfy the target unit spectral normalization; it proves sharpness of the rank lemma, which is the point here.)

A symbolic `r=1` calculation shows why this is generic. For

\[
 A=\begin{pmatrix}a&b&c\\b&d&e\\c&e&f\end{pmatrix},
 \quad S=\{1\},\ T=\{2\},\quad b\ne0,
\]

the canonical completion has

\[
 R=\begin{pmatrix}
 a&b&c\\
 b&d&e\\
 c&e&ec/b
 \end{pmatrix},
\]

and

\[
 \boxed{\det R=-\frac{(ae-bc)(be-cd)}{b}},
\]

which is nonzero on a Zariski-open set of symmetric inputs. Global rank `3r` is therefore genuinely attained, not merely an artifact of a loose subadditivity proof.

## 2. Deleting the seed before using `rank R[L,L]<=r` does not save an index

There is a slightly larger nonsymmetric rectangular block on which the correction has rank at most `r`: delete the `T` rows and the `S` columns. On

\[
 \mathcal R=[n]\setminus T,
 \qquad
 \mathcal C=[n]\setminus S,
\]

the support statement in `lem:completion` gives `R_{\mathcal R,\mathcal C}=P_{\mathcal R,\mathcal C}`, hence rank at most `r`.

However, passing from a square matrix to a submatrix obtained by deleting `r` rows and `r` columns can cost **two** singular-value indices. This loss cannot in general be replaced by one. Already for `r=1`, take

\[
 A_{\varepsilon,c}=
 \begin{pmatrix}
 1&\varepsilon&0\\
 \varepsilon&1&0\\
 0&0&c
 \end{pmatrix},
 \qquad S=\{1\},\ T=\{2\},\quad \varepsilon\ne0.
\]

The seed `A_{S,T}=[\varepsilon]` is invertible, while

\[
 A_{[n]\setminus T,\,[n]\setminus S}
 =\begin{pmatrix}\varepsilon&0\\0&c\end{pmatrix}.
\]

Taking `|c|,|eps|` arbitrarily small leaves the two largest singular values of the full matrix arbitrarily close to one, while the largest singular value of this skew-deleted block is arbitrarily small. Thus a one-index deletion inequality is false even with a nonsingular off-diagonal seed. Scaling again shows this is compatible with arbitrarily small pivot sizes at the purely algebraic level.

The standard two-sided deletion loss `2r` plus the rank-`r` correction therefore recreates the same total `3r` spectral loss as the global completion:

\[
 \text{row/column deletion loss }2r
 +\text{ restricted correction rank }r
 =3r.
\]

To force `r+1` large diagonal directions after those losses still requires

\[
 m-3r\ge r+1,
 \qquad\text{i.e.}\qquad
 \boxed{m\ge4r+1}.
\]

So merely switching from the global rank bound to a skew seed complement does **not** lower the baseline `4r+1` count.

## 3. Consequence for the 17-direction proof

The density-producing no-pivot branch uses crossing order `k=5`, and the small-ratio index may be `r=k-1=4`. In that worst case the current strict-diagonal-dominance contradiction needs five large diagonal entries in `L`. With only sixteen owner-scale singular directions, the existing rank bookkeeping can force at most

\[
 16-3\cdot4=4
\]

large diagonal entries after the global correction. Four entries are compatible with `rank R_{L,L}=4`; the contradiction disappears. Therefore:

\[
 \boxed{
 \text{the present sampling/completion/rank argument does not prove }s_{16}\text{ suffices.}
 }
\]

This is a **method barrier**, not a counterexample to a 16-eigenvalue theorem.

## 4. Interaction with the current lower-threshold analytic improvement

A separate completed repository theorem, `QFORM-LEVERAGE-HALF-DETERMINANT-v1`, proves that for a literal physical crossing `M` with maximum row leverage at most `1/2`, the characteristic-function determinant exponent improves from `-1/8` to `-1/4`. In particular, order-three volume already yields

\[
 \|p_Q\|_\infty
 \le 3\sqrt2\,e\,Z_3(M)^{-1/6}.
\]

The baseline no-pivot `s_9>=1` argument gives some random-cut crossing with

\[
 Z_3(M)\ge4^{-3}\kappa^3.
\]

If that same crossing also had leverage at most `1/2`, then

\[
 Z_3(M)^{-1/6}\le160
\]

and hence

\[
 \boxed{
 \|p_Q\|_\infty\le480\sqrt2\,e<1846.
 }
\]

Thus there is a valid **conditional nine-direction branch** retaining arbitrary within-bank quadratic terms, affine terms and product laws. But the random-cut expectation controls determinant volume, not row leverage; high-leverage/star crossings remain possible. Hence this does not lower the fixed-multiplicity theorem unconditionally.

## 5. Next proof obligation

A genuine reduction of 17 through this route needs new structure, not a bookkeeping optimization. A concrete target is:

> From a no-pivot matrix with the baseline order-three volume currency, extract a product-coordinate physical crossing with maximum row leverage `<=1/2`, **or** route the complementary high-leverage crossing to another dependence-safe density receiver with a dimension-free constant.

The baseline volume sampling by itself does not establish this dichotomy. Separately, the existing leverage-free independent-copy/BL mechanism is endpoint-only at order four (`|t|^{-1}`), so an unconditional `17 -> 13` reduction also needs a new endpoint/cancellation or structural argument.

No unconditional multiplicity below 17 is claimed in this artifact.
