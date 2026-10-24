# Intake H: Open problems from arXiv papers, July-September 2026

Collected by targeted web search + arXiv abstract/HTML/PDF fetches. Scope: math.PR and closely
related categories (math.CO with probabilistic content, math-ph), arXiv IDs 2607.*, 2608.*, 2609.*
(July, August, September 2026 only). Only problems the authors themselves call open, conjectural,
or unresolved are included; fully resolved theorems are excluded even when a paper's title mentions
a conjecture it proves.

---

### [arXiv:2609.03492] A finite-graph conjecture related to θ(p_c)=0 for Bernoulli bond percolation on ℤ^d (Lucas Flammant)
- label: Conjecture 2.2
- where: Section 2 (with the planar case proved as Theorem 2.3, and the implication for ℤ^d as Theorem 2.4)
- statement: "There exists a universal function φ:(0,+∞)→ℝ, independent of G, o, B and p, such that φ(ε)→1 as ε→0" and, for events increasing with respect to the percolation configuration with ℙ[E_b]≥1−ε for each b∈B, "ℙ[⋃_{b∈B}({o⟷b}∩E_b)]≥φ(ε)ℙ[o⟷B]."
- context: The author proves this for finite planar graphs (Theorem 2.3, with explicit φ(ε)=1−2√ε) and shows it implies θ(p_c)=0 for Bernoulli bond percolation on ℤ^d for every d≥2 (Theorem 2.4). Conjecture 2.2 is explicitly stated to remain open for general (non-planar) finite graphs; Section 4 notes the planar proof's key device ("the definition of b* cannot be reproduced directly, since there is no analogous geometric order on the boundary") does not extend.

### [arXiv:2608.19145] The critical probability for percolation on finite graphs (Micha Christoph, Patryk Morawski, Yuval Wigderson)
- label: Question 5.1
- where: Section 5, Concluding remarks
- statement: "What natural conditions on G imply that if p≥(1+ε)/λ(G) then with constant probability G_p contains a component of size Ω(|G|)?"
- context: The paper's main theorems determine the critical probability for Bernoulli bond percolation on essentially any finite graph to be 1/λ(G) (λ = spectral radius), confirming a conjecture of Krivelevich and Samotij; Question 5.1 is posed as the natural follow-up about the supercritical component-size behavior.

### [arXiv:2608.15987] Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary (Achyut Kumar)
- label: Conjecture 11.8 (Front-Markov property, full saturated regime)
- where: Section 11.5, "The remaining conjecture"
- statement: "In the full saturated regime — without the dissipative condition κ<1 of (6), and uniformly through the critical window — there is a constant C such that, for the cluster law in G_n, d_TV(L(failed cluster), L(multitype GW with M)) ≤ C(ε(δ)+η_n), with η_n→0 as G_n →^BS T and ε(δ)→0 as the saturation margin δ→∞. Equivalently, the cascade front is asymptotically Markov: conditional on the set of failed vertices at generation k and their types, the failures into generation k+1 are asymptotically independent of generations <k."
- context: Proved on the Bethe lattice and, unconditionally, on the dissipative region (κ<1); the strong-coupling regime κ≥1 is "the remaining open problem."

### [arXiv:2608.15987] (same paper) — Section 12.3, "The honest open problems"
- label: Open problem (2), "The sensitive regime"
- where: Section 12.3
- statement: "Outside saturation the type is the continuous failure strength A∈R (Proposition 3.3(2)); the mean object is an integral operator and criticality is its Perron eigenvalue, now computable by Proposition 12.1. What remains open is the limit theory: the 3/2 exponent should persist (count variance is still finite, Lemma 6.1), but the constant and the boundary dimension require the spatial CLT and Perron projection on a continuous type."

### [arXiv:2608.15987] (same paper)
- label: Open problem (3), "Sharp moment hypotheses for the CRT limit"
- where: Section 12.3
- statement: "Reduce the exponential-moment hypothesis of Theorem 6.4 to g''(1)<∞; see Remark 6.5."

### [arXiv:2608.15987] (same paper)
- label: Open problem (4), "Finite-size scaling on G_n"
- where: Section 12.3
- statement: "Quasi-stationary theory [6] for the cutoff ξ=(1−ρ(M))^{-1} against the finite size n; the window near criticality."

