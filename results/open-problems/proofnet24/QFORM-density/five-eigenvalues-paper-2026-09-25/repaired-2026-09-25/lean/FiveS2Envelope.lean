import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.MeasureTheory.Measure.Lebesgue.Integral
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic

/-!
The envelope integrals of Lemmas 2.2 and 2.3 of "Quadratic forms with five large singular values have bounded
densities" (repaired text, sha256 90f859b7).

* `envelope_integral`: `∫_ℝ min{1, (a/|t|)^p} dt = 2ap/(p-1)` for `a > 0`, `p > 1`.
* `envelope_density_constant`: `(2π)^{-1} · 2ap/(p-1) = ap/(π(p-1))`, the bound of Lemma 2.2 after Lemma 2.1(b).
* `halfmoment_envelope_integral`: `∫_ℝ |t|^{-1/2} min{1, u/|t|} dt = 8√u` for `u > 0`.
* `halfmoment_envelope_constant`: `8√u/√(2π) = 8√(u/(2π))`, the bound of Lemma 2.3 after (2.1).

At `t = 0` the integrands take the value `0` in Lean (division by zero); a single point does not change an integral.
-/

open Real MeasureTheory Set

namespace QformFiveB

/-- **Lemma 2.2, the envelope integral.** `∫_ℝ min{1, (a/|t|)^p} dt = 2ap/(p-1)`. -/
theorem envelope_integral (a p : ℝ) (ha : 0 < a) (hp : 1 < p) :
    ∫ t : ℝ, min 1 ((a / |t|) ^ p) = 2 * a * p / (p - 1) := by
  have hsym := integral_comp_abs (f := fun s : ℝ => min 1 ((a / s) ^ p))
  simp only at hsym
  rw [hsym]
  have hg1 : ∀ x ∈ Ioc (0 : ℝ) a, min 1 ((a / x) ^ p) = 1 := by
    intro x hx
    have h1 : 1 ≤ a / x := by rw [le_div_iff₀ hx.1]; linarith [hx.2]
    exact min_eq_left (one_le_rpow h1 (by linarith))
  have hg2 : ∀ x ∈ Ioi a, min 1 ((a / x) ^ p) = a ^ p * x ^ (-p) := by
    intro x hx
    have hx0 : 0 < x := lt_trans ha hx
    have h1 : a / x ≤ 1 := by rw [div_le_one hx0]; exact le_of_lt hx
    rw [min_eq_right (rpow_le_one (by positivity) h1 (by linarith)), div_rpow ha.le hx0.le,
      rpow_neg hx0.le, div_eq_mul_inv]
  have hint1 : IntegrableOn (fun x : ℝ => min 1 ((a / x) ^ p)) (Ioc 0 a) :=
    IntegrableOn.congr_fun (integrableOn_const (C := (1 : ℝ))
      (by rw [Real.volume_Ioc]; exact ENNReal.ofReal_ne_top)) (fun x hx => (hg1 x hx).symm) measurableSet_Ioc
  have hint2 : IntegrableOn (fun x : ℝ => min 1 ((a / x) ^ p)) (Ioi a) :=
    IntegrableOn.congr_fun (Integrable.const_mul (integrableOn_Ioi_rpow_of_lt (by linarith : -p < -1) ha)
      (a ^ p)) (fun x hx => (hg2 x hx).symm) measurableSet_Ioi
  rw [← Ioc_union_Ioi_eq_Ioi ha.le, setIntegral_union Ioc_disjoint_Ioi_same measurableSet_Ioi hint1 hint2,
    setIntegral_congr_fun measurableSet_Ioc hg1, setIntegral_congr_fun measurableSet_Ioi hg2,
    setIntegral_const, volume_real_Ioc_of_le ha.le, integral_const_mul,
    integral_Ioi_rpow_of_lt (by linarith) ha]
  have key : a ^ p * a ^ (-p + 1) = a := by
    rw [← rpow_add ha, show p + (-p + 1) = 1 by ring, rpow_one]
  have e : a ^ p * (-a ^ (-p + 1) / (-p + 1)) = -(a ^ p * a ^ (-p + 1)) / (-p + 1) := by ring
  rw [e, key, smul_eq_mul, mul_one, sub_zero]
  have hp1 : (-p + 1) ≠ 0 := by linarith
  have hp2 : p - 1 ≠ 0 := by linarith
  field_simp
  ring

/-- Lemma 2.2's constant: `(2π)^{-1} · 2ap/(p-1) = ap/(π(p-1))`. -/
theorem envelope_density_constant (a p : ℝ) (hp : 1 < p) :
    (2 * π)⁻¹ * (2 * a * p / (p - 1)) = a * p / (π * (p - 1)) := by
  have hp2 : p - 1 ≠ 0 := by linarith
  have hpi : π ≠ 0 := pi_ne_zero
  field_simp

