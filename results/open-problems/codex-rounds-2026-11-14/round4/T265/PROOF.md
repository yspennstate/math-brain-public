# Exact path norm of the conical interpolants

Let rho(t)=max(t,0). All networks below have the form

\[
 f(x)=\sum_{j=1}^m a_j\rho(w_j^T x),\qquad x\in\mathbb R^d,
\]

with real coefficients and no biases. Define the intrinsic path norm

\[
 \mathcal P(f)=\inf\left\{\sum_{j=1}^m |a_j|\|w_j\|_2:
       m<\infty,\ f=\sum_{j=1}^m a_j\rho(w_j^T\cdot)
       \text{ on all of }\mathbb R^d\right\}.
 \tag{1}
\]

The equality in this definition is equality of scores everywhere. This is
different from minimizing the norm subject only to sample constraints.
We first evaluate (1), then compare two scores satisfying the same sample
constraints. No assertion about a gradient-descent trajectory is made.

## 1. The exact formula

Suppose d>=2, v is in R^d, the u_k are unit vectors, and
u_k is not equal to either u_l or -u_l when k!=l. Let beta_k be nonzero
real numbers, k=1,...,K. Define

\[
 f(x)=v^T x+\sum_{k=1}^K\beta_k|u_k^T x|,
 \qquad
 Z=\left\{\sum_{k=1}^K t_k u_k: |t_k|\le |\beta_k|\right\}.
 \tag{2}
\]

Here Z is a compact convex set, the sum of the indicated line segments.
The empty sum is allowed: for K=0, Z={0}.

**Theorem 1.** The infimum in (1) is attained, and

\[
 \boxed{\mathcal P(f)=2\sum_{k=1}^K|\beta_k|
                   +2\operatorname{dist}_2(v,Z).}
 \tag{3}
\]

In particular, an even score with v=0 has
\(\mathcal P(f)=2\sum_k|\beta_k|\), and a linear score has
\(\mathcal P(v^T\cdot)=2\|v\|_2\).

### Hyperplane coefficients are forced

Take any finite representation in (1). Delete neurons with zero input
weight. Replace w_j by its unit direction and a_j by a_j||w_j||; this
leaves both its score and path cost unchanged. Group the resulting
neurons by their unoriented normal line. Choose one unit representative
u for each line. Let b^+ and b^- be the sums of the output coefficients
on directions u and -u. The group's contribution is

\[
 b^+\rho(u^Tx)+b^-\rho(-u^Tx)
   =\gamma |u^Tx|+t u^Tx,
 \quad \gamma=\frac{b^++b^-}{2},\quad
 t=\frac{b^+-b^-}{2}.
 \tag{4}
\]

Its original cost is at least

\[
 |b^+|+|b^-|=|\gamma+t|+|\gamma-t|
            =2\max\{|\gamma|,|t|\}.
 \tag{5}
\]

The last identity follows by considering |t|<=|gamma| and
|t|>=|gamma|; in each case the two summands either have the same sign
before taking absolute values, or opposite signs.

The coefficient gamma is determined by the function. Indeed, fix one
of the finitely many distinct hyperplanes H={x:u^Tx=0} in either
representation. There exists a point x_0 of H outside every other such
hyperplane. To see this, H has dimension d-1>=1, and its intersections
with the other hyperplanes are proper linear subspaces of H. Each has
Lebesgue measure zero inside H, so their finite union does not cover H.
In a small ball about x_0, all the other absolute-value terms are linear.
The one-sided gradients of gamma|u^Tx| differ, from u^Tx<0 to u^Tx>0,
by exactly 2 gamma u. Equality of the scores on that ball forces equality
of these gradient jumps. Thus gamma=beta_k on every listed hyperplane,
after matching its orientation, and gamma=0 on every additional
hyperplane. The coefficient beta is unchanged if u is replaced by -u.

Subtracting these forced even terms from the equality of the scores
also forces equality of the remaining linear vectors. If t_k are the
linear coefficients supplied by the listed groups, write

