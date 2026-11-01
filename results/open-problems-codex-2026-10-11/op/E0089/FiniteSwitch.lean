def present (mask v : Nat) : Bool := mask / 2^v % 2 == 1
def adjG (v w : Nat) : Bool := (v < 4 && 4 <= w) || (w < 4 && 4 <= v)
def adjH (v w : Nat) : Bool :=
  if (v == 0 && w == 4) || (v == 4 && w == 0) ||
     (v == 1 && w == 5) || (v == 5 && w == 1) then false
  else adjG v w || (v == 0 && w == 1) || (v == 1 && w == 0) ||
       (v == 4 && w == 5) || (v == 5 && w == 4)
def step (adj : Nat → Nat → Bool) (mask : Nat) : Nat :=
  (List.range 8).foldl (fun out v =>
    if present mask v || ((List.range 8).filter (fun w => adj v w && present mask w)).length >= 2
    then out + 2^v else out) 0
def closure (adj : Nat → Nat → Bool) (mask : Nat) : Nat :=
  (List.range 8).foldl (fun out _ => step adj out) mask

theorem graph_regular : (List.range 8).all (fun v =>
  ((List.range 8).filter (adjG v)).length == 4 &&
  ((List.range 8).filter (adjH v)).length == 4) = true := by decide +kernel

theorem switching_changes_seed : closure adjG 17 = 17 ∧ closure adjH 17 = 255 := by
  decide +kernel

theorem forced_endpoints : (List.range 256).all (fun m =>
  closure adjG (Nat.lor m 51) == closure adjH (Nat.lor m 51)) = true := by
  decide +kernel
