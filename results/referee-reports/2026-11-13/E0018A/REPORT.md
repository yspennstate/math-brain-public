PROVED

# E0018: an explicit pair with at least two instability intervals

For the **unrestricted wording** of Open question 3, the answer is yes. Take actual symmetric transition rates r in each direction and

\[
\boxed{A_0=\begin{pmatrix}-3/4&-1\\1&-3/4\end{pmatrix},\qquad
A_1=\begin{pmatrix}5/4&0\\0&-11/4\end{pmatrix}.}
\]

The top Lyapunov exponent is continuous on (0,∞) and satisfies the following certified bounds:

| Actual jump rate r | Rigorous bound | Sign |
|---:|---:|---|
| 1/10 | λ(r) > 9/50 = 0.18 | positive |
| 5 | −0.071355633951 ≤ λ(r) ≤ −0.009745897257 | negative |
| 20 | 0.070309824390 ≤ λ(r) ≤ 0.084999667350 | positive |

All finite decimals in the last two rows are exact rationals, not rounded numerical estimates. Consequently U={r>0:λ(r)>0} has at least two connected components. Each component is a nonempty open interval. More explicitly,

\[
(0,1/10]\subset U,\quad
[4.997,5.003]\cap U=\varnothing,\quad
[19.95,20.05]\subset U.
\]

The proof does not assert that U has exactly two components or certify the numerical crossing locations.

**Scope of the result.** A0 is Hurwitz, while A1 has eigenvalue 5/4 and is not Hurwitz. Their average also has a positive eigenvalue. Open question 3 does not explicitly impose the Hurwitz conditions from the preceding example; the question here also requests searching general pairs, including Hurwitz pairs. This report proves that unrestricted statement. If “as posed” is interpreted as retaining an implicit requirement that both matrices be Hurwitz, this result is only **PARTIAL for that strengthened interpretation**: no example or impossibility proof for both Hurwitz matrices was obtained. This distinction is essential.

## Exact setting and source

