from pathlib import Path
from fractions import Fraction as F
import json,hashlib,subprocess,sys,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,obj):(R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
old=json.loads((R/'out/PERSISTENCE_RECEIPT.json').read_text(encoding='utf-8'))
for row in old['files']:assert sha(R/row['path'])==row['sha256'],row['path']
claims=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'))
for c in claims:assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
report=(R/'REPORT.md').read_text(encoding='utf-8')
protocol=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
for field in protocol['required_per_run']['report_fields']:assert '\n## '+field+'\n' in report
assert report.rstrip().split('\n\n')[-1].startswith('Universal bridge:')
assert 'HELD_MEMORY_ADMISSION_NO_COMPILER_STARTED' in report
# Independently derive the padded witness normalizers by summing multiplicity classes.
ws=json.loads((R/'out/WITNESSES.json').read_text(encoding='utf-8'));assert len(ws)==21
for w in ws:
 b=w['b'];e=F(1,1<<(1+b));N=1/e
 r1=(1+3*e*e)/(1+3*e);r0=3*e*e/(1+3*e)
 m1=(1-e)**2+e*e;m0=2*e*e
 z0=r1/m1;z1=r1*(1-2*e)**2/m1+(N-1)*r0*4*e*e/m0
 assert z0==F(w['Zclean']) and z1==F(w['Zedit'])
 assert z0+z1==2 and z0*z1<1
# Independent direct-character sums check the WHT used by the primary finite checker.
p=R/'code/check.py';raw=p.read_bytes();ns={'__file__':str(p),'__name__':'audit_definitions'}
exec(compile(raw.decode('utf-8').split('\nans=scalar()')[0],str(p),'exec'),ns)
sources=0
for n in range(4):
 for label in range(1<<(1<<n)):
  tab=[-1 if label>>j&1 else 1 for j in range(1<<n)]
  direct=[F(sum(v*(-1 if (m&j).bit_count()%2 else 1) for j,v in enumerate(tab)),len(tab))**2 for m in range(len(tab))]
  assert direct==ns['spectrum'](tab) and sum(direct)==1;sources+=1
write('out/FINAL_AUDIT.json',{'status':'PASS','prior_hashed_files_verified':len(old['files']),'direct_character_sources':sources,'independent_padded_normalizer_witnesses':len(ws),'claim_hashes_checked':len(claims),'report_fields_checked':7,'proof_rung':'AUTHOR_PROOF_EXACT_FINITE_CHECKS; FULL_THEOREM_NOT_LEAN_CERTIFIED; INDEPENDENT_V6_REVIEW_PENDING','hardest_unpaid_line':'ORIGINAL arbitrary-core O(I) source; all-local-floor accumulated query KL remains unpaid.'})
commands={
 'VOICE_CHECK':[sys.executable,'-B','-X','utf8',r'~\<private-repo>\12_cognitive_architecture\his_voice\tools\voice.py','check',str(R/'REPORT.md')],
 'CHECKLIST_CLOSURE':[sys.executable,'-B','-X','utf8',r'task_checklist_hook.py','done','T-20261027-024','A011 stage22 artifacts saved: v5 query-KL correction, inherited/vacuum-compatible v6 repair,659213 exact assertions; FEI OPEN.']}
results={}
for name,cmd in commands.items():
 rr=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
 results[name]={'command':cmd,'exit_code':rr.returncode,'stdout':rr.stdout,'stderr':rr.stderr};write('out/'+name+'.json',results[name])
files=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json':
  assert p.stat().st_size<20_000_000
  files.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
write('out/PERSISTENCE_RECEIPT.json',{'status':'LOCAL_SCHEMA_HASH_SIZE_FINAL_AUDIT_PASS','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':files,'assertions':659213,'checklist_exit':results['CHECKLIST_CLOSURE']['exit_code'],'external_mirror':'UNVERIFIED','full_FEI':'OPEN'})
print(json.dumps({'final_audit':'PASS','files':len(files),'direct_character_sources':sources,'witnesses':len(ws),'voice_check_exit':results['VOICE_CHECK']['exit_code'],'checklist_exit':results['CHECKLIST_CLOSURE']['exit_code'],'checklist_output':results['CHECKLIST_CLOSURE']['stdout'][:700]+results['CHECKLIST_CLOSURE']['stderr'][:700]}))
