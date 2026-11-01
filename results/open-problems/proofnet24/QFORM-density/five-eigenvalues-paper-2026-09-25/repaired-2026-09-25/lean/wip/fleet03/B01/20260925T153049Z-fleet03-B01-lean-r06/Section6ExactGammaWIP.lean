/-!
fleet03/B01 r06 WIP: strict repaired Proposition 6.4 adapter.
Append after historical QformFive3.lean and Section6StatementAdapters.lean.
UNVERIFIED until an exact Lean/Mathlib compile and #print axioms check.
-/

namespace QformFive

noncomputable def repairedDiagSet {n : ℕ}
    (A : Matrix (Fin n) (Fin n) ℝ) : Finset ℝ := by
  classical
  exact insert 0 (Finset.univ.image (fun i => |A i i|))

noncomputable def repairedDiagCap {n : ℕ}
    (A : Matrix (Fin n) (Fin n) ℝ) : ℝ :=
  (repairedDiagSet A).max' (by
    classical
    simp [repairedDiagSet])

theorem repaired_diag_le_cap {n : ℕ}
    (A : Matrix (Fin n) (Fin n) ℝ) (i : Fin n) :
    |A i i| ≤ repairedDiagCap A := by
  classical
  unfold repairedDiagCap
  exact Finset.le_max' (repairedDiagSet A) |A i i| (by
    simp [repairedDiagSet])

theorem repaired_diagCap_nonneg {n : ℕ}
    (A : Matrix (Fin n) (Fin n) ℝ) :
    0 ≤ repairedDiagCap A := by
  classical
  unfold repairedDiagCap
  exact Finset.le_max' (repairedDiagSet A) 0 (by simp [repairedDiagSet])

theorem repaired_diagCap_lt_eta {n : ℕ}
    (A : Matrix (Fin n) (Fin n) ℝ)
    (hd : ∀ i, |A i i| < (1 / 12 : ℝ)) :
    repairedDiagCap A < (1 / 12 : ℝ) := by
  classical
  unfold repairedDiagCap
  apply (Finset.max'_lt_iff _ _).2
  intro y hy
  rw [repairedDiagSet] at hy
  rcases Finset.mem_insert.mp hy with rfl | hy
  · norm_num
  · rcases Finset.mem_image.mp hy with ⟨i, -, rfl⟩
    exact hd i

theorem repaired_strict_power_transfer
    (m : ℕ) (γ σ E : ℝ)
    (hm : m ≠ 0) (hγ : 0 ≤ γ) (hgap : γ < σ)
    (hE : σ ^ (2 * m) ≤ E) :
    γ ^ (2 * m) < E := by
  have hpow : γ ^ (2 * m) < σ ^ (2 * m) :=
    pow_lt_pow_left₀ hgap hγ (by omega)
  exact lt_of_lt_of_le hpow hE

theorem prop64_repaired_exact_eigenframe
    {n m : ℕ}
    (A : Matrix (Fin n) (Fin n) ℝ)
    (hsym : ∀ i j, A j i = A i j)
    (Φ : Matrix (Fin n) (Fin (2 * m - 1)) ℝ)
    (hΦ : Φᵀ * Φ = 1)
    (lam : Fin (2 * m - 1) → ℝ)
    (hEig : A * Φ = Φ * diagonal lam)
    (hlam : ∀ c, 1 ≤ |lam c|)
    (hd : ∀ i, |A i i| < 1 / 12)
    (hp : ∀ i j, i ≠ j →
      |A i i * A j j - A i j ^ 2| < 1 / 256)
    (hm : m ≠ 0)
    (hgamma : 0 ≤ repairedGamma m) :
    ∃ x : Fin n → Bool, ∃ sigma : ℝ,
      repairedGamma m < sigma ∧ ApproxGE m sigma (blk A x) ∧
      ∀ hG : (blk A x * (blk A x)ᵀ).IsHermitian,
        repairedGamma m ^ (2 * m) < Evol (blk A x) hG m := by
  let delta := repairedDiagCap A
  let sigma := repairedSigma m delta
  have hdelta0 : 0 ≤ delta := by
    dsimp [delta]
    exact repaired_diagCap_nonneg A
  have hdeltalt : delta < (1 / 12 : ℝ) := by
    dsimp [delta]
    exact repaired_diagCap_lt_eta A hd
  have hgap : repairedGamma m < sigma := by
    dsimp [sigma]
    exact repairedGamma_lt_sigma_of_diag_strict m delta hdeltalt
  have hsigma : 0 < sigma := lt_of_le_of_lt hgamma hgap
  have hpos :
      0 < 1 - delta - Real.sqrt 2 * (5 / 48 : ℝ) *
        (((2 * m - 1 : ℕ) : ℝ)) := by
    dsimp [sigma, repairedSigma] at hsigma
    linarith
  obtain ⟨x, hx⟩ :=
    prop64 A hsym Φ hΦ lam hEig hlam (5 / 48) delta
      (by norm_num) hdelta0
      (nopivot_entries A hd hp)
      (fun i => repaired_diag_le_cap A i)
      hpos
  have hx' : ApproxGE m sigma (blk A x) := by
    simpa [blk, sigma, repairedSigma] using hx
  refine ⟨x, sigma, hgap, hx', ?_⟩
  intro hG
  have hE : sigma ^ (2 * m) ≤ Evol (blk A x) hG m :=
    evol_of_approx (blk A x) hG m sigma hsigma hx'
  exact repaired_strict_power_transfer m (repairedGamma m) sigma
    (Evol (blk A x) hG m) hm hgamma hgap hE

end QformFive
