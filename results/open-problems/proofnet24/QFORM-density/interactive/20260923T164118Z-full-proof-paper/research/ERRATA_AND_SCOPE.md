# Corrections and scope decisions in the assembled manuscript

The full unrestricted QFORM problem remains OPEN. The following corrections preserve valid partial results while preventing unsupported closures.

1. **Volume-skeleton expectation:** an equality in the original structural report becomes an inequality when zero-weight singular minor seeds admit nonzero extensions. The inequality is sufficient for the robust decomposition. A four-coordinate disjoint-edge example gives actual value 2 versus the claimed equality value 4. The corrected proof is in `structure.tex` and the amended `NEW_PROJECTED_CROSSING.md`.

2. **Intervals versus Borel sets:** a square-root concentration bound for every interval does not imply the corresponding estimate for every Borel set of a prescribed measure. The full heavy-null density deductions in fleet02/B05 run `20260923T130427Z` and fleet04/B14 run `20260923T141430Z` use that unsupported implication. Their valid frozen-slice Fourier/interval estimates are retained; their general rough-hub closure is not a theorem of this manuscript.

3. **Indefinite spectral spread:** the sufficient smallness condition is on `max_i (|A|)_{ii}`, where `|A|=(A^2)^(1/2)`. It is not merely a condition on `max_i |A_ii|`. The conservative constant is 35, avoiding downward rounding of 34.4081... to 34.4.

4. **Rank perturbation reserve:** a claimed unavoidable loss of twice the perturbation rank is not justified. The rectangular singular-value rank inequality gives a loss of `rank(S P_H)`, at most `rank(S)`, without a Krylov-invariance assumption. The supplement proves the stronger valid statement.

5. **Lower-level constants and scaling:** the lower-level chapter corrects rounding and perturbation estimates while preserving the final no-pivot half-power bound. Truncated potentials under scaling are related by the correct inclusion of the truncation events; they are not pointwise monotone in the incorrectly claimed direction.

6. **Gaussian-mixture scope:** a bound on the average component peak is equivalent to the final density cap for scale mixtures about one deterministic center. The equivalence fails for mixtures whose narrow components have separated random centers. Both new Gaussian-mixture theorems explicitly retain the required condition. The adapted-hub argument is realized using a fresh conditional randomization, so conditioning on latent mixture variables does not change the hub kernel.

7. **Affine and spectral tails:** a theorem for exact rank three with an affine term in the range cannot automatically be used after conditioning, which may produce a linear term outside that range. The ruled one-sheet result is stated with this restriction. Arbitrary small dense quadratic tails are included only in the theorems whose proofs actually retain them.

8. **Regularity and novelty:** interval domination establishes an essentially bounded density. Continuity is asserted only when supplied by an integrable characteristic function or a separate proof. A limited search for relevant publications does not establish novelty. The paper cites classical analytic inputs and distinguishes them from the new averaging and reduction arguments.

The accompanying source catalogue records individual source claims and whether they were reproved, subsumed, used conditionally, or retained only as an archived analysis. No operational report count is presented as a count of proved theorems.
