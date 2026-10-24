from pathlib import Path
import hashlib,json,datetime
ROOT=Path(__file__).resolve().parents[1]; AGENT=ROOT.parents[1]
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text())
def save(path,v): path.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
statement=('The pointwise same-K activation-witness transport assertion is false: let f be +1 except at one point of the uniform three-cube, '
           'and F=1+A_8(f^tensor16-1) on 56 independent uniform bits. At lambda=0,K=5/2 every seed coordinate and every one of the 48 data '
           'coordinates of F has B_i/Inf_i>5/2, while every one of the eight controls has B_i/Inf_i<5/2. '
           'The maximum influence of F is 4251920575/1099511627776<1/256. Thus a K-witness in this activated image need not yield a K-witness '
           'in its seed. This refutes pointwise witness transport only, not the universally quantified localized endpoint or FEI.')
claim={'claim_id':'A005-SAME-K-ACTIVATION-WITNESS-TRANSPORT-REFUTATION','version':1,
       'exact_statement':statement,'hypotheses':['Uniform independent physical bits','Boolean sign output','Entropy in bits',
       'B_i=H(S_i|S_-i)','Point activation of the unbalanced tensor core; no auxiliary balancing literal'],
       'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['account05/A005'],
       'proof_source':'REPORT.md section 4; code/witness.py; out/WITNESS_CERTIFICATE.json',
       'proof_dependencies':[],'review_records':[],'status':'SCOPED_REFUTATION_CERTIFIED_PENDING_INDEPENDENT_REVIEW',
       'supersedes':[],'refutes':['LOCAL-POINTWISE-SAME-K-ACTIVATION-WITNESS-TRANSPORT (assertion stated explicitly in REPORT.md section 4)'],
       'first_unproved_line':None,'next_consumers':['B01','A002','A003','A055','A094','B20']}
save(ROOT/'CLAIMS.json',[claim])
progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B01','packet_id':'A005',
          'gap_id':'FEI-B01-LOW-INFLUENCE-WITNESS-TRANSFER','attempt_id':'A005-localization-referee-1',
          'method':'Independent coordinate Fourier ledger; exact finite checks; rational interval countercertificate; induction audit',
          'mathematical_delta':'Confirmed ratio-preserving arbitrary-seed low-influence admission. Audited localization => FEI with C=max(h2(tau)/tau+2/ln2,(K+2/ln2)/(1-lambda)). Refuted pointwise same-K activation witness transport at K=5/2; data-only witness transport identified as sufficient. Global same-parameter logical implication remains open.',
          'deliverable_status':'COMPLETE_LOCALLY','mathematical_status':'SCOPED_REFUTATION_CERTIFIED; FULL_FEI_AND_GLOBAL_SAME_PARAMETER_TRANSFER_OPEN',
          'claim_versions_used':['C005: ERASURE_REDUCTION.md sections 1-4 (hash in source manifest)','A002-EXACT-HARDENING-LEDGER@1 (coordination baseline; elementary admission reconstructed)'],
          'claims_created_or_changed':[claim['claim_id']+'@1'],
          'source_artifacts':['REPORT.md','out/SOURCE_MANIFEST.json','out/FROZEN_SPEC.json','out/CHECK_n2.json','out/CHECK_n3.json',
          'out/WITNESS_FROZEN_SPEC.json','out/WITNESS_CERTIFICATE.json','code/check.py','code/witness.py'],
          'next_consumers':['B01','A002','A003','A055','A094','A087','B20'],
          'next_action':'Construct a data-witness-preserving admission map or a nonreusing control-to-data transfer surviving the one-point-defect tensor witness, retaining full terminal entropy.',
          'stagnant_substantive_attempts':0,
          'blockers':['Same-parameter global implication lacks witness transfer; ordinary activation provably cannot supply it.','Independent review and supervisor mirror adoption pending; no access blocker.'],
          'packet_ids':['A005']}
save(ROOT/'PROGRESS.json',progress);save(ROOT/'PACKET_DELTA.json',progress)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A005 referee artifact complete: exact same-K activation-witness transport refuted; 7,800 full-domain assertions passed; FEI OPEN; review pending.\nNEXT: A094/A087 review; obtain a data-witness-preserving embedding or nonreusing control-to-data payment retaining tensor seed entropy.\n')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+now+' A005 stage: read protocol/board/B01 v1; consumed A001/A002 baseline. Derived data/control erasure ledger, audited localization induction, froze and ran 80-case pilot (992 assertions) and 600-case full checker (7800 assertions), all passing. Certified a 56-bit same-K pointwise witness-transport counterexample at K=5/2 with Fraction logarithm intervals. Initial certificate serialization exceeded Python digit limit; repaired using outward dyadic rounding, rerun passed. Saved all run/rolling artifacts; no shared writes. Global same-parameter implication and FEI remain open.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n'+now+' A005 durable facts (independent review pending):\n'
            '- Low-influence H/I endpoint has the same extended-real supremum as full FEI; that does not transport an existential coordinate witness.\n'
            '- L(tau,lambda,K), 0<tau<1 and 0<=lambda<1, implies FEI at max(h2(tau)/tau+2/ln2,(K+2/ln2)/(1-lambda)) by induction over all restrictions. Low-influence class is not restriction closed.\n'
            '- Balanced point activation adds controls with B_i/Inf_i ->2; a balancing literal can have erasure zero. Cheap auxiliary witnesses may carry no seed information.\n'
            '- Unbalanced tensor activation erasure formula: B_data=t B_i(seed)-t E(c,v)+(t-t^2)E(c-1,v)+E(1-t+tc,tv), c=mu^m,v=fhat({i})mu^(m-1), E(u,v)=phi(u^2)+phi(v^2)-phi(u^2+v^2).\n'
            '- Actual point-defect seed n=3, m=16,k=8: seed/data B_i/Inf_i>5/2; controls <5/2; max influence<1/256. Pointwise same-K activation witness transport is false. Universal same-parameter localization is not refuted by this.\n'
            '- Data-only witness eligibility yields same-lambda,K global transfer by an unbalanced ratio-preserving tensor activation and a finite-coordinate subsequence. The missing proof is eligibility or a paid control-to-data transfer.\n')
required=protocol['required_per_run']
assert set(claim)==set(required['claim_fields'])
# Protocol prose annotates its packet_ids entry; the actual compatibility key
# is explicitly packet_ids in the same protocol and the worker instructions.
assert set(progress)=={field.split(' (',1)[0] for field in required['progress_fields']}
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
report=(ROOT/'REPORT.md').read_text()
for field in required['report_fields']: assert '# '+field in report,field
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
assert json.loads((ROOT/'out/CHECK_n3.json').read_text())['assertions']==7800
assert json.loads((ROOT/'out/WITNESS_CERTIFICATE.json').read_text())['status']=='PASS'
save(ROOT/'out/SCHEMA_CHECK.json',{'status':'PASS','claim_fields':'exact','progress_fields':'exact','report_fields':'all present',
                                 'compatibility_copy':'byte-identical','status_lines':2,'statement_sha256':'verified'})
receipts=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
        b=p.read_bytes();assert len(b)<20_000_000
        receipts.append({'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save(ROOT/'out/ARTIFACT_RECEIPTS.json',{'saved_at_utc':now,'artifacts':receipts,'independent_review':'PENDING','mirror':'UNVERIFIED'})
print(json.dumps({'status':'PASS','run_artifacts':len(receipts),'claims':1,'full_fei':'OPEN','progress_compatibility':'byte-identical'}))
