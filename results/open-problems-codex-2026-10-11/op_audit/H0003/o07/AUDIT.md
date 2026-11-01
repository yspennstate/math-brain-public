VERDICT: PASS_WITH_GAPS

Audit date: 2026-10-12. The literal whole-cluster total-variation estimate is refuted, subject to one small graph-construction repair below. This does not establish or refute the intended local front-Markov property in the full saturated regime.

The claimant's SOLVED means a counterexample, not a proof of Conjecture 11.8. Its precise conclusion is that every finite-graph cluster law has total-variation distance at least 8/9 from the source's ordinary GW target with offspring Bin(2,3/4), and at least 26/27 under the conventional degree-three root correction. An admissible saturated family with this fixed transmission probability contradicts the proposed vanishing bound when C is uniform in the saturation margin. One admissible supercritical case suffices to refute a statement covering the full regime; solving every special case is unnecessary for a counterexample.

## Exact statement and scope

The problem states:

> In the full saturated regime — without the dissipative condition κ<1 of (6), and uniformly through the critical window — there is a constant C such that, for the cluster law in G_n, d_TV(L(failed cluster), L(multitype GW with M)) ≤ C(ε(δ)+η_n), with η_n→0 as G_n →^BS T and ε(δ)→0 as the saturation margin δ→∞. Equivalently, the cascade front is asymptotically Markov: conditional on the set of failed vertices at generation k and their types, the failures into generation k+1 are asymptotically independent of generations <k.

I independently fetched https://arxiv.org/html/2608.15987v1 and checked Sections 2.2–2.4, 9, and 11.5. This is the printed Conjecture 11.8. Hypothesis 2.4 explicitly compares the failed root cluster in finite G_n, “as a random rooted graph,” to the GW genealogy in total variation. No depth restriction, extinction conditioning, or quotient identifying large finite objects with infinite objects appears. The target offspring law is supplied by that hypothesis, rather than by the mean matrix alone. Proposition 9.1 specifies Bin(d−1,p); Example 9.2 takes d=3 and p=3/4, hence M=3/2. The introduction assumes finite connected approximating graphs. The source's apparent root-law inconsistency is accounted for by the claimant.

## Issue requiring a small repair

**ATTEMPT.md Section 5, entire construction and deterministic selection:** the union of three perfect matchings, with duplicate edges merged, need not be connected. Selecting a realization with few bad rooted balls does not ensure connectedness. This misses the connectedness assumption in the source's Section 1.1. It matters because the advertised admissible finite-graph sequence is otherwise not completely constructed.

Required fix: explicitly obtain connected approximants, either by selecting connected matching realizations with the needed local convergence, or by a bounded-degree connection of components using o(n) added edges and justifying preservation of the BS limit. This is a routine graph-approximation repair; no change to the support argument, saturation family, or survival probability is needed. I do not supply the replacement construction here.

## Quantifier and interpretation qualifications

**ATTEMPT.md Section 4, first paragraph and final contradiction:** the contradiction uses a single finite C along the saturation family. It does not refute an estimate with unrestricted C=C(δ,s_0,θ_fail), whose product with ε(δ) need not vanish. The source does not spell out all allowable dependencies of C. I accept the claimant's explicitly stated interpretation because the supplied problem asks for a vanishing saturation error with “a constant C.” The final conclusion must retain that qualification. This is already acknowledged in the attempt, not a hidden proof step.

**ATTEMPT.md Section 4, OU family and boundary-convention paragraph:** the actual OU hitting probability has a positive scale-density exponent. The negative exponent in the source's displayed formula (3) is not validated by this audit. I checked the probabilistic definition of p in that same equation and the source's explicitly admitted p=3/4 example. The family argument is valid with p understood as the defined first-passage probability. It should not be described as verification of the source's questionable integral display. The attempt itself makes this distinction.

**ATTEMPT.md Sections 6–8 and STATUS.md:** rejecting whole-cluster TV convergence does not resolve local front decoupling, critical-window uniformity for a corrected local law, or the strong-coupling SDE problem. The claimant expressly limits its conclusion accordingly. The SOLVED label is acceptable only for the literal stated inequality under the constant convention above, not as a claim to have proved the intended Markov assertion.

## Independent proof checks

**Section 2: support and measurability.** Re-derived the event of infinitude as the countable intersection over N of the union over R of {|B_R|>N}. Finite rooted balls determine these measurable events. A connected locally finite graph is infinite exactly when its ball sizes are unbounded. A cluster in a finite graph assigns this event probability zero. The variational definition of TV therefore gives d_TV(μ,ν)≥ν(infinite). This proof is correct and requires no cascade approximation or independence assertion. It also applies to any genealogical encoding of the finite cluster.

**Section 3: extinction and root correction.** Independently expanded

    (1/4 + 3s/4)^2 − s = (s−1)(9s−1)/16.

