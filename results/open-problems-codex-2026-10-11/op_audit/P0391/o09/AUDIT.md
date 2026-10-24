VERDICT: PASS

# Independent audit of P0391, 11 October 2026

The final mathematical claim is correct and complete for the problem as supplied, including its empty-initial-state caveat. I found no failing step or required mathematical repair. This verdict assesses the recorded proof, not publication priority. I did not use the claimant's own referee verdict as evidence of correctness.

## Exact claim and scope

ATTEMPT.md lines 5–9 claims, and explicitly refers to FULL_PROOF.md for, the following theorem. Let the service distribution B be fixed, nonnegative, with m=E B>0 and m2=E B^2<infinity. For every positional symmetric discipline gamma of the source, start the M/G/1 queue empty, use Poisson arrival rates lambda_r, and suppose r(1-lambda_r m) tends to any real beta. With h=m2/(2m),

    Q_r(r^2 .)/r => Gamma(sqrt(m2/m) Brownian(.) - beta*.)/h

in D([0,infinity)) with J1 topology. The stronger assertion proved is uniform state-space collapse on each finite horizon:

    sup_{s<=r^2 T} |W_r(s)-h Q_r(s)|/r -> 0 in probability.

Here gamma(n,i) is both the service share of position i at size n and the insertion probability into position i at the new size n. All such arrays are covered, including zero shares. There is no extra tail envelope, fourth moment, or restriction to PS/LCFS in the completed proof. Zero-service marks can be thinned: their insertion and immediate deletion restores the order, and the positive conditional law preserves rho, h and m2/m.

I independently downloaded and extracted arXiv:2202.02366v1. Its pp. 1–2 give exactly this positional definition, Poisson input, a fixed service distribution with finite second moment, and a real heavy-traffic drift parameter. The discussion on p. 2 supplies the empty-start qualification for universal marginal laws. The statement itself does not specify a topology; the claimed J1 convergence is an appropriate process version, stronger than just convergence at fixed times. Thus the claim answers the assigned question.

## Issues and qualifications in the submitted records

1. ATTEMPT.md lines 5–11 and 31: the final proof is in a separate, explicitly referenced file. ATTEMPT.md alone contains historical partial arguments. I therefore read FULL_PROOF.md, including its appendix, rather than judging the final claim from an obsolete partial result. This is a presentation choice, not a gap.

2. ATTEMPT.md lines 268–276 and 303: some historical sentences still say that sparse atomic laws are excluded or that the "final full-process theorem" retains the LT1 tail envelope. The latter wording is stale. Lines 11, 274, 300 and 307 explain that these are superseded stages; FULL_PROOF.md does cover sparse atomic finite-second-moment laws. Editorial fix: call the LT1 theorem an earlier theorem in line 303. This does not affect the proved result or require a mathematical correction.

3. ATTEMPT.md lines 9 and 305: the reported Lean check covers only scalar interpolation. I did not rerun Lean or regard it as formal verification of the probabilistic proof. Likewise, the reported simulations are supporting diagnostics, not a proof. The mathematical verdict below is based on independent re-derivation.

4. ATTEMPT.md line 9 and LITERATURE.md: no exact earlier published solution was verified. My bounded search also found none, but OpenAlex returned HTTP 429. This audit does not certify novelty or the absence of an earlier solution.

No issue above invalidates the final theorem or leaves a necessary mathematical step unproved.

## Independent proof checks

### Stationary augmented law and cycle reward

ATTEMPT.md lines 35–51 and FULL_PROOF.md lines 17–36: I re-derived the stationary marked product law

    pi_n = (1-rho)rho^n H^{otimes n},
    H(db,dx) = F(db) 1_{0<x<b} dx/m.

Its mass is one. The class residual mean is mu_I=E[B^2 1_{B in I}]/(2m). For I contained in (b,2b], X_I is bounded by 2b and E X_I^2<=2b mu_I. Integrating the transport derivative over x from zero to the original mark gives the deletion endpoint minus the arrival endpoint. The latter cancels the incoming insertion term since pi's count weights satisfy p_n/m=lambda p_{n-1}; matching gamma coefficients are essential. Summing the deletion coefficients gives the other cancellation. Atomic service distributions cause no difficulty because residual integration is Lebesgue integration. This is the standard symmetric-queue product-form input with its marked extension checked explicitly; no independence of transient residuals is assumed.

