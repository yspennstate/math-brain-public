from pathlib import Path
p=Path('HeightResidue.lean');s=p.read_text(encoding='utf8').replace('import Mathlib.Tactic.Omega','import Lean.Elab.Tactic.Omega');p.write_text(s,encoding='utf8')
