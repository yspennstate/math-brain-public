PARTIAL

# C0130: escape probability of a one-dimensional excited random walk

The general problem is not resolved here. I found the two-cookie formula already cited by the problem, but no published computation for the full setting in the literature checked through 13 November 2026. Below are exact branching-process representations, proofs, a finite rational procedure giving rigorous numerical enclosures, and partial bounds. A stationary-law characterization is not presented as a new solution of the open problem.

## 1. What the source asks

In [Kosygina–Zerner, arXiv:1204.1895v2](https://arxiv.org/pdf/1204.1895), Problem 3.12 is on printed page 13, immediately after Theorem 3.10. It asks for the annealed probability of no return in the transient case. It does **not** impose identical cookie strengths or specify a new restricted model.

The preceding theorem covers either (3.9), spatially stationary ergodic stacks of nonnegative cookies, possibly unbounded, excluding the deterministic stack `(1,1/2,1/2,...)` at every site; or (3.10), IID stacks, at most a deterministic M non-placebo cookies, with weak ellipticity. In the second case cookies can have either sign. The drift parameter is

\[
\delta=\mathbb E\sum_{j\ge1}(2p_j-1).
\]

Subject to those hypotheses, recurrence holds for |delta| <= 1; transience is to the right for delta > 1 and to the left for delta < -1. Reflection exchanges the last two cases. Files: [survey PDF](sources/kosygina_zerner_2013.pdf), [searchable text](sources/kosygina_zerner_2013.txt).

The work below distinguishes the full setting from the IID bounded subcase. Spatial correlations prevent an annealed one-dimensional crossing-count process from automatically being a homogeneous Markov chain.

## 2. Exact branching-process expressions

Assume first IID bounded stacks and delta > 1. A site's stack is sampled once; conditional on it, independent coins B_j have success probabilities p_j. A success means a step right. Different sites use independent stacks and coins. Define F_r to be the number of failures before success r, and

\[
Q(i,j)=P(F_{i+1}=j),\qquad Z_0=0,\quad Z_{n+1}=F^{(n)}_{Z_n+1}.
\tag{1}
\]

This is the backward branching process with one immigrant before reproduction. It counts **downcrossings** when edges are read backward from a right boundary. Successive offspring within a cookie stack need not be independent. Write bar-p = E[p_1]. For a deterministic stack, an entirely explicit kernel is

\[
Q(i,j)=p_{i+j+1}[z^i]\prod_{\ell=1}^{i+j}(1-p_\ell+p_\ell z).
\tag{2}
\]

For random stacks take the expectation of the entire expression, retaining dependence between cookies at one site.

### Proposition 1: escape, stationary mass, and a positive series

Let pi be the unique stationary law of Q. Then

\[
\boxed{e:=P_0(X_n\ne0\ (n\ge1))
 =\bar p\,\pi(0)
 =\bar p\lim_{N\to\infty}(Q^{N-1})(0,0)
 =\frac{\bar p}{E_0\tau_0^+}},
\tag{3}
\]

where tau_0^+ is the first strictly positive return time of Z to 0. In particular the following positive, convergent series is an exact expression:

\[
\boxed{e=\frac{\bar p}{1+\displaystyle\sum_{n=1}^\infty
\sum_{i_1,\ldots,i_n\ge1}
Q(0,i_1)Q(i_1,i_2)\cdots Q(i_{n-1},i_n)}}.
\tag{4}
\]

Proof. Start a walk at 1 with fresh cookies at positive sites and reflect it from 0 to 1 whenever necessary. Stop it on first hitting N. If D_k counts jumps k to k-1, then D_N=0 and

\[
D_k=F^{(k)}_{D_{k+1}+1},\qquad k=N-1,\ldots,1.
\]

Each downward excursion returns because the finite reflected interval is exited almost surely. This follows from the eventually fair stacks; in the nonnegative-cookie setting it also follows by comparison of exit opportunities with fair coins. Hence

\[
P_1(T_N<T_0)=P(D_1=0)=(Q^{N-1})(0,0).
\tag{5}
\]

The events on the left decrease to no visit to 0: staying forever in a fixed finite interval has probability zero. On the original walk's no-return event, its first step must be right, since it is almost surely transient to the right. The coin at 0 is independent of all positive stacks. This gives the limit in (3).

For delta > 1, Q is positive recurrent, as in the branching-process results of Basdevant–Singh and Kosygina–Zerner. Under weak ellipticity it is irreducible and aperiodic; in particular Q(0,0)>0. Its transition probabilities therefore converge to pi. The return-cycle formula pi(0)=1/E_0[tau_0^+] gives the other equality. Expanding E[tau]=sum_{n>=0}P(tau>n) proves (4). Every summand is nonnegative, so rearrangement requires no cancellation or unproved interchange. This also proves convergence. ∎

The spatial version is useful for the other setting in the source. For a fixed environment define Q_x from its stack at x. Then

\[
e=\mathbb E\left[p_{0,1}\lim_{N\to\infty}
(Q_{N-1}Q_{N-2}\cdots Q_1)(0,0)\right].
\tag{6}
\]

For stationary ergodic nonnegative stacks transient to the right this follows by the same finite-interval argument and bounded convergence. Independence is not required for (6). In general one cannot replace these kernels by their average or factor out p_(0,1). For bounded IID stacks with delta < -1, reflect the walk and use probabilities 1-p_j in (1)–(4).

### An independent forward formulation

Let S_k be the number of successes before the kth failure at one fresh site, with S_0=0. Define V_0=1 and V_{n+1}=S^{(n+1)}_{V_n}; 0 is absorbing. Its transition law is

\[
L(k,j)=(1-p_{k+j})[z^j]\prod_{\ell=1}^{k+j-1}(1-p_\ell+p_\ell z),\qquad k\ge1.
\tag{7}
\]

Again average the full expression for a random stack. If h is the *least* [0,1]-valued solution of

\[
h(0)=1,\qquad h(k)=\sum_{j\ge0}L(k,j)h(j),\quad k\ge1,
\tag{8}
\]

then e = bar-p (1-h(1)). Indeed h(k)=lim_n P_k(V_n=0) is the extinction probability, and first-step conditioning proves both harmonicity and minimality. The crossing-count construction identifies extinction with the walk's return to 0. The constant function 1 also solves (8); specifying minimality is essential. Actual upcrossings on an escaping path should not be confused with an unconditioned forward process: conditioning on survival changes its transition law.

For completeness, the duality follows directly from coins:

\[
Q(i,\{0,\ldots,k-1\})=L(k,\{i+1,i+2,\ldots\}).
\tag{9}
\]

The event says that success i+1 precedes failure k in either notation. It gives P_1(V_n>0)=(Q^n)(0,0) and reconfirms (3) independently of a crossing-direction convention.

### Stationary generating function

For a deterministic M-cookie stack set

\[
f(s)=\frac1{2-s},\quad C(s)=\prod_{\ell=1}^M[2p_\ell+(1-2p_\ell)s],
\quad A_i(s)=E[s^{F_{i+1}}].
\]

For i>=M-1, all M initial coins have been examined before success i+1, so

\[
A_i(s)=C(s)f(s)^{i+1}.
\]

Consequently the unique stationary probability generating function satisfies

\[
G(s)=f(s)C(s)G(f(s))+
\sum_{i=0}^{M-2}\pi(i)\{A_i(s)-C(s)f(s)^{i+1}\},\quad G(1)=1,
\tag{10}
\]

and e=p_1 G(0). For IID random stacks use E[C(s)]. Expanding according to the number of successes among the first M coins proves the identity. This is equivalent to Basdevant–Singh, Lemma 3.4, rather than an explicit evaluation of the unknown low stationary masses.

## 3. Cases with closed forms and a limitation on delta-only answers

For **one cookie per site**, with 0<p<1, delta=2p-1 lies strictly between -1 and 1. The walk is recurrent and e=0; there is no nondegenerate transient one-cookie case on Z with a fair tail. At p=1, e=1 and delta=1: the walk moves deterministically right. This exceptional stack is explicitly excluded in Theorem 3.10's nonnegative setting and fails weak ellipticity in its IID setting.

For **two cookies**, the known formula is [Zerner (2005), Theorem 18, equation (48)](https://www.mathematik.uni-tuebingen.de/user/zerner/pub/ex.pdf): for IID nonnegative two-cookie stacks,

\[
e=\frac{E[p_1](\delta-1)_+}{E[p_1(2p_2-1)]},
\tag{11}
\]

when the denominator is nonzero. Thus deterministic p_1,p_2 with delta>1 give e=(delta-1)/(2p_2-1). In particular

\[
\boxed{e_{2,p}=\left(2-\frac1{2p-1}\right)_+},\quad 1/2<p<1.
\tag{12}
\]

Section 5 below rederives this using the backward chain's drift, rather than assuming the formula in the numerical code.

There is **no formula depending on delta alone** in the full setting, even for deterministic two-cookie nonnegative stacks:

\[
\begin{array}{c|c|c}
(p_1,p_2)&\delta&e\\\hline
(9/10,4/5)&7/5&2/3\\
(4/5,9/10)&7/5&1/2.
\end{array}
\tag{13}
\]

Both satisfy ellipticity, boundedness, and independence across sites. This is an exact counterexample to a delta-only candidate, not a counterexample to the open question.

For **M identical cookies**, M>=2, the threshold is p_c=(M+1)/(2M). At p=p_c the walk is recurrent and e=0, and for p>p_c it has positive escape probability. For M>=3 I did not obtain a finite closed form; equations (3), (4), (8), and (10) are exact characterizations and the next section computes certified intervals.

## 4. A rational certificate for numerical escape probabilities

The following device controls the infinite population tail rather than discarding it. It is stated for a deterministic stack with p_j in (0,1), delta>1; the examples below have p_j>=1/2. All formulas are rational for rational p_j.

Write d=delta-1. The exact conditional drift is

\[
E_i[Z_1-i]=-d\quad(i\ge M-1).
\tag{14}
\]

To prove it, let S count successes in the first M coins. Conditional on S, the remaining required successes are i+1-S, and the fair tail has that many failures in expectation. Thus E_i Z_1 = E[M-S+i+1-S]=i+1-delta.

Let t_i=E_i[tau_0], with t_0=0. Fix K>=max(M,2). Solve two finite systems to make

\[
u_c(0)=0,\quad u_c(i)=a_i+b_i c\ (1\le i<K),\quad
u_c(i)=i/d+c\ (i\ge K)
\tag{15}
\]

satisfy u_c(i)-sum_j Q(i,j)u_c(j)=1 for 1<=i<K. With a_0=b_0=0, the systems are

\[
\begin{split}
a_i-\sum_{1\le j<K}Q(i,j)a_j
 &=1+\frac{E_i Z_1-\sum_{j<K}jQ(i,j)}d,\\
b_i-\sum_{1\le j<K}Q(i,j)b_j
 &=P_i(Z_1\ge K).
\end{split}\tag{16}
\]

The finite killed chain exits {1,...,K-1} almost surely, so these systems are invertible and 0<=b_i<1. Probabilistically b_i is the probability of exiting at or above K before hitting 0.

Let alpha_s=P(S=s), where S counts successes in the first M coins. For i>=K,

\[
Q(i,j)=2^{-i}2^{M-j-1}\sum_{s=0}^M\alpha_s
{i+j-M\choose j-M+s},\qquad j<K.
\tag{17}
\]

As usual a binomial coefficient with an invalid lower index is zero. Vandermonde's identity expands the residual in the nonnegative functions binom(i-K,ell):

\[
\begin{split}
u_c(i)-\sum_j Q(i,j)u_c(j)-1
 &=2^{-i}\sum_{\ell=0}^{K-1}{i-K\choose\ell}(B_\ell c-A_\ell),\\
w_{\ell j}&=2^{M-j-1}\sum_{s=0}^M\alpha_s
{K+j-M\choose j-M+s-\ell},\\
A_\ell&=\sum_{j<K}w_{\ell j}(a_j-j/d),\qquad
B_\ell=\sum_{j<K}w_{\ell j}(1-b_j)>0.
\end{split}\tag{18}
\]

The strict positivity uses alpha_M>0. Set

\[
c_- =\min_{0\le\ell<K} A_\ell/B_\ell,\qquad
c_+ =\max_{0\le\ell<K} A_\ell/B_\ell.
\tag{19}
\]

Then (I-Q)u_(c_-)<=1<=(I-Q)u_(c_+) at every positive integer, including the entire unbounded tail. Optional stopping gives u_(c_-) <= t <= u_(c_+). The code also checks nonnegativity of these functions for the displayed cases.

Here is justification of the optional-stopping limit despite the possibly infinite stationary mean of Z. Choose 1<r<min(delta,2). The fair-negative-binomial tail in (17) has mean i-d, variance 2i+O(1), exponentially small relative deviations and centered third absolute moment O(i^(3/2)). Taylor expansion, splitting off deviations larger than i/2, gives

\[
E_i[(Z_1+1)^r]-(i+1)^r
 =r(r-\delta)i^{r-1}+o(i^{r-1}).
\tag{20}
\]

It is negative outside a finite set and bounded above everywhere. Positive recurrence implies E_i[tau_0]<infinity. Stopping at tau_0∧n therefore gives a uniform bound on E_i[(Z_(tau_0∧n)+1)^r]. Thus the stopped populations are uniformly integrable. The functions u_c have at most linear growth, so their stopped expectations tend to u_c(0)=0. The telescoping inequalities now yield the asserted bounds on t. The same argument applies to the first return cycle starting at 0.

Finally define

\[
\begin{split}
A&=1+\sum_{j<K}Q(0,j)a_j+
\frac{E_0 Z_1-\sum_{j<K}jQ(0,j)}d,\\
B&=\sum_{j<K}Q(0,j)b_j+P_0(Z_1\ge K)\ \ge0.
\end{split}
\]

We obtain the explicit rational enclosure

\[
\boxed{\frac{p_1}{A+Bc_+}\ \le e\le\ \frac{p_1}{A+Bc_-}}.
\tag{21}
\]

No uncomputed tail constant or statistical assumption enters (21). Numerical output called a certificate below uses exact rational matrix solving and exact rational comparisons in (19). Its printed decimal expansions are approximations to stored rational endpoints.

## 5. Further bounds and asymptotics

For deterministic identical positive cookies let a=2p-1, d=Ma-1>0. Define, for 0<=i<=M-2 and r=i+1,

\[
D_i=a\sum_{f=0}^{M-r-1}(M-r-f){r+f-1\choose f}p^r(1-p)^f.
\tag{22}
\]

This is the mean unused cookie drift when the rth success occurs; it is strictly positive for these i. For all i, E_i[Z_1-i]=-d+D_i if i<=M-2 and equals -d otherwise. Apply the uniformly integrable return-cycle stopping argument above to Z itself and divide by the mean cycle length. This gives the drift-budget identity

\[
d=\sum_{i=0}^{M-2}\pi(i)D_i.
\tag{23}
\]

Stationarity also gives pi(0)>=pi(i)Q(i,0)=pi(i)p^(i+1). Hence

\[
\boxed{\frac{p d}{\sum_{i=0}^{M-2}D_i/p^{i+1}}
\le e_{M,p}\le\min\left\{2p-1,\frac{p d}{D_0}\right\}}.
\tag{24}
\]

The first two bounds follow from (23). For the bound 2p-1, increase every fair tail probability to p. Backward failure counts decrease under a common-uniform coupling, increasing the escape probability. The resulting walk is the ordinary biased random walk, whose no-return probability is 2p-1 (the right first step has probability p and the subsequent hitting probability of 0 is (1-p)/p).

When M=2, D_0=p(2p-1), so both drift-budget bounds agree and yield e=(4p-3)/(2p-1), rederiving (12). The same argument with two nonidentical or random cookies yields (11).

For each fixed M>=2, (22) is continuous and strictly positive at p_c=(M+1)/(2M). Therefore (24) proves

\[
e_{M,p}=\Theta(\delta-1)=\Theta(p-p_c)\quad\text{as }p\downarrow p_c.
\tag{25}
\]

The constants in the two sides of (24), evaluated at p_c, are explicit positive bounds for the lower and upper limiting ratios. This does not claim that the ratio has a limit or identify a critical amplitude for M>=3.

For example M=3 gives D_0=p(2p-1)(3-p), D_1=p^2(2p-1), so

\[
\frac{p(6p-4)}{(2p-1)(4-p)}\le e_{3,p}\le
\min\left\{2p-1,\frac{6p-4}{(2p-1)(3-p)}\right\},\qquad p>2/3.
\]

In particular the lower limiting ratio e/(delta-1) is at least 3/5 and the upper limiting ratio is at most 9/7 at this threshold.

Coordinatewise monotonicity is immediate from the same coin coupling: stronger cookies decrease F_r, so backward chains started at 0 remain ordered. Equations (3) and (5) give nondecreasing positive-direction escape. For delta>1, increasing the common p strictly increases e: pi(0)>0, its value is nondecreasing, and the independent first factor p increases. Stronger strict comparisons, including reorderings of cookies, are already in Peterson (2013).

There is no universal statement “escape tends to 1 as delta tends to infinity.” For fixed p>1/2, letting M grow gives

\[
\lim_{M\to\infty}e_{M,p}=2p-1.
\tag{26}
\]

Proof. Choose M_0 with M_0(2p-1)>1. As M increases, the stationary backward chains decrease in stochastic order, so their laws are tight, dominated by pi_(M_0). The kernels converge pointwise to the backward kernel with all coins of probability p. Tightness permits passage to the limit in stationarity by first restricting the initial state to a finite set. The limiting chain has unique stationary law

\[
\pi_\infty(j)=(1-q/p)(q/p)^j,\qquad q=1-p,
\]

as substitution of its generating function into the negative-binomial transition verifies. Thus p pi_M(0) tends to p-q. Different p give different limits with delta→infinity. Also, for fixed M>=2, monotonicity in M and (12) show e_(M,p)→1 as p↑1. ∎

## 6. Numerical results and independent checks

The interval endpoints in the following table have been rounded **outward** to 18 places. The underlying JSON files store the complete rational endpoints. They are numerical theorems conditional only on the proved enclosure (21), not statistical confidence intervals.

| M | p | delta | Lower bound for escape | Upper bound for escape | K |
|---|---|---|---|---|---|
| 2 | 4/5 | 6/5 | 1/3 | 1/3 | 8 |
| 2 | 9/10 | 8/5 | 3/4 | 3/4 | 8 |
| 3 | 7/10 | 6/5 | 0.192758176466314667 | 0.192758176466316259 | 80 |
| 3 | 3/4 | 3/2 | 0.400697907749519095 | 0.400697907749520262 | 80 |
| 3 | 4/5 | 9/5 | 0.556165463398440124 | 0.556165463398440125 | 128 |
| 3 | 9/10 | 12/5 | 0.795603895333744546 | 0.795603895333744548 | 96 |
| 3 | 23/30 | 8/5 | 0.456777158952984790 | 0.456777158952985705 | 80 |
| 4 | 3/4 | 2 | 0.471208001124236056 | 0.471208001124236101 | 96 |

Notice also that identical-cookie families with the same delta can have different escape probabilities: M=2,p=.9 and M=3,p=23/30 both have delta=1.6. This corroborates the exact unequal-cookie counterexample (13) without relying on reordered stacks.

Files [decimal_enclosures.json](data/decimal_enclosures.json) and `data/cert_*.json` contain the table's data. `code/escape.py` calculates the finite matrix entries by enumerating the initial M Bernoulli trials until the requested success count, then extends surviving coin paths by the exact fair negative-binomial law. The kernel is not obtained by assuming a stationary distribution.

The stronger K=128 certificate for M=3,p=4/5 gives, with outward rounding,

\[
0.556165463398440124244\le e_{3,4/5}\le0.556165463398440124318.
\]

Its unrounded rational interval has width below 7.279e-20. See [the exact certificate](data/cert_m3_p08_k128.json); it is contained in the independently recomputed K=64 and K=96 enclosures.

### Independent finite-volume calculation

`code/finite_volume.py` constructs the *actual walk's* finite Markov chain: its state consists of position in {1,...,N-1} and the number of cookies already consumed at each site, capped at M. It solves the absorbing Dirichlet problem in rational arithmetic. This is independent of the branching representation and uses no affine-tail approximation.

| M,p | N | Reachable states | Exact P_1(T_N<T_0) |
|---|---|---|---|
| 2,4/5 | 5 | 47 | 4100348/5859375 |
| 3,7/10 | 5 | 121 | 43170877631/78125000000 |
| 3,4/5 | 4 | 38 | 2617664/3515625 |
| 3,9/10 | 5 | 121 | 69242195601/78125000000 |
| 4,3/4 | 5 | 251 | 1419890817/2147483648 |

These agree with the backward-chain finite-generation computation to about 80 decimal places in 85–90 digit arithmetic. Truncating populations at 640 in this check has a separate analytic error bound: for n=N-1, the lost probability is at most n[n/(n+1)]^640. Indeed all cookies here have p>=1/2, so the chain is dominated by the all-fair backward process; its time-j law is geometric with mean j. A union bound over j<=n gives the bound. For N=5 it is below 4e-62; for N=4 it is below 4e-80. The walk calculation itself is exact rational arithmetic; the matrix-power comparison uses multiprecision arithmetic. See [finite_checks.json](data/finite_checks.json) and [the M=3,p=.8 check](data/finite_m3_p08_n4.json).

These finite-volume values are **not** the infinite-volume escape probabilities. They verify the crossing identity, including its starting-point and indexing conventions. The rational certificates separately bound the infinite-volume limit.

### Independent forward-process Monte Carlo

Each experiment uses 100,000 independent copies of the forward process in (7), starting at 1, with fresh stacks at each generation. A fair negative-binomial draw handles all tosses beyond the initial M coins. A generation counts spatial edges, not individual walk time steps. The calculation has no population cutoff; the largest observed population in these runs was below 194,000.

| M,p | Generations | p × surviving fraction | One standard error | Certified infinite-volume value, rounded |
|---|---|---|---|---|
| 3,.8 | 16,384 | .555048 | .00116602 | .55616546339844 |
| 3,.9 | 4,096 | .796491 | .00090799 | .79560389533374 |
| 4,.75 | 4,096 | .470850 | .00114646 | .47120800112424 |

All three agree within one standard error. The binomial standard error describes sampling only. Finite-generation survival is larger than infinite survival in expectation, and a finite run cannot certify nonreturn. The Monte Carlo check validates at statistical precision; it does not independently verify the last digits of the rigorous enclosures. Seeds, survival curves, and timings are saved in `data/mc_*.json`.

### Candidate closed forms

The two-cookie rational function survives all exact controls. For M=3, the simple extension (delta-1)/(2p-1) is already impossible at p=.8 because it exceeds 1. More systematically, we can exclude *every* rational function A(p)/B(p) with both polynomial degrees at most three as a formula throughout the transient interval.

Use the eight rational points p=.70,.75,.80,.85,.90,.93,.97,.99 and their exact enclosures. If a rational function with numerator and denominator degrees <=d fits, the matrix with columns

\[
1,p,\ldots,p^d,\quad e,ep,\ldots,ep^d
\tag{27}
\]

on any 2d+2 points must be singular: the coefficients of A-eB give a nonzero null vector. We take an approximate inverse R of the midpoint matrix, round its entries to rational numbers, and calculate bounds on every entry of I-RA for the **entire enclosure box** using exact rational interval arithmetic. The resulting upper bounds on its infinity norm are

| d | Certified upper bound for ||I-RA||_infinity |
|---|---|
| 1 | 6.327e-14 |
| 2 | 1.776e-10 |
| 3 | 2.549e-7 |

All are below 1. The Neumann-series criterion proves every admissible A is invertible, contradicting the required singularity. Thus the proposed low-degree rational class is rigorously excluded, allowing arbitrary real coefficients, not just small integer coefficients. Exact rational inputs, R, and residual norms are saved in [candidate_analysis.json](data/candidate_analysis.json). This is a finite certificate exclusion of low-degree formulas, not a proof that no rational function of higher degree exists.

At p=4/5,M=3, the certificate also excludes every rational number with denominator at most 1,000,000: the closest such rational to the enclosure midpoint is 502347/903233, and it is outside the enclosure. There is no inference of irrationality.

### Reproduction and resource use

From this directory, run:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/run_certificates.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/run_finite_checks.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/candidate_points.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/candidate_analysis.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/audit.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/escape.py --p 4/5 4/5 4/5 --K 128 --dps 95 --exact --output data/cert_m3_p08_k128.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/monte_carlo.py --M 3 --p .8 --samples 100000 --generations 16384 --seed 130 --output data/mc_m3_p08.json
```

Requires Python 3, SymPy, mpmath, and NumPy; the source extraction used pdftotext. There are no worker pools. Numerical processes use one library thread and inherited nice 15; raising priority to the requested nice 10 was disallowed, so the more considerate priority was retained. Exact runs record peak RSS in their JSON files and enforce a 3 GiB address-space limit where supported. All work stayed in this directory; no publication or push occurred.

The audit independently checks 156 kernel entries by polynomial coefficient extraction, including a stack with a negative cookie; checks the exact large-state drift; and compares the two-cookie certificates with (11). The independent walk-state calculations above provide a separate check on the branching construction. [Audit data](data/audit.json).

## 7. Literature checked and remaining gap

The search used the exact problem number and the phrases return probability, escape probability, and never return, followed by the cited authors and later papers. The conclusion is limited to this search and the papers below; absence from these sources is not a proof that no other paper exists. A special case explicitly cited by the open problem is insufficient for the status RESOLVED_IN_LITERATURE.

1. E. Kosygina and M. P. W. Zerner, *Excited random walks: results, methods, open problems*, Bull. Inst. Math. Acad. Sin. (N.S.) **8** (2013), 105–157; [arXiv:1204.1895v2](https://arxiv.org/abs/1204.1895). Theorem 3.10 and Problem 3.12 set the question; Section 5 explains the backward process. [Local PDF](sources/kosygina_zerner_2013.pdf).

2. M. P. W. Zerner, *Multi-excited random walks on integers*, Probab. Theory Related Fields **133** (2005), 98–122; [author's PDF](https://www.mathematik.uni-tuebingen.de/user/zerner/pub/ex.pdf). **Theorem 18, equation (48)** is the exact two-cookie escape computation. Theorem 16 proves monotonicity. The result precedes, and is expressly cited in, Problem 3.12. [Local PDF](sources/zerner_2005.pdf).

3. A.-L. Basdevant and A. Singh, *On the speed of a cookie random walk*, Probab. Theory Related Fields **141** (2008), 625–645; [arXiv:math/0611580](https://arxiv.org/abs/math/0611580). Lemma 3.4 is the stationary PGF equation; Remark 3.8 recovers two-cookie escape. The remarks preceding it express the generating function of the total number of returns using G. This provides a characterization, not evaluated escape for arbitrary stacks. [Local PDF](sources/basdevant_singh_speed_2008.pdf).

4. A.-L. Basdevant and A. Singh, *Rate of growth of a transient cookie random walk*, Electron. J. Probab. **13** (2008), paper 26, 811–851; [arXiv:math/0703275](https://arxiv.org/abs/math/0703275). Studies branching excursions and growth in the zero-speed transient regime. [Local PDF](sources/basdevant_singh_growth_2008.pdf).

5. E. Kosygina and M. P. W. Zerner, *Positively and negatively excited random walks on integers, with branching processes*, Electron. J. Probab. **13** (2008), paper 64, 1952–1979; [arXiv:0801.1924v2](https://arxiv.org/abs/0801.1924). Theorems 1 and 2 give recurrence/transience and speed criteria with both signs of cookies; Sections 3–4 and 6 develop the forward/backward connection. [Local PDF](sources/kosygina_zerner_2008.pdf).

6. E. Kosygina and T. Mountford, *Limit laws of transient excited random walks on integers*, Ann. Inst. H. Poincaré Probab. Statist. **47** (2011), 575–600; [DOI 10.1214/10-AIHP376](https://doi.org/10.1214/10-AIHP376). Theorems 2.1–2.2 control backward-cycle lifetime and progeny tails; Theorem 1.3 gives walk limit laws. These are the tail tools behind the method, not an evaluation of the escape constant. [Local PDF](sources/kosygina_mountford_2011.pdf).

7. J. Peterson, *Strict monotonicity properties in one-dimensional excited random walks*, Markov Processes Related Fields **19** (2013), 721–734; [journal page](https://math-mprf.org/journal/articles/id1316/), [arXiv:1210.4518](https://arxiv.org/abs/1210.4518). Proves strict monotonicity of positive-excursion survival under the Holmes–Salisbury ordering. It is Theorem 1.8 in the downloaded revision dated September 26, 2018 (numbered 1.7 in earlier versions). Section 2.1 gives the forward representation used in the independent check. [Local PDF](sources/peterson_monotonicity_2013.pdf).

8. E. Kosygina and M. P. W. Zerner, *Excursions of excited random walks on integers*, Electron. J. Probab. **19** (2014), paper 25, 1–25; [DOI 10.1214/EJP.v19-2940](https://doi.org/10.1214/EJP.v19-2940), [arXiv:1307.6830](https://arxiv.org/abs/1307.6830). Section 2 and Proposition 6 of the downloaded preprint explain the forward coupling. The principal theorem gives tails of finite excursions; for delta>1 the finite-depth overestimate of survival decays like N^(1-delta), with a stack-dependent constant. That does not determine the limiting escape probability. [Local PDF](sources/kosygina_zerner_excursions_2014.pdf).

9. D. Dolgopyat and E. Kosygina, *Scaling limits of recurrent excited random walks on integers*, Electron. Commun. Probab. **17** (2012), paper 35, 1–14; [arXiv:1201.0379](https://arxiv.org/abs/1201.0379). The critical case needs logarithmic scaling, while the walk remains recurrent. D. Dolgopyat and E. Kosygina, *Excursions and occupation times of critical excited random walks*, ALEA **12** (2015), 427–450; [arXiv:1410.7090](https://arxiv.org/abs/1410.7090). Gives critical excursion asymptotics and occupation limits, not positive escape at delta=1. Local PDFs: [2012](sources/dolgopyat_kosygina_2012.pdf), [2015](sources/dolgopyat_kosygina_2015.pdf).

10. B. Tóth, *Generalized Ray–Knight theory and limit theorems for self-interacting random walks on Z*, Ann. Probab. **24** (1996), 1324–1367; [author's PDF](https://www.math.bme.hu/~balint/cikkek/grk_ap.pdf). Local-time representation and diffusion-limit background for other self-interacting walks; not the bounded-cookie escape computation. [Local PDF](sources/toth_1996.pdf).

11. G. Kozma, T. Orenshtein and I. Shinkar, *Excited random walk with periodic cookies*, Ann. Inst. H. Poincaré Probab. Statist. **52** (2016), 1023–1049; [arXiv:1311.7439](https://arxiv.org/abs/1311.7439). Theorem 1.2 classifies recurrence/transience of infinite periodic stacks. Its explicit criterion is not an explicit escape probability. E. Kosygina and J. Peterson, *Excited random walks with Markovian cookie stacks*, same journal **53** (2017), 1458–1497; [arXiv:1504.06280](https://arxiv.org/abs/1504.06280). Theorems 1.5–1.8 give phase and limit-law classification in the larger Markovian-stack model. Local PDFs: [periodic](sources/kozma_orenshtein_shinkar_2016.pdf), [Markovian](sources/kosygina_peterson_2017.pdf).

12. R. G. Pinsky, *Transience/recurrence and the speed of a one-dimensional random walk in a “have your cookie and eat it” environment*, Ann. Inst. H. Poincaré Probab. Statist. **46** (2010), 949–964; [DOI 10.1214/09-AIHP331](https://doi.org/10.1214/09-AIHP331). A cookie persists until a left jump, which changes the model. Theorem 1 bounds a nonreturn probability; Remark 3 and Proposition 2 give equality in a subregime. It does not solve Problem 3.12 for fixed bounded stacks. [Local PDF](sources/pinsky_2010.pdf).

13. E. Madden, B. Kidd, O. Levin, J. Peterson, J. Smith and K. M. Stangl, *Upper and lower bounds on the speed of a one-dimensional excited random walk*, Involve **12** (2019), 97–115; [DOI 10.2140/involve.2019.12.97](https://doi.org/10.2140/involve.2019.12.97). Section 3 restates the PGF equation and explains that pi(0),...,pi(M-2) remain unknown. Its bounds concern speed. This is evidence about the computational obstruction, not a claim that an open speed problem logically implies an open escape problem. [Local PDF](sources/madden_et_al_bounds_2019.pdf).

14. A. Collevecchio, K. Hamza and T.-M. Nguyen, *Long range one-cookie random walk with positive speed*, [arXiv:2011.00493v2, 2021](https://arxiv.org/abs/2011.00493). The one-cookie transience here uses non-nearest-neighbor jumps and cannot be transferred to the one-cookie nearest-neighbor model above. [Local PDF](sources/collevecchio_hamza_nguyen_2021.pdf).

15. E. Kosygina, L. Marêché, T. Mountford and J. Peterson, *Functional limit theorems for self-interacting random walks*, [arXiv:2610.28935v1, October 20, 2026](https://arxiv.org/abs/2610.28935). Concerns inversion of joint Ray–Knight limits for self-repelling walks and their process limits. It does not compute bounded-cookie escape. This and current author publication lists were checked to extend the search beyond the older survey. [Local PDF](sources/kosygina_et_al_2026.pdf).

The unresolved part is an evaluation for arbitrary IID bounded stacks beyond the known two-cookie case, and especially for the source's broader stationary ergodic setting. Neither a new finite closed form nor a general critical amplitude is claimed. The exact representations, rational enclosures, and proofs above are partial results for the requested computation.

Task: “Open problem C0130” — received 13 November 2026, approximately 05:31 Asia/Tbilisi.
