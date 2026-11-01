# R06 / I0056 idea note — bootstrap the edge constant before feeding the vertex bootstrap

This note is intentionally written **before** any checker for this run.

The previous R06 run proved the scalar vertex bootstrap for the tetrapentagonal graph
\[
T=r\{4,5\},\qquad q:=\Phi_V(H_{4,5})=2/\sqrt3,
\]
using the retained edge lower bound
\[
h_0=\frac4{1+\sqrt3+\sqrt5}.
\]
The new route is to notice that the same plane-core inequalities also bootstrap the **edge** lower bound itself.

Descriptive Section-B moves for this run are **#5 ADD A PARAMETER**, **#25 COUNT THE SAME THING TWICE**, and **#30 DO ONE SCALE/DIRECTION AT A TIME**. All thirty labels have appeared previously in the long I0056 history, so these are not claimed to be literally never-used labels; they do not repeat the immediate predecessor's #18/#3/#12 triple.

## Idea

Assume a rigorous global edge lower bound
\[
\Phi_E(T)\ge h>0.
\]
If a finite set has edge ratio below the prospective improved bound, pass to a connected component, fill finite complement holes, and peel internal-degree-one selected vertices. Peeling a leaf changes `(B,n)` to `(B-2,n-1)`, so it cannot increase a ratio below 2. The prospective bound is below 1, hence this reduction is legitimate.

For the resulting connected induced hole-free core of minimum internal degree at least two, let

- `a` = selected vertices of internal degree 2,
- `b` = selected vertices of internal degree 3,
- `o` = selected internal-degree-4 vertices incident with the unbounded face,
- `i` = selected internal-degree-4 vertices not incident with the unbounded face.

Then
\[
N=a+b+o+i,\qquad E=|\partial_E D|=2a+b.
\]
The Euler/full-square count from the preceding vertex-bootstrap run does **not** use boundary multiplicity one for the inequality needed here. It gives
\[
F_4\ge \frac b2+i+2o-a+5.
\]
Every partial square has at least two selected/unselected transitions and each crossing edge belongs to exactly one square, so `Q_4<=E/2`. Transferring full squares to `H_{4,5}` gives
\[
qF_4\le Q_4\le E/2,
\]
hence
\[
(1+q)a+\frac{1-q}{2}b-2qo-qi\ge 5q.\tag{A}
\]

Let `I` be the `i` interior selected vertices. Their graph neighbors are all selected. Planarity of the outer-face walk gives
\[
|\partial_E I|\le b+2o.
\]
Using the assumed edge lower bound on `I` therefore gives
\[
b+2o-hi\ge0.\tag{B_h}
\]

Now define
\[
H(h):=\frac{4q(h+1)}{3hq+h+4q+2},\qquad
D_h:=3hq+h+4q+2.
\]
Take (A) with coefficient
\[
\alpha=\frac{2(h+2)}{D_h}
\]
and `(B_h)` with coefficient
\[
\beta=\frac{2q}{D_h}.
\]
A direct coefficient calculation appears to give the **exact identity**
\[
\alpha A+\beta B_h
=(2-H(h))a+(1-H(h))b-H(h)o-H(h)i
=E-H(h)N.
\]
Since the right side of (A) is `5q`, this would imply
\[
E-H(h)N\ge 5q\alpha>0,
\]
and hence the theorem
\[
\Phi_E(T)\ge h\quad\Longrightarrow\quad \Phi_E(T)\ge H(h).
\]

The positive fixed point of `H` is
\[
h_*=\frac{\sqrt{12q^2+4q+1}-1}{3q+1}.
\]
The old bound `h_0` is numerically below this fixed point, so if the coefficient identity and reduction are correct, monotone iteration yields `Phi_E(T)>=h_*`.

Finally, the preceding run's vertex bootstrap was symbolic in the edge parameter: for any rigorous edge lower `h`, it gives the fixed-point vertex lower
\[
g_*(h)=\sqrt{\frac{q+\frac h2(q-1)}{q+1}}.
\]
Thus the edge bootstrap should feed back immediately into a slightly stronger rigorous lower bound for `Phi_V(T)`, reducing the still-open mixed-face vertex interval without changing the frozen already-zero `H_{5,5}` metric.

## What must be checked before promotion

1. The connected/hole-filled/leaf-pruned reduction really preserves any hypothetical edge ratio below `H(h)`.
2. Inequality (A) remains valid without the multiplicity-one boundary normalization used elsewhere in the vertex argument.
3. The outer-face incidence bound `|partial_E I|<=b+2o` survives cut vertices/bridges.
4. The multiplier identity is exact and all coefficients are positive.
5. `h_0<h_*<1`, and the iteration is monotone and bounded.
6. Re-substituting `h_*` into the already-proved vertex bootstrap genuinely improves the certified lower endpoint below the retained exact upper witness `384566/484385`.
