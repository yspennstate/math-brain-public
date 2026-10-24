# QFORM-S16-TRANSVERSE-PHYSICAL-CROSSING-v1

Run: `20260924T125751Z-account03-B20-fixedmult-r2`.

Status: **proved deterministic strengthening of the current `s_16` endpoint geometry; no 16-eigenvalue density theorem claimed.**

This starts from the completed account01/B20 `QFORM-S16-ORDER4-PLUS-SECOND-PHYSICAL-CROSSING-v1` branch. In the unpaid no-pivot chamber it supplies a physical cut `[n]=I sqcup J`, crossing `M=A[I,J]`, and its top-four singular-value truncation `M_4` such that, with

\[
B=A[I,I],\qquad C=A[J,J],\qquad
A_0=\begin{pmatrix}B&M_4\\ M_4^T&C\end{pmatrix},
\]

one has

\[
s_{16}(A_0)\ge \alpha:=\frac{63}{64}.
\tag{1}
\]

The same branch retains the manuscript no-pivot condition

\[
|A_{ii}|<\eta:=\frac1{100}.
\tag{2}
\]

The earlier result extracted a large same-bank physical crossing but left open whether it could align with the four-dimensional carrier of `M_4`. The lemma below shows that pure alignment is impossible: one same-bank block has four strong directions whose **domain and output are transverse to the rank-four carrier**, and a literal original-coordinate internal crossing inherits a quantitative transverse packet.

## Theorem

Let

\[
U=\operatorname{Ran}(M_4)\subset\mathbb R^I,
\qquad
V=\operatorname{Ran}(M_4^T)\subset\mathbb R^J,
\]

and let `P_U,P_V` denote the corresponding orthogonal projections. Then at least one of the following holds:

\[
\boxed{s_4\bigl(B(I-P_U)\bigr)\ge\frac{63}{64}}
\tag{3I}
\]

or

\[
\boxed{s_4\bigl(C(I-P_V)\bigr)\ge\frac{63}{64}.}
\tag{3J}
\]

Because `B,C` are symmetric, the same alternative holds on the output side:

\[
s_4((I-P_U)B)\ge63/64
\quad\text{or}\quad
s_4((I-P_V)C)\ge63/64.
\tag{4}
\]

Suppose for definiteness the `B` alternative holds and put `O=B-diag(B)`. Then there is a physical coordinate partition `I=I_1 sqcup I_2`, with coordinate projections `Q_1,Q_2`, such that

\[
\boxed{
\|(I-P_U)\,[Q_1BQ_2+Q_2BQ_1]\|_{op}
\ge \frac{1559}{3200}=0.4871875
}
\tag{5}
\]

and

\[
\boxed{
\|(I-P_U)\,[Q_1BQ_2+Q_2BQ_1]\|_{F}
\ge \frac{1559}{1600}=0.974375.
}
\tag{6}
\]

Consequently, for at least one orientation `(a,b)=(1,2)` or `(2,1)`, there is a literal original-coordinate crossing `Q_a B Q_b` satisfying

\[
\boxed{
\|(I-P_U)Q_aBQ_b\|_{op}
\ge \frac{1559}{6400}=0.24359375,
}
\tag{7}
\]

and (possibly for the other orientation)

\[
\boxed{
\|(I-P_U)Q_aBQ_b\|_F
\ge \frac{1559}{3200}=0.4871875.
}
\tag{8}
\]

The identical conclusion holds with `C,V` if the `C` alternative in (3J) is the one that fires.

All coordinate partitions in (5)--(8) are literal subsets of the original independent coordinates. `P_U,P_V` are used only as deterministic coefficient-space projectors; no rotated random coordinates are declared independent.

## Proof

Set

\[
D=B\oplus C,
\qquad
K=\begin{pmatrix}0&M_4\\M_4^T&0\end{pmatrix},
\qquad
A_0=D+K.
\]

Let

\[
W=U\oplus V,
\qquad P_W=P_U\oplus P_V.
\]

Since `rank(M_4)<=4`,

\[
\dim W\le8.
\tag{9}
\]

Moreover `K=KP_W`: the off-diagonal rank-four carrier annihilates `U^perp` on the `I` side and `V^perp` on the `J` side. Hence

\[
A_0
=D(I-P_W)+(DP_W+K)
=D(I-P_W)+A_0P_W.
\tag{10}
\]

