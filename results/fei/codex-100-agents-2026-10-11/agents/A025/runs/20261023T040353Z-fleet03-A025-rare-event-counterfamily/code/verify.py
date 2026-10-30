"""Read back concrete owner-visible artifacts and exact receipt, then hash."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
import independent as E
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'out'
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
claims=read(ROOT/'CLAIMS.json'); progress=read(ROOT/'PROGRESS.json'); report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in claims)
assert all(hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256'] for c in claims)
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert progress['packet_ids']==['A025']
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
assert report.rstrip().splitlines()[-1].startswith('Universal bridge:')
assert len((ROOT.parents[1]/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
outputs={n:read(OUT/(n+'.json')) for n in ('pilot','main','targeted','REPLAY','SCALAR','FIXTURE')}
assert all(x['status']=='PASS' for x in outputs.values())
assert outputs['main']['cases']==6144 and outputs['targeted']['cases']==256
assert outputs['REPLAY']['cases']==48 and outputs['REPLAY']['controller_states']==576
assert len(outputs['SCALAR']['dense_boolean_witness'])==6
rows=outputs['FIXTURE']['physical_rows']; assert len(rows)==8
assert outputs['FIXTURE']['positive_raw_rows']==8
for r in rows:
    assert len(r['actual_rho'])==2 and sum(map(Fraction,r['actual_rho']))==1
    assert all(Fraction(x)>0 for x in r['actual_rho'])
    assert Fraction(r['raw_kappa_bounds'][0])>0
    load=lambda key:{int(k):Fraction(v) for k,v in r[key].items()}
    assert E.same(E.add(load('raw_kappa'),E.scale(load('erasure_E'),-1),E.scale(load('outcome_O'),-1)),load('net_sigma'))
for filename,pin in read(OUT/'HELPER_PROVENANCE.json').items():
    assert digest(ROOT/'code'/filename)==pin['sha256']
total=sum(x['assertions'] for x in outputs.values())
audit={'status':'PASS','total_exact_assertions':total,'receipt_rows_checked':len(rows),'positive_raw_reset_rows':outputs['FIXTURE']['positive_raw_rows'],'independent_person_review':'PENDING','formal_verified':False,'full_FEI':'OPEN','interrupted_original_targeted':'NOT_A_PASS'}
(OUT/'FINAL_AUDIT.json').write_text(json.dumps(audit,indent=2)+'\n',encoding='utf-8',newline='')
manifest=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.name!='ARTIFACT_CHECK.json':
        assert p.stat().st_size<20_000_000
        manifest.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':digest(p)})
old=read(OUT/'ARTIFACT_CHECK.json'); old['files']=manifest; old['final_receipt_audit']=audit
(OUT/'ARTIFACT_CHECK.json').write_text(json.dumps(old,indent=2)+'\n',encoding='utf-8',newline='')
for row in manifest: assert digest(ROOT/row['path'])==row['sha256']
print(json.dumps({'status':'PASS','files':len(manifest),'assertions':total,'positive_raw_rows':outputs['FIXTURE']['positive_raw_rows'],'max_file_bytes':max(r['bytes'] for r in manifest)}))
