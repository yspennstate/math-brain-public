---
name: t042_aaronson_ambainis_short_proof_checked_2026_11_12
description: "Aaronson-Ambainis conjecture proved (Nov 2026): short proof via completions and total influence as a potential read step by step, lemmas tested by computer to 7 bits; two quoted inputs not verified; remove the row"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T01:59:31+02:00
  status: verified
  evidence: "06_math_research/t042_aaronson_ambainis_agent_2026_11_12/T042_CHECK.md, t042_check.out, t042_check2.out; push 99214ebb6dadd9576229c36cadc61bf757c78cd7"
---

Row T042 (Aaronson-Ambainis conjecture), 12 Nov 2026.

Proved in November 2026: first proof Turturean, arXiv 2611.09773 (6 Nov, about 60 pages, not read); short proof Huffstutler, Miloschewsky, Podder, arXiv 2611.12795 (9 Nov), read in full; exposition arXiv 2611.11626 (abstract only). Both forms follow: a deterministic algorithm with O(Q(f)^6 / (eps delta)^2) queries right on a 1 - eps fraction of the domain, and max influence Omega(v^12 / d^12) for a bounded degree-d polynomial of variance v.

The proof in one paragraph. From a classical-adversary family lambda of cost CAdv build a completion G_t = 1[g < t], g(z) = min(1, min over 1-inputs a of the lambda^a-weighted distance to a); 4 lambda^x is a fractional certificate at every domain point and some threshold has total influence at most 4 CAdv. Certificate inequality (Lemma 4): densities delta_0, delta_1 of certified 0- and 1-inputs with certificate costs gamma_0, gamma_1 force a coordinate of influence at least delta_0 delta_1 / (gamma_0 gamma_1), also on subcubes. Query the most influential coordinate of G on the current subcube; total influence is a potential that drops by I_i each query, m = min(delta_0, delta_1) has non-increasing mean, so s e_s^2 <= 16 CAdv^2 I(G) = O(CAdv^3). CAdv = O(Q^2) is quoted from Anshu, Ben-David, Kundu (CCC 2021).

Checked: every step by hand except the two quoted results (ABDK21, OSSS). By computer from the statements: Lemma 4 on 8710 threshold pairs (all functions on 2 and 3 bits, named and random functions to 7 bits), its inner inequality (4) on 213351 subcubes (tight), the determinant argument for all functions on 3 bits, Lemma 3 on 340 random partial functions, the whole query procedure on 185 random partial functions (identity (8) exact, e_t never increases), Lemma 6 on 7500 random (tree, p) pairs. No failure. The computer check reaches 7 bits and tests the lemmas, not the exponents.

Technique card: turn a partial function into a total one that keeps cheap certificates on the domain and has small total influence, then use total influence as a potential for a greedy query tree; each query pays for itself through a certificate inequality on the current subcube. Same family as the completion framework of HKMP26.

Files: 06_math_research/t042_aaronson_ambainis_agent_2026_11_12/ (T042_CHECK.md, t042_check.py, t042_check2.py and outputs). Row proposal: remove; nearby open questions (Lovett-Zhang comparison in 2611.11626 section 2.2.3, optimal exponents) not vetted.

