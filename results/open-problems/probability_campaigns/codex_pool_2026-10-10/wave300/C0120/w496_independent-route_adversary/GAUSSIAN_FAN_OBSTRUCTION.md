# A convex Gaussian path maximum with only a logarithmic variance gain

Independently derived by w496, 2026-10-10. This graph is not Z^2. Its root degree grows with n. The result is a control on geometry-free inference, not a counterexample to C0120.

For each n, take a root and n disjoint branches containing n-1 vertices apiece. A permitted path starts at the root and follows one whole branch, so it has n vertices. All vertex weights are independent standard Gaussians. Put S_j=sum_{t=1}^{n-1}g_{t,j}, G_j=S_j/sqrt(n-1), and

    M_n^fan=g_0+sqrt(n-1) max_{1<=j<=n} G_j.

This is a maximum of Gaussian path sums. It is convex, globally sqrt(n)-Lipschitz, with nonnegative path-indicator gradient, and sum_v (D_v M_n^fan)^2=n almost surely. Each path selects exactly one vertex in each layer, and pairwise path-energy covariance is the intersection size.

## Quantitative lower bound

Let m=n and choose b=b_m with Q(b)=P(G>b)=1/m. For sufficiently large m, b>=1. Gaussian integration by parts gives the elementary Mills bounds

    b phi(b)/(b^2+1) <= Q(b) <= phi(b)/b.

For q=b+1/b, dividing the lower bound at q by the upper bound at b gives

    Q(q)/Q(b) >= [b q/(q^2+1)] exp(-(q^2-b^2)/2)
               >= (2/5) exp(-3/2) =: c_0 > 0.

Indeed bq=b^2+1, q^2+1=b^2+3+b^(-2), and for b>=1 their ratio is >=2/5. Hence, for X_m=max_j G_j,

    P(X_m<=b)=(1-1/m)^m>=1/4,
    P(X_m>=q)>=1-exp(-m Q(q))>=1-exp(-c_0)=:r_0>0.

For an independent X_m', Var(X_m)=E[(X_m-X_m')^2]/2. The two opposite events at these levels imply

    Var(X_m)>=r_0/(4 b^2).

Since Q(b)<=exp(-b^2/2) and Q(b)=1/m, b^2<=2 log m. Therefore

    Var(M_n^fan)>=1+(n-1) r_0/(8 log n).

For every fixed delta>0 this rules out Var(M_n^fan)<=C_delta n^(1-delta) uniformly in n. No asymptotic normal-maximum variance theorem or moment-convergence assumption is needed.

## Qualitative Gaussian chaos still holds

For fixed u>0 put rho=e^(-u)<1, G_j^u=rho G_j+sqrt(1-rho^2)G_j', I=argmax G, I_u=argmax G^u. Then

    E|P_n intersect P_n^u| = 1+(n-1) P(I=I_u).

Choose alpha in ((1+rho)/2,1) and a=sqrt(2 alpha log m). A union bound yields

    P(I=I_u)<=2 P(X_m<a)+m P(G_1>=a,G_1^u>=a)
              <=2 exp(-m Q(a))+m^(1-2 alpha/(1+rho)).

The bivariate bound follows from G_1+G_1^u being Gaussian of variance 2(1+rho), followed by the elementary exponential tail bound. Mills' lower bound gives m Q(a)>=c_alpha m^(1-alpha)/sqrt(log m)->infinity. Thus P(I=I_u)->0 for every fixed u>0, and the normalized expected path overlap tends to zero.

This can be made a vanishing-noise assertion without a nonuniform limit swap. Choose u_m=16 log(log m)/log m and alpha_m=(3+rho_m)/4 for sufficiently large m. Then (1-rho_m) log m ~ 16 log(log m), and the two bounds above tend to zero: the first has m Q(a_m) growing as (log m)^(7/2+o(1)), and the second is (log m)^(-4+o(1)). Therefore overlap/n tends to zero at u_n->0 while the variance has no power improvement.

The precise missing premise for any argument based only on qualitative chaos, convexity, Gaussianity, one-vertex-per-layer gradients and Dirichlet energy n is a quantitative rate exploiting the fixed lattice geometry. These structural facts alone are insufficient.

Review state: independent check from w497 pending. This proof is not a novelty claim and does not settle the lattice problem.
