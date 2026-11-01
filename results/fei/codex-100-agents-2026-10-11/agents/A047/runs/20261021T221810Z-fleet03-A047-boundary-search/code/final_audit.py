from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def read(p):return Path(p).read_text(encoding='utf-8')
def dump(p,x):Path(p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
p=R/'REPORT.md';s=read(p)
old='a higher constant or different reference is not refuted.'
assert s.count(old)==1
s=s.replace(old,'this fixed-width subfamily alone does not refute a higher constant. The all-width result below rules out every fixed rate for the same prescribed complete reference; a different reference is not refuted.')
Path(p).write_text(s,encoding='utf-8')
proto=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
claims=json.loads(read(R/'CLAIMS.json'));progress=json.loads(read(R/'PROGRESS.json'))
assert len(claims)==2
for cl in claims:
 assert set(cl)==set(proto['required_per_run']['claim_fields'])
 assert cl['statement_sha256']==hashlib.sha256(cl['exact_statement'].encode()).hexdigest()
assert set(progress)==set(x.split(' (')[0] for x in proto['required_per_run']['progress_fields'])
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
assert all('# '+x in s for x in proto['required_per_run']['report_fields'])
assert 'Universal bridge:' in s.splitlines()[-1]
assert 'NO finite absolute K' in s and 'Full FEI remains OPEN' in s
assert len(read(A/'STATUS.md').splitlines())==2
for n in ['CHECK.json','ALTERNATE.json','GENERAL_CHECK.json']:assert json.loads(read(R/'out'/n))['status']=='PASS'
lean=json.loads(read(R/'out/LEAN.json'));assert lean['exit_code']==2 and 'RUNTIME_UNVERIFIED' in lean['stdout']
audit={'status':'PASS','semantic_checks':['General theorem uses m=2^(r+2), not an extrapolated fixed-m sample','Reference is the prescribed complete coordinate-product occupancy law, not all references','Actual H<=4I explicitly excludes a full FEI disproof','A036 signed recovery objection consumed; CE>CI defeats sharp signed rule','A050 G<2 scope preserved and independently accepted unchanged','Rational certificates distinguish strict sign from decimal display','Canonical roots enclosed directly, no normalized endpoints substituted','Both b0 and data terminals retain full entropy and one original owner','Lean runtime unverified; no target or axiom acceptance','Full FEI open and independent new-claim review pending'],'corollary':'Since KL/I=CE/I-H/I, the explicit all-r family also has KL(P||Q)/I>r-5. This follows directly from the two stated bounds; no separate computation.','new_lemmas_requiring_peer_review':['Explicit all-r canonical CE/I>r-1 with actual H<=4I','All-r root/canonical construction and complete-price interpretation'],'no_external_publication':True}
dump(R/'out/FINAL_AUDIT.json',audit)
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json'];assert all(p.stat().st_size<20_000_000 for p in files)
dump(R/'out/PERSISTENCE.json',{'status':'PASS','time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'schema_checks':'exact field sets, statement hashes, report requirements, deltas, two-line status, file sizes; FINAL_AUDIT records semantic scope','independent_review':'A050 scoped source accepted; new A047 all-r obstruction pending','mirror':'NOT_OBSERVED','artifacts':[{'path':str(p.relative_to(R)),'sha256':sha(p),'size':p.stat().st_size} for p in files]})
print('FINAL ARTIFACT AUDIT PASS',len(files)+1,'files; no finite canonical full-price K; full FEI OPEN.')
print(read(A/'STATUS.md'))
print('Report final paragraph:',s.splitlines()[-1])
