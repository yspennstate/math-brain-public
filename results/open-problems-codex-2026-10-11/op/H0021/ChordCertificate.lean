import Mathlib.Data.Finset.Card

def chordPacking : Finset (Finset (ℕ × ℕ)) := {
  {(0, 5), (4, 6)},
  {(0, 6), (4, 7)},
  {(0, 7), (4, 8)},
  {(0, 8), (4, 9)},
  {(1, 6), (5, 7)},
  {(1, 7), (5, 8)},
  {(1, 8), (5, 9)},
  {(1, 9), (5, 10)},
  {(2, 7), (6, 8)},
  {(2, 8), (6, 9)},
  {(2, 9), (6, 10)},
  {(2, 10), (6, 11)},
  {(3, 8), (7, 9)},
  {(3, 9), (7, 10)},
  {(3, 10), (7, 11)},
  {(4, 10), (8, 11)},
  {(5, 11), (0, 9)},
  {(3, 7), (4, 11)}}

def chordPackingList : List (Finset (ℕ × ℕ)) := [
  {(0, 5), (4, 6)},
  {(0, 6), (4, 7)},
  {(0, 7), (4, 8)},
  {(0, 8), (4, 9)},
  {(1, 6), (5, 7)},
  {(1, 7), (5, 8)},
  {(1, 8), (5, 9)},
  {(1, 9), (5, 10)},
  {(2, 7), (6, 8)},
  {(2, 8), (6, 9)},
  {(2, 9), (6, 10)},
  {(2, 10), (6, 11)},
  {(3, 8), (7, 9)},
  {(3, 9), (7, 10)},
  {(3, 10), (7, 11)},
  {(4, 10), (8, 11)},
  {(5, 11), (0, 9)},
  {(3, 7), (4, 11)}]

theorem chordPacking_size : chordPacking.card = 18 := by decide +kernel
theorem chordPacking_disjoint : chordPackingList.Pairwise (fun A B => Disjoint A B) := by decide +kernel
theorem chordPacking_list_finset : chordPackingList.toFinset = chordPacking := by decide +kernel
#print axioms chordPacking_size
#print axioms chordPacking_disjoint
#print axioms chordPacking_list_finset
