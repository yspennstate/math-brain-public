# T054 verification, round 6

Checked 15 November 2026, Asia/Tbilisi. Release-scope assessment: PARTIAL-CLAIMED for bulk eigenvalue statistics. The continuation verdict in REPORT.md concerns the proved quantitative QUE implication below, not correctness of the OpenAI proof.

The round-5 result holds after independent re-derivation and an unchanged audit rerun. The extension in [PROOF.md](PROOF.md) removes its eigenspace-net factor: under all-unit-eigenvector delocalization ||u||_infinity<=L/sqrt(N) outside probability epsilon and permutation invariance, each prescribed k-set has maximum relative discrepancy exceeding r with probability at most

\[
 \varepsilon+2N\exp\left[-\frac{k^2r^2}
                  {2L^2(\min(k,N-k)+kr/3)}\right].
\]

Thus k/(L^2 log N)->infinity suffices, without a simple-spectrum assumption. The result includes all directions in repeated eigenspaces and complex unit eigenvectors; it excludes graph-dependent sets and a simultaneous supremum over every set. It is an application of standard concentration methods, with no novelty claim.

## Exact row and quantifiers

Our statement: “For fixed d ≥ 3, the adjacency eigenvalues of a uniform random d-regular graph on N vertices have GOE local statistics in the bulk of the Kesten–McKay law as N → ∞, and the eigenvectors are delocalized and satisfy quantum unique ergodicity.”

The graph model below is simple and labelled. “QUE” requires specifying observables and probability quantifiers. The round-3 proof already covered each prescribed deterministic bounded diagonal observable, in probability, uniformly over every unit eigenvector; the present improvement concerns relative mass on prescribed shrinking sets. No claim of arbitrary graph-dependent QUE follows.

The following theorem environments are exact copies from freshly retrieved original TeX, saved in this folder, and checked against predecessor snapshots. Source author is OpenAI in all three READMEs. The repository's [Apache-2.0 license](https://raw.githubusercontent.com/openai/math/main/LICENSE) is saved as LICENSE.openai-math; quotation attribution and source links are retained.

## Candidate 1: clean adjacency

