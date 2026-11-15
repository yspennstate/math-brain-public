PARTIAL

D0065 — Rhodes–Vargas Conjecture 6.5. Literature and normalization audit, 13 November 2026.

The maximum/derivative-chaos conjecture is resolved in the literature for Madaule's star-scale invariant fields in every integer dimension d ≥ 1. The two-dimensional square-lattice DGFF is also settled, with its limiting intensity identified as critical Liouville measure. These are substantial resolutions of the original problem, not new results of this report. The label PARTIAL refers to the full scope requested here: the review does not define a universal cutoff class, and the checked theorems do not establish its informal extension to every approximation or arbitrary refining graph. Moreover, the nonstationary DGFF normalization requires a spatial weight. A complete elementary counterexample below shows that convergence actually fails under an unrestricted interpretation of approximation to the same generalized field. It does not contradict Madaule or the DGFF results.

The exact source is saved, as plain text, in [sources/rhodes_vargas_1305.6221.txt](sources/rhodes_vargas_1305.6221.txt). Page markers refer to the PDF, starting at one; no PDF or paper image is retained. The mathematical statement on PDF/printed p. 53 is:

\[
\boxed{\sup_{x\in[0,1]^d}X_n(x)-\sqrt{2d}\,c_n
 +\frac{3}{2\sqrt{2d}}\ln c_n\longrightarrow G_d,
 \qquad\text{in law as }t\to\infty,}
\]

