---
name: ag10_openai_preprint_sections_4_6_no_gap_large_d_enters_at_lemma_6_1_2026_11_12
description: "AG10 OpenAI cubic-fourfold preprint read in full (Sections 2-7, one reader): any gap? None found; harmless sign misprint in (5.5); large d enters at Prop 5.4, Lemma 6.3 and Lemma 6.1 (the Pfaffian escapes at Prop 5.4); smooth side rests on the GW operator algebra of Thm 3.3"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T18:02:28+02:00
  status: provisional
  evidence: "06_math_research/ag10_cubic_fourfold_agent_2026_11_12/AG10_SECTIONS_4_6_READING.md (whole paper, with CORRECTION); ag10_table514.out; pushes 111-112; one reader only"
  revised: 2026-11-12T18:15 (first version said large d enters only at Lemma 6.1; corrected)
---

One reader (an agent, 12 Nov 2026) went through Sections 2 to 7 of the OpenAI preprint "Irrational cubic
fourfolds with geometric K3 categories" (AG10; local copy lit/openai/main_c.txt in the AG10 folder) line by line and
found no gap. The paper claims Kuznetsov's conjecture fails for a very general cubic in every admissible C_d with d
large. One sign misprint: in (5.5), "- v(V/B)" should be "+ v(V/B)". It is harmless, because (6.10) and the
introduction carry the right sign.

The argument has two sides.
- Smooth side, Prop 3.10. Any f: P^4 -> X has cu(f) = 1, where cu is the Lin-Shinder divisorial cocycle counting
  degree-d K3 divisors. It rests on Theorem 3.3: an algebra G of two-point genus-zero GW operators on the
  transcendental lattice splits as G_M + Q id_{T_Z} under a blowup.
  The decisive point is that the operators never mix the blocks, even when the blown-up K3 is Hodge isometric to
  T_M. The mixed relative tensor is triangular over an absolute tensor with insertion i_* W, and i_* W = 0
  (Lemma 3.6). So blocks are tracked by primitive central idempotents, with no need for unique lattice
  decomposition.
- Sarkisov side, Theorem 6.6. cu = 0 between Mori fibre spaces over points once d > d0.
  Large d enters in three places, each a bounded-family exclusion played against Lemma 4.1's 2g - 2 >= n sqrt d:
  Prop 5.4 (links over a point or a curve), Lemma 6.3 (del Pezzo ends) and Lemma 6.1 (conic ramification fields).
  A first version of this memory said "only Lemma 6.1"; that was wrong. The Pfaffian d = 14 escapes at Prop 5.4.
  Prop 5.10's two-ray tables were checked exhaustive by brute force (ag10_table514.py). The result is consistent
  with Hassett-Lai's Cremona map of P^4, whose two K3s lie in the same test class, so the net count is 0.

How to apply: a second reader should press on Theorem 3.3 (Lemmas 3.6, 3.7, the Abramovich-Fantechi and Hu-Li-Ruan
inputs) and on the chain Theorem 4.9 (BAB) -> Prop 5.4 / Lemma 6.1. The cited inputs were taken as stated. Until an
independent audit exists, the AG10 row stays on KKPY Thm 6.8 and the OpenAI claim stays unverified. If the claim
holds, Cor 1.4 also gives irrational cubic fourfolds with universally trivial CH_0.
