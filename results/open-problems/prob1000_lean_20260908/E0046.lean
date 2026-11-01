import Mathlib

/-!
# Monotonicity of the expected average singular value of complex Ginibre matrices

Bandeira, *Ten lectures and forty-two open problems*, Open Problem 1.2 (complex half):
`alpha_C(n+1) <= alpha_C(n)`.  With `S_n = sum_{k<n} r_k` the normalised half-integer Laguerre
moments, `alpha_C(n) = Gamma(3/2) S_n / n^{3/2}`, and `S` obeys
`n^2 S_{n+1} = (2 n^2 + 3/4) S_n - n^2 S_{n-1}` with `S_1 = 1`, `S_2 = 11/4`.  Writing
`rho_n = S_{n+1}/S_n` this is `rho_n = 2 + 3/(4n^2) - 1/rho_{n-1}`, and the claim is
`rho_n <= (1+1/n)^{3/2}`.  Here we certify the two analytic steps: the elementary inequality
`(1+x)^{3/2} + (1-x)^{3/2} >= 2 + 3x^2/4` on `[0,1]` and the induction.  The recurrence is a
hypothesis (it is a symbolic computation from the generating function).
-/

open Real

namespace GinibreSCV

/-- `(1+x)^{3/2} + (1-x)^{3/2} ≥ 2 + 3x²/4` for `0 ≤ x ≤ 1`, written with square roots. -/
theorem key_ineq (x : ℝ) (hx0 : 0 ≤ x) (hx1 : x ≤ 1) :
    2 + 3 * x ^ 2 / 4 ≤ (1 + x) * Real.sqrt (1 + x) + (1 - x) * Real.sqrt (1 - x) := by
  set u := Real.sqrt (1 + x) with hu
  set v := Real.sqrt (1 - x) with hv
  have hu0 : 0 ≤ u := Real.sqrt_nonneg _
  have hv0 : 0 ≤ v := Real.sqrt_nonneg _
  have hu2 : u ^ 2 = 1 + x := by rw [hu, Real.sq_sqrt]; linarith
  have hv2 : v ^ 2 = 1 - x := by rw [hv, Real.sq_sqrt]; linarith
  -- s = u + v satisfies s^2 = 2 + 2uv ≥ 2, hence s ≥ 4/3 and 3s^2 + 4s - 8 ≥ 0
  have hs2 : (u + v) ^ 2 ≥ 2 := by nlinarith [mul_nonneg hu0 hv0]
  have hs : u + v ≥ 4 / 3 := by nlinarith [hs2, hu0, hv0]
  have hq : 0 ≤ 3 * (u + v) ^ 2 + 4 * (u + v) - 8 := by nlinarith [hs2, hs]
  -- the polynomial identity: LHS - RHS = (s-2)^2 (3 s^2 + 4 s - 8) / 16 given u^2 + v^2 = 2
  have hx : x = u ^ 2 - 1 := by linarith
  have hx' : x = 1 - v ^ 2 := by linarith
  rw [hx]
  nlinarith [mul_nonneg (sq_nonneg (u + v - 2)) hq, hu2, hv2, hu0, hv0]

/-- The target function `f n = (1 + 1/n)^{3/2}`, written with a square root. -/
noncomputable def f (n : ℕ) : ℝ := (1 + 1 / (n : ℝ)) * Real.sqrt (1 + 1 / (n : ℝ))

/-- `1 / f (n-1) = (1 - 1/n)^{3/2}` for `n ≥ 2`. -/
theorem inv_f_pred (n : ℕ) (hn : 2 ≤ n) :
    1 / f (n - 1) = (1 - 1 / (n : ℝ)) * Real.sqrt (1 - 1 / (n : ℝ)) := by
  have hn' : (1 : ℝ) ≤ (n : ℝ) - 1 := by
    have : (2 : ℝ) ≤ n := by exact_mod_cast hn
    linarith
  have hpos : (0 : ℝ) < (n : ℝ) - 1 := by linarith
  have hnpos : (0 : ℝ) < (n : ℝ) := by linarith
  have hcast : ((n - 1 : ℕ) : ℝ) = (n : ℝ) - 1 := by
    rw [Nat.cast_sub (by omega : 1 ≤ n), Nat.cast_one]
  unfold f
  rw [hcast]
  have h1 : 1 + 1 / ((n : ℝ) - 1) = (n : ℝ) / ((n : ℝ) - 1) := by
    field_simp
    ring
  have h2 : 1 - 1 / (n : ℝ) = ((n : ℝ) - 1) / (n : ℝ) := by field_simp
  rw [h1, h2]
  have hA : Real.sqrt ((n : ℝ) / ((n : ℝ) - 1)) = Real.sqrt (n : ℝ) / Real.sqrt ((n : ℝ) - 1) := by
    rw [Real.sqrt_div hnpos.le]
  have hB : Real.sqrt (((n : ℝ) - 1) / (n : ℝ)) = Real.sqrt ((n : ℝ) - 1) / Real.sqrt (n : ℝ) := by
    rw [Real.sqrt_div hpos.le]
  rw [hA, hB]
  have hsA : 0 < Real.sqrt (n : ℝ) := Real.sqrt_pos.mpr hnpos
  have hsB : 0 < Real.sqrt ((n : ℝ) - 1) := Real.sqrt_pos.mpr hpos
  have hsA2 : Real.sqrt (n : ℝ) ^ 2 = (n : ℝ) := Real.sq_sqrt hnpos.le
  have hsB2 : Real.sqrt ((n : ℝ) - 1) ^ 2 = (n : ℝ) - 1 := Real.sq_sqrt hpos.le
  field_simp

