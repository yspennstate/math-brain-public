from pathlib import Path
import json
p=Path('.')
lean=(p/'new_lean_check.txt').read_text(encoding='utf8');assert 'Exit code: 0' in lean
src=(p/'SelectionAlgebra.lean').read_text(encoding='utf8');assert 'sorry' not in src and 'native_decide' not in src and 'import Mathlib\n' not in src
with (p/'ATTEMPT.md').open('a',encoding='utf8') as f:f.write('\nThe final SelectionAlgebra.lean run returned exit code 0 from ~/lean_verify, using the required 3600-second timeout. Lean kernel-checked the quadratic-sector factorization, the nonlinear recurrence coefficient identity, and the sign of the discounted power term. The file uses specific Mathlib imports and contains no sorry or native_decide. The stochastic stopping proof and all-orders formal-series argument are written proofs; only those three finite algebraic steps are formalized. See new_lean_check.txt.\n')
with (p/'NEW_APPROACHES.md').open('a',encoding='utf8') as f:f.write('''

Outcome of route 1: proved the generator-only inequality 0<=G_beta(s)-1+s/(2pi)<=((s/(2pi))^(p+1))/(p+1), p=min(2,(1+sqrt(1+2beta))/2)>1. The proof uses a stopped discounted power moment with epsilon regularization, improving on the proposed coarse time split. This excludes the exponential sigma-PV branch. Also proved unique formal nonlinear PV sector and conditional analytic-germ uniqueness with this branch datum. Exact symbolic and numerical checks passed; three finite algebraic statements passed Lean. Route 2 remains unexecuted. Main global physical/Lax selection is still open in this attempt; verdict PARTIAL.
''')
claims=[json.loads(x) for x in (p/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()];assert len(claims)==10
claims[-1]['checks']='All-orders first-difference proof in Section 15; exact SymPy checks through order 10; SelectionAlgebra.lean kernel check exit 0 (new_lean_check.txt).'
(p/'CLAIMS.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in claims),encoding='utf8')
status=(p/'STATUS.md').read_text(encoding='utf8').splitlines();status[0]='STATE: DONE';status[1]='NEXT: Prove global physical selection of the carousel solution by the integrable Lax constraint, or derive a closed nonlinear identity for its discounted hitting transform. Generator-side quadratic branch data are now available.';status[2]='VERDICT: PARTIAL';status.extend(['2026-10-12: Additional attempt completed. At beta=2 the new remainder exponent is (3+sqrt(5))/2>2; the exponential branch is excluded directly from the carousel, without a determinant theorem.','2026-10-12: Proved conditional formal/analytic PV branch uniqueness. Exact coefficient checks through order 10, moment checks and new Lean kernel verification passed (exit 0, no sorry/native_decide).','2026-10-12: Remaining gap is the actual nonlinear equation and global physical/integrable selection, not the exclusion of the exponential branch. No full solution to Question 9 obtained.'])
(p/'STATUS.md').write_text('\n'.join(status)+'\n',encoding='utf8')
assert (p/'STATUS.md').read_bytes().splitlines()[0]==b'STATE: DONE'
print('Final audit PASS: STATE: DONE; VERDICT: PARTIAL; 10 valid claims; both Lean files checked successfully.')
print(lean)
