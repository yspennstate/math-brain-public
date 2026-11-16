---
name: svgd_last_iterate_successor_conjecture_false_audit_2026_11_16
description: "Open-problem row on finite-particle rates for Stein variational gradient descent: the original kernelized-Stein-discrepancy question is answered in the literature (Balasubramanian, Banerjee and Ghosal, arXiv 2409.08469). The worker that retired the row proposed a successor, an expected last-iterate W2 rate; an adversarial auditor gave a counterexample for standard discrete SVGD with self-interactions in one dimension. Lesson: a successor conjecture written by the agent that answered the row needs an adversarial audit before it goes on a frontier card."
metadata:
  type: project
  created: 2026-11-16
  status: provisional
---

The row. A catalogue row asked for a polynomial finite-particle convergence rate for Stein variational gradient
descent (SVGD; Liu and Wang 2016). A worker agent found that the question as written is already answered:
Balasubramanian, Banerjee and Ghosal, "Improved Finite-Particle Convergence Rates for Stein Variational Gradient
Descent" (arXiv 2409.08469), give finite-particle rates in kernelized Stein discrepancy and Wasserstein-2 for the
time-averaged particle laws, improving on Shi and Mackey (2024). The row was retired as known, with that citation.

The successor. The same worker then proposed a stronger statement to keep on the frontier: an expected rate for the
last iterate in W2, not the time average.

The audit. A separate auditor agent, given the proposal and asked to break it, showed it false for standard discrete
SVGD with self-interactions: dimension 1, target V(x) = x^2/2 + cos(x)/4 (strongly convex, not Gaussian), kernel
1 + xy plus a Matérn-7/2 term, initial law N(0, 2). The argument is exact arithmetic, not a floating-point overflow.

Status and doubt. Provisional: the counterexample has been checked by the auditor only, not by a second reader and
not in a proof assistant. What would change it: a second independent check of the counterexample, or a reading of the
proposal under which the step size or the self-interaction convention differs.

How to apply. When a worker retires a row and proposes its successor in the same breath, the successor is the least
checked statement on the card: send it to an adversarial auditor of a different model family before it is listed as
open. A frontier card should carry the known result with its citation, and a successor only after it has survived
an attempt to refute it.

Acknowledgement. The known finite-particle rates are due to Krishnakumar Balasubramanian, Sayan Banerjee and Promit
Ghosal; SVGD itself to Qiang Liu and Dilin Wang.

Related: [[catalogue_row_already_solved_in_store_recall_first_2026_11_16]].
