Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but this runtime exposes no authenticated model-family selector or reasoning-effort selector, so I do not claim GPT-6 maximum. **NO MOVEMENT in the fixed metric: `R_unique=+infinity -> +infinity`; Section-B moves tried: #2 ATTACK THE NEGATION FIRST, #6 DEFORM TO A POINT YOU CAN SOLVE, #21 ASK WHO ELSE HAS THIS SHAPE.**
Problem/source: Héctor Jardón-Sánchez, Sam Mellick, Antoine Poulin, Konrad Wróbel, *Exactness and the topology of the space of invariant random equivalence relations*, PLMS 132(5) (2026), e70158, arXiv:2502.11622v2, **Question 2**; intake **I0079**.

# R06 CLOSABLE OUTSIDE — run 6 on I0079: stuck/thinking pass; the obstruction is tie-correlation, not product geometry

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, fixed metric, and why I0056 is not restarted

The native task prompt still names I0056 / Lyons--Peres Question 6.20, but R06 already reached the six-unchanged-run rotation threshold there and preserved a handoff before claiming I0079. The canonical create-only claim `operations/claims/I0079.md` still assigns I0079 exclusively to R06. I therefore do **not** restart I0056, erase its `H_{5,5}` width-zero result, or relabel its full-source `PARTIAL / audit-gated` status.

Before research I reread/rechecked current `master` at the level available to the connector: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, `operations/claims/I0079.md`, the newest own report `runs/R06/20260917T0117Z_i0079_pointwise_tie_phase_05.md`, exact repository searches for I0079/R06/P26-audit records, and the newest neighboring R07 report. No newer claim owner, posted exclusion, P26 audit of I0079, or independent audit of `I0079-R06-T5` was found.

The fixed metric remains the one in the canonical claim:

`R_unique = largest radius on which all subsequential limits agree for the frozen global-iid-nucleus-label refinement on Gamma=F_2 x F_2`.

That frozen global-label scope is now **KNOWN** by the exact bridge to published edge-measured phase independence, so the metric is already

\[
R_{\rm unique}=+\infty.
\]

It cannot move upward. The preceding report recorded unchanged count 4, so this run records **unchanged count 5**. Under the owner rule this is therefore a **stuck/thinking run**: I make no new theorem-sized claim and do not manufacture another checker merely to produce activity.

The source itself remains open-ended Question 2:

> In what generality can one say that there is a unique ideal Bernoulli Voronoi tessellation on a group?

The current source also explicitly notes that ties may be resolved equivariantly in more than one way, e.g. each boundary point may pick one of its tied nuclei at random, and then fixes a refinement. Thus refinement dependence is genuinely source-relevant rather than an invented variant.

## 2. Current status carried into this thinking run

The preceding run separated two natural refinements on the same frozen group `F_2 x F_2 = T_4 x T_4`:

1. **One global iid label per nucleus, reused at every evaluation vertex.** This scope is now **KNOWN**: Bhupatiraju's regular-tree model and DGKRW use this kind of global label, and the R06 bridge identifies the equal-tree-product labelled vertex process with D'Achille--Khezeli's phase-independent edge-measured process after the fractional-delay change of variables.
2. **Pointwise-independent tie marks `U_{v,x}`.** The previous R06 theorem `I0079-R06-T5` proves phase nonuniqueness on `T_4 x T_4`, already on one adjacent pair `o~w`, by an exact cylinder formula and disjoint rational intervals. That theorem remains **PROVED / SELF-CHECKED / AUDIT-PENDING / NOVELTY_UNVERIFIED**. It does not refute the source's open-ended Question 2; it is a negative example showing that uniqueness can depend on the refinement convention.

The exact certificate from the prior run remains:

- `artifacts/R06/20260917T0117Z_i0079_pointwise_phase_exact.py`;
- `artifacts/R06/20260917T0117Z_i0079_pointwise_phase_exact.out.txt`, ending `EXACT_RATIONAL_INTERVALS_DISJOINT / PASS`;
- certified phase gap at least `0.000303023143355440` for the one-edge cylinder on `T_4 x T_4`.

No new checker is needed for the present thinking-only pass.

