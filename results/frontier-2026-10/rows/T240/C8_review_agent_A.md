# Independent review of T240 C8 (eta cell [0.4998, 0.5002], q0 = 1) - agent A, 18 Oct 2026

Verdict: PASS. Scope: C8's new layer (eta-affine reference, two-variable defect
enclosure, cell-wide Jacobians, moving trap centre, plateau-in-ball link). The interval engine (iv_exact, iv_scm) and the closed
slice drift (= the SCM ODE) are inherited from C6/C7 and were not re-reviewed here.

Read line by line (entry_eta.py, widen_eta.py, chain_check_eta.py, entry.py's frame/jac_box_centered/hermite/poly_range):
1. Defect: delta(t, eta) - delta(t_c, eta0) split as [delta(t, eta) - delta(t_c, eta)] + [delta(t_c, eta) - delta(t_c, eta0)]; dt encloses
   d_t delta over the sub-box x cell (Acc, V, X all carry DH * the y-part; Jx over X and H), de encloses g = d_eta delta over the whole
   sub-box via its own MVT. Checked by hand: d_t g = y_tt - f_xx(x_t, y) - f_x y_t - f_(x eta) x_t and d_eta g = -f_xx(y, y) -
   2 f_(x eta) y - f_(eta eta), matching gt and ge index for index (y and y_t do not depend on eta). Correct.
2. Error ball: a priori box X + P[-R, R]^3 contains every point within 2-norm R in the z frame; Gershgorin log norm over the box and
   H; continuation (rmax < R) then r1 = e^(mu h) r0 + d h e^(mu+ h). Correct. entry.ETA is rebound to H by setup, so the a priori
   Jacobian really ranges over the cell.
3. Frames: every row's r is already switched to node k+1's frame, so q6b's partial end (node 1020, last row k = 1019) is in the frame
   q6c starts in. Junctions consistent; the 1 + 1e-12 factor on the float r is ample.
4. Trap: need = offset (interval over eta, exact) + ||Pinv_s P_K|| r_end compares like with like (last r_out is in node K's frame,
   the frame the trap converts from). Residual by MVT along c(eta) with jets over the hull cb x H. Ball covered by cubes. Correct.
5. Plateau: widen_eta's Krawczyk test with eta an interval is the parametric form (unique zero per eta); Hurwitz, odd2 and
   teacher_odd are interval tests valid for every matrix in the enclosure. Box inside ball for every eta of its cell -> the
   trap's unique equilibrium is the certified root. Correct.

Independent computations (scratchpad c8rev/review_float.py, output review_float.txt):
A. 3,672 interval jet entries (values, f_x, f_eta, all second derivatives incl. eta) at 36 random points near the path and eta in the
   cell contain central finite differences of the float closed drift: 0 outside.
B. Sampled defect |Pinv_k delta(t, eta)| at 18 times x 6 etas per segment, all 1,069 segments, eta over the full cell: max 0.274 of the
   logged d_k, 0 violations.
C. Radau (rtol 1e-12) at 9 etas across the cell: max |z_true|/r_logged over all nodes 2.15e-2 (reproduces the lead's audit_float
   number); every trajectory at t = 8000 sits within 2.3e-9 of c(eta) (rho = 2e-4), |f| ~ 1e-16, inside its own cell's plateau box.
D. Exact re-run: piece q6d (nodes 1045-1069, r_in 3/100000): all 26 rows (25 segments + the piece_done line, r_out = 2.8182005151642427e-05 exactly) equal the shipped rows in every field but the elapsed time
   chain_check_eta.py on the shipped logs: CHAIN CLOSED. sha256sum -c: 25/25 OK.

Minor (not errors): chain_check does not record or compare T and W across pieces and the trap (consistency is only implicit through
K = 1069 and nseg_total); a 'T','W' field in each head and an assert would close that. The float audit and B show the bound is
loose by ~50x at the cell ends, so a 2-4x wider cell is likely reachable with the same machinery.
E. Exact trap re-run (entry_eta.py trap ... r_end 1/10000, this machine, 18 Oct 06:3x): offset 8.9044e-05, need_rho 1.8905e-04,
   resid 8.0e-08, nsplit 1 fails (mu +9.5e-05), nsplit 2 PASS at rho 1/5000 with mu = -0.00075342 - the exact rational is
   identical to the shipped trap.jsonl's last row.
