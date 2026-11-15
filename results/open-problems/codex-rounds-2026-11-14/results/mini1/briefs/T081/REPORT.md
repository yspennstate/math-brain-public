VERDICT: PARTIAL exact obstruction to removing the boxed partition by common-shift Boltzmann averaging

For a stable boxed hard-core interaction with equal within-cube and neighboring-cube attraction, [PROOF.md](PROOF.md) derives the translation-invariant pair potential obtained by averaging its energy over grid translations. It is a hard core plus an explicit finite-range sum of tent products.

Averaging its Boltzmann weight gives a different result. Two pairs, each of length (3L/2), separated by any integer (M\geq3) cube sides in a transverse direction, have isolated weights ((1+q)/2) and joint weight ((1+q^2)/2), where (q=e^{\beta j}>1). Their joint weight exceeds the product by exactly ((q-1)^2/4), independently of their separation. The resulting effective energy therefore has no pair representation and is not additive beyond any finite range. The strict discrepancy persists on an open set of configurations.

For (n) such distant pairs, the effective energy minus the averaged energy, divided by the (2n) particles, tends to (-j/4). Thus there is also no uniform subextensive error bound between these two averages over all finite configurations. This is a statement about finite configurations, not about their equilibrium prevalence.

The concrete piece completed is an audit of this averaging shortcut. No liquid–vapour transition is proved, and no novelty claim is made for the general hidden-variable mechanism.

## Verification

Run from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 check_averaging.py > check_output.txt
```

The run passed 784 exact rational checks of the tent kernel, 24 four-particle checks in dimensions 2 and 3, variance checks at (q=2,3,5), and checks of one through eight distant pairs. Data are in [averaging_checks.json](averaging_checks.json); full output and the command are in [LOG.md](LOG.md) and [check_output.txt](check_output.txt).

The stability constant was re-derived using the occupation quadratic form. The four-particle discrepancy was re-derived as a Bernoulli variance; a half-cube shift reverses its sign relative to the product weight. The extensive limit was derived both through a hyperbolic cosine and directly from the two possible energies. Sub-core separations were checked separately: weight averaging also fails to preserve the hard core.

The checker used about 17.4 MB peak RSS and finished in about 0.03 seconds. `nice -n 15` printed a sandbox priority warning; the inherited effective nice was 20, which the script checked. No heavy computation was run.

## Literature check

The search took less than ten minutes. The opened [Qidong He, Ian Jauslin, Joel Lebowitz, Ron Peled paper, arXiv:2510.24825](https://arxiv.org/html/2510.24825v1), retains the fixed partition. The opened [Francesco Baffioni, Tobias Kuna, Immacolata Merola, Errico Presutti paper, arXiv:2611.05641](https://arxiv.org/html/2611.05641v1), treats a quantum LMP model with four-body interactions.

An additional [Hexagon manuscript](https://hexagonmath.org/pdf/2610.00734v1), dated 31 October 2026, claims the target hard-sphere/Kac coexistence theorem. Its first page credits generation to GPT-6 Astra, prompting to Qidong He, and explicitly says the results are not human-verified. Its proof was not verified here. This is an unresolved claim requiring audit, so SOLVED_ELSEWHERE.md was not created. Its Hexagon identifier is **not** an arXiv identifier: [arXiv:2610.00734](https://arxiv.org/abs/2610.00734) is an unrelated paper by Jon Lee.

## What failed and what remains uncertain

Common-shift Boltzmann averaging fails to preserve pair interactions, even though each fixed-grid Hamiltonian has finite range. Energy averaging preserves pair form, but this supplies no transfer of phase coexistence. Mixtures of normalized infinite-volume Gibbs measures have not been analyzed; their conditional grid distributions require separate work. No flaw in the Hexagon coexistence manuscript is established here, and the bounded search does not certify that no solution exists elsewhere.

## Next step

First audit the recent Hexagon claim, particularly its exact contour replacement and microscopic-background integration. If that claim does not settle the problem, work directly with the explicit averaged pair potential (5) in PROOF.md. A useful next statement would control its constrained partition functions or contour costs without interchanging energy averaging and Boltzmann averaging. The sparse configurations above rule out an unrestricted subextensive comparison; any successful comparison needs additional hypotheses on configurations or ensembles.

Task: “push this problem forward by one checkable piece” — 14 Nov 2026, 21:57 Asia/Tbilisi (session receipt).
