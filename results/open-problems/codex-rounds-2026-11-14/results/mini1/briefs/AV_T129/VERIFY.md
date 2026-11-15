# T129: singularity of random symmetric sign matrices

Verdict: **SOLVED-CLAIMED**, checked November 14, 2026. The October 3 manuscript claims the entire statement in our row. This note does not establish that its proof is correct.

## Recommended replacement for “where it stands”

OpenAI’s unrefereed preprint *The sharp exponential rate of singularity for symmetric Bernoulli matrices* (October 3, 2026) claims \(\mathbb P(A_n\text{ is singular})=(1/2+o(1))^n\) for exactly the symmetric sign model in this row. No independent proof verification, arXiv repost, or Lean formalization of this result was found in the sources checked through November 14, 2026, so record the sharp base as claimed rather than established. Its companion, *The sharp singularity rate for biased symmetric sign matrices* (October 4, 2026), treats fixed \(p\ne1/2\).

## 1. The biased-sign candidate

Author as printed: OpenAI. Title: *The sharp singularity rate for biased symmetric sign matrices*. Date as printed: October 4, 2026. The introduction defines \(A_n^{(p)}\) as a real symmetric \(n\times n\) matrix with independent entries on and above the diagonal, with probabilities \(p\) and \(1-p\) for \(+1\) and \(-1\); entries below the diagonal are determined by symmetry.

Opened [main source](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026/build/main.tex), [introduction and Theorem 1.1](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026/build/sections/01-introduction.tex), and [author/date record](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026/README.md). Exact theorem source:

```tex
\begin{theorem}\label{thm:main}
For every fixed $p\in(0,1)\setminus\{1/2\}$,
\[
 \lim_{n\to\infty}\Prob\bigl(\det A_n^{(p)}=0\bigr)^{1/n}
   =p^2+(1-p)^2.
\]
\end{theorem}
```

| Our wording | Candidate |
| --- | --- |
| Uniform symmetric sign matrix | Same symmetry and sign values, but biased signs. |
| Independent entries on **and above** the diagonal | Same independence locations, including the random diagonal. |
| Dimension \(n\times n\), \(n\to\infty\) | Same dimension and unrestricted limiting size. |
| Probability of being singular | Same event: \(\det A_n^{(p)}=0\). |
| Exponential base \(1/2\) | Base \(p^2+(1-p)^2\) for each fixed \(p\in(0,1)\setminus\{1/2\}\). |
| Equality \((1/2+o(1))^n\) | An nth-root limit is equivalent to \((p^2+(1-p)^2+o(1))^n\), not merely an unspecified exponential upper bound. |

This is a related extension, but does not itself cover the fair-sign case of T129. Substituting \(p=1/2\) is excluded by its explicit hypothesis; taking \(p\to1/2\) after a fixed-\(p\) limit supplies no uniform estimate that would fill the gap. It also asserts no result for a bias depending on \(n\). Its introduction cites the October 3 companion for the fair-sign theorem.

## 2. The fair-sign candidate

Author as printed: OpenAI. Title: *The sharp exponential rate of singularity for symmetric Bernoulli matrices*. Date as printed: October 3, 2026. The introduction defines \(A_n\) as a symmetric \(n\times n\) random matrix whose entries on and above the diagonal are independent and uniform on \(\{-1,1\}\).

Opened [main source](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-sharp-exponential-rate-of-singularity-for-symmetric-Bernoulli-matrices-October-3-2026/build/main.tex), [introduction and Theorem 1.1](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-sharp-exponential-rate-of-singularity-for-symmetric-Bernoulli-matrices-October-3-2026/build/sections/01-introduction.tex), and [author/date record](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-sharp-exponential-rate-of-singularity-for-symmetric-Bernoulli-matrices-October-3-2026/README.md). Exact theorem source:

```tex
\begin{theorem}\label{thm:main}
For the symmetric Bernoulli matrix \(A_n\),
\[
 \Pr(\det A_n=0)=\left(\frac12+o(1)\right)^n
                =2^{-n+o(n)}
 \qquad\text{as }n\to\infty.
\]
\end{theorem}
```

| Our wording | Candidate |
| --- | --- |
| “uniformly random symmetric” | Independent fair choices for the \(n(n+1)/2\) upper-triangular entries give the uniform distribution on all symmetric sign matrices. |
| “\(n\times n\) matrix” | Exactly \(n\times n\); no even-size, odd-size, or subsequence restriction. |
| “independent ±1 entries on and above the diagonal” | Same support, probabilities and independence, including the diagonal. “Bernoulli” here means signs, not \(0/1\) entries. |
| “\(A_n\) is singular” | Equivalent to \(\det A_n=0\), over the reals as in the source. |
| “\(=(1/2+o(1))^n\)” | Identical asymptotic, also written \(2^{-n+o(n)}\). |

The whole statement is claimed. The internal reduction to \(0/1\) matrices of size \(n-1\) does not change the theorem's sign model. This is the sharp exponential rate, rather than \(\exp(-cn)\) with unspecified \(c>0\); it does not claim a relative asymptotic with a specified polynomial prefactor, exact finite-size probabilities, least singular value tails, or repeated-eigenvalue bounds. Those other quantities are not required by our row.

## 3. The Fortuin–Kasteleyn candidate

Author as printed: OpenAI. Title: *Brownian continuum random tree limits of finite Fortuin–Kasteleyn maps above four*. Date as printed: September 24, 2026.

Opened [the preprint source, including the finite model and Theorem 1.1](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Brownian-continuum-random-tree-limits-of-finite-Fortuin-Kasteleyn-maps-above-four-September-24-2026/build/main.tex) and [author/date record](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Brownian-continuum-random-tree-limits-of-finite-Fortuin-Kasteleyn-maps-above-four-September-24-2026/README.md). Exact theorem source:

```tex
\begin{theorem}\label{thm:main}
For every fixed real $q>4$, there is a deterministic constant
$c(q)\in(0,\infty)$ such that, as $n\to\infty$ through all positive
integers,
\[
 \big(V(M_n),c(q)n^{-1/2}d_n,\mu_n\big)
 \ \Longrightarrow\ (\mathcal T_e,d_e,\mu_e)
\]
in the Gromov--Hausdorff--Prokhorov topology on compact metric probability
spaces modulo measure-preserving isometry.
\end{theorem}
```

Here \(M_n\) is a rooted planar map with \(n\) edges and an FK edge subset, sampled with weight \(q^{k_M(A)+(|A|-|V(M)|)/2}\); \(d_n\) is graph distance and \(\mu_n(\{v\})=\deg(v)/(2n)\). The limit is the Brownian continuum random tree coded by normalized Brownian excursion.

This is **NOT-THIS**: a planar-map metric-measure scaling limit with fixed real \(q>4\), not a random sign matrix. Size counts edges, the quantity is convergence in distribution in Gromov–Hausdorff–Prokhorov topology, and normalization is \(n^{-1/2}\). None of T129's matrix model, singularity probability, or exponential-base claim is covered. The notation \(A_n\) in this source denotes an edge subset.

## Follow-ups and verification evidence

These sources were actually opened; unavailable pages and search leads are distinguished below.

