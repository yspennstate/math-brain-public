# Exact C0029 prior digest

The ranking row is RANKING_2026-09-07.csv:428: tier 4, attempted_un, Spielman-Teng constant one. It is historical, not a certification of openness.

The original intake record is probability_1000_intake_claude_20260907/problems.jsonl:29. It asks for P(sqrt(n)*s_min(X)<=t)<=t+c^n for independent symmetric signs, all large n and small t. Its 2026-09-07 scope note already distinguishes Sah--Sahasrabudhe--Sawhney's 1+o(1) result from exact coefficient one. Primary arXiv:2405.20308v2 equations (2)--(4) confirm that distinction. I have not certified the absence of every later solution; current exact openness remains UNKNOWN.

The substantive predecessor is attempts.jsonl:23, attempt_id C0029-A001. It tries Gaussian comparison. It correctly identifies the polynomial-versus-exponential scale gap, and claims no improvement. However, its key_identity and opening result call the limiting real Gaussian law a finite-n exact law. This is false: for n=1, sqrt(n)*s_min(G)=|Z|, so its CDF is erf(t/sqrt(2)), whose derivative at zero is sqrt(2/pi)<1, whereas the claimed formula has derivative 1. Tao--Vu arXiv:0903.0614 Theorem 1.1 explicitly gives a fixed-parameter asymptotic law. Furthermore, Gaussian stochastic domination is sufficient for the target but stronger than its stated t+c^n envelope.

The read-only population store contains the same error in logical node math:probability.random-matrices:attempt-c0029-spielman-teng-conjecture-on-the-least-singular-value-of-bernoulli-matr, id claim_cbd6e1bc44ea67c88a3ad2112abab63bbfcf63f991be2eeccb063fdba514f1fa. Its body and provenance are saved in evidence/store_retrieval.json. Proposed correction preserves the historical author and unresolved result; it changes only the mathematical scope and adds the current primary comparison.

Targeted C0029/Spielman-Teng searches returned no additional matching attempts in the specifically named H_20260912 and I_20260914 attempt directories. The Lean collection's ranked annotation repeats the target but supplies no C0029 theorem or formal-check receipt. This is a bounded search report, not evidence that no proof exists elsewhere.

Team O board has no C0029 row. The probability300 board assigns C0029 to w564--w575; this triad is w573/w574/w575. w574 independently pursues Gaussian rescaling direction and an unconditional third-moment obstruction. This packet instead treats Gaussian-CDF slack, an abstract relative-error counterexample, and an exact Schur row-event identity. Neither route will be presented as a new solution.

NEXT: Referee checks the new exact row-event identity and the scoped finite-n Gaussian correction; the signed Bernoulli probability bound remains open in this packet.
