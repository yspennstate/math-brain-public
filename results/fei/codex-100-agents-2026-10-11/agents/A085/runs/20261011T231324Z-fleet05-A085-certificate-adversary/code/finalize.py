from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
sys.set_int_max_str_digits(100000)
ROOT=Path(__file__).resolve().parents[1]; AGENT=ROOT.parents[1]; OUT=ROOT/'out'
TEAM=AGENT.parent
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x): p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat(); protocol=read(PROTOCOL)
grid=read(OUT/'grid_audit.json'); finite=read(OUT/'finite_scope_audit.json'); underflow=read(OUT/'underflow_diagnostic.json')
assert grid['cases']==20736 and grid['positive']==19632 and grid['zero']==1104
assert finite['A047_cases']==20 and finite['A042_cases']==6
claims=[]; original_receipts=[]
for a in ['A071','A042','A047']:
    source=next(p for p in (TEAM/a/'runs').iterdir() if p.is_dir()); p=source/'CLAIMS.json'
    original=read(p); assert len(original)==1
    c=original[0]; orig_source=c['proof_source']
    c['proof_source']={'original_run':str(source),'original_proof_source':orig_source,'independent_review':str(ROOT/'REPORT.md'),'independent_code':str(ROOT/'code/audit.py')}
    c['review_records'].append({'reviewer':'A085/fleet05','verdict':'ACCEPT_AT_STATED_SCOPE','at_utc':now,'source':str(ROOT/'REPORT.md'),'method':{'A071':'Different centered tensor transform, positive range-reduced rational log engine, explicit raw-grid mapping and exact zero cancellation for complete 20736-case census','A042':'Independent endpoint polynomial/Taylor/zero-deficit reconstruction plus compressed-spectrum finite ratio interval containment','A047':'Independent support-mass endpoint reconstruction and full parent transform with 44-term rational interval containment for all 20 finite cases'}[a],'contributor_to_original':False,'scope_exclusions':['No all-dimensional finite-to-universal inference','No moving-basis uniform Taylor remainder inferred']})
    c['status']='INDEPENDENTLY_REVIEWED_AT_STATED_SCOPE'
    c['next_consumers']=list(dict.fromkeys(c['next_consumers']+['A090','A094','B17','B20']))
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    # Preserve and check the actual original statement/hypothesis byte content.
    orig=read(p)[0]
    for field in ['exact_statement','hypotheses','statement_sha256','version','contributors']:
        assert c[field]==orig[field]
    payload=c['exact_statement'].encode() if a=='A047' else json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()
    assert hashlib.sha256(payload).hexdigest()==c['statement_sha256']
    claims.append(c)
    original_receipts.append({'path':str(p),'sha256':sha(p),'statement_sha256':c['statement_sha256'],'preserved_original_statement':True})
    for f in source.rglob('*'):
        if f.is_file() and f.suffix in ['.py','.md','.json','.tex'] and '__pycache__' not in f.parts and f.name!='persist.py':
            original_receipts.append({'path':str(f),'sha256':sha(f),'bytes':f.stat().st_size})
