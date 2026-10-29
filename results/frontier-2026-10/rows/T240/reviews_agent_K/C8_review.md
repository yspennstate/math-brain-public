# Independent review of T240 C8 (eta cell [2499/5000, 2501/5000], q0 = 1) - agent K, 18 Oct

Files: rows/T240/C8_eta_cell, sha256sum -c SHA256SUMS all OK (copy reviewed in scratch, live folder untouched).

1. chain_check_eta.py re-run on the copy: CHAIN CLOSED, output identical to logs/chain_check.txt.
2. Read line by line (entry_eta.py segment/run_piece/run_trap, chain_check_eta.py, widen_eta.py cell):
   - defect enclosure: two-variable mean value about (t_c, eta0) with d_t delta and d_eta delta enclosed over the
     sub-box x H; g = y_t - f_x y - f_eta; d_t g = y_tt - f_xx(xhat_t, y) - f_x y_t - f_x,eta xhat_t;
     d_eta g = -f_xx(y,y) - 2 f_x,eta y - f_eta,eta: all three match the code term by term (Hm index 3 = eta).
   - X, V, Acc carry the DH*y terms; Y, VY, YTT do not (y independent of eta): correct.
   - a priori box E = X + P[-R,R]^3 with Jacobian over E x H (entry.ETA reassigned to H in setup, read at call time).
   - error ODE bound r1 = e^{mu h} r0 + d h e^{max(mu,0) h}; frame switch r <- r1 ||Pinv_{k+1} P_k||: correct.
   - junctions: piece k0 frame = frame(nodes[k0]) = previous piece's end frame; partial q6b uses float(r) x (1+1e-12),
     q6c r_in 717/25000000 clears it.
   - trap: residual by mean value along c(eta) with f_x, f_eta over cb x H; log norm over cube cells (cube contains
     the 2-norm ball; log norm convex so the cell split is sound); need = offset + ||Pinvs P_K|| r_end < rho.
   - plateau link: Krawczyk with eta as an interval gives one root per eta in each box; the checker encloses
     box - c(eta) over the whole cell (de as an interval), stored-float rounding (~1e-17) is under its 1e-12 pad.
   - the C7 helpers in entry.py, read too (C7's own review never got to them): cubic Hermite interpolates values and
     h-scaled slopes at both ends (checked by hand); poly_range is the exact centred Taylor form; lognorm_up is
     Gershgorin on the symmetric part, an upper bound of the 2-norm log norm over the interval matrix; opnorm2_up
     proves lu I - M^T M positive definite by exact leading minors; expu: e^x <= 1 + x + x^2/2 for x <= 0 (cubic
     remainder negative), e^x <= 1/(1-x) for 0 < x < 1/2; jac_box_centered is the mean value form intersected with
     the plain jet enclosure, eta read from entry.ETA = H at call time. The a priori box argument (rmax < R, E
     convex, J-bar in the interval hull) is the standard continuation argument and is applied correctly.
   No logical gap found. Not re-read: iv_exact / iv_scm / iv_h2 (the jet arithmetic itself; C6/C7 reuse it).
   One unstated assumption, not a gap in practice: a piece's r_in is in frame(nodes[k0]) recomputed in a NEW
   process, while the previous piece switched r_out into the frame it computed for the same node. That needs
   np.linalg.eig to return the same float frame in both processes; my rerun of segments 0-2 reproduced every 'sw'
   to the last digit, so it does here, but logging a hash of P at each piece end would make it checkable.
3. Replays from a fresh copy (no node cache: build() re-integrated the reference path and the sensitivity):
   - segments 0, 1, 2 (piece from r_in 0): d, mu, R, r, sw, Xw identical to q1.jsonl to the last digit;
   - segments 1065-1068 from the logged r after 1064: identical to q6d.jsonl, and the piece ends on the same exact
     r_out 64983279564539/2305843009213693952 as q6d;
   - trap at r_end 1/10000: offset, need_rho, resid, xs0, ys and PASS {rho 1/5000, nsplit 2, exact mu} identical;
   - plateau cells at both ends of E8 ([2499/5000, 7997/16000] and [8003/16000, 2501/5000], two cells each at width
     1/160000): all pass, info and centre identical to the logged rows.
VERDICT: ACCEPT C8 as stated (every eta in [2499/5000, 2501/5000], q0 = 1), conditional only on the interval jet
library iv_exact / iv_scm / iv_h2 that C6 and C7 already rest on.
