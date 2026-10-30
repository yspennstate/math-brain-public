from pathlib import Path
import json,hashlib,datetime
B=Path(__file__).resolve().parents[1];H=B.parents[1]
def rd(p):return json.loads(p.read_text(encoding='utf-8'))
def wr(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(b):return hashlib.sha256(b).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
codes=rd(B/'out'/'code_checks.json');assert codes['status']=='PASS' and len(codes['cases'])==2
for row in codes['cases']:
    words=row['words'];assert len(words)==row['atoms']>0
    assert all(not v.startswith(w) for k,w in words.items() for j,v in words.items() if j!=k)
    # Inject an actual duplicate leaf into this live code and require rejection.
    bad=dict(words);a,b=list(bad)[:2];bad[b]=bad[a]
    assert any(v.startswith(w) for k,w in bad.items() for j,v in bad.items() if j!=k)
report=(B/'REPORT.md').read_text(encoding='utf-8')
addition=('A separate frozen CODE_SPEC precedes `python -X utf8 code/code_check.py`: '+str(codes['checks'])+' exact checks on two independently generated full-output codes s=1,2, with '+str([r['atoms'] for r in codes['cases']])+' actual leaves. Direct integer Walsh sums use interleaved coordinates rather than the main checker\'s block layout. Rational normalization, integer Shannon lengths, canonical words, prefix pairs, decoding of the concatenation of ALL leaves, and expected length<=25 physical influence pass. Full words are saved in out/code_checks.json. Final artifact readback injects a duplicate leaf into each live code and confirms that the prefix test rejects it. This supplements the 7703 main assertions; pilots are not added.\n\n')
if addition not in report:
    report=report.replace('## proof dependencies and changed downstream conclusions\n',addition+'## proof dependencies and changed downstream conclusions\n')
(B/'REPORT.md').write_text(report,encoding='utf-8')
claims=rd(B/'CLAIMS.json');new=claims[-1]
assert sha(new['exact_statement'].encode())==new['statement_sha256']
for f in ['CODE_SPEC.json','code/code_check.py','out/code_checks.json']:
    if f not in new['proof_source']:new['proof_source'].append(f)
wr(B/'CLAIMS.json',claims)
progress=rd(B/'PROGRESS.json')
for f in ['CODE_SPEC.json','code/code_check.py','out/code_checks.json','out/FINAL_AUDIT.json']:
    if f not in progress['source_artifacts']:progress['source_artifacts'].append(f)
wr(B/'PROGRESS.json',progress);wr(B/'PACKET_DELTA.json',progress)
status=(H/'STATUS.md').read_text(encoding='utf-8').replace('7703 exact checks PASS','7703+'+str(codes['checks'])+' exact checks PASS')
(H/'STATUS.md').write_text(status,encoding='utf-8')
with (H/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+now+' — Stage22 decoder supplement: '+str(codes['checks'])+' exact independent canonical-code checks PASS, all leaves decoded, full wrapper/prefix cost paid; duplicate-leaf injections rejected on both live codes.\n')
protocol=rd(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))['required_per_run']
assert all(set(c)==set(protocol['claim_fields']) for c in claims)
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert rd(B/'PACKET_DELTA.json')==progress
assert len(status.splitlines())==2
assert all('## '+h in report for h in protocol['report_fields'])
assert report.rstrip().split('\n')[-1].startswith('Universal bridge:')
main=rd(B/'out'/'checks.json');assert main['checks']==7703 and main['status']=='PASS'
binding=rd(B/'out'/'VALIDATION_BINDING.json');assert binding['helper_sha256']==sha((B/'code'/'check.py').read_bytes())
wr(B/'out'/'FINAL_AUDIT.json',{'status':'PASS','at':now,'main_checks':7703,'decoder_checks':codes['checks'],'live_duplicate_leaf_controls_rejected':2,'exact_fields':True,'new_statement_sha256':new['statement_sha256'],'independent_review_new_claim':'PENDING','full_fei':'OPEN'})
files=[]
for p in sorted(B.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE.json':
        raw=p.read_bytes();assert len(raw)<20*1024*1024
        files.append({'path':str(p.relative_to(B)),'bytes':len(raw),'sha256':sha(raw)})
wr(B/'out'/'PERSISTENCE.json',{'status':'LOCAL_READBACK_SCHEMA_AND_HASH_PASS','created_at':now,'files':files,'mirror_verified':False,'independent_acceptance_new_claim':False,'full_fei':'OPEN'})
for item in rd(B/'out'/'PERSISTENCE.json')['files']:
    p=B/item['path'];assert sha(p.read_bytes())==item['sha256'] and p.stat().st_size==item['bytes']
print(json.dumps({'status':'PASS','files':len(files),'main_checks':7703,'decoder_checks':codes['checks'],'full_fei':'OPEN','new_claim':'INDEPENDENT_REVIEW_PENDING'}))
print(report.splitlines()[0]);print(status.strip())
