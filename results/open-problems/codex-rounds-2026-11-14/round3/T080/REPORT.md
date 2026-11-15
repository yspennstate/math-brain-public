VERDICT: PARTIAL uniform Gibbs bounds for completely vacant thick seams

The earlier quantitative mixing-packing result holds. An independent tagged-nucleus calculation recovers its exact density formula. A new numerical audit compares that formula with a conditional second-arrival integral in dimensions 2, 3, 4, and 8: 24 comparisons agree within 3.34e-16. Its geometric separation, mixing constant, and limiting quantifiers also survive re-check.

The new piece is a restricted version of the requested interface partition-function estimate. PROOF.md proves, for a rectangular seam S, activity z, and every admissible exterior eta,

\[
m\log(1+zv_da^d)
\leq-\log\Pr_\eta(S\text{ empty})
\leq\log\sum_{n=0}^M\frac{(z|S|)^n}{n!}
\leq U(z|S|,M).
\]

Here m counts explicit radius-a insertion balls, separated by 1+2a and protected from the exterior by center-to-boundary distance 1+a; M is an explicit packing-number upper bound. The function U(T,M) is T for T<=M and M[1+log(T/M)] for T>M. Every selected particle displacement is integrated, including the Gibbs factorial. Conditioning extends the bounds to arbitrary surrounding finite volumes and all infinite-volume Gibbs measures.

For a fixed seam width W>=2(1+a), the negative log empty-seam probability is bounded above and below by explicit positive multiples of area times log z at high activity. The proof also permits insertion sites from any slightly dilated periodic packing, in any chosen orientation, using a suitable phase. An optional upper cap uses the unrestricted optimal packing density from the earlier result.

The width restriction cannot simply be dropped: an exterior unit-spaced planar row blocks every potential center in a strip of width less than sqrt(3)/2. Its empty probability is exactly one at every activity. This obstruction is proved explicitly.

Reproduce from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py > VERIFY_OUTPUT.txt 2>&1
```

The successful run took 0.030 seconds and peaked at 15.188 MiB RSS, with actual nice priority 20. It passed the density checks, 81 exact rational grid-threshold checks, exact factorial cancellation, 48 independent truncated-exponential/tilt comparisons, and six seam examples. Full output and independent hand checks are in LOG.md; data are in density_audit.csv, seam_bounds.csv, and verification.json. Numerical checks support the analytic proof and are not interval certificates.

What failed: two initial audit launches stopped before computation because this managed Mac rejected address-space/data resource-limit changes. The final script keeps a 60-second CPU limit, uses small fixed lists, and records peak memory; it does not claim an enforced address-space cap. The nice wrapper warns because inherited priority is already 20. Extending a positive boundary-uniform bound to arbitrary thin seams fails by the blocking example.

The bounded literature check found no solution after the earlier report. Opened sources were Lewis Bowen, Marcus Michelen, Will Perkins, *A phase transition for the hard sphere model on the hyperbolic plane*, [arXiv:2607.23873v1](https://arxiv.org/html/2607.23873v1); Andreas Göbel, Matthew Jenssen, Marcus Michelen, Marcus Pappik, Will Perkins, Leon Schiller, *Uniqueness, analyticity and mixing for Gibbs point processes via spectral gaps*, [arXiv:2606.28009](https://arxiv.org/abs/2606.28009); and Biman Bagchi, *From Freezing to Terminal Packing: A Puzzle and a Paradox*, [arXiv:2608.29676](https://arxiv.org/abs/2608.29676). These concern a hyperbolic transition, uniqueness bounds, and a density-functional framework respectively. None proves Euclidean Gibbs freezing.

What remains uncertain: no novelty claim is established for this elementary Gibbs insertion bound. A general orientation defect need not contain a completely vacant region of the required width. No comparison with a healed interface, Peierls estimate, symmetry breaking, or long-range orientational order is proved. T080 remains open.

Next worker: define an interface ensemble allowing continuum displacement on both sides of two differently oriented, slightly dilated periodic regions. Compare its integrated partition function with an aligned ensemble while keeping a common exterior and changing only a bounded strip. Prove a positive cost proportional to area without assuming that strip is completely vacant; the blocking example explains why protected insertion alone cannot do this.

Task: “take the NEXT checkable step on this problem, building on that work” — 2026-11-15, first retained local clock reading 01:19:29 Asia/Tbilisi; exact receipt time unavailable.
