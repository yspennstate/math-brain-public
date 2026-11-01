from pathlib import Path
import hashlib,json,datetime

ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
REPORT_ROOT=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUPPLEMENT=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
TEAM=Path(r'~\brain_workers\FEI100_20261011')

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,data): (ROOT/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def claim_hash(c):
    return hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()

original=next((TEAM/'agents'/'A046'/'runs').rglob('CLAIMS.json'))
accepted=json.loads(original.read_text(encoding='utf-8-sig'))[0]
assert accepted['claim_id']=='A046-AND-ENDPOINT-TAX-NECESSITY'
assert accepted['statement_sha256']==claim_hash(accepted)
accepted['status']='ANALYTICALLY_PROVED_INDEPENDENTLY_REVIEWED'
accepted['proof_source']={'original_run':str(original.parent),'original_report_sha256':sha(original.parent/'REPORT.md'),'original_claim_file_sha256':sha(original),'audit_run':ROOT.name,'audit_report':'REPORT.md'}
accepted['review_records']=[{'reviewer':'fleet05/A092','verdict':'ACCEPT_AT_STATED_SCOPE','method':'Independent analytic reconstruction, recursive centered transform, conditional-law channel calculation, different rational logarithm series','source':'REPORT.md; code/reproduce.py; out/REPRODUCTION.json','repair_supplied_to_this_version':False}]
new={
    'claim_id':'A092-AND-EXPLICIT-ENDPOINT-LOWER-BOUND','version':1,
    'exact_statement':'For the actual Boolean sign f(x,y)=(-1)^(xy) with independent P(X=1)=p in (0,1/2] and P(Y=1)=1/4, and physical reveal A={X}, E=J_A-M_A >= p*(log2(1/p)/2-7). Consequently for every finite K>=0 and every integer k>2K+14, the choice p=2^(-k) gives E>Kp. This refutes universal singleton taxes bounded above by Kp; it does not refute B09 Delta, prove the sharp tax, or disprove uniform FEI.',
    'hypotheses':['actual two-bit AND truth table','independent interior product biases','orthonormal biased Fourier basis including empty coefficient','M_A=H(S_X|S_Y), J_A=I(X;S_Y) in the actual physical-child spectral experiment','Shannon entropy in bits'],
    'statement_sha256':'','contributors':['fleet05/A092'],
    'proof_source':{'run_id':ROOT.name,'path':'REPORT.md','locator':'complete derivation: explicit contributed bound','finite_calibration':'out/REPRODUCTION.json'},
    'proof_dependencies':[], 'review_records':[],
    'status':'ANALYTICALLY_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
    'refutes':['universal J_A<=M_A+Kp for a fixed finite K under all interior product biases'],
    'first_unproved_line':None,'next_consumers':['A047','A048','A087','A085','B09','B12','B13','B20']}
new['statement_sha256']=claim_hash(new)
save('CLAIMS.json',[accepted,new])
progress={
    'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B19','packet_id':'A092','gap_id':'G-BIASED-TAX','attempt_id':'A092-20261011-endpoint-review-1',
    'method':'Independent Boolean truth-table reconstruction, analytic asymptotic review, rational log sign certification and explicit endpoint bound',
    'mathematical_delta':'Accepted A046 endpoint necessity unchanged; independently certified four AND violations and one A071 calibration; contributed E>=p*(log2(1/p)/2-7). Full FEI OPEN.',
    'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'A046_REVIEW_ACCEPTED; A092_EXPLICIT_BOUND_PENDING_INDEPENDENT_REVIEW; FULL_FEI_OPEN',
    'claim_versions_used':['A046-AND-ENDPOINT-TAX-NECESSITY@1 (review target)','A071-B09-THREEBIT-GRID-CERTIFICATE@1 (one calibration only, not assumed)'],
    'claims_created_or_changed':['A046-AND-ENDPOINT-TAX-NECESSITY@1 review record','A092-AND-EXPLICIT-ENDPOINT-LOWER-BOUND@1'],
    'source_artifacts':['REPORT.md','CLAIMS.json','SEARCH_SPEC.json','code/reproduce.py','code/finalize.py','out/REPRODUCTION.json','out/SOURCE_MANIFEST.json'],
    'next_consumers':['A047','A048','A071','A087','A085','B09','B12','B13','B20'],
    'next_action':'Audit the next source-complete Boolean counterexample to a newly versioned coefficient-1/2 tax, retaining actual truth tables and rigorous sign.',
    'stagnant_substantive_attempts':0,'blockers':['B19 STREAM_NOTES.md absent; independent review proceeded. Remote copy and mirror unverified.'],
    'packet_ids':['A092']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
sources=[REPORT_ROOT/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
sources+=[SUPPLEMENT/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
sources+=list((SUPPLEMENT/'sources').glob('*.md'))+list((TEAM/'context').glob('*.txt'))+[TEAM/'BOARD.md']
sources+=list((REPORT_ROOT/'runs').rglob('REPORT.md'))
for a in ['A046','A071']:
    for p in (TEAM/'agents'/a/'runs').rglob('*'):
        if p.is_file() and p.name in ['REPORT.md','CLAIMS.json','exact_check.py']:sources.append(p)
save('out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'scope':'Consulted local source; context manuscript full proofs not independently audited'} for p in sources])
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A092 stage complete locally: A046 endpoint-tax no-go independently accepted; explicit bound contributed; full FEI OPEN.\nNEXT: Audit a new coefficient-1/2-tax Boolean counterexample; A087/A085 review the explicit corollary; A071 full-grid acceptance remains pending.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} | {ROOT.name}: Read protocol and board; B19 notes absent. Independently rebuilt AND spectra and physical channel; four rigorous excess signs and A071 minimum calibration passed. Accepted A046 unchanged; proved explicit all-p lower bound with constant 7, pending independent review. Saved all protocol artifacts; full FEI OPEN. Initial context UTF-8 decode failed; cp1252 fallback used.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nA046-AND-ENDPOINT-TAX-NECESSITY@1 independently accepted: for fixed q in (0,1/2), E=4q(1-2q)p log2(1/p)+O_q(p), maximal AND leading coefficient 1/2 at q=1/4. A092 contributed E>=p(log2(1/p)/2-7) for q=1/4 and 0<p<=1/2; integer k>2K+14 gives explicit witness against Kp. Scope is a biased singleton restriction helper, not uniform FEI. Uniform AND and its disjoint tensors have ratio exactly 2. Independent log certificates can use positive -ln(1-t) series after reducing to [1/2,1]; this avoids signed interval division. A071 minimum-positive case reproduced; full finite grid not independently accepted.\n')
protocol=json.loads((REPORT_ROOT/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
for c in [accepted,new]:
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    assert c['statement_sha256']==claim_hash(c)
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
report=(ROOT/'REPORT.md').read_text()
for field in protocol['required_per_run']['report_fields']:assert '# '+field in report
assert report.strip().splitlines()[-1].startswith('Universal bridge:')
result=json.loads((ROOT/'out'/'REPRODUCTION.json').read_text())
assert result['status']=='PASS' and result['runtime_seconds']<60
for p in ROOT.rglob('*'):
    if p.is_file():assert p.stat().st_size<20_000_000
save('out/VALIDATION.json',{'status':'PASS','at_utc':now,'schema_keys_exact':True,'statement_hashes_valid':True,'progress_copies_identical':True,'all_required_report_fields':True,'all_files_under_20MB':True,'reproduction_status':result['status'],'runtime_seconds':result['runtime_seconds'],'mirror_status':'UNVERIFIED','A071_full_grid_review':'NOT_COMPLETED'})
save('out/ARTIFACT_RECEIPTS.json',[{'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size} for p in ROOT.rglob('*') if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json'])
print(json.dumps({'status':'PASS','claim_count':2,'locally_saved':str(ROOT),'runtime_seconds':result['runtime_seconds']}))
