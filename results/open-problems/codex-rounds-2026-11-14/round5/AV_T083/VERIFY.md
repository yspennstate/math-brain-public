# Verification of T083, round 5

Checked 15 November 2026. All three manuscripts name OpenAI as author and October 4, 2026 as their date; the original main files and theorem sources were reopened and saved in [sources](sources/). Literature verdict: PARTIAL-CLAIMED, for all finite lengths under mixing and an additional internal claim for general triples. No full candidate proof is certified here.

REPORT.md uses the later continuation instruction's PROVED category only for the isolated smooth-row estimate in PROOF.md.

## Exact main theorem statements

These are verbatim theorem environments, with the original labels and macros. All three are Theorem 1.1. Their surrounding definitions were also read.

### Pointwise Multiple Ergodic Averages for Mixing Transformations

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

### Pointwise convergence of fourfold ergodic averages for mixing transformations

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

### Pointwise convergence of triple ergodic averages for mixing transformations

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

| Feature | Our row | First candidate | Fourfold candidate | Triple candidate |
|---|---|---|---|---|
| Model | One measure-preserving transformation; no mixing stated | Invertible, bimeasurable, mixing probability-preserving transformation | Same | Same; measurable inverse explicit |
| Range | Every finite k≥3 | Every finite n≥2 | Four factors | Three factors |
| Quantity | Normalized product average at n,2n,…,kn | Same, after renaming summation indices | Same at k=4 | Same at k=3 |
| Inputs | Every fixed tuple in L∞ | Same | Same | Bounded measurable complex functions |
| Strength | Almost-everywhere convergence as N→∞ | Same, all integer lengths | Same | Same |
| Limit | Existence only | Product of integrals | Product of integrals | Product of integrals |

For the first candidate, probability preservation, invertibility and bimeasurability appear immediately before its theorem. Each mixing definition is ordinary twofold mixing, μ(A∩T^{-r}B)→μ(A)μ(B) as |r|→∞. The first average is N^{-1}sum_{m=1}^N product_{j=1}^n f_j(T^{jm}x); the others use the corresponding three or four factors. No dimension parameter appears. These are full-sequence pointwise claims, rather than a norm bound, norm convergence or selected-subsequence convergence; no quantitative rate is asserted or needed.

Replacing the sum over 0≤n<N by the sum over 1≤n≤N changes the average by at most 2 product_j||f_j||∞/N. Bounded representatives can be used after removing a countable union of translated null sets. Thus the indexing and representative conventions do not change the convergence question. The exceptional null set can depend on the fixed tuple, as in the usual reading of our row.

The first main theorem covers every requested length only in the mixing class; the other two cover its four- and three-function cases. Setting unused inputs equal to one also gives shorter lengths. All three allow a nonstandard original probability space. Mixing remains an extra hypothesis: a nontrivial identity transformation is a measure-preserving nonmixing example, whose averages converge trivially to their input product rather than generally to the product of means.

Our row does not explicitly state probability normalization or invertibility. The comparison uses its conventional probability-preserving interpretation; the manuscripts make no literal assertion for infinite-measure spaces. The usual fixed-tuple shift-factor and natural-extension reductions do not remove the mixing restriction. None of the three main theorems states the arbitrary-system, all-k≥3 result.

### The internal general-triple claim

The first paper's [original inputs section](https://github.com/openai/math/blob/main/preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026/build/sections/inputs.tex), [saved here](sources/candidate1-inputs.tex), was reopened. It contains exactly:

```tex
\begin{lemma}[Triple pointwise convergence]\label{lem:triple-convergence}
On any standard invertible probability-preserving system, averages
of at most three bounded functions at distinct positive integer
slopes converge almost everywhere along all positive integer lengths.
\end{lemma}
```

This additionally claims the general k=3 case on standard invertible probability systems, using imported smooth convergence and profile approximation. The earlier conditional smoothing check remains as recorded in the earlier reports. Neither this internal claim nor any of the three main statements claims arbitrary nonmixing systems for every k≥4. A conclusion based only on their mixing titles would miss the internal triple claim.

## Follow-ups actually opened

The initial literature refresh was bounded to five minutes. The search queries are recorded in [LOG.md](LOG.md). No later settlement of the full row was identified; this is a bounded finding, not an assertion of exhaustive absence.

