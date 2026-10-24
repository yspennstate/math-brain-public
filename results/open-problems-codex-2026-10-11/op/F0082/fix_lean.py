from pathlib import Path
p=Path('FiniteChecks.lean');s=p.read_text(encoding='utf8');p.write_text('import Mathlib.Data.Real.Basic\n'+s,encoding='utf8')
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf8').replace('nu_n -> 0,   lim_', 'u_n -> 0,   lim_');p.write_text(s,encoding='utf8')
