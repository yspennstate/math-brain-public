# Hostile referee audit, 11 October 2026

This audits FULL_PROOF.md rather than inferring convergence from marginal laws or simulations. The mathematical checks below pass. The stationary-law source check, independent numerical diagnostics and successful corrected Lean execution are all recorded. The final verdict is SOLVED.

## 1. Exact scope

The rule is precisely the source's fixed positional symmetric array: insertion probabilities equal the service shares at the enlarged queue size. Arrivals and insertion randomization are independent of iid service marks. The service law is fixed, positive mean, finite second moment; the initial state is empty. No lower bound on service shares, extra moment, regular tail envelope, or PS/LCFS restriction occurs in the new argument. The target is J1 process convergence, not only marginal convergence. The reference rate is subcritical; finite-horizon change of measure covers every real beta, including negative beta.

## 2. Marked stationary law

The proposed law is a product of H(db,dx)=F(db)1_{0<x<b}dx/m at a geometrically distributed count. It retains ORIGINAL service requirement, not merely residual work. Its total mass is one because the integral of b against F is m. For a class I its mean residual contribution is E[B^2 1_I]/(2m). Atoms in F cause no difficulty: integration in residual x is with Lebesgue measure and integration in b is with F.

The service endpoint at x=b creates exactly the incoming original mark b. Its weight p_n/m equals lambda*p_{n-1}, and its positional coefficient is gamma(n,i), exactly the arrival insertion coefficient. At x=0 the mark disappears; integrating it out has coefficient integral F(db)/m=1/m. Summing positional coefficients produces the remaining cancellation. Thus the marked balance is correct. The proof uses the standard symmetric-queue product-form invariance theorem, with this explicit marked extension; formal generator cancellation alone is not substituted for an invariance theorem.

Regeneration supplies uniqueness: a finite initial workload hits empty almost surely at a subcritical rate. Empty-to-empty cycles have finite mean. Consequently the regenerative occupation measure equals the stationary product law. Zero marks may be removed: insertion followed by immediate deletion restores the order of all existing jobs; thinning preserves rho, h and m2/m.

## 3. Cycle length and the factor of r

Cycles include the idle interval and the entire subsequent busy period. Work conservation makes the busy period independent of the discipline. The FCFS branching representation gives mean busy duration m/(1-rho), hence E C=1/(lambda(1-rho))=r/lambda at the reference rate. Omitting the idle interval would give the wrong occupation formula.

For any bounded prearrival predicate f and original mark class I, compensation at the cycle stopping time gives E Y=lambda*p_I E integral_0^C f(X(s-))ds. The stopped compensated counting martingale is L2 bounded because its expected quadratic variation is at most lambda*p_I E C. Therefore optional stopping is legitimate. Regenerative occupation then gives E Y=r*p_I*pi(f), exactly, not r^2*p_I*pi(f). A first arrival after the idle interval is included; arrivals at the busy-period ending time have probability zero. Left limits do not change the time integral.

The horizon event is enlarged to the first ceil(Ar)+1 WHOLE cycles. Those cycles need not end before the horizon. A union bound on their identical distributions is valid without conditioning on the random horizon cycle count or claiming its independence from rewards. This removes the extra factor of r that spoiled the old stationary-grid treatment of unbounded residuals.

## 4. No circular compact containment

The one-sided collapse in ATTEMPT.md needs only the finite mean h of an equilibrium residual. It uses a negative Laplace transform, a workload cutoff, O(r) grid points, and the explicit factor r for conditioning stationary time zero to empty. Exponential errors survive both factors. The deterministic bridge is valid even when shares vanish or departures are simultaneous.

Then sup Q/r <= sup W/(hr)+o_P(1), yielding compact containment without any PS marginal identity or assumed queue-length limit. Workload and its idle regulator converge by the input FCLT and reflection. Busy starts have compensator lambda*I; stopping when I reaches ar gives variance O(ar). Thus N/r is tight. Both inputs precede the dyadic argument and neither depends on its conclusion.

## 5. Upcrossings and stationary concentration

Each class workload decreases between class arrivals and starts at zero in every cycle. A first exceedance of M=Cr*mu+x must occur at a class arrival with prearrival V>M-2b. On the compact-containment event its prearrival count is at most Cr. The predicate depends only on the prearrival state, so the new arrival's mark remains independent. Departures carry zero residual work and cannot cause a positive jump of class workload.

For x>=4b, this predicate forces V-n*mu>=x/2. Given stationary count n, the summands X are independent in [0,2b], with E X^2<=2b*mu. Bernstein therefore bounds the predicate by exp[-x^2/(8(V_2+b*x/3))], where V_2=n E X^2. The inequality uses an upper bound on the raw second moment, which also bounds the variance; it does not assume a finite untruncated residual second moment. The zero-variance and n=0 cases have no positive upper deviation.

For clarity, Bernstein follows directly from e^(theta X)-1-theta X <= E-series bound: k! >= 2*3^(k-2) for k>=2, and X^k <= (2b)^(k-2)X^2. Thus log E e^(theta(X-EX)) <= theta^2 E X^2/[2(1-2b*theta/3)] for 2b*theta<3. Multiply independent transforms and optimize at theta=z/(V_2+2b*z/3), z=x/2. If V_2=0 the deviation is impossible and needs no optimization.

With a_j=(1-2^(-1/4))*2^(-j/4), the ratio x/(4b) is epsilon*(1-2^(-1/4))*2^(3j/4-1), so the required inequality holds for every j beyond a fixed j0. Also V_2 <= (C/m)*r*b*w_j. Using w_j<=m2, the exponent is at least c*2^(j/2), uniformly in r and j. The finitely many smaller j use probability at most one.

