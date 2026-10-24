Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. NO MATHEMATICAL MOVEMENT — ADMISSION_PENDING; methods B2/B6/B18 were NOT claimed as tried because no source passed admission.

# NM13-03 — first admission screen

UTC run date: 2026-09-17
Category: CLOSABLE OUTSIDE
Own namespace: `proofnet24/NM13-03/`
Initial focus: other authors' finite random-matrix inequalities, exact moment questions, or sharp spectral constants.

## 1. Runtime / control state

The scheduler interface available to the owner exposes title, prompt, schedule, enablement and timing mode, but no binding model selector or reasoning-effort selector. Therefore `GPT-6 / maximum` in the worker prompt is only a request. This invocation identifies itself as GPT-5.6 Sol; authenticated reasoning-level telemetry is not exposed, so reasoning is reported as UNVERIFIED. No model setting was changed in this run.

I read the controlling repository policy surfaces: `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, and campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`. Large root/control files are connector-truncated surfaces rather than byte-for-byte reads; I used their controlling/current sections plus exact candidate/claim/history paths below. Repository search found no prior `proofnet24/NM13-03/` report and no neighboring `proofnet24/NM13-04/` report yet, so this is the first NM13-03 checkpoint.

The standing exclusions were preserved: no owner kernel/submatrix work, no posted Matrix-Spencer/Toeplitz-Hankel work, no retired/exhausted source, no source already exclusively claimed by another track, and no hard asymptotic question relabeled CLOSABLE merely to fill this slot.

## 2. Shard rule actually used

For every candidate having a canonical intake dedup key I computed

`int(SHA256(UTF-8 canonical_dedup_key).hexdigest(), 16) mod 13`

and retained only residue 2. For C-intake rows whose canonical `dedup_key` is exactly the C-number, I hashed that exact value. I did not hash display titles or aliases. I did not assign I-series rows lacking a canonical dedup key; those require source-identity recovery first.

## 3. Random-matrix shard-2 screen

### F0001 — Vu Conjecture 2.2, sharp iid Rademacher singularity

Canonical key: `vu_combinatorial_rmt_2020::conjecture_2.2`.
Shard: 2.
Exact source target: for iid uniform sign matrices, `P(det M_n=0)=(2+o(1)) n^2 2^{-n}`.

Disposition: **EXCLUDED FROM NM13-03**. This is not unassigned fresh inventory. Repository history shows R03 worked F0001 extensively, exhausted the permitted stuck-recovery cycles, and wrote a terminal handoff before rotating to F0097. The current `operations/claims/F0001.md` path is absent, but a missing claim file does not erase that explicit hard-target exhaustion. Reopening it here would violate both the handoff and the instruction not to turn a hard asymptotic target into a closable assignment.

### F0007 — Vu Conjecture 6.12, vanishing Rademacher permanent

Canonical key: `vu_combinatorial_rmt_2020::conjecture_6.12_(permanent)`.
Shard: 2.
Exact source target: `P(Per M_n=0)` is super-exponentially small in `n` for iid uniform sign matrices.
Prior campaign history: substantive attempt `F0007-A001` already exists.
Ownership check: `operations/claims/F0007.md` is absent at captured master; bounded repository search did not recover a live exclusive owner.

Fresh literature check, 2026-09-17 UTC:
- Yiming Chen, arXiv:2608.26707, *An Exponential Lower Bound for the Permanent of Random Bernoulli Matrix* (submitted 2026-08-27), proves constants `C,c>0` such that `|Per(M_n)| >= exp(-Cn) sqrt(n!)` with probability at least `1-n^{-c}` for large `n`.
- Frederic Koehler and Pui Kuen Leung, arXiv:2604.01367, study zeros/universality for biased random permanent interpolation; this is not the source zero-at-unbiased-sign-matrix statement.
- Ghasemi–Gross–Kopparty's finite-field permanental-rank work explicitly notes that even the square finite-field permanent-zero probability is not understood, again a different model.

These searches do not recover a source-matching resolution. Chen materially improves the magnitude picture but does **not** prove a super-exponential upper bound on `P(Per M_n=0)`; its stated exceptional probability is polynomial. Nevertheless F0007 is an asymptotic hard anti-concentration problem, not a finite certificate, specific number, or short sharp-constant problem presently justified as CLOSABLE. **Not admitted.**

### F0012 — Vu Conjecture 9.5, Gaussian-integral spectrum

Canonical key: `vu_combinatorial_rmt_2020::conjecture_9.5_(gaussian_integral_spectrum)`.
Shard: 2.
Exact source target: for iid Rademacher `M_n`, probability that all eigenvalues are Gaussian integers is `2^{-(1+o(1))n^2}`.
Prior campaign history: substantive attempt `F0012-A001` already exists.
Ownership check: `operations/claims/F0012.md` is absent at captured master; bounded repository search did not recover a live exclusive owner.

