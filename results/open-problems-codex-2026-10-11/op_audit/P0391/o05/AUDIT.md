VERDICT: PASS

# Independent audit of P0391

Date: 11 October 2026. I read the claimant's STATUS.md, ATTEMPT.md, all 13 records in CLAIMS.jsonl, and LITERATURE.md. Since ATTEMPT.md explicitly delegates its final theorem to FULL_PROOF.md, I also read that entire proof and REFEREE.md. The verdict rests on an independent mathematical check, not on the claimant's own referee verdict, simulations, or Lean log. All audit artifacts were written in this audit directory; the claimant directory was read only.

## Exact claim and correspondence with the problem

ATTEMPT.md:5–9 and CLAIMS.jsonl:12 claim the following. Let B have a fixed nonnegative service law with m=E[B]>0 and m2=E[B^2]<infinity. Arrivals are Poisson with rate lambda_r and independent iid service marks. For every fixed positional array gamma(n,i)>=0 with sum_i gamma(n,i)=1, service shares at size n are gamma(n,i) and arrivals insert with probabilities gamma(n+1,i). Starting empty, if r(1-lambda_r*m)->beta for any real beta, then

    Q_r(r^2 .)/r => Gamma(sqrt(m2/m)*Brownian(.)-beta*.)/h,
    h=m2/(2m),

in the J1 topology on D([0,infinity)). The stronger intermediate claim is uniform state-space collapse on each finite horizon:

    sup_{s<=r^2*T} |W_r(s)-h*Q_r(s)|/r -> 0 in probability.

I independently downloaded https://arxiv.org/pdf/2202.02366 and extracted its text into source.txt. PDF page 1 gives exactly the matching insertion/service definition and finite-second-moment heavy-traffic regime. PDF page 2 states Problem 1, allows a real heavy-traffic constant, and explains the empty-start caveat for universal marginals. The claim answers the user-specified empty-start version. It covers arbitrary gamma, including zero shares; neither an additional service moment nor a tail regularity assumption remains in the final proof. It asserts process convergence, not just marginal convergence, and is not a PS/LCFS special case.

The limit has drift -beta/h and variance rate m2/(m*h^2). Two independent consistency checks are useful: exponential services give h=m and variance rate 2/m, agreeing with the M/M/1 birth-death limit; for beta>0 the stationary mean of the proposed queue-length RBM is 1/beta, agreeing with geometric queue-length scaling.

## Issues found

1. **Stale historical wording, without a mathematical effect.** ATTEMPT.md:303 says that the “final full-process theorem” retains the extra LT1 envelope. That sentence conflicts locally with the actual final theorem at ATTEMPT.md:5–9 and FULL_PROOF.md. ATTEMPT.md:11 and 31 explicitly say the older sections are historical and superseded, so it does not restrict or invalidate the final claim. The editorial fix is to label line 303 as describing the earlier LT1 theorem. Similarly, line 276's “not yet controlled” belongs to the explicitly historical section starting at line 272.

2. **Literature and formal-verification limits are accurately bounded, not proof gaps.** ATTEMPT.md:9 does not claim a literature solution or formal verification of the stochastic theorem. I verified the two scalar statements in GridBridge.lean directly by real inequalities and inspected the saved successful execution log, but did not rerun Lean. The simulation standard errors are diagnostics, not universal estimates. No part of my mathematical verdict uses their statistical agreement.

No failing mathematical step or remaining mathematical repair was identified in the final proof. The earlier unsuccessful finite-second-moment concentration approach is explicitly abandoned rather than silently reused.

## Independent check of the final proof

### 1. Marked stationary law and well-defined dynamics

Location: ATTEMPT.md:35–51 and 9; FULL_PROOF.md:17–27.

The crucial extension retains each job's original B, not merely its residual x. I checked

    H(db,dx)=F(db)*1_{0<x<b}*dx/m,
    integral H=1,
    E_H[x*1_{b in I}]=E[B^2*1_{B in I}]/(2m).

