# Independent referee log

Task: referee `PAPER.tex`, as requested on 12 November 2026; audit began at 05:45 +04 (Asia/Tbilisi). Source line numbers below refer to the supplied, unmodified file.

Constraints: no browsing, no author programs, no other agents, no push, no writes outside this directory. The current task's restriction overrides standing requests to mutate the shared mesh, checklist or brain. Startup memory and compute status were read; no shared-state commands were run. All audit programs and their output will be saved here. Mathematical judgments are independent of the authors' computational claims. CORRECT means checked here; GAP identifies a missing qualification, argument or source verification; WRONG requires a false assertion. Bibliographic verification gaps are distinguished from gaps in the proof.

## 1. Introduction and main statement

**CORRECT  definitions and first display, lines 3740.** For a finite irreducible reversible chain, take an orthonormal basis of eigenvectors of `-Q` in `L(pi)`, and write `g = sum_{k>=2} a_k phi_k`, `sum a_k=1`. Put `d_k=a_k`. Stationarity and reversibility give

\[
C(u)=\operatorname{cov}_\pi(g(X_0),g(X_u))=\sum_{k\ge2}d_ke^{-\lambda_k|u|},
\]
\[
\operatorname{var}_\pi S_t=2\sum_{k\ge2}d_k\left(\frac t{\lambda_k}-\frac{1-e^{-\lambda_kt}}{\lambda_k^2}\right)
=t\sum_{k\ge2}\frac{2d_k}{\lambda_k}A(\lambda_kt).
\]

**CORRECT  Proposition 4.29 content quoted at lines 4144.** The preceding identity proves existence and `sigma=2 sum d_k/lambda_k >0`; it also proves `sigma<=2/lambda_2=2 tau_2`. For `u>0`, `0<A(u)<1` and `A'(u)=[1-(1+u)e^{-u}]/u>0`, so every `A(lambda_k t)` lies between `A(t/tau_2)` and 1. This proves both variance inequalities, including their relative, chain-uniform interpretation. At `t=0` use the continuous extension `A(0)=0`.

**CORRECT  fixed-chain CLT and O(t^{-1/2}) assertion, line 45, mathematical content.** Finite irreducible continuous-time chains with a nonzero centered observable have a nondegenerate additive-functional CLT; a fixed-chain BerryEsseen constant is consistent with this and with the later bound. This does not supply a uniform constant over the paper's family. **GAP  source numbering/quotation verification:** Proposition 4.51 and Proposition 4.29 cannot be certified from memory alone; no source text was consulted. This is a source-verification limitation, not a defect in the spectral derivation.

**CORRECT  [eq:op], lines 4549, as the problem stated in the audit request.** It uses the stationary chain, Kolmogorov distance and the asymptotic standard deviation `sigma sqrt(t)`. The quantifiers are: for fixed `b`, one function tends to zero and bounds every admissible chain and observable at every time. A chain depending on `s` is therefore an admissible refutation. No uniformity in `b` is needed: `b=1` alone suffices. **GAP  original wording:** exact fidelity to the unprovided AldousFill text and its numbering remains unverified.

**CORRECT  [thm:main], first display, lines 5155, conditional on the construction and proof checked below.** No parameter-independent chain is claimed. Small `s` may make the bound negative, which is harmless.

**CORRECT  [thm:main], second display and its proof, lines 5662.** For every deterministic `c>0`, `P(S_s/c<=0)=P(S_s<=0)`, and `D_K>=|P(S_s<=0)-1/2|>=P(S_s<=0)-1/2>=1/2-4/s`. This argument remains valid when the last lower bound is negative. In particular `c=sigma sqrt(s)>0`, and exact-standard-deviation normalization is positive too. It would not assert anything for `c=0`, or for negative `c`; neither is claimed.

