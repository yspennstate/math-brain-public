# account03/B13 r6 improvement — ratio-only three-bank receiver obstruction and exact extremal-product transfer

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T145955Z-account03-B13-fixedmult-audit-r6`.

## 1. A source-valid obstruction at the s8 frontier

### Theorem `QFORM-THREEBANK-RATIO-ONLY-RECEIVER-FALSE-v1`

There is no universal bounded-density theorem whose only quantitative matrix input is the current three-bank determinant ratio
\[
\frac{|\det A[H,T]|\,|\det A[S,H]|}{|\det A[S,T]|}\ge c>0
\]
(or equivalently the uniform nondegeneracy of the Schur-translated pure-triangle `H` curvature), even for cap-one product uniforms and even in the no-pivot regime.

#### Construction

Let `0<epsilon<1/100`. Take three disjoint two-coordinate physical banks `S,H,T`, each uniformly distributed on `[-1/2,1/2]^2`, independently. Put
\[
B=A[S,T]=\epsilon I_2,\qquad
C=A[S,H]=\sqrt\epsilon I_2,\qquad
E=A[H,T]=\sqrt\epsilon I_2,
\]
and set all same-bank blocks to zero. Thus
\[
Q_\epsilon
=2\epsilon S\cdot T
+2\sqrt\epsilon\,(S\cdot H+H\cdot T).
\tag{1}
\]
All six one-dimensional input densities equal one on intervals of length one.

The three determinant scales are
\[
|\det B|=\epsilon^2,\qquad
|\det C|=|\det E|=\epsilon,
\]
so the determinant-ratio certificate is exactly
\[
\boxed{\frac{|\det E|\,|\det C|}{|\det B|}=1.}
\tag{2}
\]
Moreover
\[
P_{H,H}=EB^{-1}C=I_2.
\tag{3}
\]
Hence the standard triangular shear
\[
T'=T+B^{-1}CH,\qquad
S'=S+B^{-T}E^T H
\]
turns the pure triangle into a bilinear term plus the uniformly nondegenerate induced curvature `-2 H^T H`. Thus this example satisfies the strongest local conclusion currently extracted from the s8 determinant chain: the translated pure-triangle curvature is not merely nonsingular but exactly a multiple of the identity.

Nevertheless the output density cannot have a universal bound. Since every coordinate lies in `[-1/2,1/2]`,
\[
|S\cdot T|\le\frac12,\qquad
|S\cdot H|\le\frac12,\qquad
|H\cdot T|\le\frac12,
\]
and therefore, for `epsilon<=1`,
\[
|Q_\epsilon|\le\epsilon+2\sqrt\epsilon\le3\sqrt\epsilon.
\tag{4}
\]
The law is absolutely continuous: condition on `(H,T)`. Except on the null set `H=-sqrt(epsilon)T`, equation (1) is a nonconstant affine linear form of the independent two-dimensional uniform variable `S`, hence has a conditional density; mixing these conditional laws preserves absolute continuity.

Since the entire probability mass lies in an interval of length `6 sqrt(epsilon)`, every density version satisfies
\[
\boxed{
\|p_{Q_\epsilon}\|_\infty\ge\frac1{6\sqrt\epsilon}\longrightarrow\infty.
}
\tag{5}
\]
Finally, all diagonal entries are zero and every principal two-coordinate determinant has modulus at most `epsilon<eta=1/100`, so the family is genuinely in the manuscript's no-`eta`-pivot regime.

#### Consequence

The existing s8 certificate
\[
|\det A[H,T]|\,|\det A[S,H]|
\ge(857233/980000)|\det A[S,T]|
\]
and the associated lower bound on `sigma_min(Sym P[H,H])` cannot by themselves be the hypotheses of the missing receiver. Any valid `9 -> 8` argument must also spend the **global saturation information** (for example the fixed lower bounds on the three rank-two correction pieces, the child-window localization, or another absolute scale) before or together with the triangular shear. The obstruction does not disprove an `s_8` theorem: this six-dimensional family does not satisfy the terminal `s_8(A)>=1` spectral saturation hypotheses.

This also explains why the apparently strong induced `H` curvature after shearing can be misleading: the shear translates `S,T` by `epsilon^{-1/2}H`, and the large bilinear critical term cancels that induced curvature. Product provenance must remain attached through the averaging step.

## 2. Designated account04/B13 theorem applied to the actual fixed-multiplicity slab inequality

The completed account04/B13 no-attainment purification theorem proves, for
\[
\mathcal D=\{f:0\le f\le1,\ \int f=1\}
\]
and every measurable `0<=K<=1`, the exact identity
\[
\sup_{f_1,\ldots,f_n\in\mathcal D}
\int K(x)\prod_i f_i(x_i)\,dx
=
\sup_{\substack{|E_i|=1\\E_i\text{ bounded finite unions}}}
\int_{\prod_iE_i}K(x)\,dx.
\tag{6}
\]
No optimizer, interval extremality, bounded diameter or fixed fragment count is asserted.

Apply (6) to the actual slab kernel
\[
K_J(x)=\mathbf1_{\{x^TAx+b^Tx+c\in J\}}.
\]
Combining it with the independently checked nine-direction theorem in the sibling audit gives, after normalizing `s_9(A)>=1`,
\[
\boxed{
\sup_{f_i\in\mathcal D}\Pr_f\{Q\in J\}
=
\sup_{\substack{|E_i|=1\\E_i\text{ bounded finite unions}}}
|\{x\in\prod_iE_i:Q(x)\in J\}|
<2422\,|J|.
}
\tag{7}
\]
For general density cap `K` and `s_9(A)>=s`, scaling gives `2422 K^2|J|/s`.

This is an equation-level use of the designated partner result on the fixed-multiplicity target, and it preserves arbitrary fragmented product laws exactly.

## 3. Current frontier

The newer invertible-seed overlap-one theorem shows that seven large directions already force either ordinary order-three crossing volume or a fixed positive overlap-one third-order packet. The family above refutes only a **ratio-only s8 receiver**; it does not refute an overlap-one receiver that uses its absolute third-order packet. The first live mathematical obligation is therefore narrower:

> prove a product-preserving overlap-one receiver that retains the common physical anchor through the averaging, or construct a source-valid counterexample satisfying a fixed absolute overlap-one packet.

At present the seven/eight-direction fixed-multiplicity density theorem remains open, as does the unrestricted three-large-eigenvalue conjecture.
