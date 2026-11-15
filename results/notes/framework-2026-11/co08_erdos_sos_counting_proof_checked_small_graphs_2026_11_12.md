---
name: co08_erdos_sos_counting_proof_checked_small_graphs_2026_11_12
description: "Erdos-Sos conjecture proved by a two-page counting argument over vertex orderings (exposition 2609.17877): every step read, both injections and the main inequality checked on all graphs up to 6 vertices; remove the row"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T01:33:38+02:00
  status: verified
  evidence: "06_math_research/co08_erdos_sos_agent_2026_11_12/CO08_CHECK.md, co08_check.out; push 25bb8bd1f66edc4f1a05533769f3582bf0e8a8fd"
---

Row CO08 (Erdős–Sós conjecture), 12 Nov 2026.

Proved (counting proof credited to GPT-6 Astra, 2026; written out in arXiv 2609.17877, Wood; simplified and extended in 2609.21159, Frederickson). Every graph with average degree > t - 2 contains every tree on t vertices.

The proof in one paragraph. M(G) = pairs (ordering, i) with v_1 v_i an edge, |M| = 2m(n-1)!. R(T, r) = those pairs for which the first i vertices induce a graph containing T with r at v_1. Claim: |M| <= |R(T, r)| + (t-2) n!. Lemma 3 (leaf root): |R(T-r, r')| <= |R(T, r)| + n!, by reversing the first i entries. Lemma 4 (T = T1 u T2 glued at r): |R(T1,r)| + |R(T2,r)| <= |M| + |R(T,r)| + n!, by moving the block after the first T1-prefix to the front. Induction on t. If G has no T then 2m(n-1)! <= (t-2) n!.

Checked: every step by hand; then by computer, written from the statements: all graphs on at most 5 vertices with the sets and both injections built literally (36,322 applications of the two maps, all into the stated set, all injective), all 156 graphs on 6 vertices and random graphs on 7 and 8 vertices by counting (26,176 instances of the main inequality, 4,632 of the theorem), and a control that fails when t-2 is replaced by t-3 (K_5, trees on 6 vertices).

Technique card: to prove an extremal bound for containing a rooted structure, count pairs (ordering, position) and build injections by rearranging a prefix of the ordering; the error term is one pair per ordering (the first occurrence), which is where the additive n! per tree vertex comes from. The same scheme gave the antidirected-tree conjecture and Kalai's conjecture for tight trees.

Not read: the original text, the Lean formalization. Files: 06_math_research/co08_erdos_sos_agent_2026_11_12/ (CO08_CHECK.md, co08_check.py, co08_check.out). Row proposal: remove from the open list; candidates for the slot: Loebl–Komlós–Sós, Havet–Reed–Stein–Wood. Related: [[ag05_jacobian_dim3_counterexample_recomputed_exactly_2026_11_12]], [[dg06_caratheodory_smooth_counterexample_checked_2026_11_12]].

