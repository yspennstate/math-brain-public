import Mathlib

/-!
# The binomial-ratio step in the proof of Janson's Conjecture 18.4

Moving the `j` balls of one box into `j` distinct empty boxes multiplies the number of target
configurations by `C(E, j)` and the number of preimages by at most `C(m, j)`.  The step used is
`C(m,p)/C(N,p) ≤ (m/N)^p` for `p ≤ m ≤ N`, i.e. `∏_{i<p} (m-i)/(N-i) ≤ (m/N)^p`, together with
the geometric tail of the union bound.  Both are certified here in the form actually used.
-/

open Finset BigOperators

namespace F0055

/-- `∏_{i<p} (m - i) * N^p ≤ m^p * ∏_{i<p} (N - i)` for reals `0 ≤ m ≤ N` and `p ≤ m`: each factor
satisfies `(m-i) N ≤ m (N-i)`. -/
theorem prod_ratio_le (m N : ℝ) (hm : 0 ≤ m) (hmN : m ≤ N) (p : ℕ) (hp : (p : ℝ) ≤ m) :
    (∏ i ∈ range p, (m - i)) * N ^ p ≤ m ^ p * ∏ i ∈ range p, (N - i) := by
  induction p with
  | zero => simp
  | succ p ih =>
    have hp' : (p : ℝ) ≤ m := by
      have : ((p : ℕ) : ℝ) ≤ ((p + 1 : ℕ) : ℝ) := by exact_mod_cast Nat.le_succ p
      linarith
    have ih' := ih hp'
    rw [prod_range_succ, prod_range_succ, pow_succ, pow_succ]
    have hf : (m - p) * N ≤ m * (N - p) := by nlinarith
    have h1 : 0 ≤ ∏ i ∈ range p, (m - i) := by
      apply prod_nonneg; intro i hi
      have : (i : ℝ) ≤ p := by exact_mod_cast (mem_range.mp hi).le
      linarith
    have h2 : 0 ≤ ∏ i ∈ range p, (N - i) := by
      apply prod_nonneg; intro i hi
      have : (i : ℝ) ≤ p := by exact_mod_cast (mem_range.mp hi).le
      linarith
    have hN : 0 ≤ N := by linarith
    have hmp : 0 ≤ m - p := by linarith
    have hNp : 0 ≤ N - p := by linarith
    -- (P_m (m-p)) (N^p N) ≤ (m^p m) (P_N (N-p))
    calc (∏ i ∈ range p, (m - i)) * (m - p) * (N ^ p * N)
          = ((∏ i ∈ range p, (m - i)) * N ^ p) * ((m - p) * N) := by ring
      _ ≤ (m ^ p * ∏ i ∈ range p, (N - i)) * (m * (N - p)) := by
          apply mul_le_mul ih' hf (by positivity) (by positivity)
      _ = m ^ p * m * ((∏ i ∈ range p, (N - i)) * (N - p)) := by ring

/-- The union-bound tail: if `P(Y_1 = j) ≤ A q^j` for every `j ≥ k` then the union over `n`
boxes of `{Y_i ≥ k}` has probability at most `n A q^k / (1 - q)` for `0 ≤ q < 1`. -/
theorem tail_bound (A q : ℝ) (hA : 0 ≤ A) (hq0 : 0 ≤ q) (hq1 : q < 1) (n : ℕ) (k : ℕ)
    (P : ℕ → ℝ) (hP : ∀ j, k ≤ j → P j ≤ A * q ^ j) (hP0 : ∀ j, 0 ≤ P j) :
    ∀ J, (n : ℝ) * ∑ j ∈ Ico k J, P j ≤ (n : ℝ) * (A * q ^ k / (1 - q)) := by
  intro J
  apply mul_le_mul_of_nonneg_left _ (Nat.cast_nonneg n)
  have hgeo : ∑ j ∈ Ico k J, A * q ^ j ≤ A * q ^ k / (1 - q) := by
    by_cases hJ : J ≤ k
    · rw [Ico_eq_empty_of_le hJ]; simp; positivity
    · push_neg at hJ
      have : ∑ j ∈ Ico k J, q ^ j = (q ^ k - q ^ J) / (1 - q) := by
        rw [geom_sum_Ico' hq1.ne hJ.le]
      rw [← mul_sum, this]
      have hqJ : 0 ≤ q ^ J := pow_nonneg hq0 J
      have h1q : 0 < 1 - q := by linarith
      rw [mul_div_assoc', div_le_div_iff_of_pos_right h1q]
      nlinarith
  calc ∑ j ∈ Ico k J, P j ≤ ∑ j ∈ Ico k J, A * q ^ j := sum_le_sum fun j hj => hP j (mem_Ico.mp hj).1
    _ ≤ A * q ^ k / (1 - q) := hgeo

end F0055

#print axioms F0055.prod_ratio_le
#print axioms F0055.tail_bound
