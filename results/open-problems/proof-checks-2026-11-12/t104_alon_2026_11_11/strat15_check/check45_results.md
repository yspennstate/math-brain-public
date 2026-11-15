# STRAT15 checks 4 and 5 (an agent, 13 Nov 2026)

Bank: certificates.json sha256 60441b5e0e5d7771f3d91e5b9d9904e7609b079361f6665df04835666ee710e2,
refinements.json sha256 8ab45400bc540bd8432452eb204101f490311991115147b6e2d7b02e0fc53acf (both equal READY.json).

## Check 4: coverage, partition, certificates (my_check4.py, check4_full.out)

- The 9,370 inputs (inventory non-collar records plus the 1,004 domain-audit boxes needing a new sign) each appear once in
  the bank with the identical rational box. 9,357 close in the bank; the 13 open ones each have a refinement tree.
- Every refinement split is the midpoint of the stated axis, leaf volumes sum exactly to the root volume, no open leaf.
  9,375 certificate leaves in all (9,357 + 18).
- 58 leaves re-verified with my own polynomial and tensor Bernstein code (Fractions only), targets c2, d1 = c1 + 2c2,
  C1 = c0 + c1 + c2, constraints written from the formulas, scale14 allowed only where 129D - 250tau >= 0 on the box:
  all 18 refinement leaves and 40 random bank leaves (seed 11), three certificates each. 174 of 174 pass, 455 s.
  The bank's 'absolute-envelope' certificates were checked by the full Bernstein minimum, a stronger test.

## Check 5: collar samples for every N (my_check5.py, check5.out)

Corroboration of local_uniform.py, not a replacement. In each of the 17 STRAT13 collar boxes: random points, points
pulled to vertices, and float minimisers of C_7 and c2 rounded to rationals. A point counts when every N-free
constraint and ratio >= 0 hold and it is outside the a <= 129/250 region proved elsewhere. 176 points counted.
C_N(q)/(q+1)^2 evaluated exactly at N = 7, 8, 10, 20, 100, 10^6 and c2 (N -> infinity): no negative value.
Minima 0.724 (N=7), 0.515, 0.371, 0.247, 0.201, 0.193 (N=10^6), c2 0.193, reached near the equality centres of
nodes 12091 and 20736, where T_N tends to 0. The corner ball was not sampled; local_uniform covers it by radius.

## Earlier checks (check1_reasons.md, check23_design.md)

1a sound (N-free exclusions), 1b 7,267/7,267 weaker-Farkas transfers pass with a negative control, c0, c1, c2 equal the
STRAT10 numerator by q power and c0 - c1 + c2 = (1/4) x the STRAT8 face numerator.
