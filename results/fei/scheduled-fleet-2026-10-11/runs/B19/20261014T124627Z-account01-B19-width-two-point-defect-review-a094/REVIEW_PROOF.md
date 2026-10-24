# Independent proof reconstruction

Let `d_r` be the rank-`r` point defect and `t=2^{1-r}`.  Its Walsh
coefficients are `1-t` at the empty set and have squared mass `t^2` at every
nonempty set.  Therefore

\[
\begin{aligned}
U_r&=-2(1-t)^2\log_2(1-t)+rt(1-t),\\
B_r&=r\{T((1-t)^2,t^2)+2t(1-t)\},\\
D_r&=U_r-\tfrac12U_{r-1},\qquad M_r=rD_r-B_r.
\end{aligned}
\]

For a block of size `k`, singleton orbits inside the block have total mass
`t`; those outside have mass `2^k t^2`.  Hence

\[
\Theta_{r,k}=kq(t)+(r-k)q(2^kt^2). \tag{1}
\]

The exact signed node charge for `{x,y}->{y,z}` is nonpositive iff

\[
c\ge c_{r,2}:=
\frac{M_r-\frac12M_{r-1}+2D_r
+2\Theta_{r,2}-\Theta_{r-1,2}}t. \tag{2}
\]

To prove the high-rank estimate, set

\[
F(s)=-(1-s)^2\ln(1-s)
=s-\frac32s^2+\sum_{j\ge3}\frac{2s^j}{j(j-1)(j-2)}.
\]

Then

\[
(\ln2)D_r=2F(t)-F(2t)+t\{1+(r-2)t\}\ln2.
\]

The coefficients from degree three onward in `2F(t)-F(2t)` are
nonpositive, so this term is at most `3t^2`.  Since `(r-2)t<=1/4`,
`D_r<=3t`.

Put

\[
C(s)=1-2s+2s^2,quad K(s)=F(2s)+C(s)\ln C(s),
\]

and write `K(s)=-2s^2+P(s)`.  Direct differentiation and the substitution
`u=1-2s`, `v=u^2` give

\[
P^{(4)}(s)=\frac{32(1+6v-3v^2)}{v(1+v)^3}. \tag{3}
\]

For `0<=s<=1/32`, `225/256<=v<=1`.  Positivity in (3) is immediate.  The
inequality `P^{(4)}<=48` is equivalent to

\[
3v^4+9v^3+15v^2-9v-2\ge0.
\]

Its derivative is positive on the stated interval and its value at
`225/256` is `41135274883/4294967296`.  Because the first four Taylor data of
`P` vanish, this proves

\[
0\le P(s)\le2s^4. \tag{4}
\]

Define

\[
J_r(t)=K(t)+t\ln2+(r-2)t^2\ln2.
\]

Substitution gives `(ln2)M_r=-rJ_r(t)`.  From (4), for `r>=7`,

\[
\begin{aligned}
rJ_r(t)-\frac{r-1}{2}J_{r-1}(2t)
&\ge t\ln2+t^2\{2r-4+(-r^2+6r-6)\ln2\}\\
&\quad-16(r-1)t^4\\
&\ge t\ln2\frac{51}{64}-16(r-1)t^4>0.
\end{aligned}
\]

Here `t(r^2-6r+6)<=13/64` and `16(r-1)t^3<=3/8192`; `ln2>1/2` makes the
last sign strict.  Thus

\[
M_r-\tfrac12M_{r-1}\le0. \tag{5}
\]

Finally, `q(4s)=4q(s)-8s` gives

\[
\frac{2\Theta_{r,2}-\Theta_{r-1,2}}t
=4-\frac{2(r-4)q(4t^2)}t+32(r-3)t\le6
\]

for `r>=7`.  Equations (2), (5), and `2D_r/t<=6` yield
`c_{r,2}<=12`.  The exact independent certificate covers ranks 1–6 at
`c0=14+4/ln2`.  Recursing on the unique nonconstant child completes the
tree.