## 3. Formal stuck blocker

The exact mathematical question now blocking a useful source-level classification is the simplest refinement-comparison case:

\[
\boxed{
\text{For the pointwise-independent tie refinement on the regular tree }T_4,
\text{ is the low-intensity Bernoulli--Voronoi IRE unique?}
}
\tag{BLOCK-R06-I0079-TREE}
\]

Equivalently, does the phase of the tree's discrete delay process affect even the one-edge cylinder

\[
E=\{o\text{ and a fixed neighbor }w\text{ are assigned to the same nucleus}\}?
\]

This is the right blocker because the nearest published theorem says **yes, unique** for the regular-tree Bernoulli model with **one global iid label per nucleus**. If the pointwise rule is nonunique already on `T_4`, then the product geometry was never the source of T5; the decisive distinction is the correlation structure of tie-breaking itself.

## 4. Move #2 — attack the negation of the preceding product-first intuition

The end of the previous report suggested asking whether products might be the first place where the global-label and pointwise rules diverge. I attacked that intuition rather than assuming it.

Let `T_d` be the `d`-regular tree, `q=d-1`, and fix an oriented edge `o~w`. In the standard ideal tree boundary description, a random boundary direction points from `o` through `w` with probability

\[
r=\frac1d=\frac1{q+1},
\]

so its Busemann increment from `o` to `w` is `-1` with probability `r` and `+1` with probability `1-r`.

The ideal tree delay process has geometric level weights. Writing the total intensity at integer level `m` as

\[
\lambda_m=a q^m,
\]

the total intensity below level `m` is

\[
\sum_{j<m}\lambda_j=\frac{\lambda_m}{q-1}.
\]

Now repeat only the **local one-edge case split** from T5 under pointwise-independent tie marks. Let `A_m` count level-`m` nuclei whose boundary ray points through `w` and `B_m` the rest. Then formally

\[
A_m\sim{\rm Pois}(r\lambda_m),\qquad
B_m\sim{\rm Pois}((1-r)\lambda_m),
\]
independently across the two types and levels.

Define

\[
H_r(x)
:=e^{-x}\sum_{n\ge1}\frac{x^n}{n!}\frac{1-(1-r)^n}{n}.
\tag{4.1}
\]

The same first-occupied-level analysis gives the **candidate** one-edge formula

\[
\boxed{
F_{q,a}(E)
=\sum_{m\in\mathbb Z}
 e^{-\lambda_m/(q-1)}
 \left[
 H_r(\lambda_m)+e^{-\lambda_m}H_r(q\lambda_m)
 \right],
\qquad \lambda_m=aq^m,\ r=\frac1{q+1}.
}
\tag{4.2?}
\]

I deliberately mark this `(4.2?)`: this run does **not** promote it to a theorem because the Bernoulli-to-ideal handoff for the pointwise refinement on a single tree has not been independently reconstructed on the page yet.

The second term has a striking exact simplification for every `q`. If the first occupied level has no `A`-type nucleus, then avoiding a better `A`-competitor at the next level has exponential cost

\[
r\lambda_m+r q\lambda_m
=r(1+q)\lambda_m=\lambda_m.
\]

And the two candidate classes that tie afterward have total rate

\[
(1-r)\lambda_m+r q^2\lambda_m
=\frac{q}{q+1}\lambda_m+
  \frac{q^2}{q+1}\lambda_m
=q\lambda_m,
\]
with the old-level class occupying fraction

\[
\frac{1-r}{q}=\frac1{q+1}=r.
\]
Thus the same `H_r(q lambda)` reappears. This calculation is exact algebra; what remains unverified is the complete source-limit handoff needed to call (4.2) the actual Bernoulli cylinder limit.

**Outcome #2:** the product-first hypothesis is now doubtful. The one-edge mechanism does not use the second tree factor at all once the correct tree direction probability and geometric delay levels are inserted.

## 5. Move #6 — deform `T_4 x T_4` all the way down to `T_4`

For the specific degree `d=4`,

\[
q=3,\qquad r=\frac14.
\]

Those are exactly the numerical parameters in the already proved product theorem T5. In particular, the exploratory tree expression (4.2?) becomes literally the same series as the certified product expression:

\[
H_{1/4}(x)
=e^{-x}\sum_{n\ge1}\frac{x^n}{n!}
\frac{1-(3/4)^n}{n},
\]

and

\[
F_{3,a}(E)
=\sum_m e^{-\lambda_m/2}
\left[H_{1/4}(\lambda_m)+e^{-\lambda_m}H_{1/4}(3\lambda_m)\right].
\tag{5.1?}
\]

So **if** the single-tree pointwise Bernoulli limit feeds into the standard phase process with this marked cylinder continuously, then the existing exact T5 certificate would immediately separate the same two phase values

\[
a_1=27/100,\qquad a_2=47/100
\]
with the same certified gap.

This is a much sharper handoff than “try the tree”: no new numerical search appears necessary. The unresolved step is conceptual/probabilistic, not computational.

**Outcome #6:** strong reduction. Dropping an entire tree factor appears to leave the one-edge pointwise-tie calculation unchanged for `T_4`. Product geometry is therefore unlikely to be essential to the nonuniqueness mechanism.

## 6. Move #21 — nearest solved problem and exactly what it has that this one lacks

The nearest solved problem is Bhupatiraju's low-intensity Bernoulli--Voronoi limit on regular trees. The later ideal-Poisson--Voronoi paper summarizes the model precisely: each Bernoulli nucleus receives one independent uniform `[0,1]` label, and a vertex tied between nearest nuclei is assigned to the closest nucleus with the **smallest nucleus label**. The same label is reused at every vertex. The paper states that the restriction of the phase-indexed tree IPVT to vertices has the same law for every phase under that convention.

That is **not** the pointwise-independent refinement. With global labels, if two neighboring evaluation vertices see the same tied set, their decisions are perfectly correlated through the reused nucleus labels. With pointwise marks, the two decisions are conditionally independent given the tied candidate sets. T5's reciprocal factors such as `1/N` arise exactly from this refreshed local randomness.

So the missing ingredient in the nearest solved theorem is now identified cleanly:

\[
\boxed{
\text{Bhupatiraju controls the geometry with globally reused nucleus labels;
our blocker changes the correlation structure of ties.}
}
\]

That difference is not cosmetic. It is precisely the feature that the product-tree/global-label phase-unfolding converts into a continuous fractional delay. Pointwise tie marks cannot be encoded by one delay attached to each nucleus because the same nucleus carries different tie marks at different evaluation vertices.

**Outcome #21:** the nearest solved theorem explains, rather than removes, the obstruction. Its proof/model contains a global per-nucleus random order that the pointwise problem intentionally lacks.

## 7. Every route tried and why it does or does not close the blocker

1. **Global phase cancellation / fractional delays:** succeeds for one label per nucleus, but fails structurally for pointwise marks because there is no single fractional delay `m+U_x` attached to a nucleus.
2. **Product-tree one-edge exact cylinder (T5):** proves nonuniqueness on `T_4 x T_4`, but by itself does not certify the single-tree Bernoulli-to-boundary convergence under pointwise marking.
3. **Deformation to one tree (this run):** the local Poisson algebra survives and for `T_4` appears numerically identical to T5. This is the strongest new route, but it is still a reduction, not a promoted theorem.
4. **Direct appeal to Bhupatiraju uniqueness:** invalid for the pointwise refinement because Bhupatiraju uses one global random label per nucleus.
5. **Published edge-measured phase independence:** likewise encodes one continuous delay per nucleus and therefore matches the global-label rule, not refreshed pointwise randomness.

## 8. What a complete proof now has to contain

A complete solution of `BLOCK-R06-I0079-TREE` needs exactly the step that the product proof could borrow from later product-tree machinery but the single-tree pointwise variant cannot simply cite without checking:

1. start from Bernoulli nuclei on `T_4` at a phase-controlled intensity subsequence;
2. prove the joint convergence of the finitely many candidate counts and the required pointwise tie marks for the radius-one cylinder to the marked boundary-delay Poisson process;
3. verify almost-sure continuity of the winner map for the two evaluation vertices under this **pointwise** marking convention;
4. derive (5.1?) as the actual Bernoulli cylinder limit;
5. reuse the existing exact rational certificate to show two phase subsequences have disjoint limits.

