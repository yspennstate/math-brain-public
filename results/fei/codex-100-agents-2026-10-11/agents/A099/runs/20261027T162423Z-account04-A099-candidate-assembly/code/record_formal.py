from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
p=R/'out/FORMAL_STATUS.json';d=json.loads(p.read_text(encoding='utf-8'))
assert 'RUNTIME_UNVERIFIED in 128.8s' in d['output']
d.update(status='RUNTIME_UNVERIFIED',seconds=128.8,exit_code=1,source_sha256='11fdef0fbfae919d34c4cf4190fb5fccd5adad8070a7005d50e1f103350a6a9a')
p.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
p=R/'REPORT.md';s=p.read_text(encoding='utf-8');s=s.replace('Its exact output is saved in out/LEAN.log and out/FORMAL_STATUS.json.','It returned RUNTIME_UNVERIFIED after128.8s (exit1); no Lean certification was established. Its exact output is saved in out/LEAN.log and out/FORMAL_STATUS.json.')
p.write_text(s,encoding='utf-8')
for n in ['PROGRESS.json','PACKET_DELTA.json']:
 p=R/n;d=json.loads(p.read_text(encoding='utf-8'));d['blockers'].append('Optional rational-ledger Lean check RUNTIME_UNVERIFIED after128.8s; no formal certification')
 p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Recorded formal runtime outcome without promoting the mathematical rung')
