MINOR

The obstruction theorem survives independent scrutiny. Its process is well defined, stationary, reversible and Markov, with the Dumitriu–Edelman beta-two entry law and hence the GUE **eigenvalue** law at every time. The proof establishes the claimed uniform-in-time mean-square freezing of any fixed number of edge eigenvalues on the correct order of DBM edge time. Corollary B is proved, with substantive hypotheses; it is not merely asserted. The Lanczos orbit-quotient claim is correct on the cyclic locus. There is one mathematical normalization error: the stated standard Airy time is twice what it should be. The remaining revisions below concern precision and a short measurability justification. None invalidates freezing.

This is a valid partial obstruction, with modest explanatory value. It neither constructs the requested dynamical operator limit nor disproves its existence. The process itself is prior work. I did not establish novelty of the precise freezing bound. The literature search, including 2026 sources, found no checked positive solution or general negative solution of the microscopic operator-process question.

The errors and gaps requiring correction are:

1. **Airy time has an extra factor two.** Location: [submitted REPORT.md](claim_files/REPORT.md), line 42, the interpretation around equations (11)–(12), and line 249's “standard Airy lag 2.” For equation (1)'s rate-one OU, stationary diagonal variance one, and edge scaling $n^{1/6}(\lambda-2\sqrt n)$, physical time $t=s n^{-1/3}$ corresponds to standard Airy time **s**, not $2s$. Replace that interpretation throughout and call the numerical lag standard Airy lag 1. The non-atom statements at $2s$ are themselves true, but the comparison process at the simulated lag is $\mathcal A(s)$. The numerical data and equations (3), (5)–(10) need no change. A direct check using Corwin–Hammond's normalization is equation (4), PDF p.11, together with Theorem 3.1, p.12. [Primary source](https://arxiv.org/abs/1108.2291).

2. **“GUE one-time law” is imprecise for the matrix.** Location: submitted report line 15. A real tridiagonal matrix does not have the invariant dense GUE matrix distribution. Say “the independent beta-two Dumitriu–Edelman tridiagonal law, and therefore exactly the GUE one-time eigenvalue law.” Theorem A already states the intended entry law correctly. This is a wording correction, not a defect in stationarity or the spectral claim.

3. **The one-line covariance extension must retain its hypotheses.** Location: line 15, read against Corollary B, lines 214–233. “Uniformly bounded entry covariances” must mean a uniform bound on the covariance **operator**, in the unnormalized coordinates $(a,b)$, as in (13). It also requires the same independent Dumitriu–Edelman invariant entry law, stationarity, reversibility and the stated diffusion/Sobolev calculus. Individual covariance entries being bounded is insufficient to imply (13). Having only GUE eigenvalue marginals is insufficient to apply estimate (7). Fix the short summary to retain these qualifications. The formal corollary contains them and its proof is valid. For perspective, the diagonal matrix of stationary ordered DBM particles is itself a reversible, continuous tridiagonal diffusion with bounded noise covariance and GUE eigenvalue marginals, yet has moving edges. Its entry law is not Dumitriu–Edelman's, so it is outside Corollary B.

4. **Supply the Borel kernel and separate deterministic-time cyclicity from a pathwise assertion.** Location: line 28's Lanczos paragraph. Cyclicity at every deterministic time almost surely does not by itself prove cyclicity simultaneously at all times. The stated deterministic-time Markov conclusion does hold, without this stronger assertion. Add the explicit kernel and continuity/measurability argument given below; if claiming a globally continuous positive-off-diagonal realization at every time, additionally justify avoidance of the noncyclic set or specify a full orbit-space version. This is a short exposition gap, not a counterexample to the stated orbit argument.

