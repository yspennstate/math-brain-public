# Checks and attempted counterexamples

The earlier affine obstruction holds. recheck.py was written independently and does not import the earlier worker's script. It verifies the reported Gaussian example by direct normal-density quadrature and by erfc, and computes the arrangement count both by exact integer sums and by lgamma/log-sum-exp. Exact enumeration of 512 posterior-weighted label vectors checks all ten lower tails on a nine-point one-dimensional sample. The analytic independent derivation is in LOG.md.

For the new construction, audit.py compares three descriptions of each correction: an absolute-value second difference, a piecewise triangular formula, and an explicit six-neuron ReLU sum. All 360 rational cases agree, including negative u, u=0, boundary slopes, and both tails. Full networks interpolate five exact rational samples and are evaluated at 139 points; 107 points outside their support give exact equality with the linear baseline. The odd-part identity and positive homogeneity hold exactly.

The Gaussian slope bound is derived in PROOF.md both by a Cartesian ratio transformation and by projective polar coordinates. Numerically, 42 density values from a closed formula agree with direct Cartesian density integration, with maximum relative discrepancy 6.51e-13. Six polar integrals normalize to one. Eighteen interval-union probabilities agree by Cartesian and polar integration and satisfy the stated mass bound. At zero projected signal, the independent exact check is the standard Cauchy interval formula [atan(b)-atan(a)]/pi. These quadratures audit formulas; the inequalities themselves are proved analytically.

The sample-mean second moment is derived both from raw second moments and from the covariance of F mu+sigma SFG. Exact rational enumeration checks it using 32 isotropic discrete moment atoms and 1,024 pairs of independent atoms. This discrete calculation verifies only the moment identity; it is not used as a substitute for Gaussian classification probabilities. The linear and quadratic plug-in risk inequalities are checked on 72 Gaussian cases, including zero signal, zero estimated direction, reversed directions, and flip probability 0.49.

For n=10000,d=20,s=2,eta=0.1, the quadratic variance factor is independently computed as the exact rational 67/50000. Multiplying it by 2/sqrt(2pi) and adding the localization bound gives expected excess risk at most 0.0010691876353647793. The population score-disagreement bound is 2.2323888939733122e-8. The rigorous bounds concern the explicit estimator, not a GD trajectory.

The following attempted extensions fail or require qualifications:

- A correction supported in just one cone would violate the linear odd-part identity for bias-free shallow ReLU networks. The actual corrections use antipodal cones.
- Exact proportional or antipodal projected sample directions can demand incompatible corrections. The rule rejects these cases; they have probability zero for the nonsingular Gaussian mixture. Zero first coordinate is another null exception.
- In dimension one, every bias-free shallow ReLU score is linear separately on the two half-lines. This construction needs d>=2.
- Tiny support probability does not bound parameter norm. A rational stress sample has displayed path norm about 2.56e26. The proof gives an exact representation cost and a Lipschitz lower bound for the same constructed correction as its width shrinks.
- Arbitrary shrinking cones do not establish anything about the population squared loss or the quality of numerical evaluation. The theorem concerns classification risk and exact real arithmetic.
- The slope-density bound grows with s. The stated consistency conclusion assumes bounded s; the explicit inequalities give the relevant conditions for other sequences. The quadratic bound also loses its usefulness as (1-2eta)s tends to zero, where the square-root bound remains available.
- The baseline can be zero; its classifier is then constant. Its risk is 1/2 and is covered explicitly. At zero signal every classifier has risk 1/2.
- Fixed width, bounded norm, random fixed output weights, and GD from random initialization are not covered. No dynamical, max-margin, or minimum-norm selection statement follows from the existence of these interpolants.

All computation uses standard-library Python, one process, no GPU or training libraries. Both scripts require OMP_NUM_THREADS=1 and check inherited niceness>=15 before calculations. The final audit took about 0.14 seconds and peaked at 15,728,640 bytes RSS. A 60-second CPU limit and wall alarm guard both scripts. No individual run approached the 1 GB or 20-minute limits.
