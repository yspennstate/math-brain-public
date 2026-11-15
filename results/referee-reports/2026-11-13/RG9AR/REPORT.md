Overall verdict: MINOR

The empty-start Theorem 1.1 survives this audit. I found no missing power of r, unsummable union bound, or use of a third service moment in its proof. Zero service shares do not invalidate the marked product law or its uses here. There is, however, a false extension to nonempty initial states in Remark 5.1, with a counterexample below. There is also a missing localization in the wording of Proposition 4.3's proof, and the displayed integration-by-parts calculation needs its boundary condition stated. These corrections do not require a new argument for the empty-start theorem.

References to lines below mean lines of the supplied PAPER.tex. I read the supplied code but did not execute or import it. No external sources were accessed, so the citation audit at the end distinguishes mathematical uses from bibliographic claims that cannot be checked from the supplied files.

## Theorem 1.1 — SOUND

Lines 47–57 and 269–273. The assumptions suffice for the stated empty-start limit in the J1 topology, after the local proof correction described under Proposition 4.3.

The zero-service reduction at line 65 is valid with the stipulated convention that zero-requirement arrivals depart immediately. Writing p=P(B>0), thinning gives rate lambda_r p, mean m/p, and second moment m_2/p. Load, h=m_2/(2m), sigma^2=m_2/m, and the heavy-traffic parameter are unchanged. Insertion followed by immediate deletion restores the previous order. Thus the later assumption B>0 is legitimate.

The reduction to the stable reference rate does not restrict beta to be positive. At the actual rate, on H_r=r^2(T+1), the Poisson likelihood ratio is exactly the one displayed at line 271. Independently expanding its second moment gives

    log E_0[Lambda_r^2]
      = H_r (lambda_r-lambda_r^0)^2/lambda_r^0
      -> (T+1)(1-beta)^2/m.

Consequently Cauchy–Schwarz transfers each vanishing reference-law probability to the actual law. This is a finite-horizon argument and remains valid when the actual queue is supercritical. Service requirements and insertion uniforms have the same conditional laws under both measures. No comparison or monotonicity of queue lengths between disciplines is being assumed.

For completeness, the functional CLT invoked at line 273 has the required Lindeberg condition under exactly the stated moment assumption. For the compensated input

    M_r(t) = [sum_{k<=A_r(r^2 t)} B_k - lambda_r m r^2 t]/r,

the predictable quadratic variation is lambda_r m_2 t, and its large-jump second-moment contribution on [0,T] is

    lambda_r T E[B^2; B>epsilon r] -> 0.

The drift of the uncompensated net input is -r(1-lambda_r m)t -> -beta t. Hence its limit is sigma times Brownian motion minus beta t, with sigma^2=m_2/m, rather than Var(B)/m. Poisson arrival-count fluctuations account for the difference.

Work conservation, Q_r(0)=0, and the immediate-zero-service convention give W_r(0)=0 and the exact reflection representation. Reflection and its regulator are continuous at continuous input paths; in the uniform norm, reflection has Lipschitz constant at most two. Thus the workload and regulator limits used earlier are justified. Collapse gives uniform-on-compact convergence in probability of Q_r(r^2 .)/r minus W_r(r^2 .)/(hr). Slutsky's theorem in D, together with the continuous workload limit, gives the claimed J1 convergence. Applying the argument on every fixed compact interval gives D[0,infinity) convergence.

Line 54 should say that collapse is **sufficient** for the theorem. Workload convergence and continuity of its limit alone do not make marginal queue-length convergence equivalent to collapse: marginal convergence does not identify a joint coupling. The proof uses only sufficiency, so this does not damage the theorem.

## Lemma 2.1, lem:product — SOUND, with a boundary-domain correction

Lines 76–98. The marked law is correct, including for gamma(n,i)=0. In particular, the original-size mark is length biased:

    H(original in db) = b F(db)/m,
    residual | original=b is Uniform(0,b).

