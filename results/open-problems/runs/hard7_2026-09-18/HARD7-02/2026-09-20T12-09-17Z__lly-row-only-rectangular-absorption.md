Model: **GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did not run on GPT-6 at verified maximum reasoning. NO MOVEMENT: external/source-verified `p_comb<=2 -> <=2`; in-track written candidate `p_comb<=1 -> <=1` remains pending independent validation. Methods tried this run: B7 / B12 / B27.**

# HARD7-02 — Li--Litvak--Yu Conjecture 3.9: row-only rectangular absorption and the exact terminal-column obstruction

Date: 2026-09-20 UTC  
Track: `HARD7-02`  
Status: **PARTIAL / SOURCE OPEN**  
Frozen metric: `p_comb`  
External verified value before/after: **`<=2 -> <=2` (no movement)**  
Internal written milestone before/after: **`<=1 -> <=1` pending independent validation**  
Post-STUCK1 ordinary no-movement count: **1**

## 1. Continuation / control read

This is a continuation of the exclusively owned Li--Litvak--Yu target, not a restart and not a return to the released Han band target. I reread the controlling files

- `operations/hard7_2026-09-18/CONTROL.md`,
- `operations/NEW_METHODS_2026-09-16.md`,
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`,
- `probability_campaign_2026_09/INDEX.md`,
- `probability_campaign_2026_09/RANKING.md`,
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`,
- the current claim `operations/claims/LI-LITVAK-YU-2026-SPARSE-COMBINATORIAL-CIRCULAR-LAW.md`,
- the immediately preceding HARD7-02 checkpoint `2026-09-20T11-14-09Z__lly-stuck1-dynamic-absorption-port.md`,
- the nearby non-Hermitian handoffs `R7-05/C0031` and `R7-06/C0032`, and available intake/circular-law surfaces.

No collision, posting, later source resolution, or competing owner for this exact independent-row fixed-row-sum target was found. C0031/C0032 are heavy-tail questions with different source models; the previously released Han periodic band target is also distinct. No shared root ledger is edited in this run.

The exact source remains Dongbin Li, Alexander E. Litvak and Tingzhou Yu, *Least singular values of shifted sparse random combinatorial matrices*, arXiv:2604.10446v2 (11 August 2026). Conjecture 3.9 asks for the circular law in probability whenever `d(n)->infinity`. Corollary 1.4 proves it under `d >= log^(2+eps) n`, `d=o(n)`. A fresh bounded 20 September 2026 search of the arXiv identifier, v1/v2 titles, authors, and exact fixed-row-sum/circular-law aliases again found no later theorem lowering that hypothesis for this precise model. This is bounded negative evidence, not a novelty certificate.

Source: https://arxiv.org/abs/2604.10446  
SSS comparison source: A. Sah, J. Sahasrabudhe, M. Sawhney, *The sparse circular law, revisited*, arXiv:2310.17600v2, https://arxiv.org/abs/2310.17600 .

## 2. What I tried first: break the STUCK1 port

STUCK1 selected the Sah--Sahasrabudhe--Sawhney dynamic singular-value absorption mechanism as the recovery route. I first attacked the negation of the naive port.

The direct statement “a fresh column remains Bernoulli-like at every late exposure time” is **false** in the row-combinatorial model. If the first `n-1` coordinates of a fixed row have been revealed, then the last coordinate is forced by the row-sum constraint. Thus at the final column step the conditional success probability is exactly `0` or `1`; there is no fresh column randomness at all.

This is an obstruction to a proof route, **not** a counterexample to Conjecture 3.9. It explains why the iid SSS half-step process cannot simply be copied through time `n`.

The useful outcome of B7/B12/B27 is twofold:

1. before the terminal reservoir becomes too small, the conditional columns *do* admit an exact inhomogeneous Bernoulli description and SSS-scale anti-concentration;
2. more importantly, there is an exact **row-only rectangular determinant absorption** identity that eliminates dependent-column additions entirely, because the rows of the Li--Litvak--Yu model are genuinely independent.

The second point is the new route I would pursue next.

## 3. B12 — residual density is an exact martingale

Let a row

`Y_i=(Y_{i1},...,Y_{in})`

be a uniform indicator of a `d`-subset of `[n]`, and let

`F_k = sigma(Y_{ij}: i<=n, j<=k)`.

For row `i`, put

`S_i(k)=sum_{j<=k} Y_{ij}`,  `r_i(k)=d-S_i(k)`,  `m_k=n-k`,

