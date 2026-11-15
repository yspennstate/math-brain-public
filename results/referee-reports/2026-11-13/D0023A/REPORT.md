PARTIAL

# D0023: concentration at slow sites in the disordered zero-range process

2026-11-13. The result proved here concerns the stationary distribution on growing finite rings. The original infinite-system dynamic problem is not resolved by this report. No novelty is claimed for stationary condensation.

The source is Timo Seppäläinen, *Recent results and open problems on the hydrodynamics of disordered asymmetric exclusion and zero-range processes* (1999), Section 4, Problem 2, arXiv:math/9906194, PDF p. 9. Its target is the development of spatial concentration below the hydrodynamic scale from supercritical initial data. Problem 3 on the same page separately asks about local weak convergence to the critical invariant measure. These are different questions.

The original phrase is “the particles concentrate on exceptionally slow sites.” The full source, including the surrounding wording and page delimiters, is saved in [sources/disordered_asep_open_1999.txt](sources/disordered_asep_open_1999.txt).

The inspected sources establish substantial progress: critical local convergence, hydrodynamics above critical density, local dynamic loss of mass, and annealed time-scale bounds for the exclusion representation. A stationary finite-ring statement is proved below. Neither stationary localization nor local weak convergence alone gives a joint space-time law of the developing condensates in the infinite system.

## A precise tractable statement

Fix 0<c<1, put s=1-c, and let kappa>1. On a directed ring of L sites let

    alpha_i = c+s Y_i,    P(Y_i <= y)=y^kappa,  0<=y<=1,

independently. A nonempty site i sends one particle to i+1 modulo L at total rate alpha_i, independent of its occupancy: g(n)=1 for n>=1, g(0)=0. There are N_L particles, where N_L/L -> rho. Define

    rho_c = E[c/(alpha-c)] = c kappa / [s(kappa-1)].

Assume rho>rho_c. Let I_L be the unique minimum-rate site. First sample the rates, then sample eta from the stationary distribution pi_(L,N_L)^alpha for those rates. All the following probability limits refer to this joint law, not to an assertion for almost every fixed infinite environment.

**Theorem A (finite-ring concentration).** As L->infinity,

    eta_(I_L)/L -> rho-rho_c,
    (1/L) sum_(i != I_L) eta_i -> rho_c,
    (1/L) max_(i != I_L) eta_i -> 0

in probability. In particular, for each fixed integer k>=1, the mass outside the k slowest sites is rho_c L+o_P(L).

More explicitly, take any 0<gamma<1/kappa and set

    S_L = {i: alpha_i-c <= s L^(-gamma)}.

Then

    |S_L| / L^(1-kappa gamma) -> 1,
    (1/L) sum_(i in S_L) eta_i -> rho-rho_c,
    (1/L) sum_(i not in S_L) eta_i -> rho_c.

For gamma=1/(2 kappa), this identifies a set of order sqrt(L) sites with vanishing rate tolerance s L^(-1/(2 kappa)); all its mass except o_P(L) is at its slowest site. This is stronger than an O(L) bound for the bulk.

The rate and position of the condensate obey

    L^(1/kappa) (alpha_(1)-c)/s => W,
    P(W>z)=exp(-z^kappa),   z>=0,
    I_L/L => Uniform[0,1],

and the index of the minimum is independent of the ordered rate values at each L. More generally, for fixed j, the j smallest rescaled rate gaps converge jointly to Gamma_j^(1/kappa), where Gamma_j is the sum of j independent mean-one exponential variables. Their positions converge to independent uniform positions, independent of these limiting ordered values.

For continuous test functions on the unit circle, the stationary empirical mass measure consequently converges in distribution to

    rho_c du + (rho-rho_c) delta_U,

where U is uniform on the circle. This statement gives a location, a mass, a vanishing rate tolerance, and extremal rate statistics in an explicitly specified limit.

## Proof of Theorem A

All constants C below may depend on c and kappa, but not on L. Occupations in geometric laws start at zero.

### 1. Exact stationary measure and an exact bulk representation

