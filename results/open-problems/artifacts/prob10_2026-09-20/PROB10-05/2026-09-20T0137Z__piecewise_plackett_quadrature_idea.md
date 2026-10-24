Runtime model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# PROB10-05 idea checkpoint — piecewise certified Plackett quadrature

Current source-valid fleet candidate before this run:

\[
\frac{3307}{20000}<\theta_{2,1/4}\le \frac14,
\qquad W_{1/4}=\frac{1693}{20000}=0.08465.
\]

The newest PROB10-05 report proves the exact cyclic four-cycle identity

\[
P'(c)=\frac{1}{\pi\sqrt{1-c^2}}
\left(\frac14+\frac{\arcsin q(c)}{2\pi}\right),
\qquad
q(c)=\frac{c(1+c)-2a^2}{1+c-2a^2},
\]

for `c in [b,a]`, where

\[
a=\frac{168557580}{170952323},\qquad
b=\frac{167065920}{170952323}.
\]

That report used one uniform derivative floor on the entire interval and certified only

\[
P(a)-P(b)>0.00243.
\]

## New route before code

Use the monotonicity already proved there: `q'(c)>0`. Partition `[b,a]` into 16 equal rational subintervals with left endpoints `c_j`. On each subinterval lower-bound the two increasing factors in `P'(c)` separately at `c_j`.

For the outer factor use only exact rational square certificates:

\[
\sqrt{1-c_j^2}<s_j\quad\Longrightarrow\quad
\frac{1}{\pi\sqrt{1-c^2}}>\frac{7}{22s_j}
\qquad(c\ge c_j),
\]

using `pi<22/7`.

For the bracket define a monotone rational lower envelope `B(q)`.

* For `-3/8 <= q < 0`, the old proof gives the uniform `3/16`. A second bound comes from

\[
\arcsin u=\int_0^u\frac{dt}{\sqrt{1-t^2}}
\le \frac{u}{\sqrt{1-u^2}}
\le \frac{40}{37}u
\quad(0\le u\le 3/8),
\]

because `sqrt(55)/8>37/40`. With `pi>3`, for negative `q=-u`,

\[
\frac14+\frac{\arcsin q}{2\pi}
\ge \frac14+\frac{20q}{111}.
\]

So use

\[
B(q)=\max\left\{\frac3{16},\frac14+\frac{20q}{111}\right\},\qquad q<0.
\]

* For `q>=0`, use `arcsin q>=q` and `1/(2pi)>7/44`:

\[
B(q)=\frac14+\frac{7q}{44}.
\]

Hence the entirely rational lower sum

\[
P(a)-P(b)>
\frac{a-b}{16}\sum_{j=0}^{15}\frac{7}{22s_j}B(q(c_j)).
\]

The target is to certify this lower sum above `0.003615`, replacing the old `0.00243` decrement. If successful, the inherited equicorrelation trace cap `273011/250000` becomes

\[
\operatorname{tr}(K^4)<
\frac{273011}{250000}-\frac{0.003615}{1-(7/8)^4}<1.08331.
\]

Then reuse the existing degree-18 quasimode / spectral-tail / Temple argument, without changing the source process or comparator, aiming at

\[
\theta_{2,1/4}>\frac{827}{5000}=0.1654.
\]

## Two materially different parallel attacks to test

1. **Exact circulant mode decomposition.** The four-cycle orthant can be written as `A<-|B|, C<-|D|` with two independent antisymmetric modes and one correlated symmetric pair. This may yield a direct two-dimensional integral bound sharper than Plackett quadrature, but a clean rational enclosure of the resulting Gaussian-CDF integral is still needed.

2. **Sixth spectral moment instead of fourth moment.** A certified `tr(K^6)` could constrain the non-Perron spectrum more sharply than the fourth trace and lower the Temple threshold. The obstruction is the six-dimensional orthant term; unless its cycle structure admits a comparably simple exact reduction, this route may cost more than it gains.

No code is written until the rational 16-block inequality above is fixed as the mathematical target.