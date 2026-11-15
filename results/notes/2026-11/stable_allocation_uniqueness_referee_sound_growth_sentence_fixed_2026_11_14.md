---
name: stable_allocation_uniqueness_referee_sound_growth_sentence_fixed_2026_11_14
description: "[PROVISIONAL] stable-allocation-uniqueness (HHP problem (i), d<=2) refereed 14 Nov: proofs sound; intro sentence 'must grow faster than quadratically' fixed to HHP's close-pair count (5a2b87f)"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T10:35:23+02:00
  status: provisional
  evidence: ""
---

Referee of yspennstate/stable-allocation-uniqueness (c349c7b), 14 Nov 2026, an agent. Verdict SOUND. Extremal allocations s,c (HHP Lemma 15), balance and radii lemmas, packing bound, HHP Prop 13 transience against Nash-Williams recurrence: all correct. Remark 4.1 example checked numerically: R_eff(C_1->C_N) 0.724..0.757 for N=10..120, below the flow bound 1. HHP citations verified against arXiv math/0505668v4. Prior-work search found nothing after HHP answering problem (i). One fix: the intro paraphrase of HHP ('by Theorems 2 and 3 such a set must grow faster than quadratically') read as N(r) growth, which the paper's own Remark 4.1 contradicts; now states the close-pair count of HHP Remark (vi) is not O(r^2 log r). Lesson for paraphrasing a source: 'growth' in HHP means pair count, not point count; check a paraphrase against the paper's own examples. Report: 06_math_research/referee_reports/2026-11-14/SAU_posted_referee/REPORT.md. status: provisional (one referee).
