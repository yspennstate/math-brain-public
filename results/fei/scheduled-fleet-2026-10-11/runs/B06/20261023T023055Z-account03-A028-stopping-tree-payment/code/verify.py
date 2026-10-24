"""Read back pinned artifacts and reject the live refund-dropping mutation."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
import exact_helper as e
ROOT=Path(__file__).resolve().parents[1]
def load(name):return json.loads((ROOT/name).read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def vec(x):return {int(k):F(v) for k,v in x.items()}
receipt=load('out/persistence.json')
for row in receipt['files']:
    p=ROOT/row['path']
    assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],str(p)
claim=load('CLAIMS.json')[0];progress=load('PROGRESS.json')
assert sha(ROOT/'PROGRESS.json')==sha(ROOT/'PACKET_DELTA.json')
assert hashlib.sha256(claim['exact_statement'].encode()).hexdigest()==claim['statement_sha256']
assert claim['version']==7 and progress['gap_id']=='C019' and progress['packet_ids']==['A028']
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
fields=set(protocol['required_per_run']['progress_fields']);fields.remove('packet_ids (one primary ID, for compatibility)');fields.add('packet_ids')
assert set(progress)==fields
text=(ROOT/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+field in text for field in protocol['required_per_run']['report_fields'])
assert text.rsplit('## ',1)[1].startswith('Universal bridge\n')
assert 'source/controller suppliers' in text
main=load('out/check_full.json');pilot=load('out/check_pilot.json');ind=load('out/independent.json');fix=load('out/fixture.json')
assert (main['roots'],main['queries'],main['assertions'])==(6628,17116,1666968)
assert (pilot['roots'],ind['nodes'],ind['leaves'],ind['assertions'])==(480,166,84,4355)
assert sha(ROOT/'code/check.py')==main['script_sha256']
assert 'import check' not in (ROOT/'code/independent.py').read_text(encoding='utf-8')
assert 'exact_helper' not in (ROOT/'code/independent.py').read_text(encoding='utf-8')
J=vec(fix['root_Z_equals_J']);assert e.enclosure(J)[0]>0
sharp=fix['policies'][1]['ledger']
assert vec(sharp['sig'])==J and not sharp['A'] and not sharp['zl']
assert e.enclosure(vec(fix['original_reserve']))[0]>0
guards=[];read_queries=0;refund_rows=0
for pol in fix['policies']:
    ledger=pol['ledger']
    assert not e.add(vec(ledger['sig']),vec(ledger['A']),vec(ledger['zl']),e.scale(J,-1))
    remaining=e.add({2:F(fix['original_U'])-F(fix['old_debit'])},e.scale(e.add(vec(ledger['path']),vec(ledger['ce'])),-1))
    assert remaining==vec(pol['remaining']) and e.enclosure(remaining)[0]>0
    # Actual unused original credit, with old debit retained.
    via_slack=e.add(vec(fix['original_reserve']),vec(ledger['A']),vec(ledger['zl']))
    assert remaining==via_slack
    for row in pol['queries']:
        read_queries+=1
        sigma=vec(row['sigma']);kappa=vec(row['kappa']);refund=e.add(vec(row['Ef']),vec(row['Of']))
        assert not e.add(kappa,e.scale(sigma,-1),e.scale(refund,-1))
        if e.enclosure(refund)[0]>0:
            refund_rows+=1
            try:
                assert kappa==sigma
            except AssertionError:
                guards.append(dict(policy=pol['order'],query=row['query'],mutation='replace raw reset with net reset, dropping physical erasure/outcome refunds',verdict='REJECTED_ON_LIVE_NONCONSTANT_FIXTURE',refund_interval=[str(v) for v in e.enclosure(refund)]))
            else:raise AssertionError('positive-control mutation was falsely accepted')
assert read_queries==22 and refund_rows>0 and guards
status=(ROOT.parents[1]/'STATUS.md').read_text(encoding='utf-8').splitlines()
assert len(status)==2 and status[0].startswith('STATE:') and status[1].startswith('NEXT:')
out=dict(status='PASS',pinned_files_verified=len(receipt['files']),physical_query_receipts_read=read_queries,positive_refund_rows=refund_rows,guards=guards,nonempty_domain_verified=True,statement_and_schema_verified=True,unused_original_credit_identity_verified=True,full_FEI='OPEN',independent_v7_review='PENDING')
(ROOT/'out/verify.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
files=[p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='persistence.json']
assert all(p.stat().st_size<20_000_000 for p in files)
receipt['files']=[dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=sha(p)) for p in files]
receipt['status']='LOCAL_SAVED_READBACK_VERIFIED';receipt['final_readback']='out/verify.json'
(ROOT/'out/persistence.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({k:v for k,v in out.items() if k!='guards'}))
print('refund-dropping mutation: rejected on '+str(len(guards))+' actual query receipts')
