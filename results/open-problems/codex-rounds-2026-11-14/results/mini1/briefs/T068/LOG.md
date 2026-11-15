# T068 working log

Task received: 14 November 2026, approximately 20:49 Asia/Tbilisi (16:49 UTC). “Push this problem forward by one checkable piece.”

## 20:50 — orientation and literature search started

Read the supplied instructions, local directory listing, startup memory, and compute governor state. No pre-existing mathematical work is in this folder. The governor reports `status: ok`. The current task's folder-only rule takes precedence over the earlier request to update the global mesh, checklist, and brain; those shared stores will not be edited.

Commands: `pwd`; `ls -la`; `cat ~/.claude/compute/compute_state.json`; startup-memory read; `OMP_NUM_THREADS=1 nice -n 15 python3 ~/.claude/dreaming/brain.py recall "Karp random graph clique greedy algorithm threshold"`.

The recall returned no relevant prior result. It also attempted its own background index refresh, which reported spawn failure. No further brain commands will be run. `nice` printed `setpriority: Operation not permitted`; future computation will check actual scheduling priority and use only small single-threaded standard-library programs.

Initial web queries: “Karp random graph clique log n algorithm 2025 2026 low degree threshold”; “finding cliques random graphs Karp problem algorithm lower bound 2024 2025 2026”. Search hits include an October 2026 edge-query paper and a June 2026 low-degree open-problem page. These are leads, not yet verified references.

## 20:51 — a direct broad-class advance located

Opened the arXiv abstract and full HTML of David Gamarnik, Eren C. Kızıldağ, Lutz Warnke, *Optimal Hardness of Online Algorithms for Large Independent Sets*, arXiv:2504.11450, v1 15 April 2025, v2 30 January 2026. URLs: https://arxiv.org/abs/2504.11450 and https://arxiv.org/html/2504.11450v2 . The abstract states a direct online-algorithm barrier for dense random independent sets, rather than only the related sparse/planted models mentioned in the brief. Checking theorem hypotheses and exact query model next.

Opened https://randomstrasse101.math.ethz.ch/posts/clique-low-degree/ as a lead; it is an open-problem page, not a paper used as a theorem source. The publisher's October 2026 edge-query article returned HTTP 403. Search identifies its older preprint as arXiv:2310.06826; publication date alone would not establish a new October 2026 result.

Decision: investigate the direct online barrier first. If its exact statement covers p=1/2, treat it as a substantial advance omitted from the supplied status, write the requested literature-stop artifacts, and stop. This is not evidence of an advance *after November 2026*: its dates will be stated explicitly.

## 20:52 Asia/Tbilisi / 16:52 UTC — theorem verified; stopping branch selected

The tool clock read 16:51:40 UTC at the last check. Headings are approximate local times. This search has taken about three minutes, within the ten-minute cap.

Read Definition 2.1, condition (1), Theorem 2.2 and Theorem 2.3 in the full HTML, then opened the 27-page PDF https://arxiv.org/pdf/2504.11450v2 for an independent presentation check. Theorem 2.2 covers p=1/2 and gives an explicit small-success bound. The budget is on queried vertex pairs inside the eventual output, not on the total number of future queries; accept/reject decisions are irrevocable. The unrestricted polynomial-time problem remains open.

Selected deliverable: the requested substantial-advance literature stop, with the exact clique specialization and its model limitation in SOLVED_ELSEWHERE.md. No claim of new mathematics or of a post-November-2026 publication will be made. No simulation is needed. Attempted scheduler read `ps -o pid=,ppid=,ni=,rss=,comm= -p $$,$PPID` was denied by the sandbox, so no further programs will be launched for computation.

## Final artifact and mathematical audit

Created SOLVED_ELSEWHERE.md and REPORT.md using apply_patch. The report's first line is a PARTIAL verdict, because this is an existing restricted-class result and the full question remains open.

Independent algebraic checks: (i) complementation maps independent fair edge indicators to independent fair edge indicators, and preserves query transcripts after reversing answers; (ii) at p=1/2, log_b(np)=log₂(n/2)=log₂n−1; (iii) the target event in the brief is a subset of the theorem's event without changing ε; (iv) the exponent is −ξL² in base two and −ξ[ln(n/2)]²/ln2 in the natural exponential; (v) the density range includes p=1/2 once n≥max{2d,2^d}; (vi) full pre-querying gives binom(k,2) queried output pairs, exceeding the permitted coefficient at the target scale. The model restriction was therefore not dropped accidentally.

Cross-checked the HTML theorem and constants against PDF printed page 9 (zero-based PDF page 8). This is a presentation check, not an independent verification of the underlying OGP proof. No simulations, random trials, or heavy computation were used. No git or external write was performed. Stop after final artifact readback.

Readback command: `sed -n '1,180p' SOLVED_ELSEWHERE.md REPORT.md LOG.md`. Exit 0; all three artifacts present; the required report verdict is correct. Tool clock at readback: 2026-11-14 16:53:34 UTC (20:53:34 Asia/Tbilisi). Replaced an unverified HTML fragment identifier with the opened paper URL. Literature search and verification finished within five minutes of session start.