\[
 r=v-\sum_k t_k u_k
 \tag{6}
\]

for the vector supplied by all additional groups. Their gamma is zero;
their cost is at least twice the sum of the absolute values of their
linear coefficients, which is at least 2||r|| by the triangle inequality.
Consequently the cost of every representation is at least

\[
 2\sum_k\max\{|\beta_k|,|t_k|\}+2\|r\|.
 \tag{7}
\]

### Clipping yields the lower bound

Put t_k^0=max(-|beta_k|,min(t_k,|beta_k|)) and
e_k=(|t_k|-|beta_k|)_+. Then

\[
 z_0=\sum_k t_k^0 u_k\in Z,\quad
 \|v-z_0\|\le\|r\|+\sum_k e_k.
 \tag{8}
\]

This follows from (6), since |t_k-t_k^0|=e_k and ||u_k||=1.
The right side of (7) is therefore at least

\[
 2\sum_k|\beta_k|+2\operatorname{dist}_2(v,Z).
 \tag{9}
\]

This argument includes representations with extra hyperplanes and
arbitrary cancellations. It is not a restriction to the displayed
directions.

### A representation attaining the bound

Compactness of Z gives a nearest point z_* in Z. Choose coefficients
t_k with |t_k|<=|beta_k| and z_*=sum_k t_k u_k, and put r=v-z_*.
Use the two neurons

\[
 (\beta_k+t_k)\rho(u_k^Tx)
 +(\beta_k-t_k)\rho(-u_k^Tx)
 \tag{10}
\]

for each k. By (4), their sum is beta_k|u_k^Tx|+t_k u_k^Tx;
by (5), their cost is exactly 2|beta_k|. Add
rho(r^Tx)-rho(-r^Tx), of cost 2||r||, to represent the residual
linear score. The total score is f and the total cost is (3). Zero
coefficients may be removed. The width is at most 2K+2. This proves
the theorem, including attainment and K=0.

## 2. A second lower-bound certificate

The distance term has the formula

\[
 \operatorname{dist}_2(v,Z)
   =\max_{\|y\|\le1}
       \left(v^Ty-\sum_k|\beta_k||u_k^Ty|\right).
 \tag{11}
\]

For any such y and any z in Z, the expression is at most
(v-z)^Ty<=||v-z||, since max_{z in Z} z^Ty is precisely the sum
in (11). This proves one inequality. If v is in Z, y=0 attains zero.
Otherwise let z_* be its nearest point and take
y=(v-z_*)/||v-z_*||. For any z in Z, differentiating
||v-(z_*+t(z-z_*))||^2 at t=0+ gives
(v-z_*)^T(z-z_*)<=0; a negative derivative would contradict minimality.
Thus z_* maximizes z^Ty, so the expression in (11) equals
(v-z_*)^Ty=||v-z_*||. This proves (11).

One can therefore certify (3) with an explicit representation and a
supporting vector y. The audit additionally calculates distances to
two-dimensional polygon edges, independently of (11).

## 3. Application to the earlier paired cones

Fix a finite sample in dimension d>=2 for which
U_i=(X_i)_1 is nonzero and T_i=(X_i)_2/U_i are distinct. Fix any
linear baseline g(x)=v^Tx, and define

\[
 c_i=Y_i-v^TX_i,\qquad A_i=c_i/|U_i|,\qquad
 \Delta_i=\min_{j\ne i}|T_i-T_j|.
 \tag{12}
\]

For n=1 take Delta_1=infinity. Choose 0<h_i<=Delta_i/3 and let

\[
 H_{t,h}(x)=\frac{|x_2-(t-h)x_1|-2|x_2-tx_1|
                         +|x_2-(t+h)x_1|}{2h},
 \qquad B_h=\sum_i A_i H_{T_i,h_i},\quad f_h=g+B_h.
 \tag{13}
\]

