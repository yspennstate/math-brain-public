# C0047 prior-source normalization correction

2026-10-10. Verdict: FIX the attributed sufficient spectral criterion; keep the parent conjecture and its unresolved status separate.

Audited row: probability_1000_intake_claude_20260907/attempts.jsonl, line 37, attempt C0047-A001. Its result repeatedly describes a criterion pc<1/rho while explicitly taking rho to be the spectral radius of simple random walk. That is not the criterion in the named primary source.

Primary evidence: Benjamini-Schramm, Percolation beyond Z^d, 1996, Theorem 4, printed page 76, https://emis.de/ft/41630. The displayed hypothesis is "rho(G)kp < 1", where k is the maximal degree and the paper has defined rho using simple-random-walk transition probabilities. The associated sufficient threshold condition is k rho pc<1.

For a d-regular Cayley graph, A=dP, so alpha=||A||=d rho. The correct sufficient condition is pc alpha<1, equivalently pc<1/(d rho). It is a sufficient condition for the cited argument, not an equivalent characterization of C0047.

Why the omission matters: nonamenability gives rho<1, hence 1/rho>1. Since pc<=1, pc<1/rho then holds automatically and cannot distinguish the unresolved cases. On the 4-regular Cayley tree, rho=sqrt(3)/2 and pc=1/3: the omitted-factor condition passes, whereas the actual criterion has d rho pc=2sqrt(3)/3>1 and does not apply. The tree still has pc<pu; failure of this sufficient criterion does not refute the conjecture.

Replacement text for integration: For an infinite connected quasi-transitive graph of maximal degree k with simple-random-walk spectral radius rho, the Benjamini-Schramm 1996 Theorem 4 argument yields infinitely many infinite clusters at a percolating parameter p satisfying k rho p<1. In particular, k rho pc<1 is sufficient for pc<pu. In a d-regular Cayley graph this is pc||A||<1. Nonamenability alone implies rho<1, not k rho pc<1; changing the generating set proves a separate existential statement.

Independent referee: w554 requested; no second-account admission is claimed. No live intake row or store has been edited. The mathematical statement and its source normalization are the scope of this correction.

NEXT: Locate the precise store card holding C0047-A001, attach this source correction as DRAFT concept material, and obtain the required independent audit before replacing any served statement.
