Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime/task interface provides no model-family selector, no reasoning-effort selector, no authenticated applied-runtime telemetry, and no guaranteed-duration control; I do not claim otherwise. **NO MOVEMENT in the frozen metric: `J_boundary = UNBOUNDED -> UNBOUNDED`; unchanged streak after saturation `5 -> 6`. CLOSABLE six-run rotation therefore triggers in this run.** Fresh Section-B moves: **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE; #23 DO WHAT THE PROPOSER DID NOT EXPECT; #30 ONE SCALE, ONE DIRECTION AT A TIME**.

# P20 D0010 — final sharpness test and mandatory six-run handoff

Active source before rotation: Ruodu Wang (2015), *Current Open Questions in Complete Mixability*, *Probability Surveys* 12, Open Problem 10, §2.8 / arXiv:1411.6190.

Repository / branch: `yspennstate/math-open-problems` / `master`.
Active root: `proofnet24/P20-closure-log-unimodality/successors/D0010/`.

The former Hasebe–Ueda–Wang I0081 / Problem 4.3 assignment remains source-refuted, packaged, posted in the exclusion registry, audited by two distinct OTHER tracks, and retired. It is not reopened here.

## 1. Continuity, repository reads, and why this is a rotation run

I continued from

`proofnet24/P20-closure-log-unimodality/successors/D0010/runs/2026-09-17/2026-09-17T03-10-01Z__run-report.md`,

which records `J_boundary = UNBOUNDED -> UNBOUNDED` and unchanged streak `4 -> 5`, and proves the paired-flank radius-quantile sufficient criterion `P20-D0010-PAIRED-FLANK-CM-06`.

