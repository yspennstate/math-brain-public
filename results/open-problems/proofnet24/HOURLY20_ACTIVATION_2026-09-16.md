# R01–R20: confirmed hourly schedule updates

Date: **16 September 2026**, Asia/Jerusalem.
Repository: `yspennstate/math-open-problems`; existing branch: `master`.

## Confirmed changes

All **20 existing research automation IDs** below were individually updated. Each update returned `status: SUCCESS`, `is_enabled: true`, `timing_mode: exact_schedule`, the revised GitHub-only prompt and its hourly recurrence. The confirmations were received between **12:42:56 and 12:50:05 UTC** (15:42:56–15:50:05 Asia/Jerusalem). No duplicate research tasks were created and unrelated schedules were not modified.

Every recurrence is `RRULE:FREQ=HOURLY;BYMINUTE=<minute>;BYSECOND=0`, with its own refreshed DTSTART supplied by the scheduler, no UNTIL and no COUNT. The twenty minute-of-hour slots are 00, 03, 06, ..., 57. These are invocation slots, not promises of exact report completion times.

Every revised prompt preserves its mathematical assignment and instructs the worker to continue from the actual latest GitHub proof record; use the deepest available reasoning; attempt original proofs, reductions or counterexamples rather than repetitive summaries; commit complete substantive work and actual code/certificates; confirm the commit SHA and read back the saved content; and retain explicit proof obligations and failed routes. Existing target folders take priority over fallback paths.

**Email delivery removed from all twenty prompts.** No Gmail sends, drafts, forwards, email retries or mandatory mailbox scans; no Drive uploads. The initial scheduler listing already showed native email and notification flags false for these tasks; those flags were not separately changed by the update interface. GitHub is the shared state and archive. This record does not assert control over any invocation already in progress under an older prompt.

## Verified automation registry

| Worker | Preserved target | Automation ID | Minute each hour | Update confirmation |
|---|---|---|---:|---|
| R01 | Fourier Entropy–Influence | 6aa7b563bc10819180f3cd524462dffc | 00 | SUCCESS; enabled |
| R02 | KLS | 6aa7b57642bc81919f330e26f9c4e7d0 | 03 | SUCCESS; enabled |
| R03 | Sharp Bernoulli singularity | 6aa7b58c91408191b5e2fee4e7207cad | 06 | SUCCESS; enabled |
| R04 | Critical random band matrices | 6aa7b5beb62081919e6e3b2132600818 | 09 | SUCCESS; enabled |
| R05 | Anderson extended states | 6aa7b5dcd2508191be328cbe3e73ebaa | 12 | SUCCESS; enabled |
| R06 | Two-dimensional localization | 6aa7b5f1e3c48191b8a9cc011cf621e6 | 15 | SUCCESS; enabled |
| R07 | KPZ first-passage fluctuations | 6aa7b60f13b48191a7f81f6b23a1cd04 | 18 | SUCCESS; enabled |
| R08 | First-passage limit shape | 6aa7b61fcc64819196b2b7d99eed7eb1 | 21 | SUCCESS; enabled |
| R09 | Critical percolation Z3 | 6aa7b641ea908191a10d368ba077a905 | 24 | SUCCESS; enabled |
| R10 | Square-lattice Cardy formula | 6aa7b669391081918ba308c31573a86e | 27 | SUCCESS; enabled |
| R11 | Planar self-avoiding walk | 6aa7b68c70c481919b1a131eb67b6b24 | 30 | SUCCESS; enabled |
| R12 | de Almeida–Thouless line | 6aa7b6a3818881919e741f8866c98c8f | 33 | SUCCESS; enabled |
| R13 | Komlós vector balancing | 6aa7b6c1c9f88191bbd705b3fb72cda3 | 36 | SUCCESS; enabled |
| R14 | Negative-margin perceptron | 6aa7b6d7830c81919ce14c56f8a07d5f | 39 | SUCCESS; enabled |
| R15 | Cugliandolo–Kurchan aging | 6aa7b6fc061c81919f2c9d7db32affb7 | 42 | SUCCESS; enabled |
| R16 | Beck–Fiala discrepancy | 6aa7ba8313bc8191ac81c89fd0c47226 | 45 | SUCCESS; enabled |
| R17 | Chvátal–Sankoff constant | 6aa7baa15864819191733ebdb55b5b60 | 48 | SUCCESS; enabled |
| R18 | Salem Bernoulli convolutions | 6aa7bad95ee881919a9d5df2b5972da3 | 51 | SUCCESS; enabled |
| R19 | Free group factors | 6aa7baee1b908191be8be8fdcd61c8f1 | 54 | SUCCESS; enabled |
| R20 | Kalikow directional zero–one | 6aa7bafe94688191819c3ba457bc9090 | 57 | SUCCESS; enabled |

## Committed protocol and output convention

Current operational protocol: `proofnet24/HOURLY20_PROTOCOL_2026-09-16.md`.
Its successful creation returned commit `3cd07a86643ed8cbe5fb8b8223db6a230fbd305d`.
The companion file ending `2026-09-15.md` contains inherited exact targets; its effective date was incorrectly written during this setup and is explicitly superseded by the September 16 protocol. It is not evidence of a September 15 activation.

Each completed run should create:

`<track>/runs/YYYY-MM-DD/YYYY-MM-DD_HH-MM-SS_UTC__Rxx__<unique-id>__report.md`

Reports must preserve complete equations, proof attempts, stable claim IDs, PROVED/CONDITIONAL/DISPROVED/OPEN status, failed routes, reproducible scripts/certificates, source paths and the next precise obligation. GitHub create/commit confirmation plus readback is required before claiming a push. Local files alone are not GitHub archival.

If saving fails or approval is required, the worker must obey the requirement, preserve the full unpushed report in its task conversation/local attachment when supported, and report GITHUB_SAVE_FAILED or APPROVAL_REQUIRED without treating that as mathematical failure. Workers are instructed not to pause/disable/change schedules themselves. No force pushes, historical overwrites, permission changes or unrelated personal material are authorized.

## Limits of this confirmation

This is a record of actual successful configuration updates and a successful protocol commit, not a claim that a new mathematical theorem or twenty post-update research runs have already been completed.

The scheduler interface used here exposes schedule/prompt/enabled controls, not model selection, reasoning-effort selection, a guaranteed sixty-minute execution budget or an unpausable mode. GPT-6 maximum thinking and sustained use of available time are included as user preferences. No such setting or runtime is falsely certified.

No detailed cause for the reported previous interruptions was exposed. These updates refresh and enable the schedules with no programmed end date; they cannot guarantee that platform limits, authorization requirements, outages or future pauses will never interrupt them. Future deliveries must be assessed from their actual research reports and verified commits.
