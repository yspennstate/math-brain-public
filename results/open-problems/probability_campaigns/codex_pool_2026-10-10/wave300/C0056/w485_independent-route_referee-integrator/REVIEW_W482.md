# Direct referee verdict on w482 conditional entropy route — 2026-10-10

Artifact: `~/brain_workers/w482/ATTEMPT.md`, SHA256 `82F2C9CCDAD841F252B2527007986EA6F5DC1F651D24B39AEA8363FA57EE786D`.

**Verdict: KEEP the conditional implication; do not promote (LG) or C0056.**

1. With `f(v)=b/[pi((lambda v-a)^2+b^2)]`, substitute `t=(lambda v-a)/b`, `c=1/(pi b)`. Then `f(v)dv=dt/[pi lambda(1+t^2)]`. For `I(c)=int log(1+c/(1+t^2))/(1+t^2)dt`, differentiation gives `I'(c)=pi/c(1-1/sqrt(1+c))`, so `I(c)=2pi log((1+sqrt(1+c))/2)`. The paper's displayed full-line entropy identity follows. The uniform[-1,1] conditional expectation is half an integral over [-1,1], so its upper bound is `<= [1/(2lambda)] log(1+1/b)` as claimed.
2. Under (LG), `Phi(u)=u log(1+u)` has bounded integral over the finite measure space `Omega x J`. The spectral theorem also gives `E int_J u_eta <=1`. Since Phi is superlinear, de la Vallee Poussin yields uniform integrability. Dunford-Pettis supplies a weakly convergent subsequence in `L1(Omega x J)` with nonnegative limit `F`.
3. For every bounded measurable `h(Omega)` and `phi in C_c(J)`, weak `L1` convergence pairs against `h phi`; pathwise, `int phi u_eta dE = int (P_eta*phi)dmu_x -> int phi dmu_x` because `P_eta*phi -> phi` uniformly. The pairings are bounded by `||h||_infty ||phi||_infty`, so dominated convergence applies. Equality against all bounded `h` identifies `int phi F_x dE = int phi dmu_x` almost surely. Choose a countable determining family of test functions and intersect its full-probability events. This proves `mu_x|J=F_x dE` almost surely. Countably many sites give operator-level pure a.c. on J.
4. For sufficiently small lambda, the separate nonzero-window step is valid: `||H_lambda-H_0||<=lambda` uniformly in the bounded uniform potential, and a nonnegative continuous test function supported in any nonempty `J subset (-6,6)` has strictly positive free local expectation. Norm-continuity of bounded continuous functional calculus preserves positivity at small lambda.

**Unresolved:** (LG) is a uniform expected `int_J log(1+1/b_x(E,eta))dE` bound at *fixed positive lambda* as `eta down to zero` for the infinite-volume lattice cavity. No step in the packet proves it. It is not implied by own-site spectral averaging or by the exact entropy integral. GOE remains a separate target. This is a check of w482's primary argument, not of any other review.

NEXT: Route this verdict to w482 and integration contact. Keep (LG) as an explicit hypothesis in any draft node.
