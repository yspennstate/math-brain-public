# account02/B18 — early checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

## First unpaid implication attacked

The prior B18 run isolated the non-source-separated Schur-isotropic high-shear/two-sheet survivor. The newest completed partner result account03/B18 r25 pays any ORIGINAL-coordinate residual two-plane bank carrying a positive Pluecker currency

\[
\Omega_J=\sum_{i<j\in J}\det(n,v_i,v_j)^2.
\]

The immediate unpaid question is whether that bank theorem can be combined with a genuinely product-valid low-shear estimate so that a fixed positive `Omega_J` pays the *entire shear parameter*, not just `r>=1`.

## New compiler inequality

In the exact-rank-three Schur-isotropic representation

\[
Q=(Y+r nX_0)^TD(Y+r nX_0),\qquad Y=V^TX_R,\quad V^TV=I_3,
\]
with `n^T D n=0`, suppose the physical matrix has exactly three nonzero eigenvalues of magnitude at least `s>0`, the residual frame satisfies

\[
\delta:=\max_j\|v_j\|_2^2\le \tfrac12,
\]
and some residual original-coordinate bank `J` spans exactly a two-plane and has `Omega_J>=omega>0`.

Conditioning only on the genuine original scalar `X_0`, Claude/e5f Theorem F applies to the residual product variables. Diagonalising `D` rotates only the three-column spectral factor, not the random coordinates, so row leverage remains `delta`. Hence

\[
\|p_Q\|_\infty\le 12|\det D|^{-1/3}.
\]

The completed account03/B18 r25 tilted-bank theorem gives simultaneously

\[
\|p_Q\|_\infty\le 6\,2^{2/3}[r^2|\det D|\Omega_J]^{-1/3}.
\]

Its exact-rank-three determinant ledger gives

\[
|\det D|(1+r^2)\ge s^3.
\]

Therefore, writing `x=r^2`,

\[
A(x)=\frac{12}{s}(1+x)^{1/3},\qquad
B(x)=\frac{6\,2^{2/3}}{s\,\omega^{1/3}}(1+x^{-1})^{1/3}
\]
are two valid bounds. `A` is increasing and `B` decreasing. Their unique crossing is

\[
x=(2\omega)^{-1},
\]
so for every `r>0`

\[
\boxed{\ \|p_Q\|_\infty\le \frac{12}{s}\left(1+\frac1{2\omega}\right)^{1/3}.\ }
\]

This is an essential-density statement and in fact the Theorem-F characteristic-function envelope also gives continuity for each fixed packet. No post-rotation independence is used.

## Concrete consequence for the prior B18 Hadamard stress family

For Walsh-Hadamard order `m>=8`, take residual rows

\[
v_j=m^{-1/2}(1,a_j,b_j),\qquad a_j,b_j\in\{\pm1\},
\]
with the four sign types equally frequent, `n=e_1`, and

\[
D_r=\begin{pmatrix}0&(1+r^2)^{-1/2}&0\\(1+r^2)^{-1/2}&0&0\\0&0&1\end{pmatrix}.
\]

This is the earlier mixed-source family with nonzero spectrum `{-1,1,1}`. Its residual leverage is `3/m<=1/2`. Let `J` be the two row types `(1,1,1)/sqrt(m)` and `(1,1,-1)/sqrt(m)`. Then `J` spans the plane `{(x,x,z)}`, whose normal has squared overlap `1/2` with `n`, and direct Cauchy-Binet gives

\[
\Omega_J=\frac14.
\]

Thus the *whole real line*, including the previously unpaid two-sheet side, satisfies

\[
\boxed{\ \|p_{Q_{m,r}}\|_\infty\le 12\,3^{1/3}=17.3069948436\ldots\quad(m\ge8,\ r>0).\ }
\]

This removes that exact non-source-separated Hadamard family as an obstruction. It does **not** prove general N3: the remaining survivor can have no exact two-plane original-coordinate bank with dimension-free `Omega_J`, or can have residual leverage above `1/2`.
