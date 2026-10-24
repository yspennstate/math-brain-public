from pathlib import Path
import hashlib,json,datetime
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
BASE=Path('~/mop_fei100/reports/fei-2026-10-11')
PROTO=json.loads((BASE/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
def dump(path,obj): path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
check=json.loads((ROOT/'out/CHECK.json').read_text(encoding='utf-8'))
assert check['status']=='PASS' and sum(check['counts'].values())==1962
assert check['runtime_seconds']<60
registry=json.loads((BASE/'CLAIM_REGISTRY.json').read_text(encoding='utf-8-sig'))
original=next(c for c in registry['claims'] if c['claim_id']=='B09-BIASED-BLOCK-UNCERTAINTY')
keys=PROTO['required_per_run']['claim_fields']
claim={k:original.get(k,[]) for k in keys}
claim['contributors']=original.get('contributors',['account01/B09 original candidate'])
claim['review_records']=original['review_records']+[{
 'reviewer':'A048','verdict':'PARTIAL_SCOPE_RECONSTRUCTION_ONLY',
 'method':'Independent actual truth tables, rational biased coefficients, symbolic prime-log entropy identities and analytic product channels; aligned tensor component accepted, shared-selector scope narrowed; Maassen-Uffink step not reviewed.',
 'source':'REPORT.md; TENSOR_POTENTIAL_LEDGER.tex; out/CHECK.json',
 'scope':'Existing candidate version unchanged; no full theorem acceptance; no third broad candidate opened.'}]
claim['status']=original['status']
canonical=json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()
assert hashlib.sha256(canonical).hexdigest()==claim['statement_sha256']
assert set(claim)==set(keys)
dump(ROOT/'CLAIMS.json',[claim])
progress={
 'protocol_revision':PROTO['revision'],'run_id':ROOT.name,'stream':'B10','packet_id':'A048',
 'gap_id':'G-BIASED-TAX','attempt_id':'A048-tensor-scope-1',
 'method':'Verification and scope repair of existing B09 candidate; exact channel tensorization and arbitrary-mean activation ledger.',
 'mathematical_delta':'Aligned tensor ledgers add; unrevealed factor hides arbitrary terminal entropy; biased dummies invalidate payment of unreduced P; general-mean point-control decrement L<=8I_A (strict if I_A>0) with explicit uniform logarithmic remainder; shared selector uses mean mu^t rather than t-fold selector charge.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT',
 'mathematical_status':'EXISTING_CANDIDATE_SCOPE_VERIFIED; UNIVERSAL_PAYMENT_AND_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'B09-BIASED-BLOCK-UNCERTAINTY','version':1,'role':'target only; upper inequality not assumed'}],
 'claims_created_or_changed':[{'claim_id':'B09-BIASED-BLOCK-UNCERTAINTY','version':1,'change':'partial tensor/channel scope review only; statement and pending status unchanged'}],
 'source_artifacts':['REPORT.md','TENSOR_POTENTIAL_LEDGER.tex','TENSOR_GUARDS.md','FROZEN_SPEC.json','code/check.py','out/CHECK.json','out/SOURCE_MANIFEST.json'],
 'next_consumers':['A040','A049','A050','A064','A092','A087','B20'],
 'next_action':'Construct an essential-coordinate factor-aware stopping-tree ledger retaining explicit terminal entropy, then test its nonreuse claim on the accepted sparse-bent point-surgery tree.',
 'stagnant_substantive_attempts':0,
 'blockers':['Specified B10 STREAM_NOTES.md absent; no mathematical work blocked.','Independent review and supervisor mirroring unverified.'],
 'packet_ids':['A048']}
assert set(progress)==set(k.split(' (')[0] for k in PROTO['required_per_run']['progress_fields'])
dump(ROOT/'PROGRESS.json',progress); dump(ROOT/'PACKET_DELTA.json',progress)
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
for field in PROTO['required_per_run']['report_fields']:
    assert '# '+field in (ROOT/'REPORT.md').read_text(encoding='utf-8'),field
sources=[]
for name in ('EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex'):
    sources.append((BASE/name,'Protocol in full; other files state/dispatch/candidate and A048 contract inspection'))
for p in (BASE/'runs').rglob('REPORT.md'): sources.append((p,'Earlier source reports: scope inspection; not full independent review'))
SUP=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
for name in ('CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md'):
    sources.append((SUP/name,'Supplement consulted for scope and existing controls'))
for name in ('BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','ERASURE_REDUCTION.md','ROUTE_MAP_CURATED.md','OVERLAPPING_PRODUCT_NOTE.md','LOG_ALLOCATION_CURATED.md'):
    sources.append((SUP/'sources'/name,'Relevant tensor/channel and normalization passages; no unbundled original assumed'))
TEAM=Path('~/brain_workers/FEI100_20261011')
sources.append((TEAM/'BOARD.md','Start-stage snapshot; do not repeat existing results'))
for agent in ('A046','A047','A021','A036'):
    for p in (TEAM/'agents'/agent/'runs').rglob('REPORT.md'): sources.append((p,'Relevant source-bound tensor/activation/normalization component inspection'))
for p in (TEAM/'context').glob('*.txt'): sources.append((p,'Selected passages stated in REPORT; not full independent proof audit'))
dump(ROOT/'out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'scope':scope} for p,scope in sources])
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A048 tensor-scope packet complete locally; 1,962 exact cases PASS; B09 tensor component verified, universal payment and full FEI OPEN.\nNEXT: A092/A087 review; A050/A064 build essential-coordinate factor-aware tree ledger retaining terminal entropy and test nonreuse on sparse-bent surgery.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'{stamp}: Corrected biased branch convention; final frozen verification PASS, {check["assertions"]} assertions, {check["runtime_seconds"]:.4f}s arithmetic. Saved existing-candidate partial review, general-mean activation ledger, dummy-tax and terminal-factor guards; no third broad candidate opened.\n')
lesson='For F=1+A_k(g-1) with a fair k-control point indicator, p=2^-k and m=E g, I_A=kp(1-m), L=H(F)-pH(g)<=8I_A (strict if I_A>0). Uniformly |L-4pk(1-m)|<=17p+8kp^2. The exact local M,J depend only on core mean, not its entropy. A shared biased selector replaces m by mu^t; it does not replicate the selector ledger t times. The terminal pH(g) remains arbitrary.\n'
learned=(AGENT/'LEARNED.md').read_text(encoding='utf-8')
learned=learned.replace('L=H(F)-pH(g)<8I_A.','L=H(F)-pH(g)<=8I_A (strict if I_A>0).')
if lesson not in learned: learned+=lesson
(AGENT/'LEARNED.md').write_text(learned,encoding='utf-8')
receipts=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.name not in ('RECEIPTS.json','VALIDATION.json'):
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
dump(ROOT/'out/RECEIPTS.json',receipts)
dump(ROOT/'out/VALIDATION.json',{'status':'PASS','at_utc':stamp,'protocol_fields_exact':True,'claim_statement_hash_exact':True,'progress_copies_identical':True,'files_under_20MB':True,'checked_cases':1962,'assertions':check['assertions'],'candidate_cap':'No new broad candidate; existing B09 partial scope review only','independent_review':'UNVERIFIED','mirror':'UNVERIFIED'})
print(json.dumps({'status':'PASS','receipts':len(receipts),'cases':1962,'assertions':check['assertions']}))
