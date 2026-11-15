MINOR

The mathematical claims (a) and (b) survive this audit. I found no counterexample and no load-bearing error in the binary proof, either Fisher–Rao lemma, the contraction argument, or the positive two-cycle construction. Under the survey's stated normalization, the binary threshold really is

\[
\lambda_2=\frac{3-\sqrt7}{4}=0.0885621722338523\ldots,
\]

half its printed value. For every \(m\ge3\), the claimed inequalities

\[
\frac{1-1/\sqrt{m+1}}{2m}\le\lambda_m\le
\frac{2}{3m+2+\sqrt{m^2+12m+4}}<\frac1{2m}
\]

and the limit \(2m\lambda_m\to1\) are proved. This accepts the submission as a partial result. It does not determine any exact \(\lambda_m\) for \(m\ge3\). The MINOR rating concerns source packaging, citations, and one unproved optional aside; the principal formulas need no correction. Novelty remains less certain than correctness.

The errors and gaps requiring attention are:

1. **Missing source artifacts.** `claim_files/REPORT.md:48` and `:50`, and several entries in its Section 8, describe saved texts in `sources/`, but the supplied `claim_files/` contains no such directory. The referee therefore could not inspect the claimed source extractions. Fix: distribute the cited text files or mark them unavailable in the submitted bundle. I independently obtained both arXiv versions in this review's `sources/arxiv_0902_4207v1.txt` and `sources/arxiv_0902_4207v2.txt`, and saved a verified transcription of the 2011 statement in `sources/idaqp_2011_statement.txt`.

2. **Missing directly relevant binary literature.** Section 3 and the literature list omit Karim–Hamzah–Ganikhodjaev (2022), whose formula (7), discriminant, second-iterate factors, and Theorem 3.1 already contain the relevant binary classification away from the neutral endpoint. That paper attributes the classification to Lyubich (1974). Fix: cite this antecedent and distinguish the correction of the survey's coefficient-floor value from the older classification of scalar quadratic dynamics. I did not locate an earlier explicit correction of the survey's printed value. The claim appropriately makes no unconditional priority assertion.

3. **Later literature and priority remain incompletely checked.** Section 8 does not include Saburov–Saburov's directly relevant 2025 journal paper, published in English in January 2026, or Saburov's October 2026 paper. The former explicitly leaves the unrestricted threshold unknown; its threshold zero is for a doubly stochastic subclass. The latter's abstract and bibliography are accessible, but its body was not accessible here. Fix: add these records and retain a qualified novelty statement. The original 1988 source [17] also remains unread. Consequently the discrepancy can be located in the surveys, but cannot be assigned to the original authors' calculation rather than later transcription. This is an acknowledged provenance limitation, not a defect in the independent proof.

4. **An optional correct bound is asserted without its derivation.** At `claim_files/REPORT.md:287`, the additional \(\ell^1\) factor \(2(1-m\mu)(1-\mu)\) is not justified. Fix: for \(x\in\Delta_\mu\), write \(B_{ki}=\sum_jQ_{ij,k}x_j\). Columns \(i,l\) overlap by at least \(\min(x_i,x_l)\sum_kQ_{il,k}\ge\mu\), using parent symmetry. Thus their Dobrushin coefficient is at most \(1-\mu\); \(DV=2tB\) gives the asserted tangent bound. Integrating along straight segments in \(\Delta_\mu\) proves the contraction. This aside is not used in the stronger Fisher–Rao result.

There are no further mathematical errors identified. The lack of an exact answer for \(m\ge3\), possible higher-period/nonperiodic obstructions in the remaining interval, and the inability of finite searches to prove optimality are already acknowledged in the claim and are not concealed proof steps.

The source normalization settles the factor-of-two question.

Both [arXiv v1, 24 February 2009](https://arxiv.org/html/0902.4207v1) and [v2, 12 March 2009](https://arxiv.org/html/0902.4207v2) define, in formulas (4)–(5),

\[
(Vx)_k=\sum_{i,j=1}^mP_{ij,k}x_ix_j,\qquad
P_{ij,k}\ge0,\quad P_{ij,k}=P_{ji,k},\quad
\sum_{k=1}^mP_{ij,k}=1.
\]

Here is their shared Section 9 statement, with mathematical typesetting normalized:

> Theorem 7. [17] 1) If \(P_{ij,k}>{1\over2m}\) then \(V\) is regular.
>
> 2) \(\alpha_2={1\over2}(3-\sqrt7)\).
>
> Problem 12. Find exact values of \(\alpha_m\) for any \(m\ge3\).

