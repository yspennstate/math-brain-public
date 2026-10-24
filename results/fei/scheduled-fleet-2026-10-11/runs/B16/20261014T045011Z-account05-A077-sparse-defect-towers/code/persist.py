from pathlib import Path
import json,hashlib

RUN=Path(__file__).resolve().parents[1]
AGENT=RUN.parents[1]
TEAM=Path(r'~\brain_workers\FEI100_20261011')
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
domains=[(2,1),(2,2),(4,1),(4,2),(6,1)]
chunks=[]
for k,r in domains:
    for z in (-1,0,1):
        p=RUN/'out'/f'chunk_k{k}_r{r}_z{z}.json';o=read(p)
        assert o['records'][0]['k']==k and o['records'][0]['r']==r
        assert o['selector_partition']==z and o['elapsed_seconds']<55
        chunks.append({'path':str(p.relative_to(RUN)),'sha256':sha(p),'bytes':p.stat().st_size,'output':o})
main={key:sum(x['output'][key] for x in chunks) for key in (
 'restriction_states','local_queries','eligible_private_rows','sharp_contraction_rows','assertions')}
assert main=={'restriction_states':29403,'local_queries':83511,'eligible_private_rows':338,'sharp_contraction_rows':72,'assertions':284721}
review=read(RUN/'out'/'review.json');assert review['actual_wrappers']==4168 and review['assertions']==33344
summary={'main':main,'chunks':15,'root_policy_ledgers':30,'review':review,
         'main_plus_review_assertions':main['assertions']+review['assertions'],
         'maximum_chunk_helper_seconds':max(x['output']['elapsed_seconds'] for x in chunks),
         'chunk_receipts':[{k:v for k,v in x.items() if k!='output'} for x in chunks],
         'pilot_duplicates_excluded':True,'monolithic_watchdog_coverage_claimed':False}
dump(RUN/'out'/'VALIDATION_SUMMARY.json',summary)
source=TEAM/'agents'/'A076'/'runs'/'20261014T042128Z-account05-A076-threshold-and-tribes-controls'
a78=TEAM/'agents'/'A078'/'runs'/'20261014T023613Z-account05-A078-coding-and-padding'
source_claim=next(c for c in read(source/'CLAIMS.json') if c['claim_id']=='A076-STRUCTURED-SPECTRA')
assert source_claim['version']==5
review_record={'claim_id':source_claim['claim_id'],'version':5,
 'original_statement_sha256':source_claim['statement_sha256'],'reviewer':'A077/account05',
 'scope':'PRIVATE_ADMISSION_PROOF sections1-3 equations1-5 only; earlier bundle and later sharpness/reset/equivalence clauses excluded',
 'verdict':'HOLDS_AT_STATED_SCOPED_LOCATORS','substantive_repair':False,
 'reconstruction':'REVIEW_A076.md; PROOF.md section1; code/check.py review; out/review.json',
 'whole_bundle_acceptance':False,'actual_wrappers':4168,'exact_assertions':33344}
