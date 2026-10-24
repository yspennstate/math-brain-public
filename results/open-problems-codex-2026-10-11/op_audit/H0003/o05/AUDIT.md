VERDICT: PASS_WITH_GAPS

Audit date: 2026-10-12. Claimant directory was read only. This verdict accepts a counterexample to the literal, untruncated whole-cluster total-variation estimate, subject to the small connectedness fix below. It does not accept a solution of the intended local front-Markov problem.

## Claim and source scope

STATUS.md says SOLVED; ATTEMPT.md Sections 1–4 and its conclusion explain that this means **refuted**, not proved: every finite-graph failed-cluster law has TV distance at least 8/9 from the source's admitted one-type Bin(2,3/4) GW genealogy. Section 4 supplies a saturated parameter family keeping that target supercritical while the saturation error tends to zero. The conventional three-child root gives the stronger gap 26/27. CLAIMS.jsonl makes the same limited claims.

I independently fetched https://arxiv.org/html/2608.15987v1 using Python urllib, saving source.html here. I checked the actual definitions and conjecture in the fresh text, and compared the claimant's extracted PDF pages 9, 23, 30 and 31. Hypothesis 2.4 explicitly compares the failed cluster in G_n **as a random rooted graph** with the GW genealogy in TV. Conjecture 11.8 introduces neither depth truncation nor conditioning on extinction. Example 9.2 admits d=3, p=3/4, M=3/2. Definition 2.3 imposes a saturation margin, not subcriticality. Thus a supercritical counterexample answers the displayed full-regime assertion; it need not cover the critical window separately to disprove that assertion.

There is an important distinction in the source itself: Section 1.1 assumes finite **connected** graphs. Also, the source's claimed dissipative theorem is actually restricted to a subcritical region, with a separately stated conditional critical limit. Those results do not remove supercritical targets from the literal full-regime conjecture.

## Required small fix

**ATTEMPT.md Section 5, lines 96–102: connectedness is not established.** The union of three perfect matchings, followed by merging duplicate edges, is simple and has maximum degree three, but can be disconnected. The collision estimate and Markov selection only control the fraction of roots with incorrect finite balls. Neither implies that the selected realization is connected; disconnected unions of large locally tree-like components also pass that test. Consequently the explicit approximants have not been shown to meet all of the source's standing graph hypotheses.

Required fix: add a connectivity justification to the selection, or replace this construction with an established sequence of finite connected cubic graphs converging locally to T_3, with a precise existence reference or lemma. This is a routine graph-approximation completion; none of the TV, survival, or saturation arguments depends on the particular approximants. I have not supplied the missing construction for the claimant.

## Independent proof checks

**Section 2, lines 28–44: support lemma — correct.** In the local graph sigma-field, the event of infinitude is

    I = intersection over N>=1 of union over R>=0 of {|B_R(H,o)|>N}.

Each ball event is measurable, and connectedness makes infinitude equivalent to unbounded ball cardinalities. The same reasoning applies to genealogical trees. A finite graph contains only finitely many failed vertices, regardless of how failure or spontaneous crossings are defined. Therefore mu_n(I)=0 and d_TV(mu_n,nu)>=nu(I). Passing to huge finite clusters cannot evade this event in TV.

**Section 3, lines 46–68: extinction and root convention — correct.** I independently expanded

    f(s)-s = ((s-1)(9s-1))/16,  f(s)=(1/4+3s/4)^2.

The extinction-by-generation recursion starts at a_0=0 and satisfies a_{k+1}=f(a_k). The sequence increases, remains in [0,1/9], and its limit is a fixed point by continuity. Hence it selects 1/9 rather than 1. Bounded offspring makes eventual extinction equivalent to a finite genealogy. The infinity probability is therefore 8/9. With three possible root children it is 1-(1/4+(3/4)(1/9))^3=26/27. The weaker lower bound 8/9 is valid under either convention.

Fresh Python Fraction calculations, written independently of the claimant's script, verified the polynomial coefficients, both rational probabilities, and seven monotone extinction iterations. The first three are 0.0625, 0.088134765625, and approximately 0.0999198891222477. Exact assertions passed; see verify_fast.py and fast_results.json. Independent_check.py and independent_results.json provide a second record, including eight iterations. Floating-point displays are descriptive only; the assertions use exact rationals.

**Section 4, lines 72–92: saturation and limiting contradiction — correct under the stated uniform-error reading.** Fixing delta and letting n tend to infinity gives the necessary condition s_delta <= C epsilon(delta). Keeping s_delta=8/9 while epsilon(delta) tends to zero contradicts a finite constant C uniform along that family. The final choice C epsilon(delta)<2/9 followed by C eta_n<2/9 is legitimate, even if eta_n depends on delta; no uniform-in-delta n-limit is used.

