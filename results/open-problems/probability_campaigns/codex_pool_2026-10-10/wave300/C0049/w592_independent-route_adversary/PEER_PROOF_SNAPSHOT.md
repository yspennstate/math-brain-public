# C0049 independent route

The route was recorded first in APPROACH_LOCK.md, before reading any peer proof. It uses conditional partition functions and two real boundary-ratio martingales. Source verification and current literature status are recorded separately in SOURCE_STATUS.json. Nothing here proves convergence of lattice FK interfaces.

## Exact target and prior-attempt digest

The target is Conjecture 3 (Schramm), printed p. 93 / zero-index PDF page 92 of Hugo Duminil-Copin's 2017 lectures, arXiv:1707.00520. On the square lattice, fix 0<q<=4 and p=p_c(q). Let discrete Dobrushin domains (Omega_delta,a_delta,b_delta) approximate a simply connected planar domain with distinct marked boundary points a,b. Wire the counterclockwise arc from b_delta to a_delta and leave the complementary arc free. The conjecture asks for weak convergence of the medial exploration from a_delta to b_delta to chordal SLE(kappa), where kappa=4*pi/(pi-arccos(sqrt(q)/2)). The assigned unsolved range excludes q=2. For the conditional continuum work below, the domain is mapped to the upper half-plane with a->0, b->infinity and capacity time is normalized by dg=2/(g-W)dt.

The source's Conjecture 3 uses p=p_c, not a blanket independently proved identity p_c=sqrt(q)/(1+sqrt(q)) for q<1. Any use of that self-dual value below q=1 would add an unverified hypothesis. The triangular-lattice site-percolation SLE6 theorem is a different lattice model from q=1 square-lattice bond random cluster.

The September ranking calls C0049 tier 4, attempted_un. Its intake problems.jsonl:49 and attempts.jsonl:39 contain C0049 and C0049-A001. A001 tries extending the q=2 parafermionic proof and records missing analytic estimates. Targeted exact-ID searches found no C0049-specific entry in the named H/I attempt folders or additional intake folders except an exclusion cross-reference. The Lean campaign's matching ranking row is a status list, not a formal proof. The population export contains the exact problem and attempt cards, both marked unverified, so store presence is not proof evidence. Team O holds C0050 (w339) and overlapping P0124 (w341); the boundary-ratio lane was claimed by direct peer message rather than their analytic lane.

Current source status remains UNKNOWN for the full assigned range. A primary preprint posted 6 October 2026, arXiv:2610.08507, Theorem 1.2, states convergence of free-boundary q=4 FK loops (p=2/3) in Caratheodory-approximating simply connected square-lattice domains to nested CLE4 in the Camia-Newman topology. Its statement is not a Dobrushin exploration-path theorem; transferring the boundary condition and ordered exploration still needs an argument. I checked this source's stated scope, not its entire proof. A secondary OpenAI-Math-family search lead did not expose a primary manuscript to the browsing tool; it is not evidence that the remaining cases are solved or open. No novelty claim is made.

## Finite identities

Let G=(V,E) be finite, xi a boundary identification, 0<p<1, q>0, and w_q(omega)=p^|omega|(1-p)^(|E|-|omega|) q^k_xi(omega). Write Z_xi=sum_omega w_q(omega). L1 in CLAIMS.jsonl proves the exact full-conditioning edge formula. Under a partial exploration filtration F_n the correct formula is

P_q(e open | F_n)=p P_q(C_e | F_n)+[p/(p+q(1-p))] P_q(C_e^c | F_n),

where C_e means the endpoints are connected WITHOUT e, modulo xi, in the unrevealed completed configuration. Its conditional probability is not generally determined by connectivity in the revealed subgraph.

L2. Fix vertices u,v. Fuse their xi-classes to produce xi^{uv}. Configuration by configuration, k_xi^{uv}=k_xi-1+1_{u connected to v modulo xi}. Therefore

R(q):=Z_xi^{uv}/Z_xi = q^(-1)+(1-q^(-1)) P_q(u connected to v modulo xi).

This holds for every q>0, including q<1, without positive association. For q != 1, the probability is (q R-1)/(q-1). Fuse vertices, not two arbitrary arcs which each may contain several cluster classes; the displayed one-cluster decrement requires exactly two fixed identified classes.

The exploration version is equally exact. At each atom of F_n produced by predictable adaptive edge queries, sum the original full-configuration weights over all completions consistent with that atom. Let Z_n and Z_n^{uv} be those two restricted sums. The same identity holds with P_q(A | F_n) and R_n=Z_n^{uv}/Z_n. Hence (q R_n-1)/(q-1) is a bounded martingale, by the tower property for the ONE fixed event A. No independence of queried edges is asserted. Using the original restricted weights also retains cluster factors from completed explored components; an equivalent residual graph must preserve the marked component representatives.

L3, the q=1 repair. For a fixed finite graph, fixed p, and a fixed exploration-history atom, all restricted sums are polynomials in q with positive denominator for q>0. Differentiate the pointwise identity at q=1. Since R_n(1)=1, one obtains

P_1(A | F_n)=1+partial_q R_n(q)|_{q=1}.

Thus the plain fusion ratio is completely uninformative at q=1, but its fixed-p derivative exactly recovers the Bernoulli connectivity conditional probability. This proof does not differentiate a martingale expectation across changing probability laws. Neither differentiation nor a q-to-1 limiting operation is justified uniformly in mesh or in random slit domains by this finite identity.

