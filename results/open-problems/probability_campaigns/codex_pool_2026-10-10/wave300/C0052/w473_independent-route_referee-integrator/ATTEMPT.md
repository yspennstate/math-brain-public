# C0052 independent attempt and referee result

## Source target

Duminil-Copin's 2017 Conjecture 6 asks for non-triviality of the 3D Ising model. Equations (7.1)-(7.2) operationalize this as nonvanishing, as beta increases to beta_c from below, of the spatially summed four-point Ursell function divided by chi(beta)^2 xi(beta)^3. The source's g is nonpositive; below g_+=-g. This is a near-critical infinite-volume statement. No current-open or novelty claim is certified.

## Independent route recorded first

ROUTE_PRECOMMIT.md was saved before peer proofs were opened. I chose Lee-Yang zeros of a finite ferromagnetic Ising magnetization, rather than the intake's random-current intersection second moment. If rho_1 is the first positive imaginary MGF zero and V the variance, zero factorization gives

    12/(rho_1 sqrt(V))^4 <= -kappa4(M)/V^2 <= 6/(rho_1 sqrt(V))^2.

This is an exact conditional finite-volume lemma, independently derived in CLAIMS.jsonl. It does not by itself meet the source's infinite-volume near-critical normalization. W471 and w472 independently chose the same zero method, and w471's L2 supplies a valid conditional bridge to g_+; REVIEW_PACKET.md rederives that step. My own lemma is redundant with w471 L1 and awaits w476 review before any independent promotion.

## Hardest open step

For the actual infinite-volume Gibbs marginal over the selected block Lambda(beta)=[-2R,2R]^3 with R=max(1,ceil(xi), susceptibility-half-mass radius), show that r(beta)=rho_1(beta) sqrt(Var(S_Lambda)) stays bounded on a beta-to-beta_c subsequence. W471's checked inequality g_+(beta)>=3/r(beta)^4 would then establish nonvanishing. Lee-Yang locates zeros but provides no such upper bound. Independent spins provide an exact failed closure: r grows as sqrt(N) and the fourth-moment deficit is 2/N.

## Source and attempt boundary

The 2026-09-07 intake C0052-A001 uses a random-current intersection heuristic and explicitly lacks a variance estimate. Its cluster-dimension exponent is not an established input here. Targeted searches of the named H/I attempts returned no exact C0052 hit, and the Lean annotated ranking contains only the dated title/status. Team O's board did not list C0052. The math-brain export contains the dated C0052 problem node with current status unverified. Public searches found the 2017 source, a 2021 4D triviality theorem, and numerical/bootstrap 3D studies, but no verified rigorous 3D closure; current openness remains UNKNOWN.

## Next proof step

Try to bound the block's first normalized Lee-Yang zero by a 3D-specific multi-scale inequality, with hypotheses sufficient for the actual Gibbs marginal. A bound for an isolated finite-volume box, an unnormalized zero, or a numerical model would not close the source target without a separate comparison.
