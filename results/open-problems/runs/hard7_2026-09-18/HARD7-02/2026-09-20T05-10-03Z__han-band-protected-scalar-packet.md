Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **NO MOVEMENT in the frozen source metric: `beta_band <= gamma_* -> beta_band <= gamma_*`, `gamma_* = log_2(5)/(log_2(5)+1/5) = 0.920695597782722...`. Methods tried: B9 / B20 / B28. Substantive progress: a protected three-interval packet in the scalar hard band is proved to have the same outer-only deformation geometry as Han's full-block packet, and a new all-minor matching theorem gives the full `det(I+Q^*Q)^{1/2}` coefficient-norm lower/upper scale despite the triangular scalar interfaces. The exact remaining local obstruction is now the deformation-uniform **evaluation** small-ball estimate for the Ferrers residual, not coefficient visibility.**

# HARD7-02 — second/final Section-I recovery: protected scalar packet and all-minor coefficient visibility

Status: **PARTIAL / SOURCE OPEN / STUCK2 recovery.** No circular-law exponent improvement, closure, or independent audit is claimed. This consumes the second Section-I recovery on the present Han scalar-Rademacher target. If the next bounded run does not move the frozen source metric, the control contract requires an immutable handoff and rotation to a fresh eligible HARD7-02 target rather than a third recovery on this problem.

## 1. Continuity, ownership, source status, and evidence consumed

This run resumes the exclusive claim

`operations/claims/HAN-2026-PERIODIC-RADEMACHER-BAND-CIRCULAR-LAW.md`

