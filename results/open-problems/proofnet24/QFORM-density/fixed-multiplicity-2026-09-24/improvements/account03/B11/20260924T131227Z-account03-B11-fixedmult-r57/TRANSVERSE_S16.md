# QFORM-S16-TRANSVERSE-CARRIER-v1

**Run:** `20260924T131227Z-account03-B11-fixedmult-r57`  
**Status:** proved supporting structural improvement; **no 16-eigenvalue density theorem claimed**.  
**Pinned baseline:** `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

This result starts in the normalized no-pivot chamber of the fixed-multiplicity manuscript and sharpens the current `s_16` endpoint. It is self-contained modulo the pinned manuscript's proved `prop:volume`, random-cut identity, and singular-value rank inequality.

Keep

\[
\eta=\frac1{100},\qquad \kappa=\frac1{80^2}=\frac1{6400}.
\]

## Theorem

Let `A=A^T` have no `eta`-pivot and suppose

\[
s_{16}(A)\ge1.
\]

Then either:

1. `V_5(A)>=kappa^5`, in which case the manuscript's order-five random-cut argument already gives `||p_Q||_infty<2400` for arbitrary affine terms and arbitrary independent cap-one coordinate laws; or
2. there is an original-coordinate partition `[n]=I sqcup J`, with `M=A[I,J]`, and its top-rank-four SVD truncation `M_4`, such that

\[
Z_4(M)\ge\frac{\kappa^4}{1280},\qquad
\frac{Z_5(M)}{Z_4(M)}\le\frac{5\kappa}{16},\qquad
\|M-M_4\|_F\le\frac1{64}.
\tag{1}
\]

Write

\[
D=B\oplus C,\qquad B=A[I,I],\quad C=A[J,J],
\]

and let

\[
U=\operatorname{ran}M_4\subset\mathbb R^I,\qquad
V=\operatorname{ran}M_4^T\subset\mathbb R^J,
\]

with orthogonal projections `P_U,P_V`. Then the **carrier-orthogonal same-bank operator** satisfies

\[
\boxed{
 s_8\!\left(
 \operatorname{diag}(I-P_U,I-P_V)\,D
 \right)\ge\frac{63}{64}.}
\tag{2}
\]

Consequently one of the two sides, say `I` after relabeling, obeys

\[
\boxed{s_4((I-P_U)B)\ge\frac{63}{64}.}
\tag{3}
\]

Let `O=B-diag(B)`. Since there is no `eta`-pivot,

\[
\boxed{s_4((I-P_U)O)\ge\frac{1559}{1600}.}
\tag{4}
\]

Finally there exists a literal physical sign partition `I=I_+ sqcup I_-` and its internal crossing operator

\[
C_\varepsilon=\frac{O-E_\varepsilon O E_\varepsilon}{2}
=\begin{pmatrix}0&N\\N^T&0\end{pmatrix}
\]

(in the `I_+`,`I_-` ordering) such that

\[
\boxed{
 \|(I-P_U)C_\varepsilon\|_{(4)}
 \ge\frac{1559}{800},}
\tag{5}
\]

where `||.||_(4)=sum_{j=1}^4 s_j(.)` is the Ky Fan four-norm. In particular,

\[
\boxed{
 \|(I-P_U)C_\varepsilon\|_{op}
 \ge\frac{1559}{3200}=0.4871875,}
\tag{6}
\]

and therefore `||N||_op>=1559/3200`.

The new content is (2)–(6): the same-bank modes forced by `s_16` can be made quantitatively **transverse to the old rank-four crossing carrier**. They are not allowed to hide completely inside the first crossing's four-dimensional left/right singular spaces.

## Proof

### Step 1: produce the near-rank-four crossing

Assume the already-paid alternative `V_5(A)>=kappa^5` fails. Since `s_16(A)>=1` implies `s_13(A)>=1`, the manuscript's no-pivot spectral-to-volume proposition at `k=4` gives

\[
V_4(A)\ge\kappa^4.
\tag{7}
\]

For a fair original-coordinate cut `[n]=I sqcup J`, put `M=A[I,J]`. The exact random-cut identities are

\[
\mathbb E Z_4(M)=4^{-4}V_4(A),\qquad
\mathbb E Z_5(M)=4^{-5}V_5(A).
\tag{8}
\]

Weight cuts proportionally to `Z_4(M)`. Under this probability law,

\[
\mathbb E_w\frac{Z_5(M)}{Z_4(M)}
=\frac14\frac{V_5(A)}{V_4(A)}<\frac\kappa4.
\tag{9}
\]

Markov at threshold `5kappa/16` shows that more than one fifth of the total `Z_4` weight lies on cuts satisfying

\[
\frac{Z_5(M)}{Z_4(M)}\le\frac{5\kappa}{16}.
\]

Hence one such cut also has

\[
Z_4(M)>\frac15\,\mathbb E Z_4(M)
\ge\frac{\kappa^4}{1280}.
\]

Let `sigma_1>=sigma_2>=...` be the singular values of `M` and set `x_j=sigma_j^2`. Since `Z_k=e_k(x)`, the exact identity

\[
5e_5(x)=
\sum_{|S|=4}\left(\prod_{i\in S}x_i\right)
\left(\sum_{j\notin S}x_j\right)
\]

gives

\[
\sum_{j\ge5}\sigma_j^2
\le5\frac{Z_5(M)}{Z_4(M)}
\le\frac{25\kappa}{16}=\frac1{4096}.
\tag{10}
\]

Thus the top-four SVD truncation satisfies

\[
\|M-M_4\|_F\le\frac1{64}.
\]

This reproduces the useful `s_16` reduction previously obtained by account01/B20, now as part of the closed proof chain here.

### Step 2: project away the old crossing carrier before paying rank

Define

\[
K=\begin{pmatrix}0&M_4\\M_4^T&0\end{pmatrix},
\qquad
A_0=D+K
=\begin{pmatrix}B&M_4\\M_4^T&C\end{pmatrix}.
\]

The discarded symmetric tail has operator norm exactly `||M-M_4||_op<=1/64`; hence Weyl gives

\[
s_{16}(A_0)\ge\frac{63}{64}.
\tag{11}
\]

Let

\[
P=\operatorname{diag}(P_U,P_V).
\]

Because `M_4` maps `V` to `U` and `M_4^T` maps `U` to `V`,

\[
PK=K,\qquad (I-P)K=0,
\]

and `rank P=8` (the positive `Z_4(M)` forces `rank M_4=4`). Therefore

\[
A_0=P(D+K)+(I-P)D.
\tag{12}
\]

The first summand has rank at most eight because its range is contained in `U direct_sum V`. Apply the manuscript's rank-shift inequality with

\[
T=(I-P)D,\qquad R=P(D+K),\qquad j=q=8.
\]

It yields

\[
s_{16}(A_0)\le s_8((I-P)D).
\]

Together with (11), this proves (2).

Now

\[
(I-P)D=
\operatorname{diag}((I-P_U)B,(I-P_V)C).
\]

Its singular values are the union of the singular values of the two displayed blocks. At least eight are at least `63/64`, so one block contains at least four. This is (3), after relabeling the two banks if necessary.

This is strictly stronger than merely concluding that `B` or `C` has four near-unit singular values: the four large outputs survive **after projection onto the orthogonal complement of the old rank-four crossing carrier**.

### Step 3: remove the tiny diagonal without losing transversality

Since `A` has no `eta`-pivot,

\[
\|\operatorname{diag}B\|_{op}<\eta=\frac1{100}.
\]

Writing `O=B-diag(B)`, singular-value Lipschitz continuity gives

\[
\begin{aligned}
s_4((I-P_U)O)
&\ge s_4((I-P_U)B)
   -\|(I-P_U)\operatorname{diag}B\|\\
&>\frac{63}{64}-\frac1{100}
=\frac{1559}{1600},
\end{aligned}
\]

which proves (4).

### Step 4: turn the transverse same-bank mass into a physical crossing

Let `E_eps` be a diagonal matrix of independent fair signs on the physical coordinates of `I`, and put

\[
C_\varepsilon=\frac{O-E_\varepsilon O E_\varepsilon}{2}.
\]

Because `O` has zero diagonal,

\[
\mathbb E_\varepsilon C_\varepsilon=\frac O2.
\tag{13}
\]

The Ky Fan four-norm is a convex matrix norm. Hence

\[
\begin{aligned}
\mathbb E_\varepsilon\|(I-P_U)C_\varepsilon\|_{(4)}
&\ge
\left\|(I-P_U)\mathbb E C_\varepsilon\right\|_{(4)}\\
&=\frac12\|(I-P_U)O\|_{(4)}\\
&\ge\frac12\sum_{j=1}^4 s_j((I-P_U)O)\\
&\ge2\cdot\frac{1559}{1600}
=\frac{1559}{800}.
\end{aligned}
\]

Therefore some sign pattern satisfies (5). Since

\[
\|T\|_{op}\ge\frac14\|T\|_{(4)}
\]

for every matrix `T`, (6) follows. For that sign pattern, entries connecting equal signs cancel and entries connecting opposite signs remain exactly those of `O`; after reordering physical coordinates,

\[
C_\varepsilon=\begin{pmatrix}0&N\\N^T&0\end{pmatrix}.
\]

Thus this is a literal original-coordinate crossing, not a spectral rotation. Projection cannot increase operator norm, so `||N||=||C_eps||>=||(I-P_U)C_eps||>=1559/3200`.

This completes the proof.

## What this repairs and what remains

The preceding `s_16` endpoint report left open the possibility that the extra same-bank crossing was quantitatively large but entirely aligned with the first crossing's four-dimensional carrier. Equations (2)–(6) rule that out. The remaining obstruction is now more specific:

> Find one product-preserving physical repartition, or an equivalent multi-bank Fourier receiver, that simultaneously retains a quantitative portion of the old order-four exterior volume and exposes one of the newly proved carrier-orthogonal same-bank directions as a fifth integrable direction.

A raw norm lower bound for the second crossing is not yet enough because a repartition of the `I` bank can reduce the old `Z_4` volume. Likewise, the adaptive order-four determinant theorem closes every crossing with a uniform leverage gap but not the exact near-coloop endpoint. No independence after rotation, Gaussianity, moments, bounded support, or spectral truncation is introduced here.

## Quantitative diagnostic

A deterministic-seed numerical diagnostic used 500 random `8+8` block examples with rank-four `M_4`. In every trial it checked

\[
s_{16}(D+K)\le s_8((I-P)D)
\]

and exhaustively enumerated all `2^8` physical sign splittings on one bank to check the convexity-predicted crossing lower bound. The largest observed signed violation was negative (`-2.8566e-2` for the rank inequality and `-7.1809e-1` for the split inequality). This finite computation is only a regression check; the proof above is symbolic.
