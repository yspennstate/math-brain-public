import Mathlib

/-!
# Elementary parts of three answers to questions of Hasebe, Ueda and Wang

This file checks some of the finite and elementary steps of the paper
"Free multiplicative convolution and log-unimodality: three questions of Hasebe, Ueda and Wang".
The free-probability input (the transforms, Lemma 4.1 of Hasebe, Ueda and Wang, the subordination
and branch arguments) is not formalized, nor are the steps that Section 6 of the paper lists as not
formalized; what is checked here are the inequalities listed below and the root count of Theorem B.

* `thmA_core`: for every real `L ≥ 6`, with `a = exp (-L)`,
  `a (1 - a²) (L² + π²)² < L (1 - a)⁴` and `1 < L (1 - a) / (1 + a)` (Theorem A).
* `thmB_four_roots`: for every `t > 0` there is `R ∈ (0, π)` for which the equation of
  Lemma 4.1 (3) of Hasebe, Ueda and Wang, written out for `ν = (δ_{1/10} + δ_{10}) / 2`,
  has four positive solutions (Theorem B): `R = √t / 2` when `t ≤ 8`, and
  `sin R / R = 8 / t` when `t > 8`.
* `K_B_zero`, `crossing_zero`, `crossing_three`, `crossing_mid`, `parameters`: the numerical
  part of the crossing lemma and of the choice of parameters (Theorem C).
-/

open Real Set

namespace LogUnimodality

/-! ### Exponentials and π -/

lemma exp_one_gt : (1359 / 500 : ℝ) < exp 1 :=
  (by norm_num : (1359 / 500 : ℝ) < 2.7182818283).trans Real.exp_one_gt_d9

lemma exp_one_pow' (n : ℕ) : exp 1 ^ n = exp n := by
  rw [← Real.exp_nat_mul, mul_one]

