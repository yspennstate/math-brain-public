import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Data.Finset.Powerset
import Mathlib.Tactic

/-!
Theorem 4.1 of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7), from Lemma 4.3.

`thm41_of_hub`: let `F` be a function on the finite subsets of `I` with `F(∅) > 0`; in the paper `F = Θ_ℓ`, so that
`F(∅) = E_ℓ(M)`. Suppose the conclusion (4.4) of Lemma 4.3,
`φ ≤ π^ℓ e^{ℓ/2} (2e)^{(ℓ-k)/2} ω(ℓ-k)^{1/2} F(H)^{-1/2} |t|^{-ℓ}`, holds for every `H ⊆ I` with `k = |H| ≤ ℓ`,
`F(H) > 0` and, when `k < ℓ`, condition (4.3). Then `φ ≤ (√2 π e)^ℓ ω(ℓ)^{1/2} F(∅)^{-1/2} |t|^{-ℓ}`, which is (4.2)
for `φ = |φ_Q(t)|²`. The proof is the paper's: the stopping procedure gives `H` with `F(H) ≥ 2^{-k} F(∅)`, and
`a_k ≤ a_0`.

`thm41_one`, `thm41_two`, `thm41_three`: the cases `ℓ = 1, 2, 3`, with `ω(1) = 1`, `ω(2) = 2`, `ω(3) = 9/2`, in the
form in which Corollary 4.4 (c), (b) and (a) take them as hypotheses (`FiveS4CorA.lean`, `FiveS4CorB.lean`).

The stopping procedure and the constant lemmas are repeated from `FiveS4.lean`, so that this file compiles on its own.
-/

open Finset Real

namespace QformFiveB

namespace Thm41

/-- `ω(m) = m^m / m!`; Lean's `0^0 = 1` gives `ω(0) = 1`, as in the paper. -/
noncomputable def omega (m : ℕ) : ℝ := (m : ℝ) ^ m / (m.factorial : ℝ)

theorem omega_zero : omega 0 = 1 := by simp [omega]

theorem omega_pos (m : ℕ) : 0 < omega m := by
  unfold omega
  rcases Nat.eq_zero_or_pos m with h | h
  · subst h; simp
  · exact div_pos (pow_pos (by exact_mod_cast h) m) (by exact_mod_cast Nat.factorial_pos m)

/-- `ω(m) ≤ ω(m+1)`: `ω(m+1)/ω(m) = ((m+1)/m)^m ≥ 1` (proof of Theorem 4.1). -/
theorem omega_le_succ (m : ℕ) : omega m ≤ omega (m + 1) := by
  unfold omega
  have hf : ((m + 1).factorial : ℝ) = ((m : ℝ) + 1) * (m.factorial : ℝ) := by
    rw [Nat.factorial_succ]; push_cast; ring
  have hm1 : (0 : ℝ) < (m : ℝ) + 1 := by positivity
  have hfac : (0 : ℝ) < (m.factorial : ℝ) := by exact_mod_cast Nat.factorial_pos m
  have e : ((((m + 1 : ℕ) : ℝ)) ^ (m + 1)) / ((m + 1).factorial : ℝ)
      = ((m : ℝ) + 1) ^ m / (m.factorial : ℝ) := by
    rw [hf]; push_cast
    field_simp
    ring
  rw [e]
  gcongr
  linarith

theorem omega_mono {j k : ℕ} (h : j ≤ k) : omega j ≤ omega k := by
  induction h with
  | refl => exact le_refl _
  | step _ ih => exact ih.trans (omega_le_succ _)