## Conditional continuum theorem (L4)

Let the filtration satisfy the usual conditions. Let W be an adapted continuous real driver with W_0=0 and dg_t(z)=2/(g_t(z)-W_t) dt. Fix 0<x1<x2<y, and restrict to the common unswallowed interval on which X_i=g_t(x_i)-W_t>0 and Y=g_t(y)-W_t>0. Set U_i=X_i/Y; order preservation gives 0<U_1<U_2<1. Fix kappa>0 and

H_kappa(u)=integral_{1/2}^u v^(-4/kappa)(1-v)^(8/kappa-2) dv.

Assume both H_kappa(U_i) are continuous local martingales in this same filtration. Then W is a continuous local martingale on the interval and its quadratic variation is kappa dt. Equivalently it is a Brownian driver of speed kappa up to localization and the marked-point stopping time. This is a conditional identification theorem, not an FK convergence theorem.

Proof, including semimartingale recovery. Localize to compact subintervals of 0<U_i<1, Y>0 and U_2-U_1>0. H is smooth with strictly positive derivative. Its local inverse applied to the first continuous local martingale makes U_1 a continuous semimartingale. Both g_t(x_1) and g_t(y) are continuous finite-variation processes on the localized interval. The exact identity

W_t=[g_t(x_1)-U_1(t)g_t(y)]/[1-U_1(t)]

therefore makes W a continuous semimartingale. Write W=M+A locally, with M a continuous local martingale, A continuous predictable finite variation, and V=<M>. This decomposition has W_0=M_0=A_0=0.

Ito's formula for each ratio gives, as an identity of semimartingale differentials,

dU_i=[2/U_i-2U_i] dt/Y^2 +(U_i-1)dW/Y +(U_i-1)dV/Y^2.

The finite-variation part of dH(U_i) must vanish. Divide that identity by the nonzero coefficient H'(U_i)(U_i-1)/Y^2. It becomes

Y dA + [1+(U_i-1)H''(U_i)/(2H'(U_i))] dV - 2(1+1/U_i)dt=0.

Direct differentiation of H' gives

1+(u-1)H''(u)/(2H'(u))=(2/kappa)(1+1/u).

Consequently

Y dA +(2/kappa)(1+1/U_i)(dV-kappa dt)=0, for i=1,2.

Subtract the two equalities. Since U_1<U_2 and they are locally separated, the coefficient (2/kappa)(1/U_1-1/U_2) has a locally bounded inverse. Thus dV=kappa dt as measures, even if the original finite-variation measures had singular parts. The first equality then forces dA=0. Remove the compact localizations to cover the common unswallowed interval. The Brownian characterization is Levy's theorem locally (or an extension after stopping). All hypotheses are in one common filtration; no product of conditional probabilities is used.

For a GLOBAL driver conclusion, require the two martingale assumptions for all deterministic triples n<n+1<n+2, n>=1. Their first swallowing times exhaust every finite capacity horizon: continuity bounds W on [0,T], and choosing n>sup_{t<=T} W_t makes all three positive Loewner images remain strictly to the right of W. The local characterizations agree on overlaps and imply <W>_t=kappa t globally. Levy then identifies W/sqrt(kappa) as Brownian motion. A single fixed triple alone does not justify continuation beyond swallowing.

## Failure control: one martingale does not determine kappa (L5)

Choose nu>0 unequal to kappa and one pair 0<x<y. Up to exiting a compact region with 0<U<1 and Y>0, solve the locally smooth augmented SDE/ODE system

dW=sqrt(nu)dB - [2(nu-kappa)/(kappa Y)](1+1/U)dt,
dg_t(x)=2/[g_t(x)-W]dt, dg_t(y)=2/[g_t(y)-W]dt.

Local SDE existence holds on this open region. The displayed drift exactly cancels the finite-variation term in dH_kappa(U), so H_kappa(U) is a continuous local martingale. Yet <W>=nu dt. Thus a one-observable proof would be false unless an independent zero-drift or variance argument were provided. The second distinct ratio removes this free drift/variance tradeoff.

## Endpoint and event-selection checks

For 4<kappa<8, H is an affine rescaling of a bounded beta-integral profile with parameters 1-4/kappa and 8/kappa-1. For kappa=6 these are both 1/3. For kappa=4 the locally valid primitive is H_4(u)=log(2u), which is unbounded as u approaches zero; replacing it by a bounded crossing probability without a renormalization argument is invalid.

A finite connectivity event used in L2 is NOT automatically the SLE boundary-swallowing event associated with this profile. An FK-to-SLE proof must first select the appropriate interface event or observable, establish its exact topology and boundary conditions, and then prove its limiting value. Restricted partition sums work for any fixed configuration event, but their computability does not give their conformal asymptotics.

## Single hardest remaining gap

Prove that TWO appropriate FK exploration conditional observables converge, jointly with the driver and its filtration and locally uniformly in random slit domains, to affine copies of H_kappa(U_1), H_kappa(U_2), with enough localized integrability to pass the martingale property. Exact finite partition ratios, critical crossing bounds, and deterministic-domain weak convergence do not establish this assertion. No such estimate is proved here. For q<1 even the tightness inputs must be separately justified; for q=4 the latest primary result must be checked for its precise boundary/interface scope.
