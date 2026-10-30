import Std.Tactic

theorem ledger_cancel (r e h d t : Int) (hx : r + e - t = h + d) : r + e = h + d + t := by omega
