/-
Arithmetic core of affine transfer for the uniform doubling condition.

This file formalizes the elementary real-variable steps used in
`paper2/udc_whp.tex`, Proposition `prop:affine-transfer`:

* image widths `t` in the interval `[Lam * ell, lam * beta / k)` pull back to
  source widths `t / a` in `[ell, beta / k)` whenever `lam <= a <= Lam`;
* the same interval transfer in the all-width form, without the extra `1 / k`;
* a measure identity `muA t = mu (t / a)` transfers the source doubling
  inequality to the image inequality;
* grid-scale doubling interpolates to all intermediate widths at multiplier
  `k^2` by monotonicity.

The actual slab geometry, singular-value estimate, and empirical pushforward
identity remain paper-level hypotheses. The formalization verifies the
arithmetic and order manipulations where constants are most likely to drift.

Compiles against mathlib (see `README.md`).
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace UdcAffineTransferArithmetic

/-- If an image slab has width `t` in the affine-transfer grid range and the
normal-stretch factor `a` satisfies `lam <= a <= Lam`, then its preimage width
`t / a` lies in the source range `[ell, beta / k)`. -/
theorem preimage_width_mem_grid
    {k lam Lam beta ell a t : Real}
    (hk : 0 < k) (hlam : 0 < lam) (hbeta : 0 <= beta) (hell : 0 <= ell)
    (ha_lam : lam <= a) (ha_Lam : a <= Lam)
    (ht_lower : Lam * ell <= t) (ht_upper : t < lam * beta / k) :
    And (ell <= t / a) (t / a < beta / k) := by
  have ha : 0 < a := lt_of_lt_of_le hlam ha_lam
  constructor
  next =>
    have hscale : a * ell <= t := by
      have h0 : a * ell <= Lam * ell := mul_le_mul_of_nonneg_right ha_Lam hell
      nlinarith
    field_simp [ha.ne']
    nlinarith
  next =>
    have h1 : t / a < (lam * beta / k) / a :=
      div_lt_div_of_pos_right ht_upper ha
    have hscale : lam * beta <= a * beta :=
      mul_le_mul_of_nonneg_right ha_lam hbeta
    have h2 : (lam * beta / k) / a <= beta / k := by
      field_simp [ha.ne', hk.ne']
      nlinarith
    exact lt_of_lt_of_le h1 h2

/-- All-width version of `preimage_width_mem_grid`, with target range
`[Lam * ell, lam * beta)`. -/
theorem preimage_width_mem_allwidth
    {lam Lam beta ell a t : Real}
    (hlam : 0 < lam) (hbeta : 0 <= beta) (hell : 0 <= ell)
    (ha_lam : lam <= a) (ha_Lam : a <= Lam)
    (ht_lower : Lam * ell <= t) (ht_upper : t < lam * beta) :
    And (ell <= t / a) (t / a < beta) := by
  have ha : 0 < a := lt_of_lt_of_le hlam ha_lam
  constructor
  next =>
    have hscale : a * ell <= t := by
      have h0 : a * ell <= Lam * ell := mul_le_mul_of_nonneg_right ha_Lam hell
      nlinarith
    field_simp [ha.ne']
    nlinarith
  next =>
    have h1 : t / a < (lam * beta) / a :=
      div_lt_div_of_pos_right ht_upper ha
    have hscale : lam * beta <= a * beta :=
      mul_le_mul_of_nonneg_right ha_lam hbeta
    have h2 : (lam * beta) / a <= beta := by
      field_simp [ha.ne']
      nlinarith
    exact lt_of_lt_of_le h1 h2

/-- Arithmetic transfer of the grid-form source inequality under a width
pullback identity `muA t = mu (t / a)`. This is the non-geometric core of the
grid-form affine-transfer proposition. -/
theorem affine_grid_transfer_arithmetic
    (muA mu : Real -> Real) {k delta sigma beta ell lam Lam a : Real}
    (hk : 0 < k) (hlam : 0 < lam) (hbeta : 0 <= beta) (hell : 0 <= ell)
    (ha_lam : lam <= a) (ha_Lam : a <= Lam)
    (hpull : forall t, muA t = mu (t / a))
    (hsrc : forall w, ell <= w -> w < beta / k ->
      min delta ((1 + sigma) * mu w) <= mu (k ^ 2 * w)) :
    forall t, Lam * ell <= t -> t < lam * beta / k ->
      min delta ((1 + sigma) * muA t) <= muA (k ^ 2 * t) := by
  intro t ht_lower ht_upper
  have hw :=
    preimage_width_mem_grid hk hlam hbeta hell ha_lam ha_Lam ht_lower ht_upper
  have h := hsrc (t / a) hw.1 hw.2
  rw [hpull t, hpull (k ^ 2 * t)]
  simpa [div_eq_mul_inv, mul_assoc, mul_left_comm, mul_comm] using h

/-- Arithmetic transfer of the all-width source inequality under a width
pullback identity `muA t = mu (t / a)`. -/
theorem affine_allwidth_transfer_arithmetic
    (muA mu : Real -> Real) {k delta sigma beta ell lam Lam a : Real}
    (hlam : 0 < lam) (hbeta : 0 <= beta) (hell : 0 <= ell)
    (ha_lam : lam <= a) (ha_Lam : a <= Lam)
    (hpull : forall t, muA t = mu (t / a))
    (hsrc : forall w, ell <= w -> w < beta ->
      min delta ((1 + sigma) * mu w) <= mu (k * w)) :
    forall t, Lam * ell <= t -> t < lam * beta ->
      min delta ((1 + sigma) * muA t) <= muA (k * t) := by
  intro t ht_lower ht_upper
  have hw := preimage_width_mem_allwidth hlam hbeta hell ha_lam ha_Lam ht_lower ht_upper
  have h := hsrc (t / a) hw.1 hw.2
  rw [hpull t, hpull (k * t)]
  simpa [div_eq_mul_inv, mul_assoc, mul_left_comm, mul_comm] using h

/-- Grid interpolation by monotonicity. If `w` lies between two adjacent grid
widths and below `beta / k`, then the grid inequality at the next grid point
implies the all-width inequality at `w`, with multiplier `k^2`. -/
theorem grid_step_interpolation
    (mu : Real -> Real) {k delta sigma beta ell w : Real} {i : Nat}
    (hk : 1 < k) (hsigma : 0 <= 1 + sigma) (hmono : Monotone mu)
    (hgrid : forall j : Nat, ell * k ^ j < beta ->
      min delta ((1 + sigma) * mu (ell * k ^ j)) <= mu (ell * k ^ (j + 1)))
    (hleft : ell * k ^ i <= w) (hright : w <= ell * k ^ (i + 1))
    (hupper : w < beta / k) :
    min delta ((1 + sigma) * mu w) <= mu (k ^ 2 * w) := by
  have hk0 : 0 < k := lt_trans zero_lt_one hk
  have hkw : k * w < beta := by
    have hupper' := hupper
    field_simp [hk0.ne'] at hupper'
    nlinarith
  have hnext_le : ell * k ^ (i + 1) <= k * w := by
    have hmul : k * (ell * k ^ i) <= k * w :=
      mul_le_mul_of_nonneg_left hleft (le_of_lt hk0)
    calc
      ell * k ^ (i + 1) = k * (ell * k ^ i) := by
        rw [pow_succ]
        ring
      _ <= k * w := hmul
  have hgrid_arg : ell * k ^ (i + 1) < beta := lt_of_le_of_lt hnext_le hkw
  have hgrid_step_raw := hgrid (i + 1) hgrid_arg
  have hgrid_step :
      min delta ((1 + sigma) * mu (ell * k ^ (i + 1))) <=
        mu (ell * k ^ (i + 2)) := by
    simpa [Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using hgrid_step_raw
  have htarget_arg : ell * k ^ (i + 2) <= k ^ 2 * w := by
    have hmul : k ^ 2 * (ell * k ^ i) <= k ^ 2 * w :=
      mul_le_mul_of_nonneg_left hleft (sq_nonneg k)
    calc
      ell * k ^ (i + 2) = k ^ 2 * (ell * k ^ i) := by
        rw [pow_add]
        ring
      _ <= k ^ 2 * w := hmul
  have htarget : mu (ell * k ^ (i + 2)) <= mu (k ^ 2 * w) :=
    hmono htarget_arg
  have hmu : mu w <= mu (ell * k ^ (i + 1)) := hmono hright
  have hscaled :
      (1 + sigma) * mu w <= (1 + sigma) * mu (ell * k ^ (i + 1)) :=
    mul_le_mul_of_nonneg_left hmu hsigma
  have hmin :
      min delta ((1 + sigma) * mu w) <=
        min delta ((1 + sigma) * mu (ell * k ^ (i + 1))) :=
    min_le_min_left delta hscaled
  exact le_trans hmin (le_trans hgrid_step htarget)

end UdcAffineTransferArithmetic
