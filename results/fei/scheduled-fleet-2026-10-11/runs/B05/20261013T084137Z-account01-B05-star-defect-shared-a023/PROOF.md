# Shared star--point-defect retained-credit theorem

Let `m >= 1`, let `R` be a nonempty subset of `[m]`, and let `eps` be in
`{0,1}`.  On binary variables `x,y_1,...,y_m`, put

\[
d_m(y)=1-2\mathbf 1_{\{y=0\}},\qquad
q_{R,\varepsilon}(x,y)=(-1)^{x(\varepsilon+\sum_{j\in R}y_j)},
\qquad P=q_{R,\varepsilon}d_m.
\]

All additions in the exponent are modulo two.  Let `h` be an arbitrary
Boolean function on a disjoint block and set `F=Ph`.

## Theorem

For every finite adaptive/pruned physical restriction tree `T` which queries
only variables of `P`, with uniform reach weights `w_l`,

\[
 U(F)-\sum_{\ell}w_\ell U(F_\ell)
 \le 2\le4I_{\{x,y\}}(F).
\]

The constant is independent of `m`, `|R|`, `eps`, the tree depth/order, and
the dimension or spectrum of `h`.  Moreover

\[
U(P)\le 2,
\qquad H(P)\le 10 I(P).
\]

## Spectral law

Write `delta=2^{-m}`, `t=4 delta^2`, and

\[
A=\frac{(1-4\delta)^2}{4}.
\]

For `eps=0`, the squared Fourier law of `P` has mass `A` at the two
`x`-free sets `emptyset,R`, mass `t` at every other `x`-free set, and mass
`1/4` at the two sets `{x},{x} union R`.  For `eps=1`, the `x`-free and
`x`-containing layers are interchanged.  This follows directly by pairing
the point-defect coefficients at `S` and `S triangle R`:

\[
\widehat d_m(\varnothing)=1-2\delta,
\qquad \widehat d_m(S)=-2\delta\quad(S\ne\varnothing).
\]

The law sums to one because

\[
2A+(2^m-2)t+\frac12=1.
\]

For reference, define `phi(p,q)=p log_2(q/p)` and

\[
B_s=A+\frac14+t(2^{m-s}-1),\qquad
C_s=A+t(2^{m-s}-1).
\]

The exact upper-set formulas are

\[
\begin{aligned}
U_0={}&\phi(A,1)+\phi(A,B_r)+\frac14\\
&+\sum_{s=1}^{r-1}{r\choose s}\phi(t,B_s)
+\sum_{s=1}^m\left({m\choose s}-{r\choose s}\right)t(m-s),
\end{aligned}
\]

and

\[
\begin{aligned}
U_1={}&\frac12+\phi(1/4,B_r)+\phi(A,1/2)+\phi(A,C_r)\\
&+\sum_{s=1}^{r-1}{r\choose s}\phi(t,C_s)
+\sum_{s=1}^m\left({m\choose s}-{r\choose s}\right)t(m-s),
\end{aligned}
\]

where `r=|R|` and a binomial coefficient is zero outside its usual range.

## Uniform bound

For `1 <= m <= 9`, the attached rational interval certificate evaluates all
`90` triples `(m,r,eps)`.  It gives

\[
\max U_\varepsilon<1.912218<2.
\]

For `m >= 10`, the total mass of all `t`-atoms is below `4 delta`, and every
one of their logarithms is at most `log_2(1/t)=2m-2`.  Their total
contribution is therefore below

\[
8(m-1)2^{-m}\le72/1024.
\]

Also `A >= (255/256)^2/4`.  The positive-series rational log certificate
checks the elementary envelopes

\[
\log_2(81/40)<1.02,
\quad \log_2(257/128)<1.01,
\quad \log_2\frac{1/2}{(255/256)^2/4}<1.02,
\]

and

\[
\log_2\left(1+\frac{1/512}{(255/256)^2/4}\right)<0.012.
\]

Since `A <= 1/4`, the first special term `phi(A,1)` is at most `1/2` on
this interval.  Substitution gives

\[
U_0<0.5+0.255+0.25+72/1024<1.076,
\]

and

\[
U_1<0.5+0.253+0.255+0.003+72/1024<1.082.
\]

Thus `U(P)<2` for every parameter.

## Tree and FEI consequences

Disjoint tensor additivity gives `U(Ph)=U(P)+U(h)` and the same identity at
every leaf.  The terminal `U(h)` packet therefore cancels exactly once:

\[
U(F)-\sum_\ell w_\ell U(F_\ell)
=U(P)-\sum_\ell w_\ell U(P_\ell)\le U(P)\le2.
\]

Because `R` is nonempty, exactly half the `y` inputs make `x` pivotal, so
`Inf_x(P)=1/2`.  Hence `2 <= 4 I(P)`.  Finally the accepted reduction
`H <= 2I+2U` yields `H(P) <= 10 I(P)`.

## Scope

This is a genuine shared-variable result: the quadratic star and the point
defect use the same `y` variables and their Fourier supports overlap.  It is
not the disjoint-core theorem in different notation.  It does not cover a
general quadratic factor times an arbitrary shared core, multiple defects,
or a directional queried-influence ledger.  Full FEI remains open.
