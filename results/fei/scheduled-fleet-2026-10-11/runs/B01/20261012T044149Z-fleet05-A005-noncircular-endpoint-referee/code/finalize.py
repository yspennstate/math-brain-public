from pathlib import Path
import json,hashlib,datetime,copy
ROOT=Path(__file__).resolve().parents[1]; AGENT=ROOT.parents[1]; TEAM=ROOT.parents[3]
PROTOCOL=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(PROTOCOL.read_text());fields=protocol['required_per_run']
def save(p,obj):p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def statement_hash(c):
    # These source claims hash the statement AND its hypotheses, using canonical
    # JSON; retain that exact source convention rather than bare-text hashing.
    payload={'statement':c['exact_statement'],'hypotheses':c['hypotheses']}
    return hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
leadpath=TEAM/'claude/B01/runs/20261011T225200Z/CLAIMS.json'
leadpaths=list((TEAM/'claude/B01/runs').glob('*/CLAIMS.json'))
lead=None
for p in leadpaths:
    data=json.loads(p.read_text())
    for claim in data.get('claims',[]):
        if claim['claim_id']=='B01-MINIMAL-VIOLATOR-STRUCTURE':lead=claim;leadpath=p
assert lead is not None
a002path=TEAM/'agents/A002/runs/20261011T234442Z-fleet05-A002-hardness-preserving-transformations/CLAIMS.json'
a002=next(c for c in json.loads(a002path.read_text()) if c['claim_id']=='A002-NEAR-ERASURE-MAX-CONSTANT-BRIDGE')
reviews=[]
for original,locator in [(lead,'DERIVATION.md final paragraphs; REPORT.md B01 review'),(a002,'REPORT.md A002 review')]:
    c=copy.deepcopy(original)
    assert statement_hash(c)==c['statement_sha256']
    c['review_records'].append({'reviewer':'fleet05/A005','reviewed_at_utc':stamp,'verdict':'HOLDS_AT_ORIGINAL_SCOPE',
                               'reconstruction':locator,'independence':'Exact signed physical child-slack conservation and direct packet JS; original statement unchanged; no repair supplied.',
                               'validation':'out/FULL_VALIDATION.json, 14961 exact assertions',
                               'scope_guard':'No universal near-erasure premise is proved; review is of conditional bridge/structure only.'})
    c['status']='INDEPENDENTLY_RECONSTRUCTED_AT_STATED_SCOPE'
    reviews.append(c)
statement=('For every finite uniform Boolean sign f with n relevant variables, C>=0, delta=H(f)-CI(f), '
           'sigma_i=average_s(CI(f_i,s)-H(f_i,s)), and D=H-sum B_i, the exact signed identity '
           'D+(n-1)delta+sum sigma_i=sum JS_i holds. If delta>0 and all sigma_i>=0, then n>=2 and '
           '(n-1)(H/I-C)<=2/ln2. Therefore no diverging-relevant-dimension ratio-preserving Boolean embedding '
           'of a seed of ratio R>C can have all average one-coordinate children certified at that same C. '
           'If allowances C_m vary, C_m>=R_m-(2/ln2)/(n_m-1). For disjoint tensor powers, '
           'sigma_(copy,i)(f^tensor m)=sigma_i(f)-(m-1)(H(f)-CI(f)). For the three-bit point defect at C=8/3, '
           'm=2 loses individual but retains average child certification; m>=3 loses average certification. '
           'No Boolean function with n>=11 relevant inputs and ratio at least that seed ratio has all average children certified at C=8/3.')
new={'claim_id':'A005-CHILD-CERTIFICATION-ADMISSION-OBSTRUCTION','version':1,'exact_statement':statement,
     'hypotheses':['Finite uniform independent physical cube','Boolean sign outputs','Entropy in bits','n counts relevant inputs; dummy variables deleted',
                   'Fixed C>=0; child slacks are signed','Nonadmission limit assumes n_m tends to infinity and ratio tends to R>C'],
     'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['fleet05/A005'],
     'proof_source':'DERIVATION.md equations (1)-(3); REPORT.md; out/FULL_VALIDATION.json',
     'proof_dependencies':['B01-MINIMAL-VIOLATOR-STRUCTURE@1 (independently reconstructed here)','C005 physical restriction identities and scalar JS bound (reconstructed here)'],
     'review_records':[],'status':'SOURCE_COMPLETE_SCOPED_COROLLARY_PENDING_INDEPENDENT_REVIEW','supersedes':[],
     'refutes':['Arbitrary fixed-gap seeds admit diverging-dimension ratio-preserving Boolean embeddings with all one-coordinate children certified at the same smaller constant.'],
     'first_unproved_line':None,'next_consumers':['B01','A002','A003','A027','A029','A051','A055','A064','A094','B20']}
