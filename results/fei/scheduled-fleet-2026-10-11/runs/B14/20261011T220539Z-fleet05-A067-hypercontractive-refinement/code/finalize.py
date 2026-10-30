import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

root=Path(__file__).resolve().parents[1]
agent=root.parents[1]
campaign=Path(r'~\mop_fei100\reports\fei-2026-10-11')
supplement=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
context=Path(r'~\brain_workers\FEI100_20261011\context')
a066=agent.parent/'A066'/'runs'/'20261011T214539Z-fleet05-A066-semigroup-dissipation'
protocol=json.loads((campaign/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))

def save(path,value):
    path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

source_files=[campaign/name for name in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex']]
source_files += list((campaign/'runs').rglob('REPORT.md'))
source_files += [supplement/name for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
source_files += list((supplement/'sources').glob('*.md'))
source_files += list(context.glob('*.txt'))
source_files += [agent.parent.parent/'BOARD.md',a066/'DERIVATION.md',a066/'CLAIMS.json']
save(root/'SOURCE_MANIFEST.json',{'generated_utc':datetime.now(timezone.utc).isoformat(),'sources':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in source_files if p.exists()],'missing_inputs':[str(agent.parent.parent/'claude'/'B14'/'STREAM_NOTES.md')],'reading_scope':'Protocol complete; current state/navigation and packet contracts; source excerpts and theorem locators as stated in REPORT.md. Hash inventory is provenance, not a claim of end-to-end review of every source note.'})

claims=[]
for original in json.loads((a066/'CLAIMS.json').read_text(encoding='utf-8')):
    item=copy.deepcopy(original)
    item['review_records'].append({'reviewer':'A067','verdict':'ACCEPT_AT_STATED_SCOPE','proof_source':str(root/'REVIEW_A066.md'),'method':'Independent finite-sum integration; direct binomial derivative; different dimension selection n=ceil(1/(2t))+1; source-bound analytic reconstruction, not coauthorship','reviewer_conflict':False,'shared_registry_adoption':'PENDING_B20'})
    item['status']='AUTHOR_PROVED_INDEPENDENTLY_REVIEWED_LOCAL_RECEIPT'
    claims.append(item)

common_hypotheses=['Every finite-dimensional uniform cube','Boolean outputs in {-1,1}','Entropy and logarithmic constants in bits','Zero Fourier masses omitted; constants handled explicitly']

def new_claim(identity,statement,refutes):
    item={'claim_id':identity,'version':1,'exact_statement':statement,'hypotheses':common_hypotheses,'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':common_hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),'contributors':['fleet05/A067'],'proof_source':str(root/'DERIVATION.md'),'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':refutes,'first_unproved_line':None,'next_consumers':['A070','A088','A094','B06','B13','B20']}
    claims.append(item)

new_claim('A067-LOCAL-BOOLEAN-GRANULARITY',
 'For every Boolean sign f on a finite uniform cube, write q_S=hat f(S)^2, v=1-q_empty and I=sum_S |S|q_S. For each nonzero nonempty coefficient define d_f(S)=max{|T|:T contains S and q_T>0}, and U=sum_nonempty q_S(d_f(S)-|S|). Then hat f(S) is a multiple of 2^(1-d_f(S)) and H(f)<=2I+2U-(2-log2(e))v. Thus U<=KI implies H<=(2+2K)I, and d_f(S)<=L|S| implies H<=2LI-(2-log2(e))v. Balanced support antichains give H<=2I-2. On ordinary addressing with a address variables, d_f(S)=a+1, U=a/2, and the bound gives exactly H<=2a, while generic full-cube level counting costs Theta(a^2). These are structural-regime results, not a universal payment of U or a novelty claim.',[])
new_claim('A067-MAXIMAL-SUPPORT-ENVELOPE-NOGO',
 'No universal finite K can bound the preceding U(f) by K I(f). For p=2^(-n), n>=2, the actual Boolean dictator surgery g_n=x_1-2 indicator{x=all +} has I=1+(2n-4)p and U=n-1-(2n-4)p-4np^2, so U/I diverges. Further define the valid entropy envelope E_A=(log2(e))(1-hat f(A)^2)+2 sum_nonempty_R hat(f chi_A)(R)^2(d_(f chi_A)(R)-1) for every character anchor A. On F_n=Maj_3(z)*(1-2 indicator{y=all +}), with disjoint three-variable z and n-variable y, every E_A>=3n/2, although I(F_n)=3/2+2n2^(-n)<=5/2 and H(F_n)=2+o(1). Hence min_A E_A<=K I is false universally, including anchors outside the Fourier support. These are helper refutations, not FEI counterexamples.',
 ['Universal U(f)<=K I(f) for a dimension-independent finite K','Universal min_A E_A(f)<=K I(f) for a dimension-independent finite K'])

for item in claims:
    assert set(item)==set(protocol['required_per_run']['claim_fields'])
save(root/'CLAIMS.json',claims)

