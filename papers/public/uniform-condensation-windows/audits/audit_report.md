---
title: "Five-pass audit record"
subtitle: "Uniform condensation windows for zero-radius random allocations"
author: "Review documentation for Yitzchak Shmalo"
date: "17 September 2026"
fontsize: 10pt
geometry: margin=24mm
---

# Five-pass audit record

**Paper:** Uniform condensation windows for zero-radius random allocations  
**Author:** Yitzchak Shmalo  
**Date:** 17 September 2026  
**Reviewed LaTeX SHA-256:** `b880e42a5bc57f834fe95f96330e57ed04f15bf21fc09edb6098d227d5c1442e`

Five sequential, separately documented review passes were completed by the same assistant. All identified manuscript corrections were applied. No remaining mathematical gap was identified. These are not independent referee reports or formal verification. Publication novelty remains unverified.

| Pass | Scope | Disposition |
|---|---|---|
| 1 | Source scope, versions, attribution | Passed after citation corrections; novelty unresolved |
| 2 | Finite insertion and residual inequalities | Passed rederivation and exact stress checks |
| 3 | Record summation and uniform asymptotics | No unresolved step identified |
| 4 | Path, sampling and tree consequences | Passed with quantifiers and known inputs explicit |
| 5 | Reproduction, declarations, typesetting | Passed after final preflight |

The main edits were the journal/preprint reference correction, explicit finite-lemma domains and factorial conventions, an explicit root-error bound, and accurate authorship/funding/AI declarations. The first four passes review the mathematical argument; the fifth verifies that the delivered files faithfully represent it.


\newpage

# Audit 1: source scope, hypotheses, and attribution

**Outcome: scope check passed after bibliographic corrections. Publication novelty remains unverified.**

This is the first of five separate review passes by the same assistant. It is not an independent referee report. The reviewed claim is Theorem 2.1 and Corollary 2.2, not the neighboring positive-boundary-mean problem.

## Source question and version control

The zero-radius question is Problem 19.41 on page 228 of the published survey, and Problem 18.40 on page 122 of the December 2011 preprint. The neighboring positive-mean question is 19.40 in the journal and 18.39 in the preprint. The prior draft mixed the journal bibliographic entry with preprint locators. The final manuscript now gives separate references for the journal article and preprint and explicitly identifies both question numbers. The root identity is cited to the preprint's Lemma 14.7 rather than attaching that locator ambiguously to the journal entry.

The original arXiv PDF was read and its question page visually inspected. The journal numbering was cross-checked against a reproduction of the published text. Direct publisher PDF retrieval did not succeed during this pass. This access limitation does not concern the directly inspected preprint question, but it is recorded rather than described as a successful publisher-PDF check.

Primary source: S. Janson, *Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation*, Probability Surveys 9 (2012), 103--252, doi:10.1214/11-PS188; arXiv:1112.0510v1. The related paper by Janson, Jonsson and Stefansson, arXiv:1104.2810, was checked for its actual theorem scope: its ratio-growth local-limit theorem and explicit factorial-family results do not have the general hypotheses of the current theorem. Its branching-weight indexing differs from allocation outdegree indexing; no factorial constant is transferred without that shift.

## Logical comparison with the problem

The weights are one fixed sequence of finite nonnegative numbers, with positive constant term and zero radius. The mass path is prescribed, with eventual admissibility and positive finite limiting density. There is no regularity requirement on its increments. These assumptions are retained, not strengthened to full support or ratio growth.

The claimed subsequence conclusion $Y_{(1)}/m\to1$ implies $Y_{(1)}/n\to\lambda>0$ on that subsequence. This contradicts full-sequence convergence to zero and therefore answers the entire zero-radius question, provided the argument is correct. A subsequence conclusion is sufficient for the source question; it is not a scope defect. By contrast, the argument neither proves condensation at every size nor proves literal concentration on one occupied box.

The identification of the source's nontrivial $\nu=0$ regime with zero radius was checked directly: if the radius were positive and any positive index had positive weight, the logarithmic-derivative mean at a positive argument would already be positive. A sequence supported only at zero cannot support the stated positive-density path.

## Attribution and remaining limitations

The cyclic lemma and size-biased root identity are identified as known. The source's sparse-factorial example is used only to explain why a full-sequence near-total result would be false. The manuscript does not claim to settle the positive-mean question, establish a rate uniform in the weights, or prove a universal result on an arbitrarily lacunary sampled set.

Bounded current-literature searches were conducted, but the returned material did not establish publication priority. The paper must not be announced as a independently verified new resolution on that basis. The author's affiliation, email, general funding wording, and competing-interest declaration were recovered from his existing repository manuscripts; the applicability of individual grants to a submission remains an author responsibility. No personal mathematical contributor or discussion was invented.


\newpage

# Audit 2: insertion, multiplicities, and supported residuals

