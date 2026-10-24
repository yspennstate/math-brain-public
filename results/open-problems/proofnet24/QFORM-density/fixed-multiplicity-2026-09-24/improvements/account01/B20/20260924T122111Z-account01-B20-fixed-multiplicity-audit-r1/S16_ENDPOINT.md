# QFORM-S16-ORDER4-PLUS-SECOND-PHYSICAL-CROSSING-v1

Run: `20260924T122111Z-account01-B20-fixed-multiplicity-audit-r1`

Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **new proved supporting lemma; no 16-eigenvalue density theorem claimed.**

Keep the manuscript constants

\[
\eta=\frac1{100},\qquad \kappa=\frac1{80^2}=\frac1{6400}.
\]

Let `A=A^T` have **no** `eta`-pivot and suppose

\[
s_{16}(A)\ge1.
\]

Then exactly one of the following conclusions is needed:

1. `V_5(A)>=kappa^5`, in which case the manuscript's random-cut + order-five Fourier argument already gives the full ambient density bound `<2400`; or
2. there is a literal original-coordinate cut `[n]=I sqcup J`, with `M=A[I,J]`, such that

\[
\boxed{Z_4(M)\ge \frac{\kappa^4}{1280}},
\tag{1}
\]

\[
\boxed{\frac{Z_5(M)}{Z_4(M)}\le \frac{5\kappa}{16}},
\tag{2}
\]

and therefore

\[
\boxed{\operatorname{dist}_F(M,\operatorname{rank}\le4)\le\frac1{64}}.
\tag{3}
\]

Writing the same-bank principal blocks as

\[
B=A[I,I],\qquad C=A[J,J],
\]

the same cut also satisfies

\[
\boxed{s_8(B\oplus C)\ge\frac{63}{64}}.
\tag{4}
\]

Consequently one of `B,C` has at least four singular values at least `63/64`. Since that block inherits the no-pivot condition, it contains a second literal physical internal crossing `N` with

\[
\boxed{\|N\|_{op}\ge\frac{1559}{3200}=0.4871875.}
\tag{5}
\]

Thus the entire unpaid `s_16` no-pivot chamber has been reduced to an **order-four crossing within `1/64` Frobenius distance of rank four, together with eight near-unit same-bank modes and an additional large original-coordinate crossing**. What is not yet proved is that the second crossing is quantitatively transverse to the first crossing's four-dimensional carrier; that alignment problem is the remaining obstruction to promoting this lemma to a 16-eigenvalue density theorem.

## Proof

Assume the already-paid alternative `V_5(A)>=kappa^5` fails, so

\[
V_5(A)<\kappa^5.
\tag{6}
\]

Because `s_16(A)>=1` implies `s_13(A)>=1`, Proposition `prop:volume` of the manuscript with `k=4` gives

\[
V_4(A)\ge\kappa^4.
\tag{7}
\]

Let `[n]=I sqcup J` be a fair independent physical cut and put `M=A[I,J]`. The manuscript's exact random-cut identity gives

\[
\mathbb E Z_4(M)=4^{-4}V_4(A),\qquad
\mathbb E Z_5(M)=4^{-5}V_5(A).
\tag{8}
\]

Weight cuts by `Z_4(M)`. Under the resulting probability measure (zero-weight cuts are irrelevant),

\[
\mathbb E_w\frac{Z_5(M)}{Z_4(M)}
=
\frac{\mathbb E Z_5(M)}{\mathbb E Z_4(M)}
=
\frac14\frac{V_5(A)}{V_4(A)}
<\frac\kappa4.
\tag{9}
\]

Set

\[
G=\left\{\frac{Z_5(M)}{Z_4(M)}\le\frac{5\kappa}{16}\right\}.
\]

Markov's inequality in the weighted measure gives

\[
w(G^c)<\frac{\kappa/4}{5\kappa/16}=\frac45,
\]

so more than one fifth of the total `Z_4` weight lies in `G`. Hence some physical cut in `G` satisfies

\[
Z_4(M)>\frac15\mathbb E Z_4(M)
\ge\frac15\,4^{-4}\kappa^4
=\frac{\kappa^4}{1280},
\]

