Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-04 post-P0029 shard-3 successor screen

Date checked: 2026-09-19 local.  
Selection rule: exact case-sensitive canonical candidate ID `sum(ord(c) for c in ID) % 7 == 3`.  
Slot class: CLOSABLE OUTSIDE.  
P0029 has been handed off after the six-unchanged rule and is not eligible for R7-04 continuation.

This screen is admission work only. It creates no ownership claim.

## 1. Highest-priority tier-2 shard candidates

The archived ranked intake assigns tier 2 to `P0013`, `P0029`, and `P0031` among the early shard-3 rows. `P0029` is the just-retired predecessor. I therefore checked `P0013` and `P0031` rather than jumping to a lower-ranked tier-3/4 row.

### P0013 — expected Lovasz theta of G(n,1/2)

Exact checksum:

`sum(ord(c) for c in "P0013") % 7 = 3`.

Intake/source: Randomstrasse101, *The Lovasz number for random graphs (problems 17 and 18)*, Conjecture 17. The current public source states

`E theta(G(n,1/2)) = (1+o(1)) sqrt(n)`.

Current source checked 2026-09-19: https://randomstrasse101.math.ethz.ch/posts/lovasz-circulant/ .

Ownership: no `operations/claims/P0013.md` exists on current master. However, a neighboring admission screen `proofnet24/NM13-06/runs/2026-09-17/2026-09-17T21-46-03Z__admission-screen.md` already recovered the same source and classified the remaining obligation as a sharp asymptotic upper-bound/uniform-integrability theorem rather than a finite-certificate endpoint. I rechecked the current source rather than treating that report as ownership.

Disposition: **not admitted by R7-04**. The source is a global `n->infinity` sharp-asymptotic theorem. It is honestly HARD-shaped for this constructive/CLOSABLE slot, even though the statement itself is precise. Relabeling it CLOSABLE would violate the owner classification rule. A bounded current search did not surface a source-matching resolution; that negative result is not an openness certificate.

### P0031 — sparse first-passage/Bessel pieces in forward Brownian concatenation

Exact checksum:

`sum(ord(c) for c in "P0031") % 7 = 3`.

Original source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probability Theory and Related Fields 160 (2014), 95–126, DOI 10.1007/s00440-013-0524-x; arXiv:1302.6958. Exact locator: Problem 7.4, printed PDF page 26.

The source assumes a decomposable forward Brownian motion made from Brownian pieces of length 1 most of the time, but with increasingly rare first-passage/Bessel pieces having

`T_k = inf{t>=0 : B_t^k = -1}`,

and asks **under which conditions on the frequency of those pieces** the result is a backward/two-sided Brownian motion.

Primary PDF checked 2026-09-19: https://math.washington.edu/sites/math/files/documents/research/1302.6958.pdf .

Prior attempt recovered from the campaign rank sheet: the first-passage tail satisfies the expected `t^{-1/2}` scale and suggests that a negligible exceptional time fraction is relevant, but that asymptotic observation does not construct the exact backward Brownian law after a shift.

Ownership: no `operations/claims/P0031.md` exists on current master, and repository search showed no canonical claim. This is not by itself permission to admit.

Later-work/status check: Pitman and Tang's 2015 Slepian/Brownian-bridge paper explicitly describes the broader non-identically distributed concatenation case as left open after Burdzy–Scheutzow's finite-mean i.i.d. theorem. A bounded 2026-09-19 search found no source-matching later classification theorem. Search misses are not proof of current openness.

Disposition: **not admitted by R7-04**. The source is not a single fixed proposition: it asks for a classification, uses the qualitative phrase “more and more rarely,” and does not freeze a source parameter/function class whose exact boundary would constitute closure. Converting it into, for example, a summability condition on a chosen deterministic frequency sequence would manufacture a narrower problem not explicitly posed by the source. It may be a valuable HARD/broad research program, but it is not a clean CLOSABLE source endpoint under the present admission rules.

## 2. Lower-ranked shard candidates

The next visible shard-3 Codex rows include `P0038`, `P0040`, `P0056`, `P0065`, `P0074`, `P0083`, `P0092`, `P0099`, `P0103`, `P0112`, and `P0119`. The intake descriptions are transience/percolation, spanning/minimal-forest classification, reinforced-process asymptotics, tree-automaton classification, and FPP curvature/geodesic/coexistence questions. The previously recovered campaign screens already classify the early percolation/FPP examples as HARD infinite-volume statements. None is promoted here without a complete source-current admission review.

## 3. Outcome

No fresh shard-3 candidate checked in this bounded post-retirement pass satisfies all of:

- exact shard 3;
- unclaimed/unreserved after alias check;
- source-current and non-excluded;
- precise source-level closure criterion;
- honestly CLOSABLE rather than HARD/broad;
- no silent narrowing to an attractive finite subproblem.

Therefore the successor state after P0029 retirement is **PENDING_ADMISSION**. No canonical claim is created in this run. The next R7-04 invocation should continue from materially new shard-3 candidates/status deltas rather than reopening P0029 or repeatedly rescreening P0013/P0031 without changed evidence.
