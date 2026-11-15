# T105 work log

Task: “push this problem forward by one checkable piece.” Session date: 2026-11-14 (Asia/Tbilisi). Exact prompt receipt time is not supplied.

## Start

- Read the workspace listing and `~/.claude/compute/compute_state.json`. The workspace initially contained `PROMPT.md`, `codex.log`, and `run.pid`. Governor status was `warn`, mode `owner_away_open`, with CPU saturation. No heavy computation is planned.
- Read the brain navigation index. The task-specific rule permitting writes only here overrides the earlier instructions to mutate the shared checklist, mesh, and memory. Those shared systems will not be written.
- Shell commands are requested with `OMP_NUM_THREADS=1 nice -n 15`. The sandbox prints `nice: setpriority: Operation not permitted` before running them. Priority inheritance is being checked; no numerical experiment will be launched without resolving the resource constraint.
- Began the required web literature check with searches for recent flat-torus spacing and higher-correlation results. The search phase is limited to ten minutes.

## Literature step 1

Web tool commands:

1. `search_query`: `Berry Tabor flat tori nearest neighbour spacing distribution 2024 2025 2026`; `flat tori higher correlations triple correlation Berry Tabor 2024 2025 2026`.
2. `open`: `https://arxiv.org/abs/2601.03209`, `https://arxiv.org/html/2601.03209v2`, `https://arxiv.org/abs/2609.03112`, `https://arxiv.org/abs/1809.07881`.

Output that matters:

- Kim–Marklof–Welsh, arXiv:2601.03209v2 (uploaded 5 November 2026), reports a pair-correlation theorem for three-dimensional Dirichlet boxes with Diophantine proportions. This is an omitted substantial advance in the wider conjecture, not a solution of the stated two-dimensional target. The full HTML introduction has been opened; exact hypotheses are being checked before deciding the stopping branch.
- Christopher Lutsko, arXiv:2609.03112, reports a pair-correlation result for a different integrable model. Its abstract has been opened; no claim about its proof is made.
- The author list on arXiv:1809.07881 is Christoph Aistleitner, Valentin Blomer, Maksym Radziwiłł. The supplied author list is incorrect.
- The EMS full-text search result explicitly places VanderKam’s higher-correlation work in higher dimensions, rather than establishing higher-order correlations for generic two-dimensional tori. The full paper is being checked.
- `ps -o pid,ni,comm -p $$` was denied by the sandbox, as was `nice` priority adjustment. No numerical computation will be run. Read-only orientation also read the live memory index. No shared state was modified.

## Literature step 2 and stopping decision

Further web commands:

- `search_query`: `"flat tori" "spacing" "2026" Poisson`; `"flat tori" "correlations" "2025" "2026"`; `"Berry-Tabor" "nearest" "2026"`.
- `open`: `https://arxiv.org/html/2601.03209v2` at lines 57 and 65; `https://ems.press/content/serial-article-files/42560` at lines 70 and 100.
- Read the startup memory by the requested low-priority shell invocation. `nice` remained unavailable. No further shell program is needed.
- Clock tool returned `2026-11-14 18:00:46 UTC`, i.e. 22:00:46 in the supplied timezone. The literature phase has taken only a few minutes and remains under ten minutes.

Decision: take step 1's “substantially advanced” stopping branch. The omitted 2026 three-dimensional theorem is a substantial extension beyond the results listed in the brief. It predates the brief's nominal November 2026 status date; it is new relative to its cited coverage, not demonstrably published after that unspecified check date. No later solution of the two-dimensional spacing problem was found in this bounded search. `SOLVED_ELSEWHERE.md` will explicitly distinguish an omitted partial advance from a solution. No original-proof or computation project is selected under this branch.

Theorem 1.1 and the surrounding definitions have now been read in full. The requested audit will compare the abstract, theorem, and PDF; check dimension, symmetry sector, unfolding and the explicit example; and flag the limits of this literature check.

## Audit and completion

- Web command: `open https://arxiv.org/pdf/2601.03209v2`. Output: 33-page PDF. Theorem 1.1 on printed p. 2 matches HTML Theorem 1.1 and the abstract's statistic and dimension. The metadata upload date is 5 November 2026; the manuscript's internal revision date is 5 October 2026. These dates are not interchangeable.
- Web command: `screenshot` of PDF page index 1. Output: cache-miss retrieval failure. The PDF text and HTML remain readable. No assertion depends on interpreting a figure.
- Independent normalization check 1: count positive integer vectors in the ellipsoid Σ(πmᵢ/ℓᵢ)² ≤ E. Its positive-octant volume is (1/8)(4π/3)E^(3/2)(ℓ₁ℓ₂ℓ₃/π³) = ℓ₁ℓ₂ℓ₃ E^(3/2)/(6π²).
- Independent normalization check 2: the phase-space Weyl expression is (2π)^(−3) times the physical volume ℓ₁ℓ₂ℓ₃ times the momentum-ball volume (4π/3)E^(3/2). It gives the same coefficient 1/(6π²). Both methods give a positive coefficient and the correct scale-invariant unfolded coordinate when all lengths are rescaled together.
- Explicit-example check: squared edge lengths are 1, 2^(2/3), 2^(−2/3). All ordered nontrivial ratios belong to {2^(2/3),2^(−2/3),2^(4/3),2^(−4/3)}. Each is irrational: its cube is 2^k for k = ±2 or ±4, whose 2-adic valuation is not divisible by 3, whereas a rational cube has valuation divisible by 3. The paper's Roth-theorem application therefore covers these ratios; no quantitative Roth constant is asserted here.
- Symmetry check: a rectangular 3-torus has eight sign choices when all coordinates are nonzero. Identifying global ± leaves four choices. Thus the cited positive-orthant Dirichlet result must not be described as Poisson pair correlation for that entire torus spectrum after only ± identification. Coordinate hyperplanes require separate treatment if extending to other symmetry sectors; no such extension is claimed here.
- Scope check: pair correlation is a two-point statement. It neither supplies all higher correlations nor determines nearest-neighbour gaps. The cited theorem cannot close the task's main gap.
- Background check: the arXiv author list and the published EMS PDF agree on the corrected triple-correlation authors. The EMS introduction and the 2026 introduction independently place VanderKam's higher-correlation work in higher dimensions. Original VanderKam papers were not opened or independently reviewed.
- Other lead: the opened arXiv abstract at `https://arxiv.org/abs/2609.03112` is about Christopher Lutsko's three-particle Sutherland model, not the target flat-torus spacing law. It is not needed for the stopping decision.
- Wrote `SOLVED_ELSEWHERE.md` and `REPORT.md` using the workspace patch tool. No git, external writes, accounts, messages, numerical experiments or subagents were used. No `PROOF.md` is supplied because the mandated literature stopping branch was taken.
- Final readback command: `OMP_NUM_THREADS=1 nice -n 15 /bin/cat REPORT.md SOLVED_ELSEWHERE.md`. Output confirmed both saved files and the required report verdict line. The priority warning persisted. Removed an unverified HTML fragment from the theorem link; it now links to the opened full text. Final clock: `2026-11-14 18:02:35 UTC` (22:02:35 Asia/Tbilisi). All web work finished within ten minutes.
