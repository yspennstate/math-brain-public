import Mathlib

/-!
The arithmetic of Lemma 3.1 of "The Fourier entropy-influence inequality for monotone DNF formulas of bounded width".
If `p 1 = 1` and `p (j + 1) ≥ (p j - 2 δ) / 2` for `j ≥ 1`, then `2^(k-1) p k ≥ 1 - δ (2^k - 2)` for `k ≥ 1`, that is
`p k ≥ 2^(1-k) - δ (2 - 2^(2-k))`; and if moreover `p k ≤ 2 δ`, then `δ (2^(k+1) - 2) ≥ 1`, that is
`δ ≥ 1 / (2^(k+1) - 2)`.
-/

namespace FEIMonoRec

theorem rec_bound (δ : ℝ) (p : ℕ → ℝ) (h1 : p 1 = 1)
    (hstep : ∀ j, 1 ≤ j → (p j - 2 * δ) / 2 ≤ p (j + 1)) :
    ∀ k, 1 ≤ k → 1 - δ * (2 ^ k - 2) ≤ 2 ^ (k - 1) * p k := by
  intro k hk
  induction k, hk using Nat.le_induction with
  | base => simp [h1]
  | succ n hn ih =>
    have hs := hstep n hn
    obtain ⟨m, rfl⟩ := Nat.exists_eq_add_of_le hn
    -- n = 1 + m, so 2^n = 2 * 2^m and 2^(n+1-1) = 2^n
    have e1 : (1 + m + 1 - 1) = 1 + m := by omega
    have e2 : (1 + m - 1) = m := by omega
    rw [e1]
    rw [e2] at ih
    have hp1 : (2 : ℝ) ^ (1 + m) = 2 * 2 ^ m := by rw [pow_add, pow_one]
    have hp2 : (2 : ℝ) ^ (1 + m + 1) = 2 * (2 * 2 ^ m) := by rw [pow_succ, hp1]; ring
    rw [hp1] at ih
    rw [hp2, hp1]
    have hpos : (0 : ℝ) < 2 ^ m := by positivity
    have hmul := mul_le_mul_of_nonneg_left hs (by positivity : (0 : ℝ) ≤ 2 * 2 ^ m)
    nlinarith [hmul, ih, hpos]

theorem delta_bound (δ : ℝ) (p : ℕ → ℝ) (h1 : p 1 = 1)
    (hstep : ∀ j, 1 ≤ j → (p j - 2 * δ) / 2 ≤ p (j + 1)) (k : ℕ) (hk : 1 ≤ k)
    (hblock : p k ≤ 2 * δ) : 1 ≤ δ * (2 ^ (k + 1) - 2) := by
  have hb := rec_bound δ p h1 hstep k hk
  obtain ⟨m, rfl⟩ := Nat.exists_eq_add_of_le hk
  have e2 : (1 + m - 1) = m := by omega
  rw [e2] at hb
  have hp1 : (2 : ℝ) ^ (1 + m) = 2 * 2 ^ m := by rw [pow_add, pow_one]
  have hp2 : (2 : ℝ) ^ (1 + m + 1) = 2 * (2 * 2 ^ m) := by rw [pow_succ, hp1]; ring
  rw [hp1] at hb
  rw [hp2]
  have hpos : (0 : ℝ) < 2 ^ m := by positivity
  have hmul := mul_le_mul_of_nonneg_left hblock hpos.le
  nlinarith [hmul, hb, hpos]

end FEIMonoRec

#print axioms FEIMonoRec.delta_bound
