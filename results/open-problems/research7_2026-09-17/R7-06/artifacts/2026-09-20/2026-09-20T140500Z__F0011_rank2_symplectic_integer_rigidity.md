# F0011 — rank-two symplectic support: integer rigidity, Pythagorean quotient, and endpoint exclusion

Date: 2026-09-20 UTC  
Role: C05 / R7-06 `Random Matrix Spectral Entropy`  
Canonical target: F0011 / Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4  
Status: **PROVED PARTIAL** toward the outside source, pending later independent review

## 1. Source target and inherited bottleneck

Vu's Conjecture 9.4 concerns the symmetric Rademacher matrix `M_n^sym`, with independent fair signs on and above the diagonal:

\[
\Pr\bigl(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z\bigr)
=2^{-(1/2+o(1))n^2}.
\]

Equivalently, the total number of labelled symmetric sign matrices with integral spectrum should be `2^{o(n^2)}`. The source quantifier is the total integral-spectrum event, not a fixed spectrum.

The active C05 line is a restricted centered two-eigenvalue bridge. In the inherited `|r-\lambda|=4`, `q=o(r)`, `q>4` shell, the contrast cores satisfy

\[
T,S\in\{-1,0,1\}^{d\times d},\qquad TS=ST=sI_d,
\]

with

\[
d=r-q,\qquad s=\frac r4-\varepsilon,\qquad \varepsilon\in\{+1,-1\},
\]

and

\[
D:=T-S^T,\qquad \operatorname{rank}_{\mathbb R}D=o(r).
\]

After one common-support perfect-matching normalization, `diag D=0`. The preceding C05 run showed that a pure mod-two attack cannot close the remaining orientation entropy: for `d=2m`, the fixed rank-two defect support

\[
E=\begin{pmatrix}0&J_m\\J_m&0\end{pmatrix}
\]

admits `2^{d^2/2-O(d)}` solutions of the finite-field equation `X+X^{-T}=E`.

The purpose of this note is to restore the **integer** two-sided inverse equations on exactly that symplectic support and determine what survives. The conclusion is a sharp rigidity theorem: the integer lifts collapse to a two-class equitable design with a Pythagorean quotient. Moreover, the easiest weighing-matrix endpoint is incompatible with the actual `q=o(r)` anchor geometry.

---

## 2. Rank-two signed defects on the complete two-block support

Assume `d=2m` and

\[
D=\begin{pmatrix}0&P\\Q&0\end{pmatrix},
\qquad P,Q\in\{\pm1\}^{m\times m},
\qquad \operatorname{rank}_{\mathbb R}D=2.
\tag{2.1}
\]

Because the row and column spaces of the two off-diagonal blocks occupy disjoint coordinate halves,

\[
\operatorname{rank}D=\operatorname{rank}P+\operatorname{rank}Q.
\]

Both blocks are nonzero, hence

\[
\boxed{\operatorname{rank}P=\operatorname{rank}Q=1.}
\tag{2.2}
\]

Every rank-one sign matrix factors as an outer product of sign vectors. Therefore there exist diagonal sign matrices `R_1,R_2,C_1,C_2` such that, with

\[
R=\operatorname{diag}(R_1,R_2),\qquad C=\operatorname{diag}(C_1,C_2),
\]

we have

\[
RDC=\begin{pmatrix}0&J_m\\J_m&0\end{pmatrix}.
\tag{2.3}
\]

The transformation

\[
T\mapsto RTC,\qquad S\mapsto CSR
\tag{2.4}
\]

preserves `TS=ST=sI` and sends `D=T-S^T` to `RDC`. Hence, for the core classification, we may assume from now on that

\[
\boxed{D=\begin{pmatrix}0&J\\J&0\end{pmatrix}.}
\tag{2.5}
\]

This normalization is only an internal equivalence of the contrast-core equations. When the core is required to lift back to the original C05 anchor system, the inherited row/column partition structure must still be imposed; Section 7 does exactly that.

---

## 3. New theorem I — exact block regularity forced by the integer inverse equations

Write

\[
T=\begin{pmatrix}A&B\\C&F\end{pmatrix},
\tag{3.1}
\]

