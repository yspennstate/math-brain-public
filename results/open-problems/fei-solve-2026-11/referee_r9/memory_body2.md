The monotone FEI tower record moves from FEIB31's 4.506400645515568 to 4.506428462939128775 (40-digit mpmath, 10 Nov 2026,
an agent while refereeing round 9). The word, bottom to top, is D,M^8,dual(PM(K4,4)),M,M,T(3,5), where M = perfect
matching on K3,3, D = its dual and T(w,s) = OR of s disjoint width-w terms. Plain words already pass the old record:
D,M^12 = 4.506428305525435 (3^25 variables) and D,M^10,T(3,6) = 4.506428343578881.

Mechanism: D's output mean (-0.03516) sits next to M's unstable fixed point (-0.03492), so stacking M on top lets the mean
drift away slowly (its distance roughly doubles per level). The ratio climbs while the mean drifts and falls once the mean
nears -1; D,M^k peaks at k = 12. Pinning the mean at the fixed point gives only 4.49769, and the balanced M^k tower stops at
4.47415. The gain comes from near-critical lower layers under increasingly biased upper ones, not from criticality itself.
A beam search over nine gates to depth 14 gains about 6e-9 per extra level near 4.5064285, so this family looks close to its
ceiling.

Method: the composition recursion of [[fei_monotone_tower_record_4506400_confirmed_independently_2026_11_10]] (checked
against full Walsh transforms on 12-16 variables). Double precision drifted 6.5e-10 on the 13-level word, so quote only the
40-digit values. Status: provisional. No second method has recomputed these numbers yet, and none can by brute force at
these sizes. What would confirm: an independent referee's recursion or an interval certificate on the same word.
Files: 06_math_research/fei_solve_2026_11_09/referee_r9/ (dmk_mp.py/.log, beam.py/beam_best.json, beam_mp.py/.log,
critical.py, REFEREE.md). A finite record is a lower bound for the monotone constant, not evidence that it is finite.
