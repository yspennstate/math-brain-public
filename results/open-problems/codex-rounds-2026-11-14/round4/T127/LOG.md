# T127 log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 04:55 Asia/Tbilisi.

## Scope and orientation

Read the reports, proofs, logs and Python scripts in both predecessor
directories. Neither directory was changed. Read the startup memory index,
mesh protocol and compute state. The governor reported warn,
owner_away_open, CPU saturation. No computations or other workers were
started. The specific instruction to write only here overrides the shared
mesh, checklist and brain-writing procedures; those commands were not run.
No git commands, publication, external messages or account creation occurred.

## Literature check, approximately 04:55–04:58

Used the web search tool with these queries:

- frog model 3 ary 4 ary tree recurrence transience 2026 proof
- "mt0-svg" "frog" proof
- "The frog model is recurrent on the 3-ary tree and transient on the 4-ary tree" arxiv
- site:zenodo.org "frog" "mt0-svg"

Opened the arXiv pages of Christopher Hoffman, Tobias Johnson and Matthew
Junge, arXiv:1404.6238, and Poly Mathews Jr, arXiv:2309.14443. The searches
did not identify an arXiv id for the later work. This is a negative search
result, not proof that no such id exists.

The previously identified repository and release page opened:

- https://github.com/mt0-svg/frog-model-tree
- https://github.com/mt0-svg/frog-model-tree/releases

Unlike the preceding session, these raw primary sources also opened:

- https://raw.githubusercontent.com/mt0-svg/frog-model-tree/main/STATEMENTS.md
- https://raw.githubusercontent.com/mt0-svg/frog-model-tree/main/paper/main.tex

The paper has 1,333 source lines. Inspected the introduction and model,
main theorem statements, reductions, finite-certificate criterion, lower
model and statement map. Section 1 uses exactly the initial condition and
simple random walks in T127; in particular the root has d neighbors and
other vertices d+1. Its V excludes time zero, which does not affect the
recurrence question. Theorem 1.2 states the d=4 conclusion and Theorem 1.3
the d=3 conclusion. The paper supplies a proof text, beyond the repository
announcement that was the only accessible evidence in earlier rounds.

Attempts to open the Zenodo record, the GitHub paper directory, and raw
Defs.lean, D3/Defs.lean, Solution.lean, SolutionRecurrent.lean and CITATION.cff
failed with inaccessible/cache-miss responses. The successful raw statement
map names the top-level declarations and the generated certificate modules
they require. The release page describes v2.0.0 as adding d=3 to v1's d=4
result. These are source reports; no Lean build or certificate was replayed.

## Decision

The first requested step has produced an accessible full paper asserting a
solution in the requested model. Stop under the literature branch and write
SOLVED_ELSEWHERE.md and REPORT.md. The new checkable result is retrieval and
applicability of the paper, not independent certification of its mathematics.
The source's claimed formal verification is not treated as verification
performed here. A full correctness audit remains outstanding.

Accordingly no new packet refinement was chosen, and the predecessor's
Bernoulli certificates were not rerun. Step 1 explicitly says to stop on
finding an outside solution, before the computation and extension steps.
No conclusion that the earlier result is wrong is made.

## Artifacts

Wrote SOLVED_ELSEWHERE.md with exact attribution, reference, arXiv-search
status and the verification limit. Wrote REPORT.md with a PARTIAL verdict
because the source was located and matched, while its certificates and full
proof have not been independently checked. No PROOF.md or computational
output is supplied: there is no new proof or numerical result in this session.