For x_1!=0, H_{t,h}(x)=|x_1|(1-|x_2/x_1-t|/h)_+; for
x_1=0 it is zero. The open slope intervals are disjoint because
h_i+h_j<=2|T_i-T_j|/3. At X_i its own term equals |U_i| and
all others vanish. Thus f_h(X_i)=Y_i exactly, for every such choice
of widths.

Write q(t)=e_2-t e_1, L(t)=sqrt(1+t^2), and omit all i with A_i=0.
For each remaining i, the three absolute-value directions have

\[
 \begin{array}{c|c|c}
 r&u&\beta\\ \hline
 T_i-h_i&q(r)/L(r)& A_i L(r)/(2h_i)\\
 T_i&q(r)/L(r)&-A_i L(r)/h_i\\
 T_i+h_i&q(r)/L(r)& A_i L(r)/(2h_i).
 \end{array}
 \tag{14}
\]

All these unoriented directions are distinct: within a cone h_i>0;
between cones even the closed slope intervals are disjoint, since the
strict gap above remains. Hence Theorem 1 applies without merging.
Let Z_h be the set (2) from the table, and put

\[
 C(h)=\sum_{i:A_i\ne0}\frac{|A_i|}{h_i}
    [L(T_i-h_i)+2L(T_i)+L(T_i+h_i)].
 \tag{15}
\]

**Corollary 2.** The exact intrinsic norms are

\[
 \mathcal P(B_h)=C(h),\qquad
 \mathcal P(f_h)=C(h)+2\operatorname{dist}_2(v,Z_h).
 \tag{16}
\]

In particular, the earlier displayed correction cost is minimal over
every finite representation, even if neurons outside the coordinate
plane are allowed. The earlier displayed full-score cost C(h)+2||v||
is an upper bound and need not be minimal: paired neurons can supply
part of the baseline without further cost.

Since Z_h is contained in E=span{e_1,e_2} and contains zero, if
v=v_E+v_perp is the orthogonal decomposition then

\[
 C(h)+2\|v_{\perp}\|\le\mathcal P(f_h)
                     \le C(h)+2\|v\|.
 \tag{17}
\]

If at least two A_i are nonzero, their center vectors q(T_i) are
linearly independent. The corresponding center segments in Z_h are
{lambda q(T_i): |lambda|<=|A_i|/h_i}. Express the fixed vector v_E
as a linear combination of these two q's. As both widths tend to zero,
the two allowed coefficient bounds tend to infinity, so eventually
v_E belongs to Z_h. In that event the lower bound in (17) is attained.
In dimension two this gives \(\mathcal P(f_h)=C(h)\).

## 4. Comparison with a less localized interpolant

Fix positive widths b_i<=Delta_i/3 (take any finite b_1>0 for n=1).
They give an interpolant f_b with
\(\mathcal P(f_b)\le C(b)+2\|v\|\).
For epsilon>0 set h_i(epsilon)=min(epsilon,b_i), and let
S_A=sum_i |A_i|. If S_A>0, (15) and L(t)>=1 give

\[
 \mathcal P(f_{h(\epsilon)})\ge C(h(\epsilon))
                      \ge\frac{4S_A}{\epsilon}.
 \tag{18}
\]

**Corollary 3.** Whenever

\[
 0<\epsilon<\frac{4S_A}{C(b)+2\|v\|},
 \tag{19}
\]

the narrowed score has strictly greater intrinsic path norm than an
explicit interpolating score of width at most 6n+2. It therefore cannot
be a global minimum-path-norm exact interpolant. For binary labels it
also cannot globally minimize path norm subject to Y_i f(X_i)>=1,
because the competitor satisfies these constraints with equality.

The correction cost C(h) itself strictly decreases when any h_i with
A_i!=0 is increased, with the other widths fixed. To verify this, put
z=1/h and t=T_i. Its summand divided by |A_i| is

\[
 F_t(z)=\|(z,tz-1)\|+\|(z,tz+1)\|+2L(t)z,\qquad z>0.
 \tag{20}
\]