It is not an independent original-size draw with law F. The paper uses the correct joint law. Integrating x and x^2 gives

    E_H X_I = E[B^2; B in I]/(2m),
    E_H X_I^2 = E[B^3; B in I]/(3m).

The latter quantity need not be finite for unrestricted I. Where the proof uses it, I is bounded above by 2a, so the pointwise inequality X_I^2 <= 2a X_I gives exactly the stated finite bound. No unrestricted third moment is used.

The integration-by-parts identity at lines 93–95 requires test functions satisfying

    f_n(...,(b,0),...) = f_{n-1}(the same sequence with this job deleted).

It is false for arbitrary unrelated bounded smooth f_n. This is the natural boundary condition for the queue's generator, and it should be stated. With it, the calculation is correct: the lower endpoint is the deletion state and the upper endpoint is the insertion state with residual equal to original size. The coefficient identity p_n/m=lambda p_{n-1} cancels each upper-boundary flux with insertion into that exact position. The deletion contributions, after integrating the deleted mark, have total coefficient p_{n+1}/m because the service fractions sum to one; this equals lambda p_n and cancels arrival loss at level n.

No step divides by a service share or assumes that a particular job is always served. A zero share simply gives zero service-boundary flux and zero corresponding insertion flux. Arrivals are locally finite, and departures cannot outnumber the initial jobs plus arrivals, so zeros do not create an explosion. On a bounded time interval, each arrival is inserted into a positive-share position almost surely and receives service before the next event, apart from null coincidences. Thus zero shares do not create a missing stationary atom at residual equal to original size.

Regeneration establishes uniqueness. To avoid an apparent forward-reference loop, first prove the finite busy-cycle mean in the first part of Lemma 2.2 using workload alone. Every finite initial workload reaches zero almost surely at subcritical load, independently of gamma. Thereafter the finite-mean regenerative cycles give a unique stationary occupation law. This does not use the cycle-reward identity or assume the product law to prove recurrence.

The conditional independent-summand law is used only for the reference stationary process at deterministic sampling times, or to calculate pi_r(S_j). It is never assumed for the empty-start process at arbitrary times or at a first crossing.

## Lemma 2.2, lem:cycle — SOUND

Lines 100–113. A cycle includes the idle wait and its following busy period. This convention is essential: the initiating arrival is included in its cycle's arrival count.

The workload busy period is discipline independent. The FCFS branching calculation gives mean total service m/(1-rho_r^0)=mr; nonnegativity permits summing the generation expectations without an additional moment assumption. This finite expectation also implies an almost surely finite busy period. Adding the mean idle wait gives

    E C_r = 1/lambda_r^0 + mr = r/lambda_r^0.

For the marked count, the pre-arrival predicate is predictable and the arriving size is independent of it. Its intensity is therefore lambda_r^0 p_I times the indicator of S. At the cycle stopping time the expected bracket is at most lambda_r^0 p_I E C_r, which is finite. The stopped compensated count is consequently uniformly integrable in L2, so optional stopping is justified even if the cycle length has infinite variance. Renewal reward then identifies the expected occupation time as E C_r pi_r(S), giving E Y=r p_I pi_r(S).

Useful endpoint checks are S=all states, giving r p_I arrivals of the class per cycle in expectation, and S={empty}, giving p_I, the expected indicator that the initiating arrival has that class. Both agree with the identity. No arrival-Palm size bias is mistakenly applied to the incoming B; size bias belongs to the stationary jobs in H.

## Lemma 3.1, lem:lowertail — SOUND

Lines 142–153. Only E R=h<infinity is required. Since R>0 almost surely, kappa=-log E exp(-theta_0 R)>0. For n>Cr, C>2 theta_0 K/kappa implies theta_0 Kr-kappa n <= -kappa n/2. This gives a bound exponential in r, uniformly over these n.

