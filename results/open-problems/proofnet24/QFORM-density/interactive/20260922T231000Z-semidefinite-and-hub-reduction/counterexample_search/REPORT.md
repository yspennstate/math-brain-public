## Summary

**Status: no counterexample found.** Every family tested stays below its own Gaussian limit and approaches it from below. Nothing grows with n, ε√n, the hub diagonal, the hub block, row overlap, entry scales, comb spacing or bump number. Two record bounds are sharpened, with full proofs below.

**Strongest family and its largest verified density.** In the hub families the largest value is at ε = 0, the pure star + rank one: F = 3.606 ± 0.051 (fibre identity, n−1 = 100, s = 0), against a Gaussian limit of 3.6207 from exact quadrature. The optimiser reaches 4.079 in the Gaussian hub model with a rank-3 remainder, but only by spreading the hub vector until it becomes the Gaussian (1,1,−1) form, whose value is 3√2 = 4.2426.

**One most useful next check.** A hub with an aligned twist plus a non-aligned dense bulk, with bumpy laws tuned against both at once, measured with the fibre identity. Neither Proposition S nor Theorem D covers that regime.

---

# Counterexample search in the open configurations: hubs, dense twists, lattice laws, convex rank three

**Setting.** X has independent coordinates with densities f_i ≤ 1, and Q = XᵀAX + bᵀX + c. The problem is homogeneous, so the figure of merit is F = |μ₃(A)| · sup_s p_Q(s), where μ₃ is the third largest eigenvalue in modulus. The conjecture is sup F < ∞.

## 1. Estimators

- **(E1) One hub integrated exactly.** Write Q = aX_h² + 2TX_h + R. Then p_Q(s) = E Σ_roots f_h(x)/|2ax + 2T|.
  - Its second moment diverges logarithmically at T = 0. The finite-sample mean is biased low: it came out 2–3σ below E2 in two checks.
- **(W) Exact window estimator.** P(|Q − s| ≤ δ | X′) is computed in closed form, as at most two intervals intersected with the intervals of f_h.
  - It is unbiased for the window-averaged density and bounded by 1/(2δ).
  - It matched brute force to 10⁻⁶. It underestimates cusps, so it is used only for scans.
- **(E2) Fibre identity over all coordinates.** Headline values are quoted from E2.
- **(G) Spread limits.**
  - For the hub, p(s) = ∫ φ(y₁)/(2|y₁+β|) · P_{Y₂}(|s − R| ≤ |y₁+β|) dy₁, with the inner probability in closed form. p(0) = 3.620667 at every node count.
  - For the convex side, the Gaussian part is an exact surface integral over the sphere or hyperboloid sheets. It matches the closed forms of χ²₂ − χ²₁ to four digits.

## 2. Proved statements

**Lemma (Gaussian sub-sums).** For Gaussian Y, Q = Σθ_k(Z_k + m_k)² with independent terms. So p_Q = p_{Q_S} ∗ p_{Q−Q_S} and sup p_Q ≤ sup p_{Q_S} for any subset S of terms. Adding eigenvalues at any scale never raises the peak.

**Proposition S (star + rank one, zero hub diagonal, any laws).** Let Q = 2(L + β)X_h + λ(V − v_c(L))² + F_c(L), with w ⊥ v unit vectors, f_h ≤ 1, and μ = |λ|. Then:

- ‖p_Q‖∞ ≤ 2√2 + √2 log(1/3 + 4√2/μ) for 1 ≤ μ ≤ 6√2, which is 5.360 at μ = 1.
- ‖p_Q‖∞ ≤ 2√2 for μ ≥ 6√2.

The previous zero-diagonal constant was 1/2 + 16μ^(−1/2) = 16.5. Every aligned twist κL² + κ′LV is of this form (complete the square in V), for every law including bumpy ones.

*Proof.*
1. Given X′, Q is affine in X_h with slope 2t, t = L + β. So p_Q(s) = E K(L, V), where K(l, v) = f_h(y)/(2|t|) and y = (s − λ(v − v_c)² − F_c)/(2t).
2. Pointwise, K ≤ 1/(2|t|).
3. Fix l and put u = v − v_c(l). On each branch |du/dy| = |t|/√(μ|s′ − 2ty|). So ∫K dv = μ^(−1/2)(2|t|)^(−1/2) ∫ f_h(y) · 1{one side of y₀} · |y − y₀|^(−1/2) dy. The bathtub principle bounds the last integral by 2, so ∫K dv ≤ √2 (μ|t|)^(−1/2).
4. The density ρ of (L, V) is at most 2, and the density m of T is at most √2 (k-dimensional projections have density ≤ 2^(k/2); Ball, Livshyts–Paouris–Pivovarov). Hence ∫ρK dv ≤ min(m, M)(t)/(2|t|), with M(t) = min(√2, 4√2 μ^(−1/2)|t|^(1/2)).
5. The weight 1/(2|t|) decreases in |t|, so the bathtub principle puts g = M on {|t| ≤ τ} with total mass 1.
   - M switches at t* = μ/16. The mass inside |t| ≤ t* is √2μ/12, which is below 1 exactly when μ < 6√2, and it contributes 2√2.
   - The remaining mass sits at height √2 and contributes √2 log(τ/t*), where τ/t* = 1/3 + 4√2/μ. □

