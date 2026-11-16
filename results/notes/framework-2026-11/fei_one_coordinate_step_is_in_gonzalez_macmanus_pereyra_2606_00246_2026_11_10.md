---
name: fei_one_coordinate_step_is_in_gonzalez_macmanus_pereyra_2606_00246_2026_11_10
description: "[VERIFIED] Is the FEI erasure / one-good-coordinate step new? Only half: Gonzalez-MacManus-Pereyra arXiv 2606.00246 (Jun 2026) have D_i = E_i + J_i (their eq 32), J <= 4 Inf, and sufficiency on stopping trees; Han 2312.08271 Rem 3.1-3.2 and CKLS Lemma 3.2 earlier. Ours: the converse, sharp 2/ln2, pseudo-likelihood, extremiser bound, refutations - POSTED as github.com/yspennstate/fourier-entropy-influence-one-coordinate"
metadata:
  node_type: memory
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T17:31:44+02:00
  status: provisional
  evidence: ""
  modified: 2026-11-10T16:05:22.927Z
---

Checked 10 Nov 2026 by an agent (loop T-20261110-078), reading the arXiv texts.

- Gonzalez, MacManus, Pereyra, 'Further evidence towards the Fourier Entropy-Influence conjecture', arXiv 2606.00246 v2 (9 Jun 2026).
  - Appendix B eq (32): the entropy drop H(f) - (H(f+)+H(f-))/2 when splitting x_m equals sum_S ((f+^2+f-^2)/2) h((f+-f-)^2/(2(f+^2+f-^2))), which is our E_i, plus sum ((f+^2+f-^2)/2)(1 - h(f+^2/(f+^2+f-^2))), which is our J_i.
  - Lemma 8.1 gives 1 - h(t) <= 4(1/2 - t)^2, so J <= 4 Inf. Our sharp constant is 2/ln 2.
  - Ansatz 1.1/1.2 and (22): one good coordinate at every node of a stopping tree implies FEI. This is our path formula.
  - (23) is Han's Question 3.1; they show it fails for a wrong splitting variable on mu-tribes.
  - They prove FEI for mu-tribes, tribe-separated monotone functions and semi-separated functions, and say they could not prove (21) for all Boolean or monotone functions.
- Han 2312.08271, Remark 3.1-3.2: the inductive one-coordinate route.
- CKLS ECCC 2013/052, Lemma 3.2: H(f) <= (H(g1)+H(g2))/2 + 2, the inequality version.
- No overlap: WWW 1312.3003, O'Donnell-Tan 1304.1347, KKLMS 1911.10579.
- Also new: Potapov arXiv 2609.21563 (Sep 2026), FEI for plateaued functions with sharp constant 4 and for partially bent functions with constant 2. Check it before claiming any bent or plateaued result.

What remains ours, to verify again before a paper:
- (a) the converse: FEI with C gives sum_i E_i <= H <= C I, so some i has E_i <= C Inf_i. GMP's (22) is therefore necessary, not only sufficient.
- (b) the sharp 2/ln 2.
- (c) the pseudo-likelihood form.
- (d) C* <= R <= C* + 2/ln 2.
- (e) the extremiser influence bound.
- (f) the every-coordinate version is false (bent point replacement).
- (g) Han Q3.1 = GMP (23) fails for every coordinate (our public han-question-read-once-formulas).

The P1 plan in 06_math_research/fei_papers_agent/LOOP_STATE.md is cut to a short note on (a)-(g).

POSTED 10 Nov ~18:0x: github.com/yspennstate/fourier-entropy-influence-one-coordinate (main db1b7b84), 5-page note
"The one-coordinate step in the Fourier entropy-influence conjecture" with (a)-(g), GMP cited for the split and the
sufficiency, two referee passes, code/ re-checks every number (check_jsd_lemma.py: F >= 0 on 2M points, 2/ln2 limit).
Its error term in the bent example is O(2^-k/2). A peer paper on the same step should cite this repo, not repost it.
Lesson: the FEI agent's first literature pass (and mine) missed a 2026 arXiv paper. Search arXiv by the conjecture's name for the current year before calling an FEI reduction new.
Related: [[fei_equivalent_to_erasure_entropy_one_good_coordinate_2026_11_10]] [[duplicate_paper_posted_for_t067_withdrawn_check_public_table_first_2026_11_10]] [[fei_paper_duplicate_two_machines_same_theorem_2026_11_09]]
