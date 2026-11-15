VERDICT: PARTIAL quantitative near-optimal mixing packings; the Gibbs freezing problem remains open

PROOF.md proves that in every dimension d >= 2, stationary, isotropic, translation-mixing sphere-packing laws can have intensity arbitrarily close to the unrestricted packing optimum. The result concerns unrestricted packing laws, not Gibbs measures. It gives a concrete obstruction to proving freezing from density and packing geometry alone.

For a periodic packing of intensity rho_P and Poisson grain-nucleus intensity lambda, the constructed law has intensity rho_P q_d(t), where

\[
t=(\lambda v_d)^{1/d},\qquad
q_d(t)=d\int_0^\infty u^{d-1}e^{-(u+t)^d}\,du
\geq 1-d\Gamma(2-1/d)t.
\]

For bounded local observables in radius-a windows separated by R > 8a, connected correlations are at most 8(1+m)exp(-m), with m=lambda v_d(R/4)^d. The proof gives a planar bond-orientation example, proves periodic approximation of the unrestricted optimum, and certifies that contact-containing instances are not finite-activity Gibbs laws. Mixing is asserted at each fixed grain scale; the estimate degenerates as the density approaches optimal.

The qualitative Euclidean density obstruction is already known. Section 1.4 of Lewis Bowen, Marcus Michelen, Will Perkins, *A phase transition for the hard sphere model on the hyperbolic plane*, [arXiv:2607.23873](https://arxiv.org/html/2607.23873v1), states equality of optimal and optimal Poisson-factor densities in Euclidean space. The contribution here is an explicit construction, density formula, and correlation bound, with no claim that these are new to the literature. Independent marks are used; the proof does not identify this construction with an unmarked Poisson factor.

The bounded literature check found no Euclidean high-density Gibbs ordering theorem. Two 2026 papers add context omitted from the brief: the hyperbolic theorem above, and improved uniqueness bounds in Andreas Göbel, Matthew Jenssen, Marcus Michelen, Marcus Pappik, Will Perkins, Leon Schiller, *Uniqueness, analyticity and mixing for Gibbs point processes via spectral gaps*, [arXiv:2606.28009](https://arxiv.org/abs/2606.28009). Both precede the brief's November 2026 status date and neither settles its Euclidean freezing statement. No SOLVED_ELSEWHERE.md was written.

Reproduce the numerical audit from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py > VERIFY_OUTPUT.txt
```

The corrected run passed in 0.222 seconds with peak RSS 27.109 MiB. Actual inherited nice priority was 20; the nice wrapper reported that it could not lower priority further. The script checks priority >= 15 and limits CPU time to 60 seconds. Outputs are q_table.csv, verification.json, and VERIFY_OUTPUT.txt; the complete output is also in LOG.md.

The audit compared integral and closed-form expressions in dimensions 2 and 3 (largest observed difference 2.50e-16), independently evaluated the loss constant in dimensions 2, 3, 4, and 8, and checked the radial-order-statistic interpretation with 200,000 samples per dimension. The original one-panel adaptive quadrature missed a peak and failed; a fixed initial mesh corrected it. This failure and the priority warning are retained in LOG.md. Floating-point and pseudorandom checks are supporting audits, not proof certificates. Geometric separation, density normalization, constants, covariance factors, guard bands, and limiting quantifiers were also checked independently in LOG.md.

What remains uncertain: no novelty claim is established, and no estimate for high-activity Gibbs probabilities of grain boundaries is proved. The construction has exact-contact singularities and does not supply a Gibbs competitor or a Gibbs counterexample.

Next worker: use the DLR specification to compare the weight of an interface between differently oriented, slightly dilated periodic regions with the weight after removing that interface. A useful next lemma would bound the constrained partition-function cost per unit interface area, uniformly in the finite-volume region and with the continuum displacement variables integrated. Density loss alone cannot supply such a bound; this construction shows the missing distinction explicitly.

Task: “push this problem forward by one checkable piece” — received 2026-11-14, approximately 21:56 Asia/Tbilisi.