The chain is irreducible on the finite set of nonnegative integer vectors with total N. Its stationary distribution is

    pi^alpha(eta) = (1/Z) product_i alpha_i^(-eta_i),    sum eta_i=N.       (1)

To verify stationarity directly, fix eta. For an incoming transition along i->i+1, its predecessor is eta+e_i-e_(i+1), which exists exactly when eta_(i+1)>0. Its weight divided by the weight of eta is alpha_(i+1)/alpha_i. Multiplying by its outgoing rate alpha_i gives incoming flow pi(eta) alpha_(i+1). Summing over i gives pi(eta) sum_j alpha_j 1_{eta_j>0}, exactly the total outgoing flow. Irreducibility follows by moving particles clockwise to redistribute any given total among the sites. Finite irreducibility gives uniqueness and convergence to (1) from any initial state as time tends to infinity.

Write M=min_i Y_i and a=c+s M=alpha_(I_L). Conditional on the rates, let independent variables X_i, i!=I_L, have laws

    Q^alpha(X_i=n)=(1-a/alpha_i)(a/alpha_i)^n,
    mu_i=E_Q X_i = a/(alpha_i-a),
    Var_Q X_i=mu_i(1+mu_i).

Let B=sum_(i!=I_L) X_i. Under (1), the law of (eta_i:i!=I_L) is exactly

    Q^alpha( (X_i) in . | B<=N),       eta_(I_L)=N-B.                    (2)

Indeed its unnormalized weight is a^(-N) product_(i!=I_L)(a/alpha_i)^(X_i), with the sole restriction B<=N. The factors normalizing the geometric laws do not depend on X. No approximation of a canonical ensemble by a grand-canonical ensemble is being assumed.

### 2. A high-probability event controlling the smallest rate gap

Set

    a0 = (1/kappa + 1/(2 kappa-1))/2,
    b0 = (1+a0)/2,
    h  = (kappa-1)/(4 kappa),
    r=L^(-a0),   d=L^(-b0).

These numbers satisfy

    0<a0<1/kappa<1,   a0<b0<1,
    a0 kappa-b0=h,    1-b0-a0(kappa-1)=-h.

Let G_L be the event M<=r and Y_(2)-M>=d. Then

    P(G_L^c) <= exp(-L r^kappa) + C L d r^(kappa-1)
             <= exp(-L^(1-a0 kappa)) + C L^(-h).                        (3)

For the first term, P(M>r)=(1-r^kappa)^L. Conditional on the minimum value m<=r and its index, the other L-1 samples are independent with the law of Y conditioned on Y>m. For all sufficiently large L, d<r, and the probability that any one of them lies in (m,m+d) is at most

    [(m+d)^kappa-m^kappa]/[1-m^kappa] <= C d r^(kappa-1).

A union bound proves (3). Conditioning on an exact minimum value is understood through its density, so no positive-probability atom is needed.

### 3. The very slow nonminimum sites carry negligible bulk mass

On G_L, for every i!=I_L with Y_i<=2r we have mu_i<=C/d. Consequently, under the joint law of the environment and the unconditioned variables X,

    E[1_(G_L) (1/L) sum_(i!=I_L,Y_i<=2r) X_i]
        <= C d^(-1) P(Y<=2r)
        <= C L^(b0-a0 kappa) = C L^(-h).                               (4)

Together with (3) and Markov's inequality, this proves that this part of the bulk divided by L tends to zero in probability. In particular its maximum divided by L tends to zero. The estimate avoids the generally infinite annealed expectation of 1/(Y_(2)-Y_(1)); near-ties cannot be ignored when making this argument.

### 4. The other sites have the critical mean and negligible fluctuations

On {M<=r}, for Y_i>2r,

    mu_i = (c/s+M)/(Y_i-M),
    0 <= mu_i-c/(s Y_i) <= C r/Y_i^2,
    Var_Q X_i <= C/Y_i^2.                                              (5)

Put H(r)=E[Y^(-2) 1_{Y>2r}]. Direct integration of the density kappa y^(kappa-1) shows

    H(r) = O(r^(kappa-2)) if 1<kappa<2,
           O(log(1/r))    if kappa=2,
           O(1)          if kappa>2.

