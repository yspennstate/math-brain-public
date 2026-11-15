# Referee report on PAPER.tex

**Overall verdict: SOUND.** The four-state construction and elementary proof are valid. They refute the continuous-time, stationary, Kolmogorov-distance question with a bound depending only on `b=||g||_infty` and `s=t/tau_2`, as stated in the audit request. I found no load-bearing mathematical gap or false display. This verdict does not certify the exact literature quotations or novelty, which could not be checked under the no-browsing rule.

The audit used only the supplied source and independently written programs. `PAPER.tex` was not changed. No author program, outside agent, network source, push or visible window was used. All writes were confined to this directory. Computations ran one at a time, with one numerical thread and no worker subprocesses. The longest took 4.95 seconds; the largest reported peak RSS was 552,566,784 bytes. The requested nice priority change was denied by the sandbox; the brief, single-thread computations completed within the author's resource limits.

`LOG.md` records the requested seven stages in order, including full derivations and the judgments as reached. In the tables below, GAP for an external attribution means missing source verification, not a gap in the independent proof.

## Verdict table

| Statement or step (source lines) | Verdict | Reason |
|---|---|---|
| Setup, standardization and S_t display (3740) | CORRECT | Finite reversible generator admits a real orthonormal spectral basis. |
| Existence and positivity of sigma (41) | CORRECT | `sigma=2 sum a_k/lambda_k`, with positive eigenvalues and `sum a_k=1`. |
| `sigma<=2 tau_2` (41) | CORRECT | Every inverse eigenvalue is at most `tau_2`. |
| Variance bounds and A(u) display (4244) | CORRECT | Exact variance is `2 sum a_k[t/lambda_k-(1-e^{-lambda_k t})/lambda_k]`; A is increasing. |
| Interpretation as relative variance control (45) | CORRECT | The ratio to `t sigma` is between A(t/tau_2) and 1. |
| Fixed-chain CLT and BerryEsseen rate (45) | CORRECT | Standard finite-state additive-functional statement; constants may depend on the chain. |
| Attribution to AF Propositions 4.29 and 4.51 (41,45) | GAP | Content is consistent; exact numbering and quotations were not independently recalled with confidence. |
| Open Problem wording/number (4548) | GAP | Matches the question supplied for this audit; the original text was not available for comparison. |
| [eq:op] normalization and quantifiers (4648) | CORRECT | Stationary law, asymptotic sigma sqrt(t), and a bound covering all chains at each s. |
| [thm:main], first display (5155) | CORRECT | Follows from the fully checked construction and probability proof. |
| [thm:main], every c>0 display (5659) | CORRECT | At x=0, division by positive c leaves the event unchanged. |
| Chain depending on s; liminf psi>=1/2 (62) | CORRECT | A chain-uniform bound must cover each selected chain; fix b while s grows. |
| Standardized g implies sup norm >=1 (62) | CORRECT | `1=pi(g)<=||g||_infty`. |
| Adding state count or exact variance normalization (62) | CORRECT | All examples have four states; the threshold argument works for any positive divisor. |
| Prescribed relaxation time (62) | CORRECT | Time change transfers the result to t=s tau_2. |
| What is missing is a lower bound (64) | CORRECT | The construction forces sigma/tau_2 to zero; sufficiency uses the cited inequality. |
| Lezaud bound [eq:lezaud], shape (6566) | CORRECT | Plausible spectral BerryEsseen dependence; consistent with these chains, where its RHS grows like sqrt(s). |
| Lezaud constant 26, theorem number and hypotheses (6466) | GAP | Cannot verify an unopened external result; not used in the counterexample proof. |
| Second form of [eq:lezaud] (67) | CORRECT | `sqrt(tau_2/sigma)(t/tau_2)^(-1/2)=tau_2/(sigma sqrt(t))`. |
| Class-wide lower variance ratio suffices (69,141) | CORRECT | Conditional on the cited Lezaud bound, substitute that lower bound. |
| Two-state sigma=2 tau_2 (69) | CORRECT | The centered function space has only the gap eigenmode. |
| sigma is of order s^{-2} (69) | GAP | Add for fixed b; for b=s/2 the slow variance term tends to 1/2. |
| Parameter display and g display (7381) | CORRECT | All definitions are well-defined over the full stated parameter range. |
| [lem:chain](a), alpha bounds (85,93) | CORRECT | `epsilon,bepsilon<=1/4`, and `b>=1`. |
| [lem:chain](a), m bounds and positive specified rates (85,93) | CORRECT | `alpha(1-epsilon)<=1` and `alpha(1-epsilon)>3/5` yield `b epsilon<=m<5/12<1/2`. |
| [lem:chain](b), irreducibility, balance, stationary product (86,95) | CORRECT | Positive coordinate jumps connect the states; each marginal satisfies detailed balance. |
| Direct computation -Qu=u (97) | CORRECT | Values of Q_Yu are epsilon and -(1-epsilon). |
| Direct computation -Qw=Rw (97) | CORRECT | Values of Q_Vw are -R(1+m) and R(1-m). |
| Product eigenfunction and constant (97) | CORRECT | Separate generator terms give -(R+1)uw and Q1=0. |
| [lem:chain](c), complete spectrum and tau_2 (87,97) | CORRECT | The four tensor-product eigenfunctions form a basis; R>=16. |
| [lem:chain](d), mean zero (88,99) | CORRECT | `-alpha(1-epsilon)m+b epsilon=0`. |
| [lem:chain](d), second moment one (88,99) | CORRECT | `alpha(1-epsilon)+bepsilon=1`. |
| [lem:chain](d), sup norm b (88,99) | CORRECT | `alpha<=1<=b`, and g=b on two states. |
| Definition of H,J and S_s=alpha J on H (104) | CORRECT | On H, Y stays zero throughout. |
| [eq:split], first inequality (106) | CORRECT | Event inclusion and alpha>0. |
| [eq:split], second inequality (106) | CORRECT | Union bound; independence is not needed. |
| Independence of H and J (104108) | CORRECT | They depend on independent coordinate paths under the product stationary initial law. |
| P(H) and its lower bounds (108) | CORRECT | Initial mass times exponential survival, followed by `e^{-x}>=1-x`. |
| E J=-ms (108) | CORRECT | Stationary mean of V is -m. |
| Covariance of V (108) | CORRECT | Centered V has variance 1-m and decay rate R. |
| Variance integral and bound display (109111) | CORRECT | Double-integrate the covariance; discard the nonnegative exponential correction. |
| Chebyshev display (112115) | CORRECT | The threshold for J-EJ is ms>0. |
| R ms>=bs>=s (116) | CORRECT | Substitute m>=b s^{-2} and R=s^4. |
| epsilon(1+s)<=3/(2s) (116) | CORRECT | Uses s>=2. |
| Final 1-4/s display (117120) | CORRECT | The preceding estimates actually give 1-7/(2s). |
| [rem:scale], all time-change identities (125) | CORRECT | Generator scales by kappa; integral and variance rate scale by 1/kappa. |
| Rates/R, tau_2=s^4, t=s^5 (125) | CORRECT | Choose kappa=1/R and original observation time s; divided rates are <=1. |
| [rem:sigma], g expansion display (129132) | CORRECT | Pointwise expansion leaves constant `alpha m(1-epsilon)-b epsilon=0`. |
| Orthogonality and all three norms (133) | CORRECT | Product law and centered coordinate functions. |
| Spectral sigma formula and displayed result (133136) | CORRECT | Sum squared component norms divided by 1,R,R+1, times 2. |
| ssigma -> 2b (137) | CORRECT | Slow term is `2b/[s(1-s^{-2})]`; fast terms are <=2/s^4; b fixed. |
| Probability 1-8/s for the J event (137) | CORRECT | Chebyshev at half the mean magnitude multiplies the earlier tail bound by 4. |
| Bound on S_s on its intersection with H (137) | CORRECT | J lies between -3ms/2 and -ms/2 there. |
| alpha m s normalization identity and rate (137) | CORRECT | Equals `b/((1-epsilon)sigma s^{3/2})~1/sqrt(2s)`. |
| W_s -> 0 in probability (137) | CORRECT | At an O(s^{-1/2}) threshold the failure probability is at most 19/(2s). |
| Kolmogorov distance ->1/2 (137) | CORRECT | Upper bound follows from concentration near zero; theorem supplies the matching lower bound. |
| E W_s>=A(s)->1 (137) | CORRECT | The upper variance bound also gives E W_s<=1. |
| Variance carried by H complement; sizes and probability (137) | CORRECT | In the asymptotic/typical sense: P(H^c)~1/s and E[W_s 1_H]~1/(2s). |
| Drift/rare-visit explanation (141) | CORRECT | Fast negative mean is compensated by rare positive occupation. |
| iid BerryEsseen comparison; third moment <=b (141) | CORRECT | `E|U|<=b E U=b`; use the normalized sum. |
| FeynmanKac characteristic-function formula (146) | CORRECT | For column pi, `pi^T exp(s(Q+i theta G))1` is the stationary transform. |
| Numerical example b=2,s=8 (146) | CORRECT | Independently estimated 0.884396 (SE 0.000319749); proof bound 0.8017578125. |
| Claims about author scripts and Lean checks (146) | GAP | Files and execution records were not supplied; independent checks do not certify them. |
| KipnisVaradhan historical wording (64) | GAP | Their broad reversible-process theorem is known; attributing the earlier finite-state CLT to them would overstate the claim. |
| Bolthausen broad attribution (64,179180) | CORRECT | Consistent with remembered work on Markov-functional BerryEsseen bounds; exact bibliographic details unverified. |
| Novelty and exact bibliographic particulars | GAP | No remembered prior solution that can reliably be named; priority requires a literature audit. |

