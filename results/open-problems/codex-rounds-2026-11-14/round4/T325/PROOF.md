# Untied scalar attention at arbitrary finite depth

## Theorem

Fix integers n>=1 and L>=1. Let x_1,...,x_n,x_q,w be independent
standard normal real random variables and y_i=w x_i. Set

    Z_0 = [[x_1,...,x_n,x_q], [y_1,...,y_n,0]],
    M = diag(1,...,1,0),  P = diag(0,1),
    Q_i = diag(a_i,0),  i=1,...,L,

and apply the untied linear-attention layers

    Z_i = Z_(i-1) - P Z_(i-1) M Z_(i-1)^T Q_i Z_(i-1)/n.       (1)

The prediction is minus the bottom-right entry of Z_L. Only the direct
scalar entries a_1,...,a_L are trainable. All other entries and P are
fixed; Q_i is not parametrized by separately trained key/query factors.
Let F(a) be the population squared prediction error, with no factor 1/2.

For Euclidean population gradient flow a'=-grad F(a), every pairwise
distinct initial vector has a global solution converging to the unique
global minimizer with the same coordinate ordering. In particular,
independent non-atomic random scalar initializations succeed almost
surely. The predictor implements L empirical least-squares gradient
steps from zero, with the learned step sizes given below.

Write alpha=n/2 and (z)_k=z(z+1)...(z+k-1), with (z)_0=1. Define

    r_*(s) = sum_(k=0)^L (-1)^k binom(L,k) alpha^k s^k/(alpha+1)_k. (2)

This polynomial has L distinct positive roots rho_1,...,rho_L. The
minimizing step-size vectors are exactly the permutations of

    (1/rho_1,...,1/rho_L).                                      (3)

The exact limiting prediction risk is

    F_* = L!/(alpha+1)_L
        = 2^L L! / product_(j=1)^L (n+2j).                      (4)

For each fixed L, n^L F_* tends to 2^L L!. The scalar noiseless Bayes
risk is zero, so this is also the exact excess Bayes risk. Every
stationary point other than these minima has repeated coordinates and
is a strict saddle. If an initialization has any repeated pair, its
trajectory cannot approach F_*.

## 1. Forward pass and population loss

Put S=n^(-1) sum_i x_i^2. At each layer the top row of Z remains
(x_1,...,x_n,x_q). Suppose the bottom training entries are (w-v)x_i
and the bottom query entry is -v x_q, as initially with v=0.
The bottom attention term for a layer of parameter a is

    a n^(-1) sum_i (w-v)x_i^2 x_j = a S(w-v)x_j

in every column j, including the query column. The mask excludes the
query from the sum. Subtracting the attention term preserves the stated
form, with

    v_new = v+a S(w-v).

For ell(v)=(2n)^(-1) sum_i (v x_i-y_i)^2 this is v_new=v-a ell'(v).
Consequently (1) performs L such gradient steps and

    w-v_L = w r_a(S),    r_a(s)=product_(i=1)^L (1-a_i s).

Independence and E[w^2]=E[x_q^2]=1 give

    F(a) = E[r_a(S)^2].                                        (5)

All formulas hold for arbitrary real step sizes, including zero and
negative values.

The density of S is a positive constant times
s^(alpha-1) exp(-alpha s) for s>0. Its moments are

    m_k=E[S^k]=(alpha)_k/alpha^k.                               (6)

For example, the Gaussian integral gives the moment generating function
(1-t/alpha)^(-alpha), and differentiation yields (6).

## 2. Strict convexity in coefficients and compact sublevel sets

For c=(c_1,...,c_L) define

    r_c(s)=1+sum_(k=1)^L c_k s^k,
    G(c)=E[r_c(S)^2]=1+2 b^T c+c^T H c,
    b_i=m_i,  H_ij=m_(i+j),   1<=i,j<=L.                        (7)

For u!=0,

    u^T H u=E[(sum_(i=1)^L u_i S^i)^2]>0,

because a nonzero polynomial cannot vanish on almost every positive
real number. Thus H is positive definite, and G has a unique minimizer
c_*=-H^(-1)b. Its normal equations are

    E[S^j r_(c_*)(S)]=0,  j=1,...,L.                            (8)

Writing lambda>0 for the smallest eigenvalue of H,

    G(c)-G(c_*)=(c-c_*)^T H(c-c_*) >= lambda ||c-c_*||^2.         (9)

