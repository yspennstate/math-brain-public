VERDICT: PASS (correct and complete)

# Independent audit of P0452

Date: 2026-10-12. This audit reads the claimant's files without modifying them. All fetched sources, independent code, and audit outputs are in this audit directory. I did not use the claimant's numerical programs or treat its self-audit or Lean certificates as verification of the stochastic theorem.

## Exact claim and scope

The operative claim is the final summary in **ATTEMPT.md, lines 219–225**, together with its explicitly referenced proof, **SECOND_ATTEMPT.md, Sections 1–8 and 10**. STATUS.md and the final CLAIMS.jsonl records agree with this claim. ATTEMPT.md's earlier PARTIAL conclusion is explicitly superseded.

For every fixed probability law P on the positive integers with finite first moment and P(1)<1, let each vertex have an independent P-distributed preference budget, clipped to n−1, independently of the independent symmetric continuous edge costs on the complete graph. Retain an edge precisely when both endpoints rank it within their own budgets. The claim is

    L1(G_n)/n → ρ(P) in probability,

where ρ(P) is survival of the root component of the Erlang Weighted Tree. Expected fractions converge as well. The proof also claims this for every deterministic triangular budget array with d_i(n)≤n−2 and empirical laws converging weakly to P, without requiring convergence of empirical first moments. P(1)=1 is covered separately with limiting fraction zero.

This answers the specified question, including its supercritical case, rather than just extinction or bounded-budget distributions. It does not claim an almost-sure limit, quantitative convergence rate, an infinite-mean extension, or a theorem for growing budget distributions.

I downloaded arXiv:2002.03993v5 independently. Its introductory assumptions include finite mean and P(1)<1; Section 2.1, PDF page 8, gives the deterministic-array formulation; Theorem 2.1, page 9, supplies the local limit. Section 4, question 3, page 16, explicitly asks for the reverse giant-density inequality. The exponential-moment assumptions on later spectral results are not imposed on this question. The claimed hypotheses therefore match the source, and convergence in probability plus boundedness supplies the source's expected-fraction formulation.

## Issues found

**No substantive mathematical error or missing lemma was found. No proof repair is required for this verdict.** Two presentation points should not be mistaken for independent proof gaps:

1. **Historical status statements:** ATTEMPT.md line 199 says PARTIAL, and line 216 still says the new proof is under audit; lines 219–225 state the final SOLVED conclusion. An earlier CLAIMS.jsonl coalescence record also retains the sentence “The stochastic coalescence hypothesis is unproved.” These are stale historical records, superseded by the final theorem and the explicit final claim. Consolidating the status wording would improve record clarity; it does not invalidate the referenced proof.

2. **Freshness versus mutual independence:** SECOND_ATTEMPT.md Section 2, line 27, calls the child's budget, threshold, and outgoing costs “fresh independent backbone variables.” The entire child's construction is independent of the previously explored history. Within that construction, the threshold is conditional on the budget, and the uniform outgoing costs are conditional on the threshold. Read literally as mutual independence, the phrase would be false. The subsequent conditional-on-D calculation and the kernel in Section 5 use the correct dependence throughout; I found no inference that uses the false literal reading. For clarity, the phrase could say “a fresh child block, generated with the stated conditional laws.”

## Proof checks and independent derivations

### Prior upper bound and auxiliary statements — ATTEMPT.md Sections 1–4, 6–7, 9

For fixed k, adding or removing an edge changes the number F_k of vertices in components of size at least k by at most 2(k−1): merging two small components changes the count by at most their combined size, and merging a small component with a large one adds only the small size. Resampling one cost changes preferred lists only at its endpoints, each by at most one replacement, hence changes at most four retained edges. A change requires the edge to be preferred at some endpoint before or after resampling. Uniform ranks give the upper bound 2(d_i+d_j)/(n−1) on this probability. Efron–Stein consequently gives

    Var(F_k | d) ≤ 64(k−1)^2 Σ_i d_i.

The deterministic-array tightness argument is valid: with clipped budgets, Σ_i d_i/n² ≤ M/n + #{d_i>M}/n, and weak empirical convergence makes the latter tail small after M→∞. No hidden empirical-moment convergence is needed.