For n<=Cr, dominated convergence applies because (1-exp(-theta R))/theta <= R. It gives log E exp(-theta(R-h))=o(theta). Choosing theta so that this logarithm is at most theta eta/(2C), exponential Markov gives exp(-theta eta r/2). Combining the two ranges gives positive constants c_0,c_1 independent of n and r. The event for n=0 is empty. There is no upper-tail exponential-moment assumption and no residual variance assumption.

## Proposition 3.2, prop:lower — SOUND

Lines 126–138 and 155–168. The interpolation inequality has the correct direction. Service reduces V_I at rate at most one; arrivals reduce V_I-mu Q by at most mu<=h; departures increase it by mu per departed job. Simultaneous departures only help this inequality. Applying it forwards from u and backwards from v gives both displayed sandwich bounds.

The grid has O(r) intervals, each of length delta r. The Poisson Chernoff exponent is positive for M>1/m, uniformly since lambda_r^0<=1/m. Thus the probability of any failed arrival budget is O(r exp(-c r)).

At each grid point, the conditional bound of Lemma 3.1 is uniform over n. Averaging against the geometric law costs no additional factor counting possible n. Conditioning the stationary process on Q(0)=0 costs exactly r, and the grid costs another O(r). The displayed O(r^2 exp(-c r)) is correct.

On a workload cap of Kr and the good grid/budget events, the preceding grid point gives D(t)>=-epsilon r. The workload cap can be removed by its diffusion tightness. The slightly longer T+1 horizon covers the last grid point for all sufficiently large r. Finally h>0, so hQ<=W+(hQ-W)^+ proves the asserted uniform queue-length tightness without using the upper bound or the desired queue-length CLT.

## Lemma 3.3, lem:ncycles — SOUND

Lines 170–176. After removal of zero-requirement arrivals, the count of busy-period starts is exactly the integral against arrivals of the predictable empty-workload indicator. Its compensator is lambda_r^0 I_r(t).

Stopping when the continuous idle-time process reaches ar bounds the expected bracket by lambda_r^0 ar. Dividing the martingale by r gives second moment at most lambda_r^0 a/r, which tends to zero. The workload regulator FCLT already proved independently makes I_r(r^2T)/r tight, so the stopping event is unlikely for large a. This proves the count divided by r is tight.

Importantly, this is not an unjustified uniform renewal estimate deduced just from E C_r=O(r), nor does it require finite cycle-length variance. This lemma is the reason the upper-bound union is over O_P(r) cycles, rather than O(r^2) arrivals without a class factor.

## Proposition 4.1, prop:small — SOUND

Lines 180–195. For fixed L, the moving cutoff ell_r stays in [L,2L). Conditional on Q=n<=Cr, each summand lies in [0,2L], uniformly in r and gamma. With threshold epsilon r/2, Hoeffding's exponent is

    2 (epsilon r/2)^2 / [n (2L)^2]
      >= epsilon^2 r/(8 C L^2).

Thus the constant in line 192 is correct. Averaging over n costs no factor r. Stationary conditioning and the grid give O(r^2 exp(-c r)). The interpolation applies to D_s with its own mean mu_s<=h, using the preceding and following grid points. Apply Proposition 3.2 on [0,r^2(T+1)] when removing the restriction at all grid points, including the possible point just beyond r^2T. First let r grow for fixed C and L, then let C grow. No concentration inequality for unbounded residuals is being used here.

## Proposition 4.2, prop:dyadic — SOUND

Lines 197–237. The classes partition (ell_r,r] without omissions, including atoms at endpoints: the lower endpoint is open and the upper one closed. Fix C,A,epsilon and L before taking r to infinity.

V_j is zero at cycle start, cannot increase during service or at a departure, and jumps by at most 2b_j at a class-j arrival. Therefore any strict crossing of M_j is witnessed by an arrival whose pre-state satisfies V_j>M_j-2b_j and Q<=Cr. This remains correct for the coarse classes where M_j-2b_j is negative; the empty pre-state may then qualify.

