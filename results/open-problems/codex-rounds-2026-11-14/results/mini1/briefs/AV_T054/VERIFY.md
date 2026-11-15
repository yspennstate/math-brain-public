# Verification of T054

Checked on November 14, 2026. Verdict: PARTIAL-CLAIMED. The clean bulk eigenvalue assertion is claimed in the release; the full conjunction in our row is not. This is a comparison of statements and subsequent literature, not a certification of the proofs.

## Our statement and the meaning of QUE

“For fixed d ≥ 3, the adjacency eigenvalues of a uniform random d-regular graph on N vertices have GOE local statistics in the bulk of the Kesten–McKay law as N → ∞, and the eigenvectors are delocalized and satisfy quantum unique ergodicity.”

The usual simple labelled graph interpretation is used below. If “uniform random graph” were intended to include a configuration-model multigraph, that would require a separate comparison.

The row does not specify the observable class, spectral window, or probability quantifiers in QUE. The distinction that matters here is spatial equidistribution for each eigenvector against prescribed vertex observables, rather than equidistribution after averaging over eigenvectors. A representative formulation, for a deterministic bounded mean-zero vertex function a_N, asks for small matrix elements
\[
\sum_v a_N(v)|\psi_j(v)|^2
\]
for every eigenvector in a bulk band (with the relevant uniformity in j), where \(\|\psi_j\|_2=1\). No such spatial-observable theorem is stated in the candidate main results. Sampled Gaussian moments should not silently substitute for the intended QUE formulation. However, the old note’s blanket claim that QUE at fixed degree is open is too broad: probabilistic spatial QUE against deterministic tests is already in earlier literature, as detailed below.

## Candidate 1: GOE bulk universality for fixed-degree random regular graphs

