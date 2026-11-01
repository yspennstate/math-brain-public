import Mathlib

/-!
The scalar core of the erasure bound (Lemma 2.3 of "The Fourier entropy-influence inequality for monotone DNF
formulas of bounded width"), in natural logarithms. With `Psi r = log (r + 2 sqrt r + 2)` (the paper's function is
`log₂ e + Psi / log 2`, an increasing affine image of this one):

* `ent_le`: `X log (1 + Y / X) ≤ Y` for `X ≥ 0`, `Y > 0`, which gives `E(X, Y) ≤ Y log (e (X + Y) / Y)`;
* `sq_bound`: `(1 + s)^2 + 1 ≤ s^2 + 2 |s| + 2`, which gives `psi(s) ≤ Psi(s^2)` since `sqrt (s^2) = |s|`;
* `Psi_concave`, `Psi_mono`, `Psi_zero_pos`: `Psi` is concave and nondecreasing on `[0, ∞)`, with `Psi 0 > 0`;
* `ratio_anti`: for `g` concave on `[0, ∞)` with `g 0 ≥ 0`, `g z / z` is nonincreasing on `(0, ∞)`;
* `jensen_chain`: for weights `w ≥ 0` with `0 < ∑ w ≤ ε` and `∑ w s^2 ≤ c`,
  `∑ w Psi(s^2) ≤ ε Psi(c / ε)` - the Jensen step of the lemma, with `c = 1 - 2ε`.
-/

open Real Finset

namespace FEIMonoPsi

theorem ent_le {X Y : ℝ} (hX : 0 ≤ X) (hY : 0 < Y) : X * Real.log (1 + Y / X) ≤ Y := by
  rcases hX.eq_or_lt with h | h
  · subst h
    simp only [zero_mul]
    exact hY.le
  · have hpos : (0 : ℝ) < 1 + Y / X := by positivity
    have h1 : Real.log (1 + Y / X) ≤ Y / X := by
      have := Real.log_le_sub_one_of_pos hpos
      linarith
    calc X * Real.log (1 + Y / X) ≤ X * (Y / X) := mul_le_mul_of_nonneg_left h1 h.le
      _ = Y := by field_simp

theorem sq_bound (s : ℝ) : (1 + s) ^ 2 + 1 ≤ s ^ 2 + 2 * |s| + 2 := by
  have h := le_abs_self s
  nlinarith [h]

/-- The function `r ↦ log (r + 2 √r + 2)`. -/
noncomputable def Psi (r : ℝ) : ℝ := Real.log (r + 2 * Real.sqrt r + 2)

theorem inner_pos (r : ℝ) (hr : 0 ≤ r) : 0 < r + 2 * Real.sqrt r + 2 := by
  have := Real.sqrt_nonneg r
  linarith

theorem inner_concave : ConcaveOn ℝ (Set.Ici (0 : ℝ)) (fun r => r + 2 * Real.sqrt r + 2) := by
  refine ⟨convex_Ici 0, ?_⟩
  intro x hx y hy a b ha hb hab
  have hs := Real.strictConcaveOn_sqrt.concaveOn.2 hx hy ha hb hab
  simp only [smul_eq_mul] at hs ⊢
  nlinarith [hs, hab]

theorem Psi_concave : ConcaveOn ℝ (Set.Ici (0 : ℝ)) Psi := by
  refine ⟨convex_Ici 0, ?_⟩
  intro x hx y hy a b ha hb hab
  have hux := inner_pos x hx
  have huy := inner_pos y hy
  have hxy : (0 : ℝ) ≤ a • x + b • y := by
    simp only [smul_eq_mul]
    have hx' : (0 : ℝ) ≤ x := hx
    have hy' : (0 : ℝ) ≤ y := hy
    positivity
  have h1 := strictConcaveOn_log_Ioi.concaveOn.2 (Set.mem_Ioi.mpr hux) (Set.mem_Ioi.mpr huy) ha hb hab
  have h2 := inner_concave.2 hx hy ha hb hab
  have hmid : (0 : ℝ) < a • (x + 2 * Real.sqrt x + 2) + b • (y + 2 * Real.sqrt y + 2) := by
    simp only [smul_eq_mul]
    rcases ha.eq_or_lt with h | h
    · have hb1 : b = 1 := by linarith
      subst hb1
      simp only [← h, zero_mul, zero_add, one_mul]
      exact huy
    · have := mul_pos h hux
      have := mul_nonneg hb huy.le
      linarith
  have h3 : Real.log (a • (x + 2 * Real.sqrt x + 2) + b • (y + 2 * Real.sqrt y + 2))
      ≤ Real.log (a • x + b • y + 2 * Real.sqrt (a • x + b • y) + 2) := Real.log_le_log hmid h2
  unfold Psi
  simp only [smul_eq_mul] at h1 h3 ⊢
  linarith

theorem Psi_mono {x y : ℝ} (hx : 0 ≤ x) (hxy : x ≤ y) : Psi x ≤ Psi y := by
  unfold Psi
  apply Real.log_le_log (inner_pos x hx)
  have := Real.sqrt_le_sqrt hxy
  linarith

theorem Psi_zero_pos : 0 < Psi 0 := by
  unfold Psi
  simp only [Real.sqrt_zero, mul_zero, add_zero, zero_add]
  exact Real.log_pos (by norm_num)

