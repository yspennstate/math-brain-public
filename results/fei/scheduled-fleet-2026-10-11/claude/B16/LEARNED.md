# B16 LEARNED (append only)

## 2026-10-11 23:27Z, run 20261011T225600Z-claude-B16-retained-kl-sandwich
- The retained-KL charge Q_v = sum_T m_T log2(q_T/m_T) is pinned to the entropy drop at every node: Q_v + M_v <= B_v <= Q_v + M_v/ln2 (lower constant from concavity of -(1-r)ln(1-r) on [0,1/2]), and Q_v <= Delta_v <= Q_v + 3M_v/ln2. Telescoped, any tree's Q_T differs from H(f) - E H(leaf) by at most (3/ln2) I. A Q-based tree target is FEI itself; testing Q/I on bounded-H/I families is wasted compute.
- Odd majority is the clean scalable family for the child-kappa charge: Lambda_T/I about (1/2)log2 n - 1.4 (n to 513), H/I <= 2.83. Only s=0 splits are isospectral and they carry about 1.25/sqrt(n) of the influence, so the isospectral skip does not help. Any (epsilon, kappa_min) majorant of B fails on complete trees.
- Rigorous kappa bound for any Boolean c: kappa(c) >= 1 - max(chat(empty)^2, max_j Inf_j(c)), because chat(S)^2 <= Inf_j(c) for j in S. It turns Lambda lower bounds into exact rational node arithmetic.
- Negative controls matter: wrong constants (B - Q <= 0.5M/ln2, JS <= M/ln2, Delta - Q <= 2M/ln2) trip at n = 3, 4; one control I labelled false (B >= Q + 0.01M) was in fact true, which is how the sharper lower constant Q_v + M_v <= B_v was found.
- The subagent harness refuses a Write of a file named REPORT.md; record the protocol report in CLAIMS.json proof_source and in the StructuredOutput, and name the blocker in PROGRESS.json.
- A Bash heredoc that contains an apostrophe inside double-quoted Python strings failed to parse in this shell wrapper; write scripts with the Write tool.
