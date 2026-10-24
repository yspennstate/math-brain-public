# A strictly positive service counterexample to Whitt's stochastic comparison

2026-10-02. Status: complete computer-assisted proof with exact rational arithmetic. The simpler zero-atom version has also been proved using a different, matrix-geometric certificate and independently audited. Priority and the conjecture's present literature status are unverified: searches located no prior refutation. This is a longstanding queueing comparison, not a solution of FEI, Sidorenko, or a major K-theory conjecture.

## Statement and scope

Ward Whitt, *Comparison conjectures about the M/G/s queue*, Operations Research Letters 2 (1983), 203–209, DOI [10.1016/0167-6377(83)90026-3](https://doi.org/10.1016/0167-6377(83)90026-3), Conjecture 1.1, asserts that increasing the iid service-time law in increasing convex order increases the stationary FCFS waiting-time law in usual stochastic order, with the same Poisson arrivals and homogeneous parallel servers. The [author-hosted primary paper](https://www.columbia.edu/~ww2040/comparisonConjectures1983.pdf) states the conjecture on its first page.

Here is a counterexample with two servers, arrival rate 11/10, strictly positive service times, and all moments finite. Let E have the exponential distribution of mean one, independent of the service class. Set

| Service law | Exponential multiplier | Probability |
|---|---:|---:|
| S | 1/5 | 3/7 |
| S | 8/5 | 4/7 |
| T | 1/1000 | 3/14 |
| T | 399/1000 | 3/14 |
| T | 8/5 | 4/7 |

Every multiplier means that the service is that multiplier times E. Both means are one, so both utilization levels are 11/20. To couple the laws, sample the class and E for S. On the small class replace E/5 by E/1000 or 399E/1000 with equal probabilities; on the large class leave the service unchanged. Conditional on the class and E, the mean of T is S, hence also E[T|S]=S. Jensen's inequality therefore proves S <=cx T, and consequently S <=icx T.

Nevertheless, the exact certificate proves

    .39287 < P(W_S > 0) < .39290,
    .39172 < P(W_T > 0) < .39175,
    P(W_S > 0) - P(W_T > 0) > 11/10000.

These inequalities contradict the conjectured stochastic order. They compare actual infinite-capacity, stationary FCFS queues. No finite-buffer approximation is substituted for the queue.

## Phase chain

For a service mixture with k classes, probabilities p_a and exponential rates mu_a, a job's class may be sampled when it begins service. Its pre-service wait does not depend on its own service class, so this generates the same iid service law. Use the following continuous-time Markov states:

- Count 0: one empty state.
- Count 1: the k possible classes of the job in service.
- Each count n >= 2: the unordered pair (a,b) of the two classes in service; the other n-2 jobs are waiting.

Arrivals have rate lambda and raise the count by one. If fewer than two servers are busy, an arrival chooses its class with probabilities p. At count n >= 3, a completion at a server of class a occurs at rate mu_a, lowers the count by one, and replaces that server's class by a fresh independent class with probabilities p. At count 2, the completion simply leaves the other job in service. The diagonal is minus lambda minus the sum of the rates of the busy servers. If the two classes coincide, the two completion rates add. These rules fully specify the infinite generator Q; transition rates are uniformly bounded.

The baseline has k=2, p=(3/7,4/7), mu=(5,5/8). The spread has k=3, p=(3/14,3/14,4/7), mu=(1000,1000/399,5/8). Both have lambda=11/10. By PASTA, a stationary arrival waits strictly positively if and only if it sees two busy servers. Thus the desired probability is the stationary probability that the count is at least 2.

## A rigorous finite computation for an infinite chain

Put N=80 and let A contain all states of count 0 through N. Let Q_A be the restriction of Q to A, with its original diagonals retained. This is the generator of the chain killed when an arrival takes count N to N+1. It is a finite irreducible chain before killing, and killing is accessible, so its expected killing time is finite and -Q_A is invertible.

Define two column vectors by exact linear equations:

    (-Q_A) h = 1,
    (-Q_A) g = r,       r(x)=1 if count(x)>=2, and 0 otherwise.

For an entry state x in A, h(x) is its expected time until killing and g(x) is its expected time with both servers busy before killing. The certificate constructs Q_A directly from the phase rules above and solves both equations by rational block elimination. It checks every original row of both equations exactly and checks 0<g(x)<h(x).

Let pi be the stationary law of the infinite chain and delta=pi(A^c). The incoming stationary rate vector nu to A has support only on states of count N: the count changes by one at each transition. Restricted stationarity gives

    pi_A Q_A + nu = 0,
    pi_A = nu (-Q_A)^(-1).

Consequently

    pi_A 1 = nu h = 1-delta,
    pi_A r = nu g.

The conditional delay probability within A is therefore a convex combination of the ratios g(x)/h(x) for count-N entry states, with weights proportional to nu(x)h(x). Denote their minimum and maximum by l and u. Every state outside A has both servers busy, so

    P(delay) = (1-delta) rbar + delta,
    l <= rbar <= u.

An upper bound delta<=gamma thus proves

    l <= P(delay) <= u + gamma(1-u).               (1)

This is an exact stationary-flux identity, not a claim that a truncated queue has the same stationary probabilities as the infinite queue.

## Bounding the missing stationary mass

Both service laws are dominated job by job by (8/5)E, using the same iid E and arrival sequence. For completeness, the two-server Kiefer--Wolfowitz recursion for the sorted workload vector immediately before consecutive arrivals is

    V_(j+1) = sort(( (V_j,1 + S_j, V_j,2) - A_j (1,1) )_+),

where A_j is the time to the next arrival. This map is componentwise increasing in the sorted old workload and the service duration: adding to the first coordinate, subtracting, taking positive parts, and sorting each preserve componentwise order. Starting the two systems empty in the past therefore orders their workload vectors. Each numbered job starts service no later and finishes no later in the original system, since its start is its arrival time plus the smaller workload. Thus its total number of unfinished jobs is at most that of the dominating slow queue at every time.

The slow queue is M/M/2 with service rate 5/8 per server and rho=(11/10)/(2*5/8)=22/25<1. The coupling gives stability of both original queues and domination in their stationary versions. The elementary M/M/2 stationary birth-death calculation gives

    P_slow(count >= 2) = 2rho^2/(1+rho),
    gamma := P_slow(count > N)
           = [2rho^2/(1+rho)] rho^(N-1).

Hence delta<=gamma exactly. For N=80 the displayed value of this rational gamma is approximately .000033881965083361.

## Exact outputs

`whitt_positive_service_exact.py`, using the elementary Fraction matrix helpers in `whitt_finite_independent.py`, implements (1). No floating-point arithmetic decides any assertion. It verifies the generator rows, the full rational backward equations, positivity, and the rational probability bounds. The outward rational intervals at the start of this note are checked with Fraction comparisons. Decimals are display only.

| Law | Certified lower bound, displayed | Certified upper bound, displayed |
|---|---:|---:|
| S | .392872619378512420636667195... | .392893190047224051767481936... |
| T | .391723695390425373128659150... | .391744304986939526115032326... |

The displayed lower bound on their difference is .001128314391572894521634868...; the exact rational comparison establishes that it exceeds 11/10000. The output is recorded in `whitt_positive_service_checks.json`, and can be reproduced with ordinary Python, without external packages:

    python whitt_positive_service_exact.py

## A positive tail threshold

The violation persists at an explicit positive waiting-time threshold. In the baseline queue, when an arrival sees both servers busy, its wait cannot end before at least one of those two jobs completes. The combined completion rate is at most 10, so P(0<W_S<=h)<=10h. Therefore, for h=1/100000,

    P(W_S>h)-P(W_T>h)
      >= P(W_S>0)-10h-P(W_T>0)
      > 11/10000-1/10000 = 1/1000.

Thus the stochastic-order failure is not confined to the atom of the waiting-time law at zero. The service laws themselves have no atom at zero.

## Verification and limitations

The original zero-atom pair is separately certified in `whitt_qbd_exact.py` by rational enclosures of a 3-by-3 matrix-geometric fixed point and positive boundary inverses. `whitt_finite_independent.py` verifies that pair by the different killed-chain method above. Two independent mathematical audits of the original phase model and matrix-geometric proof found no gap. The present strictly positive extension uses a directly enumerated six-phase service model and the same proven occupation-bound lemma.

This proves a counterexample to the mathematical assertion in Whitt's 1983 Conjecture 1.1. It does not disprove the weaker conjecture about mean waiting time, and it does not establish first priority. A search of current primary sources and papers citing the original assertion found no earlier refutation; that negative search result is not a proof of novelty. No external expert review has yet occurred.