/-- For `g` concave on `[0, ∞)` with `g 0 ≥ 0`, the ratio `g z / z` does not increase. -/
theorem ratio_anti {g : ℝ → ℝ} (hg : ConcaveOn ℝ (Set.Ici (0 : ℝ)) g) (h0 : 0 ≤ g 0) {y z : ℝ}
    (hy : 0 < y) (hyz : y ≤ z) : g z / z ≤ g y / y := by
  have hz : 0 < z := lt_of_lt_of_le hy hyz
  have h1 : 0 ≤ 1 - y / z := by
    have : y / z ≤ 1 := (div_le_one hz).mpr hyz
    linarith
  have h2 : 0 ≤ y / z := div_nonneg hy.le hz.le
  have key := hg.2 (Set.mem_Ici.mpr le_rfl) (Set.mem_Ici.mpr hz.le) h1 h2 (by ring)
  have hpt : (1 - y / z) • (0 : ℝ) + (y / z) • z = y := by
    simp only [smul_eq_mul, mul_zero, zero_add]
    field_simp
  rw [hpt] at key
  simp only [smul_eq_mul] at key
  have h3 : y / z * g z ≤ g y := by nlinarith [mul_nonneg h1 h0]
  have h4 : y * g z ≤ z * g y := by
    have := mul_le_mul_of_nonneg_left h3 hz.le
    have e : z * (y / z * g z) = y * g z := by field_simp
    linarith
  rw [div_le_div_iff₀ hz hy]
  linarith

/-- The Jensen step of the erasure bound. -/
theorem jensen_chain {ι : Type*} (T : Finset ι) (w s : ι → ℝ) (hw : ∀ i ∈ T, 0 ≤ w i)
    {ε c : ℝ} (hW : 0 < ∑ i ∈ T, w i) (hWε : ∑ i ∈ T, w i ≤ ε) (hc : 0 ≤ c)
    (hsec : ∑ i ∈ T, w i * s i ^ 2 ≤ c) :
    ∑ i ∈ T, w i * Psi (s i ^ 2) ≤ ε * Psi (c / ε) := by
  set W := ∑ i ∈ T, w i with hWdef
  have hε : 0 < ε := lt_of_lt_of_le hW hWε
  -- Jensen with the normalised weights w / W
  have hJ : ∑ i ∈ T, (w i / W) * Psi (s i ^ 2) ≤ Psi (∑ i ∈ T, (w i / W) * s i ^ 2) := by
    have := Psi_concave.le_map_sum (t := T) (w := fun i => w i / W) (p := fun i => s i ^ 2)
      (fun i hi => div_nonneg (hw i hi) hW.le)
      (by rw [← Finset.sum_div]; exact div_self hW.ne')
      (fun i _ => Set.mem_Ici.mpr (sq_nonneg (s i)))
    simpa [smul_eq_mul] using this
  have hsum1 : ∑ i ∈ T, (w i / W) * Psi (s i ^ 2) = (∑ i ∈ T, w i * Psi (s i ^ 2)) / W := by
    rw [Finset.sum_div]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    ring
  have hsum2 : ∑ i ∈ T, (w i / W) * s i ^ 2 = (∑ i ∈ T, w i * s i ^ 2) / W := by
    rw [Finset.sum_div]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    ring
  rw [hsum1, hsum2] at hJ
  -- monotonicity of Psi in its argument
  have hmono : Psi ((∑ i ∈ T, w i * s i ^ 2) / W) ≤ Psi (c / W) := by
    apply Psi_mono
    · apply div_nonneg _ hW.le
      exact Finset.sum_nonneg (fun i hi => mul_nonneg (hw i hi) (sq_nonneg (s i)))
    · exact div_le_div_of_nonneg_right hsec hW.le
  have hA : ∑ i ∈ T, w i * Psi (s i ^ 2) ≤ W * Psi (c / W) := by
    have := (div_le_iff₀ hW).mp (le_trans hJ hmono)
    linarith
  -- W ↦ W Psi(c / W) does not decrease: compare the ratios Psi(z)/z at z = c/W ≥ c/ε
  rcases hc.eq_or_lt with h | h
  · subst h
    simp only [zero_div] at hA ⊢
    have := Psi_zero_pos
    nlinarith
  · have hz1 : 0 < c / ε := div_pos h hε
    have hz12 : c / ε ≤ c / W := div_le_div_of_nonneg_left h.le hW hWε
    have hr := ratio_anti Psi_concave Psi_zero_pos.le hz1 hz12
    -- hr : Psi (c/W) / (c/W) ≤ Psi (c/ε) / (c/ε), i.e. W Psi(c/W) / c ≤ ε Psi(c/ε) / c
    have e1 : Psi (c / W) / (c / W) = W * Psi (c / W) / c := by field_simp
    have e2 : Psi (c / ε) / (c / ε) = ε * Psi (c / ε) / c := by field_simp
    rw [e1, e2] at hr
    have := (div_le_div_iff_of_pos_right h).mp hr
    linarith

end FEIMonoPsi

#print axioms FEIMonoPsi.jensen_chain
#print axioms FEIMonoPsi.ent_le
#print axioms FEIMonoPsi.sq_bound
