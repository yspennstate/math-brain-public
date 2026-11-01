# Independent review of T240 C9 (post-exit recovery tube to t = 820, trap in the end frame) - agent K, 18 Oct

Files: rows/T240/C9_recovery at fa70aae2; sha256sum -c SHA256SUMS all OK. Nothing in the folder was written to:
both re-runs wrote to my scratch.

1. Chain check re-run (scripts/c9_bcheck5.py on the four logs, env C9_ARB=1 C9_CLUSTER=1 C9_U=99/10000000
   C9_KAPPA=1/500 C9_FACE=section C9_HMAX=0.5; 16 s): CHAIN OK. The rows, v_end, max R and r_end_exact lines
   are identical to logs/finish_5.out: rows 200 / 400 / 288 / 798, r_end = 760573860451/2^62 = 1.6492e-07,
   max R 4.4038e-04.
2. The three junctions are the checker's own assertions, and all held on the re-run:
   - K1 (bfull14 -> brst10): brst10's v_in dominates bfull14's exact vx at row 199, ratio 1.000000.
   - K2 (brst10 -> flow599): exact switch.
   - K3 (flow599 -> plain888g8, DELTA 0.02 -> 0.01): radii carried by switch() from flow599's exact vx at row 887
     equal plain888g8's logged v_in and blocks_in, exactly.
   - Every row is contiguous and none is marked failed (rows_upto asserts both).
3. Trap re-run (c9_run.py trap 820 0.004 r_end, C9_FLOWCOL=0 C9_DELTA=0.01 C9_TRAP_FRAMEB=1; 3 min): the output
   is identical to logs/trap_plain888g8.jsonl, two rows, PASS at rho = 1/10000, nsplit 1,
   mu = -0.0073156 (an exact rational in the log), residual 5.8e-46.
4. Exit margin, recomputed by hand: need_rho = offset + sw * r_end = 4.10705e-05 + 1.0000109 * 1.64923e-07
   = 4.12354e-05, which matches the logged need_rho. Margin: rho - need_rho = 5.88e-05, so rho is 2.43 times
   need_rho. r_end is 1.65e-07, about 300 times below the 5e-05 bound the draft's step 4 states for the trap.
5. The fsolve "xtol too small" warning comes from c9_cone.plateau_float, the float seed. Its only use is as the
   centre for krawczyk(xs, 1/10^9), which asserts ok, and as the float input of adapted_frame. Neither use is
   part of a validated bound, so the warning is harmless.

Verdict: ACCEPT the chain and the trap as filed.
Scope: these re-runs are independent in execution, not in method. They run the lead's own code on the lead's
logs, so they show the files are consistent and reproducible, not that the code is correct. I did not re-read
c9_blocks.py (the block tube's Metzler comparison), c9_flow.py or c9_run.py's bpiece line by line. In C8 I read
the shared helpers (iv_exact jets aside), and the C8 review stands on them. A line-by-line read of c9_blocks.py is
the remaining step before the block bound itself counts as independently checked.

## Addendum, 14:5x: c9_blocks.py and its c9_flow helpers read line by line

These helpers are c9_flow's own copies, not the C7 entry.py functions I read for C8, so I read them here too:
up, hermite_coeffs, poly_range, lognorm_up, norm2_up, invert_rational, posdef, opnorm2_up, f_point, jv_box,
jac_box and drv. No logical gap found. Checked:
- hermite_coeffs: p(1) = p1 and p'(1) = d1 by hand. poly_range is the exact centred Taylor form. In segment_b the
  reference velocity is scaled by 1/h and its acceleration by 1/h^2.
- Defect. On each sub-interval: g(t) in g(t_c) + g'(xi)[-wh, wh], with g' = xhat'' - J(xhat) xhat'. J(x) xhat' is
  split as jv_box(X, Vc) + Jhull (V - Vc), and X lies inside the whole-segment hull Xh, so the split is sound.
  dvec is the maximum of |(P^{-1} g)_b| over the sub-intervals.
- Comparison system: z = P^{-1}(x - xhat), z' = M z - P^{-1} g with M in the hull of P^{-1} J(E) P, E convex.
  D+ |z_b| <= mu(M_bb)|z_b| + sum_c ||M_bc|| |z_c| + d_b. mu comes from Gershgorin on the interval symmetric part,
  and the off-diagonal blocks use a Frobenius bound, so the matrix is Metzler and the Mueller/Kamke comparison
  applies. B = A + cI >= 0 gives v(h) <= e^{-ch} e^{Bh} v0 + h e^{Bh} d, matching the code term by term.
  vmax = e^{Bh}(v0 + h d) bounds v on all of [0, h], because e^{Bt} is monotone for B >= 0. The a priori test
  vmax < R with E = X + sum_b |P_.b| R_b is the standard continuation argument.
- expB_up: scaling to infinity-norm < 1/2, Taylor to K = 12 with tail nrm^K / (K!(1 - nrm)) per entry, then squaring
  with nonnegative entries. All sound. emc = 1/(Taylor partial sum) >= e^{-x}.
- LNSUB grouping: group g covers sub-intervals [g n/G, (g+1) n/G), i.e. times [g h/G, (g+1) h/G]. The defect bound
  is the whole segment's (a superset) and v propagates group to group. Sound.
- switch: ||T_{bn,bo}|| from opnorm_rect_up (lu I - M^T M positive definite by exact LDL^T, then sqrt rounded up).
  Sound.
- reset_b, used in brst10 (22 resets up to row 599) and flow599 (148):
  - The identity phi_tau(x) - xr = (I - g n^T)(x - xr) + int_0^tau (f - g) holds for any n, so the FLOWCOL choice
    n = s (row 0 of P^{-1}) is legitimate.
  - |tau| <= sum ||c_b|| v_b. The Picard box check (new strictly inside B, T symmetric) encloses the flow for
    |s| <= tau_m, and the integral lies in T (f(B) - g).
  - The linear part is split as amid + aerr, with the aerr term bounded by ae ||c_bo|| v_b >= ||aerr|| |c^T z|.
    Sound.
- frame_b, frame_c and flow_adapt only choose an invertible rational frame. Any choice is valid, so the float
  eigen-solves carry no soundness weight.

Two scope points for the write-up. Neither is a gap in the computation.
(a) The resets make each trajectory's time shift up to sigma = 0.0518. That is the logged cumulative 'shift' at row
    1685, 0.051730315; it carries brst10's 0.0012 into flow599. So the tube's end set is reached by time
    820 + sigma, not 820. Forward invariance of the trap ball makes this harmless, but the glue window in (G)
    should read T_end + sigma + T_trap. The draft names the shift only in step 3.
(b) C9 holds for eta in E = [0.4999999999, 0.5000000001] (iv_scm's ETA, as the draft says), not for C8's cell
    [2499/5000, 2501/5000]. A C8 -> C9 glue is valid only on E.
Not read: c9_cluster.frame_c's internals (no soundness weight, as above) and the iv_scm/iv_exact jet arithmetic,
which C6-C8 share.
Verdict unchanged: ACCEPT. With this addendum the block bound itself is independently checked, not only re-run.
