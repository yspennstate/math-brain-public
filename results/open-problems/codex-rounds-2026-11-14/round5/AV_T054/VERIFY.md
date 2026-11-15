# T054 verification, round 5

Checked 15 November 2026, +04. The release-scope assessment remains PARTIAL-CLAIMED: the clean OpenAI main theorem claims bulk eigenvalue point-process universality and imports delocalization, without stating spatial QUE. REPORT.md follows the later continuation instructions and records the new concentration result, not a correctness judgment on the OpenAI proof.

The earlier round-4 claim holds after independent algebraic re-derivation and a rerun of its exact audit. This continuation sharpens its prescribed-set relative QUE estimate: if all unit eigenvectors satisfy ||u||_infinity<=L/sqrt(N) outside probability epsilon, and eigenspaces have dimension at most M, then for a prescribed k-subset, q=min(k,N-k),
\[
 \mathbb P\{\text{maximum relative discrepancy}>r\}
 \le \varepsilon+2N9^M
       \exp\left[-\frac{k^2r^2}{8L^2(q+kr/6)}\right].
\]
Here the maximum is over every unit eigenvector, including every vector in a repeated eigenspace. One can take M<=L^2, so k/[L^2(L^2+log N)] tending to infinity suffices, compared with the earlier k/(L^8 log N) condition. PROOF.md states and proves the result, its explicit error scale, its simple-spectrum specialization and its limits.

## Our statement and quantifiers

“For fixed d ≥ 3, the adjacency eigenvalues of a uniform random d-regular graph on N vertices have GOE local statistics in the bulk of the Kesten–McKay law as N → ∞, and the eigenvectors are delocalized and satisfy quantum unique ergodicity.”

The clean model below is simple and labelled. For each prescribed deterministic bounded vertex observable, the earlier round-3 argument gives absolute QUE in probability, uniformly over all unit eigenvectors, from known complete delocalization and label symmetry. The present extension concerns relative mass on a prescribed shrinking set. The probability event may depend on that prescribed observable or set; there is no simultaneous supremum over every set and no permission to select a set from the realized graph. Graph-dependent observables and graph balls need additional hypotheses.

The clean theorem matches every fixed d>=3 and every fixed strict-bulk energy, at the asymptotic point-process level. The main theorem does not separately claim deterministic-label gaps, uniformity over arbitrary moving energies, or unbounded correlation-count moments. The following quotations are copied exactly from freshly fetched original TeX and compared with all earlier source snapshots.

## Candidate 1: clean GOE