The supplied arXiv identifier and title identify **Florent Malrieu**, “Some simple but challenging Markov processes”, Ann. Fac. Sci. Toulouse Math. (6) 24(4) (2015), 857–883, DOI [10.5802/afst.1468](https://doi.org/10.5802/afst.1468), [arXiv:1412.7516](https://arxiv.org/abs/1412.7516). The four-author citation in the question instead belongs to a different paper, “On the stability of planar randomly switched systems”. Both PDFs are saved in `sources/`.

Section 4.1, equation (8), explicitly uses

\[
Lf(x,i)=(A_i x)\cdot\nabla f(x,i)+r[f(x,1-i)-f(x,i)].
\]

Thus the two actual transition rates are both r, and the stationary environmental probabilities are 1/2. There is no redraw/self-jump factor of two in this convention. Open question 3 is on arXiv PDF page 10 and journal page 871. The question asks for general two-by-two matrices, following examples with both matrices and every convex combination Hurwitz. We will distinguish the unrestricted question from this stronger restriction.

## Proof of the sign pattern

### Existence of the exponent and continuity in r

Write a=3/4, B0=A0+aI=J0, where J0 is rotation with unit angular speed, and B1=A1+aI=diag(2,−2). Consider the projective angle immediately after each holding period in state 0, hence at entry to state 1. The duration T0 of the next rotation period is independent Exp(r). Modulo π, it has density

\[
k_r(s)=\frac{re^{-rs}}{1-e^{-\pi r}},\qquad 0\le s<\pi.
\]

Every transition kernel of this embedded angle chain is bounded below by

\[
m_r\,d\theta,\qquad m_r=\frac{r}{e^{\pi r}-1}>0.
\]

Indeed, the state-1 flow changes the incoming angle, and the following independent rotation adds T0 modulo π. This proves a Doeblin minorization, giving a unique stationary chain and ergodic averages from every initial direction. The logarithmic norm increment in a cycle is bounded in absolute value by a constant times T0+T1. Exponential holding times have finite second moments. The additive ergodic theorem, or its elementary martingale-difference extension, therefore gives a deterministic continuous-time exponent λ(r) for every fixed nonzero initial vector, almost surely. Maximal incomplete holding times divided by elapsed time tend to zero, so evaluating only at cycle endpoints gives the same exponent. Applying this to two basis vectors also identifies it with the top matrix-cocycle exponent.

For completeness, continuity does not have to be assumed. On any compact rate neighborhood inside (0,∞), the above minorization has a uniform positive constant. The embedded transition kernel depends continuously on r in total variation, uniformly in the incoming angle: its randomness has joint density r² exp[−r(t0+t1)], while the deterministic angle maps are independent of r. The stationary angle law is consequently continuous in total variation, by the uniformly contracting Doeblin bound. The conditional mean cycle reward is bounded, continuous in the incoming angle, and continuous in r in the uniform norm; dominated convergence uses |reward|≤C(t0+t1). Dividing its stationary average by the mean cycle length 2/r proves continuity of λ.

### A rigorous lower bound for r=1/10

Let Θ be the angle at entry to state 1. Its conditional density, given everything before the preceding rotation, is at most

\[
M_r=\frac{r}{1-e^{-\pi r}}.
\]

Since log|cos θ|≤0 and ∫₀^π log|cos θ|dθ=−π log 2,

\[
\mathbb E[\log|\cos\Theta|\mid\text{past}]\ge-M_r\pi\log2.
\]

The norm multiplier during a state-0 period is exactly exp(−aT0). During a state-1 period,

\[
\log\|e^{A_1T_1}u_\Theta\|
\ge(2-a)T_1+\log|\cos\Theta|.
\]

The same conditional density bound ensures square integrability of the last term. Taking stationary cycle averages, using E T0=E T1=1/r, and dividing by 2/r yields

\[
\boxed{\lambda(r)\ge\frac14-
\frac{r^2\pi\log2}{2(1-e^{-\pi r})}.}\tag{1}
\]

For x>0, 1−e^(−x)≥x/(1+x). Together with π<4 and log 2<1, this gives, for 0<r≤1/10,

\[
\lambda(r)\ge\frac14-\frac r2(1+\pi r)\log2
>\frac14-\frac1{20}\left(1+\frac4{10}\right)=\frac9{50}>0.
\]

A separate 50-digit outward interval evaluation of (1) at r=1/10 encloses its lower-bound expression in [0.20961409817528034926562418898289607826261787389036, 0.20961409817528034926562418898289607826261787389037]. Only the simpler exact 9/50 bound is needed.

### Global generator certificates at r=5 and r=20

For this pair, with x=2θ,

\[
v_0=1,\quad v_1=-2\sin x,\qquad h_0=-3/4,\quad h_1=-3/4+2\cos x.
\]

The angle generator acts on a pair f=(f0,f1) by

\[
(\mathcal L_r f)_0=f_0'+r(f_1-f_0),\qquad
(\mathcal L_r f)_1=-2\sin(2\theta)f_1'+r(f_0-f_1).
\]

For any bounded smooth pair f, if ℓ≤h_i+(L_r f)_i≤u pointwise for both states, then ℓ≤λ(r)≤u. To prove this, apply the PDMP martingale formula to f. The bounded jump increments give quadratic variation at most Ct, hence the martingale divided by t tends to zero almost surely. The bounded f endpoint term also vanishes after division by t. Adding L_r f to the radial reward therefore does not change its long-time average. Equivalently, its stationary integral is zero.

The file `data/poisson_certificates.json` gives **all exact rational coefficients** of two such test-function pairs. Its ordering is

\[
f_i(\theta)=c_{i,0}+\sum_{k=1}^K\left[c_{i,k}\cos(2k\theta)+s_{i,k}\sin(2k\theta)\right],
\]

with arrays `[c0,c1,...,cK,s1,...,sK]`. For r=5, K=128; for r=20, K=32. All coefficients have denominator dividing 10¹². The coefficients were found approximately, then replaced by these exact rationals before verification.

For either state, exact algebra gives a finite residual

\[
h_i+(\mathcal L_r f)_i=C_i+\sum_{k=1}^{K+1}
[\alpha_{i,k}\cos(2k\theta)+\beta_{i,k}\sin(2k\theta)].
\]

Thus its global range is contained in

\[
\left[C_i-\sum_k(|\alpha_{i,k}|+|\beta_{i,k}|),\;
C_i+\sum_k(|\alpha_{i,k}|+|\beta_{i,k}|)\right].\tag{2}
\]

The exact calculations give:

| r | state | Lower endpoint in (2) | Upper endpoint in (2) |
|---:|---:|---:|---:|
| 5 | 0 | −0.040550774017 | −0.040550757183 |
| 5 | 1 | −0.071355633951 | −0.009745897257 |
| 20 | 0 | 0.077654745278 | 0.077654746482 |
| 20 | 1 | 0.070309824390 | 0.084999667350 |

This proves the claimed signs over the entire circle, without meshing θ, approximating the stationary density, or trusting a linear solver's error estimate.

There are two independent checks of (2). `code/verify_certificate.py` uses only standard-library Fraction arithmetic and rebuilds the generator action in a real sine/cosine basis; certificate construction used complex Laurent polynomials. `code/interval_audit.py` repeats the real-basis computation with mpmath.iv at 50 decimal digits, converting every rational by outward interval division. Its full endpoint intervals are saved in `data/interval_audit.json`. Both checks pass.

For explicit neighborhoods, retain the same f and note

\[
\mathcal L_r f-\mathcal L_{r_0}f=(r-r_0)(f_{1-i}-f_i).
\]

The sum of absolute real Fourier coefficients bounds ||f1−f0||∞ by D. The exact D values and arithmetic are in `data/certified_neighborhoods.json`; D<1.392 at r0=5 and D<0.683 at r0=20. Consequently (2) stays negative on [4.997,5.003] and positive on [19.95,20.05]. `code/certified_neighborhoods.py` checks this with exact fractions.

### Why this gives the requested intervals

Continuity makes U open, so every connected component is an open interval relative to (0,∞). The positive points 1/10 and 20 lie in different components because 5 lies between them and λ(5)<0. The explicit neighborhoods above also give a nonempty stable interval separating two nonempty unstable intervals.

The limiting exponents provide independent consistency checks. From the cycle norm upper bound, λ(r)≤1/4, while (1) tends to 1/4, so

\[
\lim_{r\downarrow0}\lambda(r)=\frac14
=\tfrac12\left[-\frac34+\frac54\right].
\]

Also

\[
\bar A=\frac{A_0+A_1}{2}=
\begin{pmatrix}1/4&-1/2\\1/2&-7/4\end{pmatrix},\qquad
\lim_{r\to\infty}\lambda(r)=-\frac34+\frac{\sqrt3}{2}>0.
\]

For the second limit, a precise applicable citation is Chitour–Mazanti–Monmarché–Sigalotti, Proposition 6.4. Its condition (C) holds: the lower eigenspace of the real hyperbolic average is a line, and A0 leaves no real line invariant. Their redraw matrix has both rows (1/2,1/2); take their total redraw intensity μ=2r to obtain our actual transition rate r. Neither limiting statement is needed to replace the finite-rate sign certificates.

## Angle law and exponent: derivation

For \(A_i=\begin{pmatrix}a_i&b_i\\c_i&d_i\end{pmatrix}\), put \(u=(\cos\theta,\sin\theta)\), \(u^\perp=(-\sin\theta,\cos\theta)\), with \(\theta\in\mathbb R/\pi\mathbb Z\). Define

\[
h_i(\theta)=u^TA_i u=a_i\cos^2\theta+(b_i+c_i)\sin\theta\cos\theta+d_i\sin^2\theta,
\]
\[
v_i(\theta)=(u^\perp)^TA_i u=c_i\cos^2\theta-b_i\sin^2\theta+(d_i-a_i)\sin\theta\cos\theta.
\]

Polar differentiation gives \(d\log\|X\|/dt=h_I(\theta)\), \(\dot\theta=v_I(\theta)\). Therefore, for an ergodic stationary angle/environment law \(\mu_r\), its exponent is

\[
\lambda_{\mu_r}(r)=\sum_{i=0}^1\int h_i(\theta)\,\mu_r(d\theta,i).
\]

This follows directly by integrating the radial equation and applying the ergodic theorem. If there are several invariant angle laws, their exponents must be distinguished; the top exponent is the maximal stationary exponent, not an arbitrary choice of law. For an irreducible angle process with unique stationary law it is the top exponent. Malrieu, Section 4.1.1 and Theorem 4.1, gives this construction and an explicit special-case density.

If \(\mu_r(d\theta,i)=p_i(\theta)d\theta\), integration by parts against the generator gives the stationary equations

\[
(v_0p_0)'=r(p_1-p_0),\qquad (v_1p_1)'=r(p_0-p_1),\qquad \int_0^\pi(p_0+p_1)=1.
\]

In particular \(J=v_0p_0+v_1p_1\) is constant. On any interval where both velocities are nonzero, let

\[
H(\theta)=\int_{\theta_*}^{\theta}\left(\frac1{v_0(s)}+\frac1{v_1(s)}\right)ds.
\]

Writing \(q=v_0p_0\), the complete local solution is

\[
q(\theta)=e^{-rH(\theta)}\left[C+rJ\int_{\theta_*}^{\theta}\frac{e^{rH(s)}}{v_1(s)}ds\right],\quad
p_0=q/v_0,\quad p_1=(J-q)/v_1.
\]

Choose C and J by periodicity, normalization, positivity, integrability at velocity zeros, and flux matching. In a trapping interval the flux is zero, so \(p_0=Ce^{-rH}/v_0\), \(p_1=-Ce^{-rH}/v_1\). One must not impose J=0 on a rotating process. Common fixed directions can support atoms; the distributional stationary equations, rather than this density ansatz alone, are needed there. These formulas are a direct solution of the preceding linear ODE system and do not assume smoothness across a velocity zero.

## Explicit invariant density for the exhibited pair

The general formula above can be specialized without an unevaluated matching constant. Set

\[
H(\theta)=\theta-\frac14\log|\tan\theta|.
\]

For 0<θ<π/2 define

\[
F_-(\theta)=e^{-rH(\theta)}\int_\theta^{\pi/2}e^{rH(s)}ds,
\quad p_0=J(1+rF_-),\quad
p_1=\frac{JrF_-}{2\sin(2\theta)}.
\]

For π/2<θ<π define

\[
F_+(\theta)=e^{-rH(\theta)}\int_{\pi/2}^\theta e^{rH(s)}ds,
\quad p_0=J(1-rF_+),\quad
p_1=-\frac{JrF_+}{2\sin(2\theta)}.
\]

Here J>0 is the unique constant making ∫₀^π(p0+p1)=1. These formulas follow from the flux ODE with q=p0 and boundary condition q(π/2)=J; the inadmissible homogeneous solution at that repelling zero is discarded. They have positive densities, integrable singularities at the stable direction when needed, and the required matching flux. For the second branch H′>1 implies rF+<1, verifying positivity of p0. The stationarity equations also give ∫p0=∫p1=1/2. There are no atomic stationary directions because state 0 rotates with nonzero velocity everywhere and jumps out of either state have positive rate.

The exponent is

\[
\lambda(r)=-\frac34+2\int_0^\pi\cos(2\theta)p_1(\theta)d\theta.
\]

To resolve endpoint power singularities numerically, `code/candidate_density.py` uses x=log|tan θ| separately on both half-circles, sets J=1 before final normalization, and integrates y=p0/J−1. With w(x)=e^(−|x|)/(1+e^(−2|x|)), the ODEs are

\[
y'=(r/4-rw)y-rw\quad(0<\theta<\pi/2),
\]
\[
y'=-(r/4+rw)y-rw\quad(\pi/2<\theta<\pi).
\]

The first is integrated from the repelling endpoint x=+∞ toward −∞, the second from x=−∞ toward +∞. Quadrature is accumulated as additional ODE coordinates. This is the invariant-density method, not Monte Carlo. Truncation and solver tolerances are numerical controls; rigor comes from the independent global certificates above.

## Numerical search and cross-checks

The initial exploration drew 600 traceless pairs with seed 180018, using general small-integer entries and rotation/hyperbolic normal forms with scale variation. It computed 49 logarithmically spaced rates from 10⁻³ to 10³ with a 256-cell upwind Markov generator on the projective circle. There were 515 finite successful stationary solves; singular/disconnected or failed systems were skipped, not treated as evidence. `data/search_ctmc.json` stores every successful curve and matrix. Screening looked for a horizontal level with two higher regions separated by a lower region, since a common scalar matrix shift moves the whole exponent curve vertically. The candidate was then simplified to the rational matrices stated above.

The Hurwitz subset was checked explicitly. For each saved base pair Bi, let si be its spectral abscissa and set Ai=Bi−(si+γ)I for γ in {0.01,0.05,0.1}. Both matrices then have spectral abscissa −γ. Since the environmental occupation fractions are 1/2,

\[
\lambda_A(r)=\lambda_B(r)-\tfrac12(s_0+s_1)-\gamma.
\]

`data/hurwitz_search.json` records these 1,545 Hurwitz pairs and their sampled-component counts. None had two sampled positive components. This is a limited numerical search, not a structural theorem, and does not exclude narrow components between grid points.

For the exhibited pair, the invariant-density ODE was evaluated on 403 distinct rates in [10⁻³,10²], including the certified points. All values are in `data/candidate_grid.csv`. The three sign points were recomputed with relative tolerances 2×10⁻¹¹ and 2×10⁻¹³, increasing endpoint controls from (edge,tail)=(42,36) to (50,44). The maximum change there was below 9×10⁻¹², and both environmental masses agreed with 1/2 to floating-point precision. These observed agreements are not error certificates. A plot audit detected that an initial broad-span adaptive solve could skip the active angular transition at very small rates. The final method separates the active region from the long tail and forces steps of at most 1 in x through the active region. All 403 grid rates were then independently refined with maximum step 0.5, tolerance 2×10⁻¹³, edge 50 and tail 44. The largest change from the corrected base grid was 2.631×10⁻¹¹. Environmental mass and the analytic exponent bounds were also checked; see `data/grid_audit.json` and `data/candidate_grid_refined.csv`.

The independent discretized Markov chain uses forward/backward nearest-neighbor angular moves at rates |vi(θ)|/Δθ, plus actual environmental flips at rate r. Stationary distributions were solved on 256, 1024, 4096 and 16384 cells. The recorded finest-grid generator residuals are below 1.5×10⁻¹³; mesh bias remains visible and is distinguished from that algebraic residual.

Monte Carlo uses exact matrix flow between exponential holding times, not time steps. Each rate has two independent seeds, each with 100,000 burn-in cycles and 2,000,000 retained cycles (4,000,000 actual switches), divided into 100 blocks. The C source uses a fixed SplitMix64 generator. It rescales the diagonal exponential analytically to prevent overflow. All block data are saved; standard errors are descriptive block estimates, not rigorous confidence statements.

| r | Invariant density, refined | CTMC, 16384 cells | Monte Carlo, pooled | Approximate block SE |
|---:|---:|---:|---:|---:|
| 0.1 | 0.216444855966 | 0.216417929898 | 0.216004811477 | 0.000363 |
| 5 | −0.040611505820 | −0.040711536760 | −0.041590060437 | 0.000657 |
| 20 | 0.077660185766 | 0.077491305516 | 0.077023911320 | 0.000607 |

The comparisons support the density calculation and agree with the rigorously certified signs. Numerical root finding suggests crossings near 1.2228361663 and 7.7615867626; their locations and the absence of other crossings are **not certified**.

`data/candidate_curve.png` and `.pdf` plot the density calculation, with sign certificates shown separately.

## Literature result

* Lawley, Mattingly, Reed, “Sensitivity to switching rates in stochastically switched ODEs”, Commun. Math. Sci. 12(7) (2014), 1343–1352, DOI [10.4310/CMS.2014.v12.n7.a9](https://doi.org/10.4310/CMS.2014.v12.n7.a9), [arXiv:1310.2525](https://arxiv.org/abs/1310.2525). Example 3.1 is planar. Example 3.3 constructs k separated instability windows in dimension **2k**, by direct sums. For k=2 this is 4-by-4 and does not answer E0018. Theorems 2.3–2.4 establish slow/fast stability when the individual/averaged matrices are Hurwitz.
* Benaïm, Lobry, Sari, Strickler, “A note on the top Lyapunov exponent of linear cooperative systems”, Ann. Fac. Sci. Toulouse 34(1) (2025), 225–241, DOI [10.5802/afst.1811](https://doi.org/10.5802/afst.1811), [arXiv:2302.05874](https://arxiv.org/abs/2302.05874). Slow/fast limiting formulas for cooperative systems; these alone do not give several planar instability windows. The saved arXiv version numbers its slow/fast results Propositions 4 and 5; journal numbering differs.
* Chitour, Mazanti, Monmarché, Sigalotti, “On the gap between deterministic and probabilistic Lyapunov exponents for continuous-time linear systems”, Electron. J. Probab. 28 (2023), article 43, 1–39, DOI [10.1214/23-EJP932](https://doi.org/10.1214/23-EJP932), [arXiv:2112.07005](https://arxiv.org/abs/2112.07005). Theorems 3.1 and 3.4 concern equality with the deterministic maximum and compactification of Markov switching laws; these are different from oscillations along a fixed symmetric-rate family.
* Malrieu and **Tran Hoa Phu** (rather than “Phung”), “Lotka–Volterra with randomly fluctuating environments: a full description”, [arXiv:1607.04395](https://arxiv.org/abs/1607.04395). This concerns nonlinear competition and invasion exponents. It is not a multiple-window result for constant planar linear matrices.
* Monmarché and Strickler, “Asymptotic expansion of the invariant measure for Markov-modulated ODEs at high frequency”, [arXiv:2309.16464](https://arxiv.org/abs/2309.16464). Proposition 3 constructs cooperative matrices with stable convex hull and switching instability in dimension 3; the text explicitly distinguishes the planar cooperative obstruction. Not a planar multiple-window example.
* Monmarché, Schreiber, Strickler, “Impacts of Tempo and Mode of Environmental Fluctuations on Population Growth: Slow- and Fast-Limit Approximations of Lyapunov Exponents for Periodic and Random Environments”, Bull. Math. Biol. 87 (2025), 81, DOI [10.1007/s11538-025-01443-z](https://doi.org/10.1007/s11538-025-01443-z). The asymmetric migration nonmonotonicity examples in Section 4 use d≥3 patches. Nonmonotonicity alone also does not imply two positive components.

The first pass used the named authors, the paper title and arXiv identifier, “oscillations”, “several intervals”, “switching rate”, and “Lyapunov exponent”. An expanded citation check fetched OpenAlex work W1869666954 and all 49 citing records returned on 2026-11-13. Raw responses are `data/openalex_source_work.json` and `data/openalex_citing_works.json`; the title/abstract screen is `data/citation_screen.tsv`. This inventory includes duplicates, preprints and theses; it is not 49 independently read research papers. The potentially relevant sign/exponent sources above were checked directly. Additional primary-source checks were:

* Benaïm and Strickler, “Random switching between vector fields having a common zero”, Ann. Appl. Probab. 29(1) (2019), 326–375, [DOI 10.1214/18-AAP1418](https://doi.org/10.1214/18-AAP1418), [arXiv:1702.03089](https://arxiv.org/abs/1702.03089). Section 2 develops invariant-angle growth rates and their relation to the top exponent; Section 2.4 addresses fast switching. No several-window planar example was found there.
* Hurth and Kuehn, “Random switching near bifurcations”, Stochastics and Dynamics 20(2) (2020), 2050008, [arXiv:1901.00124](https://arxiv.org/abs/1901.00124). This classifies nonlinear normal forms and invariant measures, rather than the requested rate-dependent planar linear exponent.
* Benaïm and Tough, “Regularity of the stationary density for systems with fast random switching”, Nonlinearity 38 (2025), 085012, [DOI 10.1088/1361-6544/adeef8](https://doi.org/10.1088/1361-6544/adeef8), [arXiv:2212.03632](https://arxiv.org/abs/2212.03632). This concerns density regularity, not an oscillating sign theorem. The 2021 Bakhtin–Hurth–Lawley–Mattingly density paper concerns distinct fixed points, as its abstract explicitly states; it is not a homogeneous switching-exponent answer.

No published resolution of the exact several-interval question was identified. The search is documented but cannot establish absence from the literature; no novelty priority claim is made. In particular, the higher-dimensional result in Lawley–Mattingly–Reed is not relabelled as a planar result.

## Reproduction and resource limits

Run from this directory. The sign proof can be checked without NumPy, SciPy or a compiler:

```sh
python3 code/verify_certificate.py
python3 code/certified_neighborhoods.py
```

The outward interval audit requires mpmath:

```sh
python3 code/interval_audit.py
```

For numerical checks, NumPy and SciPy are required. Matrix-flow Monte Carlo uses the system C compiler:

```sh
clang -O2 code/monte_carlo.c -o code/monte_carlo
./code/monte_carlo > data/monte_carlo_blocks.csv
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/validate_candidate.py
python3 code/audit_grid.py
python3 code/plot_candidate.py
```

Run numerical commands at nice 10 or lower scheduling priority. This session inherited nice 10; `os.getpriority` verified it. All calculations used one BLAS thread and no parallel workers. The density/CTMC validation recorded peak RSS 124,829,696 bytes, approximately 119.0 MiB. macOS sandboxing rejected `setrlimit(RLIMIT_AS)`; array sizes and measured resource use stayed well under 4 GB. No package installation, subagent, publication or push was performed. All task writes are inside this directory.

Task: “Open problem E0018” — started 2026-11-13 04:22 +04.
