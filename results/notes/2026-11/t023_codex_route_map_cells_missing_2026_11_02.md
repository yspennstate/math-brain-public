---
name: t023_codex_route_map_cells_missing_2026_11_02
description: [PROVISIONAL] T023 m023a (Codex worker, reviewed): no theorem for uniform-map Tutte/packing; Holden's Tutte proof general in Secs 3-4, uniform alphabet correlation 1/2 fits; missing cell geometry and quenched boundary control; brain recall did not help the worker
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T23:27:35+04:00
  status: provisional
  evidence: "brain-repo main 06_math_research/frontier/rows/T023/moves.jsonl c754236f"
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

T023 (Tutte / circle-packing embedding of uniform planar maps converges to sqrt(8/3)-LQG), first move m023a, moves.jsonl c754236f on brain-repo main, 2 Nov 2026. Done by a Codex worker (fleet brief m5f-T023 in ~/codex_fleet/20261102, acc1, about 8 minutes of work) and reviewed by an agent.

Result: no 2025-2026 theorem solves T023 (bounded search). Two newly found papers. Holden-Yu arXiv:2610.10480 covers circle packing and uniformization of mated-CRT maps for all gamma, sqrt(8/3) included, but for a different map law. Holden-Yu arXiv:2603.06528v2 gives conditional criteria. Holden's Tutte proof (2610.10501) is already general in Sections 3-4, with correlated step laws and any gamma. The uniform-triangulation percolation alphabet has correlation exactly 1/2 = -cos(pi gamma^2/4) at gamma^2 = 8/3. So what is missing is ensemble-specific: cell geometry, overlap moments, line connectivity, law transfer and quenched boundary control.

Caveat: the arXiv ids and page locators are the worker's reading; I checked the arithmetic, not the PDFs.

Lessons for running Codex on frontier rows:
(1) A literature-plus-route-map brief with named targets, page locators and a CLAIMS.jsonl schema came back complete in one pass and needed only a review to publish.
(2) The worker reported that brain recall and math recall returned weak or unrelated results on this question. On frontier literature, the primary papers were the useful source, so this is a brain-vs-no-brain data point against the current recall for research-frontier questions.
(3) Shell downloads from the Codex sandbox failed at DNS, while its browser tool fetched the PDFs.

Related: the T013 brief m5f-T013 runs on the same template; first T013 move [[t013_fk_crossing_rect_vs_disk_q2_q3_fail_unmatched_scale_2026_11_02]].


Checked 3 Nov 17:48 (an agent, second pass): the four arXiv ids resolve on arxiv.org, and their titles, authors and gamma match the claims (2610.10501 Holden Tutte tree-weighted sqrt2; 2610.10505 Holden-Yu packing tree-weighted; 2610.10480 Holden-Yu packing mated-CRT, whose abstract gives no gamma range; 2603.06528 v2 Holden-Yu ergodic scale-free). Correlation 1/2 and kappa' 6 re-derived by hand; audit.py reruns clean. The FK preprint is still unverified.
