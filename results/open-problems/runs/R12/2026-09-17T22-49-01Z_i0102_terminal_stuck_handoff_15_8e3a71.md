Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime provides no authenticated model-family selector, reasoning-effort selector, or completed-run effort telemetry, so I do not claim GPT-6 / maximum. **NO MOVEMENT: I0102 `(a,C,p0)=(1/2,1,5) -> (1/2,1,5)`; SECTION-I THINKING RUN / TERMINAL I0102 HANDOFF. Methods used: #8 GO THE OTHER WAY AND DISCRETIZE, #9 RANDOMIZE, #10 DERANDOMIZE.**

# R12 / I0102 — terminal stuck analysis and handoff

Run timestamp: `2026-09-17T22-49-01Z`.
Repository/branch: `yspennstate/math-open-problems`, `master`.
Deployment: `NEW-METHODS-2026-09-16`.
Status: **PARTIAL / SOURCE OPEN / TERMINAL HANDOFF FOR THIS R12 ASSIGNMENT**.

## 1. Continuity and why this is a thinking-only run

I read the required campaign and fleet state before doing anything new: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the newest own I0102 report, the prior I0102 stuck/handoff reports, and the newest neighboring Paley reports located for R20/I0100, P04/I0101, and C28/I0103.

The immediate predecessor is `runs/R12/2026-09-17T21-33-30Z_i0102_bulk_mixing_14_71c5e8.md`, commit `230d299b3baad3840a2fa78ff287adcef0f91bd3`. That report records the third consecutive no-movement run in the owner-directed fresh I0102 reassignment and explicitly reserves the next invocation for a Section-I thinking-only report. The earlier historical I0102 assignment had already consumed both allowed stuck recoveries (`2026-09-16T17-30-35Z_stuck1_91c4e7.md` and `2026-09-16T19-30-29Z_stuck2_f61a83.md`) and then wrote the handoff `2026-09-16T20-33-03Z_i0102_handoff_i0060_claim_4b71c2.md`. The owner directive says unknown/stagnation history is preserved, not reset. Therefore this run makes **no new mathematical claim and no new checker**. A third recovery on the same source would violate the current hard-task protocol.

The live Randomstrasse source still states Conjecture 28 as a uniform power saving for degree-four SoS on prime Paley graphs, and a fresh bounded search on 17 September 2026 found no source-matching resolution. Kunisky--Yu's rigorous lower bound remains `Omega(p^(1/3))`; their paper also explicitly notes that the random-graph pseudocalibration route does not immediately transfer to Paley. Current-status references checked in this run include:

- Randomstrasse 101, Conjecture 28: https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/
- Kunisky--Yu, *A Degree 4 Sum-Of-Squares Lower Bound for the Clique Number of the Paley Graph*, CCC 2023 / arXiv:2211.02713.
- Schrijver, *New code upper bounds from the Terwilliger algebra and semidefinite programming*, IEEE TIT 2005.
- Gijswijt--Mittelmann--Schrijver, *Semidefinite code bounds based on quadruple distances*, IEEE TIT 2012.

This is a bounded dated status check, not a claim that no unpublished or unindexed result exists.

## 2. (a) Exact statement that blocks

The source-closing obligation is exactly

\[
\boxed{\exists\,\delta>0,\ C<\infty,\ p_0\ \text{such that}\ U_4(p)\le C p^{1/2-\delta}\quad\text{for every prime }p\equiv1\pmod 4,\ p\ge p_0.}
\]

The frozen certified value remains `a=1/2, C=1, p0=5`. A finite prime list, a constant-factor improvement, or an `o(sqrt(p))` statement without a fixed power is not movement in this metric.

## 3. (b) Routes tried and the precise failure of each

