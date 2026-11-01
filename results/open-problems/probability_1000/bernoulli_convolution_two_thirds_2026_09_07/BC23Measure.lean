/-
The Bernoulli convolution at lambda = 2/3, defined in Lean.

  Y = (1/3) * sum_{k >= 0} B_k (2/3)^k,   B_k fair iid bits,
  mu = law(Y)  on [0,1].
-/
import Mathlib.Probability.ProductMeasure
import Mathlib.Probability.Independence.InfinitePi
import Mathlib.Probability.Independence.Integration
import Mathlib.Probability.Distributions.Bernoulli
import Mathlib.MeasureTheory.Integral.DominatedConvergence
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle

open MeasureTheory ProbabilityTheory Measure Filter
open scoped ENNReal Topology

namespace BC23

/-- The weight of the `k`-th coin: `w k = (2/3)^k / 3`. -/
noncomputable def w (k : ℕ) : ℝ := (2 / 3 : ℝ) ^ k / 3

lemma w_nonneg (k : ℕ) : 0 ≤ w k := by
  unfold w; positivity

lemma w_succ (k : ℕ) : w (k + 1) = (2 / 3 : ℝ) * w k := by
  unfold w; ring

lemma w_zero : w 0 = 1 / 3 := by norm_num [w]

lemma summable_w : Summable w := by
  have h : Summable (fun k : ℕ => (2 / 3 : ℝ) ^ k) :=
    summable_geometric_of_lt_one (by norm_num) (by norm_num)
  exact h.div_const 3

lemma tsum_w : ∑' k, w k = 1 := by
  have h : ∑' k : ℕ, (2 / 3 : ℝ) ^ k = 3 := by
    rw [tsum_geometric_of_lt_one (by norm_num) (by norm_num)]; norm_num
  have : ∑' k, w k = (∑' k : ℕ, (2 / 3 : ℝ) ^ k) / 3 := by
    unfold w; rw [← tsum_div_const]
  rw [this, h]; norm_num

/-- The coin space. -/
abbrev Coin : Type := ℕ → Bool

/-- `1/2`, as a point of the unit interval. -/
noncomputable def half : unitInterval := ⟨1 / 2, by norm_num [unitInterval]⟩

@[simp] lemma coe_half : (half : ℝ) = 1 / 2 := rfl

/-- A single fair coin. -/
noncomputable def coin : Measure Bool := bernoulliMeasure true false half

instance : IsProbabilityMeasure coin := by unfold coin; infer_instance

/-- The coin really is fair. -/
@[simp] theorem coin_true : coin.real {true} = 1 / 2 := by simp [coin, half]

@[simp] theorem coin_false : coin.real {false} = 1 / 2 := by
  simp [coin, half]; norm_num

/-- The fair coin-tossing measure on `Coin`. -/
noncomputable def P : Measure Coin := Measure.infinitePi (fun _ : ℕ => coin)

instance : IsProbabilityMeasure P := by unfold P; infer_instance

/-- The contribution of the `k`-th coin. -/
noncomputable def term (k : ℕ) (x : Bool) : ℝ := if x then w k else 0

lemma term_nonneg (k : ℕ) (x : Bool) : 0 ≤ term k x := by
  unfold term; split
  · exact w_nonneg k
  · exact le_rfl

lemma term_le (k : ℕ) (x : Bool) : term k x ≤ w k := by
  unfold term; split
  · exact le_rfl
  · exact w_nonneg k

lemma measurable_term (k : ℕ) : Measurable (term k) := by
  exact Measurable.of_discrete

/-- The partial sums. -/
noncomputable def Fpart (n : ℕ) (b : Coin) : ℝ := ∑ k ∈ Finset.range n, term k (b k)

/-- `Y`: the a.e.-convergent (indeed everywhere convergent) series. -/
noncomputable def Y (b : Coin) : ℝ := ∑' k, term k (b k)

lemma summable_Y (b : Coin) : Summable (fun k => term k (b k)) :=
  summable_w.of_nonneg_of_le (fun k => term_nonneg k (b k)) (fun k => term_le k (b k))

lemma tendsto_Fpart (b : Coin) : Tendsto (fun n => Fpart n b) atTop (𝓝 (Y b)) :=
  (summable_Y b).hasSum.tendsto_sum_nat

lemma Y_nonneg (b : Coin) : 0 ≤ Y b :=
  tsum_nonneg (fun k => term_nonneg k (b k))

lemma Y_le_one (b : Coin) : Y b ≤ 1 := by
  rw [← tsum_w]
  exact (summable_Y b).tsum_le_tsum (fun k => term_le k (b k)) summable_w

lemma measurable_Fpart (n : ℕ) : Measurable (Fpart n) := by
  unfold Fpart
  exact Finset.measurable_sum _ (fun k _ => (measurable_term k).comp (measurable_pi_apply k))

lemma measurable_Y : Measurable Y :=
  measurable_of_tendsto_metrizable measurable_Fpart
    (tendsto_pi_nhds.2 (fun b => tendsto_Fpart b))

/-- **The Bernoulli convolution at `lambda = 2/3`**, as a measure on `ℝ`. -/
noncomputable def mu : Measure ℝ := P.map Y

instance : IsProbabilityMeasure mu := by
  unfold mu; exact isProbabilityMeasure_map measurable_Y.aemeasurable

theorem mu_Icc : mu (Set.Icc (0 : ℝ) 1) = 1 := by
  unfold mu
  rw [Measure.map_apply measurable_Y measurableSet_Icc]
  have : Y ⁻¹' Set.Icc (0 : ℝ) 1 = Set.univ := by
    ext b; simp [Y_nonneg b, Y_le_one b]
  rw [this, measure_univ]

/-! ### The Fourier transform -/

/-- `e t = exp (i t)`. -/
noncomputable def e (t : ℝ) : ℂ := Complex.exp ((t : ℂ) * Complex.I)

@[simp] lemma norm_e (t : ℝ) : ‖e t‖ = 1 := Complex.norm_exp_ofReal_mul_I t

@[simp] lemma e_zero : e 0 = 1 := by simp [e]

lemma continuous_e : Continuous e := by
  unfold e; fun_prop

lemma e_finset_sum (s : Finset ℕ) (f : ℕ → ℝ) :
    ∏ k ∈ s, e (f k) = e (∑ k ∈ s, f k) := by
  unfold e
  rw [← Complex.exp_sum]
  congr 1
  push_cast
  rw [Finset.sum_mul]

/-- The Fourier coefficient, in the convention of the paper:
`muhat (xi) = int exp (- 2 pi i xi x) dmu (x)`. -/
noncomputable def muHat (ξ : ℝ) : ℂ := ∫ x, e (-(2 * Real.pi * ξ * x)) ∂mu

lemma muHat_eq_integral_P (ξ : ℝ) :
    muHat ξ = ∫ b, e (-(2 * Real.pi * ξ * Y b)) ∂P := by
  unfold muHat mu
  rw [integral_map measurable_Y.aemeasurable]
  exact (continuous_e.comp (by fun_prop)).aestronglyMeasurable

/-- The `n`-th partial product. -/
noncomputable def Q (ξ : ℝ) (n : ℕ) : ℂ :=
  ∏ k ∈ Finset.range n, (1 + e (-(2 * Real.pi * ξ * w k))) / 2

/-- The integrand at coordinate `k`. -/
noncomputable def g (ξ : ℝ) (k : ℕ) (x : Bool) : ℂ := e (-(2 * Real.pi * ξ * term k x))

lemma measurable_g (ξ : ℝ) (k : ℕ) : Measurable (g ξ k) := Measurable.of_discrete

lemma indep_g (ξ : ℝ) : iIndepFun (fun (k : ℕ) (b : Coin) => g ξ k (b k)) P :=
  iIndepFun_infinitePi (fun k => measurable_g ξ k)

/-- One coordinate: the integral of `g` against the coin-tossing measure. -/
lemma integral_g (ξ : ℝ) (k : ℕ) :
    ∫ b, g ξ k (b k) ∂P = (1 + e (-(2 * Real.pi * ξ * w k))) / 2 := by
  have hmap : P.map (fun b : Coin => b k) = coin := Measure.infinitePi_map_eval _ k
  have h1 : ∫ b, g ξ k (b k) ∂P = ∫ x, g ξ k x ∂coin := by
    rw [← hmap, integral_map (measurable_pi_apply k).aemeasurable
      (measurable_g ξ k).aestronglyMeasurable]
  rw [h1, coin, integral_bernoulliMeasure]
  simp only [g, term, if_pos, Complex.real_smul]
  norm_num [w_nonneg k, coe_half]
  ring

