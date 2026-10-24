# H0003: whole-cluster total variation has a support obstruction

Research date: 2026-10-12. This report addresses the literal statement of Conjecture 11.8, not a corrected local-convergence conjecture.

## 1. Verified statement and hypotheses

Achyut Kumar, *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1. Downloaded PDF saved as source_pdf.pdf, 36 pages.

Conjecture 11.8 is on printed page 30; the following scope discussion continues on page 31. It states:

> In the full saturated regime — without the dissipative condition κ < 1 of (6), and uniformly through the critical window — there is a constant C such that, for the cluster law in G_n,
>
> d_TV(L(failed cluster), L(multitype GW with M)) ≤ C(ε(δ) + η_n),
>
> with η_n → 0 as G_n →^BS T and ε(δ) → 0 as the saturation margin δ → ∞. Equivalently, the cascade front is asymptotically Markov: conditional on the set of failed vertices at generation k and their types, the failures into generation k+1 are asymptotically independent of generations < k.

Here the prose is transcribed verbatim, with the displayed formula converted to linear notation. The preceding standing definitions are essential:

* Section 2.1 uses finite graphs G_n converging Benjamini–Schramm to UGW(g). The state space G_* is rooted locally finite graphs with its local topology. The forward mean is m* = g''(1)/g'(1).
* Definition 2.1 has finitely many independent types, independent Brownian motions, α_d ≥ α_min > 0, b_d² ≥ μ_0 > 0, θ_uv ≥ θ_min > 0, γ ≥ 0, and logistic σ. Failure is absorption in B_fail = [θ_fail,∞).
* Definition 2.3, page 9: inf_{s in B_fail}(s−θ_uw) ≥ δ uniformly. Thus σ ≥ 1−ε(δ) on failed parents, with ε(δ)→0.
* Hypothesis 2.4, page 9, explicitly compares the **law of the failed cluster of the root in G_n, as a random rooted graph** with the entire multitype GW genealogy in total variation. There is no depth truncation, finite-horizon restriction, conditioning on extinction, or identification of large finite clusters with an infinite object.
* The target offspring law is inherited from UGW(g) and independent per-edge probabilities p_{d,d'} from the directed first-passage problem (3). The mean matrix alone would not define a GW law; Hypothesis 2.4 supplies the offspring law.
* On the one-type 3-regular limit, m*=2 and the non-root law is Bin(2,p). Proposition 9.1, page 23, prints the ordinary GW target Bin(d−1,p). Example 9.2 explicitly chooses d=3,p=3/4, giving M=3/2>1.

The conjecture says **full** saturated regime, not only ρ(M)≤1. The critical-window qualifier strengthens that scope; it does not remove the source's supercritical regime.

## 2. General support lemma — full proof

Let μ be any probability law supported on finite connected rooted locally finite graphs, and ν any probability law on the same measurable space, allowing infinite connected graphs. (Equivalently take the rooted connected component throughout.) Then

    d_TV(μ,ν) ≥ ν(graph is infinite).

Proof. Write B_R(H,o) for the radius-R ball and let A_{N,R}={|B_R(H,o)|>N}. A_{N,R} is measurable in the local topology: the radius-R rooted ball determines its truth. Local finiteness implies every such ball is finite. A rooted connected graph H is infinite exactly when for every N there is an R with |B_R(H,o)|>N. Therefore

    I={|H|=∞}=intersection_{N≥1} union_{R≥0} A_{N,R}

is measurable. Since μ is supported on finite graphs, μ(I)=0. The definition d_TV(μ,ν)=sup_A |μ(A)−ν(A)| applied to I proves the claim. If cluster laws are encoded by spanning genealogies rather than induced graphs, the same argument applies verbatim to rooted trees. ∎

For the failed cluster C_{n,δ} in any finite G_n, |C_{n,δ}|≤|V(G_n)| deterministically. This does not require any assertion about the SDE, front independence, absence of spontaneous failures, or accuracy of the paper's cellwise estimates. Consequently

    d_TV(L(C_{n,δ}), GW_δ) ≥ s_δ,

where s_δ is the target GW survival probability. An even stronger finite-n bound follows from the event {|H|>|V(G_n)|}, but the infinity event already suffices.

## 3. Exact survival calculation — full proof

Take one-type offspring K~Bin(2,3/4). Its probability generating function is

    f(s)=(1/4+3s/4)^2.

Let Z_0=1 and let a_k=P(Z_k=0). Then a_0=0. Conditional on the root's number K of offspring, all K descendant processes are independent copies. Each is extinct by generation k with probability a_k. Thus a_{k+1}=E[a_k^K]=f(a_k).

The events {Z_k=0} increase with k because zero is absorbing. Hence a_k increases to q=P(eventual extinction). Continuity of f gives q=f(q). Also f maps [0,1/9] into itself: 0≤s≤1/9 implies 0≤1/4+3s/4≤1/3, so 0≤f(s)≤1/9. Induction yields a_k≤1/9 and q≤1/9.

Direct expansion gives

    f(s)−s = (s−1)(9s−1)/16.

Therefore the only real fixed points are 1 and 1/9. The bound q≤1/9 excludes 1, so q=1/9. On nonextinction, Z_k≥1 for every k, hence there is at least one vertex in each generation and the genealogy is infinite. On extinction, extinction occurs at a finite generation, and each generation is finite since every vertex has at most two children, so the genealogy is finite. Thus

    P(GW is infinite)=1−q=8/9.

Applying Section 2 proves, for every finite n and every δ whose target is this law,

    d_TV(L(C_{n,δ}),GW(Bin(2,3/4))) ≥ 8/9.                     (A)

Root convention check. An actual uniformly rooted 3-regular graph has three possible root children, while later vertices have two. If the source is corrected to Bin(3,3/4) at the root and Bin(2,3/4) elsewhere, extinction at the root has probability (1/4+(3/4)(1/9))³=1/27. The lower bound is then 26/27, even stronger. The 8/9 bound works under either convention, so the root inconsistency is immaterial here. ∎

## 4. Saturation quantifiers and the contradiction

The intended nonvacuous meaning of C(ε(δ)+η_n) with ε(δ)→0 is that C is finite and uniform as δ grows along an admissible saturated family (and in the claimed critical window). If C were allowed to grow arbitrarily with δ, the statement would no longer assert a vanishing saturation error: C_δ=1/ε(δ) makes the displayed inequality trivial whenever ε(δ)>0.

In full generality Section 2 gives the necessary condition

    s_δ ≤ C ε(δ),

by fixing δ and taking n→∞ in the proposed inequality. Thus the conjecture would force s_δ→0 as δ→∞. This is incompatible with any admissible saturated family having liminf s_δ>0, in particular the source's supercritical Bethe target held fixed.

There is no condition in Definition 2.3 or Conjecture 11.8 forcing p≤1/2 or forcing p→1/2 as δ grows. Here is also a concrete way to keep p fixed without treating the transmission probability as an independent free symbol. For each δ>0 choose the one-type parameters α=1, γ=1, b=1, θ_uv=2, θ_fail=2+δ, and s_safe=0. Then the failed basin floor is 2+δ, so the saturation margin is exactly δ and ε(δ)=1−σ(δ)=1/(1+e^δ). The directed saturated forcing is the constant γ=1, whose OU equilibrium m_uv=1 is less than the edge threshold 2, as required in Section 2.3.

Choose the initial state of each not-yet-failed cell so its directed two-boundary first-passage probability is 3/4. Such an initial state always exists. To check this rather than assume tunability, for the OU diffusion dX=−(X−1)dt+dW between l=0 and h>0 the hitting probability is

    H_h(x)= integral_0^x exp((y−1)^2)dy / integral_0^h exp((y−1)^2)dy.

The integrand is continuous and strictly positive on the finite interval. Hence H_h is continuous and strictly increasing, H_h(0)=0, H_h(h)=1; the intermediate value theorem gives a unique x_h∈(0,h) with H_h(x_h)=3/4. To verify the formula, H_h'=a exp((x−1)^2), H_h''=2(x−1)H_h', so the generator (1/2)H_h''−(x−1)H_h' annihilates H_h. Stopping Itô's bounded martingale at the boundary exit time proves the hitting identity. Exit is almost surely finite: bounded drift on [0,h] and nondegenerate Brownian noise give a positive probability of exit in a fixed time interval, uniformly in the starting point; the Markov property iterates this to an exponential bound on survival of the interval. For example, a Brownian increment larger than h+sup|drift| over a unit interval forces exit unless exit already occurred.

If θ in the paper's pairwise boundary notation means the failure boundary, use h=2+δ and x_h; if it means the edge threshold, use h=2 and x_2. Either boundary convention permits the same prescribed p by this argument. The paper's formula (3) has a questionable scale-function sign; this obstruction uses the actual OU hitting probability, and also separately uses Example 9.2's explicitly admitted p=3/4. It does not need the questionable sign formula.

These choices satisfy the explicit ellipticity, positive threshold, mean-below-edge-threshold, finite-type, and saturation requirements. The source gives no bound on initial states beyond being between the safe and failure boundaries. Its spontaneous-failure negligibility remark (11.7) is flagged, not a hypothesis of Conjecture 11.8. Adding a new restriction on initial states, a new stopping rule, or a survival-vanishing assumption would change the question. One may instead view p=3/4 as the source's own abstract admitted Bethe parameter; the support proof is identical.

Suppose a uniform finite C existed on this saturated family. Choose δ large enough that C ε(δ)<2/9. Then choose n large enough that C η_n<2/9, using η_n→0 for that fixed δ (even allowing η_n to depend on δ). The proposed bound is less than 4/9, contradicting (A). No uniformity of η_n across δ is needed. This disproves the literal vanishing whole-cluster TV statement. ∎

## 5. Finite simple graph approximants exist — explicit probabilistic construction

For completeness, the one-type 3-regular local limit is attainable within bounded-degree finite simple graphs; it is not an infinite-tree-only parameter choice.

On an even n-element vertex set choose three independent uniform perfect matchings, take their union, and merge duplicate edges. This gives a simple graph of maximum degree 3. Before merging, expose the colored matchings successively while exploring a root's radius-R ball. In a tree with degree 3 this ball has at most B_R=1+3(2^R−1) vertices. Exposing all incident colored edges of these vertices requires at most t_R=3B_R pair revelations. Until a collision, at most 1+t_R vertices have been discovered. In each color, conditional on the previously revealed pairs of that matching, the partner of an unmatched vertex is uniform among the remaining unmatched vertices. For n>2t_R+2 its conditional probability of being an already-discovered vertex (apart from a previously revealed reverse edge, which is simply skipped) is at most (1+t_R)/(n−2t_R−1). A union bound over t_R revelations bounds the probability of any collision by

    t_R(1+t_R)/(n−2t_R−1).

No collision implies the radius-R rooted ball is exactly the ball in T_3, and no edge relevant to this ball is merged. By exchangeability, the expected fraction of roots whose radius-R ball is incorrect is bounded by this same expression. For each j choose even n_j so large that this expression for R=j is below 2^(−2j). Markov's inequality implies positive probability that the bad-root fraction is at most 2^(−j) (indeed the probability of exceeding it is <2^(−j)). Fix one such realization. For any fixed R and j≥R, a bad radius-R ball is also bad at radius j, so its fraction is ≤2^(−j)→0. Thus the deterministic sequence of chosen finite simple graphs converges BS to T_3. Its limiting degree distribution is g(s)=s³, with m*=g''(1)/g'(1)=2 and finite moments of all orders. ∎

## 6. Why the claimed equivalence fails

Let T be the supercritical GW tree above and T^[r] its truncation at depth r. Every T^[r] is finite. For every fixed depth k, the depth-k truncation of T^[r] is exactly that of T whenever r≥k. Through generations k<r the usual independent GW reproduction law is exact; its future depends only on the present generation and independent unused offspring marks. At generation r it terminates deterministically, which is also Markov (the transition can depend on the generation).

Nevertheless, Section 2 gives d_TV(L(T^[r]),L(T))≥8/9 for every r. Thus exact Markov branching on every fixed observed depth, and even exact local agreement, do not imply whole-tree TV convergence. The intended local front-decoupling assertion cannot be called equivalent to the printed global TV assertion. This example diagnoses the purported implication; it is not offered as an SDE counterexample to local front-Markovity.

## 7. Hostile-referee audit

1. **Is an infinite-tree event measurable?** Yes, Section 2 gives a countable expression in measurable finite balls.
2. **Is the compared object actually the full cluster?** Yes, Hypothesis 2.4 says “as a random rooted graph,” and Conjecture 11.8 introduces no truncation or extinction conditioning.
3. **Are supercritical laws allowed?** Yes, the full-regime language and Example 9.2 explicitly admit p=3/4 with M=3/2. If the target were restricted to ρ(M)≤1, this example would not refute that new statement.
4. **Could saturation secretly eliminate survival?** The explicit family in Section 4 retains p=3/4 by tunable initial states. No contrary restriction occurs in the definitions. More generally the unavoidable necessary condition is s_δ≤Cε(δ).
5. **Can finite clusters simulate infinity by becoming huge?** They can in the local topology, but not in TV; the infinity event has probability exactly zero for each finite n.
6. **Does changing the root law fix it?** No; it strengthens the gap to 26/27 in the conventional uniformly rooted version.
7. **Is the extinction calculation just a fixed-point guess?** No; the increasing extinction-by-generation recursion and invariant interval select the smaller root in Section 3.
8. **Does the counterexample rely on the source's unproved exact SDE reduction?** No. The actual finite cluster law can be arbitrary. Only the conjecture's prescribed target and finiteness are used.
9. **Does it disprove the intended corrected local front-Markov property?** No. That remains open in the full strong-coupling regime. The later preprint explicitly rescopes the conjecture and leaves a resonance regime open.
10. **Does C depend on δ?** The vanishing-error interpretation requires uniformity. Arbitrary δ-dependent blowup makes the written estimate vacuous, and is not a proof of an asymptotic statement. This ambiguity is recorded explicitly rather than hidden.

## 8. Checks and conclusion

check_exact.py uses exact rational arithmetic, not floating-point inference, to verify the fixed point, survival gaps, and early extinction recursion. exact_results.json stores its output. Extinction.lean is a limited formalization of the rational fixed-point algebra and invariant-interval check. Executed `lake env lean ~/brain_workers/TRIO_1011/op/H0003/Extinction.lean` from ~/lean_verify. The shared wrapper waited 1410 seconds for a slot, then ran the check with its configured 3600-second timeout. The command completed with **exit code 0 and no Lean diagnostics** on 2026-10-12. The file imports only Mathlib.Tactic.NormNum, Ring, Linarith, and Positivity, and uses neither sorry nor native_decide. Six rational-algebra lemmas are kernel checked. This does not formalize the full probabilistic or SDE argument; those proofs are written in Sections 2–6.

Conclusion: **the literal whole-cluster total-variation conjecture is false in its full stated regime**. The counterexample is the finite-support obstruction against the source's admitted supercritical Bethe target, with explicit gap 8/9. This is a mathematical counterexample, not SOLVED_IN_LITERATURE. The result recovers and independently checks a prior unpublished repository lead. No proof or counterexample to the corrected local/front-Markov conjecture at strong coupling is claimed.