and the immediately preceding checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-20T04-10-04Z__han-band-baseline-correction-phase-twist.md`.

I re-read the required control and fleet surfaces rather than restarting:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md`, `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- current HARD7-02 claim and the newest HARD7-02 report chain;
- repository alias searches for `2609.01295`, the periodic Rademacher scalar band target, and neighboring non-Hermitian claims;
- the nearby retired R7-05/C0031 heavy-tail handoff, which remains a different a.s.-ESD endpoint and is not an alias of this target;
- intake/queue surfaces available through repository search. No peer claim was overwritten and no shared root ledger was edited.

The source model remains frozen: for cyclic distance `dist_N`,

`X_ij = epsilon_ij / sqrt(2W_N+1)` if `dist_N(i,j)<=W_N`, and `0` otherwise,

with iid symmetric Rademacher `epsilon_ij`. The source question is circular-law convergence for every `W_N -> infinity`.

### Current literature baseline rechecked

1. Yi Han, *The circular law for non-Hermitian random band matrices: optimal bandwidth, periodic profile and discrete law*, arXiv:2609.01295v2, revised 8 September 2026, https://arxiv.org/abs/2609.01295v2 . The paper explicitly states the global-universality prediction `W_N -> infinity`; it proves the optimal scalar hard-indicator result under bounded density and proves a discrete theorem at `W_N >> log N` only for the different periodic **full-block** geometry. Its Section 7 / Proposition 7.3 is the local deformation-uniform three-block estimate used below as a comparison target.
2. Yi Han, arXiv:2508.18143v3, revised 12 September 2026, https://arxiv.org/abs/2508.18143v3 . For the exact scalar flat Rademacher strip, Assumption 1.8 with `q=1` and Theorem 1.12 give the presently certified exponent

`gamma_* = log_2(5)/(log_2(5)+1/5) = 0.920695597782722...`.

3. The older `8/9` theorem in arXiv:2410.16457v3 is not evidence for the frozen Rademacher atom because its relevant non-Gaussian theorem assumes bounded density. That applicability correction was made in the preceding run and is preserved.

A bounded fresh search through 20 September 2026 found no later theorem reducing `gamma_*` for the exact scalar periodic Rademacher hard-indicator model. This is bounded negative evidence, not a global novelty certificate.

### Metric

`beta_band = inf { beta in [0,1] : for every eps>0, the circular law is rigorously known for the frozen model whenever W_N >= N^(beta+eps) eventually }`.

Before: `beta_band <= gamma_*`.

After: `beta_band <= gamma_*`.

**No movement.** The auxiliary theorem below changes the identified bottleneck but does not imply a new bandwidth exponent.

## 2. Runtime capability honesty

The repository's current deployment ledger still records that the exposed task interface has controls for prompt/title/schedule/timing/enabled state but **no binding model selector, no reasoning-effort selector, no authenticated reasoning telemetry, and no guaranteed execution duration**. Thus `GPT-6 maximum` remains prompt-requested only. This invocation identifies as GPT-5.6 Sol; reasoning effort is UNVERIFIED.

The old `You cannot modify this task` event for P26 is historical, not a current universal P26 failure: current `RESULTS.md` records that P26's full update later succeeded in an authorized context. The safe workaround for an immutable/permission-denied native task is therefore to use an authorized owning context or obtain platform/workspace authorization; it is **not** to duplicate the schedule or bypass permissions. Making GPT-6/maximum enforceable would require the platform to expose and bind model/reasoning selectors to the native scheduled task. No scheduler setting was changed in this run.

## 3. Idea before code

The preceding run proved that the obvious `R^5` separator recursion cannot be improved by deterministic block-inverse bookkeeping, and that a scalar boundary phase has a universal average negative-log bound but lacks a transfer to the physical phase. I therefore did not continue that route.

The new idea is to import the *geometry* of Han's discrete full-block proof without pretending that a scalar band already contains full-block interfaces.

Take three consecutive intervals of **scalar coordinates**, each of length exactly `W`:

`L={-W,...,-1}`, `C={0,...,W-1}`, `R={W,...,2W-1}`.

For the hard scalar mask `|i-j|<=W`:

- every coordinate in the middle interval `C` is farther than `W` from the complement of `L union C union R`;
- hence conditioning/eliminating the complement can deform only the outer coordinates `O=L union R`;
- inside the packet, `LxL`, `CxC`, and `RxR` are complete random squares;
- the `L-C` and `C-R` interfaces are Ferrers triangles rather than complete squares.

This is exactly the deformation support needed by Han's full-block Proposition 7.3: the arbitrary outside matrix lives only on the two outer sites. The question is whether the loss of complete outer-center rectangles destroys the coefficient geometry or only the evaluation anti-concentration.

The main result of this run proves it does **not** destroy the coefficient geometry.

Only after proving the matching theorem below did I write the finite checker.

## 4. B9 RANDOMIZE / fresh exposure: the scalar band contains a protected packet with outer-only deformation

### Lemma 4.1 — protected scalar packet

Assume the ring is large enough that the displayed `3W` interval is represented without wrap-around; this is automatic in the sublinear-band regime after a cyclic relabelling. Let

`P=L union C union R`, with `L,C,R` as above, and let `P^c` be the complementary coordinates.

Then the scalar hard-band mask has no entries between `C` and `P^c`.

### Proof

The closest point of `P^c` to the left endpoint `0` of `C` is `-W-1`, at distance `W+1`. The closest point of `P^c` to the right endpoint `W-1` of `C` is `2W`, again at distance `W+1`. Every other center/complement pair is farther apart. Since the mask contains exactly distances at most `W`, there are no `C-P^c` or `P^c-C` entries. ∎

Consequently, whenever the complement is Schur-complemented (or the corresponding determinant identity is continued algebraically through singular complement configurations), its entire effect on the retained `3W` coordinates is supported on `O=L union R`. In the local packet notation the terminal matrix has the form

`H_sc(Q;x)=Delta_sc(x)-z I_{3W}+Emb_O(Q)`

for a completely arbitrary `2W x 2W` outside deformation `Q`, exactly as to deformation support in Han's full-block packet. What differs is only the fresh mask `Delta_sc`.

This is useful because it rules out the earlier worry that direct scalar-band links from the center necessarily create an arbitrary center deformation. Reserving three **width-W scalar intervals**, rather than three smaller artificial blocks, protects the center exactly.

## 5. B20 FIND WHY THE ALGORITHM FAILS: all outer minors remain visible

The full-block proof uses two distinct facts:

1. every outer minor of `Q` occurs in the packet coefficient vector (Han Lemma 7.5 / Section 9.1.3); and
2. after an RRQR pivot removal, the random residual can be covered by two complete iid squares of size `Theta(W)`, allowing two applications of Cook's deformed-square theorem (Han Section 9.1.2, especially equations (9.26)--(9.35)).

A priori the scalar Ferrers interfaces could have killed item 1. They do not.

### Theorem 5.1 — all-minor matching for the protected scalar packet

Let `M_W` be the bipartite row-column mask on `P=L union C union R`, with an edge `(i,j)` exactly when `|i-j|<=W`. Put `O=L union R`.

For **every** `I,J subset O` with `|I|=|J|`, the induced bipartite graph between packet rows `P\I` and packet columns `P\J` has a perfect matching.

Equivalently, every equal-size outer minor `det Q_{I,J}` occurs as the deterministic coefficient of at least one square-free atom monomial in

`det(Delta_sc(x)+Emb_O(Q))`.

### Proof

Write

`a=|L\I|`, `b=|R\I|`, `c=|L\J|`, `e=|R\J|`.

Because `|I|=|J|`,

`a+b=c+e`.

Set `delta=a-c=e-b`.

We use two elementary Ferrers facts. For a left row `p in L`, its center-column neighbours are

`{0,1,...,W+p}`.

Thus for any chosen set `S subset L`, if its elements are ordered so that the thresholds `t(p)=W+p` increase, matching row `p` to center column `t(p)` gives a triangular incidence matrix with nonzero diagonal. Hence **every** subset of `d` left rows can be matched injectively to `d` center columns. By reflection, every subset of `d` right columns can be matched injectively from `d` center rows. The row/column reversed statements also hold.

#### Case 1: `delta>=0`

Then `a=c+delta` and `e=b+delta`.

- Match any `c` of the surviving left rows bijectively to all `c` surviving left columns. This is allowed because `LxL` is complete.
- The remaining `delta` left rows are matched, by the Ferrers construction above, to `delta` center columns.
- Match all `b` surviving right rows bijectively to any `b` surviving right columns, using the complete `RxR` square.
- The remaining `delta` right columns are matched from `delta` center rows by the reflected Ferrers construction.
- Exactly `W-delta` center rows and `W-delta` center columns remain. Match them inside the complete `CxC` square.

The selected center rows and center columns in the two Ferrers steps are independent coordinate roles, so there is no conflict.

#### Case 2: `delta<0`

Put `d=-delta`. Then `c=a+d` and `b=e+d`.

- Match all surviving left rows to `a` surviving left columns; match the remaining `d` left columns from `d` center rows by the reflected Ferrers construction.
- Match `e` surviving right rows to all surviving right columns; match the remaining `d` right rows to `d` center columns by the Ferrers construction.
- Match the remaining `W-d` center rows to the remaining `W-d` center columns inside `CxC`.

Again every selected edge has distance at most `W`, and every surviving row and column is used exactly once. This is a perfect matching. ∎

### Corollary 5.2 — scalar-packet coefficient norm sees the full exterior volume

At zero shift, let the active scalar packet entries have deterministic magnitudes comparable to `W^{-1/2}` (in the frozen model they are exactly `(2W+1)^(-1/2)`) and independent formal variables. Set

`p_Q(x)=det(Delta_sc(x)+Emb_O(Q))`,

`C_sc,0(Q)=||Coeff_x p_Q||_2`.

Then uniformly in `Q in C^{2W x 2W}`,

`exp(-C W log W) det(I+Q^*Q)^(1/2) <= C_sc,0(Q) <= exp(C W log W) det(I+Q^*Q)^(1/2)`.

For the exact frozen normalization one can take the explicit lower prefactor `(2W+1)^(-3W/2)` before absorbing it into `exp(-C W log W)`.

### Proof

Fix `I,J subset O`, `|I|=|J|=k`. A packet atom matching of all rows and columns outside `I,J` contributes a square-free monomial whose coefficient is, up to sign,

`w_alpha det Q_{I,J}`,

where `w_alpha` is the product of the selected packet weights. Theorem 5.1 gives at least one such monomial for every `(I,J)`. With frozen weights,

`|w_alpha|^2=(2W+1)^(-(3W-k)) >= (2W+1)^(-3W)`.

Distinct matchings use distinct sets of atom coordinates, hence give distinct square-free monomials; their squared coefficients do not cancel in coefficient `l^2`. Therefore

`C_sc,0(Q)^2 >= (2W+1)^(-3W) sum_{k=0}^{2W} sum_{|I|=|J|=k} |det Q_{I,J}|^2`.

Conversely, every atom monomial is a partial row-column matching. There are at most

`sum_{t=0}^{3W} binom(3W,t)^2 t! <= exp(C W log W)`

such monomials, and each frozen weight product has modulus at most one. Hence the same all-minor sum gives the upper bound within `exp(CW log W)`.

Finally Cauchy-Binet, applied to the `4W x 2W` matrix `[I_{2W};Q]`, gives the exact identity

`sum_{k=0}^{2W} sum_{|I|=|J|=k} |det Q_{I,J}|^2 = det(I_{2W}+Q^*Q)`.

Taking square roots proves the claim. ∎

### Nonzero shift

If `|z|<=W^K`, each random diagonal entry is `rho x-z=rho(x-z/rho)` with `rho=(2W+1)^(-1/2)`. Translating the `3W` diagonal formal variables acts on each two-dimensional coefficient space `span{1,x}` by a triangular map whose norm and inverse norm are at most `1+|z|/rho <= W^{K+O(1)}`. Tensoring over `3W` diagonal variables costs only `exp(C_K W log W)`. Thus the same coefficient-volume comparison survives every fixed/polynomial spectral shift at the precision needed by the transfer method.

### What this rules out

The scalar packet does **not** fail because some large exterior minor is invisible to its atom polynomial. At the `exp(O(W log W))` precision used by Han's transfer argument, its coefficient norm carries the same exterior volume `det(I+Q^*Q)^(1/2)` as the full-block packet.

This was not assumed from finite computations; the proof above is for every `W`.

## 6. Exact negation test, written only after the proof

I then tested the negation of Theorem 5.1 exhaustively for `W=1,...,5`: every equal-cardinality outer deletion pair `(I,J)` was enumerated and the **explicit construction in the proof**, not merely a generic maximum-matching solver, was checked to use every surviving row/column exactly once and only edges satisfying `|i-j|<=W`.

Executed counts:

- `W=1`: 6 deletion pairs;
- `W=2`: 70;
- `W=3`: 924;
- `W=4`: 12,870;
- `W=5`: 184,756.

These counts equal `binom(4W,2W)`, as they should from `sum_k binom(2W,k)^2`.

Checker:

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-20T05-10-03Z__protected-scalar-packet-matching-check.py`

