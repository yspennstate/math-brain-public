import Mathlib.Analysis.Matrix.Spectrum
import Mathlib.Analysis.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.MeasureTheory.Measure.Lebesgue.EqHaar
import Mathlib.MeasureTheory.Measure.Haar.OfBasis
import Mathlib.Data.Real.StarOrdered
import Mathlib.Tactic

/-!
Lemma 3.2(b) of "Quadratic forms with five large singular values have bounded densities" (repaired text,
sha256 90f859b7) from Lemma 3.2(a), and the last assertion of Lemma 3.2.

Lemma 3.2(a) says that `Uᵀ X` has a density bounded by `e^{d/2}` whenever `Uᵀ U = I_d`; here it enters as the hypothesis
that `Law(Uᵀ X) ≤ K · Lebesgue` for every such `U`. The paper writes `B = P Σ Uᵀ`; the proof below uses the equivalent
factorization `B = S Vᵀ` with `S = (BBᵀ)^{1/2}` and `V = Bᵀ S⁻¹`, so that `Vᵀ V = S⁻¹ BBᵀ S⁻¹ = I_d`, and then the linear
change of variables `y ↦ S y` with `|det S| = det(BBᵀ)^{1/2}`.

* `conjDiag`: `U diag(d) Uᵀ` for the orthogonal eigenvector matrix `U` of a real symmetric `G`; products, transposes and
  determinants of these (`conjDiag_mul`, `conjDiag_transpose`, `det_conjDiag`), and `G = U diag(λ) Uᵀ` (`spectral_decomp`).
* `lemma32b`: `Law(BX) ≤ K det(BBᵀ)^{-1/2} · Lebesgue` for every `B` with `det(BBᵀ) ≠ 0` (rank `d`).
* `lemma32_dot`: the last assertion, `Law(a · X) ≤ K / |a| · Lebesgue` for `a ≠ 0` (`K = √e` from (a) with `d = 1`).

The spectral lemmas `eigU_orth`, `eigU_orth'`, `eigU_eigen` are repeated from `lean/QformFive3.lean`.
-/

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

end QformFiveB
