# Adversarial checks of the ray theorem

This is a mathematical self-audit, not an independent referee report. Deterministic arithmetic results are in verification.json; the proof is in PROOF.md.

1. **Normalization and depth indexing.** At ||u||^2=d the first preactivation variance is 2, the first postactivation mean square is 1, and the linear output variance is 2. There are h random norm multipliers for h hidden layers; the Gaussian output has no additional empirical multiplier. Thus the leading variance fluctuation is 5h/n, not 5(h-1)/n or 10h/n. This is checked directly from the conditional Gaussian norm transition.

2. **The constants 5, 44, 251, 558.** Single-factor moments were computed both by centered iid-sum formulas in the proof and by equality partitions of ordered summation indices in verify.py. Product moments were then computed both by powers of raw moments and by a separate centered-product recurrence. All rational comparisons agree, including n=1.

3. **Smooth lower-bound coefficient.** Taylor expansion in random variance gives 5 exp(-1/2)/8. Independently, for one hidden layer the exact formula is

       E cos X = [(1+(1+2/n)^(-1/2))/2]^n.

   Expanding its logarithm gives -1/2+5/(8n)+O(n^(-2)), hence the same coefficient. Decimal evaluation at n=1000000 gives n times the gap =0.379081224797536, against limiting coefficient 0.379081662320396. This numerical agreement is a diagnostic; the analytic expansion establishes the coefficient.

4. **Singular distributions and extinction.** B has an atom 2^(-n) at zero. Therefore V has an atom of mass 1-(1-2^(-n))^h at zero, and the process law has the same atom at the zero function. A density calculation directly on the untruncated process would be invalid. The TV proof explicitly uses Gaussian measures including delta_0. The W2 proof first couples to a mixture with variance in [3/4,5/4]; only that mixture receives an entropy calculation. The n=1,h=1 characteristic function was checked against its exact atom-containing law. In the h=o(n) regime the extinction probability is negligible compared with h/n.

5. **Variance cancellation after clipping.** Clipping does not preserve mean one. The proof retains b=E(Vbar-1) and bounds it by 64D4; dropping it would make the chi-square bound unjustified. Squared transport cost of the discarded part is at most 16D4. These follow from pointwise inequalities on |V-1|>1/4, including V=0.

6. **Gaussian overlap kernel and transport.** The kernel 1/sqrt(v+w-vw) was derived by Gaussian integration and checked by independent numerical quadrature for five variance pairs (maximum absolute discrepancy below 1e-14). Substituting v=1+e,w=1+e' gives 1/sqrt(1-ee'), with a minus sign. The quantile transport proof uses a positive smooth clipped density; Gaussian tail bounds justify its boundary terms and logarithmic integrability. The entropy bound is proved in the text rather than assumed for a singular law.

7. **Uniformity in growing depth.** A fixed-h asymptotic expansion would not establish h=o(n). Instead B(0)=B'(0)=0 is used with an explicit derivative bound valid on [0,1/n]. The arithmetic 36^2+4*16^2+6*5^2=2470 and 536+4*88=888 gives 1679 after double integration. Exact moment grids include h=n, even though the matching-rate assertion requires h/n->0. The grid does not prove the uniform bound; differentiating the polynomials does.

8. **Independent lower bound at large depth.** Retaining B<=2 gives at least 4/n of its variance for n>=100. The concavity deficit identity for E sqrt(B) then implies the all-depth W2 lower bound. This does not use the characteristic-function expansion. In particular a claim of W2 convergence at h proportional to n would contradict this bound.

9. **Functional scope.** Positive homogeneity is used only for nonnegative multiples of one fixed input. The entire support is one-dimensional, with an evaluation inverse. Thus scalar and functional W2 differ by exactly A, and TV is unchanged. This argument cannot be used on arbitrary compact sets. With all inputs zero the discrepancy is zero. Points of both signs, biases, or non-collinear inputs need another argument. k-point covariance nondegeneracy is unnecessary in this restricted case.

10. **Prior work.** Math-memory cards already contain the single-input product representation and depth/width variance constant. An existing T243 card records a merging-input result and numerical smooth gaps. The present proof does not claim these ingredients as new, and literature priority of its explicit transport estimate is unverified.

No failed assertion was found in these checks. The main risk is scope: this is an explicit rank-one special case, not a sharp functional theorem for general compact input sets.
