# Scalar attention with two trained factors per layer

## Statement

Fix integers n>=1 and L>=1. Let x_1,...,x_n,x_q,w be independent
standard normal real variables and y_j=w x_j. Set

    Z_0 = [[x_1,...,x_n,x_q],[y_1,...,y_n,0]],
    M=diag(1,...,1,0),  P=diag(0,1),
    K_i=diag(k_i,0),  Q_i=diag(q_i,0).

Use L untied linear-attention layers

    Z_i = Z_(i-1)
          - P Z_(i-1) M (K_i Z_(i-1))^T (Q_i Z_(i-1))/n.       (1)

Predict minus the bottom-right entry of Z_L. Train all 2L scalars
theta=(k_1,q_1,...,k_L,q_L) by Euclidean population gradient flow on
the squared prediction error f(theta), without a factor 1/2. The other
matrix entries, the value map P, and the mask M are fixed.

Every initial theta has a bounded global forward trajectory that
converges to one critical point. Every nonglobal critical point of f
has a strictly negative Hessian eigenvalue. Outside a set of Lebesgue
measure zero in R^(2L), the trajectory converges to a global minimizer.
Consequently convergence to a global minimizer holds almost surely for
every joint initialization law with a density, including independent
Gaussian initialization of these 2L factors.

Put alpha=n/2 and (z)_j=product_(h=0)^(j-1)(z+h), with (z)_0=1.
The limiting products a_i=k_i q_i are a permutation of the reciprocals
of the L distinct positive roots of

    r_*(s)=sum_(j=0)^L (-1)^j binom(L,j) alpha^j s^j/(alpha+1)_j. (2)

The resulting predictor implements L gradient steps from zero on the
empirical scalar least-squares loss. Its exact population prediction risk is

    f_* = L!/(alpha+1)_L
        = 2^L L! / product_(j=1)^L(n+2j).                       (3)

At fixed L this is asymptotic to 2^L L!/n^L. The noiseless scalar Bayes
risk is zero, so (3) is also the excess Bayes risk. Training is completed
at each finite n before taking n to infinity.

The result extends the direct-step parametrization of round 4 to two
trained scalar key/query factors per step. It does not train all entries
of the key/query matrices or the value matrices, and does not address
d>1, softmax, or discrete or stochastic training. The initialization
conclusion requires absolute continuity, not merely an atomless law.

## 1. Forward pass

Let a_i=k_i q_i and S=n^(-1) sum_j x_j^2. The matrix product K_i^T Q_i
is diag(a_i,0), so (1) is exactly the earlier direct-step architecture
with a_i in place of its trainable entry. For completeness, the top row
never changes because the first row of P is zero. If the bottom
training entries are (w-v)x_j and its query entry is -v x_q, then the
subtracted bottom attention entry in column j is a_i S(w-v)x_j,
including the query column. The mask excludes the query from S.
The new bottom row has the same form with

    v_new=v+a_i S(w-v).

This induction starts with v=0. If

    ell(v)=(2n)^(-1) sum_j(v x_j-y_j)^2,

then ell'(v)=S(v-w); hence each layer performs v_new=v-a_i ell'(v).
The residual after L layers is w product_i(1-a_i S). Integrating out
the independent w,x_q, whose second moments are one, gives

    f(theta)=F(a),   F(a)=E[r_a(S)^2],
    r_a(s)=product_(i=1)^L(1-a_i s).                            (4)

S has a density positive on (0,infinity), proportional to
s^(alpha-1) exp(-alpha s). Its moments are

    m_j=E[S^j]=(alpha)_j/alpha^j.                               (5)

These follow by differentiating the Gaussian moment generating function
E exp(tS)=(1-t/alpha)^(-alpha). In particular every expectation below
is a finite polynomial in its parameters.

## 2. Coercivity and the product-space landscape

Write r_c(s)=1+sum_(j=1)^L c_j s^j and

    G(c)=E[r_c(S)^2]=1+2b^T c+c^T Hc,
    b_j=m_j,  H_ij=m_(i+j),  1<=i,j<=L.

For nonzero u, u^T Hu=E[(sum_j u_j S^j)^2]>0: a nonzero polynomial
has only finitely many roots and S has positive density. Thus H is
positive definite. The unique minimizer is c_*=-H^(-1)b and

    G(c)-G(c_*)=(c-c_*)^T H(c-c_*).                             (6)

