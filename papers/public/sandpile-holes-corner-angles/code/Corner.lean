import Mathlib

/-!
The elementary steps of the corner lemma (Lemma 4.2) and of the vertex count (Corollary 1.2) of the paper.

Corner lemma. Polar coordinates are centred at the corner, with the sector `|θ| ≤ α/2`. The projection of the
Laplacian on `cos 2θ` is bounded below by integrating `cos 2θ` over the three pieces `[-α/2, -π/4]`,
`[-π/4, π/4]`, `[π/4, α/2]` (`integral_cos_two_*`): for an obtuse sector it is at least `a - b (1 - sin α)` when
the density lies between `a` and `b` (`projection_lower_bound`), and for `α ≤ π/2` it is at least `a sin α`
(`projection_lower_bound_acute`). The radial equation for `F = r² f` takes the divergence form
`(r⁵ f')' = r³ G` (`radial_substitution`, `radial_divergence_form`). A lower bound `κ/(4t)` for `f'` integrates
to `(κ/4) log(r₀/r)` (`log_growth`), which is unbounded as `r → 0` (`log_unbounded`). The mean-value
inequality gives `M(r) ≤ b r²/4` for the circle means (`circle_mean_integral`). With `a = k - 1` and `b = k`,
`k = H + 3`, the inequality `a ≤ b (1 - sin α)` says `sin α ≤ 1/k` (`corner_condition`).

Vertex count. For `k ≥ 2`, `k sin(π/(2k)) > 1` (`jordan`), so `arcsin(1/k) < π/(2k)` (`arcsin_inv_lt`), and the
interior angle `π - π/(2k)` of a regular `4k`-gon has sine larger than `1/k` (`regular_polygon_angle`,
`regular_polygon_sine`). At an obtuse vertex with `sin α ≤ 1/k` the exterior angle is at most `arcsin(1/k)`
(`exterior_angle_le`); exterior angles summing to `2π` then force more than `4k` of them
(`more_than_four_k_vertices`), hence at least `4k + 4` when their number is a multiple of four
(`multiple_of_four`). For `H = -1` the bound is `12`, with equality only for twelve angles `5π/6`
(`arcsin_half`, `twelve_vertices`, `twelve_vertices_eq`); for `H = 0` it is `19`, hence `20`
(`sin_pi_div_nine_gt`, `arcsin_third_lt`, `nineteen_vertices`, `twenty_vertices`). The weighted last-firing
inequality uses `min x y = (x + y - |x - y|)/2` (`min_eq_half`).
-/

open Real MeasureTheory

namespace SandpileCorners

/-! ### The integrals of `cos 2θ` -/

theorem integral_cos_two (a b : ℝ) :
    ∫ θ in a..b, cos (2 * θ) = (sin (2 * b) - sin (2 * a)) / 2 := by
  rw [intervalIntegral.integral_comp_mul_left Real.cos (two_ne_zero), integral_cos, smul_eq_mul]
  ring

theorem integral_cos_two_quarter : ∫ θ in (-(π / 4))..(π / 4), cos (2 * θ) = 1 := by
  rw [integral_cos_two]
  have h1 : 2 * (π / 4) = π / 2 := by ring
  have h2 : 2 * (-(π / 4)) = -(π / 2) := by ring
  rw [h1, h2, sin_neg, sin_pi_div_two]
  norm_num

theorem integral_cos_two_right (α : ℝ) :
    ∫ θ in (π / 4)..(α / 2), cos (2 * θ) = (sin α - 1) / 2 := by
  rw [integral_cos_two]
  have h1 : 2 * (α / 2) = α := by ring
  have h2 : 2 * (π / 4) = π / 2 := by ring
  rw [h1, h2, sin_pi_div_two]

