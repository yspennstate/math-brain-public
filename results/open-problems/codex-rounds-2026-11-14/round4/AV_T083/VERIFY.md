# Verification of T083

Checked 15 November 2026. The candidate manuscripts are by OpenAI, dated October 4, 2026. The release claims part of the row; it does not supply a main theorem covering arbitrary systems for every k≥3. This session confirms the earlier conditional transference calculation and checks the next finite operator lemma, without certifying any candidate's full proof.

Literature verdict: PARTIAL-CLAIMED, covering all finite lengths under mixing and an additional internal claim for general triples. REPORT.md uses the continuation task's PROVED category only for the isolated row lemma checked in this session.

## Exact main theorem statements

These are verbatim TeX theorem environments from the current original source files, including macros and labels. The surrounding hypotheses and definitions are described below. All three are Theorem 1.1.

### 1. Pointwise Multiple Ergodic Averages for Mixing Transformations

[Original theorem source](https://github.com/openai/math/blob/main/preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026/build/sections/introduction.tex); [saved source](sources/candidate1-introduction.tex).

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

[Original theorem source](https://github.com/openai/math/blob/main/preprints/Pointwise-convergence-of-fourfold-ergodic-averages-for-mixing-transformations-October-4-2026/build/sections/01-introduction.tex); [saved source](sources/candidate2-introduction.tex).

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

[Original theorem source](https://github.com/openai/math/blob/main/preprints/Pointwise-convergence-of-triple-ergodic-averages-for-mixing-transformations-October-4-2026/build/paper/sections/introduction.tex); [saved source](sources/candidate3-introduction.tex).

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

## Comparison with our statement

| Feature | Our row | Candidate 1 | Candidate 2 | Candidate 3 |
|---|---|---|---|---|
| System | Measure preserving, without mixing | Invertible, bimeasurable, probability preserving, mixing | Same | Same |
| Number of factors | Every finite k≥3 | Every finite n≥2 | Four | Three |
| Iterates | n,2n,…,kn of one T | Same consecutive pattern | n,2n,3n,4n | n,2n,3n |
| Inputs | Every fixed tuple in L∞ | Same | Same | Bounded measurable complex functions |
| Conclusion | Almost-everywhere convergence | Almost-everywhere convergence | Same | Same |
| Averaging lengths | All positive integers | All positive integers | Same | Same |
| Limit required | Existence only | Product of integrals | Product of integrals | Product of integrals |

Candidate 1's preceding paragraph imposes probability preservation, invertibility and bimeasurability. Its equation “mixing” means μ(A∩T^{-r}B)→μ(A)μ(B) for every pair of measurable sets as |r|→∞. The other candidates impose the same mixing condition. All three explicitly allow a nonstandard original probability space.

Each statement concerns exactly the same single-parameter averages as our row, on its stated subclass of systems. No dimension parameter appears. These are full-sequence pointwise assertions, stronger than just a norm bound, norm convergence, or subsequence convergence. The specified product limit is additional information in the mixing class.

The sum from 1 to N instead of 0 to N−1 changes an average by at most 2∏||f_j||∞/N, after removing the countable union of orbit translates of the exceptional sets for bounded representatives. The two indexing conventions therefore have the same convergence behavior. Bounded representatives and L∞ functions are equivalent for this assertion. The null set can depend on the fixed tuple; no simultaneous assertion for all tuples is requested.

Mixing is an extra hypothesis, absent from our statement. Candidate 1 covers every requested length within the mixing class; candidates 2 and 3 cover its four- and three-factor cases. None of the three main theorems covers arbitrary nonmixing systems. A nontrivial identity transformation illustrates the scope difference, although its own averages trivially converge.

Our wording also omits the probability and invertibility hypotheses present in the manuscripts. We interpret the intended row as the usual probability-preserving pointwise conjecture. This report does not claim that the manuscripts literally cover infinite-measure spaces or noninvertible transformations. Standard factor and natural-extension reductions may address the latter technical conventions, but do not remove the mixing restriction.

## The internal general-triple claim

Candidate 1's [original inputs section](https://github.com/openai/math/blob/main/preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026/build/sections/inputs.tex), saved as [candidate1-inputs.tex](sources/candidate1-inputs.tex), contains the following exact additional claim:

```tex
\begin{lemma}[Triple pointwise convergence]\label{lem:triple-convergence}
On any standard invertible probability-preserving system, averages
of at most three bounded functions at distinct positive integer
slopes converge almost everywhere along all positive integer lengths.
\end{lemma}
```

Thus “all three papers only claim mixing results” would be incomplete. This internal lemma claims the general three-factor case, on standard invertible probability systems, at distinct positive slopes. It relies on the distinct-slopes companion and its analytic estimates. It does not claim arbitrary nonmixing systems for every k≥4.

For the consecutive-triple route, the [original transfer section](sources/candidate3-transfer.tex) states “Local estimate with variation in depth” and deduces finite orbit oscillation without using mixing. The local estimate is the premise assumed in round 3. The introduction explicitly identifies its analytic dependency as OpenAI, *An L³ bound for the trilinear Hilbert transform*, October 5, 2026; its [original main source](https://github.com/openai/math/blob/main/preprints/An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026/build/paper.tex) was opened. The [base](sources/candidate3-base.tex) and [completion](sources/candidate3-completion.tex) sections invoke estimates inside that companion proof in addition to the row lemma checked here.

## Follow-ups and sources actually opened

The bounded literature refresh used the web search tool with the queries recorded in [LOG.md](LOG.md). No new settlement of the full row, matching arXiv version of these three titles, or expert certification was identified in the returned sources. This is a bounded search result, not an exhaustive assertion that no such material exists.

- Bogdan Grechuk, [*Mixing of All Orders and Pointwise Averages*](https://functor.network/user/3333/entry/2061), 10 November 2026: an exposition of the release's claims. It does not independently verify the analytic proof chain.
- [Christoph Thiele's papers page](https://www.math.uni-bonn.de/people/thiele/papers/) lists an AI-generated pointwise result for two commuting transformations. That title does not give the all-k conclusion in our row.
- Floris van Doorn, Polona Durcik, Joris Roos, Lenka Slavíková, Christoph Thiele, [*A blueprint for the formalization of norm-variation of multiple ergodic averages for commuting transformations*](https://arxiv.org/abs/2608.27321), arXiv:2608.27321, submitted 27 August 2026: the arXiv page was opened. Its abstract describes norm-variation, strengthening norm convergence, rather than our full pointwise conclusion.
- [OSVerify's actual trilinear-Hilbert-transform report](https://osverify.github.io/cases/trilinear-hilbert.html), on the October 5 version: it reports a missing endpoint inclusion, an omitted conditional-expectation term in a predictor identity, and a reversed first-failing-role convention. It proposes repairs and expressly does not establish that the main theorem is false. This concerns an analytic dependency, not a verified refutation of the ergodic claims. The present check does not validate all proposed repairs.
- [Release history](https://github.com/openai/math/blob/main/history.md), also [saved](sources/history.md): its latest entry remains October 29, 2026. No named correction or withdrawal of these three candidates is listed.
- [Lean README](https://github.com/openai/math/blob/main/lean/README.md), the original [formalization catalogue](https://github.com/openai/math/blob/main/lean/formalization.yaml), and the [lean/docs directory](https://github.com/openai/math/tree/main/lean/docs) were opened. The last web open failed with a cache miss; the GitHub connector successfully retrieved the directory listing. The catalogue has no matching ergodic/pointwise/slopes entry; its mixing hits are unrelated. The docs listing has no 154.md, the release's family number for these averages. Copies of the [catalogue](sources/formalization.yaml) and [listing](sources/lean-docs.json) are saved.
- [lean/docs/145.md](https://github.com/openai/math/blob/main/lean/docs/145.md), also [saved](sources/lean-145.md), declares formalization of the separate multiple-mixing implication for measurable sets. This is not a formalization of the pointwise-average theorem. No Lean compilation or Comparator audit was performed.
- Original TeX introductions for all three candidates, candidate 1's inputs section, and the consecutive-triple transfer, rows, base, localization and completion sections were retrieved through the read-only GitHub connector. The proof check below reads the full row section and the relevant statements and uses in the other sections; saving a source does not mean every argument in it was audited.

The earlier sessions additionally opened community review listings and the distinct-slopes manuscript. Their observations remain in their own logs; those secondary listings were not newly audited here.

## Recommended “where it stands” sentence

Keep the full arbitrary-system, all-k row open: OpenAI's *Pointwise Multiple Ergodic Averages for Mixing Transformations* (October 4, 2026) claims convergence for every finite length under mixing. Its internal Lemma 2.5 also claims three-factor convergence on arbitrary standard invertible probability systems, using companion analytic estimates. Those analytic estimates remain unverified in this check, so these claims do not establish a settlement of the full row.

## Spot check

The round 3 calculation was rechecked by read-only execution of its exact-arithmetic script and by an independent square-coordinate computation of the planting region's second moment. Both confirm mean eta²=2e²/27, hence the second-order normalized Taylor factor e²/27 and per-scale decay O(2^{-2k}). The result remains conditional on the local analytic estimate.

The single extension in this session is a verification of the consecutive-triple paper's depth-varying catalog-row lemma and its maximal premise. [PROOF.md](PROOF.md) states all hypotheses and derives the estimate in full. Persistent private columns give coefficient bounds D^{-1} and D^{3/2}; whole-row stopping with 2^ceil(5 log₂ D) buckets yields the weak maximal bound. Integrating it and applying Abel summation on deterministic input blocks yields exactly

\[
 \left(\sum_n\sum_{\nu\in\mathcal R_n}
       \|A_\nu F_{s_n}\|^2\right)^{1/2}
 \le \frac83\sqrt{9+(1+\lceil5\log_2 D\rceil)^2}\,
       B|R|^{1/2}
 \le \frac{40}{3}B\log_2(2D)|R|^{1/2}.
\]

The stopping subsets are subsets of the original whole rows, so their Bessel bound is legitimate even when selection depends on the tests. A finer observation partition may detect different hits inside a support cell only after that row has been assigned. This avoids an unjustified Bessel inference for rows multiplied by partial-support stopping masks.

No defect was found in this isolated row lemma under its complete stated hypotheses. It does not verify the full depth-variation theorem: one must still check that the constructed analytic rows and catalogs satisfy those hypotheses with the stated budgets and validate the remaining scalar estimates imported from the companion.

[check_rows.py](check_rows.py) supplies exact rational finite-model checks of whole-support assignments, branch-dependent hits, bucket sums, Bessel bounds, prefix decompositions and Abel identities, plus source-quotation and constant checks. These finite tests supplement the proof; they do not establish any unrestricted analytic theorem.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B check_rows.py`. All 4,240 stopping configurations, 8,480 Abel checks, three exact theorem quotations, four source-continuity checks and the constant identities passed. The final run used 16,744,448 bytes peak RSS, took 1.993 seconds and confirmed inherited nice=20.