**CORRECT  remaining deductions, line 62.** For fixed `b`, `liminf psi(b,s)>=1/2`. Since `1=pi(g)<=||g||_infty`, standardized functions have sup norm at least 1. The same four states suffice for all `s`, so adding state count to the proposed bound does not help. Prescribing a positive relaxation time follows by time change (checked in step 6).

**CORRECT  scope of the negative answer.** It settles exactly the stated continuous-time, stationary, Kolmogorov, chain-uniform question with dependence only on `(b,t/tau_2)` (also if state count is added). It does not refute a bound depending additionally on `sigma/tau_2`, stationary atom sizes, or the ratio of largest to smallest nonzero eigenvalue, or a fixed-chain-only limit. The proof as written is not a discrete-time construction. A different distance needs its own implication: distances that dominate Kolmogorov are also obstructed; even weak convergence to normal fails for these normalized laws (step 6), but no arbitrary unspecified distance is automatically covered.

## 2. Lezaud bound and two states

**CORRECT  plausibility and consistency of [eq:lezaud], lines 6469.** The expression has the correct time-scaling invariance and the familiar inverse spectral gap and inverse asymptotic standard deviation dependence of BerryEsseen estimates. Here `tau_2=1`, `sigma~2b/s` for fixed `b`, and at `t=s` its first term is asymptotic to `(26/sqrt(2))sqrt(s)`. The upper bound becomes vacuous, not contradictory to the lower bound approaching 1/2. For any one of these chains held fixed and `t->infinity`, it tends to zero as required.

**GAP  unverified external inequality, line 66:** A BerryEsseen inequality of Lezaud [Theorem 3.1] gives ... 26 .... The exact constant 26, hypotheses, continuous-time convention, theorem number and exponential term cannot be certified without the source, which this audit is forbidden to open. A believable shape and a consistency test do not verify a citation. The counterexample proof does not use this inequality.

**CORRECT  second form, line 67.** `sqrt(tau_2/sigma) (t/tau_2)^(-1/2)=tau_2/(sigma sqrt(t))`, using positive `tau_2,sigma,t`. A positive class-wide lower bound on `sigma/tau_2` gives the stated type of upper bound, if the cited inequality holds.

**CORRECT  two-state assertion, line 69.** With jump rates `a,c>0`, the only nonzero eigenvalue is `a+c`, and the centered subspace has dimension one. Thus every standardized observable has spectral weight 1 there and `sigma=2/(a+c)=2 tau_2`.

## 3. Construction and every part of [lem:chain]

**CORRECT  parameter and observable displays, lines 7381.** `epsilon=s^{-2}` is in `(0,1/4]`, `R=s^4>=16`, `1-b epsilon>=3/4`, so `alpha` is a well-defined positive real number. The displayed `g` takes the stated three values.

**CORRECT  (a), lines 85 and 93, all inequalities.** `alpha=(1-b epsilon)/(1-epsilon)>=1-b epsilon>=3/4`, and it is at most 1 because `b>=1`. Thus `alpha(1-epsilon)<=1` and `m>=b epsilon>0`. Also `b epsilon<=1/(2s)<=1/4`, while `alpha(1-epsilon)>3/5` since its stated lower bound is `3 sqrt(3)/8>3/5` (squaring reduces this to `27/64>9/25`). Hence `m<5/12<1/2`. All four one-coordinate jump rates are strictly positive, including at `b=1,s=2`. The zero rates for simultaneous coordinate changes are intended; all the rates are positive at line 93 should mean all specified one-coordinate rates.

**CORRECT  (b), lines 86 and 95.** Both displayed detailed balance identities hold. Each marginal mass is positive and sums to one; all four states communicate by changing one coordinate at a time. The independent product generator is `Q=Q_Y tensor I+I tensor Q_V`, hence the stated product measure is stationary and reversible.

