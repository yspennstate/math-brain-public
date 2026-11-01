import Mathlib.Analysis.Matrix.Spectrum
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.Convex.SpecificFunctions.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Data.Real.StarOrdered
import Mathlib.MeasureTheory.Function.Jacobian
import Mathlib.Analysis.Calculus.BumpFunction.Convolution
import Mathlib.Analysis.Calculus.BumpFunction.FiniteDimension
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.Topology.Order.MonotoneContinuity
import Mathlib.Analysis.Calculus.Deriv.Inverse
import Mathlib.MeasureTheory.Integral.Pi
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Analysis.Calculus.FDeriv.Pi
import Mathlib.Analysis.SpecialFunctions.Pow.Continuity
import Mathlib.MeasureTheory.Integral.Bochner.VitaliCaratheodory
import Mathlib.Tactic
import Mathlib.MeasureTheory.Measure.Haar.InnerProductSpace
import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.MeasureTheory.Measure.Decomposition.RadonNikodym
import Mathlib.Analysis.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.MeasureTheory.Measure.Haar.OfBasis

/-!
# Theorem 3.1 (the geometric Brascamp-Lieb inequality) and Lemma 3.2

For unit vectors `u_1, ..., u_N` in `ℝ^d` and `c_i > 0` with `∑ c_i u_i u_iᵀ = I`, and nonnegative
integrable `h_i`,
`∫ ∏ h_i(u_i · x)^{c_i} dx ≤ ∏ (∫ h_i)^{c_i}`.

The proof is Barthe's transport argument. For continuous positive integrable `h_i` let `T_i` be the
increasing map carrying `h_i(t) dt / ∫ h_i` to the Gaussian `γ(t) = exp(-π t²)`, and
`Φ(x) = ∑ c_i T_i(u_i · x) u_i`. Then `h_i = (∫ h_i) T_i' γ(T_i)`, Ball's determinant inequality gives
`det DΦ ≥ ∏ (T_i')^{c_i}`, the frame identity gives `∏ γ(T_i)^{c_i} ≤ γ_d(Φ)`, `Φ` is injective, and
the change of variables formula bounds the integral by `∏ (∫ h_i)^{c_i} ∫ γ_d = ∏ (∫ h_i)^{c_i}`.
General `h_i` follow by smoothing lower semicontinuous majorants (Vitali-Carathéodory) and Fatou's lemma,
then truncation and monotone convergence. No step pulls a null set of `ℝ` back along `x ↦ u_i · x`.
-/

open Matrix
open scoped BigOperators

namespace QformFiveB

namespace Ball

section Spectral

variable {n : Type*} [Fintype n] [DecidableEq n]

theorem real_star_eq_transpose (M : Matrix n n ℝ) : star M = Mᵀ := by
  rw [Matrix.star_eq_conjTranspose, Matrix.conjTranspose_eq_transpose_of_trivial]