The first two terms extend to a convex even function of z. Every convex
even function is nondecreasing for z>=0: if 0<=x<=y, express x as a
convex combination of y and -y. The last term in (20) is strictly
increasing, so F_t is strictly increasing. This proves the claim.
The extra distance in (16) is not asserted to be monotone.

For the round 3 Gaussian mixture, the population bound for f_h versus
g is 2 C_s sum_i h_i, where C_s=1/pi+s/sqrt(2pi). Thus
h_i(epsilon)<=epsilon guarantees a bound 2 C_s n epsilon, while
(18) gives an intrinsic norm cost at least 4S_A/epsilon.
These are bounds for this family, not a converse tradeoff for every
possible localized interpolant. In particular, (19) is a fixed-sample
statement. It does not prove that the round 3 choice epsilon=n^(-3)
fails norm minimality with high probability for all n: the comparison
widths and C(b) depend on the random slope gaps.

### An explicit sample certificate

In dimension two take

\[
 X_1=(1,0),\quad X_2=(1,3),\quad Y_1=1,\quad Y_2=-1.
 \tag{21}
\]

The sample-mean baseline used in round 3 is
v=(Y_1 X_1+Y_2 X_2)/2=(0,-3/2). Hence
T_1=0, T_2=3, A_1=1, A_2=7/2. Its prescribed narrow widths are
h_1=h_2=min(2^(-3),3/3)=1/8. Equation (18) gives

\[
 \mathcal P(f_h)\ge 4(1+7/2)/(1/8)=144.
 \tag{22}
\]

Use b_1=b_2=1 for the competitor. Since L(t)<=1+|t| and
|t+-b|<=|t|+b, its summand in (15) is at most
4|A_i|(1+|T_i|+b_i)/b_i. Therefore

\[
 \mathcal P(f_b)\le C(b)+2\|v\|
      \le 4\cdot1\cdot2+4\cdot(7/2)\cdot5+3=81<144.
 \tag{23}
\]

Both scores interpolate (21) exactly and have width at most fourteen.
Thus the round 3 localization rule is not in general a global
minimum-path-norm interpolating rule. All inequalities are strict by a
large margin; by continuity of the slopes, residuals, minimum widths,
and displayed bounds, the same conclusion holds on an open neighborhood
of the inputs in (21), with these labels fixed. For every nondegenerate
Gaussian mixture in dimension two the joint input density is positive
everywhere. Each label has positive posterior probability at every
finite input, even with eta=0, because both Gaussian components have
positive density. This neighborhood and label assignment consequently
have positive probability. This is a positive-probability finite-sample
counterexample to norm minimality, not an asymptotic risk claim.

## 5. Relation to parameter norm and gradient descent

For a fixed neuron, positive homogeneity permits replacing
(a,w) by (a/lambda,lambda w), lambda>0. The infimum of
\((a^2/\lambda^2+\lambda^2\|w\|^2)/2\) is |a| ||w||,
attained when the two squared terms are equal, if both are nonzero.
Zero neurons can be deleted. Applying this separately to every neuron
shows that, over all finite representations,

\[
 \inf_{f=\sum_j a_j\rho(w_j^T\cdot)}
       \frac12\sum_j(a_j^2+\|w_j\|^2)=\mathcal P(f).
 \tag{24}
\]

The competitor in (23) can be balanced with at most fourteen neurons,
so the same strict comparison excludes the narrow score from global
minimum parameter norm under unit-margin constraints at any width
at least fourteen (pad with zero neurons if needed). The statement
uses trainable real weights in both layers.

Neither a global optimum of this margin problem nor a path-norm
minimizer has been shown to be the GD limit in the setting of T265.
The next section excludes stationarity of one displayed realization.
Stationarity of another realization of the same score, selection of
another localized interpolant, and benign overfitting remain unresolved.

## 6. Feasible descent for the displayed parameter realization

Use the six-neuron realization of each term in (13): for
r=T_i-h_i,T_i,T_i+h_i, let kappa=1,-2,1, respectively, and use
weights q(r), -q(r), both with output coefficient A_i kappa/(2h_i).
Add the two baseline neurons. Delete zero-output corrections and a
zero baseline. Balance every remaining neuron by the rescaling in
(24). Consider the parameter margin problem