/-- The finite-level integral is the finite product. -/
lemma integral_e_Fpart (ξ : ℝ) (n : ℕ) :
    ∫ b, e (-(2 * Real.pi * ξ * Fpart n b)) ∂P = Q ξ n := by
  have hrw : ∀ b : Coin,
      e (-(2 * Real.pi * ξ * Fpart n b)) = ∏ i : Fin n, g ξ (i : ℕ) (b (i : ℕ)) := by
    intro b
    rw [Fin.prod_univ_eq_prod_range (fun k => g ξ k (b k)) n]
    unfold g
    rw [e_finset_sum]
    congr 1
    unfold Fpart
    rw [Finset.mul_sum, ← Finset.sum_neg_distrib]
  simp_rw [hrw]
  have hind : iIndepFun (fun (i : Fin n) (b : Coin) => g ξ (i : ℕ) (b (i : ℕ))) P :=
    (indep_g ξ).precomp (g := (Fin.val : Fin n → ℕ)) Fin.val_injective
  rw [hind.integral_fun_prod_eq_prod_integral
      (fun i => ((measurable_g ξ i).comp (measurable_pi_apply _)).aestronglyMeasurable)]
  rw [Fin.prod_univ_eq_prod_range (fun k => ∫ b, g ξ k (b k) ∂P) n]
  unfold Q
  exact Finset.prod_congr rfl (fun k _ => integral_g ξ k)

/-! ### Passing to the limit -/

/-- The Fourier coefficient is the limit of the partial products. -/
theorem tendsto_Q (ξ : ℝ) : Tendsto (Q ξ) atTop (𝓝 (muHat ξ)) := by
  have key : Tendsto (fun n => ∫ b, e (-(2 * Real.pi * ξ * Fpart n b)) ∂P) atTop
      (𝓝 (∫ b, e (-(2 * Real.pi * ξ * Y b)) ∂P)) := by
    refine tendsto_integral_of_dominated_convergence (fun _ => (1 : ℝ))
      (fun n => (continuous_e.comp (by fun_prop : Continuous fun t : ℝ =>
        -(2 * Real.pi * ξ * t))).comp_aestronglyMeasurable
        (measurable_Fpart n).aestronglyMeasurable)
      (integrable_const 1) (fun n => .of_forall fun b => by simp)
      (.of_forall fun b => ?_)
    exact (continuous_e.tendsto _).comp
      (((tendsto_const_nhds.mul (tendsto_Fpart b)).neg :
        Tendsto (fun n => -(2 * Real.pi * ξ * Fpart n b)) atTop (𝓝 (-(2 * Real.pi * ξ * Y b)))))
  simp_rw [integral_e_Fpart] at key
  rwa [← muHat_eq_integral_P] at key

/-! ### Self-similarity -/

/-- Half-angle: `(1 + e^{-2 i t}) / 2 = e^{-i t} cos t`. -/
lemma half_one_add_e (t : ℝ) : (1 + e (-(2 * t))) / 2 = e (-t) * (Real.cos t : ℂ) := by
  rw [Complex.ofReal_cos]
  unfold e
  rw [← mul_right_inj' (two_ne_zero' ℂ), mul_div_cancel₀ _ (two_ne_zero' ℂ), ← mul_assoc,
    mul_comm (2 : ℂ), mul_assoc, Complex.two_cos, mul_add, ← Complex.exp_add, ← Complex.exp_add]
  push_cast
  ring_nf
  rw [Complex.exp_zero]
  ring


