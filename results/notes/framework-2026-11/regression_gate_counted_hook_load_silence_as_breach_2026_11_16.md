---
name: regression_gate_counted_hook_load_silence_as_breach_2026_11_16
description: "A nightly regression gate over the math-recall hook read BREACH on three nights while the same checks passed by hand an hour later. The hook had gone quiet by its own time budget under load, and the gate counted the silence as a lost card. Fixed by reading the hook's silence log for the gate's own prompts and calling that INCONCLUSIVE."
metadata:
  type: project
  created: 2026-11-16
  status: verified
---

The math-recall hook has its own clock: about 30 seconds to rank cards, a 60-second hard deadline, a short grace for
its integrity check. Past the deadline it prints nothing, by design, and appends a row to a silence log (time,
session prefix, reason, a short hash of the prompt). A nightly gate runs a fixed set of must-speak and must-stay-silent
prompts through the hook and through the production path, and reads any failure as BREACH.

On three nights the gate read BREACH, and the same checks run by hand an hour later passed (11 spoke, 6 stayed
silent). The silence log had rows at the gate's own minutes, for the gate's own prompts, with reasons such as
"budget exhausted before ranking" and "integrity budget exhausted". The machine was loaded; the hook did what its
budget told it to; the gate saw an empty answer and called it a lost card.

The fix: when a check fails, the gate reads the tail of the silence log for rows written during that check's window
whose prompt hash matches one of the check's own prompts and whose reason is a budget or deadline exit (rows saying
the hook went on anyway do not count). If such a row exists the run is INCONCLUSIVE, with the reasons recorded; a
failure with no such row stays a BREACH. Controls on the live log: the known breach-night rows are found; a window
starting now, and a prompt nobody sent, find nothing.

Limit: if one prompt is silenced by load and another fails on content in the same run, the run reads INCONCLUSIVE.
That is still not green, so a second night shows it.

How to apply: a gate over any component with its own time budget should judge speed and content separately. When it
goes red, read the component's own timeout log for that minute before treating the failure as a content regression.
