# Independent audit of the prepared native campaign updates

Status: reviewed locally; no native schedules or remote repositories changed by this audit.

## Scope and timing: pass

Compared `native_updates.json` with the complete 25-task `current_automations.json` backup. The update list is an exact bijection to the twenty originally enabled B01–B20 tasks. It contains no duplicate or unknown task and touches none of the five disabled tasks. B01–B20 map respectively to F01–F20. Task identifiers were compared privately and are deliberately omitted here.

Every hourly minute and second is preserved. In particular B12/F12 retains minute 18 and second 10, inherited from its original DTSTART because its old RRULE had no BYMINUTE or BYSECOND. Every original timezone is Asia/Jerusalem, which every update retains. All twenty new RRULEs have precisely UNTIL=20261021T190842Z. Independent recurrence parsing produced no occurrence after that deadline. The native update tool documentation specifies that omitted fields preserve their current values.

All original tasks have timing_mode exact_schedule. No original event, trigger, source or condition configuration is present in the saved inventory. There is no evidence of webhook triggers needing transfer. Conversation linkage and other omitted native fields remain untouched by the partial update. No task creation, resumption of disabled tasks, additional account, or schedule extension appears in the builder.

## Research scope and honesty: pass

Every prompt gives full uniform-cube FEI or a rigorous unbounded Boolean counterfamily as its sole mathematical objective, explicitly keeps full FEI OPEN, and identifies the threshold paper as scoped prior work. All twenty prompts forbid reverting to the older Brain, Primary Directive, 200-problem, movie or mixed-portfolio mission. The F20 prompt additionally forbids old-template restoration and limits coordination to the current campaign. Stalled-route reassignment stays within FEI.

The twenty teams contain exactly five logical roles each, with the coordinator included: 100 roles, not a claim of 100 simultaneous workers. Each prompt respects actual in-run capacity. GPT-6 and maximum reasoning are requests; each prompt explicitly admits the scheduler API has no model or reasoning selector and forbids claiming configuration from prompt wording.

All prompts require committed results in the canonical private open-problems repository and a separately verified mirror in the private Brain repository. CAMPAIGN.md and F20 explicitly reserve public publication for the prepared threshold paper and its reproducibility package, not campaign reports or future unapproved manuscripts.

The prepared schedule manifest matches every native prompt hash and recurrence. The paper source hash in the prompt matches the current final main.tex: 3a395e98153f826fa9160c348e45779f204d3ea77376f40cd71ee57440ba8193. The final package contains exactly six verification scripts and six corresponding JSON outputs, as the F20 publication instruction says.

## Setup observations requiring completion before claiming deployment

1. At this audit, bundle/ contains CAMPAIGN.md, SCHEDULE_PLAN.json, TEAMS.json and team states only. The startup sources REPORT.md, CLAIMS.md, COUNTEREXAMPLES.md and baseline/threshold-paper.tex plus baseline/computations/ are not yet present. The parent is assembling these; commit and read back the actual sources before describing campaign setup as complete. The fallback prompt correctly requires reporting a missing source rather than inventing it.
2. Public routing is fully stated in CAMPAIGN.md and F20. To make every native prompt self-contained when campaign files are temporarily inaccessible, add one common sentence explicitly prohibiting public publication of campaign reports or future unapproved papers. This is a clarity improvement, not a discovered authorization defect in the current combined instructions.
3. DTSTART is computed when the builder runs and selects each next hourly occurrence. Re-running the builder immediately before deployment refreshes those dates if assembly has taken time. The fixed endpoint does not move.

No blocking scope, recurrence, model-honesty or publication-authority defect was found in the reviewed builder and generated updates. This signs off prepared configuration only, not native installation, execution, remote commits or a mathematical solution.