The strict inequality is \(>\), not \(\ge\). The paragraph before the theorem defines \(\alpha_m\) as the smallest sufficient threshold for that strict implication. I compared the extracted theorem/problem passages: v1 and v2 agree exactly. These are full plain-text extractions with the LaTeX retained; some HTML-rendered formulas also appear alongside their LaTeX representation.

In the [2011 IDAQP author-uploaded article](https://www.researchgate.net/publication/263864800_QUADRATIC_STOCHASTIC_OPERATORS_AND_PROCESSES_RESULTS_AND_OPEN_PROBLEMS), Section 2.1 uses the same ordered-pair sum and symmetry. Section 2.8, journal p.290, repeats these assertions as Theorem 2.28(i)–(ii) and the question as Problem 2.29, citing reference 40. The paragraph also explicitly asserts a unique limiting fixed point. This supports the common-limit definition required by the present question. Neither survey proves the threshold theorem.

In particular, \(P_{12,k}=P_{21,k}\), so the binary coordinate map is precisely

\[
f(x)=a x^2+2b x(1-x)+c(1-x)^2,
\quad a=P_{11,1},\ b=P_{12,1},\ c=P_{22,1}.
\]

The complementary heredity coefficients are \(1-a,1-b,1-c\). A uniform floor \(\delta\) therefore means \(a,b,c\in[\delta,1-\delta]\). There is no factor-two normalization error on the claim's side. Omitting the mixed factor 2 would change the operator class and would contradict the surveys' definitions. The printed value is a genuine discrepancy under their stated definitions, although its historical origin is unresolved.

Reference [17] is R. N. Ganikhodzhaev and A. T. Sarymsakov, *A simple criterion for regularity of quadratic stochastic operators*, Dokl. Akad. Nauk UzSSR (1988), no.11, pp.5–6, Russian. The [contemporary Uzbek bibliography, entry 128, printed p.86](https://uzbekbibliography.library.illinois.edu/Content/PDFs/1.1989.pdf.ocr_letopispechati.pdf) independently confirms the year and Russian title, “Об одном простом критерии регулярности квадратичных стохастических операторов”. This is bibliographic evidence, not access to the original proof. A later bibliography's 1986 date is not supported by this contemporary record.

The binary argument checks line by line.

Write \(A=a-2b+c\), \(B=2(b-c)\), \(C=c\), and \(g=f-x\). Positive coefficients give \(g(0)>0>g(1)\). A quadratic with these endpoint signs has exactly one root \(p\) in \((0,1)\), with \(g>0\) below it and \(g<0\) above it. The affine case has the same conclusion.

Direct expansion gives

\[
D=(B-1)^2-4AC=(2b-1)^2+4c(1-a)
\le(1-2\delta)^2+4(1-\delta)^2
=5-12\delta+8\delta^2.
\]

Both inequalities are attained simultaneously at \(a=b=\delta,c=1-\delta\); this is an extremizer, though not the only one. The smaller root of \(5-12\delta+8\delta^2=4\) is \(\delta_*=(3-\sqrt7)/4\).

I independently expanded and symbolically checked

\[
f(f(x))-x=g(x)H(x),\qquad
H=A^2x^2+A(B+1)x+AC+B+1
=\left(Ax+\frac{B+1}{2}\right)^2+\frac{4-D}{4}.
\]

Thus \(D<4\) gives \(H>0\). At \(D=4\), its possible zero \(r=-(B+1)/(2A)\) satisfies \(g(r)=(4-D)/(4A)=0\), so it cannot introduce a proper two-cycle. If \(A=0\), positivity implies \(-1<B<1\) and the map is an affine contraction. These facts give the strict signs of \(f^2(x)-x\) on either side of \(p\), including the neutral endpoint.

The extreme-limit-point proof is valid and supplies global convergence, not merely local stability. For a nontrivial omega-limit set \(\Omega\), continuity on a compact interval gives \(f(\Omega)=\Omega\). Its extrema must satisfy \(a_0<p<b_0\), since a set confined to either side cannot supply a preimage of the appropriate extremum. Preimages \(f(u)=b_0\), \(f(v)=a_0\) satisfy \(u<p<v\). Since \(f(u)\ge v>f(p)\), there is \(w\in[u,p)\) with \(f(w)=v\). But \(f^2(w)=a_0\le u\le w\), contradicting the strict sign below \(p\). Hence every orbit, including those starting at 0 or 1, converges to the unique \(p\).

For \(0<\delta<\delta_*\), put \(t=1-2\delta\). The claimed extremal map and cycle are

\[
f_\delta(x)=\delta+t(1-x)^2,\qquad
x_\pm=\frac{2t-1\pm\sqrt{4t(1-\delta)-3}}{2t}.
\]

The radicand is \(D-4>0\), is smaller than 1, and

\[
(2t-1)^2-[4t(1-\delta)-3]
=4[(1-t)^2+t\delta]>0.
\]

Since \(2t-1>0\), these inequalities put both points strictly in \((0,1)\). Independent symbolic substitution gives \(f(x_+)=x_-\), \(f(x_-)=x_+\), and they are distinct. The heredity tensor consists of \(\delta\) and \(1-\delta\). Choosing \(\delta\) strictly between any proposed smaller threshold and \(\delta_*\) proves sharpness under the strict convention. All operators with floor at least \(\delta_*\) are regular; the absence of a counterexample at the endpoint causes no difficulty.

The Fisher–Rao proof also checks, including its domain issues.

An independent way to read Lemma 1 is as conditional variance. Take independent parents \(I,J\) with distribution \(x\), offspring \(K\) with conditional law \(Q_{ij,k}\), and scores \(u_i=h_i/x_i\). The output score is

\[
\frac{(DW(x)h)_k}{W_k(x)}
=\mathbb E[u_I+u_J\mid K=k].
\]

Conditional Cauchy–Schwarz and \(\sum_i h_i=0\) bound its squared mean by

\[
\mathbb E[(u_I+u_J)^2]
=2\sum_i h_i^2/x_i.
\]

This rederives the claimed factor 2. Symmetry is used correctly in the derivative representation. For positive \(x\), if \(W_k(x)=0\), nonnegativity forces every \(Q_{ij,k}=0\), so that derivative coordinate is identically zero. Omitting its \(0/0\) term is legitimate.

For Lemma 2, multiplying the difference of the proposed sides by \((t+2\mu)/\mu\) reduces it to

\[
\sum_k\frac{v_k^2(1-2q_k)}{q_k(\mu+tq_k)}\ge0.
\]

If \(q_k\le1/2\) throughout, every term is nonnegative. Otherwise write \(q_1=s>1/2\), \(r=1-s\). The reciprocal positive weights obey

\[
\sum_{k>1}\frac{q_k(\mu+tq_k)}{1-2q_k}
\le\frac{r(\mu+tr)}{1-2r}
\le\frac{s(\mu+ts)}{2s-1}.
\]

The denominators in the last comparison agree. Weighted Cauchy–Schwarz and \(\sum_{k>1}v_k=-v_1\) cancel the sole negative term. This verifies the mixture constant, including the sometimes essential tangent constraint. Zero coordinates are handled on the fixed support, or by a limit with zero derivative there. The equal-mass two-coordinate example attains the constant.

For the actual floor \(\mu=\min P_{ij,k}>0\), let \(t=1-m\mu\). If \(t=0\), \(V\) is constant. Otherwise \(P=\mu+tQ\) is a valid symmetric stochastic decomposition. Combining the lemmas gives exactly

\[
|DV(x)h|_{V(x)}^2\le
K^2|h|_x^2,\qquad
K^2=\frac{2(1-m\mu)^2}{1-(m-2)\mu}.
\]

The metric has distance \(d(x,y)=2\arccos\sum_i\sqrt{x_iy_i}\). The map \(x\mapsto2\sqrt{x}\) realizes the closed simplex as the nonnegative spherical orthant. This distance induces its usual topology and makes it compact and complete. The open simplex alone would not be complete; the proof does not apply Banach there.

Between positive endpoints, a shortest spherical arc stays positive. Integration along that arc gives the global Lipschitz inequality in the open simplex, and continuity extends it to the closed simplex. Alternatively, restrict this already-established inequality to the complete invariant set \(\Delta_\mu\). Every boundary start enters \(\Delta_\mu\) after one step. Thus \(K<1\) gives a unique fixed point and a common global attractor for all closed-simplex starts. No boundary or completeness gap remains.

Algebraically, \(K^2<1\) is

\[
2m^2\mu^2-(3m+2)\mu+1<0.
\]

Its smaller root, rationalized, is

\[
C_m=\frac{3m+2-\sqrt{m^2+12m+4}}{4m^2}
=\frac2{3m+2+\sqrt{m^2+12m+4}}.
\]

The inequality holds for \(C_m<\mu\le1/m\). At \(\mu=1/(2m)\), \(K^2=m/(m+2)<1\), proving the strict improvement. For \(m=2\), \(C_2=(2-\sqrt2)/4=0.1464466094\ldots\). It exceeds the true \(\lambda_2\), as a nonsharp sufficient bound should, and lies below the printed \(0.1771243445\ldots\).

The higher-dimensional lower bound has exact witnesses.

I reconstructed the offspring table independently for all unordered parent pairs, with classes \(A=\{1\}\), \(C=\{3\}\), \(B=\{2,4,\ldots,m\}\). Its deterministic offspring are 3 for AA/AB, 1 for CC/CB, and 2 for AC/BB. For \(0<\ell<L_m\), the tensor \(P=\ell+(1-m\ell)Q\) has exactly the two coefficient values

\[
\ell,\qquad1-(m-1)\ell,
\]

and each offspring distribution sums to 1. Thus its minimum is exactly \(\ell>0\), including coefficients for the extra types.

Put \(t=1-m\ell\), \(z=1/t-1\), \(s=2-1/t\). Direct elimination from the swap equations gives \(u+v=s\), \(uv=\ell/t\), and

\[
(u-v)^2=s^2-4\ell/t
=\frac{(m+1)(2t-1)^2-1}{mt^2}.
\]

This is positive in the required range, since \(t>(1+1/\sqrt{m+1})/2\). Both roots are positive. Moreover \(z/\ell=m/t>m-2\), so the neutral coordinate \(z-(m-3)\ell\) is positive. The points

\[
X=(u,z-(m-3)\ell,v,\ell,\ldots,\ell),\quad
Y=(v,z-(m-3)\ell,u,\ell,\ldots,\ell)
\]

are distinct probability vectors. The induced map satisfies

\[
a'=\ell+t(c^2+2cz),\quad c'=\ell+t(a^2+2az),
\quad z'=(m-2)\ell+t(z^2+2ac).
\]

Using \(\ell=tuv\) and \(t(1+z)=1\) proves \(a'=v,c'=u\). The remaining coordinates follow from their fixed floor and normalization. This verifies \(V(X)=Y,V(Y)=X\) for every \(m\ge3\). For any proposed threshold below \(L_m\), choose its witness floor strictly between that threshold and \(L_m\). Coalescence of the two points at \(L_m\) does not weaken this supremum argument.

The following independent exact checks include the requested dimension 5 case. In each row, \(Y\) swaps coordinates 1 and 3 of \(X\).

| \(m\) | \(\ell\) | \(X\) | Larger coefficient |
|---:|---:|---|---:|
| 3 | \(2/25\) | \(((13+\sqrt{17})/38,\ 6/19,\ (13-\sqrt{17})/38)\) | \(21/25\) |
| 4 | \(11/160\) | \(((18+\sqrt5)/58,\ 1441/4640,\ (18-\sqrt5)/58,\ 11/160)\) | \(127/160\) |
| 5 | \(7/120\) | \(((25+\sqrt{30})/85,\ 301/1020,\ (25-\sqrt{30})/85,\ 7/120,\ 7/120)\) | \(23/30\) |

SymPy verified full tensor substitution, row sums, positivity and distinctness, without approximate algebraic equality tests. Differentiating the reduced \((a-c,z)\) map independently reproduces the claim's two-step trace and determinant. For the new dimension 5 example these are \(T=91/90\), \(D=49/1600\); its Schur quantities are \(281/14400\), \(29401/14400\), \(1551/1600\), all positive. The claim's dimension 3 and 4 Schur fractions also agree exactly. Extra-coordinate tangent eigenvalues are zero. Thus all three examples are attracting proper cycles, although attraction is unnecessary for the lower bound.

Multiplying the accepted bounds by \(2m\) gives lower limit \(1-1/\sqrt{m+1}\to1\) and upper limit \(4m/(3m+2+\sqrt{m^2+12m+4})\to1\). The asymptotic statement follows without any numerical extrapolation.

The independent computations are reproducible and deliberately limited in their conclusions.

I wrote `independent_checks.py` without reading, importing, executing, or copying `claim_files/code/`. It uses an independently constructed unordered-pair tensor representation and scalar summation for output audits. The exact checks, random differentials, and random orbit data are in `data/verify.json`; the search and refinement outputs are in `data/search.json` and `data/refine.json`.

- All 22 symbolic/exact certificates passed. These include the binary identities, endpoint equation, general discriminant and upper-bound equation, plus full dimension 3/4/5 cycle and attraction checks.
- Binary screening used 1,500 coefficient triples at each of six floors, including all eight corners of each coefficient box, with nine starts per triple: 9,000 maps and 81,000 trajectories. Floors were .02, \(\delta_*\pm10^{-4}\), .12, .2 and .4. Close to the transition, 100,000 iterations were used. Below the threshold proper cycles were observed; above it every screened map converged numerically. At \(\delta_*+10^{-4}\), the maximum one-step residual was \(7.30\times10^{-13}\). Endpoint convergence is established by the exact proof, not finite iteration.
- There were 1,750 random differential checks in dimensions 2,3,4,5,10, including deterministic residual tensors with zero output coordinates. Both Fisher–Rao inequalities passed. Constant maps' roundoff-sized zero derivatives were excluded from ratio denominators.
- For \(m=3,4\), random orbit screening used floors \(L_m+10^{-4}\), \((L_m+C_m)/2\), and \(C_m+10^{-4}\). At each floor it sampled residual Dirichlet tensors with concentrations .04, .4 and 2, as well as deterministic residual tensors. This covers 4,320 tensors, including 1,440 above \(C_m\), from simplex vertices and four additional starts per tensor. No nonregular candidate survived follow-up. Three ternary tensors near \(L_3\) needed 33,000–54,000 additional iterations after an initial 1,200; their residuals then fell below \(10^{-11}\). They were slow transients. The largest final spread between starts was below \(4.3\times10^{-8}\), within the stated \(10^{-7}\) screening tolerance.
- The optimized search differs from the submission's search architecture. For fixed distinct states \(X,Y\), finding the largest tensor floor subject to \(V(X)=Y,V(Y)=X\) is a linear program. I optimized the states by differential evolution, using no tensor seed from the claim, then refined the independently found tensors by finite-difference SLSQP in the full tensor/state variables. The outer runs made 16,416 LP calls. A coordinate separation constraint prevents the optimizer from passing off a fixed point as a cycle.

| \(m\) | Required coordinate separation | Largest refined floor | \(L_m\) | \(C_m\) |
|---:|---:|---:|---:|---:|
| 3 | .04 | .0832208080094 | .0833333333333 | .1111111111111 |
| 3 | .008 | .0833288332928 | .0833333333333 | .1111111111111 |
| 4 | .04 | .0690046163934 | .0690983005625 | .0899029491994 |
| 4 | .008 | .0690945539076 | .0690983005625 | .0899029491994 |

All four refined tensors pass scalar cycle residual checks, the largest below \(8.2\times10^{-14}\). None exceeds \(L_m\); hence none exceeds \(C_m\). Attempts to impose floors \(L_m+10^{-4}\) and \(C_m+10^{-4}\) on the independently optimized fixed pairs were infeasible. Those are pair-specific LP results, not global infeasibility proofs. The searches do not exclude long cycles, nonperiodic invariant sets, tiny basins, or a different family in \((L_m,C_m]\). The contraction proof excludes all nonregularity strictly above \(C_m\).

Orbit iteration renormalizes roundoff back to \(\sum x_i=1\). Without this, the degree-two homogeneous extension amplifies normal errors and can produce false overflow or decay outside the simplex. The code checks finiteness and nonnegativity. This is a numerical hygiene measure, not a modification of the exact simplex dynamics.

To reproduce, from this directory:

```sh
python3 independent_checks.py verify > data_verify_stdout.txt 2>&1
python3 independent_checks.py search > data_search_stdout.txt 2>&1
python3 independent_checks.py refine > data_refine_stdout.txt 2>&1
```

These overwrite the corresponding referee outputs. Run with nice 10; this session already inherited it, and every recorded numerical process reports nice 10. The script sets BLAS/OpenMP/Accelerate limits to one thread and requests one HiGHS thread. Numerical jobs used at most two concurrent single-thread workers, no agents, and under 124 MB peak RSS per process, comfortably below the requested limits. No PDFs, page images or scans were saved; nothing was published or pushed. All saved source files are plain text. The supplied claim files were left unchanged.

The literature supports a useful partial result, with qualified novelty.

The most relevant later general criterion I could fully read is [Fasino–Tudisco (2020), arXiv:1907.04841v3](https://arxiv.org/html/1907.04841v3). Theorem 6.1 gives the optimal one-step \(\ell^1\) coefficient, Corollary 6.2 recovers the sufficient floor \(1/(2m)\), and Corollary 7.2 gives a Hilbert-projective criterion. None states the present \(C_m\) formula or an exact unrestricted threshold.

[Karim–Hamzah–Ganikhodjaev (2022)](https://mjms.upm.edu.my/fullpaper/2022-December-16-4/Hamzah,%20N.%20Z.%20A.-727-737.pdf), Malaysian J. Math. Sci. 16(4), 727–737, uses exactly the binary mixed-term normalization here. Its discriminant and second-iterate factors on pp.731–733 agree with the independent algebra above; Theorem 3.1 distinguishes regularity for \(D<4\) from proper cycles for \(D>4\), citing Lyubich's 1974 chapter. It does not explicitly calculate the uniform coefficient-floor threshold or correct Theorem 7. Its endpoint omission is supplied by the audited proof. The underlying binary dynamics should therefore not be advertised as new.

[Saburov–Yusof (2018), MFAT 24(3), 255–264](https://mfat.imath.kiev.ua/article/2018/03/mfat_2018_03_1085.pdf), gives strictly positive operators with multiple fixed points and examples with a repelling unique fixed point. It does not determine the universal coefficient floor; its nonconvergent Example 3.4 uses floor \(\varepsilon<.001\). These precedents show that positivity alone and uniqueness alone are insufficient, but do not subsume the claimed bounds.

[Saburov–Saburov, Russian Math. Surveys 80:5 (2025), 931–933](https://www.mathnet.ru/php/archive.phtml?jrnid=rm&option_lang=eng&paperid=10256&wshow=paper), DOI 10.4213/rm10256e, directly formulates the same unrestricted threshold, records \(\alpha_m\le1/(2m)\), and says its exact least value remains unknown. Its Theorem 1 settles threshold zero only within cubic doubly stochastic matrices. The English publication date is 12 January 2026. That extra structural condition is not present in E0065.

[Saburov (2026), Functional Analysis and Its Applications 60, 312–318](https://link.springer.com/article/10.1134/S1234567826030109), published 2 October 2026, treats global stability and contraction for classes of polynomial stochastic operators. I verified the publisher abstract, dates and bibliography, including its citations to the 1988 criterion and 2025 paper. Its full body is subscription-only. Its abstract does not announce an exact unrestricted threshold; that is insufficient evidence to exclude an improvement somewhere in the unread body.

Searches also covered Rozikov, Mukhamedov, Jamilov/Zhamilov and Khamraev, including later F-stochastic, non-Volterra, partition-based and doubly stochastic work. Accessible examples are restricted classes, rather than a determination of the uniform floor for every QSO. Exact queries, access limitations and source notes are recorded in `sources/literature_search.txt`. No exact unrestricted \(\lambda_m\), \(m\ge3\), or prior occurrence of the particular \(L_m,C_m\) formulas was located in accessible sources. This is a bounded literature finding, not proof of absence.

The potential new value is the explicit all-dimensional positive-cycle lower bound, the Fisher–Rao upper bound, and the sharp leading asymptotic constant. The binary correction is mathematically established under the surveys' definitions; priority for that correction is unconfirmed. The derivative estimate itself is an elementary information-contraction calculation, so the useful contribution is its application with the sharp uniform-mixture estimate. The exact finite-dimensional thresholds for every \(m\ge3\) remain unresolved by this submission and by this referee audit.

Task: “You are an independent referee ... Break it if it is wrong.” Received 2026-11-13 approximately 09:18 Asia/Tbilisi; exact message timestamp unavailable.