The normal equations are E[S^j r_(c_*)(S)]=0 for 1<=j<=L.
The coefficients of r_a are c_j(a)=(-1)^j e_j(a), so F=G composed
with c. A sublevel of F bounds all c_j by (6). The monic polynomial

    product_i(z-a_i)=z^L+c_1 z^(L-1)+...+c_L

then bounds all a_i. Indeed, if C=max_j|c_j| and |z|>1+C,

    |sum_j c_j z^(L-j)|
       <= C sum_(j=1)^L |z|^(L-j)
       < C |z|^L/(|z|-1) < |z|^L,

so z cannot be a root. Every F sublevel is closed and bounded, hence
compact. This coercivity statement concerns products a, not factors theta.

When the a_i are distinct, the coefficient Jacobian J(a) is invertible.
If J(a)u=0, differentiating product_i(z-a_i) in direction u gives

    -sum_i u_i product_(h!=i)(z-a_h)=0

as a polynomial. At z=a_i this gives
u_i product_(h!=i)(a_i-a_h)=0, so every u_i=0. This includes a zero
coordinate, since there was no division by a_i. Thus a critical point
of F with distinct coordinates satisfies grad G=0.

For a repeated pair a_i=a_j=c, set
R(s)=product_(h!=i,j)(1-a_h s). Splitting the pair gives the exact identity

    F(a+t(e_i-e_j))
       =F(a)-2t^2 A+t^4 B,
    A=E[S^2(1-cS)^2 R(S)^2]>0,
    B=E[S^4 R(S)^2]>0.                                        (7)

Both inequalities follow from the positive density and nonzero
polynomials with constant term one before multiplication by powers of S.
In particular

    (e_i-e_j)^T Hess F(a)(e_i-e_j)=-4A<0.                      (8)

Sections 3 and 4 will show that c_* is attainable with distinct real
steps. It then follows that every critical point of F is either global
or has a repeated pair and the negative direction (8).

## 3. Optimal polynomial and positive simple roots

For r_* defined in (2), equations (5) give, for 1<=j<=L,

    E[S^j r_*(S)]
      = (alpha)_j/alpha^j
        sum_(h=0)^L (-1)^h binom(L,h) (alpha+j)_h/(alpha+1)_h.

The ratio in this sum equals

    (alpha+1+h)_(j-1)/(alpha+1)_(j-1),

a polynomial in h of degree j-1<L. Its Lth finite difference vanishes,
and the alternating binomial sum is that difference up to sign. This
verifies every normal equation. Since r_*(0)=1 and G is strictly convex,
r_* is its unique minimizing polynomial. Its degree is exactly L.

Let t_1,...,t_m be its distinct sign-changing roots on (0,infinity).
If m<L, put p(s)=product_(j=1)^m(s-t_j), with p=1 if m=0. The product
r_*(s)p(s) has one sign on (0,infinity) except for finitely many zeros:
at each sign-changing root both factors change sign. Therefore

    E[S r_*(S)p(S)] != 0.

But deg p=m<=L-1, so the normal equations say this expectation is zero.
This contradiction shows m>=L. Degree L then forces exactly L distinct
positive roots rho_1,...,rho_L, all simple, with

    r_*(s)=product_i(1-s/rho_i).

Thus the product-space minima are exactly permutations of a_i*=1/rho_i.
They lift to factor-space minima, for example by k_i=a_i*, q_i=1.
There are no other factor-space minima with a smaller value because
f=F composed with the product map.

## 4. Risk

Orthogonality of r_* to s,...,s^L gives
E[r_*^2]=E[r_*], because r_*-1 is in their span. Also
(alpha)_j/(alpha+1)_j=alpha/(alpha+j), including j=0. Hence

    f_*=sum_(j=0)^L (-1)^j binom(L,j) alpha/(alpha+j)
       =alpha integral_0^1 t^(alpha-1)(1-t)^L dt.

Integration by parts removes the power L one at a time. Its boundary
terms vanish since alpha>0. The result is

    f_*=[L/(alpha+1)][(L-1)/(alpha+2)]...[1/(alpha+L)],

which proves (3). A separate expression is f_*=1-b^T H^(-1)b, obtained
by substituting c_* in G. The audit solves that rational linear system
and integrates the squared polynomial without using (2).

