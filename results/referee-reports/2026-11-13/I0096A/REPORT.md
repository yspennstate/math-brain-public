NO_PROGRESS

# I0096: deterministic critical-threshold phase retrieval

Work begun 13 November 2026, 18:56 Asia/Tbilisi. Task: “Open problem I0096”.

No proof or counterexample to Conjecture 20 was obtained. No printed resolution was found in the literature examined. The universal polynomial bounds recovered below are already known, so they are not being reported as a new partial solution. The Gaussian and subgaussian theorems answer a different, probabilistic question.

The literature search covered two public citation indexes, exact-conjecture searches, and targeted 2025–2026 work. It was not exhaustive: not every non-arXiv citing article was available in full text, and the published Liu–Wang article could not be downloaded. Its author-uploaded manuscript text was accessible. These access limits prevent an assertion that every citing paper has been obtained or that all literature has been excluded.

## Statement

Let (m>1), (n=2m-1), and let (A\in\mathbb R^{n\times m}) be full spark: every (m) rows span \(\mathbb R^m\). Write (a_i) for row (i) and (L=\max_i\|a_i\|_2). The conjecture asks for universal (C>0) and (0<\beta<1) such that

\[
\omega(A)\le CL\beta^m.
\]

Here

\[
\omega(A)=\min_{S\subseteq[n]:\operatorname{rank}(A_{S^c})<m}
                 \sigma_m(A_S)
             =\min_{|S|=m}\sigma_{\min}(A_S).
\]

For the last equality, full spark makes the rank condition equivalent to \(|S^c|\le m-1\). Every eligible set therefore has at least \(m\) rows. Removing rows decreases its Gram matrix in the positive-semidefinite order, so the minimum is achieved by an \(m\)-row set.

At this threshold \(\omega(A)\) is also the optimal lower Lipschitz constant of \(x\mapsto |Ax|\), with quotient metric \(\min(\|x-y\|_2,\|x+y\|_2)\). The underlying partition formula is Balan–Wang, Theorem 4.3, published pp. 479–480. These identifications should not be extended to other measurement counts without checking the definitions.

## Proofs and the remaining gap

There is no proof of the conjecture in this report. The following calculations explain what the proposed approaches did establish. Expanded proofs and the unsuccessful routes are in [ATTEMPTS.md](ATTEMPTS.md).

### The proposed volume-weighted average is exactly polynomial

For \(|T|=m-1\), set

\[
v_T=\det(A_TA_T^\top),\qquad
d(T,k)=\operatorname{dist}(a_k,\operatorname{span}\{a_j:j\in T\}),\quad k\notin T.
\]

The rows in \(T\) are independent. Evaluating \(A_{T\cup\{k\}}\) on a unit normal to their span proves

\[
\sigma_{\min}(A_{T\cup\{k\}})\le d(T,k).
\]

The Gram determinant identity gives

\[
v_Td(T,k)^2=\det(A_{T\cup\{k\}})^2.
\]

Let \(G=A^\top A\). Cauchy–Binet, including its coefficient of order \(m-1\), gives

\[
D:=\sum_{|S|=m}\det(A_S)^2=\det G,
\qquad
V:=\sum_{|T|=m-1}v_T=\det G\,\operatorname{tr}(G^{-1}).
\]

Choose \(T\) with probability \(v_T/V\), and then choose \(k\) uniformly from its \(m\)-element complement. Each \(m\)-subset occurs exactly \(m\) times in the sum over \((T,k)\). Consequently

\[
\mathbb E d(T,k)^2
=\frac{D}{V}
=\frac{1}{\operatorname{tr}(G^{-1})}
\le\frac{\operatorname{tr}G}{m^2}
\le\frac{(2m-1)L^2}{m^2}.
\]

This gives only \(\omega(A)\le L\sqrt{2m-1}/m\). For a unit-norm tight frame, \(G=((2m-1)/m)I\), and the displayed expectation is exactly \((2m-1)/m^2\). Thus this particular averaging argument does not acquire an exponential factor under tightness. It leaves open a different weighting, a tail estimate, or another extremal argument.

### Why the small-determinant argument stops

Writing \(K_m=\binom{2m-1}{m}\), one obtains

