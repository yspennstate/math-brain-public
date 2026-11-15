# T067-CUBIC-FUSION-001 v1: a global signed cubic fusion inequality

Status: proof (unaudited). This is an auxiliary posterior-law inequality and its sign corollaries, not a reconstruction-threshold theorem. No priority claim.

Let u=(1/3,1/3,1/3). For a probability law mu on the three-state simplex that is invariant under every coordinate permutation, put

    M(mu)=E_mu sum_i(3p_i-1)^2,
    T(mu)=E_mu sum_i(3p_i-1)^3.

Such a law has mean u and defines the uniform-prior experiment W(dp|i)=3p_i mu(dp). Let nu be the posterior law obtained from two such experiments, with laws mu_L,mu_R, that are independent conditional on their common root. We prove, on the entire closed simplex,

    T(nu)>=(1-M(mu_R)/6)T(mu_L)
                +(1-M(mu_L)/6)T(mu_R).                    (CF)

In particular, fusion preserves nonnegative T. A positive Potts edge also preserves its sign. Consequently every canonical finite-depth ferromagnetic three-state tree posterior has T>=0. Moreover, every symmetric posterior-law fixed point of regular d-child BP with d*lambda^3<1 has T>=0. The same fixed-point assertion holds for independent random offspring with finite mean d.

These conclusions do not prove the additional second-moment contraction in the earlier conjecture T067-CUBIC-CAND-001 v1.

## 1. Orbit reduction and the exact Bayesian expression

An invariant law is a mixture of the uniform permutation orbits of sorted simplex vectors. This follows, for example, by sorting the vector and averaging its six coordinate permutations, retaining multiplicities when coordinates coincide. The two orbit tags are independent under the product of the marginal experiment laws.

For one pair of orbit tags fix the orientation of the first and average the six permutations of the second. Simultaneous permutation invariance of the statistics makes this equal to the average over both orientations. Every sorted simplex vector is

    p(r,y)=((1-r)/3, (1-r)/3+ry/2,
                            (1-r)/3+r(1-y/2)),  0<=r,y<=1.

Indeed r=1-3p_min; for r>0 take y=2(p_mid-p_min)/r. Ordering gives y in [0,1]. For r=0 all choices of y give u.

For two effective posterior vectors write alpha=3p-1, beta=3r-1, and, for each relative permutation pi,

    c_pi=alpha.beta_pi, S_pi=3+c_pi=9 sum_i p_i r_pi(i),
    v_pi=alpha+beta_pi+alpha*beta_pi-(c_pi/3)1,
    W_pi=sum_i v_pi,i^3.

The likelihood of the observation pair relative to the product of marginal observation laws is S_pi/3. If S_pi>0, its posterior has root-scaled deviation 3v_pi/S_pi. Its orbit-averaged output cubic moment is therefore

    K3=(9/6) sum_pi W_pi/S_pi^2.                           (1)

The six weights S_pi/18 sum to one. Let m_L=|alpha|^2,m_R=|beta|^2,t_L=sum alpha_i^3,t_R=sum beta_i^3. It suffices to prove the orbit inequality

    G:=K3-t_L-t_R+(m_R*t_L+m_L*t_R)/6 >=0.                (2)

Averaging (2) over the independent orbit tags gives (CF), including the products of the unconditional moments. This averaging uses the base product law; the Bayesian observation weight is already included in (1).

## 2. A polynomial with exactly the sign of the gap

The following rational scale is only an algebraic parametrization, not an edge restriction: A=99,B=140,a=A/B. Put

    f(y)=(-2,3y-2,4-3y),
    alpha=(A/(2B))*t*f(y), beta=(A/(2B))*s*pi f(z),
    0<=t,s<=B/A, 0<=y,z<=1.

