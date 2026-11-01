Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# F0095 idea before code — eliminate the neutral atom exactly

For the q=3 Ayre--Coja-Oghlan--Greenhill binomial variational functional write

\[
\Sigma_d(a)=V_d(a)-\frac d2Q(a),
\]

where, for a Poisson point process `N` of intensity `d a`,

\[
V_d(a)=\mathbb E\log S(N),
\]

\[
S(N)=3\prod_{x\in N}\frac{2+x}{3}-3\prod_{x\in N}\frac{1+2x}{3}+\prod_{x\in N}x,
\]

and

\[
Q(a)=\iint \log R(x,y)\,a(dx)a(dy),\qquad
R(x,y)=1-\frac{(1-x)(1-y)}3.
\]

The point `x=1` is exactly neutral: inserting it leaves all three products in `S` unchanged and `R(1,y)=1`.

## Exact quotient lemma

Let `b` be a probability law on `[0,1)` and

\[
a=m b+(1-m)\delta_1,\qquad 0<m\le1,\qquad \lambda=dm.
\]

Define

\[
V_b(\lambda)=\mathbb E\log S(N_{\lambda b}),\qquad
Q_b=\iint\log R(x,y)\,b(dx)b(dy).
\]

Then exactly

\[
\boxed{\Sigma_d(a)=V_b(\lambda)-\frac{\lambda^2}{2d}Q_b.}
\]

Proof: neutral Poisson points can be deleted from the vertex factor without changing `S`, leaving a Poisson process of intensity `lambda b`; and every edge term involving the neutral atom vanishes, so `Q(a)=m^2Q_b=(lambda/d)^2Q_b`.

If `V_b(lambda)<0` and `Q_b<0`, define

\[
\boxed{D_b(\lambda)=\frac{\lambda^2Q_b}{2V_b(\lambda)}>0.}
\]

Whenever `D_b(lambda)>=lambda`, the law

\[
a_d=\frac\lambda d b+\left(1-\frac\lambda d\right)\delta_1
\]

satisfies `Sigma_D(a_D)=0` and `Sigma_d(a_d)<0` for every `d>D_b(lambda)`. Thus this entire neutral-atom class reduces to minimizing the scalar quotient `D_b(lambda)` over active shapes `b` and active intensities `lambda`.

## Contact derivative / monovariant

Poisson differentiation gives

\[
V_b'(\lambda)=\mathbb E_{N,Y\sim b}[F(N+\delta_Y)-F(N)],\quad F=\log S.
\]

For fixed `b`,

\[
\frac{D_b'(\lambda)}{D_b(\lambda)}
=\frac2\lambda-\frac{V_b'(\lambda)}{V_b(\lambda)}.
\]

At `d=D_b(lambda)` put `m=lambda/d`. Since `mQ_b=2V_b(lambda)/lambda`,

\[
\frac{D_b'}{D_b}=-\frac{C_b(\lambda)}{V_b(\lambda)},
\]

where

\[
C_b(\lambda)=V_b'(\lambda)-mQ_b.
\]

But `C_b(lambda)` is exactly the `b`-average of the mass-insertion contact potential from the preceding run. Because `V_b(lambda)<0`,

\[
\boxed{\operatorname{sgn}D_b'(\lambda)=\operatorname{sgn}C_b(\lambda).}
\]

So neutral-mass optimization is not an extra numerical variable: it is a one-dimensional contact-balance equation.

## Why the minimizer is genuinely interior

For `|N|=0,1,2`, direct algebra gives `S(N)=1`. For three active marks,

\[
S(\{x,y,z\})=1-\frac29(1-x)(1-y)(1-z).
\]

Hence, if `b` is not concentrated at 1,

\[
V_b(\lambda)=-c_b\lambda^3+O(\lambda^4),\qquad
c_b=-\frac16\,\mathbb E\log\!\left(1-\frac29\prod_{i=1}^3(1-X_i)\right)>0.
\]

Since `Q_b<0`,

\[
D_b(\lambda)\sim \frac{-Q_b}{2c_b}\frac1\lambda\to\infty\qquad(\lambda\downarrow0).
\]

If `b` has finite support bounded by `z_*<1`, let `A=prod(2+x)/3`, `B=prod(1+2x)/3`, `C=prod x`. Then `C<=A` and `B/A<=r_*^{|N|}` with `r_*=(1+2z_*)/(2+z_*)<1`. Thus for all sufficiently large `|N|`, `S(N)` is between positive constant multiples of `A`, so

\[
V_b(\lambda)=\lambda\,\mathbb E_b\log\frac{2+X}{3}+O(1),
\]

with a strictly negative linear coefficient. Therefore `D_b(lambda)->infinity` as `lambda->infinity`. For every such fixed active shape, the neutral-atom quotient has at least one interior global minimizer.

## Concrete consequence for the current three-active-atom shape

Keep the active support

`(0.62520784, 0.25744044, 0.05606726)`

and exact active relative masses proportional to

`(12485014, 37444482, 42645848)`.

The quotient formulation shows that the previous total active mass `0.92575344` was slightly off the scalar contact-balance optimum. A direct one-dimensional search of `D_b(lambda)` locates the minimum near

`lambda ~= 4.33855054695`, `m ~= 0.925753437978`.

This numerical search is discovery only. The next artifact will freeze a rational neutral mass and certify a strictly negative ACG functional at `d=4.686507626077` using exact rational/outward-rounded arithmetic.