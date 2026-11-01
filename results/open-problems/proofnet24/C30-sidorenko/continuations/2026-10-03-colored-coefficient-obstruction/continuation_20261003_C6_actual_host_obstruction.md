# An exact obstruction to coefficientwise binary averaging for the Möbius ladder

Status: proved finite counterexample to a proposed method, independently checked. This is neither a counterexample to Sidorenko's conjecture nor a counterexample to total binary averaging monotonicity.

Let H be the ten-vertex Möbius ladder, with five rungs `(x_i,y_i)`, and edges `x_i y_i`, `x_i y_(i+1)`, `y_i x_(i+1)` (indices modulo five). This is isomorphic to the standard ten-cycle with diameter chords. Put G=F₂³, q=8. For two real profiles a,b indexed by integers 0,...,7 (addition is XOR), use the uniform sixteen-point kernel

\[
 W_\tau((t,x),(s,y))=\frac{8}{1524}
       [a_{x+y}+(-1)^{t+s}\tau b_{x+y}],\qquad 0\leq\tau\leq1,
\]

where

\[
 a=(3,3,503,3,3,503,3,503),\qquad
 b=(-1,2,0,2,2,0,-2,0).
\]

The row mean is one, since Σa=1524. Every kernel entry is strictly positive for 0≤τ≤1; its minimum is at least 8/1524. Let C_k denote the coefficient of τ^k in t_H(W_τ). Integration over the first binary coordinate at every source vertex retains exactly the even edge subsets. H has 64 such subsets, with counts 1,5,15,30,13 at sizes 0,4,6,8,10. Hence

\[
 t_H(W_\tau)=C_0+C_4\tau^4+C_6\tau^6+C_8\tau^8+C_{10}\tau^{10}.
\]

The exact coefficient is

\[
 \boxed{C_6=\frac{-809116997184077332220240713482240}{1524^{15}}<0.}
\]

For a compact reproducible identity, index matrices by ordered pairs `(x,y),(u,v)` in G², and abbreviate `i=x+y,j=x+v,k=u+y`. Define

\[
 Z_{xy,uv}=a_i a_j a_k,\quad X_{xy,uv}=b_i b_j b_k,
 \quad Y_{xy,uv}=b_i a_j a_k,\quad V_{xy,uv}=a_i b_j b_k,
\]
\[
 U_{xy,uv}=b_i a_j b_k,\quad T_{xy,uv}=b_i b_j a_k,
 \quad R_{xy,uv}=a_i b_j a_k,\quad S_{xy,uv}=a_i a_j b_k.
\]

The binary-coordinate transfer decomposition has blocks

\[
 Q_0(\tau)=\begin{pmatrix}Z&\tau^3X\\\tau Y&\tau^2V\end{pmatrix},
 \qquad Q_1(\tau)=\begin{pmatrix}\tau^2U&\tau R\\\tau S&\tau^2T\end{pmatrix},
\]

and

\[
 t_H(W_\tau)=\frac{8^5}{1524^{15}}
       [\operatorname{tr}Q_0(\tau)^5+\operatorname{tr}Q_1(\tau)^5].
\]

Expanding these two five-step binary paths gives

\[
 1524^{15} C_6=5\cdot8^5\operatorname{tr}
       [XVYZ^2+(RS)^2U+(SR)^2T].
\]

All entries are integers, so direct multiplication gives an exact certificate without numerical rounding. The attached Python regenerator implements all 64 paths, rather than assuming the displayed three-word formula. A separate independent checker constructs the 64 even masks from the literal 15-edge source and compares both translation-character blocks and full 64×64 quotient transfer matrices; every coefficient agrees.

For completeness, the exact coefficient numerators over the common denominator 1524^15 are:

| k | numerator |
|---|---:|
| 0 | 39231228560119961423656128859391232874555191066624 |
| 4 | 169879744341715336049550281621247098880 |
| 6 | −809116997184077332220240713482240 |
| 8 | 537746541002715694399771115520 |
| 10 | 40523330214299814592512 |

Thus `t_H(W_1)−t_H(W_0)` has the positive numerator

`169878935762464733498263970080119324672`.

The example disproves only the proposed assertion that every total colored even-subset coefficient is nonnegative. The fourth-degree coefficient, total binary averaging, and the unrestricted Möbius-ladder Sidorenko inequality remain separate questions.

Reproducible records:

- `continuation_20261003_C6_actual_host_obstruction.py/.json`: exact integer 64-path regenerator and all coefficients.
- `global_colored_ant_exact_obstruction_check.py/_checks.json`: independent exact source-mask, translation-block, and full-transfer check, without importing the author regenerator.
- `continuation_20261003_global_C6_q8_sphere_search.json`: exploratory numerical search that first identified the shape; it is not used as proof.
