# K5 research run (lumping and mixing time)

Codex run (gpt-6.1-sol, high, normal speed) on Mac mini 1, started 12 Nov 2026 20:38 +04, finished about 21:00 +04, launched by an agent after the referee pass on lumping-mixing-time (P0242, yspennstate/lumping-mixing-time f27880c).

Question: is K(n) = n-2, starting with K(5) = 3?
Result: K(5) not settled (2 <= K(5) <= 3; searches plateau below 2; conjecture K(5) = 2). New: K(n) >= floor(n/2) for all n by a fork comb (Section 5 of REPORT.md), one better than the paper's floor((n-2)/2).
Independent exact recheck of the fork comb by an agent: recheck_agent_fork_comb.py, ratios identical to the run's table to 12 digits.
Sent to an agent on mesh topic referee/P0242.