Before new mathematics I read or refreshed the controlling repository surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FLEET_2026-09-16.md`, the canonical `operations/claims/D0010.md`, the newest own report, the newest P21 state, the newest P26 support/audit state visible to the connector, the D0010 admission/history search, and the current cumulative CLOSABLE successor screening under `operations/task_health/runs/2026-09-17T034510Z/queue_screening.md`. Exact D0010 intake/attempt continuity is preserved by the canonical claim and admission report; the large historical JSONL corpus is connector-truncated when rendered wholesale, so I used exact-ID/source searches rather than pretending to have visually rendered every historical byte.

The current P21 report remains a six-run retirement/handoff with no new theorem claim, so the directed P20->P21 duty does not justify manufacturing a new audit receipt. The P26 state preserves the full claim-scoped audit `P26-AUDIT-P20-D0010-ALLM-IFF-08`; P19 independently audited the all-piece family theorem. Those audits certify a restricted D0010 theorem, not Wang Open Problem 10.

The fleet rule for a CLOSABLE track is explicit: after six unchanged runs, preserve a handoff and rotate. Source-level partial mathematics does not reset the frozen metric. This run therefore performs one final sharpness attack on the newest theorem, then hands D0010 off.

## 2. Dated source/current-literature check — 17 September 2026

I rechecked the primary source and current author-maintained status evidence.

The source §2.8 asks:

> Open Problem 10. Under what extra conditions a unimodal distribution on a bounded interval is n-CM?

The immediately following source text emphasizes the case where one inequality in the moderate-mean condition is attained by equality. The same survey's §2.2 records, among known sufficient conditions, that if a density `f` on a finite interval `[a,b]` satisfies

`f(x) > 3/(n(b-a))` on `[a,b]`,

then `F` is `n`-completely mixable.

Ruodu Wang's author-maintained working-paper page still describes the survey as twelve open questions and specifically identifies Open Problem 1 as solved and Open Problem 12 as partially solved; it does not announce a resolution of Open Problem 10. The author's homepage was updated 14 September 2026 and still lists the survey without a stated Open Problem 10 resolution. A bounded fresh search for 2025–2026 `complete mixability` + `unimodal` + `Open Problem 10`, and for the exact paired-flank/radius-quantile mechanism, did not locate a source-matching complete characterization or the sharpness construction below. This is bounded negative evidence only, not proof of worldwide openness and not a novelty certificate.

The 2024 Komisarski–Labuschagne paper continues to describe characterization of `n`-complete mixability for `n>=3` as only partially solved and lists the standard sufficient classes (symmetric unimodal, monotone, concave, and positive-lower-density). Publication novelty for the P20 synthesis remains **UNVERIFIED**.

## 3. Move #17 — the number `n-1` is not the only route into complete mixability

The preceding P20 theorem pairs left/right flank radii and uses the Wang–Wang monotone-density theorem componentwise. Its ratio band

`Q_-(u)/(n-1) <= Q_+(u) <= (n-1)Q_-(u)`

comes directly from the moderate-mean support geometry of each two-level monotone component.

The source itself contains a qualitatively different sufficient mechanism: the pointwise lower-density criterion `f > 3/(n(b-a))`. That criterion does not mention the flank-radius ratio at all. This suggests testing necessity by constructing an asymmetric mode=mean density which is `n`-CM by the lower-density route while its second-radius-weighted flank quantiles violate the factor `n-1` band.

This succeeds for every `n>=4`.

## 4. Move #23 — assume the paired-flank condition is *not* necessary

### Claim `P20-D0010-PAIRED-FLANK-NOT-NECESSARY-07`

For every integer `n>=4`, there exists a bounded-support unimodal density `f` with a mode equal to its mean such that:

1. `f` is `n`-completely mixable;
2. the paired-flank quantile condition of `P20-D0010-PAIRED-FLANK-CM-06` fails on a set of positive Lebesgue measure.

Therefore the factor-`n-1` paired-flank criterion is a sufficient condition, not a necessary condition, even inside the mode=mean subclass for every `n>=4`.

Status: **PROVED / PARTIAL SOURCE RESULT / P20 SELF-CHECK**.

This does not settle the `n=3` necessity question and does not close Wang Open Problem 10.

### Proof

Fix `n>=4`. Choose numbers

`0 < a < b < 1/2`

with

`b > (n-1)a`,

and choose

`p in (3/n, 1)`.

Define the auxiliary probability density

`g_{a,b}(x) = c 1_[-a,0)(x) + d 1_(0,b](x)`

where

`c = b/[a(a+b)]`,

`d = a/[b(a+b)]`.

First check mass and mean. We have

`ca + db = b/(a+b) + a/(a+b) = 1`,

while

`c a^2 = d b^2 = ab/(a+b)`.

Hence

`int x g_{a,b}(x) dx = -(c a^2)/2 + (d b^2)/2 = 0`.

Now let

`f(x) = p 1_[-1/2,1/2](x) + (1-p) g_{a,b}(x)`.

Because the unit interval `[-1/2,1/2]` has length one, the first term has total mass `p`; the second has total mass `1-p`. Thus `f` is a probability density. Both components have mean zero, so `E_f X = 0`.

Since `b>a`, we have `c>d`. A monotone representative of `f` has the following shape as `x` increases:

- baseline level `p` on `[-1/2,-a)`;
- higher level `p+(1-p)c` on `[-a,0)`;
- lower-but-still-above-baseline level `p+(1-p)d` on `(0,b]`;
- baseline level `p` on `(b,1/2]`.

Set the irrelevant point value `f(0)` to the left-hand high value. Then `f` is nondecreasing on `[-1/2,0]` and nonincreasing on `[0,1/2]`. Hence `0` is a mode, and it equals the mean.

Moreover

`f(x) >= p > 3/n = 3/[n((1/2)-(-1/2))]`

throughout its essential support. The sufficient condition recorded in Wang's source therefore implies that `f` is `n`-completely mixable.

It remains to compute the flank measures from `P20-D0010-PAIRED-FLANK-CM-06`. With mode `m=0` and support radii `R_-=R_+=1/2`, the left and right Stieltjes flank measures are exactly

`sigma_- = p delta_{1/2} + (1-p)c delta_a`,

`sigma_+ = p delta_{1/2} + (1-p)d delta_b`.

Indeed, their tails reproduce the two step profiles `r -> f(-r)` and `s -> f(s)`.

Their second-radius moments coincide:

`M_- = p/4 + (1-p)c a^2`

`    = p/4 + (1-p)ab/(a+b)`

`    = p/4 + (1-p)d b^2 = M_+`.

Call the common value `M`. The normalized second-radius-weighted measures

`alpha(dr)=r^2 sigma_-(dr)/M`,

`beta(ds)=s^2 sigma_+(ds)/M`

therefore have equal positive lower-atom mass

`w = [(1-p)ab/(a+b)] / M > 0`

at `a` and `b`, respectively, with the remaining mass at `1/2`.

Thus, for every `u in (0,w)`, their generalized quantiles satisfy

`Q_-(u)=a`,

`Q_+(u)=b`.

By construction `b>(n-1)a`, so

`Q_+(u) > (n-1) Q_-(u)`

on the whole interval `(0,w)`, a set of positive Lebesgue measure. The paired-flank criterion fails although `f` is `n`-CM, unimodal, and has mode equal to mean. This proves the claim. QED.

### Concrete rational instance for `n=4`

A particularly transparent instance is

`a=1/20`, `b=1/4`, `p=4/5`.

Then `b/a=5>3=n-1`, and

`g(x)=(50/3)1_[-1/20,0)(x)+(2/3)1_(0,1/4](x)`.

Hence

`f(x)=4/5 + (1/5)g(x)` on `[-1/2,1/2]`.

The density levels are `4/5`, `62/15`, `14/15`, `4/5`; it is unimodal with mode and mean zero and satisfies `f>=4/5>3/4`. Its second-radius-weighted flank measures place mass `1/25` at `1/20` and `1/4`, respectively, so the paired quantile ratio equals `5` on `u in (0,1/25)`, exceeding the allowed factor `3`.

No checker is archived for this theorem-sized analytic claim: every identity needed is displayed and exact on the page, and the frozen metric did not move. Creating a script merely to re-evaluate these four rational equalities would violate the no-redundant-checker rule.

## 5. Move #30 — one scale / one direction at a time

The construction isolates exactly where the paired-flank theorem can fail to be necessary. A common uniform floor `p` certifies `n`-CM globally by the source's lower-density theorem. On top of that floor, only one tiny left radius `a` and one larger right radius `b` are inserted. The mean-zero balance fixes their step heights, but the second-radius-weighted quantiles still see the scale ratio `b/a` directly. Taking `b/a>n-1` defeats the flank criterion on a positive quantile interval without endangering complete mixability.

For `n=3`, this particular bypass is unavailable because the source lower-density condition would require `p>1`. Therefore the construction proves non-necessity for all `n>=4` and deliberately leaves the `n=3` sharpness question open. No stronger claim is made.

## 6. D0010 mathematical handoff after six unchanged runs

The source remains **PARTIAL**, not PROVED and not REFUTED. The most useful preserved results are:

1. Exact integer tail-count necessary inequalities at the tight boundary, inherited from the corrected pre-P20 attempt.
2. `P20-D0010-THREE-PIECE-IFF-01`: a sharp three-piece `n=3` boundary family classification.
3. `P20-D0010-ALL-M-PIECE-IFF-02`: sharp classifications for an explicit family with arbitrarily many pieces, giving the frozen metric `J_boundary = UNBOUNDED`. P26 and P19 independently audited this restricted theorem; those audits do not close the parent source.
4. `P20-D0010-LAYER-TRANSPORT-03` and `P20-D0010-NONMONOTONE-ALL-N-03`: a finite interval-layer sufficient criterion and explicit nonmonotone `n`-CM families.
5. `P20-D0010-CANONICAL-LAYER-FAILURE-04`, `P20-D0010-RECUT-COUPLING-04`, and `P20-D0010-WEAK-LIMIT-CLOSURE-04`: canonical nested layer transport is not a characterization; recutting can restore a certificate; fixed-center `n`-CM is weakly closed on bounded support.
6. `P20-D0010-GENERIC-THREESTEP-CM-05`: the previously unresolved generic three-step diagnostic family is `3`-CM throughout its whole unimodal range.
7. `P20-D0010-PAIRED-FLANK-CM-06`: an infinite-dimensional sufficient criterion for mode=mean unimodal densities via second-radius-weighted flank quantiles and two-level monotone components.
8. `P20-D0010-PAIRED-FLANK-NOT-NECESSARY-07` from this run: that criterion is not necessary for any `n>=4`; the source lower-density route provides explicit counterexamples to necessity.

The central unresolved source-level issue is still a characterization, or a substantially broader necessary-and-sufficient mechanism, for bounded unimodal distributions. The `n=3` mode=mean subclass remains particularly interesting because the positive-floor bypass used in this run does not apply there.

Prior-art caution: the convexity/decomposition machinery and the standard sufficient classes are published; the 2012 complete-mixability paper explicitly anticipates asymmetric unimodal applications. The exact P20 formulations were not located in bounded searches, but **novelty remains UNVERIFIED**. Any future reassignment must redo current literature checks rather than treating this handoff as a novelty certificate.

## 7. Mandatory CLOSABLE rotation and successor gate

Because the frozen metric stayed `UNBOUNDED` for a sixth consecutive post-saturation run, P20 now **retires D0010 from active hourly research and leaves this immutable handoff for future reassignment**. This is research rotation only: it does not claim the source has been solved, refuted, or abandoned.

I then checked the freshest cumulative CLOSABLE successor screening rather than claiming from the stale rank table. `operations/task_health/runs/2026-09-17T034510Z/queue_screening.md` states that there is currently **no candidate simultaneously satisfying** all mandatory dispatch gates: exact source/locator, dated current/later/citing checks, no current owner, and genuinely CLOSABLE source scope with a stable source-matching metric. It also records that the higher-ranked plausible rows are occupied, held, literature-resolved, or not CLOSABLE.

Therefore **no lawful READY + CLOSABLE + UNASSIGNED successor is claimed in this run**. P20 enters:

`ROTATION HOLD / SUCCESSOR_ADMISSION_REQUIRED`.

I do not narrow a HARD source to fabricate a closable task, and I do not overwrite another track's claim. The next P20 invocation should advance the cumulative queue-admission cursor beyond the already screened/occupied set and create a successor claim only after fresh source/current-status/prior-history/exclusive-ownership checks succeed.

The canonical D0010 claim remains historical ownership evidence. P20's active-research release is requested through the ledger delta below; P20 does not edit shared root ledgers or peer files.

## 8. P21 second-audit duty

The newest P21 state read this run is a rotation/handoff with no new theorem claim. I therefore issue **no new P20 audit ID**. Existing concrete component audits remain preserved. A nominal receipt would violate the instruction to audit only a genuine new claim.

## 9. Model/runtime control

The exposed task interface still offers prompt/title/schedule/enabled/timing controls but no model selector, reasoning-effort selector, or guaranteed-duration control. GPT-6/maximum therefore remains prompt-requested only. Enforcing it requires product-level exposure of those selectors plus authenticated applied-runtime telemetry, or configuration from an authorized owner/admin surface.

The historically denied P26 task ID `6aa7b43682948191b697d72fec69d539` has subsequently been updated from an authorized context. If a modification denial recurs, the legitimate path is the authorized owner/admin/product context, not duplication or permission bypass.

## 10. Requested ledger delta for P26

```yaml
ledger_delta:
  track: P20
  previous_target:
    id: D0010
    source: Ruodu Wang 2015, Current Open Questions in Complete Mixability, Open Problem 10 §2.8
    metric: J_boundary
    before: UNBOUNDED
    after: UNBOUNDED
    unchanged_streak: 6
    status: PARTIAL
    activity: ROTATED_AFTER_SIX_UNCHANGED
    source_closed: false
    new_claim_this_run: P20-D0010-PAIRED-FLANK-NOT-NECESSARY-07
    new_claim_scope: paired-flank criterion non-necessary for all n>=4 inside mode=mean unimodal subclass
    handoff_path: proofnet24/P20-closure-log-unimodality/successors/D0010/runs/2026-09-17/2026-09-17T04-12-18Z__sixrun-handoff.md
  audits:
    source_level_closure: false
    restricted_all_m_family:
      p26: P26-AUDIT-P20-D0010-ALLM-IFF-08
      other: P19-AUDIT-P20-D0010-ALL-M-PIECE-IFF-22
    new_claim_this_run: P20_SELF_CHECK_ONLY
  successor:
    state: SUCCESSOR_ADMISSION_REQUIRED
    claimed_id: null
    reason: no current candidate passes READY + CLOSABLE + UNASSIGNED dispatch gates in the freshest cumulative screening
  shared_files_edited_by_P20: false
```

## 11. Integrity / no redundant work

- No D0010 checker was rerun or re-archived.
- No new finite checker was created because the only new result is theorem-sized and the frozen metric did not move.
- No peer file or shared root ledger was edited.
- No Gmail/email, Drive, public posting, paid compute, access change, workflow execution, or extra schedule was used.
- This report is the immutable six-run handoff; future P20 research on D0010 requires reassignment rather than silent continuation.

END OF CANONICAL SIX-RUN HANDOFF
