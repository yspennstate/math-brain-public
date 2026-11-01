from pathlib import Path
import json, hashlib
from fractions import Fraction
from datetime import datetime, timezone
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; AGENT=RUN.parent.parent
def load(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(b): return hashlib.sha256(b).hexdigest()
protocol=load(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
req=protocol['required_per_run']; checks=[]
def check(ok,name):
    assert ok,name
    checks.append(name)
progress=load(RUN/'PROGRESS.json'); delta=load(RUN/'PACKET_DELTA.json')
fields=[s.split(' (')[0] for s in req['progress_fields']]
check(set(progress)==set(fields),'exact progress fields')
check(progress==delta and (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes(),'identical compatibility delta')
check(progress['packet_id']=='A100' and progress['packet_ids']==['A100'],'primary packet A100')
check(progress['protocol_revision']==protocol['revision'],'protocol revision')
claims=load(RUN/'CLAIMS.json')
check(len(claims)==4,'four original-source scoped review deltas')
for c in claims:
    check(set(c)==set(req['claim_fields']),'exact claim fields: '+c['claim_id'])
    check(sha(c['exact_statement'].encode())==c['statement_sha256'],'exact statement hash: '+c['claim_id'])
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
for field in req['report_fields']: check(('## '+field+'\n') in report,'report section: '+field)
check(report.strip().split('\n\n')[-1].startswith('Universal bridge:'),'final Universal bridge paragraph')
check('Full FEI is OPEN' in report,'universal mathematical status OPEN')
questions=load(OUT/'NEXT_TEN_QUESTIONS.json')
check(len(questions)==10 and len({q['id'] for q in questions})==10,'exactly ten distinct continuation questions')
status=(AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines()
check(len(status)==2 and status[0].startswith('STATE: ') and status[1].startswith('NEXT: '),'two-line rolling status')
cert=load(OUT/'INDEPENDENT_CERTIFICATE.json')
check(cert['assertions_passed']==8544 and cert['failed']==0 and len(cert['rows'])==8,'8544 completed exact certificate assertions')
for row in cert['rows']:
    for key,value in row.items():
        if isinstance(value,dict) and set(value)=={'lower','upper'}:
            check(Fraction(value['lower'])<=Fraction(value['upper']),'interval ordered: '+str(row['k'])+'/'+row['reference']+'/'+key)
    check(Fraction(row['B_over_removed']['upper'])<3,'strict k-grid erasure bound: '+str(row['k'])+'/'+row['reference'])
block=load(OUT/'A066_BLOCK_SCOPE_INDEPENDENT.json')
g=block['positive_gap']; check(Fraction(int(g['numerator']),int(g['denominator']))>0,'128-bit actual Boolean block-scope positive gap')
ledger=load(OUT/'THEOREM_RELEASE_LEDGER.json')
accepted={(r['claim_id'],str(r['version'])) for r in ledger['accepted']}
check(('A051-PROPER-BLOCK-DESCENT-SQUEEZE','1') in accepted,'A051 squeeze accepted')
check(('A021-UNIFORM-RARE-CORE-EXPANSION','1') not in accepted,'A021 false remainder excluded')
check(('A066-POSITIVE-RESTRICTION-HEAT-LEDGER','1') not in accepted,'A066 unqualified block budget excluded')
check(('A097-B05-COMPATIBLE-REFERENCE-CERTIFICATE','1') not in accepted,'A097 partial review not full acceptance')
check(('B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO','1') in accepted,'NO_GAP_FOUND verdict does not count as adverse review')
check(all(not any(v['verdict'].startswith(('GAP','ERROR','REFUT','RETRACT','REJECT')) for v in r['review_evidence']) for r in ledger['accepted']),'adverse scope reviews override stale full approvals')
for group,key in [('accepted','accepted_statement_versions'),('partial','partial_statement_versions'),('pending','pending_statement_versions'),('withdrawn_as_full_claim','withdrawn_statement_variants')]:
    check(len(ledger[group])==ledger['counts'][key],'ledger count: '+group)
check(len(load(OUT/'CORRECTION_PROPAGATION.json')['changes'])==5,'five versioned corrections')
check(load(OUT/'PARSE_FAILURES.json')==[],'source census has no parse failure')
for p in RUN.rglob('*'):
    if not p.is_file(): continue
    check(p.stat().st_size<20_000_000,'under 20 MB: '+str(p.relative_to(RUN)))
    if p.suffix=='.json': load(p)
now=datetime.now(timezone.utc).isoformat()
result={'timestamp_utc':now,'status':'PASS','checks':checks,'package_checks_passed':len(checks),
        'mathematical_checker_assertions_passed':8544,'additional_block_scope_certificates':1,
        'full_FEI_status':'OPEN','remote_mirror_and_public_release_verified':False}
(OUT/'PACKAGE_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
files += [AGENT/name for name in ['STATUS.md','WORKLOG.md','LEARNED.md']]
receipts=[]
for p in sorted(files):
    data=p.read_bytes(); receipts.append({'path':str(p),'bytes':len(data),'sha256':sha(data)})
receipt={'timestamp_utc':now,'scope':'Saved local byte hashes; excludes this self-referential receipt. No remote or source-immutability assertion.',
         'files':receipts,'readback':'All listed files were read twice and matched.'}
(OUT/'PERSISTENCE_RECEIPTS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
for row in receipts:
    b=Path(row['path']).read_bytes(); assert len(b)==row['bytes'] and sha(b)==row['sha256'],row['path']
check(load(OUT/'PERSISTENCE_RECEIPTS.json')==receipt,'receipt serialized readback')
print(json.dumps({'status':'PASS','package_checks':len(checks)-1,'mathematical_assertions':8544,
                  'additional_block_scope_certificates':1,'local_files_rehashed':len(receipts),
                  'accepted_recorded_statement_groups':ledger['counts']['accepted_statement_versions'],
                  'full_FEI':'OPEN'},indent=2))
