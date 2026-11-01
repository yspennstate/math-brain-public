Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**, and I do not claim otherwise. **AUDIT MOVEMENT: `T_CI241 1 -> 1`; independent full-proof audits `0/2 -> 1/2`; P26 PASS, second distinct audit still missing; no new P20 theorem/checker claim.**

# P20 CI241 audit-recovery — P26 PASS, second distinct audit pending

Run date: **2026-09-18**.

Track: **P20; CLOSABLE OUTSIDE**.

Active source: Fokam Souop Rigobert and Bitjoka Laurent, *Minimal Isometric Embeddings of Graphs into Abelian Groups: Theory, Algorithms, and Applications to Signal Processing over Networks*, arXiv:2606.29391v1, Chapter 2 §2.8.3, Conjecture 2.41 / Open Problem 1.

Canonical claim: `operations/claims/FOKAM-BITJOKA-2026-CYCLIC-INTERVAL.md` @ `d1b8c8755617cbaef9b06c2eab2694bea0382258`.

Owner proof ID under audit:

`P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01`.

Canonical owner proof report:

`proofnet24/P20-closure-log-unimodality/successors/FOKAM-BITJOKA-2026-CYCLIC-INTERVAL/runs/2026-09-18/2026-09-18T06-13-00Z__run-report.md`

creation commit `ed6e0a90cf05accdbf3b617137ac80762091778b`, verified blob `6bbf365cb4f5aded37f798d5c3b7b9c81b5fad8e`.

Previous P20 audit-gate report:

`proofnet24/P20-closure-log-unimodality/successors/FOKAM-BITJOKA-2026-CYCLIC-INTERVAL/runs/2026-09-18/2026-09-18T07-12-00Z__audit-recovery.md`

creation commit `15acb62162971b9ef0b0cffb9a01d6fb2fe8535c`, verified blob `46779d59dcba648e3cd1e9cad9d66ad8504b11af`.

That prior report correctly recorded audit count `0/2`. The present run is audit recovery only: no restart of the averaging proof, no new P20 theorem, and no redundant P20 checker.

## 1. Exact source statement and frozen metric

The exact source target remains:

> For every odd integer `m` and every nonempty proper subset `x subset Z_m`, there exists a cyclic interval `W subset Z_m` such that
>
> `|W triangle x| < min(|W|, m-|W|)`.

The detailed body / Open Problem 1 wording is canonical. The unconditional-sounding abstract shorthand is not substituted for the conjecture.

Frozen source metric:

`T_CI241 := number of exact truth values of Conjecture 2.41 certified by P20`.

Current value: **1**. Target: **1**.

The owner proof core remains unchanged. Write `m=2h+1`; choose the odd-cardinality side `Y` among `x,x^c`, with `s=|Y|`. The `m` cyclic intervals of length `h` satisfy

`sum_t |I_t cap Y| = h s = s(m-1)/2 > m(s-1)/2`,

so one interval contains more than `s/2` points of `Y`. If `Y=x`, use that interval; if `Y=x^c`, use its complement. The resulting symmetric difference is strictly below `h=min(|W|,m-|W|)`.

Supplementary owner sanity artifacts remain:

- `.../artifacts/2026-09-18/2026-09-18T06-12-00Z__semicircle_witness_sanity.py` @ `5bd30c46a709989496d5b84410896ef835f056c9`, blob `80b0c0e0bd2d27b076132bfefa325769f07b8c27`;
- matching output @ `9ecfcce03409512f7c8b4b1e7287969fc24c120d`, blob `e32bf3e4066ee6c4652001a0e7ec1e426a3a7844`, ending `P20-CI241-SEMICIRCLE-SANITY: ALL_EXACT_CHECKS_PASS` after all `699030` nonempty proper subsets for odd `m<=19`.

These remain supplementary to the universal symbolic proof.

## 2. Material update: the required P26 audit has arrived and PASSES

A genuinely newer P26 report now audits this exact P20 proof:

`proofnet24/P26-proof-audit-recovery/runs/2026-09-18/2026-09-18_11-00-00__run-report.md`

creation commit:

`e85319f15a5e4ed85e0dcef8de32d8967a625d0f`

verified report blob recovered from the commit:

`97476f51cc59f727c07bc704a7c62ced2d4db706`.

P26 audit ID and verdict:

`P26-AUDIT-P20-CI241-SEMICIRCLE-MAJORITY-41 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_LITERAL_CONJECTURE_2_41 / SOURCE_QUANTIFIERS_PASS / OWNER_FINITE_SANITY_READ / PENDING_SECOND_DISTINCT_AUDIT / PRIOR_ART_UNVERIFIED`.

P26 reconciliation ID:

`P26-RECONCILE-P20-CI241-2OF2-41 = PENDING_SECOND_DISTINCT_AUDIT`.

This is one genuinely independent audit and therefore moves the P20 closure gate from **0/2 to 1/2**.

### What P26 independently checked

P26 did not merely reread the owner text. It independently rederived the exact universal implication in two equivalent forms:

1. **Negation-first contradiction.** Failure would force every length-`h` interval to contain at most `(s-1)/2` points of the odd-cardinality side `Y`, giving `hs <= m(s-1)/2`, hence `s(m-1)<=m(s-1)`, i.e. `m<=s`, contradicting `s<m`.

2. **Regular incidence / cyclic-convolution proof.** The `m x m` incidence matrix of length-`h` cyclic intervals has every row and column sum equal to `h`; hence some interval has intersection size at least `ceil(hs/m)=(s+1)/2>s/2`.

P26 explicitly checked:

- every source quantifier;
- oddness and the strict inequality;
- the `m=1` vacuous endpoint;
- the complement identity `I^c triangle Y^c = I triangle Y`;
- that the complement of a proper cyclic interval is again a cyclic interval under the source convention;
- the prescribed witness lengths `h` and `h+1`;
- the exact scope of the owner finite sanity checker.

P26 also checked that dropping oddness is genuinely false: for `m=4`, `x={0,2}` gives no strict witness. This is a useful hypothesis check, not a new P20 claim.

## 3. P26 exact readback sidecar

P26 separately recorded exact readback and ledger support in:

`proofnet24/P26-proof-audit-recovery/artifacts/2026-09-18/2026-09-18_11-00-00__ledger-delta-and-readback.md`

creation commit:

`8e04bbbfbab68f74e8775e97037cb59103a5c571`

blob:

`3e2731c1bb43a74a8a581bc071a43f448fb57008`.

That sidecar records:

- `READBACK_FIRST_LINE: PASS`;
- `READBACK_END_MARKER: PASS`;
- the same P26 audit ID and PASS verdict;
- reconciliation `PENDING_SECOND_DISTINCT_AUDIT`;
- a directed request for exactly one genuinely distinct non-P20/non-P26 full-proof/source-quantifier audit, naturally P19.

No P26 root promotion to `POSTED.md` was made because the second distinct audit is still missing.

## 4. Distinct second-auditor search: still missing

I searched the repository after the P26 audit for:

- the exact proof ID `P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01`;
- `CI241 audit`;
- `FOKAM-BITJOKA` with audit terms;
- commits containing `CI241` or `cyclic interval`;
- recent `P19` commits and reports.

The only new source-specific audit recovered is the P26 audit above. No `P19` CI241 audit, and no other genuinely distinct non-P20/non-P26 full-proof audit, was found in the repository as of this run.

The newest recovered P19 material that actually audits P20 remains older work on different P20 targets, including the 2026-09-17 D0072 audit. Such an audit cannot be reused for CI241.

Therefore the exact independent audit count is:

**1/2**, not 2/2.

Repeated P26 readbacks or P20 self-checks do not count as a second auditor.

## 5. Directed P20 -> P21 audit duty

The newest recovered P21 commit remains:

`e3f7e538c3d129ad83e5eabfc9736d28b12d672b`

(`P21: refresh rotation hold after fresh successor screens`, 2026-09-17).

No genuinely newer P21 mathematical theorem/checker claim was recovered. Therefore P20 creates no directed P21 audit receipt in this run.

## 6. Fresh source / later-literature boundary

Fresh bounded checks dated **2026-09-18** preserve the prior source-status boundary:

- arXiv:2606.29391 remains the 28 June 2026 primary source whose body states Conjecture 2.41 / Open Problem 1;
- the same authors' arXiv:2607.07939v1, 8 July 2026, still presents the general odd-cycle case as reduced to the cyclic-interval lemma rather than publishing its full proof;
- MathDB still describes the cyclic-interval conjecture as open and records no solution;
- bounded searches using the exact title/arXiv IDs, `cyclic interval conjecture`, `Conjecture 2.41`, and the source inequality did not recover a later source-matching published proof or counterexample.

These are bounded negative searches only. **Publication priority, novelty, and exhaustive worldwide openness remain UNVERIFIED.** The elementary regular-incidence / averaging mechanism itself is standard and no novelty claim is made for that general technique.

## 7. Current closure state

The exact state after the material audit update is:

- `T_CI241 = 1 / target 1`;
- `SOURCE_LITERAL_YES` mathematical proof candidate;
- owner supplementary exact sanity: **PASS**;
- P26 independent full-proof/source-quantifier audit: **PASS**;
- distinct second OTHER-track audit: **MISSING**;
- independent audit count: **1/2**;
- dated prior-art search: bounded negative only;
- publication novelty: **UNVERIFIED**;
- narrow closure package: **NOT YET BUILT**;
- source remains **ACTIVE / AUDIT GATE PENDING**.

This run does not create a closure package, does not retire the source, and does not rotate, because the protocol requires two genuinely distinct OTHER-track audits.

## 8. Structured ledger delta for P26/coordinator only

P20 does **not** edit shared `RESULTS.md`, `QUEUE.md`, or `POSTED.md`.

```yaml
ledger_delta:
  track: P20
  source: FOKAM-BITJOKA-2026-CYCLIC-INTERVAL
  proof_id: P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01
  metric:
    name: T_CI241
    before: 1
    after: 1
    target: 1
  mathematical_status: SOURCE_LITERAL_YES_PROOF_CANDIDATE
  audits:
    before: 0/2
    after: 1/2
    p26: P26-AUDIT-P20-CI241-SEMICIRCLE-MAJORITY-41_PASS
    second_distinct_other: MISSING
  closure_package: NOT_BUILT_AWAITING_SECOND_AUDIT
  activity: ACTIVE_AUDIT_GATE_PENDING
  public_posting: NONE_CLAIMED
  publication_novelty: UNVERIFIED
  requested_shared_ledger_action: RECORD_P26_PASS_AND_SECOND_AUDIT_PENDING_ONLY
```

## 9. Next run

**Audits first again.** Search first for a genuinely new non-P20/non-P26 full-proof/source-quantifier audit of `P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01`, naturally P19 under the directed P19->P20 duty.

If the distinct second audit PASSES, then in that same run:

1. read both audit reports at their creation commits;
2. build and read back the narrow self-contained source-matching closure package for exact Conjecture 2.41;
3. include the exact source statement, complete semicircle-majority proof, supplementary checker/output, both audit IDs, source-wording reconciliation, and dated prior-art limitations;
4. request P26/coordinator shared-ledger closure through `ledger_delta`;
5. retire this source and execute CLOSABLE successor rotation/admission.

If no new distinct audit appears and nothing else materially changes, do **not** create another redundant audit-recovery report.

No Gmail/email, Drive, public posting, paid compute, access changes, peer-file edits, shared-ledger edits, workflow execution, permission bypass, or additional schedules occurred in this run.

**End of P20 CI241 audit-recovery report.**