theorem eigU_orth (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    (hA.eigenvectorUnitary : Matrix n n ℝ)ᵀ * (hA.eigenvectorUnitary : Matrix n n ℝ) = 1 := by
  have h := Unitary.coe_star_mul_self hA.eigenvectorUnitary
  rw [real_star_eq_transpose] at h
  exact h

theorem eigU_orth' (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    (hA.eigenvectorUnitary : Matrix n n ℝ) * (hA.eigenvectorUnitary : Matrix n n ℝ)ᵀ = 1 := by
  have h := Unitary.coe_mul_star_self hA.eigenvectorUnitary
  rw [Unitary.coe_star, real_star_eq_transpose] at h
  exact h

theorem eigU_eigen (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    A * (hA.eigenvectorUnitary : Matrix n n ℝ)
      = (hA.eigenvectorUnitary : Matrix n n ℝ) * diagonal hA.eigenvalues := by
  ext i j
  have h := congrFun (hA.mulVec_eigenvectorBasis j) i
  simp only [Matrix.mulVec, dotProduct, Pi.smul_apply, smul_eq_mul] at h
  rw [Matrix.mul_diagonal, Matrix.mul_apply]
  simp only [IsHermitian.eigenvectorUnitary_apply]
  rw [h, mul_comm]

end Spectral

/-- The diagonal entries of `A diag(w) Aᵀ`. -/
theorem diag_conj_apply {κ ι : Type*} [Fintype ι] [DecidableEq ι] (A : Matrix κ ι ℝ) (w : ι → ℝ) (k : κ) :
    (A * diagonal w * Aᵀ) k k = ∑ i, w i * A k i ^ 2 := by
  rw [Matrix.mul_apply]
  apply Finset.sum_congr rfl
  intro i _
  rw [Matrix.mul_diagonal, Matrix.transpose_apply]
  ring

/-- The diagonal entries of `Aᵀ A`. -/
theorem gram_diag_apply {κ ι : Type*} [Fintype κ] (A : Matrix κ ι ℝ) (i : ι) :
    (Aᵀ * A) i i = ∑ k, A k i ^ 2 := by
  rw [Matrix.mul_apply]
  apply Finset.sum_congr rfl
  intro k _
  rw [Matrix.transpose_apply]
  ring

/-- **Ball's determinant inequality, in logarithmic form.** For `V ∈ ℝ^{κ×ι}` with unit columns (`(VᵀV)_{ii} = 1`) and
`c_i > 0` with `V diag(c) Vᵀ = I`, and `λ_i > 0`: `det(V diag(cλ) Vᵀ) > 0` and
`∑ c_i log λ_i ≤ log det(V diag(cλ) Vᵀ)`. -/
theorem ball_det_log {ι κ : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ] [Nonempty κ]
    (V : Matrix κ ι ℝ) (c l : ι → ℝ) (hc : ∀ i, 0 < c i) (hl : ∀ i, 0 < l i)
    (hframe : V * diagonal c * Vᵀ = 1) (hunit : ∀ i, (Vᵀ * V) i i = 1) :
    0 < (V * diagonal (fun i => c i * l i) * Vᵀ).det
      ∧ ∑ i, c i * Real.log (l i) ≤ Real.log (V * diagonal (fun i => c i * l i) * Vᵀ).det := by
  set M := V * diagonal (fun i => c i * l i) * Vᵀ with hMdef
  have hM : M.IsHermitian := by
    show Mᴴ = M
    rw [Matrix.conjTranspose_eq_transpose_of_trivial, hMdef, Matrix.transpose_mul, Matrix.transpose_mul,
      Matrix.transpose_transpose, Matrix.diagonal_transpose, Matrix.mul_assoc]
  set U : Matrix κ κ ℝ := (hM.eigenvectorUnitary : Matrix κ κ ℝ) with hU
  set μ := hM.eigenvalues with hμ
  set a : Matrix κ ι ℝ := Uᵀ * V with ha
  -- the three identities
  have hi : ∀ i, ∑ k, a k i ^ 2 = 1 := by
    intro i
    rw [← gram_diag_apply, ha, Matrix.transpose_mul, Matrix.transpose_transpose,
      show Vᵀ * U * (Uᵀ * V) = Vᵀ * (U * Uᵀ) * V by simp only [Matrix.mul_assoc], hU, eigU_orth' M hM,
      Matrix.mul_one]
    exact hunit i
  have hii : ∀ k, ∑ i, c i * a k i ^ 2 = 1 := by
    intro k
    rw [← diag_conj_apply, ha, Matrix.transpose_mul, Matrix.transpose_transpose,
      show Uᵀ * V * diagonal c * (Vᵀ * U) = Uᵀ * (V * diagonal c * Vᵀ) * U by simp only [Matrix.mul_assoc],
      hframe, Matrix.mul_one, hU, eigU_orth M hM, Matrix.one_apply_eq]
  have hiii : ∀ k, ∑ i, (c i * l i) * a k i ^ 2 = μ k := by
    intro k
    have hdiag : Uᵀ * M * U = diagonal μ := by
      rw [Matrix.mul_assoc, hU, eigU_eigen M hM, ← Matrix.mul_assoc, eigU_orth M hM, Matrix.one_mul]
    have h1 : (Uᵀ * M * U) k k = μ k := by rw [hdiag, Matrix.diagonal_apply_eq]
    rw [← h1, ← diag_conj_apply, ha, Matrix.transpose_mul, Matrix.transpose_transpose, hMdef]
    simp only [Matrix.mul_assoc]
  -- positivity of the eigenvalues
  have hμpos : ∀ k, 0 < μ k := by
    intro k
    rw [← hiii k]
    obtain ⟨i, -, hi0⟩ : ∃ i ∈ (Finset.univ : Finset ι), (0 : ℝ) < c i * a k i ^ 2 := by
      apply Finset.exists_lt_of_sum_lt
      rw [Finset.sum_const_zero, hii k]
      exact one_pos
    apply Finset.sum_pos' (fun j _ => by have := hc j; have := hl j; positivity)
    refine ⟨i, Finset.mem_univ _, ?_⟩
    have : c i * l i * a k i ^ 2 = l i * (c i * a k i ^ 2) := by ring
    rw [this]
    exact mul_pos (hl i) hi0
  -- the determinant
  have hdet : M.det = ∏ k, μ k := by
    have h := hM.det_eq_prod_eigenvalues
    rw [h]
    simp [hμ]
  have hlogdet : Real.log M.det = ∑ k, Real.log (μ k) := by
    rw [hdet, Real.log_prod]
    intro k _
    exact (hμpos k).ne'
  -- s_i
  set s : ι → ℝ := fun i => ∑ k, a k i ^ 2 * (μ k)⁻¹ with hs
  have hspos : ∀ i, 0 < s i := by
    intro i
    obtain ⟨k, -, hk⟩ : ∃ k ∈ (Finset.univ : Finset κ), (0 : ℝ) < a k i ^ 2 := by
      apply Finset.exists_lt_of_sum_lt
      rw [Finset.sum_const_zero, hi i]
      exact one_pos
    apply Finset.sum_pos' (fun j _ => by have := hμpos j; positivity)
    exact ⟨k, Finset.mem_univ _, mul_pos hk (inv_pos.2 (hμpos k))⟩
  -- Step 1: ∑_k a_{ki}² log μ_k ≥ -log s_i
  have step1 : ∀ i, -Real.log (s i) ≤ ∑ k, a k i ^ 2 * Real.log (μ k) := by
    intro i
    have hJ := (strictConcaveOn_log_Ioi.concaveOn).le_map_sum (t := Finset.univ) (w := fun k => a k i ^ 2)
      (p := fun k => (μ k)⁻¹) (fun k _ => sq_nonneg _) (hi i) (fun k _ => Set.mem_Ioi.2 (inv_pos.2 (hμpos k)))
    simp only [smul_eq_mul, Real.log_inv] at hJ
    have e : ∑ k, a k i ^ 2 * -Real.log (μ k) = -∑ k, a k i ^ 2 * Real.log (μ k) := by
      rw [← Finset.sum_neg_distrib]
      apply Finset.sum_congr rfl
      intro k _
      ring
    rw [e] at hJ
    linarith
  -- Step 2: log det M ≥ -∑ c_i log s_i
  have step2 : -∑ i, c i * Real.log (s i) ≤ Real.log M.det := by
    rw [hlogdet]
    have e : ∑ k, Real.log (μ k) = ∑ i, c i * ∑ k, a k i ^ 2 * Real.log (μ k) := by
      calc ∑ k, Real.log (μ k) = ∑ k, (∑ i, c i * a k i ^ 2) * Real.log (μ k) := by
            apply Finset.sum_congr rfl
            intro k _
            rw [hii k, one_mul]
        _ = ∑ i, c i * ∑ k, a k i ^ 2 * Real.log (μ k) := by
            simp only [Finset.sum_mul, Finset.mul_sum]
            rw [Finset.sum_comm]
            apply Finset.sum_congr rfl
            intro i _
            apply Finset.sum_congr rfl
            intro k _
            ring
    rw [e, ← Finset.sum_neg_distrib]
    apply Finset.sum_le_sum
    intro i _
    have h := mul_le_mul_of_nonneg_left (step1 i) (hc i).le
    linarith
  -- ∑ c_i = d
  have hcsum : ∑ i, c i = (Fintype.card κ : ℝ) := by
    calc ∑ i, c i = ∑ i, c i * ∑ k, a k i ^ 2 := by
          apply Finset.sum_congr rfl
          intro i _
          rw [hi i, mul_one]
      _ = ∑ k, ∑ i, c i * a k i ^ 2 := by
          simp only [Finset.mul_sum]
          rw [Finset.sum_comm]
      _ = ∑ _k : κ, (1 : ℝ) := by
          apply Finset.sum_congr rfl
          intro k _
          exact hii k
      _ = (Fintype.card κ : ℝ) := by
          rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one]
  have hd : (0 : ℝ) < Fintype.card κ := by exact_mod_cast Fintype.card_pos
  -- ∑ c_i λ_i s_i = d
  have hsum_ls : ∑ i, c i * l i * s i = (Fintype.card κ : ℝ) := by
    calc ∑ i, c i * l i * s i = ∑ k, (∑ i, (c i * l i) * a k i ^ 2) * (μ k)⁻¹ := by
          simp only [hs, Finset.mul_sum, Finset.sum_mul]
          rw [Finset.sum_comm]
          apply Finset.sum_congr rfl
          intro k _
          apply Finset.sum_congr rfl
          intro i _
          ring
      _ = ∑ _k : κ, (1 : ℝ) := by
          apply Finset.sum_congr rfl
          intro k _
          rw [hiii k, mul_inv_cancel₀ (hμpos k).ne']
      _ = (Fintype.card κ : ℝ) := by
          rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one]
  -- Step 3: ∑ c_i log(λ_i s_i) ≤ 0
  have step3 : ∑ i, c i * Real.log (l i * s i) ≤ 0 := by
    have hJ := (strictConcaveOn_log_Ioi.concaveOn).le_map_sum (t := Finset.univ)
      (w := fun i => c i / (Fintype.card κ : ℝ)) (p := fun i => l i * s i)
      (fun i _ => div_nonneg (hc i).le hd.le)
      (by rw [← Finset.sum_div, hcsum, div_self hd.ne'])
      (fun i _ => Set.mem_Ioi.2 (mul_pos (hl i) (hspos i)))
    simp only [smul_eq_mul] at hJ
    have e : ∑ i, c i / (Fintype.card κ : ℝ) * (l i * s i) = 1 := by
      rw [show ∑ i, c i / (Fintype.card κ : ℝ) * (l i * s i) = (∑ i, c i * l i * s i) / (Fintype.card κ : ℝ) by
        rw [Finset.sum_div]
        apply Finset.sum_congr rfl
        intro i _
        ring]
      rw [hsum_ls, div_self hd.ne']
    rw [e, Real.log_one] at hJ
    have e2 : ∑ i, c i / (Fintype.card κ : ℝ) * Real.log (l i * s i)
        = (∑ i, c i * Real.log (l i * s i)) / (Fintype.card κ : ℝ) := by
      rw [Finset.sum_div]
      apply Finset.sum_congr rfl
      intro i _
      ring
    rw [e2] at hJ
    exact (div_nonpos_iff.1 hJ).elim (fun h => by linarith [h.1, h.2]) (fun h => h.1)
  -- Step 4
  have e4 : ∑ i, c i * Real.log (l i) = ∑ i, c i * Real.log (l i * s i) - ∑ i, c i * Real.log (s i) := by
    rw [← Finset.sum_sub_distrib]
    apply Finset.sum_congr rfl
    intro i _
    rw [Real.log_mul (hl i).ne' (hspos i).ne']
    ring
  refine ⟨?_, ?_⟩
  · rw [hdet]
    exact Finset.prod_pos (fun k _ => hμpos k)
  · rw [e4]
    linarith

/-- **Ball's determinant inequality.** `∏ λ_i^{c_i} ≤ det(V diag(cλ) Vᵀ)`. -/
theorem ball_det {ι κ : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ] [Nonempty κ]
    (V : Matrix κ ι ℝ) (c l : ι → ℝ) (hc : ∀ i, 0 < c i) (hl : ∀ i, 0 < l i)
    (hframe : V * diagonal c * Vᵀ = 1) (hunit : ∀ i, (Vᵀ * V) i i = 1) :
    ∏ i, l i ^ c i ≤ (V * diagonal (fun i => c i * l i) * Vᵀ).det := by
  obtain ⟨hpos, h⟩ := ball_det_log V c l hc hl hframe hunit
  have e : ∏ i, l i ^ c i = Real.exp (∑ i, c i * Real.log (l i)) := by
    rw [Real.exp_sum]
    apply Finset.prod_congr rfl
    intro i _
    rw [Real.rpow_def_of_pos (hl i), mul_comm]
  rw [e, ← Real.exp_log hpos]
  exact Real.exp_le_exp.2 h

end Ball

open MeasureTheory Set Filter Topology
open scoped ENNReal

namespace BL

/-! ### The Gaussian and one-dimensional transport -/

/-- The Gaussian with integral one. -/
noncomputable def gam (t : ℝ) : ℝ := Real.exp (-Real.pi * t ^ 2)

theorem gam_pos (t : ℝ) : 0 < gam t := Real.exp_pos _

theorem continuous_gam : Continuous gam := by
  unfold gam; fun_prop

theorem integrable_gam : Integrable gam := by
  unfold gam
  exact integrable_exp_neg_mul_sq Real.pi_pos

theorem integral_gam : ∫ t, gam t = 1 := by
  unfold gam
  rw [integral_gaussian, div_self Real.pi_ne_zero, Real.sqrt_one]

/-- The distribution function of an integrable function. -/
noncomputable def cdf (f : ℝ → ℝ) (s : ℝ) : ℝ := ∫ t in Iic s, f t

theorem cdf_sub (f : ℝ → ℝ) (hf : Integrable f) (a b : ℝ) :
    cdf f b - cdf f a = ∫ t in a..b, f t := by
  unfold cdf
  exact intervalIntegral.integral_Iic_sub_Iic hf.integrableOn hf.integrableOn

theorem cdf_hasDerivAt (f : ℝ → ℝ) (hf : Integrable f) (hc : Continuous f) (s : ℝ) :
    HasDerivAt (cdf f) (f s) s := by
  have e : cdf f = fun u => cdf f 0 + ∫ t in (0:ℝ)..u, f t := by
    funext u
    have := cdf_sub f hf 0 u
    linarith
  rw [e]
  exact ((hc.integral_hasStrictDerivAt 0 s).hasDerivAt).const_add _

theorem cdf_continuous (f : ℝ → ℝ) (hf : Integrable f) (hc : Continuous f) : Continuous (cdf f) :=
  continuous_iff_continuousAt.2 fun s => (cdf_hasDerivAt f hf hc s).continuousAt

theorem cdf_strictMono (f : ℝ → ℝ) (hf : Integrable f) (hc : Continuous f) (hp : ∀ t, 0 < f t) :
    StrictMono (cdf f) := by
  intro a b hab
  have h1 := cdf_sub f hf a b
  have h2 : 0 < ∫ t in a..b, f t :=
    intervalIntegral.intervalIntegral_pos_of_pos_on (hc.intervalIntegrable a b) (fun x _ => hp x) hab
  linarith

theorem cdf_nonneg (f : ℝ → ℝ) (h0 : ∀ t, 0 ≤ f t) (s : ℝ) : 0 ≤ cdf f s :=
  setIntegral_nonneg measurableSet_Iic (fun t _ => h0 t)

theorem cdf_pos (f : ℝ → ℝ) (hf : Integrable f) (hc : Continuous f) (hp : ∀ t, 0 < f t) (s : ℝ) :
    0 < cdf f s := by
  have h1 := cdf_strictMono f hf hc hp (show s - 1 < s by linarith)
  have h2 := cdf_nonneg f (fun t => (hp t).le) (s - 1)
  linarith

theorem cdf_le_integral (f : ℝ → ℝ) (hf : Integrable f) (h0 : ∀ t, 0 ≤ f t) (s : ℝ) :
    cdf f s ≤ ∫ t, f t :=
  setIntegral_le_integral hf (Eventually.of_forall h0)

theorem cdf_lt_integral (f : ℝ → ℝ) (hf : Integrable f) (hc : Continuous f) (hp : ∀ t, 0 < f t) (s : ℝ) :
    cdf f s < ∫ t, f t :=
  (cdf_strictMono f hf hc hp (lt_add_one s)).trans_le (cdf_le_integral f hf (fun t => (hp t).le) (s + 1))

theorem cdf_tendsto_top (f : ℝ → ℝ) (hf : Integrable f) :
    Tendsto (fun n : ℕ => cdf f n) atTop (𝓝 (∫ t, f t)) := by
  have h := tendsto_setIntegral_of_monotone (μ := volume) (f := f) (s := fun n : ℕ => Iic (n : ℝ))
    (fun n => measurableSet_Iic) (fun m n hmn => Iic_subset_Iic.2 (Nat.cast_le.2 hmn)) hf.integrableOn
  have hU : (⋃ n : ℕ, Iic (n : ℝ)) = univ := by
    apply eq_univ_of_forall
    intro x
    obtain ⟨n, hn⟩ := exists_nat_ge x
    exact mem_iUnion.2 ⟨n, hn⟩
  rw [hU, Measure.restrict_univ] at h
  exact h

theorem cdf_tendsto_bot (f : ℝ → ℝ) (hf : Integrable f) :
    Tendsto (fun n : ℕ => cdf f (-(n : ℝ))) atTop (𝓝 0) := by
  have h := tendsto_setIntegral_of_antitone (μ := volume) (f := f) (s := fun n : ℕ => Iic (-(n : ℝ)))
    (fun n => measurableSet_Iic) (fun m n hmn => Iic_subset_Iic.2 (neg_le_neg (Nat.cast_le.2 hmn)))
    ⟨0, hf.integrableOn⟩
  have hI : (⋂ n : ℕ, Iic (-(n : ℝ))) = ∅ := by
    apply eq_empty_of_forall_notMem
    intro x hx
    obtain ⟨n, hn⟩ := exists_nat_gt (-x)
    have := mem_iInter.1 hx n
    simp only [mem_Iic] at this
    linarith
  rw [hI, Measure.restrict_empty, integral_zero_measure] at h
  exact h

/-- The Gaussian distribution function takes every value in `(0, 1)`. -/
theorem G_surj (p : ℝ) (hp : p ∈ Ioo (0:ℝ) 1) : ∃ t, cdf gam t = p := by
  have h1 := cdf_tendsto_bot gam integrable_gam
  have h2 := cdf_tendsto_top gam integrable_gam
  rw [integral_gam] at h2
  obtain ⟨n, hn⟩ := (h1.eventually (gt_mem_nhds hp.1)).exists
  obtain ⟨m, hm⟩ := (h2.eventually (lt_mem_nhds hp.2)).exists
  exact intermediate_value_univ (-(n : ℝ)) (m : ℝ) (cdf_continuous gam integrable_gam continuous_gam)
    ⟨hn.le, hm.le⟩

theorem G_strictMono : StrictMono (cdf gam) :=
  cdf_strictMono gam integrable_gam continuous_gam gam_pos

theorem G_mem (t : ℝ) : cdf gam t ∈ Ioo (0:ℝ) 1 := by
  refine ⟨cdf_pos gam integrable_gam continuous_gam gam_pos t, ?_⟩
  have := cdf_lt_integral gam integrable_gam continuous_gam gam_pos t
  rwa [integral_gam] at this

/-- The inverse of the Gaussian distribution function on `(0, 1)`. -/
noncomputable def Ginv : ℝ → ℝ := Function.invFun (cdf gam)

theorem G_Ginv (p : ℝ) (hp : p ∈ Ioo (0:ℝ) 1) : cdf gam (Ginv p) = p :=
  Function.invFun_eq (G_surj p hp)

theorem Ginv_G (t : ℝ) : Ginv (cdf gam t) = t :=
  Function.leftInverse_invFun G_strictMono.injective t

theorem Ginv_strictMonoOn : StrictMonoOn Ginv (Ioo (0:ℝ) 1) := by
  intro p hp q hq hpq
  by_contra h
  have h' := G_strictMono.monotone (not_lt.1 h)
  rw [G_Ginv p hp, G_Ginv q hq] at h'
  linarith

theorem Ginv_continuousAt (p : ℝ) (hp : p ∈ Ioo (0:ℝ) 1) : ContinuousAt Ginv p := by
  apply Ginv_strictMonoOn.continuousAt_of_image_mem_nhds (Ioo_mem_nhds hp.1 hp.2)
  have : Ginv '' Ioo (0:ℝ) 1 = univ := by
    apply eq_univ_of_forall
    intro t
    exact ⟨cdf gam t, G_mem t, Ginv_G t⟩
  rw [this]
  exact univ_mem

theorem Ginv_hasDerivAt (p : ℝ) (hp : p ∈ Ioo (0:ℝ) 1) :
    HasDerivAt Ginv (gam (Ginv p))⁻¹ p := by
  apply HasDerivAt.of_local_left_inverse (Ginv_continuousAt p hp)
    (cdf_hasDerivAt gam integrable_gam continuous_gam (Ginv p)) (gam_pos _).ne'
  filter_upwards [Ioo_mem_nhds hp.1 hp.2] with y hy
  exact G_Ginv y hy

/-- The increasing map carrying `f(t) dt / ∫ f` to the Gaussian. -/
noncomputable def tr (f : ℝ → ℝ) (s : ℝ) : ℝ := Ginv (cdf f s / ∫ t, f t)

/-- Its derivative. -/
noncomputable def tr' (f : ℝ → ℝ) (s : ℝ) : ℝ := (gam (tr f s))⁻¹ * (f s / ∫ t, f t)

theorem integral_pos_of_pos (f : ℝ → ℝ) (hf : Integrable f) (hc : Continuous f) (hp : ∀ t, 0 < f t) :
    0 < ∫ t, f t :=
  (cdf_pos f hf hc hp 0).trans (cdf_lt_integral f hf hc hp 0)

theorem cdf_div_mem (f : ℝ → ℝ) (hf : Integrable f) (hc : Continuous f) (hp : ∀ t, 0 < f t) (s : ℝ) :
    cdf f s / ∫ t, f t ∈ Ioo (0:ℝ) 1 := by
  have hμ := integral_pos_of_pos f hf hc hp
  exact ⟨div_pos (cdf_pos f hf hc hp s) hμ, (div_lt_one hμ).2 (cdf_lt_integral f hf hc hp s)⟩

theorem tr_strictMono (f : ℝ → ℝ) (hf : Integrable f) (hc : Continuous f) (hp : ∀ t, 0 < f t) :
    StrictMono (tr f) := by
  intro a b hab
  have hμ := integral_pos_of_pos f hf hc hp
  exact Ginv_strictMonoOn (cdf_div_mem f hf hc hp a) (cdf_div_mem f hf hc hp b)
    ((div_lt_div_iff_of_pos_right hμ).2 (cdf_strictMono f hf hc hp hab))

theorem tr_hasDerivAt (f : ℝ → ℝ) (hf : Integrable f) (hc : Continuous f) (hp : ∀ t, 0 < f t) (s : ℝ) :
    HasDerivAt (tr f) (tr' f s) s := by
  have h1 := Ginv_hasDerivAt _ (cdf_div_mem f hf hc hp s)
  have h2 := (cdf_hasDerivAt f hf hc s).div_const (∫ t, f t)
  exact h1.comp s h2

theorem tr'_pos (f : ℝ → ℝ) (hf : Integrable f) (hc : Continuous f) (hp : ∀ t, 0 < f t) (s : ℝ) :
    0 < tr' f s :=
  mul_pos (inv_pos.2 (gam_pos _)) (div_pos (hp s) (integral_pos_of_pos f hf hc hp))

/-- `f = (∫ f) T' γ(T)`: the transport equation. -/
theorem tr_eq (f : ℝ → ℝ) (hf : Integrable f) (hc : Continuous f) (hp : ∀ t, 0 < f t) (s : ℝ) :
    f s = (∫ t, f t) * tr' f s * gam (tr f s) := by
  have hμ := integral_pos_of_pos f hf hc hp
  have hg := gam_pos (tr f s)
  unfold tr'
  field_simp

/-! ### The transport map in `ℝ^d` -/

section Multi

variable {ι κ : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ]

/-- The linear forms `x ↦ u_i · x`, with `u_i` the `i`-th column of `V`. -/
def lin (V : Matrix κ ι ℝ) (i : ι) (x : κ → ℝ) : ℝ := ∑ k, V k i * x k

theorem lin_sub (V : Matrix κ ι ℝ) (i : ι) (x y : κ → ℝ) : lin V i (x - y) = lin V i x - lin V i y := by
  unfold lin
  rw [← Finset.sum_sub_distrib]
  exact Finset.sum_congr rfl fun k _ => by simp only [Pi.sub_apply]; ring

theorem continuous_lin (V : Matrix κ ι ℝ) (i : ι) : Continuous (lin V i) := by
  unfold lin; fun_prop

/-- `∑_k (∑_i V_ki θ_i) w_k = ∑_i θ_i (u_i · w)`. -/
theorem pair_identity (V : Matrix κ ι ℝ) (θ : ι → ℝ) (w : κ → ℝ) :
    ∑ k, (∑ i, V k i * θ i) * w k = ∑ i, θ i * lin V i w := by
  unfold lin
  simp_rw [Finset.sum_mul, Finset.mul_sum]
  rw [Finset.sum_comm]
  exact Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun k _ => by ring

theorem frame_apply (V : Matrix κ ι ℝ) (c : ι → ℝ) (hframe : V * diagonal c * Vᵀ = 1) (k l : κ) :
    ∑ i, V k i * c i * V l i = if k = l then 1 else 0 := by
  have h := congrFun (congrFun hframe k) l
  rw [Matrix.mul_apply] at h
  simp only [Matrix.mul_diagonal, Matrix.transpose_apply, Matrix.one_apply] at h
  exact h

/-- The frame identity recovers a vector from its coordinates `u_i · w`. -/
theorem frame_recon (V : Matrix κ ι ℝ) (c : ι → ℝ) (hframe : V * diagonal c * Vᵀ = 1) (w : κ → ℝ) (k : κ) :
    ∑ i, V k i * (c i * lin V i w) = w k := by
  have e : ∑ i, V k i * (c i * lin V i w) = ∑ l, (∑ i, V k i * c i * V l i) * w l := by
    unfold lin
    simp_rw [Finset.mul_sum, Finset.sum_mul]
    rw [Finset.sum_comm]
    exact Finset.sum_congr rfl fun l _ => Finset.sum_congr rfl fun i _ => by ring
  rw [e]
  simp only [frame_apply V c hframe, ite_mul, one_mul, zero_mul, Finset.sum_ite_eq, Finset.mem_univ, if_true]

/-- The frame inequality `|∑ c_i θ_i u_i|² ≤ ∑ c_i θ_i²`. -/
theorem frame_ineq (V : Matrix κ ι ℝ) (c : ι → ℝ) (hc : ∀ i, 0 ≤ c i) (hframe : V * diagonal c * Vᵀ = 1)
    (θ : ι → ℝ) (y : κ → ℝ) (hy : ∀ k, y k = ∑ i, V k i * (c i * θ i)) :
    ∑ k, y k ^ 2 ≤ ∑ i, c i * θ i ^ 2 := by
  have h1 : ∑ i, c i * θ i * lin V i y = ∑ k, y k ^ 2 := by
    have h := pair_identity V (fun i => c i * θ i) y
    simp only [← hy] at h
    rw [← h]
    exact Finset.sum_congr rfl fun k _ => (sq (y k)).symm
  have h2 : ∑ i, c i * lin V i y ^ 2 = ∑ k, y k ^ 2 := by
    have h := pair_identity V (fun i => c i * lin V i y) y
    simp only [frame_recon V c hframe y] at h
    rw [show ∑ i, c i * lin V i y ^ 2 = ∑ i, c i * lin V i y * lin V i y from
      Finset.sum_congr rfl fun i _ => by ring, ← h]
    exact Finset.sum_congr rfl fun k _ => (sq (y k)).symm
  have h3 : 0 ≤ ∑ i, c i * (θ i - lin V i y) ^ 2 :=
    Finset.sum_nonneg fun i _ => mul_nonneg (hc i) (sq_nonneg _)
  have e : ∑ i, c i * (θ i - lin V i y) ^ 2
      = ∑ i, c i * θ i ^ 2 - 2 * ∑ i, c i * θ i * lin V i y + ∑ i, c i * lin V i y ^ 2 := by
    rw [Finset.mul_sum, ← Finset.sum_sub_distrib, ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun i _ => by ring
  linarith

/-- The transport map `Φ(x) = ∑ c_i T_i(u_i · x) u_i`. -/
noncomputable def Phi (V : Matrix κ ι ℝ) (c : ι → ℝ) (T : ι → ℝ → ℝ) (x : κ → ℝ) : κ → ℝ :=
  fun k => ∑ i, V k i * (c i * T i (lin V i x))

theorem mono_pair (T : ℝ → ℝ) (hT : StrictMono T) (a b : ℝ) :
    0 ≤ (T a - T b) * (a - b) ∧ ((T a - T b) * (a - b) = 0 → a = b) := by
  rcases lt_trichotomy a b with h | h | h
  · have h' := hT h
    refine ⟨by nlinarith, fun h0 => ?_⟩
    have : 0 < (T a - T b) * (a - b) := mul_pos_of_neg_of_neg (by linarith) (by linarith)
    linarith
  · exact ⟨by simp [h], fun _ => h⟩
  · have h' := hT h
    refine ⟨by nlinarith, fun h0 => ?_⟩
    have : 0 < (T a - T b) * (a - b) := mul_pos (by linarith) (by linarith)
    linarith

/-- `Φ` is injective: `⟨Φ x - Φ x', x - x'⟩ = ∑ c_i (T_i a_i - T_i a_i')(a_i - a_i') > 0` unless `x = x'`. -/
theorem Phi_injective (V : Matrix κ ι ℝ) (c : ι → ℝ) (hc : ∀ i, 0 < c i) (hframe : V * diagonal c * Vᵀ = 1)
    (T : ι → ℝ → ℝ) (hT : ∀ i, StrictMono (T i)) : Function.Injective (Phi V c T) := by
  intro x x' hxx
  have hsum : ∑ i, c i * ((T i (lin V i x) - T i (lin V i x')) * (lin V i x - lin V i x')) = 0 := by
    have hp := pair_identity V (fun i => c i * (T i (lin V i x) - T i (lin V i x'))) (x - x')
    have e : ∀ k, ∑ i, V k i * (c i * (T i (lin V i x) - T i (lin V i x')))
        = Phi V c T x k - Phi V c T x' k := by
      intro k
      unfold Phi
      rw [← Finset.sum_sub_distrib]
      exact Finset.sum_congr rfl fun i _ => by ring
    simp only [e, hxx, sub_self, zero_mul, Finset.sum_const_zero] at hp
    rw [hp]
    exact Finset.sum_congr rfl fun i _ => by rw [lin_sub]; ring
  have hnn : ∀ i ∈ (Finset.univ : Finset ι),
      0 ≤ c i * ((T i (lin V i x) - T i (lin V i x')) * (lin V i x - lin V i x')) :=
    fun i _ => mul_nonneg (hc i).le (mono_pair (T i) (hT i) _ _).1
  have hlin : ∀ i, lin V i (x - x') = 0 := by
    intro i
    have h0 := (Finset.sum_eq_zero_iff_of_nonneg hnn).1 hsum i (Finset.mem_univ i)
    rcases mul_eq_zero.1 h0 with h | h
    · exact absurd h (hc i).ne'
    · rw [lin_sub, (mono_pair (T i) (hT i) _ _).2 h, sub_self]
  funext k
  have h := frame_recon V c hframe (x - x') k
  simp only [hlin, mul_zero, Finset.sum_const_zero, Pi.sub_apply] at h
  linarith

/-- The derivative matrix `V diag(c_i l_i) Vᵀ`. -/
noncomputable def DM (V : Matrix κ ι ℝ) (c l : ι → ℝ) : Matrix κ κ ℝ :=
  V * diagonal (fun i => c i * l i) * Vᵀ

theorem DM_mulVec (V : Matrix κ ι ℝ) (c l : ι → ℝ) (v : κ → ℝ) (k : κ) :
    (DM V c l *ᵥ v) k = ∑ i, V k i * (c i * (l i * lin V i v)) := by
  have h1 : DM V c l *ᵥ v = V *ᵥ (diagonal (fun i => c i * l i) *ᵥ (Vᵀ *ᵥ v)) := by
    unfold DM
    rw [Matrix.mulVec_mulVec, Matrix.mulVec_mulVec]
  rw [h1]
  simp only [Matrix.mulVec, dotProduct, Matrix.diagonal_apply, Matrix.transpose_apply, ite_mul, zero_mul,
    Finset.sum_ite_eq, Finset.mem_univ, if_true]
  unfold lin
  exact Finset.sum_congr rfl fun i _ => by ring

theorem det_toCLM (M : Matrix κ κ ℝ) :
    (LinearMap.toContinuousLinearMap (Matrix.toLin' M)).det = M.det := by
  show LinearMap.det (LinearMap.toContinuousLinearMap (Matrix.toLin' M) : (κ → ℝ) →ₗ[ℝ] (κ → ℝ)) = M.det
  rw [LinearMap.coe_toContinuousLinearMap, LinearMap.det_toLin']

theorem Phi_hasFDerivAt (V : Matrix κ ι ℝ) (c : ι → ℝ) (T T' : ι → ℝ → ℝ)
    (hT : ∀ i s, HasDerivAt (T i) (T' i s) s) (x : κ → ℝ) :
    HasFDerivAt (Phi V c T)
      (LinearMap.toContinuousLinearMap (Matrix.toLin' (DM V c (fun i => T' i (lin V i x))))) x := by
  rw [hasFDerivAt_pi']
  intro k
  have hlin : ∀ i, HasFDerivAt (lin V i)
      (∑ m, V m i • ContinuousLinearMap.proj m : (κ → ℝ) →L[ℝ] ℝ) x := by
    intro i
    have e : (⇑(∑ m, V m i • ContinuousLinearMap.proj m : (κ → ℝ) →L[ℝ] ℝ)) = lin V i := by
      funext y
      simp [lin]
    rw [← e]
    exact ContinuousLinearMap.hasFDerivAt _
  have hcomp : ∀ i ∈ (Finset.univ : Finset ι), HasFDerivAt (fun y => V k i * (c i * T i (lin V i y)))
      (V k i • c i • T' i (lin V i x) • (∑ m, V m i • ContinuousLinearMap.proj m : (κ → ℝ) →L[ℝ] ℝ)) x := by
    intro i _
    exact (((hT i (lin V i x)).comp_hasFDerivAt x (hlin i)).const_mul (c i)).const_mul (V k i)
  have key : (ContinuousLinearMap.proj k).comp
      (LinearMap.toContinuousLinearMap (Matrix.toLin' (DM V c (fun i => T' i (lin V i x)))))
      = ∑ i, V k i • c i • T' i (lin V i x) •
          (∑ m, V m i • ContinuousLinearMap.proj m : (κ → ℝ) →L[ℝ] ℝ) := by
    refine ContinuousLinearMap.ext fun v => ?_
    simp only [ContinuousLinearMap.comp_apply, ContinuousLinearMap.proj_apply,
      LinearMap.coe_toContinuousLinearMap', Matrix.toLin'_apply, ContinuousLinearMap.coe_sum',
      Finset.sum_apply, ContinuousLinearMap.coe_smul', Pi.smul_apply, smul_eq_mul]
    rw [DM_mulVec]
    unfold lin
    rfl
  rw [key]
  exact HasFDerivAt.fun_sum hcomp

/-- The Gaussian on `ℝ^κ`. -/
noncomputable def gd (y : κ → ℝ) : ℝ := Real.exp (-Real.pi * ∑ k, y k ^ 2)

theorem gd_eq_prod (y : κ → ℝ) : gd y = ∏ k, gam (y k) := by
  unfold gd gam
  rw [← Real.exp_sum, Finset.mul_sum]

theorem lintegral_gd : ∫⁻ y : κ → ℝ, ENNReal.ofReal (gd y) = 1 := by
  have hint : Integrable (fun y : κ → ℝ => ∏ k, gam (y k)) :=
    Integrable.fintype_prod (f := fun _ => gam) (μ := fun _ => volume) (fun _ => integrable_gam)
  simp_rw [gd_eq_prod]
  rw [← ofReal_integral_eq_lintegral_ofReal hint
    (Eventually.of_forall fun y => Finset.prod_nonneg fun k _ => (gam_pos _).le)]
  rw [integral_fintype_prod_volume_eq_prod (fun _ => gam)]
  simp [integral_gam]

theorem prod_ofReal_rpow {ι : Type*} [Fintype ι] (a c : ι → ℝ) (ha : ∀ i, 0 ≤ a i) (hc : ∀ i, 0 ≤ c i) :
    ∏ i, ENNReal.ofReal (a i) ^ c i = ENNReal.ofReal (∏ i, a i ^ c i) := by
  rw [ENNReal.ofReal_prod_of_nonneg (fun i _ => Real.rpow_nonneg (ha i) _)]
  exact Finset.prod_congr rfl fun i _ => ENNReal.ofReal_rpow_of_nonneg (ha i) (hc i)

/-- Theorem 3.1 for continuous, positive, integrable `h_i`, by Barthe's transport. -/
theorem bl_nice [Nonempty κ] (V : Matrix κ ι ℝ) (c : ι → ℝ) (hc : ∀ i, 0 < c i)
    (hframe : V * diagonal c * Vᵀ = 1) (hunit : ∀ i, (Vᵀ * V) i i = 1)
    (f : ι → ℝ → ℝ) (hfi : ∀ i, Integrable (f i)) (hfc : ∀ i, Continuous (f i)) (hfp : ∀ i t, 0 < f i t) :
    ∫⁻ x : κ → ℝ, ∏ i, ENNReal.ofReal (f i (lin V i x)) ^ c i ≤ ∏ i, ENNReal.ofReal (∫ t, f i t) ^ c i := by
  set μ : ι → ℝ := fun i => ∫ t, f i t with hμdef
  have hμ : ∀ i, 0 < μ i := fun i => integral_pos_of_pos (f i) (hfi i) (hfc i) (hfp i)
  set T : ι → ℝ → ℝ := fun i => tr (f i) with hTdef
  set T' : ι → ℝ → ℝ := fun i => tr' (f i) with hT'def
  have hT : ∀ i s, HasDerivAt (T i) (T' i s) s := fun i s => tr_hasDerivAt (f i) (hfi i) (hfc i) (hfp i) s
  have hTm : ∀ i, StrictMono (T i) := fun i => tr_strictMono (f i) (hfi i) (hfc i) (hfp i)
  have hT'p : ∀ i s, 0 < T' i s := fun i s => tr'_pos (f i) (hfi i) (hfc i) (hfp i) s
  have hfeq : ∀ i s, f i s = μ i * T' i s * gam (T i s) := fun i s => tr_eq (f i) (hfi i) (hfc i) (hfp i) s
  set P : ℝ := ∏ i, μ i ^ c i with hP
  have hP0 : 0 ≤ P := Finset.prod_nonneg fun i _ => Real.rpow_nonneg (hμ i).le _
  set D : (κ → ℝ) → ((κ → ℝ) →L[ℝ] (κ → ℝ)) :=
    fun x => LinearMap.toContinuousLinearMap (Matrix.toLin' (DM V c (fun i => T' i (lin V i x)))) with hD
  have hΦ : ∀ x, HasFDerivAt (Phi V c T) (D x) x := fun x => Phi_hasFDerivAt V c T T' hT x
  have hinj : Function.Injective (Phi V c T) := Phi_injective V c hc hframe T hTm
  have hpt : ∀ x, ∏ i, ENNReal.ofReal (f i (lin V i x)) ^ c i ≤
      ENNReal.ofReal P * (ENNReal.ofReal |(D x).det| * ENNReal.ofReal (gd (Phi V c T x))) := by
    intro x
    set l : ι → ℝ := fun i => T' i (lin V i x) with hl
    set θ : ι → ℝ := fun i => T i (lin V i x) with hθ
    have hl0 : ∀ i, 0 < l i := fun i => hT'p i _
    have hdet : 0 < (DM V c l).det := (Ball.ball_det_log V c l hc hl0 hframe hunit).1
    have hball : ∏ i, l i ^ c i ≤ (DM V c l).det := Ball.ball_det V c l hc hl0 hframe hunit
    have hdetD : (D x).det = (DM V c l).det := det_toCLM _
    have hgam : ∏ i, gam (θ i) ^ c i ≤ gd (Phi V c T x) := by
      have e1 : ∏ i, gam (θ i) ^ c i = Real.exp (-Real.pi * ∑ i, c i * θ i ^ 2) := by
        unfold gam
        rw [Finset.mul_sum, Real.exp_sum]
        exact Finset.prod_congr rfl fun i _ => by rw [← Real.exp_mul]; congr 1; ring
      rw [e1]
      unfold gd
      apply Real.exp_le_exp.2
      have hfr := frame_ineq V c (fun i => (hc i).le) hframe θ (Phi V c T x) (fun k => rfl)
      have hpi := Real.pi_pos
      nlinarith [mul_le_mul_of_nonneg_left hfr hpi.le]
    have hreal : ∏ i, f i (lin V i x) ^ c i ≤ P * ((DM V c l).det * gd (Phi V c T x)) := by
      have e : ∏ i, f i (lin V i x) ^ c i = P * (∏ i, l i ^ c i) * ∏ i, gam (θ i) ^ c i := by
        rw [hP, ← Finset.prod_mul_distrib, ← Finset.prod_mul_distrib]
        refine Finset.prod_congr rfl fun i _ => ?_
        rw [hfeq i, Real.mul_rpow (mul_pos (hμ i) (hT'p i _)).le (gam_pos _).le,
          Real.mul_rpow (hμ i).le (hT'p i _).le]
      rw [e, mul_assoc]
      apply mul_le_mul_of_nonneg_left _ hP0
      exact mul_le_mul hball hgam (Finset.prod_nonneg fun i _ => Real.rpow_nonneg (gam_pos _).le _) hdet.le
    rw [prod_ofReal_rpow _ _ (fun i => (hfp i _).le) (fun i => (hc i).le), hdetD, abs_of_pos hdet,
      ← ENNReal.ofReal_mul hdet.le, ← ENNReal.ofReal_mul hP0]
    exact ENNReal.ofReal_le_ofReal hreal
  have hcv := lintegral_image_eq_lintegral_abs_det_fderiv_mul volume MeasurableSet.univ
    (fun x _ => (hΦ x).hasFDerivWithinAt) hinj.injOn (fun y => ENNReal.ofReal (gd y))
  rw [Measure.restrict_univ] at hcv
  calc ∫⁻ x, ∏ i, ENNReal.ofReal (f i (lin V i x)) ^ c i
      ≤ ∫⁻ x, ENNReal.ofReal P * (ENNReal.ofReal |(D x).det| * ENNReal.ofReal (gd (Phi V c T x))) :=
        lintegral_mono hpt
    _ = ENNReal.ofReal P * ∫⁻ x, ENNReal.ofReal |(D x).det| * ENNReal.ofReal (gd (Phi V c T x)) :=
        lintegral_const_mul' _ _ ENNReal.ofReal_ne_top
    _ = ENNReal.ofReal P * ∫⁻ y in Phi V c T '' univ, ENNReal.ofReal (gd y) := by rw [hcv]
    _ ≤ ENNReal.ofReal P * ∫⁻ y, ENNReal.ofReal (gd y) :=
        mul_le_mul_left' (setLIntegral_le_lintegral _ _) _
    _ = ∏ i, ENNReal.ofReal (μ i) ^ c i := by
        rw [lintegral_gd, mul_one, hP, prod_ofReal_rpow _ _ (fun i => (hμ i).le) (fun i => (hc i).le)]

end Multi

/-! ### Lower semicontinuous functions, by smoothing and Fatou's lemma -/

section Smooth

/-- Bumps of outer radius `2/(n+2)`. -/
noncomputable def bump (n : ℕ) : ContDiffBump (0 : ℝ) where
  rIn := 1 / ((n : ℝ) + 2)
  rOut := 2 / ((n : ℝ) + 2)
  rIn_pos := by positivity
  rIn_lt_rOut := by
    have h : (0:ℝ) < (n : ℝ) + 2 := by positivity
    rw [div_lt_div_iff_of_pos_right h]
    norm_num

/-- The smoothing of `g` by the `n`-th bump. -/
noncomputable def smooth (g : ℝ → ℝ) (n : ℕ) : ℝ → ℝ :=
  convolution ((bump n).normed volume) g (ContinuousLinearMap.lsmul ℝ ℝ) volume

theorem smooth_apply (g : ℝ → ℝ) (n : ℕ) (y : ℝ) :
    smooth g n y = ∫ s, (bump n).normed volume s * g (y - s) := by
  rw [smooth, convolution_def]
  simp only [ContinuousLinearMap.lsmul_apply, smul_eq_mul]

theorem smooth_nonneg (g : ℝ → ℝ) (hg0 : ∀ t, 0 ≤ g t) (n : ℕ) (y : ℝ) : 0 ≤ smooth g n y := by
  rw [smooth_apply]
  exact integral_nonneg fun s => mul_nonneg ((bump n).nonneg_normed s) (hg0 _)

theorem smooth_continuous (g : ℝ → ℝ) (hg : Integrable g) (n : ℕ) : Continuous (smooth g n) :=
  HasCompactSupport.continuous_convolution_left (ContinuousLinearMap.lsmul ℝ ℝ)
    (bump n).hasCompactSupport_normed (bump n).continuous_normed hg.locallyIntegrable

theorem smooth_integrable (g : ℝ → ℝ) (hg : Integrable g) (n : ℕ) : Integrable (smooth g n) :=
  (bump n).integrable_normed.integrable_convolution (ContinuousLinearMap.lsmul ℝ ℝ) hg

theorem smooth_integral (g : ℝ → ℝ) (hg : Integrable g) (n : ℕ) : ∫ t, smooth g n t = ∫ t, g t := by
  rw [smooth, integral_convolution (ContinuousLinearMap.lsmul ℝ ℝ) (bump n).integrable_normed hg]
  simp [ContDiffBump.integral_normed]

/-- For lower semicontinuous `g`, `liminf_n (φ_n * g)(y) ≥ g(y)`, in the form: every `t < g y` is
eventually below the smoothing. -/
theorem smooth_ge (g : ℝ → ℝ) (hgl : LowerSemicontinuous g) (hg : Integrable g) (y t : ℝ) (ht : t < g y) :
    ∀ᶠ n in atTop, t ≤ smooth g n y := by
  obtain ⟨δ, hδ, hball⟩ := Metric.eventually_nhds_iff.1 (hgl y t ht)
  have hev : ∀ᶠ n : ℕ in atTop, 2 / ((n : ℝ) + 2) < δ := by
    obtain ⟨N, hN⟩ := exists_nat_gt (2 / δ)
    refine eventually_atTop.2 ⟨N, fun n hn => ?_⟩
    have hn' : (N : ℝ) ≤ n := Nat.cast_le.2 hn
    rw [div_lt_iff₀ (by positivity)]
    rw [div_lt_iff₀ hδ] at hN
    nlinarith
  filter_upwards [hev] with n hn
  rw [smooth_apply]
  have hconv : Integrable (fun s => (bump n).normed volume s * g (y - s)) := by
    have := (((bump n).hasCompactSupport_normed (μ := volume)).convolutionExists_left
      (ContinuousLinearMap.lsmul ℝ ℝ) ((bump n).continuous_normed (μ := volume)) hg.locallyIntegrable) y
    simpa [ConvolutionExistsAt, ContinuousLinearMap.lsmul_apply, smul_eq_mul] using this
  calc t = ∫ s, (bump n).normed volume s * t := by
        rw [integral_mul_const, ContDiffBump.integral_normed, one_mul]
    _ ≤ ∫ s, (bump n).normed volume s * g (y - s) := by
        refine integral_mono ((bump n).integrable_normed.mul_const t) hconv fun s => ?_
        by_cases hs : (bump n).normed volume s = 0
        · simp [hs]
        · have hsupp : s ∈ Metric.ball (0:ℝ) (bump n).rOut := by
            rw [← (bump n).support_normed_eq (μ := volume)]
            exact hs
          refine mul_le_mul_of_nonneg_left (le_of_lt (hball ?_)) ((bump n).nonneg_normed s)
          rw [Metric.mem_ball, dist_zero_right, Real.norm_eq_abs] at hsupp
          have hr : (bump n).rOut = 2 / ((n : ℝ) + 2) := rfl
          rw [Real.dist_eq, show y - s - y = -s by ring, abs_neg]
          linarith

/-- `L ≤ ofReal(∏ A_i^{c_i})` from the same bound with every `A_i` raised by `ε > 0`. -/
theorem le_of_forall_eps {ι : Type*} [Fintype ι] (L : ℝ≥0∞) (A c : ι → ℝ) (hA : ∀ i, 0 ≤ A i)
    (hc : ∀ i, 0 < c i) (h : ∀ ε : ℝ, 0 < ε → L ≤ ENNReal.ofReal (∏ i, (A i + ε) ^ c i)) :
    L ≤ ENNReal.ofReal (∏ i, A i ^ c i) := by
  have ht : Tendsto (fun ε : ℝ => ENNReal.ofReal (∏ i, (A i + ε) ^ c i)) (𝓝[>] 0)
      (𝓝 (ENNReal.ofReal (∏ i, A i ^ c i))) := by
    apply (ENNReal.continuous_ofReal.tendsto _).comp
    have : Tendsto (fun ε : ℝ => ∏ i, (A i + ε) ^ c i) (𝓝 0) (𝓝 (∏ i, (A i + 0) ^ c i)) := by
      apply tendsto_finset_prod
      intro i _
      exact ((Real.continuousAt_rpow_const _ _ (Or.inr (hc i).le)).tendsto).comp
        (tendsto_const_nhds.add tendsto_id)
    simpa using this.mono_left nhdsWithin_le_nhds
  exact ge_of_tendsto ht (eventually_nhdsWithin_of_forall fun ε hε => h ε hε)

/-- Theorem 3.1 for nonnegative, lower semicontinuous, integrable `h_i`. -/
theorem bl_lsc {ι κ : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ] [Nonempty κ]
    (V : Matrix κ ι ℝ) (c : ι → ℝ) (hc : ∀ i, 0 < c i)
    (hframe : V * diagonal c * Vᵀ = 1) (hunit : ∀ i, (Vᵀ * V) i i = 1)
    (g : ι → ℝ → ℝ) (hg0 : ∀ i t, 0 ≤ g i t) (hgl : ∀ i, LowerSemicontinuous (g i))
    (hgi : ∀ i, Integrable (g i)) :
    ∫⁻ x : κ → ℝ, ∏ i, ENNReal.ofReal (g i (lin V i x)) ^ c i ≤ ∏ i, ENNReal.ofReal (∫ t, g i t) ^ c i := by
  set F : (κ → ℝ) → ℝ≥0∞ := fun x => ∏ i, ENNReal.ofReal (g i (lin V i x)) ^ c i with hF
  set Dc : ℝ := ∑ i, c i with hDc
  rw [prod_ofReal_rpow _ _ (fun i => integral_nonneg (hg0 i)) (fun i => (hc i).le)]
  apply le_of_forall_eps _ _ c (fun i => integral_nonneg (hg0 i)) hc
  intro ε hε
  set G : ι → ℕ → ℝ → ℝ := fun i n s => smooth (g i) n s + ε * gam s with hG
  have hGc : ∀ i n, Continuous (G i n) := fun i n =>
    (smooth_continuous (g i) (hgi i) n).add (continuous_const.mul continuous_gam)
  have hGi : ∀ i n, Integrable (G i n) := fun i n =>
    (smooth_integrable (g i) (hgi i) n).add (integrable_gam.const_mul ε)
  have hGp : ∀ i n t, 0 < G i n t := fun i n t =>
    add_pos_of_nonneg_of_pos (smooth_nonneg (g i) (hg0 i) n t) (mul_pos hε (gam_pos t))
  have hGint : ∀ i n, ∫ t, G i n t = (∫ t, g i t) + ε := by
    intro i n
    simp only [hG]
    rw [integral_add (smooth_integrable (g i) (hgi i) n) (integrable_gam.const_mul ε),
      smooth_integral (g i) (hgi i) n, integral_const_mul, integral_gam, mul_one]
  have hnice : ∀ n, ∫⁻ x : κ → ℝ, ∏ i, ENNReal.ofReal (G i n (lin V i x)) ^ c i
      ≤ ENNReal.ofReal (∏ i, ((∫ t, g i t) + ε) ^ c i) := by
    intro n
    refine (bl_nice V c hc hframe hunit (fun i => G i n) (fun i => hGi i n) (fun i => hGc i n)
      (fun i => hGp i n)).trans_eq ?_
    rw [prod_ofReal_rpow _ _ (fun i => (integral_pos_of_pos _ (hGi i n) (hGc i n) (hGp i n)).le)
      (fun i => (hc i).le)]
    simp only [hGint]
  have hθ : ∀ θ ∈ Ioo (0:ℝ) 1, ENNReal.ofReal (θ ^ Dc) * ∫⁻ x, F x
      ≤ ENNReal.ofReal (∏ i, ((∫ t, g i t) + ε) ^ c i) := by
    intro θ hθ
    rw [← lintegral_const_mul' _ _ ENNReal.ofReal_ne_top]
    have hmeas : ∀ n, Measurable fun x : κ → ℝ => ∏ i, ENNReal.ofReal (G i n (lin V i x)) ^ c i := by
      intro n
      exact Finset.measurable_prod _ fun i _ =>
        (((hGc i n).comp (continuous_lin V i)).measurable.ennreal_ofReal).pow_const _
    calc ∫⁻ x, ENNReal.ofReal (θ ^ Dc) * F x
        ≤ ∫⁻ x, liminf (fun n => ∏ i, ENNReal.ofReal (G i n (lin V i x)) ^ c i) atTop := by
          refine lintegral_mono fun x => le_liminf_of_le (by isBoundedDefault) ?_
          have hev : ∀ᶠ n in atTop, ∀ i, θ * g i (lin V i x) ≤ G i n (lin V i x) := by
            rw [eventually_all]
            intro i
            rcases (hg0 i (lin V i x)).eq_or_lt with h0 | hpos
            · exact Eventually.of_forall fun n => by
                rw [← h0, mul_zero]
                exact (hGp i n _).le
            · filter_upwards [smooth_ge (g i) (hgl i) (hgi i) (lin V i x) (θ * g i (lin V i x))
                (by nlinarith [mul_pos (sub_pos.2 hθ.2) hpos])] with n hn
              have := mul_pos hε (gam_pos (lin V i x))
              simp only [hG]
              linarith
          filter_upwards [hev] with n hn
          simp only [hF]
          rw [prod_ofReal_rpow _ _ (fun i => hg0 i _) (fun i => (hc i).le),
            prod_ofReal_rpow _ _ (fun i => (hGp i n _).le) (fun i => (hc i).le),
            ← ENNReal.ofReal_mul (Real.rpow_nonneg hθ.1.le _)]
          apply ENNReal.ofReal_le_ofReal
          have e : θ ^ Dc * ∏ i, g i (lin V i x) ^ c i = ∏ i, (θ * g i (lin V i x)) ^ c i := by
            rw [hDc, Real.rpow_sum_of_pos hθ.1, ← Finset.prod_mul_distrib]
            exact Finset.prod_congr rfl fun i _ => (Real.mul_rpow hθ.1.le (hg0 i _)).symm
          rw [e]
          exact Finset.prod_le_prod (fun i _ => Real.rpow_nonneg (mul_nonneg hθ.1.le (hg0 i _)) _)
            fun i _ => Real.rpow_le_rpow (mul_nonneg hθ.1.le (hg0 i _)) (hn i) (hc i).le
      _ ≤ liminf (fun n => ∫⁻ x, ∏ i, ENNReal.ofReal (G i n (lin V i x)) ^ c i) atTop :=
          lintegral_liminf_le hmeas
      _ ≤ ENNReal.ofReal (∏ i, ((∫ t, g i t) + ε) ^ c i) :=
          liminf_le_of_frequently_le' (Frequently.of_forall hnice)
  have ht : Tendsto (fun θ : ℝ => ENNReal.ofReal (θ ^ Dc) * ∫⁻ x, F x) (𝓝[<] 1) (𝓝 (∫⁻ x, F x)) := by
    have h1 : Tendsto (fun θ : ℝ => ENNReal.ofReal (θ ^ Dc)) (𝓝[<] 1) (𝓝 1) := by
      have hc1 : ContinuousAt (fun θ : ℝ => ENNReal.ofReal (θ ^ Dc)) 1 :=
        ENNReal.continuous_ofReal.continuousAt.comp (Real.continuousAt_rpow_const 1 Dc (Or.inl one_ne_zero))
      have := hc1.tendsto.mono_left (nhdsWithin_le_nhds (s := Iio 1))
      simpa using this
    simpa using ENNReal.Tendsto.mul_const h1 (Or.inl one_ne_zero)
  exact le_of_tendsto ht (eventually_of_mem (Ioo_mem_nhdsLT (show (0:ℝ) < 1 by norm_num)) hθ)

end Smooth

/-! ### Bounded measurable functions (Vitali-Carathéodory), the general case, and Theorem 3.1 -/

section General

/-- Theorem 3.1 for measurable `h_i : ℝ → [0, ∞]` bounded by a constant, with finite integrals. -/
theorem bl_bdd {ι κ : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ] [Nonempty κ]
    (V : Matrix κ ι ℝ) (c : ι → ℝ) (hc : ∀ i, 0 < c i)
    (hframe : V * diagonal c * Vᵀ = 1) (hunit : ∀ i, (Vᵀ * V) i i = 1)
    (h : ι → ℝ → ℝ≥0∞) (hm : ∀ i, Measurable (h i)) (M : ℝ) (hb : ∀ i t, h i t ≤ ENNReal.ofReal M)
    (hfin : ∀ i, ∫⁻ t, h i t ≠ ∞) :
    ∫⁻ x : κ → ℝ, ∏ i, h i (lin V i x) ^ c i ≤ ∏ i, (∫⁻ t, h i t) ^ c i := by
  set A : ι → ℝ := fun i => (∫⁻ t, h i t).toReal with hA
  have hA0 : ∀ i, 0 ≤ A i := fun i => ENNReal.toReal_nonneg
  have hAe : ∀ i, ∫⁻ t, h i t = ENNReal.ofReal (A i) := fun i => (ENNReal.ofReal_toReal (hfin i)).symm
  have hR : ∏ i, (∫⁻ t, h i t) ^ c i = ENNReal.ofReal (∏ i, A i ^ c i) := by
    simp only [hAe]
    exact prod_ofReal_rpow _ _ hA0 (fun i => (hc i).le)
  rw [hR]
  apply le_of_forall_eps _ A c hA0 hc
  intro ε hε
  have hVC : ∀ i, ∃ g : ℝ → ℝ≥0∞, (∀ t, h i t ≤ g t) ∧ LowerSemicontinuous g ∧
      ∫⁻ t, g t ≤ (∫⁻ t, h i t) + ENNReal.ofReal ε := fun i =>
    exists_le_lowerSemicontinuous_lintegral_ge volume (h i) (hm i) (ENNReal.ofReal_pos.2 hε).ne'
  choose g hhg hgl hgi using hVC
  have hfinM : ∀ a : ℝ≥0∞, min a (ENNReal.ofReal M) ≠ ∞ := fun a =>
    ((min_le_right _ _).trans_lt ENNReal.ofReal_lt_top).ne
  set k : ι → ℝ → ℝ := fun i t => (min (g i t) (ENNReal.ofReal M)).toReal with hk
  have hk0 : ∀ i t, 0 ≤ k i t := fun i t => ENNReal.toReal_nonneg
  have hkof : ∀ i t, ENNReal.ofReal (k i t) = min (g i t) (ENNReal.ofReal M) := fun i t =>
    ENNReal.ofReal_toReal (hfinM _)
  have hkl : ∀ i, LowerSemicontinuous (k i) := by
    intro i
    have hcont : Continuous fun a : ℝ≥0∞ => (min a (ENNReal.ofReal M)).toReal :=
      ENNReal.continuousOn_toReal.comp_continuous (continuous_id.min continuous_const) hfinM
    have hmono : Monotone fun a : ℝ≥0∞ => (min a (ENNReal.ofReal M)).toReal := fun a b hab =>
      ENNReal.toReal_mono (hfinM b) (min_le_min_right _ hab)
    exact hcont.comp_lowerSemicontinuous (hgl i) hmono
  have hgm : ∀ i, Measurable fun t => min (g i t) (ENNReal.ofReal M) := fun i =>
    (hgl i).measurable.min measurable_const
  have hmin_le : ∀ i, ∫⁻ t, min (g i t) (ENNReal.ofReal M) ≤ ENNReal.ofReal (A i + ε) := by
    intro i
    calc ∫⁻ t, min (g i t) (ENNReal.ofReal M) ≤ ∫⁻ t, g i t := lintegral_mono fun t => min_le_left _ _
      _ ≤ (∫⁻ t, h i t) + ENNReal.ofReal ε := hgi i
      _ = ENNReal.ofReal (A i + ε) := by rw [hAe i, ENNReal.ofReal_add (hA0 i) hε.le]
  have hki : ∀ i, Integrable (k i) := fun i =>
    integrable_toReal_of_lintegral_ne_top (hgm i).aemeasurable
      ((hmin_le i).trans_lt ENNReal.ofReal_lt_top).ne
  have hkint : ∀ i, ∫ t, k i t ≤ A i + ε := by
    intro i
    have e : ENNReal.ofReal (∫ t, k i t) = ∫⁻ t, min (g i t) (ENNReal.ofReal M) := by
      rw [ofReal_integral_eq_lintegral_ofReal (hki i) (Eventually.of_forall (hk0 i))]
      simp only [hkof]
    have h2 := hmin_le i
    rw [← e] at h2
    exact (ENNReal.ofReal_le_ofReal_iff (add_nonneg (hA0 i) hε.le)).1 h2
  calc ∫⁻ x, ∏ i, h i (lin V i x) ^ c i ≤ ∫⁻ x, ∏ i, ENNReal.ofReal (k i (lin V i x)) ^ c i := by
        refine lintegral_mono fun x => Finset.prod_le_prod' fun i _ => ENNReal.rpow_le_rpow ?_ (hc i).le
        rw [hkof]
        exact le_min (hhg i _) (hb i _)
    _ ≤ ∏ i, ENNReal.ofReal (∫ t, k i t) ^ c i := bl_lsc V c hc hframe hunit k hk0 hkl hki
    _ = ENNReal.ofReal (∏ i, (∫ t, k i t) ^ c i) :=
        prod_ofReal_rpow _ _ (fun i => integral_nonneg (hk0 i)) (fun i => (hc i).le)
    _ ≤ ENNReal.ofReal (∏ i, (A i + ε) ^ c i) := by
        apply ENNReal.ofReal_le_ofReal
        exact Finset.prod_le_prod (fun i _ => Real.rpow_nonneg (integral_nonneg (hk0 i)) _)
          fun i _ => Real.rpow_le_rpow (integral_nonneg (hk0 i)) (hkint i) (hc i).le

theorem iSup_mul_iSup_mono {f g : ℕ → ℝ≥0∞} (hf : Monotone f) (hg : Monotone g) :
    (⨆ n, f n) * (⨆ n, g n) = ⨆ n, f n * g n := by
  refine le_antisymm ?_ (iSup_le fun n => mul_le_mul' (le_iSup f n) (le_iSup g n))
  rw [ENNReal.iSup_mul]
  refine iSup_le fun m => ?_
  rw [ENNReal.mul_iSup]
  refine iSup_le fun n => ?_
  exact le_iSup_of_le (max m n) (mul_le_mul' (hf (le_max_left m n)) (hg (le_max_right m n)))

theorem prod_iSup_mono {ι : Type*} (s : Finset ι) (f : ι → ℕ → ℝ≥0∞) (hf : ∀ i, Monotone (f i)) :
    ∏ i ∈ s, ⨆ n, f i n = ⨆ n, ∏ i ∈ s, f i n := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | insert a s ha ih =>
    rw [Finset.prod_insert ha, ih, iSup_mul_iSup_mono (hf a)
      (fun m n hmn => Finset.prod_le_prod' fun i _ => hf i hmn)]
    simp only [Finset.prod_insert ha]

theorem iSup_min_nat (a : ℝ≥0∞) : ⨆ n : ℕ, min a (n : ℝ≥0∞) = a := by
  apply le_antisymm (iSup_le fun n => min_le_left _ _)
  rcases eq_or_ne a ⊤ with rfl | ha
  · simp [ENNReal.iSup_natCast]
  · obtain ⟨n, hn⟩ := ENNReal.exists_nat_gt ha
    exact le_iSup_of_le n (min_eq_left hn.le).ge

theorem rpow_iSup_mono (f : ℕ → ℝ≥0∞) (c : ℝ) (hc : 0 < c) : (⨆ n, f n) ^ c = ⨆ n, f n ^ c :=
  Monotone.map_iSup_of_continuousAt (f := fun a : ℝ≥0∞ => a ^ c) ENNReal.continuous_rpow_const.continuousAt
    (ENNReal.monotone_rpow_of_nonneg hc.le) (by simp [ENNReal.zero_rpow_of_pos hc])

/-- Theorem 3.1 for measurable `h_i : ℝ → [0, ∞]` with finite integrals, in matrix form. -/
theorem bl_meas {ι κ : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ] [Nonempty κ]
    (V : Matrix κ ι ℝ) (c : ι → ℝ) (hc : ∀ i, 0 < c i)
    (hframe : V * diagonal c * Vᵀ = 1) (hunit : ∀ i, (Vᵀ * V) i i = 1)
    (h : ι → ℝ → ℝ≥0∞) (hm : ∀ i, Measurable (h i)) (hfin : ∀ i, ∫⁻ t, h i t ≠ ∞) :
    ∫⁻ x : κ → ℝ, ∏ i, h i (lin V i x) ^ c i ≤ ∏ i, (∫⁻ t, h i t) ^ c i := by
  set H : ℕ → (κ → ℝ) → ℝ≥0∞ := fun n x => ∏ i, min (h i (lin V i x)) (n : ℝ≥0∞) ^ c i with hH
  have hpt : ∀ x, ∏ i, h i (lin V i x) ^ c i = ⨆ n, H n x := by
    intro x
    simp only [hH]
    rw [← prod_iSup_mono Finset.univ (fun i n => min (h i (lin V i x)) (n : ℝ≥0∞) ^ c i)
      (fun i m n hmn => ENNReal.rpow_le_rpow (min_le_min_left _ (Nat.cast_le.2 hmn)) (hc i).le)]
    refine Finset.prod_congr rfl fun i _ => ?_
    rw [← rpow_iSup_mono _ _ (hc i), iSup_min_nat]
  have hHm : ∀ n, Measurable (H n) := fun n =>
    Finset.measurable_prod _ fun i _ =>
      (((hm i).comp (continuous_lin V i).measurable).min measurable_const).pow_const _
  have hHmono : Monotone H := fun m n hmn x =>
    Finset.prod_le_prod' fun i _ => ENNReal.rpow_le_rpow (min_le_min_left _ (Nat.cast_le.2 hmn)) (hc i).le
  simp_rw [hpt]
  rw [lintegral_iSup hHm hHmono]
  refine iSup_le fun n => ?_
  calc ∫⁻ x, H n x ≤ ∏ i, (∫⁻ t, min (h i t) (n : ℝ≥0∞)) ^ c i :=
        bl_bdd V c hc hframe hunit (fun i t => min (h i t) (n : ℝ≥0∞)) (fun i => (hm i).min measurable_const)
          (n : ℝ) (fun i t => by rw [ENNReal.ofReal_natCast]; exact min_le_right _ _)
          (fun i => ((lintegral_mono fun t => min_le_left _ _).trans_lt (hfin i).lt_top).ne)
    _ ≤ ∏ i, (∫⁻ t, h i t) ^ c i :=
        Finset.prod_le_prod' fun i _ => ENNReal.rpow_le_rpow (lintegral_mono fun t => min_le_left _ _) (hc i).le

/-- **Theorem 3.1** (the geometric Brascamp-Lieb inequality). Let `u_i ∈ ℝ^κ` be unit vectors and
`c_i > 0` with `∑_i c_i u_i u_iᵀ = I`. For measurable `h_i : ℝ → [0, ∞]` with finite integrals,
`∫ ∏_i h_i(u_i · x)^{c_i} dx ≤ ∏_i (∫ h_i)^{c_i}`. -/
theorem thm31 {ι κ : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ] [Nonempty κ]
    (u : ι → κ → ℝ) (c : ι → ℝ) (hc : ∀ i, 0 < c i) (hu : ∀ i, ∑ k, u i k ^ 2 = 1)
    (hframe : ∀ k l, ∑ i, c i * u i k * u i l = if k = l then 1 else 0)
    (h : ι → ℝ → ℝ≥0∞) (hm : ∀ i, Measurable (h i)) (hfin : ∀ i, ∫⁻ t, h i t ≠ ∞) :
    ∫⁻ x : κ → ℝ, ∏ i, h i (∑ k, u i k * x k) ^ c i ≤ ∏ i, (∫⁻ t, h i t) ^ c i := by
  set V : Matrix κ ι ℝ := Matrix.of fun k i => u i k with hV
  have hVf : V * diagonal c * Vᵀ = 1 := by
    ext k l
    rw [Matrix.mul_apply]
    simp only [Matrix.mul_diagonal, Matrix.transpose_apply, hV, Matrix.of_apply, Matrix.one_apply]
    rw [← hframe k l]
    exact Finset.sum_congr rfl fun i _ => by ring
  have hVu : ∀ i, (Vᵀ * V) i i = 1 := by
    intro i
    rw [Matrix.mul_apply, ← hu i]
    exact Finset.sum_congr rfl fun k _ => by simp [hV, sq]
  exact bl_meas V c hc hVf hVu h hm hfin

/-- Theorem 3.1 for nonnegative integrable real `h_i`, with Bochner integrals, as the paper states it. -/
theorem thm31_real {ι κ : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ] [Nonempty κ]
    (u : ι → κ → ℝ) (c : ι → ℝ) (hc : ∀ i, 0 < c i) (hu : ∀ i, ∑ k, u i k ^ 2 = 1)
    (hframe : ∀ k l, ∑ i, c i * u i k * u i l = if k = l then 1 else 0)
    (h : ι → ℝ → ℝ) (hm : ∀ i, Measurable (h i)) (h0 : ∀ i t, 0 ≤ h i t) (hi : ∀ i, Integrable (h i)) :
    ∫ x : κ → ℝ, ∏ i, h i (∑ k, u i k * x k) ^ c i ≤ ∏ i, (∫ t, h i t) ^ c i := by
  have key := thm31 u c hc hu hframe (fun i t => ENNReal.ofReal (h i t)) (fun i => (hm i).ennreal_ofReal)
    (fun i => (hi i).lintegral_lt_top.ne)
  have hcl : ∀ i, Continuous fun x : κ → ℝ => ∑ k, u i k * x k := fun i =>
    continuous_finset_sum _ fun k _ => continuous_const.mul (continuous_apply k)
  have hmeas : Measurable fun x : κ → ℝ => ∏ i, h i (∑ k, u i k * x k) ^ c i :=
    Finset.measurable_prod _ fun i _ => ((hm i).comp (hcl i).measurable).pow_const _
  rw [integral_eq_lintegral_of_nonneg_ae
    (Eventually.of_forall fun x => Finset.prod_nonneg fun i _ => Real.rpow_nonneg (h0 i _) _)
    hmeas.aestronglyMeasurable]
  apply ENNReal.toReal_le_of_le_ofReal (Finset.prod_nonneg fun i _ => Real.rpow_nonneg (integral_nonneg (h0 i)) _)
  have e1 : ∀ x : κ → ℝ, ENNReal.ofReal (∏ i, h i (∑ k, u i k * x k) ^ c i)
      = ∏ i, ENNReal.ofReal (h i (∑ k, u i k * x k)) ^ c i := fun x =>
    (prod_ofReal_rpow _ _ (fun i => h0 i _) (fun i => (hc i).le)).symm
  simp only [e1]
  refine key.trans_eq ?_
  rw [← prod_ofReal_rpow _ _ (fun i => integral_nonneg (h0 i)) (fun i => (hc i).le)]
  refine Finset.prod_congr rfl fun i _ => ?_
  rw [ofReal_integral_eq_lintegral_ofReal (hi i) (Eventually.of_forall (h0 i))]

end General

end BL

/-! ### Lemma 3.2(a): the density of `UᵀX` -/

namespace ProjA

open BL

/-- A probability measure below Lebesgue measure has a density with values in `[0, 1]`. -/
theorem density_of_le_volume (μ : Measure ℝ) [IsProbabilityMeasure μ] (h : μ ≤ volume) :
    ∃ f : ℝ → ℝ, Measurable f ∧ (∀ y, 0 ≤ f y) ∧ (∀ y, f y ≤ 1) ∧ ∫⁻ y, ENNReal.ofReal (f y) = 1 ∧
      μ = volume.withDensity fun y => ENNReal.ofReal (f y) := by
  have hac : μ ≪ volume := Measure.absolutelyContinuous_of_le h
  have hgm : Measurable (μ.rnDeriv volume) := Measure.measurable_rnDeriv μ volume
  have hle : μ.rnDeriv volume ≤ᵐ[volume] 1 := Measure.rnDeriv_le_one_of_le h
  have hae : (fun y => ENNReal.ofReal (min 1 (μ.rnDeriv volume y).toReal)) =ᵐ[volume] μ.rnDeriv volume := by
    filter_upwards [hle] with y hy
    have hy' : μ.rnDeriv volume y ≤ 1 := by simpa using hy
    have hne : μ.rnDeriv volume y ≠ ⊤ := ne_top_of_le_ne_top ENNReal.one_ne_top hy'
    have hle1 : (μ.rnDeriv volume y).toReal ≤ 1 := by
      have h1 := ENNReal.toReal_mono ENNReal.one_ne_top hy'
      simpa using h1
    rw [min_eq_right hle1, ENNReal.ofReal_toReal hne]
  have hμeq : μ = volume.withDensity fun y => ENNReal.ofReal (min 1 (μ.rnDeriv volume y).toReal) := by
    rw [withDensity_congr_ae hae, Measure.withDensity_rnDeriv_eq μ volume hac]
  refine ⟨fun y => min 1 (μ.rnDeriv volume y).toReal, measurable_const.min hgm.ennreal_toReal,
    fun y => le_min zero_le_one ENNReal.toReal_nonneg, fun y => min_le_left _ _, ?_, hμeq⟩
  show ∫⁻ y, ENNReal.ofReal (min 1 (μ.rnDeriv volume y).toReal) = 1
  rw [← setLIntegral_univ, ← withDensity_apply _ MeasurableSet.univ, ← hμeq, measure_univ]

/-- A nonnegative measurable function with `∫⁻ ofReal f = 1` is integrable. -/
theorem integrable_of_lintegral_one (f : ℝ → ℝ) (hm : Measurable f) (h0 : ∀ y, 0 ≤ f y)
    (h1 : ∫⁻ y, ENNReal.ofReal (f y) = 1) : Integrable f := by
  have h := integrable_toReal_of_lintegral_ne_top hm.ennreal_ofReal.aemeasurable (by rw [h1]; exact ENNReal.one_ne_top)
  have e : (fun y => (ENNReal.ofReal (f y)).toReal) = f := funext fun y => ENNReal.toReal_ofReal (h0 y)
  rwa [e] at h

/-- The product of measures with densities `f_i` has density `∏ f_i(x_i)`. -/
theorem pi_withDensity {ι : Type*} [Fintype ι] (ν : ι → Measure ℝ) [∀ i, IsProbabilityMeasure (ν i)]
    (f : ι → ℝ → ℝ) (h0 : ∀ i t, 0 ≤ f i t) (hi : ∀ i, Integrable (f i))
    (hν : ∀ i, ν i = volume.withDensity fun t => ENNReal.ofReal (f i t)) :
    Measure.pi ν = volume.withDensity fun x : ι → ℝ => ENNReal.ofReal (∏ i, f i (x i)) := by
  refine Measure.pi_eq fun s hs => ?_
  have hbox : MeasurableSet (Set.univ.pi s) := MeasurableSet.univ_pi hs
  rw [withDensity_apply _ hbox]
  have hind : ∀ x : ι → ℝ, (Set.univ.pi s).indicator (fun x => ENNReal.ofReal (∏ i, f i (x i))) x
      = ENNReal.ofReal (∏ i, (s i).indicator (f i) (x i)) := by
    intro x
    by_cases hx : x ∈ Set.univ.pi s
    · rw [Set.indicator_of_mem hx]
      congr 1
      exact Finset.prod_congr rfl fun i _ => (Set.indicator_of_mem (hx i (Set.mem_univ i)) _).symm
    · rw [Set.indicator_of_notMem hx]
      obtain ⟨i, hi'⟩ : ∃ i, x i ∉ s i := not_forall.1 fun h => hx (Set.mem_univ_pi.2 h)
      rw [Finset.prod_eq_zero (Finset.mem_univ i) (Set.indicator_of_notMem hi' _), ENNReal.ofReal_zero]
  rw [← lintegral_indicator hbox]
  simp_rw [hind]
  have hint : Integrable fun x : ι → ℝ => ∏ i, (s i).indicator (f i) (x i) :=
    Integrable.fintype_prod (f := fun i => (s i).indicator (f i)) (μ := fun _ => volume)
      (fun i => (hi i).indicator (hs i))
  rw [← ofReal_integral_eq_lintegral_ofReal hint (Eventually.of_forall fun x =>
      Finset.prod_nonneg fun i _ => Set.indicator_nonneg (fun t _ => h0 i t) _)]
  rw [integral_fintype_prod_volume_eq_prod (fun i => (s i).indicator (f i))]
  rw [ENNReal.ofReal_prod_of_nonneg (fun i _ => integral_nonneg fun t => Set.indicator_nonneg (fun t _ => h0 i t) _)]
  refine Finset.prod_congr rfl fun i _ => ?_
  rw [hν i, withDensity_apply _ (hs i), integral_indicator (hs i),
    ofReal_integral_eq_lintegral_ofReal (hi i).integrableOn (Eventually.of_forall fun t => h0 i t)]

variable {ι κ : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ]

theorem inner_euc (x y : EuclideanSpace ℝ ι) : inner ℝ x y = ∑ i, x.ofLp i * y.ofLp i := by
  have h : ∀ a b : ℝ, inner ℝ a b = b * a := fun a b => Real.ext_cauchy rfl
  simp only [PiLp.inner_apply, h]
  exact Finset.sum_congr rfl fun i _ => mul_comm _ _

/-- The columns of `U` extend to an orthonormal basis of `ℝ^ι` indexed by `κ ⊕ Fin m`. -/
theorem exists_completion (U : Matrix ι κ ℝ) (hU : Uᵀ * U = 1) :
    ∃ m : ℕ, Fintype.card κ + m = Fintype.card ι ∧
      ∃ b : OrthonormalBasis (κ ⊕ Fin m) ℝ (EuclideanSpace ℝ ι), ∀ k i, (b (Sum.inl k)).ofLp i = U i k := by
  set col : κ → EuclideanSpace ℝ ι := fun k => WithLp.toLp 2 (fun i => U i k) with hcol
  have hon : Orthonormal ℝ col := by
    rw [orthonormal_iff_ite]
    intro k k'
    rw [inner_euc]
    have h := congrFun (congrFun hU k) k'
    rw [Matrix.mul_apply, Matrix.one_apply] at h
    simp only [Matrix.transpose_apply] at h
    rw [← h]
  have hle : Fintype.card κ ≤ Fintype.card ι := by
    have h := hon.linearIndependent.fintype_card_le_finrank
    rwa [finrank_euclideanSpace] at h
  refine ⟨Fintype.card ι - Fintype.card κ, by omega, ?_⟩
  set v : κ ⊕ Fin (Fintype.card ι - Fintype.card κ) → EuclideanSpace ℝ ι := Sum.elim col 0 with hv
  have hv' : Orthonormal ℝ ((Set.range Sum.inl).restrict v) := by
    rw [orthonormal_iff_ite]
    rintro ⟨_, k, rfl⟩ ⟨_, k', rfl⟩
    simp only [Set.restrict_apply, hv, Sum.elim_inl, Subtype.mk.injEq, Sum.inl.injEq]
    exact (orthonormal_iff_ite.1 hon) k k'
  obtain ⟨b, hb⟩ := Orthonormal.exists_orthonormalBasis_extension_of_card_eq
    (by rw [finrank_euclideanSpace, Fintype.card_sum, Fintype.card_fin]; omega) hv'
  refine ⟨b, fun k i => ?_⟩
  rw [hb (Sum.inl k) ⟨k, rfl⟩]
  rfl

/-- Coordinates in an orthonormal basis of `ℝ^ι`, as a map of plain function spaces. -/
noncomputable def Psi {σ : Type*} [Fintype σ] (b : OrthonormalBasis σ ℝ (EuclideanSpace ℝ ι)) (v : σ → ℝ) :
    ι → ℝ :=
  (b.repr.symm (WithLp.toLp 2 v)).ofLp

theorem Psi_apply {σ : Type*} [Fintype σ] (b : OrthonormalBasis σ ℝ (EuclideanSpace ℝ ι)) (v : σ → ℝ) (i : ι) :
    Psi b v i = ∑ j, v j * (b j).ofLp i := by
  unfold Psi
  rw [← OrthonormalBasis.sum_repr_symm]
  simp [Finset.sum_apply]

theorem Psi_measurePreserving {σ : Type*} [Fintype σ] (b : OrthonormalBasis σ ℝ (EuclideanSpace ℝ ι)) :
    MeasurePreserving (Psi b) volume volume :=
  (PiLp.volume_preserving_ofLp ι).comp (b.measurePreserving_repr_symm.comp (PiLp.volume_preserving_toLp σ))

theorem basis_orth {σ : Type*} [Fintype σ] [DecidableEq σ] (b : OrthonormalBasis σ ℝ (EuclideanSpace ℝ ι))
    (j j' : σ) : ∑ i, (b j).ofLp i * (b j').ofLp i = if j = j' then 1 else 0 := by
  have h := (orthonormal_iff_ite.1 b.orthonormal) j j'
  rw [inner_euc] at h
  exact h

theorem basis_row {σ : Type*} [Fintype σ] (b : OrthonormalBasis σ ℝ (EuclideanSpace ℝ ι)) (i : ι) :
    ∑ c, (b c).ofLp i ^ 2 = 1 := by
  have h := b.repr.norm_map (EuclideanSpace.single i (1:ℝ))
  rw [EuclideanSpace.norm_single, norm_one] at h
  have h2 : ‖b.repr (EuclideanSpace.single i (1:ℝ))‖ ^ 2
      = ∑ c, ((b.repr (EuclideanSpace.single i (1:ℝ))).ofLp c) ^ 2 := by
    rw [EuclideanSpace.norm_eq, Real.sq_sqrt (Finset.sum_nonneg fun _ _ => sq_nonneg _)]
    simp [Real.norm_eq_abs, sq_abs]
  rw [h, one_pow] at h2
  rw [h2]
  refine Finset.sum_congr rfl fun c _ => ?_
  rw [OrthonormalBasis.repr_apply_apply, inner_euc]
  simp [EuclideanSpace.single_apply]

/-- `a ≥ 0 ↦ log`: `β log(1/β) ≤ 1 - β` for `0 < β`. -/
theorem entropy_le (β : ℝ) (hβ : 0 < β) : β * Real.log β⁻¹ ≤ 1 - β := by
  have h := Real.log_le_sub_one_of_pos (inv_pos.2 hβ)
  have h2 := mul_le_mul_of_nonneg_left h hβ.le
  rw [mul_sub, mul_inv_cancel₀ hβ.ne', mul_one] at h2
  exact h2

/-- `∫⁻ g(a + s t) dt = s⁻¹ ∫⁻ g` for `s > 0`. -/
theorem lintegral_affine (g : ℝ → ℝ≥0∞) (hg : Measurable g) (a s : ℝ) (hs : 0 < s) :
    ∫⁻ t, g (a + s * t) = ENNReal.ofReal s⁻¹ * ∫⁻ t, g t := by
  have hmap := Real.map_volume_mul_left hs.ne'
  have hg' : Measurable fun t => g (a + t) := hg.comp (measurable_const.add measurable_id)
  have h1 : ∫⁻ t, g (a + s * t) = ∫⁻ t, g (a + t) ∂(Measure.map (s * ·) volume) := by
    rw [lintegral_map hg' (measurable_const_mul s)]
  rw [h1, hmap, lintegral_smul_measure, lintegral_add_left_eq_self, abs_of_pos (inv_pos.2 hs)]
  rfl

/-- The fibre bound of Lemma 3.2(a): with `W` having orthonormal columns and rows of length at most one,
`∫ ∏ f_i(a_i + (W w)_i) dw ≤ exp((n - m)/2)` for densities `0 ≤ f_i ≤ 1` of total mass one. -/
theorem fiber_bound (m : ℕ) (W : Matrix ι (Fin m) ℝ)
    (hW : ∀ j l, ∑ i, W i j * W i l = if j = l then 1 else 0) (hrow : ∀ i, ∑ j, W i j ^ 2 ≤ 1)
    (f : ι → ℝ → ℝ) (hm : ∀ i, Measurable (f i)) (h0 : ∀ i t, 0 ≤ f i t) (h1 : ∀ i t, f i t ≤ 1)
    (hint : ∀ i, ∫⁻ t, ENNReal.ofReal (f i t) = 1) (a : ι → ℝ) :
    ∫⁻ w : Fin m → ℝ, ENNReal.ofReal (∏ i, f i (a i + ∑ j, W i j * w j))
      ≤ ENNReal.ofReal (Real.exp (((Fintype.card ι : ℝ) - m) / 2)) := by
  set β : ι → ℝ := fun i => ∑ j, W i j ^ 2 with hβ
  have hβ0 : ∀ i, 0 ≤ β i := fun i => Finset.sum_nonneg fun j _ => sq_nonneg _
  have hsumβ : ∑ i, β i = m := by
    simp only [hβ]
    rw [Finset.sum_comm]
    have : ∀ j, ∑ i, W i j ^ 2 = 1 := fun j => by
      rw [← (by simpa using hW j j : ∑ i, W i j * W i j = 1)]
      exact Finset.sum_congr rfl fun i _ => sq _
    simp [this]
  have hbound_le : (1 : ℝ) ≤ Real.exp (((Fintype.card ι : ℝ) - m) / 2) := by
    apply Real.one_le_exp
    have : (m : ℝ) ≤ Fintype.card ι := by
      rw [← hsumβ]
      calc ∑ i, β i ≤ ∑ _i : ι, (1 : ℝ) := Finset.sum_le_sum fun i _ => hrow i
        _ = Fintype.card ι := by simp
    linarith
  -- the case m = 0
  rcases Nat.eq_zero_or_pos m with hm0 | hmpos
  · subst hm0
    calc ∫⁻ w : Fin 0 → ℝ, ENNReal.ofReal (∏ i, f i (a i + ∑ j, W i j * w j))
        ≤ ∫⁻ _w : Fin 0 → ℝ, 1 := lintegral_mono fun w => by
          rw [← ENNReal.ofReal_one]
          exact ENNReal.ofReal_le_ofReal (Finset.prod_le_one (fun i _ => h0 i _) fun i _ => h1 i _)
      _ = 1 := by
          rw [lintegral_one, volume_pi, Measure.pi_of_empty (x := isEmptyElim)]
          simp
      _ ≤ ENNReal.ofReal (Real.exp (((Fintype.card ι : ℝ) - ((0 : ℕ) : ℝ)) / 2)) := by
          rw [← ENNReal.ofReal_one]
          exact ENNReal.ofReal_le_ofReal (by simpa using hbound_le)
  haveI : Nonempty (Fin m) := ⟨⟨0, hmpos⟩⟩
  -- the rows with β_i > 0
  set I := {i : ι // 0 < β i}
  have hWzero : ∀ i, β i = 0 → ∀ j, W i j = 0 := by
    intro i hi j
    have := (Finset.sum_eq_zero_iff_of_nonneg fun j _ => sq_nonneg (W i j)).1 hi j (Finset.mem_univ j)
    exact pow_eq_zero_iff (two_ne_zero) |>.1 this
  set u : I → Fin m → ℝ := fun i j => W i j / Real.sqrt (β i) with hu
  set c : I → ℝ := fun i => β i with hc
  have hcpos : ∀ i : I, 0 < c i := fun i => i.2
  have hsq : ∀ i : I, Real.sqrt (β i) ^ 2 = β i := fun i => Real.sq_sqrt (hβ0 i)
  have hsqpos : ∀ i : I, 0 < Real.sqrt (β i) := fun i => Real.sqrt_pos.2 i.2
  have hunit : ∀ i : I, ∑ j, u i j ^ 2 = 1 := by
    intro i
    simp only [hu, div_pow, hsq i]
    rw [← Finset.sum_div]
    exact div_self i.2.ne'
  have hframe : ∀ j l, ∑ i : I, c i * u i j * u i l = if j = l then 1 else 0 := by
    intro j l
    have e : ∀ i : I, c i * u i j * u i l = W i j * W i l := by
      intro i
      have hne : β i ≠ 0 := i.2.ne'
      simp only [hc, hu]
      calc β i * (W i j / Real.sqrt (β i)) * (W i l / Real.sqrt (β i))
          = W i j * W i l * (β i / Real.sqrt (β i) ^ 2) := by ring
        _ = W i j * W i l := by rw [hsq i, div_self hne, mul_one]
    simp only [e]
    rw [← hW j l]
    rw [← Fintype.sum_subtype_add_sum_subtype (fun i => 0 < β i) (fun i => W i j * W i l)]
    have hz : ∑ i : {i // ¬ 0 < β i}, W i j * W i l = 0 := by
      refine Finset.sum_eq_zero fun i _ => ?_
      have hb0 : β i = 0 := le_antisymm (not_lt.1 i.2) (hβ0 i)
      rw [hWzero i hb0 j, zero_mul]
    rw [hz, add_zero]
  -- the functions h_i
  set h : I → ℝ → ℝ≥0∞ := fun i t => ENNReal.ofReal (f i (a i + Real.sqrt (β i) * t)) ^ (c i)⁻¹ with hh
  have hhm : ∀ i, Measurable (h i) := fun i =>
    (((hm i).comp (measurable_const.add (measurable_const.mul measurable_id))).ennreal_ofReal).pow_const _
  have hhint : ∀ i : I, ∫⁻ t, h i t ≤ ENNReal.ofReal (Real.sqrt (β i))⁻¹ := by
    intro i
    have hp : (1 : ℝ) ≤ (c i)⁻¹ := by
      rw [one_le_inv₀ (hcpos i)]
      exact le_trans (hrow i) le_rfl
    calc ∫⁻ t, h i t ≤ ∫⁻ t, ENNReal.ofReal (f i (a i + Real.sqrt (β i) * t)) := by
          refine lintegral_mono fun t => ?_
          have hx1 : ENNReal.ofReal (f i (a i + Real.sqrt (β i) * t)) ≤ 1 := by
            rw [← ENNReal.ofReal_one]; exact ENNReal.ofReal_le_ofReal (h1 i _)
          calc h i t ≤ ENNReal.ofReal (f i (a i + Real.sqrt (β i) * t)) ^ (1 : ℝ) :=
                ENNReal.rpow_le_rpow_of_exponent_ge hx1 hp
            _ = _ := ENNReal.rpow_one _
      _ = ENNReal.ofReal (Real.sqrt (β i))⁻¹ * ∫⁻ t, ENNReal.ofReal (f i t) :=
          lintegral_affine (fun t => ENNReal.ofReal (f i t)) (hm i).ennreal_ofReal _ _ (hsqpos i)
      _ = ENNReal.ofReal (Real.sqrt (β i))⁻¹ := by rw [hint i, mul_one]
  have hfin : ∀ i, ∫⁻ t, h i t ≠ ∞ := fun i => ((hhint i).trans_lt ENNReal.ofReal_lt_top).ne
  have key := BL.thm31 u c hcpos hunit hframe h hhm hfin
  -- the integrand
  have hpt : ∀ w : Fin m → ℝ, ENNReal.ofReal (∏ i, f i (a i + ∑ j, W i j * w j))
      ≤ ∏ i : I, h i (∑ j, u i j * w j) ^ c i := by
    intro w
    have e1 : ∀ i : I, h i (∑ j, u i j * w j) ^ c i = ENNReal.ofReal (f i (a i + ∑ j, W i j * w j)) := by
      intro i
      simp only [hh]
      rw [ENNReal.rpow_inv_rpow (hcpos i).ne']
      have hne : Real.sqrt (β i) ≠ 0 := (hsqpos i).ne'
      have hlin : Real.sqrt (β i) * ∑ j, u i j * w j = ∑ j, W i j * w j := by
        rw [Finset.mul_sum]
        refine Finset.sum_congr rfl fun j _ => ?_
        simp only [hu]
        rw [← mul_assoc, mul_div_cancel₀ _ hne]
      rw [hlin]
    simp only [e1]
    rw [ENNReal.ofReal_prod_of_nonneg (fun i _ => h0 i _)]
    rw [← Fintype.prod_subtype_mul_prod_subtype (fun i => 0 < β i)
      (fun i => ENNReal.ofReal (f i (a i + ∑ j, W i j * w j)))]
    apply mul_le_of_le_one_right'
    exact Finset.prod_le_one' fun i _ => by
      rw [← ENNReal.ofReal_one]; exact ENNReal.ofReal_le_ofReal (h1 i _)
  -- the entropy estimate
  have hent : ∏ i : I, ENNReal.ofReal (Real.sqrt (β i))⁻¹ ^ c i
      ≤ ENNReal.ofReal (Real.exp (((Fintype.card ι : ℝ) - m) / 2)) := by
    rw [prod_ofReal_rpow _ _ (fun i => (inv_pos.2 (hsqpos i)).le) (fun i => (hcpos i).le)]
    apply ENNReal.ofReal_le_ofReal
    have e : ∏ i : I, (Real.sqrt (β i))⁻¹ ^ c i = Real.exp (∑ i : I, c i * Real.log (Real.sqrt (β i))⁻¹) := by
      rw [Real.exp_sum]
      refine Finset.prod_congr rfl fun i _ => ?_
      rw [Real.rpow_def_of_pos (inv_pos.2 (hsqpos i)), mul_comm]
    rw [e]
    apply Real.exp_le_exp.2
    have hterm : ∀ i : I, c i * Real.log (Real.sqrt (β i))⁻¹ ≤ (1 - β i) / 2 := by
      intro i
      have hl : Real.log (Real.sqrt (β i))⁻¹ = Real.log (β i)⁻¹ / 2 := by
        rw [Real.log_inv, Real.log_inv, Real.log_sqrt (hβ0 i)]
        ring
      rw [hl]
      have := entropy_le (β i) i.2
      simp only [hc]
      linarith
    calc ∑ i : I, c i * Real.log (Real.sqrt (β i))⁻¹ ≤ ∑ i : I, (1 - β i) / 2 :=
          Finset.sum_le_sum fun i _ => hterm i
      _ ≤ ∑ i : ι, (1 - β i) / 2 := by
          rw [← Fintype.sum_subtype_add_sum_subtype (fun i => 0 < β i) (fun i => (1 - β i) / 2)]
          have : 0 ≤ ∑ i : {i // ¬ 0 < β i}, (1 - β i) / 2 := Finset.sum_nonneg fun i _ => by
            have : β i = 0 := le_antisymm (not_lt.1 i.2) (hβ0 i)
            rw [this]; norm_num
          linarith
      _ = ((Fintype.card ι : ℝ) - m) / 2 := by
          rw [← Finset.sum_div, Finset.sum_sub_distrib, hsumβ]
          simp
  calc ∫⁻ w : Fin m → ℝ, ENNReal.ofReal (∏ i, f i (a i + ∑ j, W i j * w j))
      ≤ ∫⁻ w : Fin m → ℝ, ∏ i : I, h i (∑ j, u i j * w j) ^ c i := lintegral_mono hpt
    _ ≤ ∏ i : I, (∫⁻ t, h i t) ^ c i := key
    _ ≤ ∏ i : I, ENNReal.ofReal (Real.sqrt (β i))⁻¹ ^ c i :=
        Finset.prod_le_prod' fun i _ => ENNReal.rpow_le_rpow (hhint i) (hcpos i).le
    _ ≤ _ := hent

/-- **Lemma 3.2(a).** If `X` has independent coordinates with laws `ν_i ≤ Lebesgue` (densities at most one)
and `UᵀU = I_d`, then `UᵀX` has a density at most `e^{d/2}`. -/
theorem lemma32a (ν : ι → Measure ℝ) [∀ i, IsProbabilityMeasure (ν i)] (hν : ∀ i, ν i ≤ volume)
    (U : Matrix ι κ ℝ) (hU : Uᵀ * U = 1) :
    (Measure.pi ν).map (fun x => Uᵀ *ᵥ x) ≤ ENNReal.ofReal (Real.exp (Fintype.card κ / 2)) • volume := by
  choose f hfm hf0 hf1 hfint hfν using fun i => density_of_le_volume (ν i) (hν i)
  have hfi : ∀ i, Integrable (f i) := fun i => integrable_of_lintegral_one (f i) (hfm i) (hf0 i) (hfint i)
  have hpi := pi_withDensity ν f hf0 hfi hfν
  obtain ⟨m, hmcard, b, hb⟩ := exists_completion U hU
  set K := ENNReal.ofReal (Real.exp (Fintype.card κ / 2)) with hK
  set D : (ι → ℝ) → ℝ≥0∞ := fun x => ENNReal.ofReal (∏ i, f i (x i)) with hD
  have hDm : Measurable D :=
    (Finset.measurable_prod _ fun i _ => (hfm i).comp (measurable_pi_apply i)).ennreal_ofReal
  have hUm : Measurable fun x : ι → ℝ => Uᵀ *ᵥ x := (continuous_const.matrix_mulVec continuous_id).measurable
  set W : Matrix ι (Fin m) ℝ := fun i j => (b (Sum.inr j)).ofLp i with hWdef
  have hW : ∀ j l, ∑ i, W i j * W i l = if j = l then 1 else 0 := by
    intro j l
    have h := basis_orth b (Sum.inr j) (Sum.inr l)
    simp only [Sum.inr.injEq] at h
    exact h
  have hrow : ∀ i, ∑ j, W i j ^ 2 ≤ 1 := by
    intro i
    have h := basis_row b i
    rw [Fintype.sum_sum_type] at h
    have : 0 ≤ ∑ k, (b (Sum.inl k)).ofLp i ^ 2 := Finset.sum_nonneg fun _ _ => sq_nonneg _
    simp only [hWdef]
    linarith
  have hcardm : ((Fintype.card ι : ℝ) - m) = Fintype.card κ := by
    have : (Fintype.card κ : ℝ) + m = Fintype.card ι := by exact_mod_cast hmcard
    linarith
  have hUPsi : ∀ v : κ ⊕ Fin m → ℝ, Uᵀ *ᵥ Psi b v = fun k => v (Sum.inl k) := by
    intro v
    funext k
    simp only [Matrix.mulVec, dotProduct, Matrix.transpose_apply, Psi_apply]
    calc ∑ i, U i k * ∑ j, v j * (b j).ofLp i
        = ∑ j, v j * ∑ i, (b (Sum.inl k)).ofLp i * (b j).ofLp i := by
          simp_rw [hb, Finset.mul_sum]
          rw [Finset.sum_comm]
          exact Finset.sum_congr rfl fun j _ => Finset.sum_congr rfl fun i _ => by ring
      _ = v (Sum.inl k) := by
          simp only [basis_orth b, mul_ite, mul_one, mul_zero, Finset.sum_ite_eq, Finset.sum_ite_eq',
            Finset.mem_univ, if_true]
  have hPsi_split : ∀ (y : κ → ℝ) (w : Fin m → ℝ) (i : ι),
      Psi b ((MeasurableEquiv.sumPiEquivProdPi fun _ : κ ⊕ Fin m => ℝ).symm (y, w)) i
        = (∑ k, U i k * y k) + ∑ j, W i j * w j := by
    intro y w i
    rw [Psi_apply, Fintype.sum_sum_type]
    congr 1
    · exact Finset.sum_congr rfl fun k _ => by rw [hb k i, mul_comm]; rfl
    · exact Finset.sum_congr rfl fun j _ => by rw [mul_comm]; rfl
  rw [Measure.le_iff]
  intro A hA
  rw [Measure.map_apply hUm hA, hpi, withDensity_apply _ (hUm hA), Measure.smul_apply, smul_eq_mul]
  rw [← lintegral_indicator (hUm hA)]
  have hG : Measurable (((fun x : ι → ℝ => Uᵀ *ᵥ x) ⁻¹' A).indicator D) := hDm.indicator (hUm hA)
  rw [← (Psi_measurePreserving b).lintegral_comp hG]
  have hsplit : MeasurePreserving (MeasurableEquiv.sumPiEquivProdPi fun _ : κ ⊕ Fin m => ℝ).symm
      ((volume : Measure (κ → ℝ)).prod (volume : Measure (Fin m → ℝ))) (volume : Measure (κ ⊕ Fin m → ℝ)) :=
    (measurePreserving_sumPiEquivProdPi fun _ : κ ⊕ Fin m => (volume : Measure ℝ)).symm
  have hG2 : Measurable fun v => ((fun x : ι → ℝ => Uᵀ *ᵥ x) ⁻¹' A).indicator D (Psi b v) :=
    hG.comp (Psi_measurePreserving b).measurable
  rw [← hsplit.lintegral_comp hG2]
  rw [lintegral_prod _ ?_]
  swap
  · exact (hG2.comp (MeasurableEquiv.measurable _)).aemeasurable
  have hfib : ∀ y : κ → ℝ, ∫⁻ w : Fin m → ℝ,
      ((fun x : ι → ℝ => Uᵀ *ᵥ x) ⁻¹' A).indicator D
        (Psi b ((MeasurableEquiv.sumPiEquivProdPi fun _ : κ ⊕ Fin m => ℝ).symm (y, w)))
      ≤ A.indicator (fun _ => K) y := by
    intro y
    by_cases hy : y ∈ A
    · rw [Set.indicator_of_mem hy]
      calc _ ≤ ∫⁻ w : Fin m → ℝ, ENNReal.ofReal (∏ i, f i ((∑ k, U i k * y k) + ∑ j, W i j * w j)) := by
            refine lintegral_mono fun w => ?_
            refine (Set.indicator_le_self _ _ _).trans (le_of_eq ?_)
            simp only [hD]
            congr 2
            funext i
            rw [hPsi_split]
        _ ≤ ENNReal.ofReal (Real.exp (((Fintype.card ι : ℝ) - m) / 2)) :=
            fiber_bound m W hW hrow f hfm hf0 hf1 hfint _
        _ = K := by rw [hcardm]
    · rw [Set.indicator_of_notMem hy]
      have hz : ∀ w : Fin m → ℝ, ((fun x : ι → ℝ => Uᵀ *ᵥ x) ⁻¹' A).indicator D
          (Psi b ((MeasurableEquiv.sumPiEquivProdPi fun _ : κ ⊕ Fin m => ℝ).symm (y, w))) = 0 := by
        intro w
        apply Set.indicator_of_notMem
        rw [Set.mem_preimage, hUPsi]
        exact hy
      simp only [hz, lintegral_zero, le_refl]
  calc ∫⁻ y, ∫⁻ w, ((fun x : ι → ℝ => Uᵀ *ᵥ x) ⁻¹' A).indicator D
        (Psi b ((MeasurableEquiv.sumPiEquivProdPi fun _ : κ ⊕ Fin m => ℝ).symm (y, w)))
      ≤ ∫⁻ y, A.indicator (fun _ => K) y := lintegral_mono hfib
    _ = K * volume A := lintegral_indicator_const hA K

end ProjA

end QformFiveB

open Matrix MeasureTheory
open scoped ENNReal

namespace QformFiveB

namespace Proj

section Spectral

variable {n : Type*} [Fintype n] [DecidableEq n]

theorem real_star_eq_transpose (M : Matrix n n ℝ) : star M = Mᵀ := by
  rw [Matrix.star_eq_conjTranspose, Matrix.conjTranspose_eq_transpose_of_trivial]

/-- The eigenvector matrix of a real symmetric matrix is orthogonal. -/
theorem eigU_orth (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    (hA.eigenvectorUnitary : Matrix n n ℝ)ᵀ * (hA.eigenvectorUnitary : Matrix n n ℝ) = 1 := by
  have h := Unitary.coe_star_mul_self hA.eigenvectorUnitary
  rw [real_star_eq_transpose] at h
  exact h

theorem eigU_orth' (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    (hA.eigenvectorUnitary : Matrix n n ℝ) * (hA.eigenvectorUnitary : Matrix n n ℝ)ᵀ = 1 := by
  have h := Unitary.coe_mul_star_self hA.eigenvectorUnitary
  rw [Unitary.coe_star, real_star_eq_transpose] at h
  exact h

/-- The spectral theorem in the form `A U = U diag(λ)`. -/
theorem eigU_eigen (A : Matrix n n ℝ) (hA : A.IsHermitian) :
    A * (hA.eigenvectorUnitary : Matrix n n ℝ)
      = (hA.eigenvectorUnitary : Matrix n n ℝ) * diagonal hA.eigenvalues := by
  ext i j
  have h := congrFun (hA.mulVec_eigenvectorBasis j) i
  simp only [Matrix.mulVec, dotProduct, Pi.smul_apply, smul_eq_mul] at h
  rw [Matrix.mul_diagonal, Matrix.mul_apply]
  simp only [IsHermitian.eigenvectorUnitary_apply]
  rw [h, mul_comm]

/-- `U diag(d) Uᵀ` for the eigenvector matrix `U` of `G`. -/
noncomputable def conjDiag (G : Matrix n n ℝ) (hG : G.IsHermitian) (d : n → ℝ) : Matrix n n ℝ :=
  (hG.eigenvectorUnitary : Matrix n n ℝ) * diagonal d * (hG.eigenvectorUnitary : Matrix n n ℝ)ᵀ

/-- `G = U diag(λ) Uᵀ`. -/
theorem spectral_decomp (G : Matrix n n ℝ) (hG : G.IsHermitian) : G = conjDiag G hG hG.eigenvalues := by
  unfold conjDiag
  calc G = G * ((hG.eigenvectorUnitary : Matrix n n ℝ) * (hG.eigenvectorUnitary : Matrix n n ℝ)ᵀ) := by
        rw [eigU_orth' G hG, Matrix.mul_one]
    _ = G * (hG.eigenvectorUnitary : Matrix n n ℝ) * (hG.eigenvectorUnitary : Matrix n n ℝ)ᵀ := by
        rw [Matrix.mul_assoc]
    _ = (hG.eigenvectorUnitary : Matrix n n ℝ) * diagonal hG.eigenvalues * (hG.eigenvectorUnitary : Matrix n n ℝ)ᵀ := by
        rw [eigU_eigen G hG]

theorem conjDiag_transpose (G : Matrix n n ℝ) (hG : G.IsHermitian) (d : n → ℝ) :
    (conjDiag G hG d)ᵀ = conjDiag G hG d := by
  unfold conjDiag
  rw [Matrix.transpose_mul, Matrix.transpose_mul, Matrix.transpose_transpose, Matrix.diagonal_transpose,
    Matrix.mul_assoc]

theorem conjDiag_mul (G : Matrix n n ℝ) (hG : G.IsHermitian) (d e : n → ℝ) :
    conjDiag G hG d * conjDiag G hG e = conjDiag G hG (fun i => d i * e i) := by
  unfold conjDiag
  have h : (hG.eigenvectorUnitary : Matrix n n ℝ) * diagonal d * (hG.eigenvectorUnitary : Matrix n n ℝ)ᵀ
      * ((hG.eigenvectorUnitary : Matrix n n ℝ) * diagonal e * (hG.eigenvectorUnitary : Matrix n n ℝ)ᵀ)
      = (hG.eigenvectorUnitary : Matrix n n ℝ) * diagonal d
        * ((hG.eigenvectorUnitary : Matrix n n ℝ)ᵀ * (hG.eigenvectorUnitary : Matrix n n ℝ))
        * diagonal e * (hG.eigenvectorUnitary : Matrix n n ℝ)ᵀ := by
    simp only [Matrix.mul_assoc]
  rw [h, eigU_orth G hG, Matrix.mul_one, Matrix.mul_assoc (hG.eigenvectorUnitary : Matrix n n ℝ),
    Matrix.diagonal_mul_diagonal]

theorem conjDiag_one (G : Matrix n n ℝ) (hG : G.IsHermitian) : conjDiag G hG (fun _ => 1) = 1 := by
  unfold conjDiag
  rw [Matrix.diagonal_one, Matrix.mul_one, eigU_orth' G hG]

theorem det_conjDiag (G : Matrix n n ℝ) (hG : G.IsHermitian) (d : n → ℝ) : (conjDiag G hG d).det = ∏ i, d i := by
  unfold conjDiag
  have hU : (hG.eigenvectorUnitary : Matrix n n ℝ)ᵀ.det * (hG.eigenvectorUnitary : Matrix n n ℝ).det = 1 := by
    rw [← Matrix.det_mul, eigU_orth G hG, Matrix.det_one]
  rw [Matrix.det_mul, Matrix.det_mul, Matrix.det_diagonal]
  linear_combination (∏ i, d i) * hU

end Spectral

theorem measurable_mulVec {m k : Type*} [Fintype m] [Fintype k] [DecidableEq k] (M : Matrix m k ℝ) :
    Measurable fun x : k → ℝ => M *ᵥ x := by
  have h : (fun x : k → ℝ => M *ᵥ x) = ⇑(Matrix.toLin' M) := funext (fun x => (Matrix.toLin'_apply M x).symm)
  rw [h]
  exact (Matrix.toLin' M).continuous_of_finiteDimensional.measurable

/-- **Lemma 3.2(b) from (a).** If `Law(Uᵀ X) ≤ K · Lebesgue` for every `U` with orthonormal columns, then for every
`B ∈ ℝ^{κ×ι}` with `det(BBᵀ) ≠ 0` (rank `d = |κ|`), `Law(BX) ≤ K det(BBᵀ)^{-1/2} · Lebesgue`. -/
theorem lemma32b {ι κ : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ]
    (μ : Measure (ι → ℝ)) (K : ℝ) (hK : 0 ≤ K)
    (ha : ∀ U : Matrix ι κ ℝ, Uᵀ * U = 1 → μ.map (fun x => Uᵀ *ᵥ x) ≤ ENNReal.ofReal K • volume)
    (B : Matrix κ ι ℝ) (hB : (B * Bᵀ).det ≠ 0) :
    μ.map (fun x => B *ᵥ x) ≤ ENNReal.ofReal (K / √((B * Bᵀ).det)) • volume := by
  set G := B * Bᵀ with hGdef
  have hGh : G.IsHermitian := by
    rw [Matrix.IsHermitian, Matrix.conjTranspose_eq_transpose_of_trivial, hGdef, Matrix.transpose_mul,
      Matrix.transpose_transpose]
  have hpsd : G.PosSemidef := by
    have h := Matrix.posSemidef_self_mul_conjTranspose B
    rwa [Matrix.conjTranspose_eq_transpose_of_trivial] at h
  have hlam0 : ∀ i, 0 ≤ hGh.eigenvalues i := fun i => hpsd.eigenvalues_nonneg i
  have hdet : G.det = ∏ i, hGh.eigenvalues i := by
    conv_lhs => rw [spectral_decomp G hGh]
    exact det_conjDiag G hGh _
  have hlampos : ∀ i, 0 < hGh.eigenvalues i := by
    intro i
    rcases (hlam0 i).lt_or_eq with h | h
    · exact h
    · exfalso
      apply hB
      rw [hdet]
      exact Finset.prod_eq_zero (Finset.mem_univ i) h.symm
  set S := conjDiag G hGh (fun i => √(hGh.eigenvalues i)) with hS
  set T := conjDiag G hGh (fun i => (√(hGh.eigenvalues i))⁻¹) with hT
  have hST : S * T = 1 := by
    rw [hS, hT, conjDiag_mul]
    have e : (fun i => √(hGh.eigenvalues i) * (√(hGh.eigenvalues i))⁻¹) = fun _ => (1 : ℝ) := by
      funext i
      exact mul_inv_cancel₀ (Real.sqrt_pos.2 (hlampos i)).ne'
    rw [e, conjDiag_one]
  have hTS : T * S = 1 := by
    rw [hS, hT, conjDiag_mul]
    have e : (fun i => (√(hGh.eigenvalues i))⁻¹ * √(hGh.eigenvalues i)) = fun _ => (1 : ℝ) := by
      funext i
      exact inv_mul_cancel₀ (Real.sqrt_pos.2 (hlampos i)).ne'
    rw [e, conjDiag_one]
  have hSS : S * S = G := by
    rw [hS, conjDiag_mul]
    have e : (fun i => √(hGh.eigenvalues i) * √(hGh.eigenvalues i)) = hGh.eigenvalues := by
      funext i
      exact Real.mul_self_sqrt (hlam0 i)
    rw [e, ← spectral_decomp G hGh]
  have hTt : Tᵀ = T := conjDiag_transpose G hGh _
  set V := Bᵀ * T with hV
  have hVV : Vᵀ * V = 1 := by
    rw [hV, Matrix.transpose_mul, Matrix.transpose_transpose, hTt]
    calc T * B * (Bᵀ * T) = T * (B * Bᵀ) * T := by simp only [Matrix.mul_assoc]
      _ = T * (S * S) * T := by rw [← hGdef, hSS]
      _ = T * S * (S * T) := by simp only [Matrix.mul_assoc]
      _ = 1 := by rw [hTS, hST, Matrix.one_mul]
  have hBSV : S * Vᵀ = B := by
    rw [hV, Matrix.transpose_mul, Matrix.transpose_transpose, hTt, ← Matrix.mul_assoc, hST, Matrix.one_mul]
  have hdetS : S.det = √G.det := by
    rw [hS, det_conjDiag, hdet]
    have hsq : ∏ i, hGh.eigenvalues i = (∏ i, √(hGh.eigenvalues i)) ^ 2 := by
      rw [← Finset.prod_pow]
      apply Finset.prod_congr rfl
      intro i _
      exact (Real.sq_sqrt (hlam0 i)).symm
    rw [hsq, Real.sqrt_sq (Finset.prod_nonneg (fun i _ => Real.sqrt_nonneg _))]
  have hGpos : 0 < G.det := by
    rw [hdet]
    exact Finset.prod_pos (fun i _ => hlampos i)
  have hdetS0 : S.det ≠ 0 := by
    rw [hdetS]
    exact (Real.sqrt_pos.2 hGpos).ne'
  have hcomp : (fun x : ι → ℝ => B *ᵥ x) = (fun y : κ → ℝ => S *ᵥ y) ∘ (fun x : ι → ℝ => Vᵀ *ᵥ x) := by
    funext x
    simp only [Function.comp_apply, Matrix.mulVec_mulVec, hBSV]
  have hmapS : (volume : Measure (κ → ℝ)).map (fun y => S *ᵥ y) = ENNReal.ofReal |S.det⁻¹| • volume := by
    have hfun : (fun y : κ → ℝ => S *ᵥ y) = ⇑(Matrix.toLin' S) :=
      funext (fun y => (Matrix.toLin'_apply S y).symm)
    have h := Measure.map_linearMap_addHaar_eq_smul_addHaar (μ := (volume : Measure (κ → ℝ)))
      (f := Matrix.toLin' S) (by rw [LinearMap.det_toLin']; exact hdetS0)
    rw [LinearMap.det_toLin'] at h
    rw [hfun]
    exact h
  rw [hcomp, ← Measure.map_map (measurable_mulVec S) (measurable_mulVec Vᵀ)]
  calc (μ.map fun x => Vᵀ *ᵥ x).map (fun y => S *ᵥ y)
      ≤ (ENNReal.ofReal K • (volume : Measure (κ → ℝ))).map (fun y => S *ᵥ y) :=
        Measure.map_mono (ha V hVV) (measurable_mulVec S)
    _ = ENNReal.ofReal K • ((volume : Measure (κ → ℝ)).map (fun y => S *ᵥ y)) := Measure.map_smul _ _ _
    _ = ENNReal.ofReal (K / √G.det) • volume := by
        rw [hmapS, smul_smul, ← ENNReal.ofReal_mul hK, hdetS, abs_inv, abs_of_pos (Real.sqrt_pos.2 hGpos),
          div_eq_mul_inv]

/-- **The last assertion of Lemma 3.2.** If `Law(Uᵀ X) ≤ K · Lebesgue` for every unit vector `U` (Lemma 3.2(a) with
`d = 1`, `K = √e`), then `Law(a · X) ≤ K / |a| · Lebesgue` for every `a ≠ 0`. -/
theorem lemma32_dot {ι : Type*} [Fintype ι] [DecidableEq ι] (μ : Measure (ι → ℝ)) (K : ℝ) (hK : 0 ≤ K)
    (ha : ∀ U : Matrix ι (Fin 1) ℝ, Uᵀ * U = 1 → μ.map (fun x => Uᵀ *ᵥ x) ≤ ENNReal.ofReal K • volume)
    (a : ι → ℝ) (ha0 : a ≠ 0) :
    μ.map (fun x => a ⬝ᵥ x) ≤ ENNReal.ofReal (K / √(a ⬝ᵥ a)) • volume := by
  set B : Matrix (Fin 1) ι ℝ := Matrix.of (fun _ j => a j) with hBdef
  have hBB : (B * Bᵀ).det = a ⬝ᵥ a := by
    rw [Matrix.det_unique]
    simp [hBdef, Matrix.mul_apply, dotProduct]
  have hdot : a ⬝ᵥ a ≠ 0 := by
    intro h
    exact ha0 (dotProduct_self_eq_zero.1 h)
  have hb := lemma32b μ K hK ha B (by rw [hBB]; exact hdot)
  rw [hBB] at hb
  have hmeas0 : Measurable fun v : Fin 1 → ℝ => v 0 := measurable_pi_apply 0
  have hcomp : (fun x : ι → ℝ => a ⬝ᵥ x) = (fun v : Fin 1 → ℝ => v 0) ∘ (fun x : ι → ℝ => B *ᵥ x) := by
    funext x
    simp [hBdef, Matrix.mulVec, dotProduct]
  have hvol : (volume : Measure (Fin 1 → ℝ)).map (fun v => v 0) = volume := by
    have h := (MeasureTheory.volume_preserving_funUnique (Fin 1) ℝ).map_eq
    exact h
  rw [hcomp, ← Measure.map_map hmeas0 (measurable_mulVec B)]
  calc (μ.map fun x => B *ᵥ x).map (fun v : Fin 1 → ℝ => v 0)
      ≤ (ENNReal.ofReal (K / √(a ⬝ᵥ a)) • (volume : Measure (Fin 1 → ℝ))).map (fun v => v 0) :=
        Measure.map_mono hb hmeas0
    _ = ENNReal.ofReal (K / √(a ⬝ᵥ a)) • volume := by rw [Measure.map_smul, hvol]

end Proj

namespace Lemma32

/-- **Lemma 3.2(b)** from its hypotheses: for `X` with independent coordinates with densities at most one and `B` of
rank `d`, `BX` has a density at most `e^{d/2} det(BBᵀ)^{-1/2}`. -/
theorem lemma32b_full {ι κ : Type*} [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ]
    (ν : ι → Measure ℝ) [∀ i, IsProbabilityMeasure (ν i)] (hν : ∀ i, ν i ≤ volume)
    (B : Matrix κ ι ℝ) (hB : (B * Bᵀ).det ≠ 0) :
    (Measure.pi ν).map (fun x => B *ᵥ x)
      ≤ ENNReal.ofReal (Real.exp ((Fintype.card κ : ℝ) / 2) / √((B * Bᵀ).det)) • volume :=
  Proj.lemma32b (Measure.pi ν) (Real.exp ((Fintype.card κ : ℝ) / 2)) (Real.exp_pos _).le
    (fun U hU => ProjA.lemma32a ν hν U hU) B hB

/-- **The last assertion of Lemma 3.2**: `a · X` has a density at most `√e / |a|` for every `a ≠ 0`. -/
theorem lemma32_dot_full {ι : Type*} [Fintype ι] [DecidableEq ι]
    (ν : ι → Measure ℝ) [∀ i, IsProbabilityMeasure (ν i)] (hν : ∀ i, ν i ≤ volume)
    (a : ι → ℝ) (ha0 : a ≠ 0) :
    (Measure.pi ν).map (fun x => a ⬝ᵥ x) ≤ ENNReal.ofReal (Real.sqrt (Real.exp 1) / √(a ⬝ᵥ a)) • volume := by
  have h := Proj.lemma32_dot (Measure.pi ν) (Real.exp ((Fintype.card (Fin 1) : ℝ) / 2)) (Real.exp_pos _).le
    (fun U hU => ProjA.lemma32a ν hν U hU) a ha0
  have e : Real.exp ((Fintype.card (Fin 1) : ℝ) / 2) = Real.sqrt (Real.exp 1) := by
    rw [Fintype.card_fin, Nat.cast_one,
      show Real.exp 1 = Real.exp (1 / 2) ^ 2 by rw [← Real.exp_nat_mul]; norm_num,
      Real.sqrt_sq (Real.exp_pos _).le]
  rw [e] at h
  exact h

end Lemma32

end QformFiveB