If I is contained in (a,2a], then x*1_I is bounded by 2a and its raw second moment is at most 2a times its mean. These facts require no third or fourth moment.

For a deletion-compatible test function, integrating the service derivative in x from 0 to b gives the deletion endpoint minus the insertion endpoint, each with factor F(db)/m. At level n the latter cancels births from level n-1 since p_n/m=lambda*p_{n-1}, with exactly the same coefficient gamma(n,i). Integrating the deleted original mark and summing the shares at level n+1 cancels the negative arrival term at level n. This verifies the augmented balance, including atomic F and zero service shares. The argument uses the standard symmetric-queue stationary product form, not an assumption that transient residuals are independent.

There is no explosion: on a finite time interval there are finitely many arrivals, and each deletion removes one of the finitely many initial or arriving jobs. The subcritical workload reaches empty almost surely, so empty regeneration identifies the stationary occupation law uniquely. Removing zero-service arrivals restores the existing order immediately and preserves rho, h, and m2/m. This reduction does not discard a positive-service case.

As an additional exact test, audit_checks.py verifies augmented-generator cancellation for three bounded deletion-compatible product test functions under B=1 with probability .9 and B=9 with probability .1. All three residuals are exactly zero as rational numbers. This corroborates, but does not replace, the general endpoint calculation.

### 2. Cycle length and marked reward

Location: ATTEMPT.md:9; FULL_PROOF.md:29–36.

A cycle includes both its initial idle time and its complete busy period. Work conservation makes the busy-period workload independent of gamma. The subcritical branching representation gives mean busy duration m/(1-rho); adding 1/lambda gives E[C]=1/[lambda*(1-rho)]=r/lambda at the reference load 1-1/r.

For a prearrival state predicate f and an independent arrival class I, compensation gives

    E[Y_I(f)] = lambda*p_I*E[integral_0^C f(X(s-)) ds]
              = lambda*p_I*E[C]*pi(f)
              = r*p_I*pi(f).

I specifically checked optional stopping: the stopped compensated marked counting process has expected quadratic variation at most lambda*p_I*E[C]<infinity. Its bounded stopping approximations are L2 bounded, which justifies the expectation identity. The initial arrival is included, and left limits do not affect occupation integrals. There is no omitted conditioning factor and no mistaken factor r^2 per cycle.

### 3. Workload, one-sided collapse, and cycle count

Location: ATTEMPT.md:39, 55–82, 106–131 and 155–157; FULL_PROOF.md:40–53 and 156–178.

Work conservation gives the exact reflected compound-Poisson workload. Finite m2 supplies variance rate lambda_r*m2->m2/m and scaled drift -beta. The workload and unused-service regulator FCLTs require no queue-length theorem.

I re-derived the uniform lower-deviation estimate for iid equilibrium residuals. For n>Cr, the event S_n<=Kr is exponentially small by a negative Laplace transform. For n<=Cr, E[R]=h implies log E[exp(-theta*(R-h))]=o(theta), yielding an exponential bound on S_n-hn<-eta*r. Mixing over stationary n costs no additional factor. Conditioning on an initially empty stationary state costs exactly r; the physical grid has O(r) points. Thus the exponential error survives both factors.

The deterministic bridge

    D(v)>=D(u)-(v-u)-h*(A(v)-A(u))

is valid because service decreases workload at rate at most one, arrivals contribute at least -h, and departures increase D. Applying it to both halves of a grid interval gives D(u)-b<=D(t)<=D(v)+b. In particular, arbitrarily rapid departures do not defeat the upper bound, which uses the following grid point. Poisson interval-count deviations are exponentially small. This proves the one-sided collapse and then compact containment of Q/r without circularly assuming the final result.

Busy starts satisfy N(t)=integral 1_{W(s-)=0} dA(s), with compensator lambda*I(t). Stopping when I first reaches a*r gives martingale variance at most lambda*a*r. Consequently

    P(|N(t)-lambda*I(t)|>epsilon*r)
    <= P(I(t)>a*r)+lambda*a/(epsilon^2*r).

The tight regulator therefore implies N(r^2*T)/r is tight. This is the independent justification for counting only O_P(r) cycles.

### 4. Small original requirements

Location: ATTEMPT.md:9; FULL_PROOF.md:57–71 and 180.

With ell_r in [L,2L), the stationary summands x*1_{B<=ell_r} are iid bounded by 2L, with the stated mean mu_small. For n<=Cr, Hoeffding gives the displayed exponent -epsilon^2*r/(2*C*L^2). The grid and stationary-empty conditioning again cost only O(r^2), so the error vanishes exponentially. The same deterministic bridge applies because small-class work has total service loss at most one, arrival changes at least -mu_small, and deletion changes +mu_small. Compact containment on the enlarged grid horizon removes the count cutoff. The varying ell_r causes no problem because the bounds are uniform on [L,2L).

### 5. Dyadic upcrossings: the decisive endpoint argument

Location: ATTEMPT.md:9 and 31; FULL_PROOF.md:75–115.

For each original-size band I=(b,2b], class workload starts at zero in each cycle and increases only at class arrivals, by at most 2b. An exceedance of M=Cr*mu+x on the count cutoff therefore requires a class arrival whose prearrival state has Q<=Cr and V_class>M-2b. This is a predicate of the old state; it is independent of the new service mark. Departures remove zero residual work and cannot create an upcrossing.

When x>=4b, that predicate implies V_class-n*mu>=x/2. With raw second-moment sum V_2<=2b*n*mu, the exponential-series Bernstein calculation yields

    pi(predicate)<=exp(-x^2/[8*(V_2+b*x/3)]).

I checked the factor 8 and the b*x/3 term directly by substituting z=x/2 into the bound with individual bound 2b. The zero-variance case is empty. Using a_j=(1-2^(-1/4))*2^(-j/4), x=epsilon*r*a_j and b=r*2^(-(j+1)), its exponent is at least

    c*2^(j/2),
    c=epsilon^2*(1-2^(-1/4))^2/[4*((C/m)*m2+epsilon/3)]>0.

The requirement x>=4b holds above a fixed j0. Neither j0 nor c depends on r, L, or a tail decay rate.

On N(r^2*T)<=Ar, enlarging to the first ceil(Ar)+1 whole cycles is legitimate, even when their endings exceed the horizon. Union bounding their identical laws and using the exact reward gives a bound C_A*r^2*p_j*pi(predicate). No independence from the random horizon cycle count is assumed. Since B>b,

    r^2*p_j<=2^(2j+2)*w_j,
    w_j=E[B^2*1_{B in I_j}].

For each fixed j, w_j->0 by finite m2. For all larger j, the bound is dominated by a constant times

    m2*2^(2j+2)*exp(-c*2^(j/2)),

which is summable. Extending missing bands by zero justifies ordinary countable dominated convergence. This is valid for sparse atomic tails as well as regular tails. The finitely many j below j0 vanish using w_j->0 alone.

Independent exact-distribution tests used a mixture of a zero summand and Uniform(0,9), as furnished by the two-atomic original-size class under H. All 1,800 rational Irwin-Hall/binomial tail calculations satisfy the claimed Bernstein bound. The largest probability/bound ratio was 0.4712564301601278. An additional 2,560 parameter checks verified the explicit dyadic exponent constant. The proofs above, rather than the finite tests, justify the universal estimates.

### 6. Large arrivals, limit order, and completion

Location: ATTEMPT.md:5–9; FULL_PROOF.md:120–152.

For B>r, empty start gives the pathwise bound by total original large-arrival work. Its scaled expectation is lambda*r*T*E[B*1_{B>r}], at most lambda*T*E[B^2*1_{B>r}]->0. No stationary conditioning factor applies to this bound.