At a subcritical rate every finite-workload state reaches empty, independently of gamma, by work conservation. The FCFS branching representation gives mean busy duration m/(1-rho). Including the idle interval yields E C=1/[lambda(1-rho)], so at the reference load 1-1/r it is r/lambda. Finite-mean regeneration identifies the stationary occupation law.

For a whole cycle and a bounded prearrival predicate f, marked Poisson compensation gives

    E Y_I(f) = lambda P(B in I) E integral_0^C f(X(s-)) ds
             = r P(B in I) pi(f).

Optional stopping is justified: the compensated counting martingale stopped at C has integrable quadratic variation lambda P(B in I) E C and is L2 bounded under bounded stopping. No second moment of C is needed. The first arrival ending the idle interval is included. The predicate is independent of the new mark. The occupation formula includes the idle interval, which is necessary for the coefficient r. This key identity has no additional empty-state-conditioning factor.

### One-sided collapse, interpolation and noncircular cutoffs

ATTEMPT.md lines 55–82, 108–119 and 155–157; FULL_PROOF.md appendix: for D=W-hQ, direct accounting gives

    D(v)>=D(u)-(v-u)-h[A(v)-A(u)].

Service costs at most elapsed time, an arrival jump is B-h>=-h, and departures increase D by h. Applying this inequality on both sides of a time between grid points gives both interpolation bounds; arbitrarily fast or simultaneous departures do not break them.

For iid stationary residuals with finite mean h, a negative Laplace transform gives exponential lower deviations for n<=Cr. For n>Cr, the workload cutoff S_n<=Kr gives the exponential bound exp(theta_0 Kr-kappa n). Choosing C first as in the text makes it uniform in n. The expansion of the centered negative Laplace transform uses only finite mean, not a residual variance.

Stationary conditioning costs exactly r, and a physical grid of spacing delta*r has O(r) points. Exponential errors survive both factors. Poisson interval counts supply an O(delta*r) interpolation budget with vanishing failure probability. The workload FCLT removes the workload cutoff. Thus (hQ-W)^+/r vanishes uniformly, and Q/r compact containment follows before the dyadic argument is invoked.

FULL_PROOF.md lines 49–53: busy starts have compensator lambda times the idle regulator. Stop when that regulator reaches ar; the stopped counting martingale has variance at most lambda ar. Since the scaled workload regulator is tight by reflection of the input FCLT, the number of started cycles divided by r is tight. This argument does not assume the sought queue-length diffusion theorem.

### Bounded original requirements

FULL_PROOF.md lines 57–71 and 180: the small-class residual summands under H lie in [0,2L], including zeros for other original sizes. Their exact mean is mu_small. Conditional on Q=n<=Cr, Hoeffding yields the displayed exp(-epsilon^2 r/(2CL^2)) bound. The stationary conditioning and grid union contribute O(r^2), still harmless for fixed L. The same deterministic interpolation inequality applies to D_small, and the already established queue cutoff removes the restriction n<=Cr. The varying threshold ell_r in [L,2L) does not require convergence of mu_small.

### Dyadic upcrossings and summation

ATTEMPT.md line 9 refers to FULL_PROOF.md sections 4–5; I checked every inequality there (lines 75–143).

For a class (b,2b], its workload decreases between class arrivals and begins every cycle at zero. Exceeding M=Cr mu+x on the global count cutoff implies a class arrival with prearrival V>M-2b and Q<=Cr. When x>=4b this forces V-n mu>x/2. This is a prearrival-state predicate, not a predicate involving the incoming mark.

For iid nonnegative bounded summands, the exponential-series estimate gives

    log E exp(theta(X-E X))
       <= theta^2 E X^2 / [2(1-2b theta/3)].

With z=x/2 and theta=z/(V_2+2bz/3), the resulting upper-tail exponent is x^2/[8(V_2+bx/3)]. Raw second moments bound variance; no untruncated residual second moment is used. The bound V_2<=(C/m)rbw follows from mu=w/(2m). Substituting b=r 2^{-(j+1)} and a_j=(1-2^{-1/4})2^{-j/4} gives a lower bound c 2^{j/2} for the exponent, uniformly in r and j. The condition x>=4b holds beyond a fixed j0; the finitely many remaining classes use probability at most one.

On the cycle-count cutoff all relevant arrivals lie in the first ceil(Ar)+1 whole cycles. Taking whole cycles, even beyond the horizon, only enlarges the event. A union bound on these deterministic cycle indices and the exact reward formula gives C_A r^2 p_j pi(f_j). There is no conditioning on the random cycle count and no independence assertion about that count and cycle rewards.

