set_option maxRecDepth 100000
set_option maxHeartbeats 10000000
def wave (den k : Nat) : Nat :=
  8 * min (k % den) (den - k % den) +
  4 * min ((2*k) % den) (den - (2*k) % den) +
  2 * min ((4*k) % den) (den - (4*k) % den) +
  min ((8*k) % den) (den - (8*k) % den)
theorem a057_boundary_vertices :
  ? i j : Fin 17, wave 32 (i.val+j.val) ?
    wave 16 i.val + wave 16 j.val + 8*((i.val-j.val)+(j.val-i.val)) := by decide
