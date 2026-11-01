"""Narrow archive checks, source bookkeeping, claim rows, and DRAFT preparation."""
from pathlib import Path
import json
import difflib

ROOT=Path('~')
JOB=Path(__file__).resolve().parent
research=ROOT/'<private-repo>/06_math_research'
receipts=[]
for name, line_numbers in [('problems.jsonl',{49,52}),('attempts.jsonl',{43,46})]:
    path=research/'probability_1000_intake_D_20260908'/name
    with path.open(encoding='utf-8-sig') as f:
        for n,line in enumerate(f,1):
            if n in line_numbers:
                row=json.loads(line)
                receipts.append({'path':str(path),'line':n,'record':row})
                print('EXACT_PRIOR_ROW',n,json.dumps(row,ensure_ascii=False)[:4500])
            if n>=max(line_numbers):
                break
(JOB/'PRIOR_RECORDS.json').write_text(json.dumps(receipts,indent=2,ensure_ascii=False),encoding='utf-8')
old=[r['record'] for r in receipts if r['line']==43][0]
assert 'd_gamma = 2Q/xi' in json.dumps(old), 'Prior normalization error not present at the named line.'
verdict_path=JOB/'AUDIT_VERDICTS.jsonl'
verdicts=[json.loads(x) for x in verdict_path.read_text(encoding='utf-8').splitlines()]
for v in verdicts:
    if v['subject']=='P0297.w522.C1':
        v['verdict']='KEEP'
        v['reason']='Direct substitution is correct; the live archived D0049-A001 row at attempts.jsonl line 43 was independently read and contains d_gamma = 2Q/xi. Primary xi=gamma/d_gamma fixes it. Other archived assertions are not audited here.'
        v['source_receipt']='PRIOR_RECORDS.json'
verdict_path.write_text(''.join(json.dumps(v,ensure_ascii=False)+'\n' for v in verdicts),encoding='utf-8')

claim_path=JOB/'CLAIMS.jsonl'
claims=[json.loads(x) for x in claim_path.read_text(encoding='utf-8').splitlines()]
for row in claims:
    if row['id']=='P0297-w523-L1':
        row['source'].pop('quote',None)
        row['source']['expression_context']='Theorem 1.5 for deterministic ambient U=C, and Corollary 1.6; statement here is independently proved algebra.'
    if row['id']=='P0297-w523-S0':
        row['remaining_gap']='Primary exact statement recovered. Completeness of October 2026 openness and owner-retirement checks remains unverified.'
counterclaim={'id':'P0297-w523-C3','statement':'For every fixed gamma in (0,2), the random Borel set X=T_h^gamma of gamma-thick points is an exact counterexample to extending independent-set metric KPZ to all field-dependent random Borel sets: its Euclidean dimension is 2-gamma^2/2 and metric dimension d_gamma, while that extension predicts 2, an error gamma^2/2. At gamma=sqrt(8/3) the error is 4/3.','assumptions':['gamma fixed in (0,2)','h is a whole-plane GFF with fixed additive normalization','D_h is the gamma-LQG metric','xi=gamma/d_gamma','Q=2/gamma+gamma/2','published thick-point dimension theorem and full-dimension corollary'],'source':{'kind':'independent_campaign_route_counterexample','source_id':'owner-own-work:lqg-dependent-kpz-counterexample','license':'owner-own-work','context_url':'https://arxiv.org/html/1905.11790','locators':['Theorem 1.4 independence premise','Equation (1.11) with deterministic ambient U=C','Corollary 1.7'],'quote':'independent from $h$'},'proof_or_counterexample':'ATTEMPT.md: use the two source-backed dimensions on their finite intersection of probability-one events; substitution gives gamma*Q-gamma^2/2=2, contradicting 2-gamma^2/2. This is not an application of independent-set KPZ to the dependent set.','independent_reviewer':'w524 (pending)','remaining_gap':'Independent referee check of the campaign derivation. The original metric normalization exponent is not determined. This does not identify a flaw in the correctly scoped w522 packet.','status':'proved special case','novelty':'not claimed; primary-source consequence'}
if not any(c['id']==counterclaim['id'] for c in claims):
    claims.append(counterclaim)
claim_path.write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')

