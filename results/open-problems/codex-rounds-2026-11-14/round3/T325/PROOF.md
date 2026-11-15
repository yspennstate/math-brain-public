# Two untied scalar attention layers

## Statement

Let n >= 1 be an integer. Let x_1,...,x_n,x_q,w be independent standard
normal real variables and y_i=w x_i. Form

    Z_0 = [[x_1,...,x_n,x_q], [y_1,...,y_n,0]],
    M = diag(1,...,1,0), P = diag(0,1), Q_a = diag(a,0).

Use two linear attention layers, with separate real parameters a,b:

    Z_1 = Z_0 - P Z_0 M Z_0^T Q_a Z_0 / n,
    Z_2 = Z_1 - P Z_1 M Z_1^T Q_b Z_1 / n.

The prediction is minus the bottom-right entry of Z_2. Only a,b are
trained; P and every other entry of Q_a,Q_b remain fixed. These are direct
Q parameters, not separately trained key and query factors. This is the
scalar, untied specialization of the attention architecture in Section 3
and Appendix A.1 of the reference below.

Let F_n(a,b) be the population squared prediction error. For the Euclidean
population gradient flow

    a' = -partial_a F_n, b' = -partial_b F_n,

every initial pair with a(0) != b(0) has a global solution converging to
one of the two ordered pairs (a_-,a_+), (a_+,a_-), where

    a_± = n/(n+2) [1 ± sqrt(2/(n+4))].                    (1)

The sign of a(0)-b(0) determines the ordering. In particular any joint
initialization law assigning probability zero to a=b, including
independent random variables with densities, converges almost surely to a
global minimizer. The limiting risk is exactly

    min F_n = 8/[(n+2)(n+4)].                           (2)

The forward pass implements two gradient-descent steps, with step sizes
a,b, on the empirical least-squares objective

    ell(v) = (1/(2n)) sum_i (v x_i-y_i)^2,

starting from v=0. Thus the learned algorithm is two-step gradient descent
with unequal, population-trained step sizes. At fixed n it is not exact
Bayes regression. Its risk tends to the Bayes risk zero as n tends to
infinity, with n^2 min F_n tending to 8.

## 1. Token update and loss

Write S=(1/n) sum_i x_i^2. At any layer suppose the training entries of
the label row are (w-v)x_i and its query entry is -v x_q. This holds
initially with v=0. The first row is unchanged by the update because P
has zero first row. For parameter c, the bottom entry of the attention
term in column j, including the query column, is

    c [sum_i (w-v)x_i^2] x_j / n = c S(w-v)x_j.

The mask excludes the query from the sum. Subtracting this term gives
training entries (w-v-cS(w-v))x_i and query entry
-(v+cS(w-v))x_q. Consequently the induction continues with

    v_new = v+c S(w-v) = v-c ell'(v).

After the two layers,

    w-v_2 = (1-aS)(1-bS)w.

Since w and x_q are independent of S and have second moment one,

    F_n(a,b) = E[(1-aS)^2(1-bS)^2].                    (3)

This calculation also checks the scalar specialization of the shared
model's loss: at a=b=c it is E[(1-cS)^4]. It makes no assumption that
a,b are positive.

## 2. Moments and exact optimum

The moment generating function of S is (1-2t/n)^(-n/2) near t=0:
the Gaussian integral gives E exp(t x_i^2/n)=(1-2t/n)^(-1/2), and
independence gives its nth power. Differentiating at zero yields

    m_k := E S^k = product_{j=0}^{k-1} [(n+2j)/n], m_0=1.

In particular

    m_1=1,
    m_2=(n+2)/n,
    m_3=(n+2)(n+4)/n^2,
    m_4=(n+2)(n+4)(n+6)/n^3.                           (4)

Set p=a+b, q=ab, and define

    G(p,q)=1-2p+m_2(p^2+2q)-2m_3 p q+m_4 q^2.

