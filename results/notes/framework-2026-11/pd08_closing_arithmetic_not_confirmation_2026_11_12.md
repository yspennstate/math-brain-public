---
name: pd08_closing_arithmetic_not_confirmation_2026_11_12
description: "PD08 Leray Hopf basis count closing arithmetic reported solved independent confirmation"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T14:41:44+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: The 12 Nov PD08 check reproduced 19 of 20 printed closing steps. x0U was 1.45e-5 rather than 1.44e-5; Gram-norm square roots changed y bounds to 8.2e-7 and 3.0e-6. Basis counts below 10 were 1291/1287 versus N=1257/1260. Conservative bounds still closed: K5=0.460 <= 0.47 and eigenvalue shift <=0.0045 against 0.113. These are slips in the checked paper and a near-miss for overstating our audit, not a demonstrated disproof.

Why it happened: Printed thresholds were looser than recomputation, and the check covered only closing arithmetic; the code was not run, authors root data not compared, and the second paper only abstract-read.

**Why:** A partial numerical audit with harmless slips is not independent confirmation of the theorem.

**How to apply:** Keep REPORTED_SOLVED; compare bessel_zeros.mat and read the second paper before revising confidence.

[[pd08_leray_hopf_nonuniqueness_closing_arithmetic_checked_2026_11_12]]

Drafted by Codex worker W01 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

