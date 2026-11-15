VERDICT: PARTIAL sharp bounds for matching boundary currents on nested circuits

The two-dimensional values of d_s and d_w remain unidentified. The bounded
literature check found no newer solution. The opened arXiv page for Irina
Đanković, Maarten Markering, Jason Miller, Yizheng Yuan, *The scaling limit
of random walk and the intrinsic metric on planar critical percolation*,
[arXiv:2604.14122](https://arxiv.org/abs/2604.14122), still lists only v1.
Its Corollaries 1.3–1.4 and “Explicit lengths” discussion leave beta_res
unidentified. This does not decide Alexander–Orbach.

The round-3 result holds. An independent prescribed-divergence calculation
with exact rational LDL^T factorization reproduced all 255 earlier interface
cases, the 210 positive corrections, 729 weighted-star cases, and all 11
sharpness-family values. The latter agree exactly with the saved round-3
data. Its asymptotic factor 2 was also re-derived from the path upper bound
and corrected contraction lower bound. Earlier folders were only read.

The new piece in PROOF.md resolves the circuit-boundary case proposed by
round 3. Write A for the sum of separately wired layer resistances and
delta_i for the mismatch of their optimal currents on interface circuit C_i.
Then

    0 <= R_full-A <= sum_i Q_{C_i}(delta_i).

The coefficient 1 is sharp. All circuit edges carry zero current in the
local wired optima, and repairs on distinct circuits use disjoint edges.
Consequently no factor 2 is needed. All shell components are retained.
Circuit edges can even be split between adjacent layers: the bound works
when BOTH of the previous ordinary interface diameters are infinite.
Assigning a complete circuit to its inner layer guarantees a finite
diameter on that side, answering the previous connectivity question.

For a circuit with edge resistances rho_j, let H_j be the cumulative signed
mismatch in cyclic order, W=sum rho_j, and Hbar=sum rho_j H_j/W. The exact
repair energy is

    Q_C(delta)=sum_j rho_j(H_j-Hbar)^2 <= (W/4) TV(delta)^2.

It takes linear time to evaluate once the boundary profiles are known.
The actual demand matters: on an even unit circuit of length N, an
alternating demand of total variation 1 has energy 1/N, whereas an
antipodal unit dipole has energy N/4. This bound need not dominate the
previous harmonic diameter bound, since circuit-only repairs ignore
interior shortcuts.

A checked obstruction shows the limitation of circuit connectivity. Two
nested unit circuits, each of length 2L, with antipodal entry and exit
vertices and three connecting unit bridges, have

    A=3,  R_full=L+3,  R_full-A=Q_total=L.

The graph is planar, has maximum degree 3, and attains the circuit bound.
Thus nested circuits alone do not give a universally bounded gluing ratio.
This is an abstract planar network example, without an IIC probability
estimate or a prescribed triangular-lattice embedding.

Verification command, from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_circuits.py
```

All exact checks passed. Beyond the earlier cases, these include 1,222
weighted-circuit/demand tests, all 3,600 square-interface networks with
nonempty terminal-neighbor sets and arbitrary circuit-edge ownership,
336 nested-circuit networks, and five sizes of the obstruction family.
Among the square cases, 328 have both old diameters infinite; 656 attain
the circuit bound, including 240 with zero correction. These counts have
separate combinatorial or voltage-based checks. The script verifies the
actual repaired flows as well as the resistance inequalities. Full output
is circuit_results.json; commands and audits are in LOG.md.

Final run: 2.9471 seconds, peak RSS 17,334,272 bytes, one process, standard
library only, single-thread environment, CPU/wall limits 90/120 seconds.
The nice command warned that setpriority was denied; inherited nice 20
was checked. There were no failed mathematical tests.

What failed: circuit connectivity does not itself control the gluing ratio,
as the equality family proves. What remains uncertain: no probability or
tail estimate on circuit mismatch energies, no improvement to beta_res,
and no decision on d_s=4/3. No percolation sample or exponent fit was made.
The literature check is bounded, and prior publication of these elementary
network consequences was not investigated systematically.

Next worker: choose nested open circuits in a finite origin-to-distance-R
conditioned triangular-lattice cluster, recording the selection rule and
all conditioning. Retain all shell components and compute, in each SAME
realization, A and C=sum_i Q_{C_i}(delta_i) using the cumulative formula.
Record circuit lengths, TV mismatches, and their cumulative-current variance
separately; the latter can be much smaller than length times TV squared.
The target sufficient estimate is C<=R^{o(1)} A, jointly with an identified
exponent for A. Selection of circuit scales and comparison with ball exit
resistance also need justification. This session supplies no evidence that
the probabilistic target holds; a repair using interior paths may be
necessary if the circuit bound is too large.

Task: “take the NEXT checkable step on this problem, building on that work” —
session start 15 November 2026, approximately 04:52 Asia/Tbilisi.