For random budgets, the resampling bound min(2(k−1)|D−D′|,n) is valid. Dividing its squared expectation by n tends to zero using min(X,n)²/n≤X and finite E X. Thus the claimed concentration holds without a second moment. The event that a root component has at least k vertices is determined by its radius k−1 unmarked ball; the source local limit supplies its expectation. Finally, L1≤F_k+k−1 and p_k↓ρ yield the upper bound in probability.

The coalescence equivalence in Section 3 follows from Q=S²−Σ a_C²≥S(S−M), and conversely Q≤S²−M² when a largest large component exists. The passage to expectations is justified by boundedness. This equivalence alone does not prove the lower bound; the new proof actually supplies that missing bound.

The mean-budget-at-most-two extinction argument correctly separates the deterministic one-child backbone at D=2 from ordinary critical Galton–Watson extinction. For D=2 the independent rejection events on disjoint consecutive pairs rule out an infinite ray. The bounded-budget logarithmic path argument uses distinct outside edge sets, giving the stated exponential integrand. Independently integrating over coordinate-order simplices confirmed the path integrals for lengths 3 through 7 and their Hilbert–Schmidt upper bounds. The source exploration inequality on PDF page 78 also gives the stated bounded-budget collision estimate by Bernoulli's inequality and summing l=1,…,t. These auxiliary results are not substituted for a supercritical lower bound.

### Time representation and augmented local limit — SECOND_ATTEMPT.md Section 1

An arriving edge is accepted exactly when each endpoint has seen fewer than its budget of earlier incident arrivals. All arrivals count, including rejected ones. This is exactly bilateral ranking, and accepted edges cannot be removed by later arrivals.

At finite t, the proposal graph has independent edge probability 1−exp(−t/n); its present-edge costs tend to uniform [0,t]. Fixed-radius exploration is tight because its expected size is bounded by a finite sum of powers of n p_n. On a bounded exploration, collisions are O(M²/n), and uniform target sampling gives independent limiting budget marks even for deterministic arrays. Activity and retained-edge decisions need only an enlargement of that finite proposal neighborhood. Continuous costs remove boundary-tie problems.

The root threshold is Gamma(D+1); a non-root's Dth *other* arrival is Gamma(D), with D−1 other candidate edges uniform below it. This matches the source's EWT construction and its kernel on PDF page 6. Proposal edges omitted from the EWT are still available in the augmented limit to define activity; accepted degree is never substituted for arrival count.

The cutoff variance bound is conservative but valid: a changed weight can affect at most five cutoff edges, and it matters only if an old or new cost is at most t, probability at most 2t/n. For a changed budget, at most the proposal degree incident to that vertex matters; its expected value is at most t. These bounds yield (k−1)²(50t+2t²)/n for the IID model, and the conditional part for deterministic arrays.

### Active-leaf coverage — Sections 2–3

Before testing a fresh child, its incoming candidate cost y≤t is known but its child block is not. Conditional on D=d≥2, the probability that its threshold exceeds t and all d−1 preceding other costs exceed t is

    ∫_t^∞ e^(−z) z^(d−1)/(d−1)! · (1−t/z)^(d−1) dz
      = e^(−t) ∫_0^∞ e^(−w) w^(d−1)/(d−1)! dw
      = e^(−t).

This guarantees acceptance of the parent and exactly one incident arrival by t, hence an active leaf. The probability P(D≥2)e^(−t) is conditional on the revealed exploration history and incoming cost, not on prior acceptance. On an infinite retained component there are infinitely many eligible tests. Successive conditioning bounds avoidance through N tests by (1−a_t)^N; the possible termination of a search only decreases that bound.

Consequently an infinite cutoff component has a finite retained path to an active vertex almost surely. All proposal degrees along that finite path are finite. Increasing R and B therefore makes the uncovered infinite-component probability vanish, and increasing k eliminates the tail of finite-component sizes. Markov's inequality at the threshold η n/2 gives exactly the stated ζ/4 failure bound.

Every path through proposal-degree-at-most-B vertices lies in a graph of maximum degree B. Thus an active vertex covers at most C=1+B+⋯+B^R roots. On the one event controlling *total* uncovered mass, every union of old large components of size at least η n has at least η n/(2C) active vertices. This simultaneous conclusion avoids any unproved concentration inside an individual random component.

