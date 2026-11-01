import Init.Data.Rat.Lemmas

namespace A083
-- Each residual mask has equal nonzero mass in both actual y children.
-- These are literal unnormalized Walsh numerators of the two 2-bit leaves.
def leaf0 : List Int := [-2, 2, 2, 2]
def leaf1 : List Int := [2, -2, 2, 2]
def squares (xs : List Int) : List Int := xs.map (fun x => x*x)
theorem actual_leaf_squares :
    squares leaf0 = [4,4,4,4] ∧ squares leaf1 = [4,4,4,4] := by decide

-- With both normalized child masses 1/4, the SAME branch kernel is fair.
-- No zero-row fallback can be invoked at this query.
theorem actual_fair_kernel :
    (1/4 : Rat) / (2*((1/4+1/4)/2)) = 1/2 := by decide
theorem core_bundle :
    (squares leaf0 = [4,4,4,4] ∧ squares leaf1 = [4,4,4,4]) ∧
    (1/4 : Rat) / (2*((1/4+1/4)/2)) = 1/2 :=
  ⟨actual_leaf_squares, actual_fair_kernel⟩
end A083
