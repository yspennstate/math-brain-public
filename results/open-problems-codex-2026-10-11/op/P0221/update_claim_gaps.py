"""Bring earlier claim gap annotations up to date with this attempt's result."""
import json
from pathlib import Path
root=Path(__file__).resolve().parent
p=root/'CLAIMS.jsonl'
rows=[json.loads(s) for s in p.read_text(encoding='utf-8').splitlines() if s.strip()]
assert len(rows)==22
revisions={
    2:'This particular bound proves no limit. Model equivalence is proved separately in REVERSE_TRANSFER.md; bibliographic novelty is not certified.',
    5:'Convergence and the common limiting value remain unproved. The model comparison is now established separately in REVERSE_TRANSFER.md.',
    6:'The target initial states have y_1=1, not zero; general nonzero-state continuity and convergence remain unproved. Model equivalence is addressed separately in REVERSE_TRANSFER.md.',
    7:'Convergence and limit identification remain open. Separate model comparison now transfers the bound to the combinatorial model; novelty is not asserted.',
    8:'No convergence or exact limiting value. Separate model comparison transfers Poisson limsup bounds to the combinatorial model.',
    9:'Convergence and the common limiting value remain open; separate quantitative model comparison is proved in REVERSE_TRANSFER.md. No novelty claim.',
    10:'Convergence and the common limiting value remain open; separate quantitative model comparison is proved in REVERSE_TRANSFER.md. No novelty claim.',
    13:'Used in the forward comparison. The reverse direction uses a separate construction in REVERSE_TRANSFER.md; convergence remains open.',
    14:'This forward direction alone identifies no limit. The reverse comparison is proved separately in REVERSE_TRANSFER.md, completing model equivalence while convergence/value remain open.'
}
for i,gap in revisions.items(): rows[i-1]['remaining_gap']=gap
p.write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in rows),encoding='utf-8')
p=root/'STATUS.md'
s=p.read_text(encoding='utf-8')
assert s.startswith('STATE: DONE\n')
s=s.replace('VERDICT: PARTIAL\n','VERDICT: PARTIAL\n\n2026-10-11 FINAL: Both comparisons are proved, giving |P_n-C_n|=O(n^(-1/100)); full proofs in SECOND_ATTEMPT.md and REVERSE_TRANSFER.md. The common limsup is <=1.9440377683016505. All finite/simulator checks and supplementary Lean algebra passed. Limit existence and its value remain unresolved.\n',1)
p.write_text(s,encoding='utf-8')
print('Earlier claim gaps updated; STATE: DONE; VERDICT: PARTIAL; 22 valid claims.')