Equation (3) gives F_n(a,b)=G(a+b,ab). The quadratic part of G has matrix

    H = [[m_2,-m_3],[-m_3,m_4]].

It is positive definite: m_2>0 and

    D := m_2 m_4-m_3^2
       = 2(n+2)^2(n+4)/n^4 > 0.                      (5)

Equivalently its quadratic form is E[(-uS+vS^2)^2], strictly positive
for (u,v) != (0,0), because S has a density positive on (0,infinity).

The unique unconstrained minimizer of G solves

    m_2 p-m_3 q=1, -m_3 p+m_4 q=-m_2.

Cramer's rule and (4)-(5) give

    p_*=(m_4-m_2 m_3)/D = 2n/(n+2),
    q_*=(m_3-m_2^2)/D = n^2/[(n+2)(n+4)].             (6)

The discriminant is

    p_*^2-4q_* = 8n^2/[(n+2)^2(n+4)] > 0.            (7)

Therefore (p_*,q_*) is attained by real a,b, exactly the two orderings
of (1). Both step sizes are positive. Completing the square gives

    G(p,q)=G(p_*,q_*)+
       [(p-p_*),(q-q_*)] H [(p-p_*),(q-q_*)]^T.       (8)

At the optimum the two normal equations imply

    G(p_*,q_*)=1-p_*+m_2 q_*
              =1-2n/(n+2)+n/(n+4)
              =8/[(n+2)(n+4)],

proving (2) and uniqueness up to ordering.

## 3. All stationary points

The chain rule gives

    partial_a F_n = G_p+b G_q,
    partial_b F_n = G_p+a G_q.                        (9)

If a != b, stationarity implies G_q=0 and then G_p=0, hence exactly
the two minima in (1).

On a=b=c, either component of the gradient is

    -2g(c), g(c)=E[S(1-cS)^3].

The derivative of g is

    g'(c)=-3K(c), K(c)=E[S^2(1-cS)^2]>0.              (10)

Strict positivity follows because the quadratic polynomial inside the
expectation cannot vanish for almost every positive S. Thus g is
strictly decreasing. It is a cubic with leading coefficient -m_4<0,
so its limits as c tends to minus and plus infinity are plus and minus
infinity respectively. There is exactly one zero c_s, and c_s>0 because
g(0)=1. There are exactly three stationary points in all.

For completeness, the diagonal stationary point is a strict saddle.
Along the diagonal F_n(c,c)=E[(1-cS)^4], whose second derivative at c_s
is 12K(c_s). Along the direction (1,-1), the exact identity

    F_n(c+h,c-h)
      = E[((1-cS)^2-h^2 S^2)^2]
      = F_n(c,c)-2h^2 K(c)+h^4 m_4                  (11)

gives second derivative -4K(c_s). Symmetry makes the unit vectors
(1,1)/sqrt(2) and (1,-1)/sqrt(2) Hessian eigenvectors, with eigenvalues
6K(c_s) and -2K(c_s), respectively.

## 4. Global existence and convergence to a stationary point

The loss is coercive on R^2. Indeed, (8) bounds p,q on every sublevel
set, since H is positive definite. The identity

    a^2+b^2=p^2-2q

then bounds a,b there. Sublevel sets are also closed, hence compact.

The polynomial vector field -grad F_n is locally Lipschitz. Its local
solution satisfies

    dF_n/dt = -||grad F_n||^2 <= 0.                  (12)

It stays in the compact initial sublevel set. On a bounded neighborhood
of that set the vector field and its derivative are bounded, so the
local solution extends for all t>=0. Integrating (12), and using
F_n>=0, gives a finite integral of ||grad F_n||^2 over [0,infinity).

Here are details that this implies convergence to one of the three
stationary points. Put h(t)=||grad F_n(a(t),b(t))||^2. Its derivative is

    h'(t)=-2 grad F_n^T (Hess F_n) grad F_n,

