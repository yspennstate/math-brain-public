---
name: t359_multiclass_argmax_stores_md_points_2026_11_01
description: [PROVISIONAL] T359: M-class linear argmax on Gaussian points stores Theta~(M d) random labels (Hebbian lower, counting upper); GD stores ~0.7 Md/log M; Zipf optimum (Md)^(1-alpha)
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T23:46:20+04:00
  status: provisional
  evidence: ""
---



T359 (scaling law of a factorized associative memory, x -> argmax_y <u_y, W e_x>), 1 Nov. agent had reduced it on 18 Oct to the storage capacity c(M) d of an M-class linear classifier. The open question was whether c(M) grows linearly in M.

It does, up to logs. Hebbian sums per class with argmax decoding store M d/(8 log MK) random labels, and counting caps it at M d log(MK)/log M. So the Zipf optimum is (M d)^(1-alpha).

Measured: GD on cross-entropy stores K log M/(M d) = 0.63-0.83, flat over M = 2..32 at d = 32. At M = 2 that is the Cover 2d.

Lesson: "one-vs-rest gives no gain" was true but beside the point. Argmax lets a class lose only to the right one, so Hebbian already uses the parameters jointly.

Pushed 8b4740f (research_pushes/2026-11-01-loop-T359-multiclass-capacity); card claim_be7ba17109cd4e8593d4987f77f07574 (3 links); frontier move.

Related: [[t367_mean_field_3layer_needs_phi2_prime_nonzero_2026_11_01]] and [[t390_score_matching_weight_are_closed_form_2026_11_01]] are the same night's next-target rows after agent.