| Route already tried | What survived | Why it did not move the exponent |
|---|---|---|
| Vertex-only / degree-two dual | Exact Paley theta certificate | Restricted dual optimum is exactly `sqrt(p)`; edge-indexed rows are essential. |
| Edge-conditioning a degree-four pseudoexpectation | Exact K3 counterexample | Conditioning on an edge asks for degree-six positivity; the proposed transfer is invalid at degree four. |
| Valid one-vertex localization | Exact compiler to a neighbor-theta bound | The scalar localized theta quantity itself remains square-root scale; scalarization loses the compatibility information. |
| Global aggregate moments | Several exact moment identities | Summing by cardinality erases the union-incidence constraints that distinguish degree four from degree two. |
| Edge-compatibility theta / Hoffman style bounds | Valid graph-theoretic bounds | The natural spectral family is order `p`, much too weak. |
| Affine symmetrization | Correct quotient reduction | Internal orbit blocks still contain full-scale character operators. Symmetry reduces dimension but not norm. |
| Two-parameter character dual | Exact feasible family | Its optimum is linear in `p` (asymptotically `p/3`), so it is not the required certificate family. |
| K4 triality / permutation projection | Correct representation reduction | The dangerous quartic tensor already has a trivial-component contribution; triality alone does not cancel it. |
| One-channel Legendre/Mellin residual | Exact character factorization | The residual operator has `p` scale. Termwise operator-norm control loses the desired cancellation. |
| Exterior-square certificate | Exact second-compound identity | It saturates `T^4 <= p T^2`, reproducing only the square-root bound. |
| One-basepoint Terwilliger square root | `M=B^2` and exact orthogonality on the codimension-two subspace | The useful `sqrt(p)` factor is squared back to `p` unless another channel cancels it before norms are taken. |
| Two-basepoint triple-intersection profile | Identifies the quartic Mellin channel as a base-edge profile | The cell mean can be small while the full `L2` energy remains order `p^2`; averaging is not operator control. |
| Projective completion / points at infinity | Exact Paley conference completion | The completion satisfies an exact scaled-orthogonality identity; it removes a rank-two defect but supplies no decay. |
| Triangle-cell compression | Exact commutator and stable-rank bounds | A positive fraction of the multiplicity space mixes at full `sqrt(p)` scale; this is not a finite exceptional set. |
| Typical-mode split | Exact spectrum of the quartic Legendre operator | All but two modes have singular value exactly `p`; the hoped-for typical sub-`p` sector does not exist. |
| Deformation to a commuting endpoint | Quantitative distance-to-commutant bound | Every fixed nonzero interpolation remains noncommutative at a fixed fraction of full scale. |
| Scalar Schur/compressed gluing | Exact conference-block criterion | Scalarizing before gluing again reproduces the square-root scale. |

The common failure is now clear enough to be useful: every successful-looking reduction eventually takes a scalar average, an operator norm, or a Schur square **before** exploiting the exact `|U|=2,3,4` union-incidence coupling. That operation destroys the only sign information capable of cancelling the `+p` and `-p` quartic bulk sectors.

## 4. (c) What a proof must contain that no tried route contains

A successful proof must contain all of the following in one object, not as separate estimates:

1. A genuinely noncommutative block representation of the **full affine-symmetrized degree-four dual**, retaining vertex-edge, cubic-union, and quartic-union channels simultaneously.
2. A signed intertwiner that couples the `+p` and `-p` quartic multiplicity sectors to the cubic / vertex-edge channels **before** any absolute value, operator norm, or Schur-complement squaring is taken.
3. Control of a multiplicity space whose dimension grows with `p`; the triangle-cell stable-rank calculation rules out explaining the obstruction by finitely many exceptional modes.
4. An identity or inequality that is symbolic in `p` and all relevant cross-ratio parameters. A finite collection of prime SDPs cannot establish the required uniform exponent.
5. At the end, an explicit dual-feasible certificate (or an equivalent full proof of feasibility) whose objective has a fixed power saving. Anything that merely proves cancellation on average, on typical cross ratios, or for finitely many primes is still PARTIAL.

No route in the R12 history currently contains item 2 together with the exact union-incidence constraints.

## 5. (d) Simplest special case still unproved

The smallest re-entry point I would hand to a fresh worker is **one generic nonexceptional two-basepoint irreducible block of the actual affine-symmetrized degree-four dual**: retain its exact cubic--quartic union-incidence cross block and ask whether the signed `+p/-p` quartic sector can be reduced to `o(p)` *inside that block before norms are taken*. This is deliberately not a new theorem or a replacement source target. It is the smallest unresolved component that still contains the mechanism the full source proof would need.

A proof on only one numerical prime is not enough. The special case becomes genuinely useful only if its block formula is symbolic in `p` and in the orbit parameter so that it can be glued across the growing multiplicity space.

## 6. (e) Nearest solved problem in the literature and what it has that Paley currently lacks

The nearest successful template I found is Schrijver's 2005 code SDP. It strengthens Delsarte by keeping basepoint information in the noncommutative Terwilliger algebra of the Hamming cube and block-diagonalizing that algebra before making scalar estimates. Gijswijt--Mittelmann--Schrijver 2012 pushes the same philosophy to PSD constraints derived from quadruples and then exploits the full symmetry algebra to reduce the huge SDP. These are solved examples in which higher-order incidence information survives long enough to produce a stronger bound.

What those arguments have that the present Paley route lacks is an explicit block diagonalization in which **every higher-order incidence block is known and the inter-block PSD constraints close after symmetry reduction**. R12 has identified the Paley one- and two-basepoint character operators, but the decisive cubic--quartic intertwiner under the clique-union constraints is still missing. The recent two-basepoint Terwilliger work for prime-order circulants confirms that this is the natural algebraic category for dense Paley structure, but it concerns quantum symmetry rather than a degree-four clique-SOS power saving and supplies no missing cancellation theorem.

## 7. The three thinking moves in this run

### #8 — GO THE OTHER WAY AND DISCRETIZE

