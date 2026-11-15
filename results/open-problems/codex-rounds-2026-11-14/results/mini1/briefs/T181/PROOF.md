# Exact finite-generation Favard lengths

Use the normalization

\[
\operatorname{Fav}(E)=\frac1\pi\int_0^\pi
  |\pi_\theta(E)|\,d\theta,\qquad
\pi_\theta(x,y)=x\cos\theta+y\sin\theta.
\]

The following is a finite reduction and a certified computation for generations
0 through 5. It gives no asymptotic decay estimate.

## 1. Integer coordinates and symmetry

Fix an integer \(n\geq0\), and put

\[
D=4^n,\qquad
S_n=\left\{3\sum_{j=0}^{n-1}\epsilon_j4^j:
  \epsilon_j\in\{0,1\}\right\}.
\]

The empty sum is zero. Directly from the construction,

\[
K_n=\bigcup_{a,b\in S_n}D^{-1}([a,a+1]\times[b,b+1]).
\]

For \(0\leq t\leq1\), define

\[
L_n(t)=\left|\bigcup_{a,b\in S_n}
       [a+bt,\ a+bt+1+t]\right|.
\]

At \(\theta=\arctan t\), the projection length is
\(D^{-1}L_n(t)/\sqrt{1+t^2}\). Reflection about the horizontal
midline changes the projection in direction \(\theta\) into a translate of
the projection in direction \(-\theta\). Interchanging the two coordinates
exchanges directions \(\theta\) and \(\pi/2-\theta\). Consequently the
integrals over the four intervals of length \(\pi/4\) in \([0,\pi]\)
are equal. Since \(d\theta=dt/(1+t^2)\),

\[
\boxed{\operatorname{Fav}(K_n)=\frac{4}{\pi D}
  \int_0^1\frac{L_n(t)}{(1+t^2)^{3/2}}\,dt.} \tag{1}
\]

## 2. A complete finite set of events

Every projected endpoint has the form

\[
\lambda_{a,b,e}(t)=(a+e)+(b+e)t,
\quad a,b\in S_n,\ e\in\{0,1\}.
\]

Two distinct, nonparallel endpoint lines cross only at

\[
t=-\frac{d_x+\delta}{d_y+\delta},\qquad
d_x,d_y\in S_n-S_n,\quad\delta\in\{-1,0,1\},\quad
d_y+\delta\ne0. \tag{2}
\]

Conversely, all choices in (2) arise from endpoint pairs: the coordinate
differences can be chosen independently, and \(e-f\) realizes each allowed
\(\delta\). Include only values strictly between 0 and 1, and add 0 and 1.
Call the resulting sorted set \(T_n\). Identical endpoint lines cause ties
throughout a cell and do not need an event. Parallel unequal lines never cross.

On any open cell between consecutive members of \(T_n\), every nonidentical
pair of endpoint lines has a fixed strict order. In particular, the identities
of the left and right ends of the connected components of their union are
fixed. Thus

\[
L_n(t)=A+Bt \tag{3}
\]

on that cell, with integers \(A,B\). There is no omitted topological change:
a component can split or merge only when two endpoints coincide, and every
such coincidence is in (2).

For completeness, \(L_n\) is continuous even at event slopes. For intervals
\([u,v]\) and \([u',v']\), the measure of their symmetric difference is at
most \(|u-u'|+|v-v'|\). The symmetric difference of two unions is contained
in the union of the corresponding symmetric differences. Summing this bound
over the finitely many squares proves continuity. Hence the affine formulas
extend to the cell boundaries.

The difference set has at most \(3^n\) elements, because each base-4 digit
difference is \(-3,0,3\). Thus (2) also supplies the finite bound
\(|T_n|\leq3\cdot9^n+2\). This is a bound on the search size, not a
Favard decay estimate.

## 3. Computing the affine formula

At a rational sample \(t=p/q\) inside a cell, order the square origins
\((a_i,b_i)\) by the integers \(q a_i+p b_i\). There are
\(M=4^n\) intervals, all with length \(w=1+t\).
Write \(s_i=a_i+b_it\). For any nondecreasing starts \(s_i\),

\[
\left|\bigcup_{i=1}^M[s_i,s_i+w]\right|
 =w+\sum_{i=1}^{M-1}\min(s_{i+1}-s_i,w). \tag{4}
\]

Indeed, the first interval contributes \(w\). Because all intervals have
equal length, the rightmost endpoint among the first \(i\) intervals is
\(s_i+w\). The next interval adds \(s_{i+1}-s_i\) when this is at most
\(w\), and adds \(w\) otherwise. This proves (4) by induction.

In (4), each comparison with \(w\) is an endpoint-order comparison,
which stays fixed in the open cell. A gap contributes the coefficient pair
\((a_{i+1}-a_i,b_{i+1}-b_i)\), or else \((1,1)\).
Adding these pairs to the initial pair \((1,1)\) gives \((A,B)\)
in (3) using only integers. Two rational samples in every candidate cell
are checked against a separate endpoint-occupancy sweep by the script.

