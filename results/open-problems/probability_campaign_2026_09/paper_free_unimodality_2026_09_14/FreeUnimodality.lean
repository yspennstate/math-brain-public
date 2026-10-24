import Mathlib

/-!
# The sharp diameter threshold for unimodality of free Brownian motion: the algebraic core

Companion to the paper *The sharp diameter threshold for unimodality of free Brownian motion*
(answer to Problem 3.3 of Hasebe and Ueda, ALEA 15 (2018)): the theorem that `μ ⊞ S(0,t)` is
unimodal for every `t ≥ D_μ²`, with `D_μ` the diameter of the support of `μ`, and that the
constant is sharp.

What is checked here is every algebraic step of both proofs, over the real field:

* the two-atom identities behind the Choquet route (`pair_F_sub_one`, `pair_H`), their collapse
  to the elementary symmetric functions `D = a + b`, `m = ab` (`Psi_collapse`, `Phi_collapse`),
  Lemma A (`lemmaA`) and Lemma B (`lemmaB`), and the equality case of Lemma B (`lemmaB_eq`);
* the Cauchy-profile route: the factorisation and sign (`cauchy_profile_bound`);
* the symmetric two-point law at its critical radius: a strict maximum, never a local minimum
  (`bernoulli_profile`, `bernoulli_profile_lt`);
* the classical companion: the pair identity `H = θ (a+b) (1 - t/(ab))` (`classical_pair`) and the
  bound `ab ≤ D²/4` under `a + b ≤ D` (`ab_le`).

What is NOT formalised: Biane's description of the density, Lemma 3.1 of the source (the level-set
criterion), the extreme-point (Choquet / Winkler) reduction, and the measure-theoretic assembly.
Those are cited in the paper. The file compiles with Lean 4.33.1 and the Mathlib pinned in this
project; `#print axioms` on each theorem reports only `propext`, `Classical.choice`, `Quot.sound`.
-/

namespace FreeUnimodality

open Real

/-! ### The two-atom reduction (Choquet route)

A pair of atoms at `-a` and `b` (`a, b > 0`) with the stationarity condition `G = 0` has weights
proportional to `b A²` at `-a` and `a B²` at `b`, where `A = a² + s`, `B = b² + s`, `s = R²`.
With `Δ = bA² + aB²` the normalised weights are `bA²/Δ` and `aB²/Δ`. -/

/-- `F - 1 = Φ / Δ` for the pair, where `F = w₋ / A + w₊ / B`. -/
theorem pair_F_sub_one (a b s : ℝ) (ha : 0 < a) (hb : 0 < b) (hs : 0 < s) :
    let A := a ^ 2 + s
    let B := b ^ 2 + s
    let Δ := b * A ^ 2 + a * B ^ 2
    (b * A ^ 2 / Δ) / A + (a * B ^ 2 / Δ) / B - 1
      = (b * A * (1 - A) + a * B * (1 - B)) / Δ := by
  intro A B Δ
  have hA : A ≠ 0 := by positivity
  have hB : B ≠ 0 := by positivity
  have hΔ : Δ ≠ 0 := by positivity
  field_simp
  ring

/-- `H = Ψ / (Δ A B)` for the pair, where `H = w₋ (3a² - s)/A³ + w₊ (3b² - s)/B³`. -/
theorem pair_H (a b s : ℝ) (ha : 0 < a) (hb : 0 < b) (hs : 0 < s) :
    let A := a ^ 2 + s
    let B := b ^ 2 + s
    let Δ := b * A ^ 2 + a * B ^ 2
    (b * A ^ 2 / Δ) * (3 * a ^ 2 - s) / A ^ 3 + (a * B ^ 2 / Δ) * (3 * b ^ 2 - s) / B ^ 3
      = (b * B * (3 * a ^ 2 - s) + a * A * (3 * b ^ 2 - s)) / (Δ * A * B) := by
  intro A B Δ
  have hA : A ≠ 0 := by positivity
  have hB : B ≠ 0 := by positivity
  have hΔ : Δ ≠ 0 := by positivity
  field_simp

/-- `Ψ = D (3m² + s(6m - D²) - s²)` with `D = a + b`, `m = ab`. -/
theorem Psi_collapse (a b s : ℝ) :
    b * (b ^ 2 + s) * (3 * a ^ 2 - s) + a * (a ^ 2 + s) * (3 * b ^ 2 - s)
      = (a + b) * (3 * (a * b) ^ 2 + s * (6 * (a * b) - (a + b) ^ 2) - s ^ 2) := by
  ring

