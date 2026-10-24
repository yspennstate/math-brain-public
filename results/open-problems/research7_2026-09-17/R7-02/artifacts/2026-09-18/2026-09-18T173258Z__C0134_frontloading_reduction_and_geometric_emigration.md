Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# C0134 — front-loading reduction, Lamperti boundary, and an exact geometric-emigration family

Run date: 2026-09-18.  Slot: `R7-02`.  Canonical target: `C0134`.

Captured run-start master: `2a00d4c4b2838851e271f1a0157c2e56abfb7f46`.
Fresh master immediately before delivery work: `ca1b1c086854ee5a8b1937875f98bd014c95059c`.
Canonical ownership was re-read there and still belongs to `R7-02`.

Previous complete run report: `research7_2026-09-17/R7-02/runs/2026-09-18/2026-09-18T170800Z__report.md` @ `dcbb85f948a9c35bd21bcba7d3a1d6d2430e3786`.
Previous main artifact: `research7_2026-09-17/R7-02/artifacts/2026-09-18/2026-09-18T170300Z__C0134_truncation_and_unbounded_stack_transition_lemma.md` @ `fbbcdd22c39488571cb1482b29c00bbafd1b0fd4`.

## 1. Source scope and status

Kosygina–Zerner, *Excited random walks: results, methods, open problems*, arXiv:1204.1895v2 (2012; journal version 2013), Problem 5.3, asks whether in Theorem 5.2 one may replace `(BD)` by `(POS1)` while retaining `(IID)+(WEL)`.  In the positive one-dimensional branch this is the two-clause statement

- `delta <= 2  => v = 0`,
- `delta > 2   => v > 0`.

The previous R7-02 run proved the entire `delta>2` clause under the full source hypotheses and reduced every finite `delta<2` zero-speed case to the single critical endpoint `delta=2`.  Hence the frozen metric remains

`M_clause = 1/2`.

This run does **not** close the critical endpoint.  It gives an exact extremal reduction of the remaining source question to a scalar random-emigration branching problem, proves a complete source-valid unbounded test family, and identifies why the generic Lamperti moment theorem lands exactly on the undecided boundary.

## 2. Method B11 — square-root dualization puts the missing moment exactly at the Lamperti boundary

Let the critical source parameter be `delta=2`.  In the backward branching-like chain write, at state `x`,

`m=x+1`, `W=F_m`, `Delta=W-x`.

The previous run proved, under only finite total mean drift and `(POS1)`,

`E[Delta | x] = -1 + r_{x+1}`, with `r_m -> 0`,

`E[Delta^2 | x] = 2x + o(x)`,

and

`Delta/sqrt(x) => N(0,2)`.

Because the second moments converge to the Gaussian second moment, the family `Delta^2/x` is uniformly integrable.

Fix any `c>0`, put

`Y=sqrt(V+c)`, `y=sqrt(x+c)`, `eta=sqrt(W+c)-sqrt(x+c)`.

There is an exact algebraic identity

`eta = Delta/(2y) - eta^2/(2y)`.

Indeed, if `a=sqrt(W+c)` and `b=y`, then `Delta=(a-b)(a+b)` and

`Delta/(a+b) = Delta/(2b) - (a-b)^2/(2b)`.

Also

`eta^2 = Delta^2/(sqrt(W+c)+sqrt(x+c))^2 <= Delta^2/(x+c)`.

Since `Delta/x -> 0` in probability and `Delta^2/x` is uniformly integrable,

`E[eta^2 | x] -> 1/2`.

Taking expectations in the exact identity gives

`E[eta | x] = -3/(4y) + o(1/y)`.

Thus the square-root chain has the Lamperti coefficients

`m_1(y) ~ -mu/y`, `m_2(y) -> b`, with `mu=3/4`, `b=1/2`.

The usual invariant-moment boundary is

`2 mu/b - 1 = 2`.

But `Y^2=V+c`, so the undecided boundary moment is **exactly** the moment whose finiteness distinguishes positive speed from zero speed.  Standard asymptotically-zero-drift results decide moments strictly below and strictly above that exponent but not equality.  This is therefore not a proof of the critical case; it is a sharp diagnosis of why the first two transition coefficients alone stop one epsilon short of source closure.

This also rules out the tempting but invalid inference “same drift/variance as the bounded model implies the same speed at equality”.  At the source endpoint one needs either a boundary-tail theorem with sufficiently weak jump hypotheses, or additional structure of the cookie model.

## 3. Method B24 — exact front-loading reduction of the full critical source problem

The remaining arbitrary positive-stack problem can be reduced to a much smaller family.