## Why the main conclusion follows

For `g=sum a_k phi_k` with `sum a_k=1`, independent spectral calculation gives

\[
\sigma^2=2\sum_{k\ge2}\frac{a_k^2}{\lambda_k},\qquad
\operatorname{var}_\pi S_t=t\sum_{k\ge2}\frac{2a_k^2}{\lambda_k}A(\lambda_k t).
\]

The paper's parameters satisfy all positivity, stationarity and standardization requirements. Its probability proof yields

\[
P(S_s\le0)\ge P(H)-P(J>0)
\ge1-\frac{3}{2s}-\frac2s\ge1-\frac4s.
\]

Since dividing by a positive constant does not change the event at zero, the Kolmogorov lower bound holds for the problem's normalization. Fixing any b, even b=1, and choosing the constructed chain for each s contradicts a chain-uniform bound tending to zero. The construction also obstructs bounds that add only the number of states or an upper bound on transition rates.

Allowing additional dependence on sigma/tau_2, stationary probabilities or the ratio of extreme nonzero eigenvalues would change the question and is not excluded. This proof is specifically continuous time. Distances that dominate Kolmogorov are also obstructed, but a claim for an arbitrary unspecified different distance needs a separate argument. For these normalized laws, convergence to a standard normal fails even in the weak-convergence sense: they instead concentrate at zero.