and

`q_i(k)=r_i(k)/m_k`.

Then `q_i(k)` is exactly the conditional density of a `1` in the next unrevealed coordinate.

### Lemma 3.1 (residual-density martingale)

For every fixed row `i`, `(q_i(k))_{0<=k<n}` is a martingale. For deterministic `K<n`, writing `p=d/n`,

`E q_i(K)=p`,

and

`Var(q_i(K)) = K p(1-p) / ((n-1)(n-K))`.

Consequently, for every `delta>0`,

`P(max_{0<=k<=K} |q_i(k)-p| >= delta p)
 <= K(1-p)/(delta^2 p (n-1)(n-K)).`

#### Proof

Condition on `F_k` and set `m=n-k`, `r=r_i(k)`. The next bit is Bernoulli with success probability `r/m`, and

`q_i(k+1)=(r-Y_{i,k+1})/(m-1)`.

Therefore

`E[q_i(k+1)|F_k]=(r-r/m)/(m-1)=r/m=q_i(k)`.

Also `S_i(K)` is hypergeometric with parameters `(n,d,K)`, so

`Var S_i(K)=K p(1-p)(n-K)/(n-1)`.

Since `q_i(K)=(d-S_i(K))/(n-K)`, the variance formula follows. Apply Doob's maximal inequality to the square of the centered martingale `q_i(k)-p`. `square`

This is the conserved object found by B12: not a deterministic degree, but the exact rowwise residual-density martingale.

## 4. B7+B27 — uniform regularity works with a reservoir, and quantifiably fails at the end

Set `delta=1/2`. If `K=n-L`, Lemma 3.1 gives, for `n>=2`,

`P(max_{k<=K}|q_i(k)-p|>p/2) <= 8 n/(d L)`.

Let

`ell_d = floor((n/(2d)) log log d)`

(the SSS small-height spread scale), and define the uniform bad-row set

`B_L={i: max_{k<=n-L}|q_i(k)-p|>p/2}`.

By row independence plus only Markov's inequality,

`E|B_L| <= 8 n^2/(dL)`

and hence

`P(|B_L|>ell_d/4) <= C n/(L log log d)`

for an absolute constant `C`, for all large `n` with `d->infinity`, `d=o(n)`.

In particular, choose

`L_n = ceil(n/sqrt(log log d)).`

Then with probability

`1-O((log log d)^(-1/2))`,

**simultaneously for every `k<=n-L_n`**, all but `ell_d/4` rows satisfy

`p/2 <= q_i(k) <= 3p/2`.

Thus every coordinate set of size at least `ell_d` contains at least `3ell_d/4` conditionally regular rows at every such time. This is the useful B27 quantifier swap: one does not need every row regular, only fewer exceptional rows than the spread set can avoid.

The same argument also identifies the terminal obstruction. The certificate deteriorates when `L` falls below order `n/log log d`; and at `L=1` individual regularity is impossible, because all `q_i(n-1)` are `0` or `1`. The `n/log log d` transition is only a threshold of this *certificate*, not a claimed necessary threshold for the model.

## 5. Exact conditional fresh-column law

### Lemma 5.1

Conditioned on `F_k`, the next column

`X^(k+1)=(Y_{1,k+1},...,Y_{n,k+1})`

has independent coordinates, with

`X_i^(k+1) | F_k ~ Ber(q_i(k)).`

#### Proof

The original rows are independent. Conditional on the first `k` entries of row `i`, its remaining `n-k` coordinates are uniformly distributed among vectors with exactly `r_i(k)` ones. Hence its next bit is Bernoulli `q_i(k)`, independently across rows. `square`

So column dependence is not mysterious: after a past-column filtration, the next column is an **inhomogeneous product Bernoulli vector**. The problem is that the parameters become degenerate near the end.

## 6. Inhomogeneous SSS-scale anti-concentration before the terminal reservoir

The next statement is a direct Lévy--Kolmogorov--Rogozin consequence and is included because it pins down exactly how much of SSS survives before the terminal obstruction.

### Proposition 6.1 (inhomogeneous spread small-ball bound)

Suppose `X=(X_i)` has independent Bernoulli coordinates, and for a set `G` one has

`p/2 <= P(X_i=1) <= 3p/2 <= 1/2`, `i in G`.

Suppose `|G^c|<=ell/4`. Let `v in C^n` have at least `ell` coordinates satisfying `|v_i|>=rho`. Then for every fixed `A>=1`, uniformly in `y in C`,

