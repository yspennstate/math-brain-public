from pathlib import Path
from datetime import datetime
import json,hashlib,subprocess
H=Path(__file__).resolve().parent;B=Path('~/brain-repo')
P=B/'06_math_research/frontier/rows/T186/routes.jsonl'
M=B/'12_cognitive_architecture/agent_mesh/agent_mesh.py';PY='C:/Python314/python.exe';A='codex-term-362ebe34'
for verb,extra in [('claim',['--mode','write','--ttl','600','--purpose','Record new conditional reverse ancestry route to prevent duplicate work']),('assert',[])]:
 subprocess.run([PY,str(M),verb,'--agent',A,'--resource',str(P),*extra],capture_output=True,check=True)
r={'at':datetime.now().astimezone().isoformat(),'by':A,'row':'T186','route':'Palm-adjoint reverse causal ancestry, shared-subtree Lp moment and canonical right history occupation resolvents',
 'status':'live','why':'Proposed conditional ideal-tree lemma: rho-adjoint subcriticality gives finite reverse path count and some p>1 moment; marked late-source relative occupation tends to zero in averaged Lp. Independent review pending; no finite graph transfer or maximum-over-rare-type claim.',
 'evidence':str(H/'T186_REVERSE_ANCESTRY_ROUTE.md'),'evidence_sha256':hashlib.sha256((H/'T186_REVERSE_ANCESTRY_ROUTE.md').read_bytes()).hexdigest()}
old=P.read_bytes() if P.exists() else b''
assert r['route'].encode() not in old,'Already recorded'
P.write_bytes(old+(json.dumps(r)+'\n').encode())
(H/'ROUTES.jsonl').open('ab').write((json.dumps(r)+'\n').encode())
(H/'T186_REVERSE_ROUTE_RECORD.json').write_bytes((json.dumps(r,indent=2)+'\n').encode())
print(json.dumps(r))
