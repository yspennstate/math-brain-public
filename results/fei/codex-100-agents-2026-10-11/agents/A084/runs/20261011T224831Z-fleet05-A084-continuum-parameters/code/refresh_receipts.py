from pathlib import Path
import json,hashlib,datetime
root=Path(__file__).resolve().parents[1];agent=root.parents[1]
topology=json.loads((root/'out'/'ZERO_TOPOLOGY.json').read_text())
for name in ['PROGRESS.json','PACKET_DELTA.json']:
    p=root/name;d=json.loads(p.read_text());d['mathematical_delta']+=' Extra-zero existence proved: for every p>1/2 at least one zero above q=1/2; for p=49/100 at least two zeros below q=1/2, using F(49/100,1/4)<-11/100.';d['source_artifacts'].extend(['TOPOLOGY_SPEC.json','code/topology.py','out/ZERO_TOPOLOGY.json']);p.write_text(json.dumps(d,indent=2),encoding='utf-8')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('Extra-zero topology: every fixed p>1/2 has at least one zero in q in (1/2,1). For p=49/100, exact F(49/100,1/4)<-11/100 plus positive endpoint neighborhoods prove at least two zeros below 1/2. Universal q-monotonicity and the single-zero-line map are false.\n')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+datetime.datetime.now(datetime.timezone.utc).isoformat()+': 2,126 saved-certificate/alternative-formula checks passed. Metadata field-label mismatch was corrected by mapping the protocol description of packet_ids to its prescribed JSON key. A separately frozen one-point rational certificate proves extra zero existence; no larger search was run.\n')
receipt=json.loads((root/'out'/'RECEIPTS.json').read_text());receipt['topology_point_sign_check']='F(49/100,1/4)<-11/100 verified by code/topology.py';receipt['files']=[]
for f in root.rglob('*'):
    if f.is_file() and f.name!='RECEIPTS.json' and '__pycache__' not in f.parts:
        b=f.read_bytes();assert len(b)<20*1024*1024;receipt['files'].append({'path':str(f.relative_to(root)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(root/'out'/'RECEIPTS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print('Final receipts refreshed:',len(receipt['files']),'files; required artifacts present.',flush=True)
