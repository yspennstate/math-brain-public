# An obstruction to linear decision boundaries in the many-samples regime

Let `(X_i,Y_i)`, `1 <= i <= n`, be independent copies of a pair in
`R^d x {-1,+1}`, with `d >= 1`. Define

\[
 p(x)=\Pr(Y=+1\mid X=x),\qquad
 q(x)=\min\{p(x),1-p(x)\},\qquad
 \alpha=\mathbb E q(X).
\]

Thus `alpha` is the Bayes classification error. Use the tie convention
`sign_+(u)=+1` for `u>=0`, and `-1` otherwise. Let

\[
 E_{n,d}=\min_{w\in\mathbb R^d,b\in\mathbb R}
 \sum_{i=1}^n\mathbf1\{\operatorname{sign}_+(w^TX_i+b)\ne Y_i\},
 \quad
 M_{n,d}=2\sum_{j=0}^{\min\{d,n-1\}}{n-1\choose j}.
\]

The minimum is over finitely many possible prediction vectors, so it is
attained. Standard Borel conditional probabilities suffice throughout.
Every strict finite-sample affine prediction vector also has a rational
parameter realization, by openness of its parameter region. The events
below can therefore be expressed as countable unions of measurable events.

## Theorem 1: a binomial obstruction

For every integer `0 <= k <= n`,

\[
 \Pr(E_{n,d}\le k)
 \le \min\left\{1,M_{n,d}\Pr\bigl(\operatorname{Bin}(n,\alpha)\le k\bigr)\right\}.
 \tag{1}
\]

In particular,

\[
 \Pr(E_{n,d}=0)\le\min\{1,M_{n,d}(1-\alpha)^n\}.
 \tag{2}
\]

If `0 <= k/n < alpha <= 1/2`, then

\[
 \Pr(E_{n,d}\le k)\le
 \min\{1,\exp(\log M_{n,d}-nD(k/n\Vert\alpha))\},
 \tag{3}
\]

where

\[
 D(r\Vert a)=r\log(r/a)+(1-r)\log((1-r)/(1-a)),
 \qquad D(0\Vert a)=-\log(1-a).
\]

### Counting prediction vectors

Fix `x_1,...,x_n`, and set `z_i=(x_i,1)` in `R^{d+1}`. First, every
prediction vector with the stated tie rule is realizable with all scores
nonzero. Indeed, increase the bias by a positive number smaller than the
absolute value of every currently negative score. Zero scores become
positive and negative scores remain negative. If there are no negative
scores, any positive bias increment works.

The strict prediction vectors correspond to nonempty open regions of the
central hyperplane arrangement

\[
 H_i=\{\theta\in\mathbb R^{d+1}:z_i^T\theta=0\}.
\]

A fixed strict sign vector defines an intersection of open halfspaces;
this set is convex, so it cannot consist of multiple regions.

Here is the region-count bound, including the induction. In dimension
`p`, write `R(n,p)` for the maximum number of regions of `n` central
hyperplanes. For `n=1` it is two, and for `p=1,n>=1` it is at most two.
For `n>=2,p>=2`, insert the last hyperplane. If it duplicates an earlier
one it makes no new region. Otherwise each region it splits gives one
region in the arrangement restricted to that hyperplane. The restriction
has at most `n-1` central hyperplanes in dimension `p-1`. Thus

\[
 R(n,p)\le R(n-1,p)+R(n-1,p-1).
\]

The split regions inject into the restricted regions: their intersections
with the last hyperplane have different earlier sign vectors. The base
cases and Pascal's identity now give, by induction,

\[
 R(n,p)\le 2\sum_{j=0}^{\min\{p-1,n-1\}}{n-1\choose j}.
\]

Use `p=d+1`. This proves that the number of affine prediction vectors is
at most `M_{n,d}`, with no general-position assumption.

### Conditional noise and the binomial tail

Condition on all the inputs. For any one prediction vector `a`, its
errors are independent Bernoulli variables with parameters

\[
 e_i(a)=\Pr(Y_i\ne a_i\mid X_i)\ge q(X_i).
\]