\[
\min_{|S|=m}|\det A_S|
\le L^m\left(\frac{((2m-1)/m)^m}{K_m}\right)^{1/2}.
\]

This determinant is exponentially small, with exponential base \(1/\sqrt2\). However,

\[
\sigma_{\min}(A_S)\le |\det A_S|^{1/m}
\]

removes that exponential gain. Dividing the determinant by the other singular values requires a lower bound for their product. Row-norm control gives an upper bound, which has the wrong direction for that step.

### An exact reformulation through circuit imbalance

Define

\[
\kappa(A)=\max_{|S|=m,\ j\notin S,\ i\in S}
              |(a_j A_S^{-1})_i|.
\]

By Cramer's rule, this is the largest ratio of neighboring maximal minors, equivalently the largest ratio of nonzero coefficients in a minimal dependence among \(m+1\) rows. It is invariant under invertible right multiplication of \(A\).

Two elementary bounds are

\[
\omega(A)\le\frac{L}{\kappa(A)},                                      \tag{1}
\]

and, for any Parseval representative \(B\), meaning \(B^\top B=I\),

\[
\omega(B)\ge
\frac{1}{\sqrt{m+m(m-1)\kappa(B)^2}}.                                \tag{2}
\]

For (1), choose a circuit realizing the largest coefficient ratio and omit a smallest coefficient. The retained coefficient vector has norm at least the largest coefficient, while its image under the square submatrix transpose has norm at most \(L\) times the omitted coefficient.

For (2), fix \(S\). The rows of \(BB_S^{-1}\) on \(S\) form the identity; all other \(m(m-1)\) entries have absolute value at most \(\kappa(B)\). Since \(B\) is an isometry,

\[
\|B_S^{-1}\|_{\mathrm{op}}\le\|B_S^{-1}\|_F
=\|BB_S^{-1}\|_F\le\sqrt{m+m(m-1)\kappa(B)^2}.
\]

Whitening preserves the circuits and gives \(\max_i\|b_i\|\le1\). Thus Conjecture 20 is equivalent, up to polynomial factors and a possible change of exponential base, to forcing exponentially large circuit imbalance in every real representation of the uniform matroid \(U_{m,2m-1}\). No such lower bound was proved here. This reformulation is not claimed as a new resolution or partial bound.

The recent circuit-imbalance literature was checked after this connection arose. Dadush et al., arXiv:2510.20301v1, Theorem 1.1, p. 3, gives \(n\le\pi d^4\kappa\); this is insufficient at \(n=2d-1\). Exponential imbalance for a particular LP family, as in Bondar–Vavasis, does not imply it for every uniform-matroid representation.

### Known polynomial bounds were reproduced, not improved

Balan–Wang's equation (5.1), published p. 483, proves \(\omega(A)\le L/\sqrt m\) using a dependence among \(m+1\) rows. A stronger \(O(Lm^{-3/2})\) bound for \(m+2\) rows is already Liu–Wang, Lemma 2.4, author manuscript pp. 4–5. It applies here for \(m\ge3\).

A self-contained derivation with explicit constant is in ATTEMPTS.md. Take an orthonormal basis of the two-dimensional transpose kernel of any \((m+2)\)-row submatrix. At least half its row vectors have norm at most \(2/\sqrt{m+2}\). Two of their unoriented lines have angle at most \(\pi/\lceil(m+2)/2\rceil\). The corresponding small two-row singular value and the kernel relation give, for example,

\[
\omega(A)\le
4\pi\sqrt{5/3}\,\frac{L}{(m+2)^{3/2}},\qquad m\ge3.
\]

Because this order of decay is already in print, it does not qualify as a new `PARTIAL` result.

### Other attempted routes

Projection along one row preserves full spark after discarding an additional row and gives \(\omega(A)\le\omega(B)\) in dimension \(m-1\). It supplies no dimension-independent contraction in the projected maximum row norm.

The real three-term Plücker relation shows that neighboring minors cannot all have the same absolute magnitude. It forces a constant local separation. No argument was found that validly multiplies these local separations into an exponential ratio.

The harmonic candidates have an elementary exponential test-vector bound, proved in ATTEMPTS.md. This is a structured example; exponential Fourier/Vandermonde ill-conditioning is already established in the literature. No new exponential theorem for all unit-norm tight frames or all globally well-conditioned frames was obtained.

