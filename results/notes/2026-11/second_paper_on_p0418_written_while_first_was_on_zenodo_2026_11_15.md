---
name: second_paper_on_p0418_written_while_first_was_on_zenodo_2026_11_15
description: "[VERIFIED] Starting a paper on an open problem? Search OUR OWN public repos and Zenodo for the problem first - on 15 Nov a second P0418 paper was written, refereed twice and recommended to him for publishing while the first was already on Zenodo"
metadata:
  node_type: memory
  status: verified
  type: feedback
  originSessionId: agent-8e3d-41eb-b74a-1bc14932cde7
  modified: 2026-11-15T12:16:10.749Z
---

15 Nov 2026, an agent. Problem P0418 (D'Achille-Khezeli Question 7.2, IPVT limits of non-Poisson processes) got its paper early in the morning: public repo yspennstate/hyperbolic-voronoi-correlated-nuclei, Zenodo 10.5281/zenodo.24238909 (created 04:34Z), refereed by HVNB and HVNB2. Later the same day the same session, after a compaction, picked P0418 again as "paper 3" from agent's NOTE.md, wrote a second paper in private repo ipvt-nonpoisson-nuclei, ran two more referees (IPV1, IPV2) and a revision, and emailed him (1a1df1e2772251d8) recommending it be made public. Caught about ten minutes later by a curl of our public repos. Correction email 1a1df229d990c3fb; the second repo stays private and its fixes go into the posted paper's next version.

Why it happened: the literature search ("no prior answer found") covered arXiv and the problem's citers, not our own output; the compaction summary listed the morning paper by repo name only, not by problem number, so nothing joined the two. Same shape as [[duplicate_paper_posted_for_t067_withdrawn_check_public_table_first_2026_11_10]].

How to apply: before choosing a problem for a paper, and again before telling him a paper is ready, check our public record for that problem by number and by its key words: `curl -s "https://api.github.com/users/yspennstate/repos?per_page=100&sort=created"` (names), the Zenodo search `https://zenodo.org/api/records?q="<title words>"`, and the open-problem table's paper column. A compaction summary is not that record.
