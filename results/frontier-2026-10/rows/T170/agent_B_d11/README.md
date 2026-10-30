# T170 d = 11: two levers tested on the three-slab count chain (agent B, 18 Oct 2026)

The bound is 1/E_pi[c], from the stationary law of the (a,b,c) count chain, computed by a sparse direct solve. The baseline
arm reproduces the recorded values: d12 C16 0.140888, d12 C32 0.119454, d11 C32 0.125789.

1. Backward vertical edges (b->a at max(b-a,0), c->b at max(c-b,0)). They are valid and disjoint from the edges already used.
   The bound moves by 2.4e-7 (d12 C16), 2.8e-7 (d12 C32), 3.8e-7 (d11 C32) and 4.1e-7 (d11 C64, finished 18 Oct). The counts stay ordered a >= b >= c almost
   always, so these terms are almost always zero. backedge_test.py <d> <C> <0|1>; backedge_results.txt.
2. Sensitivity to the horizontal boundary. Scaling sigma(n) by 1.01 and 1.03 at d11 C32 moves the bound from 0.125789 to
   0.125179 and 0.123983, an elasticity of about 0.5 (sigma_sens.py <d> <C> 0 <scale>; sigma_sens_results.txt).

The d11 gap is the cap-ladder limit, about 0.1060, against the diagonal floor 0.104246: about 1.7 percent. Closing it would take
roughly 3.5 percent more boundary at every size. The hypercube bound 2mn - 2f(n) is sharp for arbitrary sets, so a chain that
treats the slab sets as worst case cannot reach d11. Wider windows and more edge types are also ruled out by earlier measurements
(see DOSSIER). A d11 proof would have to use the randomness of the slab growth. The elasticity was measured at C32 only.

3. How much room random growth leaves (eden_boundary.py 10 256 20 1; eden_boundary_m10.txt). Eden growth in one slab of Z^10,
   horizontal edges only, newborn = target of a uniformly chosen boundary edge, 20 runs. Mean boundary / sigma(n): 1.069 (n=8),
   1.123 (16), 1.189 (32), 1.263 (64), 1.352 (128), 1.457 (256); the smallest run at n=8 is 1.044. That is ten times the 3.5
   percent d11 needs. The randomness is the lever.
   One shortcut fails: accepting only births whose target has a single infected neighbour keeps the slab set a tree, but in the
   worst case the rate can drop to zero. A star with 2m arms has about 4m^2 boundary edges, and the C(2m,2) - m uninfected square
   corners take two each. So worst-case geometry kills it, and a proof has to average over the geometry. One possible route: track
   the exact joint shape of the three slabs, up to lattice symmetry, while the counts are small, and fall back to sigma above
   that. The gain sits where the clusters are small, which is where the ratio is lowest, so cost the gain before building it.
   Caveat: inside the three-slab process, slab b also gets forward births under slab a, which make it less tree-like than pure
   horizontal Eden.

4. Optimistic ceiling for exact small-shape tracking (ceiling.py 11 32; ceiling_d11_C32.txt). Replace sigma(n) by the Eden MEAN
   boundary (200 runs) for n <= K, and leave the rest of the chain unchanged. Relative gain at d11 C32: K=4 0.11 pct, K=8 0.52 pct,
   K=16 1.22 pct, K=32 1.67 pct. Needed: 1.7 pct. Tracking exact joint shapes up to 8 sites cannot close d11 even in this optimistic
   form, which uses the mean, not a worst case or a high-probability bound. A random-growth argument would have to control
   clusters of tens of sites or more. At larger caps the Eden ratio keeps growing (1.26 at 64, 1.46 at 256), so such an argument
   would have room, but it is a theorem about Eden clusters, not a finite computation.

5. Diagonal side: U-shaped detours (udetour_est.py 11; udetour_d11.txt). A geodesic edge x -> x+e is no slower than each detour
   x -> x+f -> x+f+e -> x+e, of which about 2(d-1) - 2 avoid the neighbouring steps. In a plain walk first-moment model (exponential
   Chebyshev over walks to the level hyperplane; baseline 0.10251 at d11, close to Kumar-Dhar's 0.10271), constraining each edge to
   be below the minimum of K = 16 or 18 independent Gamma(3) detours gains 0.01 pct (every other edge) to 0.03 pct (every edge). The
   optimal tilt is theta ~ 38, so the counted edges have times around 1/39, and a three-edge detour almost never beats that. Local
   comparisons longer than two edges are saturated in this dimension. The floor's distance from the truth comes from overcounting
   correlated paths, not from missing local constraints. A better diagonal floor needs a second-moment or correlation idea.
