MINOR

The advertised PARTIAL claim is mathematically correct. I found no defect in its GOE exponential limit, its lower-extreme Poisson process, its factorial-moment criterion, or its planted-coordinate obstruction. The normalization is $n^{3/2}$, and the exponential parameter is the rate $c=\sqrt{2/\pi}$, so the limiting mean is $\sqrt{\pi/2}$. The GOE argument works for every deterministic ordered index sequence, including both edges.

This does not solve E0098. The GOE result is an elementary consequence of classical Gaussian extreme-value theory; the conditional Poisson criterion is standard. The obstruction is a useful explanation of why qualitative Gaussian marginals do not settle a minimum. It provides no Wigner counterexample and does not establish that all existing methods fail. My independent literature search through 13 November 2026 found neither a proof of the stated minimum law for general fixed subgaussian Wigner atoms nor an admissible atom-dependent limiting law. That is a bounded search conclusion, not a theorem about the nonexistence of other work.

Errors, omissions, and scope corrections follow. Locations refer to the supplied [claim report](claim_files/REPORT.md), with its line numbers pinned by the artifact hashes in [data/claim_snapshot.json](data/claim_snapshot.json).

1. Prior art is incomplete at “Proof 1,” lines 67–117. The spherical Gaussian representation is cited, but the classical extreme-value/Poisson argument is not. Add Resnick, *Extreme Values, Regular Variation and Point Processes* (1987), Proposition 3.21, p. 154, for the iid point-process principle, and Rivin, *A Note on Spheres and Minima*, arXiv:math/0305252 (2003), pp. 2–4, for the same spherical minimum and its expected asymptotic. Rivin does not explicitly state the full normalized spherical exponential or Poisson limit. The appropriate description is a classical consequence proved here for completeness, with no claim of a new GOE phenomenon.

2. The literature table, lines 43–63, omits the requested Luh–O’Rourke and Nguyen–Tao–Vu checks. Add Luh–O’Rourke, arXiv:1810.00489v2, Theorems 2.4–2.5, and Nguyen–Tao–Vu, arXiv:1504.00396v2, Theorem 3.3. The former concerns independent-entry, non-Hermitian matrices; the latter gives polynomial-scale nondegeneration, including shifted Wigner matrices. Neither supplies the minimum’s exponential law. Their omission does not invalidate the report’s conclusion; the relevant checks are supplied below.

3. The obstruction’s relation to the “strongest known” Gaussian approximations needs a precise scope statement at lines 184–255 and in the opening paragraph. Its total-variation convergence for every deterministic $o(n)$-coordinate set is a strong hypothetical coordinate-marginal property. It is not literally the hypotheses or conclusions of all the cited theorems, which also involve projections, several eigenvectors, quantitative smooth tests, or quadratic forms. In particular, a finitely supported Wigner ensemble has finitely supported selected eigenvectors under a deterministic selection rule, so even a single signed coordinate has total-variation distance one from a continuous Gaussian, at every finite $n$. Add this distinction. The construction validly refutes the implication actually stated about random unit vectors; it does not refute an implication from all Wigner structure and every known estimate together.

4. “The missing input is a relative small-ball estimate,” line 3, should say “one sufficient missing input is joint relative small-ball asymptotics.” A one-coordinate estimate alone is insufficient; correlations matter. The report’s equations (6)–(7) correctly specify the joint condition. Conversely, that condition is not necessary for an exponential minimum: convergence of void probabilities alone could establish the minimum without proving Poisson count convergence. This is an exposition correction, not a gap in Proof 2.

5. The sign-switching sentence at line 302 is imprecise: “after fixing the first diagonal sign to +1” refers to the first sign of the conjugating matrix $D=\operatorname{diag}(d_i)$, namely $d_1=1$. It cannot refer to $W_{11}$, which conjugation $W\mapsto DWD$ preserves. Replace that phrase accordingly. The multiplicity $2^{n-1}$ and the tabulated counts are correct.

6. The Lévy-matrix row at line 57 suppresses qualifications in the cited Theorems 2.9–2.10 of Aggarwal–Lopatto–Marcinek: the displayed entry limits require $\alpha\in(0,2)\setminus\mathcal A$, for a countable exceptional set, and energies in a specified interval around zero. Add those qualifications or identify the row explicitly as background. This has no bearing on E0098, since these infinite-variance models are outside the subgaussian setting.

7. The supplied package lacks the `claim_files/sources/` directory promised by its report and log. Thus the full extracted texts and search log cited there are unavailable in this package. This is a packaging/reproducibility gap, not evidence that the source claims are false. Include that archive in a complete delivery. I fetched the primary papers independently into this review’s [sources/](sources/) and recorded their URLs, versions, retrieval times, and original byte hashes. No claimant code was executed or reused for the independent experiments.

