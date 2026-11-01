import Mathlib.Data.Nat.Basic

namespace C0020Second

-- All minimal open crossing masks for the specified nine-site rhombus.
-- Their graph interpretation is exhaustively checked in the Python artifact.
def primeMasks : List Nat := [7,14,28,51,56,84,112,224,403,408,448]

def covers (m p : Nat) : Bool :=
  (List.range 9).all (fun i => !(p.testBit i) || m.testBit i)

def crossing (m : Nat) : Bool := primeMasks.any (covers m)

def flip (m i : Nat) : Nat :=
  if m.testBit i then m - 2^i else m + 2^i

def pivotalCount (i : Nat) : Nat :=
  ((List.range 512).filter (fun m => crossing m != crossing (flip m i))).length

theorem center_count : pivotalCount 4 = 164 := by
  decide +kernel

theorem corner_count : pivotalCount 2 = 156 := by
  decide +kernel

theorem all_counts :
    (List.range 9).map pivotalCount = [52,104,156,104,164,104,156,104,52] := by
  decide +kernel

-- Numerator and denominator of 4/7 - (25/31)/2 after clearing denominators.
theorem and_six_drift_numerator : 4*62 - 25*7 = (73 : Nat) := by
  decide +kernel

theorem and_six_drift_denominator : 7*62 = (434 : Nat) := by
  decide +kernel

end C0020Second