## 4. Exact integration and representation of the answer

An elementary differentiation gives

\[
\frac{d}{dt}\frac{At-B}{\sqrt{1+t^2}}
 =\frac{A+Bt}{(1+t^2)^{3/2}}. \tag{5}
\]

At a reduced rational slope \(t=p/q\) with \(q>0\), the primitive
in (5) is

\[
\frac{Ap-Bq}{\sqrt{p^2+q^2}}. \tag{6}
\]

Apply (6) at both ends of every affine piece, with sign minus at its
left end and plus at its right end. Group equal positive integer
radicands \(m=p^2+q^2\), obtaining integers \(c_m\). Then

\[
\boxed{\operatorname{Fav}(K_n)=\frac{4}{\pi4^n}
  \sum_m\frac{c_m}{\sqrt m}.} \tag{7}
\]

This proves, for every finite \(n\), that \(\pi\operatorname{Fav}(K_n)\)
is algebraic and gives a terminating algorithm for it. The files
`data/certificate_nN.json` specify every \(m,c_m\) in (7); the
corresponding `data/cells_nN.csv` specify the complete function (3).
Adjacent cells with equal \((A,B)\) are merged.

## 5. Rational certificates for the decimal values

The generator uses \(Q=10^{55}\). For each radicand \(m\), compute
\(r=\lfloor Q\sqrt m\rfloor\) by the integer square root of \(mQ^2\).
If \(r^2=mQ^2\), use the exact value \(1/\sqrt m=Q/r\).
Otherwise,

\[
\frac{Q}{r+1}<\frac1{\sqrt m}<\frac Qr. \tag{8}
\]

Multiply the endpoints by \(c_m\), reversing their order when
\(c_m<0\). Round the lower endpoint downward and the upper endpoint
upward to multiples of \(Q^{-1}\), then sum. This preserves enclosure
and keeps the final denominators bounded. It avoids floating-point arithmetic.

For \(\pi\), use Machin's identity

\[
\pi=16\arctan(1/5)-4\arctan(1/239).
\]

One verification is \(\tan(2\arctan(1/5))=5/12\), hence
\(\tan(4\arctan(1/5))=120/119\), and subtracting
\(\arctan(1/239)\) gives tangent 1. The angle lies in \((0,\pi/2)\):
it is positive, and \(4\arctan(1/5)<4/5<\pi/2\).
Thus the angle equals \(\pi/4\).
The alternating series

\[
\arctan x=\sum_{k=0}^{\infty}\frac{(-1)^kx^{2k+1}}{2k+1}
\]

at each of these two arguments is enclosed between its first 100 terms
and that partial sum plus the next term. Combining these rational
intervals with the sign of each coefficient gives positive rational
endpoints \(P_-\leq\pi\leq P_+\). If (8) and outward rounding give
\(0<R_-\leq\sum c_m/\sqrt m\leq R_+\), (7) lies in

\[
\left[\frac{4R_-}{DP_+},\frac{4R_+}{DP_-}\right]. \tag{9}
\]

The JSON certificates store both exact rational endpoints of (9).
The printed decimal lower endpoint is rounded downward and the upper
endpoint upward. Each internal enclosure has width less than \(10^{-45}\).

## 6. Independent integration audit

