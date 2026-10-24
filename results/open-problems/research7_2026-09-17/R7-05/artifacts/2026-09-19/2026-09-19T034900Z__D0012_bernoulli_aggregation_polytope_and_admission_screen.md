Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# D0012 admission mathematics: exact Bernoulli aggregation polytope

Date: 2026-09-19 UTC  
Worker: R7-05 Sharp Inequality Research  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Repository: `yspennstate/math-open-problems`, branch `master`  
Captured start-of-run master: `ba8a186432c966bc838f034e9e7cc80d8c2710d2`  
Fresh pre-write master: `9b49aac4c3377c76b498fd01a87c4d2b8ef1fb3d`

## 1. Why D0012 was screened, not claimed

R7-05 entered this run in `PENDING_ADMISSION` after the mandatory six-unchanged retirement of C0031. Applying the worker partition

`sum(ord(c) for c in canonical_ID) mod 7 = 4`

to the currently visible queue/intake again leaves the same live shard family seen in the preceding handoff: `I0066`, `I0113`, `I0048`, `I0050`, `I0075`, `I0032`, `RS-2026-CL-B`, `D0012`, `I0122`, and `I0129`. All except D0012 are already claimed/held/retired/known-scope or otherwise not a lawful fresh CLOSABLE assignment in the current repository evidence. `operations/claims/D0012.md` is absent at the captured snapshot, but absence of a claim file is not enough for admission.

The outside source for D0012 is Ruodu Wang, **Current Open Questions in Complete Mixability**, *Probability Surveys* 12 (2015), 13–32, DOI `10.1214/14-PS250`, arXiv `1411.6190`, Open Problem 12, source PDF p.19. Its target is broad: characterize the aggregation set

`D_n(F_1,...,F_n) = { Law(X_1+...+X_n) : X_i ~ F_i }`

and decide whether a proposed law belongs to it.

The current author working-paper page explicitly says Open Problem 12 was only **partially solved** by Mao, Bin Wang and Ruodu Wang, *Sums of Standard Uniform Random Variables*, J. Appl. Probab. 56 (2019), 918–936. That paper gives a full characterization for standard-uniform margins when the dimension is at least three, while the two-dimensional standard-uniform case remains only partially characterized. Later aggregation-set papers continue to treat special structures rather than a general full characterization. A bounded 2026-09-19 search found no full source-level resolution; that is negative evidence only.

Therefore D0012 remains a scope hold unless a precise source-level residual can be frozen. The mathematics below is deliberately recorded as a **source-valid Bernoulli subclass**, not as source closure and not as novelty.

## 2. B2 — attack the negation: mean and support are not enough

A natural but false membership test for Bernoulli margins is: match the target sum support and the target mean.

Take three Bernoulli margins with

`p = (0.9, 0.05, 0.05)`

and propose the cardinality law

`q_0=0.2, q_1=0.6, q_2=0.2, q_3=0`.

Both sides have mean one:

`sum_i p_i = 1 = sum_k k q_k`,

and the target is supported on the correct set `{0,1,2,3}`. Yet the law is impossible. If `X_1=1`, then `S=X_1+X_2+X_3 >= 1`, hence necessarily

`P(X_1=1) <= P(S>=1)`.

Here the left side is `0.9` and the right side is `0.8`, contradiction.

This obstruction points to the correct family of subset-capacity inequalities.

## 3. B11 — dualize: exact characterization for arbitrary Bernoulli margins

### Theorem

Let `X_1,...,X_n` be `{0,1}`-valued random variables with prescribed marginal probabilities

`P(X_i=1)=p_i`, `0<=p_i<=1`.

Let `q=(q_0,...,q_n)` be a probability vector proposed for

`S=X_1+...+X_n`.

Write the marginal probabilities in decreasing order

`p_(1) >= p_(2) >= ... >= p_(n)`

and define

`R_q(m) := sum_{k=0}^n q_k min(k,m)`.

There exists a joint law of `(X_1,...,X_n)` with these marginals and

`P(S=k)=q_k` for every `k`

**if and only if**

1. total mean matches:

   `sum_{i=1}^n p_i = sum_{k=0}^n k q_k`,

2. for every `m=1,...,n-1`,

   `sum_{i=1}^m p_(i) <= R_q(m)`.

Equivalently, for every subset `A subseteq {1,...,n}`,

`sum_{i in A} p_i <= sum_k q_k min(k,|A|)`,

plus total-mean equality.

### Necessity

Let `K=S`. For every subset `A`, pointwise

`sum_{i in A} X_i <= min(K,|A|)`.

Taking expectations gives

`sum_{i in A} p_i <= E[min(K,|A|)] = R_q(|A|)`.

For a fixed cardinality `m`, the largest left side is obtained by taking the `m` largest coordinates, yielding the displayed sorted inequalities. Total-mean equality follows from `E[S]=sum_i E[X_i]`.

### Sufficiency

For `k=0,...,n`, let

`Delta(n,k) = conv{1_A : A subseteq [n], |A|=k}`.

This is the hypersimplex

`Delta(n,k) = {x in [0,1]^n : sum_i x_i=k}`.

A conditional law of a random `k`-subset has an inclusion-probability vector in `Delta(n,k)`, and conversely every point of `Delta(n,k)` is a convex combination of `k`-subset incidence vectors and therefore is realized by such a law.

Consequently the desired coupling exists exactly when

`p in C_q := sum_{k=0}^n q_k Delta(n,k)`

(Minkowski sum).

