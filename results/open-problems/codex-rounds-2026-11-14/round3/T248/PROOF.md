# Spherical inputs with Hermite rank at least three

Let the columns of X in R^{d x N} be independent and uniform on the sphere of radius sqrt(d). Let W in R^{m x d} have independent standard real Gaussian entries, independently of X. Suppose

    N/d -> alpha in (0,infinity),    m/N -> b in (0,infinity),    b != 1.

Let sigma:R->R be a fixed Lipschitz function. For a standard Gaussian Z, assume

    E sigma(Z) = E[Z sigma(Z)] = E[(Z^2-1)sigma(Z)] = 0,
    v = E sigma(Z)^2 > 0.

Set Y_ij = sigma(w_i^T x_j/sqrt(d)), K=YY^T/N, and b_N=m/N. Then

    g_N N^(2/3) [lambda_max(K)-v(1+sqrt(b_N))^2] => TW_1,
    g_N = b_N^(1/6) / [v(1+sqrt(b_N))^(4/3)].                 (1)

In particular lambda_max(K) converges in probability to v(1+sqrt(b))^2. The statement uses the exact finite-dimensional aspect ratio in its centering.

The only edge-universality theorem used below is Corollary 1.4 of Guangchen Chen and Xing Lyu, *Tracy–Widom law for sample covariance matrices under quadratic form concentration*, [arXiv:2610.41416v2](https://arxiv.org/html/2610.41416v2). It applies to independent centered real vectors with common positive covariance, uniform fixed-p Hilbert–Schmidt quadratic-form bounds, aspect ratio bounded away from one, and a uniformly regular covariance edge. It gives TW_1 centered at the finite covariance edge, with scale (2/f''(u_+))^(1/3), where f is defined below. The estimates below verify these assumptions and replace that random edge by the explicit center in (1).

## 1. Exact conditional covariance

Write u_j=x_j/sqrt(d), U=(u_1,...,u_N), and rho_jk=u_j^T u_k. Conditional on X, the feature rows

    q_i = sigma(U^T w_i) in R^N,    1 <= i <= m,

are independent and identically distributed. Each preactivation coordinate is exactly standard Gaussian. Thus E[q_i|X]=0.

Use the orthonormal probabilists' Hermite polynomials h_k=He_k/sqrt(k!) and write sigma=sum_{k>=0} a_k h_k in L^2 of Gaussian measure. The assumptions give a_0=a_1=a_2=0 and sum_{k>=3} a_k^2=v. For jointly standard Gaussian G,H of correlation rho,

    E[h_k(G)h_l(H)] = 1_{k=l} rho^k.

One way to verify the identity is to expand

    E[exp(sG-s^2/2) exp(tH-t^2/2)] = exp(rho st)

in powers of s,t. The identity extends from polynomial partial sums to sigma by Cauchy–Schwarz, since both marginals remain standard Gaussian. Consequently the conditional covariance Sigma satisfies

    Sigma_jk = sum_{l>=3} a_l^2 rho_jk^l,
    Sigma_jj = v,    |Sigma_jk| <= v |rho_jk|^3 for j != k.  (2)

Set D=Sigma-vI_N. In particular Tr D=0 exactly, not just in expectation.

For two independent unit spherical vectors, rotation invariance identifies their inner product with the first coordinate of a uniform unit vector. If g is standard Gaussian in R^d, then g/||g|| is independent of ||g||. Using E g_1^6=15 and E||g||^6=d(d+2)(d+4),

    E rho_jk^6 = 15/[d(d+2)(d+4)].

Therefore

    E||D||_F^2 <= 15 v^2 N(N-1)/[d(d+2)(d+4)] = O(d^-1),
    ||D||_op <= ||D||_F = O_p(d^-1/2),
    s_2 := Tr(D^2)/N = O_p(d^-2).                          (3)

The sixth moment can also be obtained without Gaussian radial moments: the spherical coordinate square has Beta(1/2,(d-1)/2) distribution, whose third moment is (1*3*5)/[d(d+2)(d+4)]. Independence between different pairs is not needed for (3).

## 2. A deterministic covariance-edge estimate

Fix v>0 and let r=N/m range over a compact subset of (0,infinity). Let a positive N x N matrix have eigenvalues t_j=v+delta_j, with

    sum_j delta_j=0,    epsilon=max_j |delta_j| sufficiently small,
    s_2=N^-1 sum_j delta_j^2.

Define

    f(u)=-1/u+(1/m)sum_j t_j/(1+t_j u),
    u_+ in (-1/t_max,0),    f'(u_+)=0,
    E_+=f(u_+),    gamma_+=(2/f''(u_+))^(1/3).

There are constants depending only on v and the compact range of r such that

    |u_+-u_0| + |E_+-e_0| + |gamma_+-gamma_0| <= C s_2,    (4)

where

    u_0=-1/[v(1+sqrt(r))],
    e_0=v(1+sqrt(r))^2,
    gamma_0=r^(1/6)/[v(1+sqrt(r))^(4/3)].

Also t_j are uniformly positive and bounded, and 1+t_max u_+ is uniformly positive. Thus this edge is uniformly regular in the sense needed by Chen–Lyu.

Here is a proof with uniform constants. For the scalar covariance vI let f_0(u)=-1/u+rv/(1+vu). Direct differentiation gives

    f_0'(u_0)=0,
    f_0''(u_0)=2v^3(1+sqrt(r))^4/sqrt(r)>0,
    1+vu_0=sqrt(r)/(1+sqrt(r)).

Choose a small closed interval J around u_0, uniformly in r, on which u stays negative and 1+tu has a fixed positive lower bound for |t-v|<=epsilon. The interval can be chosen so f_0''>=c>0 there and f_0' has opposite signs at its two endpoints. For j=0,1,2, Taylor expand in t the smooth functions

    partial_u^j [t/(1+tu)].

Their first-order terms cancel upon averaging because sum delta_j=0. Their second t-derivatives are uniformly bounded on J. Hence

    sup_{u in J} |f^(j)(u)-f_0^(j)(u)| <= C s_2, j=0,1,2. (5)

For small epsilon, f' has a zero in J, and f''>=c/2 there. On the entire interval (-1/t_max,0),

    f''(u)=-2/u^3+(2/m)sum_j t_j^3/(1+t_j u)^3 > 0.

Moreover f' tends to minus infinity at the left endpoint and plus infinity at the right endpoint. The zero in J is therefore the unique u_+. Equation (5) at u_0 and the mean value theorem give |u_+-u_0|<=Cs_2. A Taylor expansion in u at the stationary point u_0, together with (5), gives |E_+-e_0|<=Cs_2. The derivative f_0''' is uniformly bounded on J, so (5) gives |f''(u_+)-f_0''(u_0)|<=Cs_2. The map x->(2/x)^(1/3) is uniformly Lipschitz on the resulting positive compact interval. This proves (4). The covariance and pole-separation bounds follow from t_j=v+O(epsilon) and u_+=u_0+O(s_2).

For an additional check on sign and magnitude, expansion by one more order gives

    E_+-e_0 = [(1+sqrt(r))^2/(v sqrt(r))]s_2
                  + O(epsilon s_2+s_2^2).                 (6)

Indeed the quadratic Taylor coefficient of t/(1+tu_0) is -u_0/(1+vu_0)^3. Multiplication by r gives the coefficient in (6). Moving from u_0 to u_+ changes f by O(s_2^2), because f'(u_0)=O(s_2) and u_+-u_0=O(s_2). In particular the leading shift is positive. A separate exact sign check follows from convexity in t: the second t-derivative of t/(1+tu) is -2u/(1+tu)^3>0 on J. Jensen gives f(u)>=f_0(u) there; since u_+ is in J and u_0 minimizes f_0 on J, E_+>=e_0.

Applying (4) to (3) proves

    E_X-v(1+sqrt(N/m))^2 = O_p(d^-2),
    gamma_X-[ (N/m)^(1/6)/(v(1+sqrt(N/m))^(4/3)) ]
                                                 = O_p(d^-2). (7)

In particular the random centering displacement is o_p(m^-2/3). Operator-norm closeness alone would not give this precision.

## 3. Uniform input norm and quadratic-form concentration

There is a fixed C_U such that P(||U||_op>C_U)->0. To see this, generate independent columns by u_j=g_j/||g_j|| with g_j standard Gaussian in R^d, and write G=(g_1,...,g_N). For each column a chi-square Chernoff bound gives

    P(||g_j||^2 <= d/2) <= exp(-c d).

For example E exp(-||g_j||^2/2)=2^(-d/2), and Markov gives c=(log(2))/2-1/4>0. A union bound makes the minimum column norm at least sqrt(d/2) with probability tending to one. To bound ||G||_op, take 1/4-nets of the unit spheres in R^d and R^N, of sizes at most 9^d and 9^N. For each pair a,b the scalar a^T G b is standard Gaussian. A union bound using P(|Z|>t)<=2exp(-t^2/2), with t=4sqrt(d+N), shows that the maximum over the nets is at most t except with probability at most 2exp(-(8-log(9))(d+N)). Approximating both vectors in the bilinear supremum gives ||G||_op<=2t. Thus

    ||U||_op <= ||G||_op/min_j ||g_j|| = O(1)

with probability tending to one, since N/d stays bounded.

Now fix a deterministic U with ||U||_op<=C_U and Sigma_op<=C_S, and put q=sigma(U^T g), g standard Gaussian. The map g->q is L-Lipschitz for L=Lip(sigma) C_U, and q is centered. For a real symmetric deterministic A put F(g)=q^T A q. Its weak gradient exists almost everywhere and satisfies

    ||grad F|| <= 2L||Aq||.

The Gaussian Lp Poincare inequality, for fixed p>=2, yields

    ||F-EF||_p <= C_p L || ||Aq|| ||_p.                   (8)

All functions here have at most polynomial growth. The inequality can first be proved for smooth truncations and passed to the limit. A direct dimension-free proof uses an independent standard Gaussian g': by conditional Jensen, ||F(g)-EF||_p<=||F(g)-F(g')||_p. Along g_theta=g cos(theta)+g' sin(theta), 0<=theta<=pi/2, its derivative is the scalar product of grad F(g_theta) with h_theta=-g sin(theta)+g' cos(theta). For each theta the vectors g_theta and h_theta are independent standard Gaussians. Conditional on g_theta, that scalar product is Gaussian with variance ||grad F(g_theta)||^2. Integration and Minkowski's inequality therefore give ||F(g)-EF||_p <= (pi/2)||Z||_p || ||grad F|| ||_p. This proves the inequality used in (8) without a dimension-dependent constant.