The second summand has rank at most `dim W<=8`. Apply the manuscript's approximation-number/rank inequality with `j=8` and `q=8` to (10):

\[
s_{16}(A_0)\le s_8\bigl(D(I-P_W)\bigr).
\tag{11}
\]

Combining (1) and (11),

\[
s_8\bigl(D(I-P_W)\bigr)\ge\frac{63}{64}.
\tag{12}
\]

But

\[
D(I-P_W)
=
B(I-P_U)\oplus C(I-P_V).
\tag{13}
\]

The singular values of a block-diagonal direct sum are the union of the singular values of the two blocks. Thus at least eight singular values across the two blocks in (13) are at least `63/64`; one block therefore contributes at least four. This proves (3I)--(3J).

Assume (3I). Since `B=B^T`,

\[
\bigl(B(I-P_U)\bigr)^T=(I-P_U)B,
\]

so the two matrices have exactly the same singular values and (4) follows.

Let

\[
\Delta=\operatorname{diag}(B),\qquad O=B-\Delta.
\]

By the no-pivot condition (2),

\[
\|\Delta\|<\eta=\frac1{100}.
\]

Singular-value perturbation applied to `(I-P_U)B=(I-P_U)O+(I-P_U)Delta` gives

\[
s_4((I-P_U)O)
\ge \frac{63}{64}-\frac1{100}
=
\frac{1559}{1600}
=:\beta.
\tag{14}
\]

In particular

\[
\|(I-P_U)O\|_{op}\ge\beta,
\qquad
\|(I-P_U)O\|_F\ge2\beta,
\tag{15}
\]

the second estimate because at least four singular values are at least `beta`.

Now let `E_epsilon` be a diagonal matrix of independent fair signs on the physical coordinates of `I` and define

\[
C_\epsilon=\frac{O-E_\epsilon O E_\epsilon}{2}.
\tag{16}
\]

Because `O` has zero diagonal, `E C_epsilon=O/2`. Therefore

\[
\frac12(I-P_U)O
=
\mathbb E_\epsilon[(I-P_U)C_\epsilon].
\]

Convexity of both the operator and Frobenius norms, together with (15), gives a sign choice for which

\[
\|(I-P_U)C_\epsilon\|_{op}\ge\beta/2
=\frac{1559}{3200},
\tag{17}
\]

and (possibly after choosing a sign pattern that maximizes the Frobenius norm)

\[
\|(I-P_U)C_\epsilon\|_F\ge\beta
=\frac{1559}{1600}.
\tag{18}
\]

For any fixed sign pattern, let `I_1,I_2` be its positive and negative coordinate classes, with coordinate projections `Q_1,Q_2`. Since the sign commutator keeps exactly the entries crossing the sign partition,

\[
C_\epsilon=Q_1BQ_2+Q_2BQ_1.
\tag{19}
\]

Equations (17)--(19) prove (5) and (6), allowing different optimizing sign patterns for the two displayed norm conclusions if necessary.

Finally use the triangle inequality:

\[
\|(I-P_U)C_\epsilon\|
\le
\|(I-P_U)Q_1BQ_2\|
+
\|(I-P_U)Q_2BQ_1\|.
\]

For the operator norm and (17), one orientation is at least `beta/4=1559/6400`, proving (7). For the Frobenius norm and (18), one orientation is at least `beta/2=1559/3200`, proving (8). The `C,V` case is identical.

## What this closes and what remains

This removes the weakest form of the alignment obstruction in the account01/B20 `s_16` endpoint: the second same-bank resource cannot live entirely inside the top-four crossing carrier. There is a fixed-size physical internal crossing with a quantitatively nonzero component transverse to that carrier.

What remains is a **physical localization / side-balance step**. To turn (7) or (8) into a fifth exterior direction of one valid physical cut, one must retain a quantitative portion of the original order-four crossing after moving one side of the internal partition across the cut. Global transversality to `U` alone does not automatically imply transversality to the restricted carrier `Q_a U`; a vector can be globally far from `U` yet lie in `Q_aU` after coordinate restriction. Thus no order-five volume or `s_16` density theorem is claimed here.

The next exact implication is therefore:

`QFORM-S16-TRANSVERSE-PACKET-PLUS-ORDER4-PHYSICAL-LOCALIZATION-v1` — prove that either a repartition keeps enough order-four volume while the packet (7)/(8) supplies a fifth exterior direction, or route the carrier-concentrated side directly to an existing pivot/low-dimensional endpoint receiver.