/-- **Lemma 2.3, the envelope integral.** `∫_ℝ |t|^{-1/2} min{1, u/|t|} dt = 8√u`. -/
theorem halfmoment_envelope_integral (u : ℝ) (hu : 0 < u) :
    ∫ t : ℝ, |t| ^ (-(1 / 2 : ℝ)) * min 1 (u / |t|) = 8 * √u := by
  have hsym := integral_comp_abs (f := fun s : ℝ => s ^ (-(1 / 2 : ℝ)) * min 1 (u / s))
  simp only at hsym
  rw [hsym]
  have hg1 : ∀ x ∈ Ioc (0 : ℝ) u, x ^ (-(1 / 2 : ℝ)) * min 1 (u / x) = x ^ (-(1 / 2 : ℝ)) := by
    intro x hx
    have h1 : 1 ≤ u / x := by rw [le_div_iff₀ hx.1]; linarith [hx.2]
    rw [min_eq_left h1, mul_one]
  have hg2 : ∀ x ∈ Ioi u, x ^ (-(1 / 2 : ℝ)) * min 1 (u / x) = u * x ^ (-(3 / 2 : ℝ)) := by
    intro x hx
    have hx0 : 0 < x := lt_trans hu hx
    have h1 : u / x ≤ 1 := by rw [div_le_one hx0]; exact le_of_lt hx
    rw [min_eq_right h1]
    have e : x ^ (-(3 / 2 : ℝ)) = x ^ (-(1 / 2 : ℝ)) * x⁻¹ := by
      rw [show (-(3 / 2 : ℝ)) = -(1 / 2) + -1 by norm_num, rpow_add hx0, rpow_neg_one]
    rw [e]
    field_simp
  have hint1 : IntegrableOn (fun x : ℝ => x ^ (-(1 / 2 : ℝ)) * min 1 (u / x)) (Ioc 0 u) := by
    have h := (intervalIntegrable_iff_integrableOn_Ioc_of_le hu.le).mp
      (intervalIntegral.intervalIntegrable_rpow' (a := 0) (b := u) (by norm_num : (-1 : ℝ) < -(1 / 2)))
    exact IntegrableOn.congr_fun h (fun x hx => (hg1 x hx).symm) measurableSet_Ioc
  have hint2 : IntegrableOn (fun x : ℝ => x ^ (-(1 / 2 : ℝ)) * min 1 (u / x)) (Ioi u) :=
    IntegrableOn.congr_fun (Integrable.const_mul
      (integrableOn_Ioi_rpow_of_lt (by norm_num : -(3 / 2 : ℝ) < -1) hu) u)
      (fun x hx => (hg2 x hx).symm) measurableSet_Ioi
  rw [← Ioc_union_Ioi_eq_Ioi hu.le, setIntegral_union Ioc_disjoint_Ioi_same measurableSet_Ioi hint1 hint2,
    setIntegral_congr_fun measurableSet_Ioc hg1, setIntegral_congr_fun measurableSet_Ioi hg2,
    ← intervalIntegral.integral_of_le hu.le,
    integral_rpow (Or.inl (by norm_num : (-1 : ℝ) < -(1 / 2))), integral_const_mul,
    integral_Ioi_rpow_of_lt (by norm_num : -(3 / 2 : ℝ) < -1) hu,
    zero_rpow (by norm_num : (-(1 / 2 : ℝ) + 1) ≠ 0)]
  have h1 : u ^ (-(1 / 2 : ℝ) + 1) = √u := by
    rw [show (-(1 / 2 : ℝ) + 1) = 1 / 2 by norm_num, sqrt_eq_rpow]
  have h2 : u * u ^ (-(3 / 2 : ℝ) + 1) = √u := by
    rw [show (-(3 / 2 : ℝ) + 1) = -(1 / 2) by norm_num, rpow_neg hu.le, ← sqrt_eq_rpow]
    have hs : 0 < √u := sqrt_pos.mpr hu
    field_simp
    rw [sq_sqrt hu.le]
  have e : u * (-u ^ (-(3 / 2 : ℝ) + 1) / (-(3 / 2 : ℝ) + 1)) = 2 * (u * u ^ (-(3 / 2 : ℝ) + 1)) := by
    ring
  rw [e, h1, h2]
  ring

/-- Lemma 2.3's constant: `8√u/√(2π) = 8√(u/(2π))`. -/
theorem halfmoment_envelope_constant (u : ℝ) (hu : 0 ≤ u) :
    8 * √u / √(2 * π) = 8 * √(u / (2 * π)) := by
  rw [sqrt_div hu, mul_div_assoc]

end QformFiveB