The function h(g)=||Aq|| is L||A||_op-Lipschitz. Applying the same Gaussian rotation inequality to h gives

    ||h||_p <= E h+C_p L||A||_op.

Also

    E h <= (E h^2)^(1/2)
         = (Tr(A^T A Sigma))^(1/2) <= sqrt(C_S)||A||_F.

Combining these estimates with ||A||_op<=||A||_F proves

    ||q^T A q-Tr(A Sigma)||_p <= C_p' ||A||_F.             (9)

The constants are independent of d,N,m and of the admissible U. For complex symmetric A, apply (9) to its real and imaginary parts and use the triangle inequality. This is the moment assumption in Chen–Lyu, with an independent verification for this model.

## 4. Conditional universality and removal of conditioning

Consider the design event

    B_d={||U||_op<=C_U, ||Sigma-vI||_F<=d^-1/4}.

The preceding norm bound and (3), followed by Markov's inequality, imply P(B_d)->1. On B_d, for all sufficiently large d the covariance is uniformly positive, bounded, and regular by Section 2. The constants in (9) are uniform. Moreover

    s_2 <= d^-1/2/N = O(d^-3/2),

so m^(2/3)|E_X-e_0|->0 and |gamma_X-gamma_0|->0 uniformly on B_d.

For H=Y^T Y/m, Chen–Lyu Corollary 1.4, applied conditionally on any deterministic sequence of designs in B_d, gives

    gamma_X m^(2/3)[lambda_max(H)-E_X] => TW_1.           (10)

