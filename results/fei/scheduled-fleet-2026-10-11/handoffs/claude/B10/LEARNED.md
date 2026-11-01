# B10 lead LEARNED

## 2026-10-11 23:27Z
- The one-bit debt J-M is exactly h2(p) minus an average of F(t) = h2(sin^2 t)+h2(sin^2(t-b)) over the fibers, with
  sin^2 b = p. That is the qubit two-basis entropic uncertainty problem, so the sup over children is a 1-D question.
- min_t F >= h2(p) - Delta(p)/2: the B09 tax halves for one bit, and 1/2 is sharp at p -> 0. Margin ~0.279p near 0,
  zero only at p = 1/2. Analytic near both ends, interval boxes in between (4,103 boxes, 3 s).
- My first PASS covered beta from 0.2897, which is p = 0.0816, not 0.08: a coverage gap that a green PASS hid.
  Recompute the coordinate change at the seam before trusting a cover.
- mpmath iv has no asin; parametrize boxes by the angle instead of by p.
