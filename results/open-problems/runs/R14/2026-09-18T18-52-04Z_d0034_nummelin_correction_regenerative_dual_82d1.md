Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. CORRECTION / NO SOURCE-CLOSING MOVEMENT on D0034: the prior reported `N_rep: 2 -> 1` depended on an invalid m-step regeneration-independence step; the certified metric is restored to the admission baseline `N_rep: 2 -> 2`. Methods actually used: #11 DUALIZE, #12 FIND WHAT IS CONSERVED, #14 FIND THE GROUP ACTING.**

# R14 HARD OUTSIDE — D0034 correction and regenerative dual

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **D0034 PARTIAL / source OPEN / active R14 claim.** The negative-margin spherical perceptron, H0017, D0036, and D0039 remain handed off and are not reopened.

## 1. Continuity and mandatory reads

I reread the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the owner directive, the canonical claim `operations/claims/D0034.md`, the newest R14 report, the D0034 intake row and prior intake attempt, and neighboring admission/status reports. The current root `RESULTS.md` still warns that its R-series rows are stale and that newer immutable track reports control continuity.

The immediately preceding R14 report is

`runs/R14/2026-09-18T18-05-32Z_d0039_handoff_d0034_harris_collapse_4f71.md`.

It admitted Bradley Question 6 / D0034 after the mandatory D0039 handoff, fixed the Holroyd--Liggett stationary 1-dependent 4-coloring `X_HL` as the source-closing candidate, and defined

`N_rep = number of hidden-state cardinality regimes still requiring exclusion for X_HL after the known finite-state impossibility theorem.`

The canonical admission baseline is two regimes:

1. countably infinite-state stationary Markov representations;
2. genuinely general / uncountable-state Harris recurrent representations.

The prior report claimed to collapse (2) to (1), giving `2 -> 1`. The first obligation of this run was to audit the exact regeneration step before building on it.

## 2. Fresh source/current-literature check

Bradley's 2005 survey still states Question 6 in Section 3.3: whether there exists a strictly stationary `psi`-mixing, perhaps even 1-dependent, sequence that is not an instantaneous function of a strictly stationary Harris recurrent Markov chain.

Holroyd--Liggett, *Finitely Dependent Coloring* (Forum Math. Pi 4 (2016), e9), prove Schramm's finite-state hidden-Markov impossibility for every stationary finitely dependent proper coloring and explicitly state that the countable-state case remains open for their 1-dependent 4-coloring.

Holroyd--Hutchcroft--Levy, *Mallows Permutations and Finite Dependence* (Ann. Probab. 48 (2020), 343--379), construct other finitely dependent proper colorings that **are** functions of countable-state Markov chains, including a 1-dependent 5-coloring. Thus no blanket infinite-dimensional extension of Schramm's finite-state obstruction can be valid.

For the regeneration point below, current regeneration literature explicitly distinguishes one-step from m-step Nummelin splitting: with a one-step minorization the regenerative blocks are independent; with an `m>1` minorization the original-time blocks are in general only 1-dependent. A recent explicit statement is Choi--Ciolek, *Wild regenerative block bootstrap for Harris recurrent Markov chains*, arXiv:2510.17648 (2025), whose method treats either independent or one-dependent Nummelin blocks. This agrees with standard older treatments of regeneration-based statistics for Harris chains.

A bounded 2026-09-18 search did not locate a source-matching resolution of Bradley Question 6 or a theorem deciding whether the Holroyd--Liggett 1-dependent 4-coloring is a countable-state Markov factor. This is negative search evidence only, not a novelty certificate.

## 3. Required correction: the previous Harris-collapse proof has a real m-step gap

The previous report argued that an arbitrary stationary Harris recurrent chain can be Nummelin-split into iid original-time tours, mapped those tours to countably many finite output words, and then encoded the iid words by a countable word-position Markov chain.

The word-position construction is correct **if the output tours are iid**. The mistake is the sentence asserting iid original-time tours for a general `m`-step minorization.