/-- `Φ = D (3m² + m(1 - D²) + s(1 - 2m) - s²)` with `D = a + b`, `m = ab`. -/
theorem Phi_collapse (a b s : ℝ) :
    b * (a ^ 2 + s) * (1 - (a ^ 2 + s)) + a * (b ^ 2 + s) * (1 - (b ^ 2 + s))
      = (a + b) * (3 * (a * b) ^ 2 + (a * b) * (1 - (a + b) ^ 2) + s * (1 - 2 * (a * b)) - s ^ 2) := by
  ring

/-- `ab ≤ (a+b)²/4`. -/
theorem ab_le (a b : ℝ) : a * b ≤ (a + b) ^ 2 / 4 := by
  nlinarith [sq_nonneg (a - b)]

/-- Lemma A: if the pair has `H ≥ 0` (that is `Ψ/D ≥ 0`) then `s ≤ 3D²/4`. -/
theorem lemmaA (D m s : ℝ) (hm0 : 0 < m) (hm : m ≤ D ^ 2 / 4) (hs : 0 < s)
    (hΨ : 0 ≤ 3 * m ^ 2 + s * (6 * m - D ^ 2) - s ^ 2) : s ≤ 3 * D ^ 2 / 4 := by
  -- Ψ/D is increasing in m, so its value at m = D²/4, namely (3D² - 4s)(D² + 4s)/16, is ≥ 0.
  nlinarith [mul_pos hm0 hs, sq_nonneg (D ^ 2 / 4 - m), mul_nonneg hs.le (sub_nonneg.2 hm)]

/-- Lemma B: if `0 ≤ s ≤ 3/4`, `0 < D ≤ 1` and `0 < m ≤ D²/4` then `Φ/D ≥ 0`. -/
theorem lemmaB (D m s : ℝ) (hD0 : 0 < D) (hD : D ≤ 1) (hm0 : 0 < m) (hm : m ≤ D ^ 2 / 4)
    (hs0 : 0 ≤ s) (hs : s ≤ 3 / 4) :
    0 ≤ 3 * m ^ 2 + m * (1 - D ^ 2) + s * (1 - 2 * m) - s ^ 2 := by
  -- concave in s, so it suffices to check s = 0 and s = 3/4; at s = 3/4 the quadratic in m is
  -- decreasing on (0, D²/4] with value (1 - D²)(D² + 3)/16 ≥ 0 at the right endpoint.
  have hD2 : D ^ 2 ≤ 1 := by nlinarith
  nlinarith [mul_nonneg hs0 (sub_nonneg.2 hs), mul_nonneg hm0.le (sub_nonneg.2 hm),
    mul_nonneg hs0 (sub_nonneg.2 hD2), mul_nonneg (sub_nonneg.2 hs) (sub_nonneg.2 hD2),
    mul_nonneg hm0.le (sub_nonneg.2 hD2), sq_nonneg (D ^ 2 / 4 - m), mul_nonneg hs0 hm0.le,
    mul_nonneg (sub_nonneg.2 hs) (sub_nonneg.2 hm)]

