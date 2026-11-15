VERDICT: PARTIAL exact resistance-gluing reduction and planar obstruction

The values of d_s and d_w remain open. The bounded literature search found
no solution or substantial advance beyond the supplied brief. The opened
paper by Irina Đanković, Maarten Markering, Jason Miller, Yizheng Yuan,
*The scaling limit of random walk and the intrinsic metric on planar critical
percolation*, [arXiv:2604.14122](https://arxiv.org/abs/2604.14122), has only
v1 listed. Corollaries 1.3–1.4 leave the resistance exponent unidentified.

The completed piece is in PROOF.md. For two connected networks meeting at
an interface, it proves

    R_full = R_A + R_B + D,

where R_A,R_B are the separately wired resistances and D is an explicit
nonnegative quadratic cost of matching their optimal interface currents.
It also gives an exact version for several layers, allowing disconnected
annular pieces, and a sufficient estimate for transferring an annular
resistance exponent to the rooted resistance exponent.

A simple planar unit-resistance cycle gives

    R_A=R_B=L/(L+1),   R_full=(L+1)/2,
    D=(L-1)^2/[2(L+1)].

Consequently no universal constant bounds R_full by the sum of the separately
wired resistances, even at maximum degree 2. This is an obstruction to a
scalar gluing argument, not a counterexample to an IIC probabilistic estimate.
The identities follow from the standard minimum-energy principle; no novelty
claim is made for that principle or its quadratic consequences.

Verification command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_gluing.py
```

All exact rational checks passed: seven cycle sizes, all 255 connected
configurations in the specified three-vertex-interface family, and a
disconnected middle layer. Full-network Kirchhoff solves agreed with local
quadratic composition. An independent combinatorial count gives 255 cases,
including 210 with positive correction. Cycle numbers were independently
re-derived by series/parallel reduction. Data are in cycle_data.csv,
interface_data.csv, and validation_summary.json; commands and outputs are
in LOG.md.

The final run took 0.168 seconds and peaked at 17,039,360 bytes RSS. The
requested nice command warns that setpriority is denied; a direct check
confirms inherited nice 20. Computation used one process and the Python
standard library. Initial attempts to set AS and DATA memory limits failed
before calculation; the successful run checked actual peak RSS. CPU and
wall-time limits were 90 and 120 seconds.

What failed or remains uncertain: no quantitative control of the matching
cost under the IIC law was obtained. The reduction provides no sharper bound
on beta_res and does not decide Alexander–Orbach. The cycle example has no
IIC probability estimate, and the search cannot certify absence of all
later work.

Next worker: for a dyadic decomposition of one IIC realization, retain all
shell components and study the correction D_m defined in PROOF.md (5).
To transfer a candidate scalar shell exponent b>=0, it suffices to establish
sum_i R_i=2^{mb+o(m)} and D_m<=2^{o(m)}sum_i R_i almost surely. A proof with
b>91/96 would imply d_s<4/3 using the existing Einstein relations. Neither
of those two IIC estimates is established here.

Task: “push this problem forward by one checkable piece” — session start
14 November 2026, approximately 21:59 Asia/Tbilisi.
