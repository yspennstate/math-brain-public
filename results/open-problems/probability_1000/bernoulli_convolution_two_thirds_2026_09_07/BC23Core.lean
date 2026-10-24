import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Data.Rat.Floor
import Mathlib.Tactic.Common
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Machine-checked core of "Information decay and rationally scaled convolutions
  of the two-thirds Bernoulli measure" (manuscript v2, 6 September 2026)

What is checked here is the arithmetic and the inductive skeleton of the paper:

* `int_cmp`      : 8^13 * 3^12 < 5^25                          (Section 5)
* `c_lt`         : c = log(9/8) < 1/8                          (Section 5)
* `c_pos`        : c > 0
* `a_lt`         : a = log 2 < 7/10                            (Section 5)
* `alpha_lt`     : alpha = log(3/2)/log 3 < 3/8                (Section 5)
* `ratio_le_one` : (8/5) * (3/8)^(12/25) ≤ 1                   (the induction constant)
* `induction_bound` : the strong induction of Section 5, stated for an abstract
                   sequence S with the paper's hypotheses (base cases m = 3,4,5
                   and the shifted inequality S_m + a ≤ (8/5)(S_r + a), r = ⌈3m/8⌉),
                   giving S_m + a ≤ 2 (m-2)^(12/25) for m ≥ 3
* `deficit_bound`   : from m j_m ≤ S_m, the all-depth bound j_m ≤ 2 m^(-13/25)
* `final_constant`  : 2 c^2 + 8 * 26 < 209                     (Section 6)

Not checked here (they need measure theory well beyond a session): the Frostman
input (Shmerkin), Lemma 2.2, the fibre cocycle, Lemma 4.2 (the cyclic channel),
Proposition 5.1 itself, Lemma 6.2 (lower semicontinuity), and Proposition 7.1.
-/

open Real

namespace BC23

/-- Section 5: the integer comparison behind the exponent 12/25. -/
theorem int_cmp : (8:ℕ)^13 * 3^12 < 5^25 := by norm_num

/-- c = log(9/8) < 1/8, from log x < x - 1 for x ≠ 1. -/
theorem c_lt : Real.log (9/8) < 1/8 := by
  have h := Real.log_lt_sub_one_of_pos (by norm_num : (0:ℝ) < 9/8) (by norm_num : (9/8:ℝ) ≠ 1)
  linarith

theorem c_pos : 0 < Real.log (9/8) := Real.log_pos (by norm_num)

/-- a = log 2 < 7/10. -/
theorem a_lt : Real.log 2 < 7/10 := by
  have := Real.log_two_lt_d9
  linarith

/-- alpha = log(3/2)/log 3 < 3/8, i.e. (3/2)^8 < 3^3. -/
theorem alpha_lt : Real.log (3/2) / Real.log 3 < 3/8 := by
  have h3 : 0 < Real.log 3 := Real.log_pos (by norm_num)
  rw [div_lt_iff₀ h3]
  have h : Real.log ((3/2:ℝ)^8) < Real.log ((3:ℝ)^3) :=
    Real.log_lt_log (by positivity) (by norm_num)
  rw [Real.log_pow, Real.log_pow] at h
  push_cast at h
  linarith

/-- The constant of the induction: (8/5) (3/8)^(12/25) ≤ 1, from 8^13 3^12 < 5^25. -/
theorem ratio_le_one : (8/5:ℝ) * (3/8:ℝ) ^ ((12:ℝ)/25) ≤ 1 := by
  set y : ℝ := (3/8:ℝ) ^ ((12:ℝ)/25) with hy
  have y0 : 0 ≤ y := by positivity
  have hy25 : y ^ (25:ℕ) = (3/8:ℝ) ^ (12:ℕ) := by
    rw [hy, ← Real.rpow_natCast, ← Real.rpow_mul (by norm_num : (0:ℝ) ≤ 3/8)]
    norm_num
  have hprod : ((8/5:ℝ) * y) ^ (25:ℕ) ≤ 1 := by
    rw [mul_pow, hy25]
    have hc : ((8:ℝ)^13 * 3^12) < 5^25 := by exact_mod_cast int_cmp
    rw [div_pow, div_pow, div_mul_div_comm, div_le_one (by positivity)]
    nlinarith [hc]
  exact (pow_le_one_iff_of_nonneg (by positivity) (by norm_num : (25:ℕ) ≠ 0)).1 hprod

