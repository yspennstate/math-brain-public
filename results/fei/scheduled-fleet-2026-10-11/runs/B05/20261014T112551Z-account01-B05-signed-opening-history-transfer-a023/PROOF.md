# Signed-opening history transfer at one activation node

All logarithms are in bits. Put

\[
q(t)=t\log_2(1/t)+\frac{2t}{\ln2},\qquad
\Phi(f)=\sum_iq(\widehat f(\{i\})^2),
\]

\[
L_{c,\eta}(f)=M(f)+(1+\eta)U(f)-cI(f),
\qquad M=G-B.
\]

We use the independently reviewed half-packet invariant at its producer
constant

\[
c_*=\frac{29}{2}+\frac4{\ln2}. \tag{1}
\]

For every Boolean core `f`, its fresh fair activation `F=A(f)`, and every
`0<eta<=1`,

\[
\boxed{L_{c_*,\eta}(F)+2\Phi(F)
\le\frac12\{L_{c_*,\eta}(f)+2\Phi(f)\}.} \tag{2}
\]

The aim is to remove the empty-history assumption at this activation node.

## 1. Orbit potential and domination

For a set `X` of core physical coordinates, write

\[
E_X^f(S)=\sum_{A\subseteq X}\widehat f(S\cup A)^2
\]

and use the reviewed orbit potential

\[
\Theta_X(f)=\sum_{x\in X}q(\operatorname{Inf}_x f)
+\sum_{i\notin X}q(E_X^f(\{i\})). \tag{3}
\]

Since `q` is increasing,

\[
\boxed{\Phi(f)\le\Theta_X(f)}. \tag{4}
\]

Indeed, for `x in X`,
`fhat({x})^2<=Inf_x(f)`. For `i notin X`, the orbit energy
`E_X^f({i})` contains `fhat({i})^2` as one nonnegative summand.

## 2. Exact signed node terms

Let `z` be the activation selector, so the two restrictions of `F` are the
core `f` and a constant. At this physical selector node take:

- inherited block `Y=empty`;
- active block `Z=X union {z}`;
- queried coordinate `z`.

The signed-orbit opening and reveal terms are

\[
O=\Theta_Z(F)-\Phi(F), \tag{5}
\]

\[
R=\Theta_Z(F)-\frac12\Theta_X(f), \tag{6}
\]

because the constant child has zero potential. Therefore the whole orbit
packet cancels exactly:

\[
\boxed{R-O=\Phi(F)-\frac12\Theta_X(f).} \tag{7}
\]

No positive part of `O` or `R` is taken. The root opening is retained with
its sign.

## 3. History-transfer theorem

Combining (2), (4), and (7) gives

\[
\begin{aligned}
\Delta_zL_{c_*,\eta}(F)+2(R-O)
&=L_{c_*,\eta}(F)-\frac12L_{c_*,\eta}(f)
  +2\Phi(F)-\Theta_X(f)\\
&\le\Phi(f)-\Theta_X(f)\\
&\le0.
\end{aligned} \tag{8}
\]

Hence:

\[
\boxed{
\Delta_zL_{c_*,\eta}(A(f))+2(R-O)\le0
\quad\text{for every Boolean }f,\ X,\ 0<\eta\le1.} \tag{9}
\]

This is dimension-, depth-, bias-, and block-size-independent. The block
`X` may contain arbitrary reused core coordinates. The selector remains a
fresh fair coordinate.

## 4. Complete-tree implication

Define the signed local criterion at a physical restriction node `v` by

\[
\Delta_{x_v}L_{c_*,\eta}(f_v)+2(R_v-O_v)\le0. \tag{SOLD}
\]

Suppose a core `f` has a complete adapted physical restriction tree whose
root inherits block `X` and satisfies (SOLD) at every internal core node.
Prepend the selector node described above. Equation (9) pays that new node,
and the core branch inherits exactly `X`. Thus `A(f)` has a complete paid
tree with empty root history.

On a complete tree, the ordinary restriction telescope for `L` and the
reviewed signed-orbit identity give

\[
L_{c_*,\eta}(F)+2\Phi(F)\le0. \tag{10}
\]

At `eta=1`, the reviewed signed-mismatch reduction then yields

\[
G(F)\le(c_*+2)I(F)
=\left(\frac{33}{2}+\frac4{\ln2}\right)I(F), \tag{11}
\]

and Theorem G gives

\[
H(F)\le\left(35+\frac8{\ln2}\right)I(F). \tag{12}
\]

This is a genuine history-transfer theorem, not universal closure: the
remaining unpaid statement is existence of the inherited-`X` core tree.
The result removes the cost of opening an arbitrary reused block at one
outer fair activation node, but it does not pay later data queries or
biased/nonfresh selector nodes.

Constants have all functionals zero and require no division by influence.

