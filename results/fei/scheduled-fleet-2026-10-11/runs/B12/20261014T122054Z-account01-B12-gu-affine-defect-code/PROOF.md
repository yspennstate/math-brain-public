# Proof: affine defect sets through binary-code deletion and contraction

All logarithms are base two.  Let `V` be an affine subspace of
`F_2^n` of codimension `m>=1`, and put

\[
 f_V(x)=1-2\mathbf1_V(x).
\]

Global signs and translations of `V` do not change any squared Fourier
mass.  Choose a full-rank linear map

\[
 A:F_2^n\longrightarrow F_2^m,
\]

with columns `c_1,...,c_n`, and a target `b`, so that `V={x:Ax=b}`.
The columns may repeat and may be zero; this is the physical reused-variable
representation and no change of input coordinates is made.

## 1. Exact embedded point-defect spectrum

For `y in F_2^m`, write `s(y)=A^T y in F_2^n`.  Since `A` has rank `m`,
`s` is injective.  With

\[
 p_m=(1-2^{1-m})^2,\qquad q_m=2^{2-2m},
\]

the squared Fourier law is

\[
 p_f(0)=p_m,\qquad p_f(s(y))=q_m\quad(y\ne0),       \tag{1}
\]

and it vanishes off `im(A^T)`.  The affine target `b` contributes only a
phase `(-1)^(y dot b)` before squaring.  Thus (1) is the abstract point-defect
law of rank `m`, embedded in the physical coordinate order by the binary
column matroid of `A`.

For `y!=0`, define the exact upper-cone count

\[
 C_A(y)=|\{y':s(y')\supseteq s(y)\}|.              \tag{2}
\]

The heavy zero atom has upper mass one, while a light atom has upper mass
`q_m C_A(y)`.  Hence

\[
 U(A)=h_m+q_m\sum_{y\ne0}\log C_A(y),              \tag{3}
\]

where `h_m=p_m log(1/p_m)` (and zero masses contribute zero).

## 2. Non-coloops have nonpositive signed decrement

Fix physical coordinate `i`.  If `c_i=0`, the function is independent of
that coordinate, so `Delta_i U=I_i=0`.

Suppose `c_i!=0` and deleting it leaves `A_{-i}` of rank `m`.  Both physical
restrictions solve a nonempty affine equation for the same punctured matrix,
so their squared laws and `U` values agree with `U(A_{-i})`.

Deleting a column removes one inclusion constraint in (2).  Therefore

\[
 C_{A_{-i}}(y)\ge C_A(y)\quad\text{for every }y,
\]

and (3) gives

\[
 \Delta_iU=U(A)-U(A_{-i})\le0.                    \tag{4}
\]

Thus every non-coloop is paid by its own signed posterior relaxation; it
uses no positive source-influence budget.

## 3. Exact coloop cancellation

Now suppose `i` is a coloop: deleting `c_i` lowers the rank to `m-1`.
After a change of **output labels only**, take `c_i=e_1` and put every other
column in `span(e_2,...,e_m)`.  Write `y=(beta,z)`.  If

\[
 C(z)=|\{z':s_0(z')\supseteq s_0(z)\}|,
\]

is the cone count of the rank-`m-1` core, then a label `(0,z!=0)` has
`2C(z)` upper labels, `(1,z)` has `C(z)`, and `C(0)=2^(m-1)`.  Put
`R=sum_{z!=0} log C(z)`.  Equation (3) becomes

\[
 U(A)=h_m+q_m\bigl(2^{m-1}+m-2+2R\bigr).          \tag{5}
\]

Exactly one physical child is constant.  The other is an affine-subspace
defect of codimension `m-1` on the core and has

\[
 U(A/i)=h_{m-1}+q_{m-1}R,
 \qquad q_{m-1}=4q_m.                              \tag{6}
\]

Subtracting half of (6) from (5) cancels the entire orientation-dependent
posterior term `R`:

\[
 \Delta_iU=delta_m:=h_m-\frac12h_{m-1}
 +q_m(2^{m-1}+m-2).                                \tag{7}
\]

This is exactly the one-coordinate decrement of the ordinary point defect
on `m` independent coordinates.  The coordinate influence is also exact:

\[
 I_i=q_m|\{y:y\cdot c_i=1\}|=q_m2^{m-1}=2^{1-m}.  \tag{8}
\]

The previously proved sharp point-defect theorem gives

\[
 \frac{\delta_m}{2^{1-m}}
 \le \kappa_{pd}:=\frac14+\frac94\log_2\frac{16}{9}
 =\frac{37}{4}-\frac92\log_2 3.                   \tag{9}
\]

Its maximum is attained at `m=3`.

## 4. Sum over the actual physical coordinates

Let `d` be the number of nonzero columns and `c` the number of coloops.
By (8),

\[
 I(f_V)=d,2^{1-m}.                                \tag{10}
\]

Using (4), (7), and `c<=d`,

\[
\begin{aligned}
G(f_V)
&=\sum_{i\text{ coloop}}\delta_m
 +\sum_{i\text{ non-coloop}}\Delta_iU\\
&\le c\,\kappa_{pd}2^{1-m}
 \le \kappa_{pd}I(f_V).                           \tag{11}
\end{aligned}
\]

The estimate is sharp for this class: the rank-three coordinate point
defect, with any number of zero/dummy columns, attains `kappa_pd`.

## 5. Restriction and composition closure

Restricting a physical coordinate in `f_V` produces either two nonempty
affine fibers of the same codimension, or one affine fiber of codimension one
less together with a constant.  Therefore affine-subspace defects and
constants form a restriction-closed class.

Disjoint products add `U`, `G`, and `I` exactly.  The earlier reused-character
composition theorem also permits arbitrary character cores shared among
otherwise disjoint affine-defect residual blocks: shared core coordinates
have exact zero `Delta_iU`, while influence only increases.  Consequently the
whole generated class satisfies the single pair

\[
 (a,b)=(\kappa_{pd},0).                            \tag{12}
\]

Applying the reviewed GU reduction within this restriction-closed class,

\[
 U\le\kappa_{pd}I,
 \qquad
 H\le(2+2\kappa_{pd})I
 =\left(\frac{41}{2}-9\log_2 3\right)I.            \tag{13}
\]

This covers affine defect sets of every cardinality `2^(n-m)` and arbitrary
physical orientation.  It is not universal GU: a general Boolean negative
set is not one affine fiber, and its spectral light masses are not uniform on
a linear code.

