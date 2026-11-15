MINOR

The stated sign pattern is correct and rigorously certified. Independent stationary-density calculations, a separate finite-volume approximation, and 45 million Monte Carlo cycles reproduce it. In particular, the negative sign at r=5 survives an exact rational audit; it is not an inference from a plot or a numerical confidence interval.

My ruling on the wording is that Open question 3, read literally, permits general real 2×2 matrices. Its surrounding example is Hurwitz, including its convex hull, but the question does not expressly retain that restriction. I therefore accept the claim's explicitly qualified unrestricted theorem. I would not describe this as a resolution of the both-Hurwitz version, or as establishing the author's intended scope. The source leaves that intent ambiguous. The minor corrections below do not invalidate the theorem.

1. **Incorrect coordinate description.** Location: `claim_files/REPORT.md:254–263` and the opening docstring of `claim_files/code/candidate_density.py`. The second branch of the implemented ODE uses x=−log|tan θ|, equivalently θ=π/2+atan(exp x), not x=log|tan θ| as stated. With the latter coordinate, cos(2θ)=−tanh x on both half-circles, whereas the code uses +tanh x on the second branch. Fix the definition on that branch. The implemented second ODE and reward are consistent with the corrected coordinate; the reported numbers are correct.
2. **Incomplete account of closely related prior work.** Location: `claim_files/REPORT.md:293–308`. Add Lagasquie, arXiv:1612.01861, especially the introduction and Section 5. It directly investigates multiple planar blow-up regions, but obtains the additional region after replacing exponential matrix holding times by Gamma holding times, using 2n environmental states. Also distinguish the discrete-time windows of Porfiri–Jeter–Belykh (2019), and their nonlinear antiresonance example (2021). None is a verified prior solution to this exact two-state linear exponential-switching problem. This is a literature gap, not a refutation; the submitted report already disclaims priority.
3. **Source-package omission.** Location: `claim_files/REPORT.md:34`, its literature discussion, and `claim_files/data/artifact_hashes.json`. The supplied snapshot has no `claim_files/sources/`, although the report refers to it. Of the manifest's entries, 37 supplied files match their hashes, 25 source/manifest entries are absent, and none of the available entries has a mismatching hash. Fix the distributed manifest or supply the source bundle. I downloaded the principal sources independently into this audit's `sources/`. This observation concerns the supplied package, not whether those downloads existed in the other run.
4. **Scope and novelty remain limited.** Location: title/opening and `claim_files/REPORT.md:30,42,308`. Retain the unrestricted qualification whenever reporting the result. Neither the finite-rate signs nor the literature search resolves the Hurwitz-restricted problem, proves exactly two components, or establishes historical priority. Calling the Hurwitz reading merely a strengthening understates its motivation in the surrounding discussion. Fix by explicitly distinguishing the literal formulation from the contextual Hurwitz interpretation, as below.

No false sign, factor-of-two error, or failure of the rational certificate was found.

## Source wording and ruling