On N_r(r^2T)<=Ar the witness belongs to one of the first ceil(Ar)+1 complete cycles. Dominating by counts over all these whole cycles, even their portions beyond the horizon, only enlarges the count. Summing their expectations and using Markov gives

    P(class-j bad event with both caps)
      <= (ceil(Ar)+1) r p_j pi_r(S_j)
      <= C_A r^2 p_j pi_r(S_j).

There is no conditioning of a cycle on its length or on the realized number of cycles. Hence no independence between that count and the cycles is needed. There is also no further stationary-conditioning factor r in this argument.

For j>=j_0(epsilon), x_j>=4b_j. On S_j with Q=n<=Cr,

    V_j-n mu_j > x_j-2b_j >= x_j/2.

The conditional variance is at most

    n E_H X_{I_j}^2 <= Cr (2b_j mu_j)
      = (C/m) r b_j w_j.

Centered summands are bounded above by 2b_j. Bernstein with t=x_j/2 gives exactly x_j^2/[8(V+b_j x_j/3)], including the factor 8 and the term 1/3. The conditional bound is uniform in n, so passing to pi_r(S_j) does not multiply it by the number of queue lengths. Degenerate bands with w_j=0 have zero class-arrival probability and cause no division problem.

The full exponent and summation audit is recorded next. Its conclusion is that the claimed probability tends to zero under m_2<infinity, with no third moment and no rate assumption on the service tail.

## Proposition 4.3, prop:upper — GAP: missing localization, filled here

Lines 239–263. The proposition is true, but the assertion at line 258 is literally too broad. The complement of the event in Proposition 4.2 includes paths on which the queue-length cap or the cycle-count cap fails. On those paths it does not imply V_j<=M_j, so line 260 need not hold there.

Here is the complete local fix. Put

    G_r = {sup_{s<=r^2T} Q_r(s)<=Cr, N_r(r^2T)<=Ar},
    F_r = G_r intersect {some j and s<=r^2T have V_j(s)>M_j}.

Proposition 4.2 says P_0(F_r)->0. On G_r minus F_r, and only there, the bound at line 260 follows by summing M_j. The missing exceptional probability is bounded by

    P_0(G_r^c)+P_0(F_r)
      <= P_0(sup Q_r>Cr)+P_0(N_r>Ar)+P_0(F_r).

Line 262 already chooses C and A to make the first two terms small, so this repair supplies the intended proof without a new estimate.

The large-job estimate is valid as written. Starting empty, their total remaining work is bounded by their total arriving original work. Campbell's identity and B>r give

    E_0[sup V_b/r] <= lambda_r^0 r T E[B; B>r]
                   <= lambda_r^0 T E[B^2; B>r] -> 0.

Thus this term even vanishes in L1. It is not a maximal inequality for stationary residuals.

The decomposition of W-hQ at line 256 has the correct sign: the discarded term -(h-mu_s)Q is nonpositive. On G_r minus F_r,

    sup_s sum_j V_j(s)/r
      <= C sum_j mu_j + epsilon sum_j a_j
      <= C E[B^2; B>L]/(2m) + epsilon.

For a fully explicit limit order, fix a target deviation z>0 and an arbitrarily small probability tolerance theta. Choose C,A so the two caps fail with total limiting probability at most theta. Choose epsilon<z/4, then a fixed L with C E[B^2;B>L]/(2m)<z/4. Proposition 4.1 and the large-job estimate make their respective terms smaller than z/4 with probability tending to one. Proposition 4.2 removes F_r. Therefore the limsup probability of an upper deviation exceeding z is at most theta; let theta decrease to zero. This establishes precisely the displayed convergence in probability.

## Remark 5.1 — ERROR: the proposed initial-state extension is false

