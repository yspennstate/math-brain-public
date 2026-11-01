# Three-probe Loewner identification and stability

Author-derived conditional lemma, w399, 2026-10-10. Independently rederived and kept by w401 at these exact conditional scopes; see RECEIVED_W401_VERDICTS.jsonl. The exact Itô drift is classical; the explicit three-probe inversion and error constants are derived here, without a novelty claim. This is not a proof of the SAW scaling limit.

## Hypotheses

Let a chordal Loewner chain in H have continuous driver W, W_0=0, and half-plane capacity convention partial_t g_t(z)=2/(g_t(z)-W_t). Assume W is a continuous semimartingale with dW_t=mu_t dt+dN_t, where N is a continuous local martingale, d<N>_t=v_t dt, v_t>=0; all coefficients are locally integrable. Fix a constant alpha>0.

Take three compact vertical-slit obstacles A_i initially away from 0. Before any obstacle is hit, let h_(i,t) be the hydrodynamically normalized conformal map H minus g_t(A_i) to H. It is analytic by reflection near the current real driver and has h'_(i,t)(W_t)>0. Put M_(i,t)=[h'_(i,t)(W_t)]^alpha. Assume these three processes are local martingales on a common interval [0,tau), and the jet matrix J_t below is invertible for Lebesgue-a.e. t in that interval. Work with local stops where derivatives and coefficients are bounded; all identities then extend by localization.

Write u_i=h''_(i,t)(W_t)/h'_(i,t)(W_t), c_i=h'''_(i,t)(W_t)/h'_(i,t)(W_t), and J_t with rows (u_i,c_i,u_i^2). No probabilistic independence of probes is assumed.

## Exact drift derivation

The deterministic commuting-map equation, modulo an additive function of t which disappears on differentiation, is

partial_t h_t(z)=2 h'_t(W_t)^2/(h_t(z)-h_t(W_t))-2 h'_t(z)/(z-W_t).

Taylor expansion about W_t gives

partial_t h'_t(W_t)= h''_t(W_t)^2/[2h'_t(W_t)]-(4/3)h'''_t(W_t).

Applying Itô to the time-dependent analytic derivative at W_t, and then to its alpha-th power, yields

dM_i/M_i = alpha u_i dN + alpha [mu u_i +(v/2-4/3)c_i +(1+v(alpha-1))u_i^2/2] dt.

The time derivative here is at a fixed spatial argument before substituting W_t; the Itô term contributes (v/2)h'''. Reflection makes the derivatives real at W_t. Because the random conformal field is C^1 in time at a fixed spatial argument on the localized region, generalized Itô introduces no extra cross-variation terms. The quadratic-variation correction for taking the alpha-th power contributes alpha(alpha-1)v u_i^2/2. These give the displayed coefficients. This agrees with LSW Section 5, equations (5.2) and (5.4), PDF pages 19–20, when v is the constant kappa. The variable absolutely continuous variance rate is derived by Itô here, not asserted as the scope of their Proposition 5.2.

Define theta=(mu, v/2-4/3, [1+v(alpha-1)]/2). The three normalized drift densities are e=J_t theta. A local martingale has zero finite-variation density almost everywhere, so e=0. Invertibility gives theta=0, hence

mu_t=0, v_t=8/3, alpha=5/8

on that interval (the first two identities a.e.). If such intervals cover all finite times almost surely, Levy's characterization gives W=sqrt(8/3) B and the Loewner chain is chordal SLE(8/3). This global coverage is an explicit extra assumption, not a consequence of checking t=0.

## Concrete initial probes and local nondegeneracy

A(x,s) is the slit from x to x+i sqrt(s), x!=0, s>0. Its hydrodynamic map is x+sqrt((z-x)^2+s), with the branch asymptotic to z-x at infinity. Translation to fix 0 changes no derivatives. At z=0,

u=-s/[x(x^2+s)], c=-3s/(x^2+s)^2, u^2=s^2/[x^2(x^2+s)^2].

Use (x,s)=(1,1),(-1,1),(1,3). Then

J_0=[[-1/2,-3/4,1/4],[1/2,-3/4,1/4],[-3/4,-9/16,9/16]],

det J_0=9/32. Continuity of these jets before hitting implies a positive initial localization interval with nonzero determinant. That proves local nondegeneracy, not a global covering of times.

## Quantitative coefficient stability at this probe configuration

Suppose the normalized drift densities e_i have absolute value <=epsilon at a time with this matrix. Exact inversion gives

mu=-e_1+e_2,

v/2-4/3=-(5/3)e_1-(1/3)e_2+(8/9)e_3,

[1+v(alpha-1)]/2=-3e_1+e_2+(8/3)e_3.

Consequently |mu|<=2 epsilon, |v-8/3|<=(52/9)epsilon, and |1+v(alpha-1)|<=(40/3)epsilon. If additionally v>=v_min>0, then

|alpha-5/8| <= (31/(2 v_min)) epsilon.

For other configurations use the actual inverse: ||theta||_infinity <= ||J_t^(-1)||_infinity ||e||_infinity. If ||J_t-J_0||_infinity<=eta<3/20, the Neumann-series bound gives ||J_t^(-1)||_infinity <= (20/3)/(1-(20/3)eta). The norm is maximum absolute row sum, so the strict perturbation condition is material.

The residual is divided by alpha M_i. Small RAW relative drift dM_i/M_i is insufficient if exponents in an approximating sequence tend to zero. The continuum hypothesis requires one fixed positive limiting exponent; merely positive alpha_delta at each mesh does not establish that input. w400 independently highlighted this degeneracy in the adversarial hand check. This clarification changes no stated hypothesis or exact algebra bound.

## Why fewer probes can mislead

For the two symmetric slits (1,1),(-1,1), mu=0, v=14/3, alpha=29/14 gives both normalized drift densities zero at the initial configuration. The third slit gives e_3=9/8. This is a pointwise algebraic counterexample to identifying coefficients from those two initial tests; it does not claim these wrong coefficients make the first two processes martingales over an interval.

## P0003 scope and single hardest gap

Finite critical SAW provides exact bounded conditional obstacle martingales, but no proof here identifies their continuum limits with M_i, with a common alpha>0. Establishing that approximation uniformly in localized RANDOM slit domains is the single hardest missing input of this route. Also unproved: curve/driver tightness yielding continuous semimartingale drivers, and sufficient probe coverage to globalize the local identification. No complete SAW scaling-limit proof is claimed.
