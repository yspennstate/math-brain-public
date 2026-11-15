---
name: p0245_second_basin_is_kn_minus_an_edge_2026_11_10
description: "[PROVISIONAL] P0245 searches stop at a value above K_n? It is K_n minus one edge (ends weight 1, rest t): +0.43 at n=4 to +0.10 at n=8; ~100k runs n=5..7 found nothing below K_n"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T14:19:54+02:00
  status: provisional
  evidence: "N5_N6_PROBE_2026_11_10.md, kn_minus_edge_face.out"
---

P0245 (Aldous-Fill Open Problem 6.30, is (n-1)H_{n-1} the least stationary cover time of a reversible chain on n states?): random-restart searches on Mac mini 1 (10 Nov) covered about 92,000 local optimisations at n=5 (with and without holding), 7,500 at n=6, 400 Nelder-Mead restarts at n=6 and 100 at n=7. None went below K_n beyond float error (|gap| < 1.3e-14).

The only other local minimum they reach is K_n minus one edge {a,b}: weight 1 on the 2(n-2) edges at a or b, weight t on the other edges, no holding. Best t and gap above K_n:
- n=4: t 0.20212, 5.931646 vs 5.5 (rel 0.0785)
- n=5: t 0.54249, 8.581920 vs 25/3 (rel 0.0298)
- n=6: t 0.68099, 11.585637 vs 137/12 (rel 0.0148)
- n=7: t 0.75566, 14.824427 vs 14.7 (rel 0.0085)
- n=8: t 0.80226, 18.246338 vs 18.15 (rel 0.0053)
Absolute margin 0.43 down to 0.10, roughly c/n. It lives on the face w_ab = 0, so a global proof (face certificates in OPEN3's ordered-cone method) must clear it, and a proof that loses a constant factor near the boundary fails for large n.

How to apply: before claiming a counterexample or a global certificate for P0245, check it against this basin (a search stopping near these values has found K_n minus an edge, not something new). Files: 12_cognitive_architecture/codex_local_1108/briefs/OPEN3/independent_check_agent/N5_N6_PROBE_2026_11_10.md, kn_minus_edge_face.py/.out, second_basin_n6.py/.out. The local result (K_n strict local min, n>=4) is NOTE_local_minimality.md in the same folder. Related: [[p0245_uniform_kn_strict_local_min_with_holds_n4_to_16_2026_11_10]], [[p0245_n5_per_node_lemma_fails_on_a_path_bound_holds_in_search_2026_11_10]].

What would change it: a basin found at n>=6 that is not K_n or K_n minus an edge, or an exact rational chain below the bound.


Large n (10 Nov 14:3x, kn_minus_edge_large_n.py, exact symmetric recursion, matches the generic solver to all printed digits
for n = 4..8): out to n = 160 the best far-edge weight is t* = 1 - 1/n + O(1/n^2), and the gap to (n-1)H_{n-1} is about
2H_n/n^2 (measured/predicted 1.09 at n = 10, 0.99 from n = 40 on), so the relative gap falls like 2 log n / n^3. The
competitor sits a finite distance from K_n (one edge at weight 0) yet comes within O(log n / n^2) of the bound: a global
proof cannot have a large margin and must handle this family explicitly.

Precise rerun to n = 960 (10 Nov 15:2x, kn_minus_edge_hiprec*.py/.out, 12 digits): 2H_n - gap*n^2 is 0.095 at n=160, 0.077 at 320,
0.057 at 640, 0.047 at 960, falling steadily, so gap = 2H_n/n^2 - o(1/n^2) (a log^2 n / n tail fits, unproved). An earlier fitted
constant (gap = (2H_n - 0.10)/n^2, t* = 1 - 1/n - 3.5/n^2) was withdrawn: the term drifts and t* is too flat to read past 1/n.

Correction (10 Nov 15:54, 30-digit run kn_minus_edge_mp.py): float64 had drifted by n = 1280 (0.0437 there is really
0.0388). In 30 digits: 2H_n - gap*n^2 = 0.0649 (n=480), 0.0388 (1280), 0.0304 (1920), still falling; and
n(n(1-t*)-1) = 3.58, 3.63, 3.64, so 1 - t* = 1/n + c'/n^2 with c' about 3.65 stands after all. Trust only the 30-digit
table past n = 640.
n=2560: 0.0254 and c' 3.653; (2H_n - gap*n^2)*n/log^2 n = 0.82, 0.97, 1.02, 1.06 at n = 480..2560: a log^2 n/n tail fits, a clean power does not.
- 10 Nov 16:0x: tail fit on the 30-digit rows: 2H_n - gap n^2 = (2.04 log^2 n - 8.32 log n + 4.88)/n to 1.2e-5 (H_n form the same); leading coefficient about 2, lower ones not pinned by four points.

10 Nov 16:2x: the gap's tail is the uniform walk's (n-2,2) Hessian term in the frame where the untouched edges keep weight 1: gap = (1/2) lambda(n-2,2) (n-3)/(n-1) (2/t* - 1)^2 + o(H/n^3) (residual 0.011 H/n^3 at n=2560). An earlier '12 H/n^3 cubic remainder' was this frame choice, not a third-order term. Closed form: 2H_{n-1} - gap n^2 = (2H^2 - 10H + 2 + 2 zeta(2))/n. Pushed 064708e7b87a (N5_N6_PROBE, kn_gap_frame).
