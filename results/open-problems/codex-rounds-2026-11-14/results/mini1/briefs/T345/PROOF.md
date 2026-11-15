# Euclidean robust learning of two spherical Gaussians

## Statement and scope

For a joint distribution P of (X,Y), with Y in {0,1}, put

\[
 R_{P,e}(f)=\Pr_P\{\exists z:\|z-X\|_2\le e,\ f(z)\ne Y\},
 \qquad R^*_{P,e}=\inf_{f\text{ Borel}}R_{P,e}(f).
\]

Closed adversarial balls are used. Projections of the Borel relations defining
these events are analytic, hence universally measurable; probabilities and
integrals below are taken in completed probability spaces.

**Theorem.** Let d>=2, let Y be balanced, and suppose

\[
 X\mid Y=y\sim N(\mu_y,\sigma_y^2 I_d),\quad
 1\le\sigma_y\le S,\quad \|\mu_1-\mu_0\|_2\le M.
\]

The means and the two scales are unknown. For e>0 and 0<eta,alpha<1,
there is a randomized learner returning a Borel classifier f such that, with
probability at least 1-alpha,

\[
 R_{P,e}(f)\le R^*_{P,e}+\eta.
\]

It uses O((d+1)/(alpha eta^2)) labelled observations **per class** and a
polynomial number of arithmetic operations and internally generated Gaussian
samples in d, S, M, 1/e, 1/eta, 1/alpha. Balanced iid labelled data supply the
class counts with polynomial overhead. The computation model is real
arithmetic with Gaussian sampling and exact distance comparisons. No claim
about optimal statistical rates or a complete bit-complexity analysis is made.

In particular, for polynomially bounded S, M, 1/e and inverse-polynomial eta,
this class has a polynomial-time additive-error robust learner. This does not
cover arbitrary covariance pairs or l_infinity attacks.

The proof has four parts. The exact reduction in Part 1 does not require bounded
parameters, balanced classes, or equal scales.

## 1. An exact two-dimensional reduction

Let c=(mu_0+mu_1)/2. When the means differ, let v be the unit vector in the
direction mu_1-mu_0; otherwise choose any unit vector v. Write

\[
 x=c+t v+w,\quad w\perp v,\qquad q(x)=(t,\|w\|_2).
\]

The quotient domain is H=R x [0,infinity), with its ordinary Euclidean metric.
Let Q be the joint law of (q(X),Y), and put a_y=<mu_y-c,v>.
Conditionally on Y=y, its two coordinates are independent, with

\[
 T\sim N(a_y,\sigma_y^2),\qquad R\sim\sigma_y\chi_{d-1}.                 \tag{1}
\]

For r>0 its density is

\[
 p_y(t,r)=\frac{e^{-(t-a_y)^2/(2\sigma_y^2)}}{\sqrt{2\pi}\sigma_y}
 \frac{r^{d-2}e^{-r^2/(2\sigma_y^2)}}
 {2^{(d-3)/2}\Gamma((d-1)/2)\sigma_y^{d-1}}.                            \tag{2}
\]

This follows by splitting the isotropic Gaussian into its component along v
and its independent (d-1)-dimensional perpendicular component, then taking
polar coordinates in the latter. The angular variable Theta is uniform on
the unit sphere in v-perpendicular and independent of (T,R,Y). For d=2 this
sphere has the two points {-1,+1}; the same argument applies.

The geometric identity needed is

\[
 q(B_e(x))=B_e(q(x))\cap H.                                           \tag{3}
\]

For one inclusion, if x=c+t v+w and z=c+s v+u, the reverse triangle inequality
gives

\[
 \|q(x)-q(z)\|_2^2=(t-s)^2+(\|w\|-\|u\|)^2
 \le(t-s)^2+\|w-u\|^2=\|x-z\|^2.
\]

