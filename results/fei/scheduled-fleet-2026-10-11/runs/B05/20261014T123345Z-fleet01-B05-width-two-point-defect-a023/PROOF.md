# Sliding width-two SOLD theorem for all point defects

All FEI quantities use base-two logarithms.  Put

\[
q(t)=t\log_2(1/t)+\frac{2t}{\ln2},\qquad
L_c=M+2U-cI.
\]

At a node with inherited block `Y`, query `x`, and both children inheriting
the remapped block `Z`, the reviewed signed-orbit identity gives the complete
node charge

\[
\mathcal C_x=
\Delta_xL_c(f)+2\Theta_Y(f)
-\sum_{\sigma=\pm1}\Theta_Z(f_{x=\sigma}). \tag{1}
\]

No opening, reveal, constant-child, or terminal term has been dropped.

## 1. Exact formulas

Let `d_r` be `+1` except at one point of the `r`-cube, and set
`t=2^{1-r}`.  Define

\[
\begin{aligned}
U_r&=-2(1-t)^2\log_2(1-t)+rt(1-t),\\
B_r&=r\{T((1-t)^2,t^2)+2t(1-t)\},\\
D_r&=U_r-\tfrac12U_{r-1},\\
M_r&=rD_r-B_r,
\end{aligned} \tag{2}
\]

where

\[
T(a,b)=a\log_2\frac{a+b}{a}+b\log_2\frac{a+b}{b}.
\]

For a physical block of size `k`, symmetry gives

\[
\Theta_{r,k}=kq(t)+(r-k)q(2^kt^2). \tag{3}
\]

For the sliding transition which queries one member of a size-`k` block,
retains `k-1` members, and inserts one new coordinate, (1) is nonpositive
exactly when `c>=c_{r,k}`, where

\[
c_{r,k}=\frac{M_r-\frac12M_{r-1}+2D_r
+2\Theta_{r,k}-\Theta_{r-1,k}}{t}. \tag{4}
\]

The other restriction is constant, so its contribution is zero.

## 2. The full-block policy necessarily diverges

For `k=r` at the parent and `k=r-1` at the child, the orbit part of (4)
divided by `t` is exactly

\[
\frac{2rq(t)-(r-1)q(2t)}t
=4(r-1)+\frac4{\ln2}. \tag{5}
\]

Direct substitution in (2), or the series below, gives

\[
\frac{M_r-\frac12M_{r-1}+2D_r}{t}=1+o(1).
\]

Therefore

\[
c_r^{\rm full}=4r-3+\frac4{\ln2}+o(1), \tag{6}
\]

so no fixed coefficient can support repeated full-block inheritance.  The
rank-five positive charge at the reviewed `c*` is independently interval-
certified in `CERTIFY.out`.

## 3. Width two has a uniform coefficient

Let

\[
F(s)=-(1-s)^2\ln(1-s)
=s-\frac32s^2+\sum_{j\ge3}\frac{2s^j}{j(j-1)(j-2)}. \tag{7}
\]

Multiplying (2) by `ln 2` and simplifying yields

\[
(\ln2)D_r=2F(t)-F(2t)+t\{1+(r-2)t\}\ln2. \tag{8}
\]

All terms of degree at least three in `2F(t)-F(2t)` are nonpositive, so it
is at most `3t^2`.  Since `(r-2)t<=1/4` for `r>=3`, (8) implies

\[
D_r\le3t. \tag{9}
\]

For completeness, set

\[
C(s)=1-2s+2s^2,
\quad K(s)=F(2s)+C(s)\ln C(s),
\]

and

\[
J_r(t)=K(t)+t\ln2+(r-2)t^2\ln2.
\]

Substitution in (2) gives `(ln2)M_r=-rJ_r(t)`.  Write
`K(s)=-2s^2+P(s)`.  Direct differentiation gives
`P(0)=P'(0)=P''(0)=P'''(0)=0` and

\[
P^{(4)}(s)=\frac{32}{(1-2s)^2}
+\frac{2(4s-2)^4}{C(s)^3}
-\frac{24(4s-2)^2}{C(s)^2}+\frac{48}{C(s)}.
\]

On `0<=s<=1/32`, direct rational comparison of this expression gives
`0<=P^{(4)}(s)<=48`.  Taylor's theorem therefore gives

\[
0\le P(s)\le2s^4. \tag{10}
\]

For `r>=7`, `t<=1/64`, and hence

\[
\begin{aligned}
&rJ_r(t)-\frac{r-1}{2}J_{r-1}(2t)\\
&\quad\ge t\ln2+t^2\{2r-4+(-r^2+6r-6)\ln2\}
-16(r-1)t^4\\
&\quad\ge t\ln2\left(1-\frac{13}{64}\right)
-16(r-1)t^4>0. \tag{11}
\end{aligned}
\]

Here `t(r^2-6r+6)` is maximized at `r=7` on the indicated dyadic range,
and `16(r-1)t^3<=3/8192`, so the final strict inequality is explicit.
Equation (11) proves

\[
M_r-\tfrac12M_{r-1}\le0\qquad(r\ge7). \tag{12}
\]

For a size-two block, the exact identity `q(4s)=4q(s)-8s` gives

\[
\frac{2\Theta_{r,2}-\Theta_{r-1,2}}t
=4-\frac{2(r-4)q(4t^2)}t+32(r-3)t
\le4+32(r-3)t. \tag{13}
\]

For `r>=7` the last expression is at most `6`.  Combining (9), (12), and
(13) gives

\[
c_{r,2}\le12\qquad(r\ge7). \tag{14}
\]

For `r=3,4,5,6`, exact outward rational-log intervals certify the charge at

\[
c_0=14+\frac4{\ln2}
\]

to be strictly negative.  Thus

\[
\boxed{c_{r,2}\le c_0\quad(r\ge3).} \tag{15}
\]

The same certificate checks the rank-two transition from inherited block
size two to child block size one and the rank-one terminal query.

## 4. Complete tree and scope

At the root of `d_r` the true inherited block is empty.  For `r>=3`, compare
it with any two-coordinate block `Y`; the reviewed domination
`Theta_empty=Phi<=Theta_Y` shows that the true root charge is no larger than
the width-two charge.  Query one member, pass two surviving coordinates to
the nonconstant child, and terminate the constant child.  At every later
rank at least three, retain one block coordinate and insert one new
surviving coordinate.  Finish with the certified rank-two and rank-one
endpoint transitions.

This is a complete SOLD tree.  The signed restriction telescope therefore
gives

\[
L_{c_0,1}(d_r)+2\Phi(d_r)\le0.
\]

The reviewed mismatch reduction then yields

\[
G(d_r)\le(c_0+2)I(d_r)
=\left(16+\frac4{\ln2}\right)I(d_r), \tag{16}
\]

and the recorded GU-to-FEI reduction gives

\[
H(d_r)\le\left(34+\frac8{\ln2}\right)I(d_r). \tag{17}
\]

Equations (16)–(17) cover only the point-defect family.  The universal
width-two selection lemma for arbitrary Boolean cores remains open.