theorem integral_cos_two_left (α : ℝ) :
    ∫ θ in (-(α / 2))..(-(π / 4)), cos (2 * θ) = (sin α - 1) / 2 := by
  rw [integral_cos_two]
  have h1 : 2 * (-(α / 2)) = -α := by ring
  have h2 : 2 * (-(π / 4)) = -(π / 2) := by ring
  rw [h1, h2, sin_neg, sin_neg, sin_pi_div_two]
  ring

theorem integral_cos_two_sector (α : ℝ) : ∫ θ in (-(α / 2))..(α / 2), cos (2 * θ) = sin α := by
  rw [integral_cos_two]
  have h1 : 2 * (α / 2) = α := by ring
  have h2 : 2 * (-(α / 2)) = -α := by ring
  rw [h1, h2, sin_neg]
  ring

/-! ### The projection of the density on `cos 2θ` -/

/-- An obtuse sector: the density is at least `a` where `|θ| ≤ π/4` and at most `b` on the whole sector. -/
theorem projection_lower_bound {a b α : ℝ} {g : ℝ → ℝ} (hα1 : π / 2 ≤ α) (hα2 : α ≤ π)
    (hg : IntervalIntegrable g volume (-(α / 2)) (α / 2))
    (ha : ∀ θ ∈ Set.Icc (-(π / 4)) (π / 4), a ≤ g θ)
    (hb : ∀ θ ∈ Set.Icc (-(α / 2)) (α / 2), g θ ≤ b) :
    a - b * (1 - sin α) ≤ ∫ θ in (-(α / 2))..(α / 2), g θ * cos (2 * θ) := by
  have hpi : 0 < π := pi_pos
  have o1 : -(α / 2) ≤ -(π / 4) := by linarith
  have o2 : -(π / 4) ≤ π / 4 := by linarith
  have o3 : π / 4 ≤ α / 2 := by linarith
  have o4 : -(α / 2) ≤ α / 2 := by linarith
  have hcos : Continuous fun θ : ℝ => cos (2 * θ) := by fun_prop
  have hI : IntervalIntegrable (fun θ => g θ * cos (2 * θ)) volume (-(α / 2)) (α / 2) :=
    hg.mul_continuousOn hcos.continuousOn
  have sub1 : Set.uIcc (-(α / 2)) (-(π / 4)) ⊆ Set.uIcc (-(α / 2)) (α / 2) := by
    rw [Set.uIcc_of_le o1, Set.uIcc_of_le o4]
    exact Set.Icc_subset_Icc le_rfl (by linarith)
  have sub2 : Set.uIcc (-(π / 4)) (π / 4) ⊆ Set.uIcc (-(α / 2)) (α / 2) := by
    rw [Set.uIcc_of_le o2, Set.uIcc_of_le o4]
    exact Set.Icc_subset_Icc o1 o3
  have sub3 : Set.uIcc (π / 4) (α / 2) ⊆ Set.uIcc (-(α / 2)) (α / 2) := by
    rw [Set.uIcc_of_le o3, Set.uIcc_of_le o4]
    exact Set.Icc_subset_Icc (by linarith) le_rfl
  have i1 := hI.mono_set sub1
  have i2 := hI.mono_set sub2
  have i3 := hI.mono_set sub3
  have hc : ∀ (c x y : ℝ), IntervalIntegrable (fun θ => c * cos (2 * θ)) volume x y :=
    fun c x y => (continuous_const.mul hcos).intervalIntegrable x y
  have split : ∫ θ in (-(α / 2))..(α / 2), g θ * cos (2 * θ)
      = (∫ θ in (-(α / 2))..(-(π / 4)), g θ * cos (2 * θ))
        + (∫ θ in (-(π / 4))..(π / 4), g θ * cos (2 * θ))
        + (∫ θ in (π / 4)..(α / 2), g θ * cos (2 * θ)) := by
    rw [intervalIntegral.integral_add_adjacent_intervals i1 i2,
      intervalIntegral.integral_add_adjacent_intervals (i1.trans i2) i3]
  have left : b * ((sin α - 1) / 2) ≤ ∫ θ in (-(α / 2))..(-(π / 4)), g θ * cos (2 * θ) := by
    rw [← integral_cos_two_left, ← intervalIntegral.integral_const_mul]
    apply intervalIntegral.integral_mono_on o1 (hc b _ _) i1
    intro θ hθ
    have hneg : cos (2 * θ) ≤ 0 := by
      rw [← cos_neg]
      exact cos_nonpos_of_pi_div_two_le_of_le (by linarith [hθ.2]) (by linarith [hθ.1])
    exact mul_le_mul_of_nonpos_right (hb θ ⟨hθ.1, by linarith [hθ.2]⟩) hneg
  have mid : a * 1 ≤ ∫ θ in (-(π / 4))..(π / 4), g θ * cos (2 * θ) := by
    rw [← integral_cos_two_quarter, ← intervalIntegral.integral_const_mul]
    apply intervalIntegral.integral_mono_on o2 (hc a _ _) i2
    intro θ hθ
    have hnn : 0 ≤ cos (2 * θ) :=
      cos_nonneg_of_neg_pi_div_two_le_of_le (by linarith [hθ.1]) (by linarith [hθ.2])
    exact mul_le_mul_of_nonneg_right (ha θ hθ) hnn
  have right : b * ((sin α - 1) / 2) ≤ ∫ θ in (π / 4)..(α / 2), g θ * cos (2 * θ) := by
    rw [← integral_cos_two_right, ← intervalIntegral.integral_const_mul]
    apply intervalIntegral.integral_mono_on o3 (hc b _ _) i3
    intro θ hθ
    have hneg : cos (2 * θ) ≤ 0 :=
      cos_nonpos_of_pi_div_two_le_of_le (by linarith [hθ.1]) (by linarith [hθ.2])
    exact mul_le_mul_of_nonpos_right (hb θ ⟨by linarith [hθ.1], hθ.2⟩) hneg
  rw [split]
  linarith