Conversely, if (s,r') is in the right side of (3), choose u=r'w/||w|| when
w is nonzero. Then z=c+s v+u realizes equality in that inequality. If w=0,
choose any perpendicular unit direction for u. This proves (3), including
points on the axis and balls touching or crossing the axis.

For every Borel g:H->{0,1}, (3) gives the pointwise equality of robust losses,
and hence

\[
 R_{P,e}(g\circ q)=R_{Q,e}(g),\qquad R^*_{P,e}\le R^*_{Q,e}.             \tag{4}
\]

For the reverse inequality, take an arbitrary Borel f on R^d. For a fixed
perpendicular unit vector theta, define its meridian section

\[
 f_\theta(t,r)=f(c+t v+r\theta),\quad r\ge0.
\]

The map (t,r) -> c+t v+r theta is an isometry of H into R^d. Thus every
adversarial change in H is an allowed change for f in R^d, when the source
point lies in this meridian. Consequently

\[
 R_{P,e}(f)\ge\int R_{Q,e}(f_\theta)\,d\nu(\theta)
 \ge R^*_{Q,e},                                                       \tag{5}
\]

where the first integral uses the independence of Theta from (T,R,Y).
Taking the infimum over f proves the exact identity

\[
                         R^*_{P,e}=R^*_{Q,e}.                        \tag{6}
\]

This is an equality of infima and does not assume existence of an optimizer.
No averaging or majority vote of classifiers is used. For concentric Gaussians
the same proof, using rays instead of meridians, reduces further to the single
coordinate ||X-c||, whose conditional law is sigma_y chi_d.

## 2. A finite graph approximation with explicit radius slack

This part works for any joint law Q on the convex half-plane H.
Choose a rectangle K=[-B,B] x [0,B] with Q(K^c)<=tau. Partition it into
rectangles of side lengths at most h. Let z_1,...,z_N be their midpoints,
and C_1,...,C_N the disjoint cells, with arbitrary consistent boundary
assignments. Every point of C_i is within h of z_i. Define joint weights

\[
 w_{y,i}=\Pr_Q\{Y=y,\ Z\in C_i\}.
\]

Form a bipartite graph with one vertex (y,i) for each class and cell. Join
(0,i) and (1,j) whenever

\[
                       \|z_i-z_j\|_2\le2(e+h).                       \tag{7}
\]

Let I be any independent set, and let g_I label a point 1 exactly when it
belongs to a closed H-ball of radius e+h about a center z_i with (1,i) in I.
This is a Borel classifier, being a finite union of closed sets.

If (1,i) is selected, all sources in C_i of class 1 are robustly correct:
an e-perturbation is within e+h of z_i. If (0,j) is selected, an e-perturbation
of a point in C_j cannot be in any selected class-1 ball: otherwise the two
centers would have distance at most 2(e+h), contradicting independence.
Therefore

\[
                         R_{Q,e}(g_I)\le1-\sum_{(y,i)\in I}w_{y,i}.
\]

To compare the maximum independent-set weight W with the continuous optimum,
take any Borel g and select (y,i) if C_i contains at least one class-y source
point robustly correct for g at radius e+2h. The selected vertices are
independent. Indeed, if two opposite selected vertices satisfied (7), their
witness source points would have distance at most 2e+4h=2(e+2h). Their
midpoint lies in H and in both closed source balls, so g would have to assign
it both labels. This is impossible. The cells selected in this way contain all
robustly correct points of g in K. Thus

\[
 W\ge1-R_{Q,e+2h}(g)-\tau.
\]

Taking the infimum of the risks, even if unattained, gives

\[
                         W\ge1-R^*_{Q,e+2h}-\tau.
\]

Suppose estimated weights satisfy sum_{y,i}|hat w_{y,i}-w_{y,i}|<=delta.
If hat I maximizes estimated independent-set weight, applying this error
bound once to hat I and once to a true optimum gives

\[
 \sum_{(y,i)\in\hat I}w_{y,i}\ge W-2\delta.
\]

It follows that

\[
 R_{Q,e}(g_{\hat I})\le R^*_{Q,e+2h}+\tau+2\delta.                     \tag{8}
\]

Both the radius e+2h and the factor 2 in (7) are essential; no same-radius
claim has yet been made in (8).

Here is a polynomial implementation. Draw L iid labelled samples from Q and
use empirical weights. Including a tail category gives J=2N+1 categories.
For category probabilities p_j and empirical frequencies hat p_j,

\[
 E\sum_j|\hat p_j-p_j|
 \le\sum_j\sqrt{p_j(1-p_j)/L}\le\sqrt{J/L}.
\]

The last inequality follows from Cauchy–Schwarz and sum_j p_j(1-p_j)<=1.
Markov's inequality shows that L>=J/(beta^2 delta^2) suffices for the required
weight error with probability at least 1-beta.

For completeness, the graph optimization uses integer empirical counts.
Give arcs from the source to class-1 vertices and from class-0 vertices to
the sink their counts as capacities. Give each graph edge, directed from
class 1 to class 0, capacity L+1. A cut of capacity at most L exists, so a
minimum cut crosses no L+1 arc. Its source-side class-1 and sink-side class-0
vertices form an independent set, and the other vertices form a minimum
weight vertex cover. This is the desired maximum weight independent set.
An integral augmenting-path max-flow algorithm makes at most L augmentations:
each raises the flow by at least one and total flow is at most L. When no
augmenting path remains, the vertices reachable in the residual graph give
a cut of capacity equal to the flow. This proves optimality and gives a
polynomial algorithm in N and L.

## 3. Removing radius slack for spherical Gaussians

Work in centered coordinates c=0. Suppose the class means have norms at most
M_0 and the scales lie in [s,S_0], where s>0. Write P_a for the law of
(X/a,Y), for a=1+t and 0<=t<=1. A classifier f dilated to f_a(x)=f(x/a)
satisfies

\[
 R_{P,ae}(f_a)=R_{P_a,e}(f)\le R_{P,e}(f)+\operatorname{TV}(P_a,P).
\]

Taking infima and also using monotonicity in radius gives

\[
 0\le R^*_{P,ae}-R^*_{P,e}\le\operatorname{TV}(P_a,P).                 \tag{9}
\]

For one conditional Gaussian, integration of the logarithm of the two normal
densities gives

\[
 D_{KL}\bigl(N(\mu/a,\sigma^2 I/a^2)\|N(\mu,\sigma^2 I)\bigr)
 =\frac12\left[d(a^{-2}-1+2\log a)
       +\frac{\|\mu\|^2}{\sigma^2}(1-a^{-1})^2\right].                \tag{10}
\]

To check the scalar term, its derivative in t is
2(a^2-1)/a^3=2t(a+1)/a^3<=4t, so its value is at most 2t^2.
Also 1-a^{-1}=t/a<=t. Hence (10) is at most
t^2(d+M_0^2/(2s^2)). Pinsker's inequality yields

\[
 \operatorname{TV}(P_a,P)\le tK_0,\qquad K_0=\sqrt d+M_0/s.           \tag{11}
\]

For a common label prior, joint TV is the prior-weighted sum of conditional
TV distances; bounding each by tK_0 proves (11) for the mixture.
The elementary inequality used here is TV(A,B)<=sqrt(D_KL(A||B)/2).
One way to derive it is to apply the log-sum inequality to an event attaining
the positive density difference. For Bernoulli probabilities p,q the second
derivative of D_KL(Ber(p)||Ber(q)) in p is 1/[p(1-p)]>=4; its value and
first derivative at p=q vanish, so it is at least 2(p-q)^2.

Fix a requested population approximation parameter 0<gamma<1. Set

\[
 \tau=\gamma/8,\quad\delta=\gamma/8,\quad
 B=\sqrt{(M_0^2+dS_0^2)/\tau},\quad
 h=\frac{e\gamma}{16K_0}.                                            \tag{12}
\]

The quotient point (T,R) satisfies T^2+R^2=||X||^2 and
E||X||^2<=M_0^2+dS_0^2. Leaving [-B,B] x [0,B] implies ||X||>B,
so Markov's inequality gives the required tail bound tau.
The grid can be chosen with

\[
 N\le\lceil2B/h\rceil\lceil B/h\rceil.
\]

In (9), take a=1+2h/e; its t=gamma/(8K_0) is at most one. Equations
(6), (8), (9), and (11) now give, for the lifted classifier F,

\[
 R_{P,e}(F)\le R^*_{P,e}+\gamma/8+\gamma/8+2\gamma/8
            =R^*_{P,e}+\gamma/2.                                    \tag{13}
\]

All grid sizes, sample counts, and graph operations are polynomial in
d, M_0, S_0, 1/s, 1/e, 1/gamma, 1/beta. The samples in this part are
generated from the known Gaussian model; they are not additional observations
from an unknown distribution. A quotient sample can be generated by sampling
one axial normal and the norm of d-1 independent perpendicular normals.

## 4. Learning unknown means and scales

First note a distributional stability fact. For any two joint laws P,P',
any Borel f, and any e,

\[
 |R_{P,e}(f)-R_{P',e}(f)|\le\operatorname{TV}(P,P'),\qquad
 |R^*_{P,e}-R^*_{P',e}|\le\operatorname{TV}(P,P').                     \tag{14}
\]

The first bound is the TV bound for the fixed robust-error event, which does
not depend on the distribution. The second follows by taking infima in the
two resulting one-sided inequalities. Universal measurability does not change
the TV bound, by taking completions with respect to P+P'. Thus an optimizer
with excess rho for a fitted law within TV b has excess at most rho+2b for P.

Set b=eta/8. For each class use m fresh observations for the sample mean and
2l different observations for a variance estimate, where

\[
 m=\left\lceil\frac{8d}{\alpha b^2}\right\rceil,\qquad
 l=\left\lceil\frac{16}{\alpha b^2}\right\rceil.
\]

Define

\[
 \hat\mu_y=m^{-1}\sum_{i=1}^m X_i,\qquad
 D_j=(X'_j-X''_j)/\sqrt2,\qquad
 \hat\sigma_y^2=(ld)^{-1}\sum_{j=1}^l\|D_j\|^2.
\]

Each D_j is N(0,sigma_y^2 I), so

\[
 E\|\hat\mu_y-\mu_y\|^2=d\sigma_y^2/m,\qquad
 E(\hat\sigma_y^2/\sigma_y^2)=1,\quad
 \operatorname{Var}(\hat\sigma_y^2/\sigma_y^2)=2/(ld).
\]

Here E G^2=1 and E G^4=3 for a standard normal, giving variance 2 for each
squared normal, and independence gives the displayed variance.
Markov's inequality for the mean and Chebyshev's inequality for the scale
give failure probabilities at most alpha/8 for each of

\[
 \|\hat\mu_y-\mu_y\|\le b\sigma_y,\qquad
 |\hat\sigma_y^2/\sigma_y^2-1|\le b/\sqrt d.
\]

There are four events, so all hold with probability at least 1-alpha/2.
On this event put q_y=hat sigma_y^2/sigma_y^2; it lies in [1/2,3/2].
Another direct normal-density calculation gives

\[
 D_{KL}\bigl(N(\mu_y,\sigma_y^2I)\|
                 N(\hat\mu_y,\hat\sigma_y^2I)\bigr)
 =\frac12\left[d(q_y^{-1}-1+\log q_y)
       +\frac{\|\hat\mu_y-\mu_y\|^2}{q_y\sigma_y^2}\right].
\]

The derivative of q^{-1}-1+log q is (q-1)/q^2. Integrating from 1 and
using 1/q^2<=4 shows that this scalar expression is at most 2(q-1)^2
throughout [1/2,3/2]. Thus the displayed KL is at most 2b^2, and Pinsker
gives TV at most b for each conditional law. The joint fitted law hat P,
with the same balanced label prior, satisfies TV(P,hat P)<=b.

The fitted means are separated by at most M+2bS, and the fitted scales are
between 1/2 and 2S. After centering at their fitted midpoint, the known
parameter bounds M_0=M+S, s=1/2, S_0=2S are valid. Apply Part 3 to this
fitted model with gamma=eta and beta=alpha/2, constructing its own line of
means (any line if its means coincide). Equation (13) gives excess at most
eta/2 for hat P, except with conditional probability alpha/2. Equation (14)
then gives

\[
 R_{P,e}(F)\le R^*_{P,e}+\eta/2+2b
            =R^*_{P,e}+3\eta/4\le R^*_{P,e}+\eta.
\]

The two failure probabilities sum to alpha. The real observations used per
class are m+2l=O((d+1)/(alpha eta^2)); subsequent draws are from the fitted
model. No separation between the true means is required: the fitted line
may have a very different direction, because (14) compares entire laws.
This completes the theorem.

## Limits

The exact quotient equality holds for arbitrary positive scales and any
Euclidean radius. The polynomial-time conclusion above is quantitative in
parameter magnitudes and 1/e, rather than their bit lengths. It supplies
additive approximation and does not match the best possible sample rate.
For e=0 one may instead use the fitted ordinary Gaussian likelihood-ratio
classifier and (14). General covariance pairs and l_infinity perturbations
remain outside the theorem.