lemma exp_nat_ge (n : ℕ) : (1359 / 500 : ℝ) ^ n ≤ exp n := by
  rw [← exp_one_pow']
  gcongr
  exact exp_one_gt.le

lemma exp_six_gt : (400 : ℝ) < exp 6 := by
  have h := exp_nat_ge 6
  have h' : (400 : ℝ) < (1359 / 500) ^ 6 := by norm_num
  have e : ((6 : ℕ) : ℝ) = 6 := by norm_num
  rw [e] at h
  linarith

lemma exp_five_gt : (59 : ℝ) < exp 5 := by
  have h := exp_nat_ge 5
  have h' : (59 : ℝ) < (1359 / 500) ^ 5 := by norm_num
  have e : ((5 : ℕ) : ℝ) = 5 := by norm_num
  rw [e] at h
  linarith

lemma exp_ten_gt : (19 : ℝ) < exp 10 := by
  have h := exp_nat_ge 10
  have h' : (19 : ℝ) < (1359 / 500) ^ 10 := by norm_num
  have e : ((10 : ℕ) : ℝ) = 10 := by norm_num
  rw [e] at h
  linarith

lemma pi_sq_lt_ten : π ^ 2 < 10 := by
  have h1 : π < 63 / 20 := Real.pi_lt_d2.trans_le (by norm_num)
  have h0 := Real.pi_pos
  nlinarith

/-! ### Theorem A: the sign of the bracket, for every `L ≥ 6` -/

/-- `400 (1 + s + s²/2 + s³/6 + s⁴/24) < exp (s + 6)` for `s ≥ 0`. -/
lemma exp_lower (s : ℝ) (hs : 0 ≤ s) :
    400 * (1 + s + s ^ 2 / 2 + s ^ 3 / 6 + s ^ 4 / 24) < exp (s + 6) := by
  have hP : 1 + s + s ^ 2 / 2 + s ^ 3 / 6 + s ^ 4 / 24 ≤ exp s := by
    have h := Real.sum_le_exp_of_nonneg hs 5
    norm_num [Finset.sum_range_succ, Nat.factorial] at h
    linarith
  have hPpos : 0 < 1 + s + s ^ 2 / 2 + s ^ 3 / 6 + s ^ 4 / 24 := by
    have := pow_nonneg hs 2
    have := pow_nonneg hs 3
    have := pow_nonneg hs 4
    linarith
  rw [Real.exp_add]
  calc 400 * (1 + s + s ^ 2 / 2 + s ^ 3 / 6 + s ^ 4 / 24)
      < exp 6 * (1 + s + s ^ 2 / 2 + s ^ 3 / 6 + s ^ 4 / 24) :=
        mul_lt_mul_of_pos_right exp_six_gt hPpos
    _ ≤ exp 6 * exp s := mul_le_mul_of_nonneg_left hP (exp_pos 6).le
    _ = exp s * exp 6 := by ring

/-- The polynomial inequality behind Theorem A: every coefficient of the difference is positive. -/
lemma poly_bound (s : ℝ) (hs : 0 ≤ s) :
    ((s + 6) ^ 2 + 10) ^ 2 ≤
      (s + 6) * (399 / 400) ^ 4 * (400 * (1 + s + s ^ 2 / 2 + s ^ 3 / 6 + s ^ 4 / 24)) := by
  nlinarith [pow_nonneg hs 2, pow_nonneg hs 3, pow_nonneg hs 4, pow_nonneg hs 5]

/-- With `a = e^{-L}`: `a (1 - a²) (L² + π²)² < L (1 - a)⁴` (so `C_L < 1`) and
`L (1 - a) / (1 + a) > 1` (so the phase derivative is positive), for every real `L ≥ 6`. -/
theorem thmA_core (L : ℝ) (hL : 6 ≤ L) :
    exp (-L) * (1 - exp (-L) ^ 2) * (L ^ 2 + π ^ 2) ^ 2 < L * (1 - exp (-L)) ^ 4 ∧
    1 < L * (1 - exp (-L)) / (1 + exp (-L)) := by
  obtain ⟨s, hs, rfl⟩ : ∃ s, 0 ≤ s ∧ L = s + 6 := ⟨L - 6, by linarith, by ring⟩
  have hEL := exp_lower s hs
  have hpoly := poly_bound s hs
  have haE : exp (-(s + 6)) * exp (s + 6) = 1 := by
    rw [← Real.exp_add]; simp
  set a := exp (-(s + 6)) with ha_def
  have ha : 0 < a := exp_pos _
  have h400 : (400 : ℝ) < exp (s + 6) := by
    have := pow_nonneg hs 2
    have := pow_nonneg hs 3
    have := pow_nonneg hs 4
    linarith
  have ha400 : a < 1 / 400 := by
    rw [lt_div_iff₀ (by norm_num)]
    linarith [mul_lt_mul_of_pos_left h400 ha]
  have hL0 : 0 < s + 6 := by linarith
  constructor
  · have hX0 : 0 ≤ ((s + 6) ^ 2 + π ^ 2) ^ 2 := by positivity
    have hsq : ((s + 6) ^ 2 + π ^ 2) ^ 2 < ((s + 6) ^ 2 + 10) ^ 2 := by
      have hpi := pi_sq_lt_ten
      have e : ((s + 6) ^ 2 + 10) ^ 2 - ((s + 6) ^ 2 + π ^ 2) ^ 2 =
          (10 - π ^ 2) * (2 * (s + 6) ^ 2 + 10 + π ^ 2) := by ring
      have hpos : 0 < (10 - π ^ 2) * (2 * (s + 6) ^ 2 + 10 + π ^ 2) :=
        mul_pos (by linarith) (by positivity)
      linarith
    have hY : ((s + 6) ^ 2 + 10) ^ 2 < (s + 6) * (399 / 400) ^ 4 * exp (s + 6) := by
      have hm : (s + 6) * (399 / 400) ^ 4 * (400 * (1 + s + s ^ 2 / 2 + s ^ 3 / 6 + s ^ 4 / 24))
          < (s + 6) * (399 / 400) ^ 4 * exp (s + 6) :=
        mul_lt_mul_of_pos_left hEL (mul_pos hL0 (by norm_num))
      linarith
    have hq : (399 / 400 : ℝ) ^ 4 ≤ (1 - a) ^ 4 := by
      have h1 : (399 / 400 : ℝ) ≤ 1 - a := by linarith
      gcongr
    calc a * (1 - a ^ 2) * ((s + 6) ^ 2 + π ^ 2) ^ 2
        ≤ a * ((s + 6) ^ 2 + π ^ 2) ^ 2 := by
          apply mul_le_mul_of_nonneg_right _ hX0
          linarith [pow_pos ha 3]
      _ < a * ((s + 6) ^ 2 + 10) ^ 2 := mul_lt_mul_of_pos_left hsq ha
      _ < a * ((s + 6) * (399 / 400) ^ 4 * exp (s + 6)) := mul_lt_mul_of_pos_left hY ha
      _ = (s + 6) * (399 / 400) ^ 4 * (a * exp (s + 6)) := by ring
      _ = (s + 6) * (399 / 400) ^ 4 := by rw [haE, mul_one]
      _ ≤ (s + 6) * (1 - a) ^ 4 := mul_le_mul_of_nonneg_left hq hL0.le
  · rw [lt_div_iff₀ (by linarith)]
    nlinarith [mul_nonneg hs (by linarith : (0 : ℝ) ≤ 1 - a)]

/-! ### Theorem B: four roots of the equation of Lemma 4.1 (3), for every `t > 0` -/

/-- The integrand `r ξ / (1 + r² ξ² - 2 r ξ cos R)` of Lemma 4.1 (3) of Hasebe, Ueda and Wang. -/
noncomputable def integrand (R r ξ : ℝ) : ℝ := r * ξ / (1 + r ^ 2 * ξ ^ 2 - 2 * r * ξ * cos R)

/-- Its integral against `ν = (δ_{1/10} + δ_{10}) / 2`. -/
noncomputable def G (R r : ℝ) : ℝ := (integrand R r (1 / 10) + integrand R r 10) / 2

/-- `x / (1 + x² - 2 x c)`. -/
noncomputable def k (c x : ℝ) : ℝ := x / (1 + x ^ 2 - 2 * x * c)

lemma integrand_eq (R r ξ : ℝ) : integrand R r ξ = k (cos R) (r * ξ) := by
  unfold integrand k
  congr 1
  ring

lemma G_eq (R r : ℝ) : G R r = (k (cos R) (r * (1 / 10)) + k (cos R) (r * 10)) / 2 := by
  unfold G
  rw [integrand_eq, integrand_eq]

lemma k_den_pos {c x : ℝ} (hc : c < 1) (hx : 0 < x) : 0 < 1 + x ^ 2 - 2 * x * c := by
  nlinarith [sq_nonneg (1 - x), mul_pos hx (sub_pos.mpr hc)]

lemma k_pos {c x : ℝ} (hc : c < 1) (hx : 0 < x) : 0 < k c x :=
  div_pos hx (k_den_pos hc hx)

/-- In the variable `u = log r`: `k c (exp u) = 1 / (2 (cosh u - c))`, so that
`G R (exp u) = (k (cos R) (exp (u - log 10)) + k (cos R) (exp (u + log 10))) / 2` is the
function `F_R (u)` of the paper. -/
lemma k_exp {c : ℝ} (hc : c < 1) (u : ℝ) : k c (exp u) = 1 / (2 * (cosh u - c)) := by
  have h1 : exp u * exp (-u) = 1 := by rw [← Real.exp_add]; simp
  have h2 : 0 < 2 * (cosh u - c) := by linarith [Real.one_le_cosh u]
  unfold k
  rw [div_eq_div_iff (k_den_pos hc (exp_pos u)).ne' h2.ne', Real.cosh_eq]
  linear_combination h1

lemma k_one (c : ℝ) : k c 1 = 1 / (2 - 2 * c) := by
  unfold k
  congr 1
  ring

/-- For `c < 1`: `k c x ≤ x / (1 + x² - 2 x)` whenever the right-hand denominator is positive. -/
lemma k_le {c x : ℝ} (hc : c < 1) (hx : 0 < x) (hd : 0 < 1 + x ^ 2 - 2 * x) :
    k c x ≤ x / (1 + x ^ 2 - 2 * x) := by
  unfold k
  have h : 1 + x ^ 2 - 2 * x ≤ 1 + x ^ 2 - 2 * x * c := by
    nlinarith [mul_le_mul_of_nonneg_left hc.le hx.le]
  rw [div_le_div_iff₀ (k_den_pos hc hx) hd]
  exact mul_le_mul_of_nonneg_left h hx.le

/-- The value at the centre: `G R 1 = 1 / (101/10 - 2 cos R) ≤ 10 / 81`. -/
lemma G_one_le {R : ℝ} (hc : cos R < 1) : G R 1 ≤ 10 / 81 := by
  rw [G_eq]
  have h1 : k (cos R) (1 * (1 / 10)) ≤ 10 / 81 :=
    (k_le hc (by norm_num) (by norm_num)).trans_eq (by norm_num)
  have h2 : k (cos R) (1 * 10) ≤ 10 / 81 :=
    (k_le hc (by norm_num) (by norm_num)).trans_eq (by norm_num)
  linarith

/-- The value at the atom: `G R 10 > k (cos R) 1 / 2 = 1 / (4 - 4 cos R)`. -/
lemma G_ten_gt {R : ℝ} (hc : cos R < 1) : 1 / (4 - 4 * cos R) < G R 10 := by
  rw [G_eq, show (10 : ℝ) * (1 / 10) = 1 by norm_num, k_one]
  have h1 : 0 < k (cos R) (10 * 10) := k_pos hc (by norm_num)
  have h2 : 1 / (4 - 4 * cos R) = 1 / (2 - 2 * cos R) / 2 := by
    rw [div_div]
    congr 1
    ring
  rw [h2, add_div]
  exact lt_add_of_pos_right _ (half_pos h1)

lemma G_tenth_gt {R : ℝ} (hc : cos R < 1) : 1 / (4 - 4 * cos R) < G R (1 / 10) := by
  rw [G_eq, show (1 / 10 : ℝ) * 10 = 1 by norm_num, k_one]
  have h1 : 0 < k (cos R) (1 / 10 * (1 / 10)) := k_pos hc (by norm_num)
  have h2 : 1 / (4 - 4 * cos R) = 1 / (2 - 2 * cos R) / 2 := by
    rw [div_div]
    congr 1
    ring
  linarith

lemma G_thousand_lt {R : ℝ} (hc : cos R < 1) : G R 1000 < 1 / 8 := by
  rw [G_eq]
  have h1 : k (cos R) (1000 * (1 / 10)) ≤ 100 / 9801 :=
    (k_le hc (by norm_num) (by norm_num)).trans_eq (by norm_num)
  have h2 : k (cos R) (1000 * 10) ≤ 10000 / 99980001 :=
    (k_le hc (by norm_num) (by norm_num)).trans_eq (by norm_num)
  linarith

lemma G_thousandth_lt {R : ℝ} (hc : cos R < 1) : G R (1 / 1000) < 1 / 8 := by
  rw [G_eq]
  have h1 : k (cos R) (1 / 1000 * (1 / 10)) ≤ 10000 / 99980001 :=
    (k_le hc (by norm_num) (by norm_num)).trans_eq (by norm_num)
  have h2 : k (cos R) (1 / 1000 * 10) ≤ 100 / 9801 :=
    (k_le hc (by norm_num) (by norm_num)).trans_eq (by norm_num)
  linarith

lemma k_contOn {c a : ℝ} (hc : c < 1) (ha : 0 < a) :
    ContinuousOn (fun r => k c (r * a)) (Ioi 0) := by
  unfold k
  have h := ContinuousOn.div (f := fun r : ℝ => r * a)
    (g := fun r : ℝ => 1 + (r * a) ^ 2 - 2 * (r * a) * c) (s := Ioi (0 : ℝ))
    (by fun_prop) (by fun_prop)
    (fun r hr => (k_den_pos hc (mul_pos (Set.mem_Ioi.mp hr) ha)).ne')
  exact h

lemma G_contOn {R : ℝ} (hc : cos R < 1) : ContinuousOn (G R) (Icc (1 / 1000) 1000) := by
  have hG : G R = fun r => (k (cos R) (r * (1 / 10)) + k (cos R) (r * 10)) / 2 := by
    funext r; exact G_eq R r
  rw [hG]
  have h := ((k_contOn hc (by norm_num : (0 : ℝ) < 1 / 10)).add
    (k_contOn hc (by norm_num : (0 : ℝ) < 10))).div_const 2
  exact h.mono (fun r hr => Set.mem_Ioi.mpr (lt_of_lt_of_le (by norm_num) hr.1))

/-- Four solutions of `G R r = λ` for every level `λ` with `1/8 ≤ λ ≤ 1 / (4 - 4 cos R)`:
one in each of `(1/1000, 1/10)`, `(1/10, 1)`, `(1, 10)` and `(10, 1000)`. -/
theorem four_roots_of_window {R lev : ℝ} (hc : cos R < 1) (h1 : 1 / 8 ≤ lev)
    (h2 : lev ≤ 1 / (4 - 4 * cos R)) :
    ∃ r₁ r₂ r₃ r₄ : ℝ, 0 < r₁ ∧ r₁ < r₂ ∧ r₂ < r₃ ∧ r₃ < r₄ ∧
      G R r₁ = lev ∧ G R r₂ = lev ∧ G R r₃ = lev ∧ G R r₄ = lev := by
  have hcont := G_contOn hc
  have hA := G_thousandth_lt hc
  have hB := G_tenth_gt hc
  have hC := G_one_le hc
  have hD := G_ten_gt hc
  have hE := G_thousand_lt hc
  obtain ⟨r₁, hr₁, hG₁⟩ : lev ∈ G R '' Ioo (1 / 1000) (1 / 10) :=
    intermediate_value_Ioo (by norm_num) (hcont.mono (Icc_subset_Icc le_rfl (by norm_num)))
      ⟨by linarith, by linarith⟩
  obtain ⟨r₂, hr₂, hG₂⟩ : lev ∈ G R '' Ioo (1 / 10) 1 :=
    intermediate_value_Ioo' (by norm_num) (hcont.mono (Icc_subset_Icc (by norm_num) (by norm_num)))
      ⟨by linarith, by linarith⟩
  obtain ⟨r₃, hr₃, hG₃⟩ : lev ∈ G R '' Ioo 1 10 :=
    intermediate_value_Ioo (by norm_num) (hcont.mono (Icc_subset_Icc (by norm_num) (by norm_num)))
      ⟨by linarith, by linarith⟩
  obtain ⟨r₄, hr₄, hG₄⟩ : lev ∈ G R '' Ioo 10 1000 :=
    intermediate_value_Ioo' (by norm_num) (hcont.mono (Icc_subset_Icc (by norm_num) le_rfl))
      ⟨by linarith, by linarith⟩
  exact ⟨r₁, r₂, r₃, r₄, by linarith [hr₁.1], by linarith [hr₁.2, hr₂.1],
    by linarith [hr₂.2, hr₃.1], by linarith [hr₃.2, hr₄.1], hG₁, hG₂, hG₃, hG₄⟩

/-- `t ≤ 8`: with `R = √t / 2` the level `R / (t sin R)` lies in the window. -/
lemma level_small (t : ℝ) (ht0 : 0 < t) (ht : t ≤ 8) :
    ∃ R ∈ Ioo 0 π, cos R < 1 ∧ 1 / 8 ≤ R / (t * sin R) ∧
      R / (t * sin R) ≤ 1 / (4 - 4 * cos R) := by
  obtain ⟨R, hRdef⟩ : ∃ R, R = Real.sqrt t / 2 := ⟨_, rfl⟩
  have hR0 : 0 < R := by rw [hRdef]; exact div_pos (Real.sqrt_pos.mpr ht0) two_pos
  have hRt : t = 4 * R ^ 2 := by rw [hRdef, div_pow, Real.sq_sqrt ht0.le]; ring
  have hR2 : R ^ 2 ≤ 2 := by linarith
  have hR3 : R < 3 := by nlinarith
  have hRpi : R < π := by linarith [Real.pi_gt_three]
  have hs : 0 < sin R := Real.sin_pos_of_pos_of_lt_pi hR0 hRpi
  have hsle : sin R ≤ R := Real.sin_le hR0.le
  have hsgt : R - R ^ 3 / 6 < sin R := Real.sin_gt_sub_cube hR0
  have hcos : 1 - R ^ 2 / 2 ≤ cos R := Real.one_sub_sq_div_two_le_cos
  have hc : cos R < 1 := by
    have h := Real.cos_lt_cos_of_nonneg_of_le_pi (le_refl 0) hRpi.le hR0
    rwa [Real.cos_zero] at h
  have e : t * sin R = 4 * (R ^ 2 * sin R) := by rw [hRt]; ring
  refine ⟨R, ⟨hR0, hRpi⟩, hc, ?_, ?_⟩
  · rw [div_le_div_iff₀ (by norm_num) (mul_pos ht0 hs)]
    have h1 : R ^ 2 * sin R ≤ R ^ 2 * R := mul_le_mul_of_nonneg_left hsle (by positivity)
    have h2 : R * R ^ 2 ≤ R * 2 := mul_le_mul_of_nonneg_left hR2 hR0.le
    calc 1 * (t * sin R) = 4 * (R ^ 2 * sin R) := by rw [e]; ring
      _ ≤ 4 * (R ^ 2 * R) := by linarith
      _ = 4 * (R * R ^ 2) := by ring
      _ ≤ 4 * (R * 2) := by linarith
      _ = R * 8 := by ring
  · have h4 : 0 < 4 - 4 * cos R := by linarith
    rw [div_le_div_iff₀ (mul_pos ht0 hs) h4]
    have hA : R * (4 - 4 * cos R) ≤ R * (2 * R ^ 2) :=
      mul_le_mul_of_nonneg_left (by linarith) hR0.le
    have hB : 4 * R ^ 2 * (R - R ^ 3 / 6) ≤ 4 * R ^ 2 * sin R :=
      mul_le_mul_of_nonneg_left hsgt.le (by positivity)
    have hC : 0 ≤ R ^ 3 * (3 - R ^ 2) := mul_nonneg (pow_nonneg hR0.le 3) (by linarith)
    have hD : 4 * R ^ 2 * (R - R ^ 3 / 6) - R * (2 * R ^ 2) = 2 / 3 * (R ^ 3 * (3 - R ^ 2)) := by
      ring
    calc R * (4 - 4 * cos R) ≤ R * (2 * R ^ 2) := hA
      _ ≤ 4 * R ^ 2 * (R - R ^ 3 / 6) := by linarith
      _ ≤ 4 * R ^ 2 * sin R := hB
      _ = 1 * (t * sin R) := by rw [e]; ring

/-- `t > 8`: an angle `R ∈ (0, π)` with `sin R / R = 8 / t`; then `R / (t sin R) = 1 / 8`,
which lies in the window. -/
lemma level_large (t : ℝ) (ht : 8 < t) :
    ∃ R ∈ Ioo 0 π, cos R < 1 ∧ 1 / 8 ≤ R / (t * sin R) ∧
      R / (t * sin R) ≤ 1 / (4 - 4 * cos R) := by
  have ht0 : 0 < t := by linarith
  have h8 : 0 < 1 - 8 / t := by
    have : 8 / t < 1 := (div_lt_one ht0).mpr ht
    linarith
  obtain ⟨R₀, hR₀⟩ : ∃ R₀, R₀ = min 1 (6 * (1 - 8 / t)) := ⟨_, rfl⟩
  have hR₀pos : 0 < R₀ := by rw [hR₀]; exact lt_min one_pos (by linarith)
  have hR₀1 : R₀ ≤ 1 := by rw [hR₀]; exact min_le_left _ _
  have hR₀2 : R₀ ≤ 6 * (1 - 8 / t) := by rw [hR₀]; exact min_le_right _ _
  have hR₀pi : R₀ < π := by linarith [Real.pi_gt_three]
  have hcont : ContinuousOn (fun R => sin R / R) (Icc R₀ π) := by
    have h := Real.continuous_sin.continuousOn.div (continuousOn_id (s := Icc R₀ π))
      (fun x hx => (show (0 : ℝ) < x by linarith [hx.1]).ne')
    exact h
  have hlo : sin π / π < 8 / t := by
    rw [Real.sin_pi, zero_div]
    exact div_pos (by norm_num) ht0
  have hhi : 8 / t < sin R₀ / R₀ := by
    have h := Real.sin_gt_sub_cube hR₀pos
    have hq : R₀ * R₀ ≤ R₀ * 1 := mul_le_mul_of_nonneg_left hR₀1 hR₀pos.le
    have hsq : R₀ ^ 2 ≤ 6 * (1 - 8 / t) :=
      calc R₀ ^ 2 = R₀ * R₀ := by ring
        _ ≤ R₀ * 1 := hq
        _ = R₀ := by ring
        _ ≤ 6 * (1 - 8 / t) := hR₀2
    have hm : R₀ * R₀ ^ 2 ≤ R₀ * (6 * (1 - 8 / t)) := mul_le_mul_of_nonneg_left hsq hR₀pos.le
    rw [lt_div_iff₀ hR₀pos]
    calc 8 / t * R₀ = R₀ - R₀ * (6 * (1 - 8 / t)) / 6 := by ring
      _ ≤ R₀ - R₀ * R₀ ^ 2 / 6 := by linarith
      _ = R₀ - R₀ ^ 3 / 6 := by ring
      _ < sin R₀ := h
  obtain ⟨R, hR, hRv⟩ := intermediate_value_Ioo' hR₀pi.le hcont ⟨hlo, hhi⟩
  have hRv' : sin R / R = 8 / t := hRv
  have hR0 : 0 < R := lt_trans hR₀pos hR.1
  have hs : 0 < sin R := Real.sin_pos_of_pos_of_lt_pi hR0 hR.2
  have hc : cos R < 1 := by
    have h := Real.cos_lt_cos_of_nonneg_of_le_pi (le_refl 0) hR.2.le hR0
    rwa [Real.cos_zero] at h
  have hts : t * sin R = 8 * R := by
    rw [div_eq_div_iff hR0.ne' ht0.ne'] at hRv'
    linarith
  have hlev : R / (t * sin R) = 1 / 8 := by
    rw [hts, div_eq_div_iff (mul_pos (by norm_num) hR0).ne' (by norm_num)]
    ring
  refine ⟨R, ⟨hR0, hR.2⟩, hc, le_of_eq hlev.symm, ?_⟩
  rw [hlev, div_le_div_iff₀ (by norm_num) (by linarith)]
  linarith [Real.neg_one_le_cos R]

/-- Theorem B, root count: for every `t > 0` there is `R ∈ (0, π)` such that the equation
`(sin R / R) ∫ r ξ / (1 + r² ξ² - 2 r ξ cos R) dν(ξ) = 1 / t`, with `ν = (δ_{1/10} + δ_{10}) / 2`,
has four distinct positive solutions `r`. The angle is `R = √t / 2` for `t ≤ 8` (`level_small`)
and a solution of `sin R / R = 8 / t` for `t > 8` (`level_large`). -/
theorem thmB_four_roots (t : ℝ) (ht : 0 < t) :
    ∃ R ∈ Ioo 0 π, ∃ r₁ r₂ r₃ r₄ : ℝ, 0 < r₁ ∧ r₁ < r₂ ∧ r₂ < r₃ ∧ r₃ < r₄ ∧
      sin R / R * G R r₁ = 1 / t ∧ sin R / R * G R r₂ = 1 / t ∧
      sin R / R * G R r₃ = 1 / t ∧ sin R / R * G R r₄ = 1 / t := by
  obtain ⟨R, hR, hc, h1, h2⟩ : ∃ R ∈ Ioo 0 π, cos R < 1 ∧ 1 / 8 ≤ R / (t * sin R) ∧
      R / (t * sin R) ≤ 1 / (4 - 4 * cos R) := by
    rcases le_or_gt t 8 with h | h
    · exact level_small t ht h
    · exact level_large t h
  have hs : 0 < sin R := Real.sin_pos_of_pos_of_lt_pi hR.1 hR.2
  have key : ∀ r, G R r = R / (t * sin R) → sin R / R * G R r = 1 / t := by
    intro r hr
    rw [hr, div_mul_div_comm, div_eq_div_iff (mul_pos hR.1 (mul_pos ht hs)).ne' ht.ne']
    ring
  obtain ⟨r₁, r₂, r₃, r₄, h0, h12, h23, h34, e1, e2, e3, e4⟩ := four_roots_of_window hc h1 h2
  exact ⟨R, hR, r₁, r₂, r₃, r₄, h0, h12, h23, h34, key _ e1, key _ e2, key _ e3, key _ e4⟩

/-- The two-atom measure is not covered by Theorem 4.4 of Hasebe, Ueda and Wang:
with `α = 1/10` and `β = 10`, `β⁴ - 3 α⁴ < 2 α³ β` fails. -/
lemma thm44_hypothesis_fails : ¬ ((10 : ℝ) ^ 4 - 3 * (1 / 10) ^ 4 < 2 * (1 / 10) ^ 3 * 10) := by
  norm_num

/-- `cosh (log 10) = 101 / 20`, so `1 / (2 cosh (log 10)) = 10 / 101 < 1 / 10 < 1 / 8`. -/
lemma cosh_log_ten : cosh (log 10) = 101 / 20 := by
  rw [Real.cosh_log (by norm_num)]
  norm_num

/-! ### Theorem C: the crossing lemma -/

lemma cot_twentieth : (799 : ℝ) / 40 < cot (1 / 20) := by
  rw [Real.cot_eq_cos_div_sin]
  have hs : 0 < sin (1 / 20 : ℝ) :=
    Real.sin_pos_of_pos_of_lt_pi (by norm_num) (by linarith [Real.pi_gt_three])
  have hs2 : sin (1 / 20 : ℝ) < 1 / 20 := Real.sin_lt (by norm_num)
  have hc : 1 - (1 / 20 : ℝ) ^ 2 / 2 ≤ cos (1 / 20) := Real.one_sub_sq_div_two_le_cos
  have e : (1 - (1 / 20 : ℝ) ^ 2 / 2) = 799 / 800 := by norm_num
  rw [e] at hc
  rw [lt_div_iff₀ hs]
  linarith

lemma tanh_five_halves : (29 : ℝ) / 30 < tanh (5 / 2) := by
  rw [Real.tanh_eq]
  have hE0 : 0 < exp (5 / 2 : ℝ) := exp_pos _
  have hF0 : 0 < exp (-(5 / 2) : ℝ) := exp_pos _
  have hEF : exp (5 / 2 : ℝ) * exp (-(5 / 2)) = 1 := by
    rw [← Real.exp_add]; simp
  have hE2 : exp (5 / 2 : ℝ) * exp (5 / 2) = exp 5 := by
    rw [← Real.exp_add]; norm_num
  have h5 := exp_five_gt
  rw [lt_div_iff₀ (by linarith)]
  nlinarith

lemma tanh_five : (9 : ℝ) / 10 < tanh 5 := by
  rw [Real.tanh_eq]
  have hE0 : 0 < exp (5 : ℝ) := exp_pos _
  have hF0 : 0 < exp (-5 : ℝ) := exp_pos _
  have hEF : exp (5 : ℝ) * exp (-5) = 1 := by
    rw [← Real.exp_add]; simp
  have hE2 : exp (5 : ℝ) * exp 5 = exp 10 := by
    rw [← Real.exp_add]; norm_num
  have h10 := exp_ten_gt
  rw [lt_div_iff₀ (by linarith)]
  nlinarith

lemma arctan_lt_self {y : ℝ} (hy : 0 < y) : arctan y < y := by
  have h1 : 0 < arctan y := Real.arctan_pos.mpr hy
  have h2 : arctan y < π / 2 := Real.arctan_lt_pi_div_two y
  have h3 := Real.lt_tan h1 h2
  rwa [Real.tan_arctan] at h3

/-- `arctan x > π/2 - 1/x` for `x > 0`. -/
lemma arctan_gt {x : ℝ} (hx : 0 < x) : π / 2 - 1 / x < arctan x := by
  have h1 : arctan x⁻¹ = π / 2 - arctan x := Real.arctan_inv_of_pos hx
  have h2 : arctan x⁻¹ < x⁻¹ := arctan_lt_self (inv_pos.mpr hx)
  rw [one_div]
  linarith

/-- `arctan (1/3) > π/20 + 4/25`, through `tan (111/350) < 1/3`. -/
lemma arctan_third : π / 20 + 4 / 25 < arctan (1 / 3) := by
  have hpi : π < 3927 / 1250 := Real.pi_lt_d4.trans_le (by norm_num)
  have hpi3 := Real.pi_gt_three
  have hx : arctan (tan (111 / 350 : ℝ)) = 111 / 350 :=
    Real.arctan_tan (by linarith) (by linarith)
  have hc : 0 < cos (111 / 350 : ℝ) := Real.cos_pos_of_mem_Ioo ⟨by linarith, by linarith⟩
  have hcos : 1 - (111 / 350 : ℝ) ^ 2 / 2 ≤ cos (111 / 350) := Real.one_sub_sq_div_two_le_cos
  have e1 : (1 - (111 / 350 : ℝ) ^ 2 / 2) = 232679 / 245000 := by norm_num
  rw [e1] at hcos
  have hsin0 := Real.sin_bound (x := (111 / 350 : ℝ))
    (by rw [abs_of_pos (by norm_num : (0 : ℝ) < 111 / 350)]; norm_num)
  have hsin : sin (111 / 350 : ℝ) < 5 / 16 := by
    have h := (abs_le.mp hsin0).2
    rw [abs_of_pos (by norm_num : (0 : ℝ) < 111 / 350)] at h
    have e : (111 / 350 : ℝ) - (111 / 350) ^ 3 / 6 + (111 / 350) ^ 5 / 100 < 5 / 16 := by norm_num
    linarith
  have htan : tan (111 / 350 : ℝ) < 1 / 3 := by
    rw [Real.tan_eq_sin_div_cos, div_lt_iff₀ hc]
    linarith
  have h := Real.arctan_strictMono htan
  rw [hx] at h
  linarith

/-- `K_B(0) = cot(1/20) / (20 π)` for `B = 1/10`: the kernel `b sin b / (2π (cosh (b v) - cos b))`
at `v = 0`. -/
lemma K_B_zero :
    (1 / 10 : ℝ) * sin (1 / 10) / (2 * π * (cosh (1 / 10 * 0) - cos (1 / 10))) =
      cot (1 / 20) / (20 * π) := by
  have hs : 0 < sin (1 / 20 : ℝ) :=
    Real.sin_pos_of_pos_of_lt_pi (by norm_num) (by linarith [Real.pi_gt_three])
  have hpi := Real.pi_pos
  have h2 : sin (1 / 10 : ℝ) = 2 * sin (1 / 20) * cos (1 / 20) := by
    rw [← Real.sin_two_mul]; norm_num
  have h3 : cos (1 / 10 : ℝ) = 1 - 2 * sin (1 / 20) ^ 2 := by
    have e : (1 / 10 : ℝ) = 2 * (1 / 20) := by norm_num
    rw [e, Real.cos_two_mul]
    linarith [Real.sin_sq_add_cos_sq (1 / 20 : ℝ)]
  rw [h2, h3, mul_zero, Real.cosh_zero, sub_sub_cancel, Real.cot_eq_cos_div_sin, div_div]
  have hb : 2 * π * (2 * sin (1 / 20 : ℝ) ^ 2) ≠ 0 :=
    (mul_pos (mul_pos two_pos hpi) (mul_pos two_pos (pow_pos hs 2))).ne'
  have hd : sin (1 / 20 : ℝ) * (20 * π) ≠ 0 := (mul_pos hs (mul_pos (by norm_num) hpi)).ne'
  rw [div_eq_div_iff hb hd]
  ring

/-- `W(0) > 19/20`: `W(0) ≥ (8/5) K_B(0) + (123/125) ∫_{-100}^0 K_B`, with
`∫_{-100}^0 K_B = arctan (cot (1/20) tanh 5) / π`. -/
lemma crossing_zero :
    (19 : ℝ) / 20 < 8 / 5 * (cot (1 / 20) / (20 * π)) +
      123 / 125 * (arctan (cot (1 / 20) * tanh 5) / π) := by
  have hX := cot_twentieth
  have hT := tanh_five
  have hpi : π < 63 / 20 := Real.pi_lt_d2.trans_le (by norm_num)
  have hpi0 := Real.pi_pos
  set X := cot (1 / 20 : ℝ) with hXdef
  set T := tanh (5 : ℝ) with hTdef
  have hXT : (7191 : ℝ) / 400 < X * T := by
    nlinarith [mul_pos (sub_pos.mpr hX) (sub_pos.mpr hT)]
  have hA := arctan_gt (by linarith : (0 : ℝ) < X * T)
  have hinv : 1 / (X * T) < 400 / 7191 := by
    rw [div_lt_div_iff₀ (by linarith) (by norm_num)]
    linarith
  have hQ : 19 / 20 * π < 2 * X / 25 + 123 * arctan (X * T) / 125 := by linarith
  have hJ : 0 < π⁻¹ := inv_pos.mpr hpi0
  have hpJ : π * π⁻¹ = 1 := mul_inv_cancel₀ hpi0.ne'
  have e : 8 / 5 * (X / (20 * π)) + 123 / 125 * (arctan (X * T) / π) =
      (2 * X / 25 + 123 * arctan (X * T) / 125) * π⁻¹ := by ring
  rw [e]
  nlinarith [mul_pos (sub_pos.mpr hQ) hJ]

/-- `W(3) < 19/20`: `W(3) ≤ (8/5) K_0(3) + ∫_{-∞}^3 K_0 = 1 - arctan(1/3)/π + 4/(25π)`. -/
lemma crossing_three : 1 - arctan (1 / 3) / π + 4 / (25 * π) < (19 : ℝ) / 20 := by
  have h := arctan_third
  have hpi0 := Real.pi_pos
  have hJ : 0 < π⁻¹ := inv_pos.mpr hpi0
  have hpJ : π * π⁻¹ = 1 := mul_inv_cancel₀ hpi0.ne'
  have e : 1 - arctan (1 / 3) / π + 4 / (25 * π) =
      1 - arctan (1 / 3) * π⁻¹ + 4 / 25 * π⁻¹ := by ring
  rw [e]
  nlinarith [mul_pos (sub_pos.mpr h) hJ]

/-- `W(ℓ/2) > 19/20`: `W(ℓ/2) ≥ (123/125) ∫_{-50}^{50} K_B`, with
`∫_{-50}^{50} K_B = 2 arctan (cot (1/20) tanh (5/2)) / π`. -/
lemma crossing_mid :
    (19 : ℝ) / 20 < 123 / 125 * (2 * arctan (cot (1 / 20) * tanh (5 / 2)) / π) := by
  have hX := cot_twentieth
  have hT := tanh_five_halves
  have hpi := Real.pi_gt_three
  have hpi0 := Real.pi_pos
  set X := cot (1 / 20 : ℝ) with hXdef
  set T := tanh (5 / 2 : ℝ) with hTdef
  have hXT : (23171 : ℝ) / 1200 < X * T := by
    nlinarith [mul_pos (sub_pos.mpr hX) (sub_pos.mpr hT)]
  have hA := arctan_gt (by linarith : (0 : ℝ) < X * T)
  have hinv : 1 / (X * T) < 1200 / 23171 := by
    rw [div_lt_div_iff₀ (by linarith) (by norm_num)]
    linarith
  have hQ : 19 / 20 * π < 246 / 125 * arctan (X * T) := by linarith
  have hJ : 0 < π⁻¹ := inv_pos.mpr hpi0
  have hpJ : π * π⁻¹ = 1 := mul_inv_cancel₀ hpi0.ne'
  have e : 123 / 125 * (2 * arctan (X * T) / π) = 246 / 125 * arctan (X * T) * π⁻¹ := by ring
  rw [e]
  nlinarith [mul_pos (sub_pos.mpr hQ) hJ]

/-- The parameters of the proof of Theorem C: with `ℓ = max 100 (95 π t)` and `d = 19/20`,
`b² = π d t / ℓ ≤ 1/100`, `ℓ ≥ 100`, `p = 8/(5ℓ) ≤ 2/125`, and `b² / (π D) = t` for `D = d/ℓ`. -/
lemma parameters (t ℓ : ℝ) (hℓ : ℓ = max 100 (95 * π * t)) :
    π * (19 / 20) * t / ℓ ≤ 1 / 100 ∧ 100 ≤ ℓ ∧ 8 / (5 * ℓ) ≤ 2 / 125 ∧
      (π * (19 / 20) * t / ℓ) / (π * ((19 / 20) / ℓ)) = t := by
  have hpi0 := Real.pi_pos
  have h1 : 100 ≤ ℓ := by rw [hℓ]; exact le_max_left _ _
  have h2 : 95 * π * t ≤ ℓ := by rw [hℓ]; exact le_max_right _ _
  have hl0 : 0 < ℓ := by linarith
  refine ⟨?_, h1, ?_, ?_⟩
  · rw [div_le_div_iff₀ hl0 (by norm_num)]
    linarith
  · rw [div_le_div_iff₀ (by linarith) (by norm_num)]
    linarith
  · have hY : π * ((19 / 20) / ℓ) ≠ 0 := (mul_pos hpi0 (div_pos (by norm_num) hl0)).ne'
    rw [div_eq_iff hY]
    ring

end LogUnimodality

#print axioms LogUnimodality.thmA_core
#print axioms LogUnimodality.k_exp
#print axioms LogUnimodality.four_roots_of_window
#print axioms LogUnimodality.level_small
#print axioms LogUnimodality.level_large
#print axioms LogUnimodality.thmB_four_roots
#print axioms LogUnimodality.thm44_hypothesis_fails
#print axioms LogUnimodality.cosh_log_ten
#print axioms LogUnimodality.arctan_third
#print axioms LogUnimodality.K_B_zero
#print axioms LogUnimodality.crossing_zero
#print axioms LogUnimodality.crossing_three
#print axioms LogUnimodality.crossing_mid
#print axioms LogUnimodality.parameters