For step sizes a let c(a) be the coefficient vector of r_a. Equivalently,
c_k(a)=(-1)^k e_k(a), where e_k is the kth elementary symmetric polynomial.
Then F=G composed with c. Every F sublevel bounds c by (9). Also

    h_a(z)=product_i(z-a_i)=z^L+c_1(a)z^(L-1)+...+c_L(a).

If C=max_k |c_k(a)|, every root of h_a satisfies |a_i|<=1+C.
Indeed, for |z|>1+C,

    |sum_(k=1)^L c_k z^(L-k)|
       <= C sum_(k=1)^L |z|^(L-k)
       < C |z|^L/(|z|-1) < |z|^L,

so h_a(z) cannot be zero. Thus every F sublevel bounds a. It is closed
by continuity, hence compact. This proves coercivity even when some
step sizes vanish.

## 3. The optimal polynomial and its roots

We verify (2) directly, rather than invoke an orthogonal-polynomial
theorem. For 1<=j<=L, (6) gives

    E[S^j r_*(S)]
      = (alpha)_j/alpha^j
        sum_(k=0)^L (-1)^k binom(L,k) (alpha+j)_k/(alpha+1)_k.    (10)

The ratio in the summand satisfies

    (alpha+j)_k/(alpha+1)_k
       = (alpha+1+k)_(j-1)/(alpha+1)_(j-1).

The right side is a polynomial in k of degree j-1<L. The alternating
binomial sum of any such polynomial is zero: one application of the
forward difference reduces its degree by one, and the Lth forward
difference at zero is, up to sign, exactly that sum. This proves (8).
Since r_*(0)=1 and H is positive definite, (2) is the unique coefficient
minimizer. Its leading coefficient is nonzero, so its degree is L.

To prove its roots are distinct and positive, let t_1,...,t_m be its
distinct sign-changing roots in (0,infinity). If m<L, set
q(s)=product_(i=1)^m(s-t_i), with q=1 when m=0. On (0,infinity),
r_*(s)q(s) has one constant sign except at its finitely many zeros:
both factors change sign at every t_i, and no other root of r_* changes
sign there. It is not identically zero. Therefore

    E[S r_*(S) q(S)] != 0.

But q has degree m<=L-1, so this expectation vanishes by (8), a
contradiction. Hence m>=L. A degree-L polynomial has at most L distinct
roots; all L roots are therefore positive and simple. Its constant term
one now gives

    r_*(s)=product_(i=1)^L (1-s/rho_i).

Thus c_* is attainable by real step sizes, exactly the permutations (3),
and the coefficient minimum is the parameter minimum.

The polynomial can also be named explicitly as
L_L^(alpha)(alpha s)/L_L^(alpha)(0), the normalized generalized Laguerre
polynomial, where the usual coefficient formula for L_L^(alpha) gives
(2). No assertion about its roots or norm is being imported from that
name.

## 4. Exact optimal risk, in two forms

Since r_*-1 is a linear combination of s,...,s^L, orthogonality gives

    E[r_*(S)^2]=E[r_*(S)].                                      (11)

Using (2) and (6), and (alpha)_k/(alpha+1)_k=alpha/(alpha+k),

    E[r_*(S)]
      = sum_(k=0)^L (-1)^k binom(L,k) alpha/(alpha+k)
      = alpha integral_0^1 t^(alpha-1)(1-t)^L dt.                (12)

The integral representation is valid for every alpha>0 and is only a
finite binomial expansion. Integration by parts gives, for L>=1,

    alpha integral_0^1 t^(alpha-1)(1-t)^L dt
      = L integral_0^1 t^alpha(1-t)^(L-1) dt.

There are no boundary terms: t^alpha tends to zero at zero, and
(1-t)^L tends to zero at one. Repeating with exponent alpha+1 yields

    alpha B(alpha,L+1)
      = [L/(alpha+1)] [ (L-1)/(alpha+2)] ... [1/(alpha+L)].       (13)

For L=0 the integral is one. This proves (4) without an asymptotic
approximation.

An independent coefficient-space expression is

    F_*=1-b^T H^(-1)b,                                         (14)

obtained by substituting c_*=-H^(-1)b in (7). The audit script solves
this rational linear system without using (2), then checks (4) and
(11) by direct polynomial multiplication.

## 5. The coefficient Jacobian and stationary points