lemma Q_succ (ξ : ℝ) (n : ℕ) :
    Q ξ (n + 1) = ((1 + e (-(2 * Real.pi * ξ * w 0))) / 2) * Q (2 * ξ / 3) n := by
  unfold Q
  rw [Finset.prod_range_succ']
  rw [mul_comm]
  congr 1
  refine Finset.prod_congr rfl (fun k _ => ?_)
  congr 2
  rw [w_succ]
  ring

/-- **Self-similarity of the Fourier transform** (exponential form).
`muhat (xi) = ((1 + e^{-2 pi i xi / 3}) / 2) * muhat (2 xi / 3)`. -/
theorem muHat_selfSimilar (ξ : ℝ) :
    muHat ξ = ((1 + e (-(2 * Real.pi * ξ / 3))) / 2) * muHat (2 * ξ / 3) := by
  have h1 : Tendsto (fun n => Q ξ (n + 1)) atTop (𝓝 (muHat ξ)) :=
    (tendsto_Q ξ).comp (tendsto_add_atTop_nat 1)
  have h2 : Tendsto (fun n => Q ξ (n + 1)) atTop
      (𝓝 (((1 + e (-(2 * Real.pi * ξ * w 0))) / 2) * muHat (2 * ξ / 3))) := by
    simp_rw [Q_succ]
    exact (tendsto_Q (2 * ξ / 3)).const_mul _
  have heq := tendsto_nhds_unique h1 h2
  rw [heq, show -(2 * Real.pi * ξ * w 0) = -(2 * Real.pi * ξ / 3) by rw [w_zero]; ring]

/-- **Self-similarity, cosine form**:
`muhat (xi) = e^{-i pi xi / 3} cos (pi xi / 3) * muhat (2 xi / 3)`.
The phase `e^{-i pi xi / 3}` is present because `mu` lives on `[0,1]` and is not centred;
the bare cosine identity holds for the centred measure. -/
theorem muHat_selfSimilar_cos (ξ : ℝ) :
    muHat ξ = e (-(Real.pi * ξ / 3)) * (Real.cos (Real.pi * ξ / 3) : ℂ) * muHat (2 * ξ / 3) := by
  rw [muHat_selfSimilar ξ]
  congr 1
  rw [show -(2 * Real.pi * ξ / 3) = -(2 * (Real.pi * ξ / 3)) by ring, half_one_add_e]

/-! ### The functional equation -/

/-- **The functional equation** `muhat (3 m) = muhat (2 m)` for every integer `m`. -/
theorem muHat_functional_eq (m : ℤ) : muHat (3 * m) = muHat (2 * m) := by
  have h := muHat_selfSimilar (3 * m)
  have hphase : e (-(2 * Real.pi * (3 * (m : ℝ)) / 3)) = 1 := by
    unfold e
    have : ((-(2 * Real.pi * (3 * (m : ℝ))) / 3 : ℝ) : ℂ) * Complex.I
        = (-m : ℤ) * (2 * (Real.pi : ℂ) * Complex.I) := by
      push_cast; ring
    rw [show (-(2 * Real.pi * (3 * (m : ℝ))) / 3 : ℝ) = -(2 * Real.pi * (3 * (m : ℝ)) / 3) by ring]
      at this
    rw [this, Complex.exp_int_mul_two_pi_mul_I]
  have harg : 2 * (3 * (m : ℝ)) / 3 = 2 * m := by ring
  rw [hphase, harg] at h
  simpa using h

/-! ### The cosine product (target (a), with its phase) -/

lemma tendsto_partial_w : Tendsto (fun n => ∑ k ∈ Finset.range n, w k) atTop (𝓝 1) := by
  have := summable_w.hasSum.tendsto_sum_nat
  rwa [tsum_w] at this

/-- The partial product `Q` split into a pure phase and a real cosine product. -/
lemma Q_eq_phase_mul_cos (ξ : ℝ) (n : ℕ) :
    Q ξ n = e (-(Real.pi * ξ * ∑ k ∈ Finset.range n, w k)) *
      ((∏ k ∈ Finset.range n, Real.cos (Real.pi * ξ * w k) : ℝ) : ℂ) := by
  unfold Q
  have h1 : ∀ k ∈ Finset.range n, (1 + e (-(2 * Real.pi * ξ * w k))) / 2
      = e (-(Real.pi * ξ * w k)) * (Real.cos (Real.pi * ξ * w k) : ℂ) := by
    intro k _
    rw [show -(2 * Real.pi * ξ * w k) = -(2 * (Real.pi * ξ * w k)) by ring, half_one_add_e]
  rw [Finset.prod_congr rfl h1, Finset.prod_mul_distrib, e_finset_sum]
  push_cast
  congr 2
  rw [Finset.mul_sum, ← Finset.sum_neg_distrib]

/-- **Target (a).**  The infinite cosine product of the paper converges, and its limit is
`e^{i pi xi} muhat (xi)`; equivalently
`muhat (xi) = e^{-i pi xi} * prod_{k >= 0} cos (pi xi (2/3)^k / 3)`.
The phase `e^{-i pi xi}` is exactly the mean `1/2` of `mu`: the bare product is the Fourier
transform of the centred measure. -/
theorem tendsto_cos_prod (ξ : ℝ) :
    Tendsto (fun n => ((∏ k ∈ Finset.range n, Real.cos (Real.pi * ξ * w k) : ℝ) : ℂ)) atTop
      (𝓝 (e (Real.pi * ξ) * muHat ξ)) := by
  have hphase : Tendsto (fun n => e (Real.pi * ξ * ∑ k ∈ Finset.range n, w k)) atTop
      (𝓝 (e (Real.pi * ξ))) := by
    have h := (continuous_e.tendsto (Real.pi * ξ * 1)).comp
      ((tendsto_const_nhds (x := Real.pi * ξ)).mul tendsto_partial_w)
    simpa [Function.comp_def] using h
  have key : Tendsto
      (fun n => e (Real.pi * ξ * ∑ k ∈ Finset.range n, w k) * Q ξ n) atTop
      (𝓝 (e (Real.pi * ξ) * muHat ξ)) := hphase.mul (tendsto_Q ξ)
  refine key.congr (fun n => ?_)
  rw [Q_eq_phase_mul_cos, ← mul_assoc]
  have : e (Real.pi * ξ * ∑ k ∈ Finset.range n, w k) *
      e (-(Real.pi * ξ * ∑ k ∈ Finset.range n, w k)) = 1 := by
    unfold e
    rw [← Complex.exp_add]
    push_cast
    ring_nf
    exact Complex.exp_zero
  rw [this, one_mul]

/-- The modulus of the Fourier coefficient is the infinite product of `|cos|`.
This is the identity `|hat mu (k)|^2 = prod_{i >= 0} cos^2 (pi k 2^i / 3^(i+1))` of the paper
(note `pi * k * w i = pi * k * 2^i / 3^(i+1)`), stated as a convergence. -/
theorem tendsto_abs_cos_prod (ξ : ℝ) :
    Tendsto (fun n => |∏ k ∈ Finset.range n, Real.cos (Real.pi * ξ * w k)|) atTop
      (𝓝 ‖muHat ξ‖) := by
  have h := (tendsto_cos_prod ξ).norm
  rw [norm_mul, norm_e, one_mul] at h
  simp only [Complex.norm_real, Real.norm_eq_abs] at h
  exact h

lemma pi_mul_w (ξ : ℝ) (k : ℕ) : Real.pi * ξ * w k = Real.pi * ξ * 2 ^ k / 3 ^ (k + 1) := by
  unfold w
  rw [div_pow]
  field_simp
  ring


/-! ### Sanity checks -/

@[simp] theorem muHat_zero : muHat 0 = 1 := by
  have := tendsto_Q 0
  have hQ : ∀ n, Q 0 n = 1 := by
    intro n
    unfold Q
    norm_num
  rw [funext hQ] at this
  exact tendsto_nhds_unique this tendsto_const_nhds

theorem norm_muHat_le_one (ξ : ℝ) : ‖muHat ξ‖ ≤ 1 := by
  rw [muHat_eq_integral_P]
  calc ‖∫ b, e (-(2 * Real.pi * ξ * Y b)) ∂P‖
      ≤ ∫ b, ‖e (-(2 * Real.pi * ξ * Y b))‖ ∂P := norm_integral_le_integral_norm _
    _ = 1 := by simp

end BC23

#print axioms BC23.coin_true
#print axioms BC23.coin_false
#print axioms BC23.mu
#print axioms BC23.mu_Icc
#print axioms BC23.integral_e_Fpart
#print axioms BC23.tendsto_Q
#print axioms BC23.tendsto_cos_prod
#print axioms BC23.muHat_selfSimilar
#print axioms BC23.muHat_selfSimilar_cos
#print axioms BC23.muHat_functional_eq
#print axioms BC23.tendsto_abs_cos_prod
#print axioms BC23.pi_mul_w
#print axioms BC23.muHat_zero
#print axioms BC23.norm_muHat_le_one

#check @BC23.mu
#check @BC23.mu_Icc
#check @BC23.muHat
#check @BC23.integral_e_Fpart
#check @BC23.tendsto_Q
#check @BC23.tendsto_cos_prod
#check @BC23.tendsto_abs_cos_prod
#check @BC23.muHat_selfSimilar
#check @BC23.muHat_selfSimilar_cos
#check @BC23.muHat_functional_eq
#check @BC23.muHat_zero
#check @BC23.norm_muHat_le_one
