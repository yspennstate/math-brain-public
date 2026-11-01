# Setup receipt: 20 hourly research tasks, GitHub-only delivery

Date: 2026-09-15. User timezone: Asia/Jerusalem.
Repository: yspennstate/math-open-problems. Branch: master.

## Verified changes

The existing task prompts were read before editing. Exactly 20 selected existing tasks were updated in place through the scheduler. Every update returned SUCCESS, is_enabled=true, timing_mode=exact_schedule, and the retained FREQ=HOURLY schedule with its minute offset and no COUNT/UNTIL. No additional schedules were created. The update receipts were returned between 07:14:51 and 07:21:53 UTC on 2026-09-15.

The 19 existing research assignments were retained. The existing archivist was renamed P26 Proof Audit & Recovery and given substantive proof-bottleneck work in addition to its original verification/recovery duties. It remains the twentieth schedule, not a twenty-first task.

Every updated prompt now explicitly prohibits sending/drafting/forwarding research email and routine Gmail coordination/archival. All 20 had email_enabled=false and notifications_enabled=false in the initial scheduler inspection; the earlier explicit Gmail-send instructions were a separate delivery route and have now been removed from their prompts. No email was sent during this setup. No account-wide mail settings were changed. An execution already running with an older prompt was not cancelled by this configuration update and may still follow its earlier instructions.

Every worker is instructed to continue from complete prior research, maintain exact claim/dependency ledgers, attempt substantive mathematical work, preserve no-breakthrough attempts, commit its own COMPLETE immutable report directly to GitHub, and read it back using the actual returned commit SHA. A candidate full solution requires genuine independent complete-proof audits by two other workers. Workers must not self-disable for difficulty, no breakthrough, a restricted result, or a solved sublemma; later user stop instructions and platform limits remain binding.

## Task update receipts

| Track | Existing automation ID | Retained minute | Update result |
|---|---|---:|---|
| P01 | 6aa776d872288191aeca25649ae28125 | 00 | SUCCESS; enabled |
| P02 | 6aa777154640819194e055a4e88c9e01 | 03 | SUCCESS; enabled |
| P03 | 6aa778e84d988191a7120c1e2160d5dc | 30 | SUCCESS; enabled |
| P04 | 6aa778f56c4881919176824ec3d0bfbc | 45 | SUCCESS; enabled |
| P11 | 6aa7b116e0348191bc67bef1a41d9a39 | 12 | SUCCESS; enabled |
| P12 | 6aa7b12d7a4081919b69d0786ac5fb1a | 18 | SUCCESS; enabled |
| P13 | 6aa7b253b37c8191b693d8dc79298d37 | 05 | SUCCESS; enabled |
| P14 | 6aa7b25ce8c88191afd210fae4c41ffb | 20 | SUCCESS; enabled |
| P15 | 6aa7b265fc1481918b8682afaebbf7dd | 25 | SUCCESS; enabled |
| P16 | 6aa7b26de1a88191ae3ed17eff851eca | 40 | SUCCESS; enabled |
| P17 | 6aa7b275ca8c81919c41c34eea9a1154 | 50 | SUCCESS; enabled |
| P18 | 6aa7b27da4b081918afbbae136de8ea3 | 55 | SUCCESS; enabled |
| P19 | 6aa7b2852a9481918ab7dc5156c8b6cf | 58 | SUCCESS; enabled |
| P20 | 6aa7b28d8eb88191ad6b349f6288229f | 10 | SUCCESS; enabled |
| P21 | 6aa7b29a5c448191839a24e6f0ab1338 | 15 | SUCCESS; enabled |
| P22 | 6aa7b633bb3c81918f5a1d46066e8662 | 24 | SUCCESS; enabled |
| P23 | 6aa7b63f33348191aeddaa1cc1da8995 | 27 | SUCCESS; enabled |
| P24 | 6aa7b649d3088191a6e47e27d3787c1c | 32 | SUCCESS; enabled |
| P25 | 6aa7b653f300819183aa93aa620d8e23 | 37 | SUCCESS; enabled |
| P26 | 6aa7b43682948191b697d72fec69d539 | 59 | SUCCESS; enabled; renamed |

## GitHub configuration commits verified by read-back

- proofnet24/HOURLY_PROTOCOL_2026-09-15.md: commit a37dee46fac8ee840d1cc40fb01ea023a3bbe021; blob a5773ae98d59ab7d6420f809452c3b20565c3379. The complete committed protocol and 20-worker registry were read back.
- README.md: commit 18fd7ecad2765db8547f1410f61902074a0dddb2; blob 9d18531dff608e0165fe4434614d8c9121903c4c. The new top-level scheduled-research instruction was read back. Historical archival/layout rules were preserved.

## Important limitations, not hidden guarantees

The requested model is GPT-6 with maximum reasoning. That preference and the instruction to use the deepest available reasoning were added to every task. The exposed scheduler update action has no model or reasoning-effort parameter; no GPT-6 runtime selection or maximum-effort setting was changed or verified. Workers are instructed not to invent model/effort metadata.

All 20 selected schedules were already marked enabled at the initial inspection; subsequent update receipts also confirm enabled status. Recent research commits were visible during setup, including P16 commit ecc78060870d29d25395afe0eb6ed0d28700dd04 and P24 commit b7dd19193d809b1d55ee9ab62b42b208a5e9b2de. The evidence therefore does not establish that the entire selected portfolio was paused at inspection, or explain the user's earlier observed pause.

OpenAI's official Scheduled tasks in ChatGPT documentation states that inactive tasks may pause automatically. No switch to disable platform inactivity auto-pausing is exposed in the scheduling controls used here. Source checked during setup: https://help.openai.com/en/articles/10291617-tasks-in-chatgpt . This configuration does not bypass inactivity pauses, user pauses, limits, permissions, or safety restrictions.

Hourly schedules are execution triggers, not proof of successful future runs, continuous hour-long computation, a guaranteed completed push at an exact minute, or solved mathematics. P26 is instructed to record observed missing GitHub checkpoints and recover genuinely accessible complete outputs without using email or fabricating missing reports. Future GitHub pushes still depend on successful execution and authorized tool access.

This is a configuration and delivery repair receipt, not a new mathematical proof or a claim that all historical missing reports have been recovered.
