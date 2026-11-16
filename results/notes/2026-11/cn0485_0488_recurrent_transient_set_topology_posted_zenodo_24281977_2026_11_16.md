---
name: cn0485_0488_recurrent_transient_set_topology_posted_zenodo_24281977_2026_11_16
description: "[VERIFIED] Topology of the recurrent and transient walk sets (LMW Sec 6: R, R^c connected, simply connected, convex; CN0485-0488)? Answered and posted: repo recurrent-set-topology df5aad3, Zenodo 10.5281/zenodo.24281977, POSTED cdf3093"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T15:43:30+02:00
  status: provisional
  evidence: ""
---

Answers Li, Mossel and Weiss, Ann. Appl. Probab. 36 (2026) 4291-4310 (arXiv:2403.04108 v4 Section 6): path-connectedness of R for general S, Questions 6.7, 6.8, 6.11, 6.13.

Results (v_i = projections of the steps to the free part, r = their rank, K = conv hull):
- some v_i = 0: R star-shaped; r <= 2: R convex (LMW Cor 6.6 already has convexity for r<=2).
- no zero step and r >= 3: R homotopy equivalent to the bipartite graph B of balanced lines vs balanced planes (cover by the polytopes C_V, nerve theorem Hatcher 4G.3 + Ex 4, nerve to B by cones). So R path-connected iff B connected, simply connected iff B a tree.
- R^c: empty when r=0; star-shaped when r>=3 or 0 not in relint K; two contractible pieces when r=1 and 0 in relint K; homotopy equivalent to a circle when r=2 and 0 in relint K (section of the drift map built from a triangulation of K).
- R^c convex iff R = F iff every recurrent walk is positive recurrent.

Checks: check_nerve.py 300 trials and check_more.py (nerve 200, R^c grid 150) all 0 mismatch, reproduced on mini2 (numpy 2.0.2, scipy 1.13.1). Two outside Codex referees on mini2: both SOUND WITH GAPS, every MUST fixed (gaps were: r=0 empty case, 0 in K minus relint K case, section map choice, triangulation of R with each C_V a subcomplex). Reports: 12_cognitive_architecture/audits/reports/2026/11/16/recurrent_set_topology_referees.

Prior art: Google Scholar shows no citing paper of the journal version; Semantic Scholar and OpenAlex 0 citations (16 Nov). LMW published version checked on Crossref (doi 10.1214/26-AAP2329).

Posted 16 Nov 15:3x: public repo yspennstate/recurrent-set-topology df5aad37 (SHA256SUMS verified from a fresh clone), Zenodo 24281977 (md5 b6023a1f matches), open-problems-repo POSTED cdf3093 [skip ci]. ResearchGate entry not made yet (edit limit). Hint: what would change this - a later paper answering the same questions; recheck citing papers before any journal submission.

Related: [[grimmett_holmes_op38_coalescing_grand_couplings_posted_zenodo_24280343_2026_11_16]] (same posting recipe, same day), [[catalogue_row_already_solved_in_store_recall_first_2026_11_16]].