source={'target':'P0297','title':'Exact Hausdorff dimension of Liouville quantum gravity','checked_on':'2026-10-10','current_openness':'UNKNOWN','exact_statement':'For each fixed gamma in (0,2), determine the deterministic almost-sure Hausdorff dimension d_gamma of (C,D_h), where h is a whole-plane GFF with fixed additive constant and D_h is the gamma-LQG metric, unique up to positive deterministic multiplicative normalization.','known_anchor':{'gamma_squared':'8/3','dimension':4},'original_target_solved':False,'novelty_claim':False,'paired_proof_read':True,'independent_derivation_preceded_paired_proof':True,'independent_artifact':'INDEPENDENT.md','sources':[{'url':'https://arxiv.org/html/2509.21053v1','authors':'Rhodes and Vargas','title':'Two Decades of Probabilistic Approach to Liouville Conformal Field Theory','locator':'Section 3, distance paragraph','checked':'Primary HTML target paragraph and preceding subcritical range; original intake survey.'},{'url':'https://link.springer.com/article/10.1007/s00222-020-00991-6','authors':'Gwynne and Miller','locator':'Problem 7.1; equation (1.5)','checked':'Exact whole-plane formulation, subcritical range, xi=gamma/d_gamma, Brownian anchor.'},{'url':'https://arxiv.org/html/1905.11790','authors':'Gwynne and Pfeffer','locator':'Theorems 1.4-1.5; equation (1.11); Corollaries 1.6-1.7','checked':'Independence premise; positive denominator in subcritical range; gamma-thick subset has Euclidean dimension 2-gamma^2/2 and full metric dimension.'},{'url':'https://arxiv.org/abs/2606.10496','authors':'Bhatia, Gwynne, Harper','posted':'2026-06-09','checked':'Abstract page verified; HTML full text unavailable; dimensional-status passage not independently checked here.'}],'prior_checks':{'ranking':'P0297 dated 2026-09-07, line 554, unsolved then','H_I_attempts':'Scoped P0297 identifier searches returned no rows; title/dedup aliases were not exhaustively searched.','Lean':'Annotated ranking line 604 unsolved; no formal theorem receipt recovered.','D_intake':'D0049 and D0052 related statements and attempts read by exact lines; PRIOR_RECORDS.json. No database-alias mutation.','F_dedup_index':'Targeted JSON-key and exact-value P0297 lookup returned no record.','team_O':'Initial bounded board read did not reach P0297; paired packet reports an open row at line 559, independently check with verify_artifacts.py.','population_store':'Only the two exact P0297 cards copied by w522 were read; no new live-store query performed.','canonical_owner_retirement':'Not independently certified. Current openness remains UNKNOWN.'},'scar':{'recall_timeout_seconds':60,'index_term_hits':0,'fallback_slug':'perceptron_proof_open_gaps_fleet_2026_07_12','lesson':'Arithmetic passes and source checks do not close the hardest proof gap.','receipt':'SCAR_RECALL.json'},'independent_reviewer':'w524; pending for own new C3','formal_checker_receipt':None,'source_or_hash_check_is_a_proof':False,'brain_submission':{'prepared':True,'submitted':False,'reviewed':False,'ingested':False,'retrievable':False},'write_scope':'Research and hooks/progress handoffs staged inside worker folder. Only the task-explicit w523 DRAFT inbox is a separate destination; no live store or global hook mutation.'}
(JOB/'SOURCE_STATUS.json').write_text(json.dumps(source,indent=2,ensure_ascii=False),encoding='utf-8')

source_base={'source_id':'owner-own-work:lqg-dependent-kpz-route-audit','url':'https://arxiv.org/abs/1905.11790','revision':'campaign-derivation-2026-10-10-review-pending','license':'owner-own-work','excerpt':None}
def entry(key,name,title,statement,assumptions):
    return {'key':key,'namespace':'probability.lqg','logical_name':name,'kind':'concept','title':title,'statement':statement,'proof_text':None,'assumptions':assumptions,'domain':'probability theory; random geometry','source':dict(source_base)}
