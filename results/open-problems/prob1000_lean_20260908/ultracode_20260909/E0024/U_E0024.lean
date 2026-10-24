import Mathlib

/-!
E0024 (Hu-Sun survey, Question 4'): the algebraic step behind the Kanda-Forst
comparison of lambda-energies.  With a = lambda + Re(Phi(x)) + Re(Psi(y)) > 0,
b = Im(Phi(x)), d = Im(Psi(y)) and the Kanda-Forst bound |d| <= c a (so d^2 <= c^2 a^2),
the denominators a^2 + (b+d)^2 (process Z = (X,Y)) and a^2 + b^2 (process Z^s = (X,Y^s))
are comparable within the factor 2(1+c^2) in both directions.
-/

theorem E0024_kf_denominator_comparison (a b d c : ℝ) (hd : d ^ 2 ≤ c ^ 2 * a ^ 2) :
    a ^ 2 + b ^ 2 ≤ 2 * (1 + c ^ 2) * (a ^ 2 + (b + d) ^ 2) ∧
    a ^ 2 + (b + d) ^ 2 ≤ 2 * (1 + c ^ 2) * (a ^ 2 + b ^ 2) := by
  constructor
  · nlinarith [sq_nonneg (b + 2 * d), sq_nonneg a, mul_nonneg (sq_nonneg c) (sq_nonneg (b + d)), hd]
  · nlinarith [sq_nonneg (b - d), sq_nonneg a, mul_nonneg (sq_nonneg c) (sq_nonneg b), hd]

/-- The consequence used in the memo: for a > 0 the two integrands
    a/(a^2+(b+d)^2) and a/(a^2+b^2) are comparable within the factor 2(1+c^2). -/
theorem E0024_kf_integrand_comparison (a b d c : ℝ) (ha : 0 < a) (hd : d ^ 2 ≤ c ^ 2 * a ^ 2) :
    a / (a ^ 2 + (b + d) ^ 2) ≤ 2 * (1 + c ^ 2) * (a / (a ^ 2 + b ^ 2)) ∧
    a / (a ^ 2 + b ^ 2) ≤ 2 * (1 + c ^ 2) * (a / (a ^ 2 + (b + d) ^ 2)) := by
  obtain ⟨h1, h2⟩ := E0024_kf_denominator_comparison a b d c hd
  have hp1 : 0 < a ^ 2 + (b + d) ^ 2 := by positivity
  have hp2 : 0 < a ^ 2 + b ^ 2 := by positivity
  constructor
  · rw [← mul_div_assoc, div_le_div_iff₀ hp1 hp2]
    nlinarith [mul_le_mul_of_nonneg_left h1 ha.le]
  · rw [← mul_div_assoc, div_le_div_iff₀ hp2 hp1]
    nlinarith [mul_le_mul_of_nonneg_left h2 ha.le]

#print axioms E0024_kf_denominator_comparison
#print axioms E0024_kf_integrand_comparison
