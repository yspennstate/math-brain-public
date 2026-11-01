# Hostile referee pass for the P0220 continuation

2026-10-11. Scope: the finite joint-survival determinant and closed triple density, not novelty or full formalization.

1. **Wrong process or only a bulk limit?** The proof starts with the source's actual stationary Gamma(B) representation for linear drift x and rate-one dx dt noise. It does not substitute the translation-invariant driftless Hammersley process. Every subsequent identity is at finite thresholds, with no large-k scaling.

2. **Does P=Q in distribution identify the full joint hitting vector?** Yes: for every finite tableau size, RSK gives the entire tableau law f^lambda/n! for both P and Q. Restricting pile tops to smaller labels is proved by the update induction. Thus the whole set of first-row labels up to every cutoff matches, not merely the LIS length. B labels are finite because the corresponding iid input has increasing blocks of every fixed length almost surely.

3. **Could transposition change the path weights?** Transposing a standard (skew) filling is a bijection. It preserves f and the total box counts in every interval. It changes a first-row cap into a row-count cap exactly. The final cap is enough to keep every earlier nested diagram within d rows.

4. **Are the Poisson factorials missing a normalization?** Conditional interval counts contribute exp(-T) product Delta^h/h!. The discrete tableau contributes f^lambda/N!, with the compatible tableau count equal to the product of skew dimensions. The resulting finite d-path ensemble is a subprobability measure of total mass exp(-T)det A. The proof never divides the source measure by that mass. This prevents accidentally answering a conditioned-process question.

5. **Are noncolliding minors actually nonnegative?** The finite exterior-power calculation shows they count legal box-addition paths with coefficient u^n/n!. It proves their positivity and their exact skew-tableau value. A move cannot swap ordered positions; collision makes it zero. There is no hidden sign from reversing row order, because rows and columns are reversed together.

6. **Does a row-count cap really mean occupancy?** Yes. The d-m bottom coordinates at their minimal sites 0,...,d-m-1 are equivalent to zero last parts. These are simultaneous requirements. The generating diagonal factor is 1+z at each marked site; each d-particle configuration contributes coefficient 1 precisely when all requirements hold.

7. **Time ordering and determinant signs?** Q connects a marker only to a strictly later time, so it is strictly upper triangular and (I-QZ)^(-1) is a finite polynomial. Equal-time sites have Q entries zero. The occupation generating function is A+F Z(I-QZ)^(-1)G. Its all-marker coefficient is det A det(G A^(-1)F-Q), yielding block signs (-G,-Q), without an extra (-1)^q. GeneralBlockCertificate.lean passed with kernel checking for arbitrary finite matrix dimensions; general_block_lean.txt records exit 0.

8. **Did the exact check reuse the proposed formula?** No. The reference coefficients enumerate uniform permutations and LIS lengths at chronological input prefixes, then sum independent Poisson count compositions. The determinant branch uses rational formal-series Gaussian elimination. The direct branch does not use suffix-minimum reduction, so it also verifies that preprocessing. Fifteen constraint patterns through degree seven pass, including a fourteen-by-fourteen determinant.

9. **Is the infinite-state limit justified?** All path weights are nonnegative. Monotonicity of positions makes a terminal-position cutoff bound all previous positions. These events increase to the full finite-threshold event. A_L,G_L converge entrywise by factorial tail bounds. The block determinant is finite, so its continuity suffices. No unproved trace-class claim is used.

10. **Boundary cases?** Nonnegative zero thresholds are automatic, equal times merge by their smallest index, nonmonotone caps reduce to suffix minima by nondecreasing diagram width, d=0 gives exp(-T), q=0 gives the usual finite Toeplitz determinant, and coincident triple thresholds follow by continuity. Scalar and degenerate examples are included in the exact checker.

11. **Independent numerical check?** Positive Plancherel growth is computed using the dimension-ratio transition and integer hook counts, not skew determinants or occupation kernels. Seven numerical values agree within the analytic Poisson-tail error at final box-count cutoff 32. The computations use high precision but do not certify floating-point rounding; the exact coefficient tests and analytical proof carry the claim.

12. **Is the closed triple density consistent?** It follows by explicit differentiation of the triple survival formula, with factorial series justifying each derivative. Fifteen bivariate coefficients through degree four match independent permutations of sizes through seven. It reproduces the non-Markov boundary coefficients.

Conclusion: no mathematical gap was found in the source-specific finite-determinant evaluation using the established historical stationary representation. The remaining uncertainty is historical priority of this composition and external acceptance of the proof. Neither a new independent formalization of the entire theorem nor a theorem in print explicitly solving the source question is claimed.
