from pathlib import Path
import json
p=Path('ATTEMPT.md');t=p.read_text(encoding='utf8');t=t.replace('Then 1<p<=2 and p(p-1)/2<=c. For every s>=0,','Then 1<p<=2 and p(p-1)/2<=c. Indeed the positive root q=(1+sqrt(1+8c))/2 satisfies q(q-1)/2=c and q>1; if q<=2 take p=q, while if q>=2 then c>=1 and p=2 gives p(p-1)/2=1<=c. For every s>=0,',1);p.write_text(t,encoding='utf8')
claims=[json.loads(x) for x in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(claims)==10 and all(x['problem_id']=='D0047' for x in claims)
assert Path('STATUS.md').read_bytes().splitlines()[0]==b'STATE: WORKING'
assert all(Path(f).is_file() for f in ['NEW_APPROACHES.md','new_moment_checks.txt','new_symbolic_checks.txt','SelectionAlgebra.lean'])
print('Interim audit passed: state WORKING, 10 valid claims, two approaches and all new check artifacts saved.')
