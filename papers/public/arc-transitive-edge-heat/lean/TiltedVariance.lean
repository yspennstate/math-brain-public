import Mathlib

/-- For a(t) = sum m_i e^{-t l_i} write x_i = e^{-t l_i}. Then a' = -sum m_i l_i x_i and
a'' = sum m_i l_i^2 x_i, and the inequality below is a'^2 <= a a'', i.e. (log a)'' >= 0. -/
theorem tilted_variance_nonneg {ι : Type*} (s : Finset ι) (m x l : ι → ℝ)
    (hm : ∀ i ∈ s, 0 ≤ m i) (hx : ∀ i ∈ s, 0 ≤ x i) :
    (∑ i ∈ s, m i * l i * x i) ^ 2 ≤
      (∑ i ∈ s, m i * x i) * (∑ i ∈ s, m i * l i ^ 2 * x i) := by
  have key : (∑ i ∈ s, Real.sqrt (m i * x i) * (l i * Real.sqrt (m i * x i))) ^ 2 ≤
      (∑ i ∈ s, Real.sqrt (m i * x i) ^ 2) * ∑ i ∈ s, (l i * Real.sqrt (m i * x i)) ^ 2 :=
    Finset.sum_mul_sq_le_sq_mul_sq _ _ _
  have h1 : ∀ i ∈ s, Real.sqrt (m i * x i) * (l i * Real.sqrt (m i * x i)) = m i * l i * x i := by
    intro i hi
    have h0 : 0 ≤ m i * x i := mul_nonneg (hm i hi) (hx i hi)
    rw [mul_left_comm, Real.mul_self_sqrt h0]
    ring
  have h2 : ∀ i ∈ s, Real.sqrt (m i * x i) ^ 2 = m i * x i := by
    intro i hi
    exact Real.sq_sqrt (mul_nonneg (hm i hi) (hx i hi))
  have h3 : ∀ i ∈ s, (l i * Real.sqrt (m i * x i)) ^ 2 = m i * l i ^ 2 * x i := by
    intro i hi
    rw [mul_pow, Real.sq_sqrt (mul_nonneg (hm i hi) (hx i hi))]
    ring
  rw [Finset.sum_congr rfl h1, Finset.sum_congr rfl h2, Finset.sum_congr rfl h3] at key
  exact key
