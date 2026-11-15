MINOR

The substantive partial claim survives. Madaule proves the stated maximum/derivative-chaos limit for his compactly supported star-scale cutoff model in every fixed integer dimension. The square-lattice two-dimensional DGFF maximum and its critical-LQG mixing measure are also established. The alternating-rescaling counterexample is mathematically valid for an unrestricted cutoff interpretation. I found no fatal normalization error, erroneous theorem application, or numerical discrepancy.

The main correction is historical and interpretive: the **published** Rhodes–Vargas review explicitly restricts its conjecture to star-scale invariant limiting fields, acknowledges Madaule's result, and already explains the DGFF conformal-radius weight. The submission checks the earlier arXiv formulation without reporting these changes. Its counterexample identifies an inadequacy of unrestricted approximation criteria; it does not refute the intended canonical-cutoff conjecture. This is useful literature and normalization work, with an elementary cautionary example, rather than a new resolution of the standard maximum problem.

All claim locations below refer to `claim_files/REPORT.md`, using its line numbers. The submitted files were not changed.

1. **Omitted published formulation and status (lines 3–34, 88–102, 200–202).** The arXiv transcription of Conjecture 6.5 is accurate. However, the published review, *Probability Surveys* 11 (2014), 315–392, has Conjecture 6.3 on printed pp. 369–370 / PDF pp. 55–56. It adds the condition “If X is a star scale invariant log-correlated Gaussian field”, uses (n\to\infty), and numbers the transform (6.11). Printed p. 370 acknowledges Madaule and describes the proposed DGFF mixing measure as conformal-radius squared times derivative chaos. **Fix:** distinguish the two versions, retain the broad reading as an explicitly additional interpretation, and do not present the radius correction or recognition of Madaule as discoveries missing from the published review. The limiting field in the counterexample is itself star-scale invariant, so the new restriction on (X) alone does not forbid it; the decisive distinction is the cutoff scheme. [Published review](https://ftp.icm.edu.pl/packages/EMIS/journals/PS/images/getdoc25a8.pdf?article=218&id=1036&mode=pdf), saved in `sources/rhodes_vargas_published.txt`.

2. **Admissibility of the broad cutoff reading needs a source-based check (lines 28, 115–165).** The submission proves convergence against test functions and covariance convergence, but does not check the review's available definition of smooth approximation: Definition 3.3, arXiv PDF p. 20, renumbered Definition 3.4, published p. 336 / PDF p. 22. This check succeeds; I give it below. **Fix:** add that check and continue to exclude any assertion that the example is a fixed-mollifier or independent-scale-increment cutoff. Those exclusions are already correctly stated at line 165. Thus this is a repairable exposition gap, not an invalid counterexample. [ArXiv review](https://arxiv.org/abs/1305.6221).

3. **Acosta's domain and publication type need to remain explicit (line 46).** The thesis theorem proved there is for the coefficient-one Dirichlet continuum GFF on the unit square, extended for mollification as specified in its setup, not a theorem stated for all planar domains. Its mollifier is nonnegative, smooth, compactly supported and has integral one. **Fix:** add the square-domain restriction. A publicly deposited 2016 PhD thesis is a legitimate written result, but should be distinguished from a refereed journal theorem when saying “in print.” The submission correctly identifies it as a thesis and correctly does not identify its (Z) with continuum derivative chaos by fiat. [Acosta thesis, Chapter 6](https://conservancy.umn.edu/server/api/core/bitstreams/2cb19574-ecbc-49e6-a075-e8eb09437317/content).

4. **Literature coverage is incomplete, although its negative conclusion is appropriately qualified (lines 200–202).** Add Schweiger's four-dimensional membrane-model theorem (2020), Biskup's survey, and the Bertacco–Hairer papers from 2025–2026. The last are especially pertinent to general convolution approximations. They establish substantially more chaos universality, but do not supply the missing maximum theorem: Remark 1.14 of the accepted Bertacco–Hairer uniqueness paper explicitly leaves that extension for further work. **Fix:** add these results and retain the distinction between chaos, maximum convergence, and identification of the mixing mass. Details and exact locations appear below. [Schweiger](https://arxiv.org/abs/1903.02522), [Biskup](https://arxiv.org/abs/1712.09972), [Bertacco–Hairer](https://arxiv.org/abs/2504.07552).

5. **Source-package limitation (lines 7, 36–56, 179; supplied `claim_files/` tree).** The supplied bundle contains report, log, code and data, but no `claim_files/sources/`. Its local source links therefore cannot be followed in this bundle. This does not establish that the original run lacked those files. **Fix:** include the source archive when circulating the report. For this audit I independently retrieved the papers into this directory's `sources/`, with provenance and page boundaries. The live-URL citations and central page references checked out.

There are no additional mathematical corrections from this audit. In particular, the Gamma sign, constant conversion, DGFF spatial weight, and distinction between a discrete derivative-type limit and continuum chaos are correct.

The exact source question and its interpretation

The original source identified by the submission is Rhodes–Vargas, *Gaussian multiplicative chaos and applications: a review*, arXiv:1305.6221v1, Section 6.4, pp. 52–53. The complete retrieved text is `sources/rhodes_vargas_arxiv.txt`. For a cutoff approximation (X_n) of a centered Gaussian distribution with covariance

\[
K(x,y)=\log_+\frac{T}{|x-y|}+g(x,y),\qquad g\text{ bounded and continuous},
\]

and (c_n=\operatorname{Var}(X_n)), Conjecture 6.5 states

\[
\sup_{x\in[0,1]^d}X_n(x)-\sqrt{2d}\,c_n
 +\frac{3}{2\sqrt{2d}}\log c_n\ \longrightarrow\ G_d,
 \qquad\text{in law as }t\to\infty,
\]

\[
\mathbb E[e^{-qG_d}]
=c^{-q}\Gamma\!\left(1+\frac q{\sqrt{2d}}\right)
 \mathbb E\!\left[(M'([0,1]^d))^{-q/\sqrt{2d}}\right],\qquad c>0.
\]

The (n/t) switch is in this preprint. No (q)-range is specified there. (M') is the critical derivative chaos of Section 6.1. The logarithmic covariance coefficient is one. The publication changes are recorded in item 1 above. Both complete source versions are retained; the displayed question was not reconstructed from a secondary summary. [Original source](https://arxiv.org/abs/1305.6221).

The broad reading is defensible as a literal reading of the preprint, which introduces general cutoff approximations and does not impose a universal microscopic normalization. It is not the only reasonable reading, nor evidence that the authors intended a theorem for adversarial cutoff sequences. The source's canonical star-scale motivation and warning about poorly chosen cutoffs matter. The fair conclusion is: distributional convergence of the underlying fields, even with smoothness and a bounded covariance discrepancy, does not by itself imply the proposed centered-maximum law. Calling that a counterexample to an **unrestricted interpretation**, as the submission does, is justified. Calling it a disproof of Madaule's theorem or of fixed-mollifier universality would not be.

Theorem-by-theorem audit

Every page number below is one-based PDF pagination of the named locally saved version unless a printed page is specified. Different versions have different pagination; I did not infer journal pages by adding an offset to a preprint. All the following papers were retrieved independently, including the arXiv texts of the principal citations. The manifest `sources/manifest.txt` records source URLs, page counts and hashes. The table records the actual hypotheses relevant to the submission's use, not a claim that the theorem holds under the generic phrase “log-correlated.”

| Result and exact location | Hypotheses and conclusion checked; disposition |
|---|---|
| **Madaule**, AIHP 51 (2015), 1369–1431; Theorem 1.1, printed p. 1371 / published PDF p. 3; model and (1.4), printed p. 1370 / PDF p. 2. Also arXiv:1307.1365v3, Theorem 1.1, p. 3. Local `madaule_published.txt`, `madaule_arxiv.txt`. | Fixed (d\ge1); stationary covariance (K_t(h)=\int_0^t k(e^u h)du), (k\in C^1) a covariance kernel, (k(0)=1), supported in the unit sup-norm box. Canonical scale process. With (alpha=\sqrt{2d}), the limit CDF is (mathbb E\exp[-C_*M'([0,1]^d)e^{-alpha x}]). Its derivative expression is exactly ((alpha t-X_t)e^{alpha X_t-dt}dx); variance is (t). **Covers the submission exactly.** The remark about decaying noncompact kernels is not the proved theorem. [Paper](https://arxiv.org/abs/1307.1365). |
| **Ding–Roy–Zeitouni**, Ann. Probab. 45 (2017), 3886–3928; arXiv:1503.04588v1, assumptions pp. 2–3, Theorems 1.3–1.4 pp. 3–4. Local `ding_roy_zeitouni.txt`. | Fixed (d\ge1), Gaussian arrays on (V_N). (A.0) requires the variance upper bound and increment bound including the absolute variance-difference term; (A.1) requires uniform bulk log-correlation. (A.2) requires a single microscopic limit (log N+f(x)+g(u,v)), locally uniformly in bulk (x) and bounded offsets. (A.3) requires locally uniform macroscopic off-diagonal convergence to a continuous (h(x,y)). Theorem 1.3 centers by the expectation; Theorem 1.4 additionally gives convergence with (m_N=alpha\log N-3\log\log N/(2alpha)), (Z_N\Rightarrow Z>0), and CDF (mathbb E e^{-eta_*Ze^{-alpha x}}). **A broad maximum theorem already in print.** Its (Z) is not identified there with an arbitrarily specified continuum (M'). The submission gets this distinction right. [Paper](https://arxiv.org/abs/1503.04588). |
| **Bramson–Ding–Zeitouni**, CPAM 69 (2016), 62–123; arXiv:1301.6669v5, Theorem 1.1 p. 2, Theorem 2.5 p. 7. Local `bramson_ding_zeitouni.txt`. | Square-lattice DGFF in a square, Dirichlet boundary, killed-walk normalization. Theorems give the nondegenerate maximum limit and its positive random-mass Gumbel mixture. (g_0=2/\pi), centering (2\sqrt{g_0}\log N-3\sqrt{g_0}\log\log N/4), rate (\sqrt{2\pi}). **Correctly used**, including the rescaling by (1/\sqrt{g_0}). This theorem alone does not identify the mass as continuum LQG. [Paper](https://arxiv.org/abs/1301.6669). |
| **Biskup–Louidor**, *Extreme local extrema*, CMP 345 (2016), 271–304; arXiv:1306.2602, Theorem 1.1 and Corollary 1.2 p. 2, Theorem 1.3 p. 3, Theorem 1.4 p. 4. Local `biskup_louidor_extreme.txt`. | Same DGFF; (r_N\to\infty), (r_N/N\to0). Local-maximum process converges to a Cox process with intensity (Z(dx)e^{-alpha_0h}dh), (alpha_0=2/\sqrt{g_0}). Corollary 1.2 gives the maximum law with (Z([0,1]^2)/alpha_0) in the exponent. Theorem 1.3 gives moments of order (p<1); Theorem 1.4 constructs a coarse-field derivative-type approximation. **Correctly used without claiming final continuum identification from this paper.** [Paper](https://arxiv.org/abs/1306.2602). |
| **Biskup–Louidor**, *Conformal symmetries*, CMP 375 (2020), 175–235; arXiv:1410.4676 and author-final manuscript: Theorem 2.1 p. 5, Theorem 2.8 pp. 8–9, Theorem 2.9 p. 9, Theorem 6.1 p. 36. Local `biskup_louidor_conformal.txt`, `biskup_louidor_conformal_final.txt`. | Nonempty bounded open planar domains with finitely many connected components and finitely many boundary components of positive diameter. Lattice approximations must satisfy (2.1)–(2.2); this is not an arbitrary graph theorem. Theorem 2.9, (2.26), identifies (Z^D) in law with a scalar multiple of the heat-kernel critical-LQG measure in (2.23)–(2.25), including (operatorname{rad}_D^2). Theorem 6.1 is a truncated derivative representation, not by itself a shortcut removing those truncations. **The submission's theorem numbers, pages and qualification are correct.** [Author-final paper](https://www.math.ucla.edu/~biskup/PDFs/papers/GFF-General-final.pdf). |
| **Acosta**, EJP 19 (2014), article 90; Theorem 1.1, published PDF p. 2; arXiv:1311.2000, p. 1. Local `acosta_published.txt`, `acosta.txt`. | Continuous fields on ([0,1]^d), covariance within a uniform constant of (-\log(\epsilon\vee|x-y|)), plus short-distance increment control (1.2). Gives uniform exponential tails for the absolute recentered maximum, hence tightness. **Does not prove convergence.** The submission correctly separates this from the thesis. [Paper](https://arxiv.org/abs/1311.2000). |
| **Acosta thesis**, Minnesota, May 2016; setup printed pp. 41–42 / PDF pp. 50–51; Theorems 6.1.1–6.1.2, printed p. 43 / PDF p. 52. Local `acosta_thesis.txt`. | Coefficient-one continuum Dirichlet GFF for the unit square, convolved with nonnegative smooth compactly supported unit-mass (	heta). The theorem is precisely (Theta_r^*-(2r-3\log r/4)+eta_	heta\Rightarrowmu^*); (mu^*((-\infty,x])=mathbb E e^{-Ze^{-2x}}). **Correct convergence and sign; narrow the domain description.** No automatic identification of (Z) with the review's fully variance-subtracted chaos. [Thesis](https://conservancy.umn.edu/server/api/core/bitstreams/2cb19574-ecbc-49e6-a075-e8eb09437317/content). |
| **DRSV derivative martingale**, Ann. Probab. 42 (2014), 1769–1808; arXiv:1206.1671 journal reprint, Theorem 4 pp. 10–11, Conjecture 12 p. 16. Local `drsv_derivative.txt`. | Star-scale kernels under Section 2's conditions. Theorem 4 gives a positive, atomless, full-support derivative-measure limit. The maximum assertion is still Conjecture 12 in this paper. **Correctly used as chaos construction, not a maximum theorem.** [Paper](https://arxiv.org/abs/1206.1671). |
| **DRSV renormalization**, CMP 330 (2014), 283–330; arXiv:1212.0529v3, Theorem 5 p. 8, Corollary 6 p. 9, Theorem 10 and Definition 11 p. 12. Local `drsv_renormalization.txt`. | Star-scale chaos, and separate heat-kernel planar-GFF construction. (sqrt t M_t^alpha\to\sqrt{2/\pi}M') in probability; moments of (M') for (p<1). Definition 11, (23), includes conformal-radius squared in critical Liouville measure. **Constants, negative-moment use and radius weight in the submission agree.** [Paper](https://arxiv.org/abs/1212.0529). |
| **Junnila–Saksman**, EJP 22 (2017), article 11; predecessor arXiv:1506.05099v2, Theorem 1.1 p. 3. Local `junnila_saksman.txt`. | Hölder-regular approximants on a compact doubling metric space; uniformly bounded covariance difference, uniformly vanishing difference off each fixed diagonal neighborhood, and an existing atomless limiting chaos. Gives convergence of the other chaos to the same law. **A chaos-transfer theorem, not a supremum-transfer theorem.** Version and title difference are correctly disclosed by the submission. [Preprint](https://arxiv.org/abs/1506.05099). |
| **Junnila–Saksman–Webb**, Ann. Appl. Probab. 29 (2019), 3786–3820; Theorems A–B, printed pp. 3788–3789 / institutional-cover PDF pp. 4–5; Theorems 5.3–5.4, printed pp. 3808–3809 / PDF pp. 24–25. Local `junnila_saksman_webb_published.txt`; arXiv:1808.06838v3 also retained. | Covariance differences with local Sobolev regularity exceeding (d) permit a Hölder remainder coupling. The local almost-star-scale decomposition has independence; the global comparison generally does not. Critical-chaos convergence, including derivative normalization, follows for regular covariance remainder. Remark 5.6 / Section 5.2, printed p. 3812 / PDF p. 28, leaves maximum transfer unresolved. **Correctly used.** [Published reprint](https://acris.aalto.fi/ws/portalfiles/portal/40601990/SCI_Junnila_et.al_Decompositions.AAP1492_1.pdf). |
| **Powell**, EJP 23 (2018), article 31; arXiv:1704.06058, Theorems 1.1–1.2 p. 3. Local `powell.txt`. | Bounded simply connected planar-GFF domains; separately star-scale fields in arbitrary fixed (d). Mollifiers satisfy (1.2), with Hölder density additionally in the star-scale assertion. Gives derivative-chaos convergence and consistency of constructions. **No maximum theorem is claimed or obtained.** [Paper](https://arxiv.org/abs/1704.06058). |
| **Schweiger–Zeitouni**, CPAM 77 (2024), 2778–2859; arXiv:2205.07210v1, Theorems 1.1–1.2 p. 2, Assumption 1.3 pp. 3–4, Theorem 1.4 p. 4. Local `schweiger_zeitouni.txt`. | General fixed-(d) Gaussian arrays with quantitative sparsity of covariance defects, microscopic/macroscopic approximation, and local-law averaging conditions. Applications are planar iid uniformly elliptic conductances and the infinite bond-percolation cluster for (p) sufficiently near one. Gives the centered maximum mixture and derivative-type weak limit. **Correctly used**, without promoting it to arbitrary graphs or identifying its general mass with a specified continuum chaos. [Paper](https://arxiv.org/abs/2205.07210). |
| **Lacoin**, AIHP 60 (2024), 2328–2351; arXiv:2209.06683, Theorem 1.2 p. 4, Theorems 1.7–1.8 pp. 5–6. Local `lacoin.txt`. | The specified covariance decomposition with an almost-star-scale invariant part. Critical mollified, martingale, and derivative constructions converge with the stated normalizations. **Chaos, not maximum convergence.** [Paper](https://arxiv.org/abs/2209.06683). |
| **Ganguly–Nam**, CMP 406 (2025), article 87; arXiv:2302.03010v2, Theorems 1–2 pp. 4–5. Local `ganguly_nam.txt`. | Discrete arrays under Assumptions 1–2, fixed (d), inverse temperature (\beta>\sqrt{2d}). Gives Poisson–Dirichlet cluster weights and near-maximum level-set estimates. The remarks on p. 5 explicitly allow nonconvergence of the maximum under these assumptions. **The submission correctly refuses to infer absolute-height convergence from normalized Gibbs weights.** [Paper](https://arxiv.org/abs/2302.03010). |
| **Paquette–Zeitouni**, Forum Math. Sigma 13 (2025), e1; Theorems 1.1 and 1.4, published PDF pp. 3–4; Theorem 1.6 p. 5 identifies the model derivative measure. Local `paquette_zeitouni_published.txt`; arXiv:2209.06743 also retained. | C(\beta)E characteristic polynomials, (\beta>0); real/imaginary maxima have the specified random-shifted Gumbel limits. The model is not an exactly Gaussian cutoff family. **Correctly classified as an analogy, not a general Gaussian theorem.** [Published paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2DBD96407247AA6166F4AEA93319FF0E/S2050509424001294a.pdf/extremal_landscape_for_the_cbeta_e_ensemble.pdf). |
| **Ding–Gwynne–Zhuang**, arXiv:2310.03996, Theorem 1.2 p. 5. Local `ding_gwynne_zhuang.txt`. | Subcritical exponential metrics in (d\ge2), with the field and approximation specified in the paper. Gives metric tightness and subsequential metric limits. **Not a centered-maximum convergence theorem.** I found no identified joint “Ding–Gwynne–Wirth” maximum paper; the submission does not fabricate one. [Paper](https://arxiv.org/abs/2310.03996). |
| **Aïdékon–Shi**, Ann. Probab. 42 (2014), 959–993; arXiv:1102.0217 reprint, Theorem 1.1 p. 4. Local `aidekon_shi.txt`. | Boundary-case BRW, finite spine variance and integrability assumptions (1.1), (1.4), (1.5), conditioned on survival. Gives (sqrt n W_n\to\sqrt{2/(\pi\sigma^2)}D_\infty) in probability. The deterministic-offspring Gaussian BRW used in the submission meets those conditions and never becomes extinct. **Its SH normalization checks out.** [Paper](https://arxiv.org/abs/1102.0217). |

Independent normalization check

Put (alpha=\sqrt{2d}), let (E\sim\operatorname{Exp}(1)), and take it independent of a finite strictly positive mass (Z). Then

\[
G=\frac{\log(CZ)-\log E}{\alpha}
\quad\Longrightarrow\quad
\mathbb P(G\le x)=\mathbb E e^{-CZ e^{-\alpha x}},
\]

\[
\mathbb E e^{-qG}
=C^{-q/\alpha}\Gamma(1+q/\alpha)\mathbb E Z^{-q/\alpha}.
\]

This proves the plus sign in the Gamma factor and the positive sign of the logarithmic mass shift. For a finite identity one needs (q>-alpha) and the corresponding mass moment; for (q\ge0), Tonelli also permits extended expectations. DRSV supplies the required moments in Madaule's setting. The review's (c^{-q}) corresponds to (C=c^alpha). The submission does not make the invalid inference that convergence in law alone gives convergence of prelimit exponential moments.

For the DGFF, dividing heights by (\sqrt{g_0}) converts the centering to (2\log N-3\log\log N/4). The mixture rate becomes (\sqrt{2\pi}\sqrt{2/\pi}=2). Independently, integrating the Cox height intensity above (x) gives (Z^D(D)e^{-alpha_0x}/alpha_0), so the extra rate factor is a scalar constant. By contrast, the factor (\operatorname{rad}_D(x)^2) is spatial and cannot generally be absorbed into a scalar.

I also checked the submission's identity (4) directly. If (\operatorname{Var}X_t(x)=t+f_t(x)), then

\[
(\alpha t-X_t)e^{\alpha X_t-dt}
=e^{df_t}(\alpha\operatorname{Var}X_t-X_t)e^{\alpha X_t-d\operatorname{Var}X_t}
 -\alpha f_t e^{df_t}e^{\alpha X_t-d\operatorname{Var}X_t}.
\]

The transfer argument is valid under its expressly stated uniform convergence, total-variation tightness, and vanishing-critical-chaos assumptions. The submission appropriately does not infer total-variation tightness merely from individual weak tests. The DGFF identification has independent support in the actual BL and DRSV theorems; it does not depend on an unproved application of this conditional lemma.

Counterexample checked line by line

Let (phi) be a nonzero nonnegative smooth radial function supported inside a ball of radius (R<1/2). Its normalized autocorrelation (k) in claim line 117 is smooth, radial and nonnegative, with (k(0)=1). Positive definiteness follows directly from

\[
\sum_{i,j}c_i\overline{c_j}k(x_i-x_j)
=\frac{1}{\|\phi\|_2^2}\int\left|\sum_i c_i\phi(z+x_i)\right|^2dz\ge0.
\]

Its support is contained in the Euclidean ball of radius (2R<1), hence also in Madaule's required box. Cauchy–Schwarz gives (|k|\le1). The scale-integral covariance is positive definite and has a Gaussian white-noise realization with independent scale increments. The chosen smooth kernel gives smooth versions at each finite cutoff.

For (r>0), the change of variables (v=e^u r) gives

\[
K_\infty(r)=\int_r^\infty k(v)\frac{dv}{v}.
\]

Since (1-k(v)=O(v^2)) at zero, subtracting (\log_+(1/r)) leaves a continuous bounded remainder, including at (r=0). Thus the limiting generalized field has exactly the required coefficient-one logarithmic singularity in every (d\ge1).

For a test function (f), the support condition bounds the covariance double integral at scale (u) by (C_f e^{-du}). Integrating over (u\in[t,s]) proves the claimed (L^2)-Cauchy estimate. The test-function variances are uniformly bounded. Multiplication by (a_n=1+\delta_n/n\to1) therefore preserves the same jointly Gaussian distributional limit, not merely its formal covariance.

Here is the omitted smooth-approximation check. At (epsilon_n=e^{-n}), smoothness and symmetry of (k) give (1-k(z)\le C|z|^2), hence

\[
\begin{aligned}
\mathbb E[(\widehat X_n(x)-\widehat X_n(y))^2]
&=2a_n^2\int_0^n[1-k(e^u(x-y))]du\\
&\le C(1+a)^2 e^{2n}|x-y|^2
=C(1+a)^2\epsilon_n^{-2}|x-y|^2.
\end{aligned}
\]

Together with pointwise covariance convergence, this is Definition 3.3 with exponent two. It can be extended to all sufficiently small (epsilon) by (n=\lfloor\log(1/epsilon)\rfloor). No continuity in the cutoff parameter is required by that definition. This makes the unrestricted reading more substantive than mere distributional approximation.

The covariance-error estimate in claim lines 144–149 follows from (\sup|K_n|\le n): it is at most (2a+a^2/n). At any fixed spatial separation the original covariance is uniformly bounded, and the error tends uniformly to zero. On the diagonal, however, it equals (2\delta_n+\delta_n^2/n). Thus there is no single limiting diagonal remainder. After sampling at the cutoff scale this is precisely the sort of systematic microscopic oscillation that DRZ's (A.2) excludes.

Finally, let (U_n=\sup X_n-alpha n+b\log n\Rightarrow G), (b=3/(2alpha)), as guaranteed by Madaule. Direct substitution, without a stochastic approximation, gives

\[
\widehat U_n=a_nU_n
 -\alpha\delta_n-\alpha\delta_n^2/n
 +b\left[-\frac{\delta_n}{n}\log n+2\log(1+\delta_n/n)\right].
\]

Tightness makes ((a_n-1)U_n=o_P(1)). The remaining bracket vanishes, so the odd and even limits are (G) and (G-alpha a). A real probability law cannot equal a nonzero translate of itself. **Nonconvergence is proved.** Even replacing the variance centering by the original (n)-centering gives two different limits, now (G) and (G+alpha a); this is not rescued simply by renaming the variance parameter.

The example does not satisfy canonical independent scale increments. Already at one spatial point,

\[
\operatorname{Cov}(\widehat X_{n+1}-\widehat X_n,\widehat X_n)
=a_n(a_{n+1}-a_n)n\ne0
\]

at parity changes. It is also not a fixed normalized mollifier of the field. These observations explain, rather than conceal, why it does not contradict the positive results. Its logical value is to show that an explicit cutoff hypothesis is indispensable.

Independent computations

I wrote `independent_checks.py` without importing or executing any file in `claim_files/code/`. Results are in `data/independent_checks.json`.

- Recomputed all 8,192 CSV records in eight dimension/depth groups, checked trial uniqueness, and independently refitted all eight constants using the stated 256/384/384 partition. Medians, means, sample standard deviations, both CDF distances, mass medians and counts of nonpositive derivative sums agree with the submitted JSON; largest discrepancy is (5.56\times10^{-16}).
- At the largest depths the independent mixture/plain distances are 0.02705542188604959 / 0.17550339308159585 for (d=1), and 0.05873398660981721 / 0.16263683797811715 for (d=2). These are descriptive finite-sample values, not a proof of the limit law.
- Reintegrated the Gamma identity in exponential coordinates for (d=1,2,3), (q=0.5,1,2). Maximum absolute discrepancy was (1.46\times10^{-13}). Checked the perturbation identity by direct and expanded formulas in (d=1,2,3,10) at four cutoff sizes.
- Ran fresh, independent 256-tree Gaussian BRW samples in (d=1,2). This checks the normalization and the possible sign of finite derivative sums, not a Euclidean-field maximum. Re-derived the SH proxy using (V_v=alpha(alpha t-S_v)), spine variance (alpha^2\log2), and the usual derivative sum (alpha D_n); the proxy is indeed (sqrt{\pi t/2}\sum e^{alpha S_v-2dt}).
- The 95% DKW number for 384 observations is 0.069305 approximately. The submitted 0.069 statement is appropriate and is explicitly not a fitted-model confidence band.

The numerical process ran at inherited nice 10 with one library thread and peak RSS 81,248,256 bytes. No submitted-code execution, high-memory calculation, or parallel worker was needed. I reproduced the mathematical computations and data summaries; I do not independently certify the original run's reported 3.65-second runtime or historical RSS.

Literature result through 13 November 2026

“Beyond star-scale and 2D DGFF” is not one wholly open case. DRZ already supplies a broad sufficient-condition theorem in every fixed dimension. Schweiger–Zeitouni extends that theory to rare covariance defects and provides genuine graph examples. A further concrete example omitted by the submission is **Schweiger, *The maximum of the four-dimensional membrane model*, Ann. Probab. 48 (2020), 714–741**: arXiv:1903.02522v2, Theorem 1.1, PDF p. 2. For its specified zero-exterior discrete-bilaplacian normalization,

\[
M_N-\pi^{-1}\log N+\frac{3}{16\pi}\log\log N
\Rightarrow\mu_\infty,\qquad
\mu_\infty(( -\infty,x])=\mathbb E e^{-\gamma_*Ze^{-8\pi x}}.
\]

The paper verifies DRZ's assumptions after coefficient-one rescaling. This is a non-star-scale, four-dimensional printed maximum theorem; it does not assert a continuum-chaos identification under every approximation. Local text: `sources/schweiger_membrane.txt`. [Paper](https://arxiv.org/abs/1903.02522).

**Biskup's survey**, *Extrema of the two-dimensional Discrete Gaussian Free Field*, published in the SSPROB proceedings (2020), arXiv:1712.09972v4, Theorem 10.3 p. 128, gives the DGFF maximum convergence; Theorem 10.30 p. 145 identifies (Z^D(dx)=c\operatorname{rad}_D(x)^2\mu_\infty^{D,alpha}(dx)) in law. This independently confirms the submission's normalization distinction. The survey treats the planar DGFF, not all Gaussian fields. Local text: `sources/biskup_survey.txt`. [Survey](https://arxiv.org/abs/1712.09972).

**Bertacco–Hairer, *Uniqueness of supercritical Gaussian multiplicative chaos***, EJP 30 (2025 volume), DOI 10.1214/25-EJP1449; accepted arXiv:2504.07552v3, Theorem A p. 4, proves stable convergence of supercritical chaos for general fields with (g\in H^s_{\mathrm{loc}}(D\times D)), (s>d). Its smooth compactly supported unit-mass mollifier must additionally satisfy (A2), the Fourier moment/local-maximum conditions on p. 2. For (d=2), an even nonnegative such mollifier satisfies them. Remark 1.14 on p. 5 explicitly leaves extending Madaule's maximum result to convolution approximations for future investigation. This is important new general-cutoff literature but **not** a maximum theorem. Local text: `sources/bertacco_hairer_uniqueness.txt`. [Accepted paper](https://arxiv.org/abs/2504.07552), [institutional publication record](https://www.epfl.ch/labs/propde/publications/).

Their companion ** *How does the supercritical GMC converge?***, arXiv:2504.06956v2, revised April 2026, works with a smooth radial compactly supported star-scale seed. Theorems A–B p. 8 describe the near-extremal cluster field; Theorem C p. 11 gives stable supercritical-chaos convergence under its extra-field hypotheses (W1)–(W4). These are substantial extremal/chaos developments within that setup, not a theorem for all cutoff approximations of all log-correlated fields. Local text: `sources/bertacco_hairer_extremal.txt`. [Paper](https://arxiv.org/abs/2504.06956).

A 2026 search also found **Xie**, arXiv:2606.19207v2, now titled *Extrema of cooling branching Brownian motion and related Gaussian fields*. Its Theorem 1.1, PDF p. 5, gives tightness with a different centering for the cooling profile (alpha\in(0,1/2]), (d\ge2). This is not the fixed coefficient-one logarithmic covariance class in the question. The revised title and assumptions matter; its non-Gumbel discussion should not be mistaken for a counterexample in that class. Local text: `sources/xie_2026.txt`. [Current primary source](https://arxiv.org/abs/2606.19207).

The search covered the requested authors, exact cited titles, centered maxima, continuum convolution/mollifier approximations, and 2024–2026 extensions. Critical-chaos uniqueness, supercritical-chaos convergence, normalized Gibbs weights, and metric tightness cannot be substituted for a centered-maximum limit. In particular, passing to zero temperature after a chaos limit needs a justified interchange of limits and control of peak neighborhoods; none of the cited chaos theorems alone grants it.

The printed resolution is therefore precise: Madaule's canonical compact-support star-scale model, the square-lattice planar DGFF with the correct critical-LQG mass, and many further discrete arrays satisfying DRZ or its extensions have the predicted maximum law. Acosta adds a written fixed-mollifier continuum-GFF result for the square. The unrestricted approximation assertion is false. For additional specified continuum cutoff classes or graph classes, the necessary covariance conditions and identification of the mixing measure must actually be proved. The checked literature does not supply the universal continuum fixed-mollifier maximum/critical-chaos theorem for all regular covariance remainders; the Bertacco–Hairer remark explicitly distinguishes this from their general chaos theorem. This is a bounded literature finding, not a proof that every uncited case remains open. There is no well-posed single “all general fields” residual problem until the cutoff and normalization are specified.

Task: “You are an independent referee… Break it if it is wrong.” Received 2026-11-13, 11:16 +04 (Asia/Tbilisi).