with `m x m` blocks. Since `D=T-S^T`,

\[
S=(T-D)^T.
\]

The equation `TS=sI` is therefore

\[
TT^T-TD=sI.
\tag{3.2}
\]

Because `TT^T` is symmetric, `TD` must be symmetric. Using (2.5),

\[
TD=
\begin{pmatrix}
BJ&AJ\\FJ&CJ
\end{pmatrix}.
\tag{3.3}
\]

Let `1` denote the all-ones vector in `R^m`. Put

\[
b=B1,\quad a=A1,\quad f=F1,\quad c=C1.
\]

Then `BJ=b1^T`, etc. Symmetry of (3.3) gives

\[
\boxed{
B1=\beta1,\qquad C1=\gamma1,
\qquad A1=F1=\alpha1
}
\tag{3.4}
\]

for integers `\alpha,\beta,\gamma`.

The reverse equation `ST=sI` gives

\[
T^TT-DT=sI,
\tag{3.5}
\]

so `DT` is symmetric. The same calculation on columns yields

\[
\boxed{
1^TB=\beta1^T,\qquad 1^TC=\gamma1^T,
\qquad 1^TA=1^TF=\alpha1^T.
}
\tag{3.6}
\]

Thus every block is regular on both sides. In the binary-support normalization coming from the inherited C05 core, the off-diagonal defect cells split between `T` and `S^T`; after (2.5) this means

\[
\boxed{B,C\in\{0,1\}^{m\times m}.}
\tag{3.7}
\]

Consequently

\[
0\le\beta,\gamma\le m.
\tag{3.8}
\]

The diagonal blocks `A,F` are ternary and have common row and column sum `\alpha`.

---

## 4. New theorem II — the entire rank-two quotient lies on one Pythagorean shell

The two-dimensional block-constant subspace

\[
\operatorname{span}\{(1,0),(0,1)\}
\]

is invariant under `T` and `S`. In the unnormalized block-constant basis, the quotient matrices are

\[
Q_T=
\begin{pmatrix}
\alpha&\beta\\
\gamma&\alpha
\end{pmatrix},
\tag{4.1}
\]

and, because `S=(T-D)^T`,

\[
Q_S=
\begin{pmatrix}
\alpha&\gamma-m\\
\beta-m&\alpha
\end{pmatrix}.
\tag{4.2}
\]

Since `TS=sI`,

\[
Q_TQ_S=sI_2.
\tag{4.3}
\]

The off-diagonal entries and the difference of the diagonal entries give

\[
\alpha(\beta+\gamma-m)=0,
\tag{4.4}
\]

\[
(\beta-\gamma)(\beta+\gamma-m)=0.
\tag{4.5}
\]

If `\beta+\gamma\ne m`, then (4.4)--(4.5) force `\alpha=0` and `\beta=\gamma`; but then the first diagonal equation gives

\[
s=\beta(\beta-m)\le0,
\]

contradicting `s>0`. Hence

\[
\boxed{\beta+\gamma=m.}
\tag{4.6}
\]

The diagonal equation becomes

\[
\boxed{\alpha^2=s+\beta\gamma.}
\tag{4.7}
\]

Equivalently, with `\delta:=\beta-\gamma`,

\[
\boxed{
\delta^2+(2\alpha)^2=m^2+4s,
\qquad \delta\equiv m\pmod2.
}
\tag{4.8}
\]

Therefore the quotient parameters are not free. They lie on one integral circle. In particular, the number of possible triples `(\alpha,\beta,\gamma)` is at most the number `r_2(m^2+4s)` of representations of `m^2+4s` as a sum of two squares. Hence

\[
\boxed{
\#\{(\alpha,\beta,\gamma)\}
\le r_2(m^2+4s)
\le4\tau(m^2+4s)
=m^{o(1)}.
}
\tag{4.9}
\]

So the full `2^{\Theta(d^2)}` symplectic freedom from the mod-two shadow cannot survive in the **quotient**: all integer lifts land in a subpolynomial list of two-class quotient parameters.

---

## 5. Exact group-divisible Gram equations

From (3.2) and (3.4),