### Sprinkling and partition bound — Section 4

Conditional on the complete history at t, unseen costs have independent rate-1/n exponential residual clocks. Total arrival rate is at most n/2, yielding the stated Poisson domination and Chernoff bound. With δ=a/4 and at most δ n arrivals, each initially a n-active side retains at least a n/2 active vertices, since one arrival deactivates at most two vertices.

Any currently active cross pair must have an unseen edge: if that edge arrived earlier, both endpoints were then active, so it was accepted. Before t this contradicts distinct old components; after t it contradicts the no-cross event. There are therefore at least a² n²/4 eligible unseen pairs, giving cross-acceptance rate at least a² n/4. Absorbing at either cross acceptance or excess arrivals makes the nonabsorption probability satisfy q′≤−(a² n/4)q. The proof does **not** condition on the future arrival cap while asserting independence.

There are at most n/k old large components, hence at most 2^(n/k) partitions. Choosing k after the coverage constants makes this enumeration dominated by the exponential cross bound. The cap-tail probability is counted only once. If final component blocks do not contain almost all old large-component mass, the stated intermediate-block/greedy argument produces a macroscopic partition with no cross edge, a contradiction. Fixed-k mass concentration then proves the final lower bound by every ρ_t. The parameters may depend on ζ, but the event being bounded does not; letting ζ→0 is legitimate.

### Compact returns and absence of type escape — Section 5

For type (m,x), there are m independent slots with fresh type law μ and acceptance h(x,z)=min(x,z)/x. Integrability of m lets one choose a compact fertile K with ε=∫_(Kᶜ) m dμ<1. The expected potential in the outside-only population contracts by ε. Expected births in the next generation are at most current potential, so the entire stopped outside family, including its first K hits, has finite expectation and is finite almost surely. This proves the required no-escape statement rather than assuming a general infinite-type truncation theorem.

For first strict K returns, the term with j outside ancestors has endpoint density at most B ε^j; direct return density is at least a/b. The series is uniformly convergent, and dominated convergence on each finite path integral gives continuity on compact K. Return families have finitely many children; subtrees below their stopping-line endpoints are independent conditional on types, because membership and incoming acceptance do not inspect their future outgoing variables.

With α=m/x and π=μ/α on K, the kernel relative to π is R(s,u)α(u). Each path contribution is α(s)α(u), times intermediate α factors and symmetric min-threshold factors. Reversing the path preserves the outside integration domain. Zero-potential intermediate types contribute zero. Thus the return operator is genuinely self-adjoint in L²(K,π), bounded and compact. Positive kernel values make the top absolute spectral value a positive eigenvalue: replacing an extremal eigenvector by its absolute value maximizes the positive Rayleigh form. The eigenfunction becomes continuous and bounded away from zero on K.

The uniform probability d0 of no return children follows by rejecting every original slot. Conditional independence of those slots gives the product lower bound. At infinitely many visits to populations between 1 and L, extinction has conditional probability at least d0^L, so survival implies Z_j→∞. If λ≤1, the positive bounded eigenfunction gives uniformly bounded E Z_j, contradicting that divergence through Fatou's lemma. Full-tree survival entails return-tree survival because all stopped outside families are finite. Hence full survival entails λ>1.

### Bounded-cost survival and continuity — Sections 6–7

Depth-N and compact-L return truncations lose at most B ε^(N+1)/(1−ε) in endpoint density from long excursions. For excluded types, summing first-excluded potential and then subsequent return density gives B τ_L/(1−ε)². I checked the indices and both denominators. These bounds yield the stated uniform operator approximation. The truncations preserve path reversal. Their Rayleigh quotient exceeds one once their action on the full positive eigenfunction does, so a positive eigenfunction exists with eigenvalue greater than one.

Only the truncated process is used in the L² martingale survival proof. It has uniformly bounded offspring and bounded positive weights, so conditional variance is at most a constant times population, and the normalized martingale has summable increment variances. Its positive limiting expectation implies positive survival. All actual edges on the retained return paths have cost bounded by their parent's threshold, at most b_L, so this process really is a subprocess of a finite-cutoff tree. The root has a positive chance of reaching K by an appropriately small cost.