### 3.1 Bernoulliization of a positive stack

For a source-valid stack write

`p_i = omega(0,+1,i)`, `d_i=2p_i-1 in [0,1]`.

Conditional on the original stack, introduce independent marks

`A_i ~ Bernoulli(d_i)`

and independent fair bits

`C_i ~ Bernoulli(1/2)`.

Define the actual success bit

`B_i = 1` if `A_i=1`, and `B_i=C_i` if `A_i=0`.

Then

`P(B_i=1 | omega) = d_i + (1-d_i)/2 = p_i`,

and the `B_i` are independent conditional on `omega`.  Therefore, after enlarging the environment, the annealed coin sequence, the ERW path law, and the backward BLP law are unchanged.  Every positive cookie may be treated as a random choice between a deterministic-right cookie and a fair cookie.

Set

`N = sum_{i>=1} A_i`.

At `delta=2`, Tonelli gives

`E N = E sum_i d_i = 2`,

so `N<infinity` almost surely.

Moreover `(WEL)` implies

`P(N=0)>0`.

To see this, `(WEL)` in the left direction supplies positive probability of a stack for which every `p_i<1`, hence every `d_i<1`.  Since `sum_i d_i<infinity` almost surely at finite `delta`, on that event

`prod_i (1-d_i)>0`.

But this product is exactly the conditional probability that all Bernoulli marks vanish.  Averaging yields positive unconditional probability of `N=0`.

### 3.2 Front-loading is the fastest arrangement for a fixed marked stack

For a fixed realization of the binary marks, keep the same fair bits but move every deterministic success to the left, preserving the relative order of the fair bits.  An adjacent interchange has the form

`[fair bit C, deterministic 1] -> [deterministic 1, fair bit C]`.

After the first coordinate the new cumulative number of successes is no smaller, and after the second coordinate it is equal.  Iterating adjacent swaps proves that every prefix of the front-loaded sequence has at least as many successes as the original sequence.

Consequently, if `F_m` is the number of failures before the `m`-th success,

`F_m^front <= F_m^orig` for every `m` simultaneously.

The front-loaded stack has exactly

`N` deterministic-right cookies followed by fair cookies.

For the corresponding backward chains

`Z_{k+1}=F^{(k)}_{Z_k+1}`,

monotonicity of `F_m` in `m` and the preceding coupling give, from the common start `0`,

`Z_k^front <= Z_k^orig` for all `k` almost surely.

### 3.3 Positive recurrence at the critical point

Both chains are positive recurrent.  For the original binaryized stack, choose `M` so that

`E sum_{i<=M} A_i > 1`.

This is possible because the partial expectations increase to `2`.  Deleting all marks after `M` produces a bounded source-valid stack with drift parameter `delta_M>1`; its bounded backward BLP has finite mean return time to zero by the source’s bounded theorem (Theorem 5.4 gives a return tail of order `n^{-delta_M}`).  The full positive stack only adds deterministic successes, hence its backward chain is pathwise no larger and returns to zero no later.

For the front-loaded chain, choose `M` with `E[min(N,M)]>1` and apply the same comparison.

Because `P(N=0)>0`, the front chain is irreducible and aperiodic on the nonnegative integers: from any state there is positive probability to hit zero in one step, and from zero an `N=0` site followed by fair failures can reach every state.  The same is true for the binaryized chain.  Denote their invariant laws by `pi_front` and `pi_orig`.

Taking limits in the pathwise monotone coupling for bounded increasing test functions yields

`pi_front <=_st pi_orig`.

### 3.4 Speed is equivalent to the invariant mean

At `delta=2>1`, Theorem 3.10 of the source gives right transience.  Its hitting-time identity states

`T_n = n + 2 sum_{0<=k<=n} J^down_{n,k} + O(1)`,

where the `O(1)` term is the total time spent below zero, which is almost surely finite, and the reversed positive-side downcrossing vector has the law of `(Z_0,...,Z_n)`.

For a positive recurrent backward chain, the ergodic theorem therefore gives

- if `E_pi Z < infinity`, then `v = 1/(1+2 E_pi Z)`;
- if `E_pi Z = infinity`, then `v=0` (apply the ergodic theorem to `Z wedge K` and let `K->infinity`).

Hence the critical clause of Problem 5.3 is **equivalent** to the following purely scalar statement.

