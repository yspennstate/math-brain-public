import Std.Tactic

theorem a027_ledger (raw terminal loss : Int) (h : raw = terminal + loss) : raw - terminal = loss := by omega
