import hashlib,json,datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; AGENT=ROOT.parents[1]
REPORTS=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUPP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
TEAM=Path(r'~\brain_workers\FEI100_20261011')
A051=TEAM/'agents/A051/runs/20261011T214321Z-account05-A051-near-extremizer-definition'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def dump(path,x): path.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

assert sha(A051/'EXISTENCE_AND_LIMITS.md')=='123fcf33fb47d6823a28afd1a9f282e6f1d0f3bc38a929987510933c0bf020c8'
sources=[]
for name in ('EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex'):
    sources.append((REPORTS/name,'Protocol/status navigation; plan B11 lines 830--860 and obstruction/accounting sections'))
for name in ('CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md'):
    sources.append((SUPP/name,'Campaign supplement scope'))
for name in ('BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','ERASURE_REDUCTION.md','ADDENDUM_11_44_COMPONENT_ENTROPY_COUNTEREXAMPLE.md','ADDENDUM_11_26_CRITICAL_RARE_MOMENT.md','ROUTE_MAP_CURATED.md'):
    sources.append((SUPP/'sources'/name,'Physical restriction, criticality and component sections named in REPORT'))
for name in ('threshold_paper_38pp.txt','threshold_paper_29pp_earlier_version.txt','percolation_spectral_pivotal_entropy_30pp.txt','percolation_spectral_pivotal_entropy_31pp_other_version.txt'):
    sources.append((TEAM/'context'/name,'Current threshold 8.4 Prop 8.9/Cor 8.10; earlier composition scope; percolation introductions/Thms 1.1--1.3; no percolation premise'))
for name in ('REPORT.md','EXTREMALITY_DEFINITION.tex','EXISTENCE_AND_LIMITS.md','CLAIMS.json'):
    sources.append((A051/name,'A051 existence, reduction ledger and critical block identity, independently reviewed locally'))
for stream,run in (('B05','20261011T193057Z-account01-B05-rare-restrictions'),('B09','20261011T195500Z-account01-B09-biased-restriction-uncertainty'),('B19','20261011T195038Z-account01-B19-independent-review')):
    sources.append((REPORTS/'runs'/stream/run/'REPORT.md','Earlier run scope; no B09 proof premise'))
sources.append((TEAM/'BOARD.md','Read at stage start and before persistence; mutable byte pin is last snapshot'))
sources.append((ROOT/'out/COMPONENT_RATIO_SOURCE.md','Retrieved seven-bit source at commit 31c201a0a8caef323c65abe964ff8ed4b702fc81, blob 978c180155e1a25d4d8f34988b5216269c7b83c3'))
dump(ROOT/'out/SOURCE_MANIFEST.json',{'sources':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'locator':loc} for p,loc in sources],
     'missing_lead_notes':str(TEAM/'claude/B11/STREAM_NOTES.md'),'lead_notes_present':(TEAM/'claude/B11/STREAM_NOTES.md').exists()})

statement='For every actual Boolean sign f on a finite uniform cube with entropy in bits, every rank-r binary matrix V, every r-coordinate physical pivot block A with V_A invertible, and every syndrome word y0, set Y=VS for the squared Fourier law S, e0(t)=V_A^-1(y0+V_Ac t), b=E|S_A+e0(S_Ac)| and epsilon=P(Y!=y0). The actual restriction entropy drop L_A obeys L_A=H(Y|S_Ac)+J_A<=H(Y|S_Ac)+(2/ln2)b, with b<=r epsilon. If all proper physical restrictions have ratio at most R(f)=H(f)/I(f), then R(f)I_A<=H(Y|S_Ac)+(2/ln2)b<=h2(epsilon)+epsilon log2(2^r-1)+(2r/ln2)epsilon. If instead D_K(f)>0 and every proper restriction has D_K<=0, replace the left side by KI_A+D_K(f). For every nonzero physical flip mask u and pivot i in its support, epsilon_u=(1-|E f(x)f(x+u)|)/2 satisfies the rank-one bound R(f)I_i<=h2(epsilon_u)+(2/ln2)epsilon_u (or its threshold-critical version). No connectedness or universal influence payment is claimed.'
hypotheses=['Actual Boolean signs on finite uniform cubes; entropy in bits',
 'V has positive rank r; A consists of r physical coordinates and V_A is invertible over F2',
 'Ratio conclusions require I(f)>0 and the stated all-proper-physical-restriction comparison; constants have H=I=0',
 'Threshold conclusions require fixed finite K>=0, positive root deficit and nonpositive deficits in all proper physical restrictions']
