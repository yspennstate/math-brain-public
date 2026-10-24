import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Nat.Log
import Mathlib.Tactic.Common
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# From the exact full-period average to the partial-sum bound

`BC23Full` proves that the full-period average of the majorant `prod (1 + cos)` is exactly `1`,
hence the average of `P_K^2 = prod cos^2 (pi (3/2)^j x)` over a full period `3^(K+1)` is exactly
`2^(-(K+1))`.  Summing over one period gives, with `n = K + 1`,

  `sum_{k < 3^n} |hat mu (k)|^2 <= 3^n / 2^n = (3/2)^n`.

This file is the elementary aggregation step that turns that into a bound for every `M`:

  `sum_{k < M} |hat mu (k)|^2 <= (3/2) * M^theta`,   `theta = log(3/2)/log 3 = 0.36907...`

The constant `3/2` is exactly `3^theta`: the smallest period containing `[0, M)` has length
`3^n < 3M`, and `(3^n)^theta = (3/2)^n`.  A rigorous decimal bracket `0.369 < theta < 0.37` is
proved from the integer inequalities `2^1000 < 3^631` and `3^63 < 2^100`.

The analytic inputs (the sampling identity of item 6, the majorant `|hat mu| <= P_K` of item 3,
and the period average of item 4) enter as hypotheses; nothing here reproves them.
-/

open Finset

namespace BC23

/-- `theta = log(3/2)/log 3`, the exponent of the unconditional partial-sum bound. -/
noncomputable def theta : ℝ := Real.log (3 / 2) / Real.log 3

lemma log_three_pos : 0 < Real.log 3 := Real.log_pos (by norm_num)

lemma log_three_ne : Real.log 3 ≠ 0 := ne_of_gt log_three_pos

lemma log_threehalf_pos : 0 < Real.log (3 / 2) := Real.log_pos (by norm_num)

lemma theta_pos : 0 < theta := div_pos log_threehalf_pos log_three_pos

lemma theta_nonneg : 0 ≤ theta := le_of_lt theta_pos

/-- The defining property of the exponent: `3 ^ theta = 3/2`. -/
theorem three_rpow_theta : (3 : ℝ) ^ theta = 3 / 2 := by
  have h3 : (0 : ℝ) < 3 := by norm_num
  have hne : Real.log 3 ≠ 0 := log_three_ne
  rw [Real.rpow_def_of_pos h3, theta]
  rw [show Real.log 3 * (Real.log (3 / 2) / Real.log 3) = Real.log (3 / 2) by field_simp]
  exact Real.exp_log (by norm_num)

/-- `theta < 0.37`, from `3^63 < 2^100` (i.e. `(3/2)^100 < 3^37`). -/
theorem theta_lt : theta < 0.37 := by
  have h3 : 0 < Real.log 3 := log_three_pos
  have key : ((3 : ℝ) / 2) ^ (100 : ℕ) < (3 : ℝ) ^ (37 : ℕ) := by norm_num
  have hl := Real.log_lt_log (by positivity) key
  rw [Real.log_pow, Real.log_pow] at hl
  rw [theta, div_lt_iff₀ h3]
  push_cast at hl
  linarith

/-- `0.369 < theta`, from `2^84 < 3^53` (i.e. `3^31 < (3/2)^84`, so `theta > 31/84 = 0.369047...`). -/
theorem theta_gt : (0.369 : ℝ) < theta := by
  have h3 : 0 < Real.log 3 := log_three_pos
  have key : (3 : ℝ) ^ (31 : ℕ) < ((3 : ℝ) / 2) ^ (84 : ℕ) := by
    rw [div_pow, lt_div_iff₀ (by positivity : (0:ℝ) < 2 ^ (84:ℕ))]
    norm_num
  have hl := Real.log_lt_log (by positivity) key
  rw [Real.log_pow, Real.log_pow] at hl
  rw [theta, lt_div_iff₀ h3]
  push_cast at hl
  linarith

/-- `(3^n)^theta = (3/2)^n`. -/
lemma rpow_three_pow (n : ℕ) : ((3 : ℝ) ^ n) ^ theta = (3 / 2 : ℝ) ^ n := by
  have h3 : (0 : ℝ) ≤ 3 := by norm_num
  rw [← Real.rpow_natCast (3 : ℝ) n, ← Real.rpow_mul h3, mul_comm (n : ℝ) theta,
    Real.rpow_mul h3, three_rpow_theta, Real.rpow_natCast]

