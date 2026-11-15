# Verification of T083, round 6

Checked 15 November 2026. The literature assessment remains PARTIAL-CLAIMED: the main theorems cover mixing systems, and an internal lemma additionally claims general triple convergence. No settlement of the full arbitrary-system, all-k statement was found in the bounded refresh. REPORT.md uses the continuation task's PROVED category only for the ordinary Bessel estimate proved in [PROOF.md](PROOF.md).

## Exact main theorems

The following are exact copies of the original theorem environments, including labels and macros, freshly retrieved through read-only GitHub fetch. All three papers name OpenAI as author and October 4, 2026 as their date; their main-file headers were also read from round 5's saved sources. The theorem definitions and surrounding system hypotheses were read in each introduction.

### Pointwise Multiple Ergodic Averages for Mixing Transformations

[Original theorem source](https://github.com/openai/math/blob/main/preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026/build/sections/introduction.tex); [saved source](sources/candidate1-introduction.tex).

~~~tex
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
~~~

### Pointwise convergence of fourfold ergodic averages for mixing transformations

[Original theorem source](https://github.com/openai/math/blob/main/preprints/Pointwise-convergence-of-fourfold-ergodic-averages-for-mixing-transformations-October-4-2026/build/sections/01-introduction.tex); [saved source](sources/candidate2-introduction.tex).

~~~tex
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
~~~

### Pointwise convergence of triple ergodic averages for mixing transformations

[Original theorem source](https://github.com/openai/math/blob/main/preprints/Pointwise-convergence-of-triple-ergodic-averages-for-mixing-transformations-October-4-2026/build/paper/sections/introduction.tex); [saved source](sources/candidate3-introduction.tex).

~~~tex
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
~~~

## Comparison with our statement

| Feature | Our row | Main theorems of the candidates |
|---|---|---|
| Transformation | Measure preserving, with no mixing condition | Invertible and mixing, with measurable inverse, on a probability space |
| Number of functions | Every finite k≥3 | First paper: every n≥2; second: four; third: three |
| Times | n,2n,…,kn | Identical consecutive multiples for each stated length |
| Inputs | Every fixed bounded tuple in L∞ | Same; triple paper explicitly allows complex measurable inputs |
| Convergence | Almost everywhere as N tends to infinity | Same, along all integer lengths |
| Limit | Existence | Product of the integrals |
| Underlying space | No standardness assumption stated | Original probability space need not be standard |

The first paper's system assumptions are stated before the theorem. Mixing is ordinary twofold mixing, with no rate assumed. There is no spatial dimension parameter to compare. These claims concern pointwise convergence along the full sequence, rather than a norm estimate, norm convergence or a subsequence.

Changing the sum over 0≤n<N to the sum over 1≤n≤N changes its value by at most 2∏j||f_j||∞/N, which tends to zero. Renaming the length variable n in the first paper to k changes nothing. Bounded representatives can be chosen on the complement of a countable union of translated null sets, and the exceptional null set may depend on the fixed tuple.

The first main theorem covers all requested finite lengths under the additional mixing hypothesis. The other two cover k=4 and k=3 under the same restriction. None of these main theorems claims the full nonmixing, all-k result. The comparison uses the conventional probability-preserving interpretation of our row; the papers do not assert the literal infinite-measure version if our phrase “measure-preserving” is interpreted that broadly. Standard factor and natural-extension reductions do not remove the mixing restriction.

The first paper also states the following internal result, which goes beyond its mixing main theorem. Its [inputs section](https://github.com/openai/math/blob/main/preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026/build/sections/inputs.tex), [saved here](sources/candidate1-inputs.tex), was freshly reopened.

~~~tex
\begin{lemma}[Triple pointwise convergence]\label{lem:triple-convergence}
On any standard invertible probability-preserving system, averages
of at most three bounded functions at distinct positive integer
slopes converge almost everywhere along all positive integer lengths.
\end{lemma}
~~~

This claims the general k=3 case for standard invertible probability-preserving systems, using companion analytic estimates and profile approximation. It does not give arbitrary nonmixing systems for every k≥4. The earlier transference and row checks verify only individual implications in this chain.

## Follow-ups and sources opened

The initial refresh stopped within five minutes. Exact-title and pointwise/triple/ergodic/2026 searches found known release claims and expositions, with no later full settlement identified. This bounded result is not an exhaustive absence claim.

- [Release history](https://raw.githubusercontent.com/openai/math/main/history.md): its latest listed update is October 29, 2026, and it names no revision or withdrawal of these three candidates. An initial uppercase HISTORY.md URL returned 404; the lowercase file was then opened.
- Floris van Doorn, Polona Durcik, Joris Roos, Lenka Slavíková, Christoph Thiele, [A blueprint for the formalization of norm-variation of multiple ergodic averages for commuting transformations](https://arxiv.org/abs/2608.27321), arXiv:2608.27321, submitted August 27, 2026. The arXiv page was opened; its subject is norm-variation, not the full pointwise statement. No proof from it is used here.
- [Christoph Thiele's papers page](https://www.math.uni-bonn.de/people/thiele/papers/) lists an AI-generated pointwise result for two commuting transformations. This listing does not state the all-k≥3 result; its registry proof was not audited.
- [OSVerify's report](https://osverify.github.io/cases/trilinear-hilbert.html) on OpenAI's October 5 manuscript, An L³ bound for the trilinear Hilbert transform, was reopened. It lists an endpoint-hypothesis issue, an omitted conditional-expectation term for augmented inputs and a role-order issue, with proposed repairs. It does not establish falsity of the main theorem. These are reported issues in a dependency, not independent certification or refutation of the three pointwise papers.
- [OpenVerification front page](https://openaireview.org/) was opened after a search result mentioned multiple-mixing concerns. The opened page exposed only a JavaScript shell, without a detailed review. The snippet is not treated here as a verified new objection.
- The current [Lean README](https://github.com/openai/math/blob/main/lean/README.md), [formalization catalogue](https://github.com/openai/math/blob/main/lean/formalization.yaml), [docs listing](https://github.com/openai/math/tree/main/lean/docs) and [docs/145.md](https://github.com/openai/math/blob/main/lean/docs/145.md) were opened. The connector supplied the actual text where web rendering showed navigation. The catalogue has no ergodic/pointwise/slopes match; its mixing matches concern unrelated declarations. The 245-entry docs listing has no 154.md. Document 145 describes a separate multiple-mixing formalization. The catalogue and parsed doc names are saved in [sources/formalization.yaml](sources/formalization.yaml) and [sources/lean-doc-names.txt](sources/lean-doc-names.txt). No Lean compilation was attempted.
- Fresh original candidate introductions, the first paper's inputs section and the triple paper's base section were saved. All five match round 5 unchanged, ignoring final newline.
- OpenAI, [An L³ bound for the trilinear Hilbert transform](https://github.com/openai/math/tree/main/preprints/An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026), October 5, 2026: opened its directory, main TeX, and complete base, charts and compression sections. These are saved as H-main.tex, H-base.tex, H-charts.tex and H-compression.tex. They provide the scalar Bessel argument checked below.

No matching arXiv version of the three candidates or new expert certification was identified in the bounded refresh. Other expositions from earlier rounds were not all reopened, and their earlier observations are not counted as new checks.

## Recommended new “where it stands” sentence

Keep the arbitrary-system, all-k≥3 row open pending verification: OpenAI's Pointwise Multiple Ergodic Averages for Mixing Transformations (October 4, 2026) claims full-sequence convergence for every finite length under mixing. Its internal Lemma 2.5 also claims general three-factor convergence on standard invertible probability systems using companion analytic estimates. The release's claims and the isolated checks completed here do not establish a settlement of the full row.

## Spot check

Round 5's smooth-row estimate was independently rederived and its read-only script rerun. All exact checks passed; disjoint residue classes combine in square sum, giving logarithmic exponent 3/2 and constant 140 under its stated Bessel hypotheses.

The single extension verifies that ordinary Bessel premise from the scalar frequency hypotheses stated by manuscript H. [PROOF.md](PROOF.md) proves, for selected rows with bounded-height centers, global separation at each scale, fixed complete carriers and smooth mean-zero bumps,

\[
 \left(\sum_{(I,\nu)}|W_{I,\nu}f|^2\right)^{1/2}
 \le26 A\sqrt{S_p}\,\|f\|_2,\qquad
 S_p=p\bigl(\lceil\log_2(4p\,p!\,B^{p^2+p})\rceil+2\bigr),
 \quad p=d+1.
\]

Here d is the number of fixed unrestricted real parameters, B bounds rational coefficient height and A controls the bump's first two scaled derivatives as well as its value. The catalog has at most (3B²)^d distinct frequencies. Both its logarithmic size and the squared Bessel bound are polynomial in d and log(2B), with the stated derivative factor.

The proof supplies the missing scale count by a direct integer-minor argument; then Plancherel, local Poincaré and two antiderivatives sum the low and high frequency shells. It checks the exact center null set, missing depths, rational cancellation, the slope factor, fixed multipliers and selected subarrays. Its source application is conditional on the upstream chart/Weyl/truncation statements, which have not been certified.

[check_bessel.py](check_bessel.py) independently audits the exact height ranges, occupied scales, shell multiplicities, polynomial cancellations, Poincaré and antiderivative identities, and numerical constants. An explicit example outside the common-multiplier hypothesis gives squared output h/2048² at h complete depths, showing why that hypothesis is necessary. The example does not contradict the source, which fixes the multiplier on the birth root.

No flaw was found in this isolated Bessel step. The next check is the ordinary projected-input compression premise in H-compression.tex and its use in candidate3-base.tex lines 584–622. The chart expansion, uniform pooled coefficient tails, complete separated-scale lemma, local analytic estimate and candidate main proofs remain unverified.

