RESOLVED_IN_LITERATURE

# C0119: higher-dimensional directed-polymer chaos

The Gaussian problem in the cited source has been resolved. **B. T. Graham, “Sublinear variance for directed last-passage percolation”, Journal of Theoretical Probability 25 (2012), 687–702, Theorem 6.1**, proves the required ground-state variance bound in every dimension. It appeared online on 6 October 2010; the first preprint dates to 2009. The theorem and proof are on pp. 14–15 of [arXiv:0909.1352v3](https://arxiv.org/abs/0909.1352v3). Combining it with Chatterjee's Theorem 3.2 proves the original chaos assertion.

The finite-temperature Gaussian formulation in the request is resolved as well: **K. S. Alexander and N. Zygouras, “Subgaussian concentration and rates of convergence in directed polymers”, Electronic Journal of Probability 18 (2013), paper 5, 1–28, Theorem 1.1 (journal pp. 2–3)**, supplies an (n/\log n) variance bound for every spatial dimension and every fixed finite inverse temperature. The OU calculation below supplies the overlap conclusion. This is a consequence of published results, not a new resolution of an open problem.

## 1. What the 2008 source actually asks and proves

Source examined: [S. Chatterjee, arXiv:0810.4221v2](https://arxiv.org/abs/0810.4221v2), 16 December 2008; retained as [plain text](sources/chatterjee_2008.txt).

Section 12(2), p. 59, asks: “Prove chaos in directed polymers in dimensions ≥ 3.” Read with Sections 1 and 8, this means **ground states in an i.i.d. standard Gaussian environment**. It does not formulate a finite-temperature polymer-measure theorem or specify a low-temperature phase.

The proved example has up-right paths in (\mathbb Z_+^2), hence one time and one transverse dimension. A path visits (n) vertices, its energy is minus the sum of their Gaussian weights, and its ground state (P_n) is the unique maximizing path. Perturb the weights by

\[
 g^t=e^{-t}g+\sqrt{1-e^{-2t}}\,g',\qquad g'\text{ independent of }g.
\]

The polymer definition on p. 2 requires some (t_n\downarrow0) such that

\[
 \sup_{t\ge t_n}\mathbb E|P_n\cap P_n^t|=o(n).
 \tag{1}
\]

Definition 1.5, p. 6, gives the corresponding covariance-overlap definition for general Gaussian maxima. Theorem 3.2, p. 12, proves monotonicity, making the supremum formulation equivalent to a bound at (t_n). Theorem 8.1, p. 38, gives (\operatorname{Var}M_n\le Cn/\log n) and the resulting overlap bound in the two-dimensional example. Theorem 1.1, p. 2, takes (t_n=(\log n)^{-1/2}).

There is a dimension convention to track. Chatterjee and Graham count total lattice dimension; below (d) denotes spatial dimension, so a nearest-neighbor polymer lives in (1+d) space-time dimensions. Graham's theorem applies in either convention, including the requested (d\ge3) spatial case.

## 2. The literature result resolving the original problem

[Graham's publisher record](https://link.springer.com/article/10.1007/s10959-010-0315-6) confirms the publication, dates, pages, and DOI **10.1007/s10959-010-0315-6**. Numbering and page references here are to the full text of arXiv:0909.1352v3, rather than inferred journal page positions.

Theorem 6.1, p. 14, assumes i.i.d. standard normal vertex weights and total dimension (D\ge2). It treats both:

- up-right paths in (\mathbb Z^D), with a free endpoint on the level set (S_N);
- paths on (\mathbb Z^{D-1}\times\mathbb Z), with an increment of one in time and one nearest-neighbor spatial step, with a free endpoint on (\widehat S_N).

It proves

\[
 \operatorname{Var}T(0,S_N)=O(N/\log N),\qquad
 \operatorname{Var}\widehat T(0,\widehat S_N)=O(N/\log N).
 \tag{2}
\]

The introduction, pp. 3–4, explicitly identifies Chatterjee's higher-dimensional ground-state question and says that both versions have an affirmative answer. Thus this is not merely a point-to-point LPP result being extrapolated to a different polymer geometry.

Here is the complete implication to chaos. For a finite Gaussian path family, (M_n(g)=\max_p\sum_{v\in p}g_v) has almost-everywhere gradient (\partial_v M_n=\mathbf1_{\{v\in P_n\}}). Therefore Chatterjee's Lemma 3.3, pp. 12–13, gives

\[
 \operatorname{Var}M_n
 =\int_0^\infty e^{-s}\mathbb E|P_n\cap P_n^s|\,ds.
 \tag{3}
\]

The integrand's overlap factor is nonnegative and nonincreasing by Lemma 3.5, p. 14. Hence for (t>0),

\[
 (1-e^{-t})\mathbb E|P_n\cap P_n^t|
 \le\operatorname{Var}M_n
 \le C_D n/\log n.
\]

Choosing (t_n=(\log n)^{-1/2}) proves (1), with expected normalized overlap (O((\log n)^{-1/2})). Markov's inequality also gives convergence to zero in probability. Including or excluding a common starting vertex changes the path length, overlap and variance by at most a constant; this has no effect on the conclusion.

## 3. Finite-temperature formulation and exact OU reduction

Fix spatial dimension (d\ge1), inverse temperature (0<\beta<\infty), and i.i.d. (N(0,1)) variables (g_{i,x}). Let (P_0) be the simple symmetric nearest-neighbor walk law, started at zero, with free endpoint. Define

\[
 H_n(g,S)=\sum_{i=1}^n g_{i,S_i},\quad
 Z_{n,\beta}(g)=E_0 e^{\beta H_n(g,S)},\quad
 F_n(g)=\log Z_{n,\beta}(g),
\]

\[
 \mu_{n,\beta}^g(dS)=Z_{n,\beta}(g)^{-1}e^{\beta H_n(g,S)}P_0(dS).
\]

Given (g,g^t), sample (S\sim\mu_{n,\beta}^g) and (\widetilde S\sim\mu_{n,\beta}^{g^t}) independently. Write

\[
 I_n(S,\widetilde S)=\sum_{i=1}^n\mathbf1_{\{S_i=\widetilde S_i\}},\qquad
 Q_n(t)=\mathbb E\big[(\mu_{n,\beta}^g\otimes
                   \mu_{n,\beta}^{g^t})(I_n)\big].
\]

Thus the overlap normalized to lie in ([0,1]) is (I_n/n). The finite-temperature version of (1) is (\sup_{t\ge t_n}Q_n(t)/n\to0) for some (t_n\to0).

**Exact reduction.** For every (n),

\[
 \boxed{\operatorname{Var}(\log Z_{n,\beta})
       =\beta^2\int_0^\infty e^{-t}Q_n(t)\,dt.}
 \tag{4}
\]

In particular,

\[
 Q_n(t)\le\frac{\operatorname{Var}(\log Z_{n,\beta})}
                    {\beta^2(1-e^{-t})},\qquad t>0,
 \tag{5}
\]

and

\[
 \frac{\operatorname{Var}(\log Z_{n,\beta})}{\beta^2}
 \le n(1-e^{-t})+e^{-t}Q_n(t).
 \tag{6}
\]

Consequently, for fixed (eta>0), (\operatorname{Var}(\log Z_{n,\beta})=o(n)) is equivalent to this (n)-normalized small-OU-time overlap criterion. There is a factor of (\beta^2) in (4) when the free energy is (log Z). It disappears for the convention (\beta^{-1}\log Z).

**Proof.** Only finitely many weights are reachable in (n) steps. Put (a_{i,x}(g)=\mu_{n,\beta}^g(S_i=x)). Direct differentiation gives

\[
 \partial_{g_{i,x}}F_n(g)=\beta a_{i,x}(g),\qquad
 \|\nabla F_n(g)\|^2=\beta^2\sum_{i,x}a_{i,x}(g)^2\le\beta^2 n.
 \tag{7}
\]

So (F_n\in L^2) and its gradient is square integrable. Apply the Gaussian covariance identity, Chatterjee's Lemma 3.3, to (F_n). Conditional independence of the two samples identifies

\[
 \mathbb E\langle\nabla F_n(g),\nabla F_n(g^t)\rangle
   =\beta^2\sum_{i,x}\mathbb E[a_{i,x}(g)a_{i,x}(g^t)]
   =\beta^2 Q_n(t),
\]

which proves (4).

For completeness, let (P_t) denote the OU semigroup. For any real (h\in L^2), reversibility and the semigroup property give

\[
 \mathbb E[h(g)h(g^t)]
 =\langle h,P_t h\rangle
 =\|P_{t/2}h\|_2^2.
\]

This is nonnegative and nonincreasing in (t), by (L^2) contraction. Apply it separately to each (a_{i,x}); their finite sum (Q_n(t)) is nonincreasing. Integrating (4) over ([0,t]) proves (5). Splitting at (t), using (Q_n(s)\le n) on the first interval and (Q_n(s)\le Q_n(t)) on the second, proves (6).

If (v_n=\operatorname{Var}F_n=o(n)), set (t_n=\sqrt{v_n/(\beta^2 n)}), with an additional (1/n) if necessary to make it positive. Equation (5) gives (Q_n(t_n)/n\to0), and monotonicity gives the supremum version. Conversely (6) proves (v_n=o(n)) whenever (t_n\to0) and (Q_n(t_n)=o(n)). This proves the reduction, including its converse.

**Independent normalization check.** Expand (F_n-\mathbb EF_n=\sum_{k\ge1}F_{n,k}) in orthogonal Gaussian Hermite chaoses. The covariance is (\sum_{k\ge1}e^{-kt}\|F_{n,k}\|_2^2), while the gradient covariance is (\sum_{k\ge1}k e^{-(k-1)t}\|F_{n,k}\|_2^2). Multiplication by (e^{-t}) and integration gives (\sum_{k\ge1}\|F_{n,k}\|_2^2=\operatorname{Var}F_n). This checks the time factor and the absence of an extra factor of two independently of the overlap calculation.

## 4. The needed finite-temperature variance bound is already published

[Alexander–Zygouras, Theorem 1.1](https://doi.org/10.1214/EJP.v18-2005), journal pp. 2–3 (also p. 2 of arXiv:1204.1819v2), concerns exactly the free-endpoint simple-walk partition function above, in (1+d) dimensions for every (d\ge1). Its hypotheses are nearly gamma disorder and

\[
 \int e^{4\beta|\omega|}\,\nu(d\omega)<\infty.
\]

It proves, for (n\ge2) and (u>0),

\[
 \mathbb P\left(|F_n-\mathbb EF_n|>
            u\sqrt{n/\log n}\right)\le K_0 e^{-K_1u}.
 \tag{8}
\]

The constants may depend on the fixed dimension, environment law and inverse temperature. The published 28-page version was also obtained and its theorem statement checked directly; it is retained as [plain text](sources/alexander_zygouras_published_2013.txt). The terminology in the title refers to a scale below (\sqrt n); (8) is an exponential tail in (u), not a claim of a Gaussian (e^{-cu^2}) tail on that scale.

For standard normal disorder the transport (H^{-1}\circ\Phi) in Definition 2.1 is the identity, so its derivative is one. Their nearly gamma bound holds with (A=0,B=1). All exponential moments of (|g|) are finite; explicitly (\mathbb E e^{a|g|}=2e^{a^2/2}\Phi(a)). Thus (8) applies for every fixed finite (\beta>0), including low temperature.

Integrating the tail, with (b_n=\sqrt{n/\log n}), gives

\[
 \begin{aligned}
 \operatorname{Var}F_n
 &=2b_n^2\int_0^\infty u\,
       \mathbb P(|F_n-\mathbb EF_n|>u b_n)\,du\\
 &\le\frac{2K_0}{K_1^2}\frac n{\log n}.
 \end{aligned}
 \tag{9}
\]

Combining (5) and (9) proves

\[
 \boxed{\frac{Q_n(t)}n\le
 \min\left\{1,\frac{C_{\beta,d}}{(1-e^{-t})\log n}\right\}.}
 \tag{10}
\]

Any (t_n\to0) with (t_n\log n\to\infty) works. In particular (t_n=(\log n)^{-1/2}) gives the same logarithmic conclusion as for ground states. This holds for every spatial dimension and every fixed positive finite inverse temperature.

There is also a later independent published check: **S. Chatterjee, “Superconcentration in surface growth”, Random Structures & Algorithms 62 (2023), 304–334, online 20 July 2022, DOI 10.1002/rsa.21108**, [arXiv:2103.09199](https://arxiv.org/abs/2103.09199). Section 2.4, Theorem 2.4(3), preprint p. 9, gives (\operatorname{Var}f(t,x)\le Ct/\log t), with (f) distributed as (\beta^{-1}\log Z_t). The paragraph immediately above it attributes finite-temperature superconcentration to Alexander–Zygouras and all-dimensional ground-state superconcentration to Graham. Its environment hypothesis is a Lipschitz image of a Gaussian, including Gaussian disorder.

The BKS/Talagrand route therefore succeeds, but not by simply asserting that every fixed-start occupation probability is small. Those probabilities need not be uniformly small at low temperature. Chatterjee's 2008 Section 8 explains this obstruction and the difficulty of keeping paths directed when shifting the start. Graham and Alexander–Zygouras supply the required geometric/randomization estimates. No unproved influence estimate is being inserted into (9).

## 5. Scope: temperature, disorder, endpoints, and overlap

The result above concerns **disorder perturbations at the same fixed temperature**, not a change in temperature. The 2008 question is not asking for a polynomial chaos rate: its separate Section 12(3) asks to improve the logarithmic fluctuation bound. The logarithmic scale already suffices for its definition of chaos.

At high temperature, normalized overlap can already vanish without a perturbation. In particular, at (eta=0) the measure is independent of the environment: (Q_n(t)=\sum_{i\le n}P(S_i=\widetilde S_i)) for every (t). This is (O(\sqrt n)), (O(\log n)), or (O(1)) in spatial dimensions 1, 2, or at least 3, respectively. Thus the (n)-normalized criterion is vacuous there. The OU proof divides by (eta^2), so (eta=0) must be handled separately in just this way.

At low temperature the conclusion can be substantive. If (p(\beta)=\lim n^{-1}\mathbb EF_n(\beta)) is differentiable, Gaussian integration by parts gives

\[
 \frac{\mathbb EF_n'(\beta)}n
    =\beta\left(1-\frac{Q_n(0)}n\right),\qquad
 \lim_{n\to\infty}\frac{Q_n(0)}n
    =1-\frac{p'(\beta)}\beta.
\]

The derivative limit follows from convexity. At points with (p'(\beta)<\beta), the unperturbed expected overlap is macroscopic, while (10) makes its perturbed counterpart vanish. This condition explains the low-temperature localization hypotheses appearing in Bates's work. The proof of (10) itself does not require differentiability or a phase identification.

Neither (8) nor the OU argument asserts the requested conclusion for every possible i.i.d. non-Gaussian law. Alexander–Zygouras allow certain non-Gaussian laws for variance, but the Gaussian gradient-to-unweighted-overlap identity uses Gaussian weights. A transformed Gaussian environment introduces transport derivatives into that identity. Nor do these results automatically cover arbitrary pinned endpoints: at a boundary endpoint there can be only one admissible path, whose energy variance is linear. The present conclusion concerns the standard free-endpoint models in the question and source.

The ground-state conclusion comes directly from Graham; we do not take (eta\to\infty) in a finite-temperature bound with uncontrolled constants.

## 6. Other literature requested: what was checked

The decisive full texts were read before treating C0119 as resolved. The following additional search records explain related results and avoid conflating localization, polynomial-chaos expansions, and disorder chaos. Page numbers refer to the named preprint version unless explicitly stated otherwise.

| Work checked | Result or scope; relation to C0119 |
|---|---|
| Chatterjee, *Superconcentration and Related Topics* (Springer, 2014), DOI 10.1007/978-3-319-03886-5 | Publisher contents and chapter previews checked: Chapter 3, pp. 23–31, treats superconcentration/chaos; Chapter 5, pp. 45–56, treats Talagrand's method and polymers. The full book was not accessible here. Nica's freely available 2012 lecture transcription was saved, explicitly as lecture notes, not as the book. No unverified book theorem number is used. |
| Comets, *Directed Polymers in Random Environments*, LNM 2175 (2017), DOI 10.1007/978-3-319-50487-2 | Publisher contents/overview checked: thermodynamics pp. 13–29, martingale and (L^2) region pp. 31–55, localization pp. 75–106. Full book not accessible; it is background, not the evidence for closure. |
| Chatterjee, “Disorder chaos and multiple valleys in spin glasses”, arXiv:0907.3381 | Search and abstract check: SK spin glasses, not a new high-dimensional lattice-polymer theorem. The 2008 Gaussian identity is already sufficient here. |
| Wei-Kuo Chen and collaborators | Searches located Chen's SK-with-field paper, arXiv:1109.3249, mixed even-spin paper arXiv:1211.7354, and Chen–Kim–Sen, arXiv:2404.09409, on short-range, diluted and Lévy spin glasses. These concern different systems; no lattice-polymer closure is attributed to them. |
| Ganguly–Hegde; Basu–Ganguly–Hammond and related work | Author lists and abstracts checked. Ganguly–Hegde, arXiv:2007.03594, concerns tail exponents for planar LPP under curvature/tail hypotheses. Basu–Ganguly–Hammond–Hegde, arXiv:2006.11448, concerns geodesic watermelons in planar LPP. The directly relevant dynamical-chaos theorem is **Ganguly–Hammond**, arXiv:2010.05837v2, Theorem 1.3, p. 9, published in *Communications of the AMS* 4 (2024), 387–479: a transition near OU time (n^{-1/3}) for Brownian LPP (with the stated near-critical qualifications). It is a (1+1)-dimensional ground-state result, not needed for C0119. |
| Bates–Chatterjee, “The endpoint distribution of directed polymers”, arXiv:1612.03443v5; *Ann. Probab.* 48 (2020), 817–871 | Full-text introductory results checked: Theorem 1.1, p. 16, and Theorem 1.2, p. 17, concern endpoint atomic/geometric localization in arbitrary dimension. They do not supply the disorder-chaos reduction used here. |
| Bates–Chatterjee, “Localization in Gaussian disordered systems at low temperature”, arXiv:1906.05502v4; *Ann. Probab.* 48 (2020), 2755–2806 | Theorem 1.7, p. 10: Gaussian polymer mass is covered, up to small error, by overlap neighborhoods of finitely many paths, at differentiability points with (p'(\beta)<\beta). This concerns one environment. |
| Bates, “Full-path localization of directed polymers”, arXiv:1910.12012v4 | Theorem 1.3, p. 5: under the same derivative condition, localization holds within every interval of macroscopic length. This strengthens localization, not the two-environment chaos assertion. |
| Lacoin, “New bounds for the free energy of directed polymers in dimension 1+1 and 1+2”, arXiv:0901.0699 | Introductory theorem statements checked: free-energy/very-strong-disorder results in spatial dimensions 1 and 2. Not a higher-dimensional chaos theorem. |
| Junk–Lacoin, arXiv:2402.02562v3 | Theorem 2.2, p. 4: equality of strong and very-strong-disorder critical points and weak disorder at criticality for (d\ge3), under an upper-bounded environment hypothesis. Its Section 2.5 explicitly points to the subsequent removal of this restriction. |
| Junk–Lacoin, “Coincidence of critical points for directed polymers for general environments and random walks”, arXiv:2502.04113v2; *Orbita Mathematica* 3 (2026), 89–125 | Theorem 2.1 extends equality of critical points to environments with all exponential moments and reference walks with a positive power moment. This includes Gaussian nearest-neighbor polymers. It addresses a phase-transition question, not the missing variance bound: the latter was already available in 2013. |
| Ahlberg–Deijfen–Sfragara, “From stability to chaos in last-passage percolation”, arXiv:2302.11379v2; DOI 10.1112/blms.12941 | Introduction and main results checked: non-Gaussian point-to-point LPP with independently resampled weights, in general lattice dimension. A later extension of chaos theory, distinct from finite-temperature polymer OU chaos. |
| Ganguly–Ginsburg–Himwich, “Temperature chaos in directed polymers”, arXiv:2607.18194v1 (July 2026) | Abstract and Theorem 1.7 checked: continuum (1+1) polymer free-energy decoupling at widely separated inverse temperatures, under the same noise. This is temperature chaos in a different regime. |

The search covered the requested 2008–2026 interval up to 13 November 2026. It is not a claim to have read every citing paper. The positive closure rests on explicit full-text theorems and their proved implications, so an exhaustive negative search is unnecessary.

## 7. Verification, files, and stopping point

1. Read the original polymer definition, exact overlap criterion, OU identity, monotonicity, Theorem 8.1, and the actual wording of Section 12(2).
2. Checked Graham's free-endpoint theorem on both directed graphs, rather than substituting his point-to-point Theorem 1.3.
3. Checked the dimension translation and fixed-temperature hypotheses of Alexander–Zygouras; verified Gaussian nearly gamma admissibility directly and integrated the stated tail to recover (9).
4. Re-derived the OU-to-overlap relation from the Gibbs derivative and independently checked its time normalization by Hermite expansion. Checked monotonicity and the converse reduction, rather than extracting a fixed-time conclusion from the integral without justification.
5. Cross-checked both variance attributions against Chatterjee's later surface-growth paper, Section 2.4.
6. Source text provenance, retrieval times and SHA-256 hashes are recorded in [data/source_manifest.jsonl](data/source_manifest.jsonl). Extracted texts retain form feeds for page verification. [code/fetch_text.py](code/fetch_text.py) downloads PDFs only into process memory, pipes them to `pdftotext`, and saves only text. No PDFs, page images or scans were saved.

Following the requested stopping rule, no new open-problem attack or polymer simulation was undertaken after establishing the literature resolution. Arbitrary non-Gaussian environments, optimal quantitative chaos scales, and other endpoint geometries are not silently added to the solved statement.

Task: “Open problem C0119” — 2026-11-13, 06:35 Asia/Tbilisi (first recorded task clock).
