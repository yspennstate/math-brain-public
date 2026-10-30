"""Persist protocol fields and source receipts; all writes stay within A042."""
from pathlib import Path
import hashlib,json,datetime

root=Path(__file__).resolve().parents[1]
agent=root.parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(name,value):
    (root/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
statement=('For every fixed finite Boolean sign table under independent Bernoulli inputs, '
 'the normalized mixed-difference polynomials c_S=2^(-|S|) E Delta_S f give '
 'P(S)=w_S c_S^2, natural corrected entropy E=sum_nonempty w_S c_S^2 ln(1/c_S^2), '
 'and D=I-Var=sum_|S|>=2 (|S|-1)w_S c_S^2, with path-independent deterministic contraction. '
 'For one rare probability e and fixed interior remaining biases, E=E(g)+e K+2e^2 Z ln(1/e)+O(e^2) '
 'and D=D(g)+e L-e^2 Q, with K,Z,L,Q as in REPORT.md. If D(g)=0, either L=Q=0 and E=D=0 identically, '
 'or L>0 and Hplus/D tends to K/(L ln2). Zero-deficit interior Boolean tables are exactly constants '
 'and signed literals; a unit spectral atom after contraction is a signed parity on fair occupied coordinates.')
hyp=['finite genuine Boolean sign table','independent Bernoulli inputs','fixed interior biases on uncontracted coordinates for the one-coordinate Taylor remainder','E uses natural logarithms and Hplus=E/ln2','zero masses contribute zero; do not divide by identically zero D','no dimension-uniform Taylor remainder is asserted']
digest=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
claim={
 'claim_id':'A042-BIAS-ENDPOINT-INTERFACE','version':1,'exact_statement':statement,
 'hypotheses':hyp,'statement_sha256':digest,'contributors':['A042/fleet05'],
 'proof_source':{'run_id':root.name,'path':'REPORT.md','companion':'BIASED_ENDPOINT_SERIES.tex','validation':'out/CHECK_OUTPUT.json'},
 'proof_dependencies':['elementary mixed-difference integration','Parseval','Taylor expansion at nonzero coefficients','full Boolean identity f^2=1'],
 'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A024','A041','A044','A045','A047','A084','A090','A091']}
