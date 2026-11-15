# FEIB29 status

Completed the numerical attacks, class proofs, equivalence proof, and exact identification of the near-dictator asymptotic constant. REPORT.md gives the verdict first; PROOFS.md gives full derivations; RESULTS.md records the findings and commands.

PROVED: the summed B bound is equivalent to FEI, using parity translation and D<=2B. The near-dictator asymptotic supremum is exactly K_E=sup E/I, allowing infinity. It can be approached with B->0 and I,W1->1. Thus the requested unconditional theorem for all near dictators remains the full FEI problem.

PROVED class bounds: symmetric functions, bounded-arity read-once formulas/towers, and depth-d decision trees. Exact balanced and biased composition rules are included. The supporting parity comparison already occurs in the literature; no novelty claim is made.

CHECKED NUMERICALLY: 220 named family instances; 774 hill starts at n=6..12 with 10,884,992 proposal evaluations; 640,441 read-once monotone AND/OR formula shapes through n=14 counting dual roots. Best hill R=4.147284358433192 at n=12. Best stored table R=4.160114440563878217... at n=14. Best tested succinct tower R=4.505226154110238035... at n=531441. Full finite hex tables and exact tower circuit parameters are saved.

Audited all 774 hill champions and 308 leading formula shapes independently, plus 192 random identity controls and 48 bounded-depth trees. Independent 90-digit recomputation and directed 75-digit interval certificates agree. Peak recorded process RSS 862,896,128 bytes; one numerical process at a time, one thread, nice 10. All writes stayed in this folder. No subagents or external posts.

OPEN: FEI itself, finiteness/value of K_E, and a universal numerical B upper bound. No counterexample to boundedness was found. All deliverable computations are finished; no numerical process remains running.

NEXT: Owner/integrator to read REPORT.md and PROOFS.md. Any unconditional bound for arbitrary near-dictator error sets must overcome the proved reduction from unrestricted FEI.
