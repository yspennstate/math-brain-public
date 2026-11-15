PARTIAL

# D0064: solutions of the continuous star-equation

Task: “Open problem D0064”; started 2026-11-13 08:26 +04 (Asia/Tbilisi).

The full classification has not been proved here. The literature audit has found the known moment-based classification and construction/approximation uniqueness results, but no theorem that classifies every solution in the conjectured class. Two restricted statements are proved below, with their extra hypotheses explicit. Numerical evidence concerns a binary cascade.

## Exact question and literature audit

The requested arXiv source is saved in `sources/rhodes_vargas_2014.txt`; its Section 6 occupies pp. 42–55, and Conjecture 6.4 is on p. 52. The published version is separately saved in `sources/rhodes_vargas_2014_journal.txt`. Its numbering and pagination differ. Citations below distinguish the versions.

For a stationary, positive, locally finite random Radon measure M on R^d, the equation is an equality of random-measure laws:

\[
 M(dx)\overset d=e^{\omega_\varepsilon(x)}M^\varepsilon(dx),\qquad
 (M^\varepsilon(A))_A\overset d=(M(A/\varepsilon))_A,
 \qquad M^\varepsilon\perp\omega_\varepsilon. \tag{S}
\]

The field is stationary, Gaussian and stochastically continuous. This is review Definition 2.17, equations (2.17)–(2.18), arXiv pp. 17–18. ARV uses a different normalization: its rescaled measure includes a factor epsilon^d, and its exponential weights have expectation one.

The conjecture concerns nontrivial **ergodic lognormal** star-scale invariant measures, up to a deterministic constant. The review explicitly says stronger dependence decay than ergodicity is needed but does not give a fully quantified minimal condition in Section 6.3. DRSV Section 4.1 gives a concrete short-range version: masses on sets separated by a fixed distance R are independent. Thus stationary alone is not the intended class, and a nonergodic global random multiplier does not refute the conjecture.

If alpha in (0,1] exists with E exp(alpha omega_epsilon)=epsilon^d, the canonical parametrization, with t=log(1/epsilon), is

\[
 \omega_{e^{-t}}(x)=\frac{\gamma}{\alpha}X_t(x)
       -\frac{\gamma^2/2+d}{\alpha}t,\qquad
 \mathbb E[X_t(x)X_s(y)]=\int_0^{t\wedge s}k(e^u(x-y))\,du,
 \quad k(0)=1. \tag{P}
\]

In particular E exp(q omega)=exp{[gamma^2 q^2/(2 alpha^2)−(gamma^2/2+d)q/alpha]t}. The normalization and the admissible root condition must not be assumed proved for every stationary fixed point. RSV states existence of alpha as Conjecture 23, immediately before Conjecture 24. The review assumes it before listing the four cases.

For alpha=1 the predicted measure is c times subcritical GMC when gamma^2<2d, and c times derivative chaos when gamma^2=2d. For 0<alpha<1 it is the stable random measure over the respective control chaos Z:

\[
 \mathbb E[e^{-M(f)}\mid Z]=\exp\{-c\int f(x)^\alpha Z(dx)\},\qquad f\ge0.
 \tag{L}
\]

The alpha and gamma in (P) are independent parameters of this classification. A special physical duality relation or the low-temperature relation alpha=sqrt(2d)/beta does not apply to every dual-phase solution.



### What the checked literature proves

Theorem/page locators refer to the saved text's PDF pagination unless journal pages are explicitly given. Full-text source URLs and hashes are in `sources/MANIFEST.txt`.

