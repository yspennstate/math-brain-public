from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
p=R/'CLAIMS.json';cs=json.loads(p.read_text(encoding='utf-8'));c=cs[-1]
old='and is <=(log2(e)-1)k<4k/9.'
new='and is <=(log2(e)-1)k<=4k/9, with the second comparison strict for k>0.'
assert old in c['exact_statement'] or new in c['exact_statement']
c['exact_statement']=c['exact_statement'].replace(old,new)
c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
p.write_text(json.dumps(cs,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='')
p=R/'code/finalize.py';s=p.read_text(encoding='utf-8');p.write_text(s.replace(old,new),encoding='utf-8',newline='')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for name in ['pilot','validation','independent']:assert json.loads((R/f'out/{name}.json').read_text(encoding='utf-8'))['status']=='PASS'
report=(R/'REPORT.md').read_text(encoding='utf-8');assert report.rstrip().split('\n\n')[-1].startswith('This stage moves C019/C024')
receipt=R/'out/PERSISTENCE_RECEIPT.json';r=json.loads(receipt.read_text(encoding='utf-8'))
for f in r['files']:
    p=R/f['path']
    if f['path'] not in ['CLAIMS.json','code\\finalize.py','code/finalize.py','DERIVATION.md']:assert sha(p)==f['sha256'],f['path']
files=[]
for p in sorted(R.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts or p==receipt:continue
    assert p.stat().st_size<20_000_000
    files.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
r['files']=files;r['boundary_correction']='strict scalar comparison only for k>0; eta comparison strict only for eta>0';r['readback']='PASS'
receipt.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8',newline='')
for f in files:assert sha(R/f['path'])==f['sha256']
print(json.dumps({'status':'PASS','files':len(files),'report_readback':True,'statement_hashes':True,'FEI':'OPEN','external_review':'PENDING'}))
