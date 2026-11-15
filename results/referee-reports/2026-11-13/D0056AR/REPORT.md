MINOR

The counterexample under bare criticality is correct. I found no error in Theorems A, 1, or 2, or in Corollary 3. Theorem A alone settles the question negatively and needs no external asymptotic theorem. Theorem 1 is a valid comparison argument; its use with the published product estimate in Theorem 2 is legitimate. The submission does not prove a survival asymptotic in the finite-third-tilted-moment regime, and does not prove existence of the heavy-tail limit. Those limitations are stated correctly.

The revisions concern a numerical-certificate justification, reproduction of the submitted package, numerical precision, and attribution. None overturns the counterexample.

1. **The lower certificate endpoint is justified for a different target from the one stated.** Location: CLAIM.md §4.3, especially lines 409–414; claim_files/code/certified.py lines 63–68. Write \(\widehat q_n\) for the numerical law's survival probability, \(q_n^{[K]}\) for the exact repeatedly deleted law, and \(v_n=\lceil S\widehat q_n\rceil\). The code uses \((v_n-1)/S\) as its lower endpoint. The transport estimate proves
   \[
   |q_n^{[K]}-\widehat q_n|\le E_n/(m-1),
   \]
   so the lower endpoint furnished by that argument for the *deleted* law is \(\max\{0,(v_n-1)/S-E_n/(m-1)\}\). Deletion above K is not an increasing map, and the submission itself correctly says the two numerical laws need not be ordered. Required fix: use the two-sided error for the deleted-law enclosure, or state explicitly that the existing lower endpoint targets the original untruncated law and prove that assertion. The latter proof is straightforward: quantization lowers the positive coefficients of the exact update of its own input, moving the deficit to zero; deletion also lowers that update. Induction using monotonicity of the **untruncated** recursion gives \(\widehat X_n\le_{\rm st}X_n\), hence \((v_n-1)/S\le q_n\). Together with the upper transport error and (16), this validates the original-process intervals in §5.2. I found a proof gap in the deleted-target assertion, not a failed original-process certificate.

2. **The supplied package does not reproduce with the printed paths.** Location: CLAIM.md §2, first paragraph; §§4.1–4.3; §5.5, lines 534–546; claim_files/code/analyze.py, final report-writing block. CLAIM.md is at the audit root, whereas code and data are in claim_files/. The printed commands fail from the directory containing CLAIM.md. Changing into claim_files fixes the numerical command paths but analyze.py still opens REPORT.md there, which is absent. The manifest also lists sixteen literature PDFs that are not supplied. Required fix: provide commands and document paths matching the actual layout, and either supply the referenced literature files or remove the assertion that they accompany the submission. This is a packaging defect, not evidence against the mathematics. All fifty supplied files covered by the manifest have matching hashes; CLAIM.md matches its former REPORT.md entry.

3. **Some FFT display digits are inaccurate as values of the mathematical survival probability.** Location: §5.1, particularly the {0,5} and b=4 rows, and any fits using those F rows. For example, at m=2 and n=10,000 the submitted {0,5} FFT value is 4.004908491291294, while independent certified computation gives 4.004902865598777 for \(n^2q_n\). The six-decimal entries would therefore be 4.004908 and 4.004903 respectively. For b=4, m=2, the absolute FFT error is about 1.01e-5. Required fix for a table intended to report accurate probabilities: replace the affected F values with certified ones, or reduce their displayed precision and identify the observed numerical error for those rows. The existing F warning prevents this from being a false rigorous claim; it does not make the last printed digits accurate. This has no bearing on the proofs.

4. **Distinguish the new sparse construction from a known leaf comparison.** Location: Theorem A's proof, §3.1, and the literature discussion of the dual-conjecture paper. Chen–Hu–Shi already use the stronger deterministic inequality
   \[
   X_n\ge\sum_{i=1}^{m^n}{\bf1}_{\{X_{0,i}\ge n+1\}}
   \]
   in Remark 1.2 of their [2023 preprint / 2024 paper](https://arxiv.org/pdf/2306.12717). Required fix: cite that antecedent and identify the contribution as the explicit critical sparse law and its subsequential obstruction. The heavy-tail constants are also earlier predictions, as the submission already acknowledges. The precise novelty assessment appears below.

A general stochastic-order argument cannot repair item 1: for m=2 and K=3, let \(\nu=(16/17)\delta_0+(1/17)\delta_3\), which is critical, and \(\mu=(16/17)\delta_0+(1/17)\delta_2\le_{\rm st}\nu\). Exact convolution gives \(q(T_KF\mu)=33/289>32/289=q(T_KF\nu)\). This example does not claim that the submitted quantizer realizes this pair; it explains why an additional argument for its deleted-process lower bound is necessary.

I checked Theorem A directly. For every integer m≥2 and 1≤rho<2, each factor \(((m-1)k_j-1)\) is positive. Since \(k_j\ge2\) and \(k_j^{1-\rho}\le1\),
\[
0<A\le(m-1)\sum_{j\ge1}j^{-2}<\infty,
\qquad 0<T\le\sum_j a_j<\infty.
\]
Thus c is positive and finite; p_0 and the infinitely many nonzero positive atoms are positive; their total mass is \(c(A+T)=1\). In particular the law is nonconstant and has positive probability of being at least two.

The centering identity is exact:
\[
A=\sum_j((m-1)k_j-1)a_j,
\quad A+\sum_j a_j=(m-1)\sum_j k_ja_j.
\]
Consequently
\[
E[m^{X_0}]=c(A+\sum_j a_j)
=(m-1)c\sum_j k_ja_j=(m-1)E[X_0m^{X_0}].
\]
The common value is finite, because \(\sum_j k_ja_j=\sum_j j^{-2}2^{j(1-\rho)}\). This includes the endpoint rho=1; there is no divergent first tilted moment hidden in the construction.

For r>0 the tilted moment is
\[
E[X_0^r m^{X_0}]=c\sum_{j\ge1}j^{-2}2^{j(r-\rho)}.
\]
It is finite for r<rho by exponential decay, finite at r=rho by the summable factor j^-2, and infinite for r>rho because its summands do not tend to zero. Every ordinary polynomial moment is finite. For t>m, the summands \(c(t/m)^{2^j}/(j^2 2^{j\rho})\) do not tend to zero, so there is no exponential moment beyond m.

There is a quantifier distinction in the audit brief: a **fixed** rho-law does not have every tilted moment below two. Its exact threshold is rho. The submission's actual introduction correctly says a finite moment of *any prescribed* order below two, allowing the choice of rho to depend on that order. This is not an error in its theorem.

On the complete depth-n tree, following one leaf of value k gives an ancestor at height h at least \((k-h)^+\). Induction uses only the nonnegativity of the other children. At n_j=k_j-1, any leaf with value k_j therefore forces root survival. The independent leaves give
\[
q_{n_j}\ge1-(1-p_{k_j})^{m^{k_j-1}}
\ge1-\exp\{-m^{k_j-1}p_{k_j}\}
=1-\exp\{-c/(m j^2k_j^\rho)\}.
\]
This proves (A2), with the factor 1/m and the depth k_j-1 both correct. The exponential argument tends to zero. Hence
\[
n_j^2q_{n_j}\ge(1+o(1))\frac{c}{m}
\frac{(2^j-1)^2}{j^2 2^{j\rho}}\longrightarrow\infty.
\]
This proves the claimed limit along the subsequence, not merely an unbounded subsequence of lower bounds.

For rho=1, j=log_2(n_j+1), and k_j=n_j+1 is asymptotic to n_j. Therefore (A4) is exactly the stated lower bound. In particular
\[
\liminf_{j\to\infty}\frac{\log q_{n_j}}{\log n_j}\ge-1.
\]
The assertion \(q_n=n^{-2+o(1)}\) would force that ratio to tend to -2 along every subsequence. It is incompatible with this inequality. This argument does not assert a full asymptotic exponent for the sparse law. For rho=1 the displayed formula \(A=(m-1)\zeta(2)-\operatorname{Li}_2(1/2)\) follows by summing its two terms; it is correctly confined to that parameter choice.

For Theorem 1, the exact identity linking survival and the tilted generating functions is
\[
\boxed{\quad mG_{n+1}(m)=G_n(m)^m+(m-1)(1-q_n)^m.\quad}
\]
It follows by separating the event that the sum of the m children is zero. More generally,
\[
G_{n+1}(s)=s^{-1}G_n(s)^m+(1-s^{-1})G_n(0)^m.
\]
Differentiation at m, using the finite first tilted moment and left limits, gives the propagated defect identity (9). These formulae do not require a third tilted moment.

I checked these identities against direct Fraction convolutions, independently of the submitted programs. Two sample exact checks are:

| m | critical initial law | q_0 | G_0(m) | G_1(m) |
|---:|---|---:|---:|---:|
| 2 | p_2=1/5, p_0=4/5 | 1/5 | 8/5 | 8/5 |
| 3 | p_2=1/28, p_0=27/28 | 1/28 | 9/7 | 14337/10976 |

For the first row, \(2(8/5)=(8/5)^2+(4/5)^2\). For the second, \(3(14337/10976)=(9/7)^3+2(27/28)^3\). The small-law program also checks noncritical examples, the full generating-function identity at three rational arguments, and the propagated defect. The fact that G_1(m) can exceed G_0(m), as in the second example, causes no problem: the proof does not assume monotonicity of this sequence.

Writing u_n=G_n(m)-1 gives exactly
\[
u_{n+1}=H(u_n)-d_n,
\quad H(x)=((1+x)^m-1)/m,
\quad d_n=(m-1)(1-(1-q_n)^m)/m.
\]
Here \(H'(x)\ge1\), \(H(x)=x+a x^2+O(x^3)\) with a=(m-1)/2, and \(d_n\sim(m-1)q_n\) once q_n tends to zero. The latter follows from \((m-1)q_n\le u_n\to0\).

For the comparison lemma, set w_n=A/n. Direct expansion gives
\[
H(w_n)-w_{n+1}=(A+aA^2)/n^2+O(n^{-3}).
\]
If the forcing d_n is eventually smaller by a fixed multiple of n^-2 and u_j≥w_j at some sufficiently large j, the next gap is at least eta/j^2. Since H'≥1, the gap stays at least that positive number forever. This contradicts convergence of both sequences to zero. For forcing eventually larger by a fixed multiple of n^-2, start with u_j≤w_j and propagate the opposite gap. Both strict inequalities in Lemma 4 have the correct direction. No differentiation of an asymptotic equivalence is used.

Let \(A_\beta=\beta/(m-1)\). Then
\[
A_\beta+aA_\beta^2=(m-1)
\frac{\beta(\beta+2)}{2(m-1)^2}.
\]
If the survival liminf were strictly above this threshold, choose A>A_beta close enough that the second comparison applies. Then u_n>A/n eventually, forcing \(\liminf\log\Pi_n/\log n\ge(m-1)A>\beta\). If the survival limsup were strictly below the threshold, choose A<A_beta and obtain the opposite contradiction. These steps also cover infinite liminf or finite limsup as appropriate. The bracket, and its consequence for any extended convergent limit, follow. Theorem 1 is proved.

For Theorem 2, \(A_b=\sum_{k\ge1}((m-1)k-1)k^{-b}\) is finite and positive. For m=2 the k=1 summand is zero, not negative; k≥2 supplies strict positivity. The normalization in (4) is therefore valid, and
\[
E[m^{X_0}]=c_b(m-1)\zeta(b-1),\qquad
E[X_0m^{X_0}]=c_b\zeta(b-1).
\]
The tilted r-moment is finite exactly when r<b-1. Thus this family meets bare criticality and fails the third tilted moment when 2<b<4.

I fetched and read the relevant statements and their surrounding hypotheses in the following primary versions:

| Source and locator | Hypotheses and conclusion actually used |
|---|---|
| [Chen–Shi, arXiv:2006.06140v1](https://arxiv.org/pdf/2006.06140), pp. 1–4, Theorem 1.1 | Integer m≥2, nonnegative integer initial law, positive mass at or above two, finite critical equality, and p_k asymptotic to c_0 m^-k k^-alpha with c_0>0 and 2<alpha<4. The product indexed i=0,…,n-1, with power m-1, lies between positive constant multiples of n^(alpha-2). |
| [Chen–Derrida–Hu–Lifshits–Shi, arXiv:1705.04787v2](https://arxiv.org/pdf/1705.04787v2), pp. 1–4, Theorem 2; p. 8, Propositions 1–2 | The paper excludes constant initial laws. Under the finite critical equality, Theorem 2 gives G_n(m)→1. Its two product propositions give upper and lower quadratic growth when the third tilted moment is finite. |

Every hypothesis holds for (4). Setting alpha=b gives \(\log\Pi_n/\log n\to b-2\), so Theorem 1 yields the constant \(b(b-2)/(2(m-1)^2)\). It is strictly below \(4/(m-1)^2\) for 2<b<4, and the liminf inequality alone excludes convergence to the latter. The source proves a product bound, not a survival limit; the submission uses exactly the product bound. The harmless extra terminal factor in the older product convention does not change its exponent. The same argument with exponent two proves Corollary 3.

The numerical audit uses new programs audit_independent.py, audit_compare.py, and audit_fft_long.py. They do not import or execute anything in claim_files/code or its vendor directory. Separate dependencies were installed into audit_vendor/. Small truncated laws are iterated as exact Fraction distributions. The long certified runs use exact FLINT integer-polynomial powers with explicitly bounded quantization; they do not represent an irrational infinite-tail law as a single exact rational distribution. This distinction matters when describing what is exact.

The small checks passed 120 exact identities, 28 exact truncated-law/enclosure comparisons through generation six, 180 transport inequalities, and eight comparisons between exact truncated and untruncated trajectories. The long computations use 128 coefficient bits and 256 error bits, rather than the submission's 112 and 192. Their support at time t is K_t=10,000-t+192. The same tree argument, with B replaced by the rational upper bound m, gives
\[
0\le q_n-q_n^{[K_\bullet]}
\le m\sum_{j=0}^n m^{n-j-(K_j+1)}
=(n+1)m^{n-10000-192}.
\]
At n=10,000 this is below 1.594e-54 for m=2 and 2.471e-88 for m=3. The support schedule therefore differs from the submission's while still giving an independently rigorous check of the displayed probabilities.

I also verified the submission's fixed-cutoff bound (16). Criticality gives E_Q X_n=1/(m-1) under the m-tilted probability measure. Jensen yields G_n(m)≤B=m^(1/(m-1)). A root discrepancy requires a deletion somewhere in the tree; summing the tail bound B*m^(-K-1) over all heights proves (16). This reasoning uses monotonicity of the original recursion, not monotonicity of deletion. At K=N+128 its uniform bounds are
\[
5.87747175411144\times10^{-39}\quad(m=2),\qquad
7.34530827803670\times10^{-62}\quad(m=3).
\]
Both reported rounded bounds are correct. They control survival probabilities, not errors in tilted moments or rounding errors from FFTs.

Lemma 6 also checks out. For integers r,s≥0 the update contracts \(|m^r-m^s|\) by at most 1/m; telescoping m independent input products gives its factor M^(m-1). For deletion, the crossing case r≤K<s satisfies \(m^r-1\le m^s-m^r\) when m≥2. Finally, changing zero/nonzero status costs at least m-1. The p_0 rounding contributes at most m/S and flooring the K positive tilted coefficients at most K/S, giving (18). Directed integer rounding of that recursion is a valid certificate calculation. The issue in item 1 concerns the lower endpoint's stated target, not these estimates.

The eight independently reproduced endpoints are:

| m | law | independently computed n² q_n at n=10,000 | submitted twelve-decimal interval |
|---:|---|---:|---|
| 2 | {0,2} | 4.007963710799277 | [4.007963710799, 4.007963710800] |
| 2 | geometric | 4.005338853429370 | [4.005338853429, 4.005338853430] |
| 2 | b=3 | 1.500307923414970 | [1.500307923414, 1.500307923415] |
| 2 | sparse | 0.055798605399573 | [0.055798605399, 0.055798605400] |
| 3 | {0,2} | 1.001075562821592 | [1.001075562821, 1.001075562822] |
| 3 | geometric | 1.000595589825034 | [1.000595589825, 1.000595589826] |
| 3 | b=3 | 0.375288497543325 | [0.375288497543, 0.375288497544] |
| 3 | sparse | 0.013950630440629 | [0.013950630440, 0.013950630441] |

The independent **rational enclosures**, not just the printed centers, lie inside all eight submitted intervals. All sixteen law/offspring cases were independently run to 10,000 generations. The forty-two entries at n=1,000, 5,000, and 10,000 have direct independent comparisons; the twelve sparse table entries reproduce, and all twenty-four one-leaf diagnostics agree with an independent high-precision evaluation. All displayed tables agree with their saved sources. All forty-six regressions reproduce using independently constructed, column-normalized least-squares matrices. Their fit intercepts remain extrapolations; the unstable b=4 alternatives cannot prove a limit. Exact outputs and comparisons are in audit_results/.

The additional certified endpoints for the F rows quantify their rounding error:

| m | law | certified n² q_10000 | submitted FFT minus certified, approximately |
|---:|---|---:|---:|
| 2 | {0,5} | 4.004902865598777 | 5.62569e-6 |
| 2 | b=2.5 | 0.625055627769413 | 6.26724e-11 |
| 2 | b=3.5 | 2.606160344521983 | -1.32272e-7 |
| 2 | b=4 | 3.639732708119070 | -1.00930e-5 |
| 3 | {0,5} | 1.000506086873256 | 1.17448e-6 |
| 3 | b=2.5 | 0.156279745989204 | -1.32740e-11 |
| 3 | b=3.5 | 0.655012872143153 | -4.13832e-8 |
| 3 | b=4 | 0.922957994239232 | 2.50532e-6 |

These differences are far larger than the certified quantization and support errors. They are compatible with the submission's own warning that the F arithmetic lacks a rounding certificate.

I independently reran both binary64 diagnostics to 100,000 generations at K=100,128. All six reported checkpoints reproduce exactly in binary64:

| binary law | n=10,000 | n=50,000 | n=100,000 |
|---|---:|---:|---:|
| {0,2} | 4.008005905502262 | 4.025712335227295 | 4.385326014725255 |
| b=3 | 1.500307922757368 | 1.500091549666516 | 1.500052511750945 |

These are reproduced **FFT outputs**, not certified values of the original process. In particular, the two-point drift is not evidence against the finite-third-moment prediction. The report appropriately excludes these runs from its asymptotic fits.

The audit used at most three simultaneous numerical workers, each with one library thread and nice priority 15. The largest recorded worker peak RSS was 189.91 MiB; the sum of the three largest individual worker peaks was 458.27 MiB. The requested four-thread and 4 GB limits were respected.

The main audit commands are `python3 audit_independent.py --small`, `python3 audit_independent.py --m 2 --law power3 --N 10000` (vary m and law for the sixteen cases), and `python3 audit_compare.py`. Long diagnostic runs use `python3 audit_fft_long.py --law two2` and `--law power3`. The audit imports FLINT from audit_vendor/; source hashes, versions, rational enclosures, run metadata, and comparisons are retained in audit_sources/ and audit_results/.

The literature assessment is narrower than a claim to have solved the usual finite-moment survival conjecture. The following distinguishes earlier results from the contribution here.

In [Derrida–Shi, arXiv:2005.10208](https://arxiv.org/pdf/2005.10208), §2.1, equations (13)–(14), both binary constants 4 and b(b-2)/2 are predictions. The former is associated with a finite third tilted moment; the power-tail prediction covers 2<b≤4. These constants are not discoveries of this submission, and that source does not prove the heavy-tail survival limit.

I read Collet et al.'s Appendix III and IV in the [complete October 1983 proceedings scan](https://www.numdam.org/item/RCP25_1983__33__117_0.pdf), including visual inspection where the extracted text loses exponents. The [published metadata](https://link.springer.com/article/10.1007/BF01224830) are CMP 94 (1984), 353–370; I did not obtain the publisher's full typeset PDF. Appendix III assumes a smooth expansion before its precise survival prediction. Appendix IV, equations (AIV.5), (AIV.11), and (AIV.12), addresses nonquadratic **product** growth for singular tilted generating functions. In its two cases, the powers 1-alpha and 2-alpha correspond to b-2 after translating the singularity exponent. Chen–Shi explicitly describe their theorem as completing this earlier product analysis, including the missing b=3 case. This history supplies neither the submitted sparse construction nor a rigorous survival limit.

The [2021 Chen–Hu–Shi preprint](https://arxiv.org/pdf/2108.05610), published in PTRF 182 (2022), 641–684, has a crucial extra hypothesis in Theorem 1.2: E[t^X_0]<∞ for some t>m. It proves the exponent n^(-2+o(1)), not its leading constant. Its stated fifth-tilted-moment upper bound and exponential-moment lower bound also match the submission. The sparse law has no such exponential moment and therefore contradicts no theorem in that paper. The 2019 chapter's §9 gives weaker harmonic information; I found no version of the precise beta-dependent liminf/limsup bracket there.

For 2023–2026 I checked the arXiv title/abstract search as well as the following primary papers. Their hypotheses and conclusions do not close this deterministic-offspring survival question:

| Paper | Relevant distinction |
|---|---|
| [Chen–Hu–Shi, 2306.12717](https://arxiv.org/pdf/2306.12717), SPA 171 (2024), 104332 | Nearly subcritical exponential decay; Remark 1.2 contains the antecedent for the large-leaf comparison. |
| [Chen, 2405.09741](https://arxiv.org/html/2405.09741), published 2026 | Theorem 1.1 concerns smoothness of the free energy as a function of the initial mixture parameter, not a critical survival prefactor. |
| [Li–Zhang, 2411.13068v3](https://arxiv.org/pdf/2411.13068v3), JSP 192 (2025), 98 | Theorem 1.3(3) and Corollary 1.5(3) give a survival constant 2/(m-1)^2 for geometric offspring and geometric-type initial laws; offspring are not deterministically m. |
| [Li–Zhang, 2411.12189v2](https://arxiv.org/html/2411.12189v2) | Theorem 2.8 scales the renewal rate as a/k to obtain a continuous-time limit. This does not prove a survival limit for fixed deterministic offspring. |
| [Lotnikov–Kotova, 2502.02535](https://arxiv.org/abs/2502.02535), journal version 2024 | Sufficient conditions for free-energy phases with random offspring and general tax; no critical survival constant. |
| [Alsmeyer–Hu–Mallein, 2502.02991v2](https://arxiv.org/pdf/2502.02991v2), April 2026 version | Solvable geometric Galton–Watson models; exact critical curves and free-energy behavior concern a different offspring law. |
| [Duquesne–Shi, 2609.11435](https://arxiv.org/pdf/2609.11435), September 2026 | The continuous branching process and its Brownian-CRT representation. Its introduction explicitly leaves convergence from the discrete critical model unproved. |
| [Aldous–Contat–Curien–Hénard](https://arxiv.org/html/2205.15932), published 2023; [Chen–Contat](https://arxiv.org/abs/2402.05612), published 2025 | Parking models with arrivals at internal vertices; their recursions differ from the leaf-only iteration in this question. |

Within the literature examined through 13 November 2026, I found no prior printed statement of the explicit sparse critical family in Theorem A or of Theorem 1's exact beta-dependent bracket. The defensible new content is: the explicit sparse critical counterexample and its failure of the exponent assertion; the rigorous scalar comparison yielding the bracket for general m and beta; and, as a short consequence of known product estimates, exclusion of the universal constant for regular tilted power tails. Theorem 2 identifies the only **possible convergent** prefactor, not a proved new survival asymptotic. Its binary prefactor and the need for a moment restriction were already predicted. Corollary 3 is a consequence of the same comparison with the older quadratic product bounds. The recurrence identities, basic leaf mechanism, and product estimates are prior material. Absolute bibliographic priority cannot be established by a negative search.

Task: “Your job is to break it if it is wrong. … Write REPORT.md. … Keep LOG.md as you go.” Received 13 November 2026, approximately 02:21 local shell time (+04).
