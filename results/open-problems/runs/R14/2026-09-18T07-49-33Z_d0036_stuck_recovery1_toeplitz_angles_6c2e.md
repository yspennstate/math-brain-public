Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on D0036: `C_power: 1 -> 1`; authoritative stagnation count remains UNKNOWN. SECTION-I STUCK-RECOVERY-1/2. Methods actually used: #1 CHANGE THE CATEGORY, #20 FIND WHY THE ALGORITHM FAILS, #28 REPLACE "FOR ALL" WITH "FOR TYPICAL".**

# R14 — Bradley Question 8 stuck recovery 1: from alias witnesses to separated Toeplitz-subspace angles

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 0. Continuity, source and why this is a thinking run

Repository continuity still controls over the stale native scheduler title. I do **not** reopen the negative-margin spherical perceptron, H0017, I0089, or BIS32. The perceptron handoff retains its last supported bracket

\[
6.30297437506\le \alpha_c(-1)\le 12.78437096216,
\qquad
\alpha_U-\alpha_L=6.48139658710,
\]

and H0017 already consumed both permitted hard-task recoveries and was terminally handed off. R14's current exclusive HARD OUTSIDE claim remains `operations/claims/D0036.md`: Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, Probability Surveys 2 (2005), Section 6.5, Question 8.

Bradley's exact source question asks for a condition on a spectral density that is necessary and sufficient for a centered complex weakly stationary sequence to satisfy the interlaced linear dependence condition `r*(n)->0`. The arXiv source `math/0511078` was re-opened on 2026-09-18. Bounded fresh searches on 2026-09-18 for Bradley Question 8, `r*(n)`, interlaced maximal correlation, spectral density, and later Bradley work again found later papers on interlaced mixing but no source-matching full spectral characterization. This is bounded negative evidence only; it is not a worldwide openness or novelty certificate.

