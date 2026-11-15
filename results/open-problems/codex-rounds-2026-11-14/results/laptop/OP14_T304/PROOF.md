# A contamination-safe reduction from TV to normalized Wasserstein sampling

Throughout, TV means `sup_B |mu(B)-nu(B)|`, and W2 uses Euclidean squared transport cost. All logarithms are natural.

## 1. Statement

Let f: R^d -> R be continuously differentiable, m-strongly convex, and L-smooth, with m > 0. Let pi have density proportional to exp(-f), and let x_* be its unique minimizer. Suppose a deterministic point c and a number D >= ||c-x_*|| are available. Let an oracle algorithm return Y with law mu satisfying TV(mu,pi) <= delta, where 0 < delta < 1. No moment assumption on Y is imposed.

Set

    a_d = (d/2) log 2,
    R = (2/sqrt(m)) sqrt(a_d + log(1/delta)),
    S = D + R,
    T(y) = c + (y-c) min{1, S/||y-c||},

where T(c)=c. Then

    W2(Law(T(Y)), pi) <= 2 sqrt(delta) (D + R + 1/sqrt(m)).       (1)

The map T uses no oracle calls. A valid D can be obtained using one gradient query at c:

    D = ||grad f(c)||/m.                                         (2)

For 0 < epsilon <= 1, put

    A = d + m D^2 + log(1/epsilon),
    delta = epsilon^2 d/(512 A).                                 (3)

With this choice, the output satisfies

    W2(Law(T(Y)), pi)^2 <= (15/16) epsilon^2 d/m
                         <= epsilon^2 d/m.                      (4)

Thus a TV sampler can be converted into a sampler with the normalized Wasserstein accuracy in T304, with at most one additional gradient query. The statement concerns a reduction, not a matching minimax lower bound.

## 2. A radial exponential-moment estimate

Translate x_* to zero and subtract f(x_*), writing F(x)=f(x+x_*)-f(x_*). Then F(0)=0, grad F(0)=0, and F(x)>=m||x||^2/2. In particular the normalization Z is positive and finite, and every polynomial moment exists.

For a unit vector theta and r>=0, strong monotonicity of the gradient gives

    <grad F(r theta), theta> >= m r.

Integrating from r to r/lambda, for 0<lambda<1, gives

    F(y/lambda)-F(y) >= (m/2)(lambda^(-2)-1)||y||^2.             (5)

Indeed, if y=r theta, the left side is the integral of <grad F(s theta),theta> over [r,r/lambda]; integrating m s gives the right side. The case y=0 is immediate.

For 0<t<m/2, set lambda=sqrt(1-2t/m). Changing variables y=lambda x yields

    E_pi exp(t||X-x_*||^2)
      = lambda^(-d) Z^(-1)
        integral exp(-F(y/lambda)+t||y||^2/lambda^2) dy
      <= lambda^(-d) Z^(-1) integral exp(-F(y)) dy
      = (1-2t/m)^(-d/2).                                       (6)

The inequality uses (5) and the identity

    t/lambda^2 = (m/2)(lambda^(-2)-1).

In particular, writing r=||X-x_*||,

    P_pi(r^2 > u) <= 2^(d/2) exp(-m u/4)                       (7)

for u>=0, by Markov's inequality at t=m/4.

## 3. The target's projection error

Projection onto the ball B(c,S) moves a point x by exactly (||x-c||-S)_+. Since ||c-x_*||<=D and S=D+R,

    ||x-T(x)|| <= (||x-x_*||-R)_+.

For r>=0, (r-R)_+^2 <= (r^2-R^2)_+. By the layer-cake identity and (7),

    E_pi ||X-T(X)||^2
      <= integral from R^2 to infinity P_pi(r^2>u) du
      <= (4/m) 2^(d/2) exp(-m R^2/4)
      = 4 delta/m.                                             (8)

