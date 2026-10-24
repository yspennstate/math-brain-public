import json,hashlib,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
REPORTS=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
CONTEXT=Path(r'~\brain_workers\FEI100_20261011\context')
protocol=json.loads((REPORTS/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
def sha(b):return hashlib.sha256(b).hexdigest()
def write(path,data):path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
sources=[REPORTS/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex']]
sources += list((REPORTS/'runs').rglob('REPORT.md'))
sources += [SUP/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
sources += list((SUP/'sources').glob('*.md'))+list(CONTEXT.glob('*.txt'))
sources += [AGENT.parents[1]/'BOARD.md']
a026=AGENT.parent/'A026'/'runs'/'20261011T214052Z-account05-A026-good-coordinate-erasure'
sources += [a026/'REPORT.md',a026/'GOOD_COORDINATE_TARGET.tex',a026/'CLAIMS.json']
receipts=[]
for p in sources:
    b=p.read_bytes();receipts.append({'path':str(p),'bytes':len(b),'sha256':sha(b)})
write(ROOT/'out'/'source_receipts.json',receipts)
cert=json.loads((ROOT/'FINITE_INEQUALITY_CERTIFICATE.json').read_text())
for r in cert['results']:
    if 'assertions' in r:r['exact_checks']=r.pop('assertions')
cert.update({'domain_exhaustiveness':'All truth tables modulo output negation; no input, character, or affine symmetry reduction.',
 'total_representatives':32906,'total_nonconstant':32902,'units':'bits for entropy, uniform physical influence',
 'comparison':'Factor 2*N^2*B_i-2*Kstar*D_i into integer prime log coefficients c_p and compare positive and negative integer products.',
 'certificate_files':[f'out/selection_n{n}.bin' for n in range(1,5)],
 'rational_bound_lhs':str(2**53*5**100),'rational_bound_rhs':str(3**180),
 'separate_bridge':'EXHAUSTIVENESS_LEMMA.tex, Theorem 2',
 'independent_reproduction':'out/independent_reproduction.json; distinct implementation by same author, external review pending'})
write(ROOT/'FINITE_INEQUALITY_CERTIFICATE.json',cert)
ind=json.loads((ROOT/'out'/'independent_reproduction.json').read_text());assert cert['status']==ind['status']=='PASS'
for a,b in zip(cert['results'],ind['results']):assert a['selection_sha256']==b['selection_sha256']
partial=json.loads((ROOT/'out'/'exact_partial.json').read_text())
for r in partial:
    if 'assertions' in r:r['exact_checks']=r.pop('assertions')
write(ROOT/'out'/'exact_partial.json',partial)
statements=[
 ('A082-FINITE-TRUE-ERASURE', 'For every nonconstant Boolean sign f on at most four uniform physical variables there exists a relevant i with H(S_i|S_-i)<=Kstar Inf_i(f), where Kstar=4+(5/2)log2(5)-(9/2)log2(3)<107/40. Kstar is optimal over this domain.', ['Boolean sign truth table','uniform cube','at most four physical variables','entropy in bits']),
 ('A082-AFFINE4-ERASURE-BRIDGE', 'For every finite physical dimension, every nonconstant Boolean sign with nonzero Fourier support contained in c+V with dim_F2(V)<=4, and every disjoint product of such factors, has a relevant i with B_i<=Kstar I_i at every physical restriction, and H(f)<=(Kstar+2/ln(2))I(f).', ['Boolean sign','uniform finite physical cube','affine Fourier support dimension at most four per disjoint factor','entropy in bits'])]
claims=[]
consumers=['A026','A027','A028','A061','A073','A075','A083','A084','A085','A090','A094','B20']
for idx,(cid,s,h) in enumerate(statements):
    item={'claim_id':cid,'version':1,'exact_statement':s,'hypotheses':h,
      'statement_sha256':sha(json.dumps({'statement':s,'hypotheses':h},sort_keys=True,separators=(',',':')).encode()),
      'contributors':['A082'] if idx==0 else ['A082','A026 (source of affine-support reduction; reconstructed here)'],
      'proof_source':str(ROOT/'EXHAUSTIVENESS_LEMMA.tex')+f', Theorem {idx+1}; '+str(ROOT/'FINITE_INEQUALITY_CERTIFICATE.json'),
      'proof_dependencies':[] if idx==0 else [{'claim_id':statements[0][0],'version':1}],
      'review_records':[],'status':'PROVED_LOCAL_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
      'first_unproved_line':None,'next_consumers':consumers}
    assert set(item)==set(protocol['required_per_run']['claim_fields']);claims.append(item)
write(ROOT/'CLAIMS.json',claims)
progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B17','packet_id':'A082',
 'gap_id':'G-R-SELECT','attempt_id':'A082-TRUE-ERASURE-01','method':'exhaustive integer-product sharp certificate with separate hereditary affine-support bridge',
 'mathematical_delta':'Selectable true-erasure constant through four variables is exactly Kstar=2.672488983973..., improving A026 amplitude-derived 7/2 by 7/2-Kstar; hereditary affine4/disjoint-product FEI constant improves to Kstar+2/ln2. No aggregate B<=Kstar I claim or universal selection claim.',
 'deliverable_status':'COMPLETE_LOCAL_SAVED_REVIEW_PENDING','mathematical_status':'FINITE_TARGET_PROVED_STRUCTURAL_BRIDGE_PROVED_FULL_FEI_OPEN',
 'claim_versions_used':[{'source':'ERASURE_REDUCTION.md','scope':'Sections 1,2,4 identities rederived in Theorem 2'},{'source':str(a026/'GOOD_COORDINATE_TARGET.tex'),'scope':'affine projection and independent product proof reconstructed; 7/2 finite premise replaced'}],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':1} for c in claims],
 'source_artifacts':['REPORT.md','EXHAUSTIVENESS_LEMMA.tex','FINITE_INEQUALITY_CERTIFICATE.json','code/certify.py','code/reproduce.py','out/independent_reproduction.json','out/source_receipts.json'],
 'next_consumers':consumers,'next_action':'A090/A094 independently reconstruct and A026/A028 consume the sharp leaf certificate; next mathematical work must address bounded-cost stopping transport to these leaves, rather than enlarge a truth-table search.',
 'stagnant_substantive_attempts':0,'blockers':['No universal bounded-cost stopping reduction to affine4 leaves is proved. B17 lead notes absent at supplied path. External independent review not yet performed.'],
 'packet_ids':['A082']}
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
write(ROOT/'PROGRESS.json',progress);write(ROOT/'PACKET_DELTA.json',progress)
status='STATE: A082 certificate complete locally: sharp selectable true erasure Kstar<107/40 through n=4; hereditary affine4/product bridge proved; review pending; full FEI OPEN.\nNEXT: A090/A094 audit and A026/A028 consume sharp leaf payment; seek bounded-cost stopping transport to affine4 leaves, not a larger finite census.\n'
(AGENT/'STATUS.md').write_text(status,encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now}: Read protocol/board and current sources; B17 notes absent. Replaced A026 amplitude proxy by exact true-erasure extremum Kstar. Gray/integer products passed 32906 representatives in {cert["elapsed_seconds"]:.6f}s; independent butterfly/physical-boundary/rational-log replay passed in {ind["elapsed_seconds"]:.6f}s. Saved two claims and structural exhaustiveness theorem; full FEI remains open.\n')
(AGENT/'LEARNED.md').write_text('The exact maximum of min_{i:I_i>0} B_i/I_i over Boolean functions on at most four physical variables is Kstar=4+(5/2)log2(5)-(9/2)log2(3), strictly below 107/40. A three-variable point defect attains it at every relevant coordinate. Integer-product comparisons avoid signed interval-division risks; independent replay uses outward 2^-100 logarithm intervals.\nAffine support c+V of dimension<=4 admits either a relevant e_i outside V (B_i=JS_i=0) or at most four relevant physical coordinates. Projection under restriction preserves affine dimension; disjoint products preserve factor erasure/influence. This yields hereditary selection and H<=(Kstar+2/ln2)I for that class. Arbitrary linear Fourier coordinate changes do not preserve physical influence.\nSelected-coordinate equality does not imply extremality: the independent replay has 480 selected equalities in n=4, while only 32 tables have minimum ratio exactly Kstar. Existential selection does not assert aggregate B<=Kstar I or all-coordinate payment.\n',encoding='utf-8')
# Manifest is written last and intentionally excludes its own hash.
manifest=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='persistence_receipts.json':
        b=p.read_bytes();assert len(b)<20*1024*1024
        manifest.append({'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':sha(b)})
write(ROOT/'out'/'persistence_receipts.json',{'saved_at':now,'files':manifest,'regeneration_commands':['python -X utf8 code/discover.py --pilot','python -X utf8 code/discover.py','python -X utf8 code/certify.py','python -X utf8 code/reproduce.py','python -X utf8 code/save_stage.py'],'command_workdir':str(ROOT),'external_review':'pending','mirror_copy':'not observed'})
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert field in report
print(json.dumps({'status':'PERSISTED','claim_schema':'PASS','progress_schema':'PASS','report_fields':'PASS','packet_delta_identical':True,'manifest_files':len(manifest),'run':str(ROOT)},indent=2))