claim={'claim_id':'A052-AFFINE-SYNDROME-CRITICAL-DISORDER','version':1,'exact_statement':statement,'hypotheses':hypotheses,
 'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'contributors':['account05/A052'],
 'proof_source':{'path':str(ROOT/'CRITICAL_SOURCE_STRUCTURE.tex'),'sha256':sha(ROOT/'CRITICAL_SOURCE_STRUCTURE.tex'),'locator':'equations (1)--(3); REPORT complete derivation including two-point logarithmic Sobolev proof'},
 'proof_dependencies':[{'claim_id':'A051-CRITICAL-BLOCK-DEFICIT','version':1,'status':'LOCALLY_INDEPENDENTLY_RECONSTRUCTED_ACCEPT_AT_STATED_SCOPE','source':str(ROOT/'REVIEW_A051.md')}],
 'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
 'first_unproved_line':None,'next_consumers':['A053','A054','A055','A026','A028','A090','A094','B20']}
dump(ROOT/'CLAIMS.json',[claim])

progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B11','packet_id':'A052',
 'gap_id':'G-R-SELECT','attempt_id':'A052-affine-syndrome-1','method':'Physical deficit comparison, Fourier-fiber character demodulation, uniform logarithmic Sobolev, exact rational replay',
 'mathematical_delta':'Proved universal L_A<=H(VS|S_Ac)+(2/ln2)b and quantitative affine-concentration obstruction for every physical ratio-critical source; replayed both component failures and certified noncriticality of their sign lifts; independently reconstructed both A051 source claims.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_STRUCTURAL_THEOREM_PROVED_UNREVIEWED; UNIVERSAL_SELECTION_AND_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A051-THRESHOLD-CRITICAL-EXISTENCE','version':1,'statement_sha256':'43d9bb2d782202315b27f61ecfe592099463a7eb6e4b04982e614bdc2000b165','review':'A052 ACCEPT_AT_STATED_SCOPE locally; B20 adoption pending'},
                        {'claim_id':'A051-CRITICAL-BLOCK-DEFICIT','version':1,'statement_sha256':'867f421d03cb508140df4ec5aba393a4b4c419b07f415c004c6f8a390bfc075d','review':'A052 ACCEPT_AT_STATED_SCOPE locally; B20 adoption pending'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'NEW_SCOPED_STRUCTURAL_THEOREM'},
                              {'claim_id':'A051-THRESHOLD-CRITICAL-EXISTENCE','version':1,'change':'LOCAL_INDEPENDENT_REVIEW_SAVED; SOURCE_UNMODIFIED'},
                              {'claim_id':'A051-CRITICAL-BLOCK-DEFICIT','version':1,'change':'LOCAL_INDEPENDENT_REVIEW_SAVED; SOURCE_UNMODIFIED'}],
 'source_artifacts':['CRITICAL_SOURCE_STRUCTURE.tex','PRUNING_SCOPE.md','REVIEW_A051.md','out/SOURCE_MANIFEST.json','out/FROZEN_SPEC.json','out/FROZEN_SPEC_SIGN_REPLAY.json','code/check_structure.py','code/check_sign_lifts.py','out/PILOT_OUTPUT.json','out/CHECK_OUTPUT.json','out/SIGN_REPLAY_OUTPUT.json'],
 'next_consumers':['A053','A054','A055','A026','A028','A090','A094','B20'],
 'next_action':'Minimize the affine-syndrome descent certificate over proper pivot blocks on near-tensor/sparse-defect high-ratio candidates; seek a universally affordable block while retaining child deficits. Independent review A090/A094.',
 'stagnant_substantive_attempts':0,'blockers':['B11 STREAM_NOTES.md absent; independent allowed work completed','Universal affordable-block existence remains unproved'],
 'packet_ids':['A052']}