/-- A sector of opening at most `π/2`: the density is at least `a` on the whole sector. -/
theorem projection_lower_bound_acute {a α : ℝ} {g : ℝ → ℝ} (hα0 : 0 ≤ α) (hα1 : α ≤ π / 2)
    (hg : IntervalIntegrable g volume (-(α / 2)) (α / 2))
    (ha : ∀ θ ∈ Set.Icc (-(α / 2)) (α / 2), a ≤ g θ) :
    a * sin α ≤ ∫ θ in (-(α / 2))..(α / 2), g θ * cos (2 * θ) := by
  have hcos : Continuous fun θ : ℝ => cos (2 * θ) := by fun_prop
  have hle : -(α / 2) ≤ α / 2 := by linarith
  rw [← integral_cos_two_sector, ← intervalIntegral.integral_const_mul]
  apply intervalIntegral.integral_mono_on hle ((continuous_const.mul hcos).intervalIntegrable _ _)
    (hg.mul_continuousOn hcos.continuousOn)
  intro θ hθ
  have hnn : 0 ≤ cos (2 * θ) :=
    cos_nonneg_of_neg_pi_div_two_le_of_le (by linarith [hθ.1]) (by linarith [hθ.2])
  exact mul_le_mul_of_nonneg_right (ha θ hθ) hnn

/-- With `a = k - 1` and `b = k` the corner inequality `a ≤ b (1 - sin α)` is `sin α ≤ 1/k`. -/
theorem corner_condition {k s : ℝ} (hk : 0 < k) : k - 1 ≤ k * (1 - s) ↔ s ≤ 1 / k := by
  rw [le_div_iff₀ hk]
  constructor <;> intro h <;> nlinarith

/-! ### The radial equation -/

/-- `F = r² f`, `F' = 2 r f + r² f'`, `F'' = 2 f + 4 r f' + r² f''`. -/
theorem radial_substitution (r f f₁ f₂ : ℝ) (hr : r ≠ 0) :
    (2 * f + 4 * r * f₁ + r ^ 2 * f₂) + (2 * r * f + r ^ 2 * f₁) / r - 4 * (r ^ 2 * f) / r ^ 2
      = r ^ 2 * f₂ + 5 * r * f₁ := by
  field_simp
  ring