**CORRECT  (c), lines 87 and 97, including the direct computation.** `Q_Y u(0)=epsilon=-u(0)` and `Q_Y u(1)=-(1-epsilon)=-u(1)`. At `v=1`, `Q_V w=-R(1+m)=-Rw(1)`; at `v=-1`, `Q_V w=R(1-m)=-Rw(-1)`. Since the two generator terms act on separate coordinates, `Q(uw)=w Q_Yu+u Q_Vw=-(R+1)uw`, and `Q1=0`. Both centered coordinate functions are nonconstant; their tensor products with constants give a basis of the four-dimensional function space. These are all eigenvalues, and `R>=16>1`, so `tau_2=1`.

**CORRECT  (d), lines 88 and 99, every equality.** Independence gives `pi(g)=-alpha(1-epsilon)m+b epsilon=0`. The two terms in `g` have disjoint support, so `pi(g)=alpha(1-epsilon)+b epsilon=1`. Because `alpha<=1<=b` and `Y=1` has positive mass, the supremum equals `b`, including `b=1`.

**CORRECT  independent exact checks completed.** Ran the saved program with

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 10 python3 exact_checks.py
```

The sandbox reported `nice: setpriority: Operation not permitted`; the computation nevertheless completed successfully in 4.95 seconds. Only one computation process and one numerical thread were used. SymPy 1.13.1 verified exact detailed balance, stationarity, row sums, the three eigenvector equations, independence of the basis, the full characteristic polynomial, both moments, sup norm, all parameter bounds, the expansion and Gram matrix in step 6. A separate exact Poisson-equation solve agreed with the spectral asymptotic variance. Outputs: `exact_checks.json`, `exact_matrices.txt`.

| (b,s) | alpha | m | spectrum of -Q | pi(g) | pi(g) | max abs(g) | detailed balance residual |
|---|---|---|---|---|---|---|---|
| (1,2) | 1 | 1/3 | 0,1,16,17 | 0 | 1 | 1 | 0, exact |
| (1,10) | 1 | 1/99 | 0,1,10000,10001 | 0 | 1 | 1 | 0, exact |
| (3,6) | 27/35 | sqrt(105)/105 | 0,1,1296,1297 | 0 | 1 | 3 | 0, exact |
| (5,100) | 3325/3333 | sqrt(443289)/1329867 | 0,1,100000000,100000001 | 0 | 1 | 5 | 0, exact |

## 4. Proof, line by line

**CORRECT  H, J and the implication on H, line 104.** Starting from the product stationary law makes the complete coordinate paths independent. On the event of no `Y=1` occupation, `S_s=alpha J`; `alpha>0` preserves the sign.

**CORRECT  [eq:split], lines 105107, both inequalities.** `H intersect {J<=0}` is a subset of `{S_s<=0}`. For arbitrary events `H,B`, `P(H intersect B)>=P(H)-P(B^c)`, so the second inequality does not require independence. Independence of `H` (a Y-path event) and `J` (a V-path functional) also holds and would give the stronger product bound `P(H)P(J<=0)`. There is no misuse of independence.

**CORRECT  probability of H and both lower bounds, line 108.** The starting probability is `1-epsilon` and the holding time in state 0 is exponential of rate `epsilon`, giving `(1-epsilon)e^{-epsilon s}`. Apply `e^{-x}>=1-x` and then expand `(1-epsilon)(1-epsilon s)=1-epsilon(1+s)+epsilons`.

**CORRECT  mean and covariance, line 108.** Stationarity gives `E J=-ms`. The centered variable `V+m` has stationary variance `1-m` and transition semigroup decay `e^{-Ru}`. Thus the covariance is `(1-m)e^{-R|u|}` (negative lags are understood by a stationary extension, or only `u>=0` is needed).

**CORRECT  variance display, lines 109111.** Integrating the stationary covariance over the square `[0,s]` gives the displayed integral. Its exact value is `2(1-m)[s/R-(1-e^{-Rs})/R]`, which is bounded above by `2(1-m)s/R`.

**CORRECT  Chebyshev display, lines 112115.** `J>0` iff `J-EJ>ms`, with `ms>0`. The one-sided event lies in the two-sided Chebyshev event, so the variance bound divided by `ms` is valid; no assumption on a density is needed.

**CORRECT  line 116, both chains of inequalities.** `R ms>=s^4 bs^{-4}s=bs>=s`, so the preceding probability is at most `2/s`. Also `epsilon(1+s)=1/s+1/s<=3/(2s)` for `s>=2`.

**CORRECT  final display and conclusion, lines 117120.** The lower bound is actually `1-7/(2s)`, and weakening it to `1-4/s` is valid. Together with the lemma this proves all of [thm:main], without reliance on any external normal-approximation theorem or author software.

## 5. Independent probabilities and finite-time variances

**CORRECT  numerical test of the theorem.** Used simulation, **1,000,000 independent runs per pair**, with NumPy's seeded default generator. This samples the exact continuous-time occupation law, not a time discretization and not a Gaussian approximation. Saved program: `probability_checks.py`; output: `probability_checks.json`.

Sampling justification: represent V by rate-R refreshes with sign +1 drawn with probability `p=(1-m)/2`; null refreshes are allowed. This has exactly the specified off-diagonal rates. Conditional on a Y-constant interval of length L and `N~Poisson(R L)`, the `N+1` spacings divided by L are Dirichlet(1,...,1). For `N>=1`, sample the terminal sign, and sample the count of positive interior signs as `Binomial(N-1,p)`. Including the known initial sign and sampled terminal sign gives K positive spacings, whose total fraction is `Beta(K,N+1-K)`, with degenerate cases 0 and 1 handled explicitly. This jointly samples the integral and endpoint, preserving dependence across successive Y intervals. Y itself is sampled by exponential holding times, with its stationary initial state independent of V. Cost does not grow with the number of fast jumps.

Command:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 probability_checks.py
```

