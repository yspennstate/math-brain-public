/-!
account03/B01 r06 WIP. Exact repaired Section 6 statement adapters.
Target paper.tex commit 4e530247ec0ef4101a6e5ecf621bd35a969c42aa,
blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a.

UNVERIFIED: this runtime has no Lean/lake executable. Append after the already
compiled historical QformFive3.lean. No theorem below gets verification credit
until an exact matching Lean/Mathlib build succeeds and #print axioms is checked.
-/

namespace QformFive

def uniformSignExpectation {n : ℕ} (F : (Fin n → Bool) → ℝ) : ℝ :=
  (∑ x, F x) / (2 : ℝ) ^ n

theorem frobenius_moment_uniform {n k : ℕ}
    (o : Fin n → Fin n → ℝ) (φ : Fin n → Fin k → ℝ) :
    uniformSignExpectation (fun x =>
      ∑ a, ∑ b,
        (∑ i, ∑ j, chaos (fun i j => o i j * φ i a * φ j b) x i j) ^ 2)
      = ∑ i, ∑ j, (if i ≠ j then
          o i j * (o i j * (∑ a, φ i a ^ 2) * (∑ b, φ j b ^ 2)
                   + o j i * (∑ a, φ i a * φ j a) ^ 2) else 0) := by
  unfold uniformSignExpectation
  rw [frobenius_moment]
  rw [mul_div_cancel_left₀ _ (by positivity)]

theorem frobenius_moment_uniform_le {n k : ℕ}
    (o : Fin n → Fin n → ℝ) (φ : Fin n → Fin k → ℝ) (a : ℝ)
    (hsym : ∀ i j, o j i = o i j)
    (hbd : ∀ i j, i ≠ j → |o i j| ≤ a) :
    uniformSignExpectation (fun x =>
      ∑ c, ∑ d,
        (∑ i, ∑ j, chaos (fun i j => o i j * φ i c * φ j d) x i j) ^ 2)
      ≤ 2 * a ^ 2 * (∑ i, ∑ c, φ i c ^ 2) ^ 2 := by
  rw [frobenius_moment_uniform]
  exact frobenius_bound o φ a hsym hbd

noncomputable def repairedGamma (m : ℕ) : ℝ :=
  (44 - 5 * Real.sqrt 2 * (((2 * m - 1 : ℕ) : ℝ))) / 96

noncomputable def repairedSigma (m : ℕ) (δ : ℝ) : ℝ :=
  (1 - δ - Real.sqrt 2 * (5 / 48 : ℝ) *
    (((2 * m - 1 : ℕ) : ℝ))) / 2

theorem repairedGamma_identity (m : ℕ) :
    repairedGamma m = repairedSigma m (1 / 12) := by
  unfold repairedGamma repairedSigma
  ring

theorem repairedGamma_lt_sigma_of_diag_strict
    (m : ℕ) (δ : ℝ) (hδ : δ < (1 / 12 : ℝ)) :
    repairedGamma m < repairedSigma m δ := by
  rw [repairedGamma_identity]
  unfold repairedSigma
  linarith

end QformFive
