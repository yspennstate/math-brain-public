from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];O=R/'out'
def get(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def dump(p,x):write(p,json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
n=get(O/'NESTED_CHECKS.json');r=get(O/'R_CHECKS.json');assert n['status']==r['status']=='PASS';assert n['cases']==5 and r['cases']==2
report=(R/'REPORT.md').read_text(encoding='utf-8')
extra=f'''Supplemental frozen adversarial checks address two specific coverage gaps rather than enlarging the main enumeration: code/check_nested.py tests four depth-three sources and recomputes the repeated-wire means directly in physical space (286 exact assertions, {n['runtime_seconds']:.6f}s); code/check_r.py tests two four-bit sources with a ternary child so inherited R_tree is strictly positive (109 exact assertions, {r['runtime_seconds']:.6f}s). The AND4 at all1/3 has R_flat256/6561 but R_tree32/2187 when the inner AND3 is atomic, whereas the all-binary tree has R_tree0. All pass. These supplement the unchanged16664 main assertions and970 pilot assertions; files out/FROZEN_NESTED.json, out/NESTED_CHECKS.json, out/FROZEN_R.json and out/R_CHECKS.json preserve the domains and exact outputs.\n\n'''
assert 'Supplemental frozen adversarial checks' not in report
report=report.replace('# proof dependencies and changed downstream conclusions',extra+'# proof dependencies and changed downstream conclusions')
write(R/'REPORT.md',report)
claims=get(R/'CLAIMS.json');claims[0]['proof_source']['adversarial_checks']=['out/NESTED_CHECKS.json','out/R_CHECKS.json'];dump(R/'CLAIMS.json',claims)
progress=get(R/'PROGRESS.json');progress['source_artifacts']+=['out/NESTED_CHECKS.json','out/R_CHECKS.json'];dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
write(A/'STATUS.md','STATE: Stage19 source-complete: A045 signed transfer HOLDS; adaptive normalizer<=18Delta, absolute conversion<=47Delta/2;16664 main+395 adversarial checks PASS;FEI OPEN.\nNEXT: Pay actual two-weight J in selected complete flat/tree reference from SAME unused original deficit after adaptive debit, retaining ordinary KL and both full terminals; A045/A042/A044 review.\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write(f'\n{now} Stage19 adversarial supplement: four depth-three formulas plus physical repeated-wire check passed286 assertions; two nonzero inherited-R controls passed109. Main16664 and pilot970 unchanged. Artifacts refreshed; next actual scale J remains unpaid.\n')
protocol=get(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']
assert set(claims[0])==set(protocol['claim_fields'])
assert set(progress)==set('packet_ids' if s.startswith('packet_ids ') else s for s in protocol['progress_fields'])
assert [s[2:] for s in report.splitlines() if s.startswith('# ')]==protocol['report_fields']
assert report.strip().splitlines()[-1].startswith('Universal bridge:')
assert claims[0]['statement_sha256']==hashlib.sha256(claims[0]['exact_statement'].encode()).hexdigest()
assert claims[0]['proof_source']['sha256']==sha(R/'PROOF.md')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(R.rglob('*')) if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json'];assert all(x['bytes']<20_000_000 for x in files)
dump(O/'PERSISTENCE_RECEIPTS.json',{'status':'PASS','checks':['exact report headings and final universal bridge','exact claim/progress field sets','claim and proof hashes','byte-identical compatibility progress','two-line current status','file sizes'],'main_assertions':16664,'pilot_assertions':970,'additional_adversarial_assertions':395,'files':files,'remote_status':'supervisor copy unverified'})
print(json.dumps({'status':'PASS','files':len(files),'main':16664,'additional_adversarial':395,'report_headings':7,'FEI':'OPEN'}))
print(report.strip().splitlines()[-1])