At run start I reread the current campaign `INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the D0036 exclusive claim, the newest R14 report, the neighboring R08 D0037 report, and the D-intake/search hits around Bradley Questions 8--9. The newest R14 report records three consecutive D0036 runs with the frozen metric unchanged and explicitly triggers Section I. The shared numeric stagnation field remains `UNKNOWN`, so I do not invent a number.

This is therefore the required **thinking-only stuck recovery 1/2**. Per Section I I make no new theorem claim and create no checker-only artifact. The purpose is to identify the exact obstruction and select one genuinely different recovery route.

## 1. Frozen metric

The frozen D0036 metric remains

`C_power in {0,1}`.

It moved `0 -> 1` when R14 classified the finite algebraic-zero family and is now saturated. It is not replaced by a new metric merely to manufacture progress.

**Before: `C_power=1`. After: `C_power=1`. NO MOVEMENT.**

The current simplest unresolved test family retained from the preceding reports is

\[
f_*(e^{it})
:=
\frac{|1-e^{it}|^2}
{\log\!\left(2e/|1-e^{it}|\right)}
\quad (t\ne0),
\qquad f_*(1):=0.
\tag{1.1}
\]

The preceding R14 reports prove neither `r^*_{f_*}(n)->0` nor its negation.

## 2. Section-I item (a): the exact blocking statement

Let

\[
\gamma(k)=\frac1{2\pi}\int_{-\pi}^{\pi}e^{ikt}f_*(e^{it})\,dt.
\]

For a finite nonempty `Q subset Z`, let

\[
G_Q=(\gamma(q-q'))_{q,q'\in Q},
\]

and for finite `Q,S` let

\[
G_{Q,S}=(\gamma(q-s))_{q\in Q,s\in S}.
\]

The unresolved special case is exactly the uniform separated-subspace estimate

\[
\boxed{
\lim_{n\to\infty}
\sup_{\substack{Q,S\subset\mathbb Z\ \text{finite, nonempty}\\
\operatorname{dist}(Q,S)\ge n}}
\left\|
G_Q^{-1/2}G_{Q,S}G_S^{-1/2}
\right\|_{2\to2}
=0\ ?
}
\tag{2.1}
\]

with the usual restriction to the nondegenerate quotient if a finite Gram matrix has a null direction. This is simply the finite-dimensional spectral/Hilbert-space form of the source coefficient `r^*(n)`, not a new characterization claim.

Every successful lower-bound witness so far has attacked one highly structured pair `(Q,S)`. Equation (2.1) shows why that has stopped being enough: an upper bound must be uniform over **arbitrary finite, arbitrarily interlaced separated sets and arbitrary coefficient vectors**, while a counterexample is free to choose a geometry outside every fixed filter family.

## 3. Section-I item (b): every route tried and the precise failure

### Earlier D0036 routes

1. **#2 / #18 / #25 — fractional powers, Helson--Sarason/VMO, double exponent count.**  
   This succeeded on the finite algebraic-zero subclass: the local power exponent must match an even polynomial multiplicity, while finite polynomial factors preserve the positive-continuous sufficient class. It does not decide a zero with an additional slowly varying factor such as `(1.1)`.

2. **#3 / #12 / #30 — stronger local invariant, separated-set geometry, one scale at a time.**  
   For the order-zero logarithmic family
   \[
   h_\beta(t)=\left[\log\left(2e/|1-e^{it}|\right)\right]^{-\beta}
   \]
   R14 obtained a block alias obstruction with ordinary `r(n)->0` but nondecaying `r^*`. That obstruction is carried by a low-frequency block-average direction. Multiplication by the allowed factor `|1-e^{it}|^{2m}`, `m>=1`, removes exactly that direction from the tangent calculation, so the same witness no longer survives.

3. **#6 / #11 / #24 — deform, dualize, optimize the one-scale alias witness.**  
   For fixed smoothing order and legal separated decimation, the tangent alias profile becomes bandlimited; the very inequality needed to make the coordinate blocks separated also places every nonzero periodization mode outside the Fourier support. The phase contrast therefore vanishes.

4. **#4 / #7 / #19 — complete the fixed-order repeated-box family.**  
   The latest report closed the obvious escape hatches: every fixed integer box order `q`, every polynomial-zero order `m>=1`, and every legal physical gap `d_M->infinity` are asymptotically phase-blind. This is a route no-go, not a proof of `r^*`-mixing.

### This recovery's three new attacks

5. **#1 CHANGE THE CATEGORY — Toeplitz subspace angles.**  
   Instead of asking for another filter, rewrite the problem as `(2.1)`: angles between two coordinate subspaces in the weighted polynomial Hilbert space `L^2(f_* dt)`. The allowed factor `|1-z|^2` is multiplication by the first-difference symbol. In coefficient space, a finite polynomial of the form `(1-z)p(z)` has a vanishing total coefficient on each isolated finite component before different components interact. Thus the order-zero block-average direction that powered the `h_\beta` counterexample is no longer an admissible local direction after the difference factor. This reformulation identifies the real missing estimate but does not itself supply the uniform operator bound.

6. **#20 FIND WHY THE ALGORITHM FAILS — invert the difference to import the old bad witness.**  
   The natural counterexample algorithm is: start with the bad low-frequency block average for `h_1`, solve `(1-z)p \approx` that block average on one separated set, and reuse the order-zero correlation. The finite-support inverse necessarily introduces a compensating lobe because a finite first difference has zero total mass. Moving that compensating mass far away enlarges support and consumes separation; keeping it nearby destroys the desired block-average profile. The fixed-box theorems are concrete manifestations of this conflict. The route therefore lacks an explicit normalized witness whose compensation cost stays negligible while `dist(Q,S)->infinity`.

7. **#28 REPLACE "FOR ALL" WITH "FOR TYPICAL" — rejected for the source supremum.**  
   Random or typical separated sets may have small correlations, but `r^*(n)` is a worst-case supremum over all finite separated sets. Typical-set control is useless unless preceded by a structural theorem saying every near-extremizer can be replaced by one in the controlled typical class with negligible loss. No such near-extremizer reduction is currently available. Thus this method, by itself, cannot move the source quantity.

## 4. Section-I item (c): what a proof must contain that no current route contains

There are now two honest ways to decide `(1.1)`, and each requires an ingredient absent from every route above.

### Upper-bound route

Prove a **uniform arbitrary-geometry Toeplitz-angle estimate**: there must be an explicit `epsilon(n)->0` such that for every finite separated `Q,S`, regardless of the number, length, or interlacing of connected components,

\[
\left\|G_Q^{-1/2}G_{Q,S}G_S^{-1/2}\right\|
\le \varepsilon(\operatorname{dist}(Q,S)).
\tag{4.1}
\]

The proof has to exploit the vanishing-moment structure created by `|1-z|^2` without paying a factor proportional to the number of components and without losing control when `G_Q` or `G_S` has very small eigenvalues. None of the alias calculations is uniform over arbitrary coefficient geometry.

### Counterexample route

Construct explicit separated sets `Q_n,S_n` and coefficient vectors `a^{(n)},b^{(n)}` such that their `L^2(f_*)`-normalized cross correlation stays bounded below by a positive constant while `dist(Q_n,S_n)->infinity`. Such a witness must escape the componentwise zero-sum / vanishing-moment mechanism that kills the old block-average construction and must not belong to any fixed-order repeated-box family already ruled out.

A proof of either form would decide the special case. Current work supplies neither.

## 5. Section-I item (d): simplest special case still unproved

The simplest unresolved case remains exactly

\[
\boxed{
f_*(e^{it})=
\frac{|1-e^{it}|^2}{\log(2e/|1-e^{it}|)}.
}
\tag{5.1}
\]

It is deliberately chosen because it is one integer polynomial zero times the simplest logarithmic factor that, without the integer zero, already gives an explicit separation between ordinary `r` and interlaced `r^*`. Deciding `(5.1)` is strictly more informative than manufacturing another fixed-filter no-go and is the chosen recovery target.

## 6. Section-I item (e): nearest solved problems and exactly what they have that `(5.1)` lacks

Two neighboring solved regimes bracket `(5.1)`.

1. **Bradley's positive-continuous regime.** The source records a clean interlaced criterion when the spectral density is continuous and strictly positive (equivalently, uniformly bounded away from zero on the compact circle once continuity is fixed). In Hilbert-space terms the finite Toeplitz Gram matrices are uniformly conditioned. The present `f_*` has a zero, so that coercivity is exactly what is missing.

2. **Finite polynomial-zero closure.** The neighboring R08 argument and R14's algebraic-zero classification show that if
   \[
   f=|P|^2g,
   \]
   with `P` a finite polynomial and `g` continuous strictly positive, then the finite-window factor contraction transfers interlaced mixing from `g` to `f`. The residual factor `1/log(2e/|1-e^{it}|)` in `(5.1)` is not positive at the zero and, by the preceding R14 order-zero construction, is itself on the bad side of `r^*`. Therefore the finite-window contraction has no good base process from which to transfer.

The missing ingredient is consequently neither another polynomial factorization nor ordinary one-sided mixing. It is a mechanism showing that **one exact vanishing moment can neutralize the bad logarithmic low-frequency mode uniformly for every separated finite subspace**, or an explicit witness proving that it cannot.

## 7. Required recovery choice

I choose exactly one Section-I action:

**PROVE THE SIMPLEST UNPROVED SPECIAL CASE `(5.1)`.**

The next substantive R14 invocation should attack `(2.1)` directly rather than extend the box-filter family. A successful run must either prove a uniform estimate of type `(4.1)` or exhibit a fully normalized separated-set counterexample. If it again leaves the same obligation unchanged, that will be hard-task recovery 2/2, after which a further stuck episode requires terminal handoff/rotation rather than another lemma.

The next deliberately different Section-B triple is:

- **#9 RANDOMIZE:** use randomization only as an analytic device for arbitrary coefficient/component decompositions, not as a replacement for the worst-case supremum;
- **#15 BREAK THE SYMMETRY ON PURPOSE:** isolate a single ordered neighboring pair of components and test whether the global angle can be reduced to summable boundary interactions without losing normalization;
- **#21 ASK WHO ELSE HAS THIS SHAPE:** search the Toeplitz/weighted-polynomial/orthogonal-polynomial literature for a uniform separated-subspace angle theorem that survives a single logarithmically softened Fisher--Hartwig zero.

## 8. Prior-art / source check this run

Fresh bounded searches dated 2026-09-18 included:

- `Bradley 2005 Question 8 r*(n) spectral density necessary sufficient interlaced maximal correlation`;
- `Bradley r-star mixing spectral density stationary Gaussian interlaced rho mixing characterization`;
- exact arXiv source `math/0511078`;
- later Bradley interlaced-rho / reversible-Markov / INAR papers.

They recovered Bradley's source and later interlaced-mixing examples/results, including the fact that ordinary rho-mixing and interlaced rho-mixing can differ, but did not surface a source-matching full spectral characterization or a theorem deciding `(5.1)`. **Open status and priority remain bounded-search / UNVERIFIED beyond the source and checked literature.** No novelty claim is made for the Toeplitz-angle reformulation.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R14
  deployment: NEW-METHODS-2026-09-16
  stale_native_prompt_target:
    id: negative_margin_spherical_perceptron
    reopened: false
    last_supported_bracket:
      lower: 6.30297437506
      upper: 12.78437096216
      width: 6.48139658710
  prior_hard_target:
    id: H0017
    status: TERMINALLY_HANDED_OFF
    reopened: false
  active_target:
    id: D0036
    source: "Richard C. Bradley (2005), Question 8"
    allocation: HARD_OUTSIDE
    claim: operations/claims/D0036.md
    status: PARTIAL_OPEN_LOOKING_BOUNDED_SEARCH
  metric:
    name: C_power
    before: 1
    after: 1
    movement: NO_MOVEMENT
    authoritative_stagnation_count: UNKNOWN
  stuck_protocol:
    triggered_by_three_consecutive_unchanged_reports: true
    recovery: 1/2
    thinking_only: true
    new_theorem_claims: false
    chosen_action: PROVE_SIMPLEST_UNPROVED_SPECIAL_CASE
    special_case: "f_*(e^{it})=|1-e^{it}|^2/log(2e/|1-e^{it}|)"
  methods_used: [1, 20, 28]
  next_methods: [9, 15, 21]
  exact_blocker: "uniform Toeplitz-subspace angle in equation (2.1)"
  remaining_obligation: "decide r*_{f_*}(n)->0 by a uniform arbitrary-geometry upper bound or an explicit separated-set lower-bound witness"
  artifacts_created: false
  audits: 0/2
  shared_roots_modified: false
  peer_files_modified: false
```

## 10. Model and scheduler-control truth

The exposed task-management surface still offers prompt/title/schedule/timing/enabled controls but no binding model-family selector, reasoning-effort selector, guaranteed-duration field, or authenticated completed-run model telemetry. GPT-6/maximum therefore remains prompt-only; this run cannot truthfully claim it actually executed.

The historical `You cannot modify this task` behavior is an authorization-context boundary, not a mathematical issue. The repository records that P26 later updated successfully in an authorized context, while other IDs could still reject edits elsewhere. The legitimate remedies are the owning/admin context or platform support, not task duplication, permission bypass, or a GitHub edit. No scheduler setting was changed in this run.
