# B06 lead - learned

## 2026-10-11 (run 20261011T223800Z-claude-B06-block-tree-reductions)
- Blocks reduce to singletons at the same node (chain rule plus conditioning), and every tree ledger is a function of the leaf
  partition. Before reviewing any B06 stopping or transport claim, ask which leaf partition it uses and whether Pi_H <= K Pi_I holds there.
- The amplitude proxy A_i = 2 sum |fhat(T) fhat(T+i)| overstates true erasure: 7/2 against 2.6725 at n = 4, and 4.137 against 1.815 at
  the n = 32 threshold witness. A proxy no-go says nothing about B_i.
- The true small-n erasure constant peaks at the 3-bit point defect, not at the asymptotic point-defect family (which tends to 2).
- Identifying a spectrum class by its sorted squared coefficients is not enough: a point defect times a parity has the same sorted
  multiset. Pin the large coefficient's position (it must be at the empty set). The first strict-separation run skipped 32 classes
  instead of 4 because of this.
- In this harness a subagent cannot write REPORT.md (the Write tool refuses report files). Return the report text in the structured
  output, save the JSON records, and name the blocker in PROGRESS.json.
- Long bash heredocs with nested quotes failed to parse; write code files with the Write tool and keep shell commands short.