Thus p=p(at,y), r=p(as,z) cover the full simplex. Define

    Q_y=sum_i f_i(y)^2, T_y=sum_i f_i(y)^3,
    Q_z=sum_i f_i(z)^2, T_z=sum_i f_i(z)^3,
    C_pi=sum_i f_i(y) f_pi(i)(z),
    Snum_pi=12B^2+A^2*C_pi*t*s,
    vnum_pi,i=6AB[t*f_i(y)+s*f_pi(i)(z)]
                 +3A^2*t*s*f_i(y)*f_pi(i)(z)-A^2*C_pi*t*s,
    Wnum_pi=sum_i vnum_pi,i^3,
    D2=product_pi Snum_pi^2,
    D2_minus_pi=product_(sigma!=pi) Snum_sigma^2.

Direct substitution gives S_pi=Snum_pi/(4B^2), v_pi=vnum_pi/(12B^2), and

    K3=sum_pi Wnum_pi/(72B^2*Snum_pi^2).

Also m_L=A^2*t^2*Q_y/(4B^2), t_L=A^3*t^3*T_y/(8B^3), with the analogous right formulas. Therefore the exact polynomial

    P=[-72A^3 B^2(T_y*t^3+T_z*s^3)
          +3A^5(T_y*Q_z*t^3*s^2+Q_y*T_z*t^2*s^3)]*D2
          +8B^3 sum_pi Wnum_pi*D2_minus_pi                 (3)

satisfies

    G=P/(576B^5*D2)                                       (4)

whenever all S_pi>0. Every factor on the denominator is strictly positive on the interior simplex. Formula (3), including its constants and sign, is also independently restored against the Bayesian expression (1) below.

## 3. Whole-domain exact Bernstein certificate

The exact integer builder checks that every monomial of P is divisible by t^2*s^2. It divides by that monomial, substitutes t=(B/A)*tau and s=(B/A)*sigma, clears the rational denominators by a positive common multiplier, and divides by a positive integer coefficient gcd. The resulting polynomial H(tau,sigma,y,z) differs from P/(t^2*s^2) by a strictly positive factor. Its degrees are (13,13,14,14).

For one variable, the identity

    x^i=sum_(k=i)^n [binom(k,i)/binom(n,i)]
                              *binom(n,k)*x^k*(1-x)^(n-k)

converts monomials to a nonnegative Bernstein basis on [0,1]. Apply it in the four coordinates, with the stated degrees. Each conversion clears denominators by a positive integer multiplier and may divide by a positive gcd. The final tensor has 44,100 possible coefficients: 43,393 are strictly positive integers and 707 are zero. No coefficient is negative. Thus H>=0 on the entire closed unit box, and P>=0 on the entire original rectangle. At t*s=0 the original polynomial vanishes, so division has lost no boundary case.

The reproducible builder is checks/cubic_invariant_certificate.py. Run with --domain full and --phase raw,bern1,bern2,bern3,bern4 in that order. Alternatively checks/cubic_invariant_run.py --domain full runs those finite phases. The files checks/cubic_invariant_full_<phase>.json store every coefficient and the radial scaling/gcd metadata. Arithmetic is arbitrary-precision integer or exact rational throughout: no sampling, floating-point comparison, quadrature or truncated series enters this certificate.

The separate checks/cubic_invariant_independent_check.py imports no certificate builders. It checks every coefficient in each of the four axis transformations by exact slice dot products, all final signs, and the raw/Bernstein evaluations at six rational points and all 16 corners. At all six points it independently computes the actual posterior and its six Bayesian weights, restores the positive raw gcd and radial denominator, and verifies (4) exactly. It also verifies the direct orbit gap at all 16 corners, skipping zero-weight observations. Its report checks/cubic_invariant_independent_check.json records all source/data SHA-256 hashes and PASS. These are independent arithmetic checks within the worker; they do not replace the required external mathematical audit.

## 4. Zero-likelihood boundary observations