In every case r H(r)->0 and H(r)/L->0 for the chosen a0. Taking expectations in (5) and using Markov's inequality shows that the normalized sum of mean differences tends to zero. Conditional Chebyshev and (5) give, for each epsilon>0,

    P(M<=r, |sum_(Y_i>2r)(X_i-mu_i)|>epsilon L)
        <= C H(r)/(epsilon^2 L) ->0.                                  (6)

The truncated critical variables [c/(s Y_i)] 1_{Y_i>2r} have variance at most C H(r), and their expectation differs from rho_c by C r^(kappa-1). An ordinary Chebyshev bound therefore controls their sample mean. Thus (3)--(6) imply

    B/L -> rho_c                                                     (7)

under the joint environment/Q law.

Combining these estimates also gives an explicit bound: for every epsilon>0 and all sufficiently large L,

    P_Q(|B/L-rho_c|>epsilon)
      <= C exp(-L^(1-a0 kappa))
         + C(1+epsilon^(-1)) L^(-h)
         + C epsilon^(-1) [r H(r)+r^(kappa-1)]
         + C epsilon^(-2) H(r)/L.                                    (7a)

Here P_Q includes the random environment. To obtain (7a), allocate epsilon/3 each to the slow sum (4), the mean correction in (5), and the fluctuation plus truncated-mean error in (6); adjusting fixed numerical constants gives the displayed C. The deterministic truncated-mean bias is bounded using 1_{bias>epsilon/constant}<=constant*bias/epsilon. Every term tends to zero for each fixed epsilon. Equation (9) below transfers this quantitative bound to canonical bulk deviations, with one additional copy evaluated at any fixed number below rho-rho_c.

For a maximum bound, on {M<=r}, Y_i>2r implies

    1-a/alpha_i = s(Y_i-M)/alpha_i >= s r.

The geometric tail and a union bound give

    P(M<=r, max_(Y_i>2r) X_i>epsilon L)
        <= L exp(-s r floor(epsilon L)) ->0.                          (8)

Together with (3)--(4), this proves max_(i!=I_L) X_i/L->0.

### 5. Conditioning transfers the results to the canonical law

Since N_L/L->rho>rho_c, (7) implies E_environment Q^alpha(B>N_L)->0. Let p_alpha=Q^alpha(B<=N_L). The environment probability of p_alpha<1/2 is at most 2 E Q^alpha(B>N_L). For any bulk event A_L whose joint Q probability tends to zero, (2) therefore gives

    E_environment pi^alpha(A_L)
        <= 2 E_environment Q^alpha(A_L)
           +2 E_environment Q^alpha(B>N_L) ->0.                       (9)

This argument conditions separately for each environment; it does not inadvertently reweight the environment distribution by its acceptance probability. Applying (9) to (7)--(8), and using eta_(I_L)=N_L-B, proves all three principal limits. The fixed-k assertion follows since the other k-1 chosen sites have mass at most (k-1) times the maximum in (8) and (4).

### 6. Shrinking slow sets, rate statistics, and spatial mass

For the asserted S_L, its size is binomial with mean L^(1-kappa gamma)->infinity and relative variance at most L^(-(1-kappa gamma)), proving its size limit. Also

    P(I_L not in S_L) = (1-L^(-kappa gamma))^L ->0.

The nonminimum mass in S_L is negligible under Q as follows. The part Y_i<=2r is handled by (3)--(4). On M<=r, for 2r<Y_i<=L^(-gamma), mu_i<=C/Y_i, so its expected mass divided by L is at most C L^(-gamma(kappa-1)). If the upper endpoint is below 2r this second part is empty. Markov's inequality and (9) finish the slow-set assertions.

For the minimum,

    P(L^(1/kappa) M>z)=(1-z^kappa/L)^L -> exp(-z^kappa).

The variables Y_i^kappa are uniform. Counts in finitely many disjoint intervals of size proportional to 1/L near zero converge jointly to independent Poisson counts, by the multinomial generating function

    [1 + sum_j (length_j/L)(z_j-1)]^L
        -> exp(sum_j length_j (z_j-1)).

