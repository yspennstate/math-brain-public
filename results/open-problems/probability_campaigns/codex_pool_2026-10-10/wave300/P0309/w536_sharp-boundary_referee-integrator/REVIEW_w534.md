# Independent referee check: w534, P0309

Date: 2026-10-10. Reviewed `ATTEMPT.md` Lemmas A-C and claim rows C2-C4. C1 is superseded. Verdicts below concern mathematics only; none solves P0309.

## C2 — KEEP as a proved special case for s>3

Recomputed the normalization from the two-particle cell of volume 2. For an even-plane particle, odd-plane neighbors have horizontal offset m+a; for an odd-plane particle they have m-a, whose sum equals the first after m -> -m. Averaging the two particle types leaves one such odd-plane sum; unordered pairs contribute factor 1/2. Thus equation (A1) has exactly one factor 1/2. The lattice potential is absolutely summable for s>3.

Independently, the Fourier coefficient of a -> sum_m exp[-t(m+a)^2] at integer k is sqrt(pi/t) exp[-pi^2 k^2/t] >0. Therefore its value is strictly largest at integral a: the k=1 cosine term is strictly below 1 for nonintegral a, while all other terms cannot increase. The gamma representation integrates this strict negative difference against positive weights. Twice differentiating gives the author's coefficient -4 pi^2 sqrt(pi)/Gamma(s/2), with strictly negative integral. At t down to zero the nonzero Fourier modes are exponentially small; at t up to infinity O(t) decays exponentially. Hence differentiation under the integral is justified. Equality occurs exactly at integral a. This proves C2 at its stated scope.

## C3 — KEEP as a proved finite-support obstruction for s>3

For finite p the pair energy difference only touches finitely many moving particles. At infinity its absolute tail is bounded by C|a|sum_r |r|^{-s-1}; the Hessian tail by C sum_r |r|^{-s-2}. Both converge at s>3. Oddness of the gradient gives zero first variation. Recomputed the second derivative as 1/2 sum_{r !=0} h_s(r)sum_x(p_{x+r}-p_x)^2. For p_x=1_{x in Q_L}1_{x_3 odd}, the normalized inner sum tends to 1 exactly when r_3 is odd and to 0 otherwise; it is bounded by 2. Dominated convergence gives 1/2 sum_{r_3 odd}h_s(r), precisely the C2 curvature, so it is negative for large L. A finite small displacement then lowers relative energy. This is an explicit counterexample to force balance implying stability, with no conclusion about a stable BCC/FCC phase.

## C4 — KEEP only for the explicitly defined heat integral

At t down to zero, the Fourier difference and its first two a-derivatives are O(t^-1/2 exp[-pi^2/t]) times a polynomial; Theta(t,0)O(t)=O(t^-1). At t up to infinity, O(t)=O(exp[-t]) while the theta factors and derivatives grow at most polynomially after reducing a modulo 1. Thus D_s(a) and D_s''(0) exist for every s>0. The same positive Fourier weights prove D_s(a)<0 exactly for nonintegral a and D_s''(0)<0. This verifies the stated integral result. **Do not import the sentence about common background/self counterterms as an identification with a physical Coulomb or long-range DLR energy.** That identification is not proved in the packet and is unnecessary for C4 as claimed.

The hardest original gap remains a uniform nonlinear free-energy/order argument for a stable reference phase, controlling defects and other competitors through an infinite-volume Gibbs limit. A KEEP on C2-C4 does not establish a positive-temperature crystalline phase. Current openness and novelty remain UNKNOWN.
