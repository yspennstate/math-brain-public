C0054 boundary attempt, w606, 2026-10-10

Result scope: an exact obstruction to a specified scalar fractional-moment route, with a sharp threshold for that route in an attenuated Gaussian model. This does not refute C0054 and does not prove fixed-width bulk localization or Poisson statistics. Novelty unverified. Independent referee: w608, pending.

Exact target and source are in STATEMENT.md. C0054-A001 tried fractional moments and left block decoupling open. Its assertion that band matrices have "no rank-one structure" is too broad: conditional on all other entries, changing H_xx changes the matrix by a rank-one operator. The problem is proving contraction, not the existence of scalar diagonal averaging.

Model for the proved lemmas: a finite simple graph of maximum degree K; independent H_xx = sigma X_x, X_x standard real Gaussian; independent upper-triangular hoppings H_xy = rho sigma Z_xy on graph edges, and zero elsewhere; lower entries are complex conjugates. In the complex case Z=(X+iY)/sqrt(2) for independent standard real Gaussians. In the real case Z is standard real Gaussian. All diagonal and upper-triangular variables are jointly independent. sigma>0, rho>0. Every principal submatrix uses the inherited variables. These assumptions define the lemmas, not the full survey conjecture.

L1. Exact scalar averaging and coefficient.
For 0<s<1,
  c_s = sup_{a in C} E |X-a|^{-s}
      = 2^{-s/2} Gamma((1-s)/2)/sqrt(pi).
The supremum is understood over finite integrals and is attained at a=0; restricting to Im a>0 has the same supremum by taking a=i eta down to zero. For complex hopping E|Z|^s=Gamma(1+s/2), so
  A_C(s)=2^{-s/2} Gamma((1-s)/2) Gamma(1+s/2)/sqrt(pi).
For real hopping E|Z|^s=2^{s/2} Gamma((1+s)/2)/sqrt(pi), so
  A_R(s)=sec(pi s/2).
The exact outgoing scalar coefficient per edge is w_s=rho^s A(s), independent of sigma.

Proof. Removing Im a only increases the integrand. For real a, write |X-a|^{-s} by layer cake as an integral of indicators of intervals centered at a. A centered interval maximizes Gaussian mass among its translates, because the Gaussian density is even and decreasing in |x|. Hence the maximum is a=0. Substituting t=x^2/2 in the Gaussian integral gives c_s. In the complex case |Z|^2 is exponential of mean one; integrate t^{s/2}e^{-t}. In the real case use the same substitution and the Gamma reflection identity. Scaling cancels sigma between inverse diagonal and hopping moments.

L2. Rigorous recursion, without multiplying correlated row bounds.
Let D be any induced finite subgraph and G_D(z)=(H_D-z)^{-1}, Im z>0. Set F_D(x,y)=E|G_D(x,y)|^s. For x != y,
  F_D(x,y) <= w_s sum_{u adjacent to x, u in D\{x}} F_{D\{x}}(u,y).
For x=y, F_D(x,x) <= c_s sigma^{-s}.

Proof. The Schur complement gives G_D(x,y)=-G_D(x,x) sum_u H_xu G_{D\{x}}(u,y), and G_D(x,x)=(H_xx-a)^{-1} for a=z+h G_{D\{x}} h*. First condition on the deleted minor and the whole hopping row. The diagonal variable H_xx is independent of these variables, so L1 applies even though a depends on the hopping row. Use |sum b_u|^s <= sum |b_u|^s. After diagonal integration, H_xu is independent of G_{D\{x}}, since the entire row and column x were removed. This gives the displayed recursion by the tower property. At every recursive step the same disjoint-variable argument holds for its new principal minor. No product of dependent conditional probabilities is used.

L3. No scalar contraction at equal scale.
For either symmetry class, A(s)>1 on 0<s<1. Consequently the maximum-degree scalar row-sum certificate K rho^s A(s)<1 fails at rho=1 whenever K>=1. The elementary nonbacktracking count (K-1)rho^s A(s)<1 also fails at rho=1 whenever K>=2. This is failure of these certificates, not a lower bound on the actual Green function.

Proof. In the real case sec(pi s/2)>1. In the complex case put a(s)=log A_C(s). Then a(0)=0,
  a'(0)=log(2)/2,
  a''(s)=[psi_1((1-s)/2)+psi_1(1+s/2)]/4 >0,
where psi_1(t)=sum_{n>=0}(n+t)^{-2} for t>0. Thus a(s)>s log(2)/2>0. The derivative at zero follows from Gamma duplication (psi(1/2)=psi(1)-2 log 2). The signs establish the obstruction for every s, not merely a sampled grid.

L4. Exact attenuation threshold of a scalar counting certificate.
Let B>=1 be its branching coefficient: B=K for row sums, or B=K-1 for elementary nonbacktracking counts when K>=2. Define a(s)=log A(s). The inequality B rho^s A(s)<1 has a solution 0<s<1 exactly when 0<rho<rho_crit(B).
If B>1, let s_B be the unique solution in (0,1) of
  s_B a'(s_B)-a(s_B)=log B.
Then rho_crit(B)=exp(-a'(s_B)). For B=1, rho_crit(1)=exp(-a'(0)), equal to 1/sqrt(2) in the complex case and 1 in the real case. At equality there is no strict contraction.

Proof. a is strictly convex, a(0)=0, and a'(s) tends to infinity as s tends to one. The function h(s)=s a'(s)-a(s) has derivative s a''(s)>0, starts at zero, and tends to infinity. This proves existence and uniqueness of s_B for B>1. Logarithmic contraction is log B+s log rho+a(s)<0, equivalently log rho<-[log B+a(s)]/s for some s. The quotient has derivative [h(s)-log B]/s^2, so its unique minimum is at s_B. For B=1, strict convexity gives a(s)/s>a'(0), with equality approached as s down to zero. Strict inequality in rho is therefore both necessary and sufficient. In the real case a(s)=-log cos(pi s/2), so the defining equation is theta tan theta+log cos theta=log B, theta=pi s_B/2.

L5. Positive special case: finite-volume fractional moments below the certificate threshold.
For K>=2 put r=(K-1)rho^s A(s). If r<1 then, for x != y and graph distance d=d(x,y),
  E|G_D(x,y;E+i eta)|^s
    <= c_s sigma^{-s} [K/(K-1)] r^d/(1-r)
for every finite induced D, every real E, and every eta>0. The estimate is uniform in the size of D and spectral parameter. At x=y use L2. In disconnected components the off-diagonal Green function is zero.

Proof. Iterate L2 until first reaching y or exhausting a branch. The deleted vertices forbid repeats, so every nonzero contribution is a self-avoiding path from x to y. Its terminal diagonal bound is c_s sigma^{-s} and its n edges contribute w_s^n by the recursion. For n>=1, the number of such paths is at most K(K-1)^{n-1}. Sum from n=d to infinity. This gives the displayed expression. The graph-distance bound translates to physical distance divided by the maximum edge length in a band model. Converting this finite-volume estimate to spectral/dynamical localization and deriving Poisson statistics are not claimed here.

Single hardest remaining parent gap: obtain a genuine multiscale or block fractional-moment contraction at rho=1 for every fixed W in the stated two-dimensional normalized band ensemble, uniform in growing volume and eta down to zero. L1 and L2 alone do not supply that contraction. Even after localization, Poisson statistics require a separate multiplicity/Minami-type argument and correct unfolding.

NEXT: Pin source/model assumptions; measure exact coefficient thresholds under a fresh resource gate; submit this proof packet to w608.
