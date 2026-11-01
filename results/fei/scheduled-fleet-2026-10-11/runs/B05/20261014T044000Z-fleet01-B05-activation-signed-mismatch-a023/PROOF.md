# Proof of the fair-activation signed residual identity

All logarithms are base two.  Let `p_S=hat q(S)^2`, `m=hat q(empty)`, and
`p_i=p_{\{i\}}`.  For

\[
A(q)(z,x)=\frac{1+q(x)}2+z\frac{1-q(x)}2,
\]

the Fourier coefficients are

\[
\widehat {A(q)}(S)=\frac{\mathbf1_{S=\varnothing}+\widehat q(S)}2,
\quad
\widehat {A(q)}(S\cup\{z\})=
\frac{\mathbf1_{S=\varnothing}-\widehat q(S)}2.
\tag{1}
\]

## Selector contribution to B

For every nonempty data label `S`, the two selector masses are both `p_S/4`,
so their conditional entropy is `p_S/2`.  The empty-data masses are
`(1+m)^2/4` and `(1-m)^2/4`.  Hence

\[
B_z(A(q))=\frac{1-m^2}{2}
+\frac14T((1+m)^2,(1-m)^2)=B_z(m).\tag{2}
\]

## Data-coordinate contribution to B

Fix `i`.  For an other-data label `S` not containing `i` and `S` nonempty,
the two selector slices together contribute
`(1/2)T(p_S,p_{S\cup\{i\}})`.  The exceptional empty label contributes

\[
\frac14T((1+m)^2,p_i)+\frac14T((1-m)^2,p_i).
\]

Subtracting half the corresponding exceptional child term
`T(m^2,p_i)` gives

\[
B_i(A(q))=\frac12B_i(q)+C_i(m,p_i).\tag{3}
\]

Summing (2)--(3) proves

\[
B(A(q))=\frac12B(q)+B_z(m)+\sum_iC_i(m,p_i).\tag{4}
\]

## G, I, and the residual

The reviewed cap identity is

\[
U(A(q))=\frac12U(q)+R(m).\tag{5}
\]

Restricting a data coordinate commutes with activation, while restricting the
selector gives the constant `1` and the core `q`.  Therefore

\[
G(A(q))=\frac12G(q)+R(m)
+\sum_i\left[R(m)-\frac{R(m_i^+)+R(m_i^-)}2\right].\tag{6}
\]

The data influences are halved, and the selector is pivotal exactly where
`q=-1`, so

\[
I(A(q))=\frac12I(q)+\frac{1-m}{2}.\tag{7}
\]

Since `M=G-B`, subtract (4) from (6), then add `(1+eta)` times (5) and
subtract `c` times (7).  This yields

\[
L_{c,\eta}(A(q))=\frac12L_{c,\eta}(q)
+D_R(q)+(2+\eta)R(m)-B_z(m)-\sum_iC_i(m,p_i)-cJ(m).
\]

This is an identity with no omitted terminal term.

## Exact finite certificate

For mask `56242`, exact Walsh arithmetic gives the displayed four-bit child
statistics and `L_{2,1/4}(q)=0`.  For its activation, every term in `U`, `B`,
and every restricted `U` is a rational coefficient times `log_2(r)` for a
positive rational `r`; `-2I` is written as `(-2I)log_2(2)`.  After collecting
terms and multiplying coefficients by `256`, the residual sign is the sign of
an integer product comparison.  The supplied certificate constructs both
integers exactly and proves the positive side is larger.  Thus
`L_{2,1/4}(A(q))>0` rigorously.

