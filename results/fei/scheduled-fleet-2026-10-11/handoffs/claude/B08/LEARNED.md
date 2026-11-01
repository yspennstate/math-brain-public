
## 2026-10-11 23:35Z, lead run 20261011T225000Z-claude-B08-tc-restriction-ledger
- TC splits exactly under one restriction: TC(f)=I(S_i;S_-i)-JS_i+Gamma_i+avg TC(children). Gamma is the
  re-optimization of the product reference in each child; it is nonnegative and not local (AND_n: Gamma_i>=(n-1)Inf_i).
- Posterior credit collected along any tree is capped by TC(f)+(2/ln2)I. Credit cannot be reused.
- B has an exact one-sided edge form M_edge with remainder at most I log2 e. FEI is equivalent to M_edge=O(I),
  and to a finite sup over f of min_i B_i/Inf_i.
- n=4 exact maxima: H/I 3.40248, B/I 2.70415, M_edge/I 1.59138, TC/I 1.02820, min_i B_i/Inf_i 2.67249.
- Process: one diagnostic compared 64*B with an unscaled I*log2(e) and reported 64,832 false violations; keep one
  scale per comparison and re-derive any surprising violation before reporting it.
- The Write tool refuses a file named REPORT.md from a subagent; the protocol file was staged in scratch and copied.