I independently downloaded [Virág's paper](https://arxiv.org/abs/1804.06953) and retained its complete text as [sources/virag_1804.06953.txt](sources/virag_1804.06953.txt). On PDF p.25, Question 8 is exactly:

> Question 8 (Dynamics). Are there operator limits of matrix-valued (say Hermitian) Brownian motion?

The surrounding operator-limit framework includes embedded eigenfunctions and resolvents; the static edge example is Theorem 5.1 on p.6. The submitted report correctly restricts its conclusion to a class of tridiagonal dynamical candidates. In particular, its obstruction does not cover unbounded covariance operators, arbitrary time accelerations, nonreversible processes, other coordinate representations, or all possible continuum operators. Assigning a diagonal operator to limiting particles afterward is not the operator convergence sought in this framework.

Here is the line-by-line mathematical audit, using the submitted equation numbers.

**Construction, equation (2), proof step 1.** Start each Gaussian OU coordinate in its invariant $N(0,1)$ law, with SDE $dZ=-Z\,dt+\sqrt2\,dW$. Independence across all coordinates is essential and is stated. Rotation invariance makes each radius a Markov function of its vector process. Projection of the reversible stationary product process then gives a reversible stationary product of radii and diagonal OU coordinates. Its law is

\[
a_i\sim N(0,1),\qquad b_i\sim\chi_{2(n-i)}/\sqrt2,
\]

with independent entries. This is the beta-two tridiagonal law, not a dynamic identity with full matrix OU. The static identification is the Dumitriu–Edelman theorem. [Matrix Models for Beta Ensembles, Theorems 2.1 and 2.12](https://arxiv.org/abs/math-ph/0206043).

Ito's formula for $b=|Z|/\sqrt2$, in dimension $d=2(n-i)$, gives

\[
db=dW+\left(\frac{d-1}{2b}-b\right)dt,
\]

exactly equation (4). The smallest dimension is two, whose origin is polar; the OU-to-Brownian deterministic time change preserves this property. Thus positive off-diagonals, simple Jacobi eigenvalues and continuous ordered eigenvalue paths follow. There is no hidden eigenvalue crossing or singular-boundary failure here.

**DBM equation and clock, equations (1)–(3).** In the submitted units, dense Hermitian OU has diagonal noise $\sqrt2\,dB$, off-diagonal real and imaginary noises of variance (dt), and drift $-G\,dt$. Eigenvalue perturbation gives

\[
d\lambda_j=\sqrt2\,dB_j+
\left(2\sum_{\ell\ne j}\frac1{\lambda_j-\lambda_\ell}-\lambda_j\right)dt.
\]

So equation (1), including its repulsion coefficient, is correct. Its stationary edge is $2\sqrt n$, with fluctuations $n^{-1/6}$. For $X_j=n^{1/6}(\lambda_j-2\sqrt n)$, the martingale quadratic variation is $2n^{1/3}dt$. Hence $dt=n^{-1/3}ds$ gives $d\langle X_j\rangle=2ds$. Equivalently, for $G/\sqrt n$ the gap is $n^{-2/3}$, the eigenvalue noise variance is (2dt/n), and the same balancing gives $t\asymp n^{-1/3}$. These are two consistent scale checks.

To check the constant without inferring quadratic variation through a weak limit, the scalar OU generator has Hermite eigenvalues (-m). Its conjugated positive operator is

\[
H_{\rm osc}=-\partial_x^2+x^2/4-1/2.
\]

Under $x=2\sqrt n+n^{-1/6}z$, the centered operator satisfies

\[
n^{-1/3}(H_{\rm osc}-n)
=-\partial_z^2+z-\tfrac12n^{-1/3}+\tfrac14n^{-2/3}z^2.
\]

The edge temporal exponent is therefore $s(-\partial_z^2+z)$ when OU time is $s n^{-1/3}$. This is the standard extended Airy-kernel time, with no extra two. It agrees with the Corwin–Hammond normalization cited in correction 1.

The connection to literal Brownian motion is also correct: if $B(u)$ is standard Hermitian Brownian motion and (B(1)) is GUE, then

\[
G(t)=e^{-t}B(e^{2t})
\]

is exactly stationary rate-one matrix OU. Thus the Brownian experiment at $u=e^{2s n^{-1/3}}$, divided by $\sqrt u$, uses the intended DBM clock and tracks its moving macroscopic edge.

**Reversible maximal inequality, equation (5), proof step 2.** For smooth $f$, write the forward and reversed martingales on a fixed horizon $U$. Reversibility gives

\[
f(Y_t)-f(Y_0)=\tfrac12 M_t-
\tfrac12(\widehat M_U-\widehat M_{U-t}).
\]

The drift integrals cancel exactly. Bounding the squared supremum by

\[
\tfrac12\sup|M|^2+2\sup|\widehat M|^2
\]

and using Doob with $E M_U^2=2U E\Gamma(f)$ yields $20U E\Gamma(f)$. The constant 20 is valid. Cutoff and convolution in Gaussian $W^{1,2}$, followed by this same inequality for differences and local uniform convergence along continuous sample paths, justify the Lipschitz extension. There is no missing uniform drift or inverse-gap estimate.

**Eigenvalue energy, equation (6), proof step 3.** For a normalized real eigenvector $v$, the entry derivatives are $v_i^2$ and $2v_iv_{i+1}$. Since $\|\nabla_Z b_i\|^2=1/2$, the Gaussian-coordinate energy is

\[
\Gamma(\lambda_j)=\sum_i v_i^4+2\sum_i v_i^2v_{i+1}^2
\le3\sum_i v_i^4.
\]

The factor two on the adjacent products is correct. Moreover, $2|b(Z)-b(Z')|^2\le\|Z-Z'\|^2$; adding diagonal terms proves contraction into Frobenius norm. Ordered eigenvalues are consequently globally Lipschitz even across the exceptional derivative set. For dense Hermitian OU the corresponding energy is exactly one. This difference is the obstruction's mechanism.

**Concentration and delocalization, equations (7)–(9), proof step 4.** The chi Chernoff bound follows from its squared moment generating function. The elementary inequality $y-1-\log y\ge(\sqrt y-1)^2$ is equivalent to $q-1-\log q\ge0$, with $q=\sqrt y$. The Gaussian and chi union bounds with $r=\sqrt{12\log n}$ give the claimed failure probability at most $4n^{-5}$.

For $m=\lfloor n^{1/4}\rfloor$, the first $m$-corner differs from the constant-off-diagonal Toeplitz matrix by at most $3r+2m/\sqrt n$ in operator norm. Interlacing and the explicit cosine eigenvalues give

\[
\lambda_j\ge2\sqrt n-3r-\pi^2j^2-2.
\]

Here $m+1>n^{1/4}$ gives the stated constant in the cosine error. No edge-rigidity theorem is being smuggled into this estimate.

For $w_i=|v_i|$, with zero endpoints, put $M=\sqrt n+r$ and $D=\sum_{i=0}^{n}(w_{i+1}-w_i)^2$. Positivity of the off-diagonal entries gives

\[
\lambda_j\le r+2M\sum_i w_iw_{i+1}=r+2M-MD,
\qquad
D\le\frac{6r+\pi^2j^2+2}{M}.
\]

The absolute values make this valid also for sign-changing eigenvectors. Telescoping $w_i^2$, followed by Cauchy–Schwarz and $\sum(w_{i+1}+w_i)^2\le4$, gives $\max_i w_i^2\le2\sqrt D$. Hence

\[
E\sum_i v_i^4\le
2\sqrt{\frac{6r+\pi^2j^2+2}{\sqrt n+r}}+4n^{-5}
=O_j\big(n^{-1/4}(\log n)^{1/4}\big).
\]

Every constant and direction of inequality in (7) checks out. This is weak but sufficient delocalization.

**Uniform freezing, equations (3) and (10), proof step 5.** Apply (5) with $f=n^{1/6}\lambda_j$ and $U=S n^{-1/3}$. The amplitude-square factor $n^{1/3}$ cancels the shrinking time, leaving

\[
E\sup_{s\le S}|X_j(s)-X_j(0)|^2
\le60S E\sum_i v_i^4.
\]

Summing over $j\le k$ proves (3), including its maximum over the fixed set of eigenvalues. Static GUE edge convergence and the continuous constant-path map then give convergence in $C([0,S],\mathbb R^k)$. This proves convergence to a random constant path, not merely agreement of one-time laws. It does not claim mean-square convergence to a particular Airy random vector on a preassigned common probability space.

**Incompatibility with the Airy line ensemble, proof step 6.** The Brownian Gibbs property implies that the top curve's value at a positive time, conditional on an interval's exterior and the lower curve, has no atoms. The bridge conditioning event has positive probability by full support and endpoint separation. Its value at time zero can be fixed by taking the interval away from zero. Thus the two-time equality probability is zero for Airy and one for the frozen process. The argument is valid, with the time correction above; the Gibbs bridge has the corresponding diffusion-two normalization before the usual vertical rescaling. This establishes incompatibility without an unjustified exchange of moments and weak limits. [Corwin–Hammond, Theorem 3.1](https://arxiv.org/abs/1108.2291).

**Corollary B and the covariance lower bound.** The same forward/backward martingale argument applies to a stationary reversible diffusion with $\Gamma(f)=\nabla f^{\mathsf T}C_n\nabla f$. Under (13),

\[
\Gamma(\lambda_j)\le K\left(\sum_i v_i^4+4\sum_i v_i^2v_{i+1}^2\right)
\le5K\sum_i v_i^4.
\]

The invariant-law estimate just proved applies unchanged. The right side of the maximal bound becomes $100KS E\sum_i v_i^4$. This proves the corollary and the stated $K_n n^{-1/4}(\log n)^{1/4}\to0$ variant. Its approximation hypothesis is explicit; the report is not proving the result for arbitrary rough generalized Markov processes.

For an exact semimartingale Jacobi realization of DBM, comparison of quadratic variation instead gives

\[
1=\nabla\lambda_j^{\mathsf T}C_n\nabla\lambda_j
\le5\|C_n\|_{\rm op}\sum_i v_i^4.
\]

Consequently the displayed covariance lower bound and divergence in probability under the Dumitriu–Edelman entry law are correct. This pointwise argument does not use reversibility. It is a necessary restriction on such a realization, not a general nonexistence theorem.

The Lanczos Markov statement can be completed precisely as follows. Let $\mathcal C$ be the open set of Hermitian matrices for which $e_1$ is cyclic, and $J(H)$ their unique Jacobi representative with positive off-diagonals. The Lanczos recursion consists of matrix multiplication, inner products and division by strictly positive residual norms. Therefore $J$ and its unitary basis $Q(H)$ are continuous on $\mathcal C$, in particular Borel measurable; $Q(H)e_1=e_1$.

For $K=\{U\in U(n):Ue_1=e_1\}$, equivariance gives $J(UHU^*)=J(H)$. Conversely, equality of representatives gives the conjugating unitary $U=Q(H')Q(H)^*\in K$. Thus the fibers are exactly the $K$-orbits. The section $j\mapsto j$, viewing a Jacobi matrix as Hermitian, is continuous.

Let $P_t$ be the Hermitian Brownian or OU kernel. Its conjugation equivariance implies that $P_t(g\circ J)$ is constant on those fibers. Explicitly, define

\[
\overline P_t g(j)=\int g(J(H'))\,P_t(j,dH').
\]

For (t>0), $P_t(H,\cdot)$ has a density and the noncyclic algebraic set has Lebesgue measure zero. Any Borel extension of $J$ off $\mathcal C$ therefore leaves this kernel unchanged. The section makes the kernel measurable; the Chapman–Kolmogorov identity follows from the original kernel and cyclicity at the intermediate deterministic time. Finally,

\[
E[g(J(H_{s+t}))\mid\mathcal F^H_s]
=\overline P_tg(J(H_s)),
\]

and conditioning on the smaller Jacobi filtration proves the claimed Markov property. Brownian motion started at the zero matrix is treated from any positive time, or with its initial degenerate state specified separately. No conclusion about arbitrary noncyclic matrices collapsed by an unfinished Lanczos recursion is needed. Nor does this argument produce independent entry noises or bounded covariance operators. The sample orbit identities were also checked numerically, but the proof is the fiber/kernel argument above.

The numerical evidence was generated independently in [code/independent_simulation.py](code/independent_simulation.py); no submitted code was read, imported or reused. At each step the tridiagonal radial transition uses

\[
R_{t+h}^2=(\rho R_t+\sigma Z)^2+\sigma^2 V,
\quad \rho=e^{-h},\quad \sigma^2=1-e^{-2h},
\quad Z\sim N(0,1),\quad V\sim\chi^2_{d-1},
\]

with $b=R/\sqrt2$. This is the exact vector-OU radial transition. Dense matrices use the exact Gaussian matrix OU transition, equivalently the normalized Brownian evolution above. Neither simulation discretizes a singular drift SDE. The edge time step is always converted by $h=\Delta s\,n^{-1/3}$.

For the largest eigenvalue at $s=1$, the independent results are:

| $n$ | Tri. paths | Tri. MSE ± standard error | Matrix paths | Matrix MSE ± standard error |
|---:|---:|---:|---:|---:|
| 64 | 800 | 0.5862 ± 0.0312 | 400 | 0.9967 ± 0.0716 |
| 256 | 800 | 0.3795 ± 0.0185 | 240 | 0.9658 ± 0.0820 |
| 512 | 800 | 0.3426 ± 0.0189 | 100 | 1.0849 ± 0.1615 |
| 1024 | 800 | 0.2615 ± 0.0126 | 48 | 0.9192 ± 0.1633 |
| 2048 | 800 | 0.2111 ± 0.0113 | 16 | 0.6748 ± 0.1745 |
| 4096 | 800 | 0.1862 ± 0.0101 | — | — |

These are scaled increments squared, not raw eigenvalue increments. The second eigenvalue's tridiagonal MSE decreases from 0.4497 to 0.1291. The top eigenvalue's mean noise energy decreases from 0.3575 to 0.09295, whereas dense matrix energy is exactly one. The finite-size tridiagonal increments remain appreciable; the numerical result is a decreasing trend consistent with freezing, not a claim that $n=4096$ has reached zero motion. The dense $n=2048$ row is a small pilot with substantial uncertainty; it cannot establish a dense asymptotic trend by itself.

[Raw paired samples](data/independent_samples.csv), [all top-two summaries](data/independent_summary.csv), [comparison plot](data/independent_edge_increments.svg), and [run metadata](data/independent_metadata.json) are retained. Sixteen exact steps on $[0,1]$ also give decreasing sampled path maxima for the tridiagonal model. A grid maximum is not a continuum supremum; the latter is proved analytically.

Independent checks in [code/check_math.py](code/check_math.py) give a maximum coordinate-gradient error $9.44\times10^{-11}$. At $n=20$ and $\Delta s=10^{-4}$, matrix MSE/$\Delta s$ is $1.9363\pm0.0352$, against prediction 2; the tridiagonal value is $1.0290\pm0.0192$, against $2E\Gamma=1.0479$. Lanczos conjugacy and reconstruction errors are below $3\times10^{-15}$. These check implementation and the clock, not the limiting theorem.

[code/audit_data.py](code/audit_data.py) independently reconstructed all 72 submitted summary rows using scalar `math.fsum`: maximum discrepancy $2.23\times10^{-16}$ for MSE and $4.45\times10^{-16}$ for correlations. All 44 independent summary rows also agree to floating-point precision. This validates the submitted tables' arithmetic, not their random-number provenance or bootstrap coverage. The raw submitted artifacts were left unchanged and their hashes recorded in [data/data_audit.json](data/data_audit.json).

The main independent run took 439.5 seconds, at verified nice 10, with peak RSS 724.2 MiB. Numerical thread limits were set to one. Because `threadpoolctl` recognizes no pools on this build, a separate same-kernel macOS `libproc` audit polled native thread counts at 5 ms intervals: maximum observed was two, including its monitoring thread, and RSS stayed below 375 MiB. This is a separate resource check, not retrospective continuous monitoring of the full run. [Resource audit](data/resource_audit.json). No subagents, publication or pushes were used.

The literature findings are based on primary texts, downloaded independently as plain text. PDF pages below are one-based pages of the retained versions; form feeds preserve the boundaries. The [source manifest](data/source_manifest.json) contains URLs and hashes, and [sources/search_log.txt](sources/search_log.txt) records the search scope.

| Primary source | Location checked | Relevance to this claim and Question 8 |
|---|---|---|
| [Dumitriu–Edelman, Matrix Models for Beta Ensembles (2002)](https://arxiv.org/abs/math-ph/0206043) | Theorems 2.1, 2.12, PDF pp.6–7, 12 | Establishes the static tridiagonal laws and spectral identification. Does not identify the independent-entry dynamics with DBM. |
| [Li, The beta-Hermite and beta-Laguerre processes (2010)](https://arxiv.org/abs/1007.3905) | Definition 3.1.1, Proposition 3.1.2, Theorem 3.1.3, pp.8–11 | Already constructs independent OU/generalized-Bessel Jacobi processes. The submitted stationary beta-two process is this construction after changing normalization and initialization. Li also distinguishes its eigenvalue dynamics from Dyson's. |
| [Allez–Guionnet, A diffusive matrix model for invariant beta-ensembles (2012/2013)](https://arxiv.org/abs/1206.1460) | Theorems 2.2 and 2.4, pp.4–6 | Produces invariant matrix dynamics with DBM eigenvalues via a switching limit at fixed dimension. This does not prove a microscopic continuum-operator process limit. |
| [Holcomb–Paquette, Tridiagonal Models for Dyson Brownian Motion (2017)](https://arxiv.org/abs/1707.02700) | Theorem 2, p.5; Theorems 17–18, pp.22–23 | Gives tridiagonal DBM realizations involving spectral weights and describes finite-corner limits in a particular model. It does not prove edge-scaled convergence of a growing corner to a dynamical SAO. |
| [Corwin–Hammond (2011/2014)](https://arxiv.org/abs/1108.2291) | Equation (4), p.11; Theorem 3.1, p.12 | Establishes continuous Airy curves and their Brownian Gibbs property. Supplies the correct moving comparison process and a normalization check. |
| [Landon–Sosoe–Yau, Fixed energy universality for DBM (2019; retained v4, 2026)](https://arxiv.org/abs/1609.09011) | Theorems 2.2–2.4, pp.9–11 | Proves fixed-energy and multitime spectral universality. No convergent differential-operator process is supplied by these statements. |
| [Landon, Edge scaling limit of DBM at equilibrium (2020)](https://arxiv.org/abs/2009.11176) | Theorems 1.1–1.4, pp.1–2 | Constructs the edge particle-process limit for beta at least one and proves locally Brownian increments. This is spectral dynamics, not a dynamical SAO convergence theorem. |
| [Yabuoku (2022/2023)](https://arxiv.org/abs/2204.00736) | Theorem 2.1, pp.4–5 | Derives eigenvalue SDEs for independent Brownian/Bessel tridiagonals, involving minor spectra. Confirms that correct one-time laws do not give DBM dynamics. |
| [Edelman–Jeong–Nissim, v3, 19 February 2026](https://arxiv.org/abs/2411.01633v3) | Theorem 3.1, p.9; Problem 4, p.18; Remark 5.6, pp.19–20 | Proves fixed-corner GOE entry-process convergence, with position-dependent OU rates. Problem 4 still asks for a dynamical operator; Remark 5.6 gives perturbative evidence against the extrapolated OU-noise candidate. This is not a positive solution or a general negative theorem. |
| [Gorin–Xu–Zhang, Airy-beta line ensemble (2024)](https://arxiv.org/abs/2411.10829) | Theorems 1.4 and 1.6, pp.5–7 | Constructs the line ensemble for every positive beta and proves DBM trajectory convergence. It identifies joint spectra, without proving convergence of a differential-operator process. |
| [Huang–Zhang, v2, May 2026; Advances in Mathematics 498](https://arxiv.org/abs/2411.10586) | Theorems 1.15–1.16, pp.9–10 | Characterizes Airy-beta through meromorphic pole evolution and proves process universality. This published spectral-transform result does not establish the requested operator/eigenfunction limit. |
| [Assiotis–Li, Infinite-dimensional Dyson Brownian motion(s), September 2026](https://arxiv.org/abs/2609.26386) | Introductory Theorems A and B | Gives infinite-particle limits, Markov properties and a Stieltjes-transform SPDE. The objects are particle processes and spectral transforms. |
| [Kwak, October 2026](https://arxiv.org/abs/2610.35808) | Theorem 2.1.2, p.13; Theorems 2.2.1–2.2.2, p.26; Theorem 2.4.1, p.39 | Main statements concern static Wigner operator universality and static sharp couplings. Resolvent paths here vary in spectral parameter, not physical Brownian time. Its 1312 pages were not exhaustively audited. |

The submitted correction of the final asymptotic in EJN Remark 5.6 also checks out: from $\psi(0)=0$, $\psi'(0)=1$, the two integrals behave as $24t^{-5}$ and $t^{-2}$. The printed $t^{-1}$ in the latter is inconsistent with its displayed integrand. This ancillary correction does not turn a large-beta perturbation calculation into a fixed-beta obstruction theorem.

As of this audit, I found **no verified theorem in print answering Question 8 positively or negatively in its intended microscopic operator sense**. The most direct recent source still treats the operator question as open. This is a documented search conclusion, not a proof of absence. Static SAO limits, semigroups of a fixed random operator, line-ensemble limits, and spectral-transform evolution must not be substituted for a physical-time operator-process limit.

The exact result that can be credited here is the explicit uniform freezing bound for this stationary tridiagonal process, its correctly qualified reversible bounded-covariance extension, and the covariance-growth necessary condition for an exact DBM Jacobi realization. The construction, static law, reversible martingale method and orbit-quotient principle are established ingredients. I found no prior source stating this precise uniform estimate, but that does not establish research novelty; the report appropriately makes no novelty claim. It is a sound elementary obstruction lemma after the minor revisions above, not a resolution of D0046.

Task: “You are an independent referee ... Break it if it is wrong.” D0046. Received 2026-11-13 11:17 +04 (Asia/Tbilisi).
