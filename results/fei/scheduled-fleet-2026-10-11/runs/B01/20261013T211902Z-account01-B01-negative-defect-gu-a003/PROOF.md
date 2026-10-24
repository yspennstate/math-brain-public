# GU' transfer through sign-flipped rare point defects

All logarithms are base two.  Write

\[
U(f)=\sum_S\widehat f(S)^2\log_2\frac{\sum_{T\supseteq S}\widehat f(T)^2}{\widehat f(S)^2},
\qquad
G(f)=\sum_i\bigl(U(f)-\mathbb E_{x_i}U(f|x_i)\bigr).
\]

Let `Q_r` be `+1` except at one point of the `r`-cube, put
`N_r=-Q_r`, `p_r=2^{-r}`, and `beta_r=1-2p_r`.  Thus
`E N_r=-beta_r` and the bias tends to `-1`.  For

\[
A(q)(z,x)=\begin{cases}1,&z=+1,\\q(x),&z=-1,\end{cases}
\]

take an arbitrary Boolean base `P`, a fresh balanced character `w`, and any
finite rank sequence `r_k>=2`.  On disjoint variables define

\[
F_1=A(wP),\qquad F_k=A(N_{r_k}F_{k-1})\quad(k\ge2).
\tag{1}
\]

We prove

\[
\boxed{G(F_d)\le2^{-d}G(P)+34.}
\tag{2}
\]

Consequently, for `a>=0` and `0<=b<1`,

\[
G(P)\le aI(P)+bU(P)
\Longrightarrow
\boxed{G(F_d)\le(a+34)I(F_d)+bU(F_d).}
\tag{3}
\]

There is also the endpoint transfer

\[
U(P)\le\frac{56}{27}I(P)
\Longrightarrow
\boxed{U(F_d)\le\frac{56}{27}I(F_d),\quad
H(F_d)\le\frac{166}{27}I(F_d).}
\tag{4}
\]

## 1. Scalar identities

Define

\[
\begin{aligned}
R(t)&=E(t)-\frac12t^2\log_2(1/t^2)+\frac14(1-t^2),\\
E(t)&=\frac{(1+t)^2}{4}\log_2\frac4{(1+t)^2}
+\frac{(1-t)^2}{4}\log_2\frac2{1-t}.
\end{aligned}
\]

The exact activation identities are

\[
U(A(q))=\frac12U(q)+R(\mathbb Eq),
\tag{5}
\]

and, if `m=E q` and `m_i^+-m_i^-=2 delta_i`,

\[
G(A(q))=\frac12G(q)+R(m)
+\sum_i\left(R(m)-\frac{R(m_i^+)+R(m_i^-)}2\right).
\tag{6}
\]

We use the already proved global bounds

\[
-\frac12<R(t)<\frac74\quad(-1\le t\le1),
\tag{7}
\]

and the independently reviewed positive-side slope bound

\[
R(t)\le\frac43(1-t)\quad(0\le t\le1).
\tag{8}
\]

For `t>0`, direct cancellation gives

\[
4\bigl(R(t)-R(-t)\bigr)
=(1+t)^2\log_2\frac2{1+t}-(1-t)^2\log_2\frac2{1-t}.
\tag{9}
\]

Put `x=(1-t)/(1+t)`.  After dividing by `(1+t)^2`, positivity in
(9) is equivalent to

\[
(1-x^2)\ln(1+x)\ge x^2\ln(1/x).
\]

This follows from `ln(1+x)>=x/(1+x)` and
`ln(1/x)<=(1-x)/x`.  Hence

\[
\boxed{R(-t)\le R(t)\quad(0\le t\le1).}
\tag{10}
\]

We also need positivity only on the interval used below.  For
`1/8<=s<=1/2`, expand `R(-s)` into its two nonnegative entropy terms,
`s^2 log_2 s`, and `(1-s^2)/4`.  The inequalities

\[
\log_2\frac2{1-s}\ge1,
\quad
\log_2\frac2{1+s}\ge\frac{1-s}{2\ln2}>\frac{1-s}{2},
\quad
\log_2(1/s)\le\frac{1-s}{s\ln2}<\frac{3(1-s)}{2s}
\]

give

\[
R(-s)\ge\frac{(1-s)(s^2-12s+7)}8>0.
\tag{11}
\]

The last inequality follows because the quadratic is decreasing on this
interval and equals `5/4` at `s=1/2`.

## 2. A uniform negative-side curvature interval

For `-1<t<0`,