save('CLAIMS.json',[claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':root.name,'stream':'B09','packet_id':'A042',
 'gap_id':'G-BIASED-LTF','attempt_id':'A042-endpoint-interface-1',
 'method':'mixed-difference polynomial normalization; exact Boolean slice spectra; fixed-table Taylor expansion; compressed weighted-control reconstruction with rational logarithms',
 'mathematical_delta':'Exact closed-bias contraction and analytic-path atom orders; rare-slice entropy has no first-order rare logarithm; quadratic deficit and finite zero-deficit slice limit; all three recovered weighted controls retained with units and ordered limits; m=1 fixed-m exception explicit.',
 'deliverable_status':'COMPLETE_LOCAL_SAVED','mathematical_status':'ENDPOINT_INTERFACE_PROVED_BY_AUTHOR; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':[{'source':'source_material/reductions/paper/biased.tex','locators':['biasfull:mixture','biasfull:weightedcounter','biasfull:andmany','biasfull:localTC'],'role':'recovered controls reconstructed; no new guard claim'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['REPORT.md','BIASED_ENDPOINT_SERIES.tex','WEIGHTED_CONTROL_LIMITS.json','code/check_endpoints.py','out/FROZEN_SPEC.json','out/CHECK_OUTPUT.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'A090/A091 independently reconstruct endpoint interface; A041 compare joint leading monomials at zero-deficit weighted slices when remaining biases also degenerate to test a dimension-independent boundary estimate.',
 'stagnant_substantive_attempts':0,'blockers':[], 'packet_ids':['A042']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
checks=json.loads((root/'out/CHECK_OUTPUT.json').read_text())
save('WEIGHTED_CONTROL_LIMITS.json',{
 'source':'source_material/reductions/paper/biased.tex; REPORT.md section 4 reconstructs the proof',
 'novelty':'recovered controls; no novelty claim',
 'growing_arity':{'domain':'m>=2, q=m^(-2), eta=1/m, r=q^m, q0=(m-1)r/[1+(m-1)r]',
 'corrected_entropy_over_deficit_bits':'2+O((ln m)/m^2)+O(r) -> 2',
 'event_TC_over_spectral_I_nats':'(ln m+1)/8+O((ln m)/m) -> infinity',
 'coefficient_one_pivotal_residual_over_I_nats':'(ln m)/2-ln2+O((ln m)/m) -> infinity',
 'credit_scope':'refutes exactly multiplier one; larger multipliers unsettled'},
 'ordered_local_limit':{'domain':'eta=1/2, q0=q^m/(1+q^m); q->0 at fixed m>=1, then m->infinity',
 'each_coordinate_physical_pair_MI_ratio_nats':'m ln2/2',
 'corrected_entropy_over_deficit_bits':'2 for fixed m>=2; 2+4/ln2 for m=1',
 'uniform_in_m_small_q_remainder':False},
 'finite_certificates':checks['weighted_rational_log_certificates'],
 'full_FEI':'OPEN'})

report=Path(r'~\mop_fei100\reports\fei-2026-10-11')
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
context=Path(r'~\brain_workers\FEI100_20261011\context')
paths=[report/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((supp/'sources').glob('*.md')) + list(context.glob('*.txt'))
paths += [report/'source_material/reductions/paper/biased.tex', Path(r'~\brain_workers\FEI100_20261011\BOARD.md')]
receipts=[]
for path in paths:
    data=path.read_bytes(); content=data.decode('utf-8',errors='replace')
    receipts.append({'path':str(path),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),
     'scope':'Full protocol and biased.tex proof text inspected; remaining mathematical inspection limited to report-listed definitions, packet/guard locators, introductions and source interfaces. Hashing is provenance, not full theorem audit.'})
save('out/SOURCE_RECEIPTS.json',{'at':now,'files':receipts,'lead_notes':'requested claude/B09/STREAM_NOTES.md absent at stage start'})
(agent/'STATUS.md').write_text('STATE: A042 endpoint interface saved; 24,095 exact assertions passed; all three recovered weighted guards preserved; independent review pending; full FEI OPEN.\nNEXT: A090/A091 reconstruct endpoint proof; A041 analyze simultaneous-bias leading monomials for an arity-uniform zero-deficit boundary bound.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+now+' | A042 stage 1: read protocol/board and canonical B09 direction (lead notes absent); derived mixed-difference boundary contraction, exact slice deficit, entropy Taylor and zero/unit endpoints; reconstructed three recovered weighted guards including fixed-m=1 exception. Frozen Fraction/log pilot passed 24,095 assertions in 2.792s. Saved complete local artifacts; review/mirror pending.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n# '+now+' bias endpoint interface\n'
     '- P(S)=w_S c_S^2, c_S=2^(-|S|) E Delta_S f, makes corrected entropy sum w_S c_S^2 ln(1/c_S^2) continuous after deterministic contraction.\n'
     '- One fixed-bias rare slice: E=E(g)+eK+2e^2 Z ln(1/e)+O(e^2); D=D(g)+eL-e^2 Q. No e ln(1/e); empty derivative packet matters. Remainder is not uniform as other coefficients vanish.\n'
     '- D=0 interior means constant/signed literal. If D(g)=L=0 then Q=0 and E=D=0 identically. Unit atom requires fair occupied coordinates and gives parity; higher unit atom has D=degree-1, not zero.\n'
     '- q=m^(-2), eta=1/m guard has Hplus/D=2+O(ln(m)/m^2)+O(q^m), while event TC/I and coefficient-one credit residual diverge. Guard is recovered, not new.\n'
     '- eta=1/2 physical pair-MI obstruction requires q->0 at fixed m before m grows. Hplus/D limit is 2 only for m>=2; m=1 gives 2+4/ln2.\n'
     '- Rational log division must inspect all four corners for signed intervals; exported bounds rounded outward as exact rational text.\n')

manifest=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        data=p.read_bytes(); assert len(data)<20_000_000
        manifest.append({'path':str(p.relative_to(root)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
save('out/PERSISTENCE_RECEIPTS.json',{'at':now,'local_files':manifest,'independent_review':'PENDING','supervisor_copy':'PENDING','brain_ingestion':'PENDING','mirror_verification':'NOT_CLAIMED'})
print(json.dumps({'saved_run':str(root),'claim_count':1,'files':len(manifest),'at':now},indent=2))
