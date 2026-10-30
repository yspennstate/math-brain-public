import Lean.Elab.Command
import Lean.Util.CollectAxioms
import Lean.Data.Json.Printer
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

open _root_.Lean _root_.Lean.Elab _root_.Lean.Elab.Command in
run_cmd do
  let expected : _root_.Lean.Name := (_root_.Lean.Name.str _root_.Lean.Name.anonymous "profile_witness")
  let ci ← _root_.Lean.getConstInfo expected
  let rec encodeName (n : _root_.Lean.Name) : _root_.Lean.Json :=
    match n with
    | .anonymous => .arr #[.str "anonymous"]
    | .str parent part => .arr #[.str "str", encodeName parent, .str part]
    | .num parent number => .arr #[.str "num", encodeName parent, .str (_root_.Nat.repr number)]
  let identity := _root_.Lean.Json.compress (encodeName ci.name)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_NAME profile_witness: " identity)))
  match ci with
  | .thmInfo _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND profile_witness: theorem=true"))
  | _ => _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text "TARGET_KIND profile_witness: theorem=false"))
  let axioms ← _root_.Lean.collectAxioms expected
  let encoded := _root_.Array.map encodeName axioms
  let dependencies := _root_.Lean.Json.compress (_root_.Lean.Json.arr encoded)
  _root_.Lean.logInfo (_root_.Lean.MessageData.ofFormat (_root_.Std.Format.text (_root_.String.append "TARGET_AXIOMS profile_witness: " dependencies)))
