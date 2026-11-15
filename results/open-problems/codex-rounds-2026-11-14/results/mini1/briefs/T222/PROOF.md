# A finite-order reduction for the planar TSP variance limit

Let Q = [0,1]^2, let X_1,...,X_n be independent uniform points in Q, and
let f_n(X) = L_n be the length of the shortest closed Euclidean tour.
The square and the variance are unscaled throughout. Put f_1 = 0; a tour
on two points traverses their connecting segment twice. Repeated locations
are allowed and make no difference to the arguments.

For A contained in [n] = {1,...,n}, define

\[
 g_{n,A}(X_A)=\mathbb E[f_n(X)\mid X_A],\qquad
 h_{n,A}(X_A)=\sum_{B\subseteq A}(-1)^{|A|-|B|}g_{n,B}(X_B).
\]

Here g_{n,empty} = E[f_n]. Define the order-j interaction energy by

\[
 V_{n,j}=\sum_{|A|=j}\mathbb E[h_{n,A}^2],\qquad 1\le j\le n,
 \tag{1}
\]

and put V_{n,j} = 0 for j > n. All these quantities exist because
0 <= f_n <= n sqrt(2).

**Theorem.** For every n >= 2,

\[
 \operatorname{Var}(L_n)=\sum_{j\ge1}V_{n,j},\qquad
 \sum_{j\ge1}jV_{n,j}\le8.
 \tag{2}
\]

Consequently, for every integer m >= 0,

\[
 0\le \operatorname{Var}(L_n)-\sum_{j=1}^mV_{n,j}
 \le \frac8{m+1}.
 \tag{3}
\]

There is also the asymptotic refinement

\[
 \limsup_{n\to\infty}\sum_{j\ge1}jV_{n,j}\le\frac4\pi,
 \qquad
 \limsup_{n\to\infty}\sum_{j>m}V_{n,j}
 \le\frac4{\pi(m+1)}.
 \tag{3a}
\]

If V_{n,j} converges to v_j as n tends to infinity for each fixed j, then

\[
 \lim_{n\to\infty}\operatorname{Var}(L_n)=\sum_{j\ge1}v_j,
 \qquad \sum_{j\ge1}jv_j\le\frac4\pi.
 \tag{4}
\]

More precisely, under this hypothesis,

\[
 \left|\operatorname{Var}(L_n)-\sum_{j\ge1}v_j\right|
 \le \sum_{j=1}^m|V_{n,j}-v_j|+\frac8{m+1}.
 \tag{5}
\]

The constants 8 and 4/pi are upper bounds, not proposed values for
the limiting variance or claimed improvements over existing variance
upper bounds. The assertion that the fixed-order energies converge is a
remaining hypothesis, not a conclusion of the theorem.

## 1. A nearest-neighbor bound valid at the boundary

Fix x in Q and let S consist of n-1 independent uniform points in Q. Put
R(x,S) = min_{y in S}|x-y|. For 0 <= r <= sqrt(2), put t = r/sqrt(2).
Convexity gives

\[
 x+t(Q-x)\subseteq Q.
\]

Every point in this homothetic square has distance at most
t diam(Q) = r from x. Its area is t^2 = r^2/2. Therefore

\[
 |Q\cap B(x,r)|\ge r^2/2.
 \tag{6}
\]

The n-1 sample points miss this intersection independently, so for
0 <= u <= 2,

\[
 \mathbb P(R(x,S)^2>u\mid x)
 \le(1-u/2)^{n-1}.
\]

Distances in Q are at most sqrt(2). Integrating the tail yields

\[
 \mathbb E[R(x,S)^2\mid x]
 \le\int_0^2(1-u/2)^{n-1}\,du=\frac2n.
 \tag{7}
\]

This holds uniformly in x, including corners and edges.

There is a sharper averaged asymptotic. If X is an additional independent
uniform point and S has n-1 points, write mu_n = E[R(X,S)^2]. Then

\[
 \lim_{n\to\infty}n\mu_n=\frac1\pi.
 \tag{7a}
\]

For the lower bound, |Q intersect B(x,sqrt(u))| <= pi u gives

\[
 \mathbb P(R(x,S)^2>u\mid x)\ge(1-\pi u)^{n-1},
 \qquad 0\le u\le1/\pi.
\]

Its integral is 1/(pi n), so n mu_n >= 1/pi.

