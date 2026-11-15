# Substantial advance elsewhere; the full statement is not claimed solved

Guangchen Chen and Xing Lyu, *Tracy–Widom law for sample covariance matrices under quadratic form concentration*, [arXiv:2610.41416v2](https://arxiv.org/abs/2610.41416v2), submitted 30 October 2026, revised 4 November 2026. Read the [full HTML](https://arxiv.org/html/2610.41416v2), especially Assumptions 1.1–1.2, Theorem 1.3, Corollary 1.4, and Remark 1.5.

## What the new paper proves

For independent centered real vectors with common covariance Σ, assume every quadratic form has dimension-uniform Lp fluctuations bounded by its Hilbert–Schmidt norm, for each fixed p≥2. Assume Σ is uniformly bounded above and below, the population right edge is uniformly regular, and dimension/sample size tends to a positive limit different from one. Theorem 1.3 compares the largest eigenvalue with its Gaussian covariance counterpart; Corollary 1.4 gives TW1 fluctuations with the finite-dimensional covariance edge and scale. These are hypotheses and conclusions of the paper, not claims about every model in T248. [Chen–Lyu, §§1.1–1.2](https://arxiv.org/html/2610.41416v2#S1.SS2).

The paper's normalization, with dimension M and sample count s, is

    H = (1/s) Σ_i q_i q_iᵀ,
    f(u) = -1/u + (1/s) Σ_{α=1}^M t_α/(1+t_α u),
    f'(u_+) = 0,  -1/t_max < u_+ < 0,
    E_+ = f(u_+),  γ_+ = (2/f''(u_+))^(1/3),
    γ_+ s^(2/3) (λ_max(H)-E_+) ⇒ TW1.

Here t_α are the eigenvalues of Σ. Uniform regularity includes a constant lower bound on 1+t_max u_+.

## Why it matters for this problem

This is an application route, not an assertion that Chen and Lyu state T248 verbatim. Condition on a fixed input matrix X whose columns have norm √d. Write

    q_i = σ(Xᵀ w_i/√d) ∈ R^N,   i=1,…,m,
    Σ_X = E_w[q_i q_iᵀ | X].

The q_i are independent conditional on X. Each preactivation coordinate is exactly standard Gaussian; consequently E_w q_i=0 under the centering in T248. The map w↦q_i is Lipschitz with constant at most Lip(σ)‖X‖op/√d. Thus bounded ‖X‖op/√d gives dimension-free Gaussian Lipschitz concentration. The quadratic-form concentration implication is explicitly available in Proposition 2.8 and the discussion leading to Example 2.11 of the paper below. Its tail bound with constant K=O(1), integrated in t, gives precisely the fixed-p moment condition required here; ‖A‖op≤‖A‖HS absorbs the second term. This uses the dimension-uniform bound, rather than a subpolynomial bound that could grow with dimension.

The resulting matrix in Chen–Lyu notation is

    H = YᵀY/m,   M=N,   s=m,   y=N/m.

The desired nonzero eigenvalues are multiplied by m/N. Therefore, for any deterministic sequence of such designs satisfying the stated uniform covariance bounds and edge regularity, with N/m→y≠1, the theorem gives

    γ_X m^(2/3) [(N/m) λ_max(YYᵀ/N)-E_X] ⇒ TW1.

This is a conditional covariance-edge statement. Applying it to random designs requires checking these hypotheses on a high-probability set. Replacing E_X by a deterministic finite-size edge additionally requires controlling its random displacement at o(m^(-2/3)); convergence of the global law is insufficient. No such replacement is asserted in this report.

## Related advance opened during the search

Renyuan Ma and Theodor Misiakiewicz, *The anisotropic local law for sample covariance matrices under quadratic-form concentration*, [arXiv:2609.09440v2](https://arxiv.org/abs/2609.09440v2), revised 11 September 2026. Read the [full HTML](https://arxiv.org/html/2609.09440), Theorem 2.4, Proposition 2.8, and Example 2.11. They prove an anisotropic local law under quadratic-form concentration without an additional higher-cumulant hypothesis. Their examples include Lipschitz random-feature maps with concentrated underlying vectors, subject to the remaining covariance assumptions. This supplies an explicit bridge from Lipschitz feature maps to the concentration framework.

## Limits and attempted failure cases

- Aspect ratio exactly one is excluded by the stated Chen–Lyu hypothesis. Transposing exchanges y with 1/y and does not remove this exception.
- Gaussian inputs do not have exactly fixed column norms. Conditional coordinate means need not vanish even when Eσ(Z)=0; treating them as centered silently discards a possible finite-rank term.
- A nonzero second Hermite coefficient can create covariance structure even when the first coefficient vanishes. The original prompt's two cancellation conditions do not verify covariance edge regularity.
- A supercritical population spike violates the uniform separation condition at the rightmost population edge. Corollary 1.4 does not automatically give a TW law for the next eigenvalue after deleting that spike.
- Polynomial activations of degree at least three are not globally Lipschitz. Their treatment would require additional estimates or a justified truncation argument.
- For TW fluctuations one must use appropriate finite-size centering. An arbitrary convergence rate of aspect ratios to their limits can itself exceed the TW scale.

The search therefore found a substantial advance on the framework needed for T248, not a verified complete solution of the full spiked, non-Lipschitz, all-aspect-ratio formulation. The session stops under instruction 1.
