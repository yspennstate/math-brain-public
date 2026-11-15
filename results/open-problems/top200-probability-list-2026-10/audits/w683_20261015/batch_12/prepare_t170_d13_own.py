from pathlib import Path
from datetime import datetime
from hashlib import sha256
import json
root=Path(__file__).resolve().parent;at=datetime.now().astimezone().isoformat()
p=root/'checks/t170_d13_rolling_own.py';assert not p.exists()
source=Path('~/crash_recovery_20261014/workers_1015/term_362ebe34/T170-LEAD-ROLLING-D13-001_v2.md')
assert sha256(source.read_bytes()).hexdigest()=='7176a751f1a7de49be1d4dc86114056163a2569bcf44b3d8828014a08f6a9b52'
(root/'checks/frozen_T170-LEAD-ROLLING-D13-001_v2.md').write_bytes(source.read_bytes())
s=(root/'checks/t170_d14_rolling_own.py').read_text(encoding='utf-8')
replacements=[('T170_D14_SUBMISSION.json','T170_D13_SUBMISSION_v2.json'),('T170-LEAD-ROLLING-D14-001_v1.md','T170-LEAD-ROLLING-D13-001_v2.md'),('T170_THREE_COMPRESSED_d14_C256_BASE.json','T170_THREE_COMPRESSED_d13_C256_BASE.json'),("==(14,3,256,2**40,98624416626,65536)","==(13,3,256,2**40,104206661983,65536)"),('range(13)','range(12)'),('26*n-2*edges','24*n-2*edges'),('20736','19200'),('98624394809','104206641546'),('21817','20437'),("r['d']==14","r['d']==13"),('91464273436','95165638290'),('t170_d14_rolling','t170_d13_rolling'),('Q13','Q12')]
for old,new in replacements:
    assert old in s,old;s=s.replace(old,new)
old="assert witness['required']-(max_required-1)==1 # actual-row lowered-coefficient fault"
new="""bad_coefficient=max_required-1
actual_fault=S-bad_coefficient+(witness['front_h']-witness['h'])+witness['rc']*(witness['h_c2']-witness['h'])
if witness['ra']: actual_fault+=witness['ra']*(witness['a_child']-witness['h'])
if witness['rb']: actual_fault+=witness['rb']*(witness['b_child']-witness['h'])
assert actual_fault==1 # reconstruct actual generator row, not required-minus-required algebra"""
assert old in s;s=s.replace(old,new)
p.write_text(s,encoding='utf-8')
next_line='NEXT: Finish independent T170 D13 corrected v2 three-slab audit and all2^24-state replay.40 recovered verdicts archived through batch11 commit17a34f8506eb31d6639f038a0cf3b7a81e94ca10; claims released2. D13 v1 superseded; audit v2 only.'
for name in ['STATUS.md','NEXT.md']:
    q=root/name;lines=q.read_text(encoding='utf-8').splitlines()
    if name=='STATUS.md':lines[0:2]=['STATE: WORKING',next_line]
    else:lines[0]=next_line
    q.write_text('\n'.join(lines)+'\n\n'+at+' Batch11 full scan clean, remote verified76paths and both claims released. All degree6 computation exited. D13v2 proof fully read and frozen, account4 at semantic read; no distinct-account admission claimed. New checker derives solely from own D14 checker and exact new proof.\n',encoding='utf-8')
with (root/'ROUTES.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps({'at':at,'row':'T170','route':'Independent corrected v2 dimension13 three-slab physical and exact constructive bias audit','status':'live','why':'New named dimension13, frontier check0; v1 ambient dimension label corrected before audit','evidence':str(source),'kind':'narrowed','target':'3/4'})+'\n')
print('D13 v2 frozen; own exact checker prepared, no peer code imported. Archive11 claims released.')