\[
\boxed{\mathbb E[e^{-qG_d}]
 =\frac{1}{c^q}\Gamma\left(1+\frac q{\sqrt{2d}}\right)
 \mathbb E\left[M'([0,1]^d)^{-q/\sqrt{2d}}\right],\qquad c>0.}
 \tag{review 6.12}
\]

This transcribes Conjecture 6.5, including its switch from n to t in the limit. Its full surrounding wording is in the saved source, PDF p. 53. The displayed conjecture does not specify the range of q. The finite Laplace-transform statement below uses q ≥ 0; extension to negative q needs the stated moment conditions.

The setup is on pp. 52–53: X is centered, with covariance (2.12),
\[
K(x,y)=\ln_+\frac{T}{|x-y|}+g(x,y),
\]
where g is bounded and continuous. The logarithmic coefficient is one. The cutoff fields are X_n, and c_n = Var(X_n). The reference back to p. 50 is essential: stationarity makes this a number; the nonstationary case and badly chosen cutoffs are left informal. Section 6.4 supplies no list of hypotheses characterizing all allowed cutoffs. Section 6.1, Eq. (6.1), p. 43, uses the derivative convention
\[
M'_n(dx)=\bigl(\alpha\operatorname{Var}X_n(x)-X_n(x)\bigr)
 e^{\alpha X_n(x)-d\operatorname{Var}X_n(x)}dx,
\qquad \alpha=\sqrt{2d}.
\]
It is the limit, not the signed finite-cutoff expression, that is positive. The review's discussion after the conjecture suggests DGFF analogues in a domain and avoids boundary effects by considering an interior square. These remarks do not supply a theorem for general graphs. [Original review](https://arxiv.org/abs/1305.6221).

The following table separates maximum convergence from identification of the mixing mass. A page prefixed “PDF” is the page of the exact locally saved version, not an inferred journal page. Journal pagination and preprint pagination can differ.

| Work; exact result and location | Fields and dimensions | Maximum convergence and shift identification |
|---|---|---|
| Madaule, *Maximum of a log-correlated Gaussian field*, AIHP 51 (2015), 1369–1431. Theorem 1.1, printed p. 1371 / published PDF p. 3; hypotheses and Eq. (1.4), p. 1370 / PDF p. 2. [Published source](https://www.numdam.org/item/10.1214/14-AIHP633.pdf); local `madaule_published.txt`. | Every integer d ≥ 1. Stationary scale cutoffs with covariance K_t(x−y)=∫₀ᵗ k(eᵘ(x−y))du, k a C¹ covariance kernel, k(0)=1, supported in the unit box for the sup norm. Use the Gaussian process with independent scale increments. | **Yes, including the actual derivative chaos.** Var X_t(x)=t exactly. Theorem gives F(x)=E exp(−C* M'([0,1]^d)e^(−αx)) after replacing its z by −x. Its derivative expression is exactly (αt−X_t)e^(αX_t−dt)dx. Hence review (6.12) holds with c=(C*)^(1/α). The remark about rapidly decreasing long-range kernels is a proposed relaxation, not part of the proved theorem. |
| Ding–Roy–Zeitouni, *Convergence of the centered maximum of log-correlated Gaussian fields*, Ann. Probab. 45 (2017), 3886–3928. Theorems 1.3 and 1.4; saved arXiv:1503.04588v1 PDF pp. 3–4. [Primary source](https://arxiv.org/abs/1503.04588); local `ding_roy_zeitouni.txt`. | Fields indexed by V_N={0,…,N−1}^d, every fixed integer d ≥ 1. Assumptions (A.0)–(A.3): variance/increment bounds; bulk log-correlation; locally uniform microscopic covariance asymptotics; locally uniform macroscopic off-diagonal covariance convergence. | **Yes**, with m_N=α log N−3/(2α) log log N and F(x)=E exp(−β* Z e^(−αx)). Theorem 1.4 proves convergence in law of the explicitly defined derivative-type Z_N to Z>0. Its identification with a particular continuum, fully variance-subtracted M' is not automatic. Gamma identity holds with Z; replacement by the review's M' requires a normalization/approximation argument. |
| Bramson–Ding–Zeitouni, *Convergence in law of the maximum of the two-dimensional discrete Gaussian free field*, CPAM 69 (2016), 62–123. Theorem 1.1 and Theorem 2.5; saved arXiv:1301.6669v5 PDF pp. 2 and 7. [Primary source](https://arxiv.org/abs/1301.6669); local `bramson_ding_zeitouni.txt`. | Zero-boundary DGFF in a square of Z², d=2. Covariance is the killed simple-random-walk Green function; logarithmic coefficient g₀=2/π. | **Yes**, with m_N=2√g₀ log N−(3/4)√g₀ log log N. Theorem 2.5 gives F(x)=E exp(−α* Z e^(−√(2π)x)). It describes a positive random mixing mass, without by itself identifying it with continuum critical chaos. Divide the field by √g₀ to obtain logarithmic coefficient one and Gumbel rate 2. |
| Biskup–Louidor, *Extreme local extrema of two-dimensional discrete Gaussian free field*, CMP 345 (2016), 271–304. Theorems 1.1, 1.3, 1.4; saved arXiv:1306.2602 PDF pp. 2, 3, 4. [Primary source](https://arxiv.org/abs/1306.2602); local `biskup_louidor_extreme.txt`. | Square-lattice zero-boundary DGFF, d=2. Local maxima at radii r_N→∞, r_N/N→0. | **Yes, as part of convergence of the extremal process.** Cox intensity Z(dx)e^(−α₀h)dh, α₀=2/√g₀. Theorem 1.4 constructs Z as a limit of coarse-field derivative-martingale-like measures. Theorem 1.3 gives moments of its total mass of every order p<1, including all negative orders. This paper alone is not the final equality with continuum critical LQG. |
| Biskup–Louidor, *Conformal symmetries in the extremal process of two-dimensional discrete Gaussian Free Field*, CMP 375 (2020), 175–235. Theorems 2.1, 2.8, 2.9 and 6.1; author's final manuscript PDF pp. 5, 8–9, 36. [Author source](https://www.math.ucla.edu/~biskup/PDFs/papers/GFF-General-final.pdf); local `biskup_louidor_conformal.txt`. | Lattice approximations of bounded planar domains with finitely many nondegenerate boundary components, precisely the domain class in Section 2.1. d=2. | **Yes, and critical LQG identification is proved.** Theorem 2.9, Eq. (2.26), identifies Zᴰ in law with a constant multiple of M∞ᴰ. Equations (2.23)–(2.25) define that measure by heat-kernel cutoff, Seneta–Heyde norming, and a conformal-radius weight. This is the required completion of the DGFF mixing-mass identification, subject to the spatial normalization explained below. |
| Acosta, *Tightness of the recentered maximum of log-correlated Gaussian fields*, EJP 19 (2014), paper 90, 1–25. Theorem 1.1, published PDF/printed p. 2 (also arXiv:1311.2000 PDF p. 1). [Published source](https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/3170/3170-18890-1-PB.pdf); local `acosta_published.txt`. | Continuous fields on [0,1]^d, all integer d ≥ 1, under covariance approximation (1.1) and the short-distance increment bound (1.2). Application to the bulk mollified planar GFF. | **Tightness and exponential tail bounds only**, not convergence or identification of the limiting mass. |
| Acosta, 2016 Minnesota thesis, *Convergence in law of the centered maximum of the mollified Gaussian free field in two dimensions*. Theorems 6.1.1–6.1.2, printed p. 43 / PDF p. 52; definition of mollification pp. 41–42. [University source](https://conservancy.umn.edu/server/api/core/bitstreams/2cb19574-ecbc-49e6-a075-e8eb09437317/content); local `acosta_thesis.txt`. | Planar continuum GFF, logarithmic coefficient one, smoothed with a nonnegative C∞ compactly supported unit-mass mollifier θ. | **Yes.** Maximum minus 2r−(3/4)log r, plus a mollifier-dependent constant β_θ, converges to a mollifier-independent law. Theorem 6.1.2 gives E exp(−Z e^(−2x)). This theorem does not itself state equality of Z with the fully variance-subtracted M' in the review. |
| Duplantier–Rhodes–Sheffield–Vargas, *Critical Gaussian multiplicative chaos: convergence of the derivative martingale*, Ann. Probab. 42 (2014), 1769–1808. Theorem 4, saved journal reprint PDF pp. 10–11; Conjecture 12, PDF p. 16. [Primary source](https://arxiv.org/abs/1206.1671); local `drsv_derivative.txt`. | Star-scale invariant Gaussian fields in all integer dimensions, with the kernel hypotheses in Section 2. | Proves almost-sure convergence of derivative measures, positivity, full support, and no atoms. **Does not prove maximum convergence**: the corresponding maximum assertion is Conjecture 12, subsequently proved in Madaule's class. |
| DRSV, *Renormalization of critical Gaussian multiplicative chaos and KPZ relation*, CMP 330 (2014), 283–330. Theorem 5, Corollary 6, Theorem 10, Definition 11; saved arXiv:1212.0529v3 PDF pp. 8, 9, 12, 12. [Primary source](https://arxiv.org/abs/1212.0529); local `drsv_renormalization.txt`. | Star-scale critical chaos, every d≥1; also planar GFF heat-kernel cutoffs. | **Chaos convergence, not maximum convergence.** Theorem 5 gives √t M_t^α→√(2/π)M' in probability; Corollary 6 gives moments of M' of all orders p<1, so all negative moments needed for q≥0. Theorem 10 handles the planar GFF; Definition 11 includes rad_D² in critical Liouville measure. |
| Junnila–Saksman, *Uniqueness of critical Gaussian chaos*, EJP 22 (2017), paper 11. Theorem 1.1; saved predecessor arXiv:1506.05099v2, titled *The uniqueness of the Gaussian multiplicative chaos revisited*, PDF p. 3. [Primary source](https://arxiv.org/abs/1506.05099); local `junnila_saksman.txt`. | Hölder-regular approximating fields on compact doubling metric spaces; in particular Euclidean critical/subcritical chaos. Covariance differences are uniformly bounded and tend uniformly to zero away from the diagonal; an existing atomless limiting chaos is assumed. | **Uniqueness/transfer for chaos, not maxima.** Does not supply the short-distance information needed to transfer a centered maximum. See the explicit failure example below. The journal PDF was blocked at the publisher and institutional mirror; version and page here are deliberately those actually retrieved. |
| Junnila–Saksman–Webb, *Decompositions of log-correlated fields with applications*, Ann. Appl. Probab. 29 (2019), 3786–3820. Theorems A–B and 5.3–5.4; publisher reprint with institutional cover, PDF pp. 4–5 and 24–25 (printed pp. 3788–3789, 3808–3809). [Institutional source](https://acris.aalto.fi/ws/portalfiles/portal/40601990/SCI_Junnila_et.al_Decompositions.AAP1492_1.pdf); local `junnila_saksman_webb.txt`. | Locally regular covariance remainders; for the critical-chaos results g∈Hˢ_loc(U×U), s>d, in any d. | Decomposition and critical-chaos convergence/uniqueness, **not a general maximum theorem**. Theorem 5.4 also proves convergence in derivative normalization. Section 5.2, printed p. 3812 / PDF p. 28, explicitly leaves transferring maximum results to such decompositions for further work. |
| Powell, *Critical Gaussian chaos: convergence and uniqueness in the derivative normalisation*, EJP 23 (2018), paper 31. Theorems 1.1–1.2; saved arXiv:1704.06058 PDF p. 3. [Primary source](https://arxiv.org/abs/1704.06058); local `powell.txt`. | Planar GFF in bounded simply connected domains; star-scale fields in all d. Convolution kernels satisfy the paper's integrability conditions; the star-scale statement also assumes Hölder density. | **Derivative-chaos convergence and identification with Seneta–Heyde/white-noise constructions.** Not a maximum convergence theorem. |
| Schweiger–Zeitouni, *The maximum of log-correlated Gaussian fields in random environment*, CPAM 77 (2024), 2778–2859. Theorems 1.1, 1.2, 1.4; saved arXiv:2205.07210v1 PDF pp. 2, 2, 4. [Primary source](https://arxiv.org/abs/2205.07210); local `schweiger_zeitouni.txt`. | General theorem in every fixed d under Assumption 1.3, permitting sufficiently rare covariance defects. Applications in d=2: iid uniformly elliptic conductances; infinite Bernoulli bond-percolation cluster for p sufficiently close to 1. | **Yes**, quenched convergence to a randomly shifted Gumbel after the stated deterministic effective-conductivity normalization. Theorem 1.4 identifies a derivative-type weak limit Z. It does not identify this general Z with the review's specifically normalized continuum derivative chaos. These are important graph extensions, not arbitrary-graph results. |
| Lacoin, *Critical Gaussian multiplicative chaos revisited*, AIHP 60 (2024), 2328–2351. Theorems 1.2, 1.7–1.8; saved arXiv:2209.06683 PDF pp. 4, 5, 6. [Primary source](https://arxiv.org/abs/2209.06683); local `lacoin.txt`. | Covariances with an almost-star-scale invariant part; all integer d≥1, under the paper's decomposition assumptions. | Critical-chaos constructions and equivalence, **not centered-maximum convergence**. |
| Ganguly–Nam, *Universality of Poisson–Dirichlet law for log-correlated Gaussian fields via level set statistics*, CMP 406 (2025), article 87. Theorems 1–2; saved arXiv:2302.03010v2 PDF pp. 4–5. [Primary source](https://arxiv.org/abs/2302.03010); local `ganguly_nam.txt`. | Discrete log-correlated fields in all d under Assumptions 1–2; supercritical β>√(2d). | Universal Poisson–Dirichlet cluster weights and level-set estimates. **Not convergence of the absolute centered maximum or identification of its derivative-chaos shift.** Normalizing Gibbs weights cancels absolute height shifts. |
| Paquette–Zeitouni, *The extremal landscape for the CβE ensemble*, Forum Math. Sigma 13 (2025), e1, pp. 1–126. Theorems 1.1, 1.4, published PDF pp. 3–4. [Published source](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2DBD96407247AA6166F4AEA93319FF0E/S2050509424001294a.pdf/extremal_landscape_for_the_cbeta_e_ensemble.pdf); local `paquette_zeitouni.txt`. | Log characteristic polynomials of CβE matrices, one-dimensional parameter space; not an exactly Gaussian cutoff field. | **Yes**, a shifted Gumbel with a model derivative-martingale mass. An important recent analogous result; it is not a proof for every Gaussian cutoff. |
| “Ding–Gwynne–Wirth” | No joint paper with that author combination and the requested maximum theorem was located. Ding's publication list separates work with Gwynne from work with Wirth. | No theorem number is invented for this name. A nearby relevant title is Ding–Gwynne–Zhuang, *Tightness of exponential metrics for log-correlated Gaussian fields in arbitrary dimension*, arXiv:2310.03996, Theorem 1.2, saved PDF p. 5: **metric tightness**, not centered-maximum convergence. [Primary source](https://arxiv.org/abs/2310.03996); local `ding_gwynne_zhuang.txt`. Ding–Wirth's metric-graph level-set paper and Ding–Wirth–Wu's crossing paper address other observables, as listed on [Ding's page](https://math.pku.edu.cn/teachers/dingjian/). |

Here is the full proof of the Laplace-transform identification. Let H be a standard **maximum** Gumbel, P(H≤h)=exp(−e^(−h)). If E is an independent rate-one exponential random variable, then H=−log E has this CDF. Consequently, for s>−1,
\[
\mathbb E e^{-sH}=\int_0^\infty u^s e^{-u}\,du=\Gamma(1+s).
\]
Let Z be finite and strictly positive almost surely, independent of H, let C>0, and define
\[
G=\frac{H+\log(CZ)}\alpha.
\]
Conditioning on Z gives
\[
\mathbb P(G\le x\mid Z)=\exp(-CZ e^{-\alpha x}).
\]
For q>−α with E[Z^(−q/α)] finite, independence and the Gamma integral now give
\[
\mathbb E e^{-qG}=C^{-q/\alpha}\Gamma(1+q/\alpha)
                        \mathbb E[Z^{-q/\alpha}]. \tag{1}
\]
For q≥0 this identity also holds as an equality of extended nonnegative expectations, by Tonelli; in Madaule's setting the negative moments are finite by DRSV Corollary 6. At q=0 both sides equal one. In that setting (1) is finite for every q>−α, because positive moments of M' exist below order one. No claim about convergence of the prelimit Laplace transforms is needed: convergence in law of maxima does not by itself imply convergence of their exponential moments.

The factor in the question needs a change of constant. The random variable
\[
\frac H\alpha+\frac1\alpha\log(cM')
\]
produces c^(−q/α), not c^(−q). The review's formula is obtained by taking C=c^α, or, equivalently,
\[
G=\frac H\alpha+\log c+\frac1\alpha\log M'. \tag{2}
\]
Both constants are arbitrary positive constants, so this is a change of naming rather than a disagreement between theorems. A standard **minimum** Gumbel is −H and would give Γ(1−q/α), when finite; that is the wrong sign for this maximum problem. Larger derivative mass raises the maximum, which also checks the positive sign of log M'.

Applying this calculation to Madaule is exact. His Y_t=X_t−αt and his theorem, written with threshold −z, give the limiting CDF at x=−z as E exp(−C*M'e^(−αx)). His variance is t, and his derivative measure is precisely the review's measure. Thus every deterministic sequence t_n→∞ in this scale-cutoff family satisfies the displayed conjecture, with c=(C*)^(1/α). This argument uses the printed convergence theorem and the elementary identity above; it is not an independent proof of Madaule's theorem.

For the DGFF there are two different normalizations to convert. First, for the standard lattice field h_N with covariance the killed walk Green function, set X_N=h_N/√g₀, g₀=2/π. Then α=2 and
\[
\frac{m_N}{\sqrt{g_0}}=2\log N-\frac34\log\log N.
\]
The exponent √(2π) in the unscaled CDF becomes √(2π)√g₀=2 in the scaled CDF. Integrating the Cox intensity Zᴰ(dx)e^(−α₀h)dh above a threshold gives Zᴰ(D)e^(−α₀x)/α₀, so the factor 1/α₀ is also absorbed in C. This confirms the Gumbel-rate and Gamma conversions by a second route.

Second, consider fully variance-subtracted continuum derivative chaos M'_Wick of the coefficient-one continuum GFF. DRSV Definition 11, Eq. (23), and Biskup–Louidor's Eqs. (2.23)–(2.26) show that, up to a scalar depending on cutoff conventions, the mixing mass is
\[
L^D(A)=\int_A\operatorname{rad}_D(x)^2\,M'_{\rm Wick}(dx), \tag{3}
\]
not automatically M'_Wick(A). For multiply connected domains the corresponding radius is defined from the regular part of the Green function, as in Biskup–Louidor (2.14). On an interior compact set it is positive and bounded, but usually nonconstant. It cannot in general be absorbed in one deterministic scalar. The review's suggested DGFF interpretation must therefore use critical Liouville measure, or explicitly retain (3). This normalization issue persists even away from the boundary.

The algebra behind (3), and its higher-dimensional counterpart, can be checked directly. Suppose Var X_t(x)=t+f_t(x), with f_t→f uniformly on a compact set. Set W_t(dx)=e^(αX_t(x)−d Var X_t(x))dx and D_t(dx)=(α Var X_t(x)−X_t(x))W_t(dx). The deterministically normalized derivative expression is
\[
\widetilde D_t(dx)=(\alpha t-X_t(x))e^{\alpha X_t(x)-dt}dx
=e^{df_t(x)}D_t(dx)-\alpha f_t(x)e^{df_t(x)}W_t(dx). \tag{4}
\]
If D_t→D weakly in probability as finite signed measures, their total variation norms are tight, and W_t→0 weakly in probability, then (4) implies \widetilde D_t→e^(df)D. Indeed, the error from replacing e^(df_t) by e^(df) is bounded by its uniform difference times the total variation norm of D_t, which tends to zero in probability under these assumptions. The other error is bounded by a fixed constant times the positive mass W_t of the compact set. This proves the transfer under its explicit assumptions; tightness of total variation is an additional hypothesis here, not inferred from convergence against individual tests. In the GFF f is log rad_D plus a cutoff-dependent scalar and d=2, yielding (3).

This is why merely calling DRZ's variable “the derivative martingale” is insufficient. Its displayed expression
\[
Z_N=\sum_{v\in V_N}(\alpha\log N-\varphi_{N,v})
                          e^{\alpha\varphi_{N,v}-2d\log N}
\]
uses deterministic log N subtraction. A comparison to the Riemann sum of the fully variance-subtracted derivative chaos involves the diagonal covariance remainder and the vanishing critical chaos term in (4). Neither replacing that spatial weight by a scalar nor passing from a lattice maximum to a continuum supremum follows just from the title of a chaos-uniqueness theorem.

A complete counterexample to the unrestricted approximation reading is as follows. Choose a smooth nonnegative radial bump φ supported in a Euclidean ball of radius less than 1/2, and set
\[
k(x)=\frac{\int\phi(z)\phi(z+x)dz}{\int\phi(z)^2dz}.
\]
Then k is C∞, nonnegative, positive definite, k(0)=1, and supported in the unit box. Use Madaule's Gaussian scale process with covariance K_t(x−y)=∫₀ᵗ k(eᵘ(x−y))du. Let
\[
U_n=\sup_{[0,1]^d}X_n-\alpha n+b\log n,
\qquad b=\frac3{2\alpha}.
\]
Madaule proves U_n⇒G with a nondegenerate law. Fix a>0, put δ_n=0 for odd n and δ_n=a for even n, and define
\[
a_n=1+\frac{\delta_n}n,\qquad
\widehat X_n=a_nX_n,\qquad
\widehat c_n=\operatorname{Var}\widehat X_n=a_n^2n.
\]
These are centered smooth stationary Gaussian fields approximating the **same** generalized field as X_n. Here is a direct verification. For a compactly supported smooth test function f, independent scale increments and the support bound on k imply
\[
\operatorname{Var}\bigl((X_s-X_t)(f)\bigr)
\le C_f\int_t^s e^{-du}du\le C'_f e^{-dt},\qquad s\ge t.
\]
Indeed, the covariance integrand vanishes unless |x−y|∞≤e^(−u), and |k|≤1, so its absolute double integral against f(x)f(y) is at most a constant times e^(−du). Thus X_t(f) is L² Cauchy and uniformly L² bounded. Since a_n−1→0, also (\widehat X_n−X_n)(f)→0 in L². The limits coincide for every finite collection of test functions.

The radial choice makes k radial. Its limiting covariance, with r=|x−y| in the Euclidean norm, is
\[
K_\infty(r)=\int_r^\infty k(v)\frac{dv}{v}
=\log_+(1/r)+g(r),
\]
with g continuous and bounded on the cube, including r=0, because k(v)=1+O(v²) there. This radial kernel also satisfies Madaule's sup-norm support hypothesis.

The perturbation also has uniformly bounded covariance error:
\[
\sup_{x,y}|\operatorname{Cov}(\widehat X_n(x),\widehat X_n(y))-K_n(x-y)|
\le 2a+a^2/n,
\]
and that error tends uniformly to zero for |x−y|≥ε, every ε>0. Nevertheless its variance-centered maximum is exactly
\[
\begin{aligned}
\widehat U_n
&=\sup\widehat X_n-\alpha\widehat c_n+b\log\widehat c_n\\
&=a_nU_n+\alpha n(a_n-a_n^2)
       +b\{(1-a_n)\log n+2\log a_n\}.
\end{aligned}
\]
Since U_n is tight, the first term differs from U_n by o_P(1). The second term tends to −αδ_n along each parity subsequence, and the bracket tends to zero. Therefore
\[
\widehat U_{2m+1}\Rightarrow G,
\qquad \widehat U_{2m}\Rightarrow G-\alpha a.
\]
These distributions are different. No probability law on R equals its translate by a nonzero constant: its CDF would otherwise be periodic and could not tend to zero and one at opposite infinities. Hence \widehat U_n does not converge in law. This is valid in every d≥1.

The construction is not asserted to belong to a normalized convolution scheme or to a fixed-kernel independent-increment cutoff family; it is deliberately an approximation in the broad generalized-field and covariance sense. It proves that such broad criteria alone cannot complete the review's informal formulation. A theorem for standard fixed mollifiers may still hold under additional hypotheses. DRZ already supplies related counterexamples for discrete covariance classes (Examples 1.7–1.8 in the saved preprint, PDF pp. 5–6); those are not silently being presented as cutoffs of a single fixed continuum field.

There is also a simple positive extension that requires no new extreme-value theory. Suppose fields A_n,B_n on the same compact set are coupled so that ||A_n−B_n||∞→0 in probability, and deterministic centerings r_n,s_n satisfy s_n−r_n→ℓ. Then
\[
|\sup A_n-\sup B_n|\le\|A_n-B_n\|_\infty.
\]
If sup A_n−r_n⇒G, Slutsky's theorem yields sup B_n−s_n⇒G−ℓ. In particular, if variance parameters tend to infinity with c'_n−c_n→δ, their centerings αc−b log c differ by αδ+o(1). This transfers the maximum law when a sufficiently strong coupling is actually available. The decomposition of a field into a star-scale field plus an O(1) continuous random field does not meet this vanishing-supremum hypothesis. That extension needs spatial extrema information and the corresponding weighted chaos. No complete general-cutoff extension is claimed here.

The small computation is evidence only. [code/simulate_brw.py](code/simulate_brw.py) simulates a Gaussian branching random walk with b=2^d children and independent edge increments N(0,log 2), for d=1,2. At depth n there are b^n leaves, each of variance t=n log 2. Thus the predicted centering is αt−(3/(2α))log t, the same coefficient-one convention as above. This is a hierarchical model with parameter d, not a simulation of a Euclidean star-scale kernel or of a DGFF.

Each dimension has 1,024 independent trees, with nested depth snapshots. The main mixture uses the positive finite-depth Seneta–Heyde proxy
\[
Z_n^{SH}=\sqrt{\pi t/2}\sum_{|v|=n}e^{\alpha S_v-2dt}.
\]
The signed derivative sum D_n=∑(αt−S_v)e^(αS_v−2dt) is recorded separately, without clipping or dropping trees. It can be negative at finite depth. The SH constant can be checked from boundary-case BRW variables V_v=α(αt−S_v): their spine variance per generation is α² log 2 and the usual derivative sum is αD_n. Aïdékon–Shi, *The Seneta–Heyde scaling for the branching random walk*, Ann. Probab. 42 (2014), 959–993, Theorem 1.1, saved journal reprint PDF p. 4, states √n W_n→√(2/(πσ²))D∞ in probability. Substituting σ²=α² log 2 and the derivative αD_n gives exactly the proxy above, asymptotically; finite-depth bias remains. [Primary source](https://arxiv.org/abs/1102.0217); local `aidekon_shi.txt`.

At each depth, 256 trees supply the empirical mass mixture, 384 different trees calibrate the single constant C by matching the calibration median, and 384 held-out trees supply the validation CDF. The prediction is mean_j exp(−C Z_j^SH e^(−αx)); the plain Gumbel comparison also has its location calibrated to the same median. No conditional independence between a tree's maximum and its own derivative sum is assumed.

| d | depth | t | median centered maximum (all 1,024) | fitted C | held-out CDF distance, mixture | held-out CDF distance, plain Gumbel | trees with D_n≤0 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 10 | 6.931 | −0.318 | 0.560 | 0.050 | 0.141 | 14 |
| 1 | 12 | 8.318 | −0.340 | 0.577 | 0.030 | 0.171 | 12 |
| 1 | 14 | 9.704 | −0.251 | 0.601 | 0.046 | 0.157 | 7 |
| 1 | 16 | 11.090 | −0.301 | 0.645 | 0.027 | 0.176 | 8 |
| 2 | 5 | 3.466 | −0.576 | 0.356 | 0.061 | 0.158 | 24 |
| 2 | 6 | 4.159 | −0.521 | 0.359 | 0.052 | 0.159 | 18 |
| 2 | 7 | 4.852 | −0.522 | 0.373 | 0.050 | 0.162 | 12 |
| 2 | 8 | 5.545 | −0.532 | 0.386 | 0.059 | 0.163 | 11 |

The mixture fits better at these depths. This does not demonstrate asymptotic convergence, estimate the true limiting constant, identify continuum M', or resolve cutoff universality. Both the finite mass sample and calibration add uncertainty; the distances are descriptive, not calibrated goodness-of-fit p-values. The fitted constants drift with depth. For scale, the usual 95% DKW bound for 384 independent validation observations against their true CDF is about 0.069; this is not a confidence band for the fitted prediction.

Raw records: [data/brw_samples.csv](data/brw_samples.csv). Parameters, all summaries, and Gamma-integral checks: [data/simulation_summary.json](data/simulation_summary.json). Plot: [data/brw_cdf.svg](data/brw_cdf.svg). Random seed 650013; one process, numerical library threads limited to one, batch size 16, measured nice 10. Runtime was about 3.65 seconds and peak RSS about 0.421 GB (0.392 GiB). macOS rejected setting RLIMIT_AS; the code instead uses bounded arrays and an RSS guard. The observed memory use is well below 4 GB.

Verification included reading the theorem statements and their hypotheses in the saved primary texts, independently converting the maximum CDF and the exponential representation to check the Gamma factor, checking the DGFF exponent after rescaling and after integrating its extremal-process intensity, and deriving the spatial normalization by identity (4). Numerical quadrature at q=0.5,1,2 in d=1,2, with deterministic mass 2 and c=3, agrees with c^(−q)Γ(1+q/α)2^(−q/α) within 3×10^−13. The simulation summaries were independently recomputed from the saved CSV during the final audit. Its record is [data/final_audit.json](data/final_audit.json), and [code/audit_artifacts.py](code/audit_artifacts.py) reproduces it.

Searches covered the named authors, exact titles, “centered maximum log-correlated”, general cutoff/mollified fields, and date-qualified 2024–2026 searches. Recent results found and checked include Schweiger–Zeitouni (2024), Lacoin (2024), Ganguly–Nam (2025), and Paquette–Zeitouni (2025). No checked 2026 result supplies the missing unrestricted theorem. This is a bounded literature search, not proof that no further theorem exists. In particular, an unavailable or unidentified “Ding–Gwynne–Wirth” reference cannot support a resolution claim. No blanket assertion that all non-star-scale cases remain open is made: DRZ, Acosta's thesis, and the random-environment results already cover many such cases.

What remains outside this report's proved/literature-covered scope is an explicit theorem for any proposed additional fixed cutoff class, with its short-scale covariance conditions verified and its mixing measure identified in the chosen normalization, and any proposed class of refining graphs beyond the cited results. Arbitrary graphs need not even have logarithmic Green functions; neither the dimension nor the logarithmic coefficient is determined just by specifying a mesh.

Task: “Open problem D0065.” Received 2026-11-13, approximately 10:46 +04 (Asia/Tbilisi).
