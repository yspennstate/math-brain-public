# E0110 - Tang's Conjecture 1.5: the relaxation time of the feed-forward GRBM

Wenpin Tang, *Exponential ergodicity and convergence for generalized reflected Brownian motion*,
arXiv:1806.03755v2 (2019), Conjecture 1.5, p. 5. Ledger row E0110; earlier attempt E0110-A001.

## 1. The problem as the source states it

The object is the strong solution of (1.1),

> dX_t = dB_t + ( mu + sum_{i=1}^d U'(n_i . X_t) r_i ) dt,

which under Assumption 1.2 (Gamma positive definite; R the lower bidiagonal matrix (1.10) with
r_ii = 1, r_{i,i-1} = -1; U' >= 0 continuous, decreasing on R_-, U'(y) -> 0 as y -> +infinity,
U'(y) -> infinity as y -> -infinity, and U'(ay)/U'(by) -> infinity as y -> -infinity for a > b > 0)
has generator (1.11)

> L = (1/2) sum Gamma_ij d^2/dx_i dx_j + sum_i ( mu_i + U'(x_i) - U'(x_{i-1}) ) d/dx_i,  with x_0 = infinity.

Theorem 1.3 (mu < 0 componentwise) gives a norm-like V with
LV <= -(1/(2d||Gamma||)) (min_i |mu_i|^2 - eps) V + b 1_{B_r}. Then, verbatim (p. 5):

> "In view of (1.12), we make the following conjecture.
> **Conjecture 1.5.** Under the assumptions of Theorem 1.3, GRBM(R, mu, Gamma, U) is uniformly
> exponentially ergodic with exponent of order 1/d. That is, there exist
> W : R^d -> [1, infinity) and C > 0 such that
> ||P^t(x, .) - pi(.)||_TV <= W(x) exp(-Ct/d).   (1.15)
> Conjecture 1.5 would imply that the relaxation time to global equilibrium is of order d for a
> class of GRBMs."

Section 4 adds, for the gap process of Brownian particles with soft reflection, the drift-condition
constant K_s = min_i |mu~_i|^2 / (4d(1 + cos(pi/d))) ~ d^{-1}, and says "the exact rate of convergence
of the gap process G^s (resp. G^h) remains open."

Two readings must be kept apart. (1.15) is an upper bound on the TV distance with a free function
W. Because W is unconstrained, (1.15) is implied by any bound W_d(x) e^{-lambda_d t} with
lambda_d >= C/d, whatever the d-dependence of the prefactor (if TV <= e^{cd} W(x) e^{-at}, then for
t >= 2cd/a the right side is <= W(x) e^{-at/2} <= W(x) e^{-(a/2) t/d}, and for t < 2cd/a the bound
1 <= e^{2c} e^{-(a/2)t/d} is trivial). So the formal conjecture is exactly "the exponential rate is at
least C/d, C free of d", while the sentence after it ("relaxation time of order d") is a sharper,
two-sided claim about a transient. The ledger row quotes (1.15) correctly.

The concrete instance the paper has in mind is the O'Connell-Yor potential U(x) = -e^{-x},
U'(x) = e^{-x}, Gamma = I. I work with that potential throughout; the structure I use (feed-forward
drift and monotone U') is all of Assumption 1.2 that enters.

## 2. Finding

The d-dependence lives in a pipeline, not in a coupon collector, and its length is
sum_{i=1}^d 1/m_i, where m_i := sum_{k<=i} |mu_k| is the mean push through coordinate i at
stationarity. In particular:

(a) Under the conjecture's own hypotheses with drifts bounded away from zero (|mu_i| >= theta for all
i and d), m_i >= i theta and the pipeline length is at most sum 1/(i theta) <= (1 + log d)/theta. The
relaxation time is of order log d, not d and not d log d. The formal bound (1.15) is then true with
room to spare in the linearised model, but "of order d" is not sharp.

(b) The relaxation time is of order d exactly when the cumulative drifts m_i stay bounded in i, i.e.
when the drifts of coordinates 2..d are summable. The cleanest such case is the Brownian tandem queue
itself, mu = (-theta, 0, ..., 0) (derived in section 3.4), where every queue has the same mean push theta
and the perturbation crosses the chain at speed theta: transit time d/theta with fluctuations of order
sqrt(d)/theta. That case has mu_i = 0 for i >= 2 and lies outside the hypotheses of Theorem 1.3; its
lawful neighbours mu = (-theta, -eps, ..., -eps) have a Lyapunov constant eps^2/(2d) that degrades
much faster than the pipeline length sum_i (theta + (i-1) eps)^{-1}.

(c) In neither regime does d log d appear: the frozen-rate model is a pure-birth chain, its transit
time is a sum of independent exponentials with means 1/m_i, and for m_i = i theta that sum has, by
Renyi's representation, the law of the maximum of d iid Exp(theta) variables - mean H_d/theta and
survival function 1 - (1 - e^{-theta t})^d <= d e^{-theta t}. The coupon-collector heuristic of
attempt A001 assumed the faces equilibrate in parallel with independent random times; in a
feed-forward chain they equilibrate in sequence, and with growing rates.

What is rigorous: the stationary identity E_pi U'(X_i) = m_i (section 3.1), the exact transport
structure of the synchronous coupling (section 3.2, with the ell^1 mass identity certified in Lean),
and the closed forms for the frozen-rate chain (section 3.3, Bernoulli and harmonic bounds certified in
Lean, Renyi's identity checked by Monte Carlo). What is not: passing from the frozen-rate chain to the
nonlinear SDE, and from a Wasserstein-type coupling statement to total variation. Those two steps are
supported by direct simulation of the SDE for d = 4..64 (section 5), not proved. Status: partial.

## 3. The argument

### 3.1 The mean push through coordinate i is exact

Write b_i(x) = mu_i + U'(x_i) - U'(x_{i-1}), U'(x_0) := 0. Coordinate 1 is autonomous:
dX_1 = (mu_1 + U'(X_1)) dt + dB_1, a one-dimensional diffusion with explicit stationary density
p_1(x) proportional to exp(2 mu_1 x + 2U(x)), which vanishes at both ends. Integrating
(mu_1 + U') p_1 = p_1'/2 gives E_pi U'(X_1) = -mu_1 = |mu_1|. For i >= 2, take expectations in the
SDE under pi (E_pi |X_i| < infinity by the paper's tail estimate (1.14), since V is norm-like):
0 = mu_i + E_pi U'(X_i) - E_pi U'(X_{i-1}), so by induction E_pi U'(X_i) is finite and equals

> m_i := sum_{k<=i} |mu_k|.

For the O'Connell-Yor potential this says E_pi e^{-X_i} = m_i. Under equal drifts mu_i = -theta the
stationary coordinates sit near -log(i theta), and the local restoring rate -U''(X_i) = e^{-X_i} of
coordinate i has mean i theta: the deeper coordinates are stiffer. This identity is also the check that
validates the simulations (section 5).

### 3.2 The synchronous coupling is a pure-birth transport

Let X, X' be strong solutions driven by the same Brownian motion, and Delta := X - X'. The noise
cancels, so Delta is C^1 with

> Delta_i' = -a_i Delta_i + a_{i-1} Delta_{i-1},   a_0 := 0,
> a_i(t) := (U'(X'_i) - U'(X_i)) / (X_i - X'_i) >= 0   (a_i := 0 when Delta_i = 0),

the divided differences of the nonincreasing function U' (for the O'Connell-Yor potential U' is
nonincreasing on all of R; Assumption 1.2 only asks this on R_-, and that is where the stationary mass
of the deeper coordinates sits). This is a linear cooperative system: if Delta(0) >= 0 then
Delta(t) >= 0 for all t. Summing the equations telescopes (Lean: `mass_leaks_only_through_last`):

> d/dt sum_i Delta_i(t) = -a_d(t) Delta_d(t).

So the ell^1 coupling distance is nonincreasing and is dissipated only through the last coordinate.
Normalising, Delta(t)/sum Delta(0) is the law at time t of a time-inhomogeneous pure-birth chain on
{1, ..., d} with rate a_i(t) from i to i+1 and killing at rate a_d from d, started from
Delta(0)/sum Delta(0). A kick to coordinate 1 has to be carried through every coordinate before it can
leave. This is the whole mechanism: the relaxation is a transit, and its length is the sum of the
sojourn times.

### 3.3 The solvable case: frozen rates

Freeze a_i(t) at the stationary mean of the restoring rate, which for the O'Connell-Yor potential is
E_pi e^{-X_i} = m_i (section 3.1). Then Delta(t) = exp(-tA) Delta(0) with A lower bidiagonal
(A_ii = m_i, A_{i+1,i} = -m_i), and the mass left from a kick at coordinate 1 is
P(E_1 + ... + E_d > t) with E_i independent Exp(m_i). Three cases:

* Equal drifts, m_i = i theta: by Renyi's representation the transit time has the law of the maximum
  of d iid Exp(theta), so the mass left is exactly 1 - (1 - e^{-theta t})^d <= d e^{-theta t}
  (Lean: `mass_left_le_d_exp`, `mass_left_exp`), mean H_d/theta <= (1 + log d)/theta
  (Lean: `transit_time_le_log`). The spectrum of A is {i theta}: the exponential rate is theta,
  free of d, and all the d-dependence is the prefactor d, i.e. a transient of length (log d)/theta.
* Constant rates m_i = a (the tandem queue): Delta_k(t) = e^{-at} sum_{j<k} (at)^j/j!, the mass left is
  P(Poisson(at) <= d-1): it stays at 1 until at ~ d and drops over a window of width sqrt(d). The
  spectrum is the single point a (a Jordan block of size d): again a dimension-free rate, but a
  transient of length d/a. This is the non-normal, "order d" picture the conjecture describes.
* Anything in between: transit sum 1/m_i. Under the paper's hypotheses with |mu_i| >= theta this is
  at most (1 + log d)/theta; it reaches order d only if the drifts of coordinates 2..d are summable.

The closed forms were checked against a matrix exponential and against 200,000 Monte-Carlo draws of the
exponential sums (`chain_identity_check.py`): agreement to 3-4 digits (MC) and to 1e-15 (matrix
exponential versus the Poisson formula).

### 3.4 Which drift vector is the tandem queue

Take arrivals A (standard BM), services S_i = s_i + theta t, and the O'Connell-Yor generalised queue
q_1 = log int_{-infinity}^t exp((A - S_1)(t) - (A - S_1)(s)) ds. Ito gives
dq_1 = (-theta + e^{-q_1}) dt + d(a - s_1). The departures are D_1 = A - q_1, so
dD_1 = (theta - e^{-q_1}) dt + ds_1, and the second queue, fed by D_1, satisfies
dq_2 = (e^{-q_2} - e^{-q_1}) dt + d(s_1 - s_2). Hence the tandem is the GRBM (1.11) with
mu = (-theta, 0, ..., 0) and Gamma tridiagonal (2 on the diagonal, -1 beside it), and Burke's theorem
is the statement m_i = theta for all i. The equal-drift family mu_i = -theta with Gamma = I, which
the paper calls the O'Connell-Yor process, corresponds instead to a tandem with service rates
increasing by theta per stage; that is what makes m_i = i theta.

## 4. What is not done

* No theorem about the SDE's total-variation rate. The transport structure of section 3.2 is exact
  and pathwise, but the rates a_i(t) are random; freezing them at their means is a linearisation. The
  simulations show the nonlinear system follows the frozen-rate chain in the equal-drift family and is
  somewhat slower in the tail in the tandem-like family (the rates fluctuate, and a fluctuating rate
  transports mass more slowly on average than its mean).
* Coupling in ell^1 controls Wasserstein distances, not TV. The TV-flavoured check in section 5.3 is
  numerical.
* A lower bound of order d on the TV relaxation time in the tandem regime would need an upper bound on
  the divided differences a_i along typical paths; condition (c) of Assumption 1.2 forces -U'' to be
  unbounded, so that bound is probabilistic and I did not carry it out.
* Whether the true exponential rate lambda_d (the asymptotic slope, which governs large deviations
  such as one coordinate wandering far to the right, where the restoring force vanishes) is free of d
  for the SDE is not settled here. The conjecture's rate bound C/d is far below the linearised truth,
  so nothing here threatens (1.15); nothing here proves it either.

## 5. Checks

All runs: Euler-Maruyama, Gamma = I, U' = e^{-x}, theta = 1, one process, `sim_grbm.py`.
Family F: mu_i = -1 for all i (m_i = i). Family T: mu = (-1, -0.02, ..., -0.02) (m_i = 1 + 0.02(i-1)).
A kick Delta(0) = e_1 on top of the fluid fixed point x_i = -log m_i, 400 paths, plus the empty start
x_i = -log m_i + 2 for the observable e^{-X_d}.

### 5.1 Transit times against the frozen-rate chain (`sim_results.json`)

| family | d | sum 1/m_i | peak time of Delta_d, SDE | same, chain | half-mass time, SDE | chain | E e^{-X_d}(T)/m_d |
|---|---|---|---|---|---|---|---|
| F | 4 | 2.08 | 1.50 | 1.40 | 2.20 | 1.85 | 0.98 |
| F | 8 | 2.72 | 2.55 | 2.10 | 3.00 | 2.50 | 0.97 |
| F | 16 | 3.38 | 2.85 | 2.75 | 3.60 | 3.20 | 1.00 |
| F | 32 | 4.06 | 3.65 | 3.45 | 4.25 | 3.85 | 1.02 |
| F | 64 | 4.74 | 4.42 | 4.15 | 5.03 | 4.55 | 1.02 |
| T | 4 | 3.89 | 3.25 | 2.90 | 4.10 | 3.60 | 1.08 |
| T | 8 | 7.49 | 6.80 | 6.55 | 8.25 | 7.20 | 0.86 |
| T | 16 | 14.0 | 12.95 | 13.10 | 15.0 | 13.75 | 0.84 |
| T | 32 | 24.9 | 20.55 | 24.10 | 27.65 | 24.70 | 1.14 |
| T | 64 | 41.5 | 53.3 | 40.75 | 49.45 | 41.25 | 0.96 |

Family F grows by 0.6-0.8 per doubling of d (log 2 = 0.69; the chain says H_{2d} - H_d -> log 2).
Family T roughly doubles with d. The last column is the independent validation of the simulation
through the exact identity E_pi e^{-X_d} = m_d (section 3.1); family T at d = 8..32 is within its
own noise (the run length there is only 4 sum 1/m_i + 8 and 200 paths, and those coordinates relax
slowly). In no row does anything grow like d log d: from d = 8 to 64 family F moves by 1.9 time units
where d log d would multiply by 16.

### 5.2 Discretisation and seed control (`control_dt_seed.json`, d = 32)

Halving dt and changing the seed moves the peak time of Delta_d from 3.65 to 3.95 / 3.40 (family F,
chain 3.45) and from 20.55 to 23.45 / 23.1 (family T, chain 24.1); half-mass times move by less than
0.3 (F) and 0.8 (T). The transit times are not discretisation artefacts.

### 5.3 A total-variation check (`tv_check.json`, family F)

From the empty start (every coordinate two units above its fluid level) and the overfull start (one unit
below), 3000 paths, the largest single-coordinate marginal TV to a stationary reference (15-bin
histograms; the noise floor between two halves of the reference is 0.06-0.08) and the first time it is
below 0.15:

| d | start | max marginal TV at t = 1, 2, 3, 4, 5, 6 | first t with max TV < 0.15 |
|---|---|---|---|
| 8 | empty | 0.75, 0.44, 0.23, 0.12, 0.06, 0.04 | 3.75 |
| 32 | empty | 0.91, 0.62, 0.32, 0.16, 0.08, 0.06 | 4.25 |
| 64 | empty | 0.95, 0.71, 0.39, 0.19, 0.08, 0.06 | 4.50 |
| 8 | overfull | 0.34, 0.14, 0.07, 0.05, 0.04, 0.04 | 2.00 |
| 32 | overfull | 0.42, 0.17, 0.07, 0.05, 0.04, 0.05 | 2.25 |
| 64 | overfull | 0.47, 0.17, 0.08, 0.05, 0.05, 0.05 | 2.25 |

From d = 8 to d = 64 the TV relaxation time moves by 0.75 (empty) and 0.25 (overfull) time units, the
same log-like creep as the coupling transit in 5.1 (the chain's H_64 - H_8 = 2.0 is an upper reference;
the empty start is dominated by coordinate 1 walking down two units at speed 1 and the marginals of the
stiff deep coordinates follow it quickly). Nothing here grows like d or d log d. This is a check on
marginals, not on the joint law, and its resolution is set by the 0.06-0.08 histogram noise.

### 5.4 The strongest case that I am wrong, and the check

The case: the coupling argument is Wasserstein-flavoured and the deep coordinates are stiff, so maybe
the TV relaxation of the joint law has a slow mode the ell^1 coupling cannot see - for instance a rare
excursion of coordinate 1 to the right, during which every coordinate below it loses its push, that
would make the honest rate lambda_d shrink with d. The check that would confirm it is a TV relaxation
time that grows faster than log d in family F. Section 5.3 is that check at d = 8, 32, 64: the TV relaxation time
moves by well under one time unit over a factor 8 in d, so the confirming signal is absent. What it cannot rule out is a d-dependence of the asymptotic slope at times far beyond the
transient, which is invisible at the simulated horizons and is listed as not done.

## 6. Prior art

The session's web-search budget was exhausted before this problem; I used direct fetches of the
Semantic Scholar and arXiv APIs (the arXiv API rate-limited and returned nothing).

* Semantic Scholar lists three citations of arXiv:1806.03755, all by Tang on other topics (exploratory
  HJB, simulated annealing); none addresses Conjecture 1.5.
* Banerjee and Budhiraja, *Parameter and dimension dependence of convergence rates to stationarity for
  reflecting Brownian motions*, arXiv:1902.04501 (Ann. Appl. Probab. 2020): for the Blanchet-Chen class
  of hard-reflected RBMs they improve the relaxation-time bound from O(d^4 (log d)^2) to O((log d)^2),
  and give O(d^6 (log d)^2) for the Atlas model. Banerjee and Brown, *Dimension-free local convergence
  and perturbations for reflected Brownian motions*, arXiv:2009.12937, and Banerjee's survey
  arXiv:2208.02855, are the follow-ups. None treats the soft-reflected GRBM or the O'Connell-Yor
  potential, so Conjecture 1.5 is not settled in the literature as far as I could see; but the
  (log d)^2 result for the hard-reflected uniform class is the same message as section 3.3 - the
  dimension enters through a logarithm, not linearly, once the drifts are uniform.
* Blanchet and Chen, arXiv:1601.04111, is the d^{-4}(log d)^{-2} bound the source itself quotes.

## 7. Files

`sim_grbm.py`, `sim_results.json`, `control_dt_seed.py`, `control_dt_seed.json`, `tv_check.py`,
`tv_check.json`, `chain_identity_check.py`, `U_E0110.lean` (compiled clean in ~/erdos_fc, four
theorems, axioms propext / Classical.choice / Quot.sound only).