### [arXiv:2608.15987] (same paper)
- label: Open problem (5), "Beyond trees"
- where: Section 12.3
- statement: "Non-tree unimodular limits, where short cycles do not vanish and the cluster is not a GW genealogy."

### [arXiv:2608.15987] (same paper)
- label: Open problem (6), "Boundary fluctuations"
- where: Section 12.3
- statement: "By Theorem 5.5, the dimension of the failed boundary is finite-dimensional; what is not is the fluctuation theory on ∂S: the multifractal spectrum of transmission-weighted flows (the Legendre transform φ* of the pressure of Definition 5.2), and the harmonic measure of the cluster itself, where the dimension drop of [17] should reappear. Here the essential spectrum of K_∞ and a Weyl-type decomposition, rather than compactness, are the right tools."

### [arXiv:2608.15987] (same paper)
- label: Open problem (7), "The front profile"
- where: Section 12.3
- statement: "Theorem 11.5 controls the cluster law; it does not describe the front as a dynamical object. A travelling-wave / hydrodynamic limit for the active front — speed, shape, and Gaussian (or F–KPP-type) fluctuations of the front position on the tree, in the spirit of branching Brownian motion — is open, and is the natural continuum question behind the front-energy supermartingale of Remark 11.6. The dissipative regime κ<1, where the linearised front dynamics has a uniform spectral gap, is the place to start."

### [arXiv:2608.21125] Two problems for threshold cascades of interacting diffusions on unimodular random trees: front propagation with a Bramson correction, and the continuous-type limit theory (Achyut Kumar, Abhinav Duddala)
- label: Conjecture 3.2 (Uniform integrability of the derivative martingale ⇒ Bramson delay)
- where: Section 3.2
- statement: "Under the hypotheses of Theorem 2.1, the derivative martingale ∂W_n is uniformly integrable (equivalently, ∂W_∞>0 a.s. on survival), and consequently the time-indexed front obeys F(t)=c*t−(3/(2θ*c*))log t+O_ℙ(1), with the tightness and the limiting law of the recentred front F(t)−c*t+(3/(2θ*c*))log t given by a randomly-shifted Gumbel decorated point process, the shift being a multiple of log ∂W_∞, exactly as for branching Brownian motion."
- context: This paper is an explicit companion to arXiv:2608.15987 (above), formulating precisely two problems that paper left open, supplying the analytic framework, and proving partial theorems.

### [arXiv:2608.21125] (same paper)
- label: Conjecture 7.2 (Continuous-type CRT scaling limit)
- where: Section 7
- statement: "Under the hypotheses of Theorem 6.1 at criticality ρ(K)=1, with the additional exponential-moment hypothesis on the offspring count, the critical cluster conditioned on {|S|=n}, with graph distance rescaled by Σ_c/√n, converges in the Gromov–Hausdorff–Prokhorov sense to Aldous' Continuum Random Tree, with an explicit constant Σ_c built from σ²_off and the tilted stationary law ϖ*."

### [arXiv:2607.07410] Essential spectrum for Brox-type diffusion processes (Yuichi Shiozawa, Jian Wang)
- label: (unlabeled, stated as "the key open question" in the Introduction)
- where: Section 1, Introduction
- statement: "the key open question: can random drift perturbations break the compactness of confining deterministic diffusion semigroups?"
- context: The paper answers this affirmatively in specific regimes (Proposition 5.2) but leaves the boundary case δ>1/α genuinely open, stated in Remark 5.3 (see below).

### [arXiv:2607.07410] (same paper)
- label: Remark 5.3(ii), first case (L^{w1+W})
- where: Section 5
- statement: "For δ>1/α, we do not know if L^{w1+W} generates a compact Markovian semigroup on L²(ℝ;μ^{w1+W}). In fact, by Lemma 5.1(ii), we have Q-a.s., for any x>0, ∫_x^∞ e^{-(y^δ+V(y))} dy<∞. However, since we have no information about the decay rate of ∫_x^∞ e^{-(y^δ+V(y))} dy as x→∞, it is unclear if the left hand side of (5.6) is divergent or not as x→∞. Therefore, we could not apply [26, Theorem 2] to L^{w1+W}."