/-- **The aggregation step.**  A monotone quantity bounded by `(3/2)^n` on the periods `3^n`
obeys `S M <= (3/2) M^theta` for every `M >= 1`.  The constant is `3^theta = 3/2`. -/
theorem partial_sum_bound (S : ℕ → ℝ) (hmono : Monotone S)
    (hper : ∀ n : ℕ, S (3 ^ n) ≤ (3 / 2 : ℝ) ^ n)
    (M : ℕ) (hM : 1 ≤ M) :
    S M ≤ (3 / 2) * (M : ℝ) ^ theta := by
  set n := Nat.log 3 M + 1 with hn
  have hMne : M ≠ 0 := by omega
  -- `M < 3^n`
  have hup : M ≤ 3 ^ n := le_of_lt (Nat.lt_pow_succ_log_self (by norm_num) M)
  -- `3^n <= 3 M`
  have hlow : (3 : ℕ) ^ n ≤ 3 * M := by
    have := Nat.pow_log_le_self 3 hMne
    calc (3 : ℕ) ^ n = 3 * 3 ^ (Nat.log 3 M) := by rw [hn, pow_succ]; ring
      _ ≤ 3 * M := by omega
  have hlowR : ((3 : ℝ) ^ n) ≤ 3 * (M : ℝ) := by
    have := (Nat.cast_le (α := ℝ)).2 hlow
    push_cast at this
    linarith
  have hMR : (0 : ℝ) ≤ (M : ℝ) := Nat.cast_nonneg M
  calc S M ≤ S (3 ^ n) := hmono hup
    _ ≤ (3 / 2 : ℝ) ^ n := hper n
    _ = ((3 : ℝ) ^ n) ^ theta := (rpow_three_pow n).symm
    _ ≤ (3 * (M : ℝ)) ^ theta := Real.rpow_le_rpow (by positivity) hlowR theta_nonneg
    _ = (3 : ℝ) ^ theta * (M : ℝ) ^ theta :=
        Real.mul_rpow (by norm_num) hMR
    _ = (3 / 2) * (M : ℝ) ^ theta := by rw [three_rpow_theta]

/-- One period, from a majorant whose period sum is exactly `3^n / 2^n` (the sampling identity of
item 6 together with the exact period average of item 4). -/
theorem period_sum_le_of_majorant (a b : ℕ → ℝ) (n : ℕ)
    (hab : ∀ k ∈ range (3 ^ n), a k ≤ b k)
    (hb : ∑ k ∈ range (3 ^ n), b k = (3 : ℝ) ^ n / 2 ^ n) :
    ∑ k ∈ range (3 ^ n), a k ≤ (3 / 2 : ℝ) ^ n := by
  calc ∑ k ∈ range (3 ^ n), a k ≤ ∑ k ∈ range (3 ^ n), b k := Finset.sum_le_sum hab
    _ = (3 : ℝ) ^ n / 2 ^ n := hb
    _ = (3 / 2 : ℝ) ^ n := by rw [div_pow]

/-- **Item 5, assembled, from the period bound.**  This is the form the analysis delivers: the
only analytic input is that the sum of `|hat mu (k)|^2` over one full period `3^n` is at most
`(3/2)^n`. -/
theorem partial_sum_of_period_bound (a : ℕ → ℝ)
    (hnn : ∀ k, 0 ≤ a k)
    (hper : ∀ n : ℕ, ∑ k ∈ range (3 ^ n), a k ≤ (3 / 2 : ℝ) ^ n)
    (M : ℕ) (hM : 1 ≤ M) :
    ∑ k ∈ range M, a k ≤ (3 / 2) * (M : ℝ) ^ theta := by
  refine partial_sum_bound (fun m => ∑ k ∈ range m, a k) ?_ hper M hM
  intro p q hpq
  have hsub : range p ⊆ range q := by
    intro x hx
    simp only [mem_range] at hx ⊢
    omega
  exact Finset.sum_le_sum_of_subset_of_nonneg hsub (fun i _ _ => hnn i)

/-- The same, when the period bound comes from a scale-dependent majorant `b n` (in the
application `b n k = P_(n-1)(...)^2`, a different majorant for each octave depth) whose exact
period sum is `3^n / 2^n`. -/
theorem partial_sum_of_period_average (a : ℕ → ℝ) (b : ℕ → ℕ → ℝ)
    (hnn : ∀ k, 0 ≤ a k)
    (hab : ∀ n, ∀ k ∈ range (3 ^ n), a k ≤ b n k)
    (hb : ∀ n : ℕ, ∑ k ∈ range (3 ^ n), b n k = (3 : ℝ) ^ n / 2 ^ n)
    (M : ℕ) (hM : 1 ≤ M) :
    ∑ k ∈ range M, a k ≤ (3 / 2) * (M : ℝ) ^ theta :=
  partial_sum_of_period_bound a hnn
    (fun n => period_sum_le_of_majorant a (b n) n (hab n) (hb n)) M hM

/-- The same bound with the decimal exponent: `sum_{k < M} a k <= (3/2) M^(0.37)`. -/
theorem partial_sum_decimal (a : ℕ → ℝ)
    (hnn : ∀ k, 0 ≤ a k)
    (hper : ∀ n : ℕ, ∑ k ∈ range (3 ^ n), a k ≤ (3 / 2 : ℝ) ^ n)
    (M : ℕ) (hM : 1 ≤ M) :
    ∑ k ∈ range M, a k ≤ (3 / 2) * (M : ℝ) ^ (0.37 : ℝ) := by
  have h := partial_sum_of_period_bound a hnn hper M hM
  have hM1 : (1 : ℝ) ≤ (M : ℝ) := by exact_mod_cast hM
  have hmono : (M : ℝ) ^ theta ≤ (M : ℝ) ^ (0.37 : ℝ) :=
    Real.rpow_le_rpow_of_exponent_le hM1 (le_of_lt theta_lt)
  linarith

end BC23

#print axioms BC23.three_rpow_theta
#print axioms BC23.theta_lt
#print axioms BC23.theta_gt
#print axioms BC23.partial_sum_bound
#print axioms BC23.partial_sum_of_period_average
#print axioms BC23.partial_sum_of_period_bound
#print axioms BC23.partial_sum_decimal