| (b,s) | nonpositive / runs | estimated P(S_s<=0) | binomial SE | 1-4/s |
|---|---|---|---|---|
| (1,2) | 589126 / 1000000 | 0.589126 | 0.000491992 | -1.000000 |
| (1,10) | 895411 / 1000000 | 0.895411 | 0.000306023 | 0.600000 |
| (1,50) | 980372 / 1000000 | 0.980372 | 0.000138718 | 0.920000 |
| (3,6) | 850520 / 1000000 | 0.850520 | 0.000356561 | 0.333333 |
| (3,60) | 983301 / 1000000 | 0.983301 | 0.000128141 | 0.933333 |

All are consistent with the claimed bound; the small-s bounds are loose or vacuous. Seeds are `43020261112` through `43020261116` in table order. These are Monte Carlo estimates with the stated standard errors, not rigorous probability enclosures.

**CORRECT  exact spectral variance formula and comparison.** Define the following rational weights, with `a2=(1-b epsilon)/(1-epsilon)` and `a2m2=b epsilon/(1-epsilon)`:

\[
d_1=\frac{b^2\varepsilon}{1-\varepsilon},\quad
d_R=(a2-a2m2)(1-\varepsilon)^2,\quad
d_{R+1}=(a2-a2m2)\varepsilon(1-\varepsilon).
\]

They sum to 1. The exact expression is

\[
\operatorname{var}_\pi S_s=2\sum_{\lambda\in\{1,R,R+1\}}d_\lambda
\left[\frac{s}{\lambda}-\frac{1-e^{-\lambda s}}{\lambda^2}\right],
\qquad \sigma^2=2\sum_\lambda\frac{d_\lambda}{\lambda}.
\]

The table evaluates these exact expressions at 60-decimal working precision (rounded below). No statistical estimate is used for these variances.

| (b,s) | sigma | A(s) s sigma | var_pi S_s | s sigma |
|---|---|---|---|---|
| (1,2) | 0.748774509804 | 0.850110120169 | 0.916046222561 | 1.497549019608 |
| (1,10) | 0.0203999998020 | 0.183600924377 | 0.183798875191 | 0.203999998020 |
| (1,50) | 0.000800640000000 | 0.0392313599999990 | 0.0392316798718966 | 0.0400319999999990 |
| (3,6) | 0.515432074213 | 2.578437999443 | 2.579580633310 | 3.092592445280 |
| (3,60) | 0.00500154320988 | 0.295091049383 | 0.295091203318 | 0.300092592593 |

