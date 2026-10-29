# T067 q=4 second audit: an independent certificate for K >= 0 (agent C, 18 October 2026)

Checks Proposition 6.3 of `paper_draft_q4_d2_c259/main.tex`: K(a,b;m) >= 0 for a, b in rho(4 Delta - 1),
0 <= m <= M. Written from the paper text only; the author's `indep_cover.py` was not read.

| file | what it does |
|---|---|
| `kfeat.py` | K from Table 2, Appendix A and the definitions of H, N, J, s (lines 101 and 127), in exact rationals. Every phi_j, every g_j numerator and denominator, and both forms of g_24 were checked line by line against main.tex. |
| `cert.py` | per cell, builds G = K P^5 Q^5 S^3 = 64 P^8 Q^8 K s^3 as an exact polynomial in the 8 cell variables (python-flint), compares it with direct rational K at a random interior point for both m, then for each m takes the first (gamma, e) in (0,1), (0,2), (1/3,1), (1/3,2) for which every coefficient of (G - gamma Sigma_1 P^5 Q^5 S^3)(UV)^e is >= 0, and runs the g_24 control (shift 1743/480965 replaced by -1/10) at that (gamma, e). |
| `tally.py` | counts the results in `cert_out.jsonl` |
| `g24_ctrl.py` | random-point search for where the g_24 control makes K negative; misses the vertex minimum (output `g24_ctrl_out.txt`) |
| `g24_vert.py` | the same over scaled cell vertices with every permutation of b (output `g24_vert_out.txt`) |

Cells: 24 permutations of b's sorted coordinates x {z_0 >= z_3, z_3 >= z_0} x {w_0 >= w_3, w_3 >= w_0}, and m in {0, M}:
192 cases, as in the paper. K is affine in m, so the two values of m cover [0, M].

Results (18 October, 01:01-01:10, `cert_out.jsonl`, one line per cell):
- All 192 cases certified: every coefficient nonnegative for the first (gamma, e) tried that works.
- The direct-K spot check agrees exactly in all 96 cells, at both m.
- gamma = 0 in 168 cases and gamma = (1/3,0,0,0) in 24; e = 1 in 176 and e = 2 in 16. These are the paper's counts.
  The 24 gamma cases are the cell z_3 >= z_0, w_3 >= w_0 at m = 0, once for each permutation.
- Control 1: in each of the 24 gamma cases, gamma = 0 leaves a negative coefficient at e = 1 and at e = 2
  (minimum about -1.02e107 in every one). In each of the 16 cases with e = 2, e = 1 leaves a negative coefficient.
- Control 2: with the g_24 shift 1743/480965 replaced by -1/10, a negative coefficient appears in 96 of the 192
  cases (24 at m = 0, 72 at m = M). The modified K is itself negative there, so no certificate could pass: at
  m = M, a = (-12863/29000)(1, 1, 1, -3) and b = a with coordinates 3 and 4 swapped (a scaled cell vertex with b
  permuted; agent H's point), exact rational arithmetic gives K = 1.1952 with the paper's shift and
  K = -1.1136 at -1/10. `g24_vert.py` (K is affine in g_24) searches scaled cell vertices with every permutation of
  b: min K/phi_24 = 0.0460, at m = M, so K < 0 once the shift is below about -0.042. A random search over 1,500
  interior points (`g24_ctrl.py`, min 0.1123) misses this corner, because the minimum sits at a vertex with b in a
  different chamber from a.

Verdict: Proposition 6.3's certificate is reproduced from the paper's own tables, with its stated (gamma, e)
counts, and both of its controls behave as the paper says. The g_24 control is a statement that is actually false (K < 0
at a point of the domain), and the certificate fails on it.
