# Verification of T083: pointwise convergence of multiple ergodic averages

Checked 14 November 2026. Author on all three manuscripts: OpenAI. Date on all three: October 4, 2026. Verdict: PARTIAL-CLAIMED. The main theorems cover mixing systems; an internal lemma additionally claims the general three-function case. This report compares claims and does not certify their proofs.

## Main theorems copied exactly

The following are verbatim theorem environments from the actual TeX sources, including their labels and macros. Each is Theorem 1.1. The repository distributes the texts under Apache 2.0. Full retrieved source files are saved in sources/.

### 1. Pointwise Multiple Ergodic Averages for Mixing Transformations

[Original theorem source](https://github.com/openai/math/blob/main/preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026/build/sections/introduction.tex); [local copy](sources/candidate1-introduction.tex).

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

[Original theorem source](https://github.com/openai/math/blob/main/preprints/Pointwise-convergence-of-fourfold-ergodic-averages-for-mixing-transformations-October-4-2026/build/sections/01-introduction.tex); [local copy](sources/candidate2-01-introduction.tex).

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

[Original theorem source](https://github.com/openai/math/blob/main/preprints/Pointwise-convergence-of-triple-ergodic-averages-for-mixing-transformations-October-4-2026/build/paper/sections/introduction.tex); [local copy](sources/candidate3-introduction.tex).

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

For candidate 1, the preceding text specifies a probability space and an invertible, bimeasurable, measure-preserving T; equation (1.1) is ordinary twofold mixing, μ(A∩T^{-r}B) → μ(A)μ(B) as |r|→∞, for every pair of measurable sets. Its A_N is N^{-1}∑_{m=1}^N∏_{j=1}^n f_j(T^{jm}x). Candidate 2 uses the same mixing definition. Candidate 3 defines A_N by the three-factor formula in our question, summed from 1 to N.

## Comparison with our statement

| Feature | Our row | Candidate 1 | Candidate 2 | Candidate 3 |
|---|---|---|---|---|
| System | Measure-preserving; no mixing assumption | Probability-preserving, invertible, bimeasurable, mixing | Same | Same; measurable inverse explicit |
| Number of factors | Every finite k≥3 | Every finite n≥2 | Four | Three |
| Times | n,2n,…,kn of one T | Same, indices renamed | n,2n,3n,4n | n,2n,3n |
| Functions | Every fixed L∞ tuple | Same | Same | Bounded measurable complex inputs |
| Strength | Almost-everywhere convergence | Same | Same | Same |
| Lengths | Full sequence | All positive integers | All positive integers | All positive integers |
| Limit | Existence only | Product of integrals | Product of integrals | Product of integrals |
| Rate | None requested | None required or supplied | None required or supplied | None required or supplied |

Candidate 1 claims every k in the row only in the mixing class; candidates 2 and 3 claim its four- and three-function cases in that class. Putting unused functions equal to 1 also gives shorter lengths. These are full-sequence pointwise convergence assertions, not merely norm convergence, estimates, or subsequence convergence. No dimension parameter appears. None is a theorem about arbitrary commuting transformations or nonlinear polynomial iterates, which our row also does not require.

The indexing change from 0≤n<N to 1≤n≤N makes no difference: with M=∏‖f_j‖∞, the averages differ by at most 2M/N outside a countable union of translated null sets. Each exceptional null set may depend on the fixed tuple, as in the usual interpretation of our row.

Mixing is a genuine additional restriction: a nontrivial identity transformation is measure preserving and not mixing, so the main theorems do not cover it, even though its averages trivially converge. Mixing is stronger than weak mixing and ergodicity. The product formula is an additional conclusion, not the proposed formula on arbitrary systems. The main statements explicitly allow nonstandard probability spaces.

Our row does not explicitly require μ(X)=1 or invertibility, whereas all three main theorems do. In the usual probability-space formulation of the conjecture, a fixed tuple can be reduced to a standard shift factor and a noninvertible system handled by its natural extension; this usual reduction does not eliminate the mixing restriction. These papers make no literal claim about infinite-measure systems. This report treats our intended row as the conventional probability-preserving conjecture.

### A wider claim inside candidate 1

The main theorem is not the whole scope of the manuscript. Section 2.3, Lemma 2.5 states exactly:

```tex
\begin{lemma}[Triple pointwise convergence]\label{lem:triple-convergence}
On any standard invertible probability-preserving system, averages
of at most three bounded functions at distinct positive integer
slopes converge almost everywhere along all positive integer lengths.
\end{lemma}
```

Its proof uses Proposition 2.2, importing smooth triple convergence and profile approximation from OpenAI, *Triple ergodic averages with distinct integer slopes* (October 4, 2026). [Original inputs section and proof](https://github.com/openai/math/blob/main/preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026/build/sections/inputs.tex). The companion's [actual introduction](https://github.com/openai/math/blob/main/preprints/Triple-ergodic-averages-with-distinct-integer-slopes-October-4-2026/build/sections/introduction.tex) was opened: its main theorem also assumes mixing, but its imported smooth-oscillation ingredient is asserted without mixing. Candidate 3's Section 2 likewise gives its finite oscillation estimate for every invertible probability-preserving system and uses mixing later to identify the limit.

Lemma 2.5 explicitly claims the k=3 convergence case without mixing on standard invertible systems, relying on the companion analytic claims. Candidate 1's Section 2.1 explains encoding the integer translates of any fixed tuple into a compact metrizable shift factor; this removes standardness as a substantive obstacle on arbitrary invertible probability spaces. It would therefore be misleading to say that this release has no claim concerning the general triple problem. It supplies no all-k theorem for arbitrary nonmixing systems: in particular general k≥4 is not covered by these statements.

## Follow-ups and sources opened

1. [Repository README](https://github.com/openai/math/blob/main/README.md), [history](https://github.com/openai/math/blob/main/history.md), and each manuscript README were opened. The release describes varying verification status and warns of possible issues in unformalized outputs. No correction, withdrawal or revision naming these three papers appears in the opened history or their READMEs.
2. [Lean README](https://github.com/openai/math/blob/main/lean/README.md), [formalization catalogue](https://github.com/openai/math/blob/main/lean/formalization.yaml), [lean/docs directory](https://github.com/openai/math/tree/main/lean/docs), and [CONTENTS.md](https://github.com/openai/math/blob/main/CONTENTS.md) were opened. These manuscripts form repository family 154, distinct from our T083 numbering. There is no 154.md in that docs listing and no matching ergodic-average theorem in the formalization catalogue. No Lean proof of these three results was found. This does not assert that their dependencies are all unformalized.
3. Bogdan Grechuk, [*Mixing of All Orders and Pointwise Averages*](https://functor.network/user/3333/entry/2061), 10 November 2026, was opened. It is a named exposition of the OpenAI mixing and pointwise claims, not a referee report or independent full proof check. The page displayed no comments.
4. [*Mixing is enough?*, AI Proved What?](https://aiprovedwhat.com/episodes/154-pointwise-multiple-ergodic-mixing/), October 2026, was opened. It flags general triple Lemma 2.5 for expert review, and reports no Lean proof or expert review of the main result at its October 19 check. Its pointer to an issue report on the trilinear-Hilbert-transform dependency was followed; see item 9.
5. [Community distinct-slopes page](https://mathcommunity.github.io/oai-math-revised/papers/Triple-ergodic-averages-with-distinct-integer-slopes-October-4-2026/) was opened. It has no contributed notes and labels its automatically collected notes unreviewed. The [Plectis Atlas rendering](https://wcook04.github.io/plectis-atlas/papers/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026.html) was opened too; quotations above use original TeX.
6. [OpenVerification/OpenAIReview](https://openaireview.org/) was opened. Search results display issue flags for candidate 1; the site identifies these as AI-generated potential issues. The underlying report needs inspection before interpreting a flag as a mathematical objection.
7. Searches included exact titles, arXiv-restricted queries, and error/gap/refutation/review terms, as recorded in LOG.md. No matching arXiv version or named referee report was identified. This is a bounded negative search finding, not proof of absence. Repository metadata says issues and discussions are disabled.
8. The supplied folder URLs failed through the web tool, but connector directory and TeX reads succeeded. Raw PDFs returned unsupported application/octet-stream; quotations come from readable original TeX. The Latent Seminar page yielded no readable text and the AIProofWatch update failed to load; neither is used as an inspected proof review.

9. Opened OSVerify's [actual report on *An L³ bound for the trilinear Hilbert transform*](https://osverify.github.io/cases/trilinear-hilbert.html), reviewing OpenAI's October 5, 2026 version, and [OSVerify's project page](https://osverify.github.io/). It reports an omitted endpoint inclusion in Lemma 8.6, an incomplete predictor identity in Lemma 5.3, and a role-order convention mismatch. Each has a proposed repair; the endpoint condition is supplied in the application, and the report does not conclude that the main theorem is false. The project says its reported issues were checked by human experts. This is a specific error report on an analytic dependency, not a refutation or verification of the three ergodic-average papers. The report was read, but the analytic argument was not rechecked here.
10. Opened [lean/docs/145.md](https://github.com/openai/math/blob/main/lean/docs/145.md): it declares a Lean formalization of the companion multiple-mixing implication for measurable sets and links its Comparator challenge. This does not formalize the selected-length construction or triple oscillation bound used for pointwise convergence. In particular the invocation of multiple mixing is not by itself an established objection to the pointwise paper: the release supplies a companion claim and declared formalisation of that dependency.

## Recommended new “where it stands” sentence

The release does not claim the full pointwise convergence theorem on arbitrary probability-preserving systems for every k≥3. OpenAI's unrefereed *Pointwise Multiple Ergodic Averages for Mixing Transformations* (October 4, 2026) claims convergence for every finite k under mixing, and its Lemma 2.5 also claims general triple convergence using companion analytic estimates. Keep the full row marked open, with these partial claims noted; no matching Lean proof or independent full proof verification was found in this check.

## Spot check

Selected lemma: candidate 1, Lemma 2.5, “Triple pointwise convergence”. It supplies the one-, two- and three-slot marginals in the arbitrary-length argument, and is the part that claims progress on the unrestricted triple question. Checked its proof in the original inputs.tex, including the smooth convergence and approximation hypotheses in Proposition 2.2. The check below is conditional on those imported analytic assertions and the stated L² convergence input.

Write F_l=∏_{j=1}^3 g_j(S^{b_jl}x), with |F_l|≤1 after scaling; S=R^g removes a common divisor of the positive slopes. For rational c∈[1,2], let a=c2^m and N_m=⌊a⌋. The interval profile h_c=c^{-1}1_(0,c] gives

\[
2^{-m}\sum_{l\in\mathbb Z}h_c(l/2^m)F_l
=a^{-1}\sum_{l=1}^{N_m}F_l.
\]

Its difference from the ordinary average at N_m has absolute value at most (a−N_m)/a≤1/a. Subtracting the smooth sum with a fixed profile φ adds at most

\[
2^{-m}\sum_{l\in\mathbb Z}|h_c(l/2^m)-\varphi(l/2^m)|,
\]

which tends to ‖h_c−φ‖₁: the integrand is bounded, compactly supported and has only the interval endpoints as possible discontinuities. This verifies the paper's comparison including its floor error.

Choose countably many profiles with ‖h_c−φ_r‖₁→0 and intersect their convergence sets, for all rational c as well. On that conull set the limsup oscillation of ordinary averages at N_m is at most 2‖h_c−φ_r‖₁ for every r, hence zero. All these subsequential almost-everywhere limits equal the same L² limit of the ordinary averages: convergence in L² implies convergence in measure, identifying any almost-everywhere subsequential limit. This step does not require mixing or a constant limit.

For arbitrary |F_l|≤1 and M≥N, splitting the sums gives

\[
\left|\frac1M\sum_{l=1}^M F_l-\frac1N\sum_{l=1}^N F_l\right|
\le \frac{M-N}{M}+\frac{M-N}{M}
=\frac{2(M-N)}M.
\]

A finite rational grid of mesh δ in [1,2] approximates every N in [2^m,2^(m+1)) by M=⌊c2^m⌋ with |M−N|≤δ2^m+1. The last bound is at most 2δ+2^(1−m). Since the grid is finite and its subsequences have the same limit, first m→∞ and then δ→0 gives convergence along all integer lengths.

No defect was found in this elementary reduction. Its unresolved load lies in the imported smooth oscillation estimate and arbitrary-slope local-form extension. This limited check does not establish their correctness or that of any main theorem.


