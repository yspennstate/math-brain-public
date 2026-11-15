# D0070 work log

Task: “Open problem D0070”, received 2026-11-13, session directory created 08:29 local system clock (Asia/Tbilisi session timezone).

## Literature first

- Read startup memory index and compute governor: status ok, mode owner_away_open. No agents spawned.
- Attempted brain recall, mesh hello/digest/claim, and task checklist. Shared database writes are blocked by sandbox; use this local log. All task writes stay in this directory.
- Resource policy: single process for enumeration, nice 10, bounded depth/memory; no publication or pushes.
- Initial search found August 2026 Grimmett paper on Grigorchuk graphs; its abstract calls the general cubic bound a conjecture. This is not a solution of the full problem.
- Source PDFs will be converted through stdin/stdout in memory; only extracted text retained.

### Source reading and current gap (04:33 UTC)

- Saved arXiv:1704.05884v1 and v2 as extracted text. Read v1 Sections 2–3 in full (PDF pp. 8–14); Question 2.3 is p. 10 and Question 3.4 p. 13. Definitions distinguish transitive G_Delta from quasi-transitive Q_Delta.
- Saved and read principal theorem statements of Grimmett–Li 2020, regular-graph bounds 2015, height functions 2017, Lindorfer bridge theorem, Georgakopoulos–Wendland 2023, Panagiotis hyperbolic bounds, Gilch–Müller free products, Martineau, Grimmett–Holroyd–Peres, and Grimmett 2026 Grigorchuk bounds.
- October 2026 revision of arXiv:2608.19349, pp. 1–2 explicitly retains the general cubic question. Theorem 1.2 proves the bound for general 3-generator Grigorchuk graphs, strictly if the encoding contains all three symbols.
- Found additional 2026 papers: Grant–Li, arXiv:2601.12571 (local gadget transformations); Grimmett, arXiv:2611.00816 (SAW/trail pattern theorem). Neither principal result settles the full minimum problem.
- Nice wrapper reported setpriority denied because the process already inherits nice 10. Independently checked effective nice = 10. Use inherited nice for subsequent work.
- Candidate partial result: compute exactly the connective constant of K_m * K_2 (degree m), then prove its deficit from m is asymptotic to sqrt(m log m). This would rule out the proposed Delta-O(1) behavior, while leaving the true order of mu_min open. Free-product formula is published; no novelty claim for that formula.

### Proofs and enumeration (04:38 UTC)

- Derived the rational generating function (1+z)(1+M_m(z))/(1-z M_m(z)) for K_m*K_2, with M_m(z)=sum_{k=1}^{m-1}(m-1)_k z^k. Unique positive root z M_m(z)=1 gives its connective constant.
- Gaussian estimates around k approximately sqrt(m log m) prove mu(K_m*K_2)=m-(1+o(1))sqrt(m log m). This is a partial asymptotic obstruction, not an asymptotic formula for the infimum.
- Wrote exact C++ DFS and an independent explicit-path Python BFS; 32 graph cases completed, 1.3 seconds aggregate enumeration/check time. All n<=8 cross-checks, submultiplicativity, bridge supermultiplicativity, voltage-cover checks and free-product renewal counts passed. Python peak RSS about 25 MB; one worker at inherited nice 10.
- Cubic ladder c_30=6,656,290, ratio c_30/c_29=1.6180282695. The bridge counts are Fibonacci. Ratio is evidence only; exact phi comes from a proof.
- No cubic counterexample found. Finite graphs eventually have zero counts and are outside the question; no inference from their terminal ratios.

### Final audit (04:49 UTC)

- Final report status PARTIAL. Proved an explicit high-degree upper family with deficit asymptotic to sqrt(Delta log Delta); this refutes Delta-O(1), but leaves the minimum's actual asymptotics open.
- Checked the asymptotic a second way using the factorial ratio N!/(N-k)! and Stirling/Taylor expansion near the saddle k about N log(N/u). The Gaussian width sqrt(N) gives S about sqrt(N) exp((N-u)^2/(2N)), reproducing the log N balance. The report contains rigorous upper and lower inequalities rather than relying on this heuristic check.
- Corrected bibliography version pins against actual retained headers: regular bounds v2, height functions v5, free products v1. Downloaded the published 2020 cubic paper as text and checked theorem pages directly (4, 10–11, 15, 17, 25). Added 2024 Aubrun–Bitar and October/November 2026 results to the audit.
- Read the two-ended theorem with its infinite-path exception; did not silently apply its overbroad introductory wording to the degree-two line.
- Final computation: 35 test cases, 15 finite and 20 infinite (12 cubic infinite; some cases are isomorphic), one worker, nice 10. Peak Python RSS 26,951,680 bytes; enumerator child peak 1,818,624 bytes. Additional cases: line square to length 24 and cubic universal cover. The finite length-31 prism exactly matches the ladder through length 30.
- All checks in code/audit.py passed: 19 source texts, source hashes and version pins, report numbers, Fibonacci bridges, a second ladder count formula as a consistency check, independent renewal coefficient ratios through length 400 versus decimal roots, resource bounds, and no PDFs/images/scans in the directory.
- No publication, pushes, external messages, new agents or background daemons. Shared mesh/checklist/brain writes remained unavailable; durable mathematical conclusions are saved here rather than outside the authorized directory.
- Task complete as a partial research result: full D0070 and the unrestricted golden-mean conjecture are not claimed solved.
