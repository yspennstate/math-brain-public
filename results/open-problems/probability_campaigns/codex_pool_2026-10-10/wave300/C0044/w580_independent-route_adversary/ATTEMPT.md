# C0044 independent route, recorded before reading the paired proof

2026-10-10. This initial derivation precedes reading w579's proposed proof. Current openness is UNKNOWN pending exact source and recent-status checks. This is an obstruction to one proof method, not a counterexample to C0044.

Let E={+/-e_i:1<=i<=d}. At each x in Z^d independently sample an identically distributed probability vector omega(x,.) on E. Define tau_z omega by (tau_z omega)(x,e)=omega(x+z,e). The environment seen from the particle has kernel K f(omega)=sum_{v in E} omega(0,v) f(tau_v omega).

Independent route: for fixed nonzero ell, h(omega)=P_0^omega(X_n dot ell -> +infinity) is K-harmonic. If an equivalent stationary probability Q exists, stationarity and Jensen's equality force h to be shift invariant; spatial ergodicity then makes h constant. The quenched conditional-probability martingale can force the constant to be 0 or 1. The hardest premise is existence of that equivalent stationary Q under the original hypotheses. It cannot be replaced by spatial stationarity of the original law P.

Concrete obstruction, derived without reading a peer proof: fix e in E and set f_e(omega)=omega(-e,e), m_e=E_P[omega(0,e)]. Then

E_P[K f_e] = E_P[omega(0,e)^2] + sum_{v!=e} E_P[omega(0,v)] m_e = m_e + Var_P(omega(0,e)).

For v!=e, the factors are at distinct sites 0 and v-e, so the stated independence is available; no per-step conditional probabilities are multiplied. E_P[f_e]=m_e. Thus P is K-stationary only if every row component has variance zero, which means the row distribution is a point mass. Conversely a deterministic identical row environment is fixed by every shift and is stationary. This conclusion does not require ellipticity.

An example within uniform ellipticity in d=3: put b=1/6, delta=1/12, and sample independent fair signs sigma_x. Set omega(x,+e_1)=b+delta*sigma_x, omega(x,-e_1)=b-delta*sigma_x, and the other four components to b. Every component is >=1/12. For f_{+e_1}, E_P[f]=1/6 but E_P[K f]=25/144; their difference is 1/144. This refutes the inference that iid spatial stationarity makes P invariant under K. It makes no claim about the directional transience probability in this example.

Review status: derivation saved, independent referee w581 requested; no checked-proof or parent-solution claim.

## Exact target and prior-route boundary

Drewitz--Ramirez, arXiv:1309.2589v1, Open question 3.2 (PDF page 42; printed page 40), asks under (E) and (IID) whether P_0(A_ell) is 0 or 1 for every fixed unit vector ell. Definition 2.3 has (E): all nearest-neighbor probabilities are strictly positive almost surely. It does not assume a common positive lower bound. The present assignment concerns d>=3. Current openness as of 2026-10-10 remains UNKNOWN; a dated source and an empty search are insufficient to certify it.

The exact intake attempt C0044-A001 uses the planar two-walk intersection method; A002 corrects the vacuous intersection-of-opposite-transience-events statement. The stationary-measure observable above is different from that planar method. A001 also says the natural martingale fails because its environmental probability is not measurable in a finite region. That is not an obstruction to the full-environment martingale below. No C0044-specific proof was found in the named H/I attempt folders or Lean campaign. Team O's board contains no C0044 row. No novelty is asserted for the calculations here.

## Full-environment conditional-probability martingale

Fix ell != 0 before any almost-sure statement. Write h(omega)=P_0^omega(A_ell). This is a measurable bounded function of the entire environment, since quenched probabilities of measurable path events are measurable. For the annealed joint law let G_n=sigma(omega,X_0,...,X_n). The quenched Markov property, invariance of A_ell under deletion of finitely many initial positions, and invariance of divergence to +infinity under a finite spatial translation give

M_n = h(tau_{X_n} omega) = E[1_{A_ell} | G_n].

Thus K h=h and M_n is a bounded martingale. Since A_ell is measurable for G_infinity=sigma(union_n G_n), the upward conditional-expectation convergence theorem gives M_n -> 1_{A_ell} almost surely and in L1. This does not imply h is constant and does not establish the desired zero-one law. No finite-region measurability is required; no annealed Markov property of X alone is claimed.

## Conditional zero-one result under a stationary density

Assume more generally that the environment law P is stationary and ergodic under all lattice shifts, is elliptic, and admits a K-stationary probability Q absolutely continuous with respect to P. These are additional hypotheses, not consequences of (IID) and (E).