The distinction between concentration and variance in the remark is valid. For fixed b,

\[
\frac{\alpha ms}{\sigma\sqrt{s}}\sim\frac1{\sqrt{2s}},\qquad
P\left(|W_s|>\frac{3b}{2(1-\varepsilon)\sigma s^{3/2}}\right)\le\frac{19}{2s}.
\]

Nevertheless, `E W_s->1`. In fact

\[
E[W_s^2\mathbf1_H]=P(H)\frac{\alpha^2\{\operatorname{var}(J)+m^2s^2\}}{s\sigma^2}
\sim\frac1{2s},\qquad P(H^c)\sim\frac1s.
\]

Thus the second moment on the complement tends to one. Conditional RMS there is asymptotic to sqrt(s). This establishes the claimed rare-excursion explanation without relying on a heuristic picture.

## Exact four-state checks

State order: `(0,-1),(0,1),(1,-1),(1,1)`. `exact_checks.py` constructs Q directly from the two specified coordinate rates. All entries below were checked with exact SymPy arithmetic, including radicals. Balance residual is the full matrix `diag(pi)Q-Q^T diag(pi)`.

| (b,s) | alpha | m | eigenvalues of -Q | pi(g) | pi(g) | sup norm | balance residual |
|---|---|---|---|---|---|---|---|
| (1,2) | 1 | 1/3 | 0,1,16,17 | 0 | 1 | 1 | 0 |
| (1,10) | 1 | 1/99 | 0,1,10000,10001 | 0 | 1 | 1 | 0 |
| (3,6) | 27/35 | sqrt(105)/105 | 0,1,1296,1297 | 0 | 1 | 3 | 0 |
| (5,100) | 3325/3333 | sqrt(443289)/1329867 | 0,1,100000000,100000001 | 0 | 1 | 5 | 0 |