/-- Equality in Lemma B forces the symmetric two-point law at its critical radius:
`Φ/D = 0` with `s ≤ 3/4`, `D ≤ 1`, `0 < m ≤ D²/4` only if `D = 1`, `m = 1/4`, `s = 3/4`. -/
theorem lemmaB_eq (D m s : ℝ) (hD0 : 0 < D) (hD : D ≤ 1) (hm0 : 0 < m) (hm : m ≤ D ^ 2 / 4)
    (hs0 : 0 ≤ s) (hs : s ≤ 3 / 4)
    (h : 3 * m ^ 2 + m * (1 - D ^ 2) + s * (1 - 2 * m) - s ^ 2 = 0) :
    D = 1 ∧ m = 1 / 4 ∧ s = 3 / 4 := by
  have hD2 : D ^ 2 ≤ 1 := by nlinarith
  -- the value at s = 0 is positive
  have f0 : 0 < 3 * m ^ 2 + m * (1 - D ^ 2) := by
    nlinarith [mul_nonneg hm0.le (sub_nonneg.2 hD2), sq_nonneg m]
  -- the value at s = 3/4 is (m - D²/4)(3m - D²/4 - 1/2) + (1 - D²)(D² + 3)/16, both terms ≥ 0
  have hlin : 0 ≤ 1 / 2 + D ^ 2 / 4 - 3 * m := by nlinarith
  have q1 : 0 ≤ (D ^ 2 / 4 - m) * (1 / 2 + D ^ 2 / 4 - 3 * m) :=
    mul_nonneg (sub_nonneg.2 hm) hlin
  have q2 : 0 ≤ (1 - D ^ 2) * (D ^ 2 + 3) := mul_nonneg (sub_nonneg.2 hD2) (by positivity)
  have f34 : 3 * m ^ 2 - m * (D ^ 2 + 1 / 2) + 3 / 16
      = (D ^ 2 / 4 - m) * (1 / 2 + D ^ 2 / 4 - 3 * m) + (1 - D ^ 2) * (D ^ 2 + 3) / 16 := by ring
  -- the concavity identity in s
  have hid : 3 * m ^ 2 + m * (1 - D ^ 2) + s * (1 - 2 * m) - s ^ 2
      = (1 - 4 * s / 3) * (3 * m ^ 2 + m * (1 - D ^ 2))
        + (4 * s / 3) * (3 * m ^ 2 - m * (D ^ 2 + 1 / 2) + 3 / 16) + s * (3 / 4 - s) := by ring
  have f34nn : 0 ≤ 3 * m ^ 2 - m * (D ^ 2 + 1 / 2) + 3 / 16 := by rw [f34]; linarith
  have hs' : s = 3 / 4 := by
    by_contra hne
    have hlt : s < 3 / 4 := lt_of_le_of_ne hs hne
    have t1 : 0 < (1 - 4 * s / 3) * (3 * m ^ 2 + m * (1 - D ^ 2)) :=
      mul_pos (by linarith) f0
    have t2 : 0 ≤ (4 * s / 3) * (3 * m ^ 2 - m * (D ^ 2 + 1 / 2) + 3 / 16) :=
      mul_nonneg (by linarith) f34nn
    have t3 : 0 ≤ s * (3 / 4 - s) := mul_nonneg hs0 (by linarith)
    rw [hid] at h
    linarith
  subst hs'
  -- now h says the s = 3/4 value vanishes, so both nonnegative terms vanish
  have hq : (D ^ 2 / 4 - m) * (1 / 2 + D ^ 2 / 4 - 3 * m) + (1 - D ^ 2) * (D ^ 2 + 3) / 16 = 0 := by
    rw [← f34]; linarith
  have z2 : (1 - D ^ 2) * (D ^ 2 + 3) = 0 := by linarith
  have hD' : D = 1 := by
    have : 1 - D ^ 2 = 0 := by
      rcases mul_eq_zero.1 z2 with h1 | h1
      · exact h1
      · nlinarith
    nlinarith
  subst hD'
  have z1 : (1 / 4 - m) * (3 / 4 - 3 * m) = 0 := by
    have : ((1:ℝ) ^ 2 / 4 - m) * (1 / 2 + (1:ℝ) ^ 2 / 4 - 3 * m) = 0 := by linarith
    nlinarith [this]
  have hm' : m = 1 / 4 := by
    rcases mul_eq_zero.1 z1 with h1 | h1 <;> linarith
  exact ⟨rfl, hm', rfl⟩

/-! ### The Cauchy-profile route -/

/-- With `a = E_Q (X-u)²`, `b = E_Q (X-u)⁴`, `y = R²`: from `b + 3a² ≤ D² a`, `y ≤ 3a`, `4a ≤ D²`
one gets `(b + 2ay + y²)/(a + y) ≤ D²`, that is `1/F_R(u) ≤ D²`. -/
theorem cauchy_profile_bound (a b y D : ℝ) (ha : 0 < a) (hy : 0 < y)
    (hb : b + 3 * a ^ 2 ≤ D ^ 2 * a) (hya : y ≤ 3 * a) (haD : 4 * a ≤ D ^ 2) :
    (b + 2 * a * y + y ^ 2) / (a + y) ≤ D ^ 2 := by
  rw [div_le_iff₀ (by positivity)]
  nlinarith [mul_nonneg (sub_nonneg.2 hya) (by positivity : (0:ℝ) ≤ y + a),
    mul_nonneg (sub_nonneg.2 haD) hy.le]