For `m>1`, a regeneration at a skeleton endpoint resets the endpoint distribution but does not make the `m-1` intermediate original-time bridge coordinates independent of the adjacent tour. Standard Nummelin blocking therefore gives a 1-dependent sequence of original-time blocks, not an iid sequence. Equivalently, the bridge across a skeleton regeneration carries one unit of dependence across the putative word boundary.

Thus the implication

\[
\text{general stationary Harris representation}
\Longrightarrow
\text{countable-state Markov representation}
\]

was **not proved**. I do not claim it is false; I retract only the proof and the metric movement that depended on it.

The corrected metric is therefore the canonical admission value

\[
\boxed{N_{\rm rep}=2.}
\]

The prior `after=1` is not carried forward as certified progress.

A restricted version *is* valid: if the representing Harris chain admits a recurrent **one-step** small-set minorization (`m=1`, the strongly aperiodic split setting), the split tours are iid and the countable-output word-position construction does reduce that representation to a countable-state positive recurrent Markov representation. This is only a restricted Harris subclass and does not remove regime (2) from the fixed metric.

## 4. Method #11 — DUALIZE: exact regenerative formulation of the countable-state regime

The failed general-Harris collapse still leaves an exact and useful equivalence for the **countable-state** regime.

### Proposition 4.1 — countable Markov factors are exactly finite-mean latent iid-word concatenations

Let `A` be finite or countable and let `X=(X_i)_{i in Z}` be stationary and ergodic with values in `A`. The following are equivalent.

1. `X` is an instantaneous function of an irreducible positive recurrent countable-state stationary Markov chain.
2. `X` admits a stationary regenerative extension whose Palm blocks are iid finite `A`-words and whose block length has finite mean.

Here the regeneration boundaries are latent; they need not be measurable from `X`.

#### Proof: (1) -> (2)

Let `M` be an irreducible positive recurrent countable-state Markov chain with invariant law `pi`, and suppose `X_i=f(M_i)`. Choose any state `s` with `pi(s)>0`. Under the Palm law at a visit to `s`, successive return excursions from `s` to `s` are iid by the strong Markov property. Their lengths have finite mean `1/pi(s)` by Kac's formula. Mapping each excursion through `f` gives iid finite output words of finite mean length. The stationary law of `X` is exactly the equilibrium, length-biased concatenation of these latent words.

#### Proof: (2) -> (1)

Let the iid Palm word law be `q(w)` on a countable set of finite words, with `ellbar = sum_w q(w)|w| < infinity`. Use the countable hidden state space

\[
S=\{(w,r):q(w)>0,\ 1\le r\le |w|\}.
\]

Move deterministically from `(w,r)` to `(w,r+1)` and, at the end of a word, choose a fresh `w'` with probability `q(w')`. The invariant law is

\[
\pi(w,r)=q(w)/\bar\ell.
\]

Output the `r`th symbol of `w`. The resulting equilibrium word containing the origin is length-biased and the position is uniform, exactly matching the stationary regenerative extension. The hidden chain is countable, irreducible on the support of `q`, and positive recurrent. `□`

Therefore the surviving countable-state obligation can be restated exactly as

\[
\boxed{
\texttt{IID-WORD-HL: prove that }X_{HL}\text{ admits no finite-mean latent iid-word regenerative extension.}
}
\]

This is not yet a solution, but it removes irrelevant hidden-state coordinates and replaces the countable HMM question by a renewal/word-tiling problem directly on the output law.

### Why the dual route does not automatically solve the problem

At one fixed cut, a countable hidden Markov representation merely gives a countable mixture of product past/future laws. Since the set of finite words is already countable, a bare countable nonnegative factorization at a single cut is too weak. The real restriction is **shift-compatible finite-mean regeneration**. Any successful dual obstruction has to use that compatibility across all cuts, not just finite nonnegative rank.

## 5. Method #12 — FIND WHAT IS CONSERVED: the m-step bridge memory

The conserved object that killed the previous collapse is the intermediate `m-1`-step bridge attached to an `m`-skeleton regeneration. Resetting the skeleton endpoint does not erase that bridge from the original-time path. In the standard split-chain decomposition:

