from pathlib import Path
p=Path('MomentChecks.lean');s=p.read_text(encoding='utf8');s=s.replace('end C0100','''-- Exhaustive four-height factorial-moment table, evaluated by the kernel.
theorem binomial_table : ∀ h : Fin 4,
    (((h.val : ℚ) * ((h.val : ℚ) - 1) / 2) =
      (if h.val = 2 then 1 else if h.val = 3 then 3 else 0)) ∧
    (((h.val : ℚ) * ((h.val : ℚ) - 1) * ((h.val : ℚ) - 2) / 6) =
      (if h.val = 3 then 1 else 0)) := by
  decide +kernel

end C0100''');p.write_text(s,encoding='utf8')