which is bounded on the compact sublevel set. Hence h is uniformly
continuous. If h did not tend to zero, there would be epsilon>0 and
arbitrarily large times with h>=epsilon. The derivative bound would
give disjoint intervals of a fixed positive length on which
h>=epsilon/2, contradicting its finite integral. Thus h tends to zero.

Every cluster point is therefore stationary. More explicitly, fix
disjoint small open balls about the three stationary points. The compact
part of the sublevel set outside those balls has a positive minimum of
||grad F_n||, unless it is empty. For all sufficiently large times the
trajectory lies in their union. Continuity forces the whole remaining
trajectory to stay in one ball. Compactness supplies a cluster point
there, which must be its stationary center. All cluster points have to
be this center, because the closed ball contains no other stationary
point. A bounded trajectory with a unique cluster point converges to
that point: otherwise a sequence outside a fixed neighborhood of it
would have a different cluster point. This proves the claimed
stationary convergence without invoking an analytic-gradient theorem.

## 5. Excluding the saddle from all unequal initial pairs

Let delta=a-b. Subtracting the two flow equations in (9) gives exactly

    delta'=delta G_q(p,q),
    delta(t)=delta(0) exp(integral_0^t G_q(p(s),q(s)) ds). (13)

For each finite t the integral is finite, since the trajectory is
bounded. An initially nonzero delta remains nonzero with its original
sign.

At the diagonal stationary point,

    G_q(2c_s,c_s^2)
      =2(m_2-2c_s m_3+c_s^2 m_4)=2K(c_s)>0.          (14)

If an off-diagonal trajectory converged to this point, continuity would
give G_q>=K(c_s)>0 for every t after some T. Equation (13) would then
imply

    |delta(t)| >= |delta(T)| exp(K(c_s)(t-T)),

contradicting boundedness. Section 4 leaves only the two minima as
possible limits. Since their differences have opposite signs, (13)
also determines the ordering. This proves the convergence theorem.

The exceptional set is exact: if a(0)=b(0)=c(0), the diagonal remains
invariant and its flow is c'=2g(c). Strict decrease of g and its unique
zero imply monotone convergence to c_s (or a stationary solution if
initially there). In particular identical zero initialization fails to
reach the untied optimum. Independent continuous random initialization
avoids this entire line with probability one.

## 6. Bayes comparison and scope

With n>=1 in this scalar noiseless problem, x_1 != 0 almost surely and
w=y_1/x_1. The posterior distribution of w given the prompt is therefore
a point mass almost surely. The Bayes squared prediction risk is zero;
this is the zero-noise limit of the Gaussian ridge posterior mean.
Formula (2) is consequently the exact excess Bayes risk. It is positive
for each finite n and tends to zero with leading constant 8/n^2.

For a separate normalization check, one layer has risk
E[(1-aS)^2]=1-2a+m_2 a^2, minimized at a=n/(n+2) with risk
2/(n+2). The two-layer optimum is smaller by the factor 4/(n+4).
No factor 1/2 is included in the population loss; the 1/2 in ell only
fixes the forward-pass step-size convention.

The proof concerns population gradient flow in two direct scalar
parameters. It neither trains the fixed zero blocks nor factors Q into
independently trained key/query matrices. It proves no claim about
softmax attention, d>1, finite-task training, stochastic or discrete
gradient descent. Nor is the n=infinity loss substituted into training:
the proof is for each finite n, followed by a limit of its exact
converged risk. For S identically one the strict moment determinant and
the stationary classification would change.

## Reference

Khashayar Gatmiry, Nikunj Saunshi, Sashank J. Reddi, Stefanie Jegelka,
Sanjiv Kumar, *Can Looped Transformers Learn to Implement Multi-step
Gradient Descent for In-context Learning?*, ICML 2024,
[arXiv:2410.08292v1](https://arxiv.org/html/2410.08292v1).
The cited source supplies the attention architecture and shared/untied
residual recursions. The finite-n scalar landscape and convergence
argument above are derived directly from the stated updates.