Author: OpenAI. Date: September 23, 2026. [Original main source](https://github.com/openai/math/blob/main/preprints/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/build/main.tex), [main theorem source](https://github.com/openai/math/blob/main/preprints/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/build/sections/01-introduction.tex). Local copies: GOE-main.tex and GOE-introduction.tex.

### Exact main theorem

Theorem 1.1, copied verbatim as TeX, including its labels:

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

The notation immediately preceding it is essential. The graph is uniform among simple labelled d-regular graphs, A is the ordinary unweighted adjacency matrix, all eigenvalues count with multiplicity, and there is no conditioning on connectedness or bipartiteness. Admissible means that the simple graph ensemble is nonempty (equivalently n>d and nd even here). The density and point processes are
\[
\rho_d(t)=\frac{d\sqrt{4(d-1)-t^2}}{2\pi(d^2-t^2)},\quad
\Xi_{n,d,E}=\sum_i\delta_{n\rho_d(E)(\lambda_i-E)},\quad
\Xi_n^{\mathrm{GOE}}=\sum_i\delta_{(n/\pi)\mu_i}.
\]
The GOE off-diagonal variance is 1/n and diagonal variance 2/n. Its reference process has limiting intensity one.

### Comparison with every clause of our row

| Our clause | What this paper claims | Match and limit |
| --- | --- | --- |
| “fixed d ≥ 3” | Every fixed integer d≥3, including 3 | Exact range match; d does not grow with n. |
| “uniform random d-regular graph on N vertices” | Uniform simple labelled graph on n vertices, unconditioned | Exact match under the standard simple labelled convention; n=N is a notation change. |
| “adjacency eigenvalues” | Ordinary, unweighted adjacency, all eigenvalues with multiplicity | Exact match; no matrix normalization is concealed. The trivial eigenvalue d lies outside the open bulk and escapes bounded microscopic windows. |
| “GOE local statistics in the bulk of the Kesten–McKay law” | Laplace-functional convergence of the entire unfolded point process at each fixed interior E | Matches the fixed-energy point-process meaning of bulk local statistics; stronger than an energy-averaged statement or a density bound. The displayed theorem does not separately assert deterministic-label gap universality, convergence of unbounded correlation-counting observables, rates, or uniformity over moving energies. Those stronger formulations should not be inferred from vague convergence alone. |
| “as N → ∞” | Limit through all admissible n | Exact asymptotic match, with no finite-n quantitative error rate in Theorem 1.1. |
| “eigenvectors are delocalized” | Imported spectral input: entries of eigenvectors with squared norm n are n^{o(1)} on high-probability events | Gives the usual N^{-1/2+o(1)} bound for unit eigenvectors, but this is credited to earlier work, not the main new theorem. |
| “and satisfy quantum unique ergodicity” | No separate spatial QUE statement; Proposition 3.1 concerns finitely many sampled-edge coordinate moments | Not covered as an explicit main theorem. The moment bounds average over edge locations and do not test a prescribed nonconstant spatial weight. Existing probabilistic QUE results must also be accounted for before deciding whether a precisely formulated full row remains open. |

The [spectral-input source](https://github.com/openai/math/blob/main/preprints/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/build/sections/02-preliminaries.tex) explicitly cites Jiaoyang Huang and Horng-Tzer Yau, *Spectrum of Random d-regular Graphs Up to the Edge*, arXiv:2102.00963v3. The [opened arXiv page](https://arxiv.org/abs/2102.00963v3), revised February 2, 2025, states complete delocalization for every fixed d≥3. Our old note's restriction to “fixed large d” is therefore out of date for delocalization.

[Proposition 3.1](https://github.com/openai/math/blob/main/preprints/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/build/sections/03-entropy.tex) claims polynomial approximation of any fixed-degree monomial in endpoint coordinates for fixed numbers of sampled edges and nearby bulk eigenvectors, uniformly over graph-measurable choices of the eigenindices. This is substantial eigenvector information, but its observables have no prescribed spatial weights. It is not a statement of spatial QUE.

Candidate verdict: PARTIAL-CLAIMED, covering clean fixed-degree bulk point-process universality, with delocalization as an existing input.

## Candidate 2: Fixed-energy universality for weak Anderson disorder on random regular graphs

Author: OpenAI. Date: October 5, 2026. [Original main source](https://github.com/openai/math/blob/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/build/paper.tex), [main theorem source](https://github.com/openai/math/blob/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/build/sections/01-introduction.tex). Local copies: Anderson-paper.tex and Anderson-introduction.tex.

### Exact main theorem

Theorem 1.1, copied verbatim as TeX:

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

Here
\[
H_{n,d,w}=A_{n,d}+w\operatorname{diag}(\omega_1,\ldots,\omega_n),
\qquad \omega_v\stackrel{\mathrm{iid}}{\sim}\operatorname{Unif}[-1,1],
\]
independently of the graph. The measure \(\nu_{d,w}\) is the expectation of the root spectral measure of the corresponding infinite-tree operator, and \(\rho_{d,w}\) is its density. The GOE comparison has the same unit-intensity normalization as Candidate 1.

### Comparison

| Aspect | Comparison with our row |
| --- | --- |
| Model | Same uniform simple labelled graph underneath, but a different matrix: independent random diagonal potentials are added. Our row concerns clean adjacency. |
| Degree and energy | Every fixed d≥3; each fixed energy in a compact subinterval of the clean band. The smallness threshold depends on d and the edge margin κ. Each interior energy can be enclosed in such a band, but w must then meet that band’s threshold. |
| Disorder | Fixed positive 0<w<w0. The theorem excludes w=0 and says nothing uniform as w approaches zero with n. Substituting w=0, or interchanging the w→0 and n→∞ limits, is not authorized by this statement. |
| Density and quantity | Fixed-energy full microscopic point-process convergence, unfolded by the disordered tree density, not the clean Kesten–McKay density. Averaging is over both graph and potentials. |
| Strength | An asymptotic limit, not merely a bound; no explicit rate or explicit permitted disorder strength in Theorem 1.1. |
| Eigenvectors / QUE | Conditional Gaussian marks enter the proof, with a random variance determined by the local tree environment. The main theorem states no spatial QUE or new all-eigenvector delocalization assertion for our clean model. |

The paper cites Candidate 1 as a companion input/method. It extends the spectral-statistics claim to a different operator; it does not supply the missing clause in our row. Candidate verdict relative to the clean row: NOT-THIS as a direct theorem, though it is a related extension.

## Candidate 3: Conformal universality of bulk Ising correlations under weak interactions

Author: OpenAI. Date: September 23, 2026. [Original main source](https://github.com/openai/math/blob/main/preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/build/main.tex), [model and main theorem source](https://github.com/openai/math/blob/main/preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/build/sections/model.tex). Local copies: Ising-main.tex and Ising-model.tex.

### Exact main theorem

Theorem 1.1, copied verbatim as TeX:

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

The hypotheses “as above” specify J>0 and a fixed translation-, reflection-, and quarter-turn-invariant potential V on finite even subsets of the square lattice, of bounded range, with signed coefficients allowed. D is a bounded simply connected planar domain with C² Jordan boundary, and D_a=D∩aZ². The lattice fields are the rescaled spin a^{-1/8}σ and the rescaled, actual-state-centered bond energy a^{-1}(σσ−〈σσ〉); the comparison functions are the nearest-neighbor critical Ising limits. The mesh a tends to zero.

This is a two-dimensional Gibbs spin model with mixed spin/energy correlation functions and conformal covariance. There is no d-regular random graph, adjacency spectrum, Kesten–McKay law, GOE process, or eigenvector assertion. “Bulk” refers to points in a planar domain and “energy” to an Ising observable, not adjacency eigenvalues. Candidate verdict: NOT-THIS.

## Follow-ups and verification status

### Later scholarly papers actually opened

1. **Yukun He, Jiaoyang Huang, Xiaoyu Wang, *Bulk universality of random regular graphs*, arXiv:2610.08127v1, October 6, 2026.** Opened the [arXiv abstract page](https://arxiv.org/abs/2610.08127) and [full HTML](https://arxiv.org/html/2610.08127v1), including the main point-process theorem, Theorem 1.1 on gaps/correlations, and eigenvector statements in the introduction. This is a separate paper, not an identified arXiv version of OpenAI’s manuscript. It states fixed-energy Sine_1 convergence for every fixed d≥3, plus deterministic-label gap and fixed-energy correlation-measure universality. Its coordinates Nπρ_d(E)(λ−E) give intensity 1/π; OpenAI’s Nρ_d(E)(λ−E) give intensity one. The factor π reconciles the normalizations. A full-text search found no “OpenAI” occurrence. The paper’s existence does not validate the OpenAI proof.
2. **Jaehun Lee, *Mesoscopic eigenvalue statistics for random regular graphs: a case study*, arXiv:2611.09215v1, November 6, 2026.** Opened the [abstract page](https://arxiv.org/abs/2611.09215) and [full HTML](https://arxiv.org/html/2611.09215v1). Its introduction cites He–Huang–Wang and OpenAI for bulk universality; bibliography [40] names Candidate 1. It proves a mesoscopic CLT for a restricted test class at (log N)^{-1}≪η≪1. This is a later scholarly citation and related result, not a referee report or a proof audit, and it supplies no missing QUE theorem.

No arXiv version under any of the three exact OpenAI titles was identified by the searches. The date printed in an OpenAI manuscript should not be equated with a documented public priority date; the sources here do not establish a precedence judgment.

### Repository records actually opened

- [Repository README](https://github.com/openai/math): raw model-produced research, varying verification status, possible issues in unformalized work.
- [History](https://github.com/openai/math/blob/main/history.md), through the visible October 29 entry: no named correction or withdrawal of these three candidates. Opened each candidate README; none carried a correction or withdrawal notice.
- [CONTENTS.md](https://github.com/openai/math/blob/main/CONTENTS.md): the graph papers form family 219; Ising belongs to family 218.
- [lean/README.md](https://github.com/openai/math/blob/main/lean/README.md), [lean/ directory](https://github.com/openai/math/tree/main/lean), [lean/docs/ directory](https://github.com/openai/math/tree/main/lean/docs), [formalization.yaml](https://github.com/openai/math/blob/main/lean/formalization.yaml), and [OAI.lean](https://github.com/openai/math/blob/main/lean/OAI.lean): no listed family-219 formalization or matching graph-bulk theorem was identified. There is no 219.md in the opened docs listing. Other modules with “Anderson” in their names concern other families and are not evidence of formalizing these papers.
- [lean/docs/218.md](https://github.com/openai/math/blob/main/lean/docs/218.md): explicitly covers only the finite-graph buffered likelihood comparison from *Buffered comparison and stopping-band resolution in critical Ising*. It does not formalize Candidate 3’s conformal-universality theorem.
- [BufferedIsing challenge](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/BufferedIsing.lean): opened the actual finite statement. The challenge ends in sorry by design; it is not the separate proof module. No Lean build was run, and no claim of a checked main theorem follows.

### Expositions and commentary actually opened

- [Latent Seminar, *Microscopic spectra of random regular graphs*](https://lowrank.github.io/latent-seminar/OpenAI-Math/219-random-regular-spectra), dated October 6: explains the claims and selected mechanisms; explicitly says it is not a complete independent verification.
- [Plectis Atlas, family 219](https://wcook04.github.io/plectis-atlas/families/219.html): displays theorem material and reports no supplied Lean statement. It runs no checks itself.
- [AI Proved What, family 219](https://aiprovedwhat.com/episodes/219-goe-bulk-universality-regular-graphs/): the opened page says preprint, no peer review or Lean check, last checked October 16. Search snippets returned a longer episode text than the opened page; no conclusions here rely on that unavailable expanded text.
- [oai-math-revised, Candidate 3 entry](https://mathcommunity.github.io/oai-math-revised/papers/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/), updated November 4: no contributed notes; automatically collected notes are explicitly unreviewed. It distinguishes the finite comparison formalization from the main Ising theorem.
- [Post-Cutoff family catalogue](https://postcutoff.com/science/openai-math/): opened because the search result labels family 219 confirmed by an independent expert and cites the He–Huang–Wang paper. The fetched page did not expose that exact family passage in the returned excerpt. The search label is not treated as evidence that anyone audited the OpenAI proof.

The exact-title searches, including “error”, “gap”, “refutation”, “review”, and “arxiv”, found no identified specialist error report, referee report, or complete expert verification for these candidates. This is a bounded search result, not an assertion that no such comment exists anywhere. No new spatial QUE theorem in the OpenAI candidates was found.

### Correction to the old note about QUE

Opened Roland Bauerschmidt, Jiaoyang Huang, Horng-Tzer Yau, *Local Kesten–McKay law for random regular graphs*: [arXiv page](https://arxiv.org/abs/1609.09052) and [original PDF](https://arxiv.org/pdf/1609.09052), particularly Corollary 1.3(ii), equation (1.7), and its proof. It explicitly gives probabilistic QUE for deterministic mean-zero test vectors, uniformly over bulk eigenvectors, under its sufficiently-large-fixed-degree assumptions. Its index-set form (1.8) also concerns deterministic sets; graph-dependent tests are excluded. This is not merely quantum ergodicity averaged over eigenvectors.

Also opened Jiaoyang Huang, *Spectral Statistics of Sparse Random Graphs*, ICM 2026 proceedings, [official full text, Section 4.3](https://epubs.siam.org/doi/10.1137/25M180603X). The survey states a probabilistic QUE form without eigenvector averaging after discussing complete delocalization. It does not supply an explicit all-degrees quantitative QUE theorem in that passage.

Thus “QUE at fixed d is open” cannot be retained without specifying the intended stronger assertion and its degree range. The present verification does not prove a new corollary from exchangeability and delocalization or settle that ambiguity by choosing stronger quantifiers. The defensible release verdict is PARTIAL-CLAIMED: its explicit clean main theorem is bulk point-process universality, and it states no additional spatial QUE theorem. This is not evidence that every formulation called QUE remains open.

## Recommended replacement for “where it stands”

Bulk GOE statistics for every fixed d≥3 are proved in Yukun He, Jiaoyang Huang and Xiaoyu Wang’s *Bulk universality of random regular graphs* (arXiv:2610.08127, October 6, 2026); OpenAI’s unrefereed *GOE bulk universality for fixed-degree random regular graphs* (September 23, 2026) also claims the fixed-energy point-process result. Complete delocalization for every fixed d≥3 is already known from Jiaoyang Huang and Horng-Tzer Yau, while OpenAI’s *Fixed-energy universality for weak Anderson disorder on random regular graphs* (October 5, 2026) claims an extension with small fixed positive uniform diagonal disorder. The release states no additional spatial QUE theorem, and our QUE clause needs a precise formulation: probabilistic QUE against deterministic vertex tests was already established for sufficiently large fixed d by Roland Bauerschmidt, Jiaoyang Huang and Horng-Tzer Yau, Corollary 1.3.

Sources for the proposed three-sentence replacement are the opened He–Huang–Wang paper, the two original OpenAI theorem sources above, [Huang–Yau arXiv:2102.00963v3](https://arxiv.org/abs/2102.00963v3), and [Bauerschmidt–Huang–Yau, Corollary 1.3](https://arxiv.org/pdf/1609.09052). “Proved” in the first sentence reports the mathematical literature’s theorem claim; this verification does not certify that proof either.

## Spot check

The selected dependency is **Lemma 3.5 (Tensor coercivity)**, label ent:tensor, in the clean GOE paper’s [Section 3 source](https://github.com/openai/math/blob/main/preprints/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/build/sections/03-entropy.tex). This is the strict inequality that rules out the first non-Gaussian Hermite coefficient in the moment argument. The introduction and Section 3 identify it as the step where the open bulk and d≥3 enter. The check below concerns this finite-dimensional lemma only; it does not check the subsequent entropy expansions, limiting switching construction, or DBM application.

Its exact statement is:

```tex
\begin{lemma}[Tensor coercivity]\label{ent:tensor}
For every fixed \(j\ge3\), there exists \(c_j>0\) such that every
symmetric \(j\)-tensor \(H\) on \(D\) satisfying
\(\sigma_i^{\otimes j}P_i^{\otimes j}H=P_i^{\otimes j}H\) for all
\(i\) obeys
\begin{equation}\label{eq:ent-tensor}
 \|H\|^2-\frac12\sum_{i=1}^d\|P_i^{\otimes j}H\|^2
 \ge c_j\|H\|^2 .
\end{equation}
\end{lemma}
```


The geometry is fixed: \(p=E/d\), \(a=d(1-p^2)/(d-1)\), \(P\) projects \(\mathbb R^d\) onto \({\bf1}^{\perp}\), \(D=(\mathbb R\oplus{\bf1}^{\perp})\otimes\mathbb R^\ell\), and \(w\) is the unit central vector. Set \(v_i=pw+\sqrt a\,Pe_i\), \(U_i=\operatorname{span}(w,v_i)\otimes\mathbb R^\ell\); \(P_i\) is its orthogonal projection, and \(\sigma_i\) swaps \(w,v_i\) on this plane, acting trivially on colors.

The following checks use only these displayed definitions, with no external lemma taken on trust.

1. **Normalization and strict weights.** Since \(\|Pe_i\|^2=(d-1)/d\), \(\|v_i\|^2=p^2+a(d-1)/d=1\). With \(q=\sqrt{1-p^2}\), the bulk condition \(|E|<2\sqrt{d-1}\) is exactly \(q>(d-2)/d\). Thus
   \[
   b_s=\frac{q-(d-2)/d}{2q},\qquad
   b_t=\frac{q+(d-2)/d}{2q}
   \]
   are strictly positive and sum to one. The orthonormal bisectors \(s_i,t_i\) in the paper have squared central coordinates \((1+q)/2,(1-q)/2\). Their weighted central contribution is
   \[
   d\left(b_s\frac{1+q}{2}+b_t\frac{1-q}{2}\right)=1.
   \]
   Their mixed block sums to zero because \(\sum_iPe_i=0\). The neighbor block is a scalar multiple of identity by permutation symmetry; total trace d and central trace 1 give the neighbor block identity. This independently verifies the weighted-frame identity used in the proof.

2. **Nonnegative deficit.** Resolve the first tensor slot using that positive weighted frame. In each term, projecting the remaining slots into \(U_i\) decreases the squared norm, because orthogonal projections are contractions and act in different slots. For \(K_i=P_i^{\otimes j}H\), swap invariance exchanges the \(s_i\)- and \(t_i\)-components, so their squared norms agree; their sum is \(\|K_i\|^2\). The projected weighted sum is consequently \(\frac12\sum_i\|K_i\|^2\). Hence the asserted quadratic deficit is nonnegative.

3. **Equality and the use of three slots.** Positive weights force every discarded squared norm to vanish in the equality case. Summing the \(s_i,t_i\) terms yields
   \[
   P_i^{(r)}H=P_i^{\otimes j}H
   \quad\text{for each slot }r.
   \]
   Tensor symmetry supplies all slots from the first. The proof’s three-slot calculation is valid: projections in different slots commute, and the equality above can be applied to H each time before multiplying by the other-slot operator. It gives
   \[
   P_i^{(1)}P_k^{(1)}H
   =P_i^{(1)}P_k^{(2)}H
   =P_k^{(2)}P_i^{(3)}H
   =P_i^{(3)}P_k^{(1)}H
   =P_k^{(1)}P_i^{(1)}H.
   \]
   Thus the same-slot commutator annihilates H. This explains why j≥3, rather than just j≥2, is essential in this argument.

4. **No remaining equality direction.** In spatial coordinates write \(e_i'=Pe_i/\|Pe_i\|\); then \(P_i=ww^{\mathsf T}+e_i'(e_i')^{\mathsf T}\), tensored with the color identity. For i≠k, \(c=\langle e_i',e_k'\rangle=-1/(d-1)\). Direct multiplication gives
   \[
   [P_i,P_k]
   =c\bigl(e_i'(e_k')^{\mathsf T}-e_k'(e_i')^{\mathsf T}\bigr).
   \]
   On their two-plane its determinant is \(c^2(1-c^2)>0\), since d≥3. Thus its kernel is the orthogonal complement of that plane. These neighbor planes together span \({\bf1}^{\perp}\), so the common spatial kernel is precisely the central line. The tensor must be supported on \((w\otimes\mathbb R^\ell)^{\otimes j}\). Projected swap invariance also puts it on \((v_i\otimes\mathbb R^\ell)^{\otimes j}\); those tensor spaces have zero intersection since the two spatial lines are distinct. Therefore H=0.

For fixed d,E,ell,j, the constraint space is finite-dimensional and closed. Positivity away from zero on its unit sphere supplies the claimed \(c_j>0\). Its size is not claimed uniform as E approaches an edge; the weight \(b_s\) vanishes there. This is consistent with the bulk restriction.

**Finding:** the frame algebra, contraction step, equality argument and compactness step in this lemma withstand this check. No error was found in this selected lemma. This gives no conclusion about correctness of the complete preprint, or about a spatial QUE theorem absent from its statements.


