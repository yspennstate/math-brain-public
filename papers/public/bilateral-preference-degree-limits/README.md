# Degree fluctuations in bilateral preference random graphs

Companion material for the paper of the same title (Y. Shmalo, October 2026). [Read the paper](paper/main.pdf).

In the bilateral preference random graph LK(n,k) of La and Kabkab, independent uniform scores are placed on the edges
of the complete graph Kₙ, each vertex prefers the k edges at it with the smallest scores, and an edge is kept when both
of its endpoints prefer it. Let D be the degree of a vertex and H = k − D. Dabirian and Subramanian (*Connectivity of a
family of bilateral preference random graphs*, J. Appl. Probab. 63 (2026), Section 1.1) asked for the limiting
distribution of the standardized degree (D − 𝔼D)/√Var D. The paper finds it in every regime of k = k(n). Write
sₙ² = k(n − k)/n and g(z) = φ(z) + zΦ(z), where φ and Φ are the standard normal density and distribution function.

**Theorem 2.1.** If k → ∞ and n − k → ∞, then H/sₙ converges in distribution and in its first two moments to g(Z),
with Z standard normal. Consequently 𝔼D = k − sₙ/√π + o(sₙ), Var D = v sₙ² + o(sₙ²) with v = 1/3 + (√3 − 2)/(2π), and

(D − 𝔼D)/√Var D ⇒ L∞ = (π^(−1/2) − g(Z))/√v.

The law of L∞ has an explicit density (Section 3) and takes values below 1.04643…, so it is not normal.

**Theorems 4.2 and 5.1.** Fix r = n − 1 − k ≥ 1. Let A have the Gamma(r, 1) law and, given A, let Hᵣ be Poisson with
mean Λᵣ(A), where Λᵣ(a) = e^(−a) Σ_{ℓ<r} (r − ℓ) a^ℓ/ℓ!. Then H converges to Hᵣ in distribution and in all moments,
and the standardized degree converges to Lᵣ = (μᵣ − Hᵣ)/√νᵣ, where μᵣ = 𝔼Hᵣ = r·C(2r, r)/4^r and νᵣ = Var Hᵣ.
As r → ∞, Lᵣ ⇒ L∞.

**Theorem 6.2.** For fixed k the limit law of D is contained in the local convergence of LK(n,k) to the Erlang
weighted tree of Moharrami, Subramanian, Liu and Sundaresan; Proposition 6.1 gives a direct proof in mixed binomial
form. Together with the results above this identifies every subsequential limit of the standardized degree along any
sequence k(n): the standardized fixed-k law when k is constant, L∞ when k → ∞ and n − k → ∞, and Lᵣ when
n − 1 − k = r is constant. The laws L₁ and L₂ are different (their largest values are √(3/7) and √(243/433)), so when
n − 1 − k alternates between 1 and 2 the standardized degree has no limit, and no single law serves for all
sequences k(n).

**Proposition 7.1 and Corollary 7.3.** For every n and 1 ≤ k ≤ n − 2, 𝔼(k − D) takes the same value at the budgets k
and n − 1 − k, namely (n − 1)∫₀¹ F(t)(1 − F(t)) dt with F the Beta(k, n − 1 − k) distribution function. As n → ∞ this
identifies the constant cₖ = (2k − 1)·C(2k − 2, k − 1)/2^(2k−1) in the expansion 𝔼D = k − cₖ(1 + O(k²/n)) of Dabirian
and Subramanian with μₖ.

The proofs condition on the (k+1)st smallest score X at the vertex. Given X, H is a sum of k exchangeable indicators
with conditional mean k·qₙ(X) for an explicit function qₙ. In the interior regime the conditional variance is small
compared with sₙ², and the normal limits of the beta-distributed order statistics turn k·qₙ(X)/sₙ into g(Z). For fixed r
the limit is identified by factorial moments, and for fixed k by a Poisson approximation of binomial counts.

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/checks.py`: computations, the exact parts in rational arithmetic. Part A goes through every order of the scores
  for n = 4 and n = 5 (720 and 3 628 800 orders), records the joint law of the degree D and of the number I of vertices
  that prefer their edge to the root, and compares the mean and variance of k − D with the exact formulas of Section 2
  and the laws with Proposition 7.1; it also checks the equality of means at complementary budgets and the integral
  formula for 𝔼(k − D) for every n ≤ 24. Part B simulates LK(12, 4) and LK(12, 8), 200 000 graphs each. Part C checks the
  constants of the fixed-r limit by finite sums, closed forms and quadrature, and the approach to them at r = 1, 2, 3
  along n = 10, 20, 40, 80. Part D computes 𝔼H/sₙ and Var H/sₙ² for k = n/2 and k = n/10 up to n = 10⁶ and for k = √n
  up to n = 10⁸, and Part E checks the distribution function and density of L∞. It needs Python 3 with NumPy and SciPy
  and runs in under a minute. `code/checks_output.txt` is its output (52 checks, all pass).
- `code/RootDegree.lean`: the beta-function identity used in Lemma 2.2, the identity
  k·C(2k, k)·4^(−k) = (2k − 1)·C(2k − 2, k − 1)·2^(1−2k) behind Corollary 7.3 for every k ≥ 1, the finite sum (4.3)
  against r·C(2r, r)·4^(−r) for r ≤ 6, and for r = 1, 2 the values of the second factorial moment, of νᵣ and of μᵣ²/νᵣ,
  checked with Lean 4.33.1 and Mathlib (commit 0df444a360eaa60ab8c11dca51a86af692955474). `code/lean_output.txt` is the
  output of the check.
- `SHA256SUMS.txt`: checksums of the files above.

## Running the checks

    python code/checks.py > code/checks_output.txt

For the Lean file, in a Lake project that depends on Mathlib at the commit above:

    lake env lean RootDegree.lean

## Citation

Y. Shmalo, Degree fluctuations in bilateral preference random graphs, 2026,
https://github.com/yspennstate/bilateral-preference-degree-limits
