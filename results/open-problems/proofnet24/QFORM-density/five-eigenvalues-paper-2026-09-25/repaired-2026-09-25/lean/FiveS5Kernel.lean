import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.MeasureTheory.Function.JacobianOneDim
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.MeasureTheory.Measure.Typeclasses.NoAtoms
import Mathlib.Analysis.SpecialFunctions.Pow.NNReal
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.SpecialFunctions.Trigonometric.InverseDeriv
import Mathlib.Tactic

/-!
The bound (5.4) of Lemma 5.5 of "Quadratic forms with five large singular values have bounded densities" (repaired
text, sha256 90f859b7): `J(d) = ∫_{-1}^{1} |x|^{-1/2} |x - d|^{-1/2} dx`, taken in `[0, ∞]`, satisfies
`J(d) ≤ π + 4 log 2 + 2 log₊(1/|d|)` for `d ≠ 0`.

`J(-d) = J(d)` by the substitution `x ↦ -x` (`J_neg`). For `0 < d ≤ 1` the interval is split at `0` and `d`, and on
the three open pieces the integrand has the antiderivatives `-2 log(√(-x) + √(d - x))`, `2 arcsin √(x/d)` and
`2 log(√x + √(x - d))` (`deriv_log_branch_neg`, `deriv_arcsin_branch`, `deriv_log_branch_minus`), each continuous on the
closed piece, so the fundamental theorem of calculus for a nonnegative derivative (`lintegral_Ioo_deriv`) evaluates
them: `J(d) ≤ π + 2 log((1 + √(1 + d))(1 + √(1 - d))) + 2 log(1/d)`, and the product is at most `4`
(`J_product_le`). For `d > 1`, `|x - d| ≥ |x - 1|` on `[-1, 1]`, so `J(d) ≤ J(1)` (`J_le_J_one`). Together:
`lemma55_J`, with `log₊ t = max 0 (log t)`.
-/

open MeasureTheory Set Real
open scoped ENNReal

namespace QformFiveB

namespace Kernel

/-- `J(d) = ∫_{-1}^{1} |x|^{-1/2} |x - d|^{-1/2} dx` in `[0, ∞]` (`|0|^{-1/2} = ∞`). -/
noncomputable def J (d : ℝ) : ℝ≥0∞ :=
  ∫⁻ x in Icc (-1 : ℝ) 1, (ENNReal.ofReal |x|) ^ (-(1 / 2 : ℝ)) * (ENNReal.ofReal |x - d|) ^ (-(1 / 2 : ℝ))

/-- `s^{-1/2} t^{-1/2} = 1/(√s √t)` for `s, t > 0`. -/
theorem ennrpow_half_mul (s t : ℝ) (hs : 0 < s) (ht : 0 < t) :
    (ENNReal.ofReal s) ^ (-(1 / 2 : ℝ)) * (ENNReal.ofReal t) ^ (-(1 / 2 : ℝ))
      = ENNReal.ofReal (1 / (√s * √t)) := by
  rw [ENNReal.ofReal_rpow_of_pos hs, ENNReal.ofReal_rpow_of_pos ht,
    ← ENNReal.ofReal_mul (Real.rpow_nonneg hs.le _)]
  congr 1
  rw [Real.rpow_neg hs.le, Real.rpow_neg ht.le, ← Real.sqrt_eq_rpow, ← Real.sqrt_eq_rpow, one_div, mul_inv]