/-- `(r⁵ f')' = 5 r⁴ f' + r⁵ f'' = r³ (r² f'' + 5 r f')`. -/
theorem radial_divergence_form (r f₁ f₂ : ℝ) :
    5 * r ^ 4 * f₁ + r ^ 5 * f₂ = r ^ 3 * (r ^ 2 * f₂ + 5 * r * f₁) := by
  ring

theorem log_growth {κ r r₀ : ℝ} (hr : 0 < r) (hr₀ : 0 < r₀) :
    ∫ t in r..r₀, κ / (4 * t) = κ / 4 * log (r₀ / r) := by
  have h : (fun t : ℝ => κ / (4 * t)) = fun t => κ / 4 * t⁻¹ := by
    funext t
    ring
  rw [h, intervalIntegral.integral_const_mul, integral_inv_of_pos hr hr₀]

theorem log_unbounded {κ r₀ : ℝ} (hκ : 0 < κ) (hr₀ : 0 < r₀) (M : ℝ) :
    ∃ r, 0 < r ∧ r < r₀ ∧ M < κ / 4 * log (r₀ / r) := by
  set y := 4 * (|M| + 1) / κ with hy
  have hy0 : 0 < y := by positivity
  refine ⟨r₀ * exp (-y), by positivity, ?_, ?_⟩
  · have he : exp (-y) < 1 := by
      rw [Real.exp_lt_one_iff]
      linarith
    nlinarith
  · have hq : r₀ / (r₀ * exp (-y)) = exp y := by
      rw [exp_neg]
      field_simp
    rw [hq, log_exp, hy]
    have hval : κ / 4 * (4 * (|M| + 1) / κ) = |M| + 1 := by
      field_simp
    rw [hval]
    linarith [le_abs_self M]

/-! ### The mean-value integrals -/

/-- `M(r) ≤ ∫₀ʳ b t / 2 dt = b r² / 4`. -/
theorem circle_mean_integral (b r : ℝ) : ∫ t in (0 : ℝ)..r, b * t / 2 = b * r ^ 2 / 4 := by
  have h : (fun t : ℝ => b * t / 2) = fun t => b / 2 * t := by
    funext t
    ring
  rw [h, intervalIntegral.integral_const_mul, integral_id]
  ring

/-- The weighted last-firing inequality: `min x y = (x + y - |x - y|) / 2`. -/
theorem min_eq_half (x y : ℝ) : min x y = (x + y - |x - y|) / 2 := by
  rcases le_total x y with h | h
  · rw [min_eq_left h, abs_of_nonpos (sub_nonpos.2 h)]
    ring
  · rw [min_eq_right h, abs_of_nonneg (sub_nonneg.2 h)]
    ring

/-! ### Angles and vertex counts -/

theorem jordan (k : ℕ) (hk : 2 ≤ k) : 1 < (k : ℝ) * sin (π / (2 * k)) := by
  have hk' : (2 : ℝ) ≤ k := by exact_mod_cast hk
  have hkpos : (0 : ℝ) < k := by linarith
  have hpi := pi_pos
  have hx0 : 0 < π / (2 * k) := by positivity
  have hx1 : π / (2 * k) < π / 2 := by
    rw [div_lt_iff₀ (by positivity)]
    nlinarith
  have h := mul_lt_sin hx0 hx1
  have h2 : 2 / π * (π / (2 * k)) = 1 / k := by
    field_simp
  rw [h2, div_lt_iff₀ hkpos] at h
  linarith [mul_comm (sin (π / (2 * k))) (k : ℝ)]

