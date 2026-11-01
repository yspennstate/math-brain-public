# T353 sub-1 Renyi certificates (REFUTATION_T2.md, "Orders 1/4, 1/2 and 3/4"), audit 2 (agent C, 20 Oct 2026 03:0x)

Objects: the nine certificates (sigma 0.5, 1, 2 x orders 1/4, 1/2, 3/4, direction P||Q), the duality J_PQ(al) = J_QP(1 - al),
and the claim that the adaptive method beats the pair "in both directions".

Verdict: all nine certificates CONFIRMED with my own code and my own tail bound. The duality holds. One statement needs a
correction of wording, which does not touch the refutation: at orders 1/4 and 3/4 the two directions of the pair differ, and
only one orientation of the adaptive method beats their maximum (below).

## Own code (sub1_cert_C.py, run_sub1_C.sh, sub1_run1.txt)

- Model re-derived from "The construction" in the note's own shifted g1 coordinate, not from cert_renyi_sub1_arb_sigma.py:
  x: B -> N(g1;-2)N(g2;0), not B -> N(g1;0)N(g2;a); x': B -> N(g1;-1)N(g2;0), not B -> N(g1;0)N(g2;c); (a, c) = (2, 1) ANTI,
  (0, -1) SAME. Their script works in g1 + 1 with per-branch g2 shifts; a g2 shift common to p and q at fixed g1 changes
  nothing, so their [u, v] is my [u - 1, v - 1]. Checked by matching point values: J_ANTI - J_SAME at my -2.25 (their -1.25)
  is 2.19e-4 at order 1/2, and -0.00744 at my -1 (their 0), the note's mpmath values.
- Integral: Arb acb.integral (rigorous Gauss-Legendre; pow with analytic=True, so a branch cut touching the path is refused)
  on g2 in [-L, L], L = 12 sigma + 4, with g1 entering as an arb ball, so each enclosure holds for every g1 in the ball.
- Tail, not the note's subadditivity/Mills bound: weighted AM-GM, p^al q^(1-al) <= al p + (1-al) q, and every g2 centre has
  modulus at most 2, so the mass beyond L is at most (total weight) 2 Phibar((L-2)/sigma). It is below 1.3e-39 everywhere.
- 400 balls at sigma 1 and 2 (the note used 200), 40 at sigma 0.5.

| sigma | order | interval (note's coords) | min lower end (mine / note) | int(J_ANTI - J_SAME) >= (mine / note) |
|---|---|---|---|---|
| 1 | 1/4 | [-1.3, -1.2] | 1.19e-4 / 8.35e-5 | 1.30e-5 / 9.42e-6 |
| 1 | 1/2 | [-1.3, -1.2] | 1.77e-4 / 1.43e-4 | 1.85e-5 / 1.52e-5 |
| 1 | 3/4 | [-1.3, -1.2] | 1.20e-4 / 9.22e-5 | 1.24e-5 / 9.57e-6 |
| 2 | 1/4 | [-2.05, -1.95] | 1.34e-4 / 1.21e-4 | 1.36e-5 / 1.23e-5 |
| 2 | 1/2 | [-2.05, -1.95] | 1.85e-4 / 1.73e-4 | 1.87e-5 / 1.74e-5 |
| 2 | 3/4 | [-2.05, -1.95] | 1.36e-4 / 1.24e-4 | 1.37e-5 / 1.25e-5 |
| 0.5 | 1/4 | [-1.250001, -1.249999] | 1.79e-8 / 1.79e-8 | 3.59e-14 / 3.59e-14 |
| 0.5 | 1/2 | same | 3.25e-8 / 3.25e-8 | 6.50e-14 / 6.50e-14 |
| 0.5 | 3/4 | same | 1.68e-9 / 1.68e-9 | 3.35e-15 / 3.35e-15 |

No ball failed. Mine are larger at sigma 1 and 2 only because my balls are half as wide; at sigma 0.5, with the same 40 balls,
every printed digit agrees. Duality: the QP runs at sigma 1 reproduce the PQ lines with the order flipped, digit for digit
(QP 3/4 = PQ 1/4: 1.19e-4 / 1.30e-5; QP 1/4 = PQ 3/4: 1.20e-4 / 1.24e-5)
(each pair of lines is the same integral, int q^al p^(1-al) read from the other side).

## "Both directions": what holds (sub1_max_check.py, sub1_max_check.txt; float quadrature, row by row)

The pair's two directions are equal at order 1/2 but not at 1/4 and 3/4. At sigma 1:

| order | pair P||Q | pair Q||P | adaptive x||x' | adaptive x'||x |
|---|---|---|---|---|
| 1/4 | 0.10765 | 0.11123 | 0.10768 (below the max) | 0.11126 (beats the max) |
| 1/2 | 0.21890 | 0.21890 | 0.21895 | 0.21895 |
| 3/4 | 0.33370 | 0.32296 | 0.33377 (beats the max) | 0.32303 (below the max) |

The same pattern holds at sigma 2 and 0.5. So each orientation beats the pair in the SAME direction (that is what the
certificates prove), and against max(D(P||Q), D(Q||P)) the winning orientation is x'||x at order 1/4 and x||x' at 3/4. Under
either reading of dominance the refutation stands at every certified order: at 1/4 the max is Q||P and x'||x against Q||P is the
QP certificate at 1/4 = the PQ certificate at 3/4; at 3/4 it is the PQ certificate directly. The note should say which
orientation beats the max at 1/4 and 3/4, rather than "both directions". The gap between P||Q and Q||P (3.6e-3 at sigma 1) is far
above the quadrature error, so identifying the max needs no certificate of its own.

## Not covered
Orders above 1 and KL (other audits), sigma other than 0.5, 1, 2.
