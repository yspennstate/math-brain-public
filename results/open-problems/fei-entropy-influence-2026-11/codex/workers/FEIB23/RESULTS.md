# FEIB23 results

Final state: the census and partial theorems are complete and audited; the universal theorem is mathematically blocked. REPORT.md is the final handoff. Source assumptions: ../../RULES.md, BRIEF.md, and section 12 of ~/fei_solve_agent/workers_in/FEIB21/PROOFS.md. That section supplies the uniform-width sparse certificate; it does not resolve arbitrary linear monotone DNFs.

The fleet-specific instruction to write only in this folder supersedes the global mesh, checklist, and memory-write routine. Durable findings will be left in REPORT.md for the launching session.

Recall attempt: `env MATH_STRENGTH_NOLOG=1 PYTHONDONTWRITEBYTECODE=1 BRAIN_RECALL_REFRESH=0 nice -n 10 python3 ~/.claude/dreaming/math_recall.py 'Fourier entropy influence linear DNF read-k' --or 'bounded width monotone DNF FEI' --limit 4 --chars 7000` returned `math store not found`. The nice wrapper also printed a setpriority error; process niceness will be checked before census work.

The inherited process niceness is already 10 (`os.getpriority` and census JSON). Subsequent work does not redundantly add another 10. Census uses one thread.

The recall configuration was recovered from ~/.claude/settings.json. A successful read-only recall is saved in math_recall.txt, and a whole-card read in math_width_card.txt. It surfaced an older provisional bounded-width argument; PROOFS.md section A gives a shorter independent proof using Parseval and a minterm forcing bound. The old manuscript is not being treated as published literature.

First exhaustive census: census8.json has one representative for each isomorphism class of linear monotone DNFs on each essential dimension through eight. census8.families contains the eight-variable representatives. Integer Walsh transforms precede logarithms. The subsequent audits and rigorous logarithm certification are recorded below.

The census audits now pass. The two eight-variable labeled counts are both 18,785,639,553 (census8.labeled_check.json), obtained respectively by pair-clique recursion and by orbit–stabilizer summation. The census has 552,251 essential eight-variable classes. Rigorous log intervals in census8.certified.json separate both unique maximizers from all other classes:

- max H/I is between 3.88910541981418 and 3.88910541981709 bits per unit influence, attained by four singleton terms disjoint from the four edges of a cycle on the remaining variables.
- max min_i E_i/Inf_i is between 3.30470132244542 and 3.30470132245649 bits per unit influence, attained by two disjoint four-cycles.

For the latter, H/I=3.61251754586310 and the minimum decision-tree erasure average is 1.95247893210097; a whole-term shortest-term tree gives 1.96295819472637. For the entropy maximizer, the optimum and the tested term trees give 2.09159755870216. These tree values are floating logarithmic evaluations, independently checked against H=sum(E+J) and I=sum Inf. Source: analysis.json, command `python3 analyze.py`.

PROOFS.md now proves (SHORT), the mixed-width certificate (MIX), the single-term load criterion (LOCAL), and the quantitatively extreme-bias bound (BIAS). The arbitrary-width universal theorem remains unproved.

Final precision audit: final_audit.json and exact_values.json independently evaluate every attainer's exact prime-log expression. The final certificate uses 2^-52-bit logarithm enclosures and outward nextafter rounding after floating conversion and division. This catches small summation errors in the initial long-double decimal values. The final eight-variable maxima are approximately 3.889105419815329603 and 3.304701322451451121, respectively; both lie inside census8.certified.json's final intervals.

The full twenty-five-variable transversal computation and whole-term tree are finished: H/I=3.879971688716, min E/Inf=2.200337307740, and tree erasure average/I=2.185292568539 (TD_5_5.json, `./structured 5 5`). The tree has 1,090,967 nonterminal nodes, with the weighted influence sum matching I. The largest recorded resident size is 372,736,000 bytes.

The transversal obstruction in PROOFS.md section F proves that all the local certificates here can fail uniformly even when the function tends to a constant. It does not prove divergence of the actual erasure ratio, tree average, or H/I. This is the precise remaining block, rather than a claimed refutation of FEI.
