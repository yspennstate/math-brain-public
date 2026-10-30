from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
def write(name,data):
    (ROOT/name).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
v=json.loads((ROOT/'out/validation.json').read_text())
assert v['failures']==0 and v['cases']==3
script=(ROOT/'code/reproduce.py').read_text()
standalone=script.replace('ROOT=Path(__file__).resolve().parents[1]','ROOT=Path(__file__).resolve().parent')
(ROOT/'INDEPENDENT_REPRODUCTION.py').write_text(standalone,encoding='utf-8')
assert standalone.replace('ROOT=Path(__file__).resolve().parent','ROOT=Path(__file__).resolve().parents[1]')==script
write('REPRODUCTION_REPORT.json',{**v,'review_scope':'Three selected records only; full grid and FEI remain open','method':'Binary Moebius polynomial, direct conditional/channel entropy, positive log series','first_discrepancy':None})
src=Path('~/brain_workers/FEI100_20261011/agents/A073/runs/20261011T222436Z-fleet05-A073-certified-logarithms/CLAIMS.json')
claims=json.loads(src.read_text())
for c in claims:
    payload=json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()
    assert hashlib.sha256(payload).hexdigest()==c['statement_sha256']
    c['review_records'].append({'reviewer':'fleet05/A074','at':stamp,'verdict':'SELECTED_RECORDS_CONFIRMED_ONLY_FULL_GRID_REVIEW_PENDING' if c['claim_id'].startswith('A071') else 'ACCEPT_AT_STATED_SCOPE','scope':'Selected minimum_positive and exact_zero only; no minimum or coverage acceptance' if c['claim_id'].startswith('A071') else 'Fixed Boolean AND, p=(1/8,1/4), A={0}, J-M>1195/10000 bits','method':'Independent subset Moebius reconstruction, direct entropy of conditional/channel law, positive Taylor rational enclosure; no original code used','source':str(ROOT/'REPORT.md')})
write('CLAIMS.json',claims)
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B15','packet_id':'A074','gap_id':'G-R-SELECT','attempt_id':'A074-INDEPENDENT-REPRODUCTION-1','method':'Three-record independent Moebius/conditional-channel/Taylor reconstruction',
 'mathematical_delta':'232 exact checks reconcile all selected rational quantities; D in (0.00256647,0.00256648), exact D=0, AND J-M in (0.11954501,0.11954502). No universal payment advanced.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SELECTED_RECORDS_INDEPENDENTLY_REPRODUCED_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'use':'comparison target only'} for c in claims],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'scope-limited independent review appended; statement unchanged'} for c in claims],
 'source_artifacts':['REPORT.md','INDEPENDENT_REPRODUCTION.py','REPRODUCTION_REPORT.json','FROZEN_SPEC.json','out/validation.json','out/source_receipts.json'],
 'next_consumers':['A085','A092','A073','A075','B09','B20'],
 'next_action':'Consume a versioned singleton-tax transport candidate from A050/A057 or B09 and retain conditional M, bias tax and terminal entropy under nonreusing influence.',
 'stagnant_substantive_attempts':0,'blockers':['B15 lead notes absent at stage start; useful work completed via board handoffs','Universal stopping-tree influence payment remains unproved; not an artifact blocker'], 'packet_ids':['A074']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text())
req=protocol['required_per_run']
pf={x.split(' (')[0] for x in req['progress_fields']}
assert set(progress)==pf
for c in claims:assert set(c)==set(req['claim_fields'])
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
(AGENT/'STATUS.md').write_text('STATE: A074 packet complete locally: three selected witnesses independently reproduced, 232 exact checks PASS; full grid review pending; full FEI OPEN.\nNEXT: A085/A092 audit reconstruction; consume versioned A050/A057 or B09 singleton-tax transport candidate with conditional M and terminal entropy retained.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp}: Read protocol/board/context, B15 lead absent. Implemented independent binary Moebius spectrum and direct M/J with 40-term rational positive log series. Three witnesses reconciled, 232 assertions PASS, 0.0189664s. Initial missing out directory and legacy source encoding fixed. Saved protocol artifacts and selected reviews; no full-grid or FEI acceptance.\n')
(AGENT/'LEARNED.md').write_text('Binary multilinear Moebius coefficients yield b_S=sum_(T superset S)c_T product_(T\\S)p_i, mu_S=b_S² product_(S)p_i(1-p_i). This differs from Walsh conversion and direct centered moments.\nDirect M=-sum mu log(mu/q), J=sum w child_mu log(child_mu/q) retain separate spectral and physical selector laws.\nln(x)=sum (1-1/x)^k/k on [1,2], with remainder <=t^(N+1)/((N+1)(1-t)), gives exact rational bounds after dyadic reduction.\nSelected minimum record: 0.00256647<M-J<0.00256648. Equality record: deterministic spectral selector and identical child laws give M=J=0. Biased AND: 0.11954501<J-M<0.11954502. No grid minimum or universal FEI result follows.\n',encoding='utf-8')
manifest=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.name!='manifest.json':
        b=p.read_bytes();assert len(b)<20*1024*1024
        manifest.append({'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
write('out/manifest.json',manifest)
print(json.dumps({'artifact_count':len(manifest),'schema_checks':'PASS','selected_records':3,'assertions':v['exact_checks'],'largest_bytes':max(x['bytes'] for x in manifest)},indent=2))
