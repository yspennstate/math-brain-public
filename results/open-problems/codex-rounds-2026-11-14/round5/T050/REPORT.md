VERDICT: PARTIAL proved an explicit simultaneous-envelope theorem for fixed road windows

The round-4 finite-cell local-potential theorem holds under its stated
assumptions. Its projection identities, boundary clearance, radius and
error constant were independently re-derived in [LOG.md](LOG.md).
The bounded literature update found no verified solution of the full
continuous-law problem.

New beyond round 4: [PROOF.md](PROOF.md) proves the next named step,
the simultaneous-envelope passage associated with Lemma 10.4. For p
road periods and q edges of an anchor comparison tree, assume mean
period defect at most beta and mean absolute anchor increment error
at most c beta. The comparison budget is

    Lambda = [2p+c(p+q)] beta.

Local envelopes have expectation at most `(2K+1) Lambda` for trips
with at most K switches, and `3 Lambda` for physical competitors
with two signed center adjustments. These bounds hold simultaneously
over attachment occurrences, repeated visits and interior-edge points.
Their constants do not count microscopic occurrences or candidate paths.
The proof includes the measurability and spatial support of the envelopes.

A positive-edge finite-window example shows that linear growth with the
number of labels can be necessary under these hypotheses: each individual
pairwise anchor error has expectation at most 2 beta, while the maximum
switch difference among m labels equals m beta. This concerns what follows
from the estimates alone; it is not a counterexample to the canonical FPP
gauges or an error in the manuscript's fixed-label lemma.

Validation: a second interpolation identity checks the signs and the
period bound; independent counts check all coefficients. The proof tests
pauses, repeated visits, selected centers, empty competitor families,
disconnected subgraphs and common additive offsets. No numerical program
or simulation was needed.

Commands used `env OMP_NUM_THREADS=1 nice -n 15` followed by `rg --files`
on the four T050 folders or `cat` on the listed prior files and current
`PROOF.md LOG.md`. All prior reports, logs and proofs were read; file
enumeration found no prior research scripts and no original PROOF.md.
The exact web queries, source URLs, calculations and outputs are in LOG.md.

Opened primary source: OpenAI, *Strict convexity and differentiability of
the planar exponential first-passage limit shape*, September 24, 2026,
[manuscript](https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf),
Section 10.3 and Lemma 10.4, with Sections 15.6–15.7 read for scope.
No arXiv identifier was verified. The opened
[scope note](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/212.md)
still excludes strict convexity from its selected formalization.

Failures and limits: the first PDF open failed; the landing-page link
succeeded. The sandbox denied nice's priority change; reads completed,
and no heavy program ran. No mutation outside this folder, git, subagents
or external communication occurred. Strict convexity and the contraction
remain unproved here. No error was found in the finite-window envelope
step under its explicit assumptions.

Next worker: track p, q, c and K in the actual phase-dependent constructions.
Determine which families are averaged and which are maximized as the phase
mesh is refined. Prove the needed uniform expectation and support bounds
before using the rescaling choice in Sections 15.6–15.7. The present theorem
allows that bookkeeping to be checked without counting lattice occurrences.

Task: “take the NEXT checkable step on this problem, building on that work” —
first recorded 2026-11-15 07:41:24 Asia/Tbilisi (03:41:24 UTC;
receipt time not supplied).
