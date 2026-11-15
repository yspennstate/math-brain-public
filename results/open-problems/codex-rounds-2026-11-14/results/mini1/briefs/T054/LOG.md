# T054 work log

Task received 14 November 2026, approximately 20:46 Asia/Tbilisi (16:46 UTC): “push this problem forward by one checkable piece.”

## 1. Orientation and literature check (started 16:46 UTC)

Read PROMPT.md, the startup memory index, brain navigation index, and compute_state.json. Compute status was ok, mode owner_away_open. The task's explicit folder-only rule supersedes global instructions to mutate the external mesh, checklist, or brain. No external state is being written; no subagents or git are used.

Initial web searches: `random regular graphs fixed degree quantum unique ergodicity 2026 2610.08127`; `"quantum unique ergodicity" "random regular" 2026`.

Search results include the cited October bulk-universality paper, an ICM survey, and an older statement of QUE for sufficiently large fixed degree. Search snippets are not being treated as theorems. Next: open the primary sources and distinguish arbitrary fixed degree from sufficiently large degree, and deterministic observables from graph-dependent observables.

The initial orientation used shell reads without an explicit nice wrapper; subsequent programs use nice 15 and single-thread environment variables. No mathematical computation has run yet.

## 2. Sources opened and scope check

Opened https://arxiv.org/abs/2610.08127 and its HTML, https://arxiv.org/abs/1609.09052, https://arxiv.org/abs/2102.00963 and its HTML, and Jiaoyang Huang's publication list. Authors were checked on the primary pages. The October paper proves bulk universality, not a stated QUE theorem (HTML search `ergod` returned no match). Huang–Yau, arXiv:2102.00963v3, Theorem 1.4, already proves complete delocalization for every fixed d >= 3. The sufficiently-large-degree restriction in the brief is therefore outdated for delocalization. Further web searches for November 2026 QUE and permutation/delocalization did not identify a later solution to a specified stronger QUE problem.

Commands used for read-only orientation included `nice -n 15 sed ...`, `nice -n 15 rg ...`, and `nice -n 15 cat ...`, with OMP_NUM_THREADS=1 and the BLAS thread variables set to 1. The sandbox prints `nice: setpriority: Operation not permitted` while still running these small reads. `ps` is also denied. No heavy program will be run without a working priority/resource guard. External brain recall was not run because its implementation starts a semantic worker and writes external logs; direct memory reads were used instead, respecting the folder-only rule.

## 3. Choice, made before the proof (16:49 UTC)

The literature check took under three minutes. No post-October advance resolving a specified stronger QUE statement was found. The older all-degree delocalization theorem is relevant input, not a newly discovered post-brief solution.

Chosen piece: prove an explicit finite-N reduction from permutation invariance and complete delocalization to relative QUE on deterministic mesoscopic vertex sets, uniformly over every eigenvector, including every vector in a multiple eigenspace. Observables are indicators of a deterministic family of sets, chosen before the graph. The target bound is expressed using L where every unit eigenvector has coordinate square at most L/N. A scalar concentration bound plus an eigenspace net should suffice; dimension is at most L because of this same coordinate bound.

Why this piece: it fixes the observable/rate quantifiers that the brief leaves open and tests whether this natural QUE formulation needs any new random-graph estimate. It also avoids assuming simple spectrum. Expected scope: an elementary consequence of known delocalization, with no novelty claim for deterministic-observable QUE. Graph-dependent observables and sharper fluctuation laws are outside this target.

Planned audit: independently compute sampling variance from finite-population covariances; rederive the Bernstein exponent and net constants; inspect repeated eigenspaces, endpoint set sizes, and the failure when a set is chosen after the eigenvector. No numerical experiment is needed for a proof of this reduction.

## 4. Proof saved

Wrote PROOF.md. The finite-N result is

`P(relative QUE error > epsilon) <= q + 2 M N (N+1) 9^floor(L) exp(-epsilon^2 s/(10L))`,

where q is the failure probability of complete delocalization and s is the smallest deterministic set size. Every unit vector in every eigenspace is covered. The proof uses independent Bernoulli sampling conditioned on its cardinality, a scalar exponential-moment bound proved in the text, and a 1/4-net. The dimension bound `dim E <= L` removes a hidden simple-spectrum assumption.

The application of Huang–Yau's Theorem 1.4 is conditional on its published delocalization theorem; this session does not reprove that input. It yields relative QUE for any polynomial-size deterministic family of sets of size at least N^alpha, alpha > 0. This is recorded as a consequence of existing work, not a novel solution of an unspecified stronger QUE conjecture.

A Walsh-matrix example was included to demonstrate exactly why the abstract result cannot be extended to sets chosen from the realized eigenvector. It is not presented as a random regular graph counterexample.

## 5. Adversarial audit and report

Wrote AUDIT.md and REPORT.md. Independently using t = epsilon/(3 delta) in the scalar exponential bound gives an exponent at least (5/48) epsilon^2 p/delta, which is stronger than the stated (1/10) epsilon^2 p/delta. This recovers the numerical constant without using the optimized parameter in the proof.

Two derivations give `Var(sum_T w_i) = h(N-h)/(N(N-1)) * (sum_i w_i^2 - 1/N)`. For the exact hand example N=4, h=2, w=(1/2,1/4,1/4,0), enumeration and formula both give variance 1/24. Projection and basis-coefficient arguments both give eigenspace dimension <= L. Checked s=N, s=1, L=1, L=N, complex eigenvectors, correlated set families, and the unconditional source exception probability. No flaw was found within the stated hypotheses.

The proposed extension to graph-dependent sets fails at the conditional-uniform-subset step. This is recorded as a limitation, with an explicit abstract counterexample, not as progress on that stronger formulation.

All mathematical results and audit calculations are saved in this folder. No heavy computation, simulation, git, external write, or subagent was used. Final verdict is the proved reduction and its deterministic-set corollary, with no claim to resolve an unspecified stronger QUE problem.

Final file check: `nice -n 15 head -n 1 REPORT.md` printed the required `VERDICT: PROVED ...` first line. `nice -n 15 wc -l PROOF.md AUDIT.md REPORT.md LOG.md` confirmed the four deliverables exist (195, 63, 25, and 51 lines before this final log entry). A targeted `rg` check confirmed that constants, floor(L), and graph-dependent-observable limitations agree across the report and audit. These small reads again printed the sandbox's setpriority warning.