**CORRECT  independent audit of the numerics.** Built the actual generator again with mpmath, solved `-Qh=g`, `pi(h)=0`, and evaluated the separate identity `var S_s=2s<g,h>_pi-2<h,(I-exp(sQ))h>_pi`. It agrees with the spectral formula to absolute error below `1.6e-58` at all five pairs; the Poisson asymptotic variances also agree. As a simulator diagnostic, the full integral J was collected independently of Y occupation: its empirical mean and variance agree with their known two-state values, all within 2.22 estimated standard errors. Runtime was 1.34 seconds total; reported peak RSS 552,566,784 bytes (under 1 GB), one numerical thread, no child workers. Versions: NumPy 2.2.3, mpmath 1.3.0. This completes step 5 before consideration of the remarks.

## 6. Remarks

**CORRECT  [rem:scale], line 125, every transformation.** For `X^kappa_t=X_{kappa t}`, the generator and eigenvalues multiply by `kappa`, so the relaxation time divides by `kappa`. Change variables in the path integral to obtain `S^kappa_t=S_{kappa t}/kappa`; hence its variance rate is `sigma/kappa`, and the displayed normalized variables agree. Also `t/(tau_2/kappa)=kappa t/tau_2`. Taking `kappa=1/T` in a chain with initial `tau_2=1` prescribes any `T>0`, and observing at `t=sT` transfers the probability bound. In particular divide rates by `R` (`kappa=1/R`): `tau_2=R=s^4` and `t=Rs=s^5`. The Y rates are at most `1/R`, and the V rates become `(1m)/2<3/4`; thus all off-diagonal rates are at most 1. No upper-rate normalization rescues the proposed bound.

**CORRECT  [rem:sigma], expansion display, lines 129132.** Expand the right side:

`(b+alpha m)(y-epsilon)+alpha(1-epsilon)(v+m)-alpha(y-epsilon)(v+m)`

`=by+alpha(1-y)v + alpha m(1-epsilon)-b epsilon =g(y,v)`.

The last two terms cancel by definition of m. This is a pointwise identity at all four states, also checked exactly in `exact_checks.py`.

**CORRECT  orthogonality and all three norms, line 133.** `E u=E w=0`; independence gives `<u,w>=0`, `<u,uw>=E u E w=0`, and `<w,uw>=E u E w=0`. `E u=epsilon(1-epsilon)`, `E w=E(V+m)=1-m`, and `E(uw)` is the product of these positive norms. The spectral variance formula is exactly the one derived in step 1; it does not need an external citation for this finite chain.

**CORRECT  sigma display, lines 134136.** The squared coefficients times these norms, divided by `1,R,R+1` and multiplied by 2, give precisely the display. An exact Poisson solve agreed at all four symbolic test pairs. In particular `b+alpha m=b/(1-epsilon)` and the slow contribution is `2b epsilon/(1-epsilon)`; the other contributions are nonnegative and at most `2/R` because their spectral weights sum to at most 1.

**CORRECT  limit in line 137 for fixed b.** Multiplying by `s` gives `2b/(1-s^{-2})+O(s^{-2})`, hence the limit is `2b`; `sigma~sqrt(2)b/s`. **GAP  qualification in line 69:** In the chains of Theorem ... sigma is of order s^{-2} ... should say for fixed b. It is correct under the limit explicitly specified in the referenced remark, but not uniformly over the full two-parameter family: if `b=s/2`, its slow contribution tends to `1/2`. This is a wording issue, not a failure of the theorem.

