/-
Machine-checked scalar components of

  "Phi-mixing implies interlaced rho-mixing for Markov chains" (Bradley's Question 5).

This file covers the real-variable bookkeeping of the main theorem: the function Psi of
equation (4.4), its closed form and monotonicity, the passage from the robust-channel estimate
rho* <= Psi(kappa) and kappa^2 <= 2 phi to the two bounds of Theorem 1.1, the one-lag threshold of
Corollary 5.3, the rate transfer of Corollary 5.2, the envelope of Section 9, and the two-sided
expansion of Proposition 8.1 (the two-state chain).  Everything is stated over the reals.

Checked with Lean 4 / Mathlib (see the repository README for the exact toolchain).
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Inverse
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

open Real

namespace BradleyQ5

/-- The envelope function of equation (4.4): `Psi r = sin (min (2 arcsin r) (pi/2))`. -/
noncomputable def Psi (r : ℝ) : ℝ := Real.sin (min (2 * Real.arcsin r) (Real.pi / 2))

theorem sqrt_two_le_two : Real.sqrt 2 ≤ 2 := by
  have h4 : Real.sqrt 4 = 2 := by
    rw [show (4:ℝ) = 2 ^ 2 by norm_num]
    exact Real.sqrt_sq (by norm_num)
  calc Real.sqrt 2 ≤ Real.sqrt 4 := Real.sqrt_le_sqrt (by norm_num)
    _ = 2 := h4

theorem one_le_sqrt_two : (1:ℝ) ≤ Real.sqrt 2 := by
  calc (1:ℝ) = Real.sqrt 1 := Real.sqrt_one.symm
    _ ≤ Real.sqrt 2 := Real.sqrt_le_sqrt (by norm_num)

theorem sqrt_two_div_two_sq : (Real.sqrt 2 / 2) ^ 2 = 1 / 2 := by
  rw [div_pow, Real.sq_sqrt (by norm_num)]
  norm_num

/-- `sin (2 arcsin r) = 2 r sqrt(1 - r^2)` on `[-1, 1]`. -/
theorem sin_two_arcsin (r : ℝ) (h0 : -1 ≤ r) (h1 : r ≤ 1) :
    Real.sin (2 * Real.arcsin r) = 2 * r * Real.sqrt (1 - r ^ 2) := by
  rw [Real.sin_two_mul, Real.sin_arcsin h0 h1, Real.cos_arcsin]

/-- For `0 <= r <= sqrt 2 / 2` one has `2 arcsin r <= pi/2`. -/
theorem two_arcsin_le_pi_div_two (r : ℝ) (h0 : 0 ≤ r) (h1 : r ≤ Real.sqrt 2 / 2) :
    2 * Real.arcsin r ≤ Real.pi / 2 := by
  have hr1 : r ≤ 1 := by linarith [sqrt_two_le_two]
  have hx : r ∈ Set.Icc (-1 : ℝ) 1 := ⟨by linarith, hr1⟩
  have hy : Real.pi / 4 ∈ Set.Icc (-(Real.pi / 2)) (Real.pi / 2) := by
    constructor <;> linarith [Real.pi_pos]
  have : Real.arcsin r ≤ Real.pi / 4 := by
    rw [Real.arcsin_le_iff_le_sin hx hy, Real.sin_pi_div_four]
    exact h1
  linarith

/-- Closed form of `Psi` on `[0, sqrt 2 / 2]`: `Psi r = 2 r sqrt(1 - r^2)`. -/
theorem Psi_eq_of_le (r : ℝ) (h0 : 0 ≤ r) (h1 : r ≤ Real.sqrt 2 / 2) :
    Psi r = 2 * r * Real.sqrt (1 - r ^ 2) := by
  have hr1 : r ≤ 1 := by linarith [sqrt_two_le_two]
  unfold Psi
  rw [min_eq_left (two_arcsin_le_pi_div_two r h0 h1)]
  exact sin_two_arcsin r (by linarith) hr1

/-- On `[sqrt 2 / 2, 1]` the envelope saturates: `Psi r = 1`. -/
theorem Psi_eq_one_of_ge (r : ℝ) (h0 : Real.sqrt 2 / 2 ≤ r) (h1 : r ≤ 1) : Psi r = 1 := by
  have hx : Real.sqrt 2 / 2 ∈ Set.Icc (-1 : ℝ) 1 := by
    constructor
    · have := Real.sqrt_nonneg 2
      linarith
    · linarith [sqrt_two_le_two]
  have hy : Real.pi / 4 ∈ Set.Icc (-(Real.pi / 2)) (Real.pi / 2) := by
    constructor <;> linarith [Real.pi_pos]
  have h4 : Real.pi / 4 ≤ Real.arcsin (Real.sqrt 2 / 2) := by
    rw [Real.le_arcsin_iff_sin_le hy hx, Real.sin_pi_div_four]
  have hmono : Real.arcsin (Real.sqrt 2 / 2) ≤ Real.arcsin r := Real.monotone_arcsin h0
  have : Real.pi / 2 ≤ 2 * Real.arcsin r := by linarith
  unfold Psi
  rw [min_eq_right this, Real.sin_pi_div_two]

/-- `Psi r <= 1` always. -/
theorem Psi_le_one (r : ℝ) : Psi r ≤ 1 := Real.sin_le_one _

/-- `Psi r >= 0` for `r >= 0`. -/
theorem Psi_nonneg (r : ℝ) (h0 : 0 ≤ r) : 0 ≤ Psi r := by
  unfold Psi
  apply Real.sin_nonneg_of_nonneg_of_le_pi
  · apply le_min
    · have := Real.arcsin_nonneg.mpr h0
      linarith
    · linarith [Real.pi_pos]
  · exact le_trans (min_le_right _ _) (by linarith [Real.pi_pos])

/-- `sqrt (1 - r^2) <= 1`. -/
theorem sqrt_one_sub_sq_le_one (r : ℝ) : Real.sqrt (1 - r ^ 2) ≤ 1 := by
  calc Real.sqrt (1 - r ^ 2) ≤ Real.sqrt 1 := Real.sqrt_le_sqrt (by nlinarith [sq_nonneg r])
    _ = 1 := Real.sqrt_one

/-- The envelope is bounded by twice its argument: `Psi r <= 2 r` for `0 <= r <= 1`. -/
theorem Psi_le_two_mul (r : ℝ) (h0 : 0 ≤ r) (h1 : r ≤ 1) : Psi r ≤ 2 * r := by
  by_cases hc : r ≤ Real.sqrt 2 / 2
  · rw [Psi_eq_of_le r h0 hc]
    have hs := sqrt_one_sub_sq_le_one r
    have : 0 ≤ 2 * r := by linarith
    calc 2 * r * Real.sqrt (1 - r ^ 2) ≤ 2 * r * 1 :=
          mul_le_mul_of_nonneg_left hs this
      _ = 2 * r := by ring
  · have hc' : Real.sqrt 2 / 2 < r := lt_of_not_ge hc
    rw [Psi_eq_one_of_ge r hc'.le h1]
    linarith [one_le_sqrt_two]

/-- `Psi` is nondecreasing on `[0, 1]`. -/
theorem Psi_mono (r s : ℝ) (h0 : 0 ≤ r) (hrs : r ≤ s) (_h1 : s ≤ 1) : Psi r ≤ Psi s := by
  unfold Psi
  apply Real.sin_le_sin_of_le_of_le_pi_div_two
  · have := Real.arcsin_nonneg.mpr h0
    have hp := Real.pi_pos
    exact le_trans (by linarith : -(Real.pi / 2) ≤ 0) (le_min (by linarith) (by linarith))
  · exact min_le_right _ _
  · exact min_le_min (by linarith [Real.monotone_arcsin hrs]) le_rfl

/-- The strong bound of Theorem 1.1: if `phi <= 1/4` then
`Psi (sqrt (2 phi)) = 2 sqrt (2 phi (1 - 2 phi))`. -/
theorem Psi_sqrt_two_phi (φ : ℝ) (h0 : 0 ≤ φ) (h1 : φ ≤ 1 / 4) :
    Psi (Real.sqrt (2 * φ)) = 2 * Real.sqrt (2 * φ * (1 - 2 * φ)) := by
  have hs0 : 0 ≤ Real.sqrt (2 * φ) := Real.sqrt_nonneg _
  have hs1 : Real.sqrt (2 * φ) ≤ Real.sqrt 2 / 2 := by
    have : Real.sqrt 2 / 2 = Real.sqrt (1 / 2) := by
      rw [show (1 / 2 : ℝ) = 2 / 2 ^ 2 by norm_num, Real.sqrt_div (by norm_num),
        Real.sqrt_sq (by norm_num)]
    rw [this]
    exact Real.sqrt_le_sqrt (by linarith)
  rw [Psi_eq_of_le _ hs0 hs1, Real.sq_sqrt (by linarith),
    Real.sqrt_mul (show (0:ℝ) ≤ 2 * φ by linarith)]
  ring

/-- The bookkeeping behind Theorem 1.1.  If a quantity `ρ` satisfies `ρ <= Psi κ` (the output of
the tensorization step) and `κ^2 <= 2 φ` (the channel and row-good-set lemmas), then
`ρ <= min 1 (2 sqrt (2 φ))`. -/
theorem main_simple_bound (ρ κ φ : ℝ) (hρ : ρ ≤ Psi κ) (hκ0 : 0 ≤ κ) (hκ1 : κ ≤ 1)
    (hκφ : κ ^ 2 ≤ 2 * φ) : ρ ≤ min 1 (2 * Real.sqrt (2 * φ)) := by
  apply le_min
  · exact le_trans hρ (Psi_le_one κ)
  · have hk : κ ≤ Real.sqrt (2 * φ) := by
      calc κ = Real.sqrt (κ ^ 2) := (Real.sqrt_sq hκ0).symm
        _ ≤ Real.sqrt (2 * φ) := Real.sqrt_le_sqrt hκφ
    calc ρ ≤ Psi κ := hρ
      _ ≤ 2 * κ := Psi_le_two_mul κ hκ0 hκ1
      _ ≤ 2 * Real.sqrt (2 * φ) := by linarith

/-- The strong form: with `φ <= 1/4` one gets `ρ <= 2 sqrt (2 φ (1 - 2 φ))`. -/
theorem main_strong_bound (ρ κ φ : ℝ) (hρ : ρ ≤ Psi κ) (hκ0 : 0 ≤ κ)
    (hφ0 : 0 ≤ φ) (hφ1 : φ ≤ 1 / 4) (hκφ : κ ^ 2 ≤ 2 * φ) :
    ρ ≤ 2 * Real.sqrt (2 * φ * (1 - 2 * φ)) := by
  have hk : κ ≤ Real.sqrt (2 * φ) := by
    calc κ = Real.sqrt (κ ^ 2) := (Real.sqrt_sq hκ0).symm
      _ ≤ Real.sqrt (2 * φ) := Real.sqrt_le_sqrt hκφ
  have hs1 : Real.sqrt (2 * φ) ≤ 1 := by
    calc Real.sqrt (2 * φ) ≤ Real.sqrt 1 := Real.sqrt_le_sqrt (by linarith)
      _ = 1 := Real.sqrt_one
  calc ρ ≤ Psi κ := hρ
    _ ≤ Psi (Real.sqrt (2 * φ)) := Psi_mono κ _ hκ0 hk hs1
    _ = 2 * Real.sqrt (2 * φ * (1 - 2 * φ)) := Psi_sqrt_two_phi φ hφ0 hφ1

/-- Corollary 5.3: the threshold `φ < 1/8` makes the simple bound strictly less than one. -/
theorem one_lag_threshold (φ : ℝ) (h0 : 0 ≤ φ) (h : φ < 1 / 8) : 2 * Real.sqrt (2 * φ) < 1 := by
  have : Real.sqrt (2 * φ) < 1 / 2 := by
    have h4 : Real.sqrt ((1 / 2 : ℝ) ^ 2) = 1 / 2 := Real.sqrt_sq (by norm_num)
    calc Real.sqrt (2 * φ) < Real.sqrt ((1 / 2 : ℝ) ^ 2) :=
          Real.sqrt_lt_sqrt (by linarith) (by norm_num; linarith)
      _ = 1 / 2 := h4
  linarith

/-- The strong bound is strictly below one as soon as `φ < 1/4` (the remark after
Corollary 5.3): `2 sqrt (2 φ (1 - 2 φ)) < 1` for `0 <= φ < 1/4`. -/
theorem strong_threshold (φ : ℝ) (h0 : 0 ≤ φ) (h : φ < 1 / 4) :
    2 * Real.sqrt (2 * φ * (1 - 2 * φ)) < 1 := by
  have hlt : 2 * φ * (1 - 2 * φ) < (1 / 2 : ℝ) ^ 2 := by nlinarith
  have : Real.sqrt (2 * φ * (1 - 2 * φ)) < 1 / 2 := by
    calc Real.sqrt (2 * φ * (1 - 2 * φ)) < Real.sqrt ((1 / 2 : ℝ) ^ 2) :=
          Real.sqrt_lt_sqrt (by nlinarith) hlt
      _ = 1 / 2 := Real.sqrt_sq (by norm_num)
  linarith

/-- Corollary 5.2 (rate transfer): `φ <= A e^{-c n}` gives
`2 sqrt (2 φ) <= 2 sqrt (2 A) e^{-c n / 2}`. -/
theorem rate_transfer (φ A c : ℝ) (n : ℕ) (_hφ : 0 ≤ φ) (hA : 0 ≤ A)
    (h : φ ≤ A * Real.exp (-(c * n))) :
    2 * Real.sqrt (2 * φ) ≤ 2 * Real.sqrt (2 * A) * Real.exp (-(c * n) / 2) := by
  have hexp : Real.exp (-(c * n) / 2) ^ 2 = Real.exp (-(c * n)) := by
    rw [sq, ← Real.exp_add]
    ring_nf
  have hsq : Real.sqrt (Real.exp (-(c * n))) = Real.exp (-(c * n) / 2) := by
    rw [← hexp]
    exact Real.sqrt_sq (Real.exp_pos _).le
  calc 2 * Real.sqrt (2 * φ) ≤ 2 * Real.sqrt (2 * A * Real.exp (-(c * n))) := by
        have : 2 * φ ≤ 2 * A * Real.exp (-(c * n)) := by nlinarith
        have := Real.sqrt_le_sqrt this
        linarith
    _ = 2 * Real.sqrt (2 * A) * Real.exp (-(c * n) / 2) := by
        rw [Real.sqrt_mul (by linarith), hsq]
        ring

/-- Section 9: the lower envelope never exceeds the upper one, `sqrt (2 x) <= 2 sqrt (2 x (1 - 2 x))`
for `0 <= x <= 1/4`. -/
theorem envelope_consistent (x : ℝ) (h0 : 0 ≤ x) (h1 : x ≤ 1 / 4) :
    Real.sqrt (2 * x) ≤ 2 * Real.sqrt (2 * x * (1 - 2 * x)) := by
  have h4 : Real.sqrt 4 = 2 := by
    rw [show (4:ℝ) = 2 ^ 2 by norm_num]
    exact Real.sqrt_sq (by norm_num)
  have h2 : 2 * Real.sqrt (2 * x * (1 - 2 * x)) = Real.sqrt (4 * (2 * x * (1 - 2 * x))) := by
    rw [Real.sqrt_mul (show (0:ℝ) ≤ 4 by norm_num), h4]
  rw [h2]
  exact Real.sqrt_le_sqrt (by nlinarith)

/-! ### Proposition 8.1: the two-state chain

The lower bound of Proposition 8.1 is `2r/(1+r^2)` and the upper bound is `Psi r`.  The following
inequalities give the first-order expansion `rho*(n) = 2r + O(r^3)` and show that the lower bound
never exceeds the upper bound on the whole range `0 <= r <= sqrt 2 / 2`. -/

/-- `sqrt (1 - r^2) <= 1 - r^2/2` on `[-1, 1]`. -/
theorem sqrt_one_sub_sq_le (r : ℝ) (h : r ^ 2 ≤ 1) :
    Real.sqrt (1 - r ^ 2) ≤ 1 - r ^ 2 / 2 := by
  have hn : 0 ≤ 1 - r ^ 2 / 2 := by linarith
  calc Real.sqrt (1 - r ^ 2) ≤ Real.sqrt ((1 - r ^ 2 / 2) ^ 2) :=
        Real.sqrt_le_sqrt (by nlinarith)
    _ = 1 - r ^ 2 / 2 := Real.sqrt_sq hn

/-- `1 - r^2/2 - r^4/2 <= sqrt (1 - r^2)` on `[-1, 1]`. -/
theorem le_sqrt_one_sub_sq (r : ℝ) (h : r ^ 2 ≤ 1) :
    1 - r ^ 2 / 2 - r ^ 4 / 2 ≤ Real.sqrt (1 - r ^ 2) := by
  have hn : 0 ≤ 1 - r ^ 2 / 2 - r ^ 4 / 2 := by
    have : r ^ 4 ≤ r ^ 2 := by nlinarith [sq_nonneg r]
    nlinarith
  calc 1 - r ^ 2 / 2 - r ^ 4 / 2 = Real.sqrt ((1 - r ^ 2 / 2 - r ^ 4 / 2) ^ 2) :=
        (Real.sqrt_sq hn).symm
    _ ≤ Real.sqrt (1 - r ^ 2) := by
        apply Real.sqrt_le_sqrt
        nlinarith [sq_nonneg (r ^ 2), sq_nonneg r, pow_nonneg (sq_nonneg r) 2]

theorem sq_le_one_of_le_sqrt_two_div_two (r : ℝ) (h0 : 0 ≤ r) (h1 : r ≤ Real.sqrt 2 / 2) :
    r ^ 2 ≤ 1 := by
  have : r ^ 2 ≤ (Real.sqrt 2 / 2) ^ 2 := by
    rw [sq, sq]
    exact mul_le_mul h1 h1 h0 (by positivity)
  rw [sqrt_two_div_two_sq] at this
  linarith

/-- Upper expansion of the envelope: `Psi r <= 2 r - r^3` for `0 <= r <= sqrt 2 / 2`. -/
theorem Psi_le_expansion (r : ℝ) (h0 : 0 ≤ r) (h1 : r ≤ Real.sqrt 2 / 2) :
    Psi r ≤ 2 * r - r ^ 3 := by
  rw [Psi_eq_of_le r h0 h1]
  have hr2 : r ^ 2 ≤ 1 := sq_le_one_of_le_sqrt_two_div_two r h0 h1
  have := sqrt_one_sub_sq_le r hr2
  have h2r : 0 ≤ 2 * r := by linarith
  calc 2 * r * Real.sqrt (1 - r ^ 2) ≤ 2 * r * (1 - r ^ 2 / 2) :=
        mul_le_mul_of_nonneg_left this h2r
    _ = 2 * r - r ^ 3 := by ring

/-- Lower expansion of the envelope: `2 r - r^3 - r^5 <= Psi r` for `0 <= r <= sqrt 2 / 2`. -/
theorem expansion_le_Psi (r : ℝ) (h0 : 0 ≤ r) (h1 : r ≤ Real.sqrt 2 / 2) :
    2 * r - r ^ 3 - r ^ 5 ≤ Psi r := by
  rw [Psi_eq_of_le r h0 h1]
  have hr2 : r ^ 2 ≤ 1 := sq_le_one_of_le_sqrt_two_div_two r h0 h1
  have := le_sqrt_one_sub_sq r hr2
  have h2r : 0 ≤ 2 * r := by linarith
  calc 2 * r - r ^ 3 - r ^ 5 = 2 * r * (1 - r ^ 2 / 2 - r ^ 4 / 2) := by ring
    _ ≤ 2 * r * Real.sqrt (1 - r ^ 2) := mul_le_mul_of_nonneg_left this h2r

/-- The two-state lower bound `2r/(1+r^2)` lies between `2r - 2r^3` and `2r - 2r^3 + 2r^5`. -/
theorem lower_bound_expansion (r : ℝ) (h0 : 0 ≤ r) :
    2 * r - 2 * r ^ 3 ≤ 2 * r / (1 + r ^ 2) ∧
      2 * r / (1 + r ^ 2) ≤ 2 * r - 2 * r ^ 3 + 2 * r ^ 5 := by
  have hpos : 0 < 1 + r ^ 2 := by positivity
  constructor
  · rw [le_div_iff₀ hpos]
    nlinarith [pow_nonneg h0 5]
  · rw [div_le_iff₀ hpos]
    nlinarith [pow_nonneg h0 7]

/-- Consistency of Proposition 8.1 with Theorem 1.1: the lower bound `2r/(1+r^2)` never exceeds
the upper bound `Psi r` on `0 <= r <= sqrt 2 / 2`. -/
theorem lower_le_upper (r : ℝ) (h0 : 0 ≤ r) (h1 : r ≤ Real.sqrt 2 / 2) :
    2 * r / (1 + r ^ 2) ≤ Psi r := by
  rw [Psi_eq_of_le r h0 h1]
  have hr2 : r ^ 2 ≤ 1 / 2 := by
    have : r ^ 2 ≤ (Real.sqrt 2 / 2) ^ 2 := by
      rw [sq, sq]
      exact mul_le_mul h1 h1 h0 (by positivity)
    rw [sqrt_two_div_two_sq] at this
    exact this
  -- it suffices that 1/(1+r^2) <= sqrt(1-r^2), i.e. 1 <= (1-r^2)(1+r^2)^2
  have hkey : 1 / (1 + r ^ 2) ≤ Real.sqrt (1 - r ^ 2) := by
    have hn : 0 ≤ 1 / (1 + r ^ 2) := by positivity
    calc 1 / (1 + r ^ 2) = Real.sqrt ((1 / (1 + r ^ 2)) ^ 2) := (Real.sqrt_sq hn).symm
      _ ≤ Real.sqrt (1 - r ^ 2) := by
          apply Real.sqrt_le_sqrt
          rw [div_pow, one_pow, div_le_iff₀ (by positivity)]
          nlinarith [sq_nonneg r, sq_nonneg (r ^ 2), pow_nonneg (sq_nonneg r) 2,
            pow_nonneg (sq_nonneg r) 3]
  calc 2 * r / (1 + r ^ 2) = 2 * r * (1 / (1 + r ^ 2)) := by ring
    _ ≤ 2 * r * Real.sqrt (1 - r ^ 2) := mul_le_mul_of_nonneg_left hkey (by linarith)

end BradleyQ5

#print axioms BradleyQ5.sin_two_arcsin
#print axioms BradleyQ5.Psi_eq_of_le
#print axioms BradleyQ5.Psi_eq_one_of_ge
#print axioms BradleyQ5.Psi_le_two_mul
#print axioms BradleyQ5.Psi_mono
#print axioms BradleyQ5.Psi_sqrt_two_phi
#print axioms BradleyQ5.main_simple_bound
#print axioms BradleyQ5.main_strong_bound
#print axioms BradleyQ5.one_lag_threshold
#print axioms BradleyQ5.strong_threshold
#print axioms BradleyQ5.rate_transfer
#print axioms BradleyQ5.envelope_consistent
#print axioms BradleyQ5.Psi_le_expansion
#print axioms BradleyQ5.expansion_le_Psi
#print axioms BradleyQ5.lower_bound_expansion
#print axioms BradleyQ5.lower_le_upper