\[
TT^T
=sI+TD
=sI+
\begin{pmatrix}
\beta J&\alpha J\\
\alpha J&\gamma J
\end{pmatrix}.
\tag{5.1}
\]

Thus

\[
\boxed{AA^T+BB^T=sI+\beta J,}
\tag{5.2}
\]

\[
\boxed{CC^T+FF^T=sI+\gamma J,}
\tag{5.3}
\]

\[
\boxed{AC^T+BF^T=\alpha J.}
\tag{5.4}
\]

Likewise, from (3.5)--(3.6),

\[
T^TT
=sI+
\begin{pmatrix}
\gamma J&\alpha J\\
\alpha J&\beta J
\end{pmatrix},
\tag{5.5}
\]

so

\[
\boxed{A^TA+C^TC=sI+\gamma J,}
\tag{5.6}
\]

\[
\boxed{B^TB+F^TF=sI+\beta J,}
\tag{5.7}
\]

\[
\boxed{A^TB+C^TF=\alpha J.}
\tag{5.8}
\]

Therefore the integer lifts of the fixed symplectic defect are exactly two-class group-divisible / weighing-type systems with a rank-two quotient. On the codimension-two subspace

\[
1^\perp\oplus1^\perp,
\]

the `J` terms vanish and `T` is an exact `\sqrt{s}`-scaled isometry.

This is the structural replacement for the failed mod-two-only attack: the symplectic plateau does not disappear, but over the integers it can only occur inside a sharply constrained group-divisible design system.

---

## 6. Endpoint recursion — what the easiest integer lifts would look like

Suppose `\beta=0`. Then by (4.6), `\gamma=m`. Since `B,C` are binary and regular,

\[
B=0,\qquad C=J.
\tag{6.1}
\]

Equation (4.7) gives

\[
\alpha^2=s.
\tag{6.2}
\]

From (5.2)--(5.7),

\[
\boxed{AA^T=A^TA=sI,\qquad FF^T=F^TF=sI.}
\tag{6.3}
\]

Thus `A` and `F` are regular weighing matrices `W(m,s)` with common row and column sum `\alpha=\pm\sqrt{s}`. Conversely, any two such regular weighing matrices give a ternary inverse pair

\[
T=\begin{pmatrix}A&0\\J&F\end{pmatrix},
\qquad
S=\begin{pmatrix}A^T&0\\-J&F^T\end{pmatrix},
\tag{6.4}
\]

satisfying

\[
TS=ST=sI,
\qquad
T-S^T=
\begin{pmatrix}0&J\\J&0\end{pmatrix}.
\tag{6.5}
\]

The case `\beta=m,\gamma=0` is the transposed analogue.

Therefore the full integer inverse equation by itself does **not** turn the dense rank-two defect into a trivial fiber: at the quotient endpoint it recursively contains regular weighing-matrix problems. This is an explicit warning against claiming that low real rank plus integer biorthogonality alone gives subquadratic root entropy.

However, the actual C05 shell contains additional anchor geometry. That geometry excludes this endpoint in the near-extremal `q=o(r)` regime.

---

## 7. New theorem III — the actual C05 anchor geometry excludes the weighing endpoint when `q=o(r)`

Return to an admissible core produced from the original C05 sign root. The core rows inherit `q` row-partition labels and the core columns inherit `q` column-partition labels. The anchor masks satisfy

\[
U_{g,h}=C_{g_i,h},
\qquad
V_{g,h}=C_{g,h_j},
\qquad
D=(U-V)/2.
\tag{7.1}
\]

Thus `U` is constant as `g` varies inside one row-partition class, while `V` is constant as `h` varies inside one column-partition class.

Assume the support of `D` is the two-half pattern of Section 2. Refine each inherited row block and each inherited column block by the two half-memberships. This produces at most `2q` refined row classes in each half and at most `2q` refined column classes.

On an `E=0` product of one refined row class and one refined column class, `U=V` everywhere. Since `U` depends on the row class and the column coordinate, while `V` depends on the row coordinate and the column class, equality throughout the Cartesian product forces the common sign to be constant on that product. After the signed row/column normalization used in Section 2, this becomes a separable sign pattern

\[
\text{row sign}\times\text{column sign}\times\text{block sign}.
\tag{7.2}
\]

