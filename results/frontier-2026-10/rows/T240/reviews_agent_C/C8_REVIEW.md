# Review of C8 (deterministic entry over the eta cell [2499/5000, 2501/5000], q0 = 1)

Reviewer: agent C, 18 Oct 2026, 05:4x-06:1x. Independent of the lead (agent H) and of the parallel
review in reviews_agent_B/, which I have not read.

## Verdict

ACCEPT as a computer-assisted proof of the statement in C8_eta_cell.md, for eta in E8 = [2499/5000, 2501/5000] and
q0 = 1 only. I found no gap in the method and no error in the code that decides an inequality. Every check I reran
reproduced the logged numbers exactly. Two junctions have thin margins (below); they are correct as computed but any
change to the pieces will break them first.

## What I read

- C8_eta_cell.md in full.
- entry_eta.py in full: the reference xhat + (eta - 1/2) yhat with exact rational Hermite data; segment() (the a priori
  box, the two-variable mean-value enclosure of the defect, the log-norm step, the frame switch); trap().
- chain_check_eta.py in full; widen_eta.cell() in full; from entry.py: up, norm2_up, lognorm_up (Gershgorin on the
  symmetric part, an upper bound of the log norm), opnorm2_up (exact Sylvester minors on lu I - M^T M, then an upper
  square root), expu, frame (float eigenframe; its inverse is computed exactly in rationals, so floats affect only
  sharpness, never soundness), jac_box_centered.
- iv_exact.py lines 1-127: outward rounding in +, *, /, square, sqrt is correct (floor for lower, ceiling for upper,
  correct for either sign of the divisor); the atan series stops with the alternating remainder of the right sign
  and size for x <= 1/5; the half-angle reduction and asin = atan(x / sqrt(1 - x^2)) are correct identities; pi by
  Machin.

## The mathematics checked by hand

- d/dt of the defect and d/deta of the defect: with g = yhat' - f_x yhat - f_eta,
  d_t g = yhat'' - f_xx(x_t, yhat) - f_x yhat' - f_{x,eta} x_t and d_eta g = -f_xx(yhat, yhat) - 2 f_{x,eta} yhat
  - f_{eta,eta}. Both match the code's terms, with x_t taken over the box including its DH * yhat' part.
- The mean-value enclosure in (t, eta) about (t_c, 1/2) over a sub-interval of half-width w h and eta half-width
  1/5000 is valid because every derivative is enclosed over the whole (t, eta) box.
- Trap: res bounds |P*^{-1} f(c(eta), eta)| along the line c(eta) by a mean value in eta, and mu* bounds the log norm
  over the ball and the cell; res < -mu* rho gives an invariant contracting ball with one equilibrium per eta. The log
  shows nsplit 1 failing (mu > 0) and nsplit 2 passing with mu* = -7.534e-4; need_rho 1.8905e-4 < rho 2e-4.
- Link to the plateau: Krawczyk gives a root in each cell's box, the box lies in the trap ball (largest z-radius
  1.6699e-4 < 2e-4), and the ball has one equilibrium, so the trap's limit is the certified plateau root.

## Consistency checks on the drivers (scratch, my own script)

- iv_scm.symmetric_driver and sym4 (full_driver on (q, c, q, r, r, r, r), rows 0, 1, 3) agree exactly in value and
  in d/dx at eta = 1/2 and eta = 2501/5000; sym4_h2 agrees with sym4 to 1e-48.
- d/deta from the jets matches a central difference (step 1e-6) in all three components; the eta columns of the
  second-order jets, h[j][3], h[3][j] and h[3][3] (the eta^2 term), match central differences of the first-order jets
  in all 12 entries to six digits. So the index convention (index 3 = eta) is the one the code assumes.

## Reruns (scratch copy of scripts/, outputs compared with logs/)

- chain_check_eta.py on the logs: output identical to logs/chain_check.txt (CHAIN CLOSED).
- Segments k = 0 (q1, r_in 0), k = 356 (q5, r_in 1/5000) and k = 1045 (q6d, r_in 3/100000): d, mu, R, r, sw and Xw
  identical to the logged rows. Script: c8_rerun_segments.py beside this file.
- The whole piece q6c (nodes 1020 to 1045, r_in 717/25000000): final line identical to logs/q6c.jsonl, exact r_out
  246954426371379/2^63.
- The trap: final line identical to logs/trap.jsonl, including the exact rational mu*.
- Plateau cells 1, 32 and 64 recomputed with widen_eta.cell: 'pass' with info identical to the log.

## Margins

- q6b -> q6c at node 1020: r_out 2.867731e-5 against r_in 2.868e-5, a relative margin of about 1e-4. The partial
  piece's r_out comes from a float row times (1 + 1e-12), which is far below that margin, so the link holds; it is
  simply the first thing to break if q6b is rerun with any change.
- q5 -> q6b: 5.40e-5 against 6e-5. Trap: need_rho 1.89e-4 against 2e-4.

## Not covered by this review

- I did not reread iv_scm.py and iv_h2.py line by line; I checked them against each other and against differences
  (above). They are the same layers C7 used.
- Every other piece rerun from its logged r_in, every segment row compared on d, mu, R, r, sw and Xw (reviewer's
  c8_rerun_all.py, 18 Oct): q6d 24 segments, q6b 320, q5 344, q4 89, q3 89, q2 89, q1 89, with 0 differing rows and
  identical final lines (q6b is the partial piece and has none). With q6c above, every piece of the chain has now been
  rerun and matches its log row for row.
- The statement's scope is as C8 says: other q0, eta outside E8, and post-exit recovery remain open.
