# Independent audit of the positive-service Whitt counterexample

Auditor: heat_entropy agent. Date: 2026-10-02.

**Conclusion: PASS.** I independently checked the stochastic model, the
occupation identity, the tail domination, the exact block elimination, and the
convex-order coupling in `whitt_positive_service_exact.py`. I also ran the exact
Fraction certificate successfully. This audit establishes the stated
inequality, conditional on the elementary finite-CTMC and queue coupling facts
proved below; it does not assert publication priority.

## Model and convex order

Both systems are FCFS M/G/2 with Poisson arrival rate 11/10. The base service is
E/5 with probability 3/7 and 8E/5 with probability 4/7, where E is unit-rate
exponential. The spread service is E/1000 with probability 3/14, 399E/1000
with probability 3/14, and 8E/5 with probability 4/7. Their means are exactly 1,
so their load is 11/20 and they are stable. Every service is strictly positive.

Use the same latent branch and exponential E in a coupling. On the short base
branch, choose either E/1000 or 399E/1000 equiprobably; their conditional mean
is E/5. On the long branch keep the service unchanged. Therefore
E[T | S, latent branch] = S and hence E[T | S] = S. Jensen's inequality proves
S <=cx T, and in particular S <=icx T.

## Markov phases

The service branch of each queued customer may be drawn at its service-start
time: because these branch draws are independent and do not affect a customer
before service, this constructs the same queue law. At count one the phase is
the active exponential branch. At counts at least two the phase is the
unordered pair of active branches. A memoryless phase with rate mu[a] departs
at precisely that rate.

An arrival at count zero draws a phase with probabilities p. An arrival at
count one draws the second phase. Arrivals at counts at least two only
increment the count. A departure at count two leaves the other phase; at
counts at least three it replaces the departing server's phase by an
independent p draw and decrements the count. For repeated phases the two
slots both contribute, giving the required factor two. These transitions
agree with every A/B/C block in the script. The only removed transitions are
arrivals at count N, which kill the process at rate lambda; all finite-set
rows consequently sum to -lambda at count N and zero elsewhere.

## Exact finite system and its interpretation

Let F be all phases at counts 0,...,N and A=-Q_FF the killed-chain matrix. The
two reward columns are 1 and b=1_{count >= 2}. The block elimination computes
h=A^{-1}[1,b]. The script checks A h=[1,b] in exact Fraction arithmetic after
back-substitution, independently of the elimination steps. The two columns
are expected total occupation and expected busy occupation before killing.
The finite killed chain exits almost surely and has finite mean exit time:
uniformly over its finitely many states there is a positive probability of
N+1 consecutive arrivals before any departure, within a bounded interval.
Thus A is invertible and this occupation interpretation is valid.

Let pi be the stationary row law of the full stable chain. Write delta for
pi(F^c), and eta=pi_Fc Q_Fc,F for the stationary incoming flux into F. The
stationary equations give pi_F A=eta, hence

    pi_F 1 = eta h_total,    pi_F b = eta h_busy.

The only jumps from outside F into F are departures from count N+1 to N.
Consequently eta is supported on count N. The stationary conditional busy
probability rbar = pi_F b / pi_F 1 is a convex combination of the entry-state
ratios h_busy(N,phase)/h_total(N,phase), weighted by
eta(phase) h_total(N,phase). It lies between the minimum and maximum ratios.
All states outside F are busy, so the full delay probability is exactly

    P_delay = (1-delta) rbar + delta.

Therefore min(ratios) is a valid lower bound, and if delta <= tau then
max(ratios)+tau*(1-max(ratios)) is a valid upper bound. These are the script's
bounds. In particular, the sharper positive-service lower bound does not
need the extra factor 1-tau appearing in the older zero-service script.

## Tail bound

All phase rates are at least mu_min=5/8. Couple each iid service to an iid
Exp(5/8) service using the same unit exponential multiplier and branch draw.
The original service is no larger, customer by customer. The FCFS
Kiefer-Wolfowitz recursion is coordinatewise monotone in the sorted workload
vector and service amount. With common arrivals and empty initialization it
gives no later service starts in the original system; together with the
smaller individual services it gives no later departure time for every
customer. Thus the original number in system is no larger at each time.
Taking stationary limits gives the same order for stationary counts.

For the slow M/M/2 queue, rho=lambda/(2 mu_min)=22/25 < 1. Its delay
probability is 2*rho^2/(1+rho); the count tail above N>=2 is that probability
times rho^(N-1). For N=80 the resulting exact rational tau is approximately
0.0000338819650833609985499114781245524662539399519. The formula's exponent
is correct: the conditional tail from count two onward is geometric, and
count>N means count at least N+1.

By PASTA, the probability an arrival must wait until beginning service equals
the stationary probability count>=2, so this occupation calculation is the
quantity in Whitt's conjecture.

## Exact outcome

The successful run produces

    P_delay(base) >= 0.392872619378512420636667195074272856376960069
    P_delay(spread) <= 0.391744304986939526115032326588501813484907617

The decimals are only displays of rational bounds. The actual decision is
the exact assertion

    P_delay(base) - P_delay(spread) > 1/1000.

The displayed gap lower bound is
0.00112831439157289452163486848577104289205245201.

The reversal also holds at a positive waiting-time threshold without further
matrix computations. In the base system, the total completion hazard of the
two currently active servers is at most 10. On {W>0}, beginning service by
time t requires at least one current service completion by t. Thus
P(0<W_base<=t) <= 1-exp(-10t) <= 10t. Since
P(W_spread>t) <= P(W_spread>0), the certified gap implies

    P(W_base>1/20000) - P(W_spread>1/20000) > 1/2000.

This strict stochastic-order violation is at a strictly positive threshold.

## Original conjecture's scope

Whitt, *Comparison conjectures about the M/G/s queue*, Operations Research
Letters 2(5), 203-209 (December 1983), DOI
10.1016/0167-6377(83)90026-3, Conjecture 1.1 states that increasing convex
order of service distributions implies stochastic order of equilibrium
waiting times until beginning service. The introduction specifies iid
service, independent renewal arrivals, homogeneous parallel servers,
unlimited waiting room, and FCFS. All apply here. The original conjecture
also permits zero service: section 6 explicitly considers mixtures with a
point mass at zero, but the audited version needs no such atom.

Primary source:
https://www.columbia.edu/~ww2040/comparisonConjectures1983.pdf

I searched two engines for exact-name/convex-order/M/G/2/M/G/s counterexample
and status terms, and found no prior resolution. This is a bounded literature
search, not a proof that the result is unpublished.