For n=2, alpha=1 and (3) is 1/(L+1). For L=1 the optimal step is
n/(n+2) and risk 2/(n+2). For L=2 the two steps are
n/(n+2)[1 +/- sqrt(2/(n+4))] and risk 8/[(n+2)(n+4)]. At L=3 the
risk is 48/[(n+2)(n+4)(n+6)]. These check both normalization and scale.

Since x_1!=0 almost surely, w=y_1/x_1 is determined by any noiseless
scalar prompt of length n>=1. Its Bayes prediction risk is zero.
This is the zero-noise Gaussian ridge limit. At fixed L, multiplying
(3) by n^L and taking n to infinity gives 2^L L!.

## 5. Factor gradient flow is bounded and forward complete

Put g_i=partial_i F(a) and h_i=k_i^2+q_i^2. The chain rule gives

    k_i'=-q_i g_i,  q_i'=-k_i g_i,
    a_i'=-h_i g_i,
    f'=-sum_i h_i g_i^2=-||grad f||^2<=0.                      (9)

Moreover

    D_i=k_i^2-q_i^2

is conserved, since its derivative is -2k_i q_i g_i+2q_i k_i g_i=0.
The algebraic identity

    h_i^2=D_i^2+4a_i^2                                         (10)

now bounds the factors. In detail, (9) keeps the product vector in the
compact F sublevel from Section 2, so |a_i|<=A for some A. Equations
(10) and h_i>=0 give

    k_i^2+q_i^2 <= sqrt(D_i(0)^2+4A^2).

This holds for all initializations, including D_i=0 and double-zero pairs.
An independent bound is k_i^2<=|D_i|+|a_i| and
q_i^2<=|D_i|+|a_i|: if k_i^2>=q_i^2, then q_i^2<=|k_i q_i| and
k_i^2=q_i^2+D_i; reverse the roles otherwise.

The vector field in (9) is polynomial, hence locally Lipschitz. The
trajectory stays in a fixed compact subset of factor space. The field
is bounded on a neighborhood of that subset. If a maximal forward
existence time were finite, the bounded field would give a time-Lipschitz
trajectory and a limit at that endpoint. Local existence at the limit
would extend it, a contradiction. Thus the solution is defined for all
t>=0, and its closure is compact.

Factor-space sublevels alone are not compact: fixing a nonzero product
allows k to diverge and q to approach zero. It is the conserved D_i,
not a claimed coercivity of f, that proves boundedness.

## 6. Every nonglobal factor critical point is a strict saddle

There are two cases, and both are needed.

First suppose some pair is double zero, k_i=q_i=0. Then a_i=0. With
R_i(s)=product_(j!=i)(1-a_j s), differentiation of (4) gives

    g_i=-2E[S R_i(S)^2]<0.                                    (11)

Strict negativity follows because R_i has constant term one and is
not the zero polynomial. In the two coordinates (k_i,q_i), at their
double zero the factor Hessian has block

    [[0,g_i],[g_i,0]].

Its quadratic form on (1,1) is 2g_i<0. Equivalently, changing just
this pair to (t,t) changes a_i to t^2 and gives

    f(theta+t(e_(k_i)+e_(q_i)))
      = f(theta)-2t^2 E[S R_i^2]+t^4 E[S^2 R_i^2].              (12)

Its second derivative is -4E[S R_i^2]<0, checking the block and sign
independently. This applies at any point with a double-zero pair,
and in particular at a critical point, even when other g_j do not vanish.

Now suppose every pair (k_i,q_i) is nonzero as a vector. The derivative
B=Dpi(theta) of pi(theta)=(k_i q_i)_i has row i equal to (q_i,k_i)
in pair i and zero elsewhere. These nonzero rows have disjoint supports,
so B has full row rank. Since grad f=B^T grad F, criticality of theta
implies grad F=0. If the a_i are distinct, Section 2 and Section 3 imply
global optimality. Otherwise select a repeated pair and let v=e_i-e_j.
There is a factor direction u with Bu=v; one explicit choice in each
pair is

    u_(k_h)=q_h v_h/h_h,  u_(q_h)=k_h v_h/h_h.

At the critical point grad F=0, the Hessian chain rule is

    Hess f=B^T (Hess F)B.

The usually present term sum_h g_h Hess pi_h vanishes precisely because
all g_h=0. It follows from (8) that

    u^T Hess f u=v^T Hess F v=-4A<0.