- `m=1`: successive original-time regenerative blocks are iid;
- `m>1`: successive original-time blocks are generally 1-dependent, while blocks two apart are independent.

This is not a bookkeeping nuisance: it is exactly the amount of memory that prevents the iid-word encoding in Proposition 4.1 from being applied to an arbitrary Harris representation.

Thus the correct general-Harris target is now sharper:

\[
\boxed{
\texttt{HARRIS-HL: rule out every finite-mean latent original-time word decomposition of }X_{HL}
\texttt{ obtainable from one-dependent Nummelin blocks.}
}
\]

I am using this only as a **necessary structural form** supplied by Harris regeneration, not claiming an equivalence between arbitrary one-dependent word tilings and Harris representations.

The distinction between `IID-WORD-HL` and `HARRIS-HL` is precisely the distinction between the two surviving `N_rep` regimes. That is why the metric must remain 2.

## 6. Method #14 — FIND THE GROUP ACTING: S4 symmetry rules out the most obvious observable regeneration

The full color-permutation symmetry and 1-dependence of `X_HL` give an exact local test for the simplest possible regeneration scheme.

Fix a color `c`. For `a,b != c`, symmetry and properness give

\[
P(X_0=c)=\frac14,
\qquad
P(X_{-1}=a\mid X_0=c)=P(X_1=b\mid X_0=c)=\frac13.
\]

Because sites `-1` and `1` are distance two apart, 1-dependence makes them unconditionally independent and uniform. Hence `P(X_{-1}=a,X_1=b)=1/16`. Conditional on the side colors:

- if `a=b`, the center can be any of the three remaining colors, symmetrically, so
  \[
  P(X_{-1}=a,X_0=c,X_1=a)=\frac1{48};
  \]
- if `a!=b`, the center can be either of the two colors different from `a,b`, symmetrically, so
  \[
  P(X_{-1}=a,X_0=c,X_1=b)=\frac1{32}.
  \]

Therefore

\[
\boxed{
P(X_{-1}=a,X_1=b\mid X_0=c)
=
\begin{cases}
1/12,&a=b,\\
1/8,&a\ne b,
\end{cases}
\qquad a,b\ne c.
}
\]

If the **observable event** `X_0=c` itself were a regeneration point for the full coloring, the left and right sides would be conditionally independent and every entry would be `1/9`. They are not. Thus occurrences of a color cannot themselves be the regeneration boundaries of the full process.

This does **not** contradict Holroyd--Liggett's theorem that the binary indicator `1[X_i=c]` is a renewal process. The binary indicator forgets which non-`c` colors appear on the two sides; that forgotten information is exactly where the conditional dependence above lives.

Consequently any countable-state Markov representation must use a **strict latent refinement** of each color fiber `f^{-1}(c)`. The easy route “use the known color-renewal points as hidden returns” is certified to fail for the full coloring.

This is a real obstruction to the most natural constructive representation, but it does not exclude all latent refinements and therefore does not move `N_rep`.

## 7. What the three attacks accomplished

- **#11 DUALIZE:** replaced the countable hidden-state problem by the exact `IID-WORD-HL` latent-regeneration problem. This route survives.
- **#12 FIND WHAT IS CONSERVED:** found a fatal bridge-memory gap in the previous general-Harris collapse. The earlier `2 -> 1` movement is retracted; general Harris remains a distinct regime.
- **#14 FIND THE GROUP ACTING:** used full `S_4` symmetry to prove that a color occurrence is not a regeneration point for the full coloring, so any hidden regenerative structure must be genuinely latent. This removes the most obvious constructive counter-route but not all countable representations.

No theorem here closes either surviving regime. D0034 remains **PARTIAL / OPEN**.

## 8. Fixed metric and stagnation discipline

Canonical fixed metric:

`N_rep = number of hidden-state cardinality regimes still requiring exclusion for X_HL after finite-state impossibility.`