I checked the proposed alpha=gamma=b=1, edge threshold 2, failure threshold 2+delta, and safe boundary 0. Ellipticity, positivity, directed equilibrium 1<2, and the exact logistic error 1/(1+exp(delta)) hold. For the directed OU process, the proposed hitting function

    H_h(x) = integral_0^x exp((y-1)^2)dy / integral_0^h exp((y-1)^2)dy

has H_h(0)=0, H_h(h)=1 and strictly positive derivative. Differentiating gives H_h''=2(x-1)H_h', so the generator (1/2)d^2/dx^2-(x-1)d/dx annihilates it. On the bounded interval, the diffusion exits almost surely; bounded optional stopping identifies H_h with the hitting probability. Thus the intermediate-value choice H_h(x_h)=3/4 is justified. It is not merely an assumption that p is a free parameter. The displayed model definitions impose no fixed initial-state condition excluding this choice. Remark 11.7 flags spontaneous-crossing concerns but does not add them as hypotheses of Conjecture 11.8; actual cluster dynamics are immaterial to the finite-support argument.

**Section 5, lines 98–102: local exploration — correct apart from connectedness.** B_R=1+3(2^R-1) and t_R=3B_R are valid upper bounds. Until a collision, the unexplored partner in a matching is uniform among its remaining unmatched vertices. The numerator 1+t_R bounds discovered vertices; n-2t_R-1 is a conservative denominator. The union bound and increasing-radius Markov selection establish the stated BS convergence of some finite simple graphs. They do not establish connectedness, as noted above.

**Section 6, lines 104–108: non-equivalence example — correct with its stated scope.** Depth-r truncations agree exactly with the surviving GW process at every fixed depth k<=r, and their reproduction is Markov, with a generation-dependent terminal transition. Nevertheless every truncation is finite and the TV gap persists. This disproves the implication from fixed-depth agreement and local Markov reproduction to whole-tree TV convergence. It is explicitly not a cascade-SDE counterexample to local front-Markovity.

## Qualifications already disclosed by the claimant

**Uniform constant, Section 4 line 72.** The refutation is of a vanishing saturation-error estimate with C uniform as delta grows. The source does not exhaustively specify C's parameter dependence. If instead one allows an arbitrarily divergent C_delta, the deduction that the RHS vanishes is unavailable; only s_delta <= C_delta epsilon(delta) remains proved. With positive epsilon, choosing C_delta=1/epsilon makes such an estimate vacuous. This limitation must stay attached to the result. It is disclosed in the attempt and is consistent with the problem's asymptotic uniform-error formulation.

**Source formula (3), Section 4 line 88.** The actual OU hitting probability is correctly re-derived in the attempt. The source's printed negative-exponent integral is not that scale function. Acceptance uses the probability definition in (3) and Example 9.2's admitted target, not a validation of its erroneous analytic RHS. The claimant appropriately flags this distinction; replacing the source's target by a different quantity computed from that RHS would require a separately specified problem.

**Formal verification, Section 8 line 125.** I read Extinction.lean and lean_check.json. The six lemmas are rational algebra and interval bounds, contain no sorry or native_decide, and agree with my independent calculation. The recorded exit code is claimant evidence; I did not independently rerun Lean. These lemmas do not formally verify probability-space measurability, extinction, the SDE, graph approximants, or uniform quantifiers. The attempt accurately limits their scope, so the acceptance rests on the handwritten arguments audited above.

## Fresh bounded literature check

Using Python urllib, I queried arXiv's API with `all:"Front-Markov" OR all:"threshold cascades"`, max_results=20, and fetched the abstract of arXiv:2609.27972. The successful responses are saved as arxiv_search.xml and later_abs.html. The query recovered the source, arXiv:2608.21125, and the later multiscale paper. The latter explicitly says: “We do not prove kappa_eff < 1 throughout kappa >= 1.” Its sufficient criterion requires contraction at a finite block scale; its abstract does not settle the full conjecture. The companion also states that neither of its two problems is fully closed. No earlier exact closure or published support-obstruction counterexample was identified in this bounded search. No novelty claim follows from that.

An OpenAlex works search for `front Markov threshold cascades`, per-page=10, returned HTTP 429. That is a failed query, not evidence of absence. I did not use built-in web search. The claimant's unpublished earlier repository lead was not independently accessed and is not treated as a literature solution.

## Accepted outcome

After the small connected-approximant completion, the literal whole-cluster TV conjecture, interpreted with a uniform vanishing saturation error, is refuted by a fully verified finite-versus-infinite support obstruction. The fixed target has a gap at least 8/9. The attempted equivalence with local front-Markovity is invalid. No proof or counterexample for the corrected local front-Markov conjecture in the full saturated regime, and no solution uniform through its critical window, is established by this work.
