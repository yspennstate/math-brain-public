Independent phase started 2026-10-10 before reading w465's ATTEMPT.md or proof artifacts.

Target: nearest-neighbor ferromagnetic q-state Potts on Z^d for every integer q>=3 and d>=3. Recover the exact definition of discontinuity before equating it with latent heat or Gibbs-state nonuniqueness.

The independent route to audit is transfer of a first-order mean-field transition through a bounded approximation to the lattice free energy. The crucial missing premise is quantitative separation of the mean-field phases exceeding the allowed approximation error in the actual dimension. Uniformly small free-energy error, by itself, does not transfer a kink or a jump. A smooth convex approximation to a kink is a direct candidate obstruction; derive it separately and record the size of its error before inspecting the prover.

Primary partial theorem: Biskup-Chayes (2003), https://arxiv.org/abs/math/0207242, requires sufficiently large dimension or sufficiently strong mean-field first-order transition. Its small-error hypothesis must be checked rather than replaced by d>=3.

Hardest open piece: establish a positive critical order parameter for the actual nearest-neighbor lattice in the uncovered low-dimensional/small-q regime; a mean-field calculation alone does not do this.

Independent obstruction (saved before reading w465's proof): for every epsilon>0 set P(x)=max(0,x) and P_epsilon(x)=epsilon log(1+exp(x/epsilon)). For x>=0, subtract x; for x<=0, use P(x)=0. In both cases 0<P_epsilon(x)-P(x)<=epsilon log(2), uniformly for all real x. But P_epsilon'(x)=1/(1+exp(-x/epsilon)) is smooth and P_epsilon''(x)>0. Thus convexity plus an arbitrarily small uniform pressure error does not preserve a derivative jump. This is an elementary separately derived functional counterexample, not a counterexample to the Potts conjecture. An additional constrained-free-energy barrier or exclusion of intermediate order parameters is needed for that method.

Exact formulation recovered from Duminil-Copin's lectures, printed pp. 4-5 and 93: the source uses unit simplex spins with dot product 1 on equality and -1/(q-1) otherwise; discontinuity means positive monochromatic-boundary spontaneous magnetization at beta_c. In the equivalent standard color Hamiltonian H=-sum_edges 1{sigma_x=sigma_y}, use K=beta*q/(q-1), and FK p=1-exp(-K). Define M(K)=(q*mu_K^1(sigma_0=1)-1)/(q-1). Then C0048 asks M(K_c)>0 for every integer d>=3,q>=3. Via Edwards-Sokal this is phi^wired_{p_c,q}(0<->infinity)>0. Pressure differentiability/latent heat is a distinct observable and must not silently replace this target.

The exact quantitative derivation is in quantitative_obstruction.md. The checked saddle excess is 0.001129252781529618..., and the cited allowance is at least 0.308065413582197915..., a ratio of 272.8046533. The bound contains the factor n=q-1, and the state must be an extreme thermodynamic support pair. This calculation excludes one proposed direct proof route using that allowance; it does not exclude a sharper estimate or a different route.

After saving the independent work, I inspected w465's local-witness L1-L3. PEER_AUDIT.md gives independently derived conditional proofs and the exact endpoint-wired path stress example. The stated lemmas pass the scoped audit. The missing positive critical witness is acknowledged by the prover; no broken step or solution claim was invented. A finite-volume positive boundary gap is insufficient because the exact path example has rho_N>0 for every N and rho_N->0 exponentially.

The math-brain's exact C0048 problem and prior attempt cards were fetched read-only and compared with the intake and primary statement. Broad keyword results included spin-glass cards, whose graph/model, high-temperature regime and observable do not match the proof need. RETRIEVAL_FAILURE.md and measurement_retrieval.json record the bounded diagnostic and proposed scope repair. No population-wide recall/model load was performed.

Independent referee and response-side different-model gates remain pending; all proposed nodes are concept/DRAFT material. No formal proof or current-openness certificate is claimed.

NEXT: Establish, for each fixed integer q>=3,d>=3, a fixed finite critical cylinder witness with a positive volume-uniform gap, or obtain a sharper direct critical-magnetization estimate.