Line 276. Initial collapse and removal of all initial jobs by a subdiffusive time do not ensure collapse during that initial interval. The statement fails even for processor sharing with deterministic arriving service times.

Take integer r, arriving B=1, lambda_r=1-1/r, and processor sharing gamma(n,i)=1/n. Then h=1/2. At time zero put r initial jobs in the queue, each with original size 1 and residual requirement 1/2. Thus W_r(0)=r/2=hQ_r(0) exactly, and the scaled initial workload and queue length are bounded and converge.

Let tau_r be the common departure time of those r jobs. Until tau_r no new job can depart: its received service is at most the common additional service of an initial job, which is less than 1/2, whereas its requirement is 1. Consequently, before tau_r,

    Q_r(t)=r+A_r(t),
    integral_0^{tau_r} [1/(r+A_r(s))] ds = 1/2.

The Poisson law of large numbers on time scale r gives A_r(ru)/r -> u uniformly on compact intervals. Hence

    tau_r/r -> c = exp(1/2)-1 = 0.6487212707.

All initial jobs therefore leave in O_P(r), and in particular by the deterministic time r^(3/2) with probability tending to one. Their remaining total work at that time is o_P(r). Both readings of the remark's removal condition are satisfied.

Work conservation gives W_r(t)=r/2+A_r(t)-t up to tau_r, and W_r(tau_r)/r -> 1/2. Immediately before and after the simultaneous departure,

    (W_r-hQ_r)(tau_r-)/r -> (1-exp(1/2))/2 = -0.3243606354,
    (W_r-hQ_r)(tau_r)/r  -> 1-exp(1/2)/2   =  0.1756393646.

More simply, that departure makes W-hQ jump upward by exactly r/2, so one of its two sides has absolute value at least r/4. Since tau_r<=r^2T with probability tending to one for each fixed T>0, uniform collapse on the claimed horizon fails. This is a mathematical counterexample, not an inference from simulation.

Delete the proposed extension. A valid replacement would need assumptions controlling the initial residual profile and its evolution throughout the initial layer. Initial equality W=hQ and later disappearance of the initial population are insufficient. The theorem itself assumes an empty start and does not use this remark.

## Upper-bound exponent and power audit

For q=2^(-1/4), the relevant quantities and cancellations are:

| Quantity | Value or bound | Consequence |
| --- | --- | --- |
| Grid size, used for lower/small terms | O(r) | With conditioning cost r: O(r^2 exp(-c r)) |
| Cycle count after localization | ceil(Ar)+1=O(r) | One factor r |
| Expected qualifying class arrivals per complete cycle | r p_j pi_r(S_j) | Second factor r; no extra conditioning factor |
| Class bad probability | C_A r^2 p_j pi_r(S_j) | Starting estimate |
| b_j | r 2^(-j-1) | r/b_j=2^(j+1) |
| Class rarity | r^2 p_j <= 4^(j+1) w_j | Cancels both powers of r |
| a_j | (1-q)2^(-j/4) | Sum over j is 1 |
| x_j | epsilon(1-q) r 2^(-j/4) | Total deviation budget <=epsilon r |
| x_j/(4b_j) | epsilon(1-q)2^(3j/4-1) | j_0 independent of r |
| Variance proxy | (C/m)r b_j w_j | Uses only band-truncated second residual moment |
| Bernstein exponent | >= c 2^(j/2) | Independent of r, increasing in j |
| Dominating class bound, j>=j_0 | C_A m_2 4^(j+1) exp(-c2^(j/2)) | Summable in j |
| Bound on total intermediate work divided by r | C E[B^2;B>L]/(2m)+epsilon | Small after C is fixed and L is chosen |
| Large work divided by r in expectation | <=lambda_r^0 T E[B^2;B>r] | Tends to zero |

To rederive the Bernstein exponent explicitly,

    x_j^2/[8(V+b_j x_j/3)]
      >= epsilon^2 r a_j^2/[8 b_j(Cm_2/m+epsilon/3)]
      = [epsilon^2(1-q)^2/{4(Cm_2/m+epsilon/3)}] 2^(j/2).