Consequently, for two rows in the same refined row class, the product of their signs on every common `E=0` nonzero coordinate is one fixed sign, independent of the column.

Now suppose the endpoint `\beta=0` or `\beta=m` holds. Section 6 shows that the top-left block `A` is an exact weighing matrix `W(m,s)`. Hence distinct rows of `A` are orthogonal. For two rows in the same refined row class, their inner product is, by (7.2), plus or minus the number of columns on which both are nonzero. Orthogonality therefore forces **disjoint supports**.

Every row of `A` has exactly `s` nonzero entries among `m` columns. Hence each refined row class contains at most

\[
\left\lfloor\frac ms\right\rfloor
\tag{7.3}
\]

rows. Since at most `2q` refined classes cover the `m` top-half rows,

\[
\boxed{
m\le2q\left\lfloor\frac ms\right\rfloor.}
\tag{7.4}
\]

For the inherited shell,

\[
m=\frac d2=\frac{r-q}{2},
\qquad
s=\frac r4-\varepsilon.
\tag{7.5}
\]

For `r+2q>12` we have `m<3s`, hence `\lfloor m/s\rfloor\le2` whenever the endpoint exists. Therefore

\[
\boxed{m\le4q.}
\tag{7.6}
\]

Equivalently,

\[
\boxed{q\ge\frac r9.}
\tag{7.7}
\]

Thus the endpoint is impossible throughout the entropy-dangerous regime `q=o(r)` once `r` is large enough. In particular,

\[
\boxed{q=o(r)\quad\Longrightarrow\quad 0<\beta,\gamma<m}
\tag{7.8}
\]

for any admissible C05 lift with the complete two-block rank-two defect support.

This is the point at which the actual anchor geometry materially strengthens the abstract ternary inverse problem: the obvious regular-weighing recursion exists algebraically, but it cannot occur inside the asymptotic C05 branch.

---

## 8. Consequence for the previous symplectic counterfamily

The preceding run constructed a fixed rank-two, zero-diagonal, half-dense defect with a symplectic group of size

\[
2^{d^2/2-O(d)}
\]

in the mod-two equation. The present theorem shows exactly what a genuine integer lift on that support must satisfy:

1. after sign equivalence, the defect is `[[0,J],[J,0]]`;
2. all four `m x m` blocks of `T` have constant row and column sums;
3. the two cross degrees obey `\beta+\gamma=m`;
4. the quotient lies on the integral circle
   \[
   (\beta-\gamma)^2+(2\alpha)^2=m^2+4s;
   \]
5. the full blocks satisfy the group-divisible Gram identities (5.2)--(5.8);
6. the easiest weighing endpoint is excluded by the actual `q=o(r)` anchor geometry.

So the huge finite-field symplectic stabilizer is **not** a valid model for the integer C05 fiber. Any surviving quadratic entropy would have to live in the interior group-divisible fibers with

\[
1\le\beta,\gamma\le m-1
\]

and with only `m^{o(1)}` allowed quotient triples.

This does not yet prove that those interior fibers are `2^{o(r^2)}`. They are the next precise obstruction.

---

## 9. Next attack

The strongest next theorem is now narrower than in the previous run:

> Count the interior two-class systems (5.2)--(5.8), with `\beta+\gamma=m`, `\alpha^2=s+\beta\gamma`, blockwise anchor-sign coherence, and the inherited `q=o(r)` partition complexity.

Two concrete attacks are now available.

* **Interior overlap rigidity.** Inside one refined anchor row class, the blockwise sign coherence converts the top-half row Gram equation into a constant-intersection statement. Combine the corresponding column statement and the Pythagorean quotient constraint to force either a bounded-size association scheme or a smaller recursive design.
* **Quotient-first anti-concentration.** There are only `m^{o(1)}` quotient triples. Condition on one triple and expose the regular binary cross blocks `B,C`; then use the signed equations for `A,F` to seek an entropy loss depending on the number of independent refined anchor classes rather than on raw rank alone.

The bounded-rank Gram-defect branch, higher arithmetic shells, indefinite defects, the full centered two-eigenvalue count, and finally Vu's total integral-spectrum conjecture remain open.

No small-order census is used here.