I downloaded [arXiv:1412.7516](https://arxiv.org/pdf/1412.7516) and the [published version](https://www.numdam.org/item/AFST_2015_6_24_4_857_0.pdf), and read Section 4, including the complete text surrounding Open questions 2 and 3. The local files are `sources/malrieu_1412.7516.{pdf,txt}` and `sources/malrieu_journal.{pdf,txt}`. Open question 3 is on printed arXiv page 10 and journal page 871.

Section 4.1 says: “The two matrices A0 and A1 are Hurwitz matrices”. It also establishes stability of every convex combination of its particular shear pair. After discussing a conjecturally single instability interval and a modification of the matrices, Open question 3 asks whether one can “choose the two 2×2 matrices” to obtain “the union of several intervals”. The journal has the same substantive wording. These short quotations preserve the relevant distinction: Hurwitz is stated about the example; it is not repeated as a condition in the question.

I rule **unrestricted in the literal formulation**. Requiring the exact shear matrices would reduce the question to the preceding question about their function G. A requirement to keep both matrices Hurwitz, or even the entire convex hull Hurwitz, is a plausible contextual intention, but is not an explicit hypothesis of Open question 3. The text does not justify presenting that intention as certain. Conversely, a literal answer does not establish that the motivating Hurwitz problem has been solved. No subsequent part of Section 4 settles this ambiguity.

The verified result is consequently: there exist two real planar matrices, one Hurwitz and one not Hurwitz, for which the positive-exponent set has at least two connected components. **There is no verified both-Hurwitz example in the submission or this review.** If a problem specification expressly retains that restriction, this submission does not answer that problem and would merit MAJOR on scope. My MINOR verdict applies to the expressly unrestricted claim actually made in the submitted report.

## Model, angular law, and exponent

The paper's equation (8), journal equation (4.1), has actual flip generator

\[
Q_r=\begin{pmatrix}-r&r\\r&-r\end{pmatrix}.
\]

Thus each holding time is Exp(r), its mean is 1/r, and the stationary environmental law is (1/2,1/2). The submission uses this convention consistently. A redraw clock that independently chooses either state with probability 1/2 needs intensity 2r to give these actual flip rates.

For u=(cos θ,sin θ), θ modulo π, I derived directly

\[
\dot\theta=v_i=u_\perp^TA_i u,\qquad
\frac{d}{dt}\log\|X\|=h_i=u^TA_i u.
\]

For the submitted matrices this gives

\[
v_0=1,\quad v_1=-2\sin2\theta,\qquad
h_0=-3/4,\quad h_1=-3/4+2\cos2\theta.
\]

The stationary **joint** densities satisfy

\[
p_0'=r(p_1-p_0),\qquad (v_1p_1)'=r(p_0-p_1),
\quad \int_0^\pi p_i=1/2.
\]

Their total flux J=p0+v1 p1 is constant and positive. Imposing zero flux would be incorrect here. The radial average is

\[
\lambda(r)=-\frac34+2\int_0^\pi\cos2\theta\,p_1(\theta)\,d\theta.
\]

State 0 rotates through all projective directions. At successive entries into state 1, an independent rotation time modulo π has density bounded below by r/(exp(πr)−1). This gives a Doeblin minorization, a unique stationary angular law, and the same almost-sure exponent for each fixed nonzero initial vector. Using two basis vectors identifies this with the top matrix exponent. The minorization is uniform on compact positive rate ranges; the exponential holding-time densities and integrable cycle rewards vary continuously there. Thus λ is continuous. There is no unresolved choice of invariant angular measure in this example.

## Independent numerical work

All referee computation is in `referee_code/`. No submitted code was imported or executed. Submitted certificate coefficients were used as proof data, then checked by independently written algebra.

For the density calculation I used two coordinates directed from the repelling state-1 direction to its attracting direction:

\[
\theta_+(t)=\arctan(e^{-t}),\qquad
\theta_-(t)=\pi/2+\arctan(e^t),\qquad
w(t)=\frac1{2\cosh t}.
\]

Both have cos(2θ)=tanh t. Writing y=p0/J−1 gives

\[
y'=r\left(\sigma w(1+y)-y/4\right),\qquad
p_1|d\theta/dt|=J\sigma y/4,\qquad\sigma=+1,-1.
\]

I integrated from t=−45 to 45, with y initially zero, and normalized using ∫p0=1/2. Crucially, I integrated (cos(2θ)−1)p1 rather than the slowly decaying p1 tail. If S is the sum of ∫(1+y)w dt over the arcs and C is the sum of ∫(tanh t−1)σy/4 dt, then J=1/(2S) and λ=1/4+C/S. A refinement to endpoints ±55, half the maximum step, and tighter tolerances changed the three answers by at most 4.7×10⁻¹⁴. This is a numerical convergence observation, not a rigorous error bound.

A separate conservative upwind finite-volume method solved the stationary joint density with exact face velocities on 1,024, 4,096, 16,384 and 65,536 cells. Its finest values are shown below. Its algebraic stationarity residual is small, but its remaining mesh error is visible and is not a certificate.

My Monte Carlo uses exact rotations and diagonal matrix flows between independent exponential holding times, with analytic rescaling to avoid overflow and a PCG32 random generator. For each rate: three distinct seeds, 100,000 discarded cycles per seed, then 5,000,000 retained cycles per seed, in 100 blocks. One cycle contains two actual flips. This is 15 million retained cycles per rate and 90 million retained flips overall. Standard errors are batch estimates for the reward/time ratio, not rigorous probability bounds.

| Actual r | Independent density | Finite volume, 65,536 cells | Independent Monte Carlo | Batch SE |
|---:|---:|---:|---:|---:|
| 0.1 | 0.2164448559659 | 0.2164438842624 | 0.2164637003 | 0.0001892 |
| 5 | −0.0406115058196 | −0.0406524188779 | −0.0407130298 | 0.0003180 |
| 20 | 0.0776601857656 | 0.0775940437549 | 0.0776409208 | 0.0002696 |

A 151-rate density grid on [0.001,1000] has two sampled sign changes. Numerical roots are approximately 1.2228361665 and 7.7615867624. Neither the roots nor absence of additional components is certified. The data are `referee_data/grid.csv`, `density.json`, `monte_carlo.csv`, and `summary.json`; the independent curve is `referee_data/independent_curve.pdf`.

## The certification really is rigorous

There is **no validated enclosure of the invariant density** in the submission. Its density solver, tolerance comparisons, CTMC residuals and Monte Carlo do not provide such an enclosure. That is not a hole in its sign proof: the proof uses a different, valid method.

For any smooth bounded π-periodic pair f, define g_i=h_i+(L_r f)_i. The stationary integral of L_r f is zero. Equivalently, along trajectories the bounded endpoint correction and a bounded-jump martingale divided by elapsed time vanish. Therefore pointwise bounds ℓ≤g_i≤u imply ℓ≤λ≤u, without estimating p_i at all.

I reconstructed the supplied rational f coefficients as Laurent polynomials in z=exp(2iθ), applied Dθ z^k=2ik z^k, and multiplied by v0=1 and v1=i(z−z⁻¹). Every operation used Python Fraction integers/rationals. For g=C+Σ(a_k cos2kθ+b_k sin2kθ), the elementary bound C±Σ(|a_k|+|b_k|) is exact. This audit is `referee_code/certificates.py`, with results in `referee_data/certificate_audit.json`.

| r | State | Exact lower endpoint | Exact upper endpoint |
|---:|---:|---:|---:|
| 5 | 0 | −0.040550774017 | −0.040550757183 |
| 5 | 1 | −0.071355633951 | −0.009745897257 |
| 20 | 0 | 0.077654745278 | 0.077654746482 |
| 20 | 1 | 0.070309824390 | 0.084999667350 |

All displayed finite decimals in this table are exact rational endpoints. No floating-point rounding, unvalidated quadrature, omitted Fourier tail, or numerical linear-solver accuracy enters these bounds. The f are finite polynomials, including their highest generated harmonics. In particular, both state upper bounds at r=5 are strictly negative. The certificate construction's approximate solve is irrelevant once the rational coefficients have been checked.

I also recovered the coefficient bounds D=||f1−f0||∞ used for perturbing r, and verified the negative neighborhood [4.997,5.003] and positive neighborhood [19.95,20.05].

For r=0.1 I independently recovered the renewal lower bound. The angle entering state 1 has conditional density at most M=r/(1−exp(−πr)); the angle penalty has mean at least −Mπ log2. A cycle has mean length 2/r and its unpenalized mean growth divided by time is 1/4. Hence

\[
\lambda(r)\ge\frac14-\frac{r^2\pi\log2}{2(1-e^{-\pi r})}.
\]

Using 1−e⁻ˣ≥x/(1+x), π<4 and log2<1 proves λ(r)>9/50 for 0<r≤1/10. Thus the low-rate claim is rigorous too. Continuity and the positive/negative/positive witnesses prove at least two open connected components of {r>0:λ(r)>0}.

## Independent limiting checks and the Hurwitz obstruction

The eigenvalues of A0 are −3/4±i; those of A1 are 5/4 and −11/4. The slow-switching limit is

\[
\lim_{r\downarrow0}\lambda(r)=\tfrac12(-3/4+5/4)=1/4.
\]

Here this does not require a blanket slow-switching theorem: submultiplicativity and environmental occupations give λ(r)≤1/4, while the preceding lower bound tends to 1/4. Numerically λ(0.0001)=0.2499653436691.

The averaged matrix is

\[
\bar A=\begin{pmatrix}1/4&-1/2\\1/2&-7/4\end{pmatrix},\qquad
\alpha(\bar A)=-3/4+\sqrt3/2=0.1160254037844\ldots.
\]

The fast-switching limit equals this number. [Chitour–Mazanti–Monmarché–Sigalotti, Proposition 6.4](https://arxiv.org/pdf/2112.07005) applies: the mean has distinct real eigenvalues, and the projected A0 field moves off its lower eigenspace, satisfying condition (C). Their redraw intensity is μ=2r. This checks the necessary hypothesis rather than assuming finite-time averaging alone proves convergence of exponents. Independently, λ(100)=0.1092220461386 and λ(1000)=0.1153574463516 approach the asserted limit.

Both endpoints are unstable in this example. The intermediate negative band therefore separates two positive regions without requiring repeated bounded instability windows. Merely having a non-Hurwitz matrix does not make this automatic: two identical unstable diagonal matrices give a positive constant exponent and only one component.

Nor can scalar shifts rescue this particular pair for the Hurwitz problem. Both matrices are normal, and scalar shifts preserve normality. If shifted to become Hurwitz, each symmetric part becomes negative definite, and every switched trajectory contracts exponentially for every rate. This is also the elementary mechanism in Lawley–Mattingly–Reed's Theorem 2.1. A Hurwitz answer would require a different construction, not a relabeling of these witnesses.

## Literature result and what is new

I checked the named primary sources and independently fetched OpenAlex citation inventories for Malrieu (49 records) and Lawley–Mattingly–Reed (41 records). Raw inventories and title lists are in `referee_data/`. These are discovery aids, not 90 fully read papers. A direct DOI lookup initially returned HTTP 404; title search recovered the correct records. The search also covered oscillations, disconnected instability intervals, rate nonmonotonicity, antiresonance and stochastic windows.

- [Lawley–Mattingly–Reed (2014), Example 3.3](https://arxiv.org/pdf/1310.2525) already gives arbitrarily many separated instability regions for two matrices in dimension 2k. Two regions use dimension 4. Their planar Example 3.1 gives a positive intermediate regime and stable slow/fast regimes, not two established positive components. This is not a prior planar solution.
- [Benaïm–Le Borgne–Malrieu–Zitt (2014)](https://arxiv.org/pdf/1204.1921) assumes two Hurwitz matrices and a convex combination with a positive eigenvalue. Its rate-dependent blow-up and explicit angular laws do not establish the requested two positive components. Its particular monotonicity result, Lemma 3.3, is not a theorem for all planar pairs.
- [Lagasquie, arXiv:1612.01861](https://arxiv.org/pdf/1612.01861), is an especially relevant omitted comparison. It tries elliptic Hurwitz matrices and discusses the failure of its two-state exponential example to produce the desired extra area. Section 5 and Figure 5 produce a second area after adding environmental phases, so the matrix holding times become Gamma. That retains two distinct matrices and planar X, but changes the two-state generator. It cannot be cited as a solution in the present rate convention.
- [Porfiri–Jeter–Belykh (2019)](https://math.gsu.edu/ibelykh/2018_Automatica.pdf) gives disconnected stability windows for a discrete-time system holding an iid matrix for an integer number of steps. [Their 2021 antiresonance paper](https://math.gsu.edu/ibelykh/2021_PRResearch_antiresonance.pdf) has a nonlinear planar system with unstable modes; reciprocal radial coordinates connect it to a linear resonance problem. That nonlinear coordinate change does not furnish two constant linear matrices with the claimed sign pattern. Neither paper settles this model.
- [Benaïm–Strickler (2019)](https://arxiv.org/pdf/1702.03089) identifies the top exponent with the maximal stationary angular growth rate and treats fast switching. [Chitour–Mazanti–Monmarché–Sigalotti (2023)](https://arxiv.org/pdf/2112.07005) studies deterministic/probabilistic exponent gaps and supplies the applicable fast-limit result above. I found no multiple-window planar theorem in these results.
- [Monmarché–Strickler](https://arxiv.org/pdf/2309.16464), Proposition 3, constructs cooperative switching instability with stable convex hull in dimension 3. [Monmarché–Schreiber–Strickler](https://arxiv.org/pdf/2408.11179), Section 4.2, gives nonmonotonic growth examples with at least three patches. Neither yields the required planar pair. Cooperative slow/fast asymptotics in [Benaïm–Lobry–Sari–Strickler](https://arxiv.org/pdf/2302.05874) likewise do not settle this question.

The contribution verified here is an explicit rational, mixed Hurwitz/non-Hurwitz planar pair and finite, independently checkable certificates for its disconnected positive-exponent set. I found no prior exact example in the sources checked, but **historical novelty is not established by this search**. Generic nonmonotonicity, higher-dimensional direct sums, nonexponential holding times, discrete time, and nonlinear stabilization are already known and must not be claimed as new. The existence of several instability components with both matrices Hurwitz remains unresolved by this submission and this audit; this is a statement about what was established here, not a proof that no later paper has resolved it.

## Reproduction and audit record

Run from this directory:

```sh
python3 referee_code/certificates.py
python3 referee_code/density.py
clang -O2 -Wall -Wextra referee_code/monte_carlo.c -o referee_code/monte_carlo
./referee_code/monte_carlo > referee_data/monte_carlo.csv
python3 referee_code/summarize.py
python3 referee_code/plot.py
```

The scripts pin numerical-library threads to one. The session inherited nice=15, which is lower scheduling priority than the requested nice=10. At most two numerical processes ran concurrently; Python peak RSS was 338,149,376 bytes (about 322.5 MiB). The C simulation uses constant-size scalar state and streams its output. Work stayed well below 4 GB. No subagents, publication, pushes, package installations, or mutations of the supplied claim files occurred. `LOG.md` records intermediate findings and the exploratory numerical limitation. Source URLs, hashes, and result hashes accompany the artifacts.

Task: “You are an independent referee … Break it if it is wrong.” — started 2026-11-13 04:47 +04.
