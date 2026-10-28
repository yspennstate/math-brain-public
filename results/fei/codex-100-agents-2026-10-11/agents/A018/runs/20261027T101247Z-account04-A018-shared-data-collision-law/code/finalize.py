from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,subprocess,sys

run=Path(__file__).resolve().parents[1];base=run.parents[1]
mesh=Path(r'~\<private-repo>\12_cognitive_architecture\agent_mesh\agent_mesh.py')
subprocess.run([sys.executable,'-X','utf8',str(mesh),'assert','--agent','codex-01a17cd9','--resource',str(base)],check=True)
def read(p):return Path(p).read_text(encoding='utf-8')
def write(p,s):Path(p).write_text(s,encoding='utf-8',newline='\n')
def js(p,x):write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
main=json.loads(read(run/'out/CHECKS.json'));audit=json.loads(read(run/'out/AUDIT.json'));ghost=json.loads(read(run/'out/GHOST_GUARD.json'))
assert all(x['status']=='PASS' for x in [main,audit,ghost])
assert sum(main['counts'].values())==audit['records']==2430
assert 31**31>2**152
report=read(run/'REPORT.md')
for k,v in {'AUDIT_CHECKS':audit['checks'],'AUDIT_SECONDS':round(audit['seconds'],3),
            'GHOST_CHECKS':ghost['checks'],'GHOST_SECONDS':round(ghost['seconds'],3)}.items():
    report=report.replace('{{'+k+'}}',str(v))
assert '{{' not in report
write(run/'REPORT.md',report)

campaign=Path(r'math-open-problems/reports\fei-2026-10-11')
supp=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
team=Path(r'~\brain_workers\FEI100_20261011')
sources=[campaign/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
sources +=[supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
sources +=[p for p in (supp/'sources').rglob('*') if p.is_file() and p.suffix in ['.md','.tex','.txt','.json']]
sources +=list((team/'context').glob('*.txt'))
sources +=[team/'BOARD.md',team/'claude/B04/STREAM_NOTES.md',base/'LEARNED.md',base/'WORKLOG.md']
sources +=[p for p in (base/'runs').glob('*/REPORT.md') if p.parent!=run]
for name in ['A016','A019','A020']:
    p=sorted(p for p in (team/'agents'/name/'runs').iterdir() if (p/'REPORT.md').exists())[-1]
    sources +=[p/'REPORT.md',p/'CLAIMS.json']
sources +=[Path(r'~\AGENTS.md'),Path(r'~\<private-repo>\12_cognitive_architecture\scheduled_tasks\README.md')]
receipts=[]
for p in sources:
    b=p.read_bytes()
    try:
        s=b.decode('utf-8-sig');decoding='UTF8'
    except UnicodeDecodeError:
        s=b.decode('latin-1');decoding='LATIN1_LOSSLESS_BYTE_MAPPING; UTF8 invalid; navigation only, no new paper theorem premise'
    receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
                     'relevant_lines':[i+1 for i,l in enumerate(s.splitlines()) if any(t in l for t in ['Proposition 8.6','UNBOUNDED-MIXED','Ghost','ghost budget','FULL-FEI-ONLY'])][:12],
                     'text_decoding':decoding,
                     'scope':'source bytes read; only dependencies named in REPORT reconstructed'})
js(run/'out/SOURCE_RECEIPTS.json',receipts)