## 6. Dominated convergence is genuinely uniform over classes

The whole-cycle bound is (ceil(Ar)+1)*r*p_j*pi(f) <= C_A*r^2*p_j*pi(f). Since B>b on the class, r^2*p_j <= 2^(2j+2)*w_j. For every FIXED j, w_j <= E[B^2 1_{B>r*2^(-(j+1))}] tends to zero. For large j the bounds are dominated by C_A*m2*2^(2j+2)*exp(-c*2^(j/2)), a summable sequence independent of r and L. Extending the absent classes by zero permits ordinary countable dominated convergence. The finitely many small j vanish individually. Sparse atomic tails are covered: no rate for w_j is assumed.

The remaining class B>r is bounded directly by total original work arriving after time zero. Its expected scaled work is lambda*r*T E[B 1_{B>r}] <= lambda*T E[B^2 1_{B>r}], tending to zero. This step would fail with arbitrary large preexisting marks; empty start is essential.

## 7. Order of limits and completion

Choose count and cycle cutoffs C,A using the already proved tightness bounds. Fix the error budget epsilon. For every fixed L, the bounded-original-size discrepancy vanishes uniformly; its changing threshold ell_r stays in [L,2L], so concentration constants are uniform. The dyadic exceedance probability tends to zero for the fixed cutoffs. Their sum is at most C E[B^2 1_{B>L}]/(2m)+epsilon. Now take L large. There is no interchange requiring a uniform stationary second moment or an unproved tail rate.

The identity W-hQ=D_small+V_tail-(h-mu_small)Q bounds its positive part by |D_small|+V_tail. The previously proved negative-part bound finishes two-sided uniform collapse. The Poisson likelihood ratio has exact second moment exp[H(lambda-lambda0)^2/lambda0], bounded for H=r^2 T and rate difference O(1/r). This transfers collapse, and workload convergence gives the required J1 limit by convergence together. The constants reduce to drift -beta/h and variance m2/(m*h^2); exponential services give variance 2*mu, the birth-death value.

## 8. Independent cycle diagnostic

check_regeneration.py simulated 32,000 complete M/D/1 cycles, lambda=0.8, in 1.79 seconds. The predicate is prearrival Q<=6 and W>=2; all arrivals are in the mark class. Independent Irwin-Hall calculation under the stationary residual product law gives pi(f)=552032/3515625. Here r=5, so the exact predicted mean reward is 552032/703125=0.7851121777777778.

| Rule | Cycles | Observed mean | Estimated SE | Deviation / SE |
|---|---:|---:|---:|---:|
| PS | 8000 | 0.794875 | 0.0262452 | 0.372 |
| Middle-only | 8000 | 0.825750 | 0.0285755 | 1.422 |
| Alternating ends | 8000 | 0.763500 | 0.0269393 | -0.802 |
| Equal end shares | 8000 | 0.777875 | 0.0265247 | -0.273 |

All four agree within 1.43 estimated standard errors. The numerical check supports the cycle-reward identity but is not a proof or a universal simulation test. The earlier 288-path diagnostic tested the deterministic bridge over 246,346 events, with minimum slack -3.6e-15 (roundoff).

## 9. Formal-check status

Additional marked diagnostic: check_marked_cycles.py ran another 32,000 complete cycles with B=1 of probability .9 and B=9 of probability .1, lambda=4/9. It counted B=9 arrivals with prearrival Q<=6 and residual workload in the ORIGINAL-size class {9} at least 5. Under H, the probability of class {9} is 1/2, with conditional residual Uniform(0,9). The exact binomial/Irwin-Hall computation is
pi(f)=sum_{n=1}^6 (1/5)(4/5)^n sum_{k=1}^n binom(n,k)2^-n[1-(5/9)^k/k!]
=117178177528/373669453125.
Since r*p_I=1/2, E Y=58589088764/373669453125=0.1567938943738084. Observed means for PS, middle-only, alternating ends and equal ends were respectively .152125, .151000, .150125 and .163250; all differences are within .73 estimated standard errors. Runtime was 30.89 seconds. This tests the immutable original marks and matching insertion probabilities separately from the constant-service diagnostic. Again it is supporting numerical evidence only.

The author's online Kelly archive was fetched and confirms the standard reference and 1979 edition. Chapter 3 downloaded as a 38-page scan with no extractable text; no exact theorem quotation or page number from that scan is asserted. The proof's stationary-law input is the classical symmetric-queue product form, with the marked balance verified explicitly above. All requests and this limitation are in LITERATURE.md. This archive check found no mathematical contradiction or changed hypothesis.

GridBridge.lean formalizes only the scalar grid interpolation and its arrival-budget variant, not the stochastic theorem. The first execution failed because Real.Basic was missing; its output is preserved in lean_check_initial.txt. The corrected execution from the preceding turn left no retrievable completion log and no matching P0391 process. It was restarted sequentially on 11 October, with selective Real.Basic and Linarith imports and the requested hour timeout. The corrected run finished with exit code 0 in 1754.54 seconds; output is in lean_check.txt. The check uses ordinary Lean kernel verification, with no sorry or native_decide. No failed run is counted as passed.

## Final conclusion

No mathematical gap has been found in the regenerative dyadic argument. The stationary-law reference check is recorded above, including the scan's extraction limitation. The corrected formal execution passed. The universal finite-second-moment theorem is proved in FULL_PROOF.md; no mathematical gap remains identified by this audit. No exact published solution to P0391 has been verified by the literature searches.