**CORRECT  1-8/s probability and bound on S_s, line 137.** Let `E={|J+ms|<=ms/2}`. Chebyshev gives `P(E^c)<=4 var(J)/(ms)<=8(1-m)/(R ms)<=8/s`. On `E intersect H`, `-3ms/2<=J<=-ms/2`, so `|S_s|<=3alpha ms/2`. The stated `1-8/s` is the probability of E, not of `E intersect H`; the source makes this distinction correctly. The intersection has probability at least `1-8/s-epsilon(1+s)>=1-19/(2s)`.

**CORRECT  normalization identity and rate, line 137.** Because `alpha m=b/[s(1-epsilon)]`,

\[
\frac{\alpha ms}{\sigma\sqrt{s}}=\frac{b}{(1-\varepsilon)\sigma s^{3/2}}
\sim\frac1{\sqrt{2s}}.
\]

For fixed b this proves `W_s->0` in probability with the explicit consequence

\[
P\left(|W_s|>\frac{3b}{2(1-\varepsilon)\sigma s^{3/2}}\right)\le\frac{19}{2s}.
\]

The threshold is `O(s^{-1/2})`. These are triangular-family statements: W_s belongs to a different chain for each s. They are not a violation of a fixed-chain CLT.

**CORRECT  distance tends to 1/2, line 137; an omitted elementary argument can be supplied.** The theorem gives the liminf. For any `delta>0`, outside `[-delta,delta]` the distribution function of W_s is within its tail probability of 0 or 1, and inside that interval its distance from Phi is at most `Phi(delta)`. Consequently `D_K(W_s,Z)<=Phi(delta)+P(|W_s|>delta)`. First take `s->infinity`, then `delta->0`, to give limsup at most 1/2. Convergence in probability to a point mass alone must not be confused with convergence of CDFs at that atom, but the displayed bound avoids that issue.

**CORRECT  second moment and location of variance, last sentence of line 137, in the asymptotic sense.** The upper bound `E W_s<=1` from step 1 supplements the stated lower bound `A(s)->1`, so `E W_s->1`. Independence gives the exact identity

\[
E[W_s^2\mathbf1_H]=P(H)\frac{\alpha^2\{\operatorname{var}(J)+m^2s^2\}}{s\sigma^2}
\sim\frac1{2s}\longrightarrow0.
\]

Thus `E[W_s 1_{H^c}]->1`, and `P(H^c)~1/s`. This proves the claimed concentration of second moment, including its magnitude: the conditional RMS on `H^c` is asymptotic to `sqrt(s)`. A stronger distributional reading is also justified: conditional on `H^c`, with probability tending to one there is one entry into Y=1 from an initially zero state, with its holding time converging to Exp(1) and no terminal truncation. Therefore `W_s/sqrt(s)` conditional on `H^c` tends to `Exp(1)/sqrt(2)`. The phrase of order s^{1/2} describes a typical conditional size, not a uniform bound on every path. H still makes the small nonzero second-moment contribution displayed above. Recommend writing asymptotically carried for precision.

**CORRECT  final unnumbered remark, line 141.** The drift on Y=0 is `-alpha m`, the stationary rare positive contributions restore zero mean, and `P(H)=1-O(1/s)`. Conditional on H, Chebyshev shows negativity with probability `1-O(1/s)`. For a centered, variance-one random variable U with `|U|<=b`, `E|U|<=b E U=b`; the iid BerryEsseen bound for `n^{-1/2} sum U_i` is therefore `Cb/sqrt(n)`. The sum's normalization is implicit and should be made explicit. The lower-variance obstruction follows from the construction itself; the sufficient-condition claim additionally depends on the unverified Lezaud citation.

## 7. Attributions and novelty (memory only)

**CORRECT  remembered broad content, with confidence limits.** I recognize the AldousFill monograph and the spectral covariance/variance treatment of reversible additive functionals. The quoted Proposition 4.29 content is proved independently above (high confidence in the mathematics; low confidence in the proposition number from memory). A fixed-chain BerryEsseen statement of the type attributed to Proposition 4.51 is plausible and mathematically standard (high confidence in the broad content; low confidence in that exact number). I do not independently remember the precise wording or number of Open Problem 4.30; this report tests the problem as supplied in the audit request.