**Outcome: finite arguments passed rederivation and exact stress tests.**

This pass rederived the finite comparisons without relying on numerical agreement alone. The sharper insertion lemma permits total mass $m\ge2k$; its images contain exactly one size-$k$ box by construction, not because the total excludes two such boxes.

## Occupation-count calculation

For a positive-weight background with counts $a_j$, insert the giant and a fixed list of residual pieces into empty coordinates. With $Q=1+\sum_j r_j$, the image satisfies $b_0=a_0-Q$, $b_k=1$, and $b_j=a_j+r_j$ for $0<j<k$. This map on count vectors is injective. Its permutation-weight ratio, after normalization $w_0=1$, is

$$
w_k W_r\frac{(a_0)_{\underline Q}}
 {\prod_j(a_j+r_j)_{\underline{r_j}}}.
$$

Every background has $a_0\ge n-t$, while every image has $b_j\le\min(n,\lfloor m/j\rfloor)$. Monotonicity of the nonnegative falling factorial in its first integer argument yields the sharp bound in Lemma 3.1. The denominator is positive: the fixed residual list and $Q\le n$ guarantee that each multiplicity fits its occupancy upper bound.

The coarse bound was checked separately. If $t+Q\le n/2$, every numerator factor is at least $n/2$. Each factor corresponding to a large piece is at most $m/K$, and each terminal-piece factor is at most $n$. This produces $n2^{-(C+1)}(nK/(2m))^R$. The condition $nK\ge2m$ makes the last factor at least one. A size may occur in both roles; assigning its factorial factors to the two roles in a fixed order preserves both upper bounds.

An independent counting *method*, not an independent reviewer, was also used: enumerate ordered choices of empty labelled coordinates. A target has one giant location and at most the displayed product of falling-factorial residual choices. Deleting those choices may produce an invalid background, which only lowers the inverse multiplicity and cannot invalidate the upper bound.

## Supported residual construction

A finite subset of the positive support has the same gcd as the full support. After dividing by this gcd, the nonnegative semigroup of that finite subset contains all sufficiently large integers. The finite terminal representations therefore exist without assuming $w_1>0$.

At a greedy stage, $s_i\le a^i\le x/2$ and $h_*\le a^i$. Hence $q=\lfloor(x-h_*)/s_i\rfloor\ge1$. The new residual lies in $[h_*,h_*+s_i)$, so it is strictly below $2a^i$; the geometric index strictly decreases. The terminal set is finite, all terminal weights are positive, and its cost bound is fixed before the large-scale limit. The manuscript makes the nonnegative integer domain, empty-product convention, and zero-order falling factorial explicit.

## Executed checks

The new standalone stress checker tested 18,000 exact count-vector comparisons, including 14,862 cases with $m\ge2k$. Of these, 13,240 met the coarse-bound conditions, including 1,573 with the same residual size in both roles. Equality occurred in the sharp-bound comparison, so the checks do include boundary cases rather than only generous slack.

Three fully labelled examples enumerated 2,100, 11,760, and 45,360 insertion records. Their inverse multiplicities and image counts obey the sharp double-counting bound. The earlier 12 occupation-count examples and 391 supported greedy energy checks were also rerun. All final assertions passed with integer or rational arithmetic. These tests support the finite derivations; they do not establish the asymptotic theorem by computation.


\newpage

# Audit 3: record sums, margins, and the uniform limit

**Outcome: no unresolved step identified in the asymptotic argument.**

This pass rederived the deterministic summations and followed all constants through the probability estimate. It was performed by the same assistant as the other passes and is not independent certification.

## Record envelope and plateaus

Zero radius implies that the corrected slopes $(\log w_s+b\log s)/s$ are unbounded. Their geometric prefix maxima $B_i$ therefore increase without bound, and the least maximizing supported sizes $s_i$ tend to infinity. At an active scale $J$, $a^{J-1}<s_J\le a^J$. On an inactive scale the least maximizer cannot change: any newly available tied index is larger than the previous least maximizer. Thus the penalty $p_i=b\log(s_i)/s_i$ really is constant on each plateau.

For a plateau beginning at $\ell$ and ending just before the next active scale $v$, only active $J\ge v$ can receive a charge from that plateau. Bounding their total by

$$
p_\ell\left(\sum_{i=\ell}^{v-1}a^i\right)
\left(\sum_{J=v}^{\infty}a^{-J}\right)
\le \frac{a}{(a-1)^2}p_\ell
$$

is valid even for arbitrarily long plateaus. At active $\ell$, the bound $p_\ell\le ba\ell(\log a)a^{-\ell}$ is summable. The initial plateau contributes one finite term. Charging at all scales instead of active scales would lose this reasoning; the manuscript retains the active-scale restriction.

## Kernel and finite prefix