## Numerical search

Every candidate listed in the table was evaluated on all \(K_m\) square row submatrices. “All” refers to subset enumeration; singular values were evaluated in floating point, not exact arithmetic. Neither a global optimizer nor a rigorous certificate of the maximum over all matrices was computed.

Initial candidates were real unit-norm tight harmonic frames, row-normalized equispaced Vandermonde frames, three row-normalized Gaussian samples, three scaled Haar/QR samples, two orthonormal bases, and a simplex plus extra rows, for every \(2\le m\le12\). Additional candidates were truncated Paley conference frames, random projections/deletions of them, and projections from conference matrices of orders 30, 38, and 42. The order-10 conference candidate was numerically singular and was not treated as a full-spark example.

SLSQP maximized an epigraph variable subject to all square-submatrix singular-value constraints and unit row norms. Multiple starts were used through \(m=6\), with additional searches through \(m=9\) from the better Paley candidates. Results were normalized and independently reevaluated after optimization. All row norms in the table are at most 1 up to rounding.

| \(m\) | Subsets per candidate | Best \(\omega\) found | \(\omega^{1/m}\) | Best candidate |
|---:|---:|---:|---:|---|
| 2 | 3 | 0.7071067812 | 0.840896 | harmonic; known planar optimum |
| 3 | 10 | 0.3585701736 | 0.710436 | numerical optimization |
| 4 | 35 | 0.1597107461 | 0.632169 | numerical optimization |
| 5 | 126 | 0.08945174365 | 0.617046 | optimized projected Paley |
| 6 | 462 | 0.06305326388 | 0.630887 | optimized projected Paley |
| 7 | 1,716 | 0.05408100132 | 0.659184 | optimized truncated Paley |
| 8 | 6,435 | 0.01436522847 | 0.588388 | optimized projected Paley |
| 9 | 24,310 | 0.01350432875 | 0.619833 | truncated Paley, \(q=17\) |
| 10 | 92,378 | 0.0002542537643 | 0.437046 | harmonic |
| 11 | 352,716 | 0.00008374512277 | 0.425951 | harmonic |
| 12 | 1,352,078 | 0.00007371933722 | 0.452514 | projected Paley, \(q=29\) |

A descriptive fit of \(\log\omega\) against \(m\) for \(m=2,\ldots,9\) has slope \(-0.564192\), or fitted base \(0.568820\). Across \(m=2,\ldots,12\) the fitted base is \(0.388925\). The sharp change at \(m=10\), and the dependence on which structured candidates were available, make these unreliable estimates of the true extremal growth rate. They establish neither exponential decay of the supremum nor a subexponential counterexample family. In particular, a lower bound from a finite candidate search is not an upper bound on the worst case.

The saved records contain 160 candidates/refinements and 23,777,666 square-subset evaluations at the recorded final-candidate stage, excluding optimization iterations and unrecorded unsuccessful projection trials. Data, full-precision matrices, minimizing witnesses, and fit parameters are in [data/best.csv](data/best.csv), [data/numerics.jsonl](data/numerics.jsonl), and [data/fits.json](data/fits.json).

## Verification and resource use

- All best matrices for \(m=2,\ldots,12\) were fully enumerated again after QR factorization, then evaluated by SVD. The largest difference from the original direct-SVD minima was \(1.13\times10^{-16}\). This is numerical cross-checking, not interval certification.
- Each recorded minimizing witness was also checked using SciPy's `gesvd` driver and a singular-vector residual. Independent scalar-loop enumeration was used for the best small cases.
- The weighted-distance identity, both Cauchy–Binet sums, harmonic tightness, local Plücker relations, and the circuit-imbalance inequalities were checked in dimensions 2–7 against independently computed quantities. Maximum relative Cauchy–Binet error was \(1.56\times10^{-15}\).
- Conference identities were checked with exact integer matrix multiplication. Some bounded-input Accelerate matrix multiplies emitted floating-point warnings; finite outputs and the complete QR/SVD audit were checked rather than assuming those warnings harmless.
- Computations used batches of 2,048 matrices, one configured BLAS thread, and no worker pool. The inherited process priority was nice 20; the sandbox would not permit raising it to nice 10. The independent full audit peaked at 158,810,112 bytes RSS, about 152 MiB. The largest optimization problem was \(m=9\), with 24,310 subset constraints; its batched arrays were well below 4 GB. No more than two numerical processes ran simultaneously.
- The initial enumeration timing field was recorded before evaluation. Those fields are marked unusable; the original values remain in `data/numerics_original_timing.jsonl`. The independent audit has valid timings. No conclusions use the faulty timing fields.

For a fresh rerun, use the following order (existing recorded stages are skipped by the main enumeration/optimization script):

```sh
python3 code/numerics.py enumerate
I0096_OPT_MAX_M=7 python3 code/numerics.py optimize
I0096_OPT_MAX_M=8 python3 code/numerics.py optimize
python3 code/verify_identities.py paley
python3 code/paley_search.py
python3 code/paley_large.py
I0096_OPT_ROUND=1 python3 code/numerics.py optimize
python3 code/numerics.py summarize
python3 code/verify_identities.py
python3 code/final_audit.py
```

Candidate matrices and seeds preserve the completed run. Optimization can vary slightly with LAPACK and solver versions.

## Literature results and locators

Page numbers below refer to the explicitly named version. PDF page numbers in saved preprints are separated by `===== PDF PAGE k =====`. No PDF or paper image was retained.

| Source | Verified result and pages | Relation to this problem |
|---|---|---|
| [Bandeira et al., arXiv:2603.29571v1](https://arxiv.org/abs/2603.29571v1) | Entry 10; Definition 10.1, Conjecture 20, Open Problem 21, p. 7 | Distinguishes the universal conjecture from the Gaussian question. |
| [Balan–Wang, ACHA 38 (2015), 469–488](https://doi.org/10.1016/j.acha.2014.07.003); [arXiv:1308.4718v1](https://arxiv.org/abs/1308.4718v1) | Published Theorem 4.3, pp. 479–480; equation (5.1), p. 483; Conjecture 5.1, p. 484. Preprint Theorem 4.3, pp. 12–13; Conjecture 5.1, p. 16. | Exact lower Lipschitz formula and known polynomial bound. The preprint's negative exponent in the conjecture is a typo corrected in print. |
| [the author, arXiv:2607.06249v1](https://arxiv.org/abs/2607.06249v1) | Theorem 1.1, p. 2; Corollary 1.2, p. 4 | \(\omega(A)=4^{-m+o_P(m)}\) for Gaussian matrices. Does not bound every deterministic matrix. |
| [Häggblom, arXiv:2609.28198v1](https://arxiv.org/abs/2609.28198v1) | Theorem 2, pp. 5–6; Theorem 4, pp. 23–24; Corollary 2, p. 24 | Critical reduction and Gaussian scale \(1/(\sqrt m K_m)\), up to arbitrary diverging subexponential factors. |
| [Yang–Wen–the author, arXiv:2608.07410v1](https://arxiv.org/abs/2608.07410v1) | Theorem 1.1, pp. 2–3; Proposition 1.3 and Corollary 1.4, p. 4 | Bounded-density subgaussian extension, with critical base \(1/4\). |
| [Wen–Häggblom–Yang, arXiv:2611.06736v1](https://arxiv.org/abs/2611.06736v1) | Theorem 1.1, p. 3; Theorem 1.3, p. 4; Theorem 6.4 and Corollary 6.5, pp. 25–26 | November 2026 random surplus-row universality theorem; not a worst-case deterministic result. |
| [Liu–Wang, AEJM 9(4) (2016), 1650075](https://doi.org/10.1142/S1793557116500753) | Author manuscript Lemma 2.2, p. 3; Lemma 2.4, pp. 4–5; kernel-duality Lemma 3.1 in §3 | Known \(m^{-1/2}\) and \(m^{-3/2}\) bounds. **Journal theorem/page correspondence unavailable**; these are manuscript locators from the author-uploaded text. |
| [Liu, Operators and Matrices 18 (2024), 273–293](https://doi.org/10.7153/oam-2024-18-17) | Theorem 2.3, pp. 277–280; Theorem 2.7, pp. 284–286; Lemma 3.1, p. 287 | Sharp simplex and planar extremal results; also shows why equiangularity alone does not ensure good subframes. |
| [Xu, arXiv:2508.10452v1](https://arxiv.org/abs/2508.10452v1) | Theorem 1.1, p. 2; Corollary 1.1, p. 3 | Restricted-invertibility/best-submatrix lower bounds. The required extremum here is the worst submatrix. |
| [Xu–Xu–Zhang, arXiv:2510.04099v3](https://arxiv.org/abs/2510.04099v3) | Theorem 1.1, p. 2; Theorem 1.2, p. 3 | Optimal amplitude-map condition numbers in dimension 2; does not treat growing \(m\) at \(2m-1\) rows. |
| [Shah–Urschel, arXiv:2604.15135v3](https://arxiv.org/abs/2604.15135v3) | Theorem 1.1 and Corollary 1.2, p. 2; Theorem 1.5, p. 5 | Sharp exponential conditioning rates for structured Fourier/Vandermonde matrices, not arbitrary frames. |
| [Dadush et al., arXiv:2510.20301v1](https://arxiv.org/abs/2510.20301v1) | Theorem 1.1 and Lemma 1.2, p. 3; Theorem 1.5, p. 4 | Circuit imbalance and excluded uniform rank-two minors; no exponential lower bound in the target regime. |
| [Balan–Zou, LAA 496 (2016), 152–181](https://doi.org/10.1016/j.laa.2015.12.029) | Theorem 2.1, p. 158 | Recalls the exact real amplitude lower Lipschitz formula; other results concern extensions and complex/intensity maps. |
| [Freeman–Haider, arXiv:2502.09898](https://arxiv.org/abs/2502.09898) | Theorem 3.10, p. 19; Corollary 3.11, p. 20 | Strong-complement-property Lipschitz estimates; no universal exponential upper bound. |
| [Bandeira–Cahill–Mixon–Nelson, arXiv:1302.4618v3](https://arxiv.org/abs/1302.4618v3) | Theorem 18, pp. 12–13; Theorem 20, pp. 14–15 | Strong complement property and random stability background. Predates Balan–Wang. |
| [Rademacher–Shu, arXiv:2009.12685](https://arxiv.org/abs/2009.12685) | Theorem 1.4, p. 4 | Earlier Gaussian exponential submatrix instability, not universal deterministic instability. |
| [Alexeev–Cahill–Mixon, arXiv:1110.3548](https://arxiv.org/abs/1110.3548) | Theorem 4, p. 8; Theorem 6, p. 9; Theorem 15, p. 18 | Harmonic full-spark constructions and density of full-spark Parseval frames. Qualitative full spark supplies no quantitative lower bound. |
| [Needham–Shonkwiler, arXiv:2110.11295](https://arxiv.org/abs/2110.11295) | Theorem 1.1, p. 3 | Almost-sure full spark with prescribed norm/spectral data in the complex frame-space setting; not the claimed quantitative real upper bound. |

The extended audit is in [LITERATURE.md](LITERATURE.md). Public indexes returned 75 OpenAlex records and 90 Semantic Scholar records, giving 94 distinct normalized titles; all were retained in [data/citation_screen.csv](data/citation_screen.csv). There are 57 source text/access-note files, about 3.35 MB. Indexed phase-retrieval papers with available arXiv identifiers were retrieved as text and screened for critical-count, exponential-bound, and stability statements. The inventory distinguishes retrieved texts from title/abstract screening. Unavailable non-arXiv texts remain a coverage limitation.

The Gaussian theorem does impose one necessary restriction on a possible universal answer: a fixed universal base smaller than \(1/4\) is impossible, because the maximum Gaussian row norm is subexponential in dimension. It does not determine the worst-case base.

Perturbation results, infinite-dimensional instability, local-correlation/Gabor instability, intensity-map condition numbers, and generalized matrix-frame results do not by themselves answer the stated amplitude-map worst case. The 2025 Phasebook survey and the cited 2025–2026 construction/selection papers were also checked. No retrieved theorem proves or refutes Conjecture 20.

## What remains

A proof still needs a uniform exponential mechanism beyond the displayed averages, or an exponential circuit-imbalance lower bound for every real \(U_{m,2m-1}\) representation. A counterexample needs a dimension-growing full-spark family with a proved \(\exp(-o(m))L\) lower bound on every square subframe. The finite Paley and optimized examples provide neither.

All work and outputs stayed in this directory. Nothing was published or pushed.