`P(|<X,v>-y| <= A rho) <= C_A / sqrt(ell p).`

In particular, if `ell=ell_d`, then

`P(|<X,v>-y| <= A rho) <= C_A / sqrt(log log d).`

#### Proof

Among the `ell` significant coordinates, at least `3ell/4` lie in `G`. For at least half of those, one common real axis (`Re` or `Im`) has coefficient magnitude at least `rho/sqrt(2)`. Thus there is a set `J` with `|J|>=3ell/8` and real coefficients `a_i` satisfying `|a_i|>=rho/sqrt(2)`.

Condition on all coordinates outside `J`. For `i in J`, the two atoms of `a_i X_i` are separated by at least `rho/sqrt(2)`. At radius `rho/(4sqrt(2))`, its concentration function is at most `1-P(X_i=1)`, so the missing concentration mass is at least `p/2`. Lévy--Kolmogorov--Rogozin therefore gives

`Q(sum_{i in J} a_i X_i, A rho) <= C_A / sqrt(|J|p)`.

Conditioning on the omitted coordinates merely translates the small ball; average the resulting bound. Since `ell_d p=(1/2+o(1))log log d`, the final assertion follows. `square`

### Corollary 6.2 (projection version)

At a history satisfying the good-row event above, let `V` be an `F_k`-measurable `h`-dimensional subspace with an orthonormal basis `B` such that every `v in B` has at least `ell_d` coordinates of magnitude at least `rho`. Let `P_V` be orthogonal projection and `w` be `F_k`-measurable. Then

`P( ||P_V(X^(k+1)+w)||_2 <= rho sqrt(h) | F_k )
 <= C / sqrt(log log d)`

for `k<=n-L_n`.

#### Proof

If the squared norm is at most `rho^2 h`, then at least `h/2` basis vectors satisfy

`|<X^(k+1)+w,v>| <= sqrt(2) rho`.

Hence the event indicator is at most `(2/h)` times the sum of the corresponding individual indicators. Apply Proposition 6.1 to each basis vector and average. `square`

With the SSS choice

`rho=eta_r d^(1/2) h^(-1/2)`,

the projection threshold is exactly `eta_r d^(1/2)`, and the error has the same `O((log log d)^(-1/2))` form as SSS's small-`h` estimate. **But this only covers the column exposure while a sufficiently large reservoir remains. It does not justify the terminal SSS half-steps.**

That qualification is decisive; I am not promoting this to a full dynamic port.

## 7. The better route: remove columns from the dynamics entirely

The row-combinatorial model has a feature absent from the difficult column half-steps: its rows are exactly independent. This suggests deliberately breaking SSS's row/column symmetry.

For fixed Girko shift `z`, write, at the unnormalized level,

`A(z)=M-z sqrt(d(1-d/n)) I_n`,

and let `A_t(z)` be its first `t` rows, a `t x n` matrix. The new row at time `t+1` is

`x_{t+1}=Y_{t+1}-z sqrt(d(1-d/n)) e_{t+1}`,

and is independent of `A_t(z)`.

### Proposition 7.1 (one-sided rectangular row absorption identity)

Let `B` be any full-row-rank `t x n` complex matrix with `t<n`, and append a row `x` to form `B_+`. Then

`det(B_+ B_+^*) = det(BB^*) * ||P_{ker B} x^*||_2^2.`

Consequently, on the event that all intermediate row blocks have full row rank, for every `m<n`,

`|det A_n(z)|^2
 = det(A_m(z)A_m(z)^*)
   * product_{t=m}^{n-1} ||P_{ker A_t(z)} x_{t+1}^*||_2^2.`

#### Proof

Write the Gram matrix in block form:

`B_+B_+^* = [[BB^*, Bx^*],[xB^*, ||x||_2^2]].`

Taking the Schur complement of the invertible block `BB^*` gives

`det(B_+B_+^*)
 = det(BB^*) [ ||x||_2^2 - xB^*(BB^*)^{-1}Bx^* ].`

The bracket is exactly the squared norm of the component of `x^*` orthogonal to the row space of `B`, i.e. `||P_{ker B}x^*||_2^2`. Iterate. `square`

The identity itself is elementary Schur-complement folklore; no novelty claim is made for it. The research point is that it changes the *category* of the SSS closure obligation: instead of alternating dependent columns and independent rows, the full determinant can be grown from a wide rectangular block by **independent row additions only**.