### [arXiv:2607.07410] (same paper)
- label: Remark 5.3(ii), second case (L^{w2+W})
- where: Section 5
- statement: "On the other hand, for δ>1/α, we do not know if L^{w2+W} generates a compact Markovian semigroup on L²(ℝ;μ^{w2+W}). In fact, by Lemma 5.1(ii), we have Q-a.s., for any x>0, ∫_x^∞ e^{-y^δ+V(y)} dy<∞. Define h(x)=∫_x^∞ e^{-y^δ-V(y)} dy for x>0. In order to apply [26, Theorem 2] to L^{w2+W}, we need to calculate limsup_{x→∞} (1/h(x) − 1/h(0)) ∫_x^∞ h(y)² e^{y^δ−V(y)} dy, but this value is unknown at present."

### [arXiv:2609.11578] Negative correlation for the random-cluster model below one on high-degree regular graphs (Pengfei Tang, Zibo Zhang)
- label: Conjecture (Pairwise Negative Correlation), unnumbered but formally stated in Section 1.1
- where: Section 1.1
- statement: "For every finite graph G, every p∈(0,1), and every Q∈(0,1), the random-cluster measure φ_{G,p,Q} satisfies (1.6)," where (1.6) is Cov_ν(X_e,X_f)=ν(X_e=X_f=1)−ν(X_e=1)ν(X_f=1)⩽0 for e≠f.
- context: The authors state plainly that "even this basic two-edge covariance question is nontrivial and, on general finite graphs, has remained unresolved," and prove the conjecture only for regular graphs of increasing degree satisfying edge-isoperimetric conditions (expanders, random regular graphs, high-dimensional discrete tori), showing this restricted case is equivalent to the fully general one.

### [arXiv:2608.23661] θ(p_c,ℤ^d)=0? (Raphaël Cerf)
- label: Conjecture 1.1
- where: Section 1, Introduction
- statement: "For any d≥3, we have θ(p_c,ℤ^d)=0."
- context: This is the classical percolation-probability-at-criticality conjecture for Bernoulli site (and, by extension, bond) percolation. The paper proves a partial result (that at p_c either there is no infinite cluster or the finite-cluster-size tail is not a stretched exponential) but leaves the full conjecture open.

### [arXiv:2607.07589] Surviving from the tip of a cone in competing first-passage percolation (Daniel Ahlberg, Maria Deijfen, Matteo Sfragara)
- label: Benjamini's conjecture (attributed, unnumbered)
- where: Section 1.2, Introduction
- statement: "Benjamini asked what is the maximal angle α such that type 2 survives with positive probability," and "Benjamini suggested that the critical case is when the cone fills the whole negative half-plane, meaning that type 2 can survive if and only if α<π/2." The authors note explicitly: "The 'only if'-direction remains open, but partial and related results have been obtained."
- context: In two-type first-passage percolation on ℤ², one type starts at the origin and the other from an infinite cone of angle θ; the paper proves the "if" direction for any θ where the asymptotic shape of the one-type process has a tangent line in direction θ, leaving the general "only if" direction (no tangent case) open.

### [arXiv:2607.08160] Weak Poincaré Inequalities via Approximate Stochastic Localization: Application to Sampling the Sherrington-Kirkpatrick Model (Ewan Davies, Holden Lee, Juspreet Singh Sandhu, Jonathan Shi)
- label: Open Problem 15 (of Randomstrasse101, arXiv:2504.20539)
- where: cited and addressed throughout the paper (framing in the Introduction)
- statement: "resolution of the conjecture that Glauber dynamics mixes fast in the replica-symmetric regime for the Sherrington-Kirkpatrick model"
- context: The authors establish a weak Poincaré inequality for the SK model's Gibbs measure and efficient sampling via Glauber dynamics with warm-start initialization only for inverse temperature β<1/2, describing their result as "a significant structural step towards resolution" of the full open problem rather than a complete resolution — the full replica-symmetric regime remains open.

