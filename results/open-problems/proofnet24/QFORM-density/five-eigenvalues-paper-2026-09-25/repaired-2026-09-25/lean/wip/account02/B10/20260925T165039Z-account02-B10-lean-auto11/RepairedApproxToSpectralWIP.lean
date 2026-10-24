/-!
account02/B10 WIP — exact repaired Proposition 6.4 spectral-input bridge.
Target paper blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a.
UNVERIFIED: no local Lean/lake/elan runtime. Do not count without matching build + #print axioms evidence.
Intended after the already-compiled repaired FiveS2Weyl and FiveS2Schur definitions are available.
-/

open Matrix

namespace QformFiveB

theorem sqApprox_one_of_weylApprox {n d : ℕ}
    (A : Matrix (Fin n) (Fin n) ℝ)
    (h : Weyl.ApproxGE d 1 A) :
    SqApprox d 1 A := by
  intro R hR
  obtain ⟨v, hv0, hv⟩ := h R hR
  refine ⟨v, hv0, ?_⟩
  have hlin : Weyl.nrm v ≤ Weyl.nrm ((A - R) *ᵥ v) := by
    simpa using hv
  have hsquared :
      Weyl.nrm v ^ 2 ≤ Weyl.nrm ((A - R) *ᵥ v) ^ 2 := by
    nlinarith [hlin, Weyl.nrm_nonneg v,
      Weyl.nrm_nonneg ((A - R) *ᵥ v)]
  rw [Weyl.nrm_sq, Weyl.nrm_sq] at hsquared
  simpa [Weyl.nsq, nsq] using hsquared

theorem card_abs_eig_of_weylApprox_one {n d : ℕ}
    (A : Matrix (Fin n) (Fin n) ℝ) (hA : A.IsHermitian)
    (h : Weyl.ApproxGE d 1 A) :
    d ≤ Fintype.card {i // (1 : ℝ) ≤ |hA.eigenvalues i|} := by
  exact card_abs_eig_of_sqapprox A hA d 1 (by norm_num)
    (sqApprox_one_of_weylApprox A h)

theorem eigenframe_of_weylApprox_one {n d : ℕ}
    (A : Matrix (Fin n) (Fin n) ℝ) (hA : A.IsHermitian)
    (h : Weyl.ApproxGE d 1 A) :
    ∃ (Φ : Matrix (Fin n) (Fin d) ℝ) (lam : Fin d → ℝ),
      Φᵀ * Φ = 1 ∧ A * Φ = Φ * diagonal lam ∧ ∀ c, 1 ≤ |lam c| := by
  exact eigenframe A hA d 1
    (card_abs_eig_of_weylApprox_one A hA h)

end QformFiveB
