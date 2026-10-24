from pathlib import Path
p=Path('FusionExponents.lean');s=p.read_text(encoding='utf8');s=s.replace('(hq0 : 0 < q) (hq1 : q < 1)','(hq1 : q < 1)')
s=s.replace('#print axioms fused_diagonal_volume_exponent_positive','''-- Nonnegativity of a two-edge probability supplies the entire local lower bound.
theorem local_fusion_mean_lower_bound (c : Real) (hc : c^2 ≤ 1/16) :
    1/4 ≤ 7/16 + c/2 - c^2 := by
  have hcl : -(1/4 : Real) ≤ c := by
    nlinarith [sq_nonneg (c + 1/4)]
  nlinarith

#print axioms local_fusion_mean_lower_bound
#print axioms fused_diagonal_volume_exponent_positive''');p.write_text(s,encoding='utf8')