creation commit `37ecbe7d56452296419ab2876ddcf6e9556014c6`.

Executed output:

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-20T05-10-03Z__protected-scalar-packet-matching-check.out`

creation/readback commit `ba8b4591f9771cc9f980f979f4970e39d8005cb1`, ending

`ALL_EXACT_CHECKS_PASS = True`.

This is a self-check, not an independent audit.

## 7. B20 continued — the exact unpaid lemma is evaluation, not coefficient visibility

Trying to transplant Han Proposition 7.3 now fails at a sharply located place.

After RRQR removes the very large singular directions of `Q`, Han's full-block proof has residual outer row/column sets with counts `a,b,c,e`, `a+b=c+e`, plus all `W` central coordinates. In the full-block mask, Section 9.1.2 chooses two disjoint **complete iid squares**, each of size `Theta(W)`, covering every residual row and column. It then invokes Cook's deformed-square theorem twice. This is the step behind equations (9.26)--(9.35) of arXiv:2609.01295v2.

For the scalar interval mask the same complete-square cover is false. The cleanest witness is the extreme residual pattern

`a=W, c=0, b=0, e=W`.

The residual rows are `L union C` and the residual columns are `C union R`. The random support is

`[ Ferrers(L,C)      0          ]`
`[ complete(C,C)     Ferrers(C,R)]`.

There cannot be two complete random squares covering all `2W` residual rows and columns: after using the only `W x W` complete center square, the remaining `L x R` rectangle has no random entries. Yet Theorem 5.1 shows that this residual graph still has a perfect matching (indeed the two Ferrers pieces themselves have triangular perfect matchings).

So the full-block Step 2 fails **strictly before** coefficient reconstruction but **strictly after** combinatorial nondegeneracy.

A sufficient local lemma, now isolated without the old monodromy language, is:

> **Scalar Ferrers residual lemma (unproved).** Uniformly over all equal-size outer deletions `I,J` generated after the RRQR pivot, and uniformly over every independent polynomial-norm deterministic residual deformation `D`, prove a determinant/least-singular-value lower tail strong enough to give
>
> `P{|det(Z_res(I,J)+D)| <= exp(-C W log W)} <= p_W`, with `p_W=o(1)`,
>
> for the induced Rademacher scalar-band residual of dimension between `W` and `3W`.

A polynomial least-singular-value estimate would suffice, but the determinant formulation may be strictly easier because the Ferrers extreme has strong triangular determinant structure before deformation.

This is a materially different obstruction from the previous `det(I-P)` physical-twist resonance: we have moved the problem back to a **single protected local packet** with a fully explicit interval mask and arbitrary polynomial deformation after large-direction factorization.

## 8. B28 REPLACE FOR ALL WITH TYPICAL — a weighted-minor route instead of worst-pivot RRQR

The failed full-block transplant suggests not insisting on a worst-case coordinate pivot `(I,J)`.

The coefficient proof supplies a canonical probability measure on outer minors:

`pi_Q(I,J) = |det Q_{I,J}|^2 / det(I+Q^*Q)`, summed over all `|I|=|J|`.

Cauchy-Binet proves exactly that `sum_{I,J} pi_Q(I,J)=1`.

This gives a different possible route: replace the lexicographically selected RRQR minor by a **typical minor under `pi_Q`** and seek an averaged Ferrers-residual estimate. Large exterior volume is then sampled according to the same weights that actually constitute the packet coefficient norm. The scalar matching theorem guarantees that every sampled minor has at least one admissible atom matching, so no coefficient mass falls into an impossible residual geometry.

Why this is potentially useful:

- the circular-law argument ultimately needs normalized log determinant for Lebesgue-a.e. fixed `z`, not a uniform theorem over every adversarial exterior frame;
- a weighted-minor estimate could tolerate a small set of geometrically extreme deletion profiles if their total `pi_Q` mass is small;
- it avoids trying to prove a super-regular least-singular-value theorem for every Ferrers deletion pattern simultaneously.

What is **not** proved: pointwise determinant evaluations are sums of many minor channels and can cancel. The `pi_Q` identity is an `l^2` coefficient identity, not a direct mixture representation for `p_Q(Xi)`. An additional orthogonalization or anti-cancellation step is required. The prior scalar phase-twist average suggests one possible mechanism, but the previous run already showed that transferring an auxiliary complex twist to the physical phase is not automatic. I therefore do not count this as a source-level bound.

A sharper next question, if this target were allowed another recovery, would be whether a real, law-preserving packet randomization can orthogonalize enough of these minor channels to convert the exact `pi_Q` coefficient measure into an evaluation bound. Under Section I, however, the next run may continue this target only if it can actually move `beta_band`; otherwise it must hand off and rotate.

## 9. Comparison of the three genuinely different attacks

### B9 — randomize / reserve fresh packet

**Outcome: success at the structural level.** Reserving three consecutive scalar intervals of width `W` protects the center exactly, so arbitrary outside influence lives only on the outer `2W` coordinates. This matches the crucial deformation support of the full-block packet and removes the earlier center-deformation concern.

### B20 — find why the algorithm fails

**Outcome: one obstruction removed, one isolated.** The all-minor coefficient geometry survives the triangular interfaces, proved for all `W`. The full-block proof fails instead at its two-complete-square residual decomposition. The exact unpaid local statement is now the deformation-uniform small-ball estimate for the induced Ferrers residual.

### B28 — replace uniform by typical

**Outcome: promising exact reformulation, no theorem yet.** Cauchy-Binet produces the canonical weighted minor law `pi_Q`. It suggests averaging residual geometries according to the coefficient mass instead of using a worst RRQR pivot. The missing anti-cancellation step prevents converting this into a determinant evaluation bound in this run.

These are not the preceding B14/B24/B25 phase/symmetry/extremal-Schur attacks, and the old route was not silently resumed.

## 10. Source-level before/after and auxiliary delta

### Source metric

`beta_band <= 0.920695597782722... -> beta_band <= 0.920695597782722...`.

**No movement.** The source target `beta_band=0` remains open.

### Auxiliary progress proved this run

Before:

- no packet-level theorem showed that the scalar hard-band geometry could expose an arbitrary outside deformation only on two protected outer blocks while retaining full exterior coefficient visibility;
- it was unclear whether scalar triangular interfaces killed some outer minors.

After:

1. exact protected-packet geometry: center-to-complement coupling is zero for a three-width-`W` scalar packet;
2. exact all-`W` perfect-matching theorem for every equal-size outer deletion pair;
3. consequent `exp(+-C W log W)` scalar-packet coefficient comparison with `det(I+Q^*Q)^(1/2)`;
4. exact location of the remaining transplant failure: the full-block two-square **evaluation** step, not coefficient reconstruction;
5. canonical weighted-minor measure `pi_Q` isolated as a B28 average-case replacement for worst-pivot RRQR.

None of these is mislabeled as an exponent improvement or circular-law proof.

## 11. Prior-art / novelty qualification

Han's September paper already contains two neighboring mechanisms:

- Part I, scalar bounded-density case: a full exterior reset word and isolated coefficient monomial for `2W` fresh scalar rows;
- Part II, discrete full-block case: the all-minor coefficient identity and arbitrary outer-deformation packet estimate.

The theorem above combines the **scalar hard-interval packet geometry** with the **all-minor exterior-volume objective**. A bounded search of the current paper and the checked follow-ups did not locate this exact scalar Ferrers all-minor statement. That is not a worldwide novelty certificate; it may be implicit folklore or derivable from matching theory. The result is therefore recorded as a repository lemma supporting the open-source attack, not as a publication claim.

## 12. Remaining full-scope gap and Section-I disposition

To move `beta_band`, one still needs enough hard-edge control to complete Hermitization for an exponent strictly below `gamma_*`. The present packet theorem alone supplies no such control.

The most concrete missing local statement is the scalar Ferrers residual lemma in Section 7. A proof must survive arbitrary polynomial-norm deformations after the large RRQR directions are factored, and it must provide an `o(1)` failure bound / logarithmic-loss estimate strong enough for the global transfer calibration. Finite nonsingularity, raw perfect matchings, or coefficient `l^2` control are insufficient because evaluation cancellations remain.

This is the **second and final** Section-I recovery recorded for the current target. If the next invocation has no source-metric movement, HARD7-02 must write a terminal handoff preserving this packet theorem, the phase-twist results, and the corrected `gamma_*` baseline, then admit a fresh eligible external hard problem in the same lane under the ownership protocol.

## 13. Ledger delta for coordinator consumption

`HARD7-02 | Han periodic scalar Rademacher hard-indicator circular law | beta_band <= gamma_*=0.920695597782722... -> same | PARTIAL / SOURCE OPEN / STUCK2 recovery | new protected scalar-packet all-minor coefficient theorem; exact remaining local obstacle = deformation-uniform Ferrers-residual evaluation small ball`

No shared root ledger was edited by this worker.