Let J(a) be the L by L Jacobian of c(a). If the a_i are distinct, J is
invertible. To see this, suppose J(a)u=0. Differentiating h_a in the
direction u gives the zero polynomial

    -sum_(i=1)^L u_i product_(k!=i)(z-a_k)=0.

At z=a_j only the jth term survives, giving

    u_j product_(k!=j)(a_j-a_k)=0.

The product is nonzero, so every u_j=0. This proof also covers a zero
step size; no reciprocal coordinate is used for invertibility.

Since grad F=J^T grad G, every stationary point with distinct coordinates
has grad G=0 and is one of (3).

If a_i=a_j=c, put R(s)=product_(k!=i,j)(1-a_k s). Splitting this pair
into c+h,c-h gives the exact identity

    F(...,c+h,...,c-h,...)
      = F(a)-2h^2 E[S^2(1-cS)^2 R(S)^2]+h^4 E[S^4 R(S)^2].      (15)

The coefficient of -2h^2 is strictly positive, since
s(1-cs)R(s) is a nonzero polynomial and S has positive density.
Thus any stationary point with a repeated pair has a strictly negative
Hessian direction. Every nonglobal stationary point is a strict saddle,
and all local minima are global. This classification does not assume
there are finitely many repeated-coordinate stationary points.

## 6. Global existence and uniform separation of initially distinct steps

The vector field -grad F is polynomial, hence locally Lipschitz. Along
its local solution,

    dF/dt=-||grad F||^2<=0.                                    (16)

It stays in its compact initial sublevel set K. The field and its first
derivative are bounded on a neighborhood of K. If the maximal existence
time T were finite, the bounded field would make a(t) Lipschitz in time
on [0,T). It would have a limit in K as t increases to T, and the local
ODE theorem at that limit would extend the solution. This is a
contradiction, so the solution exists for every t>=0.

For i!=j and R as in Section 5, direct differentiation of (5) gives

    partial_i F-partial_j F
      = -2(a_i-a_j) E[S^2(1-a_i S)(1-a_j S)R(S)^2].

Consequently the difference delta_ij=a_i-a_j satisfies

    delta_ij' = delta_ij B_ij(a),
    B_ij(a)=2 E[S^2(1-a_i S)(1-a_j S)R(S)^2].                   (17)

The coefficient B_ij is a continuous polynomial in a. On K it is bounded,
so for every finite time

    delta_ij(t)=delta_ij(0) exp(integral_0^t B_ij(a(u)) du).      (18)

Thus signs are preserved and an initially zero gap stays zero.

A stronger fact prevents gaps from tending to zero as time increases.
Choose M>=1 so that K is contained in the box [-M,M]^L. On the compact
collision slice of this box, a_i=a_j=c, formula (17) becomes

    B_ij(a)=2 E[S^2(1-cS)^2 R(S)^2]>0.                          (19)

Every point has strict positivity for the same nonzero-polynomial reason
as in (15). Compactness and continuity give a positive minimum there.
There is therefore epsilon_ij>0 such that throughout the box,

    |a_i-a_j|<=epsilon_ij  implies  B_ij(a)>0.                  (20)

For rigor, if no such epsilon existed, a sequence in the compact box
with gaps tending to zero and B_ij<=0 would have a collision limit
contradicting (19). There are finitely many pairs; take a common
epsilon>0 for all of them. When L=1 there are no gaps to control.

For L>=2 there is also a direct bound verifying this sign.
Write a_i=c+delta/2, a_j=c-delta/2. Define

    K(c,R)=E[S^2(1-cS)^2 R(S)^2],   T(R)=E[S^4 R(S)^2].

Expanding the two factors in (17) gives exactly

    B_ij=2K(c,R)-(delta^2/2)T(R).                               (20a)

Let kappa be the smallest eigenvalue of the L by L matrix
W_jk=m_(j+k+2), indexed by 0<=j,k<=L-1. It is positive definite because
u^T W u=E[S^2(sum_j u_j S^j)^2]>0 for u!=0. The polynomial
(1-cs)R(s) has degree at most L-1 and constant term one, so its
coefficient vector has norm at least one; hence K(c,R)>=kappa>0.
For |a_k|<=M,

    T(R)<=U:=sum_(k=0)^(2L-4) binom(2L-4,k) M^k m_(k+4),

since |R(s)|<=(1+Ms)^(L-2) for s>=0. Therefore U>0 is finite,
and the explicit choice epsilon=sqrt(2kappa/U) implies B_ij>=kappa
whenever |delta|<=epsilon. This is a second derivation of (20), using
only a positive moment matrix and the midpoint expansion. For L=2 the
sum defining U is just m_4.