theorem arcsin_inv_lt (k : ℕ) (hk : 2 ≤ k) : arcsin (1 / k) < π / (2 * k) := by
  have hk' : (2 : ℝ) ≤ k := by exact_mod_cast hk
  have hkpos : (0 : ℝ) < k := by linarith
  have hpi := pi_pos
  rw [arcsin_lt_iff_lt_sin]
  · rw [div_lt_iff₀ hkpos]
    linarith [jordan k hk, mul_comm (sin (π / (2 * k))) (k : ℝ)]
  · have h0 : 0 ≤ 1 / (k : ℝ) := by positivity
    exact Set.mem_Icc.2 ⟨by linarith, (div_le_one hkpos).2 (by linarith)⟩
  · have h0 : 0 < π / (2 * k) := by positivity
    have h1 : π / (2 * k) ≤ π / 2 := by
      rw [div_le_iff₀ (by positivity)]
      nlinarith
    exact Set.mem_Icc.2 ⟨by linarith, h1⟩

/-- The interior angle of a regular `4k`-gon is `π - π/(2k)`. -/
theorem regular_polygon_angle (k : ℝ) (hk : k ≠ 0) : (4 * k - 2) * π / (4 * k) = π - π / (2 * k) := by
  field_simp
  ring

/-- Its sine exceeds `1/k`, so it fails the corner condition with `k = H + 3`. -/
theorem regular_polygon_sine (k : ℕ) (hk : 2 ≤ k) : 1 / (k : ℝ) < sin (π - π / (2 * k)) := by
  have hkpos : (0 : ℝ) < k := by
    have : (2 : ℝ) ≤ k := by exact_mod_cast hk
    linarith
  rw [sin_pi_sub, div_lt_iff₀ hkpos]
  linarith [jordan k hk, mul_comm (sin (π / (2 * k))) (k : ℝ)]

theorem exterior_angle_le {k α : ℝ} (hk : 1 ≤ k) (h1 : π / 2 ≤ α) (h2 : α ≤ π) (hs : sin α ≤ 1 / k) :
    π - α ≤ arcsin (1 / k) := by
  have hkpos : 0 < k := by linarith
  rw [le_arcsin_iff_sin_le]
  · rw [sin_pi_sub]
    exact hs
  · exact Set.mem_Icc.2 ⟨by linarith [pi_pos], by linarith⟩
  · have h0 : 0 ≤ 1 / k := by positivity
    exact Set.mem_Icc.2 ⟨by linarith, (div_le_one hkpos).2 hk⟩

theorem sum_le_card_mul {m : ℕ} {β : Fin m → ℝ} {c : ℝ} (hβ : ∀ i, β i ≤ c)
    (hsum : ∑ i, β i = 2 * π) : 2 * π ≤ m * c := by
  have h := Finset.sum_le_sum (fun i (_ : i ∈ (Finset.univ : Finset (Fin m))) => hβ i)
  rw [hsum, Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul] at h
  exact h