Let the merged pieces be \([t_{j-1},t_j]\), with coefficients
\(A_j,B_j\), where \(0=t_0<\cdots<t_k=1\). Put
\(I=\int_0^1 L_n(t)(1+t^2)^{-3/2}\,dt\).
Integrating by parts, using
\((t/\sqrt{1+t^2})'=(1+t^2)^{-3/2}\), gives

\[
I=\frac{L_n(1)}{\sqrt2}
   -\sum_{j=1}^k B_j
       \bigl(\sqrt{1+t_j^2}-\sqrt{1+t_{j-1}^2}\bigr).
\]

Continuity of \(L_n\) removes interior boundary terms. Since
\(L_n(1)=A_k+B_k\), collecting terms yields

\[
\boxed{I=B_1+\frac{A_k-B_k}{\sqrt2}
  +\sum_{j=1}^{k-1}(B_{j+1}-B_j)\sqrt{1+t_j^2}.} \tag{10}
\]

`audit_favard.py` reads the CSVs without importing the generator, and
evaluates (10) with direct square-root bounds on a \(10^{-60}\) grid.
For \(t_j=p/q\), use
\(\sqrt{1+t_j^2}=\sqrt{p^2+q^2}/q\). Bounds for \(\sqrt m\)
come directly from the integer square root, instead of reciprocals as in (8).
The audit uses the separate identity

\[
\pi=4\bigl(\arctan(1/2)+\arctan(1/3)\bigr),
\]

because the tangent of the sum is 1 and the sum lies in \((0,\pi/2)\).
Each arctangent is bounded with 150 alternating-series terms and the
next term. The resulting enclosures have width less than \(10^{-50}\),
overlap the original rational certificates, and lie strictly inside
the displayed decimal bounds. The audit also regenerates all square origins
by testing base-4 digits of integers and merges projected intervals at the
midpoint of every saved piece.

## 7. Controls at exceptional directions

At \(t=0\), the projection consists of \(2^n\) disjoint intervals
of length 1 before dividing by \(D\). Hence

\[
|\pi_0 K_n|=2^{-n}. \tag{11}
\]

At \(t=1\), the possible starts are numbers with base-4 digits
\(0,3,6\). There are \(3^n\) distinct starts, and any two are at
least 3 apart. To see this, take the highest place \(j\) where their
digits differ. The leading difference has magnitude at least \(3\cdot4^j\),
while the sum of all lower-place differences has magnitude at most
\(6(4^j-1)/3=2(4^j-1)\). Their difference is at least \(4^j+2\geq3\).
The intervals have length 2 and are disjoint, so

\[
|\pi_{\pi/4}K_n|=\sqrt2(3/4)^n. \tag{12}
\]

At \(t=1/2\), multiply endpoint coordinates by 2. The starts \(2a+b\)
have digits \(0,3,6,9\), so they are exactly \(3j\),
\(0\leq j<D\). Each projected interval now has length 3. These intervals
tile \([0,3D]\). Therefore

\[
|\pi_{\arctan(1/2)}K_n|=3/\sqrt5. \tag{13}
\]

Thus a fixed exceptional direction retains positive projection length at
every generation. All three identities are checked exactly by the scripts;
they also show why finitely many directional values cannot determine Favard
decay.

## 8. Small cases and computed values

For \(n=0\), \(L_0(t)=1+t\), and (1) gives
\(\operatorname{Fav}(K_0)=4/\pi\).

For \(n=1\), the ordered starts are \(0,3t,3,3+3t\).
The two comparisons \(3t\leq1+t\) and \(3-3t\geq1+t\)
hold exactly when \(t\leq1/2\). Formula (4) gives

\[
L_1(t)=
\begin{cases}2+8t,&0\leq t\leq1/2,\\6,&1/2\leq t\leq1.\end{cases}
\]

Its integral in (1) before the factor \(4/(\pi D)\) is

\[
\left[\frac{2t-8}{\sqrt{1+t^2}}\right]_0^{1/2}
+\left[\frac{6t}{\sqrt{1+t^2}}\right]_{1/2}^1
=8+3\sqrt2-4\sqrt5.
\]

Since \(D=4\),

\[
\boxed{\operatorname{Fav}(K_1)=
  \frac{8+3\sqrt2-4\sqrt5}{\pi}.}
\]

For \(n=2\), the complete merged arrangement is small enough to display.
Each row gives \(L_2(t)=A+Bt\) on the indicated interval; formulas agree
at common endpoints.

| Left slope | Right slope | A | B |
|---:|---:|---:|---:|
| 0 | 1/8 | 4 | 64 |
| 1/8 | 1/4 | 12 | 0 |
| 1/4 | 1/2 | 0 | 48 |
| 1/2 | 3/5 | 32 | -16 |
| 3/5 | 8/13 | 14 | 14 |
| 8/13 | 5/7 | 30 | -12 |
| 5/7 | 3/4 | 40 | -26 |
| 3/4 | 4/5 | 22 | -2 |
| 4/5 | 11/13 | 6 | 18 |
| 11/13 | 13/14 | 28 | -8 |
| 13/14 | 1 | 54 | -36 |

Using either (5) or (10) yields the explicit expression

\[
\boxed{\begin{aligned}
4\pi\operatorname{Fav}(K_2)={}&94+45\sqrt2-32\sqrt5+12\sqrt{17}
   +6\sqrt{34}+4\sqrt{41}\\
 &-8\sqrt{65}-2\sqrt{74}-2\sqrt{233}
   -2\sqrt{290}-2\sqrt{365}.
\end{aligned}} \tag{14}
\]

For example, (10) gives the constant \(B_1=64\) and the terminal
term \((54-(-36))/\sqrt2=45\sqrt2\). The jump at \(3/4\)
contributes \(24\sqrt{1+(3/4)^2}=30\), giving the constant 94.
The other nine jumps give the remaining nine radicals in (14).

The exact algorithm and independent audit give:

| n | Strict lower bound | Strict upper bound | Merged affine pieces |
|---:|---:|---:|---:|
| 0 | 1.27323954473516 | 1.27323954473517 | 1 |
| 1 | 1.04990339003727 | 1.04990339003728 | 2 |
| 2 | 0.92793731495768 | 0.92793731495769 | 11 |
| 3 | 0.84365831229531 | 0.84365831229532 | 73 |
| 4 | 0.77883017302463 | 0.77883017302464 | 525 |
| 5 | 0.72637720829722 | 0.72637720829723 | 3858 |

The strictness follows from the independent enclosures lying strictly
inside the displayed bounds. Values greater than 1 at the first two
generations are consistent with this normalization: a unit square has
average projection length \(4/\pi\).
