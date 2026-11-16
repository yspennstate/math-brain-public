---
name: t277_joint_three_layer_beats_degree2_floor_at_4d2_two_layer_stuck_2026_11_01
description: T277 joint training on ReLU(x^T A x): 3-layer below the degree-2 floor by n=4d^2 (0.03-0.05 at 32d^2), 2-layer stuck near it; one seed, d<=32. Folder research_pushes/2026-11-01-t277-joint-training
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T01:35:23+04:00
  status: provisional
  evidence: "research-repo research_pushes NOTE/README read 2 Nov; joint.py runs, one seed"
---

T277 target 2 numerics (jointly trained three-layer nets on ReLU(x^T A x)), 1 Nov. Result folder: yspennstate/research-repo research_pushes/2026-11-01-t277-joint-training (README.md, joint.py, joint_d16/24/32.txt).

The Nichani-Damian-Lee (2305.06986) Theorem 4 target with Gaussian inputs, all layers trained together (their theorem is layer by layer). Degree-2 floor (best fit in span{1, z, |x|^2 - d}): normalized error 0.231, 0.245, 0.249 at d = 16, 24, 32. Measured (one seed; 2-layer width 1024, 3-layer 128x128, Adam): the three-layer net drops below the floor by n = 4 d^2 at d = 24 and 32 (0.208, 0.164) and by 8 d^2 at d = 16 (0.080), reaching 0.032-0.052 at n = 32 d^2, while the two-layer net stays near the floor there (0.157, 0.220, 0.243), its gap widening with d as a d^4-sample two-layer learner would predict.

Evidence, not proof: one seed, one architecture per depth, d <= 32, and an epoch cap of about 2 million presentations (61 epochs at d = 32, n = 32 d^2). It does not rule out a much wider or longer-trained two-layer net catching up. Sibling: [[t277_g_of_quadratic_form_is_csq_easy_above_op_norm_floor_2026_11_01]].

Related: written 2 Nov to close a gap on the results-without-memory list, per [[result_memories_must_name_their_research_pushes_folder_2026_11_02]] (a result memory names its folder so the pull job can match it).

