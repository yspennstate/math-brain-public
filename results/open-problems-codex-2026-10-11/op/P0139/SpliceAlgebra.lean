import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

-- Planar signed wedge. All proofs use the kernel-checked ring tactic.
def wedge (x1 x2 y1 y2 : Real) : Real := x1 * y2 - x2 * y1

theorem splice_increment
    (ys1 ys2 yt1 yt2 es1 es2 et1 et2 Ays Ayt Bs Bt : Real) :
    (Ayt + Bt + (1/2 : Real) * wedge yt1 yt2 et1 et2) -
    (Ays + Bs + (1/2 : Real) * wedge ys1 ys2 es1 es2) -
    (1/2 : Real) * wedge (ys1+es1) (ys2+es2) (yt1+et1) (yt2+et2) =
    (Ayt-Ays-(1/2 : Real)*wedge ys1 ys2 yt1 yt2) + Bt-Bs +
    (1/2 : Real)*wedge (yt1-ys1) (yt2-ys2) (et1+es1) (et2+es2) -
    (1/2 : Real)*wedge es1 es2 et1 et2 := by
  unfold wedge
  ring

theorem wedge_difference
    (ks1 ks2 kt1 kt2 hs1 hs2 ht1 ht2 : Real) :
    wedge ks1 ks2 kt1 kt2 - wedge hs1 hs2 ht1 ht2 =
    wedge (ks1-hs1) (ks2-hs2) kt1 kt2 +
    wedge hs1 hs2 (kt1-ht1) (kt2-ht2) := by
  unfold wedge
  ring

theorem chen_area_cocycle (x1 x2 y1 y2 z1 z2 : Real) :
    (1/2 : Real)*wedge x1 x2 y1 y2 +
    (1/2 : Real)*wedge (x1+y1) (x2+y2) z1 z2 =
    (1/2 : Real)*wedge y1 y2 z1 z2 +
    (1/2 : Real)*wedge x1 x2 (y1+z1) (y2+z2) := by
  unfold wedge
  ring

theorem closed_loop_central (a b : Real) :
    a+b+(1/2 : Real)*wedge 0 0 0 0 = a+b := by
  unfold wedge
  ring