which proves (1) and (2).

Let `sigma_1>=sigma_2>=...` be the singular values of this `M`, and put `x_j=sigma_j^2`. Then `Z_k(M)=e_k(x)`. The elementary-symmetric identity

\[
5e_5(x)
=
\sum_{|S|=4}\left(\prod_{i\in S}x_i\right)
\left(\sum_{j\notin S}x_j\right)
\tag{10}
\]

is exact: every five-element monomial is counted once for each of its five deleted indices. For every four-set `S`, its complementary sum is at least the tail after the four largest entries,

\[
\sum_{j\notin S}x_j\ge\sum_{j\ge5}x_j.
\]

Therefore

\[
\sum_{j\ge5}\sigma_j^2
\le5\frac{Z_5(M)}{Z_4(M)}
\le\frac{25\kappa}{16}
=\frac1{4096}.
\tag{11}
\]

The Eckart--Young formula now gives (3).

Let `M_4` be the top-four SVD truncation and `R=M-M_4`. Then

\[
\|R\|_{op}\le\|R\|_F\le\frac1{64}.
\]

Define

\[
A_0=
\begin{pmatrix}
B&M_4\\
M_4^T&C
\end{pmatrix}.
\]

The removed symmetric off-diagonal tail has operator norm exactly `\|R\|_{op}`, so Weyl gives

\[
s_{16}(A_0)\ge1-\frac1{64}=\frac{63}{64}.
\tag{12}
\]

Write

\[
A_0=(B\oplus C)+K,
\qquad
K=
\begin{pmatrix}0&M_4\\M_4^T&0\end{pmatrix}.
\]

Since `rank M_4<=4`, `rank K<=8`. The manuscript's singular-value rank inequality with `j=8,q=8` gives

\[
s_{16}(A_0)\le s_8(B\oplus C),
\]

and (4) follows from (12).

The singular values of the block diagonal matrix `B\oplus C` are the union of those of `B` and `C`. Thus at least eight of them are at least `63/64`, and one of the two blocks, say `B`, has at least four; in particular

\[
\|B\|\ge\frac{63}{64}.
\tag{13}
\]

Because `A` has no `eta`-pivot, all diagonal entries of `B` have modulus `<eta=1/100`. For its zero-diagonal part `O=B-diag(B)`,

\[
\|O\|\ge \|B\|-\|\diag(B)\|
>\frac{63}{64}-\frac1{100}
=\frac{1559}{1600}.
\tag{14}
\]

Apply the manuscript's random-sign splitting argument used in the quarter-power lemma: for a diagonal fair-sign matrix `E_epsilon`, put

\[
C_\epsilon=\frac{O-E_\epsilon O E_\epsilon}{2}.
\]

Since `E C_epsilon=O/2`, convexity of the operator norm yields a sign choice with

\[
\|C_\epsilon\|\ge\frac12\|O\|>\frac{1559}{3200}.
\]

For the associated physical partition of the coordinates of `B`,

\[
C_\epsilon=\begin{pmatrix}0&N\\N^T&0\end{pmatrix}
\]

and hence `\|N\|=\|C_\epsilon\|`. This proves (5).

All partitions here are of original coordinates. No rotated coordinate is treated as an independent random variable, no coefficient tail is deleted from the actual quadratic form in a probabilistic argument, and the conclusion is deterministic coefficient geometry.

## Remaining exact obligation for `17 -> 16`

The second physical crossing (5) by itself does not yet force order-five exterior volume across a single full cut. It may align with the four-dimensional left/right carrier of `M_4` after the necessary physical repartition. A valid 16-eigenvalue theorem now needs one of the following, with explicit constants:

- a physical paving/transversality lemma showing that some repartition preserves a quantitative portion of `Z_4(M)` while the second crossing contributes a fifth exterior direction; or
- a direct endpoint receiver for this rank-four-plus-second-crossing geometry that retains arbitrary same-bank quadratic terms and rough product laws.

The leverage-free determinant envelope alone cannot supply this step: order four remains the non-integrable `|t|^{-1}` endpoint.
