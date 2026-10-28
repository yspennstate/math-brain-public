from pathlib import Path
import json,hashlib,datetime
r=Path(__file__).resolve().parents[1];formal=json.loads((r/'out/FORMAL_RECEIPT.json').read_text(encoding='utf-8'));status=formal['status']
if formal['status']=='ATTEMPT_RECORDED' and (r/'out/LEAN.txt').exists():
 try:status=json.loads((r/'out/LEAN.txt').read_text(encoding='utf-8'))['result']['status']
 except (ValueError,KeyError):status='SETUP_UNVERIFIED'
p=r/'REPORT.md';s=p.read_text(encoding='utf-8')
s=s.replace('The narrow formal attempt returns NO_VERIFIED_FORMAL_TARGET; no Lean certificate is claimed.','The first formal setup was rejected before any compiler launch because the --stmt receipt omitted generated imports/newlines. The byte-exact --file correction and fresh memory admission are preserved; its narrow real-algebra target returns '+status+'. No full theorem is claimed Lean-checked.')
p.write_text(s,encoding='utf-8')
with (r.parents[1]/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+datetime.datetime.now(datetime.timezone.utc).isoformat()+': Formal-receipt correction: --stmt hashes include generated imports/newlines; initial setup rejected before compiler. Preserved rejection, switched to reviewed exact --file bytes with fresh memok; corrected attempt status '+status+'. Mathematical identity/tree proof and finite results unchanged.\n')
rows=[]
for q in r.rglob('*'):
 if q.is_file() and q.name!='RECEIPTS.json':
  b=q.read_bytes();assert len(b)<20000000;rows.append(dict(path=str(q.relative_to(r)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest()))
(r/'out/RECEIPTS.json').write_text(json.dumps(dict(files=rows,remote_mirror_verified=False),indent=2),encoding='utf-8')
print('FINAL FORMAL STATUS',status,'; persistence',len(rows),'files PASS')
print((r/'out/LEAN.txt').read_text(encoding='utf-8')[:1600] if (r/'out/LEAN.txt').exists() else 'Memory admission blocked compilation')
