# P0177: a global free Brownian mode under finite variance

Label: proof (worker checked), independent audit pending w346. No novelty or full-problem solution certificate. The mode here means the global maximizer of the canonical continuous density.

Let X have mean m and finite variance sigma^2, and let mu_t be its law freely convolved with a semicircle law of variance t. If sigma=0, mu_t is a semicircle centered at m and the assertions below hold directly. Assume sigma>0. Put

    B=(sqrt(2)+2)sigma,
    A=B^2+sigma^2=(7+4sqrt(2))sigma^2,
    T=1024 A.

For every t>=T, mu_t has a unique global mode. That mode tends to m as t tends to infinity. If E|X-m|^3<infinity, putting M3=E|X-m|^3 and K=A(B+sigma)+4(B^3+M3), its location M(t) satisfies the explicit estimate |M(t)-m|<=36 K/t for t>=T. If E|X-m|^7<infinity, then

    M(t)=m-3mu_3/t+(5mu_5-22mu_2mu_3)/t^2+O_mu(t^-3),

where mu_k=E[(X-m)^k]. The threshold is a proved sufficient bound, with no optimal transition location claimed. An exponential quadratic moment, as in the original classical question, implies the required seventh moment.

Use the general Biane parametrization from Hasebe-Ueda, ALEA 15 (2018), equations (2.10), (2.13), (2.14). With w_t(u)=v_t(u)^2>0, it reads E[1/((u-X)^2+w_t(u))]=1/t, the density at psi_t(u) is sqrt(w_t(u))/(pi t), and psi_t is a homeomorphism. Hence global density maxima correspond exactly to global maxima of w_t. The function v_t is continuous and tends to zero at both infinities: for any a>0, E[1/((u-X)^2+a)] tends to zero as |u| tends to infinity by dominated convergence, forcing w_t(u)<a eventually. Thus a positive global maximum is attained.

Jensen's inequality gives w_t(m)>=t-sigma^2 when t>sigma^2. Indeed, at w=t-sigma^2 the reciprocal expectation is at least 1/t, and the expectation is strictly decreasing in positive w. Every positive solution also has w_t(u)<=t. Let u_* be any global maximizer and w_*=w_t(u_*). Then w_*>=t-sigma^2 and

    E[(u_*-X)^2/(w_*+(u_*-X)^2)]=1-w_*/t<=sigma^2/t.

Chebyshev gives P(|X-m|<=sqrt(2)sigma)>=1/2. If r=|u_*-m|-sqrt(2)sigma>0, the last expectation is at least (1/2)r^2/(t+r^2). For t>=4sigma^2 this implies r^2<=2sigma^2 t/(t-2sigma^2)<=4sigma^2. Consequently every global maximizer lies in I=[m-B,m+B].

For every u in I and t>=T, Jensen similarly yields t-A<=w_t(u)<=t. Set epsilon=1/t, r_t(u)=w_t(u)/t, d=r_t(u)+epsilon(u-X)^2, and

    C2=E[d^-2], J=E[(u-X)d^-2].

The positive implicit solution is smooth in u and r_t'(u)=-2epsilon J/C2. Its stationary points have J=0. Differentiating J along this solution gives

    J'=C2-4epsilon E[(u-X)^2 d^-3]-2r_t'(u)E[(u-X)d^-3].

Uniformly on I, E[(u-X)^2]<=A, r_t>=1-epsilon A>=1/2, C2>=(1+epsilon A)^-2>=1-2epsilon A, and |J|<=4E|u-X|. For epsilon A<=1/2, |r_t'|<=18epsilon E|u-X|, so the magnitude of the final term is at most 288epsilon A; the middle term is at most 32epsilon A. Thus J'>=1-322epsilon A>0 for t>=1024A. At least one global maximizer exists inside I, is a positive interior stationary point of w_t, and therefore has J=0. Strict increase of J permits only one such point. This proves eventual uniqueness of the global density maximizer without a compact-support or unimodality assumption.

As t tends to infinity, r_t->1 uniformly on I. The functions J(u) tend uniformly to u-m: split the integral at a bounded |X-m|, use uniform convergence on the bounded part, and dominate the tail by a constant times |X-m|+B. Its unique zero u_t therefore tends to m. The same truncation argument gives E[(u_t-X)/d]->u_t-m, so psi_t(u_t)=u_t+E[(u_t-X)/d]->m.

If M3 is finite, |d^-2-1|<=16|d-1| and |d^-1-1|<=4|d-1| because d>=1/2. With E|u-X|<=B+sigma and E|u-X|^3<=4(B^3+M3), the equation J=0 yields |u_t-m|<=16epsilon K. The spatial map then yields |psi_t(u_t)-m|<=2(16epsilon K)+4epsilon K=36K/t. All constants and hypotheses are explicit.

For the second-order expansion, translate m to zero and work with F(epsilon,u,r)=E[1/(r+epsilon(u-X)^2)]-1 and J(epsilon,u,r)=E[(u-X)/(r+epsilon(u-X)^2)^2]. Finite seventh absolute moment makes these functions C^3 up to epsilon=0 from epsilon>=0, for u near zero and r near one. Every derivative of total order at most three is dominated by a constant times 1+|X|^7 when r>=1/2. To use the ordinary C^3 implicit-function theorem, extend to epsilon<0 using the degree-three Taylor polynomial in epsilon at zero, with its smooth u,r-dependent coefficients; this matches all partial derivatives through order three at zero. No reciprocal expectation at negative epsilon is used. The Jacobian with respect to (u,r) at (epsilon,u,r)=(0,0,1) is [[0,-1],[1,0]], hence invertible. The resulting C^3 branch has a Taylor expansion with O(epsilon^3) remainder and is the unique global-maximizer branch already identified above.

Writing r=1+c1 epsilon+c2 epsilon^2+O(epsilon^3) and u=a1 epsilon+a2 epsilon^2+O(epsilon^3), direct expansion gives c1=-mu2, c2=mu4-mu2^2, a1=-2mu3, a2=3mu5-14mu2mu3. Inserting into psi=u+E[(u-X)/(r+epsilon(u-X)^2)] gives -3mu3 epsilon+(5mu5-22mu2mu3)epsilon^2+O(epsilon^3). Translation back yields the displayed formula.

Checks requiring the auditor's attention: global existence of a maximum for an unbounded initial law; the Chebyshev interval; the uniform derivative constants; the sign of r_t'; positivity of w on the entire interval; the one-sided C^3 extension rather than an unjustified analytic continuation; variance normalization; and the distinction between a unique global maximizer and the number of local density peaks.
