"""Final owner-visible readback and persistence receipts; no research search."""
import datetime
import hashlib
import json
from fractions import Fraction
from pathlib import Path

r=Path(__file__).resolve().parents[1]
a=r.parents[1]
def read(name):
    return json.loads((r/name).read_text(encoding='utf-8'))
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
old=read('out/MANIFEST.json')
for entry in old['entries']:
    p=(r/entry['path']).resolve()
    assert p.is_relative_to(r)
    assert p.stat().st_size==entry['bytes'] and digest(p)==entry['sha256'],p
claims=read('CLAIMS.json')['claims']
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
for c in claims:
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
own=next(c for c in claims if c['claim_id']=='A080-EXACT-HULL-TENSOR-FAITHFUL-BANK')
assert hashlib.sha256(own['exact_statement'].encode('utf-8')).hexdigest()==own['statement_sha256']
source=read('out/A089_SOURCE_CLAIMS.json')
if isinstance(source,dict):
    source=source['claims']
reviewed=next(c for c in claims if c['claim_id']=='A089-SHARPENED-SIGNED-COMPOSITION-RESERVE')
original=next(c for c in source if c['claim_id']==reviewed['claim_id'])
for key in ('claim_id','version','exact_statement','hypotheses','statement_sha256'):
    assert original[key]==reviewed[key]
progress=read('PROGRESS.json')
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert (r/'PROGRESS.json').read_bytes()==(r/'PACKET_DELTA.json').read_bytes()
assert progress['packet_ids']==['A080']
report=(r/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:
    assert '\n## '+field+'\n' in report
assert report.rsplit('\n## ',1)[1].startswith('Universal bridge\n')
assert 'Full FEI remains OPEN' in report and 'degraded/unverified' in report
status=(a/'STATUS.md').read_text(encoding='utf-8').splitlines()
assert len(status)==2 and status[0].startswith('STATE:') and status[1].startswith('NEXT:')
for name in ('WORKLOG.md','LEARNED.md'):
    text=(a/name).read_text(encoding='utf-8')
    assert r.name in text and 'A089130925-SIGNED-DEBIT-ERRATUM' in text
sign=read('out/SOURCE_SIGN_CHECK.json')
assert sign['status']=='PASS' and digest(r/'out/A089_SOURCE_PROOF.md')==sign['source_proof_sha256']
strong=sign['nonnegative_parent_debit_witness']
assert strong['source_written_parent_debit']=='0'
assert min(map(Fraction,strong['source_written_child_debits']))<0
assert min(map(Fraction,strong['corrected_child_debits']))>=0
assert len(strong['all_restrictions'])==27
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
entries=[]
for p in sorted(r.rglob('*')):
    if p.is_file():
        assert p.stat().st_size<20*1024*1024
        if p.name not in ('MANIFEST.json','FINAL_AUDIT.json'):
            entries.append({'path':str(p.relative_to(r)),'bytes':p.stat().st_size,'sha256':digest(p)})
manifest={'written_at_utc':stamp,'run_id':r.name,'entries':entries,'readback_previous_entries_verified':len(old['entries'])}
(r/'out/MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
audit=read('out/FINAL_AUDIT.json')
audit.update({'status':'PASS','files_manifested':len(entries),'readback_at_utc':stamp,'previous_manifest_entries_hash_verified':len(old['entries']),'source_review_statement_hypotheses_version_unchanged':True,'admissible_parent_sign_witness_checked':True,'source_owner_erratum':'PENDING_A089','proof_independence':'Separate author implementations; external independent-agent acceptance pending'})
(r/'out/FINAL_AUDIT.json').write_text(json.dumps(audit,indent=2)+'\n',encoding='utf-8')
lines=report.splitlines()
print(json.dumps({'status':'PASS','utc':stamp,'files':len(entries),'main_and_certificate_predicates':read('out/main_summary.json')['exact_predicates']+read('out/verification_summary.json')['exact_predicates'],'claims':len(claims),'report_title':lines[0],'last_heading':'Universal bridge','external_review':'PENDING','full_fei':'OPEN','source_erratum':'PENDING_A089','stage_jobs_running':False}),flush=True)
