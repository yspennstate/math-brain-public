# T054 verification and continuation

Checked 15 November 2026, +04. The explicit release-scope verdict remains **PARTIAL-CLAIMED**: the clean manuscript claims the bulk eigenvalue point-process result and imports delocalization; its main theorem states no spatial QUE conclusion. REPORT.md uses the continuation verdict format in the later task instructions.

The round 3 result survives independent checking. This continuation proves relative QUE for each prescribed deterministic shrinking vertex set, uniformly over all eigenvectors, as a consequence of known complete delocalization and label symmetry. The proof and all quantifiers are in [PROOF.md](PROOF.md); the conclusion does not certify an OpenAI proof or claim a new literature theorem.

## Our statement and the precise QUE interpretation

“For fixed d ≥ 3, the adjacency eigenvalues of a uniform random d-regular graph on N vertices have GOE local statistics in the bulk of the Kesten–McKay law as N → ∞, and the eigenvectors are delocalized and satisfy quantum unique ergodicity.”

Here the graph is simple and labelled. Round 3 established: for each prescribed deterministic bounded real vertex function a_N, the supremum over all unit eigenvectors u of the absolute difference between sum_i a_N(i)|u_i|² and N^(-1)sum_i a_N(i) tends to zero in probability. The probability event depends on the prescribed sequence of observables.

The extension here concerns the relative discrepancy
\[
 \sup_{A_Nu=\lambda u,\ \|u\|_2=1}
 \left|\frac{N}{k_N}\sum_{i\in S_N}|u_i|^2-1\right|.
\]
If all unit eigenvectors satisfy ||u||_infinity <= L_N/sqrt(N) outside probability epsilon_N, this discrepancy exceeds r with probability at most
\[
 \varepsilon_N+2N^2
 \exp\!\left[-\frac{k_N^2r^2}{8\min(k_N,N-k_N)L_N^8}\right],
 \qquad 1\le k_N<N.
\]
It therefore tends to zero in probability if epsilon_N tends to zero and k_N/(L_N^8 log N) tends to infinity. The set S_N is chosen before sampling the graph. All unit vectors in repeated eigenspaces are included. General graph-dependent observables, graph balls, singleton sets and a simultaneous supremum over every vertex set are not established.

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
| “satisfy quantum unique ergodicity” | No spatial observable appears in the main theorem. The prescribed deterministic diagonal version, and the shrinking-set extension above, follow separately from published delocalization and label symmetry. |

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

## Recheck of the earlier result and the one extension

Read REPORT.md, LOG.md and VERIFY.md in both earlier folders; read round 3 PROOF.md and both scripts completely. The first folder contains no PROOF.md or computation scripts.

The earlier concentration proof holds. Independently subtracting its two conditional expectations gives the claimed increment (x-mu) times (the current weight minus the remaining-weight mean), bounded by 4b. The projection identity gives each eigenspace dimension at most L², so the entry-to-operator step and exponent L^8 follow. Substitution of its reported threshold gives exactly 2N^(-D). Independently enumerating subsets for binary mean-zero tests reproduces its scalar permutation variance on 6,078 instances.

The chosen extension replaces a full permutation reveal by sampling only a prescribed set's labels, and estimates its relative mass rather than an absolute error. It improves the small-set threshold obtainable from the older displayed estimate: k much larger than L^4 sqrt(N log N) becomes k much larger than L^8 log N. The complement refinement uses min(k,N-k). No simplicity assumption is introduced.