This proves the claimed joint ordered-value limit, since the ordered arrival times of a rate-one Poisson process are the Gamma_j. Exchangeability and the continuous rate law make the permutation of the sample labels uniform and independent of the ordered values. Sampling a fixed number of labels without replacement from L sites converges after division by L to independent uniforms, giving the joint position statement.

Finally, (4)--(6) hold with every summand multiplied by any uniformly bounded deterministic weight f(i/L), using the same absolute mean bounds and conditional variance bound multiplied by ||f||_infinity^2. The weighted law of large numbers for the critical means follows by truncating c/(sY_i) at a fixed level, applying the variance bound to the bounded independent variables, and then using integrability to remove the truncation. For continuous f the deterministic Riemann sum tends to integral f(u)du. Thus the background mass against f converges to rho_c integral f. The minimum contributes (rho-rho_c) f(I_L/L). Applying the preceding label limit gives the empirical-measure assertion. This completes the proof.

### What time limit this proves

For each fixed L,N and environment, finite-state irreducibility proved above gives convergence to pi^alpha from uniform or any other initial data. Theorem A therefore also holds with the **iterated limit** t->infinity first, then L->infinity. There is no bound here on the mixing time that is uniform in L or in the smallest rate gap. In particular, Theorem A does not prove a concentration law in a window L(t) for the original infinite process at a specified time t.

For completeness, the finite-state convergence used here can be obtained without an unproved mixing assertion. Fix a positive observation time. From every state there is a finite sequence of allowed transitions to every other state, and the probability of executing that sequence within the time interval, with no further transitions, is positive. Thus the transition matrix at that time has all entries positive. Its smallest entry gives a positive common minorization, hence a strict contraction in total variation. Iteration proves convergence; the minorization can depend arbitrarily badly on L,N,alpha.

## The dynamic gap

For g=1 and iid rates with P(alpha-c<=epsilon) asymptotic to K epsilon^kappa, the finite critical density requires kappa>1. A region of length ell typically has its best rate within order ell^(-1/kappa) of c, and the two smallest rates have a gap on that order in probability, with substantial fluctuations. Its supercritical mass is of order (rho-rho_c)ell. Balancing that mass with a current difference of order ell^(-1/kappa) suggests

    time ~ ell^(1+1/kappa),
    ell(t) ~ t^(kappa/(kappa+1)),
    condensate mass ~ t^(kappa/(kappa+1)),
    condensate rate-c ~ t^(-1/(kappa+1)).

