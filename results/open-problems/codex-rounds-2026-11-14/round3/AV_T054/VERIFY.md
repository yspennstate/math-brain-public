# T054: continuation verification

Checked November 15, 2026, +04. The earlier report's comparison of explicit theorem statements survives rechecking. This continuation resolves its remaining qualification for one precise QUE formulation: prescribed deterministic bounded diagonal tests satisfy probabilistic QUE for every fixed d≥3 as an elementary consequence of known delocalization and label symmetry. The full argument, including repeated eigenspaces, is in [PROOF.md](PROOF.md).

The release-scope assessment remains **PARTIAL-CLAIMED**: the clean manuscript's explicit main theorem is a bulk eigenvalue theorem. Under the deterministic diagonal interpretation specified below, however, the row's QUE clause is already a consequence of earlier literature, so it should not be listed as an unexplained fixed-degree open problem. This is distinct from certifying the OpenAI proof.

## The statement being compared

“For fixed d ≥ 3, the adjacency eigenvalues of a uniform random d-regular graph on N vertices have GOE local statistics in the bulk of the Kesten–McKay law as N → ∞, and the eigenvectors are delocalized and satisfy quantum unique ergodicity.”

The graph is interpreted as simple and labelled, as in all graph papers below. The precise QUE statement established in PROOF.md is: for each deterministic bounded real vertex function a_N, chosen before sampling the graph,
\[
 \sup_{\substack{A_Nu=\lambda u\\\|u\|_2=1}}
 \left|\sum_i a_N(i)|u_i|^2-\frac1N\sum_i a_N(i)\right|
 \xrightarrow{\mathbb P}0.
\]
The supremum includes all unit vectors in repeated eigenspaces; it does not average over eigenvectors. The probability event can depend on the prescribed test sequence. No simultaneous supremum over all bounded tests, general graph-dependent observables, off-diagonal observables, or relative small-set QUE is asserted.

## Candidate 1: clean GOE