\[
 \min_\theta J(\theta)=\frac12\|\theta\|^2,
 \qquad Y_i f_\theta(X_i)\ge1\quad\text{for all }i.
 \tag{25}
\]

**Proposition 4.** If at least one A_i is nonzero, this balanced
displayed realization is not a local minimum of (25). It does not
satisfy the generalized KKT stationarity equation, even if independent
ReLU derivatives in [0,1] are permitted at each zero preactivation.
This statement concerns this realization, not all representations of
its score.

Choose k with A_k!=0 and increase h_k slightly. The initial closed
slope intervals have strictly positive gaps. There is therefore a
positive neighborhood of h_k in which the intervals remain disjoint.
All scores at the training inputs stay equal to their labels, as in
(13). The baseline and the A_i stay fixed. Along this path, balance
the displayed neurons at each width; the balanced parameters are
differentiable functions of h_k because all retained coefficients are
nonzero and all q(r) have positive norm. Their parameter objective is

\[
 J(\theta(h_k))=2\|v\|+C(h).
 \tag{26}
\]

The derivative is strictly negative. In (20), the derivative of the
convex even first two terms is nonnegative for z>0, while that of the
last term is 2L(T_k)>0. The terms are differentiable for z>0 because
their vectors have nonzero first coordinate. The chain rule gives

\[
 \frac{d}{dh_k}J(\theta(h_k))
 \le-\frac{2|A_k|L(T_k)}{h_k^2}<0.
 \tag{27}
\]

This already rules out a local minimum. To verify the stationarity
claim, put p=theta'(h_k). For every sample and neuron, at a nonzero
preactivation use its usual ReLU derivative, and at zero allow any
xi_ij in [0,1]. The resulting possible score-gradient vector has
blocks

\[
 \zeta_{ij}=
    \bigl(\rho(w_j^TX_i),\ a_j\xi_{ij}X_i\bigr).
 \tag{28}
\]

All derivatives in this display refer to the balanced parameters.
Every zero preactivation has X_i^T p_{w_j}=0. For unchanged neurons
this is immediate. For the changed cone, its endpoint normals have
no zero preactivation on any sample: its own slope lies strictly
between its endpoints, and all other slopes lie outside its closed
interval. The center normal has a zero only on X_k. Its unbalanced
weight is fixed q(T_k) or -q(T_k), and balancing only rescales it,
so its weight derivative is parallel to q(T_k) and is orthogonal to
X_k. This proves the assertion in every case.

It follows that every allowed value in (28) has the same product with
p at zero preactivations. At nonzero preactivations the product is
the ordinary directional derivative. Since all sample scores are
constant along the path, for every permitted combined score gradient
zeta_i one has zeta_i^T p=0. If generalized KKT stationarity held,
it would require

\[
 \theta=\sum_i\lambda_i Y_i\zeta_i,\qquad\lambda_i\ge0.
 \tag{29}
\]

Taking the inner product with p would give theta^T p=0, contradicting
(27). The allowed derivatives in (28) include the usual Clarke
score subgradients, so excluding (29) also excludes that convention.
All constraints in (25) are active; complementarity cannot repair
the contradiction. This proves the proposition.

An unbalanced positive rescaling of the same displayed realization
also fails stationarity: scaling one neuron's w by exp(t) and a by
exp(-t) preserves all scores. Its objective derivative at zero is
||w||^2-a^2, nonzero when that neuron is unbalanced; reversing the
path makes it negative. At zero preactivations the weight derivative
is parallel to w, so the same subgradient argument applies. If every
neuron is balanced, Proposition 4 applies instead.

These are constraints on a specified finite parameterization. The
intrinsic norm formula allows other realizations, and no exclusion
of their KKT stationarity is proved here. In particular this proposition
does not establish which network is selected by GD, nor its risk.