The factor 2^(j/2) comes from 2^j times a_j^2 proportional to 2^(-j/2), not from a remaining positive power of r.

For each fixed j, the band (r2^(-j-1),r2^(-j)] escapes to infinity, and w_j<=E[B^2;B>r2^(-j-1)]->0. For j<j_0, the finitely many bounds C_A4^(j+1)w_j vanish directly. For the remaining j the displayed dominating sequence is summable: its successive ratio is

    4 exp[-c(sqrt(2)-1)2^(j/2)] -> 0.

Extend the sequence by zero for j>=J_r and apply dominated convergence. This correctly handles the growing number J_r of bands; multiplying a worst-case band estimate by log r would be a weaker and potentially invalid substitute.

The result is sup_{s<=r^2T}|W_r(s)-hQ_r(s)|=o_P(r). The estimates do not establish a deterministic o(r), almost sure convergence, or an L1 statement for the whole collapse error. They also give no general polynomial convergence rate under a bare finite second moment. The paper's displayed probabilistic claim is the one they prove.

## Independent programs, checks, and outputs

Every program I executed is saved in this folder. The two computations were run sequentially, with standard-library Python and explicit wall-time alarms. No author program, external source, agent, visible window, or git operation was used. Numerical logs retain the environment's warning that the requested nice priority could not be set; both computations completed well within the author's resource limits.

### referee_exact_checks.py

Command: `nice -n 10 python3 -B referee_exact_checks.py > referee_exact_checks.out 2>&1`

Full results: referee_exact_checks.json and referee_exact_checks.out. Runtime: 0.286 seconds as recorded internally.

The exact Fraction computation uses B=1 with probability 4/5 and B=4 with probability 1/5, so m=8/5 and H(original=1)=H(original=4)=1/2. It tests an order-sensitive boundary-compatible function

    f_n = sum_i x_i + sum_{i<j} b_i x_i x_j.

It independently enumerates the marked law, integrates the multilinear residual expressions exactly, and checks level-by-level cancellation of service drift against insertion increments. The disciplines are LCFS, service to a middle position, half to each end, and a sparse rank-dependent 2/7–5/7 allocation. All admit zero shares for some n.

Outputs:

    exact level balance identities: 24
    exact cancellation residual: 0
    deletion boundary checks: 2568
    Bernstein/power inequality checks: 360 passed
    largest relative error in x_j/(4b_j) identity: 1.89e-15

These finite checks supplement the general balance proof; they do not replace it. No empirical agreement is used to infer the product law.

The same program independently simulates the initial cohort counterexample up to its departure, using the exact PS service clock. There are 256 repetitions at each r. Its outputs are:

| r | Mean tau_r/r | Mean D(tau_r-)/r | Mean D(tau_r)/r |
| --- | ---: | ---: | ---: |
| 64 | 0.645093 | -0.329297 | 0.170703 |
| 256 | 0.648558 | -0.325430 | 0.174570 |
| 1024 | 0.648691 | -0.324016 | 0.175984 |
| 4096 | 0.648690 | -0.324336 | 0.175664 |
| Mathematical limit | 0.648721 | -0.324361 | 0.175639 |

The jump D(tau_r)-D(tau_r-)=r/2 is also asserted on every run.

### referee_simulation.py

Command: `nice -n 10 python3 -B referee_simulation.py > referee_simulation.out 2>&1`

Full results: referee_simulation.json and referee_simulation.out. Runtime: 13.488 seconds. Recorded peak resident memory: 30,326,784 bytes. The complete audit's created programs and numerical outputs total about 27 KB before this report.

The main experiment uses Pareto tail P(B>x)=(0.6/x)^(5/2), x>=0.6. Direct moment calculation gives E B=1, E B^2=1.8, h=0.9, and E B^3=infinity. Thus the residual law has finite mean and infinite variance, as required for a meaningful stress test of the proof's moment assumptions.

