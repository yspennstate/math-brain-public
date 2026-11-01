import Init

-- Core Lean checks finite truth tables and raw Walsh transforms only.
-- Entropy/logarithm interpretation and the all-d theorem are in PROOF.md.
def paritySign (mask x : Nat) : Int :=
  let c := (if mask.testBit 0 && x.testBit 0 then 1 else 0) +
           (if mask.testBit 1 && x.testBit 1 then 1 else 0) +
           (if mask.testBit 2 && x.testBit 2 then 1 else 0)
  if c % 2 == 0 then 1 else -1

def root (x : Nat) : Int :=
  let v : Int := if x.testBit 1 == x.testBit 2 then 1 else -1
  let w : Int := if x.testBit 2 then -1 else 1
  if x.testBit 0 then w else v

def rawWalsh (f : Nat → Int) (N mask : Nat) : Int :=
  ((List.range N).map (fun x => f x * paritySign mask x)).foldl (· + ·) 0

def childPlus (x : Nat) : Int := root ((x % 2) + 4 * (x / 2))
def childMinus (x : Nat) : Int := root ((x % 2) + 2 + 4 * (x / 2))

theorem profile_witness :
    (List.range 8).map (rawWalsh root 8) = [0,0,0,0,4,-4,4,4] ∧
    (List.range 4).map (rawWalsh childPlus 4) = [0,0,4,0] ∧
    (List.range 4).map (rawWalsh childMinus 4) = [0,0,0,-4] ∧
    ((List.range 8).filter (fun x => root x != root (x ^^^ 2))).length = 4 ∧
    rawWalsh (fun x => if x.testBit 0 == x.testBit 1 then 1 else -1) 4 0 = 0 ∧
    rawWalsh (fun x => if x.testBit 1 then -1 else 1) 4 0 = 0 := by
  decide