I tried to reduce the missing cancellation to the smallest finite symbolic template: one generic two-basepoint orbit, one cubic block, one quartic sign sector, and the exact union-incidence equations between them. This is a useful organizational reduction but **not a finite-computation solution**. The prior stable-rank result shows that the number of full-scale modes grows linearly with `p`, so a fixed finite SDP receipt cannot certify a uniform power saving. What would make discretization useful is a finite *symbolic* list of block types with coefficients depending algebraically on `p` and the cross-ratio orbit, not a finite list of primes.

### #9 — RANDOMIZE

I compared the signed `+p/-p` bulk picture with a random block model in which independent signs could plausibly cancel after coupling to cubic channels. That analogy does not furnish a proof. Paley has deterministic character correlations, and Kunisky--Yu already show at the lower-bound side that the random-graph pseudocalibration strategy does not immediately transfer. More importantly, the exact R12 spectra show that the raw Paley quartic channel is maximally structured, not a small random perturbation. Randomization therefore identifies what one would *like* the mixed block to do but gives no deterministic certificate.

### #10 — DERANDOMIZE

I then asked whether the exact Paley conference / character orthogonality identities could play the role of the random cancellation deterministically. The inherited projective-conference identity and one-basepoint square-root factorization show that this orthogonality is already fully present, yet every scalar or norm-level use of it saturates the square-root barrier. Therefore orthogonality by itself is not the missing ingredient. A derandomization would need a **new mixed identity coupling different SOS union degrees**, not another identity internal to the quartic character operator.

No new theorem is claimed in these three paragraphs; they are the required thinking-run diagnosis.

## 8. Required action: terminal handoff and rotation gate

Section I allows exactly one action. I choose **MOVE TO THE NEXT PROBLEM IN `QUEUE.md` AND RECORD THE SWITCH**.

Operationally, the move off I0102 is final for this R12 assignment: I0102 remains `PARTIAL / OPEN`, frozen at `(1/2,1,5)`, with the above re-entry point. I do **not** start a third recovery and do **not** create an SDP/checker receipt.

I then checked the live queue/ownership state rather than treating the historical candidate table as automatic permission to dispatch. The current `QUEUE.md` explicitly says rows are PENDING unless a stronger admission exists; PENDING is not READY. The previously admitted HARD candidates surfaced in the queue history are no longer free: for example I0028, I0078, and I0066 now have canonical claim files, while the next high-ranked rows include `HOLD_SOURCE` / claimed cases such as I0006 and I0011. A fresh repository-wide `READY / HARD / UNASSIGNED` check recovered the recent hard handoff conclusion that no genuinely unassigned READY HARD OUTSIDE successor had been certified, and no newer free claim-safe READY HARD row was found in this run.

Therefore the lawful rotation state is **`ROTATION_WAIT / NO SUCCESSOR CLAIMED`**. This is not permission to resume I0102 next hour. It means R12 has moved off I0102 and must first admit a source-current, ownership-clean HARD outside queue target in a future run before doing new research. I did not silently promote a PENDING row, did not steal another worker's claim, and did not open a target outside `QUEUE.md` merely because it looked attractive.

## 9. Model / scheduler configuration status

The configuration issue is unchanged. The exposed task surface used by this fleet has prompt/title/schedule/timing/enablement controls but no model-family or reasoning-effort selector and no authenticated completed-run model/effort receipt. GPT-6 / maximum can therefore be requested in prompt text but cannot be verified or enforced from this surface. Product/runtime support would have to expose those selector fields and completed-run telemetry to change that. The historical P26 `You cannot modify this task` response is an authorization-context issue; the legitimate workaround is the owning account/workspace context or platform support, never a duplicate task or permission bypass. No scheduler state was changed in this run.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R12
  source_target: I0102
  source_status: OPEN
  run_kind: SECTION_I_THINKING_ONLY_TERMINAL_HANDOFF
  model_actual: GPT-5.6 Sol
  reasoning_actual: UNVERIFIED
  model_requested: GPT-6
  reasoning_requested: maximum
  metric_name: smallest_uniform_exponent_a
  before:
    a: 1/2
    C: 1
    p0: 5
  after:
    a: 1/2
    C: 1
    p0: 5
  movement: false
  status: PARTIAL_OPEN_HANDOFF
  fresh_reassignment_consecutive_no_movement_runs: 3
  historical_stuck_recoveries_completed: 2
  historical_stagnation_reset: false
  section_B_methods: [8, 9, 10]
  chosen_section_I_action: MOVE_TO_NEXT_PROBLEM_IN_QUEUE
  successor_state: ROTATION_WAIT_NO_READY_HARD_SUCCESSOR_CLAIMED
  new_mathematical_claims: 0
  new_checkers: 0
  next_I0102_recovery_permitted: false
  handoff_reentry_point: generic two-basepoint irreducible cubic-quartic signed union-incidence block
```

No email, Drive, public posting, purchase, permission change, workflow execution, scheduler modification, shared-root edit, or peer-track edit was made.