/-- The fundamental theorem of calculus in `[0, ∞]`: if `F` is continuous on `[a, b]` with derivative `F' ≥ 0` on
`(a, b)`, then `∫_{(a,b)} F' = F b - F a`. -/
theorem lintegral_Ioo_deriv (F F' : ℝ → ℝ) (a b : ℝ) (hab : a ≤ b) (hcont : ContinuousOn F (Icc a b))
    (hderiv : ∀ x ∈ Ioo a b, HasDerivAt F (F' x) x) (hpos : ∀ x ∈ Ioo a b, 0 ≤ F' x) :
    ∫⁻ x in Ioo a b, ENNReal.ofReal (F' x) = ENNReal.ofReal (F b - F a) := by
  have hint : IntegrableOn F' (Ioc a b) := intervalIntegral.integrableOn_deriv_of_nonneg hcont hderiv hpos
  rw [← ofReal_integral_eq_lintegral_ofReal (hint.mono_set Ioo_subset_Ioc_self)
      (ae_restrict_of_forall_mem measurableSet_Ioo hpos),
    ← integral_Ioc_eq_integral_Ioo, ← intervalIntegral.integral_of_le hab,
    intervalIntegral.integral_eq_sub_of_hasDerivAt_of_le hab hcont hderiv
      ((intervalIntegrable_iff_integrableOn_Ioc_of_le hab).2 hint)]

/-- On `x < 0`: `d/dx [-2 log(√(-x) + √(d - x))] = 1/(√(-x) √(d - x))`. -/
theorem deriv_log_branch_neg (d x : ℝ) (hd : 0 < d) (hx : x < 0) :
    HasDerivAt (fun x => -(2 * log (√(-x) + √(d - x)))) (1 / (√(-x) * √(d - x))) x := by
  have hx' : 0 < -x := neg_pos.2 hx
  have hdx : 0 < d - x := by linarith
  have h1 : HasDerivAt (fun x => √(-x)) (-(1 / (2 * √(-x)))) x := by
    have := (Real.hasDerivAt_sqrt hx'.ne').comp x (hasDerivAt_neg x)
    simpa using this
  have h2 : HasDerivAt (fun x => √(d - x)) (-(1 / (2 * √(d - x)))) x := by
    have := (Real.hasDerivAt_sqrt hdx.ne').comp x ((hasDerivAt_id x).const_sub d)
    simpa using this
  have hs1 : 0 < √(-x) := Real.sqrt_pos.mpr hx'
  have hs2 : 0 < √(d - x) := Real.sqrt_pos.mpr hdx
  have hsum : 0 < √(-x) + √(d - x) := by positivity
  have h3 := (((h1.add h2).log hsum.ne').const_mul 2).neg
  simp only [Pi.add_apply] at h3
  convert h3 using 1
  field_simp
  ring

/-- On `0 < x < d`: `d/dx [2 arcsin √(x/d)] = 1/(√x √(d - x))`. -/
theorem deriv_arcsin_branch (d x : ℝ) (hx : 0 < x) (hxd : x < d) :
    HasDerivAt (fun x => 2 * arcsin (√(x / d))) (1 / (√x * √(d - x))) x := by
  have hd : 0 < d := by linarith
  have hq : 0 < x / d := div_pos hx hd
  have hq1 : x / d < 1 := (div_lt_one hd).mpr hxd
  have hs : 0 < √(x / d) := Real.sqrt_pos.mpr hq
  have hs1 : √(x / d) < 1 := by
    rw [show (1 : ℝ) = √1 by simp]; exact Real.sqrt_lt_sqrt hq.le hq1
  have h1 : HasDerivAt (fun x => √(x / d)) (1 / d / (2 * √(x / d))) x := by
    have := (Real.hasDerivAt_sqrt hq.ne').comp x ((hasDerivAt_id x).div_const d)
    simpa [div_eq_mul_inv, mul_comm] using this
  have h2 := ((Real.hasDerivAt_arcsin (by linarith) hs1.ne).comp x h1).const_mul 2
  convert h2 using 1
  have hsq : √(x / d) ^ 2 = x / d := Real.sq_sqrt hq.le
  have hx' : 0 < √x := Real.sqrt_pos.mpr hx
  have hdx : 0 < d - x := by linarith
  have hdx' : 0 < √(d - x) := Real.sqrt_pos.mpr hdx
  have e1 : √(1 - √(x / d) ^ 2) = √(d - x) / √d := by
    rw [hsq, show 1 - x / d = (d - x) / d by field_simp, Real.sqrt_div hdx.le]
  have e2 : √(x / d) = √x / √d := Real.sqrt_div hx.le d
  have hsd : 0 < √d := Real.sqrt_pos.mpr hd
  have hd2 : √d * √d = d := Real.mul_self_sqrt hd.le
  rw [e1, e2]
  field_simp
  rw [Real.sq_sqrt hd.le]

/-- On `x > d > 0`: `d/dx [2 log(√x + √(x - d))] = 1/(√x √(x - d))`. -/
theorem deriv_log_branch_minus (d x : ℝ) (hd : 0 < d) (hx : d < x) :
    HasDerivAt (fun x => 2 * log (√x + √(x - d))) (1 / (√x * √(x - d))) x := by
  have hx0 : 0 < x := by linarith
  have hxd : 0 < x - d := by linarith
  have h1 : HasDerivAt (fun x => √x) (1 / (2 * √x)) x := Real.hasDerivAt_sqrt hx0.ne'
  have h2 : HasDerivAt (fun x => √(x - d)) (1 / (2 * √(x - d))) x := by
    have := (Real.hasDerivAt_sqrt hxd.ne').comp x ((hasDerivAt_id x).sub_const d)
    simpa using this
  have hs1 : 0 < √x := Real.sqrt_pos.mpr hx0
  have hs2 : 0 < √(x - d) := Real.sqrt_pos.mpr hxd
  have hsum : 0 < √x + √(x - d) := by positivity
  have h3 := ((h1.add h2).log hsum.ne').const_mul 2
  simp only [Pi.add_apply] at h3
  convert h3 using 1
  field_simp
  ring

/-- `(1 + √(1 + d))(1 + √(1 - d)) ≤ 4` for `0 ≤ d ≤ 1`. -/
theorem J_product_le (d : ℝ) (h0 : 0 ≤ d) (h1 : d ≤ 1) : (1 + √(1 + d)) * (1 + √(1 - d)) ≤ 4 := by
  set a := √(1 + d) with ha
  set b := √(1 - d) with hb
  have ha0 : 0 ≤ a := Real.sqrt_nonneg _
  have hb0 : 0 ≤ b := Real.sqrt_nonneg _
  have ha2 : a ^ 2 = 1 + d := Real.sq_sqrt (by linarith)
  have hb2 : b ^ 2 = 1 - d := Real.sq_sqrt (by linarith)
  have hab : a * b ≤ 1 := by nlinarith [sq_nonneg (a - b)]
  have hsum : a + b ≤ 2 := by nlinarith [sq_nonneg (a - b), sq_nonneg (a + b)]
  nlinarith

/-- `J(-d) = J(d)`, by the substitution `x ↦ -x`. -/
theorem J_neg (d : ℝ) : J (-d) = J d := by
  unfold J
  have himg : Neg.neg '' Icc (-1 : ℝ) 1 = Icc (-1) 1 := by
    rw [image_neg_Icc, neg_neg]
  have h := lintegral_image_eq_lintegral_abs_deriv_mul (s := Icc (-1 : ℝ) 1) (f := Neg.neg) (f' := fun _ => -1)
    measurableSet_Icc (fun x _ => (hasDerivAt_neg x).hasDerivWithinAt) neg_injective.injOn
    (fun x => (ENNReal.ofReal |x|) ^ (-(1 / 2 : ℝ)) * (ENNReal.ofReal |x - -d|) ^ (-(1 / 2 : ℝ)))
  rw [himg] at h
  rw [h]
  apply lintegral_congr
  intro x
  have e1 : |-x| = |x| := abs_neg x
  have e2 : |-x - -d| = |x - d| := by rw [show -x - -d = -(x - d) by ring, abs_neg]
  simp only [abs_neg, abs_one, ENNReal.ofReal_one, one_mul, e2]

/-- For `d > 1`, `J(d) ≤ J(1)`, since `|x - d| ≥ |x - 1|` on `[-1, 1]`. -/
theorem J_le_J_one (d : ℝ) (hd : 1 < d) : J d ≤ J 1 := by
  unfold J
  refine setLIntegral_mono' measurableSet_Icc (fun x hx => ?_)
  refine mul_le_mul_left' ?_ _
  have hc : |x - 1| ≤ |x - d| := by
    rw [abs_of_nonpos (by linarith [hx.2]), abs_of_neg (by linarith [hx.2])]
    linarith
  rw [ENNReal.rpow_neg, ENNReal.rpow_neg]
  exact ENNReal.inv_le_inv.2 (ENNReal.rpow_le_rpow (ENNReal.ofReal_le_ofReal hc) (by norm_num))

/-- For `0 < d ≤ 1`: `J(d) ≤ π + 4 log 2 + 2 log(1/d)`. -/
theorem J_le_of_pos (d : ℝ) (hd0 : 0 < d) (hd1 : d ≤ 1) :
    J d ≤ ENNReal.ofReal (π + 4 * log 2 + 2 * log (1 / d)) := by
  set K : ℝ → ℝ≥0∞ := fun x => (ENNReal.ofReal |x|) ^ (-(1 / 2 : ℝ)) * (ENNReal.ofReal |x - d|) ^ (-(1 / 2 : ℝ))
    with hK
  have hsub : Icc (-1 : ℝ) 1 ⊆ Icc (-1) 0 ∪ Icc 0 d ∪ Icc d 1 := by
    intro x hx
    rcases le_or_gt x 0 with h0 | h0
    · exact Or.inl (Or.inl ⟨hx.1, h0⟩)
    · rcases le_or_gt x d with h1 | h1
      · exact Or.inl (Or.inr ⟨h0.le, h1⟩)
      · exact Or.inr ⟨h1.le, hx.2⟩
  have hcont1 : ContinuousOn (fun x => -(2 * log (√(-x) + √(d - x)))) (Icc (-1 : ℝ) 0) := by
    have hc : Continuous (fun x : ℝ => √(-x) + √(d - x)) :=
      (Real.continuous_sqrt.comp continuous_neg).add (Real.continuous_sqrt.comp (continuous_const.sub continuous_id))
    refine (continuousOn_const.mul (hc.continuousOn.log (fun x hx => ?_))).neg
    have h1 : 0 < √(d - x) := Real.sqrt_pos.2 (by linarith [hx.2])
    have h2 : 0 ≤ √(-x) := Real.sqrt_nonneg _
    exact (by linarith : (0 : ℝ) < √(-x) + √(d - x)).ne'
  have hcont2 : ContinuousOn (fun x => 2 * arcsin (√(x / d))) (Icc 0 d) :=
    (continuous_const.mul (Real.continuous_arcsin.comp (Real.continuous_sqrt.comp (continuous_id.div_const d)))).continuousOn
  have hcont3 : ContinuousOn (fun x => 2 * log (√x + √(x - d))) (Icc d 1) := by
    have hc : Continuous (fun x : ℝ => √x + √(x - d)) :=
      Real.continuous_sqrt.add (Real.continuous_sqrt.comp (continuous_id.sub continuous_const))
    refine continuousOn_const.mul (hc.continuousOn.log (fun x hx => ?_))
    have h1 : 0 < √x := Real.sqrt_pos.2 (by linarith [hx.1])
    have h2 : 0 ≤ √(x - d) := Real.sqrt_nonneg _
    exact (by linarith : (0 : ℝ) < √x + √(x - d)).ne'
  have e1 : ∫⁻ x in Icc (-1 : ℝ) 0, K x = ENNReal.ofReal (2 * log (1 + √(1 + d)) - 2 * log √d) := by
    rw [← setLIntegral_congr Ioo_ae_eq_Icc]
    have heq : ∀ x ∈ Ioo (-1 : ℝ) 0, K x = ENNReal.ofReal (1 / (√(-x) * √(d - x))) := by
      intro x hx
      simp only [hK]
      rw [abs_of_neg hx.2, abs_of_neg (by linarith [hx.2] : x - d < 0), neg_sub]
      exact ennrpow_half_mul (-x) (d - x) (by linarith [hx.2]) (by linarith [hx.2])
    rw [setLIntegral_congr_fun measurableSet_Ioo heq,
      lintegral_Ioo_deriv (fun x => -(2 * log (√(-x) + √(d - x)))) (fun x => 1 / (√(-x) * √(d - x))) (-1) 0
        (by norm_num) hcont1 (fun x hx => deriv_log_branch_neg d x hd0 hx.2) (fun x _ => by positivity)]
    congr 1
    show -(2 * log (√(-0) + √(d - 0))) - -(2 * log (√(-(-1)) + √(d - -1)))
      = 2 * log (1 + √(1 + d)) - 2 * log √d
    rw [neg_zero, Real.sqrt_zero, zero_add, sub_zero, neg_neg, Real.sqrt_one, show d - -1 = 1 + d by ring]
    ring
  have e2 : ∫⁻ x in Icc (0 : ℝ) d, K x = ENNReal.ofReal π := by
    rw [← setLIntegral_congr Ioo_ae_eq_Icc]
    have heq : ∀ x ∈ Ioo (0 : ℝ) d, K x = ENNReal.ofReal (1 / (√x * √(d - x))) := by
      intro x hx
      simp only [hK]
      rw [abs_of_pos hx.1, abs_of_neg (by linarith [hx.2] : x - d < 0), neg_sub]
      exact ennrpow_half_mul x (d - x) hx.1 (by linarith [hx.2])
    rw [setLIntegral_congr_fun measurableSet_Ioo heq,
      lintegral_Ioo_deriv (fun x => 2 * arcsin (√(x / d))) (fun x => 1 / (√x * √(d - x))) 0 d hd0.le
        hcont2 (fun x hx => deriv_arcsin_branch d x hx.1 hx.2) (fun x _ => by positivity)]
    congr 1
    show 2 * arcsin (√(d / d)) - 2 * arcsin (√(0 / d)) = π
    rw [div_self hd0.ne', zero_div, Real.sqrt_one, Real.sqrt_zero, Real.arcsin_one, Real.arcsin_zero]
    ring
  have e3 : ∫⁻ x in Icc d 1, K x = ENNReal.ofReal (2 * log (1 + √(1 - d)) - 2 * log √d) := by
    rw [← setLIntegral_congr Ioo_ae_eq_Icc]
    have heq : ∀ x ∈ Ioo d 1, K x = ENNReal.ofReal (1 / (√x * √(x - d))) := by
      intro x hx
      simp only [hK]
      rw [abs_of_pos (by linarith [hx.1] : 0 < x), abs_of_pos (by linarith [hx.1] : 0 < x - d)]
      exact ennrpow_half_mul x (x - d) (by linarith [hx.1]) (by linarith [hx.1])
    rw [setLIntegral_congr_fun measurableSet_Ioo heq,
      lintegral_Ioo_deriv (fun x => 2 * log (√x + √(x - d))) (fun x => 1 / (√x * √(x - d))) d 1 hd1
        hcont3 (fun x hx => deriv_log_branch_minus d x hd0 hx.1) (fun x _ => by positivity)]
    congr 1
    show 2 * log (√1 + √(1 - d)) - 2 * log (√d + √(d - d)) = 2 * log (1 + √(1 - d)) - 2 * log √d
    rw [Real.sqrt_one, sub_self, Real.sqrt_zero, add_zero]
  -- the real inequality
  have hsd0 : 0 < √d := Real.sqrt_pos.2 hd0
  have hsd1 : √d ≤ 1 := by
    rw [show (1 : ℝ) = √1 by simp]
    exact Real.sqrt_le_sqrt hd1
  have hA : 0 < 1 + √(1 + d) := by positivity
  have hB : 0 < 1 + √(1 - d) := by positivity
  have hl1 : log √d ≤ log (1 + √(1 + d)) := Real.log_le_log hsd0 (by linarith [Real.sqrt_nonneg (1 + d)])
  have hl3 : log √d ≤ log (1 + √(1 - d)) := Real.log_le_log hsd0 (by linarith [Real.sqrt_nonneg (1 - d)])
  have hprod : log (1 + √(1 + d)) + log (1 + √(1 - d)) ≤ 2 * log 2 := by
    rw [← Real.log_mul hA.ne' hB.ne', show 2 * log (2 : ℝ) = log 4 by
      rw [show (4 : ℝ) = 2 ^ 2 by norm_num, Real.log_pow]; norm_num]
    exact Real.log_le_log (mul_pos hA hB) (J_product_le d hd0.le hd1)
  have hsqrtlog : log √d = log d / 2 := Real.log_sqrt hd0.le
  have hinv : log (1 / d) = -log d := by rw [one_div, Real.log_inv]
  calc J d = ∫⁻ x in Icc (-1 : ℝ) 1, K x := rfl
    _ ≤ ∫⁻ x in Icc (-1) 0 ∪ Icc 0 d ∪ Icc d 1, K x := lintegral_mono_set hsub
    _ ≤ (∫⁻ x in Icc (-1) 0 ∪ Icc 0 d, K x) + ∫⁻ x in Icc d 1, K x := lintegral_union_le _ _ _
    _ ≤ ((∫⁻ x in Icc (-1 : ℝ) 0, K x) + ∫⁻ x in Icc 0 d, K x) + ∫⁻ x in Icc d 1, K x := by
        gcongr
        exact lintegral_union_le _ _ _
    _ = ENNReal.ofReal (2 * log (1 + √(1 + d)) - 2 * log √d) + ENNReal.ofReal π
          + ENNReal.ofReal (2 * log (1 + √(1 - d)) - 2 * log √d) := by rw [e1, e2, e3]
    _ = ENNReal.ofReal ((2 * log (1 + √(1 + d)) - 2 * log √d) + π
          + (2 * log (1 + √(1 - d)) - 2 * log √d)) := by
        have hA' : 0 ≤ 2 * log (1 + √(1 + d)) - 2 * log √d := by linarith
        have hC' : 0 ≤ 2 * log (1 + √(1 - d)) - 2 * log √d := by linarith
        rw [ENNReal.ofReal_add (add_nonneg hA' Real.pi_pos.le) hC', ENNReal.ofReal_add hA' Real.pi_pos.le]
    _ ≤ ENNReal.ofReal (π + 4 * log 2 + 2 * log (1 / d)) := by
        apply ENNReal.ofReal_le_ofReal
        rw [hinv]
        linarith

/-- **Lemma 5.5, (5.4).** For `d ≠ 0`, `J(d) ≤ π + 4 log 2 + 2 log₊(1/|d|)`, with `log₊ t = max 0 (log t)`. -/
theorem lemma55_J (d : ℝ) (hd : d ≠ 0) :
    J d ≤ ENNReal.ofReal (π + 4 * log 2 + 2 * max 0 (log (1 / |d|))) := by
  have key : ∀ e : ℝ, 0 < e → J e ≤ ENNReal.ofReal (π + 4 * log 2 + 2 * max 0 (log (1 / e))) := by
    intro e he
    rcases le_or_gt e 1 with h1 | h1
    · have hlog : 0 ≤ log (1 / e) := by
        apply Real.log_nonneg
        rw [le_div_iff₀ he]
        linarith
      rw [max_eq_right hlog]
      exact J_le_of_pos e he h1
    · have hlog : log (1 / e) ≤ 0 := by
        apply Real.log_nonpos (by positivity)
        rw [div_le_iff₀ he]
        linarith
      rw [max_eq_left hlog]
      calc J e ≤ J 1 := J_le_J_one e h1
        _ ≤ ENNReal.ofReal (π + 4 * log 2 + 2 * log (1 / 1)) := J_le_of_pos 1 one_pos le_rfl
        _ = ENNReal.ofReal (π + 4 * log 2 + 2 * 0) := by norm_num
  rcases lt_or_gt_of_ne hd with hneg | hpos
  · have e : J d = J (-d) := by rw [← J_neg (-d), neg_neg]
    rw [e, abs_of_neg hneg]
    exact key (-d) (neg_pos.2 hneg)
  · rw [abs_of_pos hpos]
    exact key d hpos

end Kernel

end QformFiveB
