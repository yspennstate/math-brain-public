---
name: e0053_maxbis_minbis_open_equals_zdeborova_boettcher_via_aronow_lopatto_2026_11_13
description: "E0053 (Bandeira OP 8.5: MaxBis + MinBis = dn/2 + o(n) on random d-regular graphs) open on 13 Nov 2026 for every fixed d >= 3; Aronow-Lopatto arXiv 2609.19057 prove E MaxCut - E MaxBis = o(n), so it is exactly the zero-temperature Zdeborova-Boettcher conjecture; the positive-temperature version holds up to reconstruction (Gheissari-Perkins-Yap 2511.16620); large d up to o(sqrt d) is Dembo-Montanari-Sen"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T15:07:11.529Z
---

E0053, rank 35 on the 200 list. Source: Bandeira, "Ten lectures and forty-two open problems", Open Problem 8.5 /
Conjecture 8.5. G uniform d-regular on n vertices; conjecture (MaxBis(G) + MinBis(G))/n -> d/2.

Status 13 Nov 2026 (arXiv abstracts read, plus a web search): open for every fixed d >= 3.
- Aronow and Lopatto, "Maximum cut and maximum bisection in random regular graphs", arXiv 2609.19057 (21 Jul 2026): for
  every fixed d, E MaxCut(G_{n,d}) - E MaxBis(G_{n,d}) = o(n) (Huang's interpolation theorem plus a structural lemma on
  adding one edge). So, with concentration, Bandeira's bisection form is equivalent to the Zdeborova-Boettcher conjecture
  (arXiv 0912.4861) in its original form E MaxCut + E MinBis = dn/2 + o(n).
- Gheissari, Perkins, Yap, arXiv 2511.16620 (Nov 2025): the positive-temperature Zdeborova-Boettcher identity holds for
  inverse temperatures below the tree reconstruction threshold. Zero temperature is far past reconstruction, so this does
  not reach the conjecture.
- Dembo, Montanari, Sen (arXiv 1503.03923): both sides are d/4 +- P_* sqrt(d)/2 + o(sqrt d), which gives the identity up
  to o(sqrt d) for large d only.
- For d = 3, Lichev (Electron. J. Combin. 30(2) P40) improves the min-bisection bounds but says nothing on the identity;
  a 2025 paper on 5-regular graphs (arXiv 2509.08531) still calls it a conjecture.

Ours: 8 Sep first pass (the DMS heuristic) and Codex run E0053A on 13 Nov 02:12Z (d <= 2 trivial cases, a concentration
reduction, first-moment bounds, numerics; one audit lane, not refereed; brain referee_reports/2026-11-13/E0053A). E0053A
does not use the Aronow-Lopatto equivalence; anyone picking this up should start from the max-cut form, where the
cavity-method and Ising literature lives.
Related: [[e0052_feige_conjecture_solved_fu_et_al_and_nie_wei_2607_2026_11_13]] (the previous Bandeira item on the list).
