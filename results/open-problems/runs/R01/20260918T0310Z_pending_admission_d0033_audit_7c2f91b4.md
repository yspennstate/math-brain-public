Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; the runtime exposes no authenticated model-family selector or reasoning-effort telemetry, so I do not claim otherwise. **R01 source metric remains frozen at I0024 `C=1`; active successor metric remains `UNMEASURED` because no current `READY + CLOSABLE OUTSIDE + UNASSIGNED` successor is lawfully dispatchable. Admission methods: B22 / B26 / B27. Independent neighbor audit: `R01-AUDIT-R7-01-D0033-BRADLEY-Q5-01 = PASS_MATHEMATICAL_SOURCE_SCOPE`; publication novelty remains UNVERIFIED.**

# R01 immutable run — successor gate plus independent D0033 audit

Repository / branch: `yspennstate/math-open-problems` / `master`.
Dated source/current-status checks: 2026-09-18 UTC.

## 1. Continuity: I0024 remains frozen, not restarted

I recovered the newest R01 handoff before doing any work. The native Aldous--Fill I0024 result remains frozen at the exact `C=1` right-inverse/flow characterization

\[
\tau_2=\inf_{R:\,BR=I_{H_0}}\sup_{0\ne b\in H_0}
\frac{(Rb)^T C^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+,
\]

with the previously recorded two independent PASS audits. The six-run rotation already occurred. I do not reopen I0024, I0113, G0012, D0057, D0030, or the retired FEI assignment.

The immediately preceding R01 report is

`runs/R01/20260918T0202Z_d0030_sixrun_handoff_linearcode_nogo_c4a8e271.md`.

It retires D0030 after six unchanged ordinary runs and leaves R01 at `PENDING_ADMISSION` with no successor metric inherited.

## 2. Repository / queue recovery

I reread the current campaign index/ranking, root POSTED/RESULTS, current QUEUE, the controlling follow-up implementation manifest, the newest R01 handoff, current claim files for the apparently free finite rows, the newest coordinator admission evidence, and targeted neighboring handoffs. The intake corpus is too large for a literal byte-for-byte model-visible reread through the connector; I used exact-ID/source retrieval for candidates and do not claim otherwise.

The newest coordinator pass is

`operations/task_health/runs/2026-09-18T025600Z/admission_screen.md`

(created by commit `c3df275874103b18032edcd2c5e579617d7bdab6`). It removes I0128/Sendov as KNOWN/RESOLVED and explicitly concludes that it certified **no new `READY + CLOSABLE OUTSIDE + UNASSIGNED` candidate**. It carries H0006 only as `PENDING / HARD`, not as a dispatchable substitute.

Fresh ownership checks also show that the superficially attractive finite rows are already consumed: I0121 (union-closed) has an R02 claim, I0122 (1/3--2/3) has an exclusive native claim, I0123 (Borsuk threshold) is a HARD claimed target, and I0125 (five-dimensional kissing number) is claimed. I0012 is also claimed by another native slot. I0061 has current native-slot research history despite a historically missing canonical-claim file and is therefore not free inventory. I do not manufacture a claim from stale queue text.

Therefore R01 remains **PENDING_ADMISSION** rather than stealing a target or silently promoting a PENDING row.

### Admission methods used

- **B22 — READ THE FAILURES:** I used the newest coordinator and rotation screens rather than re-running already-failed I0105/I0106/D0012 admission paths. Those failures identify the recurring blocker: broad source quantifiers or later partial resolutions make a convenient restricted subproblem non-closable.
- **B26 — HUNT THE SPORADIC CASE:** I checked the newest finite-looking I012x rows because these were the likeliest sporadic closable successors. The apparent free cases are now claimed or resolved; the newest coordinator pass independently reaches the same no-free-closable conclusion.
- **B27 — SWAP THE QUANTIFIERS:** I rejected the tempting substitution `there exists a convenient restricted model I can solve` for the required `answer the actual outside source quantifier`. This is why H0006, D0012 and broad removal/transient-walk programs are not lawfully promoted merely because one finite subfamily can be attacked.

No new target means no legitimate new source metric can be frozen this run.

## 3. Neighbor package is now complete enough for the requested OTHER-track audit

The newest neighboring R7-01 handoff

`research7_2026-09-17/R7-01/handoffs/2026-09-18T011800Z__D0033_sixrun_handoff.md`

retains D0033 / Bradley Question 5 as a **PROVED CANDIDATE**, supplies a self-contained proof package

`research7_2026-09-17/R7-01/paper_bradley_q5_phi_to_rhostar/`

and explicitly requests independent scrutiny of eight proof interfaces. It records `P26=0/1` and `OTHER=0/1`. This is therefore the first neighboring package in the current R01 neighborhood that satisfies the owner's gate for spending an independent audit.

Audit ID:

`R01-AUDIT-R7-01-D0033-BRADLEY-Q5-01`

Verdict:

**PASS_MATHEMATICAL_SOURCE_SCOPE**.

This is a full independent mathematical/source-scope audit, not a novelty or publication-priority certificate.

## 4. Audit of Bradley source normalization and closure theorem

Primary source rechecked directly on 2026-09-18:

Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, Probability Surveys 2 (2005), 107--144, DOI `10.1214/154957805100000104`, arXiv `math/0511078`.

The source facts used by the package are correct:

1. Bradley defines directional `phi(A,B)` by conditional probabilities and maximal correlation `rho(A,B)` in equations (1.2),(1.4).
2. His equation (1.13) gives
   \[
   \rho(A,B)\le 2\sqrt{\phi(A,B)\phi(B,A)}\le 2\sqrt{\phi(A,B)}.
   \]
3. Section 3.1 explicitly treats a **not necessarily stationary** Markov chain.
4. Theorem 3.3(6) says that if `rho*(n0)<1` at one lag, then `rho*(n)` decays at least exponentially.
5. Question 5 immediately asks whether phi-mixing of a Markov chain implies rho-star-mixing.

So the package's use of one strict rho-star lag is source-valid, and its broader nonstationary scope is consistent with the literal source. The canonical repository claim is narrower (strictly stationary) and should eventually be reconciled by an authorized coordinator, but that metadata mismatch does not invalidate the theorem.

## 5. Audit of the transition-row lemma

Fix `s<t` and let `K_{s,t}(x,.)` be a regular transition kernel. For a fixed future event `B`, the function

\[
h_B(x)=K_{s,t}(x,B)-\mu_t(B)
\]

has every positive-measure set average bounded in absolute value by `phi(t-s)`, because `{X_s in D}` is a past event and `{X_t in B}` is a future event. Therefore `|h_B|<=phi(t-s)` almost everywhere.

On a standard Borel space a countable generating algebra permits one common full-measure set. For fixed `x` in that set, the class of future events satisfying the bound is closed under monotone limits, so the monotone-class extension is valid. Consequently

\[
\|K_{s,t}(x,.)-\mu_t\|_{TV}\le\phi(t-s),
\qquad
\operatorname{diam}_{TV}\{K_{s,t}(x,.):x\in A_{s,t}\}\le2\phi(t-s).
\]

I find no null-set or total-variation normalization gap here.

## 6. Audit of arbitrary-input / prefix conditioning

For any input law `lambda` supported on the good row set, the unconditional output law and the output law conditioned on an arbitrary nonnull input event are two convex mixtures of the same row family. Hence their event probabilities differ by at most the row diameter, giving

\[
\phi(U,V)\le2\phi(t-s).
\]

Bradley's (1.13), using only the trivial reverse bound `phi(V,U)<=1`, yields

\[
\rho(U,V)\le2\sqrt{2\phi(t-s)}.
\]

This survives arbitrary conditioning on an earlier-history sigma-field because (i) the transition kernel from `X_s` to `X_t` is unchanged by conditioning on variables strictly before `s`, and (ii) a full-`mu_s` row set remains conditionally full almost surely. This is precisely the robustness the proof needs; it does not assume reversed phi-mixing.

## 7. Audit of the alternating-block / Markov-separator step

Take finite separated interlaced sets `S,T` and merge their selected times into maximal monochromatic blocks. For Peyre's pair `(U_i,V_j)` condition on the minimal prefix

\[
\mathcal H_{ij}=\sigma(U_{i'}:i'<i,\;V_{j'}:j'<j).
\]

Two cases:

- If the opposite-color blocks are adjacent, every variable in `H_ij` is strictly earlier than the earlier target block. Conditional on that prefix, the chain still has the same channel `K_{s,t}` from the last state of the earlier block to the first state of the later block. Markov data processing bounds the subjective correlation by `kappa(n)`.
- If the blocks are nonadjacent, the last prefix block of the later target's color lying strictly between the two targets belongs to `H_ij`. Any state in that block is a genuine Markov separator. All other variables in `H_ij` lie on its past/separator side. Hence the two target blocks are conditionally independent given `H_ij`, so the corresponding subjective correlation is exactly zero.

I explicitly tested the index ordering in both possible initial colors; the prefix claim remains true. This is the most delicate combinatorial interface in the proof and I find it correct.

## 8. Audit of Peyre tensorization and path norm

External dependency rechecked:

Rémi Peyre, *Tensorizing maximal correlations*, arXiv:1004.1602v2 (2010), Theorem 3.3.1 and Section 3.4(a), “Minimal Hypotheses.” Section 3.4(a) states that for the N-against-M theorem it suffices to control each pair relative to exactly the sigma-field generated by earlier X-variables and earlier Y-variables. That matches `H_ij` above.

The resulting subjective-correlation matrix is the bipartite adjacency matrix of an alternating path with edge weights at most `kappa(n)`. Its largest singular value is at most

\[
2\kappa(n)\cos\frac{\pi}{m+1}<2\kappa(n).
\]

Thus for finite interlacings

\[
\rho(S,T)\le2\kappa(n)
\le4\sqrt{2\phi(n)}.
\]

The finite-to-countable extension is standard: centered `L^2` functions measurable with respect to countably generated coordinate sigma-fields are approximated in `L^2` by conditional expectations onto increasing finite coordinate sets, preserving the covariance/variance limit. No hidden finiteness restriction remains.

Therefore if `phi(n0)<1/32`, then `rho*(n0)<1`, and Bradley Theorem 3.3(6) finishes the implication.

## 9. Stress / falsification checks

I tried to break the proof at the interfaces named in the R7-01 handoff:

- **reverse-phi leak:** not present; the argument only uses the universal `phi(B,A)<=1` factor in Bradley's inequality;
- **prefix changes channel:** not present for adjacent blocks because every conditioned variable is strictly before the channel input time;
- **nonadjacent prefix straddles separator:** not present when the last intervening prefix block is chosen; no conditioned current-color block lies after that separator;
- **path operator factor:** checked on `m=3,4` where the biadjacency singular norms are `sqrt(2)` and the golden ratio respectively, agreeing with `2 cos(pi/(m+1))`;
- **nonstationary scope:** Bradley Theorem 3.3 is explicitly nonstationary, so stationarity is not being smuggled into the final step.

No counterexample to the proof architecture was found.

## 10. Prior-art audit boundary

Dated bounded web queries included:

- `"phi-mixing" "rho-star" Markov chain Bradley Question 5`;
- `"phi-mixing" "interlaced rho-mixing" Markov chain`;
- `Bradley Question 5 Markov chain rho-star`;
- `interlaced maximal correlation Markov chain phi mixing`;
- post-2010 Peyre/tensorization/Bradley follow-up searches.

These recovered Bradley's 2001 rho-but-not-rho-star Markov example, Bradley's 1997 lower-psi positive theorem, Longla's later lower-psi/copula sufficient conditions, recent copula special-class papers, and Peyre 2010. I did **not** locate a paper explicitly stating the full phi-to-rho-star implication for arbitrary Bradley-scope Markov chains.

This remains bounded negative evidence only. I therefore do **not** certify novelty, priority, or publication readiness. The audit verdict is mathematical/source-scope PASS only.

## 11. Audit result and what remains

`R01-AUDIT-R7-01-D0033-BRADLEY-Q5-01 = PASS_MATHEMATICAL_SOURCE_SCOPE`.

This may count as the required distinct OTHER-track audit for D0033. It does **not** count as P26. Protocol closure still requires the independent P26 full-proof audit and final prior-art adjudication. R7-01 itself remains retired from ordinary attacking work on D0033.

No exact-arithmetic checker is added because this audit asserts no new finite computational claim; the relevant theorem is analytic and the proof is written on the page.

## 12. Scheduler/model control

The exposed scheduled-task interface still has no model selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guarantee of an hour-long execution. GPT-6/maximum therefore remains prompt text only here.

The historical P26 `You cannot modify this task` response is authorization/context-specific. Repository evidence records a later successful P26 modification from an authorized context. The valid workaround is the owning/authorized account/context or a product/backend surface exposing the required controls; duplicating the task or bypassing permissions is not authorized.

No scheduler mutation is attempted.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  track: R01
  native_source: "Aldous-Fill Open Problem 3.44 / intake I0024"
  native_metric:
    name: "smallest rigorously proved uniform multiplicative distortion C"
    before: 1
    after: 1
    status: "FROZEN_AFTER_C1_AND_ROTATION"
  active_successor:
    id: null
    metric: UNMEASURED
    before: UNMEASURED
    after: UNMEASURED
    status: PENDING_ADMISSION
  admission_methods: [22, 26, 27]
  admission_outcome: "no current READY + CLOSABLE OUTSIDE + UNASSIGNED successor certified"
  remaining_obligation: "continue cumulative admission cursor on a future invocation; claim only a source-current ownership-clear CLOSABLE outside target create-only"
  neighboring_audit:
    target: D0033
    owner: R7-01
    audit_id: R01-AUDIT-R7-01-D0033-BRADLEY-Q5-01
    verdict: PASS_MATHEMATICAL_SOURCE_SCOPE
    novelty: UNVERIFIED
    counts_as: DISTINCT_OTHER_TRACK_AUDIT
    p26_still_required: true
  evidence:
    - "runs/R01/20260918T0202Z_d0030_sixrun_handoff_linearcode_nogo_c4a8e271.md"
    - "operations/task_health/runs/2026-09-18T025600Z/admission_screen.md"
    - "research7_2026-09-17/R7-01/handoffs/2026-09-18T011800Z__D0033_sixrun_handoff.md"
    - "research7_2026-09-17/R7-01/artifacts/2026-09-18/2026-09-18T011200Z__D0033_final_scope_and_boundary.md"
    - "research7_2026-09-17/R7-01/paper_bradley_q5_phi_to_rhostar/README.md"
  audit_ids:
    - R01-AUDIT-R7-01-D0033-BRADLEY-Q5-01
```

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, peer-file edit, shared-root edit, force push, or scheduler change was performed.