The bound r^2 p_j<=2^{2j+2}w_j is correct. For each fixed j, w_j tends to zero by integrability of B^2. The large-j bounds are dominated by

    C_A m2 2^{2j+2} exp(-c 2^{j/2}),

which is summable. Extending absent classes by zero makes ordinary countable dominated convergence applicable. This is valid even for sparse atomic laws with arbitrarily slow second-moment-tail decay; no uniform decay rate for w_j is smuggled in.

The remaining class B>r is controlled under the empty-start law by all original work arriving in that class. Its expected supremum divided by r is at most lambda T E[B^2 1_{B>r}], tending to zero. This step relies on empty start and would not address arbitrary preexisting large jobs.

Finally choose C and A using the independently established tightness, hold them fixed, and then choose L so C E[B^2 1_{B>L}]/(2m) is small. For each fixed L take r to infinity. The identity W-hQ=D_small+V_tail-(h-mu_small)Q bounds the positive discrepancy; the earlier one-sided bound controls its negative discrepancy. These choices yield the claimed two-sided uniform collapse with only E B^2 finite.

### General drift and process convergence

ATTEMPT.md lines 127–137; FULL_PROOF.md lines 148–152: the target and reference arrival rates differ by O(1/r). Direct evaluation of the Poisson likelihood-ratio second moment on H=r^2T gives

    E_0 L_r^2 = exp(H(lambda_r-lambda_r^0)^2/lambda_r^0),

bounded in r. Cauchy–Schwarz therefore transfers vanishing collapse probabilities for every real beta, including critical or supercritical target rates. Stationarity is used only at the subcritical reference rate. The marked requirements and insertion uniforms keep their laws.

The workload input FCLT has variance rate m2/m and drift -beta. Reflection and convergence together with uniform collapse give the asserted J1 limit. Its drift is -beta/h and variance rate m2/(m h^2); for exponential service these reduce to the standard birth–death coefficients. Extending over finite horizons gives D([0,infinity)) convergence.

## Historical arguments and independent computational checks

I also checked the earlier arguments in ATTEMPT.md. The fourth-moment proof uses E R^3=E B^4/(4m) and a valid Bennett bound. The LT and LT1 truncation proofs retain their advertised extra hypotheses. The finite-dimensional/L1 arguments use the source's empty-start marginal identity plus the one-sided ordering, and explicitly do not infer J1 convergence from these weaker facts. The sparse atomic example genuinely violates LT1 while having finite second moment. The Pareto example correctly gives residual tail 4/(27x^2) and interval coefficient 5/243, disproving only the old stationary concentration rate. The shrinking-dip example correctly illustrates failure of the weak-to-J1 inference. None of these earlier limitations is a counterexample to the completed regenerative proof.

Independent calculations are in check_audit.py and independent_checks.json:

- Exact rational integration of the constant-service stationary predicate gives cycle reward 552032/703125.
- Exact binomial/Irwin–Hall integration for the original-size class {9} gives 58589088764/373669453125. Both reproduce the claimant's predictions without using its simulation code.
- A marked-workload Laplace-generator balance check for the two-atom law, at four transform parameters, has maximum floating-point residual 2.50e-18.
- The dyadic exponent algebra passes 2,700 numerical parameter combinations.
- The Pareto interval-tail coefficient checks exactly as 5/243.

These computations check formulas and arithmetic; the proof of the universal theorem is the analytic argument above. I have not claimed an independent universal simulation test or formalized stochastic proof.

## Bounded literature search and what is not established

I fetched the source from https://arxiv.org/pdf/2202.02366 and saved source.pdf and source.txt. I independently queried the arXiv API for "symmetric queues" and for "symmetric queue" OR ("service disciplines" AND "heavy traffic"); responses are arxiv_search.xml and arxiv_broad.xml. The first query returns the source and an unrelated two-queue shortest-queue-first analysis. The broader query returns 14 records, including the known PS paper, but no abstract identifying a solution of the exact arbitrary-gamma question or a counterexample to it. The source itself explicitly distinguishes the known PS/LCFS cases from Problem 1.

The OpenAlex works query for symmetric queues heavy traffic returned HTTP 429; fetch_log.json records this limitation. These bounded searches establish neither novelty nor continued openness independently of the submitted proof. This is a PASS for a checked new proof in the records, not SOLVED_IN_LITERATURE. No infinite-variance theorem, renewal-arrival theorem, or arbitrary-initial-state theorem is proved by this audit.

All created files are inside the assigned audit directory. The claimant's records were read only.