**OpenAI, “GOE bulk universality for fixed-degree random regular graphs”, September 23, 2026.** Opened its [README](https://github.com/openai/math/blob/main/preprints/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/README.md) and [original introduction](https://github.com/openai/math/blob/main/preprints/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/build/sections/01-introduction.tex). The fresh introduction is saved as goe-theorem-source.tex. The main theorem environment is copied exactly:

```tex
\begin{theorem}\label{thm:main}
For every fixed integer \(d\ge3\), every fixed
\(E\in(-2\sqrt{d-1},2\sqrt{d-1})\), and every nonnegative continuous
compactly supported \(h:\R\to\R\),
\[
 \left|
 \EE\exp\!\left(-\int h\dd\Xi_{n,d,E}\right)
 -
 \EE\exp\!\left(-\int h\dd\Xi_n^{\mathrm{GOE}}\right)
 \right|\longrightarrow0
\]
as \(n\to\infty\) through all admissible sizes.
\end{theorem}
```

The model is unweighted adjacency of a uniform simple labelled d-regular graph, without conditioning on connectivity or bipartiteness. Its unfolding is Xi_(n,d,E)=sum_i delta_(n rho_d(E)(lambda_i-E)), with
\[
 \rho_d(E)=\frac{d\sqrt{4(d-1)-E^2}}{2\pi(d^2-E^2)}.
\]
The GOE reference has off-diagonal variance 1/n, diagonal variance 2/n, and is unfolded at zero by n/pi.

| Words in our statement | What the theorem actually covers |
| --- | --- |
| “For fixed d ≥ 3” | Every fixed integer d≥3, including cubic graphs; same range. |
| “uniform random d-regular graph on N vertices” | Same simple labelled model, with n=N; admissible sizes have n>d and nd even. It is not a multigraph theorem. |
| “adjacency eigenvalues” | Same ordinary unnormalized adjacency, no diagonal disorder. |
| “GOE local statistics” | Fixed-energy convergence of microscopic Laplace functionals, hence the local point-process law. The displayed theorem does not separately state deterministic-label gap universality or convergence of unbounded correlation-counting moments. |
| “in the bulk of the Kesten–McKay law” | Each fixed energy strictly inside the support; not an edge theorem or a stated uniform result for arbitrary moving energies. |
| “as N → ∞” | An asymptotic limit through all admissible sizes, not just a bound or a subsequence. No quantitative rate is given. |
| “eigenvectors are delocalized” | An imported published input in the introduction, not a new conclusion in this theorem. |
| “satisfy quantum unique ergodicity” | No spatial observable appears in the main theorem. The prescribed deterministic diagonal version, and the shrinking-set extension in PROOF.md, follow separately from published delocalization and label symmetry. |

This is the exact spectral part of the row at fixed-energy point-process strength. Missing QUE language in that main theorem does not imply that deterministic diagonal QUE is open.

## Candidate 2: Anderson disorder

**OpenAI, “Fixed-energy universality for weak Anderson disorder on random regular graphs”, October 5, 2026.** Opened its [README](https://github.com/openai/math/blob/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/README.md) and [original introduction](https://github.com/openai/math/blob/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/build/sections/01-introduction.tex). Fresh source: anderson-theorem-source.tex. Exact main theorem:

```tex
\begin{theorem}[Fixed-energy universality]\label{thm:main}
For every $d\ge3$ and every $0<\kappa<2\sqrt{d-1}$, there is
$w_0=w_0(d,\kappa)>0$ with the following property.  For each fixed
$0<w<w_0$, the restriction of $\nu_{d,w}$ to an open neighborhood of
\[
 I_{d,\kappa}=[-2\sqrt{d-1}+\kappa,\,2\sqrt{d-1}-\kappa]
\]
has a continuous density $\rho_{d,w}$, strictly positive on
$I_{d,\kappa}$.  For every fixed $E\in I_{d,\kappa}$, set
\[
 \Xi_{n,E}=\sum_{i=1}^n
       \delta_{n\rho_{d,w}(E)(\lambda_i-E)}.
\]
Then, for every nonnegative $f\in C_c(\RR)$,
\begin{equation}\label{eq:main-laplace}
 \left|
 \EE\exp\left(-\int f\,d\Xi_{n,E}\right)
 -\EE\exp\left(-\int f\,d\Xi_n^{\GOE}\right)
 \right|\longrightarrow0
\end{equation}
as $n\to\infty$ through all sizes $n>d$ with $nd$ even.
\end{theorem}
```

Here H=A+w diag(omega_i), with independent uniform omega_i on [-1,1], independent of the graph. The measure nu_(d,w) is the expected root spectral measure of the corresponding infinite-tree random operator.

The fixed-degree range and asymptotic point-process quantity agree with the spectral clause. The operator and unfolding differ: fixed positive weak disorder is required and unfolding uses rho_(d,w), not the clean Kesten–McKay density. The theorem excludes w=0; it supplies no interchange of the w→0 and n→∞ limits. Its energy interval is a compact subset of the clean bulk and its allowed disorder depends on d and the distance from the edges. It gives no additional main-theorem spatial QUE statement for clean adjacency. It is a related operator result, not the same clean-model theorem.

## Candidate 3: planar Ising

**OpenAI, “Conformal universality of bulk Ising correlations under weak interactions”, September 23, 2026.** Opened its [README](https://github.com/openai/math/blob/main/preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/README.md) and [original model section](https://github.com/openai/math/blob/main/preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/build/sections/model.tex). Fresh source: ising-theorem-source.tex. Exact main theorem:

```tex
\begin{theorem}[Conformal universality]\label{model:main}
For each $J$ and potential $V$ as above, there are $\lambda_0>0$ and real
functions $\beta_c,Z_\sigma,Z_\epsilon$ on $(-\lambda_0,\lambda_0)$,
continuous at zero, such that
\[
 \beta_c(\lambda)>0,\quad \beta_c(0)=\beta_0,\qquad
 Z_\sigma(0)=Z_\epsilon(0)=1,\quad
 Z_\sigma(\lambda)Z_\epsilon(\lambda)\ne0.
\]
For every fixed $|\lambda|<\lambda_0$, every allowed domain $D$, every
$b\in\{\mathrm{free},+,-\}$, all integers $n,m\ge0$ with $n+m\ge1$,
all pairwise distinct interior points $x_1,\ldots,x_n,y_1,\ldots,y_m$,
and all $j_1,\ldots,j_m\in\{1,2\}$, the full-sequence limit is
\begin{equation}\label{model:limit}
 \lim_{a\downarrow0}
 \left\langle\prod_{i=1}^n S_a(x_i)
                    \prod_{k=1}^m E_{a,j_k}(y_k)\right\rangle_{a,D}^{\lambda,b}
 =Z_\sigma(\lambda)^nZ_\epsilon(\lambda)^m
       \mathcal C_D^b(\boldsymbol x;\boldsymbol y).
\end{equation}
The same functions and coupling interval apply to every such choice.

At each fixed mesh, the infinite-volume limit along periodic square boxes
exists for all local observables. Using that state first, and then taking
$a\downarrow0$, gives \eqref{model:limit} with $D$ replaced by $\C$.
In particular its two-spin limit is a nonzero constant times
$|x-y|^{-1/4}$.

If $\phi:D\to D'$ is a conformal bijection between allowed domains, the
limiting correlation in $D$ is its counterpart at the image points in
$D'$, multiplied by
\begin{equation}\label{model:covariance}
 \prod_{i=1}^n|\phi'(x_i)|^{1/8}
 \prod_{k=1}^m|\phi'(y_k)|.
\end{equation}
The boundary type is transported unchanged.
\end{theorem}
```

This is a two-dimensional square-lattice Gibbs model with weak finite-range even interactions, taking lattice mesh a→0 at a critical temperature. Its quantities are mixed spin and centered bond-energy correlations, with scaling dimensions 1/8 and 1, and conformal covariance. It has no random regular graph, adjacency eigenvalue, eigenvector or GOE assertion. Thus model, dimension, observables and limiting parameter all differ; “bulk” is only a shared word. Candidate assessment: NOT-THIS.

## Follow-ups and opened-source register

The initial update search was limited to five minutes. Queries included fixed-degree random regular graphs with QUE and 2026/November, the exact GOE title with OpenAI/error/correction/refutation, and arXiv:2610.08127. No new primary result changing the earlier reports was identified; that is a bounded search finding. The already known deterministic-observable QUE corollary is not a new post-report settlement. No SOLVED_ELSEWHERE.md was created.

| Opened source in this session | Finding and limit |
| --- | --- |
| [OpenAI repository](https://github.com/openai/math), [history.md](https://raw.githubusercontent.com/openai/math/main/history.md), the three original TeX sections and their manuscript READMEs | History's latest heading remains October 29, with no named correction/withdrawal of these three candidates. The READMEs confirm OpenAI as author and the title/dates above. Source snapshots are saved here. No inference of proof correctness. |
| **Yukun He, Jiaoyang Huang, Xiaoyu Wang, “Bulk universality of random regular graphs”, [arXiv:2610.08127](https://arxiv.org/abs/2610.08127), [full HTML v1](https://arxiv.org/html/2610.08127v1)** | Still v1, submitted 6 October 2026. Same clean fixed-degree model; fixed-energy Sine_1 point process, deterministic-label gaps and fixed-energy correlations. Known to all earlier reports. No identified arXiv version relationship to the OpenAI text or independent audit of its proof. |
| **Jiaoyang Huang and Horng-Tzer Yau, “Spectrum of Random d-regular Graphs Up to the Edge”, [arXiv:2102.00963](https://arxiv.org/abs/2102.00963), [full HTML v3](https://arxiv.org/html/2102.00963v3)** | Theorem 1.4 and its following paragraph supply polylogarithmic complete delocalization and the unconditional high-probability event for every fixed d>=3. Their resolvent method covers every unit vector in repeated eigenspaces. The QUE implication is derived in the local proofs, not quoted as their explicit theorem. |
| **Jaehun Lee, “Mesoscopic eigenvalue statistics for random regular graphs: a case study”, [arXiv:2611.09215](https://arxiv.org/abs/2611.09215)** | Abstract reopened: submitted 6 November 2026, mesoscopic CLT at (log N)^(-1)<<eta<<1 for its test class. Already in the first report; not a microscopic or spatial QUE settlement. |
| [lean/README.md](https://raw.githubusercontent.com/openai/math/main/lean/README.md), [lean/docs directory](https://github.com/openai/math/tree/main/lean/docs), [formalization.yaml](https://github.com/openai/math/blob/main/lean/formalization.yaml), [scope note 218.md](https://raw.githubusercontent.com/openai/math/main/lean/docs/218.md) | Fresh directory listing: 245 scope notes, 218.md present, 219.md absent. Fresh catalogue has no matching clean-GOE, Anderson or bulk-Ising-conformal main theorem. Scope 218 describes finite-graph buffered likelihood comparison in a different Ising companion. No matching formalization identified; no Lean build or axiom audit. Saved listing and catalogue locally. |
| [Latent Seminar, “Microscopic spectra of random regular graphs”](https://lowrank.github.io/latent-seminar/OpenAI-Math/219-random-regular-spectra), 6 October 2026 | Exposition explicitly disclaims complete independent proof verification. |
| [Community GOE page](https://mathcommunity.github.io/oai-math-revised/papers/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/) | Updated November 9; no contributed notes. Automatic notes are marked unreviewed. They reproduce the known parallel bulk result and lead to other-model literature; unopened linked papers are not cited as checked references here. |
| [AI Proved What, family 219](https://aiprovedwhat.com/episodes/219-goe-bulk-universality-regular-graphs/) | Exposition/tracker, not a referee report. No expert proof validation follows from its listing. |

No matching later arXiv version of an OpenAI candidate, refutation, error report, referee report or specialist complete-proof validation was identified by this bounded search. The original report's tensor-coercivity spot check found no error in that lemma; it does not validate the remaining proof. The prior report's large-fixed-degree QUE qualification remains in the read-only predecessor record; the quantitative extension here instead uses the directly reopened all-degree Huang–Yau input.

## Recommended replacement for “where it stands” (three sentences)

Bulk GOE statistics for every fixed d≥3 are proved in Yukun He, Jiaoyang Huang and Xiaoyu Wang's *Bulk universality of random regular graphs* (arXiv:2610.08127, 6 October 2026), while OpenAI's unrefereed *GOE bulk universality for fixed-degree random regular graphs* (23 September 2026) claims fixed-energy point-process universality. Complete delocalization for every fixed d≥3 is known from Jiaoyang Huang and Horng-Tzer Yau and, with label symmetry, implies probabilistic QUE against each prescribed deterministic bounded vertex observable and relative equidistribution on prescribed sets growing faster than a sufficiently large fixed power of log N, uniformly over all eigenvectors. A stronger intended QUE requirement, such as graph-dependent observables, must be specified before calling that requirement open or settled.

## Spot check

The new load-bearing estimate is sampling-without-replacement Bernstein, PROOF.md (5)–(10). Its moment-generating-function comparison is proved by an exact pair-averaging argument for elementary symmetric polynomials; it does not pretend the samples are independent. Normalization of a unit eigenvector gives variance at most L^2/N^2 rather than the cruder L^4/N^2. The 1/4-net then controls complete eigenspaces, with at most 9^M directions per eigenspace; a basis-only delocalization hypothesis would not justify this step.

`OMP_NUM_THREADS=1 nice -n 15 python3 audit_bernstein.py` passed 6,132 subset instances, 595 high-precision Bernstein-tail comparisons, 189 exact rational exponential-product comparisons, 3,465 exact pair-averaging identities, 3,654 constant substitutions and independent quadratic-root inversions, and 69,680 direct mass/quadratic-form comparisons across 536 repeated-eigenspace compressions. The explicit fine net used in the finite audit has 130 points in dimension two; the analytic volume proof, not that audit net, establishes the 9^m cardinality bound. Runtime was 1.869 seconds, peak RSS 14,893,056 bytes, inherited niceness 20, one thread.

The counterexample in PROOF.md (15) shows that k comparable to L^2 can fail even with simple spectrum: a prescribed set misses a designated eigenvector's support with probability tending to e^(-1). Binomial-ratio and product computations agree exactly for s=2,4,8,16,32,64,128; at s=128 the miss probability is 0.36500164. Exact block-Walsh eigensystems were also checked for s=2,4,8. This counterexample concerns permutation-invariant symmetric matrices, not random regular graphs. No optimality of the logarithmic powers is claimed.

The round-4 audit was rerun unchanged through runpy from its read-only directory and all checks passed. The earlier exponent was also re-derived directly before the new extension was chosen. No proof error was found in that earlier implication.
