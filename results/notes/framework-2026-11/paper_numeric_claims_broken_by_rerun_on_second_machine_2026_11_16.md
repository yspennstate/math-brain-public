---
name: paper_numeric_claims_broken_by_rerun_on_second_machine_2026_11_16
description: "[VERIFIED] A paper states 'below 1e-28' or 'never fell below' from one run? Rerun the repository's commands on a second machine first: on 16 Nov both sentences in one paper were wrong."
metadata:
  type: feedback
  created: 2026-11-16
  status: verified
---

Before posting a paper on critical points of a gradient flow, its repository commands were rerun on a second machine.
Two sentences written from one run broke.

1. An example said the gradient at a constructed point is below 1e-28. The first machine printed 8.0e-29, the second
   1.9e-28 (a different BLAS). A floating-point residual is a fact about one machine: state an order of magnitude with
   room, here "below 1e-27".
2. A section said the distance to the critical point never fell below its initial value. The script prints the closest
   approach relative to |theta*|; the minimum was 0.0487 against a start of 0.05 (0.0471 on the null run), so 0.94 of
   the start. The sentence had been written from the escape counts, not from the closest-approach column.

How to apply. Before posting, run every command the README lists from a clean copy on a second machine, and check each
numeric sentence against the printed column it comes from, with its normalisation. Write residual bounds one order
loose. Why: the audits read the text, not the output; only a rerun could see this.
