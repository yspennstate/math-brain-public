import Mathlib.Data.Rat.Lemmas

-- Three-site immigration chain at per-edge infection rate 1/4.
def p0 : ℚ := 394304 / 507375
def p1 : ℚ := 9824 / 56375
def p2 : ℚ := 8464 / 507375
def p3 : ℚ := 2252 / 101475
def p4 : ℚ := 1696 / 507375
def p5 : ℚ := 76 / 56375
def p6 : ℚ := 1436 / 507375
def p7 : ℚ := 223 / 101475

theorem normalization : p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 = 1 := by decide +kernel

theorem strictly_positive : 0 < p0 ∧ 0 < p1 ∧ 0 < p2 ∧ 0 < p3 ∧ 0 < p4 ∧ 0 < p5 ∧ 0 < p6 ∧ 0 < p7 := by decide +kernel

theorem all_stationarity_equations :
    (((-1 : ℚ) / 4) * p0 + ((1 : ℚ) / 1) * p1 + ((1 : ℚ) / 1) * p2 + ((1 : ℚ) / 1) * p4 = 0) ∧
    (((1 : ℚ) / 4) * p0 + ((-5 : ℚ) / 4) * p1 + ((1 : ℚ) / 1) * p3 + ((1 : ℚ) / 1) * p5 = 0) ∧
    (((-3 : ℚ) / 2) * p2 + ((1 : ℚ) / 1) * p3 + ((1 : ℚ) / 1) * p6 = 0) ∧
    (((1 : ℚ) / 4) * p1 + ((1 : ℚ) / 4) * p2 + ((-9 : ℚ) / 4) * p3 + ((1 : ℚ) / 1) * p7 = 0) ∧
    (((-5 : ℚ) / 4) * p4 + ((1 : ℚ) / 1) * p5 + ((1 : ℚ) / 1) * p6 = 0) ∧
    (((1 : ℚ) / 4) * p4 + ((-9 : ℚ) / 4) * p5 + ((1 : ℚ) / 1) * p7 = 0) ∧
    (((1 : ℚ) / 4) * p2 + ((-9 : ℚ) / 4) * p6 + ((1 : ℚ) / 1) * p7 = 0) ∧
    (((1 : ℚ) / 4) * p3 + ((1 : ℚ) / 4) * p5 + ((1 : ℚ) / 4) * p6 + ((-3 : ℚ) / 1) * p7 = 0) := by decide +kernel

theorem exact_joint_probability : p6 + p7 = 2551 / 507375 := by decide +kernel

theorem smallest_scale_obstruction : (1 : ℚ) / 3^25 < p6 + p7 := by decide +kernel