For the upper bound, fix 0 < epsilon < 1/2. If x belongs to
[epsilon,1-epsilon]^2, disks of radius at most epsilon lie entirely in Q.
The exact disk area for u <= epsilon^2 and (6) for larger u give

\[
 \begin{split}
 n\mathbb E[R(x,S)^2\mid x]
 &\le n\int_0^{\epsilon^2}(1-\pi u)^{n-1}\,du
   +n\int_{\epsilon^2}^2(1-u/2)^{n-1}\,du\\
 &\le\frac1\pi+2(1-\epsilon^2/2)^n.
 \end{split}
\]

The excluded boundary strip has area 4 epsilon - 4 epsilon^2, at most
4 epsilon. On that strip use (7). Averaging therefore yields the explicit
estimate

\[
 \frac1\pi\le n\mu_n
 \le\frac1\pi+2(1-\epsilon^2/2)^n+8\epsilon.
 \tag{7b}
\]

First let n increase with epsilon fixed, then let epsilon decrease to
zero. This proves (7a) without an assumption about optimal tours.

## 2. Insertion and replacement

Write T(S) for the optimum tour length through a nonempty finite set S,
with the conventions stated above. Define

\[
 \delta(x;S)=T(S\cup\{x\})-T(S).
\]

Removing x from an optimal tour and joining its two neighbors cannot
increase length, by the triangle inequality. For a two-point tour the
remaining singleton has length zero. Thus delta(x;S) >= 0.

If S has at least two points, choose a nearest point y in S and one edge
{y,z} incident to y in an optimal tour of S. Replace that edge by
{y,x},{x,z}. The increase is

\[
 |y-x|+|x-z|-|y-z|\le2|x-y|=2R(x,S).
\]

This also applies to a two-point base tour, using either traversal of its
segment. If S is a singleton, inserting x gives exactly 2R(x,S).
Consequently, for every nonempty S,

\[
 0\le\delta(x;S)\le2R(x,S).
 \tag{8}
\]

Let X_i' be an independent uniform point and let X^{(i)} be X with only
coordinate i replaced by X_i'. Use the same base set
S_i = {X_k : k != i} for both tours. Their difference is

