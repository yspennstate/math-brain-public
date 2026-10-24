SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-23T18:19:04Z.
attacking: the ultra-thin two-single-hub survivor; convert the robust opposite-star/cofactor packet into a weighted curved-fiber bound or a sharper finite-hub reduction without dropping the nonzero tail.

# Early substantive calculation: reciprocal anchoring after one-hub projection

Work in the r40 survivor. Let the literal physical cross block be

\[
N=\begin{pmatrix}b&r^T\\ c&D\end{pmatrix},\qquad
E=\|N\|_F^2>11907/16384,
\]

with row anchor `i`, column anchor `a`, `|b|<1/32`, row/column determinant-pair inclusion marginals both `>3/5`, and full two-volume `Z2=e_2(N^TN)>(31/2048)E^2`. Put `m=(b,r)` and

\[
C=N[i^c,K](I-P_m),\quad M^2=\|m\|^2,\quad S=\|C\|_F^2.
\]

For each remaining physical row `y`, write `z=y(I-P_m)`. Cauchy--Binet/Lagrange gives the exact aggregate identity

\[
M^2S=\sum_{j\ne i}\sum_{|T|=2}\det N[\{i,j\},T]^2=\alpha_i Z_2.
\]

Thus `S>(93/10240)E>1107351/167772160` because `alpha_i>3/5` and `M^2<=E`.

Let

\[
Z_{ia}=\sum_{j\ne i,\,\beta\ne a}
       \det N[\{i,j\},\{a,\beta\}]^2.
\]

The joint determinant-pair law has `P(i in S)>3/5` and `P(a in T)>3/5`; hence if `theta=Z_ia/Z2`, then `theta>alpha_i-2/5`, so

\[
\frac{Z_{ia}}{M^2S}=\frac{\theta}{\alpha_i}>\frac13.
\]

Now use `z\perp m`. The anchored minor vector from the row `z` is

\[
f=bz_{K\setminus\{a\}}-z_a r.
\]

Since `r dot z_tail=-b z_a`,

\[
\|f\|^2=b^2\|z\|^2+M^2 z_a^2.
\]

Summing rows proves the exact new identity

\[
\boxed{Z_{ia}=b^2S+M^2\|Ce_a\|_2^2.}
\]

The r40 star floor is

\[
M^2>\frac{226233}{33554432}.
\]

Therefore

\[
\frac{\|Ce_a\|_2^2}{S}
>\frac13-\frac{b^2}{M^2}
>\frac13-\frac{32768}{226233}
=\frac{42643}{226233}
=0.1884915109\ldots .
\]

This is already a weighted, product-preserving replacement for selecting one minor: at least 18.849% of the entire row-projected crossing energy lands on the literal opposite physical anchor.

Next use the completed account03/B01 one-hub projected-E2 theorem. At threshold `epsilon=2^-24`, if `e_2(CC^T)>=epsilon`, then the full ambient form has a continuous density with

\[
\|p_Q\|_\infty
<9.4\,(M^2\epsilon)^{-1/6}<347.
\]

Otherwise let `y_1>=y_2>=...` be the squared singular values of `C` and `tau=sum_{k>=2}y_k`. Since

\[
S^2=\sum y_k^2+2e_2(CC^T)\le y_1S+2\epsilon,
\]

we get

\[
\tau<\frac{2\epsilon}{S}<\frac{20}{1107351}=1.80612\cdot10^{-5},
\qquad
\frac\tau S<0.002736399.
\]

If `v_1` is the leading right singular vector of `C`, then

\[
\|Ce_a\|^2\le y_1 |(v_1)_a|^2+\tau,
\]

so

\[
\boxed{|(v_1)_a|^2>0.1857551,\qquad |(v_1)_a|>0.43099.}
\]

The transpose gives the symmetric statement for the column-projected residual: unless that side is already paid by the same `<347` theorem, its leading residual singular direction has squared mass `>0.1857551` on the original row anchor `i`.

This does not solve QFORM. It sharpens the unpaid ultra-thin branch to two reciprocally anchored, >99.72%-rank-one projected crossings. No small nonzero tail is deleted.