This is much better adapted to the source model.

## 8. Exact second-moment geometry of a fresh slice row

The fixed-sum constraint removes only the constant direction at covariance level.

Let `Y` be a uniform `d`-subset indicator and `p=d/n`. Then

`E Y = p 1`

and exactly

`Cov(Y)=p(1-p) * n/(n-1) * (I - 11^*/n).`

Hence, for every deterministic `h`-dimensional subspace `V`,

`E ||P_V(Y-p1)||_2^2
 = p(1-p) * n/(n-1)
   * ( h - ||P_V 1||_2^2/n )
 >= p(1-p) * n/(n-1) * (h-1).`

The same lower bound remains true after adding any deterministic shift `a`, because

`E||P_V((Y-p1)+a)||^2
 = E||P_V(Y-p1)||^2 + ||P_V a||^2.`

For the row-absorption process, conditional on `A_t`, take `V=ker A_t`, `h=n-t`, and `a=p1-z sqrt(d(1-d/n))e_{t+1}`. Thus

`E[ ||P_{ker A_t} x_{t+1}^*||_2^2 | A_t ]
 >= p(1-p) n/(n-1) (h-1).`

So, except for the final one-dimensional kernel, the natural projection-energy scale is exactly

`sqrt(p h) = sqrt(dh/n)`

up to constants. This matches the scale one expects for an iid sparse row. The row constraint costs at most **one dimension** in the second moment.

This does not by itself give a lower-tail bound; it identifies the correct scale and the only deterministic covariance defect.

## 9. What has actually changed mathematically

The frozen exponent did not move, but the closure obligation did.

Before this run, the selected recovery was “port the SSS dynamic method despite dependent columns.” That formulation hides a genuine impossibility: the final conditioned column is deterministic. The current state is sharper:

- the naive column port is refuted as a route by the exact terminal-reservoir obstruction;
- an SSS-scale inhomogeneous anti-concentration statement is rigorously available before terminal depletion;
- there is an exact row-only multiplicative determinant evolution in which every increment is an **independent fixed-sum row**;
- fixed-sum covariance shows that an `h`-dimensional kernel retains the iid projection-energy scale in all but one dimension.

The new route is therefore to prove a **slice-row projection lower-tail theorem** for the evolving right kernel and combine it with a rectangular base log-volume theorem. It does not require a fresh-column theorem at all.

## 10. Exact remaining blocker

A source-closing row-only argument would need a statement of the following form, at the scales relevant to the log potential.

For `m=(1-eps)n` and every `m<=t<n`, writing `h=n-t`, establish, with a summable/accumulable error over the row-addition path,

`P( ||P_{ker A_t(z)}(Y_{t+1}-z sqrt(d(1-d/n))e_{t+1})||_2
      <= eta_{t,h} sqrt(dh/n)
    | A_t(z))
 <= q_{t,h}`

with the total negative-log cost

`(1/n) sum_{t=m}^{n-1} |log eta_{t,h}| = o_eps(1)`

and total failure/drift cost small enough to close the Girko comparison as `eps->0`, **uniformly for `d->infinity`** (or first for the intended logarithmic milestone).

The structural problem is now transparent: a slice row is blind to the constant direction, so a one-dimensional kernel spanned by `1` has no centered anti-concentration. For `h>=2`, the covariance computation says this defect can consume only one dimension, but turning that fact into an adequately strong lower-tail estimate for the random, history-dependent kernel is the missing step.

The simplest still-unproved special case is:

> If `V` is an `h`-dimensional subspace with `h>=2` and no unit vector in `V` is almost constant at the slice scale, prove an SSS-strength lower tail for `||P_V(Y+a)||_2`, uniformly in the deterministic shift `a`, for a uniform `d`-subset indicator `Y`, assuming only `d->infinity`.

Li--Litvak--Yu Lemma 6.4 already supplies a one-dimensional small-ball inequality for a uniform fixed-sum row against a non-almost-constant vector. What is missing is a basis/structural theorem for the *evolving kernel* strong enough to tensorize that slice anti-concentration without reintroducing the `C log n` net/expansion threshold.

## 11. Nearest solved mechanism and why it does not immediately close this

Sah--Sahasrabudhe--Sawhney prove the iid Bernoulli circular law for the optimal regime `d=np->infinity` by dynamically exposing rows and columns. Their small-height step uses an orthonormal basis of the small-singular subspace whose vectors have at least