One can also choose u by varying only one nonzero multiplier per pair:
if q_h!=0 set u_(k_h)=v_h/q_h, u_(q_h)=0; otherwise set
u_(k_h)=0, u_(q_h)=v_h/k_h. Along this straight factor path,
pi(theta+tu)=a+tv exactly, so (7) checks the curvature without a
Hessian chain rule. Every real symmetric matrix whose quadratic form
is negative on some vector has a negative eigenvalue. This establishes
the claimed alternative throughout R^(2L).

## 7. Convergence to a single critical point

Two standard local theorems are used here and in Section 8. Their use
does not require a global Lipschitz bound on the polynomial Hessian.

The first is the analytic gradient inequality: for an analytic function
f and a critical point p, there are a neighborhood U, C>0, and
beta in (0,1) such that

    |f(theta)-f(p)|^beta <= C||grad f(theta)||,  theta in U.     (13)

It is stated in [2], equation (0.2). Here f is a finite polynomial by
(4)-(5), so it is analytic on all of R^(2L).

For clarity, the consequence of (13) needed here can be derived as
follows. Boundedness and (9) give a limit ell of f(theta(t)) and a finite
integral of ||grad f||^2 over [0,infinity). The derivative of
z(t)=||grad f(theta(t))||^2 is

    z'=-2 grad f^T (Hess f) grad f.

It is bounded on the compact trajectory closure. Thus z is uniformly
continuous and tends to zero: otherwise infinitely many disjoint
intervals of a fixed positive length with z bounded below would
contradict integrability. Every cluster point p is therefore critical,
and f(p)=ell by continuity.

Fix one such p and a closed ball about p inside U with radius r>0.
If f(theta(t))=ell at a finite time, monotonicity and its limiting value
force f to remain constant thereafter. Equation (9) makes that tail
stationary. Otherwise put e(t)=f(theta(t))-ell>0. While theta(t) is
inside the ball, (13) and (9) give

    -d/dt e^(1-beta)
       =(1-beta)e^(-beta)||grad f||^2
       >=(1-beta)||grad f||/C.                                (14)

Since p is a cluster point and e(t)->0, choose a sufficiently late T
with ||theta(T)-p||<r/4 and C e(T)^(1-beta)/(1-beta)<r/4.
Integrating (14) until a possible first exit bounds the traveled length
by r/4. An exit would require length greater than 3r/4, a contradiction.
Thus the trajectory never exits and has finite tail length by (14).
It is Cauchy and converges. Since p was a cluster point, its limit is p.
This proves single-point convergence for every initialization, even
though the critical set can have continua.

## 8. The attraction set of all strict saddles has measure zero

The second standard theorem is the local center-stable manifold theorem
for a C^1 local diffeomorphism at a fixed point: the points whose forward
iterates remain in a sufficiently small neighborhood lie in a C^1
manifold tangent to the eigenspaces with eigenvalue modulus at most one.
The continuous-time use of this theorem, with no countability assumption
on the equilibrium set, is given in [3], Appendix A, Theorem 3 and
Corollary 3. Here is the localization and countable-cover argument.

Let p be a strict saddle of f. Choose a smooth cutoff of -grad f which
equals it near p and vanishes outside a compact set. Its flow is complete
for positive and negative time. Its time-one map T is a C^1
diffeomorphism, fixes p, and

    DT(p)=exp(-Hess f(p)).

A negative eigenvalue of Hess f(p) gives an eigenvalue of DT(p) greater
than one. The center-stable theorem therefore gives a neighborhood V_p
and a local C^1 manifold W_p of dimension at most 2L-1 which contains
every point whose cutoff-flow integer iterates stay in V_p. Shrink V_p
to lie inside the region where the original and cutoff vector fields
agree. A trajectory of the original field which remains continuously
in V_p for all future time is also a trajectory of the cutoff field
there. Its integer iterates stay in V_p, so its initial point lies in
W_p. A C^1 submanifold of positive codimension has Lebesgue measure zero:
locally it is a C^1 graph, and a countable coordinate cover reduces this
to the zero measure of a graph in a higher-dimensional space.

The open sets V_p cover the strict-saddle set S. Since Euclidean space
is second countable, this cover of S has a countable subcover
V_(p_1),V_(p_2),.... If a trajectory converges to some p in S, choose
j with p in V_(p_j). Convergence and openness imply that after some
integer m>=0 the entire continuous tail stays in V_(p_j). Consequently

    theta(m) in W_(p_j).