OpenAI, *GOE bulk universality for fixed-degree random regular graphs*, September 23, 2026. Opened the [README](https://raw.githubusercontent.com/openai/math/main/preprints/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/README.md) and [original introduction](https://raw.githubusercontent.com/openai/math/main/preprints/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/build/sections/01-introduction.tex). Fresh snapshot: goe-theorem-source.tex.

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

Here Xi_(n,d,E)=sum_i delta_(n rho_d(E)(lambda_i-E)), with rho_d the Kesten–McKay density for ordinary unnormalized adjacency. The GOE reference has off-diagonal variance 1/n, diagonal variance 2/n and is unfolded at zero by n/pi. The theorem compares Laplace functionals of microscopic point processes.

| Clause of our row | Exact coverage |
| --- | --- |
| “fixed d ≥ 3” | Every fixed integer d>=3, including d=3; same degree range. |
| “uniform random d-regular graph on N vertices” | Uniform simple labelled graph, n=N; all admissible sizes n>d with nd even. No connectivity or bipartiteness conditioning. This does not state a multigraph result. |
| “adjacency eigenvalues” | Ordinary unweighted, unnormalized adjacency; same clean operator. |
| “GOE local statistics” | Fixed-energy asymptotic point-process/Laplace-functional universality. The displayed main theorem does not separately assert deterministic-label gaps or convergence of unbounded correlation-count moments. |
| “bulk of the Kesten–McKay law” | Every fixed strict-interior energy in (-2 sqrt(d-1),2 sqrt(d-1)), with that law's density in the unfolding. No edge result or uniform assertion over arbitrary moving energies. |
| “as N → ∞” | Full admissible sequence, not a subsequence; asymptotic convergence, with no quantitative rate in this theorem. |
| “eigenvectors are delocalized” | Complete delocalization is imported in the introduction from earlier literature, rather than a new conclusion of this main theorem. |
| “satisfy quantum unique ergodicity” | No spatial observable or QUE conclusion occurs in the main theorem. Prescribed deterministic diagonal QUE follows separately from published delocalization and label symmetry, as already derived in round 3. |

The spectral portion matches the row at fixed-energy point-process strength. Missing spatial QUE in this theorem does not mean that every interpretation of fixed-degree QUE is open.

## Candidate 2: weak Anderson disorder

OpenAI, *Fixed-energy universality for weak Anderson disorder on random regular graphs*, October 5, 2026. Opened the [README](https://raw.githubusercontent.com/openai/math/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/README.md) and [original introduction](https://raw.githubusercontent.com/openai/math/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/build/sections/01-introduction.tex). Fresh snapshot: anderson-theorem-source.tex.

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

Its operator is H=A+w diag(omega_i), where omega_i are independent uniform variables on [-1,1], independent of the graph. The unfolding uses the expected root spectral measure of the infinite-tree disordered operator.

The degree range, fixed-energy point-process quantity and asymptotic strength are comparable, but the model and reference density differ. The theorem requires fixed positive sufficiently small w and a compact energy band inside the clean support; it excludes w=0 and supplies no interchange of the w->0 and n->infinity limits. It states no main-theorem spatial QUE for clean adjacency. This is related spectral universality for a different operator, not a second theorem for our exact model.

## Candidate 3: Ising correlations

OpenAI, *Conformal universality of bulk Ising correlations under weak interactions*, September 23, 2026. Opened the [README](https://raw.githubusercontent.com/openai/math/main/preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/README.md) and [original model section](https://raw.githubusercontent.com/openai/math/main/preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/build/sections/model.tex). Fresh snapshot: ising-theorem-source.tex.

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

This is a two-dimensional square-lattice Ising Gibbs model with weak finite-range even interactions. It concerns critical spin and centered bond-energy correlations, their mesh-to-zero limit and conformal covariance, with scaling dimensions 1/8 and 1. It has no random regular graph, adjacency eigenvalue, eigenvector or GOE statement. The model, dimension, observables and asymptotic parameter all differ. Assessment: NOT-THIS.

## Update search and opened-source register

The settlement search ended within five minutes of starting it. Queries combined fixed-degree random regular graphs, QUE, November 2026; the exact GOE title with error/refutation/correction; and arXiv:2610.08127. No newly identified outside settlement changes the earlier reports, so SOLVED_ELSEWHERE.md is not warranted. Later methodological reads and original-source retrievals document the selected extension; they are not a further settlement search.

| Opened in this session | What it supports |
| --- | --- |
| The three original TeX sections and three READMEs linked above; [release history](https://raw.githubusercontent.com/openai/math/main/history.md) | Exact statements and metadata. History still starts October 29 and names no correction or withdrawal of these candidates. This is not proof validation. |
| Yukun He, Jiaoyang Huang, Xiaoyu Wang, *Bulk universality of random regular graphs*, [arXiv:2610.08127 abstract](https://arxiv.org/abs/2610.08127) and [v1 full HTML](https://arxiv.org/html/2610.08127v1) | Still v1, submitted 6 October 2026. Same clean fixed-degree model: Sine_1 point process, deterministic-label gaps and fixed-energy correlations. Already known to predecessors; no identified arXiv-edition relationship to the OpenAI manuscript or independent validation of that text. |
| Jiaoyang Huang and Horng-Tzer Yau, *Spectrum of Random d-regular Graphs Up to the Edge*, [v3 full HTML](https://arxiv.org/html/2102.00963v3), Theorem 1.4 and following paragraph | Complete delocalization for every fixed d>=3 with a polylogarithmic L and unconditional exceptional probability tending to zero. The local proofs derive the QUE implication, rather than quote it as an explicit theorem of this paper. |
| Jaehun Lee, *Mesoscopic eigenvalue statistics for random regular graphs: a case study*, [arXiv:2611.09215 abstract](https://arxiv.org/abs/2611.09215) | Submitted 6 November; mesoscopic eigenvalue CLT at (log N)^(-1)<<eta<<1 for its specified test class. Already in earlier work, not a new spatial QUE settlement. |
| [lean README](https://raw.githubusercontent.com/openai/math/main/lean/README.md), [formalization catalogue](https://raw.githubusercontent.com/openai/math/main/lean/formalization.yaml), [lean/docs directory](https://github.com/openai/math/tree/main/lean/docs), [scope note 218](https://raw.githubusercontent.com/openai/math/main/lean/docs/218.md) | Fresh catalogue and connector directory listing saved locally: 245 notes, 218 present, 219 absent. No exact candidate main-theorem title/path found in catalogue. Note 218 concerns finite-graph buffered Ising likelihood comparison in a different companion; it does not prove conformal universality. No Lean build or axiom audit. |
| [Community GOE page](https://mathcommunity.github.io/oai-math-revised/papers/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/) | No contributed notes; automatic notes marked unreviewed. This is not a specialist or referee validation. |
| David Gross and Vincent Nesme, *Note on sampling without replacing from a finite collection of matrices*, [arXiv abstract](https://arxiv.org/abs/1001.2738) and [v2 PDF](https://arxiv.org/pdf/1001.2738), Section C and Lemma 2 | Primary source for convex comparison and transfer of trace-exponential bounds to sampling without replacement. The needed coupling is proved directly in PROOF.md. |
| Joel A. Tropp, *User-Friendly Tail Bounds for Sums of Random Matrices*, [author PDF](https://tropp.caltech.edu/papers/Tro11-User-Friendly-preprint.pdf), equation (2.6) and Section 3.3 | Two-factor Golden–Thompson inequality used in the proof and the warning that it cannot simply be iterated as a multi-factor product inequality. Our iteration first bounds each conditional matrix mgf by a scalar identity matrix. |

The web open of AIProofWatch failed with a cache miss. The web lean/docs directory open also failed; the read-only GitHub connector retrieved its current listing successfully. Failed opens are not counted as read sources. No newly identified matching arXiv follow-up, error report, refutation, referee report, expert full-proof validation or matching Lean main theorem was found. This is a bounded negative finding, not a claim of exhaustive absence.

## Recommended replacement for “where it stands” (three sentences)

Bulk GOE statistics for every fixed d≥3 are proved in Yukun He, Jiaoyang Huang and Xiaoyu Wang's *Bulk universality of random regular graphs* (arXiv:2610.08127, 6 October 2026), while OpenAI's unrefereed *GOE bulk universality for fixed-degree random regular graphs* (23 September 2026) claims fixed-energy point-process universality. Complete delocalization for every fixed d≥3 is known from Jiaoyang Huang and Horng-Tzer Yau and, with label symmetry, implies probabilistic QUE against each prescribed deterministic bounded vertex observable and relative equidistribution on prescribed sets growing faster than a sufficiently large fixed power of log N, uniformly over all eigenvectors. Any stronger intended QUE requirement, including graph-dependent observables, must be specified before that requirement is called open or settled.

## Spot check

The load-bearing step of this continuation is the matrix concentration estimate, PROOF.md (5)–(16). Its sampling comparison follows from an explicit conditional-mean coupling; convexity is of trace exp, not operator convexity. Rank-one eigenspace row matrices give variance <=(L^2-1)I/N^2. The two-factor Golden–Thompson inequality is imported as a standard theorem; every conditional iteration step is written out. Summing the dimension prefactors gives 2 sum_V dim V=2N.

The exact conditional coupling means were checked over 52,500 ordered draw sequences and 56,262 containing-subset extensions. Twelve genuinely noncommuting tight-frame populations passed exact matrix second-moment and direct mass checks. Separately enumerated replacement and without-replacement trace mgfs passed 72 high-precision comparisons, with an independent exponential-series calculation. The exponent and error-scale inversion passed 7,020 independent substitutions/root checks. Full output and resource/setup limitations are in LOG.md; the runnable script is audit_matrix.py. These finite checks support the written proof; they do not prove its general assertions.

To avoid relying only on small-N tail bounds above 1, a separate exact hypergeometric count covered 7,514 occupancy classes for noncommuting uniform-leverage frames at N=64 and 128. All 12 matrix-tail inequalities held; 10 upper bounds were below 1, and all actual tails were positive. At N=128,k=32,r=1/2, the actual probability was 0.000066778554 and the upper bound 0.72036925. Complementary sets gave the same probabilities after the required change of relative normalization. Final audit runtime was 1.513 seconds and peak RSS 17,596,416 bytes, one thread at niceness 20.

The old proof and its audit both survived recheck. The resulting threshold k/(L^2 log N)->infinity covers complete repeated eigenspaces; optimality of its logarithm remains unproved. The old singleton and adaptive-set counterexamples still apply to the abstract hypotheses. No further claim about the correctness of the OpenAI proof is made.