Both disciplines use the same rate lambda_r=1-1/r and start empty:

- LCFS preemptive resume serves and inserts at the newest end. This is the paper's gamma(n,1)=1 after reversing the position numbering.
- The mixed discipline gives half the capacity to each end when n>=2, full capacity when n=1, and inserts at either end with probability 1/2. For interior positions its service shares are zero.

There are 48 independent paths per discipline and r, on [0,r^2/4], for 480 paths in total. The exact event simulator updates only served endpoints. It checks both sides of every event and the final horizon; between events W-hQ is affine, so these observations give the path supremum, including the pre-departure values. Workload accounting is also checked against the sum of stored residuals.

The following numbers are for sup_{s<=r^2/4}|W(s)-0.9Q(s)|/r:

| r | rho | LCFS median | LCFS mean | LCFS 90th percentile | Mixed median | Mixed mean | Mixed 90th percentile |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 32 | 0.968750 | 0.298840 | 0.343222 | 0.616900 | 0.284419 | 0.299239 | 0.413294 |
| 64 | 0.984375 | 0.282339 | 0.296430 | 0.417178 | 0.255158 | 0.331727 | 0.367914 |
| 128 | 0.992188 | 0.210007 | 0.251058 | 0.372616 | 0.203965 | 0.226709 | 0.313510 |
| 256 | 0.996094 | 0.160886 | 0.173934 | 0.251284 | 0.196099 | 0.217922 | 0.321004 |
| 512 | 0.998047 | 0.158647 | 0.177609 | 0.279320 | 0.157470 | 0.196380 | 0.251166 |

There were 16,661,334 arrival/departure events in these main paths. The largest checked workload-accounting discrepancy was 2.53e-11 in unscaled workload units. Typical suprema decrease; some means and quantiles are nonmonotone. With only 48 samples per cell, especially under this heavy tail, these finite experiments cannot establish convergence, a rate, or monotonicity. They do not contradict the claimed probabilistic decay.

The program also independently tests the marked-cycle identity, using the two-point service law above and a predicate different from the supplied author programs:

    S = {Q<=3, remaining work of original-size-4 jobs > 3/2}.

At rho=4/5, lambda=1/2, and r=5, the exact target is

    pi(S) = sum_{n=1}^3 (1-rho)rho^n
              sum_{k=1}^n binom(n,k)2^(-n)[1-(3/8)^k/k!]
          = 15371/80000 = 0.1921375.

Here r p_I=5/5=1, so this is also E Y. The formula follows by conditioning on the number k of size-4 marks; their residuals are independent Uniform(0,4), whose sum has CDF (3/8)^k/k! at 3/2. As a second arithmetic check, the contributions from n=1,2,3 are 0.05, 0.06975, and 0.0723875. Expected cycle length is 10.

For 20,000 complete cycles per discipline, the outputs are:

| Discipline | Mean marked count | Standard error | Difference / SE | Mean cycle length |
| --- | ---: | ---: | ---: | ---: |
| LCFS | 0.192550 | 0.005044 | 0.0818 | 9.972014 |
| Mixed ends | 0.196350 | 0.004671 | 0.9019 | 10.048129 |

These checks test the pre-arrival marked count and full-cycle convention; they are not evidence in place of optional stopping or renewal reward.

## Corrections tied to lines or displays

