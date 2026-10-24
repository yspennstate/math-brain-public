P0309 paired-attempt adversary verdict (w538)

Source: w537/ATTEMPT.md, sections C1-C5. The exact inspected source is retained in PAIRED_SOURCE_SNAPSHOT.md; its digest is provenance only, not a mathematical certificate. The initial independent w538 checkpoint predates any access to w537's proof. Final referee: w539.

Verdict: KEEP C1-C5 as conditional reductions under their written assumptions. No counterexample to the stated C5 was found. Do not use a conditional crystalline-chart moment as its full-law moment. No Riesz phase is proved by this verdict.

C1 audit: p_N'(h)=E_h M_N/N and p_N''(h)=beta Var_h(M_N)/N. The normalization and beta are correct. The secant bounds use p_N(0)=0 and the admissible condition 2h<h0. Pointwise pressure convergence suffices for the squeeze; differentiability of p at h>0 is not needed. The limit in field comes after the volume limits.

C2 audit: for a<m the bracket in the lower probability bound is positive eventually because p(h)>ha; its logarithmic cost tends to zero for fixed h. The bound beta(p(h)-h) tends to zero as h decreases to zero, giving the stated liminf rate. For a>m, the Chernoff exponent beta(ha-p(h)) is strictly positive for small h. No rate at the boundary a=m is claimed. The converse uses the lower exponential rate, not an unsupported independence assumption.

C3 audit: cell invariance, N=rho K_N |C|, uniform integrability, and zero limiting boundary count are all needed to pass the local Fourier expectation. Use a bounded fundamental cell, such as a parallelepiped, to make this local weak-continuity step literal. A zero-field Gibbs conclusion still requires the explicitly separate specification-closure hypothesis. A nonzero mode by itself does not identify BCC/FCC or a full crystalline phase.

C4 audit: the normalized three-branch exponential moment has exponent max(beta a |h|,c)-c. The cost c>0 creates a flat neighborhood at h=0. This is a valid conditional-branch obstruction, not a Riesz counterexample.

Separately derived proof of the most important step, C5
Fix 0<a<r<b<=1. From |B_N|<=1 and liminf E|B_N|^2>=b^2, eventually q_N=P(|B_N|>=r)>=(b^2-r^2)/(2(1-r^2))=:q>0. Circular invariance gives P(Re B_N>=a)>=q*acos(a/r)/pi=:c_a>0 by averaging an independent auxiliary uniform angle. For fixed h>0, the full unpinned exponential moment is therefore at least c_a exp(beta h N a). Thus p_N(h)>=ha+log(c_a)/(beta N). The assumed pressure limit gives p(h)>=ha for every sufficiently small fixed positive h. Taking h down to zero gives p'_+(0)>=a, then a up to b gives p'_+(0)>=b. All constants are fixed before N tends to infinity. No particle independence is used. This proves the stated conditional C5 directly, without C2.

Concrete counterexample to replacing the full law by a selected chart (O4; w539 check pending)
Fix beta,c>0 and 0<a<=1. Under the full law, let S_N=0 with probability 1-exp(-cN), and S_N=aN exp(iTheta) with probability exp(-cN), where Theta is uniform on [0,2pi). This full law is circularly invariant and bounded by N. Conditional on the ordered branch, E|S_N/N|^2=a^2; under the full law it is a^2 exp(-cN). For M_N=Re S_N, the pressure is
p(h)=max(a|h|-c/beta,0), hence p'_+(0)=0.
Proof: the full moment is 1-exp(-cN)+exp(-cN) times the uniform angular integral of exp(beta h a N cos(theta)). That integral has logarithmic rate beta a |h|: the maximum gives the upper bound, and a fixed angular cap where the cosine exceeds 1-delta gives the matching lower bound as delta decreases to zero. Comparing the two rates proves the formula. Thus even restoring exact circular symmetry to a conditional harmonic/chart law does not justify inserting its moment into C5. The missing premise is a positive moment under the unrestricted law, or equivalent control of the chart's full-law probability cost.

Connection to the independent w538 bridge
B1 uses a Dirichlet convex displacement model, whose law is not the unrestricted unpinned Riesz law in C5. O3 shows that direct pointwise global convexity of the finite-volume Riesz energy is impossible near collisions. A proposed repair must work on a controlled region (or use a nonconvex inequality) and separately bound its unrestricted Gibbs weight. This is the concrete lemma boundary between the two lanes.

NEXT: w539 check O3/O4 and the independent C5 derivation; next proof work is a zero-exponential-cost estimate for a controlled crystalline region under the actual unrestricted Riesz law.

Provenance: the initial O1/B1 checkpoint preceded access to w537. The separate C5 derivation followed reading the paired proof; it is not a blind statement-only check. Final mathematical referee review remains pending.
