# Audit of rows/T352/agent_B/NOTE.md (agent A, 19 Oct 2026 21:1x)

Verdict: the n-free floor for Chien-Li Thm 3.7 holds. The lambda = 1 proof is correct as written. The lambda < 1 step
needs one more line (below), and with it the claim stands. The numbers reproduce by a second method. The readings of
Liang et al. and Asoodeh-Diaz were not re-checked here.

1. Minimising over beta. min_b c^2/b + a^2/(1-b) = (c+a)^2 at b = c/(c+a), for a >= 0. Correct.

2. D_tau = D in the limit (the point you asked about). Correct, and here is the argument in full. Every per-step cost is
   (c+a_t)^2 >= c^2. So a window of length T - tau costs at least (T - tau) c^2. From D_0 = 0, D_t >= min(t c, D), so
   D_t = D for t >= t* := D/c (in fact much sooner: the g-branch grows geometrically, so t* ~ log(1 + eta L D/c)/(eta L)).
   For tau < t*, the cost is >= (T - t*) c^2, which goes to infinity. So for T large the minimum is taken over tau >= t*,
   where D_tau = D. Hence lim_T min = the problem with the constraint A_tau >= D. Remark worth one line in the note:
   the plateau is reached only after about log(n)/(eta L) steps, so the floor is n-free in value but not in onset time.

3. lambda = 1. A_tau = sum_{j>=1} r^j a_{tau+j-1} (checked by unrolling from A_T = 0), and Cauchy-Schwarz gives
   sum a^2 >= D^2 (1 - r^2)/r^2 = D^2 ((1+eta L)^2 - 1) = D^2 (2 eta L + eta^2 L^2). Correct. Strict for every finite window.

4. lambda < 1: the pointwise claim "h_lam <= h_1 everywhere" is false as stated. x^lam >= x D^{lam-1} holds only on
   [0, D]; for x > D, x^lam < x D^{lam-1}. So h_lam(z) <= h_1(z) holds for z <= g_1(D), not for every z, and a path whose
   intermediate A exceeds D escapes the comparison. Fix (two lines): given a feasible (tau, a), let t' be the last t >= tau
   with A_t >= D; dropping the terms before t' keeps the path feasible and only lowers the cost (each term is
   nonnegative), and lowering a_{t'} until A_{t'} = D lowers it further. On the reduced path every A_t lies in [0, D].
   Then, by induction from A_T = 0, the lambda = 1 recursion with L' = L D^{lam-1} and the same a's satisfies
   A^1_t >= A^lam_t: z = A^lam_t + a = g_lam(A^lam_{t-1}) with A^lam_{t-1} <= D, so g_1(A^lam_{t-1}) <= z and
   h_1(z) >= A^lam_{t-1}, and h_1 is increasing. So the lambda < 1 feasible set lies inside the lambda = 1 set with L',
   and the floor follows. Also note that this needs a_t >= 0, which the theorem has (shift amounts).

5. Numbers re-derived a second way (all-active window, cost(N) = (D + c S1)^2/S2, S1 = sum w, S2 = sum w^2, w_j = r^j,
   keeping only N with mu w_N > c; eta 0.01, L = K = D = 1):
       n 10:   0.0281400 (N 180)     note: 2.814e-2
       n 1e3:  0.0201804 (N 625)     note: 2.018e-2
       n 1e6:  0.0201001 (N 1319)    note: 2.0100e-2
       floor   0.0201
   They agree. cl_floor.py prints overflow warnings at large N (r^N underflows in c/w.min()); those windows lose the
   minimum, so the values are unaffected. lambda = 1/2: the Dijkstra value 2.677e-2 is above the floor 2.01e-2
   (L' = L since D = 1), as item 4 requires.

6. The Gaussian example (item 2 of the route section) re-derived: m_k^2/v_k -> (eta K/n)^2 (c+1)/((c-1) sigma^2), so
   2 alpha m^2/v -> 2 alpha eta K^2 (2 + eta L)/(n^2 L sigma^2). Matches.

Not checked: the excerpt-level readings of 2502.17772 (the eq. 51 term you flag) and 2305.09903 Thm 2. The Doeblin route
is a plan, not a claim, and I have nothing to audit there yet. One caution on it: on the projected interval the law has
atoms at the boundary, so the minorisation needs the projected kernel's own lower bound (mass at the endpoints counts
toward m), not the torus constant.
