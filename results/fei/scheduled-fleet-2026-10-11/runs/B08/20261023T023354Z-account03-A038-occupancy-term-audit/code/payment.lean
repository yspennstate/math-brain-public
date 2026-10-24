-- UNCOMPILED: fresh memory-admission gate refused this stage.
-- This is only the scalar account, not the Fourier/occupancy theorem.
import Mathlib.Tactic.Linarith

theorem conservative_reset_payment (S A B w L : Real)
    (h : S - L >= 2 - A) (ha : A < 39/32)
    (hb : B <= 7/32) (hw : w <= 11/32) :
    S - (L + w + B) > 7/32 := by
  linarith
