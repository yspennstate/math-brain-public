import Std.Tactic.Omega

theorem quarter_bank_scaled (scale ell debit surplus : Int)
    (hscale : 0 < scale) (hell : 2 * scale <= ell)
    (hd : 2 * debit < ell + 2 * scale)
    (hs : 9 * ell + 4 * scale <= 2 * surplus) :
    4 * debit < surplus := by
  omega