\[
R''(t)=1+\frac{\ln\!\left(\dfrac{t^2}{(1+t)\sqrt{1-t}}\right)+3/4}{\ln2},
\qquad
R'''(t)=\frac{4-t-t^2}{2\ln2\,t(1-t^2)}<0.
\tag{12}
\]

Thus `R''` is decreasing on the negative side.  At `t=-1/16`, the claim
`R''(t)>-6` reduces to

\[
e^{3/4}>\frac{15\sqrt{17}}{32}.
\]

The left side exceeds
`1+3/4+9/32=65/32`, while `sqrt(17)<33/8`, so the right side is less
than `495/256<65/32`.  Therefore

\[
\boxed{R''(t)>-6\quad(-1/2\le t\le-1/16).}
\tag{13}
\]

Convexity of `R(t)+3t^2` yields, for `x,y` in this interval,

\[
R\!\left(\frac{x+y}{2}\right)-\frac{R(x)+R(y)}2
\le\frac34(x-y)^2.
\tag{14}
\]

Similarly, on `[-1/2,-1/8]`, `R''>-4`: at `-1/8` it is enough that
`e^{3/4}>21/(8sqrt(2))`, which follows from `e^{3/4}>2` and
`441<512`.  Hence the midpoint gap there is at most `(x-y)^2/2`.

## 3. Restriction-mean classification

Let `m_k=E F_k`.  Since `m_1=1/2`,

\[
m_k=\frac{1-\beta_{r_k}m_{k-1}}2,
\qquad \frac14\le m_k\le\frac12.
\tag{15}
\]

Write `T_beta(x)=(1-beta x)/2`.  Under a negative-defect activation,
every inherited restriction mean is mapped by `T_beta`.

Call a coordinate pair safe when both child means lie in `[1/8,1/2]`.
The following facts are immediate.

1. A safe pair stays safe after every `T_beta`, because `beta in [1/2,1)`.
2. A new point-defect coordinate is born safe: its two means are
   `(1-(1-4p)m)/2` and `(1-m)/2`, both in `[1/4,1/2]`.
3. A new selector has pair `(1,-beta m)`, with the second entry in
   `[-1/2,0]`.  After one further activation its pair is contained in
   `[p,3/4]`; after two it is safe.
4. At level one only the balancing character and first selector can be
   unsafe; both become safe after two negative activations.

Consequently, at every level there are at most three unsafe physical
coordinates.  Every other inherited coordinate has scalar arguments
`-beta m_i^+,-beta m_i^-` in `[-1/2,-1/16]`.

For a safe coordinate, (14) bounds its charge by
`3 beta^2 delta_i^2`.  Summing and using

\[
\sum_i\delta_i^2=W_1(F_{k-1})\le1
\]

gives a total safe inherited charge at most `3`.  Each of the at most three
unsafe coordinates costs at most `9/4` by (7), so all inherited scalar
charges cost at most

\[
3+3\cdot\frac94=\frac{39}{4}.
\tag{16}
\]

## 4. The negative point-defect block

Sign reversal does not change `U`, `I`, or `G`, so the exact point-defect
formulas give

\[
U(N_r)=U(Q_r)\le2I(Q_r)=2I(N_r),
\qquad G(N_r)=G(Q_r)\le2.
\tag{17}
\]

For a point-defect coordinate, the three arguments in (6) are
`-beta m`, `-(1-4p)m`, and `-m`.  For `r=2`, the two coordinates cost at
most `2(9/4)=9/2`.  For `r>=3`, all arguments lie in
`[-1/2,-1/8]`; the endpoint difference is `4pm`, so the aggregate charge
is at most

\[
8rp^2m^2\le\frac38.
\tag{18}
\]

Thus `9/2` is a uniform all-rank bound.

## 5. GU' recurrence

Disjoint tensor additivity and (17) contribute at most
`G(F_{k-1})/2+1`.  The root scalar is at most `7/4`, the point-defect
coordinates cost at most `9/2`, and (16) pays every inherited coordinate.
Therefore, for every `k>=2`,

\[
G(F_k)\le\frac12G(F_{k-1})+17.
\tag{19}
\]

The first balanced activation obeys
`G(F_1)<=G(P)/2+13/4`.  Since `13/4<34` and `34/2+17=34`, induction proves
(2).

Equations (5), (11), and the influence identity show

\[
I(F_d)\ge2^{-d}I(P),\qquad U(F_d)\ge2^{-d}U(P),\qquad I(F_d)\ge1.
\]

Substituting a base GU' estimate into (2) therefore proves (3), with the
coefficient `b` preserved exactly.

## 6. Endpoint recurrence

At every negative-defect step put `s=beta m`.  By (15),
`1/8<=s<=1/2`.  From (8) and (10),

\[
R(-s)\le\frac43(1-s)
\le\frac{56}{27}\frac{1+s}{2};
\tag{20}
\]

the last inequality is sharp for this comparison at `s=1/8`.  Together
with (17) and

\[
\begin{aligned}
U(F_k)&=\frac12U(F_{k-1})+\frac12U(N_r)+R(-s),\\
I(F_k)&=\frac12I(F_{k-1})+\frac12I(N_r)+\frac{1+s}{2},
\end{aligned}
\]

this proves the first part of (4).  The balanced first activation preserves
every endpoint constant at least one.  Finally apply the universal bridge
`H<=2I+2U` to obtain `H<=166 I/27`.

## 7. Scope

The ranks and negative biases are arbitrary and the constants are independent
of dimension, depth, rank sequence, and activation probabilities.  The proof
still requires fresh disjoint blocks and fair outer selectors.  It does not
cover biased selectors, mixing positive and negative defects arbitrarily,
variable reuse, or changing overlapping coherent cores.  The activated tower
class is not restriction-closed.  Thus this is a proper-class GU' theorem,
not universal GU' and not full FEI.