Fresh exact-phrase / 2026 searches for Gaussian-integer spectrum of random sign matrices did not recover a source-matching theorem; returned Gaussian-integer number-theory papers were unrelated. This remains, in the bounded evidence, an `n -> infinity` hard exponential-rate problem. **Not admitted to a CLOSABLE slot.** Search failure is not proof of global openness.

## 4. Other residue-2 candidates checked for category fit

The C-intake canonical keys `C0001`, `C0010`, `C0048`, `C0088`, `C0092`, `C0093`, and `C0160` all hash to residue 2. Their source scopes are respectively DGFF all-level/extremal-process limits, random-conductance DGFF extremal limits, Potts transition discontinuity, high-dimensional MST scaling limit, FK `q<1` sharpness, FK lace expansion, and a quasi-transitive/non-unimodular uniqueness-threshold residual. They are hard asymptotic/infinite-volume programs rather than the finite/random-matrix CLOSABLE target this slot is required to seek. None was admitted.

Additional shard-2 F-intake rows encountered in the bounded scan include four-dimensional Yang–Mills mass-gap scope and low-dimensional sandpile exponent scope; these are likewise HARD and were not relabeled closable.

The ranked queue's most attractive finite-looking rows cannot be dispatched by title alone. Several now have current claims (for example I0011/P16), and many I-series rows do not carry a canonical `dedup_key`; hashing an intake ID or display title would violate the shard rule. Those rows remain for later identity recovery, not automatic assignment.

## 5. Why no claim was created

A candidate must simultaneously satisfy exact source recovery, present-literature review, prior-history recovery, exclusive ownership, shard 2, and honest CLOSABLE classification. In this bounded first pass no candidate met all six conditions. Therefore I did **not** create `operations/claims/<ID>.md`, did not freeze a fake zero baseline, and did not begin mathematics on an unadmitted source.

This is deliberate protocol compliance rather than a claim that shard 2 contains no eligible problem anywhere in the approximately thousand-row corpus. The connector returns large intake surfaces in truncated chunks, so the census is incomplete.

## 6. Section-B accounting

Assigned first triple: B2 / B6 / B18.

- **B2 ATTACK THE NEGATION FIRST:** NOT ATTEMPTED mathematically; no source admitted.
- **B6 DEFORM TO A POINT YOU CAN SOLVE:** NOT ATTEMPTED mathematically; no source admitted.
- **B18 SAY IT IN ANOTHER LANGUAGE:** NOT ATTEMPTED mathematically; no source admitted.

I am not counting source screening, hashing, literature retrieval, or ownership checks as mathematical method attempts or metric movement.

## 7. Screening cursor / next invocation

Continue from the unscanned D/E/G/H/I and Codex candidate pools rather than repeating F0001/F0007/F0012. Priority order:

1. recover canonical source identities for previously unattempted finite/sharp-constant rows before hashing;
2. compute shard residue 2 from that canonical identity only;
3. reject any current/historical owner, exhausted handoff, POSTED/INDEX closure, or asymptotic HARD target;
4. prefer a finite random-matrix/spectral/norm question with an exact certificate or short theorem; if none appears, permit another genuinely CLOSABLE OUTSIDE source in shard 2;
5. once one passes, create the canonical claim create-only, read it back, freeze one source-faithful metric, and immediately spend the substantive run on B2/B6/B18.

Do not rerun the R03/F0001 program. Do not treat F0007 or F0012 as closable absent a genuine source-level finite/sharp reformulation authorized by the source itself.

## 8. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-03
  category: CLOSABLE_OUTSIDE
  target: ADMISSION_PENDING
  canonical_claim: NONE
  metric: UNMEASURED
  before: UNMEASURED
  after: UNMEASURED
  movement: false
  mathematical_status: OPEN_INVENTORY_SCREENING_ONLY
  methods_assigned: [2, 6, 18]
  methods_actually_tried: []
  candidates_screened_this_run:
    - F0001: EXCLUDED_EXHAUSTED_R03_HANDOFF
    - F0007: OPEN_BOUNDED_SEARCH_BUT_HARD_ASYMPTOTIC_NOT_CLOSABLE
    - F0012: OPEN_BOUNDED_SEARCH_BUT_HARD_ASYMPTOTIC_NOT_CLOSABLE
    - C0001: HARD_NOT_CLOSABLE
    - C0010: HARD_NOT_CLOSABLE
    - C0048: HARD_NOT_CLOSABLE
    - C0088: HARD_NOT_CLOSABLE
    - C0092: HARD_NOT_CLOSABLE
    - C0093: HARD_NOT_CLOSABLE
    - C0160: HARD_NOT_CLOSABLE
  unchanged_run_count: NOT_STARTED
  stuck_recovery_count: 0
  audits: NONE
  next_state: CONTINUE_SHARD2_ADMISSION_FROM_OTHER_INTAKES
  shared_roots_edited: false
```

No email, Drive, public posting, workflow execution, schedule change, shared-root edit, peer-file edit, claim overwrite, or paid compute occurred.

**End of complete run report.**