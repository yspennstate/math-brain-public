-- A finite boundary check only, not the continuous score certificate.
theorem triangle_grid :
    forall a b c : Fin 5,
      a.val + b.val <= 4 ->
      a.val + c.val <= 4 ->
      b.val + c.val <= 4 ->
      6*a.val*b.val*c.val <=
        4*(a.val*b.val+a.val*c.val+b.val*c.val) := by
  decide