new['statement_sha256']=statement_hash(new)
claims=reviews+[new]
progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B01','packet_id':'A005',
          'gap_id':'FEI-B01-LOW-INFLUENCE-WITNESS-TRANSFER','attempt_id':'A005-stage2-child-certification-referee',
          'method':'New dependency review via signed child-slack conservation; mechanism-independent dimension-gap obstruction; exact tensor certificates',
          'mathematical_delta':'Independently accepts B01 minimal-violator structure and A002 maximum-constant near-erasure bridge at scope. Proves no fixed-gap ratio-preserving admission to average-child-certified endpoints at diverging relevant dimension; signed slack identity and exact m=2 versus m=3 distinction; n>=11 threshold at C=8/3.',
          'deliverable_status':'COMPLETE_LOCALLY','mathematical_status':'TWO_SCOPED_REVIEWS_HOLDS; NONADMISSION_PROVED_PENDING_REVIEW; FULL_FEI_AND_GLOBAL_SAME_PARAMETER_LOCALIZATION_OPEN',
          'claim_versions_used':['B01-MINIMAL-VIOLATOR-STRUCTURE@1','A002-NEAR-ERASURE-MAX-CONSTANT-BRIDGE@1','C005 (primary interface reconstructed)'],
          'claims_created_or_changed':[c['claim_id']+'@'+str(c['version']) for c in claims],
          'source_artifacts':['REPORT.md','DERIVATION.md','out/SOURCE_MANIFEST.json','out/FROZEN_SPEC.json','out/PILOT_FAILURE.json',
                              'out/PILOT_VALIDATION.json','out/FULL_VALIDATION.json','code/check.py'],
          'next_consumers':['B01','A002','A003','A027','A029','A051','A055','A064','A094','A087','B20'],
          'next_action':'Audit or derive the signed Boolean near-erasure exclusion on actual C-violators with certified children, retaining the complete signed slack bank and terminal entropy; do not seek an impossible fixed-gap diverging-dimension admission map.',
          'stagnant_substantive_attempts':0,'blockers':['Universal near-erasure payment on certified children remains unproved.','Independent review of the new corollary and supervisor mirror/adoption pending.'],
          'packet_ids':['A005']}
for c in claims:
    assert set(c)==set(fields['claim_fields'])
    assert statement_hash(c)==c['statement_sha256']
assert set(progress)=={f.split(' (',1)[0] for f in fields['progress_fields']}
report=(ROOT/'REPORT.md').read_text()
for field in fields['report_fields']:assert '# '+field in report,field
assert report.rstrip().splitlines()[-1].startswith('Universal bridge:')
full=json.loads((ROOT/'out/FULL_VALIDATION.json').read_text());pilot=json.loads((ROOT/'out/PILOT_VALIDATION.json').read_text())
assert full['cases']==1129 and full['assertions']==14961 and full['failures']==0
assert pilot['cases']==97 and pilot['assertions']==837 and pilot['failures']==0
save(ROOT/'CLAIMS.json',claims);save(ROOT/'PROGRESS.json',progress);save(ROOT/'PACKET_DELTA.json',progress)
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
(AGENT/'STATUS.md').write_text('STATE: A005 stage2 complete: two scoped bridges independently reconstructed; child-certified fixed-gap admission impossible at growing dimension; 14961 exact checks PASS; FEI OPEN.\nNEXT: A094/A087 review; pay signed near-erasure debt on actual child-certified violators, retaining child slacks and terminal entropy; same-parameter localization remains open.\n',encoding='utf-8')
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+stamp+' A005 stage2 '+ROOT.name+': read board 04:39Z, unchanged B01 v1, own rolling status, new A002/A003/A027/A028/A030/A051/A075 dependencies and B20 synthesis. Retired encoder duplication before computation. Reconstructed B01 minimal-violator and A002 max-constant bridge via signed child-slack identity. Proved mechanism-independent n-gap obstruction; froze 97-case pilot/1129-case full exact domain. First pilot caught double-halved two-bit child H/I fixture; corrected to H=2,I=1 and sigma=C/2-1. Corrected pilot 837 checks, full14961 checks passed (14.508s), including n>=11 rational threshold and tensor m2/m3 certification distinction. Saved all artifacts locally; no shared writes or external communications.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n'+stamp+' A005 stage2 durable facts (new obstruction independently unreviewed):\n'
            '- For delta=H-CI and signed sigma_i=avg(CI-H)(actual child), DTC+(n-1)delta+sum sigma_i=sum JS_i exactly. Negative child slack is not a reserve.\n'
            '- If delta>0 and all average sigma_i>=0, relevant n>=2 and H/I-C<=2/((n-1)ln2). No fixed-gap ratio-preserving growing-dimension embedding can land in that endpoint, even with average certification. Dummy padding cannot evade relevant dimension.\n'
            '- With varying child allowance C_m, C_m>=R_m-2/((n_m-1)ln2), so it approaches at least the retained seed ratio.\n'
            '- Tensor transport is sigma_(copy,i)(f^tensor m)=sigma_i(f)-(m-1)(H-CI)(f). A positive-gap seed eventually makes all average children violate C.\n'
            '- Three-bit point defect at C=8/3: active two-bit child has H=2,I=1; sigma=1/3; delta in (1/6,1/3). m2 fails individual but retains average certification; m3 fails average. No n>=11 relevant-variable function of at least that seed ratio has all average children certified at C=8/3 (rationally certified).\n'
            '- B01-MINIMAL-VIOLATOR-STRUCTURE@1 and A002-NEAR-ERASURE-MAX-CONSTANT-BRIDGE@1 independently reconstructed HOLDS at original scopes. Near-erasure class premise and universal same-parameter localized criterion remain open.\n')
save(ROOT/'out/SCHEMA_CHECK.json',{'status':'PASS','claim_fields':'exact','progress_fields':'exact after prose packet_ids annotation normalization',
                                 'statement_hashes':'verified including unchanged reviewed versions','report_fields':'present','compatibility':'byte-identical',
                                 'status_lines':2,'claims':3,'reviews_holds':2,'new_scoped_claims_pending':1})
records=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
        b=p.read_bytes();assert len(b)<20_000_000
        records.append({'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save(ROOT/'out/ARTIFACT_RECEIPTS.json',{'saved_at_utc':stamp,'artifacts':records,'supervisor_mirror':'UNVERIFIED','new_claim_review':'PENDING'})
print(json.dumps({'status':'PASS','run_artifacts':len(records),'accepted_review_scopes':2,'new_scoped_corollaries':1,'full_fei':'OPEN'}))
