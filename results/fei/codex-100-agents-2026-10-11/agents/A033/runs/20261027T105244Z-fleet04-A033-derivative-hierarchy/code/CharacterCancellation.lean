import Std

def characterSum : List Bool ? Int
  | [] => 1
  | b :: bs => characterSum bs + (if b then -characterSum bs else characterSum bs)

theorem characterSum_mismatch (bs : List Bool) (h : true ? bs) : characterSum bs = 0 := by
  induction bs with
  | nil => simp at h
  | cons b bs ih =>
    cases b with
    | true => simp [characterSum]
    | false =>
      have ht : true ? bs := by simpa using h
      simp [characterSum, ih ht]
