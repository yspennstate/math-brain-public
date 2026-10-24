"""Finalize records after the submitted supplementary Lean check succeeds."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
status = root/'STATUS.md'
s = status.read_text(encoding='utf-8')
assert s.startswith('STATE: WORKING\n')
s=s.replace('STATE: WORKING\n','STATE: DONE\n',1)
lines=s.splitlines()
lines[1]='NEXT: Establish uniform continuity of Poisson optimal values at general nonzero empirical states, then prove convergence and determine the common limit.'
s='\n'.join(lines)+'\n'
s+='\n2026-10-11: Closed the second serious attempt as DONE / PARTIAL. Proved both model comparisons, hence |P_n-C_n|=O(n^(-1/100)), and transferred limsup <=(63-3 exp(-4/3))/32 to the combinatorial model. Finite arithmetic, exhaustive bundle reassignments and simulator checks passed; RepairCheck.lean passed with exit code zero. Convergence and the common limiting optimal cost remain unresolved.\n'
status.write_text(s,encoding='utf-8')

p=root/'VERIFICATION.md'
s=p.read_text(encoding='utf-8')
s=s.replace('At the time of this entry it is queued; no kernel-checked claim is made until successful completion is recorded.',
            '**PASSED, exit code 0**. All three named algebraic theorems were checked by Lean; the stochastic and limiting arguments are written proofs, not formalized proofs.')
s=s.replace('16 claim records','22 claim records')
s=s.replace('The strongest new conclusion is the one-sided quantitative comparison','The first new conclusion was the one-sided quantitative comparison')
s='\n'.join('The model comparison is now proved in both directions. Limit existence and determination remain unresolved; novelty is not asserted.' if line.startswith('The limit existence, exact limit and') else line for line in s.splitlines())+'\n'
p.write_text(s,encoding='utf-8')

p=root/'SECOND_ATTEMPT.md'
p.open('a',encoding='utf-8').write('\n## Final disposition\n\nSTATE: DONE; VERDICT: PARTIAL. Forward and reverse quantitative model transfer are proved, giving |P_n-C_n|=O(n^(-1/100)); see REVERSE_TRANSFER.md for the subsequent reverse construction and its full proof. The transferred limsup upper bound remains 1.9440377683016505. RepairCheck.lean passed with exit code zero, with no proof holes or native decision evaluation. All finite arithmetic, exhaustive label-reassignment and simulator checks passed. Optimal limit existence and the common limiting value remain unresolved.\n')

p=root/'REVERSE_TRANSFER.md'
s=p.read_text(encoding='utf-8').replace('the proposed construction yields','the construction yields')
p.write_text(s,encoding='utf-8')

claims=[json.loads(line) for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
assert len(claims)==22
for row in claims:
    assert row['problem_id']=='P0221'
    assert row['status'] in {'proved','counterexample','proved_special_case','numerical_evidence','conjecture'}
    assert {'claim','proof_location','remaining_gap','checks'}<=row.keys()
lean=(root/'RepairCheck.lean').read_text(encoding='utf-8')
assert 'sorry' not in lean and 'native_decide' not in lean
assert all(name.is_file() for name in (root/'STATUS.md',root/'LITERATURE.md',root/'ATTEMPT.md',root/'CLAIMS.jsonl'))
print('Finalized STATE: DONE; VERDICT: PARTIAL; 22 valid claims.')