**OpenAI, “GOE bulk universality for fixed-degree random regular graphs”, September 23, 2026.** Freshly opened [README](https://github.com/openai/math/blob/main/preprints/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/README.md) and [theorem source](https://github.com/openai/math/blob/main/preprints/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/build/sections/01-introduction.tex). Current source is saved in goe-theorem-source.tex. The theorem below is extracted verbatim from that source.

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

Here A is ordinary unweighted adjacency of the uniform simple labelled d-regular graph; all eigenvalues count with multiplicity, with no connectivity or bipartiteness conditioning. The notation is
\[
 \rho_d(t)=\frac{d\sqrt{4(d-1)-t^2}}{2\pi(d^2-t^2)},\qquad
 \Xi_{n,d,E}=\sum_i\delta_{n\rho_d(E)(\lambda_i-E)},\qquad
 \Xi_n^{\mathrm{GOE}}=\sum_i\delta_{(n/\pi)\mu_i}.
\]
GOE has off-diagonal variance 1/n and diagonal variance 2/n.

| Clause in our row | Exact coverage and limitation |
| --- | --- |
| Fixed d≥3 | Every fixed integer d≥3, including cubic graphs; no degree growth required. |
| Uniform random d-regular graph on N vertices | Same simple labelled model, with n=N. Admissible sizes mean n>d and nd even. A multigraph interpretation would require another comparison. |
| Adjacency eigenvalues | Same unnormalized adjacency, without diagonal disorder. |
| Bulk of Kesten–McKay law | Each fixed E strictly inside the open support. Not an edge theorem or a statement uniform over arbitrary moving energies. |
| GOE local statistics | Convergence of fixed-energy microscopic Laplace functionals, hence the point-process law. The displayed theorem does not separately assert deterministic-label gaps or unbounded correlation-counting moments. |
| As N→∞ | An asymptotic limit through every admissible size, not just a bound or a subsequence. No rate is stated. |
| Delocalized eigenvectors | Known delocalization is imported as an input, not newly established in the main theorem. |
| QUE | The explicit main theorem has no spatial-observable conclusion. Prescribed-test diagonal QUE follows separately from published delocalization and symmetry by PROOF.md. It need not be supplied by a new release theorem. |

Its explicit eigenvalue scope matches the spectral clause of our row. The absence of QUE from the displayed theorem does not imply that this version of QUE is open.

## Candidate 2: weak Anderson disorder

**OpenAI, “Fixed-energy universality for weak Anderson disorder on random regular graphs”, October 5, 2026.** Freshly opened [README](https://github.com/openai/math/blob/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/README.md) and [theorem source](https://github.com/openai/math/blob/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/build/sections/01-introduction.tex). Current source is saved in anderson-theorem-source.tex.

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

The matrix is \(H_{n,d,w}=A_{n,d}+w\operatorname{diag}(\omega_1,\ldots,\omega_n)\), where the potentials are independent uniform variables on [-1,1], independent of the uniform simple labelled graph. The deterministic measure \(\nu_{d,w}\) is the expected root spectral measure of the corresponding operator on the infinite d-regular tree.

The fixed-degree range agrees, and the conclusion is again an asymptotic fixed-energy point-process law. The model and unfolding differ: positive fixed disorder is required, and the density is the disordered tree density. The theorem excludes w=0 and does not justify interchanging a w→0 limit with n→∞. Its main theorem supplies no additional spatial QUE statement for clean adjacency. Thus it is a related operator extension, not a theorem about the exact clean model in our row.

## Candidate 3: Ising

**OpenAI, “Conformal universality of bulk Ising correlations under weak interactions”, September 23, 2026.** Freshly opened [README](https://github.com/openai/math/blob/main/preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/README.md) and [theorem source](https://github.com/openai/math/blob/main/preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/build/sections/model.tex). Current source is saved in ising-theorem-source.tex.

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

The hypotheses concern finite-range, even, symmetric square-lattice interactions; the observables are rescaled spin and centered bond energy. This is a planar Gibbs model as mesh tends to zero. It concerns neither random regular graphs nor adjacency eigenvalues or eigenvectors. The shared word “bulk” does not make its quantity, model, dimension or limit match our row. Candidate assessment: NOT-THIS.

## What was rechecked and what is new

The older report and log were read in the earlier folder, together with its VERIFY.md and the relevant TeX snapshots. No earlier PROOF.md or computation scripts exist there. The new report uses the continuation verdict format requested in the latest instructions; the release's explicit theorem-scope verdict is recorded separately above.

Fresh reading confirms the earlier main claim: clean fixed-degree point-process universality is the explicit OpenAI theorem, and its statement has no QUE test or matrix element. Independently reopened Roland Bauerschmidt, Jiaoyang Huang and Horng-Tzer Yau, *Local Kesten–McKay law for random regular graphs*, [arXiv:1609.09052](https://arxiv.org/pdf/1609.09052), Corollary 1.3(ii), equation (1.7), and its proof on PDF page 11. This already gives probabilistic QUE for prescribed deterministic tests at sufficiently large fixed degree and obtains it using exchangeability. That confirms the earlier correction of the blanket QUE-open note.

The extension is a direct proof that the all-degree delocalization theorem suffices for the same qualitative deterministic diagonal QUE conclusion. It handles the choice of eigenbasis carefully: fix any basis before introducing an independent permutation, control every entry in each compressed observable, then obtain an operator bound on each entire eigenspace. If every unit eigenvector has coordinate bound L/√N, its eigenspace has dimension at most L². The resulting estimate is
\[
 \mathbb P\left\{\sup_u|\langle u,\operatorname{diag}(a)u\rangle|>s\right\}
 \le\varepsilon_N+2N^2\exp[-Ns^2/(32L^8)]
\]
for prescribed mean-zero a in [-1,1]^N, where \(\varepsilon_N\) is the failure probability of delocalization.

The input is Jiaoyang Huang and Horng-Tzer Yau, *Spectrum of Random d-regular Graphs Up to the Edge*, [arXiv:2102.00963v3](https://arxiv.org/html/2102.00963v3), Theorem 1.4 and its following paragraph. It covers every fixed d≥3 and all eigenvectors, with a polylogarithmic coordinate factor on an event of probability tending to one. PROOF.md derives the displayed QUE consequence rather than attributing an unstated corollary to their theorem. No optimal rate, new theorem of independent interest, or proof validation of the OpenAI work is claimed.

The concentration constant, eigenspace factor and tail substitution are derived explicitly in PROOF.md. A separate exact permutation enumeration in audit_permutation.py checks the conditional expectations and variance formula for N=2,...,7; all 18 weight cases pass. The proof's test-dependent obstruction is also checked: complete delocalization cannot alone justify simultaneous control of every bounded test.

## Follow-ups: sources opened in this session

The initial update search lasted less than five minutes. Queries were:

- "random regular graphs" "quantum unique ergodicity" 2026 November
- "GOE bulk universality for fixed-degree random regular graphs" error correction
- "Bulk universality of random regular graphs" "2610.08127"
- "openai/math" "219" correction November

The following primary or repository sources were opened, not merely taken from search snippets:

1. **Yukun He, Jiaoyang Huang, Xiaoyu Wang, *Bulk universality of random regular graphs*, [arXiv:2610.08127](https://arxiv.org/abs/2610.08127).** The abstract page still displays v1, October 6, 2026. It states all-fixed-degree bulk Sine_1 point-process universality, deterministic-label gaps and fixed-energy correlations. This is the separate result already in the older report, not a new post-report solution or an identified arXiv version of OpenAI's manuscript.
2. **Jiaoyang Huang and Horng-Tzer Yau, *Spectrum of Random d-regular Graphs Up to the Edge*, [full v3 HTML](https://arxiv.org/html/2102.00963v3).** Read Theorem 1.4, its unconditional-event discussion and model definition. This is the delocalization input, not a follow-up to the release.
3. **Roland Bauerschmidt, Jiaoyang Huang and Horng-Tzer Yau, *Local Kesten–McKay law for random regular graphs*, [original PDF](https://arxiv.org/pdf/1609.09052).** Read Corollary 1.3 and its proof. This is the source of the old-note correction, not a release follow-up.
4. **[Current release history](https://github.com/openai/math/blob/main/history.md).** Visible history ends October 29; there is no named revision or withdrawal of the three candidates. Each manuscript README was also opened; none carries such a notice.
5. **[Community GOE manuscript page](https://mathcommunity.github.io/oai-math-revised/papers/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/).** It has no contributed notes. Its collected notes explicitly say they are unreviewed. It points to the same He–Huang–Wang result and other leads, which are not treated as a specialist validation. No newly verified scholarly follow-up was found in the bounded update check.
6. **[lean/](https://github.com/openai/math/tree/main/lean), [lean/docs/](https://github.com/openai/math/tree/main/lean/docs), [formalization.yaml](https://github.com/openai/math/blob/main/lean/formalization.yaml), and [218.md](https://github.com/openai/math/blob/main/lean/docs/218.md).** Fresh directory listing has 245 scope-note files, including 218.md and no 219.md. The catalogue has no matching clean-GOE or bulk-Ising-conformal title. The 218 note describes only a finite-graph buffered likelihood comparison, not the conformal theorem. No matching main-theorem Lean formalization was identified, and no Lean build was run.
7. All three current original theorem sources and READMEs linked above were opened through the read-only GitHub connector; the raw theorem files were also opened with web. The initial Anderson path without “01-” failed; the correct path succeeded. The repository [LICENSE](https://github.com/openai/math/blob/main/LICENSE) was opened.

The bounded update search did not identify an expert proof audit, refutation, referee report, or arXiv version under an exact OpenAI title that changes the earlier assessment. This is a record of this search, not a claim that no commentary exists elsewhere. The earlier worker's wider register remains in its unchanged VERIFY.md; sources appearing only there are not presented as newly opened here.

## Recommended replacement for “where it stands” (three sentences)

Bulk GOE statistics for every fixed d≥3 are established in Yukun He, Jiaoyang Huang and Xiaoyu Wang's *Bulk universality of random regular graphs* (arXiv:2610.08127, October 6, 2026), while OpenAI's unrefereed *GOE bulk universality for fixed-degree random regular graphs* (September 23, 2026) claims the fixed-energy point-process result. Complete delocalization for every fixed d≥3 is known from Jiaoyang Huang and Horng-Tzer Yau; together with label symmetry it also implies probabilistic QUE against each prescribed deterministic bounded vertex observable, uniformly over all eigenvectors, as detailed in PROOF.md. OpenAI's *Fixed-energy universality for weak Anderson disorder on random regular graphs* (October 5, 2026) concerns positive diagonal disorder, and any stronger intended QUE requirement must be specified before retaining an open QUE clause.

The word “established” reports the literature's theorem, not an independent audit of its proof. The QUE implication in the second sentence is the derivation supplied here, not a quotation from Huang–Yau.

## Spot check

This continuation checks the permutation-concentration lemma that carries the new QUE implication, rather than claiming a second full audit of the release's proof. Its increment formula was derived algebraically, then checked against conditional expectations obtained by exhaustive completion of each permutation prefix. The separate covariance derivation in PROOF.md checks its scale; exact arithmetic verifies it on signed as well as nonnegative weights. The compressed-eigenspace step handles the repeated-eigenvalue case that a union bound over one chosen eigenbasis would miss.

The older worker checked the OpenAI tensor-coercivity lemma, label ent:tensor, and reported no error; its full source and analysis were read here, but no new certification of that lemma or the full GOE proof is claimed. The present independent theorem-scope recheck and the QUE corollary do not rely on it.

Task: “Verify: has open problem T054 been settled by the OpenAI math release?” — session start observed November 15, 2026, 00:51 +04.