statement=('For every finite r>=2, W_r(a,b_1,c_1,...,b_r,c_r)=product_j g3(a,b_j,c_j), g3=-1 only at000, '
 'has CE(P_clean,R_original_marginal)<=4I after EVERY partial physical assignment and erasure of ALL remaining irrelevant coordinates; '
 'R is the original squared spectrum projected to actual essential coordinates, never a child reset. '
 'The exact all-width original reference formulas and complete case proof are in REPORT sections1-2. '
 'For arbitrary finite r_l>=2,j>=5,k>=5 these sources tensor across disjoint blocks and enter the ORIGINAL balanced hierarchy '
 'of A019-UNBOUNDED-MIXED-ADAPTIVE-CLEANED-FRONTIER@1 with unchanged literal U and Q_F: initial4I-CE>19/8 and '
 'EVERY finite adaptive mixed padding/source policy with compulsory source cleanup, both q signs and all outcomes retained, '
 'has expected complete terminal reserve>11/8-(2k+7)2^-k>=27/32. '
 'For the SAME single W_r, a=0, first pair free, b_j=1 and c_j unqueried for j>=2 gives I=1, '
 'CE_unclean=log2(2/(1+2^(-r-1)))/4+3(r+2)/4 and ghost excess>3(r-1)/4. '
 'Thus no universal constant per connected block bounds its ghost invoice; CE_unclean>4I for r>=4. '
 'At r4 the supported original-reference masses33/64,1/64,1/64,1/64 give the exact sign33<256. '
 'The particular a=1 ghost invoice remains log2(2/(1+4^-r))<1. '
 'These are cleaned source/terminal-functional results, not arbitrary-core suppliers or accumulated query-KL transaction payment; full FEI stays open.')
hyp=['Uniform independent physical0/1 bits; shared a is ONE coordinate, private pairs disjoint.',
     'Complete source reference is the fixed ORIGINAL squared spectrum projected to actual essential coordinates, all ghosts removed for the positive contract.',
     'Tensorization only BETWEEN physically disjoint W blocks; arbitrary width allowed within each block.',
     'Balanced hierarchy, U,Lq,Econv,mask and normalized original QF exactly as displayed in REPORT; no renewal,discarded sibling,or retired-influence recredit.',
     'For the application k>=5,j>=5,r_l>=2; finite adaptive physical partitions, compulsory source cleanup; u,mask,gate unqueried.',
     'Negative ghost assertion uses the displayed uncleaned actual restriction and its normalized original marginal; it is not an FEI counterexample.']
