# T104, connected five-vertex graphs at D = 2: the STRAT8 residual closed (STRAT14)

Status on 13 Nov 2026, 10:33 local. The connected n = 5, D = 2 stratum is proved.

## Statement

For every symmetric nonnegative system of five-vertex edge weights with total weight one, connected carrier and
largest Laplacian eigenvalue of multiplicity exactly D = 2, the T104 quantity satisfies T >= 0
(strat14/RESULT.md gives T = X1 + X2 + X3 - 2 S5 in full). With STRAT4 (disconnected endpoints, the only equality
types being the balanced triangle plus two isolates and two edges of weight 1/2 plus an isolate), STRAT5 (r <= 3/25),
STRAT5 and STRAT6 cells (r > 3/25, a <= 103/200), STRAT8 together with this run (r > 3/25, a > 103/200) and the radial
identity for smaller scales, every endpoint region of the stratum has an exact replay.

## What STRAT14 did

The n = 5 target is the all-N polynomial of STRAT10 at N = 5: C_N(-1) = 2 Cface coefficientwise, with
C_N(q) = 10(N-2)^2 D^2 Delta T_N, so T5 = Cface/(45 D^2 Delta) (strat14/verify_targets.py). Positivity at N = 6 gives no
sign for N = 5, so the certificates were recomputed against Cface.

- Local bounds at the two equality types, in the chart h = (x,y,k,p,q,v,z) of STRAT13: two edges T5 >= ||h||_1/20 for
  ||h||_1 <= 1/520, triangle T5 >= ||h||_1/12 for ||h||_1 <= 1/600; in matrix terms T5 >= ||S - S_P||_max/40 on radius
  1/20800 and T5 >= ||S - S_P||_max/24 on radius 1/25800 (strat14/verify_local.py, multipliers checked for all 128 sign
  vectors in each chart).
- Nine exact zero witnesses, coordinates in Q(sqrt 5) and Q(sqrt 15), one in each of the STRAT8 OPEN leaves 12437,
  12643, 13871, 14683, 14814, 17328, 17952, 18124, 18548. They are disconnected equality points, not counterexamples, and
  no strict certificate exists on a box containing one (strat14/verify_limits.py).
- Bernstein certificates with Farkas multipliers on the STRAT8 necessary constraints, splitting to depth 73: the 5,272
  OPEN leaves become 8,227 positivity leaves, 3,729 exclusions and 14 collar leaves, 6,698 splits, no OPEN leaf
  (strat14/certificates.json, verify_partition.py).
- Final ledger of the canonical root: 32,929 positive leaves, 13,937 exclusions, 14 collars, 46,879 splits, volume 1152,
  zero OPEN. replay_all.py passed all 17 stages in 606 s on Mac mini 1, with STRAT8 replayed byte-identical first.

The constraint scale14 = 40000(tau^2 - 4 Delta) - (103 D - 200 tau)^2 is used only on boxes where 103 D - 200 tau >= 0
holds throughout; there it is the complement of the region STRAT8 sets aside as proved by STRAT6 (largest gap at most
103/200), so it is a valid premise.

## Independent checks

strat14_check/my_replay14.py writes the 25 necessary constraints from the formulas in STRAT8 cover_face.necessary()
and takes the target from STRAT8 zero_face.construct(), divided by 80; both agree exactly with what STRAT14 used. It
then checks, with its own substitution and tensor Bernstein code in Fractions only, that each of the 5,272 record trees
partitions its STRAT8 box (exact volume sums, leaf boxes recomputed from the split axes), and recomputes the residual
and its Bernstein minimum on 140 leaves: 60 positivity and 60 exclusion leaves at random (seed 7) and the 10 deepest of
each kind. 140 of 140 pass (strat14_check/my_replay14_120.out).

strat14_check/my_collar14.py draws 400 exact rational points in each of the 14 collar leaves, half of them pulled
toward a box vertex. At the 239 points satisfying every necessary constraint (and lying outside the STRAT6 region) the
target is positive at all of them (strat14_check/my_collar14.out). Two collar leaves had no feasible sample; this check
corroborates the local bounds and does not replace verify_local.py.

The tarball sha256 6c8af48a2f4d1b57079f7fa09322efaec249c690c791147647ae8a88b254f9d7 matched on both machines
(strat14_check/remote_sha14_final.txt).

## What is still open in T104

The 5+1 class for N >= 7 (region (11) is proved at N = 6 only), and connected carriers with n >= 6.