- [Release history](https://raw.githubusercontent.com/openai/math/main/history.md): latest listed update October 29, 2026; no entry naming a correction or withdrawal of these candidates. Fresh original introductions, rows.tex and base.tex match round 4 unchanged.
- Floris van Doorn, Polona Durcik, Joris Roos, Lenka Slavíková, Christoph Thiele, [*A blueprint for the formalization of norm-variation of multiple ergodic averages for commuting transformations*](https://arxiv.org/abs/2608.27321), arXiv:2608.27321, submitted August 27, 2026. The arXiv page concerns norm-variation rather than the full pointwise conclusion. No proof inside that paper is relied on here.
- [Christoph Thiele's papers page](https://www.math.uni-bonn.de/people/thiele/papers/) lists an AI-generated pointwise result concerning two commuting transformations. That listing does not state the all-k≥3 result. The linked registry proof was not audited in this session.
- [OSVerify's report on the trilinear Hilbert transform dependency](https://osverify.github.io/cases/trilinear-hilbert.html), reviewing OpenAI's October 5, 2026 version: it lists an omitted endpoint inclusion, a missing conditional-expectation term for augmented inputs, and a reversed role-order convention, with proposed repairs. It expressly does not establish falsity of the main theorem. This is an error report on a dependency, not an independent certification or refutation of the ergodic claims; the repairs are not certified here.
- [Lean README](https://github.com/openai/math/blob/main/lean/README.md), [formalization catalogue](https://github.com/openai/math/blob/main/lean/formalization.yaml), [docs listing](https://github.com/openai/math/tree/main/lean/docs), and [docs/145.md](https://github.com/openai/math/blob/main/lean/docs/145.md). The catalogue and directory were retrieved through the read-only GitHub connector and saved [here](sources/formalization.yaml) and [here](sources/lean-docs.json). No ergodic/pointwise/slopes catalogue entry or docs/154.md was found; 154 is the release's family number for these papers. Document 145 declares a separate formalization of multiple mixing, not the pointwise-average theorem. No Lean compilation was performed.

No matching arXiv version of the three candidates or new expert verification was found in this refresh. Earlier sessions opened other expositions and review listings; those were not all reopened here. Their historical observations remain in the earlier VERIFY.md files and are not represented as new checks.

## Recommended new “where it stands” wording

Keep the full arbitrary-system, all-k≥3 row open pending verification: OpenAI's *Pointwise Multiple Ergodic Averages for Mixing Transformations* (October 4, 2026) claims convergence for every finite length under mixing. Its internal Lemma 2.5 also claims three-factor convergence on arbitrary standard invertible probability systems using companion analytic estimates. Those estimates remain unverified in this check, so the release's claims do not establish a settlement of the full row.

## Spot check

The round-4 row lemma was rederived through its private-coordinate comparisons, stopped-path bound, dyadic-prefix bound, weak-tail integration and Abel summation. Read-only execution of its script again passed all 4,240 stopping configurations and 8,480 Abel checks. The earlier conditional row result holds under its stated hypotheses.

The single extension is a full check and refinement of `smooth-depth`, the raw scheduled-input row estimate invoked at lines 535–578 of [base.tex](sources/candidate3-base.tex) in the separated-scale lemma. [PROOF.md](PROOF.md) checks fixed carriers, exact mean-zero bump differences, augmentation, whole-row support, observation partitions and increasing read indices. Disjoint residue-class output coordinates allow their norms to combine in square sum. Under the original selected-array Bessel and input hypotheses, this proves

\[
 \left(\sum_{(I,\nu)\in\mathcal E}
       |\mathcal W_{I,\nu}f_{s(I)}|^2\right)^{1/2}
 \le140(B_H+A)\big(\log_2(2d)\big)^{3/2}|R|^{1/2},
 \qquad d=2+\#\mathcal N.
\]

The manuscript's displayed bound is 760(B_H+A)(log_2(2d))²|R|^{1/2}. The refinement retains its hypotheses and improves only this finite operator estimate. The scalar source construction's selected-array Bessel bound, pooled coefficient envelopes, projected-input compression and full separated-scale lemma remain unverified.

[check_smooth_rows.py](check_smooth_rows.py) uses exact rational polynomial integration to check the bump decomposition and fixed-carrier martingale orthogonality, including rough overlapping carriers, changing schedules, skipped or empty lag outputs, and multiple support depths in one residue class. It independently checks the geometric tails and constant 140; numerical catalog checks supplement the written universal inequalities. Commands and final counts are in LOG.md. These finite checks support the proof and do not prove an ergodic convergence theorem.

No flaw was found in this isolated smooth-row step. The next check is the source-selected array assertion in base.tex lines 553–569: inspect the corresponding “A scale sum for one separated term” proof in manuscript H and verify its ordinary joint Bessel norm, fixed complete carriers and catalog size before invoking the now-checked row estimate.