No new large computation should be needed unless step 2 reveals a normalization mismatch. The proof should be written directly at finite cylinder level if possible, because Bhupatiraju's own tree argument is elementary and cylinder-based.

## 9. Simplest special case still unproved

The simplest still-unproved case is therefore not another product or another radius:

\[
\boxed{
T_4,\quad \text{pointwise-independent tie resolution},\quad
E=\{o\sim_{\rm Vor} w\}\text{ for one fixed edge }o\!\sim\!w.
}
\]

A proof of phase dependence for this one cylinder would already show that the source's random-refinement wording can change uniqueness even on the regular tree, despite the classical global-label uniqueness theorem.

## 10. Exactly one recovery selected

I select **prove the simplest unproved special case from Section 9** as the recovery, with one restriction imposed by the controlling closable-track rule: the next invocation reaches six unchanged runs if the frozen metric still cannot move. Therefore the next run should attempt the finite-cylinder Bernoulli-to-boundary handoff only if it can produce a genuine source-status-changing result; otherwise it must preserve this reduction in the handoff and rotate rather than spending a seventh unchanged run on I0079.

Next Section-B moves, if the special-case proof is attempted before rotation:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY** — prove only the one-edge `T_4` pointwise cylinder limit;
- **#16 COMPUTE EVERY SMALL CASE** — reuse/retarget the exact existing certificate only after the limit formula is proved;
- **#27 SWAP THE QUANTIFIERS** — formulate the result as existence of two explicit phase subsequences rather than trying to classify every phase.

## 11. Current literature / prior-art check and access limits

Fresh dated searches on 2026-09-17 rechecked the exact source question, Bhupatiraju's regular-tree result, and the current D'Achille--Khezeli phase-convergence work. The accepted source still states Question 2. The regular-tree literature explicitly describes the Bernoulli tie rule as **one iid uniform label per nucleus**, with a tied vertex choosing the nearest nucleus of smallest label. I found no current paper in the bounded search stating the pointwise-independent regular-tree variant or the product T5 theorem. Negative search evidence is not a novelty certificate.

I also inspected the current tree IPVT paper's section on regular trees. Its Proposition 6.1 gives a phase-indexed Poisson delay process with geometric level intensities, supporting the exploratory reduction above. The web PDF text was accessible, while a requested page screenshot timed out; this access failure is recorded rather than silently treated as a visual verification.

Novelty for `I0079-R06-T5` and for the proposed tree extension remains **UNVERIFIED**.

## 12. Independent audit of newest R07 package

Newest neighboring package read:

`runs/R07/20260917T0122Z_i0077_sparse_drifting_pulses_09.md`, theorem `I0077-R07-T10` and its explicit sparse drifting-pulse corollary.

**Audit ID:** `R06-AUDIT-R07-I0077-T10-20260917T0220Z`  
**Verdict:** `PASS_SCOPED / NOVELTY_UNVERIFIED`.

I checked the new theorem at its stated scope:

- Lamperti transforms Brownian survival into stationary Ornstein--Uhlenbeck survival.
- On each complete pulse, the moving permitted corridor is contained in a fixed interval `I_j`; the killed OU semigroup has `L^2(gamma)` norm `exp(-lambda_j tau_j)`. Intervening unconstrained/killed evolutions are contractions, so submultiplicativity yields `exp(-M(r,s))` for the cumulative spectral mass.
- The stationary Gaussian start plus Cauchy--Schwarz gives the displayed survival-probability bound.
- If the normalized spectral mass liminf exceeds one, choosing `kappa>1` makes `(n/R_n)^(-kappa)` summable because `R_n=O(log n)`.
- The terminal-time discretization uses a summable Brownian oscillation event and padding `eta sqrt(s)`; the choice `R_n ~ log n` is sufficient.
- The FBM transfer fixes one deterministic witness index after choosing the tail threshold and uses an inclusion of events, not an unjustified independence assumption.
- In the explicit family with pulses at logarithmic times `m^2`, the pulse-time density is zero. The harmonic-oscillator transform gives `lambda_m >= m^2/16`; pulse length `1/4` then makes cumulative spectral mass order `S^(3/2)`, so spectral mass divided by log horizon diverges.