What I verified and how
----------------------

The original question and its scope. The complete arXiv:1601.03678v3 text is [sources/survey.txt](sources/survey.txt). Its page breaks are preserved as form feeds. PDF p. 13 contains the following mathematical statement, transcribed with its notation and quantifiers restored:

> Corollary 4.8. Let $\xi,\zeta$ be sub-gaussian random variables with mean zero, and assume $\xi$ has unit variance. Let $W$ be an $n\times n$ Wigner matrix with atom variables $\xi,\zeta$. Let $v_1,\ldots,v_n$ denote the unit eigenvectors of $W$, and let $v_i(j)$ denote the $j$th coordinate of $v_i$. Then there exist constants $C,c,c_0,c_1>0$ (depending only on $\xi,\zeta$) such that, for any $n^{-c_0}<\alpha<c_0$ and $\delta\ge n^{-c_0/\alpha}$,
>
> \[
> \sup_{1\le i\le n}\mathbb P\!\left[
> \|v_i(W)\|_{\min}\le
> \frac{\delta}{n^{3/2}(\log n)^{c_1}}\right]
> \le C\frac{\delta}{\sqrt\alpha}+C\exp(-c\log^2 n).
> \]

The exact question immediately following the discussion of this corollary is:

> Open question. Is the limiting distribution of $\|v_j(W)\|_{\min}$ universal, or does it depend on the atom variables $\xi$ and $\zeta$?

