# Balanced half-activation: exact logarithmic-credit identity

All logarithms are base two.  For a Boolean sign `h`, write

\[
 p_h(S)=\widehat h(S)^2,\qquad
 U(h)=\sum_Sp_h(S)\log_2\frac{\pi_h(S)}{p_h(S)},
 \qquad G(h)=\sum_i\Delta_iU(h),
\]

and put

\[
 \mathcal S(h)=H(h)+I(h)-G(h).
\]

Let `g:{-1,1}^n->{-1,1}` be balanced.  Introduce one fresh physical
selector `z` and define its half-activation by

\[
 F(+1,x)=1,\qquad F(-1,x)=g(x).                       \tag{1}
\]

For `a_j=\widehat g({j})`, define

\[
 L_1(g)=\sum_j a_j^2\log_2\frac1{a_j^2},\qquad
 W_1(g)=\sum_j a_j^2.                                \tag{2}
\]

Zero summands have their usual value zero.

## The exact identity

Define on `[0,1]`

\[
 s(t)=-2(1-t)^2\log_2(1-t)-t^2\log_2t-t^2            \tag{3}
\]

by continuity at the endpoints, and on `[-1,1]`

\[
 D(a)=s(1/2)-\frac{s((1+a)/2)+s((1-a)/2)}2.           \tag{4}
\]

Then every balanced Boolean core satisfies

\[
 \boxed{\mathcal S(F)-\frac12\mathcal S(g)
 =\frac32-\frac12L_1(g)-\sum_jD(a_j).}               \tag{5}
\]

Equivalently,

\[
 \boxed{G(F)-\frac12G(g)
 =1+\frac12L_1(g)+\sum_jD(a_j).}                      \tag{6}
\]

To prove this, the Fourier expansion of (1) gives two atoms of mass `1/4`
from the constant coefficient and two copies of every nonconstant spectral
atom of `g`, each scaled by `1/4`.  Hence

\[
 H(F)=\frac12H(g)+2.                                  \tag{7}
\]

The selector has influence `1/2` and every data influence is halved, so

\[
 I(F)=\frac12I(g)+\frac12.                            \tag{8}
\]

The exact fresh-activation formula, specialized to activation probability
`p=1/2` and balanced defect rate `r=1/2`, has selector charge one.  For data
coordinate `j`, the two conditional defect rates are `(1+a_j)/2` and
`(1-a_j)/2`; its remaining charge is

\[
 \frac12a_j^2\log_2\frac1{a_j^2}+D(a_j).             \tag{9}
\]

Summing (9) and the selector charge proves (6).  Subtracting it from
(7)+(8) proves (5).  This derivation uses the actual physical singleton
coefficients; it does not replace them by independent spectral coordinates.

## Uniform scalar bound

For `|a|<1`, direct differentiation gives

\[
 D''(a)=-1+\frac9{4\ln2}+\frac3{4\ln2}\ln(1-a^2).
                                                               \tag{10}
\]

Thus

\[
 D''(a)\le 2c_0,
 \qquad c_0=\frac9{8\ln2}-\frac12.                   \tag{11}
\]

Since `D(0)=D'(0)=0`, integrating twice and using evenness yields

\[
 \boxed{D(a)\le c_0a^2\quad(-1\le a\le1).}           \tag{12}
\]

Continuity handles the endpoints.  The coefficient is sharp for this
scalar inequality because `D(a)/a^2 -> c_0` as `a -> 0`.

## Boolean payment of the first-level logarithm

Let `d_j=Inf_j(g)`.  The physical derivative identity gives

\[
 |a_j|=|\mathbb E D_jg|\le\mathbb E|D_jg|=d_j.        \tag{13}
\]

For `0<=x<=1`,

\[
 x^2\log_2(1/x^2)
 =x\frac{2x\ln(1/x)}{\ln2}
 \le \frac{2}{e\ln2}x.                              \tag{14}
\]

Consequently

\[
 L_1(g)\le\frac{2}{e\ln2}I(g),\qquad
 W_1(g)\le I(g).                                     \tag{15}
\]

Combining (6), (12), and (15) gives the dimension-free one-step transfer

\[
 \boxed{G(F)\le\frac12G(g)+1+c_1I(g),}               \tag{16}
\]

where

\[
 c_1=c_0+\frac1{e\ln2}
 =\frac9{8\ln2}-\frac12+\frac1{e\ln2}
 =1.6537697664\ldots.                                \tag{17}
\]

If the core obeys `G(g)<=K I(g)` for some `K>=0`, balance implies
`I(g)>=Var(g)=1`.  From (8) and (16),

\[
 G(F)\le\left(\frac K2+c_1\right)I(g)+1
 \le (K+2c_1)I(F),                                   \tag{18}
\]

with

\[
 2c_1=3.3075395328\ldots.                            \tag{19}
\]

## Scope and unpaid step

Equations (5), (6), and (16) hold for every balanced Boolean core in every
dimension and one fresh half-activation.  They replace the earlier
majority-only `Theta(log n)` description by a parameter-free payment to
actual physical influence.

They do not prove universal GU.  A naive hierarchy applies (16) at multiple
ancestors and can spend the same descendant influence repeatedly.  The
remaining lemma is a single-use ownership/telescope for the weighted
`L_1+c_0W_1` credits, or a different aggregate argument that prevents this
reuse while allowing changing coherent cores.
