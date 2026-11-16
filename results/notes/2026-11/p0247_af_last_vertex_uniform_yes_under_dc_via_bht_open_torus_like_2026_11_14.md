---
name: p0247_af_last_vertex_uniform_yes_under_dc_via_bht_open_torus_like_2026_11_14
description: "[PROVISIONAL] P0247 (Aldous-Fill book Open Problem 7.10: on vertex-transitive graphs with n -> infinity, does the last vertex covered by a walk from a fixed start converge in TV to uniform?) on 14 Nov 2026: YES for bounded-degree families with D^2 = o(n/log n), by Berestycki-Hermon-Teyssier arXiv 2202.02255 Thm 1.2 (uncovered set at t_cov + s t_hit is product Bernoulli, under P_o too) plus a short last-vertex reduction (ours, unrefereed); OPEN for torus-like and other large-diameter families (cycle exactly uniform). BHT never cite AF 7.10"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-14T10:07:05.354Z
---

P0247 on the 200 list. Source: Aldous and Fill, "Reversible Markov Chains and Random Walks on Graphs", Chapter 7,
Open Problem 7.10 (book.pdf p.246): "Let V denote the last state to be hit. In a sequence of vertex-transitive graphs
with n -> infty, is it always true that V converges (in variation distance, say) to the uniform distribution?" They add
that it is surprising there is no obvious counterexample. Under the stationary start the answer is trivially yes by
symmetry; the question is the fixed start.

Status 14 Nov 2026: PARTLY ANSWERED, by literature plus a short argument of ours (unrefereed):
- Berestycki, Hermon and Teyssier, arXiv 2202.02255 v4 (Jan 2026), Theorem 1.2: for bounded-degree vertex-transitive
  graphs, the uncovered set U(t_s) at time t_cov + s t_hit is close in TV to a product of Bernoulli(e^{-s}/n), under P_o
  as well as P_pi, if and only if the diameter condition (DC) D^2 = o(n/log n) holds. Their Theorem 4.8 (the last k points
  are uniform) is stated under P_pi only. They do not cite AF 7.10.
- Reduction: let V' be the last vertex covered by the walk after time t. The kernel K(z, y) = P_z(V = y) is doubly
  stochastic by transitivity, so TV(law of V', uniform) <= d_o(t). V = V' unless V' lies in the range R_t, and
  P(V' in R_t) <= P(post-t cover <= t_s) + P(U' meets R_t). Both U(t + t_s) = U' \ R_t and U' have Poisson(e^{-s}) size
  under P_o by Thm 1.2, so the second term -> 0 when t = o(t_hit). With t_mix <= t_rel log n <~ D^2 log n = o(n) under DC,
  t can be chosen between t_mix and t_hit. Hence V -> uniform in TV.
- Open: families violating DC, i.e. torus-like (Z_m^2, D^2 ~ n) and cycle-like growth. The cycle itself is exactly
  uniform for every start except the start vertex (Lovasz-Winkler). The 2D torus is the natural test case.
Not relevant: Prevost-Rodriguez-Sousi 2309.03192 (the late points of the 2D torus, a different question).
then decide whether to write a short note: "Last vertex of cover on vertex-transitive graphs under the diameter
Next: a GPU Monte Carlo of the last-vertex law on Z_m^2 and Z_m x C_k ladders (fixed start, TV to uniform as m grows),

Monte Carlo, 2D torus Z_m^2 (14 Nov, worker machine 1 GPU via MLX, 65,536 walks per m, start 0, scratch area p0247/
lastvertex_mlx.py + analyze.py): KS distance of the last vertex's torus distance from the start against uniform on the
other n-1 vertices = 0.0379, 0.0310, 0.0254, 0.0200, 0.0159 at m = 8, 16, 32, 64, 128 (m=128: 32,768 walks, 1.02M
steps, 4.6 h on the mini-1 GPU; x0.79-0.82 per doubling; sampling noise ~0.005); KS*log m = 0.079, 0.086, 0.088, 0.083,
0.077, flat to slightly falling. The last vertex is too rarely near the start (P(d <= m/8) 0.0396 vs uniform 0.0486 at
m=128). The orbit-TV column is useless at m >= 64 (it equals the noise TV: too many orbits for the sample). Reading:
consistent with uniformity in the limit at rate ~c/log n, c ~ 0.08, so the torus answer is likely YES but not by the DC
route. Evidence, not proof. Second m=128 seed (run_128b, seed 3, 17,099 s) done 14 Nov: KS 0.0192 alone (seed 2: 0.0159),
both seeds pooled 65,536 walks KS 0.0172 at r* 39.4, KS*log m 0.083 - the flat ~0.08 holds through m=128. Near-start ratio
P(d<=m/8) emp/unif = 0.72, 0.68, 0.75, 0.77, 0.80 for m = 8..128 (pooled 0.0390 vs 0.0486): the deficit closes slowly.
Data stays on worker machine 1 ~/p0247_20af (last_m*_s*.npy).
Next: decide whether to write a short note: "Last vertex of cover on vertex-transitive graphs under the diameter
condition", with the torus numbers as a remark; a torus proof would need the near-start deficit ~ Green function / log n. Work files: scratch area p0247/ of session agent (NOTES.md, the BHT pdf/html, the AF chapter).
