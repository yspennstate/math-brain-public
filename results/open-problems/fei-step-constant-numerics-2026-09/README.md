# Fourier entropy-influence: numerics for the coordinate step, 20-21 September 2026

For a Boolean function f with normalized Walsh spectrum p(S) = fhat(S)^2, entropy H in bits and influences Inf_i,
this folder measures how large a constant the potential-free induction step for the Fourier entropy-influence
conjecture needs. With

    Delta_i H(f) = H(f) - (H(f|x_i=0) + H(f|x_i=1)) / 2,
    min-step   rho0(f) = min over relevant i of Delta_i H / Inf_i,
    total-step tau(f)  = sum_i Delta_i H / I(f),

either statistic bounded by C over all f gives H <= C I by induction on the number of variables (min-step: restrict
the best coordinate; total-step: average over coordinates, using I(f) = Inf_i(f) + (I(f0) + I(f1))/2). Any such C is
at least sup H/I, which is at least 6.4548 by Hod's read-once construction; the best lower bound on that supremum is
6.5218 (Numaro, 2026).

## Results

- All functions of four variables: largest min-step 4.8677, largest total-step 4.9609 (`n4.json`).
- All 2^32 functions of five variables, in two shards (`n5_shard0.json`, `n5_shard1.json` and their logs): largest
  min-step still 4.8677, largest H/I 3.6237, with a histogram of the min-step in quarter-bit bins.
- Hill climbs from structured seeds: 5.2225 at n = 7 and 5.4761 at n = 8 (`search_n7.json`, `search_n8.json`).
- Tribes in closed form (`fei_step_tribes.py`, no enumeration of 2^n points, checked against brute force for
  w s <= 12): the step constant peaks at 6.0037 at width 2 with 8 clauses, then falls (5.599 at w = 3, 5.071 at
  w = 4, 4.63 at w = 5, 4.32 at w = 6, 4.11 at w = 8).
- Lexicographic chains x1 op1 (x2 op2 (...)) up to n = 20 (`fei_lex.py`): H/I <= 3.94, min-step <= 4.87, total-step
  <= 5.14 for periodic and random patterns.
- Read-once formulas by dynamic programming over the gate tree (`fei_readonce_dp*.py`, `fei_readonce_gamma*.py`),
  with the outputs under `search_logs/`.
- Certificates (`fei_cert*.py`, `run_cert_all*.py`, `crosscheck_*.py`): grid certificates for the bounds stated in
  `THEOREM_NOTE.md`, each cross-checked by a second script in mpmath. `PROGRESS.md` is the running log.

The step constant grows with n on these families, so a potential-free induction with a fixed constant does not close
the conjecture by itself; the figures above say how much room each family leaves.

## Credit

The conjecture is due to Friedgut and Kalai (1996). The read-once lower bound 6.4548 is Hod's, the record 6.5218 is
Numaro's, and the first lower bound and the read-once upper bound are O'Donnell, Wright and Zhou's (2011). The scripts
and their reading were produced by AI agents (Claude) and have not been reviewed by a person.

## Running it

`python -X utf8 <script>`; numpy only, mpmath for the certificates.
