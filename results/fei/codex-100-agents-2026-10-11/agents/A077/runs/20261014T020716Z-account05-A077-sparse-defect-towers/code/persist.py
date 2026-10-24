from pathlib import Path
import json,hashlib

RUN=Path(__file__).resolve().parents[1]
AGENT=RUN.parents[1]
SHARED=Path(r'~\brain_workers\FEI100_20261011')
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def dump(p,obj):p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def source(agent,run,file):return SHARED/'agents'/agent/'runs'/run/file
A78RUN='20261013T234208Z-account05-A078-coding-and-padding'
A76RUN='20261014T013416Z-account05-A076-threshold-and-tribes-controls'
A97RUN='20261013T222610Z-account05-A097-cross-route-transfer'
receipts=[
 (PROTOCOL,'full execution protocol v2'),
 (SHARED/'BOARD.md','full stage board with focused re-reads of truncated agent middle'),
 (SHARED/'claude'/'B16'/'STREAM_NOTES.md','full unchanged v2'),
 (AGENT/'runs'/'20261013T222235Z-account05-A077-sparse-defect-towers'/'PROOF.md','full sections1-6'),
 (source('A078',A78RUN,'PROOF.md'),'full sections1-4; scoped review sections1-2 equations1,3,4'),
 (source('A078',A78RUN,'CLAIMS.json'),'v2 complete statement and scope'),
 (source('A078',A78RUN,'REVIEW_A077.md'),'full independent acceptance of previous A077 v1'),
 (source('A078','20261012T023229Z-account05-A078-coding-and-padding','CORE_TRANSPORT_PROOF.md'),'full sections1-5'),
 (source('A076',A76RUN,'OWNED_PIVOT_PROOF.md'),'full sections1-6; scoped review sections1-5 equations1-9'),
 (source('A076',A76RUN,'CLAIMS.json'),'v4 statements, locators, review records'),
 (source('A097',A97RUN,'REPORT.md'),'full shared-data complete-reference scope'),
]
dump(RUN/'out'/'SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'scope':scope} for p,scope in receipts])
reviews=[]
for agent,run,ids,scope in [
 ('A078',A78RUN,['A078-PAIRED-QUARTER-PROFILE-AND-PADDING'],'stage3 PROOF sections1-2 equations1,3,4 only'),
 ('A076',A76RUN,['A076-STRUCTURED-SPECTRA','A076-TRIBES-PAYMENT-DISCRIMINATION'],'stage4 OWNED_PIVOT_PROOF sections1-5 equations1-9 only'),
]:
    for cl in json.loads(source(agent,run,'CLAIMS.json').read_text(encoding='utf-8-sig')):
        if cl['claim_id'] in ids:
            reviews.append({'claim_id':cl['claim_id'],'version':cl['version'],
                'original_statement_sha256':cl['statement_sha256'],'reviewer':'A077/account05','scope':scope,
                'verdict':'HOLDS_AT_STATED_SCOPED_LOCATORS','substantive_repair':False,
                'reconstruction':'REVIEW.md; PROOF.md; independent truth constructor, physical edge counts and F2 quadratic restriction census',
                'whole_bundle_acceptance':False})
dump(RUN/'REVIEW.json',reviews)
statement=(
 'For every even k>=2 and integer r>=1 on independent uniform physical bits, let G(s,x)=1-2*1{s=0,x=0}, '
 'H(s)=(-1)^(sum paired s-coordinate products), A=1{r fresh controls all zero}, Gp=1+A(G-1),Hp=1+A(H-1), '
 'and W choose Gp/Hp with one fresh fair selector z. Put a=2^-k,b=2^(-k/2),q=2^-r,c=(1-b+a)/2. '
 'All x,shared,selector,activation influences are respectively qa/2,q(a+1/2)/2,qc,qc, and '
 'I(W)=q[k/4+(k+1)a/2+(r+1)c]. The exact signed private-query correction D=B_x(W)-B_x(Gp)/2 equals '
 'q(2^k-1)S(-a,a;b)+q(1-q)S(-a,a;b-1)+S(1-qa,qa;1-q+qb), '
 'S(u,d;v)=[Phi((u+v)^2,d^2)+Phi((u-v)^2,d^2)]/4-Phi(u^2,d^2)/2. '
 'For even k>=4 its ratio D/Inf_x(W)>=k-4 and Q_x(W)/Inf_x(W)>=k-11/2 uniformly in r. '
 'Taking r=k makes both branch minority probabilities, every root influence and total I(W) tend to zero. '
 'Nevertheless an activation-first complete physical policy has B_tree,Q_tree<=5I(W) and H(W)<8I(W). '
 'Its activation prefix consumes rqc, has B<=4rqc and retains exactly qH(F), including both terminal core entropies; '
 'the surviving base policy consumes qI(F), including final zero-erasure selector influence, at B<=5qI(F). '
 'This refutes a universal prescribed-private-query price under rarity/weak-influence hypotheses, not selected-pivot admission or FEI.'
)
cid='A077-RARE-RARE-ACTIVATED-COLLISION'
deps=[
 {'claim_id':'A078-PAIRED-QUARTER-PROFILE-AND-PADDING','version':2,'scope':'stage3 actual family and private-row obstruction; independently reconstructed scoped HOLDS'},
 {'claim_id':'A076-STRUCTURED-SPECTRA','version':4,'scope':'OWNED_PIVOT_PROOF sections1-4; independently reconstructed scoped HOLDS'},
 {'claim_id':'A076-TRIBES-PAYMENT-DISCRIMINATION','version':4,'scope':'OWNED_PIVOT_PROOF sections2-5 including fixture paid policy; independently reconstructed scoped HOLDS'}
]
claims=[{'claim_id':cid,'version':1,'exact_statement':statement,
 'hypotheses':['Actual Boolean truth formulas above; k even>=2,r integer>=1','Independent uniform physical inputs; entropy bits',
               'Divergence bounds require k even>=4','Activation-first paid policy is explicit; arbitrary interleavings are not priced'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A077/account05'],
 'proof_source':{'proof':'PROOF.md sections1-5','checks':'code/check.py; out/full.json; out/review.json'},
 'proof_dependencies':deps,'review_records':[],'status':'AUTHOR_PROVED_EXACT_CHECKED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':['Uniform prescribed-query |D|<=C Inf for both rare branches with all root influences and total influence tending to zero',
                         'Uniform prescribed-query Q<=C Inf under the same rarity and weak-influence hypotheses'],
 'first_unproved_line':None,
 'next_consumers':['A076','A078','A037','A064','A091','A097','A092','A088','claude/B16','B20']}]
dump(RUN/'CLAIMS.json',claims)
next_action=('Price the weighted bad private-query bill under arbitrary interleaving on the activated bent/spike family '
             'from one unqueried mismatch/selector reserve, using its conserved expected physical influence and retaining both terminal core costs.')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B16','packet_id':'A077',
 'gap_id':'G-R-MISMATCH','attempt_id':'A077-G-R-MISMATCH-04',
 'method':'Scoped independent A078/A076 reconstruction; common rare activation and three-sector exact Phi correction; exclusive activation/core stopping ledger',
 'mathematical_delta':'Both branches and all root influences can become rare with I->0 while D/Inf_x>=k-4 persists; explicit paid activation-first B_tree<=5I with terminal cores retained.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'RARE_RARE_LOCAL_PAYMENT_OBSTRUCTION_PROVED_INTERLEAVED_RESERVE_OPEN',
 'claim_versions_used':deps,'claims_created_or_changed':[cid+'@1','scoped A078@2/A076@4 reviews HOLDS; no whole-bundle acceptance'],
 'source_artifacts':['REPORT.md','PROOF.md','REVIEW.md','REVIEW.json','FROZEN_SPEC.json','REVIEW_FROZEN_SPEC.json',
                     'MULTISCALE_COST_LEDGER.json','code/check.py','code/exact_math.py','out/pilot.json','out/full.json','out/review.json','out/PILOT_CORRECTION.json'],
 'next_consumers':claims[0]['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['New application independent review and remote adoption unverified; arbitrary interleaving and universal terminal-core payment remain open'],
 'packet_ids':['A077']}
dump(RUN/'PROGRESS.json',progress);dump(RUN/'PACKET_DELTA.json',progress)
status=('STATE: A077 stage4 complete: rare/rare activation preserves D/Inf>=k-4 despite all root influences and I->0; paid B_tree<=5I; 10,674 main exact checks; scoped A078/A076 HOLDS; FEI OPEN.\n'
        'NEXT: Pay weighted bad private exposure under arbitrary interleaving from one conserved unqueried-selector reserve; retain both terminal core costs.\n')
(AGENT/'STATUS.md').write_text(status,encoding='utf-8')
entry=('\n2026-10-14 stage4 (20261014T020716Z): Consumed A078 multishared obstruction and A076 derivative-gap policy; no repeated two-bit scan. '
       'Proved common activation preserves D/Inf_x>=k-4 uniformly in activation depth, with both branch biases, all root influences and total I tending to zero at r=k. '
       'Activation-first consumes rqc and retains qH(F); base suffix consumes qI(F), total B_tree<=5I and H<8I. '
       '10,674 main assertions PASS; 3,556 separately frozen quadratic-review assertions PASS (same review cases already in main, not new coverage). '
       'Initial pilot omitted terminal character influence; fixed final zero-erasure z reveal and saved receipt. '
       'Main spec omitted quadratic subdomain; separately froze/reproduced it, original result retained. '
       'Scoped A078 v2 and A076 v4 reviews HOLDS; previous A077 v1 local acceptance observed in A078. NEXT interleaved mismatch reserve; FEI OPEN.\n')
work=AGENT/'WORKLOG.md'
if RUN.name not in work.read_text(encoding='utf-8-sig'):
    with work.open('a',encoding='utf-8') as f:f.write(entry)
learn=AGENT/'LEARNED.md'
durable=('\n## 2026-10-14 rare/rare activated collision\n\n'
 'For the actual commonly activated shared bent/spike selector, with a=2^-k,b=2^(-k/2),q=2^-r,c=(1-b+a)/2, '
 'Inf_x=qa/2 and I=q[k/4+(k+1)a/2+(r+1)c]. The exact three-sector signed correction is '
 'q(2^k-1)S(-a,a;b)+q(1-q)S(-a,a;b-1)+S(1-qa,qa;1-q+qb); D/Inf_x>=k-4 (even k>=4), uniformly in r. '
 'At r=k both branches become rare and every root influence and total I vanish. Minority bias does not replace a paid pivot or terminal reserve.\n\n'
 'Any point activation control has B=Phi((1-j)^2,j^2)+2j(1-j)<=4j. Activation-first uses rqc, retaining qH(base) exactly; '
 'the reconstructed quadratic/point-defect suffix costs at most5qI(base). These accounts are disjoint, with complete B_tree<=5I and H<8I. '
 'This is not an FEI counterexample. A terminal selector character has H=B=JS=0 but nonzero influence, which must still be counted or consumed.\n\n'
 'A078 v2 stage3 equations1,3,4 and A076 v4 OWNED_PIVOT_PROOF equations1-9 were independently reconstructed at those locators; whole bundles are not accepted. '
 'A078 REVIEW_A077 independently accepts our one-shared-bit v1 locally; no shared-index adoption inferred. '
 'Next universal mechanism: price bad private exposure under arbitrary interleaving using one conserved expected unqueried-selector influence account and full terminal costs.\n')
if '## 2026-10-14 rare/rare activated collision' not in learn.read_text(encoding='utf-8-sig'):
    with learn.open('a',encoding='utf-8') as f:f.write(durable)
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8-sig'))
assert set(claims[0])==set(protocol['required_per_run']['claim_fields'])
fields=[x if not x.startswith('packet_ids ') else 'packet_ids' for x in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(fields)
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
manifest=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and '__pycache__' not in p.parts and p.name!='ARTIFACT_MANIFEST.json':
        assert p.stat().st_size<20*1024*1024
        manifest.append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)})
dump(RUN/'out'/'ARTIFACT_MANIFEST.json',manifest)
print(json.dumps({'claim_schema':'PASS','progress_schema':'PASS','compatibility_copy':'PASS',
 'report_fields':'PASS','artifacts':len(manifest),'main_assertions':10674,'separate_review_assertions':3556,'largest_bytes':max(x['bytes'] for x in manifest)}))
