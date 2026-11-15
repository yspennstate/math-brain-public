---
name: fei_monotone_tower_record_4506428_near_critical_dmk_2026_11_10
description: "FEI monotone tower record beyond FEIB31? Yes: M,D^8,PM(K4,4),D,D,dual T(4,3),T(3,5),T(3,5) = 4.506428465445 (depth 15, two methods, 40 digits); D,M^8,dual PM(K4,4),M,M,T(3,5) = 4.5064284629; pinned M-tower target 4.5064554627; rank only in extended precision (10 Nov)"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T18:26:06+02:00
  status: verified
  evidence: "06_math_research/fei_solve_2026_11_09/referee_r9/REFEREE.md"
---

The monotone FEI tower record moves from FEIB31's 4.506400645515568 to 4.506428462939128775 (40-digit mpmath, 10 Nov 2026,
an agent while refereeing round 9). The word, bottom to top, is D,M^8,dual(PM(K4,4)),M,M,T(3,5), where M = perfect
matching on K3,3, D = its dual and T(w,s) = OR of s disjoint width-w terms. Plain words already pass the old record:
D,M^12 = 4.506428305525435 (3^25 variables) and D,M^10,T(3,6) = 4.506428343578881.

Update 18:3x: the depth-15 beam word M,D^8,P,D,D,dual T(4,3),T(3,5),T(3,5) gives 4.506428465445233 in 40 digits (beam15_mp.py), the best value now.

Mechanism: D's output mean (-0.03516) sits next to M's unstable fixed point (-0.03492), so stacking M on top lets the mean
drift away slowly (its distance roughly doubles per level). The ratio climbs while the mean drifts and falls once the mean
nears -1; D,M^k peaks at k = 12. Pinning the mean exactly at the fixed point makes the M tower converge to 4.5064554627
(40 digits, an agent's pinned.py; my double-precision critical.py read 4.5064554516, 1.1e-8 low; a first run pinned at
+0.0349 by a sign slip and read 4.49769, void). The pinned value depends on the start state, so it is a target, not a bound. So the gain IS
criticality, and the drift off the fixed point is what loses it: a bottom word whose mean lands closer to -0.0349185 keeps
more levels critical, and 4.5064555 is the target for this family.
A beam search over nine gates to depth 14 gains about 6e-9 per extra level near 4.5064285, so this family looks close to its
ceiling.

Method: the composition recursion of [[fei_monotone_tower_record_4506400_confirmed_independently_2026_11_10]] (checked
against full Walsh transforms on 12-16 variables). Double precision drifted 6.5e-10 on the 13-level word, so quote only the
40-digit values. Second method, 10 Nov 18:29: an agent's separately derived recursion (fei_papers_agent/p2/code/record.py, brute-force
checked on 444 coordinates) agrees on D,M^8,dual P,M,M,T(3,5) and D,M^12 to every digit, and on FEIB31's record to 33 digits.
Status: both words are confirmed by two methods; the depth-15 word M,D^8,P,D,D,dual T(4,3),T(3,5),T(3,5) =
4.506428465445233177909 agrees to 3.9e-25 (10 Nov 19:1x). Double precision is off by 3.8e-9 on it, more than the gap between
the two words: rank towers only in extended precision.
Interval certificate: done 10 Nov 20:2x, see the last paragraph.
Files: 06_math_research/fei_solve_2026_11_09/referee_r9/ (dmk_mp.py/.log, beam.py/beam_best.json, beam_mp.py/.log,
critical.py, REFEREE.md). A finite record is a lower bound for the monotone constant, not evidence that it is finite.


Independent check (an agent, 10 Nov 19:16): a from-scratch leaf-ratio recursion (own encoding, own FWHT and superset
transform, 50-digit mpmath) reproduces all five claimed tower values to every printed digit, including the record word
D,M^8,dual PM(K4,4),M,M,T(3,5) = 4.506428462939128775 and FEIB31 4.506400645515568. That makes the record confirmed by a
second method. Checks the arithmetic, not minimality of the leaf or any supremum. Files:
06_math_research/fei_solve_2026_11_09/audit_agent/ (LEAF_RATIO_REFEREE_2026_11_10.md, fei_leaf_referee.py/.json).

Interval certificate (10 Nov 20:2x, an agent): 06_math_research/fei_solve_2026_11_09/interval_cert_agent/CERT.md. Outward-rounded 60-digit mpmath intervals through the same recursion enclose the record word M,D^8,P,D,D,dual T(4,3),T(3,5),T(3,5) at 4.50642846544523317790928639 (width 1e-48) and D,M^12 at 4.50642830552543541 (width 2e-51); both lower ends beat FEIB31 4.5064006455 by 2.8e-5. Rigorous for the recursion; the recursion itself rests on referee_r9/REFEREE.md. Also D,M^8,dual PM(4),M,M,T(3,5) at 4.50642846293912877531 (width 8e-51), beats FEIB31 by 2.78e-5. Gate names: Pd = dual PM(4) (not dual PM(K4)) - read the gate dict in beam_mp.py before relabelling a word.
