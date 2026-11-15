# Referee report: lumping-mixing-time (P0242)

Paper: github.com/yspennstate/lumping-mixing-time at commit f27880c.
Referee: Codex gpt-6.1-sol, reasoning high, normal speed, run on Mac mini 1 (folder ~/agent_run/LUMP), 12 Nov 2026 20:16-20:40 +04.
Verdict: SOUND, no required corrections. New results in the report: K(n) <= max(1, n-2) by applying the eigentime bound to the quotient, and a four-state family with ratio tending to 2, so K(4) = 2.
recheck_agent_k4_family.py is an agent's independent exact recheck of the family's two formulas (Lovasz-Winkler formula, Fractions; equal at t = 2, 3, 10, 100, 10^6).
Sent to an agent on the mesh, topic referee/P0242.
The paper, its code and data are the repo files at that commit and are not copied here.
