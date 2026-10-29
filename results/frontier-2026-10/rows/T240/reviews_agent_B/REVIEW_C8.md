# Review of T240 C8 (deterministic entry over the eta cell [2499/5000, 2501/5000], q0 = 1)

Reviewer: agent B (independent of the author, agent H; same model family, so not a distinct account).
Read: C8_eta_cell.md; scripts/entry_eta.py and chain_check_eta.py whole; entry.py (frames, log norm, operator norm,
exponential bound, Hermite reference); widen_eta.py cell test; check_symmetric_closed.closed. Files hashed:
sha256sum -c SHA256SUMS 25/25 OK.

VERDICT: PASS. The drift is the T240 model's overlap ODE; C6/C7 carry it and I checked it again here by an independent
Monte Carlo, below.

## What I checked by hand

1. The defect enclosure (entry_eta.segment). The two-variable mean value split
   delta(t, eta) - delta(t_c, eta0) = d_t delta(xi, eta)(t - t_c) + d_eta delta(t_c, eta')(eta - eta0)
   needs d_t delta over (sub-interval x cell) and d_eta delta at t_c over the cell; the code encloses both over the
   larger set (sub-interval x cell), which is valid. Re-derived: d_t delta = xhat'' - f_x xhat'; g = d_eta delta =
   y' - f_x y - f_eta; d_t g = y'' - f_xx[xhat', y] - f_x y' - f_{x eta} xhat'; d_eta g = -f_xx[y, y] - 2 f_{x eta} y
   - f_{eta eta}. All four match the code term by term (gt, ge use the 4-variable Hessian h4[i].h with index 3 = eta,
   the symmetric cross term appearing once from each side). V and Acc carry the (eta - eta0) y', y'' parts through DH.
2. Segment growth. With the a priori box E = hull(X) + P [-R, R]^3 and mu the Gershgorin bound of the symmetric part
   of P^-1 J(E, cell) P, |z|' <= mu |z| + d gives r1 = e^{mu h} r0 + d h e^{max(mu,0) h}; the bootstrap
   (r0 + d h) e^{mu+ h} < R keeps the solution in E. expu is an upper bound on both branches (x <= 0: Taylor remainder
   x^3/6 e^xi <= 0; 0 < x < 1/2: e^x <= 1/(1-x)). entry.ETA is a module global read at call time, so setup()'s
   assignment of the whole cell does reach jac_box_centered and point_f (no frozen default argument).
3. Frames. P is a float eigenframe turned into exact rationals and Pinv its exact rational inverse; the switch factor
   ||Pinv_{k+1} P_k||_2 is bounded above by exact Sylvester minors. Correct.
4. Start. nodes[0] = (1, 0, 0) exactly and y(0) = 0 exactly, so the error is 0 at t = 0 for every eta in the cell, and
   chain_check asserts the first piece starts at node 0 with r_in = 0. C8 does not use C7's exit set at all: the chain
   is self-contained from t = 0. (This answers the author's second question.)
5. Junctions and the partial piece. r_out is stored as an exact Fraction string for finished pieces; for q6b the last
   row's r is the radius at node 1020 in node 1020's frame (r is switched before the row is written), float(Fraction)
   is correctly rounded, and the factor 1 + 1e-12 covers it. q6c then starts in the frame of node 1020. Correct.
6. Trap. need = |Pinv_s (xhat(T, eta) - c(eta))| + ||Pinv_s P_K|| r_end, with eta - eta0 carried by DH: correct.
   Residual: f(c(eta), eta) = f(xs0, eta0) + [f_x ys + f_eta](point on the segment)(eta - eta0), the jets taken over
   cb x H, which contains that segment: correct. The log norm is bounded over a cover of the cube [-rho, rho]^3 (which
   contains the ball) and over the cell. res < -mu* rho makes the ball forward invariant and the flow a contraction on
   it, hence one equilibrium per eta and exponential convergence at rate |mu*|.
7. Linking. Each pass cell is a parametric Krawczyk certificate (f0 and the Jacobian both over the eta interval, image
   strictly inside the box, ||I - A J|| < 1), so each eta in the cell has exactly one zero in its box; the box (float
   centre, half-width info[0], both padded by 1e-12, which dominates their rounding) lies in the trap ball for every
   eta of the cell. The cover test on sorted cells is conservative (it can only fail spuriously).

## What I re-ran (my copy of scripts and logs, (local dir), files here)

- junctions.py: rebuilt the reference from scratch (the lead's pickle cache was not copied) and recomputed the first and
  last segment of every piece, 16 segments: t, d, mu and R are bit-identical to the lead's rows (junctions.txt). So the
  reference used by every piece is the one this environment builds, and the junction comparisons are between the same
  reference points.
- chain_check_eta.py on the shipped logs: output byte-identical to logs/chain_check.txt (CHAIN CLOSED).
- cells_recheck.py: the C6 cell test on the first, a middle and the last plateau cell, from the recorded centres: all
  pass, box half-widths equal to the logged ones to five figures.
- sym_consistency.py: iv_scm.symmetric_driver (defect value, Jacobian, trap log norm) and the 4-variable full_driver
  slice sym4 (g and the trap residual) agree exactly in value and f_x at three points; sym4's f_eta and its 4x4 Hessian
  agree with finite differences of the float closed form to 1e-11 and 3e-8; iv_h2's 3-variable Hessian equals sym4's
  q, c, r block exactly.
- mc_drift.py: direct Gaussian Monte Carlo of the online-SGD increments (the T240 model's lambda/nu covariance, erf activation, the eta^2 E[delta delta] term) at four slice states, one of them the plateau root, and eta = 0.5 and 0.4998 (mc_drift.txt): 20 of 24 z-scores within 2 against cs.closed, and iv_scm's midpoint equals cs.closed to six figures. The four with |z| in 2.2-2.9 were drawn again with fresh seeds and 4-16 times the reps (mc_recheck.txt, mc_recheck2.txt): all within 1.9. So the drift the certificate integrates is the model's.

## Remarks (not blocking)

R1. The pieces read the reference from a pickle cache, and nothing in a piece's header binds it to one reference. The
    bit-identical rebuild above settles it for this certificate; for later cells a hash of (tq, nodes, slopes, ys,
    yslopes) in each header, checked by chain_check, would make the junctions self-verifying.
R2. The float sanity check (worst |z_true| / r_cert = 2.15e-2 at the cell's ends) agrees in shape with the certificate's
    slack; nothing in the proof depends on it.
R3. Scope as stated: q0 = 1 only, the cell only, the symmetric slice (whose invariance under the full ODE is the
    S2 x S2 symmetry of the committee machine, used by C4 and not re-proved here).
