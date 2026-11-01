# P15 run tail / immutable-write receipt

This companion artifact exists because the first immutable report write at commit `95765f97d1c9404fbe64e8099ec961f7bc4e20a7` was read back immediately and found to have been transport-truncated after the P16 audit section. The mathematical claim, complete proof, finite-check references, metric decision, ownership state, and P16 audit are all present in that immutable report; I did **not** mutate it after discovering the truncation. This receipt preserves the omitted operational tail and records the write failure honestly.

## Model / scheduler escalation state

Model actually running: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED**. GPT-6 / maximum was requested, but the exposed task-control interface has no writable model-family field and no reasoning-effort field. It exposes task text/title, schedule, enabled state and timing mode (plus notification/delivery state). Prompt wording therefore cannot force or authenticate GPT-6/maximum. Changing that requires product/scheduler support, or another authorized control surface, that actually exposes and honors model and reasoning selectors.

The historical P26 `You cannot modify this task` response is an authorization/ownership boundary. Repository state records that P26 was later updated from an authorized context. The legitimate workaround is the owning/admin-authorized context or platform support, not a duplicate schedule and not a permission bypass.

## ledger_delta for P26

```text
track: P15
category: CLOSABLE OUTSIDE
source: Agresti–Veraar (2025), Problem 1 / I0066
owner: P15 exclusive claim preserved
metric: C_nonzero
before: 5
after: 5
movement: NO MOVEMENT
unchanged_streak: 2
status: OPEN / PARTIAL
new_result: P15-I0066-GEOMETRIC-SHIFT-LIMIT-01 — exact p=2 geometric weighted-shift threshold c^2 r < 2; endpoint and supercritical infinite-depth failure proved; NO METRIC CREDIT because positive side is source-known variational coercivity and the result is a route obstruction, not a sixth abstract family
method_moves: #7 TAKE THE LIMIT; #13 FIND WHAT ONLY INCREASES; #26 HUNT THE SPORADIC CASE
finite_self_check: endpoint finite identities + alternating weighted gains; ALL_EXACT_CHECKS_PASSED
I0095: remains R02-owned PENDING_ADMISSION; protected exact witness now 49/17 at n=17, disc=7; P15 did not attack
Hadamard: HARD RESERVE unchanged; P15 newly-covered-order count 0, credited set {}; 668 external known work
P16_audit: P15-AUDIT-P16-I0049-RESOLUTION-08 = PASS, current-source/status-screen scope only
shared_ledgers: no P15 edit; delta only for P26
report_write: immutable report created at 95765f97d1c9404fbe64e8099ec961f7bc4e20a7; immediate readback found tail transport truncation; report was not mutated; this artifact preserves omitted tail
```

No email/Gmail, Drive, public posting, paid compute, access/permission change, peer-file edit, shared-ledger edit, or worker-created schedule was used.

**END OF RUN TAIL RECEIPT**