bundle={'spec':'mathbrain-draft-v1','author_agent':'w523','bundle_slug':'lqg-dependent-set-kpz-counterexample-001','entries':[
    entry('thick-dimensions','subcritical-gamma-thick-point-metric-dimension-inputs','Subcritical gamma-thick-point dimensions','DRAFT, independent review pending. Fix gamma in (0,2). Let h be a whole-plane GFF and D_h its gamma-LQG metric, with deterministic dimension d_gamma. Let T_h^gamma={z: lim_{r->0} h_r(z)/log(1/r)=gamma}. For this fixed gamma, almost surely its Euclidean Hausdorff dimension is 2-gamma^2/2 and its D_h-Hausdorff dimension is d_gamma. These are published source inputs: Gwynne-Pfeffer equation (1.11) with deterministic ambient C, and Corollary 1.7. No numerical value of d_gamma is supplied.',['gamma fixed in (0,2)','whole-plane GFF h with fixed additive normalization','D_h is the gamma-LQG metric','published thick-point theorem and Corollary 1.7']),
    entry('false-bridge','refuted-unrestricted-field-dependent-metric-kpz-bridge','Refuted unrestricted metric KPZ bridge','REFUTED AUXILIARY BRIDGE; draft campaign audit pending. Extending the independent-set metric KPZ equality dim_E(X)=xi*Q*dim_D(X)-(xi^2/2)*dim_D(X)^2 to every random Borel set X, with no restriction on dependence on the GFF h, is false. The published exact equality assumes deterministic X or random X independent of h. This failure concerns a proposed extension of a theorem, not the problem of determining the LQG metric dimension.',['gamma fixed in (0,2)','xi=gamma/d_gamma','Q=2/gamma+gamma/2','distinguish Euclidean and metric Hausdorff dimensions']),
    entry('counterexample','gamma-thick-point-counterexample-to-unrestricted-metric-kpz','Gamma-thick-point counterexample to unrestricted metric KPZ','DRAFT source-backed counterexample, independent review pending. For every fixed gamma in (0,2), choose the field-dependent random Borel set X=T_h^gamma. Its Euclidean dimension is 2-gamma^2/2 and metric dimension d_gamma. With xi=gamma/d_gamma and Q=2/gamma+gamma/2, the unrestricted metric KPZ expression instead equals gamma*Q-gamma^2/2=2. The error is exactly gamma^2/2>0, and equals 4/3 at gamma=sqrt(8/3). Retain the published independence premise or use a valid dependent-set theorem. This counterexample does not compute d_gamma and is not a flaw attributed to a proof that already retains the premise.',['gamma fixed in (0,2)','X is the gamma-thick-point set of the same field h','two published dimension inputs in thick-dimensions','xi=gamma/d_gamma','Q=2/gamma+gamma/2'])
], 'relations':[
    {'from_key':'counterexample','to_key':'thick-dimensions','kind':'depends_on','rationale':'The counterexample substitutes the two exact source-backed dimensions of this same field-dependent set.'},
    {'from_key':'counterexample','to_key':'false-bridge','kind':'refutes','rationale':'The proposed equality predicts 2 for the chosen set, differing from its actual Euclidean dimension by gamma^2/2>0.'}
], 'review_state':'unreviewed concept-only DRAFT; assigned referee pending'}
(JOB/'bundle_local_001.json').write_text(json.dumps(bundle,indent=2,ensure_ascii=False),encoding='utf-8')

hook={'id':'lqg-dependent-kpz-w523-01','area':'math','event':'stage-start','cue':'Applying exact independent-set metric KPZ to an h-selected random set without a separate independence or dependent-set theorem','fire_when':'Unrestricted KPZ applied to X=T_h^gamma predicts Euclidean dimension 2 instead of 2-gamma^2/2.','silent_when':'Use metric KPZ on a deterministic set or a random set sampled independently of h; or use the dedicated thick-point theorem with deterministic ambient set.','text':'Before applying exact metric KPZ, check how the set was chosen. Gamma-thick points depend on h: independent-set KPZ gives 2, but their Euclidean dimension is 2-gamma^2/2. Use the dedicated thick-point theorem or a valid dependence argument.','evidence':'ATTEMPT.md C3; CLAIMS.jsonl P0297-w523-C3; MEASUREMENTS.json dependent_set_bridge; Gwynne-Pfeffer Theorem 1.4, equation (1.11), Corollary 1.7','proposer':'w523'}
assert len(hook['text'])<=300
hook_text=json.dumps(hook,ensure_ascii=False)+'\n'
(JOB/'HOOK_PROPOSAL.jsonl').write_text(hook_text,encoding='utf-8')
patches=JOB/'patches'
patches.mkdir(exist_ok=True)
target='~/primary_directive/hooks1000/proposals/lqg-dependent-kpz-w523.jsonl'
diff=''.join(difflib.unified_diff([],hook_text.splitlines(keepends=True),fromfile='a/'+target,tofile='b/'+target))
(patches/'01_lqg_dependent_kpz_guard.diff').write_text(diff,encoding='utf-8')
event={'agent':'w523','row':'S1.P0297.w523.C3','event':'Saved five independent P0297 prover audit verdicts and a gamma-thick-point counterexample to unrestricted metric KPZ; concept draft awaiting referee.','evidence':str(JOB/'REVIEW_PACKET.md'),'state':'prepared; not posted outside worker folder'}
(JOB/'PROGRESS_EVENT.json').write_text(json.dumps(event,indent=2),encoding='utf-8')
for who in ['w522','w524']:
    handoff={'to':who,'from':'w523','target':'P0297','status':'file handoff; mesh team delivery unavailable','review_packet':str(JOB/'REVIEW_PACKET.md'),'independent_artifact':str(JOB/'INDEPENDENT.md'),'audit_verdicts':str(JOB/'AUDIT_VERDICTS.jsonl'),'own_new_claim':'P0297-w523-C3; exact gamma-thick-point counterexample to unrestricted dependent-set metric KPZ; w524 independent check requested','request':'Keep L1-L4 and C1 within their algebraic scope; do not mark the original target solved. Review C3 before theorem promotion.'}
    (JOB/f'HANDOFF_{who.upper()}.json').write_text(json.dumps(handoff,indent=2),encoding='utf-8')
print('Prepared: 5 finalized audit rows, C3 claim, 3 concept entries, 2 exact supporting relations, 1 staged hook, 2 file handoffs.')
