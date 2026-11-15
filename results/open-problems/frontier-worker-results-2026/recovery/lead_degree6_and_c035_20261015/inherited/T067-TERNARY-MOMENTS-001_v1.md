# T067-TERNARY-MOMENTS-001 v1: exact q=3 fusion moment inequalities

Status: proof (unaudited). These are auxiliary inequalities, not a reconstruction-threshold theorem. No priority claim.

Let a posterior experiment have uniform prior on three states and an unconditional posterior law invariant under all state permutations. Write u=(1/3,1/3,1/3), and use root-scale moments

    M(mu)=E|3(p-u)|^2, U(mu)=E|3(p-u)|^4,
    T(mu)=E sum_i[3(p_i-1/3)]^3.

Every such law defines a valid experiment by W(dp|i)=3p_i mu(dp). Fusion means two experiments independent conditional on the same root. Set eta=2887/5000. The following hold.

1. If nu is the posterior after two eta-edge children whose original posterior law is mu, then

       U(nu)<=2 eta^4 U(mu)+(3/5)M(mu)^2.                    (F1)

   The same inequality holds for a smaller positive edge eigenvalue.

2. Let mu_L be any symmetric posterior law and let mu_R be a symmetric posterior law supported on p_i>=(1-eta)/3. If nu is their fusion, then

       U(nu)<=U(mu_L)+U(mu_R)+5 M(mu_L)M(mu_R).              (F2)

3. Under the assumptions of 2,

       |T(nu)-T(mu_L)-T(mu_R)|
           <=(5/3)M(mu_L)M(mu_R).                          (C)

Signed cubic moments are not ordered here by Blackwell comparison. Their domain is covered directly by the certificate.

## Bayesian orbit formula and coverage

An invariant law is a mixture of uniform permutation orbits. Each orbit law has mean u. It suffices to prove the respective orbit inequality for every pair of orbit tags and average over their product law. Fix one orientation of the first orbit and average all six permutations of the second. Simultaneous permutation invariance makes this equal to averaging both orientations; repeated permutations retain their natural multiplicity.

Every sorted posterior is p(r,y)=((1-r)/3,(1-r)/3+ry/2,(1-r)/3+r(1-y/2)), 0<=r,y<=1. Indeed r=1-3p_min, and y=2(p_mid-p_min)/r when r>0.

Write a=A/B for an algebraic radial scale. Put f(y)=(-2,3y-2,4-3y), alpha=(a/2)t f(y), beta=(a/2)s pi f(z). These are root-scaled deviations of the actual effective posterior vectors p(at,y), p(as,z), not necessarily of p(t,y), p(s,z). Define

    m_L=|alpha|^2, m_R=|beta|^2, c=alpha.beta, S=3+c,
    v=alpha+beta+alpha*beta-(c/3)1, N=|v|^2, W=sum_i v_i^3.

The observation-pair likelihood relative to the product of marginal observation laws is S/3. The root-scaled output deviation is 3v/S. Thus the orbit output moments are exactly

    K4=(27/6) sum_pi N_pi^2/S_pi^3,
    K3=(9/6) sum_pi W_pi/S_pi^2.                            (1)

For F1 use a=eta, 0<=t,s<=1: these effective posteriors are precisely the eta-edge messages from arbitrary simplex posteriors. Here S>=3(1-eta^2)>0.

For F2 and C use a=99/140, 0<=t<=140/99, 0<=s<=eta*140/99. The first effective radial parameter ranges over [0,1], the second over [0,eta]. This is exactly the asserted left/right domain. The effective right coordinates are at least (1-eta)/3, so S=9 sum_i p_i r_i>=3(1-eta)>0. Artificial pre-edge vectors outside the simplex are never interpreted as probability vectors.

## Exact fourth-moment polynomials

Let Q_y=sum_i f_i(y)^2, Q_z=sum_i f_i(z)^2, C_pi=sum_i f_i(y)f_pi(i)(z), L21_pi=sum_i f_i(y)^2 f_pi(i)(z), and L12_pi=sum_i f_i(y)f_pi(i)(z)^2. Define

    Snum_pi=12B^2+A^2 C_pi ts,       S_pi=Snum_pi/(4B^2),
    Nnum_pi=24A^2 B^2(Q_y t^2+Q_z s^2)+48A^2 B^2 C_pi ts
             +24A^3 B(L21_pi t^2s+L12_pi ts^2)+A^4 Q_yQ_z t^2s^2,
    N_pi=Nnum_pi/(96B^4).

The identity used to expand N is sum alpha_i^2 beta_i^2-c^2/3=m_L m_R/6, obtained by eliminating the third coordinate of both zero-sum triples.

For a positive rational C_e=p/q, let D3=product_pi Snum_pi^3, D3_minus_pi=product_(sigma!=pi) Snum_sigma^3, and

    P4=[2q A^8(Q_y^2 t^4+Q_z^2 s^4)
          +2p A^4 B^4 Q_yQ_z t^2s^2]D3
         -q A^4 B^2 sum_pi Nnum_pi^2 D3_minus_pi.