**CORRECT  KipnisVaradhan attribution at the level of broad content.** I remember their 1986 reversible-process additive-functional CLT, including the finite `H_{-1}`/inverse-generator condition and applications to exclusion (high confidence). All centered observables on the present finite irreducible chains satisfy that condition. **GAP  phrase at line 64:** due in this generality to Kipnis and Varadhan is historically imprecise if it refers only to finite irreducible chains: their important extension is to general reversible processes, while the finite-state CLT predates them. Suggested wording: For the general reversible-process setting, see Kipnis and Varadhan. No mathematical step here requires their theorem.

**CORRECT  Bolthausen attribution at the broad level.** I remember Bolthausen's work on BerryEsseen bounds for Markov-chain functionals (moderate/high confidence), including a discrete-chain context, consistent with the cited title. I cannot certify year, volume, pages or exact hypotheses from memory.

**GAP  Lezaud theorem and bibliographic particulars.** I recognize Lezaud's spectral-method concentration/BerryEsseen work (moderate confidence); exact coefficient, theorem number and continuous-time formula remain unverified as recorded in step 2. Likewise the bibliography's precise journal/page/title details have not been independently checked. No references are invented to fill this gap.

**GAP  novelty cannot be established from memory.** I do not know a paper that I can reliably name as already resolving this exact AldousFill problem. The mechanism is familiar: an observable with tiny projection onto a slow rare-state mode and most of its instantaneous variance in a fast mode can have an asymptotic variance set by rare excursions, giving poor uniform Gaussian approximation. This resembles standard rare-event triangular-array failures of a uniform CLT and a slow switch coupled to a fast background. Familiarity of the mechanism is not evidence of a published solution or of folklore status of this exact four-state example, particularly at `b=1`. I cannot certify priority, nor identify a prior answer, from memory. No outside search was performed.

## Final supplementary audit and disposition

After steps 17, ran `supplementary_checks.py` with the same one-thread environment as step 5. A conventional simulation of every actual four-state jump at `(b,s)=(1,2)`, using 200,000 runs and a different seed, gave `P(S_s<=0)=0.587285`, SE `0.001100866`. It differs from the occupation sampler by 1.53 combined standard errors. This independently tests the unusual occupation-sampling implementation. The same program also checked the paper's line-146 example `(b,s)=(2,8)` with 1,000,000 occupation-law samples: `0.884396`, SE `0.000319749`, consistent with the paper's Fourier value `0.8844` and its lower-precision simulation `0.8894 +/- 0.0044`. The analytic proof bound is `0.8017578125`, agreeing with `0.8018`. Total supplemental runtime 0.36 seconds, peak RSS 319,602,688 bytes. Outputs saved in `supplementary_checks.json`.

**CORRECT  characteristic function at line 146.** With the stationary distribution represented as a column vector and `G=diag(g)`, the finite-state FeynmanKac formula is `pi^T exp(s(Q+i theta G)) 1`. **GAP  author verification claims, line 146:** the cited scripts, Lean file, Lean version, grids and claimed symbolic verification were not available in this folder and were not opened elsewhere. The independent work here does not verify their existence or execution. A minor row/column convention ambiguity remains between `pi Q=0` and `pi^T exp(...)`; fix by specifying the convention.

**Overall mathematical verdict: SOUND.** No gap or error was found in [thm:main], [lem:chain], or the elementary proof. The claims in the remarks follow with the qualifications above. The negative answer is valid for the question as supplied. The exact external quotations, Lezaud inequality, novelty, author software/formalization and nonmathematical declarations remain unverified; none is an input needed for the counterexample proof. `REPORT.md` collects the verdicts, numerical tables, commands, wording issues and limitations.