First, Q is equivalent to P (the equivalence part of Kozlov's theorem, Drewitz--Ramirez Theorem 2.12). Here is the support argument, included so this dependence can be checked independently. Let rho=dQ/dP. Shift stationarity and QK=Q imply, P-almost surely,

rho(omega) = sum_{e in E} omega(-e,e) rho(tau_{-e} omega).

This follows by testing bounded measurable functions and changing variables separately for each shift; all terms are nonnegative integrable. On {rho=0}, ellipticity forces rho(tau_{-e} omega)=0 for every e. Shift stationarity makes the zero-density set and each of its shifted copies have the same P-measure, so these inclusions are equalities modulo null sets. Spatial ergodicity makes P(rho=0) equal to 0 or 1. Its value cannot be 1 because integral rho dP=1. Therefore rho>0 P-almost surely and Q~P.

Next K h=h and the probability-vector identity give the pointwise energy identity

K(h^2)(omega)-h(omega)^2 = sum_e omega(0,e) [h(tau_e omega)-h(omega)]^2.

Integration with respect to the stationary Q makes the left side zero. The right side is nonnegative; each weight is strictly positive Q-almost surely. Hence h(tau_e omega)=h(omega) Q-almost surely for every e, and equivalence transfers these equalities to P. Take the countable intersection of all translated full-measure sets to handle every lattice position. Spatial ergodicity then makes h=c P-almost surely. For almost every environment, h(tau_x omega)=c for every x, so M_n=c at every n along every walk. The martingale limit proved above yields 1_{A_ell}=c almost surely, so c is 0 or 1.

Conclusion: for each fixed ell, a stationary probability Q<<P suffices for the directional zero-one law under (E) and spatial ergodicity. This is an independently derived conditional argument using a known Kozlov hypothesis, not a new resolution of C0044. No simultaneous almost-sure assertion over the uncountable set of directions is made.

## The single hardest remaining piece

The original assumptions do not furnish a K-stationary probability with density relative to P. Compactness/Cesaro averaging may furnish an invariant probability, but not its absolute continuity. The one-site variance calculation rules out simply taking Q=P in every nondegenerate iid model. Proving the needed absolute continuity, or finding another argument forcing h constant without it, remains the gap. Failure of this route never refutes the parent conjecture.

## Disjoint quantitative lemma: the exact one-step bias

After reading w579's independently committed harmonic-energy route, this worker retains the following change-of-measure calculation as its disjoint mathematical contribution. Occupation-density criteria belong to w579. No duplicate energy argument is offered as a novelty claim.

For every shift-stationary law P (independence is not needed for this first identity), the one-step environment law PK has Radon--Nikodym density

S(omega)=sum_{e in E} omega(-e,e)

relative to P. Indeed, for bounded measurable f, shift each summand in E_P[sum_e omega(0,e)f(tau_e omega)] to obtain E_P[f sum_e omega(-e,e)]. The mean of S is one by row normalization and spatial stationarity.

If the rows are iid, the incoming components in S are evaluated at the pairwise distinct sites -e, so they are independent. Therefore the Pearson chi-square divergence chi^2(PK||P)=E_P[(S-1)^2] is exactly sum_e Var_P(omega(0,e)). This finite quantity is at most sum_e m_e(1-m_e)=1-sum_e m_e^2, where m_e=E_P[omega(0,e)]. It vanishes exactly for a deterministic common row law. This is a direct one-step change-of-measure identity and does not use harmonicity or an invariant-Q argument.

In the uniformly elliptic d=3 sign example above, S=1+delta*(sigma_{-e_1}-sigma_{+e_1}), so S takes values 5/6, 1, 7/6 with probabilities 1/4, 1/2, 1/4. Hence chi^2(PK||P)=1/72 and total variation ||PK-P||_TV=(1/2)E_P|S-1|=1/24. The first-site transition observable omega(0,e) alone has unchanged expectation after one step; it misses this bias. The backward-neighbor observable f_e detects it exactly by 1/144. This is why checking only fresh-site marginals cannot establish full environmental stationarity.

## Public status lead

The paired worker's statement names a public primary claim at https://raw.githubusercontent.com/openai/math/main/lean/docs/220.md. The document explicitly claims the strict-elliptic iid d>=3 annealed directional law and links a September 23, 2026 preprint and Lean comparator. This claim is not yet a checked proof receipt. Current openness stays UNKNOWN while the actual statement, proof and assumptions are inspected. Neither this worker nor the dated ranking certifies present openness.

NEXT: Independently check the density-support and energy arguments, and audit w579's proposed bridge at its exact artifact once available.