- canonical admission baseline: `2`;
- previous report's claimed value: `1`, now **RETRACTED AS UNSUPPORTED** because of the m-step iid-block error;
- certified value entering this corrected run: `2`;
- certified value after this run: `2`;
- source-closing target: `0`.

So this run has **no source-closing movement**. The authoritative shared stagnation count remains `UNKNOWN`; I do not manufacture a streak from the corrected report.

The correction is substantive research hygiene, not a metric improvement. No finite checker is appropriate: the new claims are theorem-sized and are proved on the page.

## 9. Next new-method attack

The next triple must not repeat `#11,#12,#14`. The most informative next run is:

- **#2 ATTACK THE NEGATION FIRST:** actively try to construct a countable-state representation of `X_HL` by refining the known one-color renewal points; if it succeeds, this candidate is dead and R14 must seek another source-valid Bradley-Q6 process.
- **#18 SAY IT IN ANOTHER LANGUAGE:** translate `IID-WORD-HL` into a shift-compatible positive-realization / formal-language renewal equation for the exact Holroyd--Liggett cylinder probabilities, rather than one-cut nonnegative rank.
- **#24 FIND THE EXTREMAL OBJECT:** identify the minimal latent refinement at a color-renewal point compatible with the exact 3-by-3 side-color matrix above, and test whether repeated refinement forces infinite-mean regeneration or a contradiction.

A useful success criterion is not another local identity. It is either (i) an explicit positive recurrent countable hidden chain for `X_HL`, which refutes this candidate route, or (ii) a proof that every finite-mean iid-word regenerative extension violates an exact family of Holroyd--Liggett cylinder probabilities, which would eliminate the countable-state regime and move `N_rep:2 -> 1` for real.

## 10. Model / scheduler control

The exposed scheduler surface still provides prompt/title/schedule/timing/enabled controls but no binding model-family selector, reasoning-effort selector, guaranteed-runtime field, or authenticated completed-run model telemetry. Thus the requested `GPT-6 / maximum` remains prompt-only; this report does not claim it ran.

The historical `You cannot modify this task` response for one P26 context is an authorization-context issue, not something to bypass. Repository evidence records that P26 was later updated successfully from another authorized context. The valid workaround for any still-inaccessible task remains the owning/admin context or platform support; no scheduler state, permission, workflow, or duplicate task was changed here.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R14
  lane: HARD OUTSIDE
  active_target:
    id: D0034
    source: "Bradley 2005, Basic Properties of Strong Mixing Conditions, Question 6"
    candidate: "Holroyd-Liggett stationary 1-dependent 4-coloring"
    status: "PARTIAL / OPEN"
    claim_path: operations/claims/D0034.md
  metric:
    name: N_rep
    definition: "hidden-state cardinality regimes still requiring exclusion after finite-state impossibility"
    canonical_admission_baseline: 2
    prior_reported_after: 1
    correction: "prior 2->1 movement retracted; general m-step Nummelin blocks are only 1-dependent, not iid"
    before_this_run: 2
    after_this_run: 2
    movement: false
    authoritative_stagnation_count: UNKNOWN
  methods_actual: [11, 12, 14]
  proved_this_run:
    - "Countable positive recurrent Markov factor iff there exists a finite-mean latent iid-output-word regenerative extension"
    - "Restricted one-step-minorization Harris outputs collapse to the countable-state word-position construction"
    - "For X_HL, conditioning on X_0=c gives side-color probabilities 1/12 on the diagonal and 1/8 off diagonal; an observable color occurrence is not a full-process regeneration point"
  retracted_this_run:
    - "General countable-output Harris-collapse lemma from the preceding report; proof invalid for m>1 splitting"
  remaining_obligations:
    - IID-WORD-HL
    - HARRIS-HL
  source_resolution: "none found in bounded 2026-09-18 search"
  novelty: "UNVERIFIED; no novelty claim for standard regeneration facts or the word-position encoding"
  new_finite_claims: 0
  artifacts_created: 0
  next_methods: [2, 18, 24]
  prohibited_actions_taken: []
```