For an initially nonzero gap, (17)-(18) and (20) show that
g(t)=|delta_ij(t)| obeys g'(t)>0 whenever 0<g(t)<=epsilon. It follows that

    |delta_ij(t)| >= min(|delta_ij(0)|,epsilon)>0,  t>=0.        (21)

Indeed, on any interval where g<epsilon its derivative is positive, so
it cannot enter below epsilon from above or decrease below its initial
value when starting below epsilon. This proves a uniform positive
lower bound on each gap, dependent on n,L and the initial sublevel.

## 7. Convergence to the optimum

Assume all initial coordinates are distinct. For L>=2 let eta>0 be the
smallest lower bound in (21). The trajectory stays in the compact set

    K_eta={a in K: |a_i-a_j|>=eta for every i!=j}.

For L=1, set K_eta=K without imposing any gap condition.

At every point there J is invertible by Section 5. Continuity of the
smallest singular value on a compact set supplies sigma>0 such that

    ||J(a)^T v||>=sigma ||v||  for all a in K_eta and all v.    (22)

For L=1, J=-1 and sigma=1. By (7) and (9), for u=c(a)-c_*,

    ||grad G||^2=4u^T H^2u>=4lambda u^T H u=4lambda(F-F_*).

Together with (16) and (22), this yields

    (F-F_*)' <= -4sigma^2 lambda(F-F_*),
    F(a(t))-F_* <= (F(a(0))-F_*) exp(-4sigma^2 lambda t).         (23)

In particular (9) gives c(a(t))->c_*.

Every cluster point of a(t) is in K_eta and has coefficient vector c_*.
It is therefore one of the permutations (3). Formula (18) preserves
the strict coordinate ordering. Exactly one of these permutations has
that ordering, so all cluster points coincide. Compactness implies
convergence to this point: otherwise a sequence outside a fixed
neighborhood would have a different cluster point. This proves the
theorem without a stationary-point convergence theorem.

If a pair is initially equal, it stays equal by (18). Its closed
collision hyperplane intersects K in a compact set containing no global
minimizer, since all roots of r_* are simple. The minimum of F on that
intersection is strictly greater than F_*. Such a trajectory cannot
approach the optimal risk. Thus, for L>=2, pairwise distinctness is the
exact condition for convergence to the global risk in this model.

## 8. Checks, Bayes comparison, and scope

For L=1, (2)-(4) give a=n/(n+2) and risk 2/(n+2).
For L=2 the coefficient vector is

    c_1=-2n/(n+2),   c_2=n^2/[(n+2)(n+4)].

The step sizes are n/(n+2)[1 +/- sqrt(2/(n+4))], and the risk is
8/[(n+2)(n+4)], recovering the earlier two-layer theorem. For L=3,

    r_*(s)=1-3n s/(n+2)+3n^2 s^2/[(n+2)(n+4)]
             -n^3 s^3/[(n+2)(n+4)(n+6)],
    F_*=48/[(n+2)(n+4)(n+6)].

For any n>=1, x_1!=0 almost surely and w=y_1/x_1, so the posterior of
w given the noiseless scalar prompt is a point mass. The Bayes squared
prediction risk is zero, the zero-noise limit of Gaussian ridge
regression. For fixed finite L, (4) gives the stated asymptotic excess
risk. Training is completed for each finite n before taking this limit.

The theorem trains L direct scalar attention parameters from arbitrary
pairwise distinct values. It does not train all attention blocks,
factor the Q_i into trained keys and queries, treat d>1, or use softmax.
It concerns exact population gradient flow, not discrete or stochastic
training. The constants in (21)-(23) can deteriorate with n,L and near
colliding initializations; no uniform training-time bound is asserted.
The result does not prove the full T325 claim.

## Architectural reference

Khashayar Gatmiry, Nikunj Saunshi, Sashank J. Reddi, Stefanie Jegelka,
Sanjiv Kumar, *Can Looped Transformers Learn to Implement Multi-step
Gradient Descent for In-context Learning?*, ICML 2024,
[arXiv:2410.08292v1](https://arxiv.org/html/2410.08292v1), Section 3 and
Appendix A.1. This reference supplies the linear-attention architecture;
the scalar coefficient, separation, and convergence arguments above are
derived from (1).
