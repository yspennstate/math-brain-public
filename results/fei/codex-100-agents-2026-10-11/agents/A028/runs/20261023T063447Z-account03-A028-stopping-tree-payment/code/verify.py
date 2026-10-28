"""Pinned package readback; live mathematical mutation guards, not pass-label only."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
import exact_helper as e
R=Path(__file__).resolve().parents[1];AGENT=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def vec(d):return {int(k):F(v) for k,v in d.items()}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def eq(a,b):assert not e.add(a,e.scale(b,-1))
receipt=read(R/'out/persistence.json')
for row in receipt['files']:
    p=R/row['path'];assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes']
claim=read(R/'CLAIMS.json')[0];progress=read(R/'PROGRESS.json')
assert claim['version']==8 and claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode()).hexdigest()
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
proto=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
assert set(claim)==set(proto['required_per_run']['claim_fields'])
fields=set(proto['required_per_run']['progress_fields']);fields.remove('packet_ids (one primary ID, for compatibility)');fields.add('packet_ids')
assert set(progress)==fields and progress['gap_id']=='C019' and progress['packet_ids']==['A028']
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+field in report for field in proto['required_per_run']['report_fields'])
assert report.rsplit('## ',1)[1].startswith('Universal bridge\n')
assert 'first unsupported universal line' in report and 'Root controller calibration' in report and 'not paid by the root JS' in report
main=read(R/'out/check_full.json');ind=read(R/'out/independent.json');obs=read(R/'out/obstruction.json')
assert (main['cases'],main['queries'],main['assertions'])==(3521,8748,1088506)
assert (ind['nodes'],ind['leaves'],ind['assertions'])==(166,84,6781)
assert sha(R/'code/check.py')==main['script_sha256']
assert main['guards'].get('vacuum_needed') and main['guards'].get('positive_shape')
guards=[]
v=main['guards']['vacuum_needed']
assert e.enclosure(vec(v['vacuum']))[0]>0
try:eq(vec(v['S']),vec(v['Z']))
except AssertionError:guards.append('REJECTED dropping actual controller vacuum KL on a live inherited child')
else:raise AssertionError('vacuum-dropping mutation falsely passed')
obsdelta=vec(obs['strict_excess']);assert e.enclosure(obsdelta)[0]>0
assert obs['Jroot']==obs['Zroot']==obs['source_debt']=='0' and obs['all_source_children_nonconstant']
try:assert e.enclosure(obsdelta)[1]<=0
except AssertionError:guards.append('REJECTED JS-only conversion payment on actual nonconstant-source dummy-DATA witness; integer4>3')
else:raise AssertionError('missing-root-liability mutation falsely passed')
shape=vec(main['fixture']['root_shape']);assert e.enclosure(shape)[0]>0
old=read(R.parent/'20261023T023055Z-account03-A028-stopping-tree-payment/out/fixture.json')
fix=main['fixture'];eq(vec(old['original_reserve']),e.add(vec(fix['reserve']),shape))
eq(vec(fix['root_S']),vec(old['root_Z_equals_J']))
assert e.enclosure(vec(fix['reserve']))[0]>0
assert fix['U']==old['original_U']=='45/4' and fix['old_debit']==old['old_debit']=='1/8'
rows=positive_refunds=terminals=0
for pol in main['policies']:
    assert len(pol['terminals'])==pol['leaves'] and len(pol['receipts'])==pol['nodes']-pol['leaves']
    terminals+=len(pol['terminals']);ledger=pol['ledger']
    eq(e.add(vec(ledger['sig']),vec(ledger['A']),vec(ledger['Sleaf'])),vec(fix['root_S']))
    unused=e.add(vec(fix['reserve']),vec(ledger['A']),vec(ledger['Sleaf']))
    actual_unused=e.add({2:F(fix['U'])-F(fix['old_debit'])},e.scale(e.add(vec(ledger['path']),vec(ledger['ce'])),-1))
    eq(unused,actual_unused);assert e.enclosure(unused)[0]>0
    for row in pol['receipts']:
        rows+=1
        sigma,kappa=vec(row['sigma']),vec(row['kappa']);refund=e.add(vec(row['Ef']),vec(row['Of']))
        eq(kappa,e.add(sigma,refund))
        assert sum(F(x) for x in row['rho'])==1 and min(F(x) for x in row['rho'])>0
        assert len(row['child_D'])==len(row['child_S'])==2
        if e.enclosure(refund)[0]>0:
            positive_refunds+=1
            try:eq(kappa,sigma)
            except AssertionError:pass
            else:raise AssertionError('output-refund-dropping mutation falsely passed')
assert rows>0 and terminals>0 and positive_refunds>0
guards.append('REJECTED output-refund-dropping mutation on '+str(positive_refunds)+' live actual query rows')
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
print(report[report.index('The first unsupported universal line'):report.index('## executed validation')].strip())
out=dict(status='PASS',pinned_files_verified=len(receipt['files']),live_query_receipts=rows,full_terminal_receipts=terminals,positive_output_refund_rows=positive_refunds,guards=guards,original_v7_reserve_reconciled='new reserve=old reserve-controller shape debt; same U/old debit',full_FEI='OPEN',v8_peer_review='PENDING')
(R/'out/verify.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='persistence.json']
assert all(p.stat().st_size<20_000_000 for p in files)
receipt['files']=[dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)) for p in files]
receipt['status']='LOCAL_SAVED_READBACK_VERIFIED';receipt['readback']='out/verify.json'
(R/'out/persistence.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps(out))
