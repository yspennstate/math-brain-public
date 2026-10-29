# C9: post-exit recovery from the symmetric plateau, full seven-overlap ODE, eta in E

Author: agent H (lead). Computer-assisted, exact outward interval arithmetic (iv_exact.py, 160-bit fixed point;
floats only build the reference path and the frames, never decide an inequality). Trust base: Python integers and
Fractions, plus, in the tube runs (C9_ARB=1), Arb/FLINT for the arcsine at interval endpoints (360-bit balls rounded
outward to the 1/2^160 grid; cross-checked against the series-with-remainder path on 2000 random points). The Krawczyk,
cone and trap steps can be rerun with C9_ARB unset (series path only) at about ten times the cost. Kind: special. Target: phase (c) of
the ARCHITECTURE. Needs an independent reviewer. DRAFT: numbers marked [pending] come from the running chain.

## Statement

Let E = [0.4999999999, 0.5000000001] (C6/C7's interval) and let F be the K = M = 2 erf overlap drift in the seven
coordinates x = (Q11, Q12, Q22, R11, R12, R21, R22) (with the eta^2 term, as evaluated by iv_scm.full_driver). For every
eta in E let x*(eta) be the symmetric plateau of C6 (unique zero in the certified Krawczyk box X*, width 1.23e-9).
Let P be the teacher-swap-adapted eigenframe at the float plateau (rational, exact inverse), u the coordinate along its
unstable column and s the six stable coordinates, and let

    N = { x*(eta) + P(u, s) : |u| <= U_c, |s_i| <= kappa U_c },    U_c = 1/100000, kappa = 1/500.

Then for every eta in E, every solution of x' = F(x, eta) that starts in N with |s_i| <= kappa |u| and u != 0 crosses
the section u_c := (P^{-1}(x - xc))_0 = sign(u) U_s, U_s = 99/10^7, before leaving N, exists for all later time, and converges exponentially: to the swapped teacher
(1, 0, 1, 0, 1, 1, 0) when u > 0 and to the teacher (1, 0, 1, 1, 0, 0, 1) when u < 0. Both are exact zeros of F for every
eta, and both are linearly stable.

So the deterministic part of phase (c) holds on E: once the transverse coordinate has escaped to the scale of U inside the
cone, the ODE carries the state to a permutation of the teacher, and the generalization error tends to 0.

Not included: eta outside E; the stochastic glue (that the SGD state, after tau_N, lies in the cone at the scale U with
probability tending to 1 and that the fixed-horizon theorem then applies on the O(1) remaining window).

## Proof outline

1. Plateau box. Seven-dimensional Krawczyk test on X* over E (rho 1e-9): OK. Unique zero x*(eta) in X* for each eta.
2. Cone lemma. Over the Jacobian hull of N (all eta in E), in the frame P, with m_uu, m_us, m_su, mu_ss the interval
   bounds of the unstable entry, the coupling rows and the stable block's log norm:
       kappa (m_uu - mu_ss) > |m_su| + kappa^2 |m_us|   and   m_uu - kappa |m_us| > 0.
   The first makes the cone |s| <= kappa |u| forward invariant inside N; the second makes |u| grow at rate
   >= grow > 0 there, so every solution in the cone with u != 0 reaches |u| = U in finite time, with |s| <= kappa U.
   Measured at (U_c, kappa) = (1/100000, 1/500): margin 4.3e-5, grow 0.031614 (also OK at 1/300, 1/200 and at U_c = 1/50000).
2a. Section. xc is the centre of X*, and (P^{-1}(x*(eta) - xc))_i is at most zo_i in absolute value (zo_0 about 8e-9 < U_c - U_s).
   While a cone solution's u (relative to x*(eta)) runs from small to U_c, its u_c runs from below U_s to above U_s, so it
   crosses u_c = U_s at a point with |u| <= U_s + zo_0 and hence |s_i (rel. xc)| <= kappa (U_s + zo_0) + zo_i. The crossing set
   is { p0 + P z : z_0 = 0, |z_i| <= kappa (U_s + zo_0) + zo_i }, p0 = xc + U_s P[:, 0]: its spread along the unstable
   direction is exactly 0. (A face u = U about x*(eta) would carry a u-spread of zo_0, a time shift of zo_0/(lambda U)
   that the path's speed amplifies along the escape.)
3. Tube from the section. From the crossing set of 2a, a cubic Hermite reference with exact rational nodes (1687 nodes, t in [0, 820]) is followed by a
   validated integration that bounds the error z = P_k^{-1}(x - xhat) block by block (a block is one real eigen-direction
   or one complex pair of the frame P_k at node k):
       D+ v <= A v + d,   A_bb = log norm of the diagonal block, A_bc = norm of the off block, over the a priori box,
       v(h) <= e^{-ch} e^{Bh} v(0) + h e^{Bh} d,   B = A + cI >= 0,
   with e^{Bh} bounded entrywise (Taylor plus tail after scaling, then squaring; entries nonnegative, so the bounds
   compose) and the a priori box verified by the same inequality on a doubled radius. At a frame switch,
   v_new_b <= sum_c ||(P_{k+1}^{-1} P_k)_bc|| v_c (spectral norms by Sylvester minors).
   A single Euclidean ball cannot be used here: its log norm contains the unstable eigenvalue and it grows by about
   e^{0.0316 t} along the escape, while the spread of the face set lies in the stable blocks.
   The tube is three logged pieces joined at two nodes:
     (i)   nodes 0..200, plain eigenframe (clustered: eigenvalues within DELTA share one orthonormal block), rows 0..199
           of logs/bfull14.jsonl;
     (ii)  nodes 200..600, same frame, rows 200..599 of logs/brst10.jsonl (a resume from bfull14's exact radii at line 199;
           that run failed later, at k856, and its rows after 599 are not used; each row is a self-contained segment
           bound, valid on its own);
     (iii) nodes 600..888, flow-adapted frame, eigenvalue clusters at gap DELTA = 0.02, rows 600..887 of logs/flow599.jsonl
           (its rows after 887 are not used);
     (iv)  nodes 888..1686, the plain clustered frame at DELTA = 0.01, no section resets, logs/plain888g8.jsonl
           (resumed from flow599's exact radii at line 887), with the comparison step taken per group of sub-intervals
           (C9_LNSUB = 8, three of the 24 sub-intervals per group; below).
   At the first junction the resumed radii dominate the prefix's exact radii block by block (ratio 1.000000). At the
   second the frame changes: the radii at node 600 are carried from the plain frame to the flow-adapted frame by the
   frame-switch bound above, and c9_bcheck5.py recomputes that switch exactly and finds it equal to the logged v_in. At
   the third the frame changes back: from t ~ 421 every eigenvalue is negative (-0.0215, -0.0234, -0.0433, -0.239, ...),
   so no reset is needed, and the radii at node 888 are carried from the flow-adapted frame (DELTA = 0.02) into the plain
   clustered frame (DELTA = 0.01, blocks [2,1,1,1,1,1]) by the same switch bound; c9_bcheck5.py recomputes it exactly and
   finds it equal to the logged v_in (|v| 9.3e-5 to 4.3e-4: the plain frame's slow pair is far from orthogonal to the
   flow-adapted columns).
   Why the flow frame is left at node 888. In the flow-adapted frame block 0 is fed by the coupling to the slow pair
   (off-block norm 0.070 over the box) and the reset that removes it costs more as |f| falls (|f| = 5.4e-3 at node 888,
   9e-7 at the end; the stopping time grows as 1/|f|): a reset at node 931 would have taken |v| from 1.83e-4 to 2.51e-4.
   The flow-frame run was heading past the trap's budget.
   Grouped comparison. With one Jacobian enclosure over the whole segment's reference hull, the slow block's interval log
   norm was +0.0048 against the point value -0.0215: the hull adds |J'| h |f| (the reference moves about 1.5e-3 over a
   segment). On group g = [t_k + g h/G, t_k + (g+1) h/G] the deviation obeys the same block inequality with A_g enclosed
   over E_g = (reference hull over the group) + P[-R_g, R_g], the defect bound d holding on the whole segment; R_g is
   validated by the same test (e^{B_g h/G}(v + d h/G) < R_g entrywise) and v is carried from group to group. With
   G = 8 the slow block's interval log norm is -0.0100 at node 888.
   Flow-adapted frame. From node 600 the flow direction g = f(x_k)/|f(x_k)| is a one-dimensional block of its own; it
   replaces the eigen-column carrying most of P_k^{-1} g, and the rest of that block stays one block. A section reset at
   node k replaces the tube S by the set reached at the stopping time tau(x) = -<n, x - x_k>, with
   n = s (row 0 of P_k^{-1}) and s fixed by <n, f(x_k)> = 1 (reset at every node), so n^T P_k = s e_0 exactly: the reset removes the flow-direction
   block and leaves every other block's radius alone up to the remainder int_0^tau (f(phi_r x) - g) dr, which is bounded
   over a validated a priori box. A bounded time shift per trajectory is harmless here because the trap ball of step 4 is
   forward invariant.
   Why the frame changes at node 600. In the plain frame the reset along g did not help: after t ~ 270 the unstable
   eigenvector is far from parallel to the flow, so each reset cut |v| by under 0.5 pct, and the plain-frame tubes broke
   their a priori box at t ~ 405 (block-0 log norm over the box climbing from 0.053 to 0.276 as the radius grew; the
   Jacobian moves about 30 per unit radius there).
   [pending: rows per piece, max a priori radius, v_end, r_end = |v_end| (Euclidean, |z| <= |v|)]
4. Trap. At the target T (the swapped teacher), with P_t its eigenframe, the interval log norm mu_t of P_t^{-1} J P_t over
   the ball |P_t^{-1}(x - T)| <= rho (all eta in E) is negative and the residual |P_t^{-1} F(T)| is 0, so the ball is
   forward invariant and every solution in it converges to T at rate |mu_t|. The tube's end set lies in the ball:
   |P_t^{-1}(xhat_K - T)| + ||P_t^{-1} P_K|| |v_end| <= rho.
   Measured (logs/trap_pre2.jsonl, T = swapped teacher, reference end node at t = 820): residual exactly 0 (enclosure
   width 5.8e-46), cond(P_t) = 5.50, |P_t^{-1}(xhat_K - T)| <= 4.108e-5, ||P_t^{-1} P_K|| <= 1.00038; at rho = 1e-4, one
   cell, mu_t <= -0.007316 (exact rational in the log). So the trap closes for any tube end radius v_end <= 5e-5
   (need_rho = 9.11e-5 at v_end = 5e-5). Larger rho fail: the Jacobian moves by about 190 rho across the ball, so mu_t
   turns positive near rho = 2e-4 (sink spectrum -0.541, -0.356, -0.223 (x2), -0.0475, -0.0221 (x2)).
   Wider trap (logs/trap_wide.jsonl, v_end = 1e-4, need_rho = 1.411e-4): at rho = 3/20000 with each frame coordinate
   split in two (128 cells) mu_t <= -0.01097 (exact rational in the log); one cell gives mu_t = +7.8e-5. So the trap
   closes for any tube end radius v_end <= 1e-4.
   Wider still (logs/trap_r1o4000.jsonl, v_end = 2.5e-4, need_rho = 2.912e-4, rho = 3e-4): one cell mu_t = +0.0223, two
   per coordinate (128 cells) mu_t = +0.00016, both fail; three per coordinate (2187 cells) mu_t <= -0.007204 (exact
   rational in the log), PASS. The excess over the sink's -0.0221 at one and two cells is interval wrapping, which shrinks
   with the cell width. So the trap closes for any tube end radius v_end <= 2.5e-4.
   The tube's radii at node K live in its own block frame (frame_b, plain clustered, DELTA = 0.01), so the finish runs the
   trap with P_K = that frame (C9_TRAP_FRAMEB = 1): ||P_t^{-1} P_K|| <= 1.0000 (probe), the budget is unchanged.
5. The other sign. Let tau swap the teacher indices (R_i1 <-> R_i2). F(tau x) = tau F(x) (relabelling the teacher units in
   the drift; consistent with the interval enclosures at sample points, c9_swap_check.py). The Krawczyk test proves x*(eta)
   unique in B = xc + [-rho, rho]^7 with xc exactly tau-fixed (all four R entries equal), so B is tau-invariant and
   x*(eta) is tau-fixed. (The returned enclosure X* is not tau-invariant to the last bit, so the argument uses B.) Every
   column of P is exactly tau-even or tau-odd (checked in rationals; parities -1, 1, 1, 1, -1, 1, 1, the unstable column
   odd), so the row of P^{-1} giving u_c is tau-odd and u_c(tau x) = -u_c(x). So tau maps the
   section u_c = U_s onto u_c = -U_s and the swapped teacher onto the teacher, and step 3-4 for u > 0 give u < 0.

## Files

scripts/c9_cone.py (Krawczyk, adapted frame, cone lemma), c9_flow.py (Hermite reference, defect, single-ball segment
kept for comparison), c9_blocks.py (block tube), c9_run.py (setup, count, bpiece, trap; env C9_U, C9_KAPPA),
c9_bcheck.py / c9_bcheck2.py (chain checks for one run / prefix plus one resume), c9_bcheck3.py (the three-part chain
with the frame switch recomputed), c9_cluster.py (clustered frame), logs/ (every segment row), SHA256SUMS. Env for (iii):
C9_ARB=1 C9_CLUSTER=1 C9_U=99/10000000 C9_KAPPA=1/500 C9_FACE=section C9_HMAX=0.5 C9_FLOWCOL=1 C9_RESET=1.

## What the stochastic glue must supply (not proved here)

Write X^N_t for the overlap process of online SGD at learning rate eta/N, time in units of N steps. C9 is used through the
following statement, which is the remaining gap of phase (c):

    (G) For every eta in E there are stopping times tau_N such that, with probability tending to 1,
        X^N_{tau_N} lies in N, |s| <= kappa |u|/2 and |u| = U_c/2 in the frame P at x*(eta).

Given (G), the fixed-horizon limit theorem (the ODE approximation on [0, T] with error O(N^{-1/2} log N) uniformly in
probability) applies from tau_N over the window [tau_N, tau_N + T_end + T_trap], and the uniform tube of step 3 has
radius v_end << rho, so X^N stays within the trap ball's attraction and the generalization error tends to 0. The halved
cone (kappa/2, U_c/2) leaves room for the O(N^{-1/2} log N) deviation at the restart. (G) itself needs the escape law
near the saddle: the transverse coordinate's fluctuation is O(N^{-1/2}) at the plateau and grows at rate lambda_u, while
the stable coordinates are pinned at O(N^{-1/2}) by the contraction; so the ratio |s|/|u| at |u| = U_c/2 is
O(N^{-1/2}/U_c), below kappa/2 for N large. This is the standard saddle-escape argument (linearize, compare with the OU
process in the stable block and a scaled geometric growth in u), and it is the next item.
Two cautions on the sketch. The cone at the restart is tiny in absolute terms (kappa U_c/2 = 5e-9), so "N large" means
N^{-1/2} log N well below that: the statement is asymptotic, with no useful finite-N content at these constants. And the
trap ball controls X^N only over the finite window; the conclusion "error tends to 0" is the limit N -> infinity at a
fixed time after the window (the ODE limit), not a statement about t -> infinity at fixed N.