> **Random-emigration critical statement RE(2).**  For every integer-valued `N>=0` with `E N=2` and `P(N=0)>0`, the positive recurrent Markov chain
>
> `Z_{k+1} = sum_{j=1}^{(Z_k+1-N_k)_+} xi_{k,j}`,
>
> where the `N_k` are iid copies of `N` and the `xi_{k,j}` are iid `Geom(1/2)` variables on `{0,1,...}` with mean `1`, has invariant mean `E_pi Z=infinity`.

The implication in both directions is exact:

- If RE(2) holds, front-loading gives `E pi_front Z=infinity`, stochastic domination forces `E pi_orig Z=infinity`, and every source-valid critical environment has zero speed.
- If RE(2) fails for some `N`, then the iid environment with its first `N` cookies deterministic right and every later cookie fair satisfies `(IID)+(WEL)+(POS1)`, has `delta=2`, and has positive speed `1/(1+2E_pi Z)`, giving a source-valid counterexample.

This is the strongest structural reduction obtained in this run.

## 4. Method B5 — exact one-parameter geometric-emigration family

The extremal reduction suggests testing RE(2) on explicit unbounded laws.  Take

`P(N=n)=p q^n`, `n>=0`, `q=1-p`,

and parameterize by its mean

`delta=q/p`, i.e. `p=1/(delta+1)`, `q=delta/(delta+1)`.

This is a genuinely unbounded `(IID)+(WEL)+(POS1)` family for every `delta>0` because `P(N=0)=p>0`.

Let `T(z)=1/(2-z)`, the pgf of `Geom(1/2)`.  Conditional on `Z=x`, with `m=x+1`,

`Z' = S_{(m-N)_+}`,

where `S_r` is a sum of `r` iid `Geom(1/2)` variables.  Summing the geometric law of `N` gives the exact transition pgf

`E[z^{Z'} | Z=x] = [p T(z)^{x+2} + q^{x+2}(T(z)-1)]/[T(z)-q]`.

For `delta>1` the chain is positive recurrent.  Let

`Phi(z)=E_pi z^Z`.

Stationarity yields

`Phi(z)(a-q) = p a^2 Phi(a) + q^2(a-1) Phi(q)`,

where `a=T(z)`.

Conjugate the Möbius map `T` to translation by writing

`z=1-1/u`, `Psi(u)=Phi(1-1/u)`.

Since `T(1-1/u)=1-1/(u+1)`, the stationary equation becomes

`Psi(u+1) = A_delta(u) Psi(u) + [delta^2/(delta+1)] Psi(delta+1) (u+1)/u^2`,

with

`A_delta(u)=((u-delta)(u+1))/u^2`.

Because `Psi(u)->1`, multiplying the increment equation by `u` and taking the limit forces

`Psi(delta+1)=1-1/delta^2`.

(If the limiting coefficient were nonzero, the increments along an integer translate of `u` would have one sign and size comparable with `1/u`, contradicting convergence of `Psi`.)

Thus for the deficit

`d(u)=1-Psi(u)`

one gets the remarkably simple universal recurrence

`d(u+1)=A_delta(u)d(u)+1/u^2`.

### 4.1 Exact critical solution

At `delta=2`, `Psi(3)=3/4`, hence `d_3=1/4`, and for integers `n>=3`,

`d_{n+1}=((n-2)(n+1)/n^2)d_n+1/n^2`.

Define

`g_n=((n-2)(n-1)/n)d_n`.

Then

`g_{n+1}-g_n=(n-1)/(n(n+1))=-1/n+2/(n+1)`,

and `g_3=1/6`.  Summation gives

`g_n=H_{n-1}+2/n-2`,

so

`1-Phi(1-1/n) = [n(H_{n-1}-2)+2]/[(n-2)(n-1)]`.

In particular,

`n[1-Phi(1-1/n)] ~ log n -> infinity`.

But for every nonnegative integer-valued `Z`,

`[1-(1-1/n)^Z]/(1/n) -> Z`

monotonically.  Therefore

`E_pi Z = infinity`.

The speed of this unbounded critical environment is exactly zero.

### 4.2 Supercritical parameter and exact speed

For `delta>2`, variation of constants in

`d(u+1)=A_delta(u)d(u)+1/u^2`

and the product identity

`prod_{k=m}^{n-1} A_delta(k)
 = [Gamma(n-delta)Gamma(m)/(Gamma(m-delta)Gamma(n))] (n/m)`

show

`u d(u) -> 1/(delta-2)`.

Hence monotone convergence of the pgf difference quotient gives

`E_pi Z = 1/(delta-2)`.

The hitting-time formula then gives the exact speed

`v(delta) = 1/(1+2/(delta-2)) = (delta-2)/delta`,  for `delta>2`.

