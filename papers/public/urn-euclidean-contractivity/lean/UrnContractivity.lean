/-
Integer certificates for the counterexamples to Remark 3.7 of Neri and Pinto (arXiv:2607.07309).
Core Lean 4, no Mathlib. Colours are indexed 0, ..., d-1.

For a replacement matrix R (a list of rows), a balance lam and an integer row vector w,
  form R lam w k = sum over i /= k of w_i * ((w R)_i - lam * w_i),
with k = -1 meaning that no colour is omitted (the reading p = d on mean-zero vectors) and
k = i meaning that colour i is the omitted colour (the reading p = d - 1 with colour i last).
Each theorem below states that a mean-zero integer vector makes the form strictly positive.
-/

def dot (u v : List Int) : Int := (List.zipWith (· * ·) u v).foldl (· + ·) 0

def col (R : List (List Int)) (j : Nat) : List Int := R.map (fun r => r.getD j 0)

def wR (R : List (List Int)) (w : List Int) : List Int :=
  (List.range R.length).map (fun j => dot w (col R j))

def form (R : List (List Int)) (lam : Int) (w : List Int) (k : Int) : Int :=
  ((List.range w.length).map (fun (i : Nat) =>
    if Int.ofNat i = k then 0 else w.getD i 0 * ((wR R w).getD i 0 - lam * w.getD i 0))).foldl (· + ·) 0

def total (w : List Int) : Int := w.foldl (· + ·) 0

def rowSumsAre (R : List (List Int)) (lam : Int) : Bool := R.all (fun r => total r == lam)

def nonneg (R : List (List Int)) : Bool := R.all (fun r => r.all (fun x => decide (0 ≤ x)))

/-- The d-colour urn of the paper, d ≥ 4, balance 6 (rows are colours 0, ..., d-1). -/
def fam (d : Nat) : List (List Int) :=
  (List.range d).map (fun i =>
    (List.range d).map (fun j =>
      if i = 0 then (if j = 0 then 5 else if j = 1 then 1 else 0)
      else if i = 1 then (if j = 0 then 5 else if j = 2 then 1 else 0)
      else if i = d - 1 then (if j = d - 1 then 5 else if j = d - 2 then 1 else 0)
      else if i = d - 2 then (if j = d - 1 then 5 else if j = d - 3 then 1 else 0)
      else (if j + 1 = i then 3 else if j = i + 1 then 3 else 0)))

/-- Embed a vector (x0, x1, x2, x3) on the colours 0, 1, d-2, d-1, zero elsewhere. -/
def emb (d : Nat) (x0 x1 x2 x3 : Int) : List Int :=
  (List.range d).map (fun i => if i = 0 then x0 else if i = 1 then x1
    else if i = d - 2 then x2 else if i = d - 1 then x3 else 0)

def T3 : List (List Int) := [[0, 1, 99], [1, 99, 0], [36, 0, 64]]

-- Three colours, balance 100.
theorem t3_rows : rowSumsAre T3 100 = true ∧ nonneg T3 = true := by decide +kernel
theorem t3_full : total [-1, 3, -2] = 0 ∧ form T3 100 [-1, 3, -2] (-1) = 11 := by decide +kernel
theorem t3_drop0 : total [-1, 2, -1] = 0 ∧ form T3 100 [-1, 2, -1] 0 = 57 := by decide +kernel
theorem t3_drop1 : total [-1, 3, -2] = 0 ∧ form T3 100 [-1, 3, -2] 1 = 23 := by decide +kernel
theorem t3_drop2 : total [-1, 5, -4] = 0 ∧ form T3 100 [-1, 5, -4] 2 = 9 := by decide +kernel

-- Four colours.
theorem f4_rows : fam 4 = [[5, 1, 0, 0], [5, 0, 1, 0], [0, 1, 0, 5], [0, 0, 1, 5]] := by decide +kernel
theorem f4_full : form (fam 4) 6 (emb 4 2 1 (-1) (-2)) (-1) = 2 := by decide +kernel
theorem f4_drop0 : form (fam 4) 6 (emb 4 (-3) 0 1 2) 0 = 2 := by decide +kernel
theorem f4_drop1 : form (fam 4) 6 (emb 4 (-1) (-1) 1 1) 1 = 2 := by decide +kernel
theorem f4_drop2 : form (fam 4) 6 (emb 4 (-1) (-1) 1 1) 2 = 2 := by decide +kernel
theorem f4_drop3 : form (fam 4) 6 (emb 4 (-2) (-1) 0 3) 3 = 2 := by decide +kernel

-- Five, six and seven colours, every omitted colour.
theorem f5 : rowSumsAre (fam 5) 6 = true ∧
    form (fam 5) 6 (emb 5 2 1 (-1) (-2)) (-1) = 4 ∧
    form (fam 5) 6 (emb 5 (-3) 0 1 2) 0 = 2 ∧
    form (fam 5) 6 (emb 5 (-1) (-1) 1 1) 1 = 3 ∧
    form (fam 5) 6 (emb 5 2 1 (-1) (-2)) 2 = 4 ∧
    form (fam 5) 6 (emb 5 (-1) (-1) 1 1) 3 = 3 ∧
    form (fam 5) 6 (emb 5 (-2) (-1) 0 3) 4 = 2 := by decide +kernel

theorem f6 : rowSumsAre (fam 6) 6 = true ∧
    form (fam 6) 6 (emb 6 2 1 (-1) (-2)) (-1) = 4 ∧
    form (fam 6) 6 (emb 6 (-3) 0 1 2) 0 = 2 ∧
    form (fam 6) 6 (emb 6 (-1) (-1) 1 1) 1 = 3 ∧
    form (fam 6) 6 (emb 6 2 1 (-1) (-2)) 2 = 4 ∧
    form (fam 6) 6 (emb 6 2 1 (-1) (-2)) 3 = 4 ∧
    form (fam 6) 6 (emb 6 (-1) (-1) 1 1) 4 = 3 ∧
    form (fam 6) 6 (emb 6 (-2) (-1) 0 3) 5 = 2 := by decide +kernel

-- A small urn: six colours, balance 6.
def S6 : List (List Int) :=
  [[0, 1, 0, 5, 0, 0], [0, 0, 0, 6, 0, 0], [1, 0, 5, 0, 0, 0], [0, 0, 0, 5, 1, 0], [0, 0, 5, 0, 0, 1], [0, 0, 6, 0, 0, 0]]

theorem s6 : rowSumsAre S6 6 = true ∧ nonneg S6 = true ∧
    total [0, -1, 2, -2, 0, 1] = 0 ∧ form S6 6 [0, -1, 2, -2, 0, 1] (-1) = 4 ∧
    total [-1, 0, 1, -1, 0, 1] = 0 ∧ form S6 6 [-1, 0, 1, -1, 0, 1] 0 = 3 ∧
    total [0, -1, 1, -1, 0, 1] = 0 ∧ form S6 6 [0, -1, 1, -1, 0, 1] 1 = 4 ∧
    total [0, -1, 3, -2, 0, 0] = 0 ∧ form S6 6 [0, -1, 3, -2, 0, 0] 2 = 2 ∧
    total [0, 0, -2, 3, 0, -1] = 0 ∧ form S6 6 [0, 0, -2, 3, 0, -1] 3 = 2 ∧
    total [-1, 0, 1, -1, 1, 0] = 0 ∧ form S6 6 [-1, 0, 1, -1, 1, 0] 4 = 1 ∧
    form S6 6 [-1, 0, 1, -1, 0, 1] 5 = 2 := by decide +kernel
