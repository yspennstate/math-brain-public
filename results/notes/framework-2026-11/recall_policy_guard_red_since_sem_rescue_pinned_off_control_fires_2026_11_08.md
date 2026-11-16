---
name: recall_policy_guard_red_since_sem_rescue_pinned_off_control_fires_2026_11_08
description: "[VERIFIED] recall_policy_regression went red since the 30 Oct sem rescue: a [sem]-only row put the contract at rank 4 for a negative; router fine (rescue off: 10/10 positives, 31 negatives quiet); guard now pins rescue off, planted control still fires"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T03:23:13+04:00
  status: verified
  evidence: "guard runs before/after, planted-negative control, 8 Nov 03:23; framework 57e0704289"
---

Why did recall_policy_regression.py go red with the canonical router unchanged? The semantic rescue lane. Found and fixed by an agent on 8 Nov about 03:23.

- The guard failed one negative: "Do not implement canonical brain improvements; explain the phrase historically" had the contract NODE at rank 4, tagged [sem; owner-stated], so the query-meaning lane alone put it there.
- Since 30 Oct that lane's own top two memories go to ranks 4-5 ([[recall_sem_rescue_lane_top_two_at_ranks_4_5_2026_10_30]]). Negatives must stay out of the top 8, so the guard has probably been red since then; nothing I found shows a run in between.
- Two checks. With BRAIN_RECALL_SEM_RESCUE=0 the guard passes: 10 positives at rank 1, 31 negatives quiet. With BRAIN_RECALL_QSEM_K=0 the node also leaves the top 8.
- The rescue never touches ranks 1-3 and cannot route. The guard already pins usage tilt off for the same reason, so it now also sets BRAIN_RECALL_SEM_RESCUE=0 inside rank(), with a comment.
- Control after the fix: a scratch copy with "please build a brain dashboard" planted as a negative fires at rank 1 and the guard exits 1. It still catches a real router fire.
- Live copy changed (backup recall_policy_regression.py.pre_semrescue_20261108); brain-framework 57e0704289, pushed and equal on origin.

How to apply: when a guard goes red after a new recall lane lands, read the failing row's lane tag before blaming the code it guards. A [sem]-only row at rank 4-5 is the rescue. Rerun the guard after any change to the fused list. The live pipeline still shows the contract at rank 4 for that quoted-phrase question, which fits a question about the phrase.