This implication is uniform over B_d at every fixed continuity point of the limiting distribution. Otherwise one could select a subsequence of dimensions and a deterministic bad design in each B_d at which the distribution functions differ by a fixed positive amount. Those designs still satisfy all the uniform constants and the aspect-ratio hypothesis of the theorem, contradicting (10) along that subsequence. If needed the subsequence may be completed by arbitrary designs in B_d; this set is nonempty for all sufficiently large dimensions since its probability tends to one.

Uniform convergence in (10), uniform edge replacement on B_d, and P(B_d)->1 allow integration over X. Slutsky's theorem yields

    gamma_0 m^(2/3)[lambda_max(H)-v(1+sqrt(N/m))^2]
                                                        => TW_1. (11)

The required tightness for changing the scale follows from (10) and the same uniformity argument. This step does not require independence between the random edge and the largest eigenvalue.

The nonzero eigenvalues of H and K differ by m/N. Thus, with r=N/m,

    lambda_max(H)=r lambda_max(K),
    r^-1 v(1+sqrt(r))^2=v(1+sqrt(b_N))^2,
    gamma_0 r m^(2/3)=g_N N^(2/3).

Substitution in (11) proves (1). Tightness at scale N^-2/3 and convergence of b_N give the claimed convergence in probability.

## 5. Scope and checks

The activation class is nonempty: sigma(t)=sin(t)-(exp(3/2)/2)sin(2t) is Lipschitz and odd. The Gaussian identity E[Z sin(aZ)]=a exp(-a^2/2) cancels its degree-one coefficient, and oddness cancels degrees zero and two. It is nonzero in Gaussian L^2.

The extra degree-two cancellation is essential to this proof. With a_2 nonzero, spherical correlations squared have mean 1/d. Formula (2) then admits a covariance component of order N/d in a distinguished direction, so the Frobenius-small argument no longer applies. This does not by itself prove an outlier, nor does it rule out subcritical cases.

The proof does not cover inputs of random column norm, a linear Hermite component, supercritical spikes and the first eigenvalue below them, non-Lipschitz polynomial activations, or m/N->1. It uses a cited edge-universality theorem rather than reproving it. No conclusion for these omitted cases follows from (1).
