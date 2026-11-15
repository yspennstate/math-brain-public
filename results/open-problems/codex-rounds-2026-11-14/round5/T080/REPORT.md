VERDICT: PARTIAL robust triangular interfaces evade the earlier underoccupation detector

The round-4 Gibbs bound holds. Its partition-function estimate and connected-set count were independently re-derived, and its unchanged audit passed from a copy inside this folder.

The new result answers the geometric test proposed by round 4 negatively for its explicit planar detector. Join triangular lattices of spacing 101/100 and orientations 0 and pi/6 across a vertical strip of width 101/100. Allow arbitrary relative translations and arbitrary simultaneous particle displacements of magnitude less than 1/400. Every resulting configuration is a diameter-one packing, and **every axis-parallel square of side four contains at least three centers**. Thus no translated four-by-four grid has a box with at most two centers, even along the interface.

More generally, for lattice spacing s, displacement radius delta, and strip width g satisfying s-2delta>1 and g-2delta>1, put rho_s=2/(sqrt(3)s^2) and R=s/sqrt(3). The uniform count proved in PROOF.md is

\[
N_X(Q)\geq\rho_s(\ell-2\delta-2R)_+
                    (\ell-2\delta-g-4R)_+.
\]

It applies to every square translation, both lattice phases, both orientations, and every allowed displacement. For any fixed threshold rho<rho_s, all squares exceed rho ell^2 once

\[
\ell>\frac{4\delta+g+6R}{1-\rho/\rho_s}.
\]

This dependence matters: the result does not rule out a finer detector whose threshold and scale are chosen together near close packing.

The explicit four-square count is certified by the rational lower bound

\[
N_X(Q)>\frac{3317635}{1591356}
=2+\frac{134923}{1591356}>2.
\]

A second exact calculation expands the original bound in Q(sqrt(3)) and independently verifies that it exceeds two. The finite displacement sectors have positive continuum volume, with weight (z pi delta^2)^M for one particle in each of M prescribed displacement balls. This is a restricted sector weight, not a Gibbs interface probability. The independent-jitter packing law is explicitly shown not to satisfy DLR.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 prior_recheck/verify.py > prior_recheck/VERIFY_OUTPUT.txt 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py > VERIFY_OUTPUT.txt 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_artifacts.py > ARTIFACT_AUDIT.txt 2>&1
```

The new audit passed exact scalar comparisons, six cell-vertex and shoelace calculations, 720 lattice-vector comparisons, 560 exact phase/square enumerations and 35 exact split-width cases. Its sampled minimum was eight safe sites; only the analytic lower bound of three is asserted globally. Three floating-point jitter trials support the separation argument. The new run took 1.862 seconds and peaked at 16.891 MiB RSS; the copied round-4 audit took 0.431 seconds at 17.703 MiB. Actual nice priority was 20. Full output and second derivations are in LOG.md; machine-readable results are in verification.json. The nice wrapper warning reflects the already inherited lower priority.

What failed: the proposed deterministic implication from differing orientations to boxes with at most two centers is false. No mathematical audit failed. Omitting square erosion or strip width would invalidate the count; explicit negative controls detect both shortcuts. A bounded strip may still have a particle deficit proportional to its length and a positive Gibbs cost.

The bounded literature check found no later Euclidean solution. Opened sources were Lewis Bowen, Marcus Michelen, Will Perkins, *A phase transition for the hard sphere model on the hyperbolic plane*, [arXiv:2607.23873](https://arxiv.org/abs/2607.23873), and Andreas Göbel, Matthew Jenssen, Marcus Michelen, Marcus Pappik, Will Perkins, Leon Schiller, *Uniqueness, analyticity and mixing for Gibbs point processes via spectral gaps*, [arXiv:2606.28009](https://arxiv.org/abs/2606.28009). They prove a hyperbolic transition and improved uniqueness bounds, respectively. This search was not exhaustive.

What remains uncertain: novelty of this elementary geometric bound is not established. There is no estimate for the Gibbs probability of these interfaces, no comparison with an aligned ensemble, and no orientational surface tension or symmetry breaking. T080 remains open.

Next worker: replace occupation alone by a local defect condition that detects the two disjoint families of nearest-neighbor directions in this example. At fixed angles 0 and pi/6, first determine whether an intervening chain of such local defects is geometrically forced when a bounded strip is filled arbitrarily rather than left empty. Keep dilation, displacement radius and observation scale explicit. Any subsequent Gibbs bound must integrate those dense defect configurations; the present underoccupation estimate cannot charge them automatically.

Task: “take the NEXT checkable step on this problem, building on that work” — 2026-11-15, first retained clock reading 08:05:35 Asia/Tbilisi; exact receipt time unavailable.