Direct substitution into (1) gives the exact signed gap

    a^4(m_L^2+m_R^2)+C_e m_L m_R-a^4 K4
         =P4/(32q B^8 D3).                                (2)

For F1 use a=eta,C_e=3/5. Nonnegativity gives K4<=m_L^2+m_R^2+(3/5)eta^-4 m_Lm_R. Average the two independent identical orbit tags, whose moments are m=eta^2 M(mu), U_edge=eta^4 U(mu). This yields F1. For smaller eigenvalue the two-edge experiment is a degradation of that at eta: retain the eta observation with probability lambda/eta, otherwise replace it by an independent marginal observation. Its likelihood is 1-lambda+3lambda p_i. Conditional Jensen for the convex fourth power gives U(nu_lambda)<=U(nu_eta); the right side of F1 already uses root-scale input moments and is unchanged.

For F2 use a=99/140,C_e=5a^4 on the larger radial rectangle above. Divide the resulting nonnegative gap by a^4 to obtain K4<=m_L^2+m_R^2+5m_Lm_R. Averaging the orbit tags proves F2. This step uses domain coverage, not a change in the actual edge eigenvalue.

## Exact signed cubic polynomials

Let T_y=sum_i f_i(y)^3 and T_z=sum_i f_i(z)^3. Define

    vnum_pi,i=6AB[t f_i(y)+s f_pi(i)(z)]
                 +3A^2ts f_i(y)f_pi(i)(z)-A^2 C_pi ts,
    v_pi,i=vnum_pi,i/(12B^2),
    Wnum_pi=sum_i vnum_pi,i^3,
    D2=product_pi Snum_pi^2.

The builders assert the zero-sum identity sum_i vnum_pi,i=0 as an exact polynomial identity. Formula (1) becomes K3=sum_pi Wnum_pi/(72B^2 Snum_pi^2). Set C_3=p/q=5/3. For sign epsilon in {+1,-1}, put

    P3_epsilon=[epsilon*18q A^3 B(T_y t^3+T_z s^3)
                   +9p A^4 Q_yQ_z t^2s^2]D2
                 -epsilon*2q B^2 sum_pi Wnum_pi D2_minus_pi.

Then exactly

    epsilon*(sum_i alpha_i^3+sum_i beta_i^3-K3)+C_3 m_Lm_R
         =P3_epsilon/(144q B^4 D2).                        (3)

Both signs are nonnegative on the full rectangle used for F2. Averaging gives C. No convexity assumption is made on the cubic statistic.

## All-domain certificate and independent restoration

Each raw builder asserts that every surviving monomial of P4 or P3 is divisible by t^2s^2. It divides by this monomial, replaces t=L*tau,s=R*sigma with the appropriate positive rational rectangle endpoints, clears the radial denominators by a single positive multiplier, and divides by positive coefficient gcd. The resulting polynomial H has the sign of the original gap away from t*s=0. At either zero radial coordinate the original gap is zero, so all boundaries are included.

The degree bounds (tau,sigma,y,z) and final tensor sizes are:

| Certificate | Degrees | Strictly positive integer Bernstein coefficients |
| --- | --- | --- |
| Fourth prefix | (20,20,22,22) | 233289 |
| Fourth generic fusion | (20,20,22,22) | 233289 |
| Cubic upper | (13,13,14,14) | 44100 |
| Cubic lower | (13,13,14,14) | 44100 |

For degree n, x^i=sum_(k>=i) [binom(k,i)/binom(n,i)] binom(n,k)x^k(1-x)^(n-k). Applying this identity in each coordinate produces a nonnegative tensor-product basis on the closed unit box. Positive integer lcm factors clear every coefficient denominator, and positive gcd divisions only rescale. All final coefficients are strictly positive by arbitrary-precision integer comparison. Thus these are entire-domain inequalities, with no floating-point step, numerical quadrature or truncation.

The builders are checks/ternary_fourth_certificate.py and checks/ternary_cubic_certificate.py. Run each --mode prefix|merge (fourth) or upper|lower (cubic), first --phase raw, then bern1,bern2,bern3,bern4. Every phase saves a checkpoint under checks/ternary_{fourth,cubic}_<mode>_<phase>.json. Largest file is under 50MB, and each phase has an estimated allocation below 500MB.

The separate checks/ternary_moment_independent_check.py imports no builders. It independently checks every stored axis transform by grouped slice dot products, every final integer sign, raw/Bernstein equality at five rational points and all 16 corners, and the original Bayesian gap at those five points for each certificate. It restores the exact radial denominator and raw gcd before comparing (2)/(3). Two invalid fourth constants and an invalid cubic constant produce negative exact gaps as controls. The report checks/ternary_moment_independent_check.json records SHA-256 hashes, restored gaps and PASS. These verification checks supplement the identities above; independent model audit remains pending.

NEXT: Apply F1,F2,C to a ternary BP fixed point, then supply a separately verified finite-depth entry bound.
