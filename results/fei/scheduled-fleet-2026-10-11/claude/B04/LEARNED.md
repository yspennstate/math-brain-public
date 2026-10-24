# B04 lead - learned (append, dated)

## 2026-10-11 23:25 UTC (run 20261011T224500Z-claude-B04-sharp-selector-debt)
- The selector debt splits as Delta=M_W+B_W (threshold Prop 8.6). M_W<=(2/ln2)I_W always and telescopes along any tree; it is never the obstacle. Spend effort on B_W only.
- B_W<=|W|h2(I_W/|W|) is one line (subadditivity plus concavity) and is first-order sharp with M_W: tensor bent splices give Delta=I_sel(m+3/ln2)-O(I_sel^2). Selector-only routes are now fully priced; do not try another one.
- At a one-bit node the log factor is exactly an edge-isoperimetry fact: d log2(1/d)<=2I(D), D the half-difference. The bent splice is the extremal case because a single point is edge-isoperimetrically optimal.
- Where the selector mass sits decides everything: level-one mass (bent splice) costs log2(1/I_sel) per unit; high-level mass (A019 point modules) costs O(1). Same mechanism as FEI itself.
- Charging the boundary at every node of a fixed order costs the second moment sum C(|S|,2)fhat^2. Adaptivity or the exact B_W (parity / KL credit) is the only way forward on this route.
- Process: the harness refused REPORT.md from this Claude subagent ("subagents should return findings as text"); the report text went into the structured output for the coordinator to persist. Plan for that from the start next stage.
- Codex checks this stage: A016, A017, A018, A019 all hold at their stated scope; A017 and A018 are baseline reconstructions, A019 is a narrow genuine extension.