The published input is **Jiaoyang Huang and Horng-Tzer Yau, “Spectrum of Random d-regular Graphs Up to the Edge”, [arXiv:2102.00963v3](https://arxiv.org/html/2102.00963v3)**, revised 2 February 2025, Theorem 1.4 and the following unconditional-event discussion. It supplies a fixed polylogarithmic L_N and epsilon_N→0 for every fixed d≥3. The derivation of relative QUE is supplied here; it is not quoted as an explicit Huang–Yau theorem. In particular prescribed sets of size N^alpha, for any fixed alpha>0, are covered.

## Follow-ups and sources opened

The initial update search was bounded to five minutes. Web queries were the fixed-degree QUE query with 2026/Huang/Yau, the exact clean GOE title with OpenAI/error, and He/Huang/Wang/arXiv:2610.08127. No new result changing round 3 was identified. Subsequent opens document the existing source trail and theorem statements.

| Opened source | What was found and what it does not establish |
| --- | --- |
| **Yukun He, Jiaoyang Huang, Xiaoyu Wang, “Bulk universality of random regular graphs”, [arXiv:2610.08127](https://arxiv.org/abs/2610.08127)** | Abstract page still gives v1, 6 October 2026; bulk Sine_1 point process, deterministic-label gaps and fixed-energy correlations for every fixed d≥3. Already known to round 3; no identified version relationship to the OpenAI paper or proof audit. |
| **Jiaoyang Huang and Horng-Tzer Yau, [arXiv:2102.00963v3 full HTML](https://arxiv.org/html/2102.00963v3)** | Theorem 1.4, model and following paragraph checked directly. Gives all-degree complete delocalization and its unconditional exceptional probability; the input to PROOF.md. |
| **Roland Bauerschmidt, Jiaoyang Huang, Horng-Tzer Yau, “Local Kesten–McKay law for random regular graphs”, [arXiv:1609.09052](https://arxiv.org/abs/1609.09052)** | Abstract and authors reopened. Large fixed-degree local law and delocalization. Its QUE corollary was read in the earlier verification record; this session does not pretend the abstract alone states it. |
| **Jaehun Lee, “Mesoscopic eigenvalue statistics for random regular graphs: a case study”, [arXiv:2611.09215](https://arxiv.org/abs/2611.09215)** | Abstract page reopened: v1, 6 November 2026, a mesoscopic CLT for (log N)^(-1) << eta << 1 and restricted test functions. It is not a microscopic bulk/QUE settlement. Its citation to OpenAI was checked by the first worker; only the abstract is newly opened here. |
| [OpenAI release history](https://github.com/openai/math/blob/main/history.md) and all three manuscript READMEs linked above | History still ends 29 October. No named correction or withdrawal of these candidates; their READMEs identify author OpenAI and the dates quoted above. An absence of notices is not proof validation. |
| [Community GOE manuscript page](https://mathcommunity.github.io/oai-math-revised/papers/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/) | “No notes yet”; automatically collected notes are explicitly unreviewed. No specialist validation can be inferred from those notes. |
| [Latent Seminar, “Microscopic spectra of random regular graphs”](https://lowrank.github.io/latent-seminar/OpenAI-Math/219-random-regular-spectra), 6 October 2026 | Exposition expressly limits its review to statements and selected mechanisms and disclaims independent verification of the full proofs. |
| [lean/README.md](https://github.com/openai/math/blob/main/lean/README.md), [lean/docs/](https://github.com/openai/math/tree/main/lean/docs), [formalization.yaml](https://github.com/openai/math/blob/main/lean/formalization.yaml), [218.md](https://github.com/openai/math/blob/main/lean/docs/218.md) | Fresh connector listing has 245 scope-note files, including 218.md and no 219.md. Catalogue has no matching clean-GOE, Anderson or bulk-Ising-conformal main theorem. Scope 218 is a finite-graph buffered likelihood comparison for a different companion, not conformal universality. No matching main-theorem formalization identified; no Lean build or axiom audit. Web open of lean/ itself failed with a cache miss; the connector directory listing succeeded for lean/docs/. |
| All three original TeX sections linked in the candidate entries | Opened freshly with web and the read-only GitHub connector; saved locally and compared with both earlier snapshots. These are the preprints themselves, not summaries alone. |

The bounded search did not identify an exact-title arXiv version of an OpenAI manuscript, a refutation, an error report, a referee report or a specialist complete-proof audit that changes the earlier assessment. This is a limited search finding, not a claim that no commentary exists. No newly discovered settlement justified SOLVED_ELSEWHERE.md.

## Recommended replacement for “where it stands” (three sentences)

Bulk GOE statistics for every fixed d≥3 are proved in Yukun He, Jiaoyang Huang and Xiaoyu Wang's *Bulk universality of random regular graphs* (arXiv:2610.08127, 6 October 2026), while OpenAI's unrefereed *GOE bulk universality for fixed-degree random regular graphs* (23 September 2026) claims fixed-energy point-process universality. Complete delocalization for every fixed d≥3 is known from Jiaoyang Huang and Horng-Tzer Yau and, together with label symmetry, implies probabilistic QUE against each prescribed deterministic bounded vertex observable and relative equidistribution on each prescribed set growing faster than a sufficiently large fixed power of log N, uniformly over all eigenvectors. Any stronger intended QUE requirement, such as graph-dependent observables, must be specified before retaining an open QUE clause.

## Spot check

The load-bearing lemma for this continuation is the finite-subset concentration bound (6) in PROOF.md. Its increment formula was derived directly and checked against exhaustive completion averages, with the empty/full-set endpoints treated separately. Its mean and variance were recomputed by two distinct counting arguments, and the exact matrix audit checks repeated-eigenspace compression as well as an actual counterexample ensemble for singleton and adaptive-set claims.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 audit_subsets.py`. It passed 189 subset cases, 6,132 subset instances, 7,032 prefix checks, 6,078 instances of the older variance identity, 538 compressed-eigenspace subset cases, and four Walsh ensembles with 340 coordinate checks. Peak RSS was 15,351,808 bytes; one thread; inherited niceness 20; runtime 0.23 seconds.

The first worker spot-checked the clean OpenAI tensor-coercivity lemma and found no error. That record is preserved in its unchanged VERIFY.md; this session makes no additional claim about the rest of the OpenAI proof. The main new result does not depend on that lemma.

Task: “Verify: has open problem T054 been settled by the OpenAI math release?” — session start approximately 15 November 2026, 04:15 +04.

