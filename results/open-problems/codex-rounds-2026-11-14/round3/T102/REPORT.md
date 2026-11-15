VERDICT: PARTIAL sharp bounds for boundary-current matching costs

The values of d_s and d_w, and the two-dimensional Alexander–Orbach question,
remain open. The five-minute literature check located no newer solution.
The opened arXiv page for Irina Đanković, Maarten Markering, Jason Miller,
Yizheng Yuan, *The scaling limit of random walk and the intrinsic metric on
planar critical percolation*, [arXiv:2604.14122](https://arxiv.org/abs/2604.14122),
still lists only v1. Corollaries 1.3–1.4 express the triangular-lattice IIC
exponents in terms of the unidentified beta_res.

The earlier gluing identity and obstruction hold. They were re-derived from
energy orthogonality and independently checked with unit-voltage Dirichlet
solves. All 255 earlier interface configurations, including the 210 positive
corrections, and all seven earlier cycle values agree exactly. The previous
folder was only read.

The extension in PROOF.md gives an explicit upper bound on the earlier
matching cost. For two connected pieces, write t for the total variation
between their optimal interface-current profiles and a,b for the ordinary,
UNWIRED resistance diameters of that interface inside the two pieces. Then

    D_2 <= [ab/(a+b)] t^2.

Equality holds for every two-vertex interface. For several layers, let
k_i=a_i b_i/(a_i+b_i) and let t_i be the adjacent profile mismatch. Then

    D_m <= 2 sum_i k_i t_i^2.

The factor 2 is optimal, even for three planar layers of unit resistances
and maximum degree 3. An explicit family satisfies D_3/(sum_i k_i t_i^2)->2.
The proof also permits disconnected layers when each nonzero mismatch can
be repaired on at least one side having finite resistance diameter.

Consequently an annular approach can replace the previous condition on the
abstract minimum D_m by the sufficient estimate

    sum_i k_i t_i^2 <= 2^{o(m)} sum_i R_i.

Together with sum_i R_i=2^{mb+o(m)}, this transfers exponent b to the rooted
resistance along dyadic scales. No such estimate is proved for the IIC.
These are consequences of minimum energy and a boundary transport argument;
no claim of a new general electrical-network principle is made.

Verification command, run from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_matching.py
```

All exact checks passed: the earlier cases above; 729 pairs of weighted
three-arm stars; 128 three-layer strips; 11 sharpness-family cases; and the
previous disconnected example. At L=1024 the sharpness ratio is
1.9970760280. Its full resistance agrees with a separate two-variable flow
minimization, and its asymptotics follow from a path upper bound and a
Rayleigh-contraction lower bound. Complete rational output is in
matching_results.json; commands and audit details are in LOG.md.

The final run used one process, standard-library rational arithmetic,
15,810,560 bytes peak RSS, and 0.3646 seconds. The requested nice command
warned that setpriority was denied; the program verified inherited nice 20.
The single-thread environment and 90-second CPU/120-second wall limits were
checked or set by the script.

What failed: coefficient 1 in the many-layer bound is false; repairs can
reinforce on a shared edge. During audit, the first quotient-network count
in the sharpness proof was found incorrect and replaced by contracting all
four unit edges. The corrected lower bound is (1/L+2/K)^(-1); the exact
network computations and limiting coefficient are unchanged.

What remains uncertain: no probability bound on these mismatch energies,
no improvement to beta_res, and no decision on d_s=4/3. Worst-pair unshorted
diameters may be too coarse, or infinite, for ordinary IIC shells. The
bounded literature search cannot certify absence of later work, and the
network inequalities have not been checked for prior publication.

Next worker: test a decomposition at nested open circuits, retaining all
shell components. First check whether at least one adjacent shell connects
each circuit boundary. For each interface compute t_i and the smaller finite
unshorted diameter, then compare sum_i k_i t_i^2 to sum_i R_i in the SAME
realizations. If worst-pair diameters dominate, use the dipole-coupling
bound in PROOF.md Section 2 on the actual signed mismatch instead. A
percolation tail estimate, rather than another scalar resistance identity,
is the missing step. This report gives no evidence that the needed ratio
is subpolynomial.

Task: “take the NEXT checkable step on this problem, building on that work” —
session start 15 November 2026, approximately 01:28 Asia/Tbilisi.