dump(RUN/'REVIEW_A076.json',[review_record])
receipts=[
 (PROTOCOL,'complete v2 protocol'),
 (TEAM/'BOARD.md','2026-10-14 04:50 UTC board and focused middle-agent rereads'),
 (TEAM/'claude'/'B16'/'STREAM_NOTES.md','full unchanged v2'),
 (source/'PRIVATE_ADMISSION_PROOF.md','full sections1-6; reviewed sections1-3 equations1-5 only'),
 (source/'CLAIMS.json','version5 statements and review locators'),
 (a78/'PROOF.md','full sections1-5; actual shadow ownership context, not a paid arbitrary core dependency'),
 (AGENT/'runs'/'20261014T020716Z-account05-A077-sparse-defect-towers'/'PROOF.md','prior actual rare/rare family, physical ledger and paid-order proof'),
]
dump(RUN/'out'/'SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'scope':scope} for p,scope in receipts])
statement=(
 'For any Boolean pair on independent uniform bits, before a fresh selector is revealed, let delta be the physical mismatch probability '
 'and let eligibility be absorbing under data restrictions. At marked private queries suppose expected eligible-child mismatch mass is '
 'at most (1-gamma) times the parent mismatch, 0<gamma<=1. The single mark M=(4/gamma)delta*1_eligible pays '
 'sum_marked w[B_i(mux)-B_i(private core)/4]+E M_leaf<=M_root. '
 'For every even k>=2,r>=1, let G=1-2*1{s=0,x=0},H=(-1)^(sum paired s-coordinate products),A=1{r controls zero}, '
 'Gp=1+A(G-1),Hp=1+A(H-1),W=mux_z(Gp,Hp). At every restriction before z is revealed, eligibility means active gates, '
 'a surviving nonconstant point-defect base G and nonconstant base H. Every eligible G-private exposure contracts the weighted '
 'eligible mismatch mass by at least1/3; the2/3 surviving fraction is attained at k=2 private x for every r. '
 'Set K=12delta*1_eligible+10delta*1_z_unqueried, and K=0 after z revelation. '
 'Every finite adaptive fresh-coordinate stopping tree, including arbitrary early selector revelation and arbitrary interleaving, satisfies '
 'B_tree(W)+E K_leaf<=10P_data+K_root, K_root=22Inf_z(W). Coordinate-wise influence conservation gives '
 'P_data=I_data(root)-E I_data(leaf),P_z=Inf_z(root)-E Inf_z(leaf). '
 'The exact entropy law is H(W)=B_tree+JS_tree+E H(actual leaf),JS_tree<=2(P_data+P_z)/ln2; unqueried-selector leaf entropy '
 'is half both residual core entropies plus the exact paired Fourier potential. Complete constant-leaf trees have B_tree,Q_tree<=22I(W),H(W)<25I(W). '
 'The existing class entropy bound H(W)<8I(W) remains stronger; the new result is repeated-exposure ownership with retained terminal banks. '
 'No released-child hypothesis is proved for arbitrary cores whose two children remain eligible.'
)
cid='A077-GEOMETRIC-MARKED-PRIVATE-RESERVE'
deps=[{'claim_id':'A076-STRUCTURED-SPECTRA','version':5,
       'scope':'PRIVATE_ADMISSION_PROOF sections1-3 equations1-5; independently reconstructed scoped HOLDS in REVIEW_A076.json'}]
consumers=['A076','A078','A058','A027','A064','A091','A092','A088','claude/B16','B20']
claims=[{'claim_id':cid,'version':1,'exact_statement':statement,
 'hypotheses':['Independent uniform physical inputs; entropy bits','Generic mark requires absorbing eligibility and its explicit release fraction gamma',
               'Actual family k even>=2,r integer>=1; fixed point activation and paired quadratic branches',
               'Finite adaptive fresh-coordinate tree, arbitrary stopping and selector timing; terminal cores retained'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A077/account05'],
 'proof_source':{'proof':'PROOF.md sections1-7','certificates':'code/check.py; out/VALIDATION_SUMMARY.json; all15 exact chunk outputs'},
 'proof_dependencies':deps,'review_records':[],'status':'AUTHOR_PROVED_EXACT_CHECKED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':consumers}]
dump(RUN/'CLAIMS.json',claims)
next_action=('At a second private collision with both core children nonconstant, replace the point-defect exit by one actual unused certified signed child surplus, '
             'preserving original selector account, inherited quarter erasure, and both exact terminal spectra; use A076 repeated-reset witness as guard.')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B16','packet_id':'A077',
 'gap_id':'G-R-MISMATCH','attempt_id':'A077-G-R-MISMATCH-05',
 'method':'Scoped A076 quarter-admission review; absorbing mismatch mark with geometric point-defect exits; exact all-restriction stopping-bank certificates',
 'mathematical_delta':'Repeated private exposures in actual rare/rare tower paid by one released mark, with1/3 exit and reserved selector component; arbitrary adaptive interleaving and selector timing satisfy B_T+E K_leaf<=10P_data+22Inf_z(root).',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'GEOMETRIC_EXIT_OWNERSHIP_PROVED_GENERAL_CHILD_SURPLUS_OPEN',
 'claim_versions_used':deps,'claims_created_or_changed':[cid+'@1','A076-STRUCTURED-SPECTRA@5 scoped sections1-3 review HOLDS'],
 'source_artifacts':['REPORT.md','PROOF.md','REVIEW_A076.md','REVIEW_A076.json','FROZEN_SPEC.json','REVIEW_FROZEN_SPEC.json',
                     'CHUNK_FROZEN_SPEC.json','MULTISCALE_COST_LEDGER.json','code/check.py','code/exact_math.py',
                     'out/pilot.json','out/review.json','out/FULL_WATCHDOG.json','out/VALIDATION_SUMMARY.json'],
 'next_consumers':consumers,'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['New release/application independent review and remote adoption pending; generic two-live-child release and arbitrary terminal-core payment open'],
 'packet_ids':['A077']}
dump(RUN/'PROGRESS.json',progress);dump(RUN/'PACKET_DELTA.json',progress)
status=('STATE: A077 stage5 complete: repeated rare-private exposures paid by one geometric mark; arbitrary interleaving/selector timing B_T+E K_leaf<=10P_data+22Inf_z; 318,065 exact main+review checks; A076 scoped HOLDS; FEI OPEN.\n'
        'NEXT: Replace the point-exit release by unused certified signed child surplus at a second private collision with both children nonconstant; retain original selector account, quarter core bill and both terminals.\n')
(AGENT/'STATUS.md').write_text(status,encoding='utf-8')
entry=('\n2026-10-14 stage5 ('+RUN.name+'): Consumed and independently reviewed A076 first-private/antichain admission (4168 wrappers,33344 exact checks); '
       'did not duplicate it. Proved absorbing mismatch mark with gamma=1/3 for repeated point-private exposures, including newly irrelevant quadratic partners. '
       'Kept separate reserved selector component; any adaptive stopped tree has B_T+E K_leaf<=10P_data+22Inf_z(root), arbitrary early z and mixed order. '
       'Monolithic55-second watchdog hit without sign failure; unchanged domain partitioned into15 sequential selector-state chunks, all saved immediately: '
       '29403 states,83511 queries,284721 exact checks; total main+review318065, max helper48.471348s. '
       'No new class entropy constant claimed (older H<8I is better); NEXT certify live-child signed surplus instead of point exit. FEI OPEN.\n')
work=AGENT/'WORKLOG.md'
if RUN.name not in work.read_text(encoding='utf-8-sig'):
    with work.open('a',encoding='utf-8') as f:f.write(entry)
learn=AGENT/'LEARNED.md'
heading='## 2026-10-14 geometric private-exposure mark'
durable=('\n'+heading+'\n\n'
 'A076 stage5 private query admission retains a quarter: 0<=B_i(mux)-B_i(private core)/4<=4delta; scoped local/antichain theorem independently HOLDS. '
 'Its four-delta allowance cannot be reset at each layer.\n\n'
 'If eligibility is absorbing and a marked private query releases at least gamma of eligible mismatch mass, M=(4/gamma)delta*1_eligible '
 'pays all repeated remainders by its stopped telescope. In the actual common-activated bent/spike family, G survival implies base H mean h<=1/2 '
 'and private point derivative a<=h^2<=(1-h)/2. Answer1 kills G; answer0 keeps at most2/3 mismatch mass. '
 'Thus M=12delta*1_eligible pays the repeated private bills. Retain S=10delta for later selector B; K=M+S is zero after z reveal.\n\n'
 'Every adaptive fresh-coordinate stopped tree on that family, with arbitrary selector timing, satisfies B_T+E K_leaf<=10P_data+22Inf_z(root). '
 'Terminal H is the exact actual core law, not K_leaf; both inherited branch entropies remain when z is unqueried. '
 'The new content is the physical release/ownership certificate, not a class H/I improvement. '
 'Generic two-live-child restrictions need not release any mismatch mass, so the next target is genuinely unused signed child surplus, with inherited quarter and terminals retained.\n')
if heading not in learn.read_text(encoding='utf-8-sig'):
    with learn.open('a',encoding='utf-8') as f:f.write(durable)
protocol=read(PROTOCOL)
assert set(claims[0])==set(protocol['required_per_run']['claim_fields'])
fields=[x if not x.startswith('packet_ids ') else 'packet_ids' for x in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(fields)
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
manifest=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and '__pycache__' not in p.parts and p.name!='ARTIFACT_MANIFEST.json':
        assert p.stat().st_size<20*1024*1024
        manifest.append({'path':str(p.relative_to(RUN)),'sha256':sha(p),'bytes':p.stat().st_size})
dump(RUN/'out'/'ARTIFACT_MANIFEST.json',manifest)
print(json.dumps({'claim_schema':'PASS','progress_schema':'PASS','compatibility_copy':'PASS','report_fields':'PASS',
 'artifacts':len(manifest),'main_assertions':main['assertions'],'review_assertions':review['assertions'],
 'total_assertions':summary['main_plus_review_assertions'],'largest_bytes':max(x['bytes'] for x in manifest)}))
