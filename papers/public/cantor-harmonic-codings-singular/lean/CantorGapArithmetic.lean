/-
  The rational arithmetic of Section 4, cross-multiplied into statements about natural numbers.
  Lean 4, no external libraries; every proof is kernel evaluation.

  u0 = 52/243, r0 = 128/243, E8 = 955961/524288 (energy of the first eight levels),
  tail = 384 (2/3)^17, E_* = E8 + tail, G_L >= 1/(1 + E_*), G_R <= 13703/45323.
-/

-- D0 = [4/128, 5/128] and C0 = [8/243, 9/243]: u0 = (8/243 - 4/128) * 128 and r0 = 128/243
theorem u0_value : 8 * 128 - 4 * 243 = 52 := by decide

-- u0 / r0 = 13/32 < 1
theorem margin_left : 52 * 32 = 13 * 128 ∧ 13 < 32 := by decide

-- (1 - u0 - r0) / r0 = 63/128 < 9
theorem margin_right : (243 - 52 - 128) * 128 = 63 * 128 ∧ 63 < 9 * 128 := by decide

-- (1/2 - u0) / r0 = (243 - 104) / 256 = 139/256, and 1/3 < 139/256 < 2/3
theorem midpoint_in_gap : 243 - 2 * 52 = 139 ∧ 256 < 3 * 139 ∧ 3 * 139 < 2 * 256 := by decide

-- 384 (2/3)^17 = 2^24 / 3^16 = 16777216 / 43046721
theorem tail_value : 384 * 2 ^ 17 * 43046721 = 16777216 * 3 ^ 17 := by decide

-- 524288 * 43046721 = 2^19 * 3^16 = 22568879259648
theorem common_denominator : 524288 * 43046721 = 22568879259648 ∧ 2 ^ 19 * 3 ^ 16 = 22568879259648 := by decide

-- E_* = 955961/524288 + 16777216/43046721 = 49947079476089/22568879259648
theorem estar_value : 955961 * 43046721 + 16777216 * 524288 = 49947079476089 := by decide

-- 1/(1 + E_*) = 22568879259648/72515958735737
theorem gl_value : 22568879259648 + 49947079476089 = 72515958735737 := by decide

-- C_R = 13703/31620 gives G_R = C_R/(1 + C_R) = 13703/45323
theorem gr_value : 31620 + 13703 = 45323 := by decide

-- the gap: 22568879259648/72515958735737 > 13703/45323
theorem branch_gap : 13703 * 72515958735737 < 22568879259648 * 45323 := by decide

-- p >= a/(a+b) with a = 22568879259648/72515958735737, b = 13703/45323, written over the common denominator
theorem split_value :
    22568879259648 * 45323 = 1022889314685026304 ∧
    22568879259648 * 45323 + 13703 * 72515958735737 = 2016575497240830415 := by decide

-- and that ratio exceeds 1/2
theorem split_gap : 2016575497240830415 < 2 * 1022889314685026304 := by decide