\[
 f_n(X)-f_n(X^{(i)})=\delta(X_i;S_i)-\delta(X_i';S_i).
\]

For a,b >= 0, (a-b)^2 <= a^2+b^2. Equations (7) and (8) therefore give

\[
 \mathbb E[(f_n(X)-f_n(X^{(i)}))^2]
 \le 2\mathbb E[\delta(X_i;S_i)^2]
 \le8\mathbb E[R(X_i,S_i)^2]\le\frac{16}{n}.
 \tag{9}
\]

## 3. Orthogonality and the exact resampling identity

For every nonempty A and every i in A,

\[
 \mathbb E[h_{n,A}(X_A)\mid X_{A\setminus\{i\}}]=0.
 \tag{10}
\]

To see this, pair each summand indexed by B not containing i with the
summand indexed by B union {i}. Integration over X_i changes
g_{n,B union {i}} to g_{n,B}, since the coordinates are independent; the
two signs are opposite. If A != C, choose a coordinate in one of A,C but
not the other. Integrating over that coordinate using (10) proves
E[h_{n,A}h_{n,C}] = 0.

Summing the defining formula for h_{n,A} over all A contained in [n]
leaves only g_{n,[n]} = f_n: for a fixed B the coefficient is
sum_{A: B subset A subset [n]} (-1)^{|A|-|B|}, which is zero unless
B = [n], when it is one. Thus

\[
 f_n-\mathbb E f_n=\sum_{\varnothing\ne A\subseteq[n]}h_{n,A}.
 \tag{11}
\]

Orthogonality proves the variance equality in (2).

Conditionally on X_{-i} = (X_k : k != i), f_n(X) and f_n(X^{(i)}) are
independent identically distributed random variables. Hence

\[
 \frac12\mathbb E[(f_n(X)-f_n(X^{(i)}))^2]
 =\mathbb E[\operatorname{Var}(f_n\mid X_{-i})].
 \tag{12}
\]

Integrating (11) over X_i removes exactly those components whose index
sets contain i. Therefore

\[
 f_n-\mathbb E[f_n\mid X_{-i}]=\sum_{A:i\in A}h_{n,A}.
\]

Squaring, taking expectation and using orthogonality in the original
product space gives

\[
 \mathbb E[\operatorname{Var}(f_n\mid X_{-i})]
 =\sum_{A:i\in A}\mathbb E[h_{n,A}^2].
 \tag{13}
\]

Summing (12)-(13) over i counts each component exactly |A| times:

\[
 \sum_{j\ge1}jV_{n,j}
 =\frac12\sum_{i=1}^n
    \mathbb E[(f_n(X)-f_n(X^{(i)}))^2]
 \le\frac12 n\frac{16}{n}=8.
 \tag{14}
\]

This proves (2). Since j >= m+1 in the omitted tail, (3) follows.

Before applying the last inequality in (9), the same calculation gives
sum_j j V_{n,j} <= 4 n mu_n. Equation (7a) proves (3a). In particular,
(7b) supplies the finite-n refinement

\[
 \sum_j jV_{n,j}\le
 \min\left\{8,\frac4\pi+8(1-\epsilon^2/2)^n+32\epsilon\right\},
 \quad 0<\epsilon<1/2.
 \tag{14a}
\]

For each finite M, coefficient convergence and (3a) imply
sum_{j=1}^M j v_j <= 4/pi. Letting M increase proves the second assertion
of (4), and in particular the limiting tail has size at most 8/(m+1).
Both the finite-n tail and the limiting tail belong to the same interval
[0,8/(m+1)]. Their difference in absolute value is at most 8/(m+1).
This proves (5). First let n increase for fixed m, and then let m
increase; (4) follows.

The spectra are also precompact in the space of absolutely summable
sequences. Indeed, each coordinate belongs to [0,8/j], so successive
subsequence selections and a diagonal argument give coordinatewise
convergence along a subsequence of any given sequence. Its limit has
weighted sum at most 8 by the finite-sum argument above. For this
subsequence, the sum of absolute differences of all coordinates is at most
the corresponding sum up to m plus 16/(m+1), using (3) for both tails.
First increase the subsequence index, then m. This proves convergence in
the norm sum_j |V_j|. It proves existence of subsequential spectra, not
their uniqueness.

## 4. Equivalent covariance formulas and another sufficient condition

For 0 <= rho <= 1, form Y^rho by retaining each X_i with probability rho
and otherwise replacing it by an independent uniform point. All retention
decisions and fresh points are independent. Define

\[
 C_n(\rho)=\operatorname{Cov}(f_n(X),f_n(Y^\rho)).
\]

Given X, a component h_{n,A}(Y_A^rho) has conditional expectation
rho^{|A|} h_{n,A}(X_A). Indeed, if any coordinate of A is refreshed,
integration over that coordinate gives zero by (10); if all are retained,
the component is unchanged. Using (11) and orthogonality gives

\[
 C_n(\rho)=\sum_{j\ge1}\rho^j V_{n,j}.
 \tag{15}
\]

In particular, these covariance functions are increasing, and

\[
 0\le C_n'(\rho)=\sum_{j\ge1}j\rho^{j-1}V_{n,j}\le8,
 \qquad 0\le\rho\le1.
 \tag{16}
\]

The endpoint at zero is interpreted by the polynomial derivative.
Since 1-rho^j <= j(1-rho), (14)-(15) imply

\[
 0\le\operatorname{Var}(L_n)-C_n(\rho)\le8(1-\rho).
 \tag{17}
\]

Equation (3a) also gives
limsup_n (Var(L_n)-C_n(rho)) <= (4/pi)(1-rho) for each fixed rho.

Thus it is also sufficient to prove convergence of C_n(rho_r) for one
sequence rho_r in [0,1) tending to 1. For completeness, if a_r is the
limit at rho_r, then (16) gives
|a_r-a_s| <= 8|rho_r-rho_s|. The a_r have a limit a, and (17) gives
limsup_n |Var(L_n)-a| <= 8(1-rho_r)+|a_r-a|. Let r tend to infinity.
No control of n-dependent retention probabilities is required.

The full centered length has an explicit finite-order approximation:

\[
 F_n^{(m)}=\sum_{1\le|A|\le m}h_{n,A},\qquad
 \mathbb E[(L_n-\mathbb E L_n-F_n^{(m)})^2]\le\frac8{m+1}.
 \tag{18}
\]

Its fixed-order coefficients can be expressed without constructing every
component separately. Put

\[
 K_{n,k}=\operatorname{Var}(\mathbb E[f_n\mid X_1,\ldots,X_k]),
 \qquad K_{n,0}=0.
\]

Conditioning (11) on the first k variables keeps exactly the components
supported in those variables. Symmetry makes E[h_{n,A}^2] depend only on
|A|. If a_{n,j} is this common value, then

\[
 K_{n,k}=\sum_{j=1}^k\binom{k}{j}a_{n,j},\qquad
 V_{n,j}=\binom nj a_{n,j}.
\]

For 1 <= j <= n, binomial inversion yields the explicit formula

\[
 V_{n,j}=\binom nj\sum_{k=0}^j(-1)^{j-k}\binom jk K_{n,k}.
 \tag{19}
\]

To verify the inversion, the coefficient of a_{n,l} in its right-hand
sum before multiplication by binom(n,j) is
binom(j,l) sum_{k=l}^j (-1)^{j-k} binom(j-l,k-l), which equals zero
unless l=j, when it is one.

There is a coupled-tour interpretation of K_{n,k}: take two n-point
samples with their first k points shared and all remaining points mutually
independent. Their tour lengths are conditionally independent given the
shared points, with the same conditional mean. Their covariance is
therefore exactly K_{n,k}.

## 5. Independent checks of the constants

The bound 2/n in (7) has an order-statistic derivation that does not
integrate the nearest-distance tail. Fix x in Q and define

\[
 p_x(y)=\inf\{t\in[0,1]: y\in x+t(Q-x)\}.
\]

These homothetic squares are nested. For a uniform Y in Q,
P(p_x(Y) <= t) = t^2 for 0 <= t <= 1, because the square has area t^2.
Thus p_x(Y)^2 is uniform on [0,1]. For n-1 independent points the minimum
of these squared gauges has mean 1/n. One way to compute this mean is
that the n spacings made by n-1 uniform order statistics, including the
two endpoint spacings, have equal means by permutation symmetry of their
constant joint density on the spacing simplex. Their sum is one. The
first spacing is the minimum, so its mean is 1/n.

Choose a sample point attaining the minimum gauge. Its squared Euclidean
distance from x is at most 2 times that gauge squared, by diam(Q)^2 = 2.
The nearest Euclidean point can only be closer, proving E[R^2] <= 2/n
again. The argument works when x is on the boundary; boundaries have area
zero in the gauge distribution.

The energy constant 8 can also be obtained without a replacement pair.
For a fixed base S_i, T(S_i) is a constant under conditioning on X_{-i}.
The mean minimizes mean squared error among constants, so

\[
 \operatorname{Var}(f_n\mid X_{-i})
 \le\mathbb E[(f_n-T(S_i))^2\mid X_{-i}]
 =\mathbb E[\delta(X_i;S_i)^2\mid X_{-i}].
\]

After taking expectation, (7)-(8) bound this by 8/n. Summing (13)
over i gives sum_j j V_{n,j} <= n(8/n) = 8 independently of the
factor 1/2 in (12).

Finally, the factor 2 in the insertion bound has a direct closed-walk
check. At a nearest base point y, append the detour y,x,y to an optimal
base tour. Its added length is 2|x-y|. Shortcut repeated vertices using
the triangle inequality to obtain a tour of no greater length. A singleton
base attains this added cost exactly, so this universal factor cannot be
reduced using insertion alone.

## 6. What the reduction leaves open

Neither convergence of V_{n,j} for any fixed j nor convergence of
C_n(rho) for a fixed rho in (0,1) is proved here. Bounds (3), (17), and
(18) alone do not imply convergence of the variance. They show that
arbitrarily high interaction orders and passage from fixed noise to zero
noise cause no additional obstruction once the corresponding fixed-order
or fixed-noise limits have been established.

The sufficiency of fixed-order convergence is not claimed to be necessary:
total variance can converge while its mass moves between two fixed orders.
Likewise, the first-moment bound on the interaction order gives compactness,
not uniqueness of a limiting spectrum.

No localization of the optimal tour is used. An add-one cost can be bounded
by a nearby detour even if finding the optimum changes edges far away.
Local convergence of the input point process therefore cannot, by itself,
be substituted for the missing convergence hypotheses.

The conjecture addressed here is Section 3, problem (2), of Sourav
Chatterjee, *A general method for lower bounds on fluctuations of random
variables*, arXiv:1706.04290,
https://arxiv.org/html/1706.04290v3. The product-space decomposition and
resampling identities above are derived explicitly; their use here makes
no claim of novelty for those general tools.
