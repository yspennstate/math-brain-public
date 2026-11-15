# T013: critical square-lattice FK conformal limits

Checked 14 November 2026. Verdict: **SOLVED-CLAIMED**, for the entire stated parameter range and both interface and loop conclusions. This records the scope of the claim; it does not certify the proof.

## 1. Conformal Limits of Critical Square-Lattice Random-Cluster Interfaces

Author: **OpenAI**. Date on the manuscript: **October 5, 2026**. Opened the manuscript's TeX, not just its abstract: [main.tex](https://github.com/openai/math/blob/main/preprints/Conformal-Limits-of-Critical-Square-Lattice-Random-Cluster-Interfaces-October-5-2026/build/main.tex), [introduction.tex](https://github.com/openai/math/blob/main/preprints/Conformal-Limits-of-Critical-Square-Lattice-Random-Cluster-Interfaces-October-5-2026/build/sections/introduction.tex). The exact introductory source is saved as [sources/c1-introduction.tex](sources/c1-introduction.tex).

Theorem 1.1, “Interfaces and all nested loops,” is copied below exactly from the TeX source, including its source labels:

```latex
\begin{theorem}[Interfaces and all nested loops]
\label{intro:main}
For every fixed real $1\le q\le4$, the following assertions hold.
\begin{enumerate}[label=\textup{(\roman*)}]
\item For every bounded Jordan domain $D$ with distinct boundary marks
$a,b$, and every approximation satisfying
\eqref{intro:marked-jordan}, the Dobrushin strand $\eta_n$ converges in
law, in \eqref{intro:curve-metric}, to chordal $\SLE_{\kappa(q)}$ from
$a$ to $b$ in $D$.
\item Under the specified free infinite-volume law,
$\Gamma_\delta$ converges in law as $\delta\downarrow0$ to the nested
whole-plane $\CLE_{\kappa(q)}$, in the spherical collection topology
just defined.  The limit is M\"obius invariant.
\end{enumerate}
Both conclusions hold along every mesh sequence.  No uniformity in $q$
is asserted.
\end{theorem}
```

The referenced definitions immediately preceding the theorem are part of its meaning:

- The graph is the nearest-neighbor square lattice with its ordinary Euclidean embedding. Its probability law is proportional to \(p_q^{|A|}(1-p_q)^{|E|-|A|}q^{k_\xi(A)}\), with \(p_q=\sqrt q/(1+\sqrt q)\). This is the model in our row, not a random map or a changed embedding.
- The parameter is exactly \(\kappa(q)=4\pi/\arccos(-\sqrt q/2)\), with the inverse cosine in \([0,\pi]\).
- A domain approximation is the interior of a simple nearest-neighbor lattice polygon. Counterclockwise boundary parametrizations converge uniformly, with the distinct marks fixed at parameters \(0,1/2\). The counterclockwise arc from \(b_n\) to \(a_n\) is wired, the complementary arc is free, and the interface is oriented from \(a_n\) to \(b_n\). Wired-arc boundary edges are omitted from sampling and declared open for drawing; because their endpoints are already identified, this gives the ordinary FK marginal on all other edges.
- The curve metric is uniform distance modulo increasing reparametrization. It retains ordered traversal, including repeated visits; it does not assert convergence in natural or capacity parametrization.
- The loop experiment uses the free infinite-volume FK law on \(\mathbb Z^2\). It keeps every nesting level. Its spherical matching topology pairs all loops above each diameter cutoff and retains distinct copies even if their images coincide. The limit is the nested whole-plane CLE.

### Comparison with every clause of our row

| Our statement | What the theorem actually claims | Coverage |
| --- | --- | --- |
| Critical FK random-cluster model on \(\mathbb Z^2\) | Same square lattice, Euclidean embedding, FK probability weights, \(p_c=\sqrt q/(1+\sqrt q)\) | Exact model match |
| Dimension two | Domains in \(\mathbb C\), mesh-scaled \(\mathbb Z^2\) | Exact match |
| \(1\le q\le4\) | Every fixed real \(1\le q\le4\), including both endpoints | Entire range; no uniformity as \(q\) varies |
| Interfaces converge to SLE | Dobrushin strands converge in law to chordal SLE in every bounded marked Jordan domain with the specified uniform boundary approximation | Full usual chordal-interface formulation; not merely tightness, subsequential limits, or crossing bounds |
| \(\kappa=4\pi/\arccos(-\sqrt q/2)\) | Exactly the same formula | Exact match |
| \(\kappa(1)=6,\ \kappa(2)=16/3,\ \kappa(4)=4\) | The formula yields \(\arccos(-1/2)=2\pi/3,\ \arccos(-1/\sqrt2)=3\pi/4,\ \arccos(-1)=\pi\) | All three values agree |
| Full loop ensemble converges to CLE | Complete nested free-plane loops converge in law to nested whole-plane CLE with matching of full loops | Explicitly covers the full-loop clause |
| Convergence | Both assertions hold along every mesh sequence | Full limit, not just an existence result |

Thus no part of T013's stated SLE/CLE prediction is omitted from the **claim**. The row leaves boundary conditions and topology implicit; the theorem makes the standard Dobrushin-interface and free-plane-loop versions precise. It does not claim arbitrary boundary conditions, arbitrary lattices, uniformity in \(q\), or time-parametrized interfaces; none is required by our row. The \(q=1\) case therefore also claims the square-lattice bond-percolation instance identified as T002.

## 2. Self-dual random-cluster interfaces below one

Author: **OpenAI**. Date: **September 23, 2026**. Opened [main.tex](https://github.com/openai/math/blob/main/preprints/Self-dual-random-cluster-interfaces-below-one-September-23-2026/build/main.tex) and [00-introduction.tex](https://github.com/openai/math/blob/main/preprints/Self-dual-random-cluster-interfaces-below-one-September-23-2026/build/sections/00-introduction.tex); the latter is saved as [sources/c2-introduction.tex](sources/c2-introduction.tex).

Theorem 1.1, “Below-one interface convergence,” exactly as in the TeX:

```latex
\begin{theorem}[Below-one interface convergence]\label{thm:main}
For every fixed $q\in(0,1)$ and every marked domain approximation just
specified, the laws of $\eta_\delta$ converge as $\delta\to0$ in
the metric \eqref{eq:curve-metric} to chordal
$\SLE_\kappa(D;a,b)$, where
\[
 \kappa=\frac{4\pi}{\arccos(-\sqrt q/2)}.
\]
The convergence holds along the full mesh sequence.
\end{theorem}
```

Here the preceding setup requires a bounded Jordan domain with smooth simple boundary, simple nearest-neighbor polygon approximations with uniformly convergent marked boundary parametrizations, and the ordinary finite wired/free FK law at the self-dual parameter. The curve metric is again uniform distance modulo increasing reparametrization. The paper explicitly does not require prior identification of an infinite-volume critical point for \(q<1\).

The model and dimension agree with ours, but the main theorem's range \(0<q<1\) has **no intersection** with \(1\le q\le4\): in particular it excludes \(q=1\). Its \(\kappa\) lies in \((6,8)\), outside our row's \([4,6]\), and it concerns one interface, not a complete CLE loop ensemble. Taken alone, the main theorem is **NOT-THIS** for T013.

There is nevertheless an important relevant secondary statement: Corollary 1.3, “Combined finite-law parameter range,” claims chordal SLE convergence for every fixed \(0<q<4\) in smooth Jordan domains. Its proof invokes Theorem 1.1(i) of the September 23 companion *Square-lattice FK interfaces and nested loops for \(1\le q<4\)* for the range \(1\le q<4\). Therefore the paper as a whole repeats a **PARTIAL-CLAIMED** T013 assertion: the interface part for \(1\le q<4\), under smooth-domain hypotheses, using that companion. It excludes \(q=4\), supplies no CLE assertion here, and is not an independent proof of the relevant range. The exact corollary and its dependency are in the saved source.

## 3. Random Walks on Critical FK–Ising Maps and Liouville Brownian Motion

Author: **OpenAI**. Date: **October 5, 2026**. Opened [main.tex](https://github.com/openai/math/blob/main/preprints/Random-Walks-on-Critical-FK-Ising-Maps-and-Liouville-Brownian-Motion-October-5-2026/build/main.tex) and [introduction.tex](https://github.com/openai/math/blob/main/preprints/Random-Walks-on-Critical-FK-Ising-Maps-and-Liouville-Brownian-Motion-October-5-2026/build/sections/introduction.tex); saved as [sources/c3-introduction.tex](sources/c3-introduction.tex).

Theorem 1.1, exactly as in the TeX:

```latex
\begin{theorem}\label{thm:main}
Let $(M_n,A_n)$ have law \eqref{eq:fk-law}, and let $a_n>0$ be any
deterministic sequence with $a_n\to0$ such that
\begin{equation}\label{eq:assumed-ghp}
 (V_n,a_nd_n,\mu_n)\ \Longrightarrow\ (S,D_h,\mu_h)
\end{equation}
in Gromov--Hausdorff--Prokhorov law. Given the map, start $r$ independent
simple random walks $X^{n,1},\ldots,X^{n,r}$ independently from $\mu_n$.
Given $h$, start $r$ independent Liouville Brownian motions
$B^{h,1},\ldots,B^{h,r}$ independently from $\mu_h$, with the convention
\eqref{eq:continuum-form}. For every fixed integer $r\ge1$,
\begin{equation}\label{eq:main-limit}
 \left(\overline M_n,a_nd_n,\mu_n;
       (\overline X^{n,j}_{nt})_{t\ge0,\,1\le j\le r}\right)
 \ \Longrightarrow\
 \left(S,D_h,\mu_h;
       (B^{h,j}_t)_{t\ge0,\,1\le j\le r}\right)
\end{equation}
in the curve-decorated Gromov--Hausdorff--Prokhorov topology.
\end{theorem}
```

The preceding definitions sample rooted pairs \((M,A)\) of a planar multigraph and an FK edge set, with \(n\) edges and weight proportional to \(2^{\ell(M,A)/2}\); loops and multiple edges are allowed. The metric is graph distance, \(\mu_n(v)=\deg(v)/(2n)\), and the walks use every map edge, not just open FK edges. The continuum object is the ordinary unit-area \(\sqrt3\)-Liouville quantum gravity sphere. The theorem assumes a deterministic metric scaling giving that metric-measure limit, and the prose explicitly imports additional electrical and operator results from a spectral companion.

This is **NOT-THIS**. It has \(q=2\) FK decoration on a random planar map, rather than the fixed square lattice; its quantity is a stationary walk trajectory, rather than an FK interface or loop ensemble; and its limit is time-parametrized Liouville Brownian motion jointly with a random surface, rather than SLE/CLE in a Euclidean domain. The fact that both settings are planar does not bridge these differences. It establishes no clause of T013, even its already-known \(q=2\) lattice-interface clause.

## Follow-ups and verification status

Searches used the web search tool, with exact titles, arXiv restrictions, and the additional terms “error,” “gap,” “correction,” “review,” and “referee.” The findings below are limited to the sources actually opened, as of 14 November 2026.

### Error report and partial automated reviews

Opened Jim Jardine / Lattice24's [openai-math-audit README](https://github.com/JJardine919/openai-math-audit/blob/main/README.md), [RESULTS.tsv](https://github.com/JJardine919/openai-math-audit/blob/main/RESULTS.tsv), [original rank-35 error report](https://github.com/JJardine919/openai-math-audit/blob/main/evidence/review_035_square_lattice_fk.json), and [first skeptic report](https://github.com/JJardine919/openai-math-audit/blob/main/evidence/skeptic1_035.json). Its audit status is dated October 16, with an October 28 update.

Finding 1 names the **September 23 companion**, not the October 5 candidate. It reports that the reflection argument's strict power saving would also suppress the undifferenced normalized observable, contradicting its required nonzero factorization. Its update says this finding was unchanged upstream. The report describes Claude-generated reviews and three skeptic passes; this is a published model-assisted error report, not a human specialist's referee judgment.

The same audit's candidate-specific reports were opened:

- [rank_023.json](https://github.com/JJardine919/openai-math-audit/blob/main/reviews/rank_023.json), on candidate 1, says “no_gap_found” but explicitly leaves the physical reflection transfer, normalization, gap closure, and several later sections unchecked.
- [rank_027.json](https://github.com/JJardine919/openai-math-audit/blob/main/reviews/rank_027.json), on candidate 2, is partial and leaves many of its main analytic estimates unchecked; it identifies the corollary's dependency on the September companion.
- [rank_364.json](https://github.com/JJardine919/openai-math-audit/blob/main/reviews/rank_364.json), on candidate 3, reports checking its path-limit argument while leaving the companion's substantive proofs unverified.

Consequently “no gap found” in the table is not complete verification. The October candidate contains the same cited normalization and strict-budget steps; the source-level check is below. The audit does not establish a refutation of the conjectured limits themselves.

### Exposition, arXiv, and the independent q=4 paper

Opened [Latent Seminar, *Random-cluster curves: conformal limits and natural time*](https://lowrank.github.io/latent-seminar/OpenAI-Math/223-fk-interfaces), dated October 6, 2026. It explains the family and the distinct \(q=4\) field argument, but explicitly disclaims independent verification of complete proofs. Also opened the three candidate pages on [oai-math-revised (candidate 1)](https://mathcommunity.github.io/oai-math-revised/papers/Conformal-Limits-of-Critical-Square-Lattice-Random-Cluster-Interfaces-October-5-2026/), [candidate 2](https://mathcommunity.github.io/oai-math-revised/papers/Self-dual-random-cluster-interfaces-below-one-September-23-2026/), and [candidate 3](https://mathcommunity.github.io/oai-math-revised/papers/Random-Walks-on-Critical-FK-Ising-Maps-and-Liouville-Brownian-Motion-October-5-2026/). Their collected commentary is explicitly unreviewed and AI-generated; it was used to locate original sources.

No arXiv version of any of the three OpenAI titles, human referee report, or named specialist endorsement of their proofs was found in the searches. This is a bounded search result, not a claim that none exists.

Opened both the [arXiv page](https://arxiv.org/abs/2610.08507) and [full HTML paper](https://arxiv.org/html/2610.08507v1) for **Emile Averous, Hugo Duminil-Copin, Tiancheng He, Piet Lammers and Ioan Manolescu**, *Conformal invariance of the planar four-state Potts model and its random-cluster representation*, submitted **October 6, 2026**. Theorem 1.2 states free-boundary \(q=4,p=2/3\) loop convergence to CLE(4) in simply connected domains under Carathéodory approximation; its proof explicitly extends the outermost-loop result to nested loops. This is the independent endpoint preprint already in our note, not an arXiv version or validation of OpenAI's general-\(q\) argument. No journal reference is listed on the opened arXiv page.

### Lean and release changes

Opened the official [repository README](https://github.com/openai/math/blob/main/README.md), [lean/README.md](https://github.com/openai/math/blob/main/lean/README.md), [lean/formalization.yaml](https://github.com/openai/math/blob/main/lean/formalization.yaml), [lean/docs/211.md](https://github.com/openai/math/blob/main/lean/docs/211.md), and [history.md](https://github.com/openai/math/blob/main/history.md), plus each manuscript's README. Attempting [lean/docs/223.md](https://raw.githubusercontent.com/openai/math/main/lean/docs/223.md) returned 404. No entry identifying any candidate manuscript was found in the formalization catalogue.

The family-211 Lean scope note is **only for the \(q>4\) Brownian continuum-random-tree limit of FK maps**. A family-level Lean badge therefore does not certify candidate 3's FK–Ising walk theorem, much less T013. No Lean proof of either square-lattice candidate was located. No Lean build was attempted.

The official history and candidate READMEs record no repair or withdrawal of these three titles. The general README warns that some unformalized results may have issues and presents the collection as model-produced research material. Absence of a listed correction is not confirmation of correctness.

## Recommended replacement “where it stands” text

The established \(q=2\) result and the separate October 6, 2026 \(q=4\) loop preprint of Emile Averous, Hugo Duminil-Copin, Tiancheng He, Piet Lammers and Ioan Manolescu remain the baseline. OpenAI's *Conformal Limits of Critical Square-Lattice Random-Cluster Interfaces* (October 5, 2026) claims the full SLE/CLE statement for every \(1\le q\le4\), including \(q=1\), but no matching Lean proof or human referee validation was found. Record the general-range advance as claimed and unrefereed, with a model-assisted error report on the September companion's shared holomorphicity argument, rather than marking the remaining cases settled.

## Spot check

Selected result: the October manuscript's Proposition **“Mixed derivative saving”**, label `hol:mixed-bound`, in [observable.tex](https://github.com/openai/math/blob/main/preprints/Conformal-Limits-of-Critical-Square-Lattice-Random-Cluster-Interfaces-October-5-2026/build/sections/observable.tex). This is the analytic step that supplies holomorphicity of the crossing observable for \(q<4\), hence supports the identification of the SLE driver and the loop limits. It asserts
\[
 \left|(\delta_{1,z}^{(2)}+i\delta_{2,z}^{(2)})
            \delta_{j,u}^{(2)}\mathcal H_g(z,u)\right|
       =O(n^{-2-c}),\qquad c>0.
\]
The paper calls it a proposition; it is the lemma-sized estimate checked here. Read its proof, the reflection-cost subsection and templates, the normalized observable, gap closure and factorization, and the three exponent budgets in [preliminaries.tex](https://github.com/openai/math/blob/main/preprints/Conformal-Limits-of-Critical-Square-Lattice-Random-Cluster-Interfaces-October-5-2026/build/sections/preliminaries.tex). Full copies are saved locally as [sources/c1-observable.tex](sources/c1-observable.tex) and [sources/c1-preliminaries.tex](sources/c1-preliminaries.tex).

**The exponent arithmetic checks.** If \(\varepsilon\) is the expected extraction deficit, the two extracted angular powers multiply to \(n^{-2+2\varepsilon}\), since \((1+\rho)+(1-\rho)=2\). The claimed remaining cost is
\[
 E=3P+D_*+\tfrac12\sum_j\log(F_-(a_j)/F_+(a_j)).
\]
There are two charge lists of total charge one. Applying the charge budget to each gives half of their combined logarithmic ratio at most \(-P+o(\log n)\), so \(E\le2P+D_*+o(\log n)\). The rectangle budget gives \(P+D_*\le-2(C_0+C_1)+o(\log n)\le o(\log n)\), hence \(E\le P+o(\log n)\le-c_0\log n+o(\log n)\). This rederives the power and sign without assuming the proposition. Choosing \(2\varepsilon\) and the losses smaller than \(c_0\) gives the asserted exponent **if** the reflected physical norms have the claimed costs.

**The load-bearing doubt is the physical norm comparison, not the addition of exponents.** The strict saving in that subsection is attributed to the reflected boundary features and remote charge factors. It explicitly assigns bounded cost to unextracted insertions. The normalized function itself is
\[
 \mathcal H_g=\Xi_g/(Z_g^{\rm cap}\mathbb E_{\mu_g}[UT_g]).
\]
The Lattice24 objection is that the same reflection and leaf-cost argument can then be applied to the undifferenced \(\Xi_g\), retaining its two source insertions, and yields \(|\mathcal H_g|\le n^{-c_0+o(1)}\). Gap closure has positive multipliers bounded above and below; complete-wall factorization has a multiplier bounded away from zero and gives
\[
 \mathcal H_{\rm full}(z,u)=a_n h_n(z)J_n(u)+o(1).
\]
The proposed extension of the norm bound would therefore force \(h(z)J(u)=0\), whereas the boundary identification requires a nondegenerate conformal map \(h\), and the source proves that \(J\) has different boundary values. These are precisely the labels and equations present in the October candidate, not merely in the September paper named by the audit.

The unresolved point is whether the claimed leaf bound really extends to those undifferenced source diagrams, or whether the reflected norm/weight comparison omits a restriction or a compensating factor. The printed argument does not make such a distinction apparent. This is a substantive source-level concern corroborating the reported gap mechanism, not a completed independent refutation or a judgment that the main theorem is false.

Finally, deleting the strict saving would not repair this proof: \(n^{-2+2\varepsilon}\), divided by the squared stencil mesh \((2/n)^2\), is \(n^{2\varepsilon}/4\), which does not tend to zero. A bound that genuinely distinguishes the mixed stencil from the undifferenced observable is needed at this step. This spot check addresses \(q<4\); it does not audit the separate \(q=4\) field argument.

## Source record

All remote operations were reads. No git command, post, account creation, Lean compilation, or numerical simulation was used. The three introductory source files and the two checked proof sections are retained in `sources/`; their equations were not rewritten there. The repository's [Apache 2.0 license](https://github.com/openai/math/blob/main/LICENSE) was opened. TeX theorem quotations above preserve the source wording and macros; the explanatory text is new.

The supplied GitHub folder pages initially failed through the web cache. The GitHub connector's contents listings and raw-file reads succeeded. Directory listings were opened for each candidate root, build directory, and sections directory. Exact manuscript files opened are linked in the three candidate sections; follow-up files and the failed Lean documentation lookup are linked above.

Task: “Verify: has open problem T013 been settled by the OpenAI math release?” — 14 November 2026, 20:54:49 Asia/Tbilisi (PROMPT.md file timestamp; no separate user-message clock was supplied).

