from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
SHARED=Path('~/brain_workers/FEI100_20261011')
PROTOCOL=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8'))
statement=(
'For g(X,Y)=(-1)^(XY) under independent Bernoulli(p), Bernoulli(q), 0<p,q<1, with A={X}, the complete strict-sign regions and zero set of F=J_A-M_A are those in PROOF.md, as follows. '
'Put psi(x)=h2(sin^2 x), theta=arcsin(sqrt(p)), alpha=atan(sqrt(p/(1-p))*(1-2q)), w=1-4pq(1-q). Then F=w[psi(theta)-psi(alpha)-psi(theta-alpha)]. '
'There is a unique s_* in (0,pi/4) with 2psi(s_*/2)=psi(s_*); p_*=sin^2(s_*) lies strictly between 7634531/20971520 and 152690623/419430400. '
'For G_s(x)=psi(x)+psi(s-x)-psi(s), 0<x<s<pi/2: if s>=pi/4, G_s>0; if s<s_*, G_s<0; if s=s_*, G_s<0 except G_s(s/2)=0; if s_*<s<pi/4, it has exactly two simple zeros a(s),s-a(s), with 0<a(s)<s/2, is positive between them, and negative outside. '
'For q<1/2, F=-w G_theta(alpha). For q>1/2,p<=1/2, F<0. For q>1/2,p>1/2, let q0=1/(2p), s=pi/2-theta, b=-alpha: F=-w G_s(b) for q<q0, F=0 at q=q0, and F<0 for q>q0. Also F(p,1/2)=0. '
'The numbers of distinct interior q zeros are respectively 1,2,3,1,4,3,2 on p in (0,p_*), {p_*}, (p_*,1/2), {1/2}, (1/2,1-p_*), {1-p_*}, (1-p_*,1). '
'On the continuous outer edges F(0,q)=F(1,q)=F(p,0)=0 and F(p,1)=-h2(4p(1-p)). '
'Both actual singleton choices {X} and {Y} violate J_A<=M_A for every real 0<p,q<p_*.'
)
hypotheses=['Independent Bernoulli inputs with 0<p,q<1','Actual Boolean sign g=(-1)^(XY)','Normalized orthonormal product Fourier basis','M_A is conditional spectral entropy and J_A actual physical-child mixture mutual information','Shannon entropy in bits; outer edges mean continuous limits']
sha=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest()
claim={'claim_id':'A084-AND-CONTINUUM-CERTIFICATE','version':2,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':sha,'contributors':['A084'],'proof_source':{'path':str(ROOT/'PROOF.md'),'report':str(ROOT/'REPORT.md'),'certificate':'out/THRESHOLD_CERTIFICATE.json','validation':['out/GRID_CHECKS.json','out/DERIVATIVE_CHECKS.json','out/HYPERBOLA_ZERO_FIXTURES.json']},'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_TARGET_COMPLETE_PENDING_INDEPENDENT_REVIEW','supersedes':[{'claim_id':'A084-AND-CONTINUUM-CERTIFICATE','version':1,'reason':'Completes the same open packet from restricted rectangles to the full continuum sign map; the old restricted theorem remains valid.'}],'refutes':['A tax-free biased J_A<=M_A theorem after existential singleton choice, even on all two-bit AND biases.'],'first_unproved_line':None,'next_consumers':['A090','A094','B09','A041','A046','A050','A057','A064','A096']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
(ROOT/'CLAIMS.json').write_text(json.dumps([claim],indent=2),encoding='utf-8')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B17','packet_id':'A084','gap_id':'G-BIASED-TAX','attempt_id':'A084-continuum-2','method':'Exact conditional qubit-sector reduction; globally positive fourth derivative; strict-concavity root count; rational transition bracket and exact point checks','mathematical_delta':'Full real-parameter AND sign map proved, including second exact zero hyperbola, all additional roots/tangencies, unique p_* in (0.3640428066253662,0.3640428137779236), and both-singleton tax-free no-go on (0,p_*)^2. Replaces 902 unresolved-box gap with a complete continuum theorem. 2901 checks and 5 symbolic derivative identities pass.','deliverable_status':'ARTIFACT_COMPLETE_TARGET_COMPLETE_REVIEW_PENDING','mathematical_status':'AND_CONTINUUM_PACKET_RESOLVED_FULL_FEI_OPEN','claim_versions_used':[],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':2}],'source_artifacts':['REPORT.md','PROOF.md','CLAIMS.json','FROZEN_SPEC.json','DERIVATIVE_SPEC.json','PLOT_SPEC.json','code/check_signmap.py','code/check_derivatives.py','code/plot_signmap.py','out/THRESHOLD_CERTIFICATE.json','out/GRID_CHECKS.json','out/DERIVATIVE_CHECKS.json','out/HYPERBOLA_ZERO_FIXTURES.json','out/RESULT.json','out/SIGN_MAP.svg','out/SIGN_MAP.png'],'next_consumers':claim['next_consumers'],'next_action':'A090/A094 reconstruct the completed analytic map; B09/B13 apply its both-singleton correction domain to a source-complete terminal-inclusive physical tree payment with one-use influence. Retire AND sampling.','stagnant_substantive_attempts':0,'blockers':['No blocker at the packet target; universal nonreusing biased correction plus conditional-entropy payment remains unproved.'],'packet_ids':['A084']}
expected={x.split(' (',1)[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
for name in ['PROGRESS.json','PACKET_DELTA.json']:(ROOT/name).write_text(json.dumps(progress,indent=2),encoding='utf-8')
inputs=[PROTOCOL,SHARED/'BOARD.md',SHARED/'claude'/'B17'/'STREAM_NOTES.md',AGENT/'STATUS.md',AGENT/'LEARNED.md',AGENT/'runs'/'20261011T224831Z-account05-A084-continuum-parameters'/'REPORT.md',AGENT/'runs'/'20261011T224831Z-account05-A084-continuum-parameters'/'code'/'certify.py']
source=[]
for f in inputs:
    b=f.read_bytes();source.append({'path':str(f),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'role':'read-only input or pre-stage rolling snapshot'})
(ROOT/'out'/'SOURCE_RECEIPTS.json').write_text(json.dumps(source,indent=2),encoding='utf-8')
state='STATE: A084 stage 2 complete: full AND continuum sign map proved; all zero counts and exact p_* bracket; 2901 checks plus five symbolic identities pass; review pending, FEI OPEN.\nNEXT: A090/A094 review curvature and angle reflections; consume the both-singleton correction region in a terminal-inclusive B09/B13 tree payment; retire AND grids.\n'
(AGENT/'STATUS.md').write_text(state,encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp}: Stage2 resumed after reading board/B17 v2 and own status. Replaced brute box refinement by actual conditional-sector amplitude reduction. Derived psi fourth derivative >=32/ln2, strict concavity of G derivative, unique transition, full sign map and 1/2/3/1/4/3/2 q-root counts. Certified p_* in (7634531/20971520,152690623/419430400); 2901 exact/geometry checks passed in 0.7234s. Symbolic derivative checker initially left an equivalent trig residual; exact tangent rationalization resolved it, five identities passed in 0.4982s. Saved complete proof and standalone figure, refined the same claim to v2. Both singleton choices fail tax-free transfer on (0,p_*)^2. No FEI claim or independent acceptance inferred.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage2 closes the prior full-map gap: F=w[psi(theta)-psi(alpha)-psi(theta-alpha)], psi=h(sin^2), theta=asin(sqrt(p)), alpha=atan(sqrt(p/(1-p))(1-2q)), w=1-4pq(1-q). The fourth derivative of psi is >=32/ln2 via y=cot(2x) and |asinh y|<=|y|. Thus G_s derivative is strictly concave on its half interval. Unique p_* between 7634531/20971520 and 152690623/419430400 (~0.36404281) determines all extra zero branches. In addition to q=1/2, exact q=1/(2p) is zero when p>1/2. For each fixed p, root counts on intervals separated by p_*,1/2,1-p_* are 1,2,3,1,4,3,2 (singleton threshold rows included). Both singleton choices have J>M on (0,p_*)^2. Retire the 902-box refinement; nonreusing tree payment remains the global gap.\n')
# Validate protocol fields and all recorded fractions without rerunning the
# already passed mathematical checks. Final receipts bind exact bytes.
cert=json.loads((ROOT/'out'/'THRESHOLD_CERTIFICATE.json').read_text())
from fractions import Fraction as R
lo,hi=map(R,cert['bracket']);assert hi-lo<R(1,10**8)
assert R(cert['endpoint_K_intervals'][0][1])<0<R(cert['endpoint_K_intervals'][1][0])
assert json.loads((ROOT/'PROGRESS.json').read_text())==json.loads((ROOT/'PACKET_DELTA.json').read_text())
for heading in protocol['required_per_run']['report_fields']:
    assert '## '+heading in (ROOT/'REPORT.md').read_text()
assert (ROOT/'REPORT.md').read_text().rstrip().splitlines()[-1].startswith('**Universal bridge:**')
required=['REPORT.md','PROOF.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json']
assert all((ROOT/f).is_file() for f in required)
files=[]
for f in ROOT.rglob('*'):
    if f.is_file() and f.name!='RECEIPTS.json' and '__pycache__' not in f.parts:
        b=f.read_bytes();assert len(b)<20*1024*1024
        files.append({'path':str(f.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
receipt={'required_files_verified':required,'protocol_schema_check':'PASS; descriptive packet_ids label normalized to actual prescribed key','claim_statement_hash_verified':True,'compatibility_copy_verified':True,'transition_endpoints_exact_signs':'PASS','mathematical_checks':2901,'symbolic_derivative_identities':5,'independent_review':'pending','mirror_verification':'not performed; supervisor copy pending','files':files}
(ROOT/'out'/'RECEIPTS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
(ROOT/'out'/'DERIVATION_CHECKPOINT.json').write_text(json.dumps({'state':'COMPLETE_AUTHOR_PROOF_WITH_EXECUTED_CHECKS','proof':'PROOF.md','target':'full interior AND sign map','first_unproved_line_at_target':None,'universal_remaining_gap':'Nonreusing biased correction and conditional spectral entropy payment in actual physical stopping trees','independent_review':'pending'},indent=2),encoding='utf-8')
# The checkpoint changed after the first file pass; refresh its hash.
for item in receipt['files']:
    if item['path']==str(Path('out')/'DERIVATION_CHECKPOINT.json'):
        b=(ROOT/item['path']).read_bytes();item['bytes']=len(b);item['sha256']=hashlib.sha256(b).hexdigest()
(ROOT/'out'/'RECEIPTS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'saved':required,'claim':'A084-AND-CONTINUUM-CERTIFICATE@2','files_receipted':len(files),'packet_target':'COMPLETE; independent review pending','full_fei':'OPEN'}),flush=True)