/-- The induction: a positive sequence with `rho 1 = 11/4` and
`rho n = 2 + 3/(4 n^2) - 1/rho (n-1)` for `n ≥ 2` stays below `f n`. -/
theorem rho_le_f (rho : ℕ → ℝ) (hpos : ∀ n, 1 ≤ n → 0 < rho n)
    (h1 : rho 1 = 11 / 4)
    (hrec : ∀ n, 2 ≤ n → rho n = 2 + 3 / (4 * (n : ℝ) ^ 2) - 1 / rho (n - 1)) :
    ∀ n, 1 ≤ n → rho n ≤ f n := by
  intro n hn
  induction n with
  | zero => omega
  | succ m ih =>
    rcases Nat.lt_or_ge m 1 with hm | hm
    · -- m = 0 : n = 1
      have hm0 : m = 0 := by omega
      subst hm0
      rw [h1]
      unfold f
      have hs : Real.sqrt (1 + 1 / ((1 : ℕ) : ℝ)) = Real.sqrt 2 := by norm_num
      rw [hs]
      have h2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
      have h2pos : 0 ≤ Real.sqrt 2 := Real.sqrt_nonneg _
      norm_num
      nlinarith [h2, h2pos]
    · -- m ≥ 1 : n = m + 1 ≥ 2
      have hn2 : 2 ≤ m + 1 := by omega
      have hih := ih hm
      have hρ := hrec (m + 1) hn2
      have hpm : 0 < rho m := hpos m hm
      have hfm : 0 < f m := by
        unfold f
        have : (0 : ℝ) < 1 + 1 / ((m : ℕ) : ℝ) := by positivity
        positivity
      have hstep : 1 / f m ≤ 1 / rho m := one_div_le_one_div_of_le hpm hih
      have hinv : 1 / f ((m + 1) - 1) = (1 - 1 / ((m + 1 : ℕ) : ℝ)) * Real.sqrt (1 - 1 / ((m + 1 : ℕ) : ℝ)) :=
        inv_f_pred (m + 1) hn2
      simp only [Nat.add_sub_cancel] at hinv hρ
      have hx0 : (0 : ℝ) ≤ 1 / ((m + 1 : ℕ) : ℝ) := by positivity
      have hx1 : 1 / ((m + 1 : ℕ) : ℝ) ≤ 1 := by
        rw [div_le_one (by positivity)]
        exact_mod_cast Nat.succ_le_succ (Nat.zero_le m)
      have hkey := key_ineq (1 / ((m + 1 : ℕ) : ℝ)) hx0 hx1
      have hsq : (1 / ((m + 1 : ℕ) : ℝ)) ^ 2 = 1 / ((m + 1 : ℕ) : ℝ) ^ 2 := by ring
      unfold f
      rw [hρ]
      have : 3 / (4 * ((m + 1 : ℕ) : ℝ) ^ 2) = 3 * (1 / ((m + 1 : ℕ) : ℝ)) ^ 2 / 4 := by
        rw [hsq]; ring
      rw [this]
      have hlow : (1 - 1 / ((m + 1 : ℕ) : ℝ)) * Real.sqrt (1 - 1 / ((m + 1 : ℕ) : ℝ)) ≤ 1 / rho m := by
        rw [← hinv]; exact hstep
      linarith [hkey, hlow]

end GinibreSCV

#print axioms GinibreSCV.key_ineq
#print axioms GinibreSCV.inv_f_pred
#print axioms GinibreSCV.rho_le_f