I found no mathematical gap in T10 or the displayed explicit corollary at this scope. This is not a re-audit of all earlier R07 compilers and not a novelty audit of Burdzy--Scheutzow Problem 7.8.

## 13. Model/runtime control boundary

The implementation manifest still records the same actual interface limitation: task controls expose prompt/title, schedule, timing mode and enabled state, but **no model selector, no reasoning-effort selector, no authenticated runtime-model telemetry, and no guaranteed hour-long execution setting**. Therefore `GPT-6 / maximum` remains prompt text rather than an enforceable runtime configuration in this worker.

The prior `You cannot modify this task` result for one P26 task ID was a context/ownership permission boundary. The legitimate workaround is the owning authorized task-control context or platform support; duplicating the task or bypassing permissions is not acceptable. No scheduler mutation was attempted.

## 14. Structured ledger_delta

```yaml
ledger_delta:
  worker: R06
  source:
    intake: I0079
    authors: [Hector Jardon-Sanchez, Sam Mellick, Antoine Poulin, Konrad Wrobel]
    title: Exactness and the topology of the space of invariant random equivalence relations
    locator: Question 2
  continuity:
    predecessor_I0056: "preserved / rotated; not restarted"
    canonical_claim: operations/claims/I0079.md
  fixed_metric:
    name: R_unique
    before: +infinity
    after: +infinity
    movement: none
    unchanged_count: 5
    note: "metric belongs to frozen global-iid-nucleus-label F_2 x F_2 scope, now KNOWN"
  source_status: PARTIAL
  carried_results:
    global_label_F2xF2: "KNOWN / direct published corollary"
    pointwise_F2xF2_T5: "PROVED / SELF-CHECKED / AUDIT-PENDING / NOVELTY_UNVERIFIED"
  this_run:
    type: "STUCK / THINKING ONLY"
    new_theorem_claims: 0
    tried_moves: [2, 6, 21]
    blocker: "uniqueness versus phase dependence for pointwise-independent tie refinement on single regular tree T_4"
    strongest_reduction: "exploratory one-edge local algebra on T_4 matches the already certified T_4 x T_4 T5 series; Bernoulli-to-boundary pointwise-mark handoff remains to be proved"
    simplest_unproved_case: "T_4, one edge, pointwise-independent tie marks"
    selected_recovery: "prove the simplest unproved special case, subject to six-unchanged-run rotation rule"
    next_moves: [4, 16, 27]
  evidence:
    prior_report: runs/R06/20260917T0117Z_i0079_pointwise_tie_phase_05.md
    prior_exact_checker: artifacts/R06/20260917T0117Z_i0079_pointwise_phase_exact.py
    prior_exact_output: artifacts/R06/20260917T0117Z_i0079_pointwise_phase_exact.out.txt
    source_visual_access: "PDF text accessible; screenshot request timed out"
  audits:
    P26_I0079: NOT_FOUND
    independent_T5: NOT_FOUND
    R06_AUDIT_R07_I0077_T10_20260917T0220Z: "PASS_SCOPED / NOVELTY_UNVERIFIED"
  remaining_obligation: >-
    Prove or refute the single-tree pointwise-mark one-edge phase formula at the actual
    Bernoulli-cylinder level; obtain independent audits for any source-relevant new theorem.
    If the next run has no metric-changing/source-status-changing event, preserve this handoff
    and rotate at the six-unchanged closable threshold.
```

## 15. Bottom line

The frozen metric cannot improve: it remains `+infinity`, so this is correctly a thinking run rather than another certificate run. The useful progress is a sharper diagnosis. The phase-nonuniqueness mechanism from the product theorem appears to survive **unchanged on `T_4` at one edge**; what distinguishes the known unique tree theorem is not tree versus product geometry but **globally correlated nucleus labels versus pointwise-refreshed tie randomness**. I have left this as a reduction rather than a theorem until the single-tree Bernoulli-to-boundary handoff is written cleanly and independently checked.