The last equality follows from m R^2/4 = a_d+log(1/delta). Coupling X with T(X) therefore gives

    W2(T_# pi,pi) <= 2 sqrt(delta/m).                           (9)

## 4. Coupling after projection

A measurable map contracts TV: for every Borel B,

    |T_#mu(B)-T_#pi(B)|
      = |mu(T^(-1)(B))-pi(T^(-1)(B))| <= delta.

Both projected measures are supported in a ball of diameter 2S. To see the resulting transport bound explicitly, take their densities p,q with respect to their sum and let rho have density min(p,q). Its mass is 1-alpha, where alpha is their TV distance. Match this common mass identically. If alpha>0, couple the two residual probability measures in any way. Every residual pair is at distance at most 2S. (If alpha=0 there is no residual.) This gives

    W2(T_#mu,T_#pi)^2 <= 4 S^2 alpha <= 4 S^2 delta.            (10)

The projected measures have finite second moments even when mu does not. The triangle inequality for W2, together with (9) and (10), proves (1).

For (2), strong convexity and grad f(x_*)=0 give

    m||c-x_*||^2 <= <grad f(c),c-x_*>
                 <= ||grad f(c)|| ||c-x_*||.

If c=x_*, (2) is immediate; otherwise division proves it.

## 5. Explicit accuracy allocation

Let t=log(1/epsilon)>=0 and A=d+mD^2+t. Then A>=d>=1. From (3),

    s := log(1/delta) = 2t+log 512+log(A/d).

Since log u<=u-1 for u>=1, and d>=1,

    log(A/d) <= A/d-1 <= A-1.

Also t<=A and log 512<7, so

    s <= 2A+7+A-1 = 3A+6 <= 9A.                              (11)

The elementary inequality log 2<1 now gives

    mR^2 = 4(a_d+s) <= 2d+4s <= 38A.                          (12)

By Cauchy--Schwarz in R^3,

    m(D+R+1/sqrt(m))^2
      <= 3(mD^2+mR^2+1)
      <= 3(A+38A+A) = 120A.                                   (13)

Squaring (1) and applying (13) yields

    W2(T_#mu,pi)^2 <= 480 delta A/m
                   = (480/512) epsilon^2 d/m
                   = (15/16) epsilon^2 d/m,

which proves (4). In particular, delta<=1/512, so this choice lies in the usual small-TV-error range.

## 6. Corollary for a subpolynomial TV query bound

The following input is a cited preprint theorem, not proved here. Wei Guo, Bo Yuan, Ye He, Jiaming Liang, Molei Tao, and Yongxin Chen, *Subpolynomial-Query Proximal Sampling Beyond Log-Concavity*, arXiv:2611.03442v1, Theorem 3, state: for a C^2 potential with L-Lipschitz gradient and an m-log-Sobolev target, their sampler uses at most

    C_nu kappa (d+kappa+delta^(-1)+G0)^nu                      (14)

gradient queries on every execution, for each fixed nu>0 and 0<delta<1/4. Here d>=2, kappa=L/m, c is a supplied point, and G0=||grad f(c)||^2/L. The constants depend only on nu. See [the theorem and its assumptions](https://arxiv.org/html/2611.03442v1#S2.SS3).

For C^2 m-strongly convex L-smooth f, the required m-log-Sobolev inequality holds; this implication is stated in Section 2.2 of the same paper. Consequently (14) applies. No assertion that (14) extends verbatim to merely C^1 potentials is needed for this corollary.

Use (2), so mD^2=kappa G0, and let

    B=d+kappa+epsilon^(-1)+G0.

For 0<epsilon<=1, B>=1 and

    A=d+kappa G0+log(1/epsilon)
      <= B+B^2 <= 2B^2.                                      (15)

Here d+log(1/epsilon)<=d+epsilon^(-1)<=B and kappa G0<=B^2. Thus

    delta^(-1) = 512A/(epsilon^2 d) <= 1024B^4,
    d+kappa+delta^(-1)+G0 <= 1025B^4.                         (16)

Given any eta>0, apply (14) with nu=eta/4 and the tolerance (3), then project. The one query used to compute D gives a deterministic total query bound

    1+C_(eta/4) kappa (1025B^4)^(eta/4)
      <= C'_eta kappa B^eta.                                 (17)

The last inequality absorbs 1 because kappa B^eta>=1. Therefore, conditional on the cited TV theorem, for every fixed eta>0 a C^2 strongly log-concave target can be sampled to

    W2 <= epsilon sqrt(d/m)

using at most

    C'_eta kappa (d+kappa+epsilon^(-1)+G0)^eta

gradient queries, uniformly over the algorithm's randomness. The constants can be large and no bound on computation between queries is asserted.

For fixed kappa, epsilon, and G0 this rules out the necessity of any fixed positive dimension exponent for this oracle model. It does not give the sharp subpolynomial rate, a high-accuracy bound polynomial in log(1/epsilon), an arbitrary-value-only oracle bound, or an improved lower bound.

## 7. Why an unmodified TV output is insufficient

Even for pi=N(0,I_d), the law mu=(1-delta)pi+delta H has TV(mu,pi)<=delta for every probability law H. If H has an infinite second moment, mu does too and W2(mu,pi)=infinity. Hence the inference from TV accuracy to finite Wasserstein error cannot omit a moment-control step. Projection above supplies it without evaluating f at Y and without assuming anything about contaminated outputs.