`ell=(n/(2d)) log log d`

coordinates above the required scale, followed by a Lévy--Kolmogorov--Rogozin bound giving `O((log log d)^(-1/2))` small-ball error.

Li--Litvak--Yu's source has two relevant ingredients: independent fixed-sum rows and a fixed-sum small-ball inequality for non-almost-constant vectors. Their present steep-vector/expansion implementation, however, is developed in the `d >= C log n` least-singular-value range, and their introduction explicitly emphasizes the asymmetry between `M` and `M^T` caused by dependent columns.

The row-only identity above is designed to remove precisely that transpose/column half of the SSS route.

## 12. Methods audit (the three required fresh Section-B moves)

### B7 — TAKE THE LIMIT

I tracked the conditional row density as `d->infinity` and identified an SSS-scale regime in which the inhomogeneous column small-ball error is still `O((log log d)^(-1/2))`. This works before terminal reservoir depletion, but the limit also exposes the exact last-column degeneracy.

**Outcome:** useful partial theorem; direct all-the-way column port fails.

### B12 — FIND WHAT IS CONSERVED

The exact conserved object is the residual-density martingale `q_i(k)`. On the row-only route, the fixed-sum covariance is exactly isotropic on `1^perp`; the row constraint removes only the constant direction.

**Outcome:** successful structural reduction, with explicit formulas.

### B27 — SWAP THE QUANTIFIERS

Instead of demanding every conditional row probability remain near `p`, I allowed an exceptional row set smaller than the SSS spread set. This proves uniform anti-concentration over every spread set while a reservoir remains. The swap cannot fix the terminal step because at one remaining column every row is conditionally deterministic.

**Outcome:** successful until the terminal reservoir; exact failure mode identified.

## 13. Next route if this target continues

Do **not** spend the next run refining the martingale constants. The route has moved categories.

Next three proposed Section-B moves, distinct from this run:

- **B4 — PROVE SOMETHING WEAKER, COMPLETELY:** prove a one-sided rectangular dynamic theorem under an abstract “kernel vectors are non-almost-constant” hypothesis.
- **B15 — BREAK THE SYMMETRY ON PURPOSE:** use only independent row additions, never conditional column additions.
- **B19 — MAKE IT AN ALGORITHM:** write an explicit row-absorption schedule from an `(1-eps)n x n` rectangular block to the square matrix and account exactly for log-volume cost at every step.

A promising bridge is to combine Proposition 7.1 with Li--Litvak--Yu Lemma 6.4 rather than with their full square least-singular-value theorem.

## 14. Honest labels / protocol

- Source Conjecture 3.9: **OPEN**.
- This run: **PARTIAL**.
- External verified frozen milestone: **`p_comb<=2`**.
- In-track `p_comb<=1`: still **pending independent validation**, unchanged.
- No finite enumerative claim was introduced, so no checker was manufactured merely for bookkeeping.
- Proposition 7.1 is elementary linear algebra and is explicitly treated as folklore mechanism, not novelty certification.
- No closure, refutation, or source-level solution is claimed.
- No paper folder or audit request is created because closure conditions are not met.

## 15. Runtime / scheduler status requested by owner

Still true in this invocation: there is **no native scheduler field exposed here for model selection, reasoning/effort selection, or guaranteed run duration**. The available task controls are title/prompt, schedule/timing mode, and enabled state. Therefore “GPT-6, maximum” can be requested in prompt text but cannot be authenticated or bound by this worker. A real fix requires the scheduler/product backend to expose and honor model and effort selectors (and runtime policy), not another wording change in the prompt.

This run actually reports **GPT-5.6 Sol / reasoning UNVERIFIED** and does not claim otherwise.

For the historical P26 task that returned `You cannot modify this task`: this worker will not bypass the ownership/permission failure by recreating or duplicating that schedule. The lawful workaround is modification by the task's authorized owner through an interface that has write permission, or a platform/support-side permission repair; if neither is available, leave that task untouched and use a separately authorized audit path rather than silently replacing it.

## 16. Root-ledger delta for owner-controlled merge

No shared root ledger was edited. The delta to record, if the owner merges it later, is:

`HARD7-02 | Li--Litvak--Yu Conj. 3.9 | p_comb | external <=2 -> <=2; internal <=1 remains unaudited | PARTIAL | new row-only rectangular determinant absorption route; direct SSS column port has exact terminal determinism obstruction`