It remains to prove that the stated inequalities characterize `C_q`.

For any `c in R^n`, reorder coordinates so that

`c_1 >= c_2 >= ... >= c_n`,

and apply the same permutation to `p`. The support function of the hypersimplex is

`h_{Delta(n,k)}(c) = c_1+...+c_k`.

Hence

`h_{C_q}(c) = sum_k q_k (c_1+...+c_k)`.

Set `P_m=sum_{i=1}^m p_i`. Abel summation gives

`c dot p = c_n sum_i p_i + sum_{m=1}^{n-1} (c_m-c_{m+1}) P_m`.

Similarly, for each k,

`c_1+...+c_k = c_n k + sum_{m=1}^{n-1} (c_m-c_{m+1}) min(k,m)`.

After averaging with weights `q_k`,

`h_{C_q}(c) = c_n sum_k kq_k + sum_{m=1}^{n-1}(c_m-c_{m+1})R_q(m)`.

The total-mean equality and the assumed inequalities `P_m<=R_q(m)` imply

`c dot p <= h_{C_q}(c)`

for every `c`, because every coefficient `c_m-c_{m+1}` is nonnegative.

If `p` were not in the closed convex set `C_q`, the separating-hyperplane theorem would produce a vector `c` with

`c dot p > h_{C_q}(c)`, contradiction. Thus `p in C_q`, and decomposing `p=sum_k q_k u^(k)` with `u^(k) in Delta(n,k)` constructs the required coupling: sample `K~q`, then conditional on `K=k` sample a `k`-subset whose inclusion vector is `u^(k)`, and set `X_i=1_{i in A}`. QED.

### Three-margin corollary

For `n=3`, after sorting `p_1>=p_2>=p_3`, feasibility is equivalent to

`p_1+p_2+p_3 = q_1+2q_2+3q_3`,

`p_1 <= 1-q_0`,

`p_1+p_2 <= q_1+2q_2+2q_3`.

The lower bound `p_3>=q_3` is already contained in these by subtracting the second two-coordinate inequality from total-mean equality.

### Equal Bernoulli margins

If every margin is Bernoulli(p), then **every** cardinality law `q` with mean `np` is realizable. Indeed, conditional on `K=k`, choose a uniformly random `k`-subset. Every coordinate then has conditional inclusion probability `k/n`, so its unconditional marginal is `E[K]/n=p`.

This is a complete exact subclass theorem for D0012, but it remains only a subclass of the source's general arbitrary-margin aggregation-set problem.

## 4. B5 — add a parameter: the Bernoulli membership boundary is piecewise linear

Fix the Bernoulli marginal vector `p` and two target cardinality laws `q` and `q'` having the same mean as `sum_i p_i`. Define

`q(lambda)=(1-lambda)q+lambda q'`, `0<=lambda<=1`.

For each `m`, define the feasibility slack

`s_m(lambda)=R_{q(lambda)}(m)-sum_{i=1}^m p_(i)`.

The theorem gives an exact one-dimensional membership criterion:

`q(lambda)` is feasible **iff** `s_m(lambda)>=0` for every `m=1,...,n-1`.

Moreover

`d s_m / d lambda = sum_k (q'_k-q_k) min(k,m)`

is constant. Hence the feasible parameter set is a closed interval (possibly empty), and every boundary point is witnessed by a saturated top-m inequality. There is no hidden nonlinear obstruction in this Bernoulli slice of the aggregation problem.

This provides a clean sensitivity/continuation structure for exact finite-support experiments without mistaking them for a solution of the parent Open Problem 12.

## 5. Prior-art / novelty caution

The proof is a direct hypersimplex/base-polytope argument, so it should be regarded as likely standard polyhedral probability rather than new mathematics absent a dedicated literature check. A bounded web search on 2026-09-19 recovered modern hypersimplex rounding work that explicitly treats `Delta(n,k)` as the set of inclusion-probability vectors of random k-subsets, but did not expose this exact aggregation-membership statement. That search miss is not a novelty certificate.

The important research value here is narrower: it makes precise which finite-support D0012 subproblem is easy and thereby prevents a future worker from promoting a Bernoulli LP/polytope result to full source closure.

## 6. Admission consequences

### D0012

Disposition after this run: **HOLD_SCOPE / PENDING / NOT READY**.

Reasons:

- the source's literal target is a general characterization of aggregation sets, not just Bernoulli margins;
- the 2019 standard-uniform subclass is already a substantial later result and the current author's page explicitly calls Open Problem 12 only partially solved;
- the theorem above supplies another exact subclass but does not change that source-level quantifier;
- no source-valid full-closure metric can honestly be frozen from this subclass alone.

No claim is created.

### I0048 cross-check

The shard also contains I0048. Existing immutable R08 work already reconciles the preferential-attachment percolation threshold: Hazra--van der Hofstad--Ray (Electronic Journal of Probability, 2026) gives the fixed-outdegree threshold, and the R08 comparison shows that the zero/positive boundary agrees under exponent matching while positive numerical thresholds need not coincide. The broader word `results` in the historical source remains too unfrozen to manufacture a fresh residual CLOSABLE theorem. I0048 therefore remains unavailable as a fresh R7-05 successor.

### Remaining shard rows

The remaining visible shard-4 rows are excluded by current canonical claims/history, explicit retirement without release, or unresolved source-scope holds. No lawful fresh CLOSABLE successor is admitted in this run.

R7-05 remains `PENDING_ADMISSION`; no inherited C0031 metric or stagnation count is carried forward.
