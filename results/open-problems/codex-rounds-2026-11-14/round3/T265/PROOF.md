# Localized interpolation by bias-free two-layer ReLU networks

Write rho(z)=max(z,0) and sign_+(z)=+1 for z>=0, -1 otherwise. A two-layer network here has score

\[
f(x)=\sum_{j=1}^m a_j\rho(w_j^\top x),
\]

with real output weights and no hidden or output biases. Its classification risk is
\(R(f)=\Pr(\operatorname{sign}_+(f(X))\ne Y)\), evaluated on a fresh independent pair. All population statements about a fitted network condition on its training sample.

The construction below is an explicit interpolation rule. It is not a gradient-descent result.

## 1. Model and statement

Let d>=2, sigma>0, mu in R^d, and 0<=eta<1/2. Independently generate

\[
S\sim\operatorname{Unif}\{-1,+1\},\qquad G\sim N(0,I_d),\qquad
\Pr(F=-1)=\eta,
\]

and set X=S mu+sigma G and Y=SF. The training pairs (X_i,Y_i), i=1,...,n, are iid. Put

\[
s=\|\mu\|/\sigma,\qquad a=1-2\eta,\qquad
\alpha=\eta+a\Phi(-s),\qquad
C_s=\frac1\pi+\frac{s}{\sqrt{2\pi}}.
\tag{1}
\]

The number alpha is the Bayes classification risk. When mu!=0 the Bayes decision is sign_+(mu^T x), since the ratio of the two Gaussian component densities is exp(2 mu^T x/sigma^2), and flipping labels with probability eta<1/2 preserves the posterior decision. Its clean-label error is Phi(-s), yielding (1). When mu=0, Y is independent of X and alpha=1/2.

**Theorem.** There is an explicit measurable interpolation rule, using only the observed data, with a bias-free two-layer ReLU score f_n of width at most 6n+2, such that almost surely

\[
f_n(X_i)=Y_i\quad(1\le i\le n).
\tag{2}
\]

Let

\[
v_n=\frac1n\sum_{i=1}^nY_iX_i,\qquad g_n(x)=v_n^\top x.
\tag{3}
\]

For every nonexceptional sample,

\[
\Pr_X\{f_n(X)\ne g_n(X)\mid\text{sample}\}
\le \frac{2C_s}{n^2}.
\tag{4}
\]

The expected excess classification risk obeys

\[
0\le\mathbb E R(f_n)-\alpha
\le \sqrt{\frac2\pi}
\sqrt{\frac{d+4\eta(1-\eta)s^2}{n}}
+\frac{2C_s}{n^2}.
\tag{5}
\]

In particular, for bounded s and d/n tending to zero, this data-dependent interpolating rule is Bayes consistent in expected risk and in probability. It works in fixed dimension d>=2 as well. The conclusion concerns classification risk; it gives no population squared-loss bound.

For s>0 there is a sharper bound. With V=(d+4 eta(1-eta)s^2)/n,

\[
\mathbb E R(f_n)-\alpha\le\sqrt{\frac2\pi}
\min\left\{\sqrt V,\frac{V}{(1-2\eta)s}\right\}
+\frac{2C_s}{n^2}.
\tag{5a}
\]

For fixed s>0 and fixed eta<1/2 this is O(d/n+n^{-2}).

## 2. A homogeneous triangular correction

For t in R, h>0, and (u,v) in R^2, define

\[
H_{t,h}(u,v)=\frac{|v-(t-h)u|-2|v-tu|+|v-(t+h)u|}{2h}.
\tag{6}
\]

If u!=0 and z=v/u, factoring out |u| gives

\[
H_{t,h}(u,v)=|u|\left(1-\frac{|z-t|}{h}\right)_+.
\tag{7}
\]

To check (7), put r=z-t. For r<=-h or r>=h the second difference |r+h|-2|r|+|r-h| is zero. For -h<=r<=0 it is 2(h+r), and for 0<=r<=h it is 2(h-r). Division by 2h proves the formula in every case. If u=0, (6) is zero, since its numerator is |v|-2|v|+|v|. Thus H is continuous, even under (u,v)->(-u,-v), nonnegative, and positively homogeneous. It vanishes outside the paired cones

\[
u\ne0,\qquad |v/u-t|<h.
\tag{8}
\]

It is positive exactly inside (8). The two cones are antipodal; a single cone alone would not give this even function.

Since |z|=rho(z)+rho(-z), equation (6) is a sum of six ReLU neurons with linear inputs and no biases. In R^d use u=x_1, v=x_2, and let

\[
q(r)=e_2-r e_1.
\]

The six first-layer weights are q(t-h), -q(t-h), q(t), -q(t), q(t+h), -q(t+h). Their output coefficients are, in this order, (1,1,-2,-2,1,1)/(2h).

## 3. Interpolation rule

Write U_i=(X_i)_1 and V_i=(X_i)_2. Almost surely every U_i is nonzero, and all slopes T_i=V_i/U_i are distinct. Indeed, the two-dimensional Gaussian mixture has a Lebesgue density. The ratio has a density by the change of variables used in Section 4, so independent ratios do not coincide with positive probability. A finite union over the indices proves the assertion for the full sample.

On this event define

\[
\Delta_i=\min_{j\ne i}|T_i-T_j|,\qquad
h_i=\min\{n^{-3},\Delta_i/3\}.
\tag{9}
\]

For n=1 set Delta_1=+infinity. Every h_i is positive. The intervals (T_i-h_i,T_i+h_i) are pairwise disjoint, because for i!=j both h_i and h_j are at most |T_i-T_j|/3, so their sum is strictly smaller than the distance between their centers.

Set

\[
c_i=Y_i-g_n(X_i),\qquad A_i=\frac{c_i}{|U_i|},\qquad
f_n(x)=g_n(x)+\sum_{i=1}^n A_i H_{T_i,h_i}(x_1,x_2).
\tag{10}
\]

All coefficients are finite. At x=X_i, the i-th triangular function equals |U_i| by (7). Every other triangular function vanishes, since T_i is outside its interval. Therefore f_n(X_i)=g_n(X_i)+c_i=Y_i, proving (2).

Represent g_n as rho(v_n^T x)-rho(-v_n^T x), and each H as the six-neuron representation above. This proves the width bound 6n+2. On the null exceptional event define f_n=0. Finite sums, ratios with nonzero denominators, absolute values, and finite minima show that the rule is measurable. In particular it requires neither mu, sigma nor eta.

Every correction is supported in the union of the paired cones with slope in

\[
I_n=\bigcup_{i=1}^n(T_i-h_i,T_i+h_i).
\tag{11}
\]

This is a statement about the score itself, so it also bounds disagreement of the two classifiers.

## 4. A density bound for Gaussian slopes

Scale the first two coordinates of a fresh X by sigma. Their distribution is the equal mixture N(m,I_2) and N(-m,I_2), where m=(mu_1,mu_2)/sigma. The ratio V/U is unchanged by (U,V)->(-U,-V), so both components have the same ratio law. It suffices to use N(m,I_2).

Write m=(b,c), L=1+t^2, and r=(b+tc)/L. The change of variables (u,t)->(u,tu) has absolute Jacobian |u|. Completing the square gives the ratio density

\[
p_T(t)=\frac1{2\pi}\exp\left(-\frac{(bt-c)^2}{2L}\right)
\int_{\mathbb R}|u|\exp\left(-\frac L2(u-r)^2\right)\,du.
\tag{12}
\]

The square completion follows by expanding
(u-b)^2+(tu-c)^2=L(u-r)^2+(bt-c)^2/L. The exceptional line u=0 has Gaussian measure zero, so this change of variables accounts for the whole probability law.

Using |u|<=|u-r|+|r|, the integral in (12) is at most

\[
\frac2L+|r|\sqrt{\frac{2\pi}{L}}.
\]

The first term follows by the substitution z=u-r and integrating |z| exp(-Lz^2/2); the second is the Gaussian integral. Since |b+tc|<=||m||sqrt(L) and the exponential prefactor is at most one,

\[
p_T(t)\le\frac1{\pi L}+\frac{|b+tc|}{\sqrt{2\pi}L^{3/2}}
\le\frac{1/\pi+\|m\|/\sqrt{2\pi}}{1+t^2}
\le\frac{C_s}{1+t^2}\le C_s.
\tag{13}
\]

For a fixed training sample its intervals in (11) are fixed, while the test X is independent. Hence (13) gives

\[
\Pr_X(T\in I_n\mid\text{sample})
\le2C_s\sum_i h_i\le\frac{2C_s}{n^2},
\]

proving (4), even though the intervals depend on all training labels through the fitted score. In fact the interval locations and widths use only training inputs. A bound larger than one may always be truncated to one.

As a second derivation of the constant, let q_theta be the directional density of N(m,I_2) and let k=m^T(cos(theta),sin(theta)). Adding opposite directions and integrating the radius gives

\[
q_\theta+q_{\theta+\pi}
=\frac1{2\pi}e^{-(\|m\|^2-k^2)/2}
\int_{\mathbb R}|r|e^{-(r-k)^2/2}\,dr
\le\frac1\pi+\frac{|k|}{\sqrt{2\pi}}\le C_s.
\]

Here the same triangle bound yields the displayed integral bound 2+|k|sqrt(2pi). The projective angle theta=arctan(t) has Jacobian 1/(1+t^2), recovering (13) by polar coordinates. When m=0, (12) gives the exact Cauchy density 1/[pi(1+t^2)].

## 5. Risk of the sample-mean baseline

Independence and the identities E F=a and E SG=0 give

\[
\mathbb E(YX)=a\mu,
\qquad
\mathbb E\|YX\|^2=\|\mu\|^2+d\sigma^2.
\]

Thus, for e=v_n-a mu,

\[
\mathbb E\|e\|^2
=\frac{d\sigma^2+(1-a^2)\|\mu\|^2}{n}
=\frac{d\sigma^2+4\eta(1-\eta)\|\mu\|^2}{n}.
\tag{14}
\]

The cross terms between centered sample summands vanish by independence. Independently, YX=F mu+sigma SFG, where SFG is standard Gaussian independent of F: conditioning on S,F only flips the sign of G. Therefore the covariance is sigma^2 I_d+4 eta(1-eta) mu mu^T, whose trace divided by n gives (14) again.

For a fixed v!=0, symmetry between the two latent classes gives

\[
R(v^\top\cdot)=\eta+a\Phi\left(-\frac{v^\top\mu}{\sigma\|v\|}\right).
\tag{15}
\]

For mu!=0, let v_0=a mu. Normalization and the triangle inequality imply

\[
\left\|\frac v{\|v\|}-\frac{v_0}{\|v_0\|}\right\|
\le\frac{2\|v-v_0\|}{\|v_0\|}.
\tag{16}
\]

For completeness, insert v/||v_0|| between the two vectors. The resulting upper bound is
| ||v_0||-||v|| |/||v_0||+||v-v_0||/||v_0||, and the reverse triangle inequality proves (16). Therefore

\[
0\le s-\frac{v^\top\mu}{\sigma\|v\|}
\le\frac{2\|v-a\mu\|}{a\sigma}.
\]

The normal distribution function is 1/sqrt(2pi)-Lipschitz, because its density is bounded by that constant. Equations (1) and (15) yield

\[
0\le R(v^\top\cdot)-\alpha
\le\sqrt{\frac2\pi}\frac{\|v-a\mu\|}{\sigma}.
\tag{17}
\]

If v=0, sign_+(v^T x) is constant and its risk is 1/2. Its excess risk is a[Phi(s)-1/2]<=a s/sqrt(2pi), also bounded by the right side of (17), since ||v-a mu||=a||mu||. If mu=0, the excess risk of every classifier is zero. Thus (17) covers the degenerate cases too.

Apply (17) conditionally with v=v_n, average, and use Cauchy–Schwarz with (14). This gives

\[
\mathbb E R(g_n)-\alpha
\le\sqrt{\frac2\pi}\sqrt{\frac{d+4\eta(1-\eta)s^2}{n}}.
\tag{18}
\]

For the sharper estimate assume s>0. For v!=0 let theta be the angle between v and mu. The exact identity between unit vectors gives

\[
s-\frac{v^\top\mu}{\sigma\|v\|}
=s(1-\cos\theta)
=\frac{s}{2}\left\|\frac v{\|v\|}-\frac\mu{\|\mu\|}\right\|^2
\le\frac{2\|v-a\mu\|^2}{a^2\sigma\|\mu\|}.
\]

Use (15) and the same normal-density bound to obtain

\[
R(v^\top\cdot)-\alpha
\le\sqrt{\frac2\pi}\frac{\|v-a\mu\|^2}{a\sigma\|\mu\|}.
\tag{18a}
\]

