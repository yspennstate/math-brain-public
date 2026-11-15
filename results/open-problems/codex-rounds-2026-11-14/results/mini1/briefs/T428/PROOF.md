# Signed exponentially decaying profiles: a Brownian tuning lemma

## Scope

This note proves a spectral statement for the gap of two independent standard
planar Brownian motions. It does not prove convergence of stochastic flows.
The connection to Conjecture 1.17 of Hindy Drillick, Jonathan Hou and Shalin
Parekh, *A universality result for the critical 2d stochastic heat flow*,
[arXiv:2609.15832](https://arxiv.org/html/2609.15832v1), is the coefficient
in Definition 1.14 and the tuning in (1.4). The time integral below starts at
zero, as that definition requires.

The profile is fixed, rather than an arbitrary sequence of profiles, and has
strictly positive integral. No nonnegativity or positive definiteness is
assumed in the lemma.

## Statement

Let f be a real measurable function on R^2 satisfying

    |f(x)| <= C exp(-a |x|),     C,a > 0,
    m := integral f(x) dx > 0.

Write L=log N, where N>1, and set

    p_t(z) = (4 pi t)^(-1) exp(-|z|^2/(4t)),
    S_N(z) = integral_0^N p_t(z) dt,
    T_N^f h(x) = L^(-1) integral S_N(x-y) f(y) h(y) dy.

The generator of p_t is Delta. In particular it is the gap kernel, rather
than the kernel of one standard Brownian motion. Define, away from zero,

    g(z) = (log 4 - gamma - 2 log |z|)/(4 pi),
    I(f) = integral integral f(x) g(x-y) f(y) dx dy,
    mu = m/(4 pi).

Here gamma is Euler's constant. Values of kernels on the diagonal can be
assigned arbitrarily; all operator kernels are understood almost everywhere.

For all sufficiently large N the following assertions hold.

1. T_N^f is a compact bounded operator on complex L^2(R^2). It has a
   positive real algebraically simple eigenvalue Lambda_N(f) that strictly
   dominates every other spectral value in modulus. Its expansion is

       Lambda_N(f) = m/(4 pi) + I(f)/(m log N) + O((log N)^(-2)).       (1)

2. Put u=|f|^(1/2), v=sgn(f)|f|^(1/2), and let

       A_N h(x) = L^(-1) u(x) integral S_N(x-y) v(y) h(y) dy,
       P h = u integral v(y)h(y)dy / m.

   There is a constant K depending on f such that

       sup_{k>=1} ||Lambda_N(f)^(-k) A_N^k - P|| <= K/log N.          (2)

   Thus signed spatial products have a uniformly controlled leading
   eigenvalue even for unbounded numbers of factors. In particular,

       sup_{k>=0} | integral v A_N^k u / (m Lambda_N(f)^k) - 1 |
           <= K/log N.                                             (3)

   The integral in (3) is a linear functional, with no conjugation of
   the real function v. These formulas do not define renewal probabilities.

3. Let f_R=f 1_{|x|<=R}. There exist R_0,N_0,K depending on f such that
   for R>=R_0 and N>=N_0,

       |Lambda_N(f_R)-Lambda_N(f)|
           <= K ((R+1)^2 exp(-aR) + (log N)^(-2)).                   (4)

   Consequently, if kappa>1/a and R_N=kappa log log N for large N,

       Lambda_N(f_{R_N})-Lambda_N(f) = o(1/log N).                   (5)

4. For any real theta, the Brownian spectral tuning

       log N Lambda_N(beta_N^2 f) = 1 + theta/log N + o(1/log N)     (6)

   is equivalent, for positive beta_N, to

       beta_N^2 = 4 pi/(m log N)
           * [1 + (theta - 4 pi I(f)/m^2)/log N + o(1/log N)].       (7)

   The same beta_N satisfies (6) with f_{R_N} in place of f for every
   cutoff in (5).

## Proof

### 1. The integrated heat kernel and its remainder

For r=|z|>0 substitute s=r^2/(4t). This gives

    S_N(z) = (4 pi)^(-1) E_1(r^2/(4N)),
    E_1(q) = integral_q^infinity exp(-s)/s ds.

For q>0,

    E_1(q) = -gamma - log q + H(q),
    H(q) = integral_0^q (1-exp(-s))/s ds,
    0 <= H(q) <= q.

The last inequality uses 0 <= 1-exp(-s) <= s. It follows that

    S_N(z) = (log N)/(4 pi) + g(z) + r_N(z),
    0 <= r_N(z) <= |z|^2/(16 pi N).                                (8)

The normalization of gamma in this identity can also be obtained from
the finite integrals in the audit below.

All polynomial moments of |f| are finite. Also g has only a logarithmic
singularity at zero. Specifically, for |z|<1,

    |g(z)| <= K(1+|log |z||),

and for |z|>=1, |g(z)| <= K(1+|z|). Since f is bounded and integrable,

    integral integral |f(x)f(y)| |g(x-y)|^2 dx dy < infinity.         (9)

Indeed, in |x-y|<1, first bound |f(y)| by C and integrate
(1+|log |x-y||)^2 over that unit disk, then integrate |f(x)|.
The disk integral is finite by polar coordinates. In its complement use
|x-y|<=|x|+|y| and the finite second moments of |f|. This also proves
absolute convergence of I(f), by Cauchy--Schwarz with weight
|f(x)f(y)| dx dy.

### 2. Compact operators and their relation

For fixed N, S_N belongs to L^2(R^2). Near zero this follows from its
logarithmic singularity. At infinity use

    E_1(q) <= exp(-q)/q,

which follows by bounding 1/s by 1/q in its defining integral.
Thus the square integral of the kernel of T_N^f equals

    L^(-2) ||S_N||_2^2 ||f||_2^2 < infinity.

So T_N^f is Hilbert--Schmidt and hence compact.

Convolution by S_N, denoted C_N, is bounded on L^2 with norm at most N:
each convolution by p_t has norm at most one, and one integrates from
zero to N. Multiplication by u and v is bounded, because f is bounded.
Take X=L^(-1) C_N M_v and Y=M_u. Then

    XY=T_N^f,                 YX=A_N.                              (10)

For z!=0 the identity

    (z-XY)^(-1) = z^(-1) [Id + X (z-YX)^(-1) Y]

holds whenever the right side exists, as direct multiplication verifies.
Exchanging X and Y gives the converse. Therefore T_N^f and A_N have
the same nonzero spectrum. They also have the same algebraic
multiplicities there: Y intertwines XY and YX and is injective on every
generalized eigenspace for a nonzero eigenvalue. If Yh=0 then XYh=0,
whereas XY is invertible on that generalized eigenspace. Applying the
same argument to X gives injections in both directions between these
finite-dimensional spaces, so their dimensions coincide.

If f is compactly supported in J, this full-space definition also agrees
with the operator on L^2(J): restrict a full-space eigenfunction to J.
For a nonzero eigenvalue lambda its restriction cannot vanish, because
T_N^f only uses values on J. Conversely, a restricted eigenfunction h
extends to the full space by lambda^(-1)T_N^f(h 1_J); this extension is
in L^2 and has restriction h. Thus the nonzero eigenvalues agree with
the compact-support definition as well.

By (8),

    A_N = A_0 + L^(-1) K_f + D_N,
    A_0 h = (4 pi)^(-1) u integral v h = mu P h,                     (11)

where K_f has kernel u(x)g(x-y)v(y). Equation (9) proves K_f is
Hilbert--Schmidt. The kernel of D_N is L^(-1)u(x)r_N(x-y)v(y).
Its norm is at most its Hilbert--Schmidt norm, and (8) gives

    ||D_N|| <= [integral integral |f(x)f(y)| |x-y|^4 dx dy]^(1/2)
                   / (16 pi N L)
             <= K/(N L).                                         (12)

In particular A_N is compact and ||A_N-A_0||<=K/L.
Although A_N is usually not self-adjoint, no self-adjoint perturbation
claim will be needed.

### 3. The simple real eigenvalue

The functional ell(h)=integral v h is bounded, and ell(u)=m>0.
Consequently P^2=P, its range is the span of u, and A_0=mu P.
For z outside {0,mu},

    (z-A_0)^(-1) = z^(-1)(Id-P) + (z-mu)^(-1)P.                    (13)

Let Gamma be the positively oriented circle |z-mu|=mu/4.
Formula (13) bounds the resolvent uniformly on Gamma. If E_N=A_N-A_0,
the Neumann series for

    z-A_N = (z-A_0)[Id-(z-A_0)^(-1)E_N]

therefore converges there for large N. The corresponding spectral
projection

    P_N = (2 pi i)^(-1) integral_Gamma (z-A_N)^(-1) dz

satisfies ||P_N-P||<=K||E_N||<=K/L by the resolvent identity.
For large N this distance is less than one. Two projections at distance
less than one have ranges of equal finite dimension: restricting one
projection to the other's range is injective, in both directions.
Hence P_N has rank one.

The same Neumann argument on the complement of the disks
|z|<mu/4 and |z-mu|<mu/4 shows that there is no spectrum there.
The bound is uniform on that complement by (13), including as
|z| tends to infinity. Thus A_N has exactly one eigenvalue, counted
with algebraic multiplicity, in the disk about mu. Call it lambda_N.
Because its kernel is real, conjugation preserves its spectrum.
The disk is invariant under conjugation and has just one eigenvalue;
therefore lambda_N is real. It is larger than 3mu/4, while every other
spectral value has modulus less than mu/4. By (10) this proves the
existence, simplicity and dominance asserted for Lambda_N(f)=lambda_N.

To compute the correction, normalize an eigenvector by

    w_N = m P_N u / ell(P_N u).

The denominator tends to m, so w_N=u+O(1/L) in L^2 and ell(w_N)=m.
Apply ell to A_N w_N=lambda_N w_N. Since A_0=mu P,

    lambda_N = mu + ell(E_N w_N)/m
             = mu + ell(E_N u)/m + O(||E_N||^2).

By absolute convergence established in (9),

    ell(K_f u) = integral integral f(x)g(x-y)f(y) dx dy = I(f).

Using (12) now gives

    lambda_N = mu + I(f)/(m L) + O(L^(-2)+(N L)^(-1)).

Since log N <= N, this proves (1).

### 4. Uniform powers

Spectral projections commute with the operator they project. Set

    B_N=A_N(Id-P_N).

Because A_0=mu P and P(Id-P)=0,

    ||B_N|| <= ||E_N|| ||Id-P_N|| + mu ||P(P-P_N)|| <= K/L.

Furthermore A_N=lambda_N P_N+B_N, and both cross products of
P_N and B_N vanish. Hence for every integer k>=1,

    lambda_N^(-k) A_N^k = P_N + lambda_N^(-k) B_N^k.

As lambda_N>=3mu/4, the last term has norm at most (K/L)^k
after enlarging K. For N sufficiently large, K/L<1; its supremum
over k>=1 is K/L. This proves (2). Applying ell on the left and u
on the right proves (3) for k>=1, because ell(Pu)=m. For k=0
the expression in (3) is exactly one.

### 5. Uniformity under cutoffs

Let m_R=integral f_R. Polar coordinates give

    |m_R-m| <= 2 pi C integral_R^infinity r exp(-ar) dr
             <= K(R+1)exp(-aR).                                   (14)

Choose R_0 so large that m_R>=m/2 for every R>=R_0.
All moment bounds, supremum bounds and Hilbert--Schmidt bounds above
are uniform for this family. The norms of its rank-one projections
are at most 2||f||_1/m. The eigenvalue separation is uniformly
positive, since mu_R=m_R/(4pi)>=m/(8pi).
Thus the resolvent arguments and the expansion (1), with f_R,m_R
in place of f,m, hold with common N_0 and common error constant.
For clarity this last assertion follows directly from (13): its
resolvent bounds depend only on a positive lower bound for mu_R
and an upper bound for ||P_R||, both just supplied. The bounds on
E_N and D_N are likewise uniform.

To compare the correction integrals, first note that

    integral |f(y)| |g(x-y)| dy <= K(1+|x|).                        (15)

On |x-y|<1 use boundedness of f and integrability of |log |x-y||
over the unit disk. On the complement use
|g(x-y)|<=K(1+|x|+|y|), then integrate the zeroth and first moments
of |f|. The part removed from the double integral I(f) has either
|x|>R or |y|>R. By symmetry of g, (15), and polar coordinates,

    |I(f_R)-I(f)|
       <= 2 integral_{|x|>R} |f(x)|
                    integral |f(y)||g(x-y)|dy dx
       <= K integral_R^infinity r(1+r)exp(-ar) dr
       <= K(R+1)^2 exp(-aR).                                      (16)

Equations (14)--(16), m_R>=m/2, and the uniform version of (1)
give (4), since L>=1 for large N. For R_N=kappa log L,

    L(R_N+1)^2 exp(-aR_N)
       = O((log L)^2 L^(1-a kappa)) -> 0

when a kappa>1, and L*L^(-2)->0. This proves (5).

The assertion in (4) is an asymptotic estimate with a L^(-2)
error floor. It is not a fixed-N continuity rate as R tends to infinity.

### 6. Critical tuning

For b>0, T_N^{bf}=b T_N^f. Thus

    Lambda_N(beta_N^2 f)=beta_N^2 Lambda_N(f).

Using (1) and m>0, its reciprocal has the expansion

    Lambda_N(f)^(-1)
       = (4 pi/m)[1 - 4 pi I(f)/(m^2 L) + O(L^(-2))].

Solving (6) for beta_N^2 yields (7), and substituting (7) in (1)
gives the converse. In particular beta_N^2 L is bounded. Therefore
(5) implies

    L |Lambda_N(beta_N^2 f_{R_N})-Lambda_N(beta_N^2 f)|
       = beta_N^2 L |Lambda_N(f_{R_N})-Lambda_N(f)|
       = o(1/L).

This preserves theta in (6) and completes the proof.

## A signed positive-definite example

Let phi_s(x)=(2 pi s)^(-1) exp(-|x|^2/(2s)) and take

    f=2 phi_1-phi_2.

This profile has m=1, is positive near zero and negative for all
sufficiently large |x|. It satisfies an exponential envelope, since
each Gaussian does. Its Fourier transform, with convention
hat f(k)=integral exp(-i k.x)f(x)dx, is

    2 exp(-|k|^2/2)-exp(-|k|^2)=2q-q^2>=0,     0<=q<=1.

It is therefore a possible covariance profile: positivity of its
quadratic form follows by Fourier inversion against test functions.
This example does not assert a stochastic-flow convergence theorem.

For a centered planar Gaussian Z of covariance s Id,
|Z|^2/(2s) is an exponential random variable of mean one. Hence

    E log |Z| = (log(2s)-gamma)/2,
    E g(Z) = (4 pi)^(-1) log(2/s).

The difference of independent Gaussian vectors of covariances s Id
and t Id has covariance (s+t) Id. Consequently

    I(f) = (4 pi)^(-1)
       [4 log(2/2)-4 log(2/3)+log(2/4)]
         = (4 pi)^(-1) log(81/32).                                (17)

The critical tuning in this example is therefore

    beta_N^2 = 4 pi/log N
       * [1 + (theta-log(81/32))/log N + o(1/log N)].                (18)

## Independent checks and limits of the result

The heat-kernel constant can be checked without using the E_1
expansion. Put q=|z|^2/4 and split the time integral at 1:

    4 pi [S_N(z)-(log N)/(4pi)]
      = integral_0^1 exp(-q/t) dt/t
        + integral_1^N [exp(-q/t)-1] dt/t.

For q>0 the limit as N tends to infinity is finite. Substituting
s=q/t in the two integrals gives

    F(q)=integral_q^infinity exp(-s) ds/s
           + integral_0^q [exp(-s)-1] ds/s.

Differentiation gives F'(q)=-1/q. At q=1,

    F(1)=integral_1^infinity exp(-s) ds/s
           + integral_0^1 [exp(-s)-1] ds/s = -gamma.

The last equality follows by integration by parts in
Gamma'(1)=integral_0^infinity exp(-s)log s ds=-gamma, first
integrating from epsilon and then letting epsilon decrease to zero.
Thus F(q)=-gamma-log q. The omitted tail has absolute value at
most integral_N^infinity q dt/t^2=q/N. This independently
recovers both the constant and the remainder in (8).

There is a second check of (17). Define the heat overlap

    H(t)=integral integral f(x)p_t(x-y)f(y) dx dy.

Gaussian convolution gives

    H(t)=(2 pi)^(-1)[4/(2+2t)-4/(3+2t)+1/(4+2t)].

Integrating this rational function gives exactly

    integral_0^N H(t)dt
       = (4 pi)^(-1)[4 log(1+N)
                     -4 log(1+2N/3)+log(1+N/2)].                  (19)

Subtract (log N)/(4pi) and let N increase. The resulting constant
is again log(81/32)/(4pi). This calculation uses heat overlaps
rather than logarithmic Gaussian moments. Numerically integrating
H(t) on (0,1) and H(t)-1/(4pi t) on (1,infinity) provides a further
check in `verify.py`.

The positive-mass condition is essential to this proof. If m=0,
A_0^2=0, and there is no isolated eigenvalue mu about which to run
the resolvent argument. The proof gives no conclusion in that case.
Constants also need not remain bounded as m decreases to zero.

The growing cutoffs f_{R_N} have supports of increasing radii, so
they do not satisfy a fixed support-radius hypothesis. Equation (5)
alone does not justify applying a compact-support universality
theorem to them. Signed weights also cannot be normalized into the
positive renewal probabilities used in the target paper. Controlling
the time-resolved signed renewal kernels and the higher moments
remains outside this result.

Even when f is a covariance, the hard cutoff f_R need not be positive
definite. The cutoff assertion is about operators; it does not construct
an approximating Gaussian environment.

Finally, a general N-dependent gap process need not have the
explicit remainder (8). No claim is made that the paper's hypotheses
alone imply the weighted norm estimate (11). The statement proved
here concerns the Brownian gap and fixed positive-mass profiles.
