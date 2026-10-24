import Mathlib.Data.Fin.Basic

-- Each paired Poisson cluster contributes zero, one, or two endpoints to a set.
-- This inequality is the finite step behind the atom-count variance bound.
theorem paired_cluster_second_moment_bound :
    ∀ a : Fin 3, a.val * a.val ≤ 2 * a.val := by
  decide

#print axioms paired_cluster_second_moment_bound
