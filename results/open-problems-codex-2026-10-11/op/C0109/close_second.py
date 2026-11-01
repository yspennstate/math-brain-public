from pathlib import Path
import json
root=Path(__file__).parent
p=root/'STATUS.md'
s=p.read_text(encoding='utf-8-sig')
s=s.replace('STATE: WORKING','STATE: DONE',1)
lines=s.splitlines()
lines[1]='NEXT: Determine the sharp exponent: close the gap between the new e/(12+4e) upper rate and the fixed-law lower obstruction.'
s='\n'.join(lines)+'\n'
log='2026-10-11: Second serious attempt finalized PARTIAL: two new routes recorded, unconditional truncation transfer and nonoptimal beta=e/(12+4e) source-metric upper rate proved conventionally, detailed hostile audits and auxiliary checks saved; exact optimal dependence unresolved.\n'
if log.strip() not in s:s+=log
p.write_text(s,encoding='utf8')
assert p.read_bytes().splitlines()[0]==b'STATE: DONE'
assert '\nVERDICT: PARTIAL\n' in s
rows=[json.loads(x) for x in (root/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert all(c['problem_id']=='C0109' for c in rows)
for name in ['ATTEMPT.md','LITERATURE.md','SECOND_APPROACHES.md','SECOND_ATTEMPT.md','DIRECT_UPPER.md','DIRECT_REFEREE.md','SECOND_RESULT.md','direct_checks.json','local_checks.json']:
 assert (root/name).is_file()
print('STATE: DONE; VERDICT: PARTIAL;',len(rows),'claim records validated.')
