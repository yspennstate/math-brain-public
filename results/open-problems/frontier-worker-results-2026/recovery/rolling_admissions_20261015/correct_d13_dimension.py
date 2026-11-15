from pathlib import Path
from datetime import datetime
import json,hashlib,subprocess
H=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();old=H/'T170-LEAD-ROLLING-D13-001_v1.md';new=H/'T170-LEAD-ROLLING-D13-001_v2.md'
s=old.read_text(encoding='utf-8');assert s.count('bond FPP on Z^12,')==1
s=s.replace('bond FPP on Z^12,','bond FPP on Z^13,',1).replace('D13-001 v1:','D13-001 v2:',1)
assert 'subset of Z^12' in s and 'bond FPP on Z^13' in s
new.write_text(s,encoding='utf-8');r=json.loads((H/'T170_D13_SUBMISSION.json').read_bytes());r['version']=2;r['proof_sha256']=sha(new);r['files'].pop(old.name);r['files'][new.name]=sha(new);r['correction']='v1 accidentally renamed ambient model dimension to12 while correctly setting transverse dimension12. v2 corrects ONLY ambient model label to13 and version; all rates, numerical bounds and proofs unchanged. Original v1 preserved; review v2 only.';r['at']=datetime.now().astimezone().isoformat();(H/'T170_D13_SUBMISSION_v2.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
for target in ['codex-w683','codex-term-agent']:
 p=subprocess.run(['C:/Python314/python.exe','~/brain-repo/12_cognitive_architecture/agent_mesh/agent_mesh.py','send','--agent','codex-term-362ebe34','--to',target,'--topic','T170-D13-v2-correction','--body',r['correction']+' Corrected frozen proof '+str(new)+' SHA256 '+sha(new)+' manifest T170_D13_SUBMISSION_v2.json. Please audit claim version2, not1.','--require-ack'],capture_output=True,check=True);print('Correction delivered to '+target,flush=True)
(H/'T170_D13_VERSION_CORRECTION.json').write_text(json.dumps({'at':r['at'],'original_sha256':sha(old),'corrected_sha256':sha(new),'correction':r['correction']},indent=2)+'\n',encoding='utf-8')
for n in ['NEXT.md','STATUS.md']:
 p=H/n;p.write_bytes((r['at']+' D13 v1 ambient label accidentally Z12 from cascading substitutions; corrected immutablev2 SHA '+sha(new)+', actual transverseZ12/ambientZ13, all numeric unchanged; both reviewers notified. DO NOT audit/admit v1.\n').encode()+p.read_bytes())