/-- The symmetric two-point law on `{-c, c}` at `R² = 3c²`:
`F_R(s) - 1/(4c²) = - s⁴ / (4c² (s⁴ + 4c² s² + 16c⁴))`. -/
theorem bernoulli_profile (c s : ℝ) (hc : 0 < c) :
    (1 / 2) * (1 / ((c - s) ^ 2 + 3 * c ^ 2) + 1 / ((c + s) ^ 2 + 3 * c ^ 2)) - 1 / (4 * c ^ 2)
      = - s ^ 4 / (4 * c ^ 2 * (s ^ 4 + 4 * c ^ 2 * s ^ 2 + 16 * c ^ 4)) := by
  have h1 : (c - s) ^ 2 + 3 * c ^ 2 ≠ 0 := by positivity
  have h2 : (c + s) ^ 2 + 3 * c ^ 2 ≠ 0 := by positivity
  have h3 : s ^ 4 + 4 * c ^ 2 * s ^ 2 + 16 * c ^ 4 ≠ 0 := by positivity
  field_simp
  ring

/-- Hence the critical-radius profile of the symmetric two-point law is strictly below its value at
the centre away from the centre: the centre is a strict maximum, not a local minimum. -/
theorem bernoulli_profile_lt (c s : ℝ) (hc : 0 < c) (hs : s ≠ 0) :
    (1 / 2) * (1 / ((c - s) ^ 2 + 3 * c ^ 2) + 1 / ((c + s) ^ 2 + 3 * c ^ 2)) < 1 / (4 * c ^ 2) := by
  have h := bernoulli_profile c s hc
  have hpos : 0 < s ^ 4 / (4 * c ^ 2 * (s ^ 4 + 4 * c ^ 2 * s ^ 2 + 16 * c ^ 4)) := by
    have : 0 < s ^ 4 := by positivity
    positivity
  rw [neg_div] at h
  linarith

/-! ### The classical companion -/

/-- For a pair at `-a`, `b` with `p a φ(a) = q b φ(b) = θ`, the second-derivative functional is
`θ (a + b) (1 - t/(ab))`. -/
theorem classical_pair (a b t θ : ℝ) (ha : 0 < a) (hb : 0 < b) :
    θ / a * (a ^ 2 - t) + θ / b * (b ^ 2 - t) = θ * (a + b) * (1 - t / (a * b)) := by
  field_simp
  ring

/-- So `H ≥ 0` for the pair (with `θ > 0`) forces `t ≤ ab ≤ D²/4` when `a + b ≤ D`. -/
theorem classical_threshold (a b t θ D : ℝ) (ha : 0 < a) (hb : 0 < b) (hθ : 0 < θ)
    (hab : a + b ≤ D) (hH : 0 ≤ θ / a * (a ^ 2 - t) + θ / b * (b ^ 2 - t)) :
    t ≤ D ^ 2 / 4 := by
  rw [classical_pair a b t θ ha hb] at hH
  have hab' : 0 < a * b := by positivity
  have hpos : 0 < θ * (a + b) := by positivity
  have h1 : 0 ≤ 1 - t / (a * b) := by
    by_contra hneg
    have hneg' : 1 - t / (a * b) < 0 := lt_of_not_ge hneg
    have := mul_neg_of_pos_of_neg hpos hneg'
    linarith
  have h2 : t ≤ a * b := by
    have := sub_nonneg.1 h1
    rwa [div_le_one hab'] at this
  have h3 : a * b ≤ (a + b) ^ 2 / 4 := ab_le a b
  have h4 : (a + b) ^ 2 ≤ D ^ 2 := by
    have : 0 ≤ a + b := by positivity
    nlinarith
  linarith

end FreeUnimodality

#print axioms FreeUnimodality.pair_F_sub_one
#print axioms FreeUnimodality.pair_H
#print axioms FreeUnimodality.Psi_collapse
#print axioms FreeUnimodality.Phi_collapse
#print axioms FreeUnimodality.ab_le
#print axioms FreeUnimodality.lemmaA
#print axioms FreeUnimodality.lemmaB
#print axioms FreeUnimodality.lemmaB_eq
#print axioms FreeUnimodality.cauchy_profile_bound
#print axioms FreeUnimodality.bernoulli_profile
#print axioms FreeUnimodality.bernoulli_profile_lt
#print axioms FreeUnimodality.classical_pair
#print axioms FreeUnimodality.classical_threshold