Expanding $B_{J-1}-B_i$ into nonnegative increments allows rearrangement. At lag $t=J-\ell$, the coefficient of one increment before multiplication by $2a^2$ is $a^{1-D}/(a-1)$ for $1\le t\le D-1$, and $a^{-t}/(a-1)$ for $t\ge D$. Summing gives exactly the manuscript's $\Theta(a,D)$, which tends to zero as $D$ grows for each fixed $a>1$.

The terminal term is not discarded. Beyond a fixed $J_0$, its contribution from later increments is at most $\kappa\sum d_\ell$, with $\kappa=Ma^{1-J_0}/(a-1)$. The earlier increments contribute only a fixed finite constant. Choosing $D$ first and $J_0$ later makes both coefficients less than $1/4$. This forces bounded record growth if the favorable margins were eventually bounded above, contradicting zero radius.

The finite-prefix inequality was also rederived from $G_J/s_J=d_J-(b\log s_J+E_J)/s_J$. The negative margins are retained in the weighted sum; they are not silently dropped. The error terms have the displayed geometric upper bounds. Bounding the positive maximum using the finite total $\sum s_J^{-1}\le T_{J_0}$ gives the stated quantitative consequence.

## Uniform probability estimate

The auxiliary probabilities use only sizes up to the preceding record cutoff. The bound $q_j\le j^{-b}$ and $b>2$ supply a summable first-moment majorant. For each fixed positive $j$, $w_j e^{-B_{J-1}j}$ tends to zero, so the auxiliary mean tends to zero by dominated convergence. No asymptotic equivalence of the original and truncated models is assumed.

The upper density and lower density bounds ensure that all relevant box counts are of order $k$, uniformly. A Markov bound and a finite pigeonhole argument select a background mass $t\le\delta k$ with probability at least $1/(2(\lfloor\delta k\rfloor+1))$. The exact residual satisfies $2\delta k\le r\le5\delta k$ and is represented by the greedy construction. The insertion conditions are guaranteed by the explicitly fixed $K$ and $\delta$.

Both the numerator upper bound and the inserted denominator contain the *same* factor $A_J^n$. They cancel exactly. The leftover prefactor is bounded by the displayed constant independent of both $m$ and $n$ in the window. The entire failure probability is therefore bounded by $Ce^{-G_J}$. Selecting margins tending to infinity proves the uniform theorem. The gcd reduction preserves the ratio of maximum to total and rescales the density interval correctly.

## Quantifiers and tests

The order is: fix the law, accuracy and density interval; then fix $a,b,D,\delta,K$ and the finite terminal data; only then select record scales. The final diagonal selection over accuracies is separate. No law varies with the selected size, and no almost-sure assertion is inferred from convergence in probability.

All 412 prior finite-prefix inequalities were reproduced. The new checker verified 84 exact geometric and tail identities, including bases $101/100$ and lag boundaries $D=2,3,11$. The prior long-plateau and convolution tests also passed. No numerical tail truncation is used to justify an infinite sum.


\newpage

# Audit 4: path quantifiers, tree roots, and sampling sharpness

**Outcome: the stated consequences passed review; their scope remains explicit.**

## Full and sampled paths

For a prescribed full path, the chosen scale $k$ determines a prospective index near $(1+4\delta)k/\lambda$. The assumption $m_n/n\to\lambda$ alone puts the resulting pair into the mass window. No hitting argument, bounded upward increment, or monotonicity of the path is needed.

For a sampled set with successive-index ratio tending to one, its first point above this prospective index is asymptotically at the same location. This justifies the dense-sampling extension. It does not apply to every arbitrary subsequence. A further thinning can make selected indices strictly increasing, because the prospective indices tend to infinity.

The whole-interval consequence is also valid. The path error $m_n-\lambda n=o(n)$ is uniformly small over every sufficiently remote interval whose endpoints are fixed multiples of $k$. The narrower interval in equation (31) leaves positive margin inside the mass slab. Its cardinality is asymptotic to $\delta k/\lambda$. The paper does not claim a density of such intervals among all integers or a law-uniform convergence rate.

Expectation convergence follows from the deterministic bound $0\le Y_{(1)}/m_n\le1$, and the second-largest-box bound follows from $Y_{(2)}\le m_n-Y_{(1)}$. These arguments do not need an additional uniform-integrability hypothesis.

## Allocation-to-tree transfer and the root

For total degree $n-1$, the cyclic lemma identifies the allocation degree-count law with the simply generated tree degree-count law. Rotation preserves the product weight and the maximum. A nontrivial period cannot occur for the full degree sequence because the sum of degree-minus-one increments is $-1$.

Conditioned on the degree counts $A_j$, the number of plane trees is $(n-1)!/\prod_jA_j!$. Removing a root of degree $j$ leaves an ordered forest of $j$ trees, giving $j(n-2)!/((A_j-1)!\prod_{i\ne j}A_i!)$ possibilities. Their ratio is $jA_j/(n-1)$. This is the known size-biased root identity, not a new identity. The final paper explicitly takes $n\ge2$ before using its denominator and cites the correct preprint locator.

On the event that the maximum degree exceeds $(n-1)/2$, it is unique. Its conditional probability of occurring at the root is $D/(n-1)$. The final manuscript includes the error bound

$$
\Pr(D\le(n-1)/2)+\mathbb E[1-D/(n-1)],
$$

which tends to zero on the condensation subsequence. The number of vertices at depth at least two is exactly $n-1-d^+(o)$, giving the final geometric consequence. The independent calculation method in the new checker enumerated 23,713 plane trees of sizes 2 through 11 and verified 422 root identities across 138 degree-count classes. This is not a new independent reviewer.

## Necessity of the sampling criterion

When infinitely many sampled gaps have ratio at least $\theta>1$, the constructed support consists of zero, one, and their left endpoints. The weights at large supported values are $e^{k^2}$, so they form one fixed zero-radius sequence. The path $m_n=n-1$ is admissible via zeros and ones.

A supported left endpoint $k$ is unavailable at $n=k$ because the total is $n-1$. At any later sampled index it satisfies $n\ge\theta k$. Hence every configuration has maximum at most $\max(1,n/\theta)$, ruling out near-total condensation on that sampled set. With unbounded gap ratios, the same argument separates a finite initial support from later points and forces a deterministic vanishing maximum fraction.

This disproves universality when the sampling condition fails; it does not say that every individual law fails. The deterministic powers-of-two, factorial, and irregular-gap tests were rerun, including equality at the gap threshold. The published source's sparse-support examples remain consistent with both directions.


\newpage

# Audit 5: reproducibility, declarations, and document delivery

**Outcome: computational reproduction and manuscript preflight passed.**

## Reproduction

The two earlier exact checkers were copied without modification from their verified repository blobs. The bundled loader checks the predecessor script's SHA-256 before executing it. The uniform-window output reproduced the saved prior output byte-for-byte. A second run of the new stress checker reproduced its output byte-for-byte as well. Python was run without optimization, so its assertion checks were active.

The explicit finite law used for the window illustration is fixed: below mass 120 its positive support is $\{2,3,5,17\}$ with weights $2^{j^2}$ and $w_0=1$, and factorial support points from $5!$ onward extend it to zero radius. All 97 pairs with $20\le m\le22$ and $1/2\le m/n\le2$ are covered. The sharp upper bound is at most $2^{-189}$; the actual worst probability and both insertion bounds agree with the manuscript's rounded table. Span-three checks reproduce the relevant coefficients exactly.

No finite scan is used as a proof of zero radius, the existence of infinitely many favorable records, or an asymptotic limit. The code documentation, manuscript declaration, and review reports all retain this distinction.

## Manuscript and attribution

The final manuscript contains the author's name, Einstein Institute of Mathematics / Hebrew University affiliation, verified correspondence email, standard funding acknowledgement, competing-interest disclosure, and an AI-use declaration adapted to what actually occurred. It does not copy the previous paper's claims about Claude reviewers, Lean formalization, or human approval. No person is thanked for a contribution or discussion that was not established.

The five review passes are explicitly described as work by the same assistant. They are not five independent votes, and no source-resolution registry was promoted on their basis. The grants and competing-interest text match the author's recent standard declaration; independent confirmation of grant applicability was not performed.

## Build and rendering

The article was compiled twice with pdfLaTeX. Its metadata identifies the title and Yitzchak Shmalo. Preflight found 53 unique labels, 52 reference uses, three bibliographic keys, no undefined references, no LaTeX warnings, no overfull boxes, and no text blocks outside the page bounds. It is 11 pages in A4 format. All pages were rendered to images for layout review, with additional full-size inspection of the title page, a proof-heavy page, and the declarations/reference page.

An initial text-extraction assertion looked for mixed-case author text, while the AMS class renders the title author in small capitals. The assertion was made case-insensitive and rerun; the typeset author's name and PDF metadata were already correct. This was a test-harness issue, not a mathematical or author-name correction.

## Package boundary and remaining review

The package includes the paper PDF, root LaTeX source, three standard-library Python checkers, both saved result files, the five reports, and build instructions. Intermediate TeX build files and rendered page images are excluded from the delivered archive. Repository delivery contains the textual source, reports, and runnable checks; the compiled PDFs are also delivered directly and by email.

No unresolved mathematical gap was identified in these five passes. That conclusion remains a self-review assessment. Independent expert review, an exhaustive prior-art assessment, author approval of the final declarations, and any journal refereeing are separate future steps. The manuscript is therefore delivered as a complete research draft, not as an independently certified resolution.