progress={'protocol_revision':protocol['revision'],'run_id':root.name,'stream':'B14','packet_id':'A067','gap_id':'FEI-B14-A067-INITIAL','attempt_id':'A067-stage1-local-granularity','method':'Integer-valued mixed derivatives; local superset degree; exact Boolean spectra; single-anchor and tensor guards; independent analytic A066 review','mathematical_delta':'Boolean coefficient-local entropy bound H<=2I+2U-(2-log2(e))Var closes U<=KI regime; addressing separates the generic level count by a factor Theta(a). Universal U and optimized single-character arithmetic-envelope payments are refuted. A066 dependency chain independently reviewed. Full FEI remains open.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT_REVIEW_AND_COPY_PENDING','mathematical_status':'PROVED_REGIME_AND_HELPER_REFUTATIONS_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'use':'INDEPENDENT_REVIEW_ONLY_NOT_A_PREMISE_OF_NEW_REGIME'} for c in claims[:2]],'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status']} for c in claims],'source_artifacts':['DERIVATION.md','BOOLEAN_HYPERCONTRACTIVE_REFINEMENT.tex','REGIME_COMPARISON.md','REVIEW_A066.md','SOURCE_MANIFEST.json','FROZEN_SPEC.json','FROZEN_SPEC_FACTORIZED.json','FROZEN_SPEC_ADDRESS.json','out/check_pilot.json','out/check_n4.json','out/check_families_factorized.json','out/check_address.json','out/DIRECT_FAMILY_LIMIT.md'],'next_consumers':['A070','A088','A094','B06','B13','B20'],'next_action':'Independently review the local granularity proof and all-anchor tensor obstruction; then replace maximal support degree by a tail-stable arithmetic charge or a fully paid partition, starting with Maj3 tensor point defect. Do not reopen raw or single-anchor maximal-support payment.','stagnant_substantive_attempts':0,'blockers':['Full-FEI access-tree/partition and tail-stable charge remain unproved','B14 lead notes absent','A067 new claims independent review pending','Shared registry adoption and supervisor GitHub/brain copying not verified'],'packet_ids':['A067']}
# The protocol's last list item annotates packet_ids in prose; the user
# explicitly requires the actual JSON key packet_ids (not that annotation).
progress_keys={field.split(' (',1)[0] for field in protocol['required_per_run']['progress_fields']}
assert set(progress)==progress_keys
save(root/'PROGRESS.json',progress)
save(root/'PACKET_DELTA.json',progress)
assert (root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes()

checks={}
for name in ['pilot','n4','families_factorized','address']:
    result=json.loads((root/'out'/('check_'+name+'.json')).read_text(encoding='utf-8'))
    assert result['complete']
    checks[name]={k:result[k] for k in ['assertions','elapsed_seconds']}
save(root/'out'/'VALIDATION_SUMMARY.json',{'checks':checks,'total_exact_assertions':sum(v['assertions'] for v in checks.values()),'direct_family_attempt':'Runtime limit exception retained, no result counted','logarithmic_inequalities':'Analytic proof; no floating logarithm certificate claimed','independent_review':'A066 dependency chain reviewed analytically; A067 claims pending'})

(agent/'STATUS.md').write_text('STATE: A067 stage complete locally: Boolean local-granularity regime and two helper no-gos proved; exact checks passed; A066 independently reviewed; full FEI OPEN.\nNEXT: A088/A094 review; A070 pursue a tail-stable arithmetic or fully paid partition charge on Maj3 tensor point defect, retaining C019 terminal entropy.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('2026-10-12: Completed 65,814-table exhaustive integer checks through n=4. Direct all-anchor family job exceeded its 60-second frozen limit; guard placement recorded as inadequate. Exact product-factorized replacement verified all 4,064 anchors in 0.4993 s. Corrected a mistaken level-count comparison on point defects; level counting is tight there, whereas addressing gives the strict Theta(a) gain. Saved source-bound A066 independent review, both requested deliverables and all protocol files; new claims review and supervisor copying pending.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nPoint-defect within-level spectra are uniform, so generic level counting is tight; only marginal counting loses a factor n there. For the existing addressing baseline, local upper degree a+1 and U=a/2 give the exact 2a entropy bound, versus Theta(a^2) generic level counting. Keep a runtime guard inside the anchor loop; exact product-support factorization avoids redundant full transforms without dropping anchors.\n')

receipts=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json' and '__pycache__' not in str(p):
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(root/'out'/'ARTIFACT_RECEIPTS.json',{'generated_utc':datetime.now(timezone.utc).isoformat(),'files':receipts,'local_save':'VERIFIED_BYTE_READBACK','supervisor_copy':'PENDING_NOT_CLAIMED'})
print(json.dumps({'saved_claims':len(claims),'new_pending_candidates':2,'reviewed_a066_candidates':2,'total_exact_assertions':sum(v['assertions'] for v in checks.values()),'receipted_artifacts':len(receipts),'schema_fields':'MATCH_PROTOCOL_EXACTLY'},indent=2))
