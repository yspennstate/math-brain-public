import json,pathlib,subprocess
w=pathlib.Path('~/brain_workers/w538')
p=w/'publish_packet.py';s=p.read_text(encoding='utf-8-sig');s=s.replace('Please independently check O1, B1, O2, especially beta','Please independently check B1, O1-O4 and the paired C5 derivation; especially beta');p.write_text(s,encoding='utf-8')
command=['python','-X','utf8','~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py','claim','--agent','w538','--resource','~/math-brain-inbox/w538','--mode','write','--purpose','Own P0309 final DRAFT and atomic rename only; paired C1-C5 audit complete; no ingestion','--ttl','900']
r=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',timeout=60)
(w/'INBOX_CLAIM_RECEIPT.json').write_text(json.dumps({'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr},indent=2),encoding='utf-8')
print(r.stdout or r.stderr)
assert r.returncode==0,'Draft publication requires the narrow covering claim'
r=subprocess.run(['python','-X','utf8',str(p)],capture_output=True,text=True,encoding='utf-8',timeout=240)
(w/'PUBLICATION_RECEIPT.json').write_text(json.dumps({'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr},ensure_ascii=False,indent=2),encoding='utf-8')
print(r.stdout);print(r.stderr)
raise SystemExit(r.returncode)
