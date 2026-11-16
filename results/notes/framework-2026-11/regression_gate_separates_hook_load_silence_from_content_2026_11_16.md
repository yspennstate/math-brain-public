---
name: regression_gate_separates_hook_load_silence_from_content_2026_11_16
description: "Nightly math-brain regression gate read red on three nights while the same checks by hand passed. The recall hook had gone quiet by its own time budget under load, and the gate counted the quiet as a lost card. The gate now reads the hook's silence log for its own prompts and calls such a run inconclusive, not a breach."
metadata:
  type: project
  created: 2026-11-16
  status: verified
---

The math-brain recall hook runs on every prompt with its own clock: 30 seconds to rank, a 60-second hard deadline,
a 2-second grace for the integrity check on the top card. Past the clock it prints nothing, so the prompt is not
held up, and writes one line to a silence log: time, session prefix, reason, and the first ten hex digits of the
SHA-1 of the prompt.

The nightly regression gate asks the hook a fixed set of questions that must get an answer (a health check of
eleven must-speak and six must-stay-silent prompts, and one question sent through the production dispatcher). On
13, 14 and 16 November it read BREACH: the health check returned 1, and the production probe served no block. Run by
hand an hour later, every check passed. The silence log showed why. At the gate's own minutes, for the gate's own
prompts (matched by the fingerprint), the hook had stopped on its clock: `integrity_budget_exhausted`,
`budget_exhausted_before_ranking` at 48 to 56 seconds, `hard_deadline`. The machine was loaded, so the hook did what
it was built to do, and the gate read that as a lost card.

The gate already treated a health-check row that timed out twice as an instrument error: the run reads
INCONCLUSIVE, which is neither a pass nor a breach. Silence by the hook's own clock now gets the same treatment. When
a check fails, the gate reads the silence log for rows written during that check's window whose fingerprint
matches one of the check's own prompts and whose reason is budget- or deadline-shaped. If any exist, the run
records an error with the reasons, not a breach. A failure with no such row stays a breach. Rows saying the hook
exceeded its budget but went on (`..._proceeding`) do not count.

Controls on the live log: the production probe's silence of 16 November 02:21 is found; must-speak prompts
silenced since 13 November are found; a window starting after the last run, and a prompt nobody sent, find nothing.
A quiet run of the patched gate passes.

The limit: if one must-speak prompt is silenced by load and another fails on content in the same run, the run reads
INCONCLUSIVE. That is still not green, so a second night shows it.

The general rule: when a component has its own time budget and fails silently past it, a check on its content has
to see that budget. Either the check reads the component's own record of why it went quiet, or it gives the
component a budget of its own and judges speed separately. A check that reads only "no answer" cannot tell a slow
machine from a broken memory.