The source is [O’Rourke–Vu–Wang, arXiv:1601.03678v3](https://arxiv.org/abs/1601.03678v3), subsequently JCTA 144 (2016), 361–442; the journal question is on p. 377. These are mathematical statements, with the original prose retained above.

The claim reads this fairly. The survey uses unit Euclidean norm, increasing eigenvalue order, and $\|v\|_{\min}=\min_k|v(k)|$, which is not a norm. Its definition is real symmetric with independent upper-triangular atoms; its corollary adds centered subgaussian atoms and unit off-diagonal variance. The question itself specifies neither scaling nor an eigenvector-index regime. Without scaling the limit is trivially zero, because every unit vector has minimum at most $n^{-1/2}$. The $n^{3/2}$ scaling is the substantive interpretation, supported by the GOE calculation and the preceding bounds. Taking fixed atom laws as $n\to\infty$ is appropriate here. An $n$-dependent increasingly sparse law would require a separate statement.

The corollary is a supremum of individual probabilities, not a probability that all eigenvectors simultaneously obey the bound. It has no bulk restriction. A conjecture for every deterministic $j_n\in\{1,\ldots,n\}$ is a reasonable precise strengthening, and the claim proves it only for GOE. It says nothing about the minimum over the whole eigenbasis or about an index selected adaptively from the eigenvectors. Multiplying the matrix by $n^{-1/2}$ leaves all these eigenvectors unchanged.

The GOE proof, line by line. Let $G_1,\ldots,G_n$ be independent standard real Gaussians, $R_n=(\sum_kG_k^2)^{1/2}$, and $S_n=R_n/\sqrt n$.

* The density of an unscaled GOE matrix is proportional to $\exp(-\operatorname{Tr}W^2/4)$, with diagonal variance two and off-diagonal variance one. It is orthogonally invariant. Its spectrum is simple almost surely, since the repeated-eigenvalue discriminant is a nonzero polynomial and the entry law has a density. Each ordered eigenline is therefore uniform. An independent random sign gives a spherical unit vector; absolute coordinates are unaffected by this sign. This handles any deterministic ordered index, exactly, at every finite $n$.
* Polar coordinates factor the Gaussian law into a uniform direction $U=G/R_n$ and an independent chi-distributed radius $R_n$. This verifies the requested norm independence. However, the raw minimum $M_n=\min_k|G_k|$ is not independent of $R_n$: $M_n=R_n\min_k|U_k|$. The claimant does not make that erroneous independence assumption.
* The half-normal density is $f(x)=c e^{-x^2/2}$, $x\ge0$, where $c=\sqrt{2/\pi}$. Its CDF satisfies $F(x)=cx+O(x^3)$. Consequently
  \[
  \mathbb P(nM_n>t)=(1-F(t/n))^n\longrightarrow e^{-ct},\qquad t\ge0.
  \]
  Both terms needed for the logarithm expansion hold: $nF(t/n)\to ct$ and $nF(t/n)^2\to0$. The rate is $c$, not its reciprocal and not one.
* Since $S_n\to1$ by the law of large numbers,
  \[
  n^{3/2}\min_k|U_k|=\frac{nM_n}{S_n}\Rightarrow\operatorname{Exp}(c).
  \]
  Slutsky’s theorem needs no independence of numerator and denominator. The claim’s alternative survival-probability sandwich is also valid.
* For a nonnegative compactly supported continuous test function $h$, the Laplace functional of $\sum_k\delta_{n|G_k|}$ is
  \[
  \left[1-\frac1n\int_0^\infty(1-e^{-h(y)})f(y/n)\,dy\right]^n
  \longrightarrow
  \exp\!\left[-c\int_0^\infty(1-e^{-h(y)})\,dy\right].
  \]
  This is a homogeneous Poisson process with intensity $c\,dy$. The space is $[0,\infty)$, with vague convergence on compact sets, including neighborhoods of zero.
* Dividing all points by $S_n\to1$ preserves that limit. If $\operatorname{supp}h\subset[0,B]$ and $1/2\le S_n\le2$, only raw points in $[0,2B]$ contribute. Their number is tight, since its expectation is $nF(2B/n)=O(1)$. Uniform continuity bounds the change on this tight set. Bounded Laplace functionals then converge in expectation. This justifies the normalization step rather than assuming independence. The result is exactly
  \[
  \sum_{k=1}^n\delta_{n^{3/2}|v_{j_n}(k)|}\Rightarrow\operatorname{PPP}(c\,dx).
  \]

I also checked the constant a second way from the exact joint spherical density. For fixed $r$, the signed first $r$ coordinates of $\sqrt n U$ have density

\[
C_{n,r}(1-\|y\|^2/n)^{(n-r-2)/2}\mathbf1_{\|y\|<\sqrt n},\qquad
C_{n,r}=\frac{\Gamma(n/2)}{\Gamma((n-r)/2)(\pi n)^{r/2}}.
\]

On $[-t/n,t/n]^r$, its density converges uniformly to $(2\pi)^{-r/2}$. Therefore the small-box probability is $(ct/n)^r(1+o(1))$. The lower and upper bounds displayed in the claim have the correct factor $1-rt^2/n^3$ and the correct exponent. Independent numerical evaluations and a Gaussian CDF derivative check are saved in [data/math_checks.json](data/math_checks.json).

The factorial-moment criterion. With $N_n(t)=\sum_k\mathbf1_{\{\sqrt n|V_n(k)|\le t/n\}}$, the claim’s sum over ordered distinct coordinates is exactly $\mathbb E(N_n(t))_r$. The truncated binomial identity used to bound each point probability has the right coefficients and the right parity. Taking $n\to\infty$ at each fixed truncation and then taking the truncation to infinity proves $N_n(t)\Rightarrow\operatorname{Poisson}(ct)$. The identity $N_n(t)=0\iff n^{3/2}\min_k|V_n(k)|>t$ proves the exponential limit. Independent coordinate permutation preserves the minimum and justifies averaged probabilities even without exchangeability. The displayed density condition is sufficient, including its $2^r$ factor. A full point-process conclusion in a non-Gaussian model would additionally require mixed counts for disjoint intervals; the report only uses its one-window criterion to obtain the minimum.

The obstruction. Let $I$ be uniform on the coordinate labels. Plant zero at $I$ and put a uniform unit vector on its complement, of dimension $d=n-1$. The result is exchangeable and has minimum zero. For a deterministic set $J$, $|J|=m=o(n)$, the exceptional event $I\in J$ has probability $m/n\to0$. Conditional on its complement, the marginal is a scaled projection of a $d$-dimensional sphere. This already explains why the planted coordinate is invisible to sublinear coordinate samples.

The density and entropy calculation in the claim supplies a complete proof even for $m$ much larger than $\sqrt n$. Writing $z=d/2$, $u=m/2$, $b=z-u$, its relative entropy is

\[
D(u)=\log\Gamma(z)-\log\Gamma(b)-u\log z+(b-1)(\psi(b)-\psi(z))+u.
\]

Differentiation really gives $D'(u)=\psi(z)-\log z+1-(b-1)\psi'(b)$. For $b\ge1$, Jensen gives $\psi(z)\le\log z$ and the trigamma series gives $\psi'(b)\ge1/b$. Hence $D'(u)\le1/b$, and integration gives $D(u)\le\log(d/(d-m))\to0$. Pinsker proves the asserted total-variation convergence. The additional scaling has squared scale $s_n^2=1+O(1/n)$; its Gaussian relative entropy is $O(m/n^2)$. Adding the mixture error $m/n$ proves uniformity over deterministic coordinate subsets. I differentiated the entropy formula independently, including a symbolic algebra check in [code/referee_exact.py](code/referee_exact.py).

The nonzero modification is also correct. Plant $\varepsilon a n^{-3/2}$, with independent sign $\varepsilon$, and make the complementary radius $R=\sqrt{1-a^2/n^3}$. Every coordinate is nonzero almost surely, and the same total-variation bound holds. The complementary scaled minimum is multiplied by $R(n/(n-1))^{3/2}\to1$; thus the full minimum converges to $\min(a,E)$, with $E\sim\operatorname{Exp}(c)$. Its atom at $a$ has mass $e^{-ca}$. The construction is valid, not a normalization oversight.

This obstruction concerns the right statistical issue. In the zero version, for fixed $r,t>0$, the leading joint small-box probability is

\[
\mathbb P\{\sqrt n|Z(1)|,\ldots,\sqrt n|Z(r)|\le t/n\}
=\frac{(ct)^r+r(ct)^{r-1}+o(1)}{n^r}.
\]

The extra term arises when the planted index is one of these $r$ labels. It changes exactly the leading rare-event probability, while every fixed-dimensional Gaussian limit survives. For fixed coordinate polynomials, the spherical moment formula also shows only $O(1/n)$ changes in the Gaussian moment limits. Thus the example is more than an objection to a very weak one-coordinate central limit theorem. Nevertheless it is an example of unit vectors, not eigenvectors of an independent-entry Wigner model.

Independent matrix experiments. I wrote [code/referee_simulation.py](code/referee_simulation.py) before inspecting the claimant’s simulation source. It uses fresh seed 918273645, fresh matrices, and no claimant code or data as simulation input. GOE has off-diagonal $N(0,1)$ and diagonal $N(0,2)$; the Rademacher model has independent signs on and above the diagonal. An irrelevant common division by $\sqrt n$ keeps spectral magnitudes bounded. Each matrix supplies ordered indices $1$, $n/2+1$, and $n$, analyzed as separate groups.

There were 4,340 independent matrices and 13,020 selected eigenvectors. The comparison CDF was fixed as $1-e^{-ct}$, with no fitted parameter. Means and largest KS distance among the three index groups are:

| Ensemble | $n$ | Matrices | Lower-edge mean | Bulk mean | Upper-edge mean | Largest KS distance |
|---|---:|---:|---:|---:|---:|---:|
| GOE | 128 | 1200 | 1.2613 | 1.2414 | 1.2248 | 0.03283 |
| GOE | 512 | 600 | 1.3340 | 1.1742 | 1.3536 | 0.04535 |
| GOE | 1024 | 250 | 1.2398 | 1.2187 | 1.3896 | 0.07496 |
| GOE | 2000 | 120 | 1.0946 | 1.3311 | 1.3376 | 0.10185 |
| Rademacher | 128 | 1200 | 1.2736 | 1.1960 | 1.2759 | 0.03491 |
| Rademacher | 512 | 600 | 1.2744 | 1.3164 | 1.1958 | 0.04333 |
| Rademacher | 1024 | 250 | 1.2392 | 1.1735 | 1.2245 | 0.07785 |
| Rademacher | 2000 | 120 | 1.1041 | 1.3308 | 1.3801 | 0.09582 |

The target mean is 1.253314. The pointwise 95% DKW CDF half-widths for these sample sizes are respectively 0.03921, 0.05544, 0.08589, and 0.12398. Every empirical CDF lies within its corresponding band around the limiting exponential; the smallest reported KS p-value is 0.09159. These are compatibility checks of finite-$n$ distributions, not evidence of a proved convergence rate or proof of universality. At $n=2000$, standard errors of the means are roughly 0.09–0.13, so modest rate changes are poorly resolved. Simultaneous inference across groups must account for multiplicity; no rejection appears even before that adjustment. Eigenvectors from one matrix were never pooled as independent observations.

The raw data, group statistics including count factorial moments, and plotting artifact are [data/samples.csv](data/samples.csv), [data/summary.csv](data/summary.csv), and [data/referee_cdfs.svg](data/referee_cdfs.svg). Counts at thresholds $t=0.5,1,2$ were retained to examine the Poisson prediction; they do not prove it.

All selected minima were positive in floating point and exceeded $10^{-12}$; neither fact certifies exact nonvanishing. The main run used 490.04 seconds and peak RSS 340,787,200 bytes, with one worker and numerical thread limits set to one. Maximum eigenpair residual was $3.67\times10^{-15}$, and maximum unit-norm error was $7.78\times10^{-16}$. Fresh matrices at $n=128,512,2000$ were also solved using both narrow MRRR and full divide-and-conquer; the maximum disagreement in the scaled minimum was $3.33\times10^{-10}$, recorded in [data/solver_comparison.json](data/solver_comparison.json).

SciPy emitted arithmetic-status warnings inside its exact KS matrix-power routine on this Accelerate installation. All outputs were finite. I independently recomputed every KS statistic directly from sorted samples, with agreement within $10^{-14}$, and compared p-values to the usual asymptotic series, with maximum absolute discrepancy 0.01031. The report’s compatibility statement also follows from the directly computed KS statistics and the DKW bound, without depending on those exact p-values. See [data/ks_audit.json](data/ks_audit.json). The launcher explicitly uses nice 10; the sandbox denies separate priority inspection. All numerical subprocesses inherit that priority and set numerical thread limits. Compute state was checked throughout and did not enter distress. No simulation used a process pool.

I also recalculated the claimant’s main statistics directly from its CSV: 14,490 rows, 36 groups, exactly matching scaling, five unadjusted rejections at 0.05, and the stated single Bonferroni rejection for centered Bernoulli $p=0.1$, $n=128$, upper edge. The rederived numbers are in [data/claim_data_recalculation.json](data/claim_data_recalculation.json). That finite-size rejection is not an asymptotic counterexample, and the claimant appropriately reports it rather than concealing it.

Exact Rademacher zeros. Diagonal sign conjugation preserves zero coordinates but does not force them: it changes their signs. A simple-spectrum witness is

\[
A=\begin{pmatrix}1&1&1\\1&1&1\\1&1&-1\end{pmatrix},\qquad
A(1,-1,0)^T=0,\qquad \det(xI-A)=x(x^2-x-4).
\]

More generally, $e_a-e_b$ is an eigenvector if $W_{aa}=W_{bb}$ and $W_{ka}=W_{kb}$ for $k\notin\{a,b\}$. For a fixed pair in the fully Rademacher model, this has probability $2^{-(n-1)}$. The $e_a+e_b$ version uses opposite external entries and has the same probability. These are real finite-size mechanisms with exponentially decreasing probabilities. Counting either mechanism over label pairs remains $O(n^2 2^{-n})$; this is an upper bound for these mechanisms, not an upper bound for every possible exact zero.

My independent exhaustive enumeration in [code/referee_exact.py](code/referee_exact.py) reproduced:

| Diagonal law | $n$ | All sign assignments | Simple spectrum | Simple spectrum with some zero coordinate |
|---|---:|---:|---:|---:|
| Rademacher | 2 | 8 | 8 | 0 |
| Rademacher | 3 | 64 | 48 | 48 |
| Rademacher | 4 | 1024 | 768 | 576 |
| Zero | 2 | 2 | 2 | 0 |
| Zero | 3 | 8 | 0 | 0 |
| Zero | 4 | 64 | 48 | 48 |
| Zero | 5 | 1024 | 0 | 0 |

For a simple-spectrum symmetric integer matrix, let $p=\det(xI-A)$ and $p_i=\det(xI-A^{(i)})$. The exact identity $p_i(\lambda_j)=p'(\lambda_j)|v_j(i)|^2$ makes a polynomial gcd test decisive. I used exact integer/rational arithmetic, checked squarefreeness first, and did not call a tiny floating-point coordinate an exact zero. Repeated eigenspaces were counted separately: an eigenspace of dimension at least two intersects every coordinate hyperplane nontrivially, so an existential zero is automatic there, whereas a selected numerical eigenbasis is basis-dependent. See [data/exact_zeros.json](data/exact_zeros.json).

A further independent-seed search examined 3,000 fully Rademacher matrices at each small size, using full eigensystems as a trigger and exact characteristic-polynomial/minor gcds to certify every reported positive:

| $n$ | Certified simple matrices with a zero / 3000 | Certified repeated spectra / 3000 |
|---:|---:|---:|
| 8 | 1675 | 339 |
| 12 | 721 | 57 |
| 16 | 132 | 6 |
| 24 | 1 | 0 |
| 32 | 0 | 0 |
| 64 | 0 | 0 |

All triggered candidates were certified as either an exact zero in simple spectrum or a repeated spectrum. Negative results use a numerical trigger and are not exact exhaustive certificates. These counts concern existence anywhere in an eigenbasis, not the probability for one fixed ordered index. Code, seed, triggers, and witness matrices are in [code/referee_small_zero.py](code/referee_small_zero.py) and [data/small_zero_search.json](data/small_zero_search.json).

The decisive asymptotic fact is already printed: survey Theorem 1.4, PDF p. 3, gives probability $O_A(n^{-A})$, for every fixed $A$, of any zero coordinate of any eigenvector under the subgaussian hypotheses. I checked its primary basis in Tao–Vu’s Proposition 2.2: for a block matrix $[A,X;X^T,a]$, an eigenvector $(u,0)$ requires $Au=\lambda u$ and $X^Tu=0$. The proposition bounds that event for the independent minor and row. A union over deleted coordinates, with a larger fixed exponent, proves the advertised conclusion. The separate derivation from survey Theorem 4.7, using $\delta=n^{-B}$, fixed sufficiently small $\alpha$, and a union over $n^2$ coordinate/index pairs, is also valid. Thus an asymptotically nonnegligible exact-zero probability cannot break universality for fixed Rademacher atoms. This theorem does not identify the law of very small nonzero coordinates.

Literature result and value
---------------------------

I checked actual statements and parameter scales, not just titles or abstracts. Sources below are saved as plain text with PDF page boundaries; pages in the table refer to the pinned arXiv versions. Searches used “minimum coordinate,” “smallest coordinate,” “smallest eigenvector entry,” “minimum absolute coordinate,” “no-gaps delocalization,” “small-ball,” and “Poisson,” with Wigner/eigenvector qualifiers, and followed the 2026 papers’ references. The search record is [sources/SEARCH_LOG.txt](sources/SEARCH_LOG.txt).

| Primary source | Checked result | Relevance and limitation |
|---|---|---|
| [Rivin, math/0305252v1](https://arxiv.org/abs/math/0305252v1), [text](sources/rivin_spheres_minima.txt) | Theorems 1–3, pp. 2–4 | The same spherical minimum, Gaussian/polar reduction, and expected asymptotic $\sqrt{\pi/2}\,n^{-3/2}$. This is prior work on the minimum, but not an explicit statement of the full GOE point-process limit. |
| [Resnick, 1987](https://link.springer.com/book/10.1007/978-0-387-75953-1) | Proposition 3.21, p. 154 | Classical iid rare-event point-process convergence. Applying it to $n\vert G_k\vert $, then using radius concentration, gives the claimed GOE process. This is an application of printed general theory; I do not assert that the book prints this exact GOE formulation. |
| [Bourgade–Yau, 1312.1301v6](https://arxiv.org/abs/1312.1301v6), [text](sources/bourgade_yau.txt) | Theorem 1.2, Corollaries 1.3–1.4, pp. 5–6 | Fixed-dimensional Gaussian moments and QUE for generalized Wigner matrices with all normalized moments bounded. The printed index set is the bulk together with ranks within $n^{1/4}$ of the edges; intermediate regimes are omitted there. No microscopic relative small-box estimate. |
| [Benigni, 1711.07103v3](https://arxiv.org/abs/1711.07103v3), [text](sources/benigni_deformed.txt) | Theorem 1.3, Corollary 1.4, Theorem 1.7, pp. 5–6 | Bulk eigenvector Gaussianity/QUE for a mesoscopic diagonal deformation, with a nonconstant variance profile. Different model; finite marginals do not give its minimum law. |
| [Benigni, 1908.10855v2](https://arxiv.org/abs/1908.10855v2), [text](sources/benigni_fermionic.txt) | Theorems 1.2 and 1.5, pp. 4, 6 | Fermionic flow and decorrelation of partial masses/overlaps. These are averaged polynomial observables, not a near-zero point process. |
| [Benigni–Lopatto, 2007.09585v2](https://arxiv.org/abs/2007.09585v2), [text](sources/benigni_lopatto_delocalization.txt) | Theorems 1.2–1.4, pp. 3–4 | Optimal upper delocalization, under subexponential tails, throughout the spectrum. Largest-coordinate bounds, with additional smoothness for a whole-basis sharp bound. |
| [Benigni–Lopatto, 2103.12013v3](https://arxiv.org/abs/2103.12013v3), [text](sources/benigni_lopatto_que.txt) | Theorems 1.2 and 1.4, pp. 2–3 | All-index CLT for sums of squared projections on $n^\epsilon\le\vert I\vert \le n^{1-\epsilon}$, and high-probability QUE. This is not joint Gaussian entrywise approximation of that many coordinates. |
| [Marcinek–Yau, 2005.08425v1](https://arxiv.org/abs/2005.08425v1), [text](sources/marcinek_yau.txt) | Theorems 2.5 and 2.8, p. 14 | Joint fixed-polynomial projection limits, first for regular Gaussian-divisible bulk models, then for generalized Wigner bulk eigenvectors. The degree-dependent additive error cannot simply be substituted into $n^{-r}$-probability boxes. |
| [Cipolloni–Erdős–Schröder, 2012.13215v4](https://arxiv.org/abs/2012.13215v4), [text](sources/ces_eth.txt) | Theorem 2.2, p. 5 | ETH for bounded deterministic observables, simultaneous in eigenvector indices, with $n^{-1/2+\epsilon}$ error. Does not count entries near zero. |
| [Cipolloni–Erdős–Schröder, 2103.06730v3](https://arxiv.org/abs/2103.06730v3), [text](sources/ces_normality.txt) | Theorem 2.2, p. 6 | Bulk Gaussian fluctuations of high-rank quadratic forms with nonvanishing normalized traceless variance. No minimum theorem. |
| [Rudelson–Vershynin, 1506.04012v1](https://arxiv.org/abs/1506.04012v1), [text](sources/rudelson_vershynin.txt) | Theorems 1.3 and 1.5, Remark 1.6, pp. 3–4 | No-gaps lower mass bounds under independence/anticoncentration/norm assumptions. The continuous statement starts with sets larger than eight coordinates; the meaningful discrete range in this version has $\epsilon\gtrsim n^{-1/7}$, despite a formal $\epsilon\ge1/n$ statement. Neither is the $n^{-3/2}$ minimum law. |
| [Luh–O’Rourke, 1810.00489v2](https://arxiv.org/abs/1810.00489v2), [text](sources/luh_orourke.txt) | Theorems 2.4–2.5, p. 5 | Independent real entries, non-Hermitian matrix; the $m=1$ real-eigenvector bound has scale $t n^{-3}$. It is neither a sharp distributional law nor a symmetric Wigner theorem. The paper also treats genuinely complex matrices and rectangular normal vectors, which must be kept separate. |
| [Nguyen–Tao–Vu, 1504.00396v2](https://arxiv.org/abs/1504.00396v2), [text](sources/nguyen_tao_vu_gaps.txt) | Theorem 3.3, p. 6 | For subgaussian Wigner noise plus polynomial-norm deterministic shifts, all eigenvector entries exceed $n^{-B(A)}$ except on an $O(n^{-A})$ event. Nonvanishing/nondegeneration, not the leading small-ball constant. |
| [Tao–Vu, 1412.1438v1](https://arxiv.org/abs/1412.1438v1), [text](sources/tao_vu_simple.txt) | Theorem 1.3 and Proposition 2.2, pp. 2–3 | Superpolynomial simplicity and the minor-row orthogonality estimate. Directly excludes a persistent exact-zero obstruction for fixed nontrivial atoms. |
| [Knowles–Yin, 1102.0057v4](https://arxiv.org/abs/1102.0057v4), [text](sources/knowles_yin.txt) | Theorems 1.6 and 1.10, pp. 4–6 | Fixed edge observables under two-moment comparison and level repulsion; bulk comparison under four off-diagonal/two diagonal matching moments. Not the needed fine-scale relative comparison. |
| [Tao–Vu, 1103.2801v2](https://arxiv.org/abs/1103.2801v2), [text](sources/tao_vu_eigenvectors.txt) | Theorems 7–8, pp. 6–7 | Smooth comparison for polynomially growing collections under moment matching. The derivative restrictions exclude a direct substitution of the microscopic minimum event. Rademacher does not match the Gaussian fourth moment. |
| [Benigni–Cipolloni, 2212.10694v1](https://arxiv.org/abs/2212.10694v1), [text](sources/benigni_cipolloni.txt) | Theorem 2.2, p. 4 | Joint Gaussian fluctuations of finitely many bulk quadratic forms under an effective-rank condition. No shrinking-coordinate-window counts. |
| [Benigni–Rezaei Feyzabady, 2509.19581v1](https://arxiv.org/abs/2509.19581v1), [text](sources/benigni_feyzabady_2026.txt) | Theorem 1.2, p. 2 | Gaussian process limits for deterministic regular families of bulk quadratic-form observables. This is not a process of tiny eigenvector coordinates. |
| [Benigni–Lopatto, 2606.06419v2](https://arxiv.org/abs/2606.06419v2), [text](sources/benigni_lopatto_2026.txt) | Theorems 1.2–1.3, Corollary 1.4, Theorems 1.6–1.7, pp. 3–5 | All-index Gaussian projections and a Poisson process for upper extremes, centered at $2\log n-\log\log n-\log\pi$. Under smoothness, growing-coordinate comparison has explicit additive errors. Detailed scale obstruction below. |
| [Bao–Bucht–Schnelli, 2606.17425v1](https://arxiv.org/abs/2606.17425v1), [text](sources/bao_bucht_schnelli_2026.txt) | Theorems 1.5, 1.7, 1.9, pp. 3–4 | Edge upper extremes, intermediate ranks near the maximum, and a smooth comparison allowing arbitrary order-statistic ranks. Its derivative restrictions do not permit the rescaled smallest entry. |
| [Osman, 2609.11630v1](https://arxiv.org/abs/2609.11630v1), [text](sources/osman_2026.txt) | Theorems 1.2–1.3, pp. 3–4 | Gumbel laws for the largest entry at an eigenvalue nearest fixed energy, and for the whole basis under the stated complex/real four-moment assumptions. Different statistic; fixed energy and fixed ordered index must also be distinguished. |
| [Fyodorov–Shcherbina–Shcherbina, 2611.12858v1](https://arxiv.org/abs/2611.12858v1), [text](sources/fyodorov_shcherbina_2026.txt) | Theorem 2.4, Corollary 2.3, pp. 10–11 | A genuine lower-extreme Poisson/exponential result, but for complex GUE Rosenzweig–Porter occupations with $1<\gamma<2$, diagonal disorder, and a fixed-energy Kac–Rice law. Squared minimum scale $n^{-1-\gamma}$; neither a solution nor a counterexample to this real Wigner question. |
| [Aggarwal–Lopatto–Marcinek, 2002.09355v3](https://arxiv.org/abs/2002.09355v3), [text](sources/aggarwal_lopatto_marcinek.txt) | Theorems 2.9–2.10, p. 8 | Non-Gaussian variance-mixture entry laws for infinite-variance Lévy matrices, with the stated exclusions and energy restrictions. Outside the assumptions here. |

The most serious possible shortcut is the 2026 quantitative work. Benigni–Lopatto Theorem 1.6 assumes smooth entries and $RQ\le Cn^{1/2-b}$, where $Q$ is the number of projections and $R$ their span dimension. For $Q$ distinct coordinates of one eigenvector, $R=Q$, hence only $Q\le n^{1/4-\epsilon}$ follows. More importantly, Theorem 1.7 gives additive rectangular Kolmogorov error $O(n^{-b+\kappa})$; even for fixed dimension its printed general error is $n^{-1/2+\kappa}$. The Gaussian probability of $|\sqrt n v(k)|\le t/n$ is of order $n^{-1}$, and the $r$-coordinate probability is of order $n^{-r}$. Those errors do not identify their leading terms. Smooth cutoffs on width $1/n$ require second derivatives of order $n^2$, whereas Theorem 1.6 imposes a much smaller derivative-growth exponent $\delta_2<b\le1/2$. The report’s reading of these restrictions is correct.

Likewise, Bao–Bucht–Schnelli Theorem 1.9 does allow the smallest *rank*, but its test function acts on $n|v(k)|^2$. At the minimum this variable is of order $n^{-2}$; a nonconstant function of the rescaled minimum has first derivative of order $n^2$. The theorem bounds derivatives by $C_m n^{m\epsilon/4}$. Thus “arbitrary order statistics” does not give the needed limit at this scale. Upper-extreme Poisson convergence also does not imply a lower-extreme process: after upper centering, the tiny entries escape to minus infinity and are invisible to compactly supported tests.

Exactly what survives review is therefore: an unconditional classical GOE theorem for every deterministic index; a correct sufficient joint rare-event criterion; a correct exchangeable-vector counterexample to the inference from all sublinear coordinate Gaussian marginals; exact finite-size zero examples and asymptotic nonvanishing under the stated atoms; and numerical compatibility with the conjectured limit. There is no new unconditional universality theorem for a non-Gaussian Wigner atom, and no refutation of universality. The material has value as a careful explanatory and computational audit. Its novelty as a resolution or substantive advance on E0098 is insufficient.

Reproduction uses the independent programs in `code/`: `fetch_texts.py`, `referee_simulation.py`, `referee_exact.py`, `referee_small_zero.py`, `referee_numerics.py`, and `referee_plot.py`. The main simulation refuses to overwrite its raw sample file. All retained paper sources are plain text; no source PDFs, page images, or scans were saved. The SVG is an independently generated simulation plot. No publication, push, or external-state mutation was performed.

Task: “You are an independent referee … Break it if it is wrong.” E0098 — 13 November 2026, 11:43 Asia/Tbilisi.