/-- **The stopping procedure of Theorem 4.1.** For any `F` on finite sets with `F(∅) > 0` and any `ℓ`, there is
`H ⊆ I` with `|H| ≤ ℓ`, `2^{-|H|} F(∅) ≤ F(H)`, and, if `|H| < ℓ`, `F(H ∪ {j}) ≤ F(H)/2` for all `j ∈ I \ H`. -/
theorem hub_selection {ι : Type*} [DecidableEq ι] (I : Finset ι) (F : Finset ι → ℝ) (ℓ : ℕ) :
    ∃ H ⊆ I, H.card ≤ ℓ ∧ (2 : ℝ)⁻¹ ^ H.card * F ∅ ≤ F H ∧
      (H.card < ℓ → ∀ j ∈ I \ H, F (insert j H) ≤ F H / 2) := by
  have aux : ∀ d : ℕ, ∀ H ⊆ I, H.card + d = ℓ → (2 : ℝ)⁻¹ ^ H.card * F ∅ ≤ F H →
      ∃ H' ⊆ I, H'.card ≤ ℓ ∧ (2 : ℝ)⁻¹ ^ H'.card * F ∅ ≤ F H' ∧
        (H'.card < ℓ → ∀ j ∈ I \ H', F (insert j H') ≤ F H' / 2) := by
    intro d
    induction d with
    | zero =>
      intro H hHI hcard hF
      refine ⟨H, hHI, by omega, hF, fun h => absurd h (by omega)⟩
    | succ d ih =>
      intro H hHI hcard hF
      by_cases hall : ∀ j ∈ I \ H, F (insert j H) ≤ F H / 2
      · exact ⟨H, hHI, by omega, hF, fun _ => hall⟩
      · push_neg at hall
        obtain ⟨j, hj, hjF⟩ := hall
        have hjI : j ∈ I := (mem_sdiff.mp hj).1
        have hjH : j ∉ H := (mem_sdiff.mp hj).2
        have hcard' : (insert j H).card = H.card + 1 := card_insert_of_notMem hjH
        apply ih (insert j H) (insert_subset hjI hHI) (by omega)
        rw [hcard', pow_succ]
        have : (2 : ℝ)⁻¹ ^ H.card * F ∅ * 2⁻¹ ≤ F H / 2 := by
          have := mul_le_mul_of_nonneg_right hF (by norm_num : (0 : ℝ) ≤ 2⁻¹)
          linarith [show F H / 2 = F H * 2⁻¹ by ring]
        calc (2 : ℝ)⁻¹ ^ H.card * 2⁻¹ * F ∅ = (2 : ℝ)⁻¹ ^ H.card * F ∅ * 2⁻¹ := by ring
          _ ≤ F H / 2 := this
          _ ≤ F (insert j H) := hjF.le
  exact aux ℓ ∅ (empty_subset I) (by simp) (by simp)

/-- **The constant of Theorem 4.1.** With `a_k² = (2e)^{ℓ-k} ω(ℓ-k) 2^k` (write `j = ℓ - k`),
`e^k a_k² ≤ a_0²`; in particular `a_k ≤ a_0`. -/
theorem decay_const_ratio (j k : ℕ) :
    exp 1 ^ k * ((2 * exp 1) ^ j * omega j * 2 ^ k) ≤ (2 * exp 1) ^ (j + k) * omega (j + k) := by
  have hω := omega_mono (Nat.le_add_right j k)
  have h0 : 0 ≤ (2 * exp 1) ^ j := by positivity
  calc exp 1 ^ k * ((2 * exp 1) ^ j * omega j * 2 ^ k)
      = (2 * exp 1) ^ j * (2 * exp 1) ^ k * omega j := by rw [mul_pow]; ring
    _ ≤ (2 * exp 1) ^ j * (2 * exp 1) ^ k * omega (j + k) := by
        apply mul_le_mul_of_nonneg_left hω; positivity
    _ = (2 * exp 1) ^ (j + k) * omega (j + k) := by rw [pow_add]

theorem decay_const_le (j k : ℕ) :
    (2 * exp 1) ^ j * omega j * 2 ^ k ≤ (2 * exp 1) ^ (j + k) * omega (j + k) := by
  have h := decay_const_ratio j k
  have h1 : 1 ≤ exp 1 ^ k := one_le_pow₀ (by linarith [add_one_le_exp (1 : ℝ)])
  have h2 : 0 ≤ (2 * exp 1) ^ j * omega j * 2 ^ k := by
    have := omega_pos j; positivity
  nlinarith

/-- `π^ℓ e^{ℓ/2} (2e)^{ℓ/2} = (√2 π e)^ℓ`, written with square roots. -/
theorem decay_const_identity (ℓ : ℕ) :
    π ^ ℓ * (√(exp 1)) ^ ℓ * (√(2 * exp 1)) ^ ℓ = (√2 * π * exp 1) ^ ℓ := by
  have he : 0 ≤ exp 1 := (exp_pos 1).le
  have h : π * √(exp 1) * √(2 * exp 1) = √2 * π * exp 1 := by
    rw [Real.sqrt_mul (by norm_num : (0 : ℝ) ≤ 2)]
    have : √(exp 1) * √(exp 1) = exp 1 := Real.mul_self_sqrt he
    calc π * √(exp 1) * (√2 * √(exp 1)) = √2 * π * (√(exp 1) * √(exp 1)) := by ring
      _ = √2 * π * exp 1 := by rw [this]
  rw [← mul_pow, ← mul_pow, h]

theorem omega_one : omega 1 = 1 := by norm_num [omega]

theorem omega_two : omega 2 = 2 := by norm_num [omega, Nat.factorial]

theorem omega_three : omega 3 = 9 / 2 := by norm_num [omega, Nat.factorial]

theorem sq_sqrt_pow (x : ℝ) (hx : 0 ≤ x) (n : ℕ) : (√x ^ n) ^ 2 = x ^ n := by
  rw [← pow_mul, mul_comm, pow_mul, Real.sq_sqrt hx]

theorem sqrt_pow_eq (x : ℝ) (hx : 0 ≤ x) (n : ℕ) : √(x ^ n) = √x ^ n := by
  rw [← sq_sqrt_pow x hx n, Real.sqrt_sq (by positivity)]

/-- `a_k ≤ a_0`, with square roots: `√(2e)^{ℓ-k} ω(ℓ-k)^{1/2} √2^k ≤ √(2e)^ℓ ω(ℓ)^{1/2}` for `k ≤ ℓ`. -/
theorem decay_const_sqrt_le (ℓ k : ℕ) (hk : k ≤ ℓ) :
    √(2 * exp 1) ^ (ℓ - k) * √(omega (ℓ - k)) * √2 ^ k ≤ √(2 * exp 1) ^ ℓ * √(omega ℓ) := by
  have h2e : (0 : ℝ) ≤ 2 * exp 1 := by positivity
  have hω1 := (omega_pos (ℓ - k)).le
  have hω2 := (omega_pos ℓ).le
  have h := decay_const_le (ℓ - k) k
  rw [Nat.sub_add_cancel hk] at h
  have ha : 0 ≤ √(2 * exp 1) ^ (ℓ - k) * √(omega (ℓ - k)) * √2 ^ k := by positivity
  have hb : 0 ≤ √(2 * exp 1) ^ ℓ * √(omega ℓ) := by positivity
  refine (pow_le_pow_iff_left₀ ha hb two_ne_zero).1 ?_
  rw [mul_pow, mul_pow, mul_pow, sq_sqrt_pow _ h2e, sq_sqrt_pow _ h2e, sq_sqrt_pow _ (by norm_num : (0 : ℝ) ≤ 2),
    Real.sq_sqrt hω1, Real.sq_sqrt hω2]
  exact h

theorem rpow_neg_half_eq (x : ℝ) (hx : 0 < x) : x ^ (-(1 / 2 : ℝ)) = (√x)⁻¹ := by
  rw [Real.rpow_neg hx.le, ← Real.sqrt_eq_rpow]

/-- `F(H) ≥ 2^{-k} F(∅) > 0` gives `F(H)^{-1/2} ≤ √2^k F(∅)^{-1/2}`. -/
theorem neg_half_le (a b : ℝ) (k : ℕ) (hb : 0 < b) (h : (2 : ℝ)⁻¹ ^ k * b ≤ a) :
    a ^ (-(1 / 2 : ℝ)) ≤ √2 ^ k * b ^ (-(1 / 2 : ℝ)) := by
  have h2k : 0 < (2 : ℝ)⁻¹ ^ k * b := by positivity
  have ha : 0 < a := h2k.trans_le h
  rw [rpow_neg_half_eq a ha, rpow_neg_half_eq b hb]
  have hs : √((2 : ℝ)⁻¹ ^ k * b) = (√2 ^ k)⁻¹ * √b := by
    rw [Real.sqrt_mul (by positivity), inv_pow, Real.sqrt_inv, sqrt_pow_eq 2 (by norm_num)]
  have hle : (√2 ^ k)⁻¹ * √b ≤ √a := hs ▸ Real.sqrt_le_sqrt h
  have hpos : 0 < (√2 ^ k)⁻¹ * √b := by positivity
  calc (√a)⁻¹ ≤ ((√2 ^ k)⁻¹ * √b)⁻¹ := inv_anti₀ hpos hle
    _ = √2 ^ k * (√b)⁻¹ := by rw [mul_inv, inv_inv]

/-- **Theorem 4.1 from Lemma 4.3.** If (4.4) holds for every admissible `H`, then (4.2) holds:
`φ ≤ (√2 π e)^ℓ ω(ℓ)^{1/2} F(∅)^{-1/2} |t|^{-ℓ}`. -/
theorem thm41_of_hub {ι : Type*} [DecidableEq ι] (I : Finset ι) (F : Finset ι → ℝ) (ℓ : ℕ) (hF : 0 < F ∅)
    (φ t : ℝ)
    (hhub : ∀ H ⊆ I, H.card ≤ ℓ → 0 < F H → (H.card < ℓ → ∀ j ∈ I \ H, F (insert j H) ≤ F H / 2) →
      φ ≤ π ^ ℓ * √(exp 1) ^ ℓ * √(2 * exp 1) ^ (ℓ - H.card) * √(omega (ℓ - H.card))
        * F H ^ (-(1 / 2 : ℝ)) * |t| ^ (-(ℓ : ℝ))) :
    φ ≤ (√2 * π * exp 1) ^ ℓ * √(omega ℓ) * F ∅ ^ (-(1 / 2 : ℝ)) * |t| ^ (-(ℓ : ℝ)) := by
  obtain ⟨H, hHI, hcard, hFH, hdiff⟩ := hub_selection I F ℓ
  have h2k : 0 < (2 : ℝ)⁻¹ ^ H.card * F ∅ := by positivity
  have hFHpos : 0 < F H := h2k.trans_le hFH
  have h := hhub H hHI hcard hFHpos hdiff
  have hinv := neg_half_le (F H) (F ∅) H.card hF hFH
  have hT : 0 ≤ |t| ^ (-(ℓ : ℝ)) := Real.rpow_nonneg (abs_nonneg t) _
  have hF0 : 0 ≤ F ∅ ^ (-(1 / 2 : ℝ)) := Real.rpow_nonneg hF.le _
  have hP : 0 ≤ π ^ ℓ * √(exp 1) ^ ℓ := by positivity
  have hP' : 0 ≤ π ^ ℓ * √(exp 1) ^ ℓ * √(2 * exp 1) ^ (ℓ - H.card) * √(omega (ℓ - H.card)) := by positivity
  calc φ ≤ π ^ ℓ * √(exp 1) ^ ℓ * √(2 * exp 1) ^ (ℓ - H.card) * √(omega (ℓ - H.card))
        * F H ^ (-(1 / 2 : ℝ)) * |t| ^ (-(ℓ : ℝ)) := h
    _ ≤ π ^ ℓ * √(exp 1) ^ ℓ * √(2 * exp 1) ^ (ℓ - H.card) * √(omega (ℓ - H.card))
        * (√2 ^ H.card * F ∅ ^ (-(1 / 2 : ℝ))) * |t| ^ (-(ℓ : ℝ)) :=
        mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left hinv hP') hT
    _ = π ^ ℓ * √(exp 1) ^ ℓ * (√(2 * exp 1) ^ (ℓ - H.card) * √(omega (ℓ - H.card)) * √2 ^ H.card)
        * F ∅ ^ (-(1 / 2 : ℝ)) * |t| ^ (-(ℓ : ℝ)) := by ring
    _ ≤ π ^ ℓ * √(exp 1) ^ ℓ * (√(2 * exp 1) ^ ℓ * √(omega ℓ)) * F ∅ ^ (-(1 / 2 : ℝ)) * |t| ^ (-(ℓ : ℝ)) :=
        mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_right
          (mul_le_mul_of_nonneg_left (decay_const_sqrt_le ℓ H.card hcard) hP) hF0) hT
    _ = (π ^ ℓ * √(exp 1) ^ ℓ * √(2 * exp 1) ^ ℓ) * √(omega ℓ) * F ∅ ^ (-(1 / 2 : ℝ)) * |t| ^ (-(ℓ : ℝ)) := by
        ring
    _ = (√2 * π * exp 1) ^ ℓ * √(omega ℓ) * F ∅ ^ (-(1 / 2 : ℝ)) * |t| ^ (-(ℓ : ℝ)) := by
        rw [decay_const_identity]

/-- Theorem 4.1 with `ℓ = 3` (`ω(3) = 9/2`), the hypothesis of Corollary 4.4(a). -/
theorem thm41_three {ι : Type*} [DecidableEq ι] (I : Finset ι) (F : Finset ι → ℝ) (hF : 0 < F ∅) (φ t : ℝ)
    (hhub : ∀ H ⊆ I, H.card ≤ 3 → 0 < F H → (H.card < 3 → ∀ j ∈ I \ H, F (insert j H) ≤ F H / 2) →
      φ ≤ π ^ 3 * √(exp 1) ^ 3 * √(2 * exp 1) ^ (3 - H.card) * √(omega (3 - H.card))
        * F H ^ (-(1 / 2 : ℝ)) * |t| ^ (-((3 : ℕ) : ℝ))) :
    φ ≤ (√2 * π * exp 1) ^ 3 * √(9 / 2) * F ∅ ^ (-(1 / 2 : ℝ)) * |t| ^ (-(3 : ℝ)) := by
  have h := thm41_of_hub I F 3 hF φ t hhub
  have e : ((3 : ℕ) : ℝ) = 3 := by norm_num
  rw [omega_three, e] at h
  exact h

/-- Theorem 4.1 with `ℓ = 2` (`ω(2) = 2`), the hypothesis of Corollary 4.4(b). -/
theorem thm41_two {ι : Type*} [DecidableEq ι] (I : Finset ι) (F : Finset ι → ℝ) (hF : 0 < F ∅) (φ t : ℝ)
    (hhub : ∀ H ⊆ I, H.card ≤ 2 → 0 < F H → (H.card < 2 → ∀ j ∈ I \ H, F (insert j H) ≤ F H / 2) →
      φ ≤ π ^ 2 * √(exp 1) ^ 2 * √(2 * exp 1) ^ (2 - H.card) * √(omega (2 - H.card))
        * F H ^ (-(1 / 2 : ℝ)) * |t| ^ (-((2 : ℕ) : ℝ))) :
    φ ≤ (√2 * π * exp 1) ^ 2 * √2 * F ∅ ^ (-(1 / 2 : ℝ)) * |t| ^ (-(2 : ℝ)) := by
  have h := thm41_of_hub I F 2 hF φ t hhub
  have e : ((2 : ℕ) : ℝ) = 2 := by norm_num
  rw [omega_two, e] at h
  exact h

/-- Theorem 4.1 with `ℓ = 1` (`ω(1) = 1`), the hypothesis of Corollary 4.4(c). -/
theorem thm41_one {ι : Type*} [DecidableEq ι] (I : Finset ι) (F : Finset ι → ℝ) (hF : 0 < F ∅) (φ t : ℝ)
    (hhub : ∀ H ⊆ I, H.card ≤ 1 → 0 < F H → (H.card < 1 → ∀ j ∈ I \ H, F (insert j H) ≤ F H / 2) →
      φ ≤ π ^ 1 * √(exp 1) ^ 1 * √(2 * exp 1) ^ (1 - H.card) * √(omega (1 - H.card))
        * F H ^ (-(1 / 2 : ℝ)) * |t| ^ (-((1 : ℕ) : ℝ))) :
    φ ≤ (√2 * π * exp 1) ^ 1 * √1 * F ∅ ^ (-(1 / 2 : ℝ)) * |t| ^ (-(1 : ℝ)) := by
  have h := thm41_of_hub I F 1 hF φ t hhub
  rw [omega_one, Nat.cast_one] at h
  exact h

end Thm41

end QformFiveB