To see the required stochastic comparison explicitly, take independent
uniform variables `U_i` on `[0,1]`. The vector
`1{U_i<=e_i(a)}` has the conditional distribution of the errors, and
coordinatewise dominates `B_i=1{U_i<=q(X_i)}`. Consequently,

\[
 \Pr\left(\sum_i\mathbf1\{Y_i\ne a_i\}\le k\mid X_1,...,X_n\right)
 \le \Pr\left(\sum_i B_i\le k\mid X_1,...,X_n\right).
\]

Union-bound over the at most `M_{n,d}` prediction vectors. The comparison
distribution on the right does not depend on `a`, even though the list
of prediction vectors depends on the inputs. After averaging over the
inputs, the `B_i` are independent Bernoulli variables with common
parameter `E q(X)=alpha`: the pairs `(X_i,U_i)` are independent.
This proves (1); (2) is its `k=0` case.

For completeness, let `B` have distribution `Bin(n,alpha)`. For `t>0`,
Markov's inequality gives

\[
 \Pr(B\le nr)\le e^{tnr}(1-\alpha+\alpha e^{-t})^n.
\]

For `0<r<alpha`, choose
`e^{-t}=r(1-alpha)/(alpha(1-r))`. Substitution gives
`exp(-n D(r||alpha))`. At `r=0`, let `t` tend to infinity.
This proves (3).

## Corollary 2: the best affine training error

For `n-1>=d`,

\[
 \log M_{n,d}\le \log 2+d\log\frac{e(n-1)}d.
 \tag{4}
\]

Indeed, put `N=n-1` and `x=d/N<=1`. Then

\[
 x^d\sum_{j=0}^d{N\choose j}
 \le\sum_{j=0}^d{N\choose j}x^j
 \le(1+x)^N\le e^d.
\]

For `0<=r<alpha`, the second derivative of `D(r||alpha)` with respect
to `r` is `1/(r(1-r))>=4`. Since the value and first derivative vanish
at `r=alpha`, integration twice gives
`D(r||alpha)>=2(r-alpha)^2`, with endpoints by continuity. Thus for
`0<u<=alpha`,

\[
 \Pr(E_{n,d}/n\le\alpha-u)
 \le M_{n,d}e^{-2nu^2}.
 \tag{5}
\]

The noninteger threshold is handled by taking its floor in (3).
If `n/d -> infinity`, (4) implies `log M_{n,d}/n -> 0`.
For example, for `0<delta<1`, with probability at least `1-delta`,

\[
 E_{n,d}/n\ge\alpha-
 \sqrt{\frac{\log M_{n,d}+\log(1/\delta)}{2n}}.
 \tag{6}
\]

If the square root exceeds `alpha`, (6) holds deterministically by
nonnegativity. In particular, for fixed `alpha>0`, every affine
classifier makes at least `(alpha-o(1))n` errors with probability tending
to one. If a Bayes classifier belongs to the affine class, its training
errors have distribution `Bin(n,alpha)`, and therefore
`E_{n,d}/n -> alpha` in probability. For this last upper bound, the
variance of that binomial proportion is at most `1/(4n)`, so Chebyshev's
inequality suffices.

## Corollary 3: symmetric Gaussian mixtures and growing signal

Let

\[
 S\sim\operatorname{Unif}\{-1,+1\},\quad
 X=S\mu+\sigma G,\quad G\sim N(0,I_d),\quad
 Y=SF,
 \tag{7}
\]

where `sigma>0`, `Pr(F=-1)=eta`, `0<=eta<1/2`, and `S,G,F` are
independent. The model permits parameters to vary with `n`. Put
`s=||mu||/sigma`.

For `mu!=0`, the ratio of the two conditional Gaussian densities is

\[
 \frac{\exp(-\|x-\mu\|^2/(2\sigma^2))}
 {\exp(-\|x+\mu\|^2/(2\sigma^2))}
 =\exp(2\mu^Tx/\sigma^2).
\]

Thus the Bayes classifier for `S` is `sign_+(mu^T x)`. Its error is
`Phi(-s)`, because conditional on `S=+1`,
`mu^T X=||mu||^2+sigma||mu|| Z` for a standard normal `Z`, and the
other class is symmetric. Flipping the label changes the posterior
`p_S(x)` into `eta+(1-2eta)p_S(x)`, preserving the Bayes decision.
The Bayes error for `Y` is consequently

