# Global augmented candidate and the signed-opening obstruction

All logarithms in the mathematical statements are base two. Put

\[
q(t)=t\log_2(1/t)+\frac{2t}{\ln2},\qquad
\Phi(f)=\sum_i q(\widehat f(\{i\})^2),
\]

\[
L_{c,\eta}(f)=M(f)+(1+\eta)U(f)-cI(f),
\qquad M=G-B.
\]

The reviewed signed-mismatch reduction says that universal
`L_{c,eta}<=0` implies

\[
G\le(c+2)I+(1-\eta)U. \tag{1}
\]

We freeze `eta=1` and the reviewer-strengthened fresh-activation constant

\[
c_\dagger=\frac{29}{2}+\frac2{\ln2}. \tag{2}
\]

Thus the global augmented candidate

\[
\boxed{L_{c_\dagger,1}(f)+2\Phi(f)\le0} \tag{GA}
\]

would imply universal GU with

\[
(a,b)=\left(\frac{33}{2}+\frac2{\ln2},0\right) \tag{3}
\]

and hence

\[
H(f)\le\left(35+\frac4{\ln2}\right)I(f). \tag{4}
\]

No assertion that (GA) is proved is made here.

## 1. Bounded stress test of (GA)

`CHECK_GLOBAL_AUGMENTED.py` computes exact rational Walsh coefficients and
influence and floating entropies. It found no positive residual among all
Boolean functions through four variables (complement symmetry fixed), 700
seeded random functions on dimensions five through nine, and point defects,
dictators, and parities through dimension twelve. The largest nonconstant
residual was `-0.0930761265...`; the finite test is diagnostic only and is
not evidence of a universal theorem.

## 2. Exact orbit identity for activation

For a live physical block `X`, let

\[
E_X^f(S)=\sum_{A\subseteq X}\widehat f(S\cup A)^2
\]

and use the independently reviewed orbit potential

\[
\Theta_X(f)=\sum_{x\in X}q(\operatorname{Inf}_x(f))
+\sum_{i\notin X}q(E_X^f(\{i\})). \tag{5}
\]

Let `A(f)` be the fresh fair activation with selector `z`, let
`m=E f`, and put `J=(1-m)/2`. Define

\[
D_X(f)=\sum_{x\in X}\operatorname{Inf}_x(f)
+\sum_{i\notin X}E_X^f(\{i\}). \tag{6}
\]

Because `Inf_z(Af)=J`, every old physical influence and every old orbit
energy is halved. The exact scalar identity

\[
q(t/2)=\frac12q(t)+\frac t2
\]

therefore gives

\[
\boxed{
\Theta_{X\cup\{z\}}(Af)
=q(J)+\frac12\Theta_X(f)+\frac12D_X(f).} \tag{7}
\]

This is the exact whole-orbit analogue of the singleton identity. The new
linear term `D_X/2` is absent in the fresh singleton calculation.

## 3. Refutation of the positive orbit lift

The direct attempt to extend the fresh invariant is

\[
\boxed{
L_{c_\dagger,1}(Af)+2\Theta_{X\cup\{z\}}(Af)
\le\frac12\{L_{c_\dagger,1}(f)+2\Theta_X(f)\}.} \tag{POL}
\]

The exact activation recurrence writes its left-minus-right residual as

\[
\mathcal R(f,X)=
\sum_iP(m,a_i)+3R(m)-B_z(m)-c_\dagger J
+2q(J)+D_X(f), \tag{8}
\]

where `a_i=fhat({i})` and `P,R,B_z` are the source-reviewed scalar
activation terms.

Take the genuine three-bit point defect: `f=-1` at one vertex and `+1`
elsewhere, with `X` all three coordinates. Then

\[
m=\frac34,\quad J=\frac18,\quad
a_i=-\frac14,\quad D_X(f)=I(f)=\frac34. \tag{9}
\]

Exact rational-log simplification gives

\[
\begin{aligned}
(\ln2)\mathcal R(f,X)
={}&\frac14+\frac{495}{32}\ln2+\frac{27}{8}\ln3\\
&-\frac{85}{16}\ln5-\frac{49}{16}\ln7.
\end{aligned} \tag{10}
\]

`CERTIFY_ORBIT_LIFT.py` encloses every logarithm by an exact rational
atanh series with an explicit rational tail. It certifies

\[
(\ln2)\mathcal R>0.1704481822534689,
\qquad
\boxed{\mathcal R>0.2459047472656179\text{ bits}.} \tag{11}
\]

Therefore (POL) is **REFUTED**. The failure is not numerical, does not use
an arbitrary spectral law, and does not refute (GA), GU, or FEI. It proves
that replacing the fresh singleton packet by a positive orbit packet loses
the signed opening refund even at rank three.

The point-defect family also diagnoses the scale: if the coefficient `2`
in (POL) is replaced by any fixed positive `lambda`, the exact orbit part
contains

\[
\lambda q(2^{-r})+\frac\lambda2 r2^{1-r},
\]

whose ratio to `I=r2^{1-r}` retains a nonvanishing charge while the root
opening itself grows logarithmically relative to influence. This is why a
positive memoryless orbit potential is the wrong mechanism.

## 4. Strictly smaller signed unpaid inequality

The reviewed signed-orbit theorem supplies, at every physical restriction
node `v`, an opening `O_v`, reveal credit `R_v`, and the exact complete-tree
identity

\[
\sum_vw_v(R_v-O_v)=\Phi(f). \tag{12}
\]

This isolates the following sufficient criterion.

> **SIGNED-ORBIT-L-DRIFT (`SOLD(c)`).** Every nonconstant genuine Boolean
> `f` admits a complete physical restriction tree and adapted active blocks
> such that at every internal node
> \[
> \Delta_{x_v}L_{c,1}(f_v)+2(R_v-O_v)\le0. \tag{13}
> \]

Summing (13) with path probabilities, all terminal functions being
constants, gives

\[
L_{c,1}(f)+2\Phi(f)\le0. \tag{14}
\]

Thus `SOLD(c_dagger)` proves (GA), the explicit GU pair (3), and the FEI
constant (4). Unlike (POL), (13) keeps the indispensable negative opening
term and the terminal reserve. It is the precise smaller unpaid inequality
left by this run; it has not been proved.

Constants have `I=U=G=Phi=0` and satisfy all endpoint statements without
division by influence.