On the complement of the dyadic exceedances, total intermediate-band work divided by r is at most C*E[B^2*1_{B>L}]/(2m)+epsilon. The correct limit order is to choose the count and cycle cutoffs by previously proved tightness, choose the error allocation, take r->infinity for fixed L, and then increase L. This proves uniform vanishing of large-original-size work. The identity

    W-hQ=D_small+V_tail-(h-mu_small)*Q

bounds the positive discrepancy by |D_small|+V_tail. Together with the previously established negative discrepancy, it proves the full uniform collapse.

For arbitrary real beta, lambda_r-lambda_r^0=O(1/r). The Poisson likelihood ratio on H=r^2*T has exact second moment

    E_0[L_r^2]=exp(H*(lambda_r-lambda_r^0)^2/lambda_r^0),

which is bounded. Cauchy–Schwarz transfers vanishing collapse probabilities to critical and supercritical target sequences as well. No stationary law is asserted for those target sequences. The target workload FCLT and uniform collapse then give J1 convergence to the continuous RBM on every compact interval and hence on [0,infinity).

## Historical arguments and supporting claims

I also checked the older arguments in ATTEMPT.md rather than treating their previous limitations as a failure of the final proof. The fourth-moment route uses E[R^3]=E[B^4]/(4m), and its residual-tail union bound is genuinely o(r^-2). The Bennett truncation exponent and the O(r^2) grid/conditioning cost agree. The two logarithmic-tail extensions correctly keep their additional assumptions; their exponent/log r limits are -6 and -5 respectively. The weighted-tail monotonicity implication at lines 258–261 is valid.

The finite-dimensional argument at lines 143–147 correctly combines one-sided ordering with equal marginal laws; the bounded strictly increasing test function forces equality of the joint limiting coordinates. The occupation/L1 argument does not silently assert tightness in J1. The shrinking-dip example at lines 309–311 indeed has vanishing L1 error and deterministic-time errors, but a nonvanishing uniform error, so its stated obstruction is valid.

The sparse atomic example at lines 263–267 has finite second moment and violates LT1. The Pareto example at lines 280–285 has residual tail 4/(27*x^2); its band probability is exactly 5/(243*epsilon^2*r^2), producing an order-1/r lower bound after summing disjoint events. These refute auxiliary shortcuts, not the final diffusion theorem.

I independently recomputed both diagnostic stationary probabilities and cycle rewards using rational arithmetic. They equal 552032/3515625 and 552032/703125 in the deterministic case, and 117178177528/373669453125 and 58589088764/373669453125 in the marked case. The saved simulation means and standard errors are consistent with the stated comparisons. I did not rerun the claimant's Monte Carlo paths, and agreement would not prove convergence in any event.

## Fresh bounded literature search and limits of the conclusion

All web requests used Python urllib; no built-in web search or image tool was used. The source PDF fetch succeeded. A fresh arXiv query for symmetric queues and symmetric-queue diffusion returned the source and an unrelated two-queue shortest-queue-first analysis. A broader query for symmetric heavy traffic or service disciplines in heavy traffic returned 16 records. I inspected their abstracts: the PS diffusion paper, modulated/DPS stationary limits, FCFS multiclass systems, polling models, SBP steady-state methods, and the newer two-server JSQ convergence-rate paper do not assert the requested arbitrary positional-symmetric M/G/1 process theorem. Crossref's 30-result query likewise supplied no exact universal solution. OpenAlex returned HTTP 429, which is a failed search, not evidence of an empty literature.

The exact URLs, responses, abstracts and failure are retained in literature_checks.json, broader_literature.json and the corresponding response files. Independent computational checks and their script are math_checks.json and audit_checks.py. This search verifies neither priority nor exhaustive current openness. It found no earlier solution or counterexample to the exact claim in the inspected material.

The proved result is the universal empty-start Poisson M/G/1 finite-second-moment diffusion theorem stated above. This audit does not establish the infinite-variance Problem 2, general renewal arrivals, arbitrary non-symmetric disciplines, or an unrestricted nonempty-initial-state theorem. The probabilistic theorem is not Lean-formalized. Within the requested scope, the written proof is correct and complete.