The extinction-by-generation recursion starts at a_0=0 and satisfies a_{k+1}=f(a_k). Its limit is a fixed point by continuity. The interval [0,1/9] is invariant, since 1/4+3s/4≤1/3 there. Monotonicity of extinction events selects q=1/9 rather than 1. Bounded offspring makes survival equivalent to infinite genealogy. Thus survival is exactly 8/9. With three potential root children, root extinction is (1/4+(3/4)(1/9))^3=1/27, giving 26/27. No root convention removes the obstruction.

I implemented fresh Fraction-based checks of the factorization at 101 rational inputs, the exact fixed point, both survival fractions, and six extinction iterations. The identity itself was also derived symbolically by hand, rather than inferred from the finite sample. All checks passed; the iterates begin 0.0625, 0.088134765625, 0.0999198891222477 and stay below 1/9. The output is in independent_checks.json.

**Section 4: saturation and attainability of p.** The displayed parameters α=b=γ=1, edge threshold 2, failure floor 2+δ, and safe level 0 satisfy the listed positivity and ellipticity requirements, m=1<2, and the exact saturation margin δ. Logistic saturation gives ε(δ)=1/(1+e^δ). There is no stated upper bound on initial states or mandatory spontaneous-failure exclusion in Definitions 2.1–2.3 or Conjecture 11.8; Remark 11.7 flags a concern rather than adding such an assumption. These parameters are dissipative on degree-three graphs, but the full-regime conjecture includes dissipative cases too. This does not claim a new strong-coupling theorem.

For the stated OU diffusion, the generator is L=(1/2)∂²−(x−1)∂. Differentiating H_h(x)=∫_0^x exp((y−1)^2)dy / ∫_0^h exp((y−1)^2)dy gives LH_h=0 and boundary values 0,1. The exit-time argument is valid: bounded drift on the interval and a sufficiently large unit-time Brownian increment imply a uniformly positive exit probability; iteration gives almost-sure exit. Bounded stopped H_h permits the martingale limit. Strict positivity of its derivative and the intermediate value theorem give an initial state with H_h=3/4 for every finite h. Numerical quadrature/root finding independently returned probabilities within 10^−12 of 3/4 for h=2,3,5,10. This numerics checks the construction; existence for all h is supplied by the analytic argument.

The TV lower bound s_δ≤C(ε(δ)+η_n) implies s_δ≤Cε(δ) after the fixed-δ n-limit. Taking δ large and then n large contradicts s_δ=8/9. Allowing η_n to depend on δ does not affect this order of limits. The constants 2/9 and 4/9 used in the attempt produce a strict contradiction correctly.

**Section 5: local graph approximation.** Rechecked B_R=1+3(2^R−1), the at-most 3B_R pair exposures, uniform partners in partially exposed matchings, the collision union bound, and the increasing-radius deterministic selection via Markov's inequality. These establish bounded-degree finite simple approximants with the asserted BS limit. Merging duplicates is harmless when no relevant collision occurs. The only missing hypothesis is connectedness, identified above.

**Section 6: purported equivalence.** Depth-r truncations of a surviving GW tree agree exactly at each fixed depth k≤r, but remain finite and have TV gap at least 8/9 from the full tree. Ordinary independent offspring are used up to depth r, followed by deterministic termination. This is a valid demonstration that fixed-depth agreement and a Markov property do not imply global TV convergence. It is not an SDE counterexample to local front-Markovity, and the attempt correctly says so.

**Section 8: formal-check scope.** Read Extinction.lean without executing claimant code. Its six lemmas concern rational algebra and an invariant interval; they contain no sorry or native_decide. They do not formalize real-valued extinction limits, the SDE, graph approximants, or the conjecture. The attempt reports that limitation accurately. I did not rerun Lean or independently certify its reported historical exit status; the mathematical calculations were independently checked instead.

## Fresh bounded literature check

Used Python urllib only, with responses retained here. The arXiv API query for “front-Markov” or “multiscale front-decoupling” returned arXiv:2609.27972 and one irrelevant move-to-front paper. I independently fetched the abstract of 2609.27972. It gives a finite-scale gain-matrix contraction criterion and explicitly says: “We do not prove kappa_eff < 1 throughout kappa >= 1.” It is not a solution of the exact full-regime conjecture. The OpenAlex query was attempted and returned HTTP 429; that is a search limitation, not a negative bibliographic result. No published exact solution or earlier published instance of this counterexample was established by this bounded search. The claimant's reported earlier unpublished repository lead was not used as evidence of correctness or novelty.

Evidence: fetch_log.json, fresh_source.html, fresh_source_excerpts.txt, fresh_arxiv.xml, fresh_later_abs.html, verify.py, and independent_checks.json. All audit writes were confined to this folder; the claimant's folder was read only.

The result stands after the connected-approximants repair: the literal vanishing whole-cluster TV estimate cannot hold against a target with fixed positive survival probability. The corrected local/full-regime front-Markov question remains unresolved by this work.