*Second check:* at μ = 1, τ = 0.37438, and the water-filling integral evaluates directly to 5.360.

**Proposition S2 (two hubs, A_HH = 0, anything else).** ‖p_Q‖∞ ≤ 2√2 (s₁s₂)^(−1/2), where s₁, s₂ are the singular values of A_{H,Hᶜ}. The earlier bound was 1/2 + 8σ⁻².

*Proof.*
1. Given X_{Hᶜ}, the conditional density is at most 1/max(|c₁|, |c₂|), where (c₁, c₂) = 2(T₁, T₂).
2. (T₁, T₂) has density D ≤ 2/(s₁s₂).
3. Bathtub on the square |z|∞ ≤ r with 4r²D = 1 gives E[1/(2|T|∞)] ≤ 4Dr = 2√D. □

For orthonormal rows the bound is 2.828, against an exact Gaussian value of 2.436.

## 3. Numerical results

F includes μ₃. Laws are uniform unless stated.

**(a) Star + rank one + εW.**
- **Gaussian limit.** With W in span{wwᵀ, vvᵀ, wvᵀ + vwᵀ} and couplings, linear terms and leaf variances all optimised, the maximiser is the pure star: 3.6207.
- **Finite n, nine W types.** At n − 1 = 50, with ε√n from 0 to 3, F decreases monotonically in ε for every type (Wigner, aligned, low rank, complement-supported, sign pattern, Hadamard). At ε√n = 3 it is 1.17–3.02.
- **Growth in n (pure star, E1).**

  | n − 1 | 30 | 100 | 300 | 1000 |
  |---|---|---|---|---|
  | F | 3.580 | 3.545 | 3.569 | 3.577 |

  It is flat. E2 at n − 1 = 100 gives 3.606 ± 0.051.
- **Rank-3 Gaussian remainder.** The 4.079 comes from coupling the hub to a third direction (weight 1.025), which lowers the hub coordinate's leverage to 0.49. The reason a genuine hub loses: ∫ f|y|^(−1/2) is 2.83 for a uniform coordinate, 3.17 for a pair sum, and 3.20 for a Gaussian.

**(b) Hub diagonal a** (E2, common random numbers).

| a | 0 | 0.01 | 0.03 | 0.1 | 0.3 |
|---|---|---|---|---|---|
| F | 3.606 | 3.585 | 3.543 | 3.401 | 3.018 |

Window scans over 240 configurations with dense remainders peak at 3.41. F decreases in a.

**(c) Two hubs with a hub block.** Blocks up to 0.3 and rows at 90°, 30° and 10°: the maximum is 2.76. Hub blocks change F by less than 0.1. Hub-of-hubs structures stay at or below 2.54.

**(d) Multi-scale structures and lattice or bumpy laws.**
- Gaussian spectra at scales 2^(±k) give 0.40–2.56, as the Lemma predicts.
- Multi-scale (geometric) hub rows give 3.48–3.57.
- Lattice-tuned laws (|ψ(2π/Δ)| ≈ 1), with aligned twists and a Wigner bulk: 3.48 at Δ = 1/M, 0.54 at Δ = 1, 0.07 at Δ = 2.
- Boxes at random positions in [−R/2, R/2]: 3.32 at R = 1, 0.04 at R = 16.
- The bumpy laws of twist_obstruction/ (its N13 construction, where the twisted Fourier L¹ norm grows like 2πN) give F = 0.29, 0.11, 0.04 for N = 2, 3, 4. The density falls like N⁻³ while the L¹ norm grows.
- Aligned twists lower F only through μ₃; the window densities are unchanged.

**(e) Convex side of rank three** (1–2 heavy coordinates plus a Gaussian bulk; heavy row, eigenvalues and all linear terms optimised).
- Two-sheet side: maximum 3.559 at s = −0.0031. E2 on actual product measures (n = 40 and 160) gives 3.47 and 3.59.
- Definite side: 2.903, which is the Gaussian (1,1,1) value.
- A heavy coordinate on the negative axis fattens the two-sheet side away from the cone but lowers the cone value. Nothing exceeds 4.24.

**Law optimisation.** Gauss–Seidel best responses, from uniform and from random multi-interval starts, converge to unit intervals and reach the uniform-law value (3.10–3.19 at n − 1 = 8). The Jacobi version, which updates all coordinates at once, overshoots and was discarded.

## 4. Conclusion

No family grows. The only values above the pure-hub level come from turning hubs into spread directions, where the supremum is 3√2. The Fourier obstruction from bumpy laws under aligned twists does not carry over to the density: Proposition S bounds the aligned case for all laws, and numerically those laws lower the density.

