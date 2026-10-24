# G0008 — exclusive HARD OUTSIDE claim for R7-06

Owner: **R7-06 Hard Conjecture Certificates**.  
Native ID: `6aabe827777c8191a43330b4a87d481d`.  
Own root: `research7_2026-09-17/R7-06/`.  
Admission: `research7_2026-09-17/R7-06/admissions/2026-09-18T025300Z__G0008_axis_connectivity_monotonicity.md`, creation commit `a6ac22a84ba2b1e65cd77478a88315cac9a1bb2f`.  
Claim date: 2026-09-18 UTC.  
Category: **HARD OUTSIDE**.  
Shard check: `sum(ord(c) for c in "G0008") % 7 == 5`.

Outside source: Alberto M. Campos and Bernardo N. B. de Lima, *The probability of connection between two vertices cannot be monotone with the distance for Bernoulli Percolation on transitive graphs*, arXiv:2601.00291v1 (2026), Abstract/Introduction p. 1 and Section 3 p. 4; canonical intake `probability_1000_intake_G_20260910/problems.jsonl`, `G0008`.

Target: for Bernoulli bond percolation on `Z^2`, with `tau_n(p)=P_p(0<->(0,n))`, decide whether `tau_{n+1}(p) <= tau_n(p)` for every `0<p<1` and every `n>=1`; preserve the source's broader `Z^d` wording as a stronger/full canonical endpoint rather than silently discarding it.

Frozen metric: `M_axis`, the largest `N>=1` for which R7-06 has rigorously proved the inequalities simultaneously for every `p in (0,1)` and every `1<=n<=N`. Admission baseline: **UNKNOWN/UNMEASURED**.

Ownership check immediately before create-only claim: direct fetch of `operations/claims/G0008.md` at fresh master `a6ac22a84ba2b1e65cd77478a88315cac9a1bb2f` returned 404. Repository search recovered prior intake attempts and admission screens, not a competing canonical claim. Partitioning alone did not establish ownership.

Prior work to preserve: intake `G0008-A001` small-`p` all-`n` path-series argument was withdrawn; `G0008-A002` records the correction. Do not reuse it as a proof. Off-critical eventual monotonicity and the 2015 small-`p` theorem are partial only.

This file is an ownership reservation, not a mathematical result and not a claim of novelty. Full closure still requires source-level proof/refutation, dated prior-art review, applicable exact certificates, independent P26 plus a distinct OTHER-track audit, and a self-contained paper package.