| Work | Exact result and locator | Consequence for D0064 |
|---|---|---|
| Rhodes–Vargas, *Probability Surveys* 11 (2014), 315–392, [DOI 10.1214/13-PS218](https://doi.org/10.1214/13-PS218) | arXiv:1305.6221, Conjecture 6.4, p. 52; **published version Conjecture 6.2, p. 369**, with its setup on p. 368 | The requested classification. Published numbering differs from the prompt's arXiv numbering. |
| Allez–Rhodes–Vargas, *PTRF* 155 (2013), 751–788, [arXiv:1102.1895v3](https://arxiv.org/abs/1102.1895) | Theorem 4, p. 5 (d=1); Theorem 10, p. 6 (general d, with differentiability off zero); Definition 3, p. 4 | Good Gaussian star weights plus a finite 1+delta moment imply M=YQ, with Q a GMC independent of Y. Ergodicity makes Y deterministic. The general-d statement has an extra regularity hypothesis. This does not classify solutions with only moments below one. |
| Rhodes–Sohier–Vargas, *Ann. Probab.* 42 (2014), 689–724, [DOI 10.1214/12-AOP810](https://doi.org/10.1214/12-AOP810), arXiv:1201.5219 | Assumption 15, journal pp. 697–698; Theorem 16, p. **698**; Conjectures 23–24, pp. **704–705** | Classification beyond Gaussian weights with a 1+delta moment: M=YQ for Lévy chaos Q with rate g(y)=y. The good assumptions include a second exponential moment of the weight field, decorrelation and scale regularity. Conjecture 24 gives precisely the corresponding four-phase question. The final journal title uses “random structures”; the arXiv title uses “random measures.” |
| Barral–Jin–Rhodes–Vargas, *Comm. Math. Phys.* 323 (2013), 451–485, [arXiv:1202.5296](https://arxiv.org/abs/1202.5296) | Theorem 2, pp. 10–11; Proposition 4 and Remark 5, p. 11; conditional Laplace formula (14), p. 10 | Constructs the atomic dual measure and identifies its stable conditional law. Gives existence and approximation independence within that construction, not classification of arbitrary fixed points. |
| Duplantier–Rhodes–Sheffield–Vargas, *Ann. Probab.* 42 (2014), 1769–1808, [arXiv:1206.1671](https://arxiv.org/abs/1206.1671) | Theorem 4, pp. 10–11; Proposition 5, pp. 11–12; Section 4.1, pp. 12–13 | Constructs the positive, diffuse derivative measure and proves it solves the star-equation. Section 4.1 explicitly leaves the uniqueness part of the four-case statement to be completed. |
| Duplantier–Rhodes–Sheffield–Vargas, *Comm. Math. Phys.* 330 (2014), 283–330, [arXiv:1212.0529](https://arxiv.org/abs/1212.0529) | Theorem 5, p. 8 | Critical Seneta–Heyde convergence to a constant times derivative chaos. This is a renormalized approximation theorem. |
| Madaule–Rhodes–Vargas, *Ann. Appl. Probab.* 26 (2016), 643–690, [arXiv:1310.5574v1](https://arxiv.org/abs/1310.5574) | Theorem 2.2 and Corollary 2.3, p. 4, under Assumption (A), p. 3 | Proves freezing and identifies the stable measure over derivative chaos for the specified approximations. Resolves the separate freezing-limit conjecture in that setting. Does not classify every solution of (S). |
| Barral–Kupiainen–Nikula–Saksman–Webb, *Ann. Probab.* 43 (2015), 2205–2249, [arXiv:1303.4548](https://arxiv.org/abs/1303.4548) | Theorem 1, p. 6; Theorems 2 and 4, p. 7 | Tail asymptotics, continuity and dimension results for the constructed one-dimensional critical chaos. These are not a uniqueness theorem for arbitrary star solutions. Their *Critical Mandelbrot cascades*, CMP 325 (2014), 685–711, concerns the tree analogue. |
| Junnila–Saksman, *Electron. J. Probab.* 22 (2017), paper 11, 1–31, [arXiv:1506.05099](https://arxiv.org/abs/1506.05099) | Saved arXiv version, Theorem 1.1, p. 3 | Compares two approximation sequences under covariance conditions, assuming a nonatomic limit for one. “Uniqueness” means approximation independence, not classification of all solutions of (S). The arXiv title is *The uniqueness of the Gaussian multiplicative chaos revisited*. |
| Powell, *Electron. J. Probab.* 23 (2018), paper 31, 1–26, [arXiv:1704.06058](https://arxiv.org/abs/1704.06058) | Theorems 1.1–1.2, p. 3 of saved arXiv version | Derivative-normalized convolution approximations converge to the canonical critical measure, independently of the mollifier. |
| Powell, *Markov Process. Related Fields* 27 (2021), 557–606, [arXiv:2006.13767](https://arxiv.org/abs/2006.13767) | Theorem 2.5, p. 9 of saved version | General critical construction; surveys the distinction between constructions and their universality. |
| Bertacco–Hairer, *Electron. J. Probab.* 30 (2025), 1–22, [DOI 10.1214/25-EJP1449](https://doi.org/10.1214/25-EJP1449), [arXiv:2504.07552v3](https://arxiv.org/abs/2504.07552) | Theorem A, p. 4 of v3; assumptions (A1)–(A2), p. 2, and Sobolev regularity in Theorem A | General convolution approximations converge stably to the frozen measure, up to a mollifier-dependent constant. Its title, *Uniqueness of supercritical Gaussian multiplicative chaos*, does not assert arbitrary-fixed-point uniqueness. |

The requested “Durand” and “Biermé–Durand” pointers did not identify a relevant classification paper in the searches. Searches also surfaced Biermé–Durieu–Wang on generalized random fields, which is a different author combination and subject. No classification theorem is attributed to these ambiguous pointers.

The search included the supplied author/title combinations, “star-equation”, “star-scale invariant”, “classification”, “solutions” and “uniqueness”, and forward citations dated 2014–2026 to the review and RSV. The saved OpenAlex metadata records the queries, returned titles and an authentication failure in cursor pagination; date-partitioned requests supplement that search, giving 408 distinct review-citation records and 23 RSV records. These are metadata records, not full-text audits of every citing work. Metadata and search snippets were used to select papers, not as proofs of theorem content. No checked result resolves all of Conjecture 6.4. This is a bounded literature search, not a claim that every relevant 2026 paper has been read.

## Reduction to smoothing-transform ideas

For a tree with independent reproduction vectors (T_i), the fixed-point equation is

\[
 Y\overset d=\sum_i T_iY_i,
 \qquad \phi(q)=\mathbb E\prod_i\phi(qT_i),
 \qquad Y_i\text{ iid and independent of }(T_i).
\]

Write L(v) for the product of weights on the path to v and m(q)=E sum_i T_i^q. Under the usual supercritical branching, integrability and nonlattice hypotheses, the characteristic exponent satisfies m(alpha)=1 and m'(alpha)<=0. In the regular case, the endogenous control W is the limit of sum_{|v|=n} L(v)^alpha. In the boundary case m'(alpha)=0, it is a derivative-martingale limit D. All nonzero nonnegative fixed points have Laplace transform

\[
 \phi(q)=\mathbb E\exp(-c q^\alpha W)
 \quad\text{or}\quad
 \phi(q)=\mathbb E\exp(-c q^\alpha D). \tag{T}
\]

For alpha=1 these reduce to cW and cD. For alpha<1 they are stable mixtures. In lattice cases a multiplicatively periodic factor can replace c; the Gaussian nondegenerate weights used below are nonlattice. Thus “complete classification” always carries hypotheses on the reproduction law.

Precise references: Alsmeyer–Biggins–Meiners, *Ann. Probab.* 40 (2012), 2069–2105, [arXiv:0906.3133](https://arxiv.org/abs/0906.3133), Theorem 2.2, p. 5, Corollary 2.3, p. 6, and Theorem 8.3, p. 14 of the saved version. For regular and boundary cases together, Alsmeyer–Mallein, *J. Theoret. Probab.* 35 (2022), 2569–2599, [arXiv:1907.04111](https://arxiv.org/abs/1907.04111), Theorems 1.2 and 1.5, pp. 5 and 6. These specify the moment assumptions and geometric exception. Earlier references are Durrett–Liggett, *Z. Wahrscheinlichkeitstheorie verw. Gebiete* 64 (1983), 275–301, [DOI 10.1007/BF00532962](https://doi.org/10.1007/BF00532962), and Liu, *Adv. Appl. Probab.* 30 (1998), 85–112, [DOI 10.1239/aap/1035227993](https://doi.org/10.1239/aap/1035227993). The 1995 Liu preprint was also saved; its theorem numbering is not silently substituted for the 1998 paper.

The tree proof disintegrates an arbitrary fixed point through

\[
 F_n(q)=\prod_{|v|=n}\phi(qL(v)).
\]

The branching property makes this a bounded martingale. Renewal/harmonic-function arguments identify its limit as exp(−c q^alpha W), or the derivative version. The stable extra randomness is a conclusion of the proof.

For the continuum, iterating (S) produces a coarse field times **one spatially dependent rescaled measure**. Values in distinct cells are not iid copies conditional on the coarse field. Even a finite dependence range only provides separated cells, with intervening regions and field variation to control. There is no immediate product of one-variable transforms to which the tree renewal theorem applies. The missing general step is to recover, from an arbitrary solution, the canonical control chaos and the conditional functional (L), including conditional independence on disjoint sets. Establishing (L) for a constructed solution is the easy direction and does not establish that recovery. Theorems A and B below isolate two restricted versions of this step.

## Theorem A: classification with a specified conditional Lévy decomposition

Fix 0<alpha<=1. Let Z be a given nonzero stationary positive random Radon measure, chosen to be the canonical subcritical GMC or the critical derivative chaos. At some epsilon in (0,1), let W(x)=exp(omega_epsilon(x)) be a positive continuous stationary field with a nondegenerate lognormal one-point law. Suppose Z has its usual scale decomposition

\[
 Z_*=W^\alpha Z^\varepsilon,\qquad Z_*\overset d=Z,
 \qquad Z^\varepsilon(A)\overset d=Z(A/\varepsilon),
 \qquad W\perp Z^\varepsilon. \tag{A1}
\]

Here and below multiplication means multiplication of a measure by the displayed function. For the Gaussian parametrization (P), (A1) is exactly the star decomposition of subcritical or derivative chaos with Gaussian weight alpha omega.

For an arbitrary nonnegative Lévy exponent

\[
 \psi(q)=a q+\int_{(0,\infty)}(1-e^{-qz})\,\nu(dz),\quad
 a\ge0,\quad \int(1\wedge z)\nu(dz)<\infty, \tag{A2}
\]

let K_psi(zeta) be the law with Laplace functional exp(−int psi(f) dzeta). No stability assumption is made. Suppose a pair (Z,M) has conditional law M|Z=K_psi(Z), and a rescaled copy (Z^epsilon,M^epsilon) of that pair is independent of W. Impose the following additional compatibility of the small-scale decomposition:

\[
 \mathcal L(WM^\varepsilon\mid W,Z^\varepsilon)
       =K_\psi(W^\alpha Z^\varepsilon). \tag{A3}
\]

Thus, after multiplying the fine-scale measure by the coarse field, its conditional law uses the same exponent and the updated control measure. This is a substantive assumption about the coupling; it does **not** follow merely from the marginal fixed-point equation (S).

**Conclusion.** If M is nonzero, there is c>0 such that psi(q)=c q^alpha for all q>=0. If alpha=1, M=cZ almost surely in this coupling. If alpha<1, M is exactly the positive alpha-stable atomic measure over Z, with Laplace functional (L). Conversely these laws satisfy (A3) and (S), with the joint scaling of the pair. The conditional classification applies both below and at criticality, without a moment assumption on Z or M.

### Proof

Conditional on W and Z^epsilon, the assumed fine-scale Lévy law gives

\[
 \mathbb E[e^{-(WM^\varepsilon)(f)}\mid W,Z^\varepsilon]
   =\exp\{-\int\psi(W(x)f(x))Z^\varepsilon(dx)\}.
\]

By (A3) the same expression equals

\[
 \exp\{-\int W(x)^\alpha\psi(f(x))Z^\varepsilon(dx)\}.
\]

All exponents are finite for bounded f of compact support: W is locally bounded, psi is finite and continuous, and Z^epsilon is locally finite. Taking f=1_A for a countable generating ring of bounded boxes and using injectivity of the exponential gives equality of the locally finite measures

\[
 \psi(W(x))Z^\varepsilon(dx)
       =W(x)^\alpha\psi(1)Z^\varepsilon(dx)\quad\text{a.s.} \tag{A4}
\]

The simultaneous event is obtained from the countable ring; equality extends to all bounded Borel sets by uniqueness of measures. Put h(w)=psi(w)−w^alpha psi(1). Hence h(W(x))=0 for Z^epsilon-almost every x, almost surely.

Choose a bounded box B with P(Z^epsilon(B)>0)>0. Such a box exists since Z^epsilon is nonzero with positive probability and R^d is a countable union of boxes. Define the finite deterministic measure

\[
 \mu_B(dx)=\mathbb E\left[\frac{1_B(x)Z^\varepsilon(dx)}{1+Z^\varepsilon(B)}\right].
\]

It has 0<mu_B(B)<=1. Independence of W and Z^epsilon, stationarity of the one-point law of W, and Tonelli's theorem give

\[
 0=\mathbb E\int_B
       \frac{1_{\{h(W(x))\ne0\}}}{1+Z^\varepsilon(B)}Z^\varepsilon(dx)
   =\mathbb P(h(W(0))\ne0)\mu_B(B).
\]

Thus h(W(0))=0 almost surely. A nondegenerate lognormal law gives positive mass to every open subinterval of (0,infinity). Continuity of h therefore implies h(w)=0 for every w>0. Consequently psi(q)=c q^alpha, c=psi(1). If c=0 the exponent vanishes and M is zero, so nontriviality gives c>0.

For alpha=1 the conditional functional exp(−c int f dZ) is that of the deterministic measure cZ. For 0<alpha<1, integration by parts gives

\[
 \int_0^\infty(1-e^{-qz})z^{-1-\alpha}\,dz
    =\frac{\Gamma(1-\alpha)}{\alpha}q^\alpha. \tag{A5}
\]

The boundary terms vanish because alpha lies strictly between zero and one; substituting u=qz then yields the gamma integral. Given Z, take a Poisson random measure on R^d x (0,infinity) with intensity

\[
 Z(dx)\,\frac{c\alpha}{\Gamma(1-\alpha)}z^{-1-\alpha}\,dz
\]

and sum z delta_x over its points. On any compact set, jumps greater than one are finite in number. The sum of jumps below one has finite conditional expectation, since int_0^1 z z^{−1−alpha} dz<infinity. Hence the measure is locally finite almost surely and purely atomic. The Poisson Laplace formula and (A5) give precisely (L). That formula follows first for jumps restricted to [1/n,n], where the compound Poisson calculation applies, then by monotone convergence. Uniqueness of the Laplace functionals identifies the required conditional law.

Conversely, for psi(q)=c q^alpha,

\[
 \psi(Wf)=c(Wf)^\alpha=W^\alpha\psi(f)
\]

pointwise. The preceding conditional calculation proves (A3). Taking expectations and using (A1) proves the joint law of (Z_*,WM^epsilon) equals that of (Z,M), hence proves (S). Scaling the conditional functional verifies the required joint law of the fine pair. This completes both directions. □

For a zero Gaussian parameter the nondegenerate one-point assumption is unavailable. If (A3) holds at every scale and W=epsilon^{d/alpha}, equality of conditional functionals instead gives psi(epsilon^{d/alpha}q)=epsilon^d psi(q). Varying epsilon and q gives the same homogeneity and conclusion.

If the control chaos has independence for regions at distance greater than R, the resulting M has this property too: conditionally on the control, restrictions to disjoint regions are independent, and their conditional laws depend only on the corresponding control restrictions. This proves independence first for Laplace functionals, then for the restrictions' laws. In particular these examples are mixing and ergodic under translations. Thus the theorem's class contains actual members of the intended short-range class. The new assumption is the conditional Lévy decomposition and (A3), not stationarity alone. No novelty relative to standard Lévy-basis homogeneity arguments is claimed.

## Theorem B: an L2 classification allowing non-Gaussian weights

This gives a separate restricted result that starts from the marginal star-equation and proves that its independent terminal randomness disappears. It needs no conditional Lévy representation.

Let (W_t(x))_{t>=0,x in R^d} be a jointly measurable stationary positive field, locally bounded for finite t, such that:

1. W_0=1 and, for each x, W_t(x) is a mean-one martingale in a common filtration. It has independent multiplicative scale increments: the increment from t to t+s is an independent copy of W_s(e^t x).
2. For a measurable function F and constants R>0, 0<=kappa<d,

\[
 \mathbb E[W_t(x)W_t(y)]
   =\exp\left\{\int_0^t F(e^s(x-y))\,ds\right\},\qquad
 F(0)=\kappa,\quad F(z)\le\kappa 1_{\{|z|\le R\}}. \tag{B1}
\]

Let M be a stationary positive random Radon measure with E M(dx)=c dx, 0<c<infinity, and finite second moments on compact sets. Suppose its reduced covariance is a finite signed measure C: for bounded compactly supported f,g,

\[
 \operatorname{Cov}(M(f),M(g))
   =\int_{\mathbb R^d}\!dx\int_{\mathbb R^d} C(dz)f(x)g(x+z),
 \qquad |C|(\mathbb R^d)<\infty. \tag{B2}
\]

For each t suppose the marginal star-equation takes the normalized form

\[
 M\overset d=W_t U_t,\qquad
 U_t(A)=e^{-dt}M'(e^t A),\qquad M'\overset d=M,\quad M'\perp W_t. \tag{B3}
\]

**Conclusion.** Along integer t, the chaos Q_t(dx)=W_t(x)dx converges locally to a random Radon measure Q with convergence in L2 against continuous compactly supported tests, and

\[
 M\overset d=cQ.
\]

In fact the terminal-noise error has the explicit bound

\[
 \mathbb E\big[(M_t(f)-cQ_t(f))^2\big]
 \le \|f\|_\infty\|f\|_1 |C|(\mathbb R^d)
                 e^{-(d-\kappa)t},\qquad M_t=W_tU_t. \tag{B4}
\]

For Gaussian W_t=exp(gamma X_t−gamma^2 t/2), take F=gamma^2 k, k supported in the radius-R ball, and kappa=gamma^2. This proves uniqueness in the restricted alpha=1, gamma^2<d class satisfying (B2). It does not reach the full gamma^2<2d interval or criticality. For non-Gaussian scale fields the same proof applies verbatim if (B1) holds.

### Proof

For z!=0, the upper bound on F implies

\[
 \int_0^t F(e^sz)\,ds
       \le\kappa\min\{t,\log_+(R/|z|)\}.
\]

Therefore

\[
 \mathbb E[W_t(x)W_t(y)]\le H(x-y),\qquad
 H(z)=\max\{1,(R/|z|)^\kappa\}. \tag{B5}
\]

H is locally integrable because kappa<d. Consequently, for compactly supported f,

\[
 \sup_t\mathbb E Q_t(f)^2
    \le\int\!\int |f(x)f(y)|H(x-y)\,dx\,dy<\infty.
\]

Conditional Fubini shows Q_t(f) is a martingale. Its L2 boundedness gives convergence in L2 and almost surely along integer t, which suffices for the classification. Simultaneous convergence for a countable dense set of continuous compactly supported functions, together with convergence and boundedness of Q_t(h_j) for nonnegative continuous cutoffs h_j>=1 on an exhaustion of compact sets, yields a positive locally bounded linear functional. Extend it by uniform approximation on each compact support; the Riesz representation theorem gives a random Radon measure Q. This also proves local vague convergence. The L2 limit for any test f agrees with Q(f), and E Q(f)=int f dx. Thus Q is nontrivial.

Changing variables u=e^t x in (B2) proves

\[
 \operatorname{Cov}(U_t(h),U_t(g))
   =e^{-dt}\int dx\int C(dz)h(x)g(x+e^{-t}z). \tag{B6}
\]

Condition on W_t. Its local boundedness permits (B6) with h=g=f W_t. Independence gives E[M_t(f)|W_t]=cQ_t(f). By (B6), its conditional variance, after averaging over W_t, is

\[
 e^{-dt}\int C(dz)\int dx\,
 f(x)f(x+e^{-t}z)
 \mathbb E[W_t(x)W_t(x+e^{-t}z)]. \tag{B7}
\]

All operations are justified by the absolute bound below. From (B1), or directly Cauchy–Schwarz and E W_t(x)^2=e^{kappa t}, the last expectation is at most e^{kappa t}. Also

\[
 \int |f(x)f(x+e^{-t}z)|\,dx\le\|f\|_\infty\|f\|_1.
\]

Replacing C by its total variation in (B7) proves (B4). Thus M_t(f)−cQ_t(f) tends to zero in L2. For bounded Borel tests, the L2 limit agrees with integration against Q: approximate such a test almost everywhere by uniformly bounded continuous tests, then use (B5) and dominated convergence for the uniform second-moment bound. The construction of an independent U_t can be made separately for each t; consistency of these copies is unnecessary for this bound. Q_t(f) tends in L2 to Q(f) along integer t, so M_t(f) converges in distribution to cQ(f). Every M_t has the law of M by (B3). Apply the same argument to every linear combination of finitely many test functions. Their joint laws agree, and a countable measure-determining set of tests implies M has the law of cQ. □

The limit Q is atomless. Indeed (B5) gives E[Q(I)^2]<=C r^(2d−kappa) for a cube I of side r<=1. Cover a fixed bounded box by O(r^(−d)) such cubes. Markov's inequality bounds the probability that any cube has mass greater than eta by C eta^(−2) r^(d−kappa), which tends to zero. An atom of mass greater than eta would belong to one such cube at every resolution. Taking a countable union over rational eta>0 and bounded boxes excludes all atoms.

This assumption set is nonempty and is not restricted to Gaussian noise. For example, let N be a Poisson random measure on R^d x [0,infinity) with intensity lambda e^{ds} dz ds. Fix a ball B of finite volume and a nonzero real a. Set

\[
 P_t(x)=a\int_0^t\int 1_{\{e^s(z-x)\in B\}}N(dz,ds),\qquad
 W_t(x)=\exp\{P_t(x)-\lambda|B|(e^a-1)t\}.
\]

Disjoint scale intervals are independent and the change of variables z'=e^t z, s'=s−t gives the scale cocycle. The elementary Poisson exponential formula gives E W_t=1 and (B1) with

\[
 F(z)=\lambda(e^a-1)^2|B\cap(B+z)|,\qquad
 \kappa=\lambda(e^a-1)^2|B|.
\]

Choose lambda so kappa<d. On bounded spatial sets at finite t there are only finitely many relevant Poisson points, so W_t is locally bounded. The constructed Q has reduced covariance

\[
 C_Q(dz)=\left[\exp\left\{\int_0^\infty F(e^s z)\,ds\right\}-1\right]dz.
\]

Indeed L2 convergence passes the second moments to the limit for pairs of compactly supported tests. The density vanishes outside the difference ball B−B and is integrable near zero by (B5), so its total variation is finite. Splitting the scale process at t and passing to the limit proves (B3) for Q: multiplication by a fixed locally bounded weight is justified conditionally using the L2 bounds, first for simple functions and then by the bounded-Borel-test approximation above, conditional on the independent, locally bounded coarse field. Equivalently the same conclusion follows from the convergence of the fine chaos against the fixed test f W_t. Hence this is an explicit non-Gaussian example in the classified class.

The finite total variation in (B2) excludes a nonconstant global random intensity, whose covariance would contain a nonzero constant-density part. This matches the role of ergodicity. It is a stronger quantitative assumption than the conjecture's vague dependence decay, so Theorem B is not an unrestricted solution or a replacement for RSV Theorem 16.

## Discrete computation: evidence only

The binary tree has d=1, scale ratio 2, and independent edge increments G~N(0,log 2). Set

\[
 T_i=\exp\left\{\frac{\gamma}{\alpha}G_i
           -\frac{1+\gamma^2/2}{\alpha}\log2\right\},\qquad
 m(q)=2^{1-(1+\gamma^2/2)q/\alpha+\gamma^2q^2/(2\alpha^2)}.
\]

Then m(alpha)=1 and m'(alpha)=(log2)(gamma^2/2−1)/alpha. The regular and boundary choices are gamma^2=0.5 and 2; the other parameter is alpha=1 or 0.6. This reproduces all four parameter regimes without conflating alpha with the Gaussian coefficient of the atomic measure.

Let A_v=T_v^alpha and Z_n=sum_{|v|=n} product_{e<=v} A_e. The Gaussian tree is simulated explicitly. With independent terminal seeds having Laplace transform exp(−q^alpha), the n-step smoothing iterate has, conditional on the entire tree, Laplace transform exp(−q^alpha Z_n). Hence its mass can be simulated exactly in law as Z_n^{1/alpha} S_alpha. This conditional identity follows by multiplying the independent terminal Laplace transforms; it is not an assertion of continuum independence. For alpha=1 use S_1=1.

The program also computes the actual bounded-seed iterate sum_{|v|=n} product T_e, finite-depth critical derivative masses, and spatial cell masses with independent stable marks. It keeps the Gaussian control samples in CSV. Conditional Laplace estimates integrate out the additional stable variable analytically to reduce sampling noise.

The two runs use 512 independent root trees each: seed 20261113 to depth 18, and seed 20261114 to depth 16. Here are raw and renormalized medians from the first run. The listed critical normalization uses t=n log 2.

| Regime | alpha | gamma^2 | Raw median, n=8 | Raw median, n=18 | Normalization | Normalized median, n=8 | Normalized median, n=18 |
|---|---:|---:|---:|---:|---|---:|---:|
| Standard | 1 | 0.5 | 0.8171 | 0.8120 | 1 | 0.8171 | 0.8120 |
| Critical | 1 | 2 | 0.2226 | 0.1361 | t^(1/2) | 0.5241 | 0.4807 |
| Dual, stable seeds | 0.6 | 0.5 | 0.7021 | 0.6480 | 1 | 0.7021 | 0.6480 |
| Frozen, stable seeds | 0.6 | 2 | 0.1131 | 0.0458 | t^(1/(2 alpha)) | 0.4715 | 0.3749 |

The regular cases are consistent with a nonzero additive-chaos fixed point and its stable mixture. The raw critical cases decrease; the renormalizations keep their typical sizes at order one. This is limited finite-depth evidence. In the independent second run the normalized critical median is 0.3357 and the converted derivative median is 0.3993, so the critical approximation remains quantitatively rough.

At depth 18 the conditional Laplace estimates for the normalized candidates, at q=0.25, are:

| Standard | Critical | Dual | Frozen |
|---:|---:|---:|---:|
| 0.7973 ± 0.0050 | 0.7822 ± 0.0114 | 0.6831 ± 0.0070 | 0.7014 ± 0.0130 |

The errors here are one Monte Carlo standard error across independent root trees, not bounds on finite-depth bias. At q=1 the conditional transform of a stable mixture coincides with that of its control, so q=1 alone would not distinguish the regimes. Transforms at q=0.25, 1 and 4 are saved.

Initialization matters. With alpha=0.6, gamma^2=0.5 and bounded terminal seed 1, m(1)=0.7637175655<1. Its n-step expected total mass is m(1)^n, which is **exactly 1/128 at n=18**. Markov's inequality already proves collapse to zero in probability. The simulated medians decrease from 0.04744 at n=8 to 0.00262 at n=18. A positive dual fixed point exists, but this bounded-seed unnormalized iteration does not select it.

For frozen weights the bounded-seed median decreases from 0.01855 to 0.00329 between n=8 and 18. Its low-temperature normalization differs from stable-seed normalization: t^(3/(2 alpha)) gives medians 1.3429 and 1.8113. These depths show substantial correction terms and do not establish convergence to a specific constant multiple of the frozen law. For alpha=1 at criticality, the finite-depth derivative mass can still be negative: 4 of 512 samples were negative at depth 18. It was not clipped and used as if it were an exact positive fixed point. Its median after multiplying by sqrt(2/pi) is 0.5015, compared with 0.4807 for sqrt(t) Z_n.

For a separate spatial diagnostic, normalized cell masses have collision statistic I=sum_j p_j^2. Subcritical Gaussian control at depths 8,12,16 gives mean I=0.02273, 0.00605, 0.00112. Stable-marked cell masses instead give 0.4523, 0.3982, 0.3625, with standard errors 0.0272, 0.0245, 0.0254. The persistent collision mass is consistent with atomicity. The critical-control and stable-marked values at depth 16 are 0.06528 and 0.44539 ± 0.02444, respectively. Critical control remains more concentrated at these depths.

There is also an exact finite-partition check. If independent positive alpha-stable cell masses have control probabilities p_j summing to one, then

\[
 \mathbb E\sum_j\left(\frac{S_j}{\sum_i S_i}\right)^2
       =1-\alpha+\alpha\sum_j p_j^2. \tag{C}
\]

To verify (C), use s^(−2)=int_0^infinity u exp(−us)du and differentiate the transforms exp(−p_j u^alpha) twice. The two terms in the integral are alpha^2 sum p_j^2 times int u^(2alpha−1)e^(−u^alpha)du, and alpha(1−alpha) times int u^(alpha−1)e^(−u^alpha)du. Substitution v=u^alpha gives alpha sum p_j^2 and 1−alpha. Tonelli justifies the calculation. Thus the predicted depth-16 spatial values are 0.40067 (subcritical control) and 0.43917 (critical control), both within two reported standard errors of their simulations. This checks a feature of the simulated stable mixture; it does not test whether an arbitrary continuum solution has such a mixture representation.

One additional smoothing step applied to the depth-18 empirical normalized laws gives Laplace residuals at q=1 of 0.0040, 0.0107, 0.0103 and 0.0188 for standard, critical, dual and frozen. The terminal-sample standard errors are 0.0090, 0.0146, 0.0151 and 0.0178. The residuals and original estimates share terminal samples, so these are diagnostics, not independent-error confidence tests. The data are compatible with the candidates at this resolution; they cannot certify a fixed-point law.

### Reproduction and resource record

Run from this directory:

```sh
python3 code/cascade.py --seed 20261113 --depth 18
python3 code/cascade.py --seed 20261114 --depth 16
python3 code/check_math.py
```

The launcher here already provides nice 10, which each numeric program checks. Numeric libraries are restricted to one thread. The final recorded peak resident sizes are 1,238,302,720 and 1,086,275,584 bytes (about 1.24 and 1.09 GB, decimal); runtimes were about 11.2 and 4.1 seconds. macOS rejected an attempted RLIMIT_AS setting, so it is **not** reported as an enforced limit. Explicit array bounds and measured peak RSS kept the runs below the requested 4 GB. No subprocess workers, model workers or GPU compute were used.

The source fetcher holds PDF bytes only in memory and streams them to pdftotext. Only text is saved under `sources/`. `data/` contains CSV samples, summaries and JSON diagnostics. No PDFs, scans, page images, publication or pushes were made.

## Audit and remaining gap

The proof audit rederived the terminal error's exponent by scaling the covariance measure, giving e^(−dt) from the rescaled terminal covariance and e^(kappa t) from the weight's second moment. As an independent check, a Poisson terminal measure has reduced covariance c delta_0; its conditional weighted variance is exactly c e^(−dt) int f(x)^2 E W_t(x)^2 dx, with the same exponent. The Lévy intensity constant was checked by integration by parts and independently by numerical quadrature. Gaussian m(alpha) and m'(alpha) were checked using Gauss–Hermite quadrature and direct first-generation samples; all assertions in `data/math_checks.json` passed. The stable sampler's bounded Laplace observables agreed within three standard errors with exp(−q^alpha); an independent alpha=1/2 normal-variable representation was also checked.

Theorem A deliberately assumes the conditional decomposition that a general classification still needs to discover. Theorem B proves its conclusion from the marginal equation, but requires an integrable reduced covariance and kappa<d. Neither proves the general no-moment critical or atomic classification. No counterexample in the intended ergodic/decaying-dependence class was found. The status is therefore **PARTIAL**, with two complete restricted proofs and reproducible finite-depth evidence.

Task: “Open problem D0064”; task clock recorded at start: 2026-11-13 08:26 +04.
