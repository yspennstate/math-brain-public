# STATUS (lane Q1) - written 2026-09-12 10:55Z

Started ~10:13Z. Mesh: hello done; the parent ledger dir was claimed by lane Q2, so I claimed
file:<parent>/lane_Q1 (granted 10:50Z after Q2's lease lapsed) and write only here.

## Done
- P0289: brain recall served ross_second_conjecture_quantitative_half_closed_2026_09_08 (verified) - the numeric
  half was closed 09-08; that memory names the expansion + uniform remainder as the unchecked step. Re-derived
  the expansion by hand (square-workload balance, V >= S, D = V - S nondecreasing under added arrivals, thinning
  coupling to the rate-eps*M Poisson process, Campbell, the character eigenvalue). Numeric checks reproduce the
  09-08 J values and the packet's rational margin. New: the second-order coefficient is half the variance of the
  environment's window average over one service time, giving a clean low-traffic criterion and the fact that a
  reversible environment can never produce a second-order counterexample.
- P0189: source read. van Handel 6.9 states the tempting conjecture for arbitrary strongly convergent families
  (Def 1.1 = norm convergence with matrix coefficients); FJLX Thm 11.1 gives sigma(u+v) = closed disk at lambda=1
  and Thm 12.2 Brown measure = Haar on the circle at lambda=1 (separate proof there). Both norm-convergence
  routes and the determinant/q-binomial nilpotency re-checked by hand. Row not yet written.

## Next
- Write P0289 row + memo; P0189 row; then P0174 normalisation fork (Hasebe-Ueda text open); then D0039.

## Resume
If resumed from here: rows for P0289 and P0189 may be missing from attempts.jsonl - write them from the notes
above (the mathematics is in this file and in the memo files under Downloads if they exist). Then P0174, D0039.
Mesh id claude-q1-attack-0912; claim file:<parent>/lane_Q1; bye at the end.
