# T304: scope of the OpenAI claims

Verification date: 14 November 2026. Author of all three candidate manuscripts: **OpenAI**, as printed in their TeX title blocks and citation READMEs. This report distinguishes theorem claims from proof correctness.

The relevant claim is partial: it fixes the best polynomial dimension exponent in a normalized, fixed-accuracy oracle model. It does not determine the query complexity as a function of dimension, condition number, and accuracy requested by T304.

## 1. Subpolynomial query complexity for well-conditioned log-concave sampling

OpenAI, September 26, 2026. [Manuscript](https://github.com/openai/math/blob/main/preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/article.pdf); [main theorem and model in the original TeX](https://github.com/openai/math/blob/main/preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/build/sections/introduction.tex).

Theorem 1.1 is copied verbatim below, as TeX. The paper's model immediately before it is: d≥2, V∈C²(Rᵈ), V(0)=0, ∇V(0)=0, and I≼∇²V(x)≼2I for every x. A query returns both V(x) and ∇V(x) exactly. Measurable adaptive randomized algorithms have unrestricted computation between queries. Q(d) is the minimum query cap on **every execution** needed for TV error at most 1/10, uniformly over this class.

```tex
\begin{theorem}\label{thm:main}
In the oracle model above, for every \(\varepsilon>0\)
there is \(C_\varepsilon<\infty\) such that
\[
                  Q(d)\le C_\varepsilon d^\varepsilon
                  \qquad(d\ge2).
\]
There are also absolute constants \(c>0\) and \(d_0\)
such that
\[
                  Q(d)\ge c\log d\qquad(d\ge d_0).
\]
The lower bound applies to arbitrary randomized adaptive
first-order algorithms. In particular, \(\gamma_*=0\).
\end{theorem}
```

## 2. A Nearly Quartic Separation Between Randomized and Quantum Query Complexity

OpenAI, October 5, 2026. [Manuscript](https://github.com/openai/math/blob/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf); [main theorem in the original TeX](https://github.com/openai/math/blob/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/build/sections/01-introduction.tex).

Theorem 1.1, verbatim TeX (R and Q denote randomized and quantum bounded-error **bit** query complexity of total Boolean functions; error is at most 1/3 on every input):

```tex
\begin{theorem}\label{thm:main}
The optimal power is $\alpha_{\mathrm{tot}}=4$.
More precisely, $\R(f)=O((1+\Q(f))^4)$ for every total Boolean function.
For each fixed integer $k\ge2$, there are positive constants $c_k,C_k,b_k$
and total Boolean functions $F_{k,m}$, for all sufficiently large powers
of four $m$, such that
\begin{equation}\label{eq:main-family}
 \Q(F_{k,m})\le C_k\sqrt m\,(\log m)^{b_k},
 \qquad
 \R(F_{k,m})\ge c_k\frac{m^{2-1/k}}{(\log m)^2}.
\end{equation}
\end{theorem}
```

## 3. A dimension-free logarithmic Sobolev inequality for subgaussian log-concave measures

OpenAI, September 23, 2026. [Manuscript](https://github.com/openai/math/blob/main/preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/paper.pdf); [main theorem in the original TeX](https://github.com/openai/math/blob/main/preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/build/sections/01-introduction.tex).

The marginal condition referenced in the theorem is sup over unit θ of E exp(⟨X,θ⟩²/a²)≤2. D denotes the Euclidean gradient. Theorem 1.1, verbatim TeX:

```tex
\begin{theorem}\label{thm:main}
There is an absolute constant \(C<\infty\) with the following property.
For every \(n\ge1\), every centered log-concave probability measure
\(\mu\) with a Lebesgue density on \(\R^n\), and every \(a>0\)
satisfying \eqref{eq:intro-subgaussian} for \(X\sim\mu\),
\[
 \Ent_\mu(f^2)\le C a^2\int_{\R^n}|Df|^2\,d\mu
 \qquad\text{for every }f\in C_c^\infty(\R^n).
\]
The same constant works in every dimension.
\end{theorem}
```

## Detailed comparison with our statement

### Candidate 1: PARTIAL-CLAIMED

To avoid confusing two different epsilons, write δ for the preprint's arbitrary positive dimension exponent, and ε for the sampling tolerance in T304.

| Words in T304 | What the preprint actually asserts | Scope comparison |
| --- | --- | --- |
| “targets π ∝ exp(−f) on Rᵈ” | π_V ∝ exp(−V) on Rᵈ | Same target form. |
| “f m-strongly convex and L-smooth” | V∈C², I≼∇²V≼2I, V(0)=0, ∇V(0)=0 | A subclass. T304 does not explicitly require C² or a supplied minimizer. The value normalization is harmless; knowing the minimizer is information. |
| “condition number κ=L/m” | Lower curvature 1 and upper curvature 2 | Covers the class with condition number at most 2. Rescaling handles a known positive lower curvature m and L≤2m, with a supplied mode; it does not turn general κ into 2. |
| “as a function of d” | Every integer d≥2; eventual logarithmic lower bound | General dimension, not a one-dimensional or product-target result. |
| “gradient (or value) queries” | Each exact query returns the pair (V(x),∇V(x)) | A joint oracle. Section 8 says the main large-dimension construction uses only gradients, while its bounded-dimension fallback uses values too. The stated theorem is not a value-only theorem, nor a complete separate treatment of both oracle models. |
| “output a sample within total variation ε” | TV≤1/10, uniformly over the normalized class | Same distance, one fixed accuracy. The theorem gives no rate in ε. Its C_δ is indexed by the exponent, not an error tolerance. |
| “or Wasserstein ε·sqrt(d/m)” | No corresponding final-target Wasserstein query-complexity theorem in the main statement | Intermediate W₂ estimates used to prove the TV bound do not state the requested Wasserstein accuracy tradeoff. TV error alone does not control W₂ for arbitrary sampler outputs. |
| “minimal number” | c log d≤Q(d)≤C_δ d^δ for every δ>0 | Upper and lower bounds, not a matching asymptotic query rate. Only the infimal polynomial exponent is claimed to equal zero. |
| “MALA from a warm start” | No warm sample is an input; the upper construction starts at the supplied mode | Not the same initialization model. With the supplied mode, a warm sample could simply be ignored, so its absence is not an obstruction to the upper bound; a warm sample alone is not a supplied mode. The preprint's lower theorem does not state a warm-start lower bound. |
| “d^{1/3} … and d^{1/2} … optimal in their respective accuracy regimes” | Every fixed positive power can be beaten in the stated κ≤2, known-mode, constant-TV-error model | Claims that these positive powers are unnecessary in that restricted minimax model. It neither proves optimality of either algorithm nor settles all their Wasserstein and high-accuracy regimes. |
| Query budget | A deterministic cap on every execution, with free unrestricted real computation between calls | Stronger than an expected-query bound, but not a polynomial-time or finite-precision algorithm guarantee. |

Thus the claim changes the constant-accuracy dimension picture substantially. It does not answer the full T304 question. In particular, exponent zero allows super-polylogarithmic growth such as exp((log d)^{1/3}); no contradiction with the November lower bound follows.

### Candidate 2: NOT-THIS

The input is a total Boolean function f:{0,1}ⁿ→{0,1}, and the output is one bit correct with probability at least 2/3. R and Q count classical randomized and quantum **input-bit** queries; they do not count potential or gradient evaluations. The parameter m in F_{k,m} is a construction size, unrelated to the strong-convexity parameter m in T304.

The equality α_tot=4 is a sharp universal **exponent** relating two Boolean decision complexities. The displayed family has a quantum upper bound and a randomized lower bound approaching that exponent; it is not a sampling bound, a bound in κ, a TV/Wasserstein guarantee, or a result about a warm start. The word “query” is the only substantive overlap.

### Candidate 3: NOT-THIS

This is an entropy inequality for centered log-concave Lebesgue densities with uniformly subgaussian linear marginals. Its gradient Df acts on a test function in the Dirichlet energy, not on a potential queried by an algorithm. The theorem holds in every n≥1 and is dimension-free in its inequality constant; it counts no oracle operations and supplies no sampler.

Strong log-concavity is compatible with the hypotheses after centering, but the target class is different: positive lower curvature and smoothness are unnecessary, and uniform laws on convex bodies are included. The paper itself recalls the classical dimension-free log-Sobolev inequality under positive lower curvature. Its transport-entropy corollary controls W₂² by relative entropy; it does not give an algorithm, an oracle budget, or the requested optimal dependence on d, κ, or sampling error. It therefore does not settle T304 even if its theorem is correct.

## Follow-ups actually opened

Searches were made on 14 November 2026 using the web search tool, including all three titles with arXiv, error, correction, review, refutation, and related author/topic terms. The following are positive findings; absence statements below mean “not found in these searches,” not that none can exist.

### Sampling paper

1. **Huanjian Zhou and Taiji Suzuki**, [*Towards the Query Complexity of Sampling under Strong Log-Concavity and Log-Sobolev Inequalities*](https://arxiv.org/abs/2611.05813), arXiv:2611.05813v1, submitted 4 November 2026. Opened the abstract and [full HTML](https://arxiv.org/html/2611.05813v1), especially the results table, Theorem 1 discussion, and references. They explicitly combine OpenAI's subpolynomial upper bound with their exp(Ω((log d)^{1/3})) lower bound at κ=2 and TV error 1/10. Their discussion says the lower bound persists with a constant warm start and both mode and mean known to be zero. This is later mathematical engagement and a stronger lower bound, not a refutation or a matching rate. It corrects the old row's omission of the subpolynomial upper claim.

2. **Wei Guo, Bo Yuan, Ye He, Jiaming Liang, Molei Tao, and Yongxin Chen**, [*Subpolynomial-Query Proximal Sampling Beyond Log-Concavity*](https://arxiv.org/abs/2611.03442), arXiv:2611.03442v1, submitted 2 November 2026. Opened the abstract and [full HTML](https://arxiv.org/html/2611.03442v1), including main assumptions/results and Appendix B.1. They use OpenAI's noisy conditional sampler. Under β-smoothness and α-LSI, their claimed gradient-only deterministic query cap for TV error ε is
   \[
   C_ν κ(d+κ+ε^{-1}+G₀)^ν,  κ=β/α,  G₀=||∇V(x₀)||²/β,
   \]
   for every fixed ν>0, starting from N(x₀,β^{-1}I). Strongly convex smooth targets are included via LSI. This extends conditioning, accuracy, and initialization coverage, while importing the OpenAI derivative and recursive implementation estimates. It does not establish an optimal κ or accuracy rate, and its inverse-accuracy dependence is not a polylogarithmic bound. It is a dependent extension, not independent verification of the imported proof.

3. **Evan Dogariu**, [*Sharp Lower Bounds for Parallel Log-Concave Sampling*](https://arxiv.org/abs/2611.15849), arXiv:2611.15849v1, submitted 11 November 2026. Opened abstract and [full HTML](https://arxiv.org/html/2611.15849v1), especially related work. It cites both OpenAI and Zhou–Suzuki; its principal bounds concern parallel rounds with a width constraint and Gaussian depth-width tradeoffs. They do not close the sequential total-query gap in T304.

4. [Latent Seminar, *Subpolynomial queries for log-concave sampling*](https://lowrank.github.io/latent-seminar/OpenAI-Math/139-log-concave-sampling-queries), 7 October 2026, and [Closed Form's sampling exposition](https://closedform.nishachay.tech/e/openai-math-2026-139/) were opened. They explain the claim; they do not supply an independent full proof review. Closed Form explicitly labels its explanation AI-generated.

5. Opened the [Plectis Atlas statement page](https://wcook04.github.io/plectis-atlas/statements/LogConcaveQuery.html) and the [community collection's paper page](https://mathcommunity.github.io/oai-math-revised/papers/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/). The latter has no contributed named notes and labels its automatically collected material unreviewed. Followed its [Samplinglib PR 314](https://github.com/DakeBU/Automization-Sampling-Optimisation-Geometry-Lib/pull/314): it is an integration protocol separating reusable leaves from the source-specific proof route, not a certificate that T304 is settled.

### Boolean query paper

Opened the [community paper page](https://mathcommunity.github.io/oai-math-revised/papers/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/), the [Open Mathematics Courses exposition](https://kokunoyumeto.github.io/open-math-courses-public/courses/randomized-versus-quantum-query-complexity/), and [AI Proof Watch's 18 October assessment](https://aiproofwatch.com/updates/openai-reports-a-nearly-quartic-quantum-query-separation-75dd39e7). These do not document a completed independent expert verification.

Also opened [kusasyu36/openai-math-audit's original audit report 284](https://github.com/kusasyu36/openai-math-audit/blob/main/audits/284/REPORT.md), dated 29 October 2026. It explicitly identifies a Claude subagent as auditor. It reports no clear error in the portions examined, distinguishes an exponent tending to four from a single quartic-up-to-polylogarithms separation, and leaves selected steps for expert checking. This is an AI-assisted audit report, not a referee report. No inference about sampling follows from it.

### Sobolev paper

**Shuchen Li and Ilias Zadik**, [*Functional inequalities from the fundamental limits of Bayesian estimation*](https://arxiv.org/abs/2611.05831), arXiv:2611.05831v1, submitted 4 November 2026. Opened abstract and [full HTML](https://arxiv.org/html/2611.05831v1), including Section 1.2. They contrast their dimension-dependent log-Sobolev bound with OpenAI's dimension-free claim and explicitly say they have not verified OpenAI's proof. This is a later expert-authored comment, not a validation or refutation.

Opened [Latent Seminar's Sobolev exposition](https://lowrank.github.io/latent-seminar/OpenAI-Math/093-subgaussian-log-sobolev), 6 October 2026, and the [community paper page](https://mathcommunity.github.io/oai-math-revised/papers/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/). The exposition disclaims independent complete-proof verification; the community page has no contributed named notes.

### Corrections, arXiv versions, and formalization

- Opened the [release README](https://github.com/openai/math/blob/main/README.md), [history](https://github.com/openai/math/blob/main/history.md), and each candidate's citation README. The history records corrections and withdrawals of other manuscripts, but none for these three; their READMEs contain no withdrawal/error notice. No separate arXiv version of any of the three OpenAI candidates was located. The November papers above are distinct later papers.
- No specific refutation or referee report for these candidates was located. The searches did find the AI audit and later discussions just described. These are not interchangeable forms of verification.
- Opened the [Lean README](https://github.com/openai/math/blob/main/lean/README.md), [formalization catalogue](https://github.com/openai/math/blob/main/lean/formalization.yaml), full lean/docs/ directory listing, and [scope note 139](https://github.com/openai/math/blob/main/lean/docs/139.md). The catalogue and note associate the sampling result with `OAI.LogConcaveSampling.exact_source_main`.
- Opened [Comparator statement](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/LogConcaveQuery.lean), [Comparator configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/LogConcaveQuery.json), [solution Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/LogConcave/Main.lean), and [Model.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/LogConcave/Model.lean). The exposed definitions include the C² curvature class, normalized Gibbs law, measurable adaptive oracle algorithms, and TV≤1/10; the top-level solution combines upper, logarithmic lower, and exponent-zero theorems. The challenge file ends in a placeholder `sorry`; the separate solution supplies the proof. The configuration permits only `propext`, `Quot.sound`, and `Classical.choice`. These are inspected source artifacts; the full import graph was not rebuilt or audited here.
- No matching formalization entry or scope note was found for the Boolean-query or Sobolev candidate. The paths `lean/docs/284.md` and `lean/docs/093.md` return 404 and are absent from the directory listing. Root `docs/` also returns 404; the documentation consulted is in `lean/docs/`.

The original TeX and selected Lean/release files actually retrieved are saved under `sources/`; failed fetches and the search trail are recorded in LOG.md. No third-party catalogue label has been used as proof of correctness.

## Recommended replacement for “where it stands”

Open in full: OpenAI's “Subpolynomial query complexity for well-conditioned log-concave sampling” (September 26, 2026), with a supplied Lean formalization, claims fewer than any fixed positive power of dimension in exact value-and-gradient queries for twice continuously differentiable targets with a known minimizer, condition number at most 2, and TV error 1/10. Zhou and Suzuki's November 2026 lower bound rules out polylogarithmic queries even in this regime, leaving a gap within subpolynomial growth. Later work extends the upper-bound construction to general smooth targets satisfying a log-Sobolev inequality, but the optimal joint dependence on dimension, condition number and accuracy, and the full Wasserstein and high-accuracy regimes in our row, remain unresolved.

## Spot check

Selected the Gaussian-center absorption lemma, Lemma 7.1 (`lem:compiler-absorption`) in [the original implementation section](https://github.com/openai/math/blob/main/preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/build/sections/implementation.tex). It is the central identity permitting a recursively computed conditional mean to be implemented at a noisy center without treating exact conditional means as free oracles. This check concerns that lemma and its conditional use, not all derivative estimates or the complete sampler.

Assume the deterministic, query-preserving identity
\[
 Q(x+\Delta;z+v\otimes\Delta/r)=Q(x;z),
 \qquad \|v\|\le D_s.
\]
Set a=v/(2D_s), n=r/(2D_s), and P=(I-aaᵀ)^{1/2}. Then ||a||≤1/2, so P exists and its eigenvalues are between sqrt(3)/2 and 1. For independent standard Gaussian Z and slot array G, the translation identity gives, pointwise,
\[
 Q(x+nZ;PG)=Q(x;PG-a\otimes Z).
\]
The sign is negative: translate the call back from x+nZ to x. The restored array H=PG−a⊗Z is jointly Gaussian and
\[
 \operatorname{Cov}(H)=(PP^T+aa^T)\otimes I_d=I_m\otimes I_d.
\]
Equivalently, for arbitrary test slot vectors t_j its characteristic function is exp(−(Σ_j|t_j|²)/2). Thus its slots really are independent standard Gaussians, not merely uncorrelated variables. This verifies the claimed equality in output law and the physical-query identity.

The restored seeds are correlated with Z: Cov(H,Z)=−a⊗I_d. The lemma only asserts a marginal law, so it would be invalid to condition again on the noisy center and claim the restored seeds are fresh. In the preprint's accuracy induction, it instead conditions on parent anchors, making the intended exact center deterministic, uses disjoint fresh term blocks, and invokes fixed-seed stability to compare an inaccurate center with an ideal x+nZ **before** absorption. Under precisely those stated independence assumptions the conditional version is valid; it does not assume that actual intermediate centers are already exact.

The corresponding [Lean noisy-center squared-error statement](https://github.com/openai/math/blob/main/lean/OAI/Probability/LogConcave/OraclePrograms/NoisyCenterSquaredError.lean) was also opened. It explicitly assumes the anchor/noise product law and fixed-seed Lipschitz bound and separates the center error from the standalone routine error. No defect was found in this Gaussian identity or in those stated conditional hypotheses. This local check does not certify that every required shift, stability, tensor, and recursion estimate in the full construction has been proved.