Let Phi_m be the original time-m map. It exists on all R^(2L) by Section 5.
It is C^1, and its derivative is invertible at every point. Indeed, along
any trajectory its variational matrix U solves

    U'=-Hess f(theta(t))U,  U(0)=I,
    det U(m)=exp(-integral_0^m trace(Hess f(theta(t)))dt)>0.

The integral is finite on each bounded finite trajectory segment. The
inverse function theorem makes Phi_m a local C^1 diffeomorphism.
Its local inverses are locally Lipschitz after restricting to smaller
coordinate balls. Such maps send null sets to null sets; covering the
domain by countably many such charts shows that the preimage
Phi_m^(-1)(W_(p_j)) has measure zero. No global backward completeness
of the original polynomial field is being asserted.

The initial points converging to S are contained in

    union_(j>=1) union_(m>=0) Phi_m^(-1)(W_(p_j)),

a countable union of null sets. Hence this whole attraction set is null.
Section 7 gives a critical-point limit for every initialization, and
Section 6 says every nonglobal critical point belongs to S. All other
initializations therefore converge to a global minimum. Absolute
continuity of the initialization law gives the claimed probability-one
conclusion.

## 9. Limits of the factors and exceptional initializations

At a successful limit each product a_i*>0 is one of the steps in
Section 3. The invariant D_i and (10) identify the factor magnitudes:

    (k_i*)^2=(sqrt(D_i^2+4(a_i*)^2)+D_i)/2,
    (q_i*)^2=(sqrt(D_i^2+4(a_i*)^2)-D_i)/2.                      (15)

Both are strictly positive, and the factors have the same sign because
their product is positive. The layer permutation need not preserve the
ordering of initial products. From (9), unequal h_i destroy the earlier
pair-gap identity. For example, at n=2,L=2, take
(k_1,q_1)=(1,1), (k_2,q_2)=(2,1/2). Both products are 1, but the
common product gradient is 22 while h_1=2, h_2=17/4. Thus
(a_1-a_2)'=(17/4-2)22=99/2, not zero.

Exceptional initializations really exist. At one layer, take k=-q!=0.
The sum k+q remains zero because (k+q)'=-(k+q)g. Then a=-k^2<=0,
g=-2(1-m_2 a)=-2(1+m_2 k^2), and

    k'=-2k(1+m_2 k^2).

Hence k and q tend to zero and the risk tends to F(0)=1, whereas the
global risk is 2/(n+2)<1. At any depth, a layer initialized with k_i=-q_i
remains on that hyperplane and has nonpositive product, incompatible
with every global minimum. Such hyperplanes are null under a joint
density. This also shows why a distribution supported on a lower
dimensional set, even if atomless, is not covered by the theorem.

The proof gives no uniform time bound in n,L, factor imbalances, or
distance from saddle attraction sets. It identifies the algorithm and
the limiting risk only in the stated scalar, fixed-block, population-flow
setting. It does not prove the unrestricted T325 conjecture.

## References

[1] Khashayar Gatmiry, Nikunj Saunshi, Sashank J. Reddi, Stefanie Jegelka,
Sanjiv Kumar, *Can Looped Transformers Learn to Implement Multi-step
Gradient Descent for In-context Learning?*, ICML 2024,
[arXiv:2410.08292v1](https://arxiv.org/html/2410.08292v1), Section 3 and
Appendix A.1. This supplies the fixed-block linear-attention architecture.

[2] Tobias Holck Colding, William P. Minicozzi II, *Lojasiewicz inequalities
and applications*, [arXiv:1402.5087v3](https://arxiv.org/pdf/1402.5087),
equation (0.2). Only the finite-dimensional analytic gradient inequality
is used.

[3] Arthur Castello B. de Oliveira, Milad Siami, Eduardo D. Sontag,
*Convergence analysis of gradient flow for overparameterized LQR
formulations*, Automatica 182 (2025), 112504,
[full text](https://sontaglab.org/FTPDIR/2025_automatica_olivera_siami_sontag_overparametrized_lqr_reprint.pdf),
Appendix A, Theorem 3 and Corollaries 3–4. Only its general local-flow and
strict-saddle results are used, with the model-specific hypotheses
verified above; no LQR-specific result is applied.
