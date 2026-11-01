from pathlib import Path
import json,hashlib
from fractions import Fraction as F
from datetime import datetime,timezone
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; AGENT=RUN.parent.parent
def load(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(b): return hashlib.sha256(b).hexdigest()
checks=[]
def check(ok,msg):
    assert ok,msg
    checks.append(msg)
protocol=load(OUT/'EXECUTION_PROTOCOL_SNAPSHOT.json'); req=protocol['required_per_run']
p=load(RUN/'PROGRESS.json'); d=load(RUN/'PACKET_DELTA.json')
check(set(p)=={s.split(' (')[0] for s in req['progress_fields']},'exact progress fields')
check(p==d and (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes(),'byte-identical packet compatibility copy')
check(p['protocol_revision']==protocol['revision'] and p['packet_ids']==['A100'] and p['packet_id']=='A100','protocol revision and primary packet')
claims=load(RUN/'CLAIMS.json'); check(len(claims)==2,'two original-source review deltas')
for c in claims:
    check(set(c)==set(req['claim_fields']),'exact claim fields: '+c['claim_id'])
    check(sha(c['exact_statement'].encode())==c['statement_sha256'],'exact statement hash: '+c['claim_id'])
    check(c['review_records'][-1]['reviewer']=='A100/fleet05' and not c['review_records'][-1]['material_repair_to_reviewed_version'],'independent review without coauthor repair: '+c['claim_id'])
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
for s in req['report_fields']: check('## '+s+'\n' in report,'report field: '+s)
check(report.strip().split('\n\n')[-1].startswith('Universal bridge:'),'final Universal bridge paragraph')
check('Full FEI is OPEN' in report,'universal target remains OPEN')
status=(AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines()
check(len(status)==2 and status[0].startswith('STATE: ') and status[1].startswith('NEXT: '),'two-line current status')
check(all((AGENT/f).is_file() for f in ['WORKLOG.md','LEARNED.md']),'rolling durable notes exist')
q=load(OUT/'NEXT_TEN_QUESTIONS.json'); check(len(q)==10 and len({x['id'] for x in q})==10,'ten unique research questions')
cert=load(OUT/'INDEPENDENT_CHECK.json')
check(cert['status']=='PASS' and cert['assertions_passed']==14748 and cert['failures']==0,'14748 completed exact assertions')
check(cert['heat_roots']==276 and cert['activated_roots']==240,'frozen final case counts')
check(cert['runtime_seconds']<60,'completed mathematical job below 60 seconds')
check(F(cert['e_enclosure']['lower'])<F(cert['e_enclosure']['upper']),'rigorous e enclosure ordered')
check(F(cert['beta_lower'])==2+2/F(cert['e_enclosure']['upper'])**2,'joint-budget certification uses a lower bound on actual beta')
pilot=load(OUT/'PILOT_CHECK.json'); check(pilot['assertions_passed']==148 and pilot['runtime_seconds']<60,'completed pilot separated from final count')
mutation=load(OUT/'SUPPORT_CONDITIONING_CERTIFICATE.json')
check(mutation['status']=='PASS' and mutation['D_complete_bits']==1 and mutation['D_support_conditioned_bits']==0 and mutation['actual_M_bits']==0,'actual Boolean support-conditioning negative control')
check(mutation['incorrect_conditioned_substitution_M_bits']=='1/2' and mutation['reference_mass_on_derivative_support']=='1/2','lost support mass retained explicitly')
ledger=load(OUT/'THEOREM_RELEASE_LEDGER.json'); accepted={(r['claim_id'],str(r['version'])) for r in ledger['accepted']}
for c,v in [('A066-POSITIVE-RESTRICTION-HEAT-LEDGER','2'),('A096-TERMINAL-KL-REFUND-AUDIT','1'),('A090-PARITY-TAIL-LOW-INFLUENCE-COMPLETENESS','1'),('A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER','1'),('B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO','1')]:
    check((c,v) in accepted,'required scoped acceptance retained: '+c+'@'+v)
for c,v in [('A066-POSITIVE-RESTRICTION-HEAT-LEDGER','1'),('A021-UNIFORM-RARE-CORE-EXPANSION','1')]:
    check((c,v) not in accepted,'false or unqualified old bundle excluded: '+c+'@'+v)
for r in ledger['accepted']:
    check(any(v['verdict'] in ledger['full_verdict_dictionary'] for v in r['review_evidence']),'explicit full-scope verdict: '+r['claim_id'])
    check(not any(v['verdict'].startswith(('GAP','ERROR','REFUT','RETRACT','REJECT')) for v in r['review_evidence']),'no unresolved negative scope verdict: '+r['claim_id'])
for group,key in [('accepted','accepted_statement_versions'),('partial','partial_statement_versions'),('pending','pending_statement_versions'),('withdrawn_as_full_claim','withdrawn_statement_variants')]:
    check(len(ledger[group])==ledger['counts'][key],'ledger count matches: '+group)
check(any(x['reason']=='review explicitly concerns another version' and x['claim_id']=='A066-POSITIVE-RESTRICTION-HEAT-LEDGER' for x in ledger['ignored_nonindependent_or_other_version_reviews']),'v1 review not silently applied to v2')
check(load(OUT/'PARSE_FAILURES.json')==[],'no source JSON parse failures')
states=load(OUT/'PERSISTENCE_AND_RELEASE_STATES.json')
check(not states['canonical_adoption_verified'] and not states['durable_private']['new_run_remote_mirror_verified'] and not states['publicly_released']['new_release_verified'],'save/review distinct from remote adoption and release')
for f in RUN.rglob('*'):
    if not f.is_file(): continue
    check(f.stat().st_size<20_000_000,'under 20 MB: '+str(f.relative_to(RUN)))
    if f.suffix=='.json': load(f)
now=datetime.now(timezone.utc).isoformat()
result={'timestamp_utc':now,'status':'PASS','package_checks_passed':len(checks),'checks':checks,
        'mathematical_assertions_passed':14748,'additional_normalization_countercertificate':1,
        'full_FEI_status':'OPEN','proof_validation_limit':'Package checks and finite certificates do not certify the entire accepted upstream inventory.'}
(OUT/'PACKAGE_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
files=[f for f in RUN.rglob('*') if f.is_file() and f.name!='PERSISTENCE_RECEIPTS.json']+[AGENT/f for f in ['STATUS.md','WORKLOG.md','LEARNED.md']]
rows=[{'path':str(f),'bytes':f.stat().st_size,'sha256':sha(f.read_bytes())} for f in sorted(files)]
receipt={'timestamp_utc':now,'scope':'Current local run and rolling files; excludes this self-referential receipt. Remote durability/public release not asserted.','files':rows,'readback':'All listed bytes reread and matched.'}
(OUT/'PERSISTENCE_RECEIPTS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
for row in rows:
    b=Path(row['path']).read_bytes(); assert len(b)==row['bytes'] and sha(b)==row['sha256'],row['path']
assert load(OUT/'PERSISTENCE_RECEIPTS.json')==receipt
print(json.dumps({'status':'PASS','package_checks':len(checks),'local_files_rehashed':len(rows),'mathematical_assertions':14748,'additional_support_countercertificate':1,'full_FEI':'OPEN'},indent=2),flush=True)