1. **Line 54:** replace “the theorem is equivalent to” by “it suffices to prove.” The stated explanation gives the sufficient direction and does not supply joint convergence for a converse.
2. **Lines 93–95, integration-by-parts display:** require deletion-compatible test functions with f_n(...,(b,0),...)=f_{n-1}(deleted state). Without that condition the displayed equality is false for arbitrary smooth f_n. This is a presentation correction to the balance computation, not a counterexample to the product law.
3. **Lines 97–108:** make the logical order explicit: workload first proves finite-mean recurrence; product balance identifies the stationary law; then renewal reward uses it. The finite-mean part of Lemma 2.2 does not depend on Lemma 2.1, so no substantive circularity is necessary.
4. **Line 194:** specify that queue-length tightness is applied with horizon T+1 to cover the following grid point beyond r^2T. The stated tightness result already permits this.
5. **Lines 258–260:** replace “On the complement of the event in Proposition [4.2]” by “On the queue-length and cycle-count cap event, outside the bad event in Proposition [4.2].” Include the two cap-failure probabilities when bounding the final exceptional probability. Line 262 already supplies their control.
6. **Line 276, second sentence of Remark 5.1:** delete the proposed extension, or replace it with a proved condition controlling the entire initial layer. The explicit PS counterexample above satisfies its stated conditions and violates collapse.

I found no reason to change the constants or powers in the lower-tail bound, Hoeffding display, Bernstein display, likelihood-ratio display, or large-job estimate. No stylistic changes unrelated to correctness are requested.

## Audit of cited results and their uses

| Citation | Use visible in the text | Assessment within this audit |
| --- | --- | --- |
| Kelly [Kel], Chapter 3 | Symmetric discipline definition and stationary product form, including original-size marks | The marked statement and zero-share case are independently supported by the supplied balance argument once its boundary domain is specified. I cannot certify the exact chapter's formulation or whether its presentation expressly permits zeros without the source text. The proof need not rely on extending a strictly-positive-share theorem by assertion. |
| Whitt [Whi] | Compound-Poisson functional CLT, reflection and regulator continuity, workload limit | These are the appropriate kinds of results. Their hypotheses here are verified above by finite-second-moment Lindeberg and the continuous limit. Mere drift/variance calculation would not by itself prove a functional CLT, but the invoked theorem supplies that step. The citation has no theorem/page locator, so exact-source verification remains unavailable. |
| Fralix–Zwart [FZ] | Empty-start fixed-time queue-length insensitivity | Used as background only. The proof does not turn fixed-time insensitivity into pathwise collapse. The external historical assertion cannot be checked from the provided files. |
| Gromoll [Gro] | Prior PS diffusion limit and moment assumption | Historical comparison only; not used as an input. Its exact stated hypotheses are not locally available for verification. |
| Lambert–Simatos–Zwart [LSZ] | Prior PS limit under second moment alone | Historical comparison only; not used as an input. Exact scope requires the cited paper. |
| Limic [Lim] | Prior LCFS/LIFO heavy-traffic result | Historical comparison only; not used as an input. Exact scope requires the cited paper. |
| Zwart [Zwa], Problem 1 | Motivation and identification of the conjecture | Not a mathematical premise of the proof. I assessed the claim specified in the audit request; the original problem text was not supplied. |
| Bramson [Bra], Williams [Wil] | Examples of other state-space-collapse methods | Background only. No theorem from either is imported into the proof. |
| Computations [code] | Diagnostic programs and claimed Lean scalar check | The supplied three Python programs and output files were read, not trusted as proof or executed. Their simulation roles are consistent with the text. The supplied folder contains no Lean file, so that part of the external repository description cannot be checked here. A scalar interpolation check would not formalize the stochastic argument. |
| MathBrainRepo, MathBrainPaper, BrainFramework | Project description and provenance | No mathematical theorem is invoked from them. Their external contents and provenance claims are outside what the supplied files can establish. |

The main proof therefore does not rest on the unverified historical comparisons, simulation agreement, or an unavailable Lean file. Its load-bearing external inputs are standard product-form theory and the workload functional CLT/continuous mapping facts; the stationary balance and the needed moment conditions have been checked directly above.

Task: “You are refereeing a mathematical paper that has been posted.” Audit clock first recorded: 14 November 2026, 00:27 +04 (Asia/Tbilisi).