When v=0 the earlier bound a[Phi(s)-1/2]<=a s/sqrt(2pi) is at most the right side of (18a), which equals sqrt(2/pi) a s. Averaging (18a) with (14) yields sqrt(2/pi) V/(a s). Take the smaller of this and (18) to prove the baseline part of (5a).

Finally the pointwise difference of the two misclassification indicators is at most the indicator of classifier disagreement, itself at most 1{f_n(X)!=g_n(X)}. Add (4) to (18) to prove (5), and to the improved baseline bound to prove (5a). Nonnegativity follows from the Bayes definition of alpha. If the right side tends to zero, Markov's inequality applied to the nonnegative excess risk gives convergence in probability.

One also obtains a finite-sample probability statement: for 0<delta<1, Markov's inequality on (14) and (17) give, with probability at least 1-delta,

\[
R(f_n)-\alpha\le
\sqrt{\frac{2}{\pi\delta}}
\sqrt{\frac{d+4\eta(1-\eta)s^2}{n}}+\frac{2C_s}{n^2}.
\tag{19}
\]

## 6. Relation to the earlier affine obstruction

Let M_(n,d)=2 sum_{j=0}^{min(d,n-1)} binom(n-1,j). The earlier result gives, with probability at least 1-delta,

\[
\min_{\text{affine }h}\frac1n\#\{i:h(X_i)\ne Y_i\}
\ge\alpha-\sqrt{\frac{\log M_{n,d}+\log(1/\delta)}{2n}}.
\tag{20}
\]

The minimum is over affine classifiers, using the same tie convention. Since f_n(X_i)=Y_i, replacing Y_i in (20) by sign_+(f_n(X_i)) changes no indicator. If n/d tends to infinity and alpha stays bounded below, the right side is alpha-o(1) with probability tending to one, by choosing delta tending to zero slowly and using log M_(n,d)=o(n).

Thus the interpolating classifier differs from *every* affine classifier on a positive fraction of the training points, while its population disagreement with the particular data-dependent affine classifier sign_+(g_n) is at most 2C_s/n^2. For bounded s this tends to zero. Equations (2), (4), and (20) give the nonlinear localization left unresolved by the earlier affine reduction at the level of an explicit interpolation rule.

## 7. Parameter cost and limits

For a displayed representation define its path norm as P=sum_j |a_j| ||w_j||. The representation in Section 3 has

\[
P=2\|v_n\|+\sum_i\frac{|A_i|}{h_i}
\left[\sqrt{1+(T_i-h_i)^2}+2\sqrt{1+T_i^2}
+\sqrt{1+(T_i+h_i)^2}\right].
\tag{21}
\]

This follows by summing the norms of the six weights and their absolute coefficients. In particular the i-th summand is at most 4|A_i|(1+|T_i|+h_i)/h_i. No bound on these data-dependent quantities is asserted.

Some cost of narrowing these particular corrections is unavoidable. Write B=f_n-g_n. At X_i it has value c_i. At x_i'=X_i+h_i U_i e_2 its slope is T_i+h_i, and every triangular correction is zero, including the i-th one at its endpoint. Hence B(x_i')=0 and ||x_i'-X_i||=h_i|U_i|. If c_i!=0, the Lipschitz constant of B is at least

\[
\frac{|c_i|}{h_i|U_i|}=\frac{|A_i|}{h_i}.
\tag{22}
\]

Every ReLU representation has Lipschitz constant at most its path norm, since rho is 1-Lipschitz. Therefore every representation of this same B has path norm at least the maximum of (22). For a fixed sample with some c_i!=0, shrinking that h_i to zero sends this lower bound to infinity. This does not prove a norm lower bound for every possible localized interpolant.

The paired corrections respect the identity

\[
f(x)-f(-x)=\left(\sum_j a_jw_j\right)^\top x
\]

for every bias-free shallow ReLU network. Indeed rho(z)-rho(-z)=z. Here each correction is even and only g_n contributes to the odd part. Exact antipodal sample collisions with incompatible even corrections would be an obstruction; they have probability zero in this Gaussian model.

These networks have width growing linearly with n and potentially very large norms. No claim is made that GD from random initialization selects them, that they minimize a margin or norm objective, or that bounded-width networks admit the same construction. The consistency statement is for noisy-label classification risk alpha; fixed eta>0 prevents risk from tending to zero. Rescaling f_n by a scalar tending to infinity preserves its classifier and drives its empirical logistic loss to zero, but says nothing about a GD trajectory.
