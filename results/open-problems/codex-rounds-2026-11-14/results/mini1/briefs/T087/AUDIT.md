# Audit of the finite-scale reduction

## The factor in the lower bound, derived a second way

There is a probability measure on pairs (configuration, crossing component): integrate a function by summing it over every crossing component and dividing by k(n)=E K_n. If S is the number of its vertices in B_n, then

    E_* S = E W/k(n),     E_* S^2 = E Q/k(n).

Nonnegativity of the variance under this measure gives

    E Q ≥ (E W)^2/k(n).

Using E Q ≤ V_n X(2n) and E W ≥ V_n π(3n) yields

    X(2n) ≥ V_n π(3n)^2/k(n).

This checks the volume factor and the single power of k(n) without factoring an expectation or asserting independence of component count and mass.

## Shell cardinality, counted independently

Expanding (2r+1)^3−(2r−1)^3 gives 24r^2+2. A second count partitions the shell by the first coordinate attaining absolute value r:

    2(2r+1)^2 + 2(2r−1)(2r+1) + 2(2r−1)^2
      = 24r^2+2.

The factors in the three terms correspond respectively to |x_1|=r; |x_1|<r and |x_2|=r; and |x_1|,|x_2|<r and |x_3|=r. The classes are disjoint and exhaustive. At r=1 this gives 26 vertices, agreeing with 3^3−1. Summing the difference of cubes from r=1 through R telescopes to (2R+1)^3−1.

## Independent exponent checks

The defect is d−2a−s. If a pointwise exponent b exists, summing over shells gives s=d−b, hence the same defect is b−2a. With hypothetical mean-field inputs a=2 and s=2, these expressions both give d−6: the first is d−4−2; the second uses b=d−2 and is d−2−4. Thus the reduction forces polynomial crossing-cluster counts above dimension six rather than falsely predicting hyperscaling there. These are consistency inputs, not a new proof of mean-field exponents.

For d=3, substituting b=1+η and a=1/ρ gives defect 1+η−2/ρ. If it vanishes, then 2−η+2/ρ=3. Separately substituting β=ν/ρ and γ=ν(2−η) into γ+2β gives precisely ν(2−η+2/ρ), so it equals 3ν. Both near-critical substitutions are explicitly additional assumptions.

## Attempts to break the argument

1. **Boundary escape.** For x in B_n, the translated box of radius 3n has boundary at distance at least 2n from the origin. A path to it must first hit ∂B_{2n}; its prefix is a valid path in the induced finite graph. Endpoints at exactly distance 2n cause no problem. The argument uses nearest-neighbour edges and cannot be applied unchanged to long-range percolation.

2. **False independence.** K_n and Q can be strongly dependent. The proof uses E sqrt(K_n Q) ≤ sqrt(E K_n E Q); it never replaces E(K_n Q) with E K_n E Q. The only independence used is between endpoint-arm events in two deterministic disjoint boxes.

3. **Which clusters are counted.** Wiring all boundary vertices together can merge components without providing genuine open connections between their inner vertices, invalidating (6). The hypothesis uses the induced graph with no wiring. Whole-lattice clusters require a different distinction: regrouping the crossing components by their genuine whole-lattice clusters preserves W, and the resulting squared masses still count genuinely connected pairs. Thus (1) also admits a whole-lattice-cluster variant if W and Q are regrouped consistently. That variant is not a finite-volume observable. The initial draft called the local definition essential; the audit showed that this was too strong, and the wording was corrected. No theorem or inequality required alteration.

4. **Paths for X.** The upper bound on E Q uses unrestricted connections and is in the correct direction. It would be unjustified to silently replace X by susceptibility using paths restricted to B_n; x−y and translation change the domains.

5. **Expectation versus typical count.** Tightness of K_n does not imply (H). As an abstract warning example, a count equal to n^2 with probability 1/n and 1 otherwise is tight but has expectation n+1−1/n. Rare large counts cannot be discarded. This example is not asserted to describe percolation.

6. **Exponent existence without regular variation.** An expression f(n)=n^{q+o(1)} does not imply a uniform ratio bound f(m)/f(n)≈(m/n)^q. The proof only compares fixed multiples and fixed power scales. In the reverse implication, s>0 and t<1 give the strict logarithmic gap log[X(3n)/X(N)]/log N→−s(1−t), which justifies the subtraction before taking t→1. No uniformity as t→1 is required.

7. **Every integer scale.** The upper arm estimate initially concerns π(3n). Monotonicity with n=floor(r/3) extends it to all r. The lower estimate uses m=3n exactly and N=ceil((3n)^{1/t}), and therefore bounds π(n) at every sufficiently large integer n. No sparse-subsequence limit is promoted to a full limit.

8. **Endpoint regimes.** Theorem 2 excludes a=0, a=d/2, s=0, and s=d. The power sum and the positive gap used in subtraction would require separate treatment at the endpoints. No conclusion for them is claimed.

9. **Averages, suprema, and pointwise decay.** X and M have exponents under the stated hypotheses. Summing a uniform pointwise law implies the corresponding exponent for X, but the reverse inference is not available. Corollary 4 supplies a supremum envelope law only. A prescribed point may have smaller τ(x) than the supremum.

10. **Unproved hypotheses.** Neither (H) nor one of the equivalent exponent-existence statements is established here at p_c on Z^3. The piece is a conditional reduction, not a solution of T087. No statement in this proof relies on the inaccessible September 2026 continuity manuscript.

No numerical experiment was used. All arithmetic above is exact and was checked by the two indicated derivations.
