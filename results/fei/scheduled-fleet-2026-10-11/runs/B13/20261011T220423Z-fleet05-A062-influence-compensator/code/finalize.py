"""Save and verify A062 protocol metadata; all writes stay in A062."""
from pathlib import Path
import hashlib,json

run=Path(__file__).resolve().parents[1]
owner=run.parents[1]
protocol_root=Path(r'~\mop_fei100\reports\fei-2026-10-11')
supplement=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
context=Path(r'~\brain_workers\FEI100_20261011\context')
protocol=json.loads((protocol_root/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
def save(name,value):
    (run/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

sources=[]
paths=[protocol_root/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md',
      'CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json',
      'AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex']]
paths += [supplement/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += [supplement/'sources'/x for x in ['ERASURE_REDUCTION.md','BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','LOG_ALLOCATION_CURATED.md']]
paths += list((protocol_root/'runs').rglob('REPORT.md'))
paths += list(context.glob('*.txt'))
paths += [Path(r'~\brain_workers\FEI100_20261011\BOARD.md')]
for p in paths:
    sources.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,
      'scope':'relevant proof passages and statement structure' if p.suffix=='.txt' or p.suffix=='.tex' else 'campaign navigation or read source report'})
save('out/SOURCES.json',sources)

consumers=['A023','A026','A027','A028','A029','A037','A064','A087','A094','B20']
claims=[]
def claim(cid,statement,hypotheses,proof,refutes):
    digest=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,
                                  separators=(',',':')).encode('utf-8')).hexdigest()
    claims.append({'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hypotheses,
      'statement_sha256':digest,'contributors':['A062'],'proof_source':proof,'proof_dependencies':[],
      'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
      'refutes':refutes,'first_unproved_line':None,'next_consumers':consumers})
claim('A062-INFLUENCE-STOPPING-INTERFACE',
      'For every finite uniform-cube Boolean f and every fair adaptive fresh-coordinate/block restriction tree, including independently randomized policies and stopping, I(f)=E sum_{t<tau} I_{A_t}(g_t)+E I(g_tau), and the same physical tree obeys H(f)=E sum_{t<tau} delta_{A_t}(g_t)+E H(g_tau). Each original coordinate separately conserves its expected queried cost plus terminal influence. These identities hold for arbitrary waiting/stopping at fixed dimension by bounded convergence. For a genuinely unbounded nonnegative process with the stated drift and integrable initial budget, cumulative costs are integrable, Fatou gives only the terminal inequality, and uniform integrability of residual influence (separately entropy) suffices for equality.',
      ['Boolean signs on the uniform finite cube for the concrete tree theorem','decisions measurable in independent auxiliary randomness and revealed physical history','selected input coordinates are fresh and unrevealed signs stay fair','entropy in bits; ordinary influence','infinite-time terminal restriction at fixed n is the eventual stabilized restriction','abstract unbounded extension assumes its one-step drift and finite initial expected budget; limit identification is not asserted'],
      ['FAIR_TREE_INFLUENCE_PROCESS.tex','STOPPING_JUSTIFICATION.md','out/CHECK.json'],[])
claim('A062-BOOLEAN-DIMENSION-LIMIT-OBSTRUCTION',
      'There is an actual Boolean activation family F_k=1+A_k(g_k-1), with k fair controls, p_k=2^{-k}, and balanced g_k=y_0 times 2^{k-1} quadratic bent two-bit factors, for which I(F_k)=1/2+(k+1)2^{-k}<=3/2. Stopping after control revelation gives terminal influence (2^{k-1}+1)1_{A_k} and terminal entropy 2^k 1_{A_k}; on coupled infinite fair controls they converge to zero almost surely but their expectations tend to 1/2 and equal 1. Thus bounded root influence does not imply dimension-uniform terminal uniform integrability or allow exchanging these terminal expectations with almost-sure limits. Also an activated two-bit parity has root influence 3/2 and a child of influence 2, so residual influence need not decrease pathwise.',
      ['k is a positive integer','all control/data inputs are independent uniform signs','controls are revealed in order and the tree stops at the first inactive control or after all k controls','entropy is in bits','dimension-limit comparison is across F_k, not unbounded stopping for one fixed finite-dimensional function'],
      ['STOPPING_JUSTIFICATION.md','out/LIMIT_CHECK.json','out/CHECK.json'],
      ['bounded root budgets alone justify terminal expectation exchange across dimension limits','residual physical influence always decreases on each restriction branch'])
save('CLAIMS.json',claims)

progress={'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B13','packet_id':'A062',
 'gap_id':'FEI-B13-A062-INITIAL','attempt_id':'A062-influence-compensator-1',
 'method':'finite conditional drift telescope; per-label budgets; bounded convergence at fixed n; analytic Boolean tail obstruction',
 'mathematical_delta':'Completed recovered influence/stopping baseline locally with exact same-tree entropy and labelled nonreuse; made tail conditions explicit and certified a Boolean dimension-limit obstruction. C019 universal payment remains open.',
 'deliverable_status':'COMPLETE_LOCAL_REVIEW_PENDING','mathematical_status':'BASELINE_INTERFACE_PROVED_LOCAL; FULL_FEI_OPEN',
 'claim_versions_used':[],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':1} for c in claims],
 'source_artifacts':['REPORT.md','FAIR_TREE_INFLUENCE_PROCESS.tex','STOPPING_JUSTIFICATION.md','out/SOURCES.json','out/CHECK.json','out/LIMIT_CHECK.json'],
 'next_consumers':consumers,
 'next_action':'A064: apply labelled terminal reserves to its explicit debt candidate on full B05 control-first and selector-first trees and identify the first unpaid expected logarithmic charge; A087/A094 review this baseline independently.',
 'stagnant_substantive_attempts':0,
 'blockers':['Independent review and supervisor mirror verification pending; B13 STREAM_NOTES.md absent; universal erasure/debt payment unproved.'],
 'packet_ids':['A062']}
save('PROGRESS.json',progress)
save('PACKET_DELTA.json',progress)

required=protocol['required_per_run']
expected_progress={x.split(' (')[0] for x in required['progress_fields']}
assert set(progress)==expected_progress
for c in claims:
    assert set(c)==set(required['claim_fields'])
    digest=hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},
                    sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert c['statement_sha256']==digest
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
report=(run/'REPORT.md').read_text(encoding='utf-8')
for field in required['report_fields']:
    assert '## '+field in report
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
check=json.loads((run/'out/CHECK.json').read_text())
limits=json.loads((run/'out/LIMIT_CHECK.json').read_text())
assert check['failures']==limits['failures']==0
assert check['truth_tables']==278 and check['assertions']==184658
assert limits['assertions']==36
assert check['runtime_seconds']<60 and limits['runtime_seconds']<60
receipts=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json':
        assert p.stat().st_size <20_000_000
        receipts.append({'path':str(p.relative_to(run)),'bytes':p.stat().st_size,'sha256':sha(p)})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    p=owner/name
    receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
assert len((owner/'STATUS.md').read_text().splitlines())==2
save('out/RECEIPTS.json',{'run_id':run.name,'local_saved':True,'independent_review':'PENDING',
     'mirror_verified':False,'schema_checks_passed':True,'files':receipts})
print(json.dumps({'schema_checks_passed':True,'claim_count':len(claims),
      'exact_assertions_passed':check['assertions']+limits['assertions'],
      'receipted_files':len(receipts),'full_fei':'OPEN'},indent=2))
