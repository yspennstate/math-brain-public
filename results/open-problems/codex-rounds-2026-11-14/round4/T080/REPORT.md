VERDICT: PARTIAL uniform exponential bounds for connected underoccupied regions

The earlier density construction and vacant-seam estimate hold. The round-3 audit was rerun unchanged from a copy inside this folder, and its main inequalities were independently re-derived in LOG.md.

The new piece allows particles in the defect and sums over its possible connected shapes. Partition space into boxes of side ell. Suppose each box admits m_0 mutually compatible protected insertion balls of volume b. Set v=ell^d and choose 0<r<m_0. For zv>=r, define

\[
\tau=m_0\log(1+zb)-r[1+\log(zv/r)],\qquad
q=(2d)^2e^{-\tau}.
\]

For any prescribed n boxes, the probability that their union contains at most rn centers is at most exp(-n tau), capped at one. All continuum displacement variables are integrated. A canonical tree traversal bounds the number of connected n-box sets containing a fixed box by (2d)^(2(n-1)). Consequently, in every infinite-volume hard-sphere Gibbs measure,

\[
\Pr\{|K(j)|\geq n\}\leq
\min\{1,q^n/(2d)^2\},
\]

where K(j) is the face-connected component of boxes with at most r centers containing box j. Thus q<1 excludes infinite underoccupied components. Finite-volume versions use only boxes wholly inside the sampling region and are uniform over admissible fixed exteriors.

For ell=4 and insertion radius a=1/4, the following rigorous sufficient constants use only pi>3 and e<3:

| Dimension | Maximum count in an underoccupied box | Sufficient activity | Bound on q |
|---|---:|---:|---:|
| 2 | 2 | z>=4096 | 4/9 |
| 3 | 4 | z>=65536 | 729/16384 |

More generally, for every fixed number-density threshold 0<rho<rho_*, periodic insertion families permit a box size and activity threshold for which the same exponential component bound holds for boxes containing at most rho ell^d centers. These choices are not uniform as rho approaches the optimal packing density rho_*.

Reproduce both audits from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 prior_recheck/verify.py > prior_recheck/VERIFY_OUTPUT.txt 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py > VERIFY_OUTPUT.txt 2>&1
```

The new audit passed 3,072 exact weighted-graph comparisons, 150 floating-point tilt comparisons, two independent enumerations of connected sets, and exact rational checks of both stated activity bounds. Anchored connected-set counts were 1,4,18,76,315 in d=2 through size five and 1,6,45,344 in d=3 through size four. The run took 0.271 seconds, peaked at 16.219 MiB RSS, and confirmed actual nice priority 20. PROOF.md contains the analytic argument; LOG.md contains commands, complete output, and attempts to break it. Floating-point checks are not interval certificates. The copied earlier audit passed in 0.030 seconds at 15.625 MiB RSS.

What failed or required correction: the sufficient bound is uninformative for the tested d=3, z=10000 case. The finite-volume component statement needed an explicit restriction to boxes inside the sampling region; including arbitrary exterior boxes would be false. The corrected proof includes that restriction. No new computation failed. The nice wrapper warns because the inherited priority is already 20.

The five-minute literature check found no later Euclidean solution. Opened sources were Lewis Bowen, Marcus Michelen, Will Perkins, *A phase transition for the hard sphere model on the hyperbolic plane*, [arXiv:2607.23873](https://arxiv.org/abs/2607.23873), and Andreas Göbel, Matthew Jenssen, Marcus Michelen, Marcus Pappik, Will Perkins, Leon Schiller, *Uniqueness, analyticity and mixing for Gibbs point processes via spectral gaps*, [arXiv:2606.28009](https://arxiv.org/abs/2606.28009). They concern a hyperbolic transition and improved uniqueness bounds, respectively. Neither settles Euclidean freezing. This bounded search is not exhaustive.

What remains uncertain: novelty of this elementary Gibbs estimate is not established. A dense orientation interface need not be underoccupied at the chosen scale or threshold. No comparison with an aligned interface, positive orientational surface tension, orientational order, or translational symmetry breaking is proved. T080 remains open.

Next worker: test the missing geometric implication for two fixed, non-equivalent planar triangular-lattice orientations, allowing continuum displacements and relative shifts on both sides of a bounded strip. Determine whether the interface forces enough underoccupied boxes for this bound to apply, or exhibit an interface that evades such a count. Any positive claim must retain its dependence on orientation angle, dilation, and box scale. The present result supplies the Gibbs weight and shape count only after an occupation deficit has been established.

Task: “take the NEXT checkable step on this problem, building on that work” — 2026-11-15, first retained clock reading 04:41:23 Asia/Tbilisi; exact receipt time unavailable.
