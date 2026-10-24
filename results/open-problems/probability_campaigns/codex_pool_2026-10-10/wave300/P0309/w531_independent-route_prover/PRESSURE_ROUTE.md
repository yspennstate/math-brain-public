# Main independent route: a bounded periodic source and a pressure cusp

2026-10-10, w531. This replaces the historical phonon mechanism as the main independent route. Complete conditional lemmas follow. No positive pressure slope has been proved for a Riesz gas, and no novelty claim is made. Review requested: w533.

## P1. Exact finite-volume identities for the unlabelled gas

Fix finite s>3, beta>0, mu in R, and an invertible 3 by 3 matrix A whose Gram matrix A^T A has equal diagonal entries a and equal off-diagonal entries b, with a-b>0 and a+2b>0. Put Lambda=A Z^3, v=|det A|, and K_j=2pi A^{-T} e_j, j=1,2,3. This Gram condition makes permutations of the three primitive basis vectors Euclidean isometries; it includes standard primitive bases for BCC and FCC after scaling. It does not assert that either lattice is a ground state.

On the torus R^3/(N Lambda), N a positive integer, use the repulsive periodized potential

W_N(r)=sum_{m in Z^3} |r+N A m|^(-s),

with value infinity at a coincident pair modulo the torus. For noncoincident points the series converges because s>3. Let E_N(x_1,...,x_n)=sum_{i<j} W_N(x_i-x_j). A nonnegative, particle-number-proportional self-image constant could be added, but it is not used here. Define

Psi(x)=sum_{j=1}^3 cos(K_j dot x),
Q(x_1,...,x_n)=sum_i Psi(x_i),
Z_N(h)=sum_{n>=0} [1/n!] integral_{torus^n} exp[beta mu n-beta E_N+beta h Q] dx_1...dx_n,
p_N(h)=[1/(beta N^3 v)] log Z_N(h).

For every real h, Z_N(h) is finite and positive: 1<=Z_N(h)<=exp(N^3 v exp(beta(mu+3|h|))). On any bounded h interval the Poisson exponential series dominates derivatives of every order. Hence p_N is differentiable (indeed real analytic), and

p_N'(h)=(N^3 v)^(-1) E_N,h Q,
p_N''(h)=beta (N^3 v)^(-1) Var_N,h Q>=0.

Translation by t_*=A(1/2,1/2,1/2) changes Psi to -Psi and leaves E_N and Lebesgue measure invariant, proving p_N(h)=p_N(-h). In particular p_N'(0)=0 at every finite N. This does not determine the one-sided derivative of a limiting pressure.

For any k distinct insertion positions, the factorial correlation density obeys

rho_N,h^(k)(x_1,...,x_k) <= exp[k beta(mu+3|h|)].

Proof. Extract these k particles from the grand-canonical series. Their mutual and exterior interaction energies are nonnegative, so deleting all energies incident to them increases each integrand. The remaining grand-canonical series is at most Z_N(h), which cancels the denominator. Their activities are at most exp(beta(mu+3|h|)) each. This proves the bound with no assumption about independence.

## P2. Pressure cusp extracts three nonzero Fourier coefficients

Additional hypotheses: p_N(h) converges to a finite p(h) on an interval around 0; and there exists m=p'_+(0)>0. The first assumption is a thermodynamic pressure hypothesis, not a proved crystallization estimate. Convexity and evenness pass to p. The density bound above makes p locally Lipschitz, so m is finite. Evenness gives p'_-(0)=-m: a positive right slope is a cusp.

Choose h_l down to 0 with h_l>0. Choose increasing N_l so that

|p_N_l(h_l)-p(h_l)| + |p_N_l(0)-p(0)| <= h_l/l.

Such a diagonal exists by convergence at each of the two fixed arguments. Convexity gives

p_N_l'(h_l) >= [p_N_l(h_l)-p_N_l(0)]/h_l
             >= [p(h_l)-p(0)]/h_l - 1/l,

so liminf_l p_N_l'(h_l)>=m. This is a volume-first selection; an arbitrary h(N) does not follow from pressure convergence.

View each torus law locally by periodically lifting the point configuration. Any fixed bounded observation window injects into the torus for all sufficiently large N, so the k=1,2 factorial density bounds apply there. They give uniformly bounded local second moments, tight local counts, and a uniform small-distance bound for pairs. Thus local subsequential point-process limits exist and are simple and locally finite. Their expected intensities are absolutely continuous and locally bounded, so fixed cell boundaries carry no expected mass. The second-moment bound implies uniform integrability of one-cell counts.

Let P be a local subsequential limit along this diagonal and lambda=E_P eta its intensity measure. All finite laws are invariant under Lambda-translations, basis permutations, and inversion x->-x. These symmetries pass to the local limit. For a centered half-open fundamental cell F, define

c_j = v^(-1) integral_F exp(-iK_j dot x) lambda(dx).

Inversion makes each c_j real; primitive-basis permutation symmetry makes c_1=c_2=c_3. For the finite torus law, lattice periodicity and tiling imply