### [arXiv:2608.04303] The rank and layer distributions in random recursive trees (Huck Stepanyants, P. L. Krapivsky, Harrison Hartle, Dmitri Krioukov)
- label: Conjecture 1
- where: Section II, Main results (traveling-wave analysis in Appendix A)
- statement: "The layer distribution ℓ_k is asymptotically ℓ_k=exp[−(1/e)k−(3/(2e))log k−O(1)]."
- context: Derived via a traveling-wave method and supported by analytic and numerical evidence in Appendix A ("Traveling wave analysis for Conjecture"); not proved rigorously in the paper.

### [arXiv:2607.07309] Quantitative limit theorems for generalized Pólya urns with applications to random tree models (Morenikeji Neri, Pedro Pinto)
- label: Remark 3.7 (posed as an open question, not a numbered Conjecture)
- where: Section 3, "Main results: Quantitative limit theorems for generalized Pólya urns"
- statement: "If one can show that λ_max(symm(C_p J_p(R^⊤−λI)C_p^⊤))<0 for p=d or d−1 for all tenable, irreducible generalized Pólya urns, then not only would Theorem 1.1 follow, but one would also obtain quantitative rates..."
- context: The authors flag this contractivity condition as unverified in general; establishing it for all tenable, irreducible urns would strengthen and generalize their quantitative convergence-rate results for outdegree statistics in random recursive tree models.

### [arXiv:2608.06358] Universality in random graphs via optimal linking systems: trees and beyond (Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii)
- label: Conjecture 1.4 (Sharp threshold for tree universality)
- where: Section 1.6, "Further challenges"
- statement: "For every ε>0 and integer Δ≥2, whp G(n,(1+ε)ln n/n) is 𝒯_{n,Δ}-universal."
- context: The paper proves universality (containment of every n-vertex tree of bounded max degree) at G(n,C ln n/n) for some absolute constant C>1, answering a question of Montgomery, but the sharp threshold at p=(1+ε)ln n/n (matching the connectivity threshold) is conjectural.

### [arXiv:2608.06358] (same paper)
- label: Conjecture 1.5 (Cycle factor universality)
- where: Section 1.6
- statement: "For every ε>0 and ℓ≥(1+ε)ln n/ln ln n, whp G(n,(1+ε)ln n/n) is 𝒞_{n,ℓ}-universal."

### [arXiv:2608.06358] (same paper)
- label: Conjecture 1.6 (Optimal linking system depth)
- where: Section 1.6
- statement: "Fix ε>0, and let k≥(1+ε)ln n/ln ln n... Then, whp G(n,(1+ε)ln n/n) contains an (a,b,k)-linking system." The authors add: "obtaining tight bounds on the maximal depth of linking systems in sparse random graphs appears to be a fundamental problem."

### [arXiv:2607.27082] Extinction and Survival in an Interval-Activation Frog Model on ℤ with Random Survival Parameters and Symmetric Random Walks (Gustavo Oshiro de Carvalho, Fábio Prates Machado, José Hermenegildo Ramírez-González)
- label: (unlabeled open gap, Remark 6 / Theorem 5(ii))
- where: Section on the critical line β=1/r
- statement: "For β=1/r, the preceding theorem identifies the exact asymptotic of n·ℙ(D^→≥n), but the two firework comparisons yield only sufficient criteria. The survival and extinction constants differ by a factor of four." The survival criterion requires liminf_{n→∞} ℓ(n^r) > 1/(𝔼[η_0]κ) while the extinction criterion requires limsup_{n→∞} ℓ(n^r) < 1/(4𝔼[η_0]κ); the authors state "the full phase diagram on the critical line is not determined by the present argument."
- context: On the sharp off-critical threshold β_c=1/r (survival for β<1/r, extinction a.s. for β>1/r) is established, but the behavior exactly at the critical line β=1/r is left with a factor-of-four gap between the authors' sufficient conditions for survival and extinction.

### [arXiv:2607.22383] Constrained Multi-Relational Graphons with Maximum Entropy (Juan Alvarado, Jan Ramon, Yuyi Wang)
- label: The RRS conjecture (Radin–Ren–Sadun), attributed and named by the authors
- where: Section 1.1.1
- statement: "Radin, Ren, and Sadun conjectured, on the strength of numerical experiments, that the solutions are always step functions — equivalently, stochastic block models, multipodal functions, or echelon functions... We call this the RRS conjecture, and a positive answer is more than a structural curiosity: it collapses an infinite-dimensional functional optimization to a finite-dimensional parametric one."
- context: The paper resolves the RRS conjecture for constrained multi-relational graphons "in the non-extremal regime," under the condition that the subgraph density constraints are analytically independent; prior work was "confined to single-relation graphs and to specific constraint families." The extremal regime (and, implicitly, dependent constraint families) is left open; the paper's own Section 6.2, "Open Questions and Future Directions," is referenced in its table of contents but its exact text could not be retrieved through available fetches (see failed fetches below).

