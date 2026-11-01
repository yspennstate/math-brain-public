from pathlib import Path
import json
p=Path('.')
lean=(p/'lean_check.txt').read_text(encoding='utf8')
assert 'Exit code: 0' in lean,lean
src=(p/'BoundaryAlgebra.lean').read_text(encoding='utf8')
assert 'sorry' not in src and 'native_decide' not in src and 'import Mathlib\n' not in src
with (p/'ATTEMPT.md').open('a',encoding='utf8') as f:
 f.write('\n## 11. Final formal-verification outcome\n\nThe final `lake env lean ~/brain_workers/TRIO_1011/op/D0047/BoundaryAlgebra.lean` invocation, run from ~/lean_verify with a 3600-second subprocess timeout, returned exit code 0. Lean kernel-checked triangular_jet_step and linear_sigma_branch. The file imports only Real.Basic and the required field_simp, linarith, and ring tactics, and contains no sorry or native_decide. Earlier encoding/import failures were corrected before this successful run. The stochastic and analytic statements remain written proofs, not Lean-verified theorems.\n')
(p/'STATUS.md').write_text('''STATE: DONE
NEXT: Prove physical carousel selection of a global integrable solution, or derive closed differential identities for V(s,0)=E[exp(-(beta/4)tau)]; obtain branch data beyond the intensity slope.
VERDICT: PARTIAL

2026-10-12: Confirmed Virag Question 9 verbatim on PDF page 25; the question does not specify beta or a particular Painleve equation. Chose beta=2 sigma-PV as the concrete classical target.
2026-10-12: Searched arXiv, Crossref, OpenAlex, Semantic Scholar and GitHub via Python. No exact solution theorem found. OpenAlex was rate-limited; actual source citations were retrieved from Semantic Scholar. This bounded search does not certify current global open status.
2026-10-12: Read brain recalls, intake attempts and six prior D0047 reports from origin/master, without modifying those stores or the repository.
2026-10-12: Proved an exact stopped-phase/discounted-hitting representation of the gap, its zero-drift profile, and a formal boundary-jet nonclosure lemma. Proved that the exact exponential sigma-PV branch shares the intensity slope, so intensity alone does not select the physical branch.
2026-10-12: SymPy checks passed. Small Nystrom determinant checks agreed with the external beta=2 quartic gap coefficient. Two finite algebraic steps passed Lean kernel verification (exit 0), with no sorry or native_decide.
2026-10-12: Finished this attempt with the precise physical-selection/nonlinear-closure gap recorded in ATTEMPT.md Sections 8-11. No full proof or counterexample to Question 9 was obtained.
''',encoding='utf8')
claims=[json.loads(line) for line in (p/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(claims)==7
assert (p/'STATUS.md').read_bytes().startswith(b'STATE: DONE\n')
assert all(c['problem_id']=='D0047' for c in claims)
print((p/'STATUS.md').read_text(encoding='utf8'))
print(lean)
print('Final artifact audit: 7 valid claims, required files present, STATUS first line exact.')
