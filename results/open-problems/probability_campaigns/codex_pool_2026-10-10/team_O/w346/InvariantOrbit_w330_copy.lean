def forwardIter {A : Type} (T : A -> A) : Nat -> A -> A
  | 0, x => x
  | n + 1, x => T (forwardIter T n x)

theorem invariant_forward_iter {A : Type} (T : A -> A) (p : A -> Prop)
    (h : forall x, p (T x) <-> p x) (n : Nat) (x : A) :
    p (forwardIter T n x) <-> p x := by
  induction n with
  | zero => exact Iff.rfl
  | succ n ih => exact (h (forwardIter T n x)).trans ih

theorem invariant_selected_forward_iter {A : Type} (T : A -> A) (p : A -> Prop)
    (h : forall x, p (T x) <-> p x) (N : A -> Nat) (x : A) :
    p (forwardIter T (N x) x) <-> p x :=
  invariant_forward_iter T p h (N x) x
