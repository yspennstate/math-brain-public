import Lean

theorem A034_column_fibers (a b : Bool) :
  ((([(false, false), (false, true), (true, false), (true, true)] : List (Bool × Bool)).filter
    (fun t => !(Bool.xor (a && t.1) (b && t.2)))).length =
    (if a || b then 2 else 4) := by
  cases a <;> cases b <;> decide
