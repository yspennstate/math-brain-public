# T049: minimal-spanning-forest components

Checked 14 November 2026. The three proposed title matches do not claim the statement in T049. All three manuscripts name the author as **OpenAI**. The statements below are transcribed from the actual TeX theorem environments, retaining their wording and mathematical notation; layout and theorem labels are rendered as Markdown. No conclusion about the correctness of their proofs is needed for this comparison.

## The statement being checked

Our statement is: “The minimal spanning forest of Z^d with iid uniform edge weights (free and wired coincide on Z^d) is a single tree for d < 8 and has infinitely many components for d > 8.”

Thus the model is the minimal spanning forest (FMSF/WMSF), the graph is the nearest-neighbour lattice, the inputs are IID edge weights, and the quantity is the almost-sure number of components. The requested ranges are integer dimensions below and above 8; the statement makes no claim at d=8. The outstanding low-dimensional portion of the supplied note is d=3,4,5,6,7, and the other requested portion is every d≥9. The assertion “open for every d≥3” in the note concerns the component question more broadly, including d=8.

## 1. The free uniform spanning forest is a factor of IID — September 25, 2026

Author: OpenAI. Opened the [paper's TeX entry point](https://raw.githubusercontent.com/openai/math/main/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/build/paper.tex) and [actual introduction/theorem source](https://raw.githubusercontent.com/openai/math/main/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/build/sections/introduction.tex), lines 47–60. The [manuscript README](https://raw.githubusercontent.com/openai/math/main/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/README.md) confirms title, author, date, and PDF filename.

Theorem 1.1, exactly:

> There is one Borel, root-independent, equivariant rule
> \[
>  \Phi(G,U,e)\in\{0,1\}
> \]
> such that, for every infinite connected locally finite simple undirected
> unweighted graph \(G\) and independent
> \(\operatorname{Uniform}[0,1]\) vertex labels \(U=(U_v)_{v\in V(G)}\), the entire
> edge set
> \[
>  \{e\in E(G):\Phi(G,U,e)=1\}
> \]
> has law \(\mathrm{FUSF}_G\).

Comparison with each part of our statement:

| T049 phrase | What this theorem actually says |
|---|---|
| “minimal spanning forest” | Free **uniform** spanning forest. A uniform sample from finite spanning trees is different from the tree minimising IID edge weights. |
| “of Z^d” | The lattice is included in its graph class, in every positive integer dimension. This overlap of graphs does not identify the forest laws. |
| “iid uniform edge weights” | IID uniform **vertex labels** used to sample an unweighted FUSF law. These labels are not edge costs for minimisation. |
| “free and wired coincide” | The theorem samples the free uniform law; it does not establish the free/wired minimal-forest equality. |
| “a single tree for d<8” | No connectivity or dimension-threshold conclusion. |
| “infinitely many components for d>8” | No component-count conclusion. |
| Strength | Exact equality of a sampler's output law with FUSF, not a bound or a special case of the requested component theorem. |

The same introduction has a further main theorem (Theorem 1.3, “Strongly Rayleigh processes on countable groups”), exactly:

> Let \(\Gamma\) be a countable group and let \(\nu\) be a strongly Rayleigh
> probability law on \(\{0,1\}^{\Gamma}\) invariant under every \(\tau_g\).
> There is a Borel map
> \[
>  \Phi_\nu:[0,1]^{\Gamma}\longrightarrow\{0,1\}^{\Gamma}
> \]
> such that \(\Phi_\nu(\tau_g u)=\tau_g\Phi_\nu(u)\) for every \(g\in\Gamma\)
> and every \(u\in[0,1]^{\Gamma}\), and such that \(\Phi_\nu(U)\) has law \(\nu\)
> when the coordinates of \(U\) are independent \(\operatorname{Uniform}[0,1]\)
> variables.

Here \((\tau_g a)_h=a_{g^{-1}h}\). This too is a sampling statement with no minimal-forest component conclusion. Neither requested dimension range is covered.

## 2. Metric-measure limits of subcritical FK and spanning-tree planar maps — September 24, 2026

Author: OpenAI. Opened [build/main.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/build/main.tex), the [actual introduction/theorem source](https://raw.githubusercontent.com/openai/math/main/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/build/sections/01-introduction.tex), and the [manuscript README](https://raw.githubusercontent.com/openai/math/main/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/README.md).

Theorem 1.1 (“Metric and measure convergence”), exactly:

> For each fixed \(q\in(0,4)\) in the FK ensemble, and for the spanning-tree
> ensemble, there are deterministic positive numbers \(a_n\to0\) such that
> \[
>           (V(M_n),a_nd_n,\mu_n)
>              \xrightarrow[n\to\infty]{\mathrm{law}}
>           (S,D_h,\mu_h)
> \]
> in Gromov--Hausdorff--Prokhorov topology on compact metric probability
> spaces modulo measure-preserving isometry. The limit has the parameter
> specified above. Convergence holds through all positive integers \(n\);
> the root and decoration are forgotten.

The preceding definitions matter: \(M_n\) is a finite rooted planar map with n edges. The FK law on map/subgraph pairs is proportional to \(q^{\ell(M,A)/2}\); the spanning-tree law is uniform on rooted map–spanning-tree pairs. Distances use every primal edge, and \(\mu_n(v)=\deg_{M_n}(v)/(2n)\). The limiting sphere has \(\gamma\in(\sqrt2,2)\) given by \(q=2+2\cos(\pi\gamma^2/2)\), or \(\gamma=\sqrt2\) for spanning-tree maps.

| T049 phrase | What this theorem actually says |
|---|---|
| “minimal spanning forest” | FK-decorated or uniform-spanning-tree-decorated random planar maps. No minimum-weight optimisation. |
| “of Z^d” | Random finite spherical maps, allowing loops and multiple edges; not a fixed lattice in any dimension. |
| “iid uniform edge weights” | No such minimising edge costs; every primal edge has length one for graph distance. |
| “single tree” / “infinitely many components” | Convergence of the whole map as a compact metric probability space, with its decoration forgotten. Connectivity of a finite spanning-tree decoration is built into the ensemble and proves no infinite-lattice forest theorem. |
| “d<8” / “d>8” | Parameters are fixed q, LQG parameter gamma, and size n. None is the lattice dimension d. |
| Strength | A qualitative scaling limit, with unspecified deterministic distance normalisation; no component count or dimensional special case of T049. |

Neither requested range is covered. “Subcritical” here refers to LQG \(\gamma<2\), not subcritical lattice edge-weight percolation; the FK maps are at their self-dual critical point.

## 3. The sharp factor-of-IID threshold for the free Ising model on regular trees — September 26, 2026

Author: OpenAI. Opened [build/main.tex](https://raw.githubusercontent.com/openai/math/main/preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/build/main.tex), the [actual introduction/theorem source](https://raw.githubusercontent.com/openai/math/main/preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/build/sections/01-introduction.tex), lines 34–43, and the [manuscript README](https://raw.githubusercontent.com/openai/math/main/preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/README.md).

Theorem 1.1, exactly (retaining the equation-reference command from the TeX):

> For every integer \(d\ge3\) and every \(\beta\ge0\), the free zero-field
> Ising law \(\mu_{d,\beta}\) is a factor of IID in the sense of
> `\eqref{eq:equivariance}` if and only if
> \[
>                          \tanh\beta\le(d-1)^{-1/2}.
> \]
> In this range the factor can be chosen to commute with every
> automorphism on every label input.

The referenced convention is \(\Phi(gU)=g\Phi(U)\) almost surely for each fixed \(g\in\operatorname{Aut}(T_d)\); its exceptional null set may depend on g. The final sentence claims a version equivariant on every input.

| T049 phrase | What this theorem actually says |
|---|---|
| “minimal spanning forest” | A probability law on vertex spins in \(\{-1,1\}\); not a forest. |
| “of Z^d” | The infinite d-regular tree; d is vertex degree, not lattice dimension. Lattices in dimensions ≥2 have cycles. |
| “iid uniform edge weights” | IID uniform vertex labels used to generate correlated spins at inverse temperature beta. |
| “single tree” / “infinitely many components” | Whether the spin law is an IID factor. No random forest's components are counted. |
| “d<8” / “d>8” | All integer degrees d≥3, with a beta-dependent threshold; there is no transition at lattice dimension 8. |
| Strength | An exact iff sampling threshold, including equality. It is neither a bound nor a partial solution to the component-count conjecture. |

Neither requested range is covered. The word “free” means the free Ising state here, not the free minimal spanning forest.

## Follow-ups and formalisation

The following records were opened; later searches and any further findings are recorded below and in LOG.md.

- [Repository README](https://raw.githubusercontent.com/openai/math/main/README.md), [manuscript catalogue](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md), [history](https://raw.githubusercontent.com/openai/math/main/history.md), [Lean README](https://raw.githubusercontent.com/openai/math/main/lean/README.md), and [formalisation catalogue](https://raw.githubusercontent.com/openai/math/main/lean/formalization.yaml). The opened history ends on 29 October 2026 and names no withdrawal or correction for these three titles.
- FUSF: [Lean scope note 231](https://raw.githubusercontent.com/openai/math/main/lean/docs/231.md), [Comparator statement](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/FreeUniformSpanningForest.lean), [configuration](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/FreeUniformSpanningForest.json), and [solution entry point](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Probability/SpanningForest/Factor.lean). The solution theorem `OAI.Problem336.fusf_is_factor_iid` invokes `FinalFactor.exists_factor`. The scope is the universal FUSF sampler, not T049.
- Ising: [Lean scope note 236](https://raw.githubusercontent.com/openai/math/main/lean/docs/236.md), [Comparator statement](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/FreeIsing.lean), [configuration](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/FreeIsing.json), and [solution entry point](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Probability/FreeIsing/Main.lean). The solution states `OAI.Problem367.free_ising_factor_iff_threshold`; its proof uses imported variance/recovery results. The documented scope is almost-sure equivariance for each fixed automorphism and the threshold including equality, not finitary coding or the stronger every-input version. Neither is T049.
- The challenge files' `sorry` commands are placeholders for comparison with solutions, not evidence that the solution files themselves contain these gaps. The two configurations point to separate solution modules and permit only the usual `propext`, `Quot.sound`, and `Classical.choice` axioms. The [Comparator instructions](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/README.md) were opened. No Lean build or independent check of imported proof dependencies was performed.
- Planar maps: [Lean scope note 211](https://raw.githubusercontent.com/openai/math/main/lean/docs/211.md) covers **Brownian continuum random tree limits of finite Fortuin–Kasteleyn maps above four**, a different manuscript with q>4. It does not certify the candidate's q∈(0,4) or spanning-tree LQG claim. No entry for the candidate title was found in the opened formalisation catalogue.
- [Latent Seminar, “Sampling the free uniform spanning forest from IID labels”](https://lowrank.github.io/latent-seminar/OpenAI-Math/231-spanning-forest-factors), dated 6 October 2026, is a later exposition. It expressly limits its review to statements and selected mechanisms and does not independently verify the whole proof.
- [Community Ising record](https://mathcommunity.github.io/oai-math-revised/papers/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/) has no contributed notes; the additional notes are explicitly AI-collected on 21 October and unreviewed. This supplies no referee endorsement or refutation.

### Later material found and limits of the search

- Opened the [forest community record](https://mathcommunity.github.io/oai-math-revised/papers/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/), updated 4 November, and the [planar-map community record](https://mathcommunity.github.io/oai-math-revised/papers/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/), updated 9 November. Both say there are no contributed notes and distinguish unreviewed automatic notes from human review. The forest page reports Comparator acceptance on 26 October. Its [linked log](https://raw.githubusercontent.com/mathcommunity/oai-math-revised/main/checks/comparator-2026-10-26/logs/FreeUniformSpanningForest.log) was requested but could not be fetched, so acceptance is recorded as the page's report, not a log independently read. Opened the [community Lean-check documentation](https://raw.githubusercontent.com/mathcommunity/oai-math-revised/main/docs/LEAN_CHECKS.md). None of this checks a statement about minimal-forest components.
- Opened [Latent Seminar, “The sharp IID-factor threshold for free tree Ising spins”](https://lowrank.github.io/latent-seminar/OpenAI-Math/236-tree-ising-factors), dated 6 October 2026. Like its forest exposition, it expressly excludes independent verification of the complete proof.
- Opened [Perplexity, “Subcritical FK and Spanning-Tree Maps Converge to the Liouville Quantum Gravity Sphere”](https://orply.com/articles/perplexity/211-6-metric-measure-limits-of-subcritical-fk-and-spanning-tree-planar-maps-b2111b3c), 11 October 2026. It explains the candidate's claimed theorem; it supplies no referee report.
- Opened **Nina Holden**, *The Tutte embedding of tree-weighted planar maps converges to Liouville quantum gravity*, submitted 7 October 2026: [arXiv record](https://arxiv.org/abs/2610.10501) and [full HTML](https://arxiv.org/html/2610.10501). The author's statement after Section 1.3 names the candidate *Metric-measure limits of subcritical FK and spanning-tree planar maps* as an input to OpenAI's related linear-clock paper and says the released OpenAI papers solve several questions in the preceding future-directions discussion. This is a named expert's published acknowledgment of related claims, not a referee report, a check of the candidate's proof, or a minimal-spanning-forest result. Her own theorem concerns Tutte-embedded tree-weighted disks and random walks; it is independent work, not an arXiv version of the candidate.
- Opened **Nina Holden, Pu Yu**, *The circle packing and Riemann uniformization embedding of the tree-weighted planar maps converges to Liouville quantum gravity* (title as displayed on its arXiv abstract page), submitted 7 October 2026: [arXiv record](https://arxiv.org/abs/2610.10505) and [full HTML v1](https://arxiv.org/html/2610.10505v1). The HTML title instead reads “The circle packing and Riemann uniformization embedding of tree-weighted planar maps converge to Liouville quantum gravity”. Their statement immediately before the acknowledgements says that, to their knowledge, their results and the OpenAI results imply neither one another. This is an expert scope comment about related conformal-embedding work, not a review of the candidate's proof. It concerns neither T049 nor an arXiv version of the OpenAI preprint.

Searches used each exact candidate title with `arxiv error correction review` and with `refutation mistake gap` or `mistake gap referee`; separate `site:arxiv.org` title searches were also run. No arXiv version of any of the three candidates, specific refutation/error report, or formal referee report was found in those searches and the opened records. The named expert comment above and the expositions are the positive follow-up findings. An existing-issues search page linked by the Ising record could not be fetched; no claim of a complete issue-tracker audit is made. These are search findings as of 14 November, not proof that no other commentary exists.

## Check against the original model

Opened **Russell Lyons, Yuval Peres, Oded Schramm, “Minimal spanning forests”**, [arXiv page](https://arxiv.org/abs/math/0412263) and [full paper](https://arxiv.org/pdf/math/0412263), Annals of Probability 34 (2006), 1665–1692. Its introduction separately defines the minimal forest by deleting edges maximal on cycles and the uniform forest by limits of uniform spanning trees. It explicitly distinguishes the two laws and states that FMSF and WMSF agree on the lattice. Consequently, the shared words “free”, “spanning forest”, and “IID” do not connect the first candidate's theorem to T049.

The same paper's Question 6.8 asks which lattice dimensions give a single minimal tree and records the conjectural threshold 8, with the boundary dimension left uncertain. Question 6.10 separately asks whether the component count must be 1 or infinity. This independently confirms that the target is a component-count question, not an IID-factor question. This old paper is background evidence, not a November 2026 status survey; the current negative finding rests on the actual candidate theorems and the follow-up search.

## Recommended replacement for “where it stands”

The supplied status remains unchanged by these three preprints: the minimal spanning forest is a single tree on Z², while its component count in each dimension d≥3 remains open in the literature checked here. OpenAI's *The free uniform spanning forest is a factor of IID* (September 25, 2026) concerns sampling the uniform forest, and *Metric-measure limits of subcritical FK and spanning-tree planar maps* (September 24, 2026) concerns finite random maps. *The sharp factor-of-IID threshold for the free Ising model on regular trees* (September 26, 2026) concerns Ising spins, so none claims the dimension-8 minimal-forest conjecture.

## Spot check

Selected Lemma 4.1, “Deterministic inversion”, in the forest preprint's [decoder source](https://raw.githubusercontent.com/openai/math/main/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/build/sections/decoder.tex), lines 11–88. This is the step turning a posterior-response estimate into a measurable sampler driven only by independent noise. Without deterministic inversion, knowing that an already planted sample has Brownian innovations would not construct an IID factor.

The lemma assumes countable I, a jointly Borel drift b with values in [0,1]^I, and a finite constant L such that

\[
\sup_i|b_i(t,y)-b_i(t,y')|\le L\sup_j|y_j-y'_j|
\]

whenever the coordinate differences have finite supremum. It concludes that every coordinatewise continuous input w has a unique solution of

\[
Z_i(t)=w_i(t)+\int_0^t b_i(s,Z(s))\,ds,
\]

with a Borel, causal solution map respecting the drift's relabeling symmetries.

Rechecking the argument gives:

1. Set Z⁰=w and iterate the right-hand side. Borel bounded scalar integrands make every coordinate iterate continuous. The base increment is at most t. Induction and the response assumption give
   \[
   \sup_i|Z_i^{k+1}(t)-Z_i^k(t)|\le \frac{L^k t^{k+1}}{(k+1)!}.
   \]
   At each induction step the two fields do have bounded differences. On every finite time interval the majorants sum, so the iterates converge uniformly in the coordinate differences and in time. This does not require w itself to be bounded over I.
2. The same Lipschitz bound permits passage through each scalar integral. Any second solution differs from w by at most t; induction comparing that solution with the Picard iterates gives the same vanishing factorial remainder. Hence uniqueness holds. As a second check, two solutions differ by at most 2t, and their supremum discrepancy satisfies the integral Gronwall inequality with zero initial discrepancy; countability makes that supremum measurable.
3. Evaluation of a countable family of continuous paths is continuous in the product compact-open topology. Parameter integration of a bounded Borel integrand is Borel. Rational-time coordinate evaluations generate the path-space Borel sigma-field, so the iterates and their limit give a Borel solution map. Each iteration uses only earlier times and commutes with the specified coordinate relabelings, and these properties pass to the limit.

No gap was found in this lemma under its stated assumptions. This check does not establish that the actual forest drift satisfies those assumptions, verify the innovations argument or the whole paper, or alter the NOT-THIS verdict. No simulation or Lean compilation was used.

Task: “Verify: has open problem T049 been settled by the OpenAI math release?” — 14 November 2026; request clock time was not supplied.
