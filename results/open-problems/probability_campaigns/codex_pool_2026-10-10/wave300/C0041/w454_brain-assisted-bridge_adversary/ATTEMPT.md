# C0041: independent adversarial bridge note

Saved 2026-10-10 before reading w453's proof.

The primary statement in Campos and Ramirez, *Ellipticity criteria for ballistic behavior of random walks in random environment*, Conjecture 1.1, is: for nearest-neighbor RWRE on Z^d, d >= 2, under a uniformly elliptic iid site environment, P_0(X_n dot l -> +infinity)=1 should imply P_0(liminf X_n dot l / n > 0)=1. The 2013 source is historical evidence; current openness is UNKNOWN pending targeted status checks.

The principal bridge I will audit is regeneration-time integrability. Almost-sure finiteness supplies no first-moment bound. Even deterministic unit regeneration displacements and iid durations do not supply one.

Independent obstruction C0041-w454-001: let P(T_i=m)=1/[m(m+1)] for m>=1 independently. Put S_k=sum T_i and Y_t=max{k:S_k<=t}. Then P(T>=m)=1/m, T<infinity almost surely, and E[T]=infinity. For every fixed M, the strong law for min(T_i,M) gives liminf S_k/k >= E[min(T,M)]. The latter increases to infinity, hence S_k/k -> infinity. Since Y_t -> infinity and t>=S_{Y_t}, Y_t/t <= Y_t/S_{Y_t} -> 0. Thus Y_t is transient to the right and has zero speed.

This is a counterexample to an inference, outside the C0041 model class: Y has holding times and is not a uniformly elliptic nearest-neighbor RWRE. The exact missing input is quantitative control strong enough to yield E[T]<infinity (for example, a summable duration tail), established under the actual environment law and conditioning.

Second independent bridge, also saved before reading w453: let X be a nearest-neighbor Markov chain on Z^d, starting at 0, with every directional transition at least kappa>0. No iid assumption is needed here. Let tau be any a.s.-finite nonnegative integer random variable, not necessarily a stopping time, and R=max_{0<=j<=tau}|X_j|_infinity. For integer r>=0, put L=2r+1 and let H_r be the first exit from [-r,r]^d. From every site in this cube, L successive +e_1 steps exit; their conditional probability is at least kappa^L. Iterating conditional one-block survival bounds, rather than asserting independence, gives P(H_r>t) <= (1-kappa^L)^floor(t/L). Consequently

P(tau>t) <= P(R>r) + exp(-kappa^(2r+1) floor(t/(2r+1))).

If P(R>r)<=C exp(-a r), with a>2 log(1/kappa), choose c with 1/a<c<1/[2 log(1/kappa)] and r=floor(c log(t+1)). The first term is O(t^(-ac)), which is summable. The second is at most exp(-c_0 t^(1-2c log(1/kappa))/log(t+1)) for sufficiently large t, also summable. Thus E[tau]<infinity. Under conditioning on an event D with probability p>0, the same statement holds with P(R>r|D) for the first term and p^-1 multiplying the second term; it does not assert that the conditioned walk preserves its transition lower bound.

This supplies a rigorous sufficient bridge under an extra spatial-tail hypothesis. Directional transience alone supplies no such exponential tail or rate, and the bound is too crude to turn every stretched-exponential spatial tail into an integrable clock. Establishing the needed quantitative spatial or time control from the actual C0041 assumptions remains the hard piece. This bridge is an unreviewed special-case result, not a solution of C0041.

Source-status discovery: a public 23 September 2026 preprint with the target's title is linked by openai/math/lean/docs/220.md. The linked comparator theorem contains `sorry`; the comparator is a statement specification, so this does not refute the accompanying paper or its separate formalization. A checked theorem/dependency/axiom receipt is still required. The raw PDF could not be parsed by the web tool (octet-stream); retrieve only the relevant source material locally next.

NEXT: Read exact intake records, the scar and math-brain hypotheses; then audit w453's main step and the new preprint's scope.
