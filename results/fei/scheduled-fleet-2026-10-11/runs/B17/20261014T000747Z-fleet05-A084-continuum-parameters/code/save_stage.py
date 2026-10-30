from pathlib import Path
import json, hashlib, datetime

ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
SHARED=AGENT.parents[1]
PROTOCOL=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8'))
def save(path,obj):
    path.write_text(json.dumps(obj,indent=2),encoding='utf-8')
def digest(path):
    b=path.read_bytes()
    return {'path':str(path),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

sources=[PROTOCOL,SHARED/'BOARD.md',SHARED/'claude/B17/STREAM_NOTES.md',AGENT/'STATUS.md',
    SHARED/'agents/A072/runs/20261013T222130Z-fleet05-A072-exact-walsh-engine/REPORT.md',
    SHARED/'agents/A072/runs/20261013T222130Z-fleet05-A072-exact-walsh-engine/CLAIMS.json',
    SHARED/'agents/A072/runs/20261013T222130Z-fleet05-A072-exact-walsh-engine/code/check.py',
    SHARED/'agents/A072/runs/20261013T222130Z-fleet05-A072-exact-walsh-engine/out/orientation_policy.json',
    SHARED/'agents/A071/runs/20261013T215901Z-fleet05-A071-search-space-design/REPORT.md']
save(ROOT/'out/SOURCE_RECEIPTS.json',[dict(digest(p),role='Read-only source; current bytes at persistence, not a historical immutable snapshot') for p in sources])
statement=('Let h:{-1,1}^6->{-1,1} be negative exactly at binary input indices {0,1,2,4,8,16,32,6,17,40}, with bit0 denoting +1. '
    'For every nonconstant uniform-cube Boolean core g of every finite dimension n with minority output probability p_min in [1/16,1/2], orient g0 to P(g0=-1)=p_min, and set g1=g0 when p_min<=7/32 and g1=-g0 otherwise. '
    'Compose six disjoint identical copies F=h(g1,...,g1). For every relevant physical core coordinate i and every block j, '
    'B_(j,i)(F)/Inf_(j,i)(F)>=B_i(g)/Inf_i(g), where B_i=H(S_i|S_-i) for the squared uniform Fourier spectrum, in bits. '
    'The increase is strict when the singleton Fourier coefficient beta_i is nonzero. '
    'For the induced mean m and q=2p(1-p)^3(2-p), the exact signed reserve R_m(t)=sum_T phi(U_T,tD_T)-q phi(m^2,t) is nonnegative for all real t>=0 in the stated oriented bias bands, with equality at t=0. '
    'The full terminal identity is H(F)=6q H(g)+C_p with C_p=H_p(h)-6q h2(1-m^2), and I(F)=6q I(g). '
    'No arbitrary-dimensional rare-sector exclusion, iteration closure, or universal FEI bound is asserted.')
hypotheses=['Actual Boolean core on the uniform cube, finite arbitrary dimension and nonconstant',
    'Minority probability in [1/16,1/2]; balanced tie may be oriented either way',
    'Six identical core copies on disjoint physical variable blocks; specified six-bit gate',
    'True conditional spectral erasure entropy and true physical influence; entropies in bits',
    'Normalized orthonormal biased outer expansion used only as an exact composition identity']
sha=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest()
consumers=['A075','A071','A072','A089','A074','A092','A090','A094','B15','B17','B20']
claim={'claim_id':'A084-F6-CONTINUUM-ADMISSION','version':1,'exact_statement':statement,
    'hypotheses':hypotheses,'statement_sha256':sha,'contributors':['A084'],
    'proof_source':{'path':str(ROOT/'PROOF.md'),'report':str(ROOT/'REPORT.md'),
        'certificates':['out/MINORITY_ORIENTATION.json','out/COMPLEMENT_ORIENTATION.json'],
        'validation':['out/GROUPING_CHECKS.json','out/PHYSICAL_RESULT.json','out/CONTINUUM_RESULT.json']},
    'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_RESTRICTED_CONTINUUM_PENDING_INDEPENDENT_REVIEW',
    'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':consumers}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save(ROOT/'CLAIMS.json',[claim])
progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B17','packet_id':'A084',
    'gap_id':'G-R-SELECT','attempt_id':'A084-continuum-3',
    'method':'Weighted-geometric-mean boundary reduction; four exact packet ratios; thirteen rational interval boxes; analytic balanced boundary; exact physical composition checks',
    'mathematical_delta':'Closes all real singleton parameters and all core dimensions for common-sign admission on minority bias [1/16,1/2]. Thirteen exact interval boxes, 17 formal rational identities and 217 physical assertions passed. Rare-bias, iteration closure and terminal payment remain open.',
    'deliverable_status':'ARTIFACT_COMPLETE_REVIEW_PENDING','mathematical_status':'RESTRICTED_CONTINUUM_ADMISSION_PROVED_FULL_FEI_OPEN',
    'claim_versions_used':[{'claim_id':'A072-F6-SIXBIT-GUARDED-ADMISSION','version':1,'role':'Source-bound precursor only; signed identity rederived, not a proof assumption'}],
    'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
    'source_artifacts':['REPORT.md','PROOF.md','CLAIMS.json','CONTINUUM_SPEC.json','SYMBOLIC_SPEC.json','code/certify_continuum.py','code/check_physical.py','code/check_grouping.py','out/CONTINUUM_RESULT.json','out/GROUPING_CHECKS.json','out/PHYSICAL_RESULT.json','out/SOURCE_RECEIPTS.json'],
    'next_consumers':consumers,
    'next_action':'Resolve actual arbitrary-dimensional high-E cores at p_min<1/16 by exclusion or owned signed payment, retaining full terminal C_p and checking bias closure; independent reviewers A074/A092/A090/A094.',
    'stagnant_substantive_attempts':0,
    'blockers':['No blocker inside proved bias band; independent review pending.','Arbitrary-dimensional high-E rare sector p_min<1/16 unresolved.','Iteration-closed bias policy and terminal-inclusive physical payment for C_p unresolved.'],
    'packet_ids':['A084']}