Additional exact assertions check pi Q=0, Q1=0, every eigenvector equation, the full characteristic polynomial, the g expansion, its component Gram matrix, and agreement of sigma with an independent centered Poisson-equation solve. Full matrices are in `exact_matrices.txt`; structured results are in `exact_checks.json`.

Command used (nice priority request was denied; calculation completed):

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 10 python3 exact_checks.py
```

## Independent probabilities and variances

These are **simulations with 1,000,000 independent runs per pair**. Standard errors are `sqrt(p_hat(1-p_hat)/1000000)`; they do not include a deterministic numerical-inversion error because no inversion was used.

| (b,s) | count with S_s<=0 | estimated probability | standard error | theorem bound 1-4/s |
|---|---|---|---|---|
| (1,2) | 589126 | 0.589126 | 0.000491992 | -1.000000 |
| (1,10) | 895411 | 0.895411 | 0.000306023 | 0.600000 |
| (1,50) | 980372 | 0.980372 | 0.000138718 | 0.920000 |
| (3,6) | 850520 | 0.850520 | 0.000356561 | 0.333333 |
| (3,60) | 983301 | 0.983301 | 0.000128141 | 0.933333 |

The saved program `probability_checks.py` samples the exact occupation law through rate-R stationary refreshes. Conditional on N refreshes, N+1 time spacings have a Dirichlet law; aggregate positive time is beta-distributed conditional on a binomial count of positive signs. It jointly samples the occupation and terminal sign, retaining the correct dependence between intervals. Y uses ordinary exponential holding times. This avoids the billions of fast jumps a direct simulation would require across all runs. There is no time-grid or diffusion approximation. The full justification is in `LOG.md` and the program docstring. Seeds are `43020261112` through `43020261116` in table order.

The finite-time variances below are **exact analytic spectral expressions evaluated at 60-decimal working precision**, rounded for display. Let

\[
D=\alpha^2-\frac{b^2\varepsilon^2}{(1-\varepsilon)^2},\quad
d_1=\frac{b^2\varepsilon}{1-\varepsilon},\quad
d_R=D(1-\varepsilon)^2,\quad
d_{R+1}=D\varepsilon(1-\varepsilon).
\]

These rational weights sum to one. Evaluate `sigma=2 sum d_lambda/lambda` and

\[
\operatorname{var}_\pi S_s=2\sum_{\lambda\in\{1,R,R+1\}}d_\lambda
\left(\frac{s}{\lambda}-\frac{1-e^{-\lambda s}}{\lambda^2}\right).
\]

| (b,s) | sigma | A(s) s sigma | exact-expression var_pi S_s | s sigma |
|---|---|---|---|---|
| (1,2) | 0.748774509804 | 0.850110120169 | 0.916046222561 | 1.497549019608 |
| (1,10) | 0.0203999998020 | 0.183600924377 | 0.183798875191 | 0.203999998020 |
| (1,50) | 0.000800640000000 | 0.0392313599999990 | 0.0392316798718966 | 0.0400319999999990 |
| (3,6) | 0.515432074213 | 2.578437999443 | 2.579580633310 | 3.092592445280 |
| (3,60) | 0.00500154320988 | 0.295091049383 | 0.295091203318 | 0.300092592593 |

All lie between the two claimed bounds. A separate generator-based Poisson solve and matrix exponential gave

\[
\operatorname{var}_\pi S_s=2s\langle g,h\rangle_\pi
-2\langle h,(I-e^{sQ})h\rangle_\pi,\qquad -Qh=g,\quad\pi(h)=0,
\]

agreeing with the spectral values to absolute error below `1.6e-58`. This is numerical corroboration of an analytic identity, not a formally certified interval calculation. Simulated mean and variance of the entire V integral also passed their exact two-state moment diagnostics, within 2.22 estimated standard errors.

Command producing both tables and `probability_checks.json`:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 probability_checks.py
```