First apply (4) to strictly positive posterior coordinates, where S_pi>0, to prove (2). At a boundary pair with S_pi=0, the observation pair has probability zero. Define its contribution to the cubic expectation to be zero. This is the continuous extension: the absolute root-posterior cubic statistic is bounded by 24 on the compact simplex, so its weighted absolute contribution is at most 24*S_pi/18 and tends to zero with S_pi. The input moments are continuous. Approximate any boundary orbit pair by mixing each input vector with a positive amount of u and take the limit. It follows that (2) holds on the full closed simplex. Finally average over the orbit tags as in Section 1; all statistics are bounded, so the expectations are legitimate. This completes the proof of (CF).

## 5. Nonnegative cubic moment of canonical posteriors

On the three-state simplex, M<=6: the convex function sum_i(3p_i-1)^2 has value 6 at every vertex, so its value anywhere is at most 6. Hence both coefficients in (CF) belong to [0,1]. Fusion of two laws with T>=0 has T>=0.

A ferromagnetic edge of eigenvalue lambda>=0 changes a child posterior p to u+lambda*(p-u). Its cubic moment is lambda^3*T, preserving nonnegativity. A fully observed leaf has the uniform law on the three vertices and T=6. A leaf carrying no observation has law delta_u and T=0. Induct on a finite tree, fusing its branches successively. This proves T>=0 for its canonical root posterior. In particular it holds for every finite-depth regular tree and, conditionally on every locally finite tree shape, every finite-depth Galton-Watson tree. Bounded convergence preserves this sign in any canonical posterior-law limit.

## 6. Sign of arbitrary subcritical or critical BP fixed points

Let mu be an invariant fixed point and suppose, toward contradiction, that T=T(mu)<0. An individual child message has cubic moment t=lambda^3*T<=0 and second moment m=lambda^2*M(mu)<=6. For j independent conditional-root child experiments, let T_j,M_j be the cubic/second moments of their fused posterior law; T_0=M_0=0. By (CF), for every j>=1,

    T_j >= alpha*T_(j-1)+beta_(j-1)*t,
    alpha=1-m/6 in [0,1], beta_(j-1)=1-M_(j-1)/6 in [0,1].

Inductively T_j>=j*t. Indeed multiplication by alpha preserves the inductive lower bound, and alpha*(j-1)+beta_(j-1)<=j; multiplying the latter by t<=0 reverses the inequality. For a regular d-child fixed point this gives

    T=T_d>=d*lambda^3*T.

If d*lambda^3<1 and T<0, its right side is strictly greater than T, a contradiction. The zero-edge case is also covered (the output is uniform).

For random offspring D independent of the root and of the iid child experiments, assume E D=d<infinity. Conditional on D=j the same calculation gives T_j>=j*lambda^3*T. The count D is part of the observed tree and carries no root information; the fixed-point output cubic moment is E[T_D]. Thus again T>=d*lambda^3*T, impossible for T<0 if d*lambda^3<1. Integrability is harmless: T_D is uniformly bounded, and D*lambda^3*T is integrable by the finite-mean assumption.

For 0<lambda<1, d*lambda^2<=1 implies d*lambda^3<=lambda<1. Hence these regular and finite-mean random-offspring fixed points all have T>=0 throughout the positive Kesten-Stigum nonreconstruction region. Repeated fusion then gives nonnegative T for every finite prefix of their child experiments as well.

## 7. A stronger proposed inequality is false

Adding +M(mu_L)*M(mu_R)/6 to the right side of (CF) is invalid. An exact orbit counterexample has sorted tags

    p_L=(0,1/18,17/18),
    p_R=(2113/15000,2113/15000,5387/7500).

The gap for that stronger inequality is exactly

    -69138269216314344791/432561467250000000000 <0.

The separate checker reproduces this negative control. Both input cubic moments are positive, so this counterexample concerns the stronger quantitative formula and does not contradict the sign-preservation corollary actually proved here.

NEXT: Apply the nonnegative sign in the exact second-moment identity to derive a local fixed-point exclusion estimate uniform in the regular tree degree.