assert set(progress)=={x.split(' (',1)[0] for x in protocol['required_per_run']['progress_fields']}
for name in ['PROGRESS.json','PACKET_DELTA.json']:save(ROOT/name,progress)

report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
report=report.replace('    python -X utf8 code/check_physical.py','    python -X utf8 code/check_physical.py\n    python -X utf8 code/check_grouping.py')
report=report.replace('The actual-core verifier reconstructs', 'The supplementary symbolic checker verifies 17 global rational-polynomial identities (12 packet-to-ratio identities, four aggregate weights, and their sum q), not merely sampled polynomial equalities; SymPy 1.14.0, runtime 76.3544 seconds, out/GROUPING_CHECKS.json.\n\nThe actual-core verifier reconstructs')
report=report.replace('all jobs below their frozen CPU-runtime budgets and under the 30-minute rule', 'the supplementary grouping verifier took 76.3544 seconds, exceeding the 55-second symbolic pilot budget; this overrun is recorded rather than described as compliant with that budget. It was a fixed algebra check, not an expanded search; all jobs were under the 30-minute limit')
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: A084 stage 3 author proof complete: all-dimensional common-sign admission on minority bias [1/16,1/2]; 13 exact boxes, 17 symbolic identities, 217 physical assertions; independent review pending, FEI OPEN.\nNEXT: Resolve high-E rare bias p_min<1/16 via actual-core exclusion or owned signed payment; retain C_p and check iteration bias closure; A074/A092/A090/A094 review.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp}: Stage3 read board/B17/own status and protocol; B17 AND direction is stale and already finished, so consumed new A071/A072 continuum gap. Floating pilots were discovery only. Derived signed physical-coordinate identity and geometric-mean slope criterion. Four ratio groups yield exact 13-box all-real certificate on [1/16,1/2] minority bias with one orientation; analytic boundaries include balanced mean. 25 packet checks, 17 formal symbolic identities and 217 actual physical assertions passed. Initial symbolic parser created a different m symbol; explicit locals fixed the internal assertion without changing formulas. Supplementary fixed grouping check ran 76.3544s, over the 55s symbolic pilot budget, within 30min and <150MB; no search expansion or memok override. Saved author theorem pending independent review, with rare bias, iteration and full terminal C_p payment unresolved.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage3: For positive signed packets, c=m^2, u=U/D and lambda=D/q, the boundary slope A=sum D log2(u/c) controls ALL t>=0: G(t)=product(t+u)^lambda has G\'(t)>=1, hence A>=0 implies R(t)>=0. Negative A forces failure near t=0. The specified six-bit gate has four exact U/D ratio groups. Common policy: minority orientation up to p_min=7/32, complemented above; thirteen rational boxes and analytic m in [-1/2,0] prove admission for every dimension and p_min in [1/16,1/2]. This preserves true B_i/Inf_i for every coordinate simultaneously. It is not bias-iteration closure or a terminal payment: H(F)=6qH(g)+C_p must remain. As p_min->0, normalized slopes are 2log2 p_min+6+o(1) and 2log2 p_min+2+o(1), so both fail eventually; actual high-E realizability below1/16 remains unknown. See stage3 PROOF.md and exact certificates.\n')
save(ROOT/'out/CHECKPOINT.json',{'state':'COMPLETE_AUTHOR_PROOF_CHECKS_PASSED','bias_scope':'minority [1/16,1/2], every finite core dimension','boxes':13,'symbolic_identities':17,'physical_assertions':217,'independent_review':'pending','universal_fei':'OPEN'})
for heading in protocol['required_per_run']['report_fields']:assert '## '+heading in report
assert report.rstrip().splitlines()[-1].startswith('**Universal bridge:**')
assert json.loads((ROOT/'PROGRESS.json').read_text())==json.loads((ROOT/'PACKET_DELTA.json').read_text())
files=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json' and '__pycache__' not in p.parts:
        item=digest(p);assert item['bytes']<20*1024*1024
        item['path']=str(p.relative_to(ROOT));files.append(item)
save(ROOT/'out/RECEIPTS.json',{'required_files_verified':['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json'],
    'protocol_fields':'PASS','claim_statement_hash_verified':True,'compatibility_copy_verified':True,
    'certificate_boxes':13,'formal_symbolic_identities':17,'physical_assertions':217,
    'independent_review':'pending','supervisor_copy':'pending','files':files})
for item in files:
    assert hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest()==item['sha256']
print(json.dumps({'saved':ROOT.name,'claim':claim['claim_id']+'@1','files_receipted':len(files),'readback':'PASS','full_FEI':'OPEN'}))