def digest(s,h):return hashlib.sha256(json.dumps({'exact_statement':s,'hypotheses':h},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
claim={'claim_id':'A018-GROWING-SHARED-COORDINATE-ORIGINAL-SOURCE','version':1,'exact_statement':statement,'hypotheses':hyp,
       'statement_sha256':digest(statement,hyp),'contributors':['A018/account04'],
       'proof_source':['REPORT.md','code/check_windmill.py','code/audit_certificates.py','code/ghost_guard.py','out/SOURCE_CERTIFICATES.json','out/CHECKS.json','out/AUDIT.json','out/GHOST_GUARD.json'],
       'proof_dependencies':[{'claim_id':'A019-UNBOUNDED-MIXED-ADAPTIVE-CLEANED-FRONTIER','version':1,'statement_sha256':'82362ae124b321eb8385a001db6c1a1f2d8f0f27790ef372e69c77d22e8b124f','scope':'Application only; general-source clause reconstructed from displayed formulas; source contract proved directly here'}],
       'review_records':[],'status':'ANALYTIC_PROOF_EXACT_CHECKED_INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[],
       'first_unproved_line':None,'next_consumers':['A016','A019','A020','A094','B04-lead','B20']}
review_statement=('The finite cleaned-E source contract ONLY in A016-ADAPTIVE-OVERLAPPING-BLOCK-CLEANUP-AND-PADDING-CONTINUATION@1 '
                  'HOLDS unchanged: all243 labelled physical partial assignments of E=g3(a,b,c)g3(a,d,e) satisfy '
                  'CE(P_clean,R_original_marginal)<=4I. This is a scoped independent reconstruction, not acceptance of its other clauses.')
review_hyp=['Exactly the finite r2 cleaned source contract of the named unchanged source.']
review={'claim_id':'A018-REVIEW-A016-CLEANED-E-SOURCE','version':1,'exact_statement':review_statement,'hypotheses':review_hyp,
        'statement_sha256':digest(review_statement,review_hyp),'contributors':['A018/account04'],
        'proof_source':['code/check_windmill.py','code/audit_certificates.py','out/SOURCE_CERTIFICATES.json','out/AUDIT.json'],
        'proof_dependencies':[],'review_records':[{'reviewer':'A018/account04','independent':True,'verdict':'HOLDS_UNCHANGED_SCOPED',
        'source_claim':'A016-ADAPTIVE-OVERLAPPING-BLOCK-CLEANUP-AND-PADDING-CONTINUATION@1',
        'source_statement_sha256':'0eaa3c94b8d1672d90f21b6f6976f816d0ffe42a631901a05a92ccd872a8a8cd',
        'scope':'Finite243-assignment cleaned-E source contract ONLY','substantive_repair':False,
        'method':'Own physical truth,edge,Walsh code plus direct-character independent representation; no author-checker imports'}],
        'status':'INDEPENDENT_RECONSTRUCTION_HOLDS_SCOPED','supersedes':[],'refutes':[],'first_unproved_line':None,
        'next_consumers':['A016','A019','A020','B04-lead','B20']}
claims=[claim,review];js(run/'CLAIMS.json',claims)
next_action='A016/A019/A020 audit all-width source formula,t1 cases,and unbounded within-block ghost invoice; then price a TWO-shared-selector coupled source from SAME original account, with actual cleanup and query-KL scope explicit.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run.name,'stream':'B04','packet_id':'A018','gap_id':'G-LOWSEL-COLLISION',
 'attempt_id':'A018-stage22-growing-connected-original-source','method':'All-cylinder analytic original-spectrum projection and scalar code bounds; exact physical certificates and independent direct-character audit; adverse ghost family.',
 'mathematical_delta':'ALL widths r>=2 satisfy rate4 cleaned ORIGINAL source contract; gives arbitrary mixed cleaned terminal reserve>27/32 for tensor products of arbitrary widths. ONE connected uncleaned block has I=1 and ghost invoice>3(r-1)/4; per-block uniform ghost payment FALSE.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_ANALYTIC_PROOF_EXACT_CHECKED; NEW_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':['A019-UNBOUNDED-MIXED-ADAPTIVE-CLEANED-FRONTIER@1','A016-ADAPTIVE-OVERLAPPING-BLOCK-CLEANUP-AND-PADDING-CONTINUATION@1 (finite-source review only)'],
 'claims_created_or_changed':[c['claim_id']+'@1' for c in claims],
 'source_artifacts':['REPORT.md','CLAIMS.json','out/FROZEN_SPEC.json','out/AUDIT_FROZEN_SPEC.json','out/GHOST_FROZEN_SPEC.json','out/CHECKS.json','out/AUDIT.json','out/GHOST_GUARD.json','out/SOURCE_CERTIFICATES.json','out/SOURCE_RECEIPTS.json','out/LEAN_DISPOSITION.json'],
 'next_consumers':['A016','A019','A020','A094','B04-lead','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['General indecomposable Boolean ORIGINAL source supplier unpaid; star separation is a real hypothesis.',
             'Accumulated physical-query KL transaction payment not established; conclusion is complete terminal functional.',
             'Independent acceptance,registry adoption,supervisor copying and remote mirror unverified.',
             'Lean compile not admitted: fresh memok exit1. Brain identity/dream notes stale and unused.'],
 'packet_ids':['A018']}
js(run/'PROGRESS.json',progress);write(run/'PACKET_DELTA.json',read(run/'PROGRESS.json'))
total=main['checks']+audit['checks']+ghost['checks']
stamp=datetime.now(timezone.utc).isoformat()
write(base/'STATUS.md',f'STATE: A018 stage22 saved: ALL-width shared-coordinate ORIGINAL clean-source CE<=4I; SAME mixed terminal reserve>27/32; connected-block ghost invoice unbounded; {total} exact checks PASS; FEI OPEN,review pending.\nNEXT: {next_action}\n')
lesson=(f'\n\n## {stamp} stage22/account04\n'
 'For every r>=2,W_r=product g3(a,b_j,c_j) has CE(P_clean,R_original_projected)<=4I at EVERY physical cylinder. '
 'When a survives and d private bits remain,R(e,empty)=(1+(-1)^e*2^(1-r)+2^-d)/4; nonempty rows2^(-d-2). '
 'When a is removed,R=delta0/2+U_d/2. Use ORIGINAL mu=2^-r; branch mean b is different. '
 'The a0 branch consists only of signed g2 factors,literals,constants; t>=2 uses empty floors1/8,t1 needs45/16<3 and53/16<5; constants cleaned to mass1. '
 'Therefore arbitrary finite widths enter A019 same-original balanced mixed CLEANED frontier with reserve>27/32 and root>19/8,all outcomes/old U. '
 'Terminal-functional scope does not pay an additional accumulated query-KL transaction. '
 'At a1,ghost invoice log2(2/(1+4^-r))<1 despite2r ghosts. But at a0,first pair live,b_j=1,c_j ghost forj>=2, '
 'I=1 and CEunclean=log2(2/(1+2^(-r-1)))/4+3(r+2)/4; cleanup invoice>3(r-1)/4. '
 'So NO constant per connected block controls all ghosts; r4 exact witness33<256 disproves uncleaned rate4. '
 f'Main28702+audit19160+guard{ghost["checks"]}={total} exact assertions PASS;pilot excluded. '
 'Finite243-state A016 source clause independently HOLDS only at that scope. New all-width theorem pending review. '
 'Next two shared selectors with coupled private branches and actual cleanup price; no more closed E-family query-count tests.\n')
if 'stage22/account04' not in read(base/'LEARNED.md'):
    with (base/'LEARNED.md').open('ab') as f:f.write(lesson.encode('utf-8'))
log=(f'\n{stamp} | Stage22/account04: board consumes saved repeated-seed NEXT; newer A019/A016/A020 already handle mixed cleaned histories. '
 'Changed to growing connected ORIGINAL source supplier. Proved all-r cleaned rate4 contract; same balanced owner application retains>27/32. '
 'Adversarial cleanup test found linear within-ONE-block ghost debt with I1; exact r4 sign33<256. '
 f'{total} exact main/audit/guard checks PASS,plus2471 pilot. '
 'Lean admission refused,no compiler. Required files/rolling state saved; no other work stopped or detached jobs; FEI OPEN,new review/mirror pending.\n')
if 'Stage22/account04:' not in read(base/'WORKLOG.md'):
    with (base/'WORKLOG.md').open('ab') as f:f.write(log.encode('utf-8'))
protocol=json.loads(read(campaign/'EXECUTION_PROTOCOL.json'))
expected=set(protocol['required_per_run']['claim_fields'])
assert all(set(c)==expected and c['statement_sha256']==digest(c['exact_statement'],c['hypotheses']) for c in claims)
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert len(read(base/'STATUS.md').splitlines())==2
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
manifest=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        b=p.read_bytes();assert len(b)<20*1024*1024
        manifest.append({'path':str(p.relative_to(run)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
js(run/'out/PERSISTENCE_RECEIPTS.json',{'timestamp':stamp,'exact_claim_fields':True,'exact_progress_fields':True,
    'statement_hash_recipe':'sha256 compact sorted JSON {exact_statement,hypotheses},utf8 ensure_ascii=False',
    'progress_delta_byte_identical':True,'status_two_lines':True,'total_exact_checks_excluding_pilot':total,
    'files':manifest,'independent_review':'new theorem pending; finite A016 source reviewed only',
    'remote_mirror':'unverified; supervisor route','no_existing_work_stopped':True,'no_detached_job_started':True})
print(json.dumps({'status':'SAVED_VALIDATED','checks':total,'claims':len(claims),'files':len(manifest),'run':str(run)}))
