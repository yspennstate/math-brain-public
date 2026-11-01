Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum.**

# HARD7-03 second idea-before-code — exact full centre-pair winner decomposition

The omitted-cone calculation in the preceding idea is positive but still throws away configurations. A stronger B7/B18/B25 route is to integrate the genuinely nonnested centre pair exactly, conditional on the first layer, by partitioning according to which of four shifted exponential variables is the global winner.

Condition on `(A_{-1},A_0,A_1)` and put

\[
Y_X=s_X+E_X,
\quad Y_C=s_C+E_C,
\quad Y_D=s_D+E_D,
\quad Y_Z=s_Z+E_Z,
\]

where the `E` variables are iid `Exp(1)` and

\[
s_X=A_{-1},\quad s_C=\max(A_{-1},A_0),
\quad s_D=\max(A_{-1},A_0,A_1),
\quad s_Z=\max(A_0,A_1).
\]

Thus `s_D` is the largest shift. Set

\[
R=\max(Y_C,Y_D),\quad S=\max(R,Y_X),\quad T=\max(R,Y_Z),
\]
\[
U=\min(S,T),\qquad V=\max(S,T).
\]

For the already proved two-clock kernel,

\[
K_\theta(S,T)=\frac{e^{\theta U}}q-
\frac{\theta}{qa}e^{U-qV},
\qquad q=1-\theta,\quad a=2-\theta.
\tag{1}
\]

## Winner partition

If the global maximum `V` is attained by `Y_C` or `Y_D`, then `U=V`. If it is attained by `Y_X`, then

\[
U=M_X:=\max(Y_Z,Y_C,Y_D),
\]

and if it is attained by `Y_Z`, then

\[
U=M_Z:=\max(Y_X,Y_C,Y_D).
\]

For a common winner `i in {C,D}`, define

\[
W_i:=E[e^{\theta Y_i};Y_i=V\mid A].
\]

The two terms in (1) combine to coefficient

\[
\frac1q-\frac{\theta}{qa}=\frac2a.
\]

For an outer winner `i in {X,Z}`, `M_i` includes `Y_D`, hence `M_i>=s_D>=s_i`. Conditional on `M_i=m`,

\[
P(Y_i>m)=e^{s_i-m},
\]

and

\[
E[e^{m-qY_i};Y_i>m\mid M_i=m]
=\int_m^\infty e^{m-qy}e^{-(y-s_i)}dy
=\frac{e^{s_i-qm}}a.
\]

Therefore the exact outer-winner coefficient is

\[
\frac1q-\frac{\theta}{qa^2}
=\frac{4-\theta}{a^2}.
\]

Writing

\[
R_i:=E[e^{-qM_i}\mid A],
\]

we obtain the exact conditional centre-pair moment

\[
\boxed{
P_{\rm ctr}(A)=\frac2a(W_C+W_D)
+\frac{4-\theta}{a^2}
\left(e^{s_X}R_X+e^{s_Z}R_Z\right).}
\tag{2}
\]

This is the full centre pair, not a one-sided event slice.

## Finite subset formulas

Because `s_D` is the largest shift, winner integration starts at `s_D`. For `i in {C,D}`, with universe `I={X,Z,C,D}`,

\[
\boxed{
W_i=e^{s_i}\sum_{S\subseteq I\setminus\{i\}}
\frac{(-1)^{|S|}}{q+|S|}
\exp\left(\sum_{j\in S}s_j-(q+|S|)s_D\right).}
\tag{3}
\]

For outer `i in {X,Z}`, integration by parts against the maximum of the other three shifted exponentials gives

\[
\boxed{
R_i=q\sum_{S\subseteq I\setminus\{i\}}
\frac{(-1)^{|S|}}{q+|S|}
\exp\left(\sum_{j\in S}s_j-(q+|S|)s_D\right).}
\tag{4}
\]

The previous common-window lower bound for this same centre pair is

\[
Q_{\rm ctr}(A)=\frac2a E[e^{\theta\max(Y_C,Y_D)}\mid A],
\tag{5}
\]

and the two-variable version of (3) gives (5) exactly.

## Exact integration over the first layer

On each of the six strict order cones of `(A_{-1},A_0,A_1)`, write the ordered values as

\[
A_{(1)}=u,\qquad A_{(2)}=u+v,\qquad A_{(3)}=u+v+w,
\qquad u,v,w\ge0.
\]

The iid exponential density is `e^{-3u-2v-w}`. Every summand of (2)--(5) is `c exp(alpha u+beta v+gamma w)`, so its cone integral is exactly

\[
\boxed{
\frac{c}{(3-\alpha)(2-\beta)(1-\gamma)}}.
\tag{6}
\]

Thus the full centre-pair gain is a finite rational sum at rational `theta`; no simulation or numerical quadrature is needed.

At `theta=723/1250`, preliminary exact arithmetic gives

\[
P_{\rm ctr}=\frac{11253444786300730080604553222656250000000}
{589014585036522512566911293259319803207},
\]

\[
Q_{\rm ctr}=\frac{50552368164062500000000}{2794229721911833952401},
\]

and hence

\[
\boxed{
\delta_{\rm ctr}^{\rm full}=P_{\rm ctr}-Q_{\rm ctr}
=\frac{1133148258990652534484863281250000000}
{1117674734414653724035884806943680841}
\approx1.0138443896954534.}
\tag{7}
\]

The preceding checkpoint had already incorporated only

\[
\delta_{\rm ctr}^{\rm prev}
=\frac{7354736328125000000000}{16049588934017308109901}
\approx0.4582507600887237
\]

per centre pair. Therefore the **incremental** gain to apply to the current four-step bound is `4(delta_full-delta_prev)`, not `4 delta_full`; this avoids double counting. A final exact checker should verify (2)--(7) by all six order cones, verify positivity cone by cone, update the current four-step rational, and only then certify a new rational Chernoff shape constant.