- [Repository README](https://github.com/openai/math/blob/main/README.md): describes the manuscripts as raw research data and acknowledges possible issues in unformalized results. This is the publisher's status description.
- [Repository history](https://github.com/openai/math/blob/main/history.md) and all three candidate README files: no correction, withdrawal, or replacement edition for these candidates was found. Read-only directory commit-history API requests for all three candidates each returned only initial commit adc7f1241b42e322a6451854ab7e4b4c146bf78a, October 6, 2026, 21:58:50 UTC. The theorem links above are pinned to that commit.
- [MathDB's target entry](https://mathdb.com/p/340387/the-optimal-singularity-probability-conjecture-for-random-sy): lists both manuscripts as OpenAI claims, each with zero endorsements in the opened record; the visible contributor name is Shaowu Zhang. This is a claim listing, not a referee report.
- [Columbia Student Probability Seminar, Fall 2026](https://www.math.columbia.edu/~jshen/26fall.html): Jiahe Shen's October 8 historical survey announcement discusses the recent symmetric sharp-rate claim and distinguishes it from established published results. No written proof audit or endorsement is supplied.
- [Plectis Atlas, family 239](https://wcook04.github.io/plectis-atlas/families/239.html): reproduces the two claims and reports no Lean statement or Comparator run for this family. The atlas says it runs no checks itself. Its only listed outside commentary is an unsigned, explicitly unverified tier list; that linked tier list was not opened.
- [Proofweave, family 239](https://proofweave.org/publications/openai-math/239): indexed October 13, 2026; gives no reviewed explanation artifact, identifies no formalization coverage, and marks replay pending. It supplies no independent proof audit.
- [Carlos Toledo, *OpenAI's math release: what it claims beyond what it checks*](https://carlostoledo.co/reports/openai-math.html): audits formal statements and finite witnesses elsewhere in the release. Searching its opened text for 239 found no match. No result-specific assessment of these singularity proofs was located there; its general findings do not verify or refute T129.
- [Huaijin Liang, Kexin Yu and Tingzhou Yu, *Exponential singularity and rank bounds for random symmetric matrices*, arXiv:2610.39424](https://arxiv.org/abs/2610.39424), submitted October 29, 2026: opened the abstract page and [full HTML](https://arxiv.org/html/2610.39424v1). Theorem 1.1 gives \(\mathbb P(\operatorname{rank}A\le n-k)\le2e^{-c_\beta nk}\) under a general largest-atom assumption, for all \(1\le k\le n\), with arbitrary diagonal distribution independent of the off-diagonal family. It is later related literature, already noted in our row, rather than an arXiv version or validation of OpenAI's theorem; it does not identify the base \(1/2\).

No arXiv version of either singularity manuscript, specific refutation, error report, published referee report, or independent verification of the full proof was found in this search. This concerns the sources checked, not proof that none exists.

### Lean folder and docs

Opened [lean/](https://github.com/openai/math/tree/main/lean), [Lean README](https://github.com/openai/math/blob/main/lean/README.md), [formalization.yaml](https://github.com/openai/math/blob/main/lean/formalization.yaml), [OAI.lean imports](https://github.com/openai/math/blob/main/lean/OAI.lean), and the [lean/docs](https://github.com/openai/math/tree/main/lean/docs) and [ComparatorChallenges](https://github.com/openai/math/tree/main/lean/ComparatorChallenges) listings. No document 239, singularity comparator, or corresponding matrix-singularity import was identified. A direct request for lean/docs/239.md returned 404; the only Bernoulli-named comparator listed is BernoulliNonflatInSeven, a different subject.

The third candidate has [scope documentation, lean/docs/211.md](https://github.com/openai/math/blob/main/lean/docs/211.md), explicitly naming its planar-map theorem. Opened [FKCRT.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/FKCRT.lean) and [FKCRT.json](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/FKCRT.json); the configuration names solution module OAI.Probability.FKMaps.Convergence and theorem OAI.FKCRT.finite_fk_maps_converge_to_brownian_crt. This concerns the unrelated map result and gives no formal evidence for T129. No Lean build was run. Absence from formalization.yaml alone would be insufficient: it also lacks the explicitly documented FKCRT name.

### Search and retrieval record

Used the web search tool with each exact candidate title; both singularity titles plus site:arxiv.org; and combinations of OpenAI, symmetric Bernoulli, singularity, 239, error, gap, refutation, expert proof, and Sahasrabudhe. Also searched the planar-map title with arxiv/error. Repository issue search for repo:openai/math singularity returned no issues; this is weak negative evidence because issue availability can limit a search.

The supplied GitHub folder URLs initially failed in the web tool with “Cache miss”; the read-only GitHub connector successfully opened their listings and TeX sources. No theorem was inferred from a title or abstract alone. A root docs/ request returned 404; documentation is under lean/docs/. The [lowrank latent-seminar exposition](https://lowrank.github.io/latent-seminar/OpenAI-Math/239-symmetric-singularity) appeared in search, but direct open failed; its full content is not relied upon here. Other unopened search hits are not evidence in this report.

Saved TeX, notices, catalogue and relevant Lean files are under [sources/](sources/). The source links identify the files supplying the exact quotations.

## Spot check

Selected the October 3 paper's Lemma 11.2, “Cost of heavy retained layers” (source label lem:heavy-retention-cost), the conditional probability input used to exclude large high-layer tails in Proposition 2.7, “Potential moment”. That moment, together with Proposition 2.6, gives the expected admissible-column bound needed for the sharp singularity rate. This check covers the lemma and its retention-lattice input, not the entire potential-moment argument.

Sources read in detail: [Section 11](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-sharp-exponential-rate-of-singularity-for-symmetric-Bernoulli-matrices-October-3-2026/build/sections/11-minor-paths.tex) and [Section 7](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-sharp-exponential-rate-of-singularity-for-symmetric-Bernoulli-matrices-October-3-2026/build/sections/07-minor-moves.tex).

The lemma fixes a nonsingular bit matrix \(C\), a quotient \(\pi:\mathbb Z^m\twoheadrightarrow H\) with \(C\mathbb Z^m\subseteq\ker\pi\), and conditionally uniform \(v\in\{0,1\}^m\). Put \(\nu_p=(\log_Np)/N\), \(R=\lceil(\log\log N)^2\rceil\), and let \(Q\) sum \(k_H(p,e)\nu_p\) over retained layers of height at least \(R-1\). For fixed \(0<\eta<1\), \(q_0=\eta/(100\log N)\), it asserts
\[
 \mathbb P(Q\in[q,2q)\mid\mathcal F)\le2^{-3qN/5},
 \qquad q_0\le q\le1/2,
\]
for all sufficiently large \(N\).

The retention-lattice implication can be checked directly. Write \(H_p=\bigoplus_i\mathbb Z/p^{b_i}\mathbb Z\), and let \(r_i\) be the capped valuation of coordinate \(i\) of \(\pi(v)\). Modulo \(p^t\), its order exponent is \(u_t=\max_i(\min(b_i,t)-r_i)_+\). The number of retained layers among the first \(b_i\) is \(b_i-u_{b_i}\le r_i\). If \(a_i\) selected layers reach cyclic factor \(i\), then \(a_i\le r_i\), forcing divisibility by \(p^{a_i}\). The subgroup so obtained has index \(\prod_{(p,e)\in E}p^{k_H(p,e)}=N^{Nq(E)}\). Its preimage \(K_E\) contains \(C\mathbb Z^m\).

For a fixed mask, let \(j\) coordinate images in \(\mathbb Z^m/K_E\) be a maximal family with distinct subset sums. Conditioning on the other bits leaves at most one assignment to those \(j\) bits for membership in \(K_E\), so probability is at most \(2^{-j}\). Maximality expresses each coordinate image in that family with coefficients in \(\{-1,0,1\}\); the selected columns form an identity block, so the coefficient matrix \(M\) has rank \(j\). Nonsingularity of \(C\) implies \(MC\) also has rank \(j\). Its columns lie in the kernel of the surjection from \(\mathbb Z^j\) onto \(\mathbb Z^m/K_E\), and each entry has absolute value at most \(m\le N\). Choosing \(j\) independent columns and applying Hadamard gives
\[
 N^{Nq(E)}\le(N\sqrt j)^j\le N^{3j/2}.
\]
Thus \(j\ge2q(E)N/3\), giving the fixed-mask bound \(2^{-2q(E)N/3}\). The index inequality has the needed direction: the lattice generated by those independent columns is contained in the kernel lattice. The trivial-group case \(j=0\) is harmless.

The union-bound entropy also fits. For \(p\le\sqrt N\), distinct plateau heights give \(d_p^2\le2\sum_e k_H(p,e)\). Since \(|H|\le|\det C|\le N^{N/2}\), Cauchy–Schwarz bounds their total plateau count by \(O(N^{3/4}\sqrt{\log N})\). Encoding all retained prefixes costs \(O(N^{3/4}(\log N)^{3/2})=o(N/\log N)\), hence \(o_\eta(qN)\) uniformly for \(q\ge q_0\). For \(p>\sqrt N\), each eligible layer weighs at least \(R/(3N)\), so there are at most \(3N/(2R)\) eligible layers and a mask with \(Q<2q\) selects at most \(6qN/R\). Its entropy is
\[
 O\!\left(\frac{qN}{R}(1+\log(1/q))\right)=o_\eta(qN),
\]
because \(1+\log(1/q)=O_\eta(\log\log N)\) and \(R\asymp(\log\log N)^2\). Combining entropy with the fixed-mask cost yields \(2^{-(2/3-o_\eta(1))qN}\le2^{-3qN/5}\). The coefficient margin is \(2/3-3/5=1/15\). Here \(Q\) measures normalized logarithmic index, while \(qN\) is the probability exponent.

No error was found in this lemma's argument or its retention-lattice dependency. Conditional uniformity of the tested column is essential; the statement does not permit arbitrary conditioning on its future outcome. The cube-concentration theorem, certificate-pricing argument and full potential-moment proof remain unaudited, so this spot check does not change the claim-only verdict.

Task: “Verify: has open problem T129 been settled by the OpenAI math release?” — received November 14, 2026, approximately 21:07 Asia/Tbilisi.