As a separate implementation check, `supplementary_checks.py` simulates actual four-state jumps at `(1,2)`: 200,000 runs gave 0.587285, SE 0.001100866, within 1.53 combined standard errors of the occupation sampler. It also checks the paper's `(2,8)` example: 1,000,000 occupation samples gave 0.884396, SE 0.000319749, agreeing with the stated 0.8844; the sharper analytic bound is 0.8017578125, rounding to 0.8018. Saved output: `supplementary_checks.json`.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 supplementary_checks.py
```

## Wording issues and typos noticed

No unequivocal mathematical typographical error was found. The following sentences or conventions merit clarification:

| Location | Text or issue | Suggested correction or qualification |
|---|---|---|
| Line 43 | A(u) is written with u^{-1}. | If t=0 is included, define A(0)=0 by continuity; otherwise state t>0. |
| Line 45 | K depends on the chain. | Say may depend on the chain and observable, or explain that standardization on a fixed finite chain allows a uniform choice over g. |
| Line 64 | due in this generality to Kipnis and Varadhan. | Specify their extension to general reversible processes; avoid suggesting they originated the elementary finite-state CLT. |
| Line 69 | sigma is of order s^{-2}. | Add for fixed b, as already specified at line 137. |
| Line 93 | all the rates are positive. | Say all specified coordinate jump rates; simultaneous changes have rate zero. |
| Line 137 | So the distance ... tends to 1/2. | Add the short concentration/CDF upper-bound argument recorded in the log. The conclusion is correct. |
| Line 137 | the variance ... is carried by the complement of H. | Say asymptotically carried; H has a small nonzero second-moment contribution. |
| Line 137 | on which |W_s| is of order s^{1/2}. | Specify typical conditional size or conditional RMS; it is not a pointwise bound for every path. |
| Line 141 | For sums of n independent copies ... bound Cbn^{-1/2}. | Explicitly identify the normalized sum n^{-1/2} sum U_i and distance to the standard normal. |
| Line 146 | Both pi Q=0 and pi^T exp(...) appear. | Specify row/column convention; if pi is a column, stationarity reads pi^T Q=0. |

## Attributions, novelty and limits of this audit

From memory, the broad AldousFill spectral statements are consistent with the mathematics derived here. I cannot confidently certify the exact numbers 4.29, 4.51 and 4.30 or the original open problem wording. The question quoted in the audit request is answered by the theorem, and no external proposition is needed for that proof.

I remember KipnisVaradhan's 1986 reversible-process additive-functional CLT with an inverse-generator/H_{-1} integrability condition (high confidence), and Bolthausen's Markov-functional BerryEsseen work (moderate/high confidence). Exact bibliography particulars were not checked. I recognize Lezaud's spectral concentration and BerryEsseen work (moderate confidence), but cannot certify the coefficient 26, Theorem 3.1, hypotheses or continuous-time exponential term. Its quoted shape is plausible and does not conflict with the example: at t=s its leading term is asymptotic to `(26/sqrt(2))sqrt(s)`, hence vacuous. This external inequality is not used to prove the negative answer.

I do not know a prior paper I can reliably name as settling this exact open problem. A slow rare-state switch combined with a fast fluctuating observable is a familiar rare-event obstruction to a uniform CLT. That familiarity does not establish that this particular result was already known, or that the four-state construction with b=1 is folklore. Novelty remains unverified; no references have been invented.

The authors' scripts, formal Lean proof, software versions and larger computation grids were not available here and were not checked. Nor were funding, affiliations, historical AI-work accounts, linked repositories or other nonmathematical declarations verified. The Monte Carlo probabilities have sampling error, and high-precision arithmetic here is not an interval proof. The analytic derivations, rather than these numerical checks, establish the theorem.

Task: refereeing a mathematical paper ... be a hard, independent referee  12 November 2026, 05:45 +04 (first recorded local audit clock).