save(ROOT/'CLAIMS.json',claims)
save(OUT/'reviewed_source_receipts.json',original_receipts)
failure={
    'packet_id':'A085','review_scope':'B17 lead v1 named sources A071, A042 and A047','completed_scope_verdict':True,
    'verdicts':[{'claim_id':c['claim_id'],'version':c['version'],'verdict':'HOLDS_AT_STATED_SCOPE'} for c in claims],
    'actual_registered_claim_refutations':[],
    'first_unsupported_implications':{
        'A071':'20736 finite representatives imply arbitrary real bias or dimension >=4',
        'A042':'Fixed-slice K/L or continuity of E,D implies dimension-uniform Hplus/D across simultaneous degenerate biases',
        'A047':'Fixed-child leading coefficient <=1/2 implies finite-p half-tax or uniform moving-basis remainder'},
    'support_transition_witness':{
        'total_variables':2,'typical_child':'g(Y)=2Y-1','rare_child':'h(Y)=1','data_bias':'q=P(Y=1)',
        'coefficient_when_q_not_half':'4q-4','debt_at_q_half':'0 for all selector p',
        'iterated_limit_data_after_selector':-2,'iterated_limit_selector_after_data':0,
        'refuted_extension':'Uniform O(p) remainder for the fixed-pair p log2(1/p) expansion over q near 1/2',
        'proof':'REPORT.md: continuity at fixed p and exact support coefficient'},
    'floating_pipeline_failure':underflow,
    'full_fei':'OPEN','review_of_this_review':'A090 primary; A094 alternate; pending'
}
save(ROOT/'CERTIFICATE_FAILURE.json',failure)
progress={
    'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B17','packet_id':'A085','gap_id':'FEI-B17-A085-INITIAL',
    'attempt_id':'A085-scope-audit-v1','method':'Independent exact certificate reconstruction, symmetry census, positive range-reduced log intervals, endpoint proof audit, symbolic support-transition and binary64 diagnostic',
    'mathematical_delta':'A071 finite grid@1, A042 endpoint interface@1 and A047 fixed-child endpoint@1 accepted independently at scope. All 20736 representatives resolved; 192000 raw cases covered. 18 A042 ratios and 20 A047 finite intervals certified by containment. Explicit two-variable nonuniform remainder and n=539 point-defect underflow diagnostics. Full FEI unchanged.',
    'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_CERTIFICATES_INDEPENDENTLY_ACCEPTED; UNIVERSAL_BRIDGE_OPEN',
    'claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'use':'Object of independent review, not assumed premise','statement_sha256':c['statement_sha256']} for c in claims],
    'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'A085 independent scope acceptance; original statement unchanged'} for c in claims],
    'source_artifacts':['REPORT.md','CERTIFICATE_ADVERSARY.md','CERTIFICATE_FAILURE.json','FROZEN_SPEC.json','FINITE_REFINEMENT_SPEC.json','UNDERFLOW_DIAGNOSTIC_SPEC.json','code/audit.py','code/underflow.py','out/grid_audit.json','out/coverage_audit.json','out/finite_scope_audit.json','out/underflow_diagnostic.json','out/source_receipts.json','out/reviewed_source_receipts.json'],
    'next_consumers':['A050','A057','A071','A082','A083','A084','A090','A094','A096','A098','B09','B15','B17','B20'],
    'next_action':'Audit next source-complete uniform singleton-tax/conditional-entropy stopping-tree transport from A050/A057/A096 against support-transition and terminal nonreuse obligations; A090 independently reviews this audit.',
    'stagnant_substantive_attempts':0,'blockers':['Full FEI finite-p payment and terminal-corrected tree transport remain unproved; supervisor copy/mirror and adoption unverified'],
    'packet_ids':['A085']
}
fields={f.split(' (')[0] for f in protocol['required_per_run']['progress_fields']}
assert set(progress)==fields
save(ROOT/'PROGRESS.json',progress); (ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())
(AGENT/'STATUS.md').write_text('STATE: A085 scope audit complete locally: A071 full grid and A042/A047 endpoint interfaces accepted at scope; explicit nonuniform remainder and underflow diagnostics; full FEI OPEN.\nNEXT: A090/A094 review; audit uniform singleton-tax tree transport from A050/A057/A096 with conditional entropy, terminal cost and nonreused influence.\n',encoding='utf8')
if not (AGENT/'WORKLOG.md').exists() or 'Stage A085:' not in (AGENT/'WORKLOG.md').read_text(encoding='utf8'):
    with (AGENT/'WORKLOG.md').open('a',encoding='utf8') as f:
        f.write(f'\n{now} — Stage A085: read protocol, board and B17 lead; independent full A071 grid passed 62570 checks (19632 positive, 1104 zero), raw symmetry coverage passed. Reconstructed A042/A047 endpoint proofs; final 975-check finite run certifies 18 A042 ratios and 20 A047 interval cases by containment. Initial serialization guard failure recorded and repaired locally. Proved two-variable nonuniform-remainder witness and scalar point-defect binary64 thresholds 55/56/539; 540 exact scalar diagnostic cases passed. Saved protocol files and scoped acceptance records. Full FEI OPEN; external adoption/mirror unverified.\n')
report=(ROOT/'REPORT.md').read_text(encoding='utf8')
assert all(field in report for field in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
for row in finite['A047']:
    lo,hi=map(__import__('fractions').Fraction,row['debt_bounds']); assert lo<=hi
for row in finite['A042']:
    for field in ['Hplus_D','TC_I','credit_I']:
        lo,hi=map(__import__('fractions').Fraction,row[field]); assert lo<=hi
validation={'protocol_field_sets':'PASS','compatibility_copy':'BYTE_IDENTICAL','reviewed_original_statements':'PRESERVED','all_saved_intervals':'NONEMPTY','A071_cases':grid['cases'],'A071_zero':grid['zero'],'A071_positive':grid['positive'],'A042_certified_ratios':18,'A047_certified_finite_cases':20,'scope_verdict':'COMPLETE','full_fei':'OPEN','upstream_review_records':'A085 independently accepted at scope','review_of_A085':'PENDING','external_copy_or_mirror':'UNVERIFIED','generated_at':now}
save(OUT/'validation.json',validation)
manifest=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='manifest.json' and '__pycache__' not in p.parts:
        assert p.stat().st_size<20_000_000
        manifest.append({'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size})
save(OUT/'manifest.json',manifest)
assert all(sha(ROOT/r['path'])==r['sha256'] for r in manifest)
print(json.dumps({'validation':validation,'manifest_files':len(manifest),'largest_file_bytes':max(r['bytes'] for r in manifest)},indent=2),flush=True)
