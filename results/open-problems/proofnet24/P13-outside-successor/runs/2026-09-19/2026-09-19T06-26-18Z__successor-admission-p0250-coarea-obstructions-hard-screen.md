Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. ADMISSION HOLD / SUCCESSOR METRIC `UNMEASURED -> UNMEASURED`; no source-level movement; methods actually tried: B2, B11, B16.**

# P13 CLOSABLE OUTSIDE — P0250 directed-cut dualization and exact obstruction screen

UTC report time: 2026-09-19T06:26:18Z  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Own root: `proofnet24/P13-outside-successor/`  
Native slot: `6aa7b253b37c8191b693d8dc79298d37`  
Run status: `SUCCESSOR_ADMISSION_HOLD`

## 1. Continuity, lifecycle, and mandatory first screen

I continued the actual P13 successor-admission state rather than the retired scheduler title. The former I0051 / Aldous--Janson Open Problem 9 clade-covariance route remains **RETIRED**. The later C0021 recursive-majority successor reached its mandatory six-unchanged-run handoff in

`proofnet24/P13-outside-successor/runs/2026-09-19/2026-09-19T00-15-35Z__c0021-k3-width4-sixrun-rotation.md`

and was not reopened. The newest P13 report before this invocation remained a successor-admission hold with metric `UNMEASURED`.

The owner-mandated first successor lead I0054 was checked first. R11 has a newer immutable report

`runs/R11/2026-09-19T05-40-00Z_i0054-crt-rotor-u040-c061-e84b.md`

and moved its own frozen class metric `60 -> 61`. Its canonical I0054 ownership remains R11. P13 therefore did not touch I0054, create a competing claim, or repeat its mathematics.

Current fleet evidence also still has free exact-source READY CLOSABLE inventory at zero: the newest R02 census records `E_ready: 0 -> 0`; the genuinely new Kim--Mattman--Oh and Romero CLOSABLE admissions are already owner-bound. No queue/source/claim release discovered in this invocation transfers either to P13.