\[
 \alpha=\eta+(1-2\eta)\Phi(-s).
 \tag{8}
\]

At `mu=0`, both labels are independent of `X` and (8) gives `alpha=1/2`.
Equations (1)–(6) apply with (8). In particular, fixed positive flip
rate rules out affine interpolation whenever `n/d -> infinity`, at
any signal strength. Fixed finite `s` also rules it out with `eta=0`.

More generally, define `A=log M_{n,d}`. From (2) and `log(1-alpha)<=-alpha`,

\[
 \Pr(E_{n,d}=0)\le \min\{1,\exp(A-n\alpha)\}.
 \tag{9}
\]

Hence `n alpha-A -> infinity` suffices to rule out interpolation.
The stronger condition `n alpha/A -> infinity` is convenient when
`alpha` tends to zero.

For an explicit signal obstruction with no flips, put `t=n/d -> infinity`.
For any fixed `epsilon` in `(0,2)`, if

\[
 s^2\le(2-\epsilon)\log t
 \tag{10}
\]

eventually, then the probability of affine interpolation tends to zero.
To check this, write `phi` for the standard normal density and
`h=1/(s+1)`. Monotonicity of `phi` on `[0,infinity)` gives

\[
 \Phi(-s)\ge\int_s^{s+h}\phi(z)\,dz
 \ge h\phi(s+h)
 =h\phi(s)e^{-sh-h^2/2}
 \ge\frac{e^{-1}}{\sqrt{2\pi}(s+1)}e^{-s^2/2},
\]

because `sh+h^2/2=1-h+h^2/2<=1` for `0<h<=1`.
Using (10),

\[
 \alpha\ge c\,\frac{t^{-1+\epsilon/2}}{1+\sqrt{\log t}}
\]

for an absolute positive `c`. Meanwhile (4) gives
`A<=log 2+d log(et)`. Therefore

\[
 \frac{n\alpha}{A}\ge
 c\frac{t^{\epsilon/2}}
 {(1+\sqrt{\log t})(\log(et)+\log 2)}\longrightarrow\infty.
\]

Also `A>=log 2>0`, so `n alpha-A -> infinity`, proving the claim.
This is a sufficient obstruction, not a sharp separation threshold and
not a sufficient condition for interpolation above the displayed scale.

## Corollary 4: what an interpolating network must do

Let `f` be any score function that strictly interpolates the sample:
`Y_i f(X_i)>0` for every `i`. For every affine classifier `h`,

\[
 \#\{i:\operatorname{sign}_+(f(X_i))\ne h(X_i)\}
 =\#\{i:Y_i\ne h(X_i)\}\ge E_{n,d}.
 \tag{11}
\]

Thus (6) is a simultaneous lower bound on the fraction of training
decisions on which *every* interpolating network must differ from
*every* affine classifier. With fixed `alpha>0` and `n/d -> infinity`,
that fraction is at least `alpha-o(1)`, regardless of network width.

In particular, a positive-margin limiting network with an affine
decision boundary cannot exist on a sample with `E_{n,d}>0`.
The probability of such a limit is bounded by (2), for any training
algorithm, any initialization, and any width. This applies to a
prospective extension of a theorem whose limiting network has both
positive training margins and a linear decision boundary.

There is also a direct obstruction to a stronger activation assumption.
Suppose a network has a nonzero output weight `a_j` and satisfies

\[
 a_jY_i\langle w_j,X_i\rangle>0\quad\hbox{for all }i.
 \tag{12}
\]

Then `sign_+(a_j<w_j,x>)` alone interpolates the sample, since its score
has the same sign as `Y_i` at every input. Thus the probability that
even one neuron satisfies (12) is at most (2). This includes the
class-dependent activation alignment used in the cited directional
convergence argument.

The positive-margin condition cannot be dropped from the limiting
statement: a normalized score can vanish on training inputs while
smaller terms still fit their labels. Equations (11)–(12) do not require
any convergence assumption. None of these statements rules out benign
overfitting by nonlinear ReLU classifiers.
