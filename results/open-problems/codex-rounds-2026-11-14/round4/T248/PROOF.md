# Spherical inputs with a strictly subcritical quadratic Hermite component

Let X have independent columns uniform on the sphere of radius sqrt(d), and
let W have independent real standard Gaussian entries, independently of X.
Suppose

    N/d -> alpha in (0,infinity),    m/N -> b in (0,infinity),    b != 1.

Let sigma be a fixed Lipschitz function, with orthonormal Gaussian Hermite
coefficients a_k, such that

    a_0=a_1=0,    v=E sigma(Z)^2>0,    q=a_2^2.

Assume the strict inequality

    q alpha sqrt(b) < v.                                      (1)

For Y_ij=sigma(w_i^T x_j/sqrt(d)), K=YY^T/N and b_N=m/N, the conclusion is

    [b_N^(1/6)/(v(1+sqrt(b_N))^(4/3))] N^(2/3)
      [lambda_max(K)-v(1+sqrt(b_N))^2] => TW_1.                 (2)

In particular lambda_max(K)->v(1+sqrt(b))^2 in probability. The center in
(2) uses the actual finite-dimensional aspect ratio. The case q=0 is
included, but the extension is q>0 subject to (1).

The external universality input is Corollary 1.4 of Guangchen Chen and
Xing Lyu, *Tracy–Widom law for sample covariance matrices under quadratic
form concentration*, [arXiv:2610.41416v2](https://arxiv.org/html/2610.41416v2).
It gives TW_1 for independent centered real vectors with common positive
covariance, uniform fixed-p Hilbert–Schmidt quadratic-form bounds, aspect
ratio tending to a positive limit other than one, and uniformly bounded
covariance eigenvalues separated from zero and from the right-edge pole.
For sample count m it centers at f(u_+) and scales by
m^(2/3)(2/f''(u_+))^(1/3), with f as in Section 4 below. The remaining
argument verifies these hypotheses and replaces that conditional center.

## 1. Conditional covariance and its quadratic component

Put u_j=x_j/sqrt(d), U=(u_1,...,u_N), and rho_jk=u_j^T u_k. Conditional on
U, the vectors p_i=sigma(U^T w_i) in R^N are independent and identically
distributed, with mean zero: each preactivation coordinate is exactly
standard Gaussian.

Write h_k=He_k/sqrt(k!), using the probabilists' Hermite polynomials. The
generating-function identity

    E exp(sG-s^2/2) exp(tH-t^2/2)=exp(rho st)

for jointly standard Gaussian G,H of correlation rho gives
E[h_k(G)h_l(H)]=1_{k=l}rho^k. Expanding sigma in Gaussian L^2 and passing
to the limit by Cauchy–Schwarz therefore gives the exact conditional
covariance

    Sigma_jk = sum_{l>=2} a_l^2 rho_jk^l,    Sigma_jj=v.

Here Parseval's identity gives sum_{l>=2} a_l^2=v, since a_0=a_1=0.

Define symmetric matrices B and R with zero diagonal and off-diagonal
entries

    B_jk=rho_jk^2-1/d,
    R_jk=sum_{l>=3} a_l^2 rho_jk^l.

Then the exact decomposition is

    Sigma=(v-q/d)I+(q/d)11^T+qB+R.                           (3)

In particular Tr Sigma=Nv. For j!=k, |R_jk|<=v|rho_jk|^3. Spherical
coordinate moments give

    E rho^(2s)=(1*3*...*(2s-1))/[d(d+2)...(d+2s-2)].          (4)

For completeness, take a standard Gaussian g in R^d and write g=r u.
Its length r and direction u are independent. The moments E g_1^(2s)
and E r^(2s) are respectively the numerator and denominator in (4),
by the Gaussian moment recursion and the chi-square moment recursion.
Consequently

    E||R||_F^2 <= 15v^2 N(N-1)/[d(d+2)(d+4)] = O(d^-1).     (5)

Also, without separating Hermite degrees, |Sigma_jk|<=v rho_jk^2 for
j!=k. Writing D=Sigma-vI gives

    Tr D=0,
    E Tr D^2 <= 3v^2 N(N-1)/[d(d+2)] = O(1).                 (6)

The estimate in (6) alone does not give operator-norm convergence of the
remainder in (3); the next lemma supplies it.

## 2. Exact fourth trace of the centered squared-correlation matrix

Suppose d>=2 and set

    c=1-1/d,    tau=2/[d(d+2)],    (N)_k=N(N-1)...(N-k+1),
    mu_4=12(d-1)(5d^2-13d+12)/[d^4(d+2)(d+4)(d+6)].

The exact identity is

    E Tr B^4 = (N)_2 mu_4 + 2(N)_3(c tau)^2
                         + (N)_4 c tau^3.                  (7)

In particular

    E Tr B^4 <= 60 N^2/d^4 + 8 N^3/d^4 + 8 N^4/d^6,
    ||B||_op=O_p(d^-1/4)=o_p(1) when N/d stays bounded.        (8)

To prove (7), consider the real Hilbert space H of traceless symmetric
d by d matrices with inner product Tr(AB), and put z(u)=uu^T-I/d. Its
dimension is d(d+1)/2-1, and

    E z=0,    ||z||_F^2=c,
    E[<z,A><z,C>]=tau <A,C> for A,C in H.                    (9)

Indeed rotational invariance and sign symmetry give

    E u_a u_b u_c u_e
       =(delta_ab delta_ce+delta_ac delta_be+delta_ae delta_bc)
                                                    /[d(d+2)].

One can determine its constant by summing E(sum_a u_a^2)^2=1.
Contracting against traceless symmetric A,C proves (9).
Since B_jk=<z(u_j),z(u_k)> off the diagonal, its conditional second
moment given u_j equals tau||z(u_j)||_F^2=c tau, independently of u_j.

Expand Tr B^4 as the sum over ordered closed walks (i,j,k,l,i). Because
B has zero diagonal, adjacent indices are distinct. There are exactly
three cases.

With two distinct indices the walk alternates i,j,i,j. There are (N)_2
such walks and each contributes E(rho^2-1/d)^4=mu_4. Expanding the fourth
power and substituting (4) gives

    mu_4=105/[d(d+2)(d+4)(d+6)]
         -60/[d^2(d+2)(d+4)]
         +18/[d^3(d+2)]-3/d^4,

which simplifies to the formula above.

With three distinct indices, either i=k or j=l, exclusively. Each class
has (N)_3 walks. Conditioning on the repeated vertex, the two other
vertices are independent and the expectation is (c tau)^2.

With four distinct indices there are (N)_4 walks. Integrating z(u_i)
first gives

    E_i[<z_i,z_j><z_l,z_i>]=tau<z_j,z_l>.

Integrating z(u_k) then gives a second factor tau and a second copy of
<z_j,z_l>. Its squared expectation is c tau, so the contribution is
c tau^3. This proves (7). Equivalently, this cycle expectation is
Tr((E z tensor z)^4)=dim(H) tau^4=c tau^3, since dim(H) tau=c.

For d>=2, 5d^2-13d+12<=5d^2, so mu_4<=60/d^4. Also c<=1 and tau<=2/d^2.
These inequalities give (8)'s fourth-trace bound. Finally B is symmetric,
so ||B||_op^4<=Tr B^4. Markov's inequality proves its stated stochastic
bound. Independence among different entries of B was never assumed.

## 3. Covariance eigenvalues and the precise subcritical inequality

The first two terms on the right of (3) have eigenvalues

    v+q(N-1)/d    once,    v-q/d    with multiplicity N-1.

By (5), (8) and the variational eigenvalue inequalities,

    lambda_max(Sigma)=v+q(N-1)/d+o_p(1),
    max_{2<=j<=N}|lambda_j(Sigma)-v|=o_p(1),
    lambda_min(Sigma)>=v-o_p(1).                            (10)

These statements also hold for q=0. For q>0, they identify a single
separated *population covariance* eigenvalue v+q alpha. They do not
assert a sample outlier.

Put r=N/m and u_0=-1/[v(1+sqrt(r))]. The limiting pole separation at this
point is

    1+(v+q alpha)lim(u_0)
       =[v/sqrt(b)-q alpha]/[v(1+1/sqrt(b))].                (11)

It is strictly positive exactly under (1). It follows from (10)–(11) that
there are deterministic eta>0 and c_*>0 such that, with probability tending
to one,

    c_*<=lambda_min(Sigma)<=lambda_max(Sigma)
                              <=v(1+sqrt(r))-eta.           (12)

The margin in (12) is the reason for the strict inequality in (1).

## 4. A trace-cancellation edge lemma allowing a subcritical spike

Fix v>0 and let r=N/m stay in a compact subset of (0,infinity). Consider
positive population eigenvalues t_1,...,t_N satisfying

    N^-1 sum_j t_j=v,
    c_*<=t_j<=v(1+sqrt(r))-eta,
    s_2=N^-1 sum_j(t_j-v)^2 -> 0,                            (13)

with fixed positive c_*,eta. Define

    f(u)=-1/u+(1/m)sum_j t_j/(1+t_j u),
    f_0(u)=-1/u+rv/(1+vu),
    u_+ in (-1/t_max,0),    f'(u_+)=0,
    E_+=f(u_+),    gamma_+=(2/f''(u_+))^(1/3),
    e_0=v(1+sqrt(r))^2,
    gamma_0=r^(1/6)/[v(1+sqrt(r))^(4/3)].

For all sufficiently small s_2, uniformly in these data,

    |u_+-u_0|+|E_+-e_0|+|gamma_+-gamma_0|<=C s_2,
    1+t_max u_+>=c_1>0.                                   (14)

Here individual deviations t_j-v need not tend to zero.

To prove the lemma, the upper bound in (13) gives

    1+t_j u_0>=eta/[v(1+sqrt(r))].

Choose a closed interval J about u_0, of fixed sufficiently small radius,
so that all its u are negative and every 1+t_j u and 1+vu has a uniform
positive lower bound. This is possible uniformly in r because all t_j
are uniformly bounded. Direct differentiation gives

    f_0'(u_0)=0,
    f_0''(u_0)=2v^3(1+sqrt(r))^4/sqrt(r)>0.

Shrink J, uniformly, so that f_0'' is bounded below there and f_0' has
strict opposite signs at its endpoints. For delta=t-v the exact identity

    t/(1+tu)-v/(1+vu)-delta/(1+vu)^2
          =-u delta^2/[(1+vu)^2(1+tu)]                     (15)

holds by bringing terms to a common denominator. Its right side and its
first two derivatives in u are bounded in absolute value by C delta^2
on J. Averaging, the linear term vanishes by (13), so

    sup_J |f^(k)-f_0^(k)|<=C s_2,    k=0,1,2.               (16)

For small s_2, f' has a root in J and f'' is uniformly positive there.
On the entire pole interval,

    f''(u)=-2/u^3+(2/m)sum_j t_j^3/(1+t_j u)^3>0,

and f' tends to minus infinity at the left endpoint and plus infinity
at zero. Thus this root is the unique u_+. The mean value theorem and
(16) give |u_+-u_0|<=Cs_2. Bounds on f_0'' on J and f_0'(u_0)=0 then give
|E_+-e_0|<=Cs_2. The bounded derivative f_0''' and (16) give the bound
for gamma_+. The pole separation follows by continuity. This proves (14).

As an independent sign check, t/(1+tu) is convex in t for negative u with
positive denominators. Jensen's inequality gives f(u)>=f_0(u) on J.
Since u_0 minimizes f_0 there, E_+>=e_0.

Apply the lemma to Sigma using (6) and (12). Since N is proportional to d,

    s_2=Tr D^2/N=O_p(N^-1),
    E_X-v(1+sqrt(N/m))^2=O_p(N^-1),
    gamma_X-gamma_0=O_p(N^-1).                              (17)

In particular m^(2/3)(E_X-e_0)->0 in probability. Although the covariance
spike has nonvanishing height, its finite mass and exact trace cancellation
make the centering error negligible at the TW scale.

## 5. Quadratic-form concentration with uniform constants

With probability tending to one, ||U||_op is bounded by a deterministic
constant. Here are elementary estimates sufficient for this assertion.
Represent u_j=g_j/||g_j|| with independent standard Gaussian g_j in R^d,
and put G=(g_1,...,g_N). Markov's inequality applied to exp(-||g_j||^2/2)
gives

    P(||g_j||^2<d/2)<=exp(-d[(log 2)/2-1/4]).

A union bound makes min_j||g_j||>=sqrt(d/2) with probability tending to one.
Take 1/4-nets of the two unit spheres, of sizes at most 9^d and 9^N.
For each pair of net vectors, their bilinear form against G is standard
Gaussian. The Gaussian tail bound and a union bound imply that its maximum
absolute value is at most 4sqrt(d+N), with failure probability at most
2exp(-(8-log 9)(d+N)). Approximating each unit vector by its net gives
||G||_op<=8sqrt(d+N). Thus ||U||_op is bounded, since N/d stays bounded.

Now fix a deterministic U with that norm bound and with bounded Sigma.
Write p=sigma(U^T g) and L=Lip(sigma)||U||_op. The map g->p is L-Lipschitz.
For any locally Lipschitz real F with the moments below finite, the
Gaussian rotation inequality is

    ||F-EF||_p <= (pi/2)||Z||_p || ||grad F|| ||_p,    p>=2.  (18)

To see it, introduce an independent standard Gaussian g' and set
g_theta=g cos(theta)+g' sin(theta) and
h_theta=-g sin(theta)+g' cos(theta). Conditional Jensen bounds the left
side by ||F(g)-F(g')||_p. Integrate the derivative
<grad F(g_theta),h_theta> from 0 to pi/2 and apply Minkowski. For each
theta, g_theta and h_theta are independent standard Gaussian vectors,
so conditional integration over h_theta yields ||Z||_p times the gradient
norm in L^p. Smooth approximation proves the same for locally Lipschitz
functions of polynomial growth, including those used here.

For real symmetric A, the chain rule gives

    ||grad(p^T A p)||<=2L||Ap||.

The function h(g)=||Ap|| is L||A||_op-Lipschitz. From (18),

    ||h||_p <= E h+C_p L||A||_op,
    E h <= (Tr(A^T A Sigma))^(1/2)<=sqrt(||Sigma||_op)||A||_F.

Applying (18) once more proves

    ||p^T A p-Tr(A Sigma)||_p<=C_p'||A||_F,                  (19)

uniformly over these U and dimensions. Complex symmetric A are handled
by real and imaginary parts. Thus (19) verifies the moment hypothesis
of the external theorem without independent coordinates within p.

## 6. Conditional universality and unconditional deterministic centering

To specify a deterministic class on which all constants are uniform,
choose the event consisting of

    ||U||_op<=C_U,    ||B||_op<=N^-1/8,
    ||R||_F<=N^-1/8,    Tr D^2<=N^1/6.                     (20)

Its probability tends to one. Indeed (8) bounds the second failure
probability by O(N^-1/2), (5) bounds the third by O(N^-3/4), and (6)
bounds the fourth by O(N^-1/6); the first was proved above. The deterministic
aspect-ratio limits and (1) ensure (12) uniformly on (20) for all sufficiently
large dimensions. The edge lemma then gives

    s_2<=N^-5/6,
    m^(2/3)|E_X-e_0|=O(N^-1/6)->0,
    |gamma_X-gamma_0|->0                                   (21)

uniformly on (20). All covariance eigenvalue bounds, pole margins and
constants in (19) are uniform on this event.

For H=Y^T Y/m, the external corollary, conditional on any deterministic
sequence of designs in (20), now gives

    gamma_X m^(2/3)[lambda_max(H)-E_X] => TW_1.              (22)

The convergence of conditional distribution functions in (22) is uniform
over (20) at every fixed continuity point. Otherwise select a subsequence
and one deterministic violating design at each dimension. Those designs
have the uniform hypotheses just verified, contradicting (22) for that
deterministic sequence. The same argument gives uniform tightness, allowing
the centering and scaling replacements in (21). Integrating the conditional
distributions and using P((20))->1 gives

    gamma_0 m^(2/3)[lambda_max(H)-v(1+sqrt(r))^2] => TW_1.

Finally lambda_max(H)=r lambda_max(K), because Y^T Y and YY^T have the
same nonzero eigenvalues. The identities

    r^-1 v(1+sqrt(r))^2=v(1+sqrt(b_N))^2,
    gamma_0 r m^(2/3)
      =[b_N^(1/6)/(v(1+sqrt(b_N))^(4/3))]N^(2/3)

prove (2). Its tightness and b_N->b also imply convergence in probability
of the largest eigenvalue to the stated limiting edge.

## 7. Scope and boundary checks

A bounded Lipschitz example with q>0 is

    sigma(t)=cos(t)-exp(-1/2),
    q=exp(-1)/2,    v=(1-exp(-1))^2/2.

Its mean vanishes by the Gaussian characteristic function, its linear
coefficient vanishes by evenness, and its second coefficient is
-exp(-1/2)/sqrt(2). Indeed differentiating E exp(itZ)=exp(-t^2/2) twice
at t=1 gives E Z^2 cos(Z)=0; hence E[(Z^2-1)cos(Z)]=-exp(-1/2).
The variance formula follows from cos^2(Z)=(1+cos(2Z))/2. The condition
(1) becomes

    alpha sqrt(b)<exp(1)-2+exp(-1).

For example alpha=1 and b=1/4 satisfies it, since exp(1)>5/2 makes the
right side greater than 1/2. This confirms that the extension includes
nonzero quadratic coefficients rather than only rank at least three.

At equality in (1), the expression in (11) is zero, so uniform regularity
cannot be obtained by this argument. If the inequality reverses, that
expression is negative and the MP stationary point lies across a population
pole. Thus this proof gives no critical or supercritical fluctuation law.
It does not prove a sample outlier rule in those regimes or TW1 for the
first eigenvalue below such outliers. Random-norm inputs, a nonzero linear
Hermite coefficient, non-Lipschitz polynomial activations and b=1 are also
outside this theorem.
