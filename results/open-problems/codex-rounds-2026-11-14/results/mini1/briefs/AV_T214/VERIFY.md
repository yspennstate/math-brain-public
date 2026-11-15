# T214 — free Ising on regular trees

Checked 14 November 2026. Verdict: SOLVED-CLAIMED. This is a report of the claimed theorem and available checking evidence, not a judgment that the preprint's proof is correct.

## Exact theorem statements and comparison

### 1. The sharp factor-of-IID threshold for the free Ising model on regular trees

OpenAI, September 26, 2026. Theorem 1.1, quoted verbatim from the [included introduction TeX](https://github.com/openai/math/blob/main/preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/build/sections/01-introduction.tex). The main TeX file, introduction and manuscript README were opened; exact copies are saved in `sources/`.

```tex
\begin{theorem}\label{thm:main}\label{thm:sharp}
For every integer $d\ge3$ and every $\beta\ge0$, the free zero-field
Ising law $\mu_{d,\beta}$ is a factor of IID in the sense of
\eqref{eq:equivariance} if and only if
\[
                         \tanh\beta\le(d-1)^{-1/2}.
\]
In this range the factor can be chosen to commute with every
automorphism on every label input.
\end{theorem}
```

Here equation (1.1), cited in the theorem, defines a measurable map from independent uniform vertex labels to spins, satisfying Φ(gU)=gΦ(U) almost surely for each fixed g in Aut(T_d). The introduction defines the free law by a fair starting spin and independent edge transitions with agreement probability (1+tanh β)/2. Thus it is the same free-boundary, zero-field ferromagnetic Gibbs measure as our row, not a wired state, gradient law, or finite-volume approximation.

| Our statement | Preprint | Comparison |
| --- | --- | --- |
| Infinite d-regular tree, d ≥ 3 | T_d infinite, every integer d ≥ 3 | Exact graph and degree range; d=3 included |
| Zero-field ferromagnetic Ising, free boundary | Free zero-field Ising, β ≥ 0, specified broadcast cylinders | Same spin law; μ_β versus μ_{d,β} is notation |
| tanh β ≤ (d−1)^(−1/2) | The identical inequality, explicitly including equality | Entire requested range; no small universal constant and no large-degree restriction |
| Aut(T_d)-equivariant | Almost-sure equivariance for each fixed automorphism, plus an everywhere-equivariant version | Covers the requested symmetry under either convention |
| Measurable factor of IID labels | Borel factor of independent Uniform[0,1] vertex labels | Exact-law construction, not just a bound, asymptotic, or weak limit |
| Positive implication in this range | If and only if | Claims our whole statement and recalls the known strict converse |

The statement is for each fixed (d,β). It does not claim finitary coding, coding-radius bounds, a practical sampling algorithm, parameter-uniform coding, antiferromagnetism, or a result on other graphs. None of these is required by our row.

### 2. The free uniform spanning forest is a factor of IID

OpenAI, September 25, 2026. Theorem 1.1, quoted verbatim from the [included introduction TeX](https://github.com/openai/math/blob/main/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/build/sections/introduction.tex). The main TeX file, introduction and manuscript README were opened; exact copies are saved in `sources/`.

```tex
\begin{theorem}\label{thm:main}
There is one Borel, root-independent, equivariant rule
\[
 \Phi(G,U,e)\in\{0,1\}
\]
such that, for every infinite connected locally finite simple undirected
unweighted graph $G$ and independent
$\operatorname{Uniform}[0,1]$ vertex labels $U=(U_v)_{v\in V(G)}$, the entire
edge set
\[
 \{e\in E(G):\Phi(G,U,e)=1\}
\]
has law $\FUSF_G$.
\end{theorem}
```

In this quote `\FUSF_G` denotes the free uniform spanning forest law. This samples an edge subset of a fixed graph, with no inverse temperature or Ising spin distribution. Even on T_d the free forest is deterministic: every finite connected subtree is already its unique spanning tree, so the limit contains every edge. Producing that forest provides no assignment of correlated ±1 spins. The paper's further theorem for invariant strongly Rayleigh laws on countable groups does not assert the ferromagnetic Ising spin law is in that class or construct it; its introduction instead cites the sharp-Ising paper as a companion using a different recovery argument. Candidate verdict: NOT-THIS for T214.

### 3. Metric-measure limits of subcritical FK and spanning-tree planar maps

OpenAI, September 24, 2026. Theorem 1.1, quoted verbatim from the [included introduction TeX](https://github.com/openai/math/blob/main/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/build/sections/01-introduction.tex). The main TeX file, introduction and manuscript README were opened; exact copies are saved in `sources/`.

```tex
\begin{theorem}[Metric and measure convergence]\label{thm:main}\label{tree:thm:main}
For each fixed \(q\in(0,4)\) in the FK ensemble, and for the spanning-tree
ensemble, there are deterministic positive numbers \(a_n\to0\) such that
\[
          (V(M_n),a_nd_n,\mu_n)
             \xrightarrow[n\to\infty]{\mathrm{law}}
          (S,D_h,\mu_h)
\]
in Gromov--Hausdorff--Prokhorov topology on compact metric probability
spaces modulo measure-preserving isometry. The limit has the parameter
specified above. Convergence holds through all positive integers \(n\);
the root and decoration are forgotten.
\end{theorem}
```

The preceding definitions set d_n to distance using all primal edges, μ_n(v)=deg(v)/(2n), and q=2+2 cos(πγ²/2), with γ in (√2,2) for FK and γ=√2 for spanning-tree maps. The limit is an ordinary unit-area γ-LQG sphere. This concerns finite random planar maps, followed by a Gromov–Hausdorff–Prokhorov scaling limit, not an infinite fixed regular tree or an IID spin factor. The q=2 FK–Ising instance remains a planar-map metric statement; it gives no β range, Aut(T_d) map, or exact Ising sampler. The deterministic normalizations a_n and convergence in law are entirely different quantities from the existence of a measurable factor. Candidate verdict: NOT-THIS for T214.

## Formalisation opened

- [Repository README](https://github.com/openai/math/blob/main/README.md), [history](https://github.com/openai/math/blob/main/history.md), [formalisation catalogue](https://github.com/openai/math/blob/main/lean/formalization.yaml), [Lean README](https://github.com/openai/math/blob/main/lean/README.md), and [Comparator instructions](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/README.md). The README describes model-produced research data at differing verification stages. History through 29 October lists no Ising-specific correction or withdrawal.
- [Ising scope note, family 236](https://github.com/openai/math/blob/main/lean/docs/236.md), [challenge statement](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/FreeIsing.lean), [configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/FreeIsing.json), [solution Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/FreeIsing/Main.lean), and [Model.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/FreeIsing/Model.lean). The catalogue links `OAI.Problem367.free_ising_factor_iff_threshold` to this manuscript. Namespace Problem367 is not family 367; `lean/docs/367.md`, also opened, concerns a different problem.

The solution's statement is:

```lean
theorem free_ising_factor_iff_threshold :
    ∀ (d : ℕ) (beta : ℝ), 3 ≤ d → 0 ≤ beta → (IsFactorOfIID d (Real.tanh beta) ↔ Real.tanh beta ≤ 1 / Real.sqrt ((d : ℝ) - 1))
```

The definitions use reduced words with adjacent unequal letters in Fin d for T_d, all adjacency-preserving bijections for its automorphisms, independent uniform vertex labels, and the free Ising connected-cylinder probabilities. `IsFactorOfIID` quantifies an actual measurable map with the correct pushforward law and almost-sure equivariance separately for each automorphism. This matches our requested measurable-factor statement including equality. The selected declaration does not itself assert the paper's extra everywhere-equivariant version. The challenge's `sorry` is a statement placeholder, with the proof supplied separately in the solution module; the configuration permits only `propext`, `Quot.sound`, and `Classical.choice`, with no definition holes.

Opened the [forest scope note](https://github.com/openai/math/blob/main/lean/docs/231.md), which links the forest and strongly-Rayleigh results. Opened the [maps family scope note](https://github.com/openai/math/blob/main/lean/docs/211.md): it links only the separate q>4 continuum-random-tree paper. A Lean result for that family must not be credited as a formalisation of this q∈(0,4) paper.

## Follow-ups and checks

Absence statements describe this search as of 14 November 2026, not proof that no later item exists.

1. **Matching formal-check reports, opened directly.** [MathVet's fidelity table](https://github.com/mathvet/mathvet/blob/14c7f918cd336d0da03a02aae5a0eed4a429d4db/reviews/openai-math/fidelity-table.csv) classifies family 236 as full coverage; its [challenge-status table](https://github.com/mathvet/mathvet/blob/14c7f918cd336d0da03a02aae5a0eed4a429d4db/reviews/openai-math/challenge-status.csv) reports a sandboxed Comparator pass for FreeIsing at 2026-10-08 19:33 UTC, against the release's `fd4aeeb` challenge. These are primary records of the checking project's own assessment, not a referee report.
2. **Second checker, opened directly.** Carlos Toledo's cert-machine [statement assessment](https://github.com/carlostoledo1891/cert-machine/blob/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-statements.json) marks family 236 MATCHES, with both the iff threshold and automorphism equivariance covered. Its [kernel record](https://github.com/carlostoledo1891/cert-machine/blob/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-kernel.json) reports a successful FreeIsing Comparator run at 2026-10-10 09:06 UTC with both Lean's kernel and nanoda accepting and zero definition holes. Relevant entries are preserved in `sources/outside-check-records.md`. This report does not independently reproduce those runs.
3. **Later community check, opened directly.** The [mathcommunity FreeIsing log](https://github.com/mathcommunity/oai-math-revised/blob/main/checks/comparator-2026-10-26/logs/FreeIsing.log), saved locally, ends in kernel acceptance and successful comparison. The accompanying [checking notes](https://github.com/mathcommunity/oai-math-revised/blob/main/docs/LEAN_CHECKS.md) date the runs to 25–26 October and disclose agent operation and precompiled proof modules in the same workspace. They distinguish formal-statement checking from manuscript review. Nanoda was not enabled for FreeIsing in this particular run; the independent-kernel claim above comes from cert-machine instead.
4. **Expositions actually opened.** Latent Seminar's [The sharp IID-factor threshold for free tree Ising spins](https://lowrank.github.io/latent-seminar/OpenAI-Math/236-tree-ising-factors) and [Sampling the free uniform spanning forest from IID labels](https://lowrank.github.io/latent-seminar/OpenAI-Math/231-spanning-forest-factors), both dated 6 October 2026, explain the respective mechanisms while expressly excluding independent verification of the complete proofs. The [Plectis Atlas FreeIsing page](https://wcook04.github.io/plectis-atlas/statements/FreeIsing.html) was opened as a route to the original checking records; its own source comparison distinguishes the paper's everywhere-equivariant version from the selected Lean statement.
5. **Community manuscript pages actually opened.** The mathcommunity pages for [Ising](https://mathcommunity.github.io/oai-math-revised/papers/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/), [forest](https://mathcommunity.github.io/oai-math-revised/papers/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/), and [planar maps](https://mathcommunity.github.io/oai-math-revised/papers/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/) displayed no reader notes. Their automatically collected literature links were treated as leads and checked against original sources where used.
6. **Later planar-map literature actually opened.** Nina Holden, [The Tutte embedding of tree-weighted planar maps converges to Liouville quantum gravity](https://arxiv.org/abs/2610.10501), submitted 7 October 2026: abstract page, HTML v1 and PDF opened. It concerns conformal embedding of tree-weighted maps with boundary. Nina Holden and Pu Yu, [The circle packing and Riemann uniformization embedding of the tree-weighted planar maps converges to Liouville quantum gravity](https://arxiv.org/abs/2610.10505), submitted 7 October 2026: abstract page and HTML v1 opened. The latter paper's introductory statement says its results and the OpenAI results do not imply one another. These are related map papers, not versions or confirmations of T214. The community catalogue attributes an OpenAI-related comment to Holden's single-author paper, but an `OpenAI` search in both the opened HTML and PDF found none; that catalogue attribution is not adopted here.
7. **Prior baseline actually opened.** Danny Nam, Allan Sly, and Lingfu Zhang, [Ising model on trees and factors of IID](https://arxiv.org/abs/2012.09484), arXiv:2012.09484v2, revised 22 January 2022: the abstract page confirms the free ferromagnetic regular-tree model, the known uniqueness and reconstruction ranges, and their construction with an absolute constant times the reconstruction scale. This is prior work, not a follow-up to the release.

Web searches used the three exact titles and combinations with arXiv, error, gap, refutation, proof, review, and referee; additional searches combined OpenAI, free Ising, factor, and MathOverflow. No matching arXiv version of any of the three OpenAI manuscripts was located. No Ising-specific refutation, error report, refereed publication, or named specialist endorsement of its proof was located in the opened sources. The two later map papers and the formal-check reports are the concrete follow-ups found. Search also located AI Proved What and DiscoverIA Ising pages, but attempted opens returned cache misses; their snippets are not evidence for a finding in this report.

## Recommended replacement for our row

OpenAI's preprint *The sharp factor-of-IID threshold for the free Ising model on regular trees* (September 26, 2026) claims the full nonreconstruction range tanh(β)≤(d−1)^(−1/2) for every d≥3, including equality. A matching Lean theorem and solution are supplied, with outside reports of successful Comparator checks. Record the row as solved-claimed; no refereed publication or specialist endorsement was located in the sources checked.

## Spot check

Selected **Lemma 8.2, Small-time log-factor estimate**, in [the critical-comparison section](https://github.com/openai/math/blob/main/preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/build/sections/08-critical-comparison.tex), saved as `sources/ising-critical-comparison.tex`. This is the decisive small-time endpoint estimate: the path sums produce S(t)/t, so the crude S≤CV would not give an integrable coefficient. Its claim is

\[
S(t)\le C_TV(t)\left(t^{1/4}+\frac{1+\log(K_T/V(t))}{\log^2(1/t)}\right),
\]

for sufficiently small positive t with V(t)>0. Here V is the mean-square site-field discrepancy of the conditional copies, S is their mean-square discrepancy in log a on a directed edge, a(z)=(1−tanh²z)/(1−θ²tanh²z), and θ=(d−1)^(−1/2). The check below assumes the earlier cavity identities, uniform discrepancy bound H_T, invariance of the two-copy law, and Lemma 8.1's one-copy tail estimate; it does not verify all those upstream results.

Let Y,Y′ be the two cavity fields on an edge, and Z,Z′ those on its reverse. The two site equations are h_j=Y+ψ(Z), h_i=Z+ψ(Y), with |ψ′|≤θ. Subtracting and eliminating ΔZ gives

\[
(1-\theta^2)|\Delta Y|\le |\Delta h_j|+\theta|\Delta h_i|.
\]

Minkowski's inequality and invariance give ||ΔY||₂≤√V/(1−θ); the deterministic bound similarly gives |ΔY|≤H_T/(1−θ). Thus the constants and denominator used by the lemma are consistent.

Differentiating directly, with x=tanh z, gives

\[
(\log a)'(z)=-\frac{2(1-\theta^2)x}{1-\theta^2x^2}.
\]

Its magnitude is at most 2|x|≤2|z| and at most 2. On |Y|,|Y′|≤t^(1/8), the mean-value theorem therefore bounds the contribution to S by 4t^(1/4)V/(1−θ)². On the complement, the global derivative bound gives CV, while the bounded discrepancy and the union of the two marginal tail events give C_T exp(−cJ), where J=log²(1/t). No independence of Y and Y′ is used. The total is consequently bounded by

\[
C t^{1/4}V+\min\{CV,C_T e^{-cJ}\}.
\]

Put u=V and I=1+log(K_T/u), with K_T>max(1,H_T²). If u≤exp(−cJ/2), then I≥cJ/2 and the first branch of the minimum is at most C uI/J. If u>exp(−cJ/2), the second branch divided by u is at most C_T exp(−cJ/2), and J exp(−cJ/2) is bounded. Since I≥1, this also gives C_T uI/J. This proves precisely the displayed lemma under its stated upstream inputs, including when V≥1.

As a separate check of its purpose, dividing the estimate by t gives V times t^(−3/4)+I/[t log²(1/t)]. The two time coefficients are integrable at zero: their integrals up to ε are 4ε^(1/4) and 1/log(1/ε). The ensuing Osgood argument also has the required divergent state integral: integrating du/[u(1+log(K_T/u))] toward zero diverges. These magnitude, sign, and endpoint checks found no defect in Lemma 8.2's argument conditional on its inputs. They do not certify the full critical path estimates, the stochastic coupling, or the paper's proof.