p_N'(h)=sum_{j=1}^3 [v^(-1) integral_F cos(K_j dot x) lambda_N,h(dx)].

Local convergence, boundary-nullness, and uniform integrability pass these cell expectations to the limit. Therefore 3c_j>=m>0 for each j.

If lambda is invariant under translation t, its nonzero coefficient c_j must equal exp(-iK_j dot t)c_j. Thus K_j dot t belongs to 2pi Z for every j, equivalently A^{-1}t in Z^3. Conversely lambda is Lambda-periodic. Its group of translation periods is therefore EXACTLY Lambda. This distinguishes a full-rank periodic mean intensity from a single-mode witness that could still allow continuous transverse translations.

Conditional Gibbs conclusion: IF this local limit P satisfies the zero-field Riesz DLR specification in STATEMENT_FOR_ADVERSARY.md, then it is a lattice-periodic zero-field Gibbs law breaking continuous translations. Translation covariance gives distinct translated Gibbs laws for the same beta,mu,s. Gibbs membership is an explicit additional hypothesis of this implication. Tightness or a nonzero Fourier coefficient alone does not prove it. No claim is made about extremality, classification of every Gibbs state, the optimal lattice, Coulomb renormalization, or a numerical critical temperature.

## P3. Positive pinned response does not imply a cusp

This obstruction is exact. For V independent fair signs sigma_i, define Z_V^ind(h)=(2 cosh(beta h))^V. Its pressure is p^ind(h)=beta^(-1)log(2cosh(beta h)), with positive derivative tanh(beta h) at every h>0, but p'_+(0)=0. Inferring spontaneous order merely from positive pinned response is false.

For a distinct two-state system whose only states have total order parameter +/-V, Z_V^coll(h)=2cosh(beta V h). Its pressure tends to |h|, so p'_+(0)=1, although every finite-volume derivative at 0 is zero. The diagonal h_V=1/(beta V^2) has derivative tanh(1/V)->0; h_V=1/sqrt(V) has derivative tanh(beta sqrt(V))->1. These examples verify why the cusp estimate and the volume-first selection are genuine proof obligations. They are toy models, not Riesz gases or independent audits.

## P4. A relative-entropy witness would close the pressure-slope estimate

Let G_N,0 be the zero-source law in P1, V_N=N^3 v, and T_N,h a trial on the SAME unlabelled configuration space, absolutely continuous with respect to G_N,0, with finite relative entropy D(T_N,h || G_N,0) and E_T |Q|<infinity. For h>0,

p_N(h)-p_N(0) >= h E_T Q/V_N - D(T_N,h || G_N,0)/(beta V_N).

Proof. The source density is dG_N,h/dG_N,0=exp(beta h Q) Z_N(0)/Z_N(h). Consequently

D(T || G_N,h) = D(T || G_N,0)-beta h E_T Q+beta V_N[p_N(h)-p_N(0)] >= 0.

Rearrange. The two finiteness assumptions justify this identity. Source and zero-source laws have the same support. No factorization of the trial is used. A law concentrated on deterministic lattice positions is singular and is not an admissible finite-entropy trial.

Suppose the pressure convergence in P2 holds. If for all sufficiently small h>0,

liminf_N E_T_N,h Q/V_N >= q>0,
limsup_N D(T_N,h || G_N,0)/(beta V_N h) <= epsilon(h),
epsilon(h)->0 as h down to zero,

then [p(h)-p(0)]/h>=q-epsilon(h) and p'_+(0)>=q>0. The geometric and Gibbs-limit conditions of P2 would then give its phase conclusion. This is a conditional certificate, not an entropy estimate obtained for a Riesz gas.

An exact special case is T_N=G_N,0 conditioned on an event B_N with Q>=q V_N and -log G_N,0(B_N)=o(V_N). Its entropy is -log G_N,0(B_N), giving p(h)-p(0)>=hq after N tends to infinity at fixed h. No such nonexponentially rare crystalline sector has been established. If D/(beta V_N) instead retains a positive cost c, the bound hq-c is ineffective as h down to zero. A fixed free-energy approximation error cannot establish the cusp; the required error scale is o(h) per volume.

## The missing estimate for P0309

Single hardest open piece in this route: for a physically appropriate A, beta,mu,s prove a strict linear zero-source pressure increase

lim_{h down to 0} [p(h)-p(0)]/h > 0

for the FULL unlabelled Riesz gas. No such inequality is established here. A proposed energy argument must compare the unrestricted partition function with and without the source, including defects, entropy, competing arrangements, and long-range effects if s<=3. Reference phonon variance or a favourable crystalline subset in Z cannot give an upper bound on the unrestricted competing phases. The zero-field DLR-limit condition must also be verified; it is separated as a named condition rather than hidden in the pressure argument.

Next concrete proof step: construct absolutely continuous unlabelled ordered trials with relative-entropy cost o(h) per volume, controlling competing configurations through the actual zero-field Gibbs denominator. A fixed positive free-energy error, a bound of order h^2, or a nonzero response at fixed h will not close the gap.