The generating equation with h_t(x,z)=min(t,x,z)/x is correct. Dominated convergence makes e_* a full-process fixed point. The surviving bounded-cost subprocess makes 1−e_* positive on K, and direct positive transitions then give a *uniform* gap below one on K. Iterating the fixed-point identity to first K returns is justified by almost-sure finiteness of stopped outside families and bounded convergence. On return extinction the generation product eventually equals one; on return survival it is at most (1−c)^(Z_j) and tends to zero. This identifies e_* with extinction, first on K and then on every finite ordinary type. Integrating the separate Gamma(D+1) root law proves ρ_t↑ρ. This is the essential argument preventing an invalid exchange of survival and increasing cutoffs.

Combining this continuity with Section 4 and the prior upper bound proves the final theorem for both stated budget formulations. Bounded vertex fractions imply convergence of expectations. The probability-integral transform in Section 10 correctly extends the exponential-cost proof to any IID atomless cost law while preserving ranks almost surely.

## Independent computation and evidence

The code and results are `independent_checks.py`, `independent_checks.json`, `return_stress_independent.py`, and `return_stress_independent.json`. All assertions passed.

- Exhausted 61,440 one-edge sensitivity cases on five vertices.
- Exhausted all 81 budget vectors in {1,2,3}⁴, all 720 K4 arrival orders, and all seven prefixes: 408,240 states. Checked 715,440 qualifying active cross pairs and the equality of final temporal acceptance with bilateral ranking.
- Checked 2,994,093 relevant integer component-mass partition instances.
- Numerically integrated the active-leaf identity for d=2,3,7,25 and t=0.25,1,3,6,15; all matched e^(−t).
- Evaluated compact-complement potential using the actual gamma type law for P(D=1+m) proportional to m^(−5/2), which has finite mean and infinite variance. The tested complements had potentials approximately 0.460874, 0.148754, and 0.047134.
- Independently formed slot mean matrices, return Schur complements, weighted-symmetry identities, excursion truncations, and extinction fixed points. In the separate harder stress case, ε=0.92, direct compact radius=0.983939<1, full return radius=6.418806>1, and one outside ancestor already gives radius=1.597325>1. Symmetry residuals were below 7×10^(−18). These finite-type proxies check the algebra and mechanism; they are not samples from the continuous EWT or proofs of its limits.
- Checked an exact finite-state stopped-arrival example with eight vertices: nonabsorption probability at δ=0.125 was 0.773875, below the claimed hazard bound 0.939413. This complements the general conditional-rate derivation, not a replacement for it.
- Computed exact rational path integrals for lengths 3–7, obtaining 5/4, 23/27, 677/1152, 7313/18000, and 218491/777600, respectively; each satisfies the claimed historical Section 7 bound.

No finite test certifies the stochastic limit. The verdict rests on the independently checked written arguments above. I did not independently rerun the claimant's Lean tooling; its finite algebra certificates are unnecessary for this verdict and cannot certify the analytic or probabilistic steps.

## Bounded independent literature search

Saved requests and outcomes are in `fetch_log.json`. Fresh arXiv searches for “Erlang Weighted Tree”/“La-Kabkab” returned the source alone; a “bilateral preference” search returned an unrelated negotiation paper. Semantic Scholar's arXiv-source citation endpoint returned the arXiv and journal records of the Dabirian–Subramanian connectivity paper. OpenAlex returned HTTP 429, so its search is inconclusive.

I independently fetched and read the first-page abstract and theorem of arXiv:2209.05677v3. Its connectivity result concerns k near log n and does not establish the fixed-distribution giant lower bound. The source PDF itself explicitly leaves that bound open. This bounded search found no earlier exact solution or known counterexample; it is not a certification of priority or of absence from the literature. The claimant's verdict is assessed as an original SOLVED claim, not SOLVED_IN_LITERATURE.

The result established by the audited proof is the matching fixed-finite-mean giant-density limit. Neither simulations, growing-budget connectivity, local convergence alone, nor an unproved infinite-type approximation is being credited as the lower-bound proof.