For `delta<=2`, monotonicity in the geometric parameter together with the critical computation and the source recurrence/transience criterion gives `v=0`.  Thus this entire unbounded source-valid family has the sharp bounded-model threshold:

`v(delta)=0` for `delta<=2`, and `v(delta)=(delta-2)/delta` for `delta>2`.

In particular the one-sided ballistic slope at the endpoint in this family is

`v'(2+)=1/2`.

This exact family is a test case, not a source-level solution.  A fresh literature check found Patrick Carper’s 2026 preprint *A Branching Process with Geometric Emigration and the “Have Your Cookie and Eat It” Random Walk* (arXiv:2609.06311), whose abstract explicitly studies stationary means for a branching process with geometric emigration.  The PDF was not retrievable in this run, so exact parameter correspondence was not verified.  Accordingly **no novelty claim is made** for the geometric-emigration formulas above; they are retained as an independent derivation and a calibration case for RE(2).

## 5. What failed and what remains

B11 does not settle the endpoint: it lands precisely on the equality case excluded by generic invariant-moment criteria.

B24 did not find a source-valid counterexample.  Instead it reduced every critical positive stack to the faster front-loaded random-length model and showed that the full source question is equivalent to RE(2).

B5 tested a genuinely unbounded law with no deterministic depth cutoff.  The geometric-emigration family still has zero speed at mean drift `2`; it therefore supplies no counterexample.  Its exact logarithmic pgf singularity, `1-Phi(1-1/n) ~ (log n)/n`, is the expected critical signature.

The exact remaining mathematical question is now:

`For arbitrary N>=0 with E N=2 and P(N=0)>0, prove or disprove E_pi Z=infinity for Z' = sum_{1}^{(Z+1-N)_+} Geom(1/2).`

This is materially narrower than arbitrary random cookie stacks and isolates all unbounded-stack difficulty into the tail of a single integer-valued emigration variable.

## 6. Dated source / prior-art checks, 2026-09-18

- Primary source re-read: Kosygina–Zerner arXiv:1204.1895v2, Problem 5.3, Theorem 5.2, Theorem 4.1, Proposition 4.2, and the backward-BLP construction around equations (5.1)–(5.3).
- Peterson, *Strict monotonicity properties in one-dimensional excited random walks* (2013; arXiv:1210.4518), records the Holmes–Salisbury prefix-success partial order and a branching-process coupling.  The front-loading coupling above is written directly because our environment is random and unbounded; the literature strongly cautions against presenting prefix-success monotonicity itself as new.
- Chakhtoun, 2019 PhD thesis, *One-Dimensional Excited Random Walk with Unboundedly Many Excitations Per Site*, states that its extension requires a tail-decay estimate / moment conditions on the number of excitations.  A 2026 Bath thesis likewise describes Chakhtoun’s hypotheses as appropriate moment bounds on the random number of excitations.  This does not settle arbitrary `(POS1)`.
- Travers, *Excited Random Walk in a Markovian Environment*, EJP 23 (2018), treats a broad Markovian class and recovers ballisticity thresholds there, but not the unrestricted iid positive infinite-stack source scope.
- Carper, arXiv:2609.06311 (submitted 2026-09-05), is a very recent geometric-emigration branching-process preprint.  Abstract-level overlap was found; exact theorem overlap was not checked because the full text was unavailable through the current retrieval path.

Search misses and inaccessible full text are not evidence of novelty.

## 7. Metric and next attack

Frozen metric: `M_clause`.

Before: `1/2`.
After: `1/2`.
Movement: **NO MOVEMENT** on the source-level metric.
Ordinary unchanged count: `0 -> 1`.
Status: **PARTIAL**.

This run used the planned nonrepeating methods **B11 / B24 / B5**.

The next nonrepeating attack should be **B7 / B21 / B30**:

1. **B7 (truncate/limit with quantitative control):** exploit the fact that the front-loaded chain and its `N wedge M` truncation agree below level `M`; seek a uniform lower bound on stationary tail mass that survives `M->infinity` at `E N=2`.
2. **B21 (import analogous-field technique):** treat RE(2) as a critical Galton–Watson process with random emigration and import renewal/queueing or critical migration theorems, checking equality-case hypotheses exactly rather than assuming them.
3. **B30 (localize/glue):** decompose excursions into dyadic population bands and show that finite mean of `N` makes catastrophic emigration negligible on each scale (`x P(N>x)->0`), then glue scale-crossing probabilities to force the harmonic `1/x` stationary tail lower bound.

No closure label is promoted.  Independent P26 and OTHER-track audits and a source-scoped paper package remain future closure requirements even if RE(2) is resolved.