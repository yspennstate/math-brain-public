import Mathlib

/-!
# The flow parameter on cones: identities and constants

Machine checks for the paper *Multicommodity flow, the relaxation time and the diameter*.
The combinatorial inputs (the eigenvalues of a cone, the distance counts in the incidence graph
of a projective plane, the shape of the flows) are taken from the paper; the file checks that the
formulas built from them are as stated.

* `spectrum_quadratic`: the `2 × 2` block in the proof of Lemma 3.1.
* `hub_load`: the value `2(d+1)(1 - π_v)` in Lemma 3.2.
* `lengths_sum`, `cert_lower`: the total length and the last inequality in Lemma 3.3.
* `r_eq_3d_bound`, `explicit_quantifier`: the explicit quantifiers after the proof of Theorem 1.1.
* `V3_from_cert`, `one_sub_theta`, `theta_mem`, `loads_equal`, `load_eq_V3`: the certificate with
  `r = 3` and the routing in the proof of Proposition 5.1.
* `V3_strictMono`, `ratio_strictMonoOn`, `ratio_37_lt_two`, `two_lt_ratio_38`, `two_lt_ratio_iff`:
  on projective-plane cones the ratio `F/(τ₂Δ)` is increasing in `s` and exceeds `2` exactly for
  `s ≥ 38` (Proposition 5.1).
* `V3_37`, `V3_41`, `V3_49`: exact entries of Table 1 (`V3_38` serves the threshold).
* `degree_constant`, `log_constant`: the constants `65` and `2.55` in Proposition 6.1.
-/

namespace FlowParameter

/-! ### Cones over regular graphs -/

/-- On functions constant on the base, `P` acts by `[[0, 1], [1/(d+1), d/(d+1)]]`;
its characteristic polynomial is `(x - 1)(x + 1/(d+1))`. -/
theorem spectrum_quadratic (d x : ℝ) (hd : 0 < d) :
    (0 - x) * (d / (d + 1) - x) - 1 * (1 / (d + 1)) = (x - 1) * (x + 1 / (d + 1)) := by
  have h : d + 1 ≠ 0 := by positivity
  field_simp
  ring

/-- The hub routing: `2m · 2π_v(1 - π_v) = 2(d+1)(1 - π_v)`, with `2m = n(d+2)` and
`π_v = (d+1)/(n(d+2))`. -/
theorem hub_load (d n : ℝ) (hd : 0 < d) (hn : 0 < n) :
    n * (d + 2) * (2 * ((d + 1) / (n * (d + 2))) * (1 - (d + 1) / (n * (d + 2))))
      = 2 * (d + 1) * (1 - (d + 1) / (n * (d + 2))) := by
  have h : n * (d + 2) ≠ 0 := by positivity
  field_simp

/-- The two-length certificate: base edges of length `2L/r` and spokes of length
`L = (d+2)r/(r+d)` have total length `2m = n(d+2)`. -/
theorem lengths_sum (d r n : ℝ) (hd : 0 < d) (hr : 0 < r) :
    n * d / 2 * (2 * ((d + 2) * r / (r + d)) / r) + n * ((d + 2) * r / (r + d))
      = n * (d + 2) := by
  have h1 : r + d ≠ 0 := by positivity
  have h2 : r ≠ 0 := hr.ne'
  field_simp
  ring

/-- The last step of the certificate bound:
`2L[π_h π_B + π_v² n(n - 1 - B)] ≥ 2(d+1) (r/(r+d)) (1 - (1+B)/n)`. -/
theorem cert_lower (d r n B : ℝ) (hd : 0 < d) (hr : 0 < r) (hn : 0 < n) (hB : 0 ≤ B) :
    2 * (d + 1) * (r / (r + d)) * (1 - (1 + B) / n) ≤
      2 * ((d + 2) * r / (r + d)) * (1 / (d + 2) * (n * ((d + 1) / (n * (d + 2))))
        + ((d + 1) / (n * (d + 2))) ^ 2 * (n * (n - 1 - B))) := by
  rw [← sub_nonneg]
  have key :
      2 * ((d + 2) * r / (r + d)) * (1 / (d + 2) * (n * ((d + 1) / (n * (d + 2))))
        + ((d + 1) / (n * (d + 2))) ^ 2 * (n * (n - 1 - B)))
        - 2 * (d + 1) * (r / (r + d)) * (1 - (1 + B) / n)
      = 2 * (d + 1) * r * (1 + B) / ((r + d) * (d + 2) * n) := by
    have h1 : r + d ≠ 0 := by positivity
    have h2 : d + 2 ≠ 0 := by positivity
    have h3 : n ≠ 0 := hn.ne'
    field_simp
    ring
  rw [key]
  positivity

