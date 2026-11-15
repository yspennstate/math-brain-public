---
name: i0031_aldous_fill_7_31_tau0_resolved_by_markowsky_koolen_2010_2026_11_08
description: "[VERIFIED] I0031 Aldous-Fill Open Problem 7.31 (tau_0=O(n) on distance-regular graphs, not cycles) is answered in print: Markowsky-Koolen EJC 17 (2010) #R78 Prop 3, H_uv <= 2(n-1); tau_0 <= (195/101)(n-1); no paper of ours; tau_2=O(log n) part open"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T04:15:30+02:00
  status: provisional
  evidence: ""
---

Aldous-Fill Open Problem 7.31 asks whether tau_0 = O(n) over distance-regular graphs other than cycles. It is settled: G. Markowsky and J. Koolen, A conjecture of Biggs concerning the resistance of a distance-regular graph, Electron. J. Combin. 17 (2010) #R78, doi 10.37236/350. Theorem 1: for degree k>2, max resistance d_D <= (195/101) d_1, equality only for the Biggs-Smith graph. Proposition 3: H_uv <= 2(n-1), C_uv <= 4(n-1). With d_1=(n-1)/m (Foster plus equal edge resistances) and C=2mR=2H, max H <= (195/101)(n-1), hence tau_0 < 2(n-1). Checked 8 Nov 2026 against the paper's own text (pages 1 and 13). The side question tau_2 = O(log n) is NOT settled there (their Prop 5 gives only tau_2 <= 4(n-1)); hypercubes and odd graphs give O(log n); finitely many DRGs per degree k>=3 (Bang-Dubickas-Koolen-Moulton 2015), so only k->infinity families matter.

**Why:** the papers-and-repos loop (T-20261107-015) must not write a paper claiming this; it is a literature resolution. Found by a Codex worker on acc4 (rollout 01a1b8b1) whose workspace-write sandbox on Windows refused every file write and whose turn then died on 'workspace routing discovery timed out' - the finding survived only in the rollout.

**How to apply:** mark I0031 literature-resolved in any open-problem list; cite Markowsky-Koolen Prop 3. When launching a Codex worker that must write files on this laptop, check its sandbox can write (or read the result from the rollout). Record: brain_math_loop_1e0a/papers1107/I0031_codex/LITERATURE.md.