/-- r = ⌈3m/8⌉ as a natural number. -/
noncomputable def r (m : ℕ) : ℕ := Nat.ceil ((3:ℝ) * m / 8)

theorem r_ge_three {m : ℕ} (hm : 6 ≤ m) : 3 ≤ r m := by
  unfold r
  have : (2:ℝ) < 3 * m / 8 := by
    have : (6:ℝ) ≤ m := by exact_mod_cast hm
    linarith
  exact Nat.lt_ceil.2 this

theorem r_lt {m : ℕ} (hm : 6 ≤ m) : r m < m := by
  unfold r
  have : (3:ℝ) * m / 8 ≤ ((m - 1 : ℕ) : ℝ) := by
    have : (6:ℝ) ≤ m := by exact_mod_cast hm
    push_cast [Nat.cast_sub (by omega : 1 ≤ m)]
    linarith
  have h := Nat.ceil_le.2 this
  omega

/-- r - 2 ≤ (3/8)(m - 2) as reals, for m ≥ 6. -/
theorem r_sub_two_le {m : ℕ} (hm : 6 ≤ m) : ((r m : ℝ) - 2) ≤ (3/8) * ((m:ℝ) - 2) := by
  unfold r
  have h1 : (Nat.ceil ((3:ℝ) * m / 8) : ℝ) < (3:ℝ) * m / 8 + 1 := Nat.ceil_lt_add_one (by positivity)
  have h6 : (6:ℝ) ≤ m := by exact_mod_cast hm
  linarith

/-- Section 5, the strong induction: with the base cases and the shifted inequality
    the sequence obeys S_m + a ≤ 2 (m - 2)^(12/25) for every m ≥ 3. -/
theorem induction_bound (S : ℕ → ℝ) (a : ℝ)
    (hbase : ∀ m, 3 ≤ m → m ≤ 5 → S m + a < 2)
    (hstep : ∀ m, 6 ≤ m → S m + a ≤ (8/5) * (S (r m) + a)) :
    ∀ m, 3 ≤ m → S m + a ≤ 2 * ((m:ℝ) - 2) ^ ((12:ℝ)/25) := by
  intro m
  induction m using Nat.strong_induction_on with
  | _ m ih =>
    intro hm3
    by_cases hm : m ≤ 5
    · -- base cases: (m-2)^(12/25) ≥ 1 since m - 2 ≥ 1
      have h1 : (1:ℝ) ≤ (m:ℝ) - 2 := by
        have : (3:ℝ) ≤ m := by exact_mod_cast hm3
        linarith
      have hp : (1:ℝ) ≤ ((m:ℝ) - 2) ^ ((12:ℝ)/25) :=
        Real.one_le_rpow h1 (by norm_num)
      have := hbase m hm3 hm
      linarith
    · push Not at hm
      have hm6 : 6 ≤ m := by omega
      have hr3 := r_ge_three hm6
      have hrm := r_lt hm6
      have ihr := ih (r m) hrm hr3
      have hstepm := hstep m hm6
      -- (r-2)^(12/25) ≤ ((3/8)(m-2))^(12/25) = (3/8)^(12/25) (m-2)^(12/25)
      have hr2 : (0:ℝ) ≤ (r m : ℝ) - 2 := by
        have : (3:ℝ) ≤ (r m : ℝ) := by exact_mod_cast hr3
        linarith
      have hm2 : (0:ℝ) ≤ (m:ℝ) - 2 := by
        have : (6:ℝ) ≤ m := by exact_mod_cast hm6
        linarith
      have hmono : ((r m : ℝ) - 2) ^ ((12:ℝ)/25) ≤ ((3/8) * ((m:ℝ) - 2)) ^ ((12:ℝ)/25) :=
        Real.rpow_le_rpow hr2 (r_sub_two_le hm6) (by norm_num)
      have hsplit : ((3/8:ℝ) * ((m:ℝ) - 2)) ^ ((12:ℝ)/25)
          = (3/8:ℝ) ^ ((12:ℝ)/25) * ((m:ℝ) - 2) ^ ((12:ℝ)/25) :=
        Real.mul_rpow (by norm_num) hm2
      have hpos : (0:ℝ) ≤ ((m:ℝ) - 2) ^ ((12:ℝ)/25) := by positivity
      have key : (8/5:ℝ) * (2 * ((r m : ℝ) - 2) ^ ((12:ℝ)/25)) ≤ 2 * ((m:ℝ) - 2) ^ ((12:ℝ)/25) := by
        calc (8/5:ℝ) * (2 * ((r m : ℝ) - 2) ^ ((12:ℝ)/25))
            ≤ (8/5:ℝ) * (2 * ((3/8:ℝ) ^ ((12:ℝ)/25) * ((m:ℝ) - 2) ^ ((12:ℝ)/25))) := by
              rw [← hsplit]; gcongr
          _ = ((8/5:ℝ) * (3/8:ℝ) ^ ((12:ℝ)/25)) * (2 * ((m:ℝ) - 2) ^ ((12:ℝ)/25)) := by ring
          _ ≤ 1 * (2 * ((m:ℝ) - 2) ^ ((12:ℝ)/25)) := by
              gcongr
              exact ratio_le_one
          _ = 2 * ((m:ℝ) - 2) ^ ((12:ℝ)/25) := by ring
      calc S m + a ≤ (8/5) * (S (r m) + a) := hstepm
        _ ≤ (8/5) * (2 * ((r m : ℝ) - 2) ^ ((12:ℝ)/25)) := by gcongr
        _ ≤ 2 * ((m:ℝ) - 2) ^ ((12:ℝ)/25) := key