/-- With `r = 3d` and `n ≥ 2(1 + B)` the lower bound of the theorem on cones is at least
`(3/4)(d+1)`. -/
theorem r_eq_3d_bound (d n B : ℝ) (hd : 0 < d) (hB : 0 ≤ B) (hn : 2 * (1 + B) ≤ n) :
    3 / 4 * (d + 1) ≤ 2 * (d + 1) * (3 * d / (3 * d + d)) * (1 - (1 + B) / n) := by
  have hn0 : 0 < n := by linarith
  have h1 : 3 * d / (3 * d + d) = 3 / 4 := by
    have : 3 * d + d ≠ 0 := by positivity
    field_simp
    ring
  have h2 : (1 + B) / n ≤ 1 / 2 := by
    rw [div_le_iff₀ hn0]
    linarith
  rw [h1]
  nlinarith

/-- The explicit quantifier in the proof of the main theorem: `(3/8)(103 - 2√101) > 30`. -/
theorem explicit_quantifier : 30 < 3 / 8 * (103 - 2 * Real.sqrt 101) := by
  have h : Real.sqrt 101 < 201 / 20 := by
    rw [Real.sqrt_lt' (by norm_num)]
    norm_num
  linarith

/-! ### Projective-plane cones -/

/-- The closed form of the flow parameter on the cone over the incidence graph of a projective
plane of order `s`. -/
noncomputable def V3 (s : ℝ) : ℝ :=
  (s + 2) * (5 * s ^ 3 + 19 * s ^ 2 + 13 * s + 8) / ((s + 3) * (s + 4) * (s ^ 2 + s + 1))

/-- The share of the traffic between two vertices at distance three that goes through the hub. -/
noncomputable def theta (s : ℝ) : ℝ := 3 * (s ^ 2 + 3 * s + 1) / (s * (s + 2) * (s + 4))

/-- The certificate with `r = 3`: `d = s+1`, `n = 2(s²+s+1)`, `L = 3(d+2)/(3+d)`,
`π_h = 1/(s+3)`, `π_v = (s+2)/(n(s+3))`, and from every base vertex `s+1`, `s²+s` and `s²`
vertices at distances one, two and three. -/
theorem V3_from_cert (s : ℝ) (hs : 0 < s) :
    2 * ((s + 3) * 3 / (3 + (s + 1))) *
      (1 / (s + 3) * (2 * (s ^ 2 + s + 1) * ((s + 2) / (2 * (s ^ 2 + s + 1) * (s + 3))))
        + ((s + 2) / (2 * (s ^ 2 + s + 1) * (s + 3))) ^ 2 *
          (2 * (s ^ 2 + s + 1) * ((s + 1) / 3 + 2 * (s ^ 2 + s) / 3 + s ^ 2)))
      = V3 s := by
  unfold V3
  have h1 : s ^ 2 + s + 1 ≠ 0 := by positivity
  have h2 : s + 3 ≠ 0 := by positivity
  have h3 : 3 + (s + 1) ≠ 0 := by positivity
  have h4 : s + 4 ≠ 0 := by positivity
  field_simp
  ring

theorem one_sub_theta (s : ℝ) (hs : 0 < s) :
    1 - theta s = (s - 1) * (s + 1) * (s + 3) / (s * (s + 2) * (s + 4)) := by
  unfold theta
  have h : s * (s + 2) * (s + 4) ≠ 0 := by positivity
  field_simp
  ring

theorem theta_mem (s : ℝ) (hs : 1 ≤ s) : 0 < theta s ∧ theta s ≤ 1 := by
  have hs0 : 0 < s := by linarith
  refine ⟨by unfold theta; positivity, ?_⟩
  have h := one_sub_theta s hs0
  have h' : 0 ≤ (s - 1) * (s + 1) * (s + 3) / (s * (s + 2) * (s + 4)) := by
    apply div_nonneg
    · exact mul_nonneg (mul_nonneg (by linarith) (by linarith)) (by linarith)
    · positivity
  linarith

/-- The routing in the proof: the load of a spoke equals the load of a base edge. -/
theorem loads_equal (s : ℝ) (hs : 0 < s) :
    2 * (1 / (s + 3)) * ((s + 2) / (2 * (s ^ 2 + s + 1) * (s + 3)))
        + 2 * theta s * s ^ 2 * ((s + 2) / (2 * (s ^ 2 + s + 1) * (s + 3))) ^ 2
      = ((s + 2) / (2 * (s ^ 2 + s + 1) * (s + 3))) ^ 2 *
          (2 + 4 * s + 6 * s ^ 2 * (1 - theta s) / (s + 1)) := by
  unfold theta
  have h1 : s ^ 2 + s + 1 ≠ 0 := by positivity
  have h2 : s + 3 ≠ 0 := by positivity
  have h3 : s + 1 ≠ 0 := by positivity
  have h4 : s * (s + 2) * (s + 4) ≠ 0 := by positivity
  field_simp
  ring

/-- ... and `2m` times that load, `2m = 2(s²+s+1)(s+3)`, is `V3`. -/
theorem load_eq_V3 (s : ℝ) (hs : 0 < s) :
    2 * (s ^ 2 + s + 1) * (s + 3) *
      (2 * (1 / (s + 3)) * ((s + 2) / (2 * (s ^ 2 + s + 1) * (s + 3)))
        + 2 * theta s * s ^ 2 * ((s + 2) / (2 * (s ^ 2 + s + 1) * (s + 3))) ^ 2) = V3 s := by
  unfold theta V3
  have h1 : s ^ 2 + s + 1 ≠ 0 := by positivity
  have h2 : s + 3 ≠ 0 := by positivity
  have h3 : s + 4 ≠ 0 := by positivity
  have h4 : s * (s + 2) * (s + 4) ≠ 0 := by positivity
  field_simp
  ring

theorem V3_strictMono {s t : ℝ} (hs : 0 < s) (hst : s < t) : V3 s < V3 t := by
  have ht : 0 < t := lt_trans hs hst
  unfold V3
  rw [div_lt_div_iff₀ (by positivity) (by positivity)]
  have key :
      (t + 2) * (5 * t ^ 3 + 19 * t ^ 2 + 13 * t + 8) * ((s + 3) * (s + 4) * (s ^ 2 + s + 1))
        - (s + 2) * (5 * s ^ 3 + 19 * s ^ 2 + 13 * s + 8) * ((t + 3) * (t + 4) * (t ^ 2 + t + 1))
      = (t - s) * (11 * s ^ 3 * t ^ 3 + 49 * s ^ 3 * t ^ 2 + 61 * s ^ 3 * t + 44 * s ^ 3
          + 49 * s ^ 2 * t ^ 3 + 233 * s ^ 2 * t ^ 2 + 323 * s ^ 2 * t + 220 * s ^ 2
          + 61 * s * t ^ 3 + 323 * s * t ^ 2 + 509 * s * t + 292 * s
          + 44 * t ^ 3 + 220 * t ^ 2 + 292 * t + 104) := by
    ring
  have hK : 0 < (t - s) * (11 * s ^ 3 * t ^ 3 + 49 * s ^ 3 * t ^ 2 + 61 * s ^ 3 * t + 44 * s ^ 3
          + 49 * s ^ 2 * t ^ 3 + 233 * s ^ 2 * t ^ 2 + 323 * s ^ 2 * t + 220 * s ^ 2
          + 61 * s * t ^ 3 + 323 * s * t ^ 2 + 509 * s * t + 292 * s
          + 44 * t ^ 3 + 220 * t ^ 2 + 292 * t + 104) := by
    apply mul_pos (by linarith)
    positivity
  linarith

/-- `F/(τ₂Δ)` on the cone over a projective plane of order `s`, where `τ₂ = (s+2)/(s+2-√s)`
and `Δ = 2`. -/
noncomputable def ratio (s : ℝ) : ℝ := V3 s / ((s + 2) / (s + 2 - Real.sqrt s) * 2)

theorem sqrt_lt_add_two (s : ℝ) (hs : 0 ≤ s) : Real.sqrt s < s + 2 := by
  nlinarith [Real.sq_sqrt hs, Real.sqrt_nonneg s, sq_nonneg (Real.sqrt s - 1 / 2)]

theorem ratio_eq (s : ℝ) (hs : 0 ≤ s) :
    ratio s = V3 s / 2 * (1 - Real.sqrt s / (s + 2)) := by
  unfold ratio
  have h1 : s + 2 - Real.sqrt s ≠ 0 := by
    have := sqrt_lt_add_two s hs
    exact ne_of_gt (by linarith)
  have h2 : s + 2 ≠ 0 := ne_of_gt (by linarith)
  field_simp

theorem sqrt_div_strictAnti {s t : ℝ} (hs : 2 ≤ s) (hst : s < t) :
    Real.sqrt t / (t + 2) < Real.sqrt s / (s + 2) := by
  have ha2 : Real.sqrt s ^ 2 = s := Real.sq_sqrt (by linarith)
  have hb2 : Real.sqrt t ^ 2 = t := Real.sq_sqrt (by linarith)
  have ha0 : 0 ≤ Real.sqrt s := Real.sqrt_nonneg s
  have hab : Real.sqrt s < Real.sqrt t := Real.sqrt_lt_sqrt (by linarith) hst
  have ha_pos : 0 < Real.sqrt s := by nlinarith
  have hprod : 2 < Real.sqrt s * Real.sqrt t := by
    nlinarith [mul_lt_mul_of_pos_left hab ha_pos]
  rw [div_lt_div_iff₀ (by linarith) (by linarith)]
  nlinarith [mul_pos (sub_pos.mpr hab) (sub_pos.mpr hprod)]

/-- The ratio is increasing in `s` for `s ≥ 2`. -/
theorem ratio_strictMonoOn : StrictMonoOn ratio (Set.Ici 2) := by
  intro s hs t ht hst
  simp only [Set.mem_Ici] at hs ht
  rw [ratio_eq s (by linarith), ratio_eq t (by linarith)]
  have hs0 : 0 < s := by linarith
  have h1 : V3 s < V3 t := V3_strictMono hs0 hst
  have h2 := sqrt_div_strictAnti hs hst
  have h3 : 0 < V3 s := by unfold V3; positivity
  have h4 : 0 < 1 - Real.sqrt s / (s + 2) := by
    have := sqrt_lt_add_two s (by linarith)
    rw [sub_pos, div_lt_one (by linarith)]
    exact this
  exact mul_lt_mul'' (by linarith) (by linarith) (by linarith) h4.le

theorem V3_37 : V3 37 = 727389 / 153832 := by unfold V3; norm_num

theorem V3_38 : V3 38 = 2015320 / 425621 := by unfold V3; norm_num

theorem V3_41 : V3 41 = 1080977 / 227436 := by unfold V3; norm_num

theorem V3_49 : V3 49 = 10786653 / 2251652 := by unfold V3; norm_num

theorem ratio_37_lt_two : ratio 37 < 2 := by
  rw [ratio_eq 37 (by norm_num), V3_37]
  have h : (601 : ℝ) / 100 < Real.sqrt 37 := by
    rw [Real.lt_sqrt (by norm_num)]
    norm_num
  have h' : Real.sqrt 37 / (37 + 2) = Real.sqrt 37 / 39 := by norm_num
  rw [h']
  linarith

theorem two_lt_ratio_38 : 2 < ratio 38 := by
  rw [ratio_eq 38 (by norm_num), V3_38]
  have h : Real.sqrt 38 < 31 / 5 := by
    rw [Real.sqrt_lt' (by norm_num)]
    norm_num
  have h' : Real.sqrt 38 / (38 + 2) = Real.sqrt 38 / 40 := by norm_num
  rw [h']
  linarith

/-- The ratio exceeds `2` exactly for the orders `s ≥ 38`. -/
theorem two_lt_ratio_iff (s : ℕ) (hs : 2 ≤ s) : 2 < ratio s ↔ 38 ≤ s := by
  constructor
  · intro h
    by_contra hlt
    have hs37n : s ≤ 37 := by omega
    have hs37 : (s : ℝ) ≤ 37 := by exact_mod_cast hs37n
    have hs2 : (2 : ℝ) ≤ s := by exact_mod_cast hs
    rcases eq_or_lt_of_le hs37 with heq | hlt'
    · rw [heq] at h
      linarith [ratio_37_lt_two]
    · have := ratio_strictMonoOn (Set.mem_Ici.mpr hs2) (Set.mem_Ici.mpr (by norm_num)) hlt'
      linarith [ratio_37_lt_two]
  · intro h
    have h38 : (38 : ℝ) ≤ s := by exact_mod_cast h
    rcases eq_or_lt_of_le h38 with heq | hlt
    · rw [← heq]
      exact two_lt_ratio_38
    · have := ratio_strictMonoOn (Set.mem_Ici.mpr (by norm_num)) (Set.mem_Ici.mpr (by linarith)) hlt
      linarith [two_lt_ratio_38]

/-! ### The constants in the bounded-degree bound -/

theorem degree_constant : 16 * Real.exp 1 / (Real.exp 1 - 1) * 2.55 < 65 := by
  have he := Real.exp_one_gt_d9
  have he' : 0 < Real.exp 1 - 1 := by linarith
  rw [div_mul_eq_mul_div, div_lt_iff₀ he']
  nlinarith

theorem log_three_gt : (1.0925 : ℝ) < Real.log 3 := by
  rw [Real.lt_log_iff_exp_lt (by norm_num)]
  have h1 : Real.exp 1.0925 = Real.exp 1 * Real.exp 0.0925 := by
    rw [← Real.exp_add]
    norm_num
  have h2 : (-0.0925 : ℝ) + 1 ≤ Real.exp (-0.0925) := Real.add_one_le_exp _
  have h3 : Real.exp 0.0925 * Real.exp (-0.0925) = 1 := by
    rw [← Real.exp_add]
    norm_num
  have h4 : 0 < Real.exp 0.0925 := Real.exp_pos _
  have h5 : Real.exp 0.0925 * 0.9075 ≤ 1 := by nlinarith
  have h6 := Real.exp_one_lt_d9
  have h7 : 0 < Real.exp 1 := Real.exp_pos _
  rw [h1]
  nlinarith

theorem log_constant : 1 + Real.log 2 < 1.55 * Real.log 3 := by
  have h1 := Real.log_two_lt_d9
  have h2 := log_three_gt
  linarith

end FlowParameter

#print axioms FlowParameter.two_lt_ratio_iff
#print axioms FlowParameter.load_eq_V3
#print axioms FlowParameter.loads_equal
#print axioms FlowParameter.V3_from_cert
#print axioms FlowParameter.theta_mem
#print axioms FlowParameter.cert_lower
#print axioms FlowParameter.r_eq_3d_bound
#print axioms FlowParameter.explicit_quantifier
#print axioms FlowParameter.degree_constant
#print axioms FlowParameter.log_constant
#print axioms FlowParameter.spectrum_quadratic
#print axioms FlowParameter.hub_load
#print axioms FlowParameter.lengths_sum
#print axioms FlowParameter.V3_49
#print axioms FlowParameter.V3_41
