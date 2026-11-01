## 2026-10-11 23:36 UTC (claude B02 lead)
- thm:posteriorforest takes f = h_1 with N = 1: the root normalization v(Lambda + log Z) and the root rarity v b cancel to
  zero for every pi. What is left is a pure rank inequality; with one order it is sum_j Inf_j ln r(j) - E ln|A|!.
- Tribes separates one gate from many: every single-gate table loses log m, the block forest stays near K_ref + 3.2.
  Gate costs must be paid per used gate per set, not per coordinate.
- Tribes closed forms worth reusing: P(A) = 4 q^{2(m-k)} 4^{-wk}, I = 2mw q^{m-1} 2^{-w}, E k = 4m q^m 2^{-w},
  H = -P0 log P0 - 2v(1 + m log q) + 2 E k (w + log q). H/I -> 4 at m = 2^w.
- Tool note: long shell heredocs failed to parse; writing files in chunks under 4 KB worked.