I reread/recovered the controlling owner directive at anchor
`749da260517828ed311f6f1b1af74915c054bdf3`,
`operations/NEW_METHODS_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, the newest P13 report and terminal C0021 handoff, the newest relevant R11/R02/NM13 neighbor evidence, and the P0250 source and attempt ledger entries. Missing history is not converted to zero.

## 2. Highest useful unclaimed screen this run: P0250

With no lawful free READY CLOSABLE successor, I screened the next mathematically useful unclaimed legacy intake target rather than fabricating a claim:

**P0250 — Kalai absorption bound from a directed cut parameter.**

The campaign source row is source-exact:

- source: Aldous--Fill, *Reversible Markov Chains and Random Walks on Graphs*;
- locator: Open Problem 9.27, PDF page 332 / parsed PDF page index 331;
- canonical key: `kalai_absorption_bound_from_a_directed_cut_parameter`;
- historical status: source says open;
- campaign result status: `attempted_unsolved`;
- no canonical `operations/claims/P0250.md` exists at the time of this run.

The exact source model is a Markov chain on `1,...,n` with state 1 absorbing and, for every `i>=2`, transitions only to smaller states. For a proper set `A` with `1 notin A`, write

\[
Q(A,A^c)=\sum_{i\in A}\sum_{j\in A^c}p(i,j),
\qquad
c(A)=\frac{|A||A^c|}{nQ(A,A^c)},
\qquad
\kappa=\max_A c(A).
\]

The source asks whether
\[
\max_i E_iT_1
\]
is bounded by a polynomial function of `kappa log n`.

The recovered prior campaign attempt checked two calibration chains: uniform descent has harmonic expected absorption, while the deterministic predecessor chain has linear absorption and correspondingly large `kappa`. Its recorded obstruction was that the cut condition controls average outward transition mass over a set, whereas a long random descent can concentrate on atypical vertices inside that set. The prior attempt explicitly suggested a level-set or occupation-flow bridge.

Fresh bounded public searches dated 2026-09-19 used the exact phrases `Open Problem 9.27`, `Kalai absorption`, `directed cut parameter`, and the Aldous--Fill source title. They recovered the source but no checked later primary paper announcing a resolution of this exact problem. This is bounded negative evidence only, not a global openness or novelty certificate. The required screenshot attempt on the relevant author-hosted PDF page failed with a cache miss; the parsed PDF text was available and matched the source statement, so the visual-access failure is recorded rather than silently treated as verification.

Current neighboring fleet screening classifies P0250 as a **global asymptotic polynomial-bound problem / HARD**, not an honest CLOSABLE endpoint. This run therefore performs substantive admission-screen mathematics but does **not** reclassify or admit it to P13.

## 3. B11 — DUALIZE: the cut system is exactly an oriented coarea inequality

The idea was to turn every cut inequality simultaneously into a functional inequality, so that the source hitting-time vector itself can be inserted without guessing a privileged family of cuts.

### Theorem 1 (exact oriented coarea dual of `kappa`)

Let `f:{1,...,n}->[0,infinity)` satisfy `f(1)=0`. Then

\[
\boxed{
\sum_{i=2}^n\sum_{j<i}p(i,j)\,(f(i)-f(j))_+
\ge
\frac1{n\kappa}
\sum_{i=1}^n\sum_{j=1}^n (f(i)-f(j))_+ .
}
\tag{3.1}
\]

Moreover the family of inequalities (3.1), over all such nonnegative `f`, is equivalent to the defining cut inequalities for `kappa`.

### Proof

For `t>=0` set
\[
A_t=\{i:f(i)>t\}.
\]
Because `f(1)=0`, every nonempty `A_t` excludes state 1, so by the definition of `kappa`,
\[
Q(A_t,A_t^c)\ge \frac{|A_t||A_t^c|}{n\kappa}.
\tag{3.2}
\]

Integrate (3.2) over `t>=0`. For a fixed directed edge `(i,j)`, the indicator that `i in A_t` and `j notin A_t` is one exactly for a set of `t` of length `(f(i)-f(j))_+`. Therefore
\[
\int_0^\infty Q(A_t,A_t^c)\,dt
=
\sum_{i=2}^n\sum_{j<i}p(i,j)(f(i)-f(j))_+.
\]
Similarly, for an ordered pair `(i,j)`, the indicator that `i in A_t` and `j notin A_t` has integral `(f(i)-f(j))_+`, so
\[
\int_0^\infty |A_t||A_t^c|\,dt
=
\sum_{i,j}(f(i)-f(j))_+.
\]
Integrating (3.2) gives (3.1).

Conversely, for any proper `A` excluding 1, insert `f=1_A` into (3.1). The left side is exactly `Q(A,A^c)` and the right side is `|A||A^c|/(n kappa)`. Thus the functional system contains every original cut inequality. QED.

This is not a source solution, but it is a clean exact reformulation of the entire cut parameter rather than a heuristic analogy with reversible Cheeger inequalities.

## 4. Apply the dual inequality to the source hitting-time vector

Let
\[
h_i=E_iT_1,\qquad h_1=0.
\]
Because the chain is strictly downward,
\[
h_i=1+\sum_{j<i}p(i,j)h_j\qquad(i\ge2).
\tag{4.1}
\]

Define the positive and negative oriented variations
\[
J(h)=\sum_{i>j}p(i,j)(h_i-h_j)_+,
\qquad
U(h)=\sum_{i>j}p(i,j)(h_j-h_i)_+.
\]

Subtracting the two parts of the signed edge difference in each row of (4.1) gives
\[
\sum_{j<i}p(i,j)(h_i-h_j)=1.
\]
Summing over `i=2,...,n` therefore yields the exact identity
\[
\boxed{J(h)-U(h)=n-1,}
\qquad\text{equivalently}\qquad
\boxed{J(h)=n-1+U(h).}
\tag{4.2}
\]

Combining Theorem 1 with (4.2) gives
\[
\boxed{
\sum_{i,j}(h_i-h_j)_+
\le
n\kappa\,[\,n-1+U(h)\,].
}
\tag{4.3}
\]

The point of (4.3) is diagnostic. A reversible-style argument that silently assumes every downward transition also decreases the remaining hitting time would set `U(h)=0`. The source model does not permit that assumption. B2 below gives the smallest possible exact obstruction even when the largest hitting time is still at the top state. Also, even controlling `U(h)` would not by itself finish Open Problem 9.27: one must still turn the global pair-dispersion bound into a bound polynomial in `kappa log n` rather than one retaining powers of `n`. Thus the missing source ingredient is a genuine concentration/occupation-flow theorem, not merely a prettier cut identity.

## 5. B2 — ATTACK THE NEGATION: hitting time need not respect the downward order

A natural attempted shortcut is:

> since every transition goes from a larger label to a smaller label, perhaps `h_i` is nondecreasing in `i`.

That is false.

### Theorem 2 (minimal top-max monotonicity obstruction)

There is a five-state strictly downward chain whose largest hitting time is at state 5 but whose hitting-time sequence has an interior downward-order inversion. Five states are minimal for such an example with the top state required to be a global maximizer.

Take

\[
2\to1,\qquad
3\to2,\qquad
4\to
\begin{cases}
1,&3/4,\\
3,&1/4,
\end{cases}
\qquad
5\to4.
\tag{5.1}
\]

Then the exact recursion gives
\[
(h_1,h_2,h_3,h_4,h_5)
=
\left(0,1,2,\frac32,\frac52\right).
\tag{5.2}
\]
Hence `h_4<h_3`, while `h_5=max_i h_i`.

For this chain the exact cut maximum is
\[
\kappa=\frac65.
\]
The oriented quantities in (4.2) are
\[
J(h)=\frac{33}{8},\qquad
U(h)=\frac18,\qquad
J(h)-U(h)=4=n-1,
\]
and
\[
\sum_{i,j}(h_i-h_j)_+=12.
\]
Thus the upward-in-`h` edge `4->3` has positive mass and the coarea route cannot erase `U(h)` by topological ordering.

### Minimality proof

For at most four states, `h_2=1` and
\[
h_3=1+p(3,2)h_2=1+p(3,2)\ge1=h_2.
\]
If the top state 4 is also a global maximizer, then `h_4>=h_3`. Hence no interior inversion is possible under that top-max requirement for `n<=4`. The five-state construction (5.1) attains one, so five is minimal. QED.

The exact checker independently verifies the chain, every cut, `kappa=6/5`, the coarea integrals, and the signed balance.

## 6. B16 — COMPUTE SMALL CASES: the extremal `kappa` cut need not be contiguous

A second tempting simplification is to use only intervals, prefixes, or suffixes in the topological label order. That too fails in the first small dimension where a useful witness appears.

Consider the five-state chain
\[
2\to1,
\]
\[
3\to
\begin{cases}
1,&1/4,\\
2,&3/4,
\end{cases}
\]
\[
4\to
\begin{cases}
2,&1/4,\\
3,&3/4,
\end{cases}
\qquad
5\to3.
\tag{6.1}
\]

Its exact hitting times are
\[
(h_1,h_2,h_3,h_4,h_5)
=
\left(0,1,\frac74,\frac{41}{16},\frac{11}{4}\right).
\tag{6.2}
\]

Exhaustive exact enumeration of all 15 nonempty subsets of `{2,3,4,5}` finds
\[
\boxed{\kappa=\frac65}
\]
with the **unique** maximizing set
\[
\boxed{A=\{3,5\},}
\]
which is noncontiguous in the source order. Its outward mass is exactly `Q(A,A^c)=1`.

By contrast the best value over all contiguous label intervals is only
\[
\boxed{\kappa_{\rm interval}=\frac{24}{25},}
\]
so
\[
\boxed{\frac{\kappa}{\kappa_{\rm interval}}=\frac54.}
\tag{6.3}
\]

For transparency, the exact `c(A)` values by subset are:

- singletons `{2},{3},{4},{5}`: `4/5`;
- pairs `{2,3}:24/25`, `{2,4}:24/35`, `{2,5}:3/5`, `{3,4}:24/25`, `{3,5}:6/5`, `{4,5}:3/5`;
- triples `{2,3,4}:24/25`, `{2,3,5}:24/25`, `{2,4,5}:24/55`, `{3,4,5}:24/25`;
- `{2,3,4,5}:16/25`.

Therefore any proof that replaces the source's maximum over arbitrary subsets by only contiguous order cuts is not source-faithful. Together with Theorem 2, this rules out the two simplest one-dimensional reductions: neither the hitting-time potential nor the extremal cut geometry is forced to align with the topological labels.

## 7. Exact self-check and artifact receipts

Before committing any finite claim I wrote and executed the exact-arithmetic checker

`proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T06-21-36Z__p0250-coarea-obstruction-selfcheck.py`.

It uses only `fractions.Fraction`, regenerates both chains, solves hitting times by exact backward recursion, exhaustively enumerates every P0250 cut in each five-state witness, recomputes the coarea identities, and checks the signed Bellman balance. The executed output contains 96 exact assertions and ends

`ALL_EXACT_P0250_COAREA_OBSTRUCTION_CHECKS_PASS`.

Checker create commit:
`2b12924a8139abbe533ef8f204a3b874a68a5ae7`.

Checker read-back blob:
`01b33866fb33b907f0ce93512ecd7c614736cfa9`.

Output create commit:
`9bef8b4d6727dd11122e8156aae4aadcfd6cee88`.

Output read-back blob:
`417978d9aac51138ea979e29d68f4449f3d5b446`.

This is explicitly a **P13 self-check**, not an independent audit.

## 8. Admission disposition

The mathematics above is real movement in understanding P0250, but it does not change the successor-admission gate.

- P0250 remains a global all-`n` polynomial-bound question.
- The exact coarea dualization exposes the correct full cut geometry, but does not yield a polynomial in `kappa log n`.
- The smallest exact witnesses show that both label-monotone hitting-time reductions and interval-only cut reductions fail.
- A source proof still needs an occupation/concentration mechanism controlling atypical path mass across the full arbitrary-cut system.
- Current neighboring fleet classification is therefore confirmed: **P0250 is HARD OUTSIDE, not an honest CLOSABLE successor for P13.**

Accordingly I did **not** create `operations/claims/P0250.md`, did not initialize a fake metric, and did not start an unchanged-run counter. The P13 successor metric remains

`UNMEASURED -> UNMEASURED`.

No source is claimed globally open from the bounded literature search.

## 9. Structured ledger delta for P26

```yaml
ledger_delta:
  worker: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  category: CLOSABLE_OUTSIDE
  run_status: SUCCESSOR_ADMISSION_HOLD
  active_successor_source_id: null
  active_claim_id: null
  active_claim_path: null
  screened_source_id: P0250
  screened_canonical_dedup_key: kalai_absorption_bound_from_a_directed_cut_parameter
  screened_disposition: HARD_OUTSIDE_NOT_ADMITTED
  source_metric_name: null
  metric_before: UNMEASURED
  metric_after: UNMEASURED
  source_movement: false
  methods_attempted: [2, 11, 16]
  new_math:
    - exact_oriented_coarea_dual_equivalent_to_full_kappa_cut_system
    - minimal_five_state_top_max_hitting_time_order_inversion
    - five_state_unique_noncontiguous_kappa_maximizer_with_5_over_4_interval_gap
  exact_checker: proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T06-21-36Z__p0250-coarea-obstruction-selfcheck.py
  exact_checker_commit: 2b12924a8139abbe533ef8f204a3b874a68a5ae7
  exact_output: proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T06-21-36Z__p0250-coarea-obstruction-selfcheck.out
  exact_output_commit: 9bef8b4d6727dd11122e8156aae4aadcfd6cee88
  self_check_only: true
  independent_audit: false
  successor_unchanged_run_count: 0
  successor_stuck_recovery_count: 0
  i0054_peer_owned: true
  i0054_peer_metric_latest: 61
  retired_i0051_reopened: false
  terminal_c0021_reopened: false
  canonical_claim_created: false
```

No shared-root ledger, historical report, peer file, scheduler, email/Drive resource, public post, workflow, permission, credential, or branch history was modified.
