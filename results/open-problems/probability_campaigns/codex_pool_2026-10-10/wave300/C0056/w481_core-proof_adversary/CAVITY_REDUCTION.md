# Independent cavity reduction and the still-missing estimate

2026-10-10, w481. Independently derived before reading w480's proof. This is a standard conditional proof route, with a complete proof of its reduction, not a proof of C0056 or a novelty claim. Independent reviewer: w482, pending.

Fix lambda>0. Let H=A+lambda V on l^2(Z^3), with nearest-neighbor hopping A of either sign and iid V_x uniform on [-1,1]. Fix a bounded nonempty open interval I. Remove site 0, obtaining H^(0). Let h be its vector of six hopping coefficients to the origin, so ||h||^2=6. For z=E+i eta put

S(z)=<h,(H^(0)-z)^(-1)h>, a(z)=E+Re S(z), b(z)=eta+Im S(z)>0.

The input M below is NOT established:

M: For this fixed lambda and interval I, there exists eta_n decreasing to zero such that Q = sup_n integral_I E[b(E+i eta_n)^(-1)] dE < infinity.

No constant is required to be uniform as lambda decreases to zero. The eta limit is at fixed positive lambda.

## Reduction: M implies purely absolutely continuous spectrum on I

Conditional on all potentials except V_0, the Schur complement gives

G_00(z)=1/(lambda V_0-z-S(z)); Im G_00(z)=b/((lambda V_0-a)^2+b^2).

V_0 is independent of H^(0), hence of a and b. Write q=Im G_00. Direct integration over the independent single site gives

E[q^2 | H^(0)]
 = (1/(2 lambda)) integral_{-lambda}^{lambda} b^2/((u-a)^2+b^2)^2 du
 <= pi/(4 lambda b).

The whole-line integral used here is pi/(2b), obtained by substituting t=(u-a)/b and integrating (1+t^2)^(-2). Thus M implies sup_n E integral_I q(E+i eta_n)^2 dE <= pi Q/(4 lambda).

Here is the required spectral criterion with the limit justified. Let mu be any finite positive spectral measure and q_eta(E)=integral eta/((t-E)^2+eta^2) mu(dt). Put L=liminf_n integral_I q_eta_n^2. If L is finite, select a subsequence whose squared norms tend to L. For every real phi in C_c(I), the Poisson approximate-identity formula yields

integral phi dmu = lim_n (1/pi) integral_I phi(E) q_eta_n(E) dE.

Along the selected subsequence, Cauchy-Schwarz implies |integral phi dmu| <= sqrt(L)/pi * ||phi||_2. This linear functional extends continuously from C_c(I) to L^2(I). The Riesz representation theorem gives a density rho in L^2(I); equality on C_c(I) identifies mu restricted to I with rho dE, and ||rho||_2^2 <= L/pi^2. There is no exchange of the omega and eta limits here.

Apply Fatou to the random nonnegative squared norms. E[L] <= liminf_n E integral_I q_eta_n^2 <= pi Q/(4 lambda), so L is finite almost surely and E||rho_0||_2^2 <= Q/(4 pi lambda). Translation invariance gives the same conclusion at each site. Intersect the countably many probability-one events. For a Lebesgue-null Borel B contained in I, ||chi_B(H)delta_x||^2=mu_x(B)=0 at every site. Completeness of the site basis implies chi_B(H)=0. This proves pure absolute continuity of the spectral restriction on I, subject to M.

Nonzero weight is a separate condition. To conclude extended states, also require chi_I(H) != 0. For I inside the free band, this follows from the standard iid rare-box Weyl-sequence argument when the single-site support contains 0. It is not an implication of the L^2 criterion alone. No GOE eigenvalue-statistics conclusion follows from this reduction.

## Why the existing elementary estimates do not establish M

Single-site spectral averaging gives E[q | H^(0)] <= pi/(2 lambda), regardless of how small b is. It therefore supplies no inverse-b moment. INDEPENDENT_OBSTRUCTION.md gives a pure-point operator satisfying exactly such a uniform first-moment bound.

A deterministic resolvent comparison with the free cavity gives

|S_lambda(z)-S_0(z)| <= ||h||^2 ||R_lambda^(0)(z)|| ||lambda V|| ||R_0^(0)(z)|| <= 6 lambda/eta^2.

This estimate follows from the resolvent identity, bounded |V_x|<=1, and ||R(z)||<=1/eta. It cannot retain a positive free damping bound uniformly as eta decreases to zero at fixed lambda. A condition coupling lambda to eta would address a different limit.

The cavity is one connected lattice with shared potentials. Its six neighbor contributions and off-diagonal terms are not independent branches. No product of per-neighbor probabilities or tree recursion has been used.

## Necessary control on resonances for this particular L^2 route

On the event R={|a|<=lambda/2, b<=lambda/2}, the interval [a-b,a+b] is inside [-lambda,lambda]. On that interval q>=1/(2b), and therefore

E[q^2 | H^(0)] >= 1_R/(4 lambda b).

A uniform integrated second-moment bound thus necessarily controls E[b^(-1) 1_R]. M controls b^(-1) without that restriction and is sufficient, not claimed necessary for absolute continuity or for every possible proof route. The exact bottleneck in this route is a resonant small-damping estimate for the correlated lattice cavity at fixed nonzero disorder.

NEXT: Audit the paired lemma's substitute for this input; reject any replacement by first moments, a tree independence assumption, or a weak-coupling limit taken before the eta boundary limit.