theorem more_than_four_k_vertices (k m : ℕ) (hk : 2 ≤ k) (β : Fin m → ℝ)
    (hβ : ∀ i, β i ≤ arcsin (1 / k)) (hsum : ∑ i, β i = 2 * π) : 4 * k < m := by
  have hpi := pi_pos
  have h1 := sum_le_card_mul hβ hsum
  have h2 := arcsin_inv_lt k hk
  have hk' : (2 : ℝ) ≤ k := by exact_mod_cast hk
  rcases Nat.eq_zero_or_pos m with h0 | h0
  · subst h0
    simp at h1
    linarith
  · have hmpos : (0 : ℝ) < m := by exact_mod_cast h0
    have h4 : (m : ℝ) * arcsin (1 / k) < m * (π / (2 * k)) := mul_lt_mul_of_pos_left h2 hmpos
    have h5 : 2 * π * (2 * k) < m * π := by
      have h6 : 2 * π < m * (π / (2 * k)) := lt_of_le_of_lt h1 h4
      rw [mul_div_assoc', lt_div_iff₀ (by positivity)] at h6
      exact h6
    have h7 : (4 * k : ℝ) < m := by nlinarith
    exact_mod_cast h7

theorem multiple_of_four {k m : ℕ} (h : 4 * k < m) (h4 : 4 ∣ m) : 4 * k + 4 ≤ m := by
  omega

theorem arcsin_half : arcsin (1 / 2) = π / 6 := by
  rw [← sin_pi_div_six]
  apply arcsin_sin <;> linarith [pi_pos]

theorem twelve_vertices {m : ℕ} {β : Fin m → ℝ} (hβ : ∀ i, β i ≤ π / 6) (hsum : ∑ i, β i = 2 * π) :
    12 ≤ m := by
  have hpi := pi_pos
  have h1 := sum_le_card_mul hβ hsum
  have h2 : (12 : ℝ) ≤ m := by nlinarith
  exact_mod_cast h2

theorem twelve_vertices_eq {β : Fin 12 → ℝ} (hβ : ∀ i, β i ≤ π / 6) (hsum : ∑ i, β i = 2 * π) :
    ∀ i, β i = π / 6 := by
  have hnn : ∀ i ∈ (Finset.univ : Finset (Fin 12)), 0 ≤ π / 6 - β i := fun i _ => sub_nonneg.2 (hβ i)
  have hzero : ∑ i, (π / 6 - β i) = 0 := by
    rw [Finset.sum_sub_distrib, hsum, Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
    push_cast
    ring
  intro i
  have h := (Finset.sum_eq_zero_iff_of_nonneg hnn).1 hzero i (Finset.mem_univ i)
  linarith

theorem sin_pi_div_nine_gt : 1 / 3 < sin (π / 9) := by
  have h1 := pi_gt_d2
  have h2 := pi_lt_d2
  have hx0 : 0 < π / 9 := by positivity
  have h := sin_gt_sub_cube hx0
  have hxl : 0.3488 < π / 9 := by linarith
  have hxu : π / 9 < 0.35 := by linarith
  have hsq : (π / 9) ^ 2 < 0.35 ^ 2 := by nlinarith
  have hcube : (π / 9) ^ 3 < 0.35 ^ 3 := by nlinarith
  norm_num at hcube ⊢
  nlinarith

theorem arcsin_third_lt : arcsin (1 / 3) < π / 9 := by
  have hpi := pi_pos
  rw [arcsin_lt_iff_lt_sin]
  · exact sin_pi_div_nine_gt
  · exact Set.mem_Icc.2 ⟨by norm_num, by norm_num⟩
  · exact Set.mem_Icc.2 ⟨by linarith, by linarith⟩

theorem nineteen_vertices {m : ℕ} {β : Fin m → ℝ} (hβ : ∀ i, β i ≤ arcsin (1 / 3))
    (hsum : ∑ i, β i = 2 * π) : 18 < m := by
  have hpi := pi_pos
  have h1 := sum_le_card_mul hβ hsum
  have h2 := arcsin_third_lt
  have h3 : 0 < arcsin (1 / 3) := arcsin_pos.2 (by norm_num)
  by_contra hcon
  have hm : (m : ℝ) ≤ 18 := by exact_mod_cast not_lt.1 hcon
  nlinarith

theorem twenty_vertices {m : ℕ} {β : Fin m → ℝ} (hβ : ∀ i, β i ≤ arcsin (1 / 3))
    (hsum : ∑ i, β i = 2 * π) (h4 : 4 ∣ m) : 20 ≤ m := by
  have := nineteen_vertices hβ hsum
  omega

end SandpileCorners

#print axioms SandpileCorners.projection_lower_bound
#print axioms SandpileCorners.projection_lower_bound_acute
#print axioms SandpileCorners.log_unbounded
#print axioms SandpileCorners.more_than_four_k_vertices
#print axioms SandpileCorners.regular_polygon_sine
#print axioms SandpileCorners.twelve_vertices_eq
#print axioms SandpileCorners.twenty_vertices
