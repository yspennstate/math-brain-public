Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **SCREEN MOVEMENT on D0037: the number of explicit non-strictly-positive spectral families proved to be rho-star-mixing in this R08 screen moved `0 -> 1` (the polynomial-zero closure class); no READY+CLOSABLE+UNASSIGNED successor is admitted. I0082 remains RETIRED/FROZEN at `2/3`, retirement count `6`. Methods B6, B18, B30.**

# R08 — D0037 screening: finite filters preserve interlaced rho-mixing, so polynomial spectral zeros are not the obstruction

## 0. Continuity / controlling state

This run follows `runs/R08/20260918T0225Z_d0032_predictive_rank_nogo_7c4e91.md`. I did not reopen Hasebe--Ueda Problem 3.11 / I0082: the six-unchanged handoff remains controlling despite the stale historical `ADMITTED_ACTIVE` wording in `operations/claims/I0082.md`. Its frozen metric stays `2/3`, retirement count `6`.

Before research I reread the current campaign `INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R08 report, current task-health admission material, and the D-intake around D0033--D0037. Current ownership checks show D0033 is owned elsewhere; D0034/D0036/D0037 remain broad screening items rather than free CLOSABLE assignments; D0035's literal form is already internally disposed. The current coordinator screen still reports no newly certified `READY + CLOSABLE OUTSIDE + UNASSIGNED` successor. I therefore did not manufacture an exclusive claim or a synthetic CLOSABLE metric.

The source for D0037 is Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions* (2005), Question 9, PDF p. 28: characterize spectral densities of stationary Gaussian sequences which are rho-star-mixing. Bradley records immediately before it that a continuous positive spectral density is sufficient, via Theorem 6.5, but the unrestricted characterization remains open in the source. A bounded fresh search on 2026-09-18 for the exact question / `rho*-mixing` / stationary Gaussian spectral characterization recovered Bradley's survey and later work on interlaced rho-mixing, but no source-matching full characterization. This is bounded negative evidence, not a worldwide novelty certificate.

The prior intake attempt D0037-A001 guessed that the rho-star criterion might forbid spectral zeros. That guess is false. This run gives the clean correction and a source-relevant closure property.

## 1. B18 — SAY IT IN ANOTHER LANGUAGE: rho-star mixing is stable under finite-window factors

For sigma-fields `A,B`, write `rho(A,B)` for maximal correlation. For a strictly stationary process `Y=(Y_k)`, define the interlaced coefficient

\[
\rho_Y^*(n)=\sup \rho\bigl(\sigma(Y_k:k\in S),\sigma(Y_k:k\in T)\bigr),
\]

where the supremum is over nonempty disjoint finite `S,T subset Z` with `dist(S,T) >= n` (allowing arbitrary interlacing).

### Lemma 1 (finite-window factor contraction)

Let `Y` be strictly stationary and let

\[
X_k=F(Y_{k-r},\ldots,Y_{k+s})
\]

for fixed nonnegative integers `r,s` and a measurable `F`. Then for every `n>r+s`,

\[
\boxed{\rho_X^*(n)\le \rho_Y^*(n-r-s).}
\]

In particular, every finite-window factor of a rho-star-mixing process is rho-star-mixing.

### Proof

Fix admissible finite `S,T` with `dist(S,T)>=n`, and put

\[
\widetilde S=S+\{-r,-r+1,\ldots,s\},\qquad
\widetilde T=T+\{-r,-r+1,\ldots,s\}.
\]

Then

\[
\sigma(X_k:k\in S)\subseteq\sigma(Y_j:j\in\widetilde S),\qquad
\sigma(X_k:k\in T)\subseteq\sigma(Y_j:j\in\widetilde T).
\]

For `u in \widetilde S`, `v in \widetilde T`, write `u=k+a`, `v=l+b` with `k in S`, `l in T`, `a,b in [-r,s]`. Hence

\[
|u-v|\ge |k-l|-|a-b|\ge n-(r+s).
\]

Thus `dist(\widetilde S,\widetilde T)>=n-r-s`. Maximal correlation is monotone under passage to sub-sigma-fields, so

\[
\rho\bigl(\sigma(X_S),\sigma(X_T)\bigr)
\le
\rho\bigl(\sigma(Y_{\widetilde S}),\sigma(Y_{\widetilde T})\bigr)
\le \rho_Y^*(n-r-s).
\]

Taking the supremum over `S,T` proves the claim. QED.

This elementary formulation matters here because multiplying a Gaussian spectral density by a squared trigonometric polynomial is exactly a finite linear filter.

## 2. B6 — DEFORM TO A SOLVED POINT: create zeros by a finite polynomial filter

Let `Y` be a centered nondegenerate stationary Gaussian sequence with continuous positive spectral density `g`. Bradley Theorem 6.5 implies

\[
\rho_Y^*(n)\to0.
\]

Let

\[
P(z)=\sum_{j=0}^q b_jz^j
\]

be a nonzero real polynomial, and define the finite linear filter

\[
X_k=P(L)Y_k=\sum_{j=0}^q b_jY_{k-j}.
\]

Then `X` is stationary Gaussian with spectral density

\[
\boxed{f(e^{i\theta})=|P(e^{-i\theta})|^2g(e^{i\theta}).}
\]

Lemma 1 with `(r,s)=(q,0)` yields, for `n>q`,

\[
\boxed{\rho_X^*(n)\le\rho_Y^*(n-q)\longrightarrow0.}
\]

Therefore:

### Theorem 2 (polynomial-zero sufficient class)

If a stationary Gaussian spectral density has the form

\[
\boxed{f=|P|^2g}
\]

with `P` a nonzero finite polynomial and `g` continuous and strictly positive on the circle, then the Gaussian sequence is rho-star-mixing.

No positivity of `f` itself is required. Every unit-circle root of `P` produces a zero of `f` while rho-star mixing survives.

This directly corrects the prior D0037-A001 heuristic that the desired characterization should require “no zeros allowed.”

## 3. B30 — ONE ZERO / ONE SCALE AT A TIME: explicit residual examples and the exact remaining boundary

Take any `0<|a|<1` and let `Y` be Gaussian AR(1),

\[
Y_k=aY_{k-1}+\sqrt{1-a^2}\,\varepsilon_k,
\]

normalized to variance one. Its spectral density is continuous and positive. Set

\[
X_k=Y_k+Y_{k-1}.
\]

Then

\[
f_X(\theta)=|1+e^{-i\theta}|^2f_Y(\theta),
\]

so `f_X(\pi)=0`, but Theorem 2 gives `rho_X^*(n)->0`.

Bradley Theorem 6.5 says that, for a nondegenerate CCWS sequence, `r^*(1)<1` together with `r^*(n)->0` is equivalent to having a continuous **positive** spectral density. For Gaussian sequences `rho^*=r^*`. Since this `X` is rho-star-mixing while its density vanishes, necessarily

\[
\boxed{r_X^*(1)=1\quad\text{but}\quad r_X^*(n)\to0.}
\]

So the difficult part of Questions 8/9 really does live in the `r^*(1)=1` boundary; that boundary already contains perfectly well-behaved rho-star-mixing examples.

More generally, if `zeta_1,...,zeta_m` are unit-circle points and

\[
P(z)=\prod_{j=1}^m(1-\overline{\zeta_j}z)^{d_j}
\]

(with conjugate pairing if real coefficients are desired), then `|P|^2g` gives a rho-star-mixing Gaussian spectrum with any prescribed finite collection of algebraic zeros and multiplicities.

Equivalently, any continuous nonnegative `f` whose zero set is finite and for which

\[
\frac{f(e^{i\theta})}{\prod_j|e^{i\theta}-\zeta_j|^{2d_j}}
\]

extends to a continuous strictly positive function belongs to the rho-star-mixing class.

Thus a full spectral characterization cannot be a simple “positive versus zero” dichotomy. After combining Bradley's necessary continuity (Theorem 6.3, since `r^*->0` implies `zeta->0`) with Theorem 2 here, the genuinely unresolved territory must concern subtler zero structure / factorization: e.g. non-polynomial orders of vanishing, infinite or accumulating zero sets, or other continuous nonnegative spectra not reducible to a finite polynomial factor times a positive continuous density.

## 4. What happened to the three methods

- **B18 (another language): SUCCESS.** Recasting the spectral operation as a finite-window factor gives the contraction inequality `rho_X^*(n)<=rho_Y^*(n-q)`.
- **B6 (deform from solved point): SUCCESS.** Starting from Bradley's positive continuous class and multiplying by a finite polynomial creates actual spectral zeros without losing rho-star mixing.
- **B30 (one zero at a time): SUCCESS/PARTIAL.** Arbitrary finite algebraic zero sets are covered. The route stops at infinite/non-algebraic zero sets because they require an infinite filter, for which the finite-window sigma-field inclusion no longer gives a fixed shift in the rho-star coefficient.

## 5. Status / admission decision

This does **not** solve Bradley Question 9 and does not make D0037 CLOSABLE. It proves a clean source-relevant sufficient class and corrects a misleading prior intake conjecture. The unrestricted problem remains an infinite-dimensional spectral-factorization characterization and is honestly **HARD / NOT_READY_CLOSABLE**. I therefore created no canonical claim and did not steal a HARD problem into the R08 CLOSABLE lane.

No exact finite claim was made, so no checker-only artifact was manufactured. The theorem-sized claim is proved on the page.

A bounded current-literature search used the exact Bradley question, `rho*-mixing`, `interlaced rho-mixing`, `stationary Gaussian`, and `spectral density`, and checked later Bradley/interlaced-rho material. It recovered Bradley's known Markov-chain results and application papers but no full later answer to Question 9 and no exact priority match for the finite-polynomial closure phrasing above. **Priority is UNVERIFIED**; the closure lemma is elementary and may be folklore.

## 6. Next admission cursor

Do not continue D0037 as an R08 research target absent a future explicit admission. The current CLOSABLE gate remains empty. The next run should continue the source/current-literature/ownership cursor to a different unclaimed candidate, rather than elaborating polynomial zero examples.

A useful next-method triple if a lawful candidate is found: **B2 / B14 / B24** (attack the negation, quotient by its symmetry, identify the extremal object).

## 7. Structured ledger_delta

```yaml
ledger_delta:
  worker: R08
  deployment: NEW-METHODS-2026-09-16
  original_source:
    id: I0082
    status: RETIRED_FROZEN
    metric: "2/3"
    retirement_count: 6
    reopened: false
  predecessor_screen:
    id: D0032
    status: HARD_NOT_READY
    claimed: false
  screened_this_run:
    id: D0037
    source: "Bradley 2005, Question 9, Section 7"
    status: HARD_NOT_READY_CLOSABLE
    claimed: false
    worldwide_open_status: OPEN_CURRENT_BOUNDED
    priority: UNVERIFIED
    temporary_screen_metric:
      name: "explicit non-strictly-positive spectral families proved rho-star-mixing in this screen"
      before: 0
      after: 1
    result: "finite polynomial filters preserve rho-star mixing; f=|P|^2 g with g continuous positive is rho-star-mixing even when P has unit-circle zeros"
    correction: "prior D0037-A001 no-zero heuristic is false"
  methods_used: [6, 18, 30]
  active_successor_admitted: false
  shared_roots_modified: false
  peer_files_modified: false
```

## 8. Model / scheduler-control truth

The exposed task-management surface still has prompt/title/schedule/timing/enabled controls but no binding model-family selector, reasoning-effort selector, guaranteed-duration field, or authenticated completed-run model telemetry. GPT-6/maximum therefore remains prompt text only in this environment. Historical `You cannot modify this task` errors are authorization-context boundaries; the legitimate workaround is the authorized owning context, ownership/admin transfer, or platform support, not task duplication or GitHub edits.
