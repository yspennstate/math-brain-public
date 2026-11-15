NO_PROGRESS

# I0072: quadratic reaction–diffusion systems with mass control

This is a literature audit and an unsuccessful proof attempt, not a solution of Problem 8. No inspected theorem gives almost-sure global well-posedness under all its hypotheses, and no new restricted global theorem or counterexample is established here. The two superlinear-noise follow-up questions are also not answered in their stated generality. The search was conducted on 13 November 2026; absence from the inspected literature is not a proof that no other result exists.

## 1. The source statement and the meaning of the question

Page references below distinguish the arXiv v5 pagination (103 pages) from the NoDEA article pagination (150 pages, article 123). The supplied `survey_v5.txt` was checked against a fresh extraction of [arXiv:2501.18561v5](https://arxiv.org/pdf/2501.18561v5): the page-marked texts agree exactly. The supplied published text was also read and its relevant statements verified against the published PDF from TU Delft, retrieved and immediately converted to text. The Delft file has one repository cover sheet before the 150-page article; its PDF page numbers are therefore one higher than the article page numbers used here. Direct Springer retrieval returned an HTML access response, recorded separately.

### Equation (8.14)

On v5 p. 69 / published pp. 96–97, the equation is

\[
\begin{cases}
 du_i-\nu_i\Delta u_i\,dt
 =f_i(\cdot,u)\,dt+
 \displaystyle\sum_{n\ge1}\big[(b_{n,i}\cdot\nabla)u_i+g_{n,i}(\cdot,u)\big]\,dW^n,
 &\text{on }\mathbb T^d,\\
 u_i(0)=u_{0,i},&\text{on }\mathbb T^d,
\end{cases}\tag{8.14}
\]

Here \(i=1,\ldots,\ell\), \(\ell\ge1\); \(u=(u_i)_{i=1}^{\ell}\) is real and vector valued; \(\nu_i>0\) are the species diffusivities; and
\((b_{n,i}\cdot\nabla)u_i=\sum_{j=1}^d b^j_{n,i}\partial_j u_i\).
The stochastic integrals are Itô integrals. The same sequence of independent standard real Brownian motions \((W^n)_{n\ge1}\), on the given filtered probability space \((\Omega,\mathcal A,\mathbb P,(\mathscr F_t)_{t\ge0})\), drives all species. Independence between different species' forcing is not required. Equivalently the driving process is cylindrical on \(\mathcal U=\ell^2\). The coefficients are square summable over the noise index. This is spatially correlated transport noise plus an \(\ell^2\)-valued Nemytskii noise; it is not general space-time white noise. There is no cross diffusion in the principal deterministic or transport terms. No divergence-free condition on \(b_{n,i}\), and no common-transport condition across species, is imposed.

Section 8.2 proves its stated results on the torus, with periodic boundary conditions. It explicitly treats \(d\ge2\), with \(d=1\) accessible by a separate argument or a dummy variable (AV23, Section 6). Problem 8 broadens the question to \(\mathcal O=\mathbb T^d\) or \(\mathbb R^d\), \(\ell\ge2\), without an upper dimension bound. There is no spatial boundary on \(\mathbb R^d\). The problem adds “possibly additional boundary conditions in case \(\mathcal O\ne\mathbb T^d\),” but does not specify a bounded domain or a particular boundary condition. Consequently it is not an exact Dirichlet or Neumann theorem on arbitrary bounded domains. Section 8.2, p. 68 / published p. 96, expressly explains the difficulty of stochastic maximal regularity with boundary conditions and transport noise. No boundary compatibility hypothesis can be supplied as if it were part of the printed problem.

### Assumption 8.4, transcribed with source defects exposed

V5 p. 69 / published p. 97 defines Assumption 8.4\((p,\kappa,q,h,\delta)\) for integers \(d\ge2\), \(\ell\ge1\),
\[
q\in[2,\infty),\quad p\in[2,\infty),\quad h>1,\quad\delta\in[1,2).
\]
For every species \(i\):

1. There is \(\alpha>\delta-1\) such that, for every \(j=1,\ldots,d\),
   \((b^j_{n,i})_{n\ge1}\in C^\alpha(\mathbb T^d;\ell^2)\).
2. **As printed**, there is \(\mu>0\) such that, for every \(x,\xi\),
   \[
   \sum_{j,k=1}^d\sum_{n\ge1}b^j_{n,i}(x)b^k_{n,i}(x)\xi_j\xi_k
   \ \mathbf{\ge}\ (2\nu_i-\mu)|\xi|^2.
   \]
   This direction is erroneous as a parabolicity condition: it is vacuous if \(\mu\ge2\nu_i\). The meaningful condition used in the cited local theory is
   \[
   \sum_n|b_{n,i}(x)\cdot\xi|^2\le(2\nu_i-\mu)|\xi|^2,
   \quad\text{equivalently}\quad
   \nu_i I-\tfrac12\sum_n b_{n,i}\otimes b_{n,i}\ge\tfrac\mu2 I.
   \tag{P}
   \]
   AV23 Assumption 2.1(3), published p. 255, and AV24a Assumption 2.1(3), arXiv v4 p. 7, have the correct sign. All mathematical calculations in this report use (P), not the erroneous printed inequality. No counterexample based on that typo is claimed.
3. **As printed**, the domains of \(f_i,g_i\) are \(\mathbb T^d\times\mathbb R\), with \(\mathcal B(\mathbb T^d)\otimes\mathcal B(\mathbb R)\)-measurability. For a system their last argument is necessarily \(\mathbb R^\ell\); the displayed scalar domain is another notational defect. With that vector argument understood, the requirements are
   \[
   f_i(\cdot,0)\in L^\infty(\mathbb T^d),\qquad
   g_i(\cdot,0)\in L^\infty(\mathbb T^d;\ell^2),
   \]
   and, uniformly in \(x\),
   \[
   |f_i(x,y)-f_i(x,y')|
   \lesssim(1+|y|^{h-1}+|y'|^{h-1})|y-y'|,
   \]
   \[
   \|g_i(x,y)-g_i(x,y')\|_{\ell^2}
   \lesssim(1+|y|^{(h-1)/2}+|y'|^{(h-1)/2})|y-y'|.
   \tag{8.4.3}
   \]
4. Either:
   \[
   p>2,\quad q\ge2,\quad1\le\delta<\frac{h+1}{h},\qquad
   \frac{1+\kappa}{p}+\frac12\left(\delta+\frac dq\right)=\frac h{h-1},
   \]
   \[
   \frac d{d-\delta}<q<\frac{d(h-1)}{h+1-\delta(h-1)};
   \tag{8.4.4i}
   \]
   or \(p=q=2,\ \kappa=0,\ \delta=1,\ h\le(4+d)/d\), additionally \(h<3\) when \(d=2\).

The surrounding local theory also requires \(\kappa\in[0,p/2-1)\cup\{0\}\), with the Hilbert case \(p=2\) using \(\kappa=0\). Here \(C^\alpha\) is spatial Hölder regularity, \(H^{s,q}\) is the Bessel potential space, and \(B^s_{q,p}\) is a Besov space. The simplified assumption is time independent and deterministic; Remark 8.12 explains the larger progressively measurable, divergence-form setting of AV23. That extension is not an extra condition in Problem 8.

### Conditions (1)–(5) of Problem 8

V5 p. 93 / published pp. 131–132 specifies \((b_{n,i})_n\in C^\gamma(\mathcal O;\ell^2)\), \(\gamma>0\), and asks for global well-posedness when, for each \(i\):

1. \(u_0\in[0,\infty)^\ell\), meaning componentwise nonnegative initial functions, almost surely, rather than a declaration that the datum is a spatially constant vector.
2. \(g_i:\mathbb R^\ell\to\ell^2\) is globally Lipschitz, and \(g_i(u)=0\) for every \(u\in[0,\infty)^\ell\) with \(u_i=0\).
3. \(f_i(u)\ge0\) for every \(u\in[0,\infty)^\ell\) with \(u_i=0\).
4. **The exact printed quantifier is** \(\exists K_1,K_2\ge0\) such that
   \[
   \sum_{j=1}^{\ell}f_j(u)\le K_0+K_1\sum_{j=1}^{\ell}u_j,
   \qquad u\in[0,\infty)^\ell.
   \]
   \(K_2\) is unused and \(K_0\) is not quantified there. The coherent mass-control reading is finite constants \(K_0,K_1\), which may be enlarged to nonnegative ones. The inequality is mass *control*, not an assertion of equality or pathwise conservation of stochastic total mass.
5. Uniformly for \(u,u'\in[0,\infty)^\ell\),
   \[
   |f_i(u)-f_i(u')|\lesssim(1+|u|+|u'|)|u-u'|.
   \]

Thus the local Lipschitz constant grows **linearly**, and \(f\) grows at most **quadratically**. There is no triangular structure or entropy-dissipation assumption. The problem suppresses \(x\)-dependence of \(f,g\). Condition (2) implies the stronger useful bound \(\|g_i(u)\|_{\ell^2}\le L u_i\) on the nonnegative orthant: compare \(u\) with the vector obtained by setting its \(i\)th component to zero.

Problem 7, on the same page, instead allows arbitrary polynomial drift order \(h>1\) and imposes a lower triangular invertible matrix \(R\) with nonnegative entries and \(Rf(y)\le(1+\sum_i y_i)r\), componentwise. That additional structure is absent from Problem 8.

The final sentence of Problem 8 literally asks for “\(h=3/2\) in Assumption 8.4(3).” In that assumption \(h\) is the *drift* order and the diffusion order is \((h+1)/2\). Consequently literal \(h=3/2\) means drift order \(3/2\), diffusion order \(5/4\). The scaling-optimal diffusion order for the quadratic drift in Problem 8 is instead **\(3/2\), obtained by putting \(h=2\)** in (8.4.3). Both readings are recorded; they are not interchangeable. The intended cubic-half diffusion question is not answered here, and neither is the literal alternative general subquadratic-drift question.

### Solution class and initial data

The problem's five-item list does **not** itself name an initial-data norm. The precise Section 8.2 framework is (8.13):
\[
X_0=H^{-\delta,q}(\mathbb T^d;\mathbb R^\ell),\qquad
X_1=H^{2-\delta,q}(\mathbb T^d;\mathbb R^\ell),\qquad
E=(X_0,X_1)_{1-(1+\kappa)/p,p}
 =B^{2-\delta-2(1+\kappa)/p}_{q,p}.
\]
An \(\mathscr F_0\)-measurable datum lies in \(L^0_{\mathscr F_0}(\Omega;E)\); no finite probability moment is required for local existence. Positivity for distributional data has its distributional meaning. A maximal solution \((u,\sigma)\) is strongly progressively measurable, uniquely determined on overlaps of lifetimes, and along stopping times \(\sigma_m\uparrow\sigma\) satisfies almost surely
\[
u\in L^p(0,\sigma_m;t^\kappa dt;X_1)\cap C([0,\sigma_m];E),
\]
with the integrated Itô equation in \(X_0\), Bochner drift integrals and a cylindrical stochastic integral. The nonlinear terms have the local integrability in Remark 8.5:
\(f_i(u)\in L^p(t^\kappa;H^{-\delta,q})\) and
\(g_i(u)\in L^p(t^\kappa;H^{1-\delta,q}(\ell^2))\).
Definitions 4.5–4.6 are on v5 p. 30. **Global** means \(\mathbb P(\sigma=\infty)=1\), not existence on an event of high probability, nor merely global martingale or renormalized solutions. Well-posedness also includes uniqueness and the corresponding continuous-dependence property; the precise global continuity conclusion in Theorem 8.15(3) is convergence in probability in \(C([0,T];B^{d/q-2/(h-1)}_{q,p})\), for \(p\ge q\ge d(h-1)/2\).

In the critical case (8.4.4i),
\[
E=B^{d/q-2/(h-1)}_{q,p},
\]
so the quadratic drift has critical smoothness \(d/q-2\). Theorem 8.6, v5 pp. 70–71 / published pp. 98–99, also gives, at positive times,
\[
u\in L^r_{\rm loc}((0,\sigma);H^{1,r})
\cap C^{\theta/2,\theta}_{\rm loc}((0,\sigma)\times\mathbb T^d;\mathbb R^\ell),
\quad r>2,\quad0<\theta<1.
\]
There is a further source mismatch: Theorem 8.6 prints the critical Besov formula for all of Assumption 8.4, whereas case (ii) has trace \(E=L^2\), and that agrees with the critical formula only when \(h=1+4/d\). AV23's separate Hilbert-space result, Propositions 7.1–7.2 (published pp. 292–293), uses \(L^2\) data; one must not infer arbitrary negative-Besov-data existence in this subcritical case from the displayed survey formula. Nonnegative bounded functions on the torus are an unambiguous classical-data subclass of the local theories (enlarge the growth parameter if necessary). On \(\mathbb R^d\), bounded functions need not lie in the above inhomogeneous finite-\(q\) spaces: an exact full-space theorem must specify integrability or an appropriate uniformly local space. Problem 8 leaves that choice unstated.

## 2. Literature first: what the actual theorems cover

The references here are to primary papers or an author-uploaded manuscript. Search-result descriptions were used only to find papers, never as theorem statements. The AV24a published file has two repository cover sheets: PDF page 14 is journal p. 4881, for example. ArXiv page numbers below are the numbered manuscript pages.

### The deterministic comparison

| Paper and exact location | Hypotheses relevant to I0072 | Conclusion and comparison |
|---|---|---|
| [Caputo–Goudon–Vasseur, arXiv:1709.05694](https://arxiv.org/pdf/1709.05694), Theorems 1.1 and 1.2, p. 5; structural assumptions h1–h4, p. 3 | Cauchy problem on \(\mathbb R^d\), constant positive species diffusivities; smooth bounded nonnegative data. Theorem 1.1 is the four-species reversible binary reaction. Theorem 1.2 assumes mass conservation and entropy dissipation, allowing a small superquadratic extension. The displayed theorems treat \(d\ge3\); the lower-dimensional cases are prior results discussed on p. 4. | Unique global smooth solutions, bounded on every finite time interval. The entropy hypothesis is additional to Problem 8. The proof combines a Hölder bound on a potential of total mass, duality and a De Giorgi argument; see pp. 5–8 and Sections 3–5. |
| [Souplet, arXiv:1804.05193](https://arxiv.org/pdf/1804.05193), main **unnumbered Theorem**, p. 3, referred to subsequently as Theorem 1; conditions (2)–(4), (8), (9), pp. 1–2 | All \(d\ge1\), \(\mathbb R^d\) or smooth bounded domain with Neumann boundary; bounded nonnegative data, each component nontrivial; \(C^1\) reactions, quasi-positivity, mass dissipation, **entropy dissipation**, derivative bound \(|\nabla f_i(u)|\le M(1+|u|)\). Remark 1(a) extends to Dirichlet boundary conditions. | Global classical solutions. This has extra entropy structure; it is not a theorem under mass control alone. Its proof uses entropy variables and auxiliary heat problems, pp. 4–7. Journal location: J. Evol. Equ. 18 (2018), 1713–1720. |
| [Fellner–Morgan–Tang, arXiv:1808.01315v2](https://arxiv.org/pdf/1808.01315v2), Theorem 1.1, p. 2; (A1)–(A5), pp. 1–2; Lemma 1.1, pp. 3–4 | All \(d\ge1\), \(\mathbb R^d\) or bounded smooth domain with Neumann boundary; arbitrary positive constant diffusivities; bounded nonnegative data; locally Lipschitz quasi-positive reactions; \(\sum f_i\le K_0+K_1\sum u_i\), \(K_0\ge0,K_1\in\mathbb R\); growth at most \(2+\varepsilon\) for sufficiently small \(\varepsilon>0\). No entropy or triangular hypothesis. | Unique global classical solution. This is the deterministic theorem matching the structural generality of Problem 8. The decisive potential estimate is Lemmas 3.4–3.5, pp. 14–15, and Appendix A, pp. 23–26; the interpolation closure is Lemmas 3.7–3.9, pp. 15–17. |
| [Pierre–Suzuki–Yamada, author manuscript](https://www.researchgate.net/publication/322150307_Dissipative_reaction_diffusion_systems_with_quadratic_growth), HAL hal-01671797, manuscript Theorems 1–3, pp. 3–4 | Bounded smooth domain, homogeneous Neumann boundary, all dimensions; locally Lipschitz quasi-positive quadratic reactions, mass dissipation, and lower bound \(\partial f_j/\partial u_j\ge-C(1+|u|)\). | Theorem 1: global weak solution for nonnegative \(L^1\) data. Theorem 2: relatively compact orbit in \(L^1\). Theorem 3: for \(d\le2\), sufficiently smooth data give a classical uniformly bounded solution. This is not all-dimensional classical uniqueness. Published: Indiana Univ. Math. J. 68 (2019), 291–322, DOI 10.1512/iumj.2019.68.7447. Direct HAL retrieval was challenged; the manuscript text uploaded by coauthor Yamada was read online. |
| [Cañizo–Desvillettes–Fellner, arXiv:1304.4040](https://arxiv.org/pdf/1304.4040), Proposition 1.1, pp. 2–3; Lemmas 2.1–2.2 and duality proof, pp. 7–10 | Deterministic adjoint diffusion \(\partial_t S-\Delta(aS)=0\), \(a_*\le a\le a^*\), bounded smooth domain; \(p>2\) with \(C_{(a_*+a^*)/2,p'}(a^*-a_*)/2<1\). | An improved \(L^p\) bound on total mass. Continuation from \(p=2\) gives some improvement beyond two without arbitrary diffusivity closeness, but not an arbitrary large exponent. No stochastic integral is present in this proposition. |

In particular, it is FMT, rather than an entropy-only quadratic theorem, that one would have to reproduce to answer the whole stochastic question.

### Agresti–Veraar: local theory, coercivity, and particular mass-controlled models

[AV23, *Local well-posedness and positivity*](https://research-explorer.ista.ac.at/download/13135/14895/2023_JourDifferentialEquations_Agresti.pdf) has Assumption 2.1 on journal pp. 255–256 and Theorem **2.7**, pp. 259–260, for local existence in critical Besov spaces on the torus. Theorem **2.10**, p. 261, and Corollary **2.11**, p. 262, give blow-up criteria, and Theorem **2.13**, p. 263, positivity. Proposition **7.1**, p. 292, supplies the Hilbert-space local theory with \(L^2\) initial data, and Proposition **7.2**, p. 293, regularity. The survey cites “Theorem 2.6” for the local theorem; the final published paper numbers it 2.7. This reference-number shift does not create a global theorem.

[AV24a, *Global well-posedness of weakly dissipative systems*](https://arxiv.org/pdf/2301.06897v4) proves Theorem **3.2**, arXiv pp. 10–11 / journal pp. 4881–4882, under an additional \(L^\zeta\)-coercivity assumption, \(\zeta\ge\max\{2,d(h-1)/2\}\). This balances the weighted reaction term and the **full** quadratic variation against diffusion; ordinary mass control is insufficient. Theorem **4.5**, arXiv p. 24 / journal p. 4898, treats a particular two-species predator–prey system for \(1\le d\le4\), with model-specific bounds on the superlinear noise. Theorems **4.9** and **4.11**, arXiv pp. 27 and 29 / journal pp. 4902 and 4906, concern the Brusselator in dimensions 1–2 and 3. Theorem **5.2**, arXiv p. 35 / journal p. 4913, gives continuous dependence when the requisite energy estimates hold. These are important subclasses, not the arbitrary \(\ell\)-component quadratic system of Problem 8. The survey's corresponding coercive result is Theorem **8.15**, v5 pp. 72–73 / published pp. 102–103; its explicit predator–prey example is Theorem **8.18**, v5 p. 74 / published p. 104.

### The 2025–2026 papers

| Paper and precise result | Domain, noise and growth | Comparison with Problem 8 |
|---|---|---|
| [Milesis–Salins, 2604.06645v2](https://arxiv.org/pdf/2604.06645v2), Theorem **5.1**, p. 29 (two species), Theorem **5.2**, p. 31 (general system); Assumptions 0–11, pp. 9–13 | Bounded smooth domain in any \(d\); Dirichlet or Neumann boundary; nonnegative \(L^\infty\) data; polynomial locally Lipschitz quasi-positive reactions; **triangular** mass control. Finite family of white-in-time, spatially coloured Gaussian random measures. Nemytskii coefficients are locally Lipschitz, vanish on the corresponding face, and have **linear growth**. Kernel assumptions include pointwise nonnegativity, a heat-convolution singularity \(t^{-\eta}\), \(\eta<1\), and uniform spatial integrability. | Unique global mild solution with uniform stopped supremum moments. No transport term. It supplies a result in the direction of Problem 7 with \(b=0\), in its own domain/noise setting. It does not remove triangular structure for Problem 8 and does not allow general superlinear \(g\). V1 (8 April, 37 pages) was checked too; v2 is 26 May, 38 pages. |
| [Agresti–Germ–Veraar, 2606.07417](https://arxiv.org/abs/2606.07417), **all three posted versions** | Bounded smooth domain; Dirichlet, with Neumann variants noted; system in general \(d\), subject to colouring-dependent local parameter restrictions. Noise is \(g_{ij}(x,u)R_j\,dB^j\), with \(L^2\)-cylindrical \(B^j\), orthonormal spatial series and weighted \(\ell^\zeta\) colouring. It can be non-trace-class; white noise is included in one dimension. There is **no** \((b\cdot\nabla)u\,dW\) term. | Local existence, regularization, positivity and blow-up criteria are not global a priori bounds for mass control. Its applications to named models do not prove the general Problem 8. See the version table below. |
| [Agresti–Sauerbrey–Veraar, 2511.12692v1](https://arxiv.org/pdf/2511.12692v1), Theorem **3.4**, pp. 20–21; Theorem **3.5**, p. 21; Theorem **5.4**, p. 31 | Torus, all \(d\); uniformly parabolic scalar divergence-form SPDE with bounded measurable leading diffusion and transport \(b\in C^{3+\delta}(\ell^2)\), \(\delta>0\) (Remark 1.2 gives a weakened flow condition). Source norms satisfy \(2/p+d/q<1\). | Genuine stochastic De Giorgi–Nash–Moser estimates now exist with **smooth** transport, so the survey's historical comment must be updated. They do not cover arbitrary \(C^\gamma\), \(\gamma>0\), nor by themselves prove the nonlinear mass-controlled system. The application is a scalar quasilinear equation. |
| [Agresti–Kniely–Tang, 2608.13332](https://arxiv.org/pdf/2608.13332), Theorem **3.4**, p. 15; Theorem **3.5**, pp. 15–16 | Torus, \(d\ge2\); complex-balanced chemical networks with no boundary equilibria in the stated positive mass classes; bounded \(L^q\) initial-data sets; specially chosen finite-mode common divergence-free **Stratonovich transport** noise; polynomial reaction growth, \(g=0\). | For every \(\varepsilon>0\) a suitable noise is chosen giving \(\mathbb P(\tau=\infty)>1-\varepsilon\). This differs from \(\mathbb P(\sigma=\infty)=1\) for each given admissible noise; both quantifiers and extra reaction structure matter. It does not resolve Problem 8. |
| [Leocata–Vovelle, 2404.05360v1](https://arxiv.org/pdf/2404.05360v1), Theorem **1.1**, p. 4; Theorem **3.1**, p. 11; Theorem **4.1**, p. 16 | Torus, \(d=1,2\); **four-species reversible binary reaction**; smooth nonnegative data; finite-dimensional Brownian Nemytskii noise, smooth face-vanishing coefficients, \(\sum_\alpha|\sigma_{i\alpha}(a)|^2\le\nu(a_1a_3+a_2a_4)\), with \(C_B\nu\le1\). | Unique global regular solutions. The noise envelope is of linear order and small; no transport is present. This is a useful stochastic quadratic/duality result, not general mass control or the \(3/2\)-growth follow-up. Their backward-SPDE method is directly relevant to the failed route below. |

AGV was checked by version rather than assuming the latest result from the title:

| Version/date | Local theorem | Regularization | Blow-up / positivity | Actual global result |
|---|---|---|---|---|
| v1, 5 June 2026, 46 pages | Theorem 2.9, p. 12 | Theorem 2.12, p. 13 | Theorem 2.20, pp. 15–16; Corollary 2.21, p. 16; Theorem 2.24, p. 17 | Corollary 3.14, pp. 23–24 |
| v2, 16 July 2026, 46 pages | Theorem 2.9, p. 12 | Theorem 2.12, p. 13 | Same numbers/pages as v1 | Corollary 3.14, pp. 23–24 |
| v3, 9 November 2026, 50 pages | Theorem 2.9, pp. 13–14 | Theorem 2.12, p. 15 | Theorem 2.20 and Corollary 2.21, p. 17; Theorem 2.24, p. 19 | Corollary 3.14, p. 26 |

In every AGV version, Corollary **3.14** is a **scalar** equation on a bounded interval with space-time white noise and the additional asymptotic restrictions
\[
|f(y)|=O(|y|\log|y|),\qquad
 g(y)=o\bigl(|y|(\log|y|)^{1/4}\bigr).
\]
It restarts the regularized local solution using an existing global theorem. It does not establish a quadratic system with merely mass control. V3's discussion on pp. 2–3 expressly positions the theory as groundwork for further global results; Remark 2.19, p. 16, distinguishes the earlier trace-class theory with transport. A local exponent allowance for \(g\) is not a global theorem at that exponent.

An additional late-2026 search lead, [Xiong–Xu, 2610.41400](https://arxiv.org/abs/2610.41400), concerns a one-dimensional Neumann catalytic model with square-root Nemytskii coefficients and a special inward-drift/covariance condition. Its equation on pp. 1–2 is already outside Problem 8's Lipschitz-face assumptions and has no transport noise. It gives no extension of the five-hypothesis statement. A search aggregator had incorrectly associated this title with 2610.40517; opening that identifier exposed an unrelated Landau paper. That lead was rejected rather than cited as reaction–diffusion evidence.

**Literature outcome.** The deterministic \(b=g=0\) subclass is resolved by FMT; several particular stochastic reaction systems, triangular systems without transport, and some coercive systems including superlinear noise are resolved by the papers above. No inspected printed theorem answers the full base question or either general follow-up. Therefore the report is not labelled RESOLVED_IN_LITERATURE. These existing subclasses are also not claimed as new PARTIAL progress.

## 3. Attempted proof and the precise point where it stops

All calculations below use the corrected parabolicity (P). They are first performed after a positive time \(s>0\), up to localizing stopping times \(\tau_m<\sigma\), using the instantaneous regularity from Section 8.2. Events \(\{\sigma>s,\|u(s)\|_{L^r}\le N\}\in\mathscr F_s\) localize initial moments when necessary. For smooth coefficients the displayed Itô identities are standard; the component energy estimate extends by approximation and the regularization/linear-restart argument used in AV24a. The formal adjoint calculation below is explicitly not claimed as an established BSPDE existence theorem for rough coefficients.

### 3.1 What parabolicity and Lipschitz noise really control

For \(r\ge2\), write
\[
Y_r=\sum_i\int_{\mathbb T^d}u_i^r,\qquad
D_r=\sum_i\int_{\mathbb T^d}u_i^{r-2}|\nabla u_i|^2.
\]
Itô's formula gives
\[
\begin{split}
dY_r={}&-r(r-1)\sum_i\nu_i\int u_i^{r-2}|\nabla u_i|^2\,dt
+r\sum_i\int u_i^{r-1}f_i(u)\,dt\\
&+\frac{r(r-1)}2\sum_i\int u_i^{r-2}
 \|((b_{n,i}\cdot\nabla)u_i+g_{n,i}(u))_n\|_{\ell^2}^2\,dt+dM_r.
\end{split}\tag{E}
\]
The pure transport part of the quadratic variation is **positive**. Combined with the negative Laplacian term it leaves at least \(\mu/2\) of diffusion before the cross term is estimated. Young's inequality, reserving part of that margin, and \(\|g_i(u)\|_{\ell^2}\le L u_i\), yield
\[
dY_r+c_rD_r\,dt
\le r\sum_i\int u_i^{r-1}f_i(u)\,dt+C_rY_r\,dt+dM_r.
\tag{E1}
\]
Thus it is valid to absorb the transport correction in this **componentwise** energy calculation. It does not remove the weighted reaction term. Quadratic growth bounds that term by \(C(1+\int S^{r+1})\), where \(S=\sum_i u_i\); the extra power is exactly the unclosed quantity.

A concrete algebra check rules out deriving the needed coercivity just from mass control. Take
\[
f_1(u,v)=uv,\qquad f_2(u,v)=-uv.
\]
It is quasi-positive, quadratic and has zero total reaction. Nevertheless, at \((u,v)=(2R,R)\),
\[
u f_1+v f_2=2R^3.
\]
More generally, for any positive diagonal weights \(\alpha_1,\alpha_2\) and \(r>1\), choosing a fixed ratio \(u/v\) with \(\alpha_1u^{r-1}>\alpha_2v^{r-1}\) makes
\(uv(\alpha_1u^{r-1}-\alpha_2v^{r-1})\) grow as \(R^{r+1}\), not \(R^r\). The same example gives positive entropy production \(uv\log(u/v)\) when \(u>v\). This disproves two proposed implications—mass control implies diagonal energy coercivity, and mass control implies entropy dissipation—without being a blow-up counterexample. The system itself is in a known tractable subclass.

### 3.2 The equation for total concentration

Put
\[
S=\sum_i u_i,\quad V=\sum_i\nu_i u_i,\quad F=\sum_i f_i(u),\quad
G_n=\sum_i g_{n,i}(u),\quad
H_n=\sum_i b_{n,i}\cdot\nabla u_i.
\]
Then
\[
dS=\Delta V\,dt+F\,dt+\sum_n(H_n+G_n)\,dW^n,
\quad F\le K_0+K_1S,\quad\|G\|_{\ell^2}\le LS.
\tag{M}
\]
Where \(S>0\), let \(\lambda_i=u_i/S\) and \(a=V/S\); choose any admissible values at \(S=0\). Then \(\min_i\nu_i\le a\le\max_i\nu_i\) and \(\Delta V=\Delta(aS)\). This is the deterministic duality structure.

Two extra problems are visible already in (M).

* With species-dependent transport, \(H\) is not simply a prescribed smooth coefficient times \(\nabla S\).
* Even the spatial total mass is not automatically controlled by the reaction inequality. For smooth \(b\),
  \[
  \int H_n=-\sum_i\int(\operatorname{div}b_{n,i})u_i.
  \]
  A bound by \(\int S\) requires control of these divergences. It is absent for arbitrary \(C^\gamma\), \(0<\gamma<1\). One cannot differentiate the Hölder coefficients and then assume their derivatives are bounded.

If all transports are divergence-free, their integrals vanish. In that **restricted** situation, with \(m(t)=\int S(t)\), the diffusion coefficient in its scalar stochastic inequality is bounded by \(Lm(t)\). Localized BDG and stochastic Gronwall give finite-horizon mass moments after localizing the initial mass. There is no such conclusion from a reaction mass inequality alone with arbitrary compressible rough transport. This observation is a restriction of a priori estimates, not a proof of global regularity.

### 3.3 Why deterministic improved duality cannot simply be averaged

For \(b=0\), deterministic duality tests the mass equation with the solution of a backward equation of the form
\[
-\partial_t\phi-a\Delta\phi=\psi,\qquad \phi(T)=0,\qquad\psi\ge0.
\tag{D}
\]
In the SPDE, \(a(t)=V(t)/S(t)\) is random and adapted. Solving (D) separately for each path generally makes \(\phi(t)\) depend on \(a(r)\) for \(r>t\). It is not an admissible predictable integrand in \(\int\langle\phi,G\rangle dW\). Stopping the forward solution does not change this dependence on future coefficients.

The elementary defect in “its expectation is zero” is already seen by the illegal integrand \(W_T\): the pathwise sum \(\sum_j W_T(W_{t_{j+1}}-W_{t_j})\) equals \(W_T^2\), with expectation \(T\). This is not an Itô integral. It illustrates why a future-dependent test cannot be discarded as a martingale.

The adapted replacement, even with \(b=0\), is a backward SPDE
\[
d\phi=-(a\Delta\phi+\psi)\,dt+\sum_n Z_n\,dW^n,
\qquad\phi(T)=0.
\tag{BD}
\]
Itô's product rule now adds the quadratic-covariation term
\[
\sum_n\int\!\int G_nZ_n\,dx\,dt.
\tag{C}
\]
This term has no favourable sign. The valid Lipschitz bound gives
\(|\sum G_nZ_n|\le LS\|Z\|_{\ell^2}\), not zero. Closing an \(L^{2+\varepsilon}(\Omega\times Q_T)\) estimate needs estimates for the martingale integrand \(Z\) in the conjugate space, with the right constants, positivity of the dual solution, and a justified stopped duality identity. Deterministic maximal regularity for (D) supplies none of these martingale-integrand estimates. Small time or a suitable perturbative structure may help, but an absorption constant must be proved; it cannot be assumed.

Leocata–Vovelle does exactly the additional work of using a BSPDE: equation (3.10), p. 11, and estimates through pp. 12–15. Its entropy structure and smallness condition \(C_B\nu\le1\) control its own covariance term. Those hypotheses do not follow from Problem 8. This is evidence that the objection is substantive, not a claim that stochastic duality is impossible.

For clarity, even the more favourable divergence-free transport subcase leads formally to a nontrivial adjoint. Set
\[
\beta_n=\sum_i\lambda_i b_{n,i},\qquad H_n=\operatorname{div}(\beta_nS)
\]
when each \(b_{n,i}\) is divergence-free. Jensen's inequality and (P) give the useful identity of inequalities
\[
a|\xi|^2-\frac12\sum_n|\beta_n\cdot\xi|^2
\ge\sum_i\lambda_i\left(\nu_i|\xi|^2-\frac12\sum_n|b_{n,i}\cdot\xi|^2\right)
\ge\frac\mu2|\xi|^2.
\tag{J}
\]
So positivity and the Itô sign do preserve effective parabolicity. But \(\beta\) depends on the solution's ratios and is only bounded measurable. The candidate backward equation is
\[
d\phi=-\left(a\Delta\phi-\sum_n\beta_n\cdot\nabla Z_n+\psi\right)dt
       +\sum_n Z_n\,dW^n.
\tag{BT}
\]
The sign of the \(-\beta\cdot\nabla Z\) term follows from the adjoint of \(\operatorname{div}(\beta\,\cdot)\). In the product with (M), it cancels the transport contribution to the covariance, leaving (C) and the reaction term. With compressible smooth coefficients there are additional terms \(-S\sum_i\lambda_i\operatorname{div}b_{n,i}\) in the noise. For arbitrary Hölder transport even this decomposition is unavailable with bounded zero-order coefficients.

I have not proved the required positive dual solvability and uniform \(L^{p'}\)-estimates for (BT), or the consequent improved forward estimate under Problem 8's hypotheses. Applying the survey's stochastic maximal regularity theorem to \((a,\beta)\) is unjustified: their spatial regularity is not the regularity assumed in that theorem. Formula (J) is a valid necessary check, not a replacement for that missing theorem.

### 3.4 Exponents: an improvement just above two is not all-dimensional closure

Even if the missing improved estimate supplied \(u\in L^{2+\varepsilon}(Q_T)\), its direct use in an ordinary parabolic bootstrap requires care. For quadratic drift, \(u\in L^q\) gives \(f(u)\in L^{q/2}\). With parabolic dimension \(D=d+2\), deterministic heat potential smoothing gives the schematic update
\[
\frac1{q_{\rm new}}=\frac2q-\frac2D,
\quad\text{hence}\quad
q_{\rm new}=\frac{Dq}{2D-2q}
\tag{B}
\]
when the exponents are finite and admissible. Improvement requires
\[
q>\frac{d+2}{2}.
\]
For \(q=2+\varepsilon\) this says \(\varepsilon>(d-2)/2\). An unspecified small positive improvement works for this drift threshold in dimensions one and two; it does not reach all dimensions, and in dimension three needs \(\varepsilon>1/2\). Noise has its own mixed-norm and moment requirements, so (B) is a check on the deterministic bootstrap, not a claimed SPDE theorem. No exchange of probability and time exponents was made.

Likewise, \(L^{2+\varepsilon}(Q_T)\) alone is not the critical trace limit or the pair of norms in Theorem 5.1. That theorem (v5 p. 34 / published p. 48) rules out finite explosion when a limit exists in \(X_{1-(1+\kappa)/p,p}\), or when both the corresponding time supremum and \(L^p(0,\sigma;X_{1-\kappa/p})\) norm remain finite. Theorem 8.9, v5 p. 71 / published p. 100, provides the usable reaction–diffusion variants. At quadratic scaling, the critical concentration exponent is \(d/2\); a sufficiently strong bound \(\sup_{s<t<\sigma}\|u(t)\|_{L^r}<\infty\), with admissible parameters and \(r>\max\{2,d/2\}\), would suffice. None was established from (1)–(5). An expected mass bound cannot be substituted for it.

### 3.5 The FMT/De Giorgi alternative also leaves a missing stochastic estimate

FMT introduces \(\widehat V(t)=\int_0^tV(r)dr\), with an auxiliary positive heat solution, and obtains a scalar equation with merely measurable uniformly positive coefficient. Its Hölder estimate and the gradient interpolation lemma close a strict sublinear power inequality for \(\|u\|_\infty\). In the stochastic equation, the integrated mass identity becomes
\[
S(t)=S(0)+\Delta\widehat V(t)+\int_0^tF(r)dr+
\sum_n\int_0^t(H_n+G_n)\,dW^n.
\tag{POT}
\]
The last term is not a bounded deterministic source controlled by the reaction mass inequality. In particular it contains \(\nabla u_i\) with species-dependent coefficients. Removing it by writing \(u=v+Z\) leaves \(v\) of arbitrary sign and reactions \(f(v+Z)\); the positivity-based ratios and comparison inequalities used by FMT no longer follow for \(v\). A separate stochastic estimate is needed before the deterministic potential proof applies.

The 2025 stochastic DGNM theorem does not fill this exact gap: its operator is scalar divergence form and its sources must already have the specified mixed-norm integrability; the coefficient \(b\) is smooth. The mass equation involves \(\Delta(aS)\), the adjoint diffusion, not \(\operatorname{div}(a\nabla S)\). Replacing one by the other adds uncontrolled derivatives of the merely measurable ratio \(a\). Species-specific stochastic flows would also evaluate the reaction components at different spatial points and lose the common-point mass cancellation. These are the particular steps preventing a valid import of FMT here.

The entropy-based CGV/Souplet route cannot simply avoid the difficulty: mass control does not imply its entropy sign, as the explicit transfer example above shows. The CGV Hölder-potential argument and its De Giorgi scaling use more than an \(L^2\) estimate, so attributing an all-dimensional bootstrap to that estimate alone would also be incorrect.

### 3.6 Superlinear \(g\)

For the intended optimal order \(3/2\), use \(h=2\) in (8.4.3). The face condition then gives
\[
\|g_i(u)\|_{\ell^2}\lesssim u_i(1+|u|^{1/2}).
\]
The noise contribution to (E) is bounded by a multiple of
\(\sum_i u_i^r(1+|u|)\), including order \(r+1\), rather than the order-\(r\) term in (E1). It is positive and has no general cancellation from \(\sum_i f_i\le K_0+K_1S\). A coercive reaction can absorb it, explaining the scope of AV24a, but plain mass control supplies no such coercivity. This demonstrates why the follow-up cannot be inferred from the Lipschitz-noise argument; it does not establish blow-up or disprove global existence.

## 4. What was checked, and the remaining claim

The evidence and checks are saved alongside this report:

- `data/fetch_manifest.jsonl`: retrieval URLs, timestamps, byte hashes and page counts. Remote PDF bytes were held in memory and piped to `pdftotext -layout - -`; no PDF file or page image was written.
- `data/source_comparison.json`: exact page-marked-text matches for the supplied survey v5, supplied AGV v2 (`reaction_2026.txt`) and supplied AGV v3, against freshly retrieved versions. The supplied published survey was checked at the relevant passages against the institutional-repository copy.
- `data/source_index.json` and `data/source_headings.txt`: theorem/assumption headings with file line numbers and PDF page numbers. Journal page numbers were checked against printed headers, accounting for repository cover sheets.
- `data/search_log.md`: the search terms, versions, access limitations, and excluded false lead. The PSY manuscript was read through an author-uploaded online text; its online manuscript page numbers, not unverified journal theorem pages, are reported.
- `code/check_algebra.py` and `data/algebra_checks.json`: exact rational checks of the drift/noise exponent conversion, the bootstrap threshold, the critical trace identity, the transfer-reaction energy calculation by two formulas, and the sign/margin of the Itô correction. These checks verify algebra only, not the missing stochastic analytic estimate.
- `LOG.md`: progress and decisions. There were no subagents, simulations, pushes, external publications, or changes outside the task directory. Source retrieval used at most four concurrent lightweight jobs; the extraction script preserves inherited niceness when it is already at least 10, avoiding an unnecessary priority change.

The load-bearing stochastic points were rechecked in two forms: direct componentwise Itô energy and adjoint-product covariance; the scaling exponent was checked both from the trace equality and the parabolic heat-potential relation. The checks support the stated obstruction, not an impossibility theorem. In particular:

1. Parabolicity has the correct coercive sign after the positive transport quadratic variation is included.
2. An adapted stochastic dual requires a martingale integrand, and its covariance with forward noise remains in the estimate.
3. A deterministic future-dependent dual does not become an adapted test by stopping the forward solution.
4. \(L^{2+\varepsilon}\) by itself does not imply the blow-up criterion in arbitrary dimension.
5. Superlinear noise adds a higher-order positive Itô term, which mass control alone does not sign-control.

The missing result is a quantitative, stopped stochastic duality/potential estimate for the actual species-dependent rough transport equation, strong enough to enter a valid bootstrap and the survey's blow-up criteria. It has not been established in this work. The source's full base question and its superlinear extensions therefore remain unproved here. No unproved lemma is promoted to a PARTIAL theorem.

Task: “Open problem I0072” — run began 13 November 2026, 18:56 Asia/Tbilisi (the user-message timestamp was not supplied).
