Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO SOURCE-METRIC MOVEMENT: frozen Aldous–Fill I0024 remains `C=1`; successor metric remains `UNMEASURED -> UNMEASURED`; status `PENDING_ADMISSION`; methods #8 DISCRETIZE, #14 FIND THE GROUP ACTING, #19 MAKE IT AN ALGORITHM.**

# R01 — post-P0219 ownership transition and next-source stress test

Repository: private `yspennstate/math-open-problems`, branch `master`.

## 1. Frozen I0024 remains frozen

I recovered the current R01 state before doing any successor work. The original R01 source is David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs*, Open Problem 3.44. The maintained source page was rechecked on 2026-09-19 at

`https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch3.S8.html`.

It still asks literally:

> Does there exist a characterization of the relaxation time as exactly an inf over flows?

and immediately distinguishes this from the Chapter-4 inequality giving only an upper bound.

The frozen R01 solution remains

\[
\tau_2=
\inf_{R:\,BR=I_{H_0}}
\sup_{0\ne b\in H_0}
\frac{(Rb)^T C^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+,
\]

so the fixed distortion metric remains

\[
\boxed{C=1.}
\]

I0024 is not reopened. Existing independent source-level mathematical audits are preserved, including `R20-AUDIT-R01-I0024-03` and `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10`; both preserve the prior-art/novelty caveat rather than converting a mathematical audit into a publication-priority certificate.

The old R01 FEI assignment remains retired; P03 owns FEI. The later KPS/Nielsen successor reached its six-supported-unchanged terminal handoff and is not restarted here.

---

## 2. Repository continuity: P0219 is no longer available to R01

Previous own immutable report:

`runs/R01/20260919T0343Z_p0219_basdevant_free_backstep_reduction_21_18_4_b7a3c912.md`

creation commit:

`9b49aac4c3377c76b498fd01a87c4d2b8ef1fb3d`.

Before research I recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current follow-up implementation record, the newest own report, current neighboring P0219 reports and the relevant intake/catalog records. Large append-only intake ledgers were handled through their indexed candidate records and exact changed-file deltas rather than falsely claiming a fresh visual byte-for-byte reread of every historical JSONL.

At a captured prewrite master `8e6ca3ae50a70e4128166ce9be806223372fa802`, exact compare against the preceding R01 report commit was complete: **55 commits ahead / 0 behind / `too_large=null`**.

The decisive changed file is now

`operations/claims/P0219.md`.

It records P0219 as

`CLAIMED / MANUALLY ADMITTED / CLOSABLE OUTSIDE`

with exclusive owner/native slot

`6aa7ebbe26308191a40003a950a2307a`.

The claim explicitly inherits the R01/R06/P13 P0219 work, including the one-sided sharp lower bound, the exact routing dual/witness, and the reduction to a free-backstep routing-tax problem. Its new owner freezes

\[
T(q)=\limsup_{n\to\infty}\frac{\mathbb E[U_n(C_q)-W_n(C_q)]}{n}
\]

and

\[
\alpha_{\rm tax}=\sup\{\alpha\ge0:T(q)=O(q^\alpha)\},
\]

with baseline `alpha_tax=0` and target stronger than square-root scale.

Therefore **R01 stops mathematical work on P0219 immediately**. Continuing it here would duplicate a current exclusive owner and violate the create-only ownership contract. The previous R01 work is preserved as predecessor evidence for the rightful owner; it is not deleted, relabeled, or claimed as current R01 ownership.

This is a lifecycle transition, not source-metric movement for R01. R01 remains `PENDING_ADMISSION`.

---

## 3. Admission guardrail: exact-looking does not mean available

I screened exact-looking Aldous/Markov candidates before selecting any new route.

A useful negative control is `P0243`, Aldous–Fill Open Problem 4.48. Its canonical claim path is absent, which superficially could look like an ownership gap. But the repository already contains a complete 2026-09-14 settlement packet:

`probability_1000_attempts_I_20260914/Probability_P0243_Aldous_Fill_open_problem_4_48_2026-09-14.md`.

That packet gives:

- a reversible three-state birth-and-death counterexample to part (a), `tau_1 <= tau_0`;
- a full optional-stopping/eigenfunction proof of part (b), `tau_2 <= tau_1^(2)`.

Current R7-02 admission work consequently classifies P0243 as `already settled/excluded`. A missing `operations/claims/P0243.md` is therefore **not** permission to reclaim it. This is exactly the distinction the owner contract requires between ownership absence and source availability.

Likewise P0245 is currently canonically claimed by NM13-09, while P0209 is recorded by current admission screens as settled/campaign-result. Neither is available.

---

## 4. Strongest unclaimed mathematical near-lead checked this run: P0216

I then stress-tested `P0216`, *Limit constant for common random two-dimensional partial orders*. Direct canonical claim lookup remains absent, so there is no current owner found at that path; this is only an ownership check, not an admission.

Outside source: David Aldous, *Largest common substructures in probabilistic combinatorics*, original 2003 document and maintained open-problem page:

`https://www.stat.berkeley.edu/~aldous/Research/OP/substructures.html`

and linked `common_subs.pdf`.

For two independent random coordinatewise partial orders on `[n]`, generated by iid uniform points in `[0,1]^2`, Aldous defines `C_n` as the largest label subset on which the two induced partial orders agree and conjectures

\[
\boxed{\mathbb E C_n\sim c n^{1/3},\qquad 0<c<\infty.}
\]

The source itself gives two distinct `n^{1/3}` lower constructions and says a first-moment `O(n^{1/3})` upper bound is not hard, while establishing the value **or existence** of the presumed limit constant may be genuinely hard.

The maintained 2026 source page still describes the two-dimensional partial-order problem as an old direction that was not pursued further; its later updates concern the cladogram/LCS branches, not a source-matching resolution of the partial-order constant. Bounded searches dated 2026-09-19 using the exact title, `random two-dimensional partial order`, `largest common substructure`, and `n^(1/3)` recovered the source and adjacent common-substructure literature but no checked primary paper proving the displayed limit. This is bounded negative evidence only, not worldwide novelty certification.

The key conclusion is classification: **P0216 is mathematically current-looking but HARD, not a lawful CLOSABLE R01 successor.** I did not create a claim.

The three fresh Section-B moves below were used as an admission stress test: could a new formulation make P0216 genuinely short/closable? The answer this run is no, but the reformulation is useful enough to preserve.

---

## 5. Method #8 — DISCRETIZE: exact conflict-graph formulation

Let the two random partial orders be `P` and `P'`. Define a graph `H_n` on label set `[n]` by putting an edge `{i,j}` exactly when the relation of `i,j` in `P` differs from their relation in `P'`. Each relation has three possibilities:

- `i < j`,
- `j < i`,
- incomparable.

Then, deterministically for every realization,

\[
\boxed{C_n=\alpha(H_n).}
\tag{5.1}
\]

### Proof

A subset `A` has identical induced partial orders in `P` and `P'` iff every unordered pair `{i,j}` inside `A` has the same relation in both structures. By definition this is equivalent to `A` containing no edge of `H_n`. Maximizing `|A|` gives (5.1). `QED`

This is more than a computational encoding: it identifies the exact object whose extremal asymptotics matter.

Now write the four coordinates attached to label `i` as

\[
Z_i=(X_i,Y_i,X'_i,Y'_i)\in[0,1]^4,
\]

with the `Z_i` iid uniform. There is a deterministic symmetric `{0,1}`-valued kernel

\[
W(z,z')={\bf1}\{\text{the coordinatewise-order relation in the first pair differs from that in the second}\}
\]

such that `H_n` is exactly the `W`-random graph obtained from iid latent points `Z_1,...,Z_n`.

Thus P0216 can be restated as an **independence-number problem for one explicit random-free graphon**:

\[
\boxed{\mathbb E\alpha(G(n,W))\sim c n^{1/3}.}
\tag{5.2}
\]

This formulation explains why ordinary dense `G(n,p)` intuition is useless: edge marginals are dense but the latent geometric dependence creates polynomial-size independent sets.

**Outcome #8:** useful exact category reduction, but it does not make the constant problem finite or short.

---

## 6. Method #14 — FIND THE GROUP ACTING: exchangeability gives the first moment, not the constant

The graphon formulation exposes the full label-permutation action. `H_n` is vertex-exchangeable because its latent `Z_i` are iid. More strongly, restriction to any fixed `k` labels has exactly the same law as `H_k`.

Therefore, if

\[
p_k:=\Pr(H_k\text{ has no edges}),
\]

then for the number `N_k` of agreeing `k`-subsets,

\[
\mathbb E N_k=\binom nk p_k,
\qquad
\Pr(C_n\ge k)\le \binom nk p_k.
\tag{6.1}
\]

This is the source's first-moment mechanism in symmetry language. The important point is what it **does not** give. To prove a limit constant one needs sharp control of the crossover window of `binom(n,k)p_k` together with dependence/second-moment or a structural construction tight enough at `k=Theta(n^{1/3})`. Exchangeability alone supplies no subadditivity in `n` and no reason that `E C_n/n^{1/3}` should converge.

**Outcome #14:** symmetry collapses the source to a sequence of finite induced-order coincidence probabilities `p_k`, but the missing constant is precisely the large-`k` asymptotic/dependence problem. This is evidence for HARD classification, not a route to a short CLOSABLE certificate.

---

## 7. Method #19 — MAKE IT AN ALGORITHM: exact finite optimization reveals the wrong bottleneck

Equation (5.1) gives an exact constructive algorithmic statement for every realization:

1. compute the three-way pair relation in each of the two partial orders;
2. build the conflict graph `H_n`;
3. output a maximum independent set of `H_n`.

This is an exact finite reduction, but it does **not** solve the probabilistic source problem. Generic maximum-independent-set complexity is irrelevant to the asymptotic constant, and the kernel `W` has rigid semi-algebraic geometry that must be exploited probabilistically.

The most promising research direction exposed by the algorithmic language would be to study the `n^{1/3}` independence scale directly from the explicit four-dimensional kernel—e.g. via a variational/large-deviation problem for sparse latent regions or a renormalized occupancy process—rather than by generic graph optimization.

However, that is a theorem programme, not a short endpoint. I therefore do not promote P0216 to CLOSABLE and do not create an exact checker merely to certify the tautological finite reduction.

**Outcome #19:** the algorithm identifies the finite object but confirms that the obstacle is asymptotic geometry/dependence, not finite optimization.

---

## 8. Admission verdict and next route

No source examined this run passes all of

`exact outside source + currently open at checked scope + not posted/settled + full-source CLOSABLE shape + ownership-clear + lifecycle-available`.

In particular:

- P0219 is now a good CLOSABLE target but is **owned by another slot**;
- P0243 is exact-shaped but **already settled/excluded**;
- P0245 is **owned**;
- P0209 is **settled/campaign-result**;
- P0216 is ownership-clear at the canonical path but **HARD**, with the source itself emphasizing the limit-constant obstruction.

Therefore R01 remains

`PENDING_ADMISSION / NO ACTIVE SUCCESSOR`.

No new canonical claim, checker, audit request, shared-root edit, peer-file edit, email, Drive item, public posting, purchase, permission change, workflow change, or scheduler change was made.

The strongest practical lesson from the P0219 transition is that the next R01 admission should preferentially be a mature PENDING source for which existing work has already reduced the **full source statement** to one bounded obstruction. Merely finding a famous open source or a pretty reformulation is not enough.

Suggested next fresh Section-B triple if no admission event occurs before the next invocation: **#11 DUALIZE, #13 FIND WHAT ONLY INCREASES, #15 BREAK THE SYMMETRY ON PURPOSE**, applied only to a newly verified ownership-clear CLOSABLE near-lead, not to P0219 and not by relabeling P0216.

---

## 9. Model / scheduler-control truth

The current repository implementation record still documents that the exposed scheduler surface has task identity/title, prompt, schedule/timing mode and enabled state, but **no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run model/effort receipt, and no guaranteed-duration control**. Thus `GPT-6 / maximum` remains a prompt request on this surface, not an enforceable or attestable runtime setting.

The historical P26 response `You cannot modify this task` remains an authorization/context boundary. The lawful workaround is the owning/otherwise-authorized product/workspace/API/admin context or platform support for that exact task. It is not legitimate to duplicate the task or bypass permissions. No scheduler mutation was attempted here.

---

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R01
  lane: CLOSABLE_OUTSIDE
  frozen_source:
    id: I0024
    source: Aldous-Fill Open Problem 3.44
    metric: smallest_uniform_flow_characterization_distortion_C
    before: 1
    after: 1
    lifecycle: FROZEN_DO_NOT_REOPEN
    formula: "tau2 = inf_{BR=I_H0} sup_{b!=0} (Rb)^T C^{-1}(Rb)/(b^T Pi^{-1}b)"
    audits:
      - R20-AUDIT-R01-I0024-03
      - P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10
    prior_art_novelty: UNVERIFIED
  active_successor: null
  successor_metric:
    before: UNMEASURED
    after: UNMEASURED
    moved: false
  status_before: PENDING_ADMISSION
  status_after: PENDING_ADMISSION
  unchanged_count: UNKNOWN_UNMEASURED_NO_ADMITTED_SOURCE
  continuity:
    predecessor_report: runs/R01/20260919T0343Z_p0219_basdevant_free_backstep_reduction_21_18_4_b7a3c912.md
    predecessor_commit: 9b49aac4c3377c76b498fd01a87c4d2b8ef1fb3d
    captured_prewrite_master: 8e6ca3ae50a70e4128166ce9be806223372fa802
    compare_ahead: 55
    compare_behind: 0
    compare_too_large: null
  material_lifecycle_delta:
    P0219:
      before: PENDING_NOT_READY_UNOWNED_IN_R01_REPORT
      after: CLAIMED_MANUALLY_ADMITTED_CLOSABLE_OUTSIDE
      owner_native: 6aa7ebbe26308191a40003a950a2307a
      r01_action: STOP_RESEARCH_AND_PRESERVE_HANDOFF_EVIDENCE
  candidate_stress_test:
    id: P0216
    canonical_claim_path_present: false
    source_shape: HARD_LIMIT_CONSTANT
    source_target: "E C_n ~ c n^(1/3), 0<c<infinity"
    exact_reformulation: "C_n = alpha(G(n,W)) for explicit 0/1 graphon W on [0,1]^4"
    admission: REJECT_HARD_NOT_CLOSABLE
    current_resolution_recovered_in_bounded_search: false
    negative_search_is_not_novelty_proof: true
  guardrails:
    P0243: SETTLED_EXCLUDED
    P0245: OWNED_NM13_09
    P0209: SETTLED_CAMPAIGN_RESULT
  methods_this_run: [8, 14, 19]
  methods_outcome:
    8: exact_conflict_graph_and_graphon_reformulation
    14: exchangeability_first_moment_reduction_but_no_limit_mechanism
    19: exact_MIS_algorithm_identifies_asymptotic_geometry_as_real_obstruction
  new_claims: 0
  new_finite_checkers: 0
  new_audits: 0
  remaining_obligation: >-
    Admit a genuinely ownership-clear full-source CLOSABLE OUTSIDE successor;
    do not reopen I0024/KPS/P0219 and do not relabel P0216 HARD work as CLOSABLE.
  next_methods_if_still_pending: [11, 13, 15]
```
