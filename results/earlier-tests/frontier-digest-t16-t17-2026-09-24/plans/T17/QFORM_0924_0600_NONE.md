# Research plan: bounded-density conjecture for quadratic forms

**Owner's goal:** a full proof. It's an open problem: I'll aim at the full statement, but each block of work should produce verified output (lemma, reduction, special case, or counterexample). I won't claim a proof without a complete written argument checked line by line, and I'll list every remaining gap explicitly.

## 1. First concrete step (≈45 min): write out the reductions with full proofs
- **Extreme points.** P(Q(X)∈[s,s+ε]) is multilinear in the densities f_i. By the bathtub principle, WLOG X_i is uniform on a set E_i with |E_i|=1 (finite unions of intervals by approximation).
- **Inhomogeneous strengthening.** Target q(x)=xᵀAx+⟨b,x⟩+c with the same hypothesis on A. Conditioning creates linear terms, and this class is closed under conditioning and translation. Sanity-check it on Gaussians.
- **Coarea:** f(s)=∫_{q=s} 1_E dH^{n−1}/|∇q| with E=ΠE_i. Large density has two sources: near-critical regions (small |∇q|), and E containing much level-set area relative to |∇q| (thin curved shells).
- A brief literature check, if permitted: is the problem still open, and what are the strongest partial results?

*Why first:* every later argument conditions on coordinates, so the setup must survive conditioning.

## 2. Easy cases, to calibrate (≈1 h)
- **Gaussian:** three eigenvalues ⇒ two share a sign ⇒ density ≤ 1/2.
- **Diagonal A:** take two same-sign coordinates. The densities of λX_i² are ≤ (λu)^{−1/2}, their convolution is ≤ π, and conditioning on the rest cannot raise the sup.
- **n=3:** split the level set by which partial derivative dominates and project along that coordinate (Loomis–Whitney style). Product structure plus |Ax|≥|x| should give an absolute constant. Completing the square extends this to any A with a 3×3 principal block whose eigenvalues all have modulus ≥1.
- **Sharpness:** 2X₁X₂ (eigenvalues ±1) has a log-singular density, so "three" is the natural sign-free threshold.

These cases locate the real difficulty: delocalized eigenvectors, where no bounded block carries the curvature.

## 3. Stress-test the statement (≈1 h, interleaved)
Adversarial laws: uniform on M intervals of length 1/M with spacing d (a lattice plus tiny noise), paired with integer forms. The density then roughly reduces to weighted lattice-point counts on quadrics, and representation numbers of ternary forms fluctuate (class numbers), so check whether this can beat O(1). Add exact small-n numerics with adversarial E_i. A counterexample would be a legitimate outcome.

## 4. Main route: localized/delocalized dichotomy
- **Delocalized model case:** Q=|PX|², P a 3×n matrix with orthonormal rows. Rudelson–Vershynin only gives f(t)≲√t (sphere area over gradient). The missing piece is a "no thin curved shell" estimate: P(||PX|−ρ|≤δ)≲ρδ. Tools: Ball–Rogozin on nearly flat caps of size √(ρδ); Brascamp–Lieb/RV for 2–3-dim projections; a quantitative Schwartz–Zippel-type argument that a linear image of a product measure cannot concentrate near a curved surface.
- **Then:** indefinite signatures, and forms with many small eigenvalues. I expect the latter to be the hardest part.
- **Gluing:** split the coordinates at random into I∪J and condition on X_J. Target dichotomy: either A_{IJ} has two singular values ≳1, so the new linear term v=2A_{IJ}X_J has E[1/|v|]<∞ (this needs dimension ≥2, as 2X₁X₂ shows), or a good bounded principal block exists (Step 2). The catch is the leftover quadratic part A_{II} near its critical points; that is where the real work is.

*Why this route:* the model case isolates the one new phenomenon neither RV nor Ball handles alone: curved level sets meeting linear images of product measures.

## 5. Build on
Ball's cube slicing + Rogozin (linear forms: density ≤ √2/|θ|); Bobkov–Chistyakov (maximal density of sums); Rudelson–Vershynin and Livshyts–Paouris–Pivovarov (projection densities ≤ C^d); Brascamp–Lieb; Loomis–Whitney; coarea; Gaussian chi-square computations.

## 6. Avoid
- **Cauchy–Schwarz decoupling** (Costello–Tao–Vu, Vershynin): it squares probabilities, giving P≲√ε, never a density bound.
- **Fourier decay of φ_Q:** bounded-density laws can be lattice-like at large scales, so φ_Q need not decay. Use Fourier only locally (Ball).
- **Carbery–Wright:** gives only ε^{1/2} and needs log-concavity.
- **Lindeberg/CLT:** needs smooth test functions and fails exactly in localized cases.
- **Rogozin-style rearrangement:** the bathtub extremizers are superlevel sets of functions that need not be unimodal, so they need not be intervals.

## 7. Output
A running log of proved lemmas, open gaps, and failed attempts (with the reason each failed).