/-- From m j_m ≤ S_m, a > 0 and the induction bound: j_m ≤ 2 m^(-13/25) for m ≥ 3. -/
theorem deficit_bound (S j : ℕ → ℝ) (a : ℝ) (ha : 0 < a)
    (hS : ∀ m, 3 ≤ m → S m + a ≤ 2 * ((m:ℝ) - 2) ^ ((12:ℝ)/25))
    (hj : ∀ m : ℕ, 1 ≤ m → (m:ℝ) * j m ≤ S m) :
    ∀ m, 3 ≤ m → j m ≤ 2 * (m:ℝ) ^ (-(13:ℝ)/25) := by
  intro m hm3
  have hmpos : (0:ℝ) < m := by
    have : (3:ℝ) ≤ m := by exact_mod_cast hm3
    linarith
  have h1 := hS m hm3
  have h2 := hj m (by omega)
  have hm2 : (0:ℝ) ≤ (m:ℝ) - 2 := by
    have : (3:ℝ) ≤ m := by exact_mod_cast hm3
    linarith
  have hmono : ((m:ℝ) - 2) ^ ((12:ℝ)/25) ≤ (m:ℝ) ^ ((12:ℝ)/25) :=
    Real.rpow_le_rpow hm2 (by linarith) (by norm_num)
  -- j_m ≤ S_m / m ≤ 2 m^(12/25) / m = 2 m^(-13/25)
  have hjm : j m ≤ S m / m := by
    rw [le_div_iff₀ hmpos]; linarith
  have hSm : S m ≤ 2 * (m:ℝ) ^ ((12:ℝ)/25) := by linarith
  have hdiv : 2 * (m:ℝ) ^ ((12:ℝ)/25) / m = 2 * (m:ℝ) ^ (-(13:ℝ)/25) := by
    rw [mul_div_assoc, div_eq_mul_inv, ← Real.rpow_neg_one, ← Real.rpow_add hmpos]
    norm_num
  calc j m ≤ S m / m := hjm
    _ ≤ 2 * (m:ℝ) ^ ((12:ℝ)/25) / m := by gcongr
    _ = 2 * (m:ℝ) ^ (-(13:ℝ)/25) := hdiv

/-- Section 6, the final constant: 2 c^2 + 8 (1 + 25) < 209 because c < 1/8. -/
theorem final_constant : 2 * (Real.log (9/8))^2 + 8 * 26 < 209 := by
  have h1 := c_lt
  have h0 := c_pos
  nlinarith

end BC23

#print axioms BC23.int_cmp
#print axioms BC23.c_lt
#print axioms BC23.a_lt
#print axioms BC23.alpha_lt
#print axioms BC23.ratio_le_one
#print axioms BC23.induction_bound
#print axioms BC23.deficit_bound
#print axioms BC23.final_constant
