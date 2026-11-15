---
name: t104_note_what_is_ours_and_what_is_bacher_alon_kozma_2026_11_12
description: "T104 (Alon 2/3 conjecture) not solved; in our note the hook spectrum, the sign case and the star values n-2, n-1 are Bacher / Alon-Kozma, ours are the k/j hook constant, n=4, the two-eigenvalue family; single-eigenvector state fails at n=5"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T00:13:38+02:00
  status: provisional
  evidence: "T104_NOTE.md and STATE.md in 06_math_research/t104_alon_agent_2026_11_11, brain repo commit b715de397052; Alon-Kozma arXiv 1003.1710v2 read; Codex referee report AUDIT_CODEX_NOTE_REPORT.md"
---

Row T104 (Alon's Conjecture 1.5, arXiv 2610.22151: lambda_min(G, tau) >= (2/3) lambda_min(G, sigma) for sigma
dominating tau, every weighted graph) is NOT solved. What exists is a note of partial results,
06_math_research/t104_alon_agent_2026_11_11/T104_NOTE.md in the brain repo, not posted anywhere.

What the citation pass of 12 Nov found already published, so never present it as new:
- Hooks: the spectrum on [n-k, 1^k] is the k-fold sums of the spectrum on [n-1, 1] (Bacher, J. Algebra 167 (1994)
  460-472); Alon-Kozma (Canad. Math. Bull. 56 (2013) 13-30, arXiv 1003.1710, Appendix A) identify Bacher's exterior
  powers with the hook Specht modules and deduce the chain [n-1,1] > [n-2,1^2] > ... > [1^n].
- tau = [1^n]: Alon-Kozma Corollary 2 (lambda_1 on the sign representation is twice the total weight).
- The star values n-2 on [2,1^(n-2)] and n-1 on [2,2,1^(n-4)]: Alon-Kozma Corollary 1 (that pair is not comparable
  in the Aldous order). So the constant (n-2)/(n-1) of our Conjecture F cannot be raised.

What stays ours after that reading (one Codex referee, gpt-6.1-sol high; partial Lean and numeric checks by
an agent): the dual form of the comparison (Prop. 2.1); the constant k/j between hooks; n = 4 with constant
2/3 (Theorem 4.2; the scalar bound is a Lean proof, the representation step is not formalised); for the pair
[2,1^(n-2)], [2,2,1^(n-4)] the comparison with constant (n-2)/(n-1) on graphs whose Laplacian has two distinct
nonzero eigenvalues patterns (Theorems 5.2, 5.3; Lemma 5.4 needs n >= 5); the finite certificate for n = 5..13,
reproduced by the referee.

A dead route, recorded so it is not walked again: the state A A^*/tr(A A^*) built from the top eigenvector does NOT
satisfy the dual inequality transposition by transposition. n = 5, x = (1,1,0,0,-2)/sqrt 6, transposition (1 5):
1/2 against 13/24 (fails by 1/24; also at (2 5)). It holds only after summing against the graph's weights. Script
state_check_n5.py in the folder.

Method lesson: before calling a lemma about S_n Laplacians new, read Alon-Kozma and Bacher; the first draft of the
note had three unattributed statements that were theirs, and a word search of the source paper alone did not show
it. The source paper's own reference list is where the overlap was.

Would change this: a line-by-line reading of the five 2024-2026 follow-ups (checked by abstract only), or a proof
of Conjecture F for general graphs at n = 5.