dump(ROOT/'PROGRESS.json',progress);dump(ROOT/'PACKET_DELTA.json',progress)

protocol=json.loads((REPORTS/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))['required_per_run']
assert set(claim)==set(protocol['claim_fields'])
expected={x if not x.startswith('packet_ids ') else 'packet_ids' for x in protocol['progress_fields']}
assert set(progress)==expected
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
for name in ('PILOT_OUTPUT.json','CHECK_OUTPUT.json','SIGN_REPLAY_OUTPUT.json'):
    assert json.loads((ROOT/'out'/name).read_text())['status']=='PASS'
assert json.loads((ROOT/'out/CHECK_OUTPUT.json').read_text())['small']['syndrome_cases']==20680

now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A052 structural packet complete locally: affine-syndrome disorder forced by physical criticality; 65,321 exact full/replay assertions PASS; full FEI OPEN, independent review pending.\nNEXT: A090/A094 review; A053/A054/A055 test proper-pivot syndrome descent on near-tensor/sparse-defect candidates; universal block selection remains unpaid.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+now+' — Read protocol/board and A051; lead notes absent. Derived Fourier-fiber demodulation channel estimate J_A<=2b/ln2 and critical anti-affine-concentration restriction. Frozen exact pilot passed 895 assertions; full check passed 65,307 assertions across 278 tables and 20,680 syndrome cases; two sign-lift replays passed 14 assertions. Reproduced both component failures and larger-ratio proper descendants. Saved local independent reconstructions of both A051 claims. Connectedness and universal affordable block remain open; no shared or external writes.\n')
(AGENT/'LEARNED.md').write_text('''# A052 durable facts

- Physical all-descendant ratio criticality supplies L_A>=R I_A only by the average child-deficit comparison. Dimension-critical K-violations strengthen this to L_A>=KI_A+D_K. Children need not inherit criticality.
- For rank-r binary V and an invertible r-coordinate physical pivot A, H(S_A|S_Ac)=H(VS|S_Ac). With e0(t)=V_A^-1(y0+V_Ac t), fiberwise character demodulation and logarithmic Sobolev prove J_A<=2 E|S_A+e0(S_Ac)|/ln2. The demodulated fibers are analytic real functions, not Boolean descendants.
- Let epsilon=P(VS!=y0). Criticality forces R I_A<=h2(epsilon)+epsilon log2(2^r-1)+(2r/ln2)epsilon. Rank one gives epsilon_u=(1-|E f(x)f(x+u)|)/2 and R I_i<=h2(epsilon_u)+2epsilon_u/ln2 for i in u. This quantitatively excludes signed symmetry, but permits epsilon and influence to vanish together.
- The historical nine-bit connected-components example refutes raw entropy subadditivity; the seven-bit example refutes maximum raw component ratio. Both inherited indicators have a larger-ratio two-data-bit physical restriction. Their sign lifts separately have point-defect physical restrictions with H/I greater by >1/2, certified exactly here. Raw indicator entropy is not probability entropy.
- Arbitrary-core sparse activation preserves FEI hardness as a class. Amplified violating cores are smaller violating physical restrictions, so the standard construction fails dimension-criticality. Rarity or raw AND-power criticality does not pay full-degree logarithmic moments.
- Primary next gap: a universal proper pivot block with H(VS|S_Ac)+(2/ln2)b<=K I_A. The current structural theorem is necessary, not a universal FEI bound or connected-support result.
''',encoding='utf-8')

files=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='RECEIPTS.json' and '__pycache__' not in p.parts]
assert all(p.stat().st_size<20*1024*1024 for p in files)
dump(ROOT/'out/RECEIPTS.json',{'generated_at':now,'local_only':True,'remote_mirror_verified':False,
 'files':[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)],
 'rolling_files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in (AGENT/'STATUS.md',AGENT/'WORKLOG.md',AGENT/'LEARNED.md')]})
print(json.dumps({'status':'PASS','claim_schema':'EXACT','progress_schema':'EXACT','receipt_files':len(files),'claim_count':1,'local_only':True}))
