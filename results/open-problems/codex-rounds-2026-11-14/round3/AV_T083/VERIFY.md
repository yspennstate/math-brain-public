# T083 literature verification and continuation

Checked 15 November 2026. The three manuscripts name OpenAI as author and October 4, 2026 as their date. The literature verdict remains PARTIAL-CLAIMED; the continuation result is a conditional transference check, reported as PARTIAL in REPORT.md under this session's requested format. No proof of a candidate main theorem is certified.

## Exact main theorem statements

These are exact theorem environments from the current original TeX, retrieved through the read-only GitHub connector. They match the earlier source cache. The repository is distributed under Apache 2.0.

### 1. Pointwise Multiple Ergodic Averages for Mixing Transformations

[Original source](https://github.com/openai/math/blob/main/preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026/build/sections/introduction.tex); [saved source](sources/candidate1-introduction.tex).

```tex
\begin{theorem}\label{thm:main}
Suppose that $T$ satisfies \eqref{eq:mixing}. For every integer
$n\ge2$ and every fixed $f_1,\ldots,f_n\in L^\infty(\mu)$,
\[
 A_N(f_1,\ldots,f_n)(x)
 \longrightarrow\prod_{j=1}^n\int_X f_j\dd\mu
 \qquad\text{for $\mu$-almost every }x,
\]
as $N$ tends to infinity through all positive integers. The probability
space need not be standard, and no rate of mixing is required.
\end{theorem}
```

### 2. Pointwise convergence of fourfold ergodic averages for mixing transformations

[Original source](https://github.com/openai/math/blob/main/preprints/Pointwise-convergence-of-fourfold-ergodic-averages-for-mixing-transformations-October-4-2026/build/sections/01-introduction.tex); [saved source](sources/candidate2-introduction.tex).

```tex
\begin{theorem}\label{thm:main}
Let $(X,\mathcal F,\mu)$ be a probability space and let $T:X\to X$
be invertible, bimeasurable, measure preserving, and mixing in the sense
of \eqref{eq:mixing}. For every $f_1,f_2,f_3,f_4\in L^\infty(\mu)$,
\[
 \frac1N\sum_{n=1}^N
 f_1(T^nx)f_2(T^{2n}x)f_3(T^{3n}x)f_4(T^{4n}x)
 \longrightarrow \prod_{j=1}^4\int_X f_j\dd\mu
\]
for $\mu$-almost every $x$, along all positive integers $N$.
The original probability space need not be standard.
\end{theorem}
```

### 3. Pointwise convergence of triple ergodic averages for mixing transformations

[Original source](https://github.com/openai/math/blob/main/preprints/Pointwise-convergence-of-triple-ergodic-averages-for-mixing-transformations-October-4-2026/build/paper/sections/introduction.tex); [saved source](sources/candidate3-introduction.tex).

```tex
\begin{theorem}\label{thm:main}
Let $(X,\mathcal F,\mu)$ be an arbitrary probability space and let
$T:X\to X$ be an invertible mixing probability preserving transformation
with measurable inverse.  For every triple of bounded measurable functions
$f_1,f_2,f_3:X\to\C$,
\[
 A_N(f_1,f_2,f_3)(x)
 \longrightarrow \prod_{j=1}^3\int_X f_j\,d\mu
 \quad\text{for $\mu$-almost every }x
\]
as $N\to\infty$ through all positive integers.  The exceptional null set
may depend on the triple of functions.
\end{theorem}
```

For candidate 1, the preceding text specifies an invertible, bimeasurable, measure-preserving transformation of a probability space. Its mixing equation is ordinary twofold mixing: μ(A∩T^(-r)B)→μ(A)μ(B) as |r|→∞. Its A_N is N^(-1)∑_{m=1}^N∏_{j=1}^n f_j(T^(jm)x). Candidate 2 uses the same mixing condition; candidate 3 defines A_N with the three times n,2n,3n. These definitions were read in the saved introductions.

## Comparison with our row

| Feature | Our statement | Candidate 1 | Candidate 2 | Candidate 3 |
|---|---|---|---|---|
| Underlying system | Measure-preserving, no mixing stated | Probability-preserving, invertible, bimeasurable, mixing | Same | Same; measurable inverse explicit |
| Factor count | Every finite k≥3 | Every finite n≥2 | Four | Three |
| Times and quantity | One T, n,2n,…,kn; normalized product sum | Same after renaming indices | Same at k=4 | Same at k=3 |
| Inputs | Every fixed L∞ tuple | Same | Same | Bounded measurable complex functions |
| Conclusion | Existence of a limit almost everywhere | Full-sequence almost-everywhere convergence | Same | Same |
| Averaging lengths | All N→∞ | All positive integers | Same | Same |
| Limit identification | No formula requested | Product of means | Product of means | Product of means |

There is no dimension parameter to compare. All three assert the requested pointwise strength, rather than a norm bound, norm convergence, or convergence on a selected subsequence. The product-of-means limit is an additional conclusion in the mixing class. Setting unused inputs equal to one gives shorter averages.

The sums from 1 to N differ from our sums from 0 to N−1 by two endpoint terms, bounded in absolute value by 2∏||f_j||∞/N. The null set may depend on the fixed tuple in both formulations. Allowing arbitrary probability spaces removes a standardness restriction but does not remove mixing.

Mixing is a genuine restriction: the identity map on a probability space with a set of measure strictly between zero and one is measure preserving and not mixing. Its average is the fixed product of the inputs, illustrating why the product-of-means formula is not the formula for arbitrary systems. None of the three main theorems literally covers arbitrary nonmixing systems for every k≥3. The row also omits probability normalization and invertibility; this comparison uses the conventional probability-preserving interpretation of the problem. These papers make no literal claim for infinite-measure systems.

### Internal claim beyond the mixing main theorem

Candidate 1's current [inputs section](https://github.com/openai/math/blob/main/preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026/build/sections/inputs.tex), saved as [candidate1-inputs.tex](sources/candidate1-inputs.tex), contains this exact statement:

```tex
\begin{lemma}[Triple pointwise convergence]\label{lem:triple-convergence}
On any standard invertible probability-preserving system, averages
of at most three bounded functions at distinct positive integer
slopes converge almost everywhere along all positive integer lengths.
\end{lemma}
```

This is an internal claim of the general triple case, with standardness and invertibility as written. Its preceding proposition imports smooth triple convergence and signed-profile approximation from OpenAI, *Triple ergodic averages with distinct integer slopes* (October 4, 2026), without mixing. Candidate 1 explains the standard shift-factor reduction for a fixed tuple. Consequently a title-only conclusion that the release has no claim about general triples would be wrong.

Candidate 3's [ergodic section](https://github.com/openai/math/blob/main/preprints/Pointwise-convergence-of-triple-ergodic-averages-for-mixing-transformations-October-4-2026/build/paper/sections/ergodic.tex), saved [here](sources/candidate3-ergodic.tex), similarly states its finite oscillation estimate on every invertible probability-preserving system. This is the premise below the earlier smoothing check. Mixing is used later to identify the limit. The wider internal claims remain claims; they are not independently verified here.

## Follow-ups actually opened in this session

The initial literature refresh was limited to five minutes. The searches and source-access details are in LOG.md. Nothing found justified a SOLVED_ELSEWHERE.md.

- [Release history](https://raw.githubusercontent.com/openai/math/main/history.md): latest listed entry October 29, 2026; no named correction or withdrawal of these three candidates. The current introductions and checked transfer sources match the earlier copies.
- Bogdan Grechuk, [*Mixing of All Orders and Pointwise Averages*](https://functor.network/user/3333/entry/2061), 10 November 2026: exposition of the claims. It is not an independent full proof audit.
- Floris van Doorn, Polona Durcik, Joris Roos, Lenka Slavíková, Christoph Thiele, [*A blueprint for the formalization of norm-variation of multiple ergodic averages for commuting transformations*](https://arxiv.org/abs/2608.27321), arXiv:2608.27321, submitted 27 August 2026: abstract explicitly concerns norm-variation, a strengthening of norm convergence. It does not state the pointwise conclusion in our row. Only the arXiv page was needed for this scope check.
- [Christoph Thiele's papers page](https://www.math.uni-bonn.de/people/thiele/papers/) lists an AI-generated pointwise result for **two** commuting transformations with F. van Doorn, P. Durcik, J. Roos and L. Slavikova, and links [Palomar entry PALOMAR-2026-10-18-000026](https://palomar-registry.org/entry?id=PALOMAR-2026-10-18-000026&version=1). The registry entry itself displayed a JavaScript placeholder. That two-transformation title gives no settlement of the k≥3 problem; no unshown registry proof is relied on.
- [OpenVerification](https://openaireview.org/) displays potential issues for candidate 1, including dependence on multiple mixing. It describes AI-assisted issue detection. A listing is not a mathematical refutation; the release itself supplies a companion multiple-mixing claim.
- [OSVerify's report on *An L³ bound for the trilinear Hilbert transform*](https://osverify.github.io/cases/trilinear-hilbert.html), reviewing OpenAI's October 5 version: three issues with proposed repairs, concerning an endpoint inclusion, a predictor identity and role ordering. The report expressly does not establish falsity of the main theorem. This is an error report on an analytic dependency, not certification or refutation of the ergodic theorems.
- [Lean README](https://github.com/openai/math/blob/main/lean/README.md), [formalization catalogue](https://github.com/openai/math/blob/main/lean/formalization.yaml), and [docs listing](https://github.com/openai/math/tree/main/lean/docs): the current catalogue has no ergodic/pointwise/slopes match and the docs listing has no 154.md (the repository family number, unrelated to T083). No matching pointwise-average formalization was found. Catalogue text is [saved](sources/formalization.yaml).
- [lean/docs/145.md](https://github.com/openai/math/blob/main/lean/docs/145.md), [saved copy](sources/lean-145.md), declares a formalization of the separate implication from ordinary mixing to mixing of all finite orders for measurable sets. It does not formalize triple oscillation or the pointwise theorem. No Lean compilation or Comparator audit was performed here.
- The original TeX sections of the three candidates, candidate 1's inputs, and the distinct-slopes companion's [transfer section](https://github.com/openai/math/blob/main/preprints/Triple-ergodic-averages-with-distinct-integer-slopes-October-4-2026/build/sections/transfer.tex) were opened through the read-only connector and saved locally. The companion explicitly separates convergence from mixing-based limit identification.

No matching arXiv version of the three candidates, new named referee report, or independently checked settlement was identified in the bounded search. This is not an exhaustive claim of absence. The earlier worker's wider catalogue of opened pages remains in its read-only VERIFY.md; the items above are the sources reopened or newly opened here.

## Recommended new “where it stands” wording

Retain the full arbitrary-system, all-k≥3 row as open pending verification. OpenAI's unrefereed *Pointwise Multiple Ergodic Averages for Mixing Transformations* (October 4, 2026) claims convergence for every finite k under mixing, and its Lemma 2.5 additionally claims general triple convergence using companion estimates. No independent full proof verification or matching Lean formalization of the pointwise theorem was found in this check.

## Spot check

The earlier worker checked candidate 1's Lemma 2.5, conditionally on imported smooth convergence and profile density. Independently rederived its interval-profile identity, floor error, Riemann-sum comparison, countable conull intersection, identification by a common L² limit, and the estimate |A_M−A_N|≤2|M−N|/max(M,N). That conditional check holds.

The single extension here is the next bridge: candidate 3's local depth-variation estimate ⇒ finite orbit oscillation. A complete derivation is in [PROOF.md](PROOF.md), based on the [original transfer section](https://github.com/openai/math/blob/main/preprints/Pointwise-convergence-of-triple-ergodic-averages-for-mixing-transformations-October-4-2026/build/paper/sections/transfer.tex). The analytic local estimate is assumed, not verified.

The exact scale-difference kernel, translation averaging, integer planting, complex phase linearization and finite orbit cutoff all check out under that assumption. The planting region Q_e has area 4e²/3, zero first η moment and normalized second η moment 2e²/27. Taylor's theorem therefore sharpens the paper's first-order estimate to

\[
 |I_k-A_eD_k|
 \leq A_e\frac{e^2}{27}(2B+4e/3+1)
       \|b''\|_\infty L\,2^{-2k},
 \qquad e=1/100,\quad b=\varphi_2-\varphi,
\]

where supp b⊂[−B,B], B≥1, and k≥0. Summing divides by A_e and contributes the exact factor 4e²/81=1/202500 before the support-count and derivative factors. This is stronger decay in k, not a uniformly smaller profile-dependent constant or a stronger convergence theorem.

[check_transference.py](check_transference.py) checks the polygon moments by two independent exact-rational integrations, the kernel expansion, the sharp quadratic Taylor coefficient, 140 prefix/phase cases, six current-versus-earlier sources and all three exact theorem quotations. The initial run used about 15.5 MB RSS and 0.003 seconds; the final quotation audit is recorded in LOG.md.

No defect was found in this conditional transference bridge. The next load-bearing input to inspect is the depth-variation theorem itself and its use of the trilinear-Hilbert-transform companion. Neither this check nor the earlier one certifies a candidate main theorem.

