> Inherited round-5 verification record. Its historical opens belong to earlier sessions; the round-6 continuation is appended below.

> Inherited verification record from round 4, read in this session. Historical source opens are attributed to those sessions; the round-5 audit and fresh openings are appended below.

# T137: the Parisi formula for diluted spin glasses

Original verification checked on 14 November 2026. This inherited record is retained with its source files; the 15 November continuation and new source audit are appended below. **The three supplied candidates give a partial claim for our whole row.** The matching OpenAI preprint claims the pressure formula for Viana–Bray and all diluted even-K spin models at every positive temperature, and for even-K SAT. It expressly excludes odd-K SAT. A separate later paper by Dmitry Panchenko claims all of the row, including odd-K SAT; this is a distinct proof claim, not a confirmation that OpenAI's proof is correct.

## 1. The matching preprint

OpenAI, *The Mézard–Parisi formula for diluted spin glasses*, September 23, 2026. Opened its [actual main TeX file](https://github.com/openai/math/blob/main/preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/main.tex), [model and main theorem](https://github.com/openai/math/blob/main/preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/model.tex), [named-model corollaries](https://github.com/openai/math/blob/main/preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/consequences.tex), introduction, proof overview and selected proof sections. Local copies are under [sources/](sources/).

The main result is Theorem 2.1. The following is copied exactly from the TeX source, including its labels and references:

```tex
\begin{theorem}\label{main:theorem}
Under \eqref{model:integrability}--\eqref{model:positivity}, the thermodynamic
limit exists and
\begin{equation}\label{main:formula}
 \lim_{N\to\infty}F_N=\inf_{r\ge0}\Phi_r.
\end{equation}
\end{theorem}
```

The referenced hypotheses fix **even** p >= 2 and density alpha > 0. They require E max_s |theta(s)| + E|h| < infinity and a factorization
e^{theta(s)} = a(1+b product_l f_l(s_l)),
with a > 0, independent identically distributed f_l, b independent of all f_l, |b product_l f_l(s_l)| < 1 for every tuple, and finite nonnegative E[(-b)^n] for every n >= 1. The Hamiltonian has Pois(alpha N) independent clauses and independent uniform site indices **with replacement**, plus independent fields. F_N is exactly N^{-1} E log Z_N with counting measure on the spins.

Here Phi_r is the infimum of B_r over the trial law and exponents 0 < m_1 < ... < m_r < 1, with r = 0 allowed. The source defines
B_r = log 2 + E log T_0 V_s - alpha(p-1) E log T_0 V_e;
T_0 is the successive conditional power-mean recursion, V_s the one-site cavity insertion, and V_e the one-clause correction. Thus the displayed conclusion is the proposed hierarchical cavity variational equality, not just existence of a pressure limit.

The two named-model corollaries remove any uncertainty about the coupling laws and temperature range. Their statements are also exact source quotations:

```tex
\begin{corollary}[Viana--Bray and diluted even-spin models]
\label[corollary]{models:spin}
Fix an even integer $p\ge2$, $\alpha>0$, and independent real random
variables $J,H$ such that $J$ has a symmetric distribution and
$\E|J|+\E|H|<\infty$. For every $\beta>0$, the model with
\[
 \theta_\beta(s_1,\ldots,s_p)=\beta J\prod_{\ell=1}^p s_\ell,
 \qquad h_\beta=\beta H
\]
satisfies the variational formula \eqref{main:formula}, with the trial
functional evaluated at these interaction and field laws. In particular,
this holds for the Viana--Bray model~\cite{VB85}, which is the case $p=2$.
\end{corollary}
```

```tex
\begin{corollary}[Soft random even-$K$ SAT]
\label[corollary]{models:sat}
Fix an even integer $K\ge2$ and $\alpha>0$. Let
$\varepsilon_1,\ldots,\varepsilon_K$ be independent fair signs and let
$W\ge0$ be independent of the signs, with $\E W<\infty$. For every
$\beta>0$, the interaction
\[
 \theta_\beta(s_1,\ldots,s_K)
 =-\beta W\prod_{\ell=1}^K\frac{1+\varepsilon_\ell s_\ell}{2},
 \qquad h=0,
\]
satisfies \eqref{main:formula}. The choice $W=1$ is the soft random
even-$K$ SAT model; $W$ gives an independent nonnegative clause weight.
\end{corollary}
```

### Comparison with each part of our statement

| Wording in our row | What the preprint actually claims | Coverage |
| --- | --- | --- |
| N Ising spins | Spins in {-1,1}^N, N tending to infinity; no spatial dimension assumption | Same spin space and limit |
| Each unordered pair independently present with probability c/N | Poisson number alpha N of ordered, independently sampled two-site clauses, with replacement | Different finite-N convention; same limiting pressure at alpha = c/2 by the elementary comparison below |
| Symmetric signs or standard Gaussian couplings | Every symmetric J with E|J| < infinity, and independent integrable field H | Both requested laws included, with H = 0 |
| Every beta > 0 | Every beta > 0, every alpha > 0, with theta_beta = beta J product s_l | Entire requested temperature and fixed-density range |
| lim N^{-1} E log Z_N equals the Mézard–Parisi formula | Exact equality with inf_{r >= 0} Phi_r, including log 2 in the counting-measure normalization | Equality, not merely an upper bound |
| Full replica symmetry breaking where needed | No fixed finite number of hierarchy levels and no finite-support assumption on the overlap law | Covers the pressure formula with unrestricted finite-depth infimum; does not identify phases, prove which depth is needed, prove attainment, or construct an infinite-depth Gibbs state |
| Diluted K-spin, K even | Explicit corollary for every even p >= 2 | Included |
| Random K-SAT at positive temperature, with no parity restriction | Explicit corollary only for even K >= 2, soft clauses of weight W = 1 | Odd K, including 3-SAT, is not covered |

**Finite-N convention, not a hidden restriction.** For p = 2, Poisson thinning at alpha = c/2 gives independent Pois(c/N) multiplicities on unordered pairs; loops have mean c/2 in total. Coupling each multiplicity to a Bernoulli(c/N) edge needs an expected O(c^2) edge insertions/deletions in total, and deleting the loops costs O(c) terms. A single bond changes log Z by at most beta|J|, so the expected pressures differ by O(beta E|J|(c+c^2)/N), tending to zero at each fixed c and beta. This is an elementary model comparison made here, not a theorem quoted from the preprint; both requested laws have the needed first moment. The factor of two matters: alpha counts clauses per spin, while c is mean degree. At c = 0 the pressure is log 2 directly.

**What “full RSB” means for this comparison.** The row asks for the pressure value. An infimum over every finite hierarchy depth permits arbitrarily many levels and does not impose finite RSB. The manuscript itself explicitly says that its theorem does not assume attainment or construct a limiting infinite-depth Gibbs state. If the row also intended a theorem describing the actual Gibbs-state hierarchy, that additional assertion is not claimed here.

The final remark of the SAT section explicitly excludes random 3-SAT and points to a companion with a different trial functional and sign-indexed message pairs that need not be probabilities. A formula of that different kind is not the missing Mézard–Parisi equality for odd-K SAT.

## 2. Orthogonally invariant Ising models

OpenAI, *All-temperature pressure for orthogonally invariant Ising spin glasses*, September 25, 2026. Opened the [actual principal TeX source](https://github.com/openai/math/blob/main/preprints/All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026/build/invariant-sk.tex). Its Theorem 1.1 is exactly:

```tex
\begin{theorem}[Limiting pressure]\label{thm:main}
Let $\Lambda_N$ be deterministic real diagonal matrices whose empirical
spectral measures converge weakly to a compactly supported probability
law $\mu$. Assume that their smallest and largest eigenvalues converge
to the respective edges of $\supp\mu$. Let $U_N$ be Haar distributed
on $O(N)$, and define $P_N$ using the uniform spin probability in
Equation~\eqref{eq:pressure}. With $S$ and $G_1$ as in
Equations~\eqref{eq:S}--\eqref{eq:G},
\begin{equation}
 \lim_{N\to\infty}\E P_N
 =\lim_{N\to\infty}P_N
 =\mathcal F(\mu)
 :=\inf_{p\in\cP}\{S(p)+G_1(p)\},
 \label{eq:variational}
\end{equation}
where the second limit holds almost surely. No independence of the
matrices $U_N$ across dimensions is required.
\end{theorem}
```

The model is P_N = N^{-1} log[2^{-N} sum_sigma exp{sigma^T U_N^T Lambda_N U_N sigma/2}], with deterministic spectral data and Haar-distributed eigenvectors. S and G_1 are the paper's spectral/overlap variational functionals. Its normalization differs from ours by log 2, but the decisive difference is the disorder law: a sparse independent-edge Viana–Bray interaction matrix is not Haar orthogonally invariant with those spectral hypotheses. Diagonalizing a sparse matrix does not make its eigenvectors Haar. The theorem gives an all-temperature pressure equality for another model, not for sparse K-spin hyperedges or SAT clauses. **Candidate verdict: NOT-THIS.**

## 3. Tensor saturation

OpenAI, *Tensor saturation for even spin groups*, September 24, 2026. Opened [main.tex](https://github.com/openai/math/blob/main/preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/build/main.tex) and the [actual introduction and main theorem](https://github.com/openai/math/blob/main/preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/build/sections/01-introduction.tex). Theorem 1.1 is exactly:

```tex
\begin{theorem}[Type-$D$ saturation]\label{thm:main}
Let $G=\Spin(2n)$, $n\ge2$, and let $\lambda,\mu,\nu$ be dominant
integral weights such that $\lambda+\mu+\nu\in Q(D_n)$. Then, for every
positive integer $N$,
\[
 \bigl(V(\lambda)\otimes V(\mu)\otimes V(\nu)\bigr)^G\ne0
 \quad\Longleftrightarrow\quad
 \bigl(V(N\lambda)\otimes V(N\mu)\otimes V(N\nu)\bigr)^G\ne0.
\]
\end{theorem}
```

These are complex Lie-group representations and tensor invariants, not Ising spins or disordered Hamiltonians. The n >= 2 is the rank parameter of Spin(2n), and N is an integer dilation of highest weights; neither is the thermodynamic size in T137. There is no inverse temperature, partition function, random coupling, or Mézard–Parisi functional. **Candidate verdict: NOT-THIS.**

## 4. Later work and verification status

**A later proof claim covering the full row.** Opened Dmitry Panchenko, [*The Mézard-Parisi formula*, arXiv:2610.39545](https://arxiv.org/abs/2610.39545), submitted October 29, 2026, and its [full HTML text](https://arxiv.org/html/2610.39545v1), especially Section 2 and Theorem 2.1. It states equality for diluted even-K spin glasses with K >= 2 and standard Gaussian or symmetric-sign J, and random K-sat for every K >= 2. Its model uses Poisson clauses and independent site indices with replacement. The new structural claim removes the finite-support overlap assumption. This is a different manuscript, with Dmitry Panchenko as its sole listed author, not an arXiv version of the OpenAI paper.

Panchenko's AI acknowledgement credits ChatGPT Astra with finding his proof, says that he checked and rewrote it, and describes the subsequently released OpenAI proof as apparently following a different approach. That is a named expert's statement about his own proof and the relation of the two approaches; it does not certify OpenAI's argument. The opened arXiv page lists v1 only and no journal reference. No referee report or journal acceptance was found in the searches.

**Companion details.** Opened Dmitry Panchenko, [*Ghirlanda–Guerra identities and cavity equations for diluted spin glass models*, arXiv:2610.39542](https://arxiv.org/abs/2610.39542), October 29, 2026, and its [HTML text](https://arxiv.org/html/2610.39542v1). It supplies the cavity lower-bound inputs for his main paper, including simultaneous identities and cavity equations under negligible perturbations. This companion is not an independent review of the OpenAI preprint.

**Repository corrections and errors.** Opened [history.md](https://github.com/openai/math/blob/main/history.md), all three preprint READMEs, and the [all-state issues API](https://api.github.com/repos/openai/math/issues?state=all&per_page=100). The history and candidate READMEs contain no correction or withdrawal for these three papers; the issue collection returned four pull requests and no candidate-specific error report. Searches for the titles together with error, refutation, review and arXiv found no specific refutation or referee report. This records what was found, not an assertion that none exists.

**Lean artifacts.** Opened the [Lean README](https://github.com/openai/math/blob/main/lean/README.md), [formalization catalogue](https://github.com/openai/math/blob/main/lean/formalization.yaml), [family 221 scope note](https://github.com/openai/math/blob/main/lean/docs/221.md), [DilutedSpin comparator statement](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/DilutedSpin.lean), [checking configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/DilutedSpin.json), and [solution entry point](https://github.com/openai/math/blob/main/lean/OAI/Probability/DilutedSpin/Main.lean). The comparator encodes the even-arity, factorization, independence, integrability and positivity hypotheses and the same pressure convergence. Its `sorry` marks the challenge to be supplied by the separate solution; the solution entry point contains a proof using imported upper- and lower-bound results. The checking configuration permits only the standard axioms propext, Quot.sound and Classical.choice, and disables nanoda. These are supplied formalization artifacts, not a successful build or an independent semantic audit performed here.

Also opened [family 234's scope note](https://github.com/openai/math/blob/main/lean/docs/234.md), its [comparator configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/InvariantIsing.json), and [solution entry point](https://github.com/openai/math/blob/main/lean/OAI/Probability/InvariantIsing/Unconditional.lean). They concern the Haar-invariant model, including temperature, field and ground-state extensions, so they do not expand coverage of T137. No family-204 scope note was present at `lean/docs/204.md` (404); the opened docs directory also lacks it. No corresponding tensor-saturation formalization was found. The YAML retrieved during this check did not list either candidate's title or module, despite the existing 221/234 docs/configurations; the specific artifacts are the stronger evidence that they are supplied. No Lean compilation was attempted under the task's resource constraints.

**Expositions opened.** [AI Proved What?, “Many states, one exact formula?”](https://aiprovedwhat.com/episodes/221-mezard-parisi-diluted-spin-glasses/) explains the even-arity scope and proof strategy; its October 19 status says it did not build the Lean proof and found no expert reaction at that time. It is an exposition, not a referee report. Opened the [community tensor-saturation page](https://mathcommunity.github.io/oai-math-revised/papers/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/): its notes section has no substantive review and its automatically collected literature notes are explicitly unreviewed. These pages are used only as records of their own status/comments; mathematical coverage above is taken from the actual manuscripts.

**A later recorded Comparator check.** The [community diluted-paper page](https://mathcommunity.github.io/oai-math-revised/papers/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/), updated November 9, links an accepted run dated October 26. Opened the [actual DilutedSpin run log](https://github.com/mathcommunity/oai-math-revised/blob/main/checks/comparator-2026-10-26/logs/DilutedSpin.log), which records successful challenge and solution builds, followed by “Lean default kernel accepts the solution” and “Your solution is okay!”. The [maintainers' checking note](https://github.com/mathcommunity/oai-math-revised/blob/main/docs/LEAN_CHECKS.md) says the run used pinned dependencies and standard permitted axioms, with solution modules precompiled in the same workspace, a deviation from the strictest adversarial-check setting. It explicitly distinguishes acceptance of the formal statement from verifying that the formal definitions and statement express the paper's mathematical claim. This is useful recorded formal-check evidence, not a referee report or a proof-correctness verdict here.

Opened the [run-results table](https://github.com/mathcommunity/oai-math-revised/blob/main/checks/comparator-2026-10-26/results.tsv) as well: both DilutedSpin and InvariantIsing are marked accepted. Saved the diluted run log, checking note and those two table rows under sources/. The invariant entry's acceptance also concerns its own model, not T137.

Also opened the [Latent Seminar exposition of family 234](https://lowrank.github.io/latent-seminar/OpenAI-Math/234-invariant-spin-glasses); it disclaims complete proof verification and any Lean build or semantic equivalence check. A separate slatinwine.github.io exposition returned a cache miss and supplied no inspected content.

## Recommended replacement for “where it stands”

OpenAI's preprint *The Mézard–Parisi formula for diluted spin glasses* (September 23, 2026) claims the formula at every positive temperature for Viana–Bray, diluted even-K spin glasses and even-K random SAT, with an infimum over all finite hierarchy depths; it does not cover odd-K SAT. Dmitry Panchenko's later preprint *The Mézard-Parisi formula* (October 29, 2026, arXiv:2610.39545) separately claims the full formula, including random K-SAT for every K >= 2. The full row therefore has a proof claim, but the three OpenAI candidates alone cover only part of it, and this check does not establish correctness or peer review.

## Search and opening record

Successful manuscript openings were made through the read-only GitHub connector at the source links above; the web tool's initial attempts at the three GitHub folders returned cache misses. Guessed `build/paper.tex` URLs returned 404; directory listings located the actual source paths. No theorem has been reconstructed from a title or search snippet.

Web searches used the candidate titles and variants with OpenAI, 2026, arXiv, error, review, and proof, plus arXiv:2610.39545. The dated, incremental record of commands, failures and findings is [LOG.md](LOG.md). Only actually opened manuscripts are cited as papers; search-only leads to older literature are not being used as new citations.

## Spot check

Selected the lemma **Charging fresh splits**, source label `tree:charging`, in [the actual trees section](https://github.com/openai/math/blob/main/preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/trees.tex), together with its canceled-anchor extension rule and telescoping identity. This is a load-bearing coefficient estimate: the decorrelation induction divides by a reference coefficient with a small factor for every delayed branch, and would fail if absolute errors were amplified by inverse powers of the depth.

The lemma states that, starting from q old leaves and adding k colors, if b specified target branching vertices have depths absent from all old branching vertices, then the sum of absolute coefficients of allowed histories is at most C_{q,k} delta^b, with delta = 1/L. For the product J of their reference factors, it also gives a bound on that sum divided by |J| when m_d >= eta > 0 at those vertices.

The check uses the displayed extension rule, not an assumption of cancellation:

1. At a vertex of depth d with n children, a fresh path has coefficient m_d - n m_{d+1}, which is negative. Summing its absolute value over all internal vertices telescopes to the current number s of leaves: every non-root internal vertex's incoming m_d cancels its negative contribution, the root contributes no incoming term because m_0 = 0, and each terminal leaf contributes m_L = 1. There are at most s reusable old leaves, each of coefficient 1, so an unrestricted step has absolute mass at most 2s <= 2(q+k).
2. A previously unary vertex has coefficient m_d - m_{d+1} = -delta. At any fixed depth there are at most s vertices. Thus requiring a step to create a branch at a prescribed depth has absolute mass at most s delta <= (q+k)delta.
3. Each designated target branch must first have become branching during an added fresh path, since its depth was not an old branching depth. One fresh path creates exactly one branching vertex and then continues through new unary vertices. Thus distinct designated vertices have distinct creation steps, even if they have the same depth in different branches. There are at most k!/(k-b)! assignments of vertices to steps. Enlarging each class by discarding all other constraints and summing sequentially gives exactly the proof's bound
   [k!/(k-b)!] (q+k)^b [2(q+k)]^{k-b} delta^b.
4. For a target vertex of arity a_v, its first reference factor has magnitude delta. Its remaining factors satisfy |m_d - j m_{d+1}| = (j-1)m_d + j delta >= eta for j >= 2. Therefore |J| >= delta^b eta^{sum_v(a_v-2)}. The power of delta cancels in the ratio. Repeated depths in different branches do not remove any of these factors.

A small independent check gives the same scaling. With one old anchor and two fresh colors making a three-leaf star at depth d, the two coefficients are -delta and -(m_d+2delta), so their product is delta(m_d+2delta): one small factor for the one branching vertex. If instead they form a nested binary tree at depths d < e, both creation vertices are unary when split and the coefficient product is delta^2, one factor for each of the two vertices.

No gap was found in this coefficient lemma under its stated hypotheses. This checks only the combinatorial estimate and its normalization, not the score-concentration selection, the prescribed-tree identities, the full multioverlap induction, or the independent-message comparison. It gives no verdict on the complete proof.

## Continuation: 15 November 2026

The short update search did not change the literature verdict. Independently reopened Dmitry Panchenko's [arXiv record](https://arxiv.org/abs/2610.39545) and [full paper](https://arxiv.org/html/2610.39545v1), including the models and Theorem 2.1, and his [companion abstract](https://arxiv.org/abs/2610.39542). The full-row preprint claim was already known in both previous sessions; it is not a newly discovered solution in this continuation. Searches for the identifier with correction, erratum and refutation returned no results. No new referee report, correction, or independent proof assessment was located in this limited search.

The round-3 Poisson/Bernoulli comparison was independently re-derived. With p=c/N, each unordered pair has Pois(p) multiplicity and the optimal expected edit count against Bernoulli(p) is 2[p-1+exp(-p)]. Multiplying by beta E|J| binom(N,2)/N, and using p-1+exp(-p)<=p^2/2, recovers exactly beta E|J| c^2(N-1)/(2N^2). Centered loops contribute zero to the expected log partition function. The earlier bound holds.

### New result: definition-level Lean comparison

Opened the actual solution's [Model.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/DilutedSpin/Model.lean), [Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/DilutedSpin/Main.lean), [ExactVariationalLower.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/DilutedSpin/ExactVariationalLower.lean) and [ProxyRateIncrement.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/DilutedSpin/ProxyRateIncrement.lean), and reopened the actual [model and main theorem source](https://github.com/openai/math/blob/main/preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/model.tex) and [challenge statement](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/DilutedSpin.lean). Also inspected `MeasureHierarchy.lean`, `HierarchyBasic.lean`, and `UpperTrial.lean` from that solution directory. The seven directly relevant source files are saved locally; `sources/current-fetch-manifest.json` records directory-reported blob identifiers for the saved solution files.

The challenge and actual solution share identical definitions, from `Spin` through `variationalValue`, including the two Borel-space instances. All 21 named type/model/function declarations in this block agree; so do the challenge and solution theorem headers. The source-level comparison is reproducible with `OMP_NUM_THREADS=1 nice -n 15 python3 audit_definitions.py`. Its normalized block hash is `14579345f6e6c35dc1e49b286bff8996edf34273b2101a595a4691c63cac868a`. A separate raw comparison, retaining comments and whitespace inside the block, agrees as well (6371 bytes, excluding the challenge theorem's comment and stub).

| Part of the manuscript | Actual solution definition | Finding |
| --- | --- | --- |
| Even p>=2, alpha>0, first moments, factorization, iid f_l, b independent, finite nonnegative moments | `Model`, `Admissible` | Same explicit hypotheses; no bounded-J or finite-RSB hypothesis added |
| Counting-measure, unperturbed F_N with Pois(alpha N) clauses and independent uniform indices | `logWeight`, `logPartition`, `pressure` | Same finite-N expectation for N>=1; averaging denominator is N^(kp), so repetitions remain allowed |
| q_x, C_theta, U_theta, log V_s | `q`, `edge`, `appendSpin`, `message`, `siteLog` | Same messages and final-spin insertion; site average includes 1/2 |
| Weak-topology nested probability measures and independent message labels | `Hierarchy`, `trialLog` | Same trial space and independent product laws; no finite-support or message-moment condition |
| Conditional power means with increasing m_1,...,m_r | `logMean`, `Exponents` | Same recursion by induction; checked r=0,1,2 explicitly; physical disorder is fixed during recursion |
| B_r and unrestricted inf_r Phi_r | `functional`, `phi`, `variationalValue` | Same site rate alpha p, correction alpha(p-1), additive log 2 and all natural hierarchy depths |
| Thermodynamic equality | `mezard_parisi` | Convergence of this pressure to this variational value; the entry point combines imported lower and upper bounds |

[The round-4 PROOF.md](~/codex_op_1114r4/briefs/AV_T137/PROOF.md) gives the identification in detail, including first-moment bounds ensuring ordinary integrals, nonempty bounded-below real infima, and explicit factorization witnesses for both requested coupling laws and even-K SAT. A direct constant-clause example separately checks the normalization and density factors. No semantic mismatch was found in these definitions. This narrows the earlier unchecked semantic question, but it does not certify the whole proof: Lean was not built, the entire import closure and library instance elaboration were not audited, and the full-RSB lower-bound argument was not verified.

The recommended three-sentence replacement above remains unchanged: the supplied OpenAI candidates give only an even-arity claim, while Panchenko's separate preprint claims the full row. The source audit does not remove the odd-K restriction or turn a recorded formal-check result into an independent correctness judgment.

## Round 5: lower-bound reduction audit, 15 November 2026

The five-minute literature update found no new result beyond Panchenko's already recorded full-row preprint claim, and no specific correction or refutation in the returned results. Reopened his [arXiv record](https://arxiv.org/abs/2610.39545) and [full text](https://arxiv.org/html/2610.39545v1). No proof correctness or peer-review finding is added. The earlier three-sentence recommended replacement remains applicable.

Freshly opened all three candidates' actual main-theorem sources with the read-only GitHub connector: the diluted [model section](https://github.com/openai/math/blob/main/preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/model.tex), the invariant [principal source](https://github.com/openai/math/blob/main/preprints/All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026/build/invariant-sk.tex), and the tensor [introduction](https://github.com/openai/math/blob/main/preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/build/sections/01-introduction.tex). Their exact theorem quotations above match these fresh source texts. New copies are saved with `-current.tex` names; the inherited source records are retained separately. The coverage verdict is unchanged.

Independently rechecked the preceding round's source identity with a separate token-stream method: all 1,007 non-comment definition tokens match, and the theorem headers agree. This is a textual recheck of its reported main finding, not another complete semantic audit.

### Spot check: the lower-bound chain

The single extension is the reduction from the bounded symmetric model to the integrable admissible model, starting at [ExactVariationalLower.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/DilutedSpin/ExactVariationalLower.lean) and following [SymmetricTrialLower.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/DilutedSpin/SymmetricTrialLower.lean). [The round-5 PROOF.md](~/codex_op_1114r5/briefs/AV_T137/PROOF.md) writes out the mathematics, with the bounded-model inputs explicitly assumed. No gap was found in this reduction.

- Subtracting theta(all-plus) removes the potentially asymmetric multiplier a. Joint independence of b from the iid f vector then yields a permutation-invariant centered law; no expectation of log a is needed.
- Pressure and every trial functional shift by exactly -alpha E theta(all-plus). The two shifts cancel in the lower bound.
- The pressure stability error is alpha D+d, and the functional stability error is alpha(2p-1)D+d, uniformly in hierarchy depth and trial law. Clipping therefore costs 2 alpha p D_K+2d_K in the lower-bound comparison. Explicitly, D_K=E(||theta||_infinity-K)_+ and d_K=E(|h|-K)_+; first moments suffice.
- BoundedCavityLower chooses depth before size, with three errors below epsilon/4, giving one finite trial below liminf pressure+3 epsilon/4. The displayed combination introduces no finite-RSB hypothesis and does not interchange the size and depth limits.

The saved proof separates this elementary reduction from its three substantive bounded-model inputs: the common perturbation selector, the independent-message cavity comparison, and the increment-to-proxy estimate. Their full proofs and import closures are not certified. In particular, FullShapeControl is supplied by an imported selector; merely seeing it in an intermediate lemma would not establish that selector's correctness.

The exact remaining comparison route is `CavityProxy.cavityProxy_comparison_tendsto` -> `UpperInsertion.poissonInsertionOn_comparison_tendsto_ae` -> `UpperInsertion.randomInsertionOn_comparison_tendsto_ae` -> `AveragedEnergyRoot.randomInsertionOn_comparison_tendsto` -> `RandomInsertion.randomInsertion_comparison_tendsto`. Here filenames identify the modules; the declarations are in the DilutedSpinGlass.UniversalDictionary namespace. The last displayed proof invokes `reservoirInsertion_comparison`, `reservoirShapeError_tendsto`, and a logarithm-series tail bound. Auditing that independent-message step is the next task; it was not completed by this reduction check.

Round-5 source openings, their URLs, reported modification dates and local SHA256 hashes are recorded in [its source_manifest.json](~/codex_op_1114r5/briefs/AV_T137/source_manifest.json). `audit_lower_chain.py` rechecks the earlier identity, all three exact main theorems, and the declaration locations; its output is [the round-5 audit_output.txt](~/codex_op_1114r5/briefs/AV_T137/audit_output.txt). This script neither parses nor builds Lean. All shell work was tiny and single-threaded; actual observed process nice priority was 20, despite the sandbox warning on an additional nice request. No computation approaching the memory or runtime limits was run.

## Round 6: bounded-insertion comparison, 15 November 2026

The short literature update reopened Dmitry Panchenko's [main arXiv record](https://arxiv.org/abs/2610.39545), [full paper](https://arxiv.org/html/2610.39545v1) and [companion record](https://arxiv.org/abs/2610.39542). The known October 29 full-row claim remains the relevant later work; no new correction, refutation or independent resolution appeared in the limited searches recorded in [LOG.md](LOG.md). This is not a new proof-correctness assessment.

Freshly reopened all three candidate theorem sources through the read-only GitHub connector: the [diluted model section](https://github.com/openai/math/blob/main/preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/model.tex), [orthogonally invariant principal source](https://github.com/openai/math/blob/main/preprints/All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026/build/invariant-sk.tex), and [tensor introduction](https://github.com/openai/math/blob/main/preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/build/sections/01-introduction.tex). Their exact main theorem statements above are unchanged. Local fresh copies are `sources/diluted-r6.tex`, `sources/invariant-r6.tex`, `sources/tensor-r6.tex`; the comparisons and hashes are reproducible with [audit_insertion.py](audit_insertion.py).

### Spot check

The single new audit follows `randomInsertion_comparison_tendsto` from [RandomInsertion.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/DilutedSpin/RandomInsertion.lean) to the actual finite bound in [RootLogComparison.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/DilutedSpin/RootLogComparison.lean), its [finite logarithmic expansion](https://github.com/openai/math/blob/main/lean/OAI/Probability/DilutedSpin/FiniteLogExpansion.lean), and the shape-limit route through [ReservoirShapeLimit.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/DilutedSpin/ReservoirShapeLimit.lean). Thirty fresh Lean openings are individually listed with URLs and local hashes in [source_manifest.json](source_manifest.json). Historical files copied from round 5 are outside that fresh-opening list.

[PROOF.md](PROOF.md) independently derives the following parts, rather than assuming their imported Lean statements:

- Differentiating a tilted prescribed-tree density leaves the coefficient m_j-c*m_(j+1) at each internal vertex. Terminal terms cancel because the final exponent is one. Normalizing the negative coefficients by the leaf count gives a probability growth law and the exact Taylor coefficients (-1)^k/(k+1) times its tree moments.
- The bounded insertion has radius rho=1-exp(-2D-1) in (0,1). Its K-term remainder is at most rho^(K+1)/((K+1)(1-rho)), uniformly in depth and positive exponents. Real analyticity extends the expansion to every |t|<1.
- Walsh inversion and product-measure telescoping give exactly a times the sum of nonempty subset-overlap deviations for a independent site labels, with no extra factor two.
- The reservoir's Poisson intensity r_N=alpha*N*(N/(N+1))^(p-1) differs from alpha*N by at most alpha*(p-1). Score differentiation and an independent Poisson-affinity calculation both bound the root-law distance by (alpha*N-r_N)/sqrt(r_N), which vanishes. Changing both law and overlap center costs at most three times this distance per subset.
- Shape MAD is controlled by the finite sum of induced-subtree variances using Young's inequality. Given vanishing regular-topology variance averages and the stated depth-counting estimate, this yields the needed shape-error limit. Fixing the logarithmic truncation order before taking depth to infinity then proves the ordered-limit comparison. Directly summing the crude exponential shape envelope over all orders would fail at large insertion radius.

The independent exact arithmetic check compares formal power-mean series against tree-growth moments through order six. All 30 comparisons pass, including depths one, two and three, conditional nonuniform kernels, equal exponents and exponent 1/97; tree probabilities and leaf counts also agree exactly. Twelve additional exact tests directly compare the absolute-mass difference of the mixed product law and product of mean laws against the overlap-deviation bound, for one to three leaves and zero to three site labels; all pass. Command: `OMP_NUM_THREADS=1 nice -n 15 python3 audit_insertion.py > audit_output.txt`. Output is [audit_output.txt](audit_output.txt); this is not a Lean build. The three fresh main-theorem comparisons also pass; their hashes and URLs are in [preprint_manifest.json](preprint_manifest.json).

The remaining mathematical inputs are explicit: the complete independent-label encoding, the regular-overlap concentration and marker estimates, and the combinatorial regular-depth bound `qExpect_subtree_regular_bound`. No gap was found in the finite comparison or transfer checked here. The next concrete concentration check starts with `physicalOverlapLimsup_bound` in [PhysicalOverlapLimit.lean](sources/PhysicalOverlapLimit.lean), especially its use of `physicalOverlapAverage_le_marker` and `physicalShapeLimsup_tendsto`. A successful finite comparison conditional on these inputs does not certify the whole formula.

The recommended three-sentence replacement in the earlier section remains unchanged. The new work narrows the proof audit; it does not extend the OpenAI theorem to odd-K SAT or establish peer review.

