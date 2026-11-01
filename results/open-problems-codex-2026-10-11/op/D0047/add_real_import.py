from pathlib import Path
p=Path('BoundaryAlgebra.lean');t=p.read_text(encoding='utf8');p.write_text('import Mathlib.Data.Real.Basic\n'+t,encoding='utf8')
# Preserve prior Lean errors as diagnostic history, not checked proofs.
Path('lean_initial_errors.txt').write_text(Path('lean_check.txt').read_text(encoding='utf8'),encoding='utf8')