This balance is a heuristic, consistent with Krug's scaling discussion and Jain–Barma's growth analysis; it is not part of Theorem A. The rate gap has no deterministic lower bound on its typical scale. Very close competitors can retain substantial masses for much longer than the typical scale suggests. [Krug's review](https://arxiv.org/abs/cond-mat/9912411), [Jain–Barma](https://arxiv.org/abs/cond-mat/0305098).

On the infinite line there is almost surely no globally slowest site when the infimum c is unattained. For rightward jumps, an upstream slow site restricts the current available downstream. A statement based solely on the k smallest rates in an arbitrary centered window ignores inflow from outside that window. A satisfactory dynamic theorem would specify an initial law (for example iid occupations of supercritical mean and finite variance, independent of the rates), the observation frame and boundary influence, and a rescaled random measure of location, rate, and queue mass. One would want tightness, identification of its limit, and a proof that it accounts for the excess mass. The stationary point-process description in Theorem A supplies none of the missing time control.

Density alone also does not rule out preexisting mesoscopic piles. There is an elementary persistence bound: at site x,

    eta_x(t) >= eta_x(0)-P_x(t),

where P_x is its rate-alpha_x Poisson process of attempted services. Arrivals only increase the left-hand side, and at most one particle departs at each attempt. Thus, for t>=0,

    P(eta_x(t) >= eta_x(0)-2t) >= 1-exp[-(2 log 2-1)t]

when alpha_x<=1. This follows from E[2^(P_x(t))]=exp(alpha_x t)<=exp(t) and Markov's inequality for P_x(t)>2t. Large initial piles at fast sites can therefore persist. This is one reason a uniform theorem over all initial states with a prescribed asymptotic density needs more careful formulation than the iid-initial-state picture.

## What was checked and how

The proof was audited for the main failure points: the geometric law starts at zero; the minimum site is omitted before setting the fugacity to its rate; conditioning is performed for each fixed environment; and the near-tie inverse gap is truncated on a high-probability event rather than assigned a finite annealed expectation. The explicit exponents satisfy a0 kappa-b0=h and 1-b0-a0(kappa-1)=-h. Both the mean correction r H(r) and the variance bound H(r)/L vanish throughout kappa>1.

The formula for rho_c follows both by integrating the rate density and by setting Y=U^(1/kappa) and integrating c/(s U^(1/kappa)). The canonical weights and the conditioned geometric representation were checked independently by enumerating all 15 states of a three-site, four-particle ring with rates (0.3,0.55,0.9). The maximum balance residual was 2.78e-17; the two probability formulas differed by at most 5.56e-17. These numerical checks support implementation and algebra; the proof above does not depend on them.

### Exact continuous-time simulation

[code/tazrp.cpp](code/tazrp.cpp) uses Poisson uniformization. In an interval of length Delta, it draws a Poisson(L Delta) number of proposals, chooses a site uniformly for each proposal, and moves a particle if the site is occupied and a fresh uniform number is below alpha_i. Thinning gives exactly the required transition rates alpha_i 1_{eta_i>0}. Independent proposal counts in successive intervals give the exact joint law at the observation times; there is no time-discretization step.

The experiment uses c=0.3, kappa=1.5,2,3, L=128,384, six independent environments for each pair, and N=round((rho_c+2)L). The initial configuration is

    eta_i(0)=floor((i+1)N/L)-floor(iN/L),   0<=i<L.

Its discrepancy from a constant-density profile is at most one particle on every interval. The times are tau L^(1+1/kappa), with tau=0,.005,.01,.02,.05,.1,.2,.5,1,2,4. This uses a candidate coarsening scale to organize the observations; it does not estimate that exponent from the data.

There are 396 full snapshots, 298,460,791 attempted services and 98,687,121 successful moves across the 36 trajectories. Mass and nonnegativity hold at every snapshot. The Python analysis independently recomputed masses at the slowest, five slowest, and ten slowest sites from the saved raw rates and occupations. All checks passed. Full data are in [data/dynamics.csv](data/dynamics.csv), [data/rates.csv](data/rates.csv), and [data/states.jsonl](data/states.jsonl).

At the final observation tau=4:

| kappa | L | Mean mass at slowest / ((rho-rho_c)L) | Largest pile at slowest | Largest pile among 5 slowest |
|---:|---:|---:|---:|---:|
| 1.5 | 128 | 0.619 | 4/6 | 6/6 |
| 1.5 | 384 | 0.864 | 6/6 | 6/6 |
| 2 | 128 | 0.647 | 4/6 | 6/6 |
| 2 | 384 | 0.471 | 4/6 | 6/6 |
| 3 | 128 | 0.640 | 6/6 | 6/6 |
| 3 | 384 | 0.557 | 6/6 | 6/6 |

The denominator in the actual computation is N-rho_c L, so the rounding of N is accounted for exactly. The numerator is the raw occupancy at the slowest site, including its background particles. At these sizes and times substantial mass can remain at other sites. The largest pile is strongly associated with low rate rank, but the single-site excess fraction does not increase monotonically with L in this small sample. These observations establish neither equilibrium nor a dynamic scaling limit.

The CSV also tracks the mass on alpha_i-c<=s L^(-1/(2 kappa)) and a signed estimate of excess there, obtained by subtracting sum c/(alpha_i-c) over that set. This finite-sample critical baseline can be large; it is a diagnostic, not a proved decomposition of the transient mass. The background outside this set need not have density rho_c at the measured finite times.

The plot [data/concentration.svg](data/concentration.svg) shows the mean slowest-site mass over time. [data/profile.svg](data/profile.svg) shows four snapshots from the prespecified run 12 with the five slowest rates marked. These are original simulation figures, not paper images.

For an independent dynamic validation, 50,000 three-site trajectories were compared at time 20 with the transition law of the separately enumerated generator. Total variation error was 0.005327; the largest single-state error was 1.755 binomial standard errors. A positive Poisson-series calculation and the matrix exponential agreed to 1.39e-16. SciPy emitted internal matrix-multiplication warnings, retained in [data/verification.json](data/verification.json); both final probability vectors were finite and the independent calculation resolved that numerical concern.

An additional 300 independent environment/geometric-bulk samples for each kappa and L=64,256,1024,4096 check the unconditioned representation used in the proof. At L=4096 the median bulk densities were 1.310,0.947,0.831 versus rho_c=1.286,0.857,0.643. The observed probabilities B>N were 0.010,0.013,0.010. These are **unconditioned auxiliary samples**, not canonical stationary samples; none were silently rejected or used to reweight environments. The heavy near-tie tail is a reason to report medians rather than annealed means. See [data/bulk_diagnostics.csv](data/bulk_diagnostics.csv) and [data/bulk_summary.json](data/bulk_summary.json).

All numerical work used one thread at nice 10. The analysis peak resident memory was 111,591,424 bytes (about 106.4 MiB), far below 4 GB. The C++ simulator stores O(L) state and streams snapshots to disk; it has no thread creation or large allocations. Its runtime memory was not separately profiled. No PDF, scan, or paper image was saved. No publication or push was performed.

### Reproduction

Run from this directory:

```sh
clang++ -O3 -std=c++17 code/tazrp.cpp -o code/tazrp
./code/tazrp --validate
./code/tazrp
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/check_and_analyze.py
```

The programs set their own priority to at least nice 10. The analysis sets numerical library thread limits and keeps its plotting caches inside data/. Python requires numpy, scipy, and matplotlib; source retrieval additionally requires requests and pypdf. Seeds are fixed and recorded. The C++ standard library's distribution algorithms can vary across platforms; the raw outputs preserve this run exactly.

## Literature results and their scope

Unless a journal page is explicitly given, the page numbers below are **PDF pages of the saved arXiv version**, whose page delimiters are present in the text files. They are not inferred journal page numbers. Source URLs, extraction lengths, and SHA-256 hashes of the transient source bytes are in [sources/manifest.txt](sources/manifest.txt). Later-version pagination can differ from the journal. The text files give the precise statements to check.

| Reference and inspected location | What it proves or analyzes | Relation to D0023 |
|---|---|---|
| Seppäläinen (1999), Section 4, Problem 2, PDF p. 9; [source](https://arxiv.org/abs/math/9906194) | Asks for the developing concentration below the hydrodynamic scale. Problem 3 separately asks local weak convergence. | The exact target of this report. |
| Andjel–Ferrari–Guiol–Landim, SPA 90 (2000), 67–81; Theorem 2.1, PDF p. 5; Theorems 2.3–2.4, PDF p. 7; [source](https://arxiv.org/abs/math/9911205) | Characterizes extremal invariant measures for the constant-rate totally asymmetric model and proves critical weak convergence from strictly supercritical initial density, under its environment assumptions. | Resolves the relevant constant-rate local-convergence question; it does not locate the transient excess masses. |
| BMRS, BJPS 29 (2015), 313–335; Theorems 2.1–2.2, PDF pp. 6–7; Theorem 2.3, pp. 7–8; Theorem 2.4, p. 8; [source](https://arxiv.org/abs/1411.4318) | Upper critical domination; necessity of the left-density condition; counterexamples beyond nearest-neighbor jumps; sufficiency under its hypotheses, including (H). | Domain-of-attraction results, not a condensate point-process law. |
| BMRS, AIHP 53 (2017), 766–801; Theorem 2.2, arXiv v2 PDF p. 10; [source](https://arxiv.org/abs/1411.4305) | With its stated environment, finite-critical-density and convexity hypotheses, liminf left empirical density >=rho_c implies quenched weak convergence to the critical measure. The introduction, pp. 2–3, separates mesoscopic condensate evolution from escape of mass. | The theorem addresses escape of mass. The developing condensate picture is motivation, not the statement proved. |
| BMRS, Ann. Probab. 48 (2020), 404–444; Theorem 2.1, PDF p. 10; [source](https://arxiv.org/abs/1801.01654) | Hydrodynamic convergence to the entropy solution, including supercritical initial profiles when slow defects are macroscopically dense; the flux is constant above rho_c. | Extends the hydrodynamic theorem. A flat supercritical profile still carries no information about the finer-scale mass locations. |
| BMRS, PTRF 176 (2020), 149–202; Theorem 2.3, PDF pp. 15–16; Theorem 2.4, p. 17; Theorem 2.5, p. 18; [source](https://arxiv.org/abs/1804.06148) | Strong local convergence at typical observation sequences to the critical measure when the lower hydrodynamic density is >=rho_c; a time-averaged version without typicality; convergence from configurations with a limiting left density. | A precise dynamic loss-of-mass result. Bounded local observables do not determine how much mass sits at exceptional moving sites. |
| BMRS survey, *Zero-range process in random environment*, 2020 preprint, 2021 chapter; Section 2, PDF pp. 3–6; [source](https://arxiv.org/abs/2008.06386) | Reviews the convergence, hydrodynamic and local-equilibrium theorems. The traffic-jam discussion is explicitly introduced as heuristics. | Useful confirmation of which part of the picture the BMRS theorem statements cover. |
| Grigorescu–Kang–Seppäläinen, Ann. Appl. Probab. 14 (2004), 1577–1602; Theorem 1, PDF p. 6; Theorem 2, p. 7; [source](https://arxiv.org/abs/math/0303336) | Annealed upper and lower tail bounds for the tagged-particle correction and for particle counts ahead of a jam's hydrodynamic front. | Rigorous mesoscopic time-scale information for the equivalent exclusion model, but no full joint law of site rates and excess queue masses. |
| Krug–Ferrari, J. Phys. A 29 (1996), L465–L471; [publisher](https://doi.org/10.1088/0305-4470/29/18/004). Evans, EPL 36 (1996), 13; [text](https://arxiv.org/abs/cond-mat/9606036). Krug review, 2000; [text](https://arxiv.org/abs/cond-mat/9912411) | Phase transition, stationary condensation and its exclusion/traffic interpretation; scaling arguments for coarsening. Krug–Ferrari's abstract was inspected; full PDF retrieval was blocked. | Foundational phase picture; no uninspected numbered dynamic theorem is attributed to the inaccessible paper. |
| Godrèche–Luck (2012), J. Stat. Mech. P12013; discussion, PDF p. 29; [source](https://arxiv.org/abs/1209.4749) | Stationary interaction/disorder phase diagram and localization properties. Its concluding discussion identifies condensate formation dynamics as a further problem. | Does not by itself provide the requested dynamic theorem. |
| Chleboun–Grosskinsky, J. Stat. Phys. 154 (2014), 432–465; Theorems 4.3–4.4, PDF pp. 30,32; [source](https://arxiv.org/abs/1306.3587) | Equivalence of ensembles in inhomogeneous systems, including a critical background outside suitable near-trap sets. | Rigorous stationary background/condensed-phase separation in broad models; no prescribed growing-window time limit. |
| Mailler–Mörters–Ueltschi, SPA 126 (2016), 3283–3309; Theorems 2.1–2.2, PDF p. 4; Theorem 2.3, p. 5; [source](https://arxiv.org/abs/1509.07672) | One stationary macroscopic condensate; rank localization for strong disorder and Gamma disorder laws in an intermediate regime. Assumes stationary weights with exponent beta>1. | Genuine rigorous localization, but an equilibrium theorem for interacting weights; its assumptions do not include constant g=1. |
| Jain–Barma, PRL 91 (2003), 135701; PDF pp. 1,3–4; [source](https://arxiv.org/abs/cond-mat/0305098) | Analytical scaling arguments and simulations for formation from a uniform profile in the disordered driven ZRP. | Directly relevant coarsening picture, not a mathematical proof of a joint mass-location limit. |
| Jatuviriyapornchai–Grosskinsky, J. Phys. A 49 (2016), 185005; abstract, PDF p. 1; [source](https://arxiv.org/abs/1511.09357) | Effective size-biased birth-death descriptions of homogeneous coarsening, based partly on heuristic assumptions. | Different mechanism and no resolution of iid site-disorder dynamics. |
| Jatuviriyapornchai–Grosskinsky, J. Stat. Phys. 191 (2024), 147; Theorem 1, PDF p. 7; Theorems 2–3, pp. 9–10; [source](https://arxiv.org/abs/2404.02590) | Stationary condensation and cluster scales induced by a fast rate at a selected occupation number. | The rate modification depends on occupation and size; it is not iid sitewise disorder. |
| Sethuraman–Xue, Ann. Probab. 52 (2024), 1048–1092; Theorem 4.2, PDF p. 16; [source](https://arxiv.org/abs/2205.10252) | For bounded increasing rates and finitely many defects in a symmetric model, the hydrodynamic measure has explicit defect atoms and evolving boundary conditions. | A rigorous dynamic concentration theorem in a different, finite-defect diffusive setting. |
| Armendáriz–Beltrán–Cuesta–Jara, SPA 179 (2025), 104507; preprint *Fluid limit for the coarsening phase...*, Theorem 2.9, PDF p. 6; [source](https://arxiv.org/abs/2302.05497) | Fluid coarsening paths on a fixed finite graph as the particle number grows; constant-rate networks are included. | Fixed graph and growing mass, rather than a growing iid environment at fixed supercritical density. |
| Emrah–Janjigian–Seppäläinen, CMP 406 (2025), *Anomalous geodesics...*; Theorem 3.9, PDF p. 24; [source](https://arxiv.org/abs/2408.13382) | A second-class customer in a specified inhomogeneous queue tandem either becomes trapped or escapes at positive speed; gives its trapping and speed laws. | A location law for a second-class customer, not the distribution of supercritical first-class excess mass. |
| Blank–Chleboun–Grosskinsky–Jatuviriyapornchai (2026), Theorem 1, PDF p. 4; Theorems 2–3, p. 6; [source](https://arxiv.org/abs/2603.00806) | Stationary cluster-size laws for spatially homogeneous lattice gases with size-dependent weights. | Different model and equilibrium limit. |

For clarity, GKS Theorem 1 really is a quantitative result on the expected scale. In its notation, F(c+epsilon)~K epsilon^(nu+1), nu>0, and the iid initial gaps have mean u>u* and finite variance. Write kappa=nu+1, beta=kappa/(kappa+1), A=(kappa+1)^(kappa+1)/kappa^kappa. Then for z>0,

    exp[-K z^(kappa+1)/(u-u*)]
       <= liminf P((sigma_0(t)-ct)/t^beta > z)
       <= limsup P((sigma_0(t)-ct)/t^beta > z)
       <= exp[-K z^(kappa+1)/(A(u-u*))].

These are disorder-averaged bounds, not a claimed exact limiting distribution, and the observed variable is a tagged exclusion particle. The constants and exponent were checked against a second text extraction of that theorem page.

The search also checked Menshikov–Popov–Wade, *Semi-infinite particle systems with exclusion interaction and heterogeneous jump rates*, published online in 2025, PTRF 195 (2026), 73–107. Its abstract and model concern stability from finite perturbations of close packing and convergence of interparticle gaps; that initial condition is different from positive supercritical gap density throughout an infinite system. [Publisher](https://doi.org/10.1007/s00440-024-01357-2).

The classification PARTIAL records the scope achieved here: a complete stationary growing-ring concentration theorem, explicit extremal statistics and rate tolerance, audited simulations from supercritical initial data, and identification of rigorous related dynamic results. No inspected theorem yields the complete evolving condensate description requested in the original Problem 2. This is a literature assessment with the search coverage in [sources/SEARCH_NOTES.txt](sources/SEARCH_NOTES.txt), not a proof that no other relevant result exists.

Task: “Open problem D0023” — 2026-11-13, approximately 10:27 Asia/Tbilisi (session start; shell clock).