---

## Summary

- **Papers with at least one quoted open problem/conjecture: 14**, spanning July 2026 (2607.*), August 2026 (2608.*), and September 2026 (2609.*) submissions to math.PR / math.CO (probabilistic content) / math-ph.
- **Total open problems/conjectures quoted: 25** (arXiv:2608.15987 alone contributed 7 — a "Discussion: criticality certificates in the sensitive regime, and open problems" section explicitly titled "The honest open problems" listing seven numbered items; its companion paper arXiv:2608.21125 contributed 2 more).
- This falls short of the 40-100 target and the "at least 15 distinct papers" target despite roughly 45 distinct search queries and ~35 abstract/HTML/PDF fetches. The main obstacle: most July-September 2026 math.PR papers found via search either (a) resolve a previously-known conjecture completely with no remaining open statement, (b) state open questions only informally/parenthetically without any formal "Conjecture/Question/Open Problem" label and without a quotable self-contained sentence, or (c) are recent enough that WebSearch's snippet index has not yet indexed their full text, making it necessary to fetch each candidate individually (slow, and many fetches returned "no explicit label found" even when the abstract mentioned unresolved aspects).

### Search queries used (representative, ~45 total)
"open problems" math.PR 2026; "Conjecture 1.1" percolation 2026; random matrices open problems survey 2026; branching random walk / free probability / random polymers / Brownian motion "remains open" 2026; interacting particle systems open problems 2026; arXiv 2607/2608/2609 combined with: "Conjecture", "Open Problem", "we conjecture that", "it would be interesting to", "we pose the following", cutoff phenomenon, random matrix "Conjecture 1.3/1.4/1.5", "we conjecture" random graphs, epidemic/contact process, Poisson-Dirichlet/coalescent, stochastic block model, Oberwolfach report probability, workshop "problem session", Poisson urn/Polya urn, stochastic heat equation/parabolic Anderson, quantum walk, random Schrodinger operator, phase transition random graph, bootstrap percolation, random regular graph spectral, chase-escape/frog model/activated random walk, cover time, graphon/graph limit, Malliavin calculus/Wiener chaos, extremes of Gaussian field, Ramsey random, first passage percolation shape, superprocess/measure-valued, Anderson localization, diffusion limited aggregation, queueing/stochastic game, random tree "Conjecture 1" limit, mean field optimal stopping/mean field games, isoperimetry/functional inequality, fractional Brownian motion/rough path, random recursive tree/preferential attachment, Erdos-Renyi/random hypergraph.

### Fetches that failed or returned no usable content
- https://arxiv.org/pdf/2608.15987 (as PDF via WebFetch's summarizer — content was compressed binary; resolved by using the Read tool directly on the saved PDF file instead)
- https://pith.science/paper/2608.21125 (empty content; resolved by finding and fetching the real arXiv abstract page directly)
- https://arxiv.org/pdf/2607.07410 (same binary-PDF issue; resolved via Read tool on the saved file)
- https://arxiv.org/pdf/2607.22383 (same binary-PDF issue; Section 6.2 "Open Questions and Future Directions" was located in the table of contents but its exact page/text could not be reached within budget — the paper is referenced above with the conjecture statement and the non-extremal/extremal-regime distinction only)
- Numerous WebFetch calls on abstract pages for candidate papers (2607.05345, 2608.13084, 2609.03359, 2608.31056, 2607.21443, 2609.01143, 2608.10190, 2609.01851, 2607.08712, 2609.05297, 2608.28816, 2609.05581, 2608.24616, 2609.08454) returned abstracts with no explicitly labeled Conjecture/Open Problem/Question statement, or the conjecture referenced was fully resolved by that same paper; these were excluded from the intake.
