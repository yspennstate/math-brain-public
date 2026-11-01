"""Persist protocol-exact ledgers and SHA256 receipts; no external writes."""
from pathlib import Path
import hashlib, json

ROOT=Path(__file__).resolve().parents[3]
RUN=Path(__file__).resolve().parents[1]
PROTOCOL_PATH=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(PROTOCOL_PATH.read_text(encoding='utf-8'))
def save(p,value):
    p.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def receipt(p):
    data=p.read_bytes()
    return {'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

statement=('For every uniform Boolean OR of gates each combining at most M regular functions, '
 'the disjoint least-pivotal-gate derivative partition defines normalized laws nu_j and rho_j. '
 'For every kappa_j>=1, epsilon_j=sum_T(nu_j(T)-kappa_j*rho_j(T))_+, '
 'E_nu_j G_j <= E0+(24/5)log2(M*kappa_j)+epsilon_j*Gmax_j, '
 'where E0=(24/5)[log2(sqrt(2e)+2^(3/5))+log2 e]. '
 'For the source-component forest with global root odds lambda*pi_l, 0<lambda<=1, '
 'the explicit congestion Gamma in REPORT equation (2) yields '
 'H(f)<=[K0+E0+(29/5)log2 M+Gamma]I(f), with every root/label/subset/normalization cost retained. '
 'Addressing on a selectors has read 2^a, kappa_j<=2, epsilon_j=0, '
 'Gamma<3/4+24/5 and H<=50I for all integers a>=1; this is a known class calibration. '
 'For the projective-plane line union over any prime q with delta_q=(q^2+q)2^(-q)<1, '
 'worst-event derivative congestion is at least (q+1)(1-delta_q)^2, hence is unbounded. '
 'Least-gate masses lie between 2^(-q)(1-delta_q) and 2^(-q). '
 'More generally, ideal pieces with disjoint Fourier supports outside E certify '
 'epsilon_j(4)<=nu_j(E)+(4*sum_l||a_l-d_jl||_2^2+2*||sum_l(a_l-d_jl)||_2^2)/alpha_j. '
 'On PP_q this gives epsilon_j(4)*Gmax_j<=308/5 for every prime q, '
 'and sum_j alpha_j E_nu_j G_j<93 I(PP_q). '
 'The complete PP root/label/subset payment and universal FEI remain open.')
claim={
 'claim_id':'A014-INTERFERENCE-COMPLETE-CRITERION-AND-PP-GUARD','version':1,
 'exact_statement':statement,
 'hypotheses':['Uniform finite cube; Boolean +/-1 output; OR of nonconstant structured gates',
 'Each outer gate combines at most M regular functions; source signed rank and rarity tails',
 'Disjoint physical least-pivotal-gate derivative pieces; zero pieces omitted',
 'Bits; 0<lambda<=1; deterministic minimizing assignment and source-component forest',
 'The PP infinite family is restricted to prime q, sufficient for unbounded read'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),
 'contributors':['A014'],
 'proof_source':{'path':str(RUN/'REPORT.md'),'sha256':receipt(RUN/'REPORT.md')['sha256'],
 'locators':['derivation sections 1-5','equations (1)-(13)']},
 'proof_dependencies':[{'claim_id':'C003','version':'published Section 5 source',
 'scope_used':'Signed rank/rarity piece tails and finite queue construction, not an assumed refined congestion bound',
 'source':r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents\baseline\current-threshold-paper.tex',
 'locators':['lem:ranktail','union:rare','union:normalizer','union:K0','union:Gtail']}],
 'review_records':[], 'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],
 'refutes':[{'statement':'Worst-event kappa_j is bounded independently of q for PP_q',
             'source':'B03 STREAM_NOTES v1 proposed helper, not a previously accepted theorem',
             'witness':'PP_q over primes q, empty residual Fourier event; REPORT (6)-(7)'}],
 'first_unproved_line':None,
 'next_consumers':['B03 Claude lead','A006','A009','A086','A094','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save(RUN/'CLAIMS.json',[claim])

progress={
 'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B03','packet_id':'A014',
 'gap_id':'G-J-COST','attempt_id':'A014-interference-1',
 'method':'Normalized incoherent-law tail; positive spectral excess; ideal-piece L2 repair; orthogonal blocks; complete queue witness; exact Walsh/Fraction tests',
 'mathematical_delta':'Proved interference-with-exception lemma and complete all-cost congestion criterion. Addressing gives bounded Gamma with unbounded read, as a known-class calibration. PP_q worst-event kappa disproved and repaired: ideal private-block L2 certificate pays epsilon(4)*Gmax<=308/5 and total rank/rarity <93I for every prime q. Least-gate equal-mass premise corrected; PP2/PP3 exactly checked.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT_REVIEW_PENDING',
 'mathematical_status':'SCOPED_THEOREM_PROVED_PACKET_AND_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'C003','version':'published Section 5 signed tails and queue'},
                        {'source':'B03 STREAM_NOTES','version':1,'role':'direction only; PP helper rejected, not a proof dependency'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['REPORT.md','CLAIMS.json','FROZEN_SPEC.json','L2_FROZEN_SPEC.json',
                     'code/check.py','code/l2_check.py','code/finalize.py',
                     'out/pilot.json','out/check.json','out/l2_check.json','out/receipts.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'A086/A094 reconstruct the general L2 perturbation proof and all-prime PP rank payment. Consume lead root/label/subset payment on the same minimizing assignment and fixed reference, then substitute unconditional rank <93I to finish the complete PP overlap theorem.',
 'stagnant_substantive_attempts':0,
 'blockers':['No independent review of this version yet',
             'Complete PP root/label/subset payment on the same fixed reference is not yet consumed',
             'Supervisor persistence/mirror ingestion and downstream adoption not observed'],
 'packet_ids':['A014']}
# The protocol list annotates its final field as
# "packet_ids (one primary ID, for compatibility)"; compatibility specifies
# the actual JSON key packet_ids. Strip this descriptive parenthesis only.
expected_progress={x.split(' (',1)[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected_progress
save(RUN/'PROGRESS.json',progress); save(RUN/'PACKET_DELTA.json',progress)

report_root=PROTOCOL_PATH.parent
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
ctx=Path(r'~\brain_workers\FEI100_20261011\context')
source_files=[PROTOCOL_PATH]+[report_root/n for n in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json',
 'OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
source_files += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md',
 'sources/OVERLAPPING_PRODUCT_NOTE.md','sources/LOG_ALLOCATION_CURATED.md','baseline/current-threshold-paper.tex']]
source_files += list(ctx.glob('*.txt'))
source_files += [Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),
 Path(r'~\brain_workers\FEI100_20261011\claude\B03\STREAM_NOTES.md')]
source_files += list((report_root/'runs').rglob('REPORT.md'))
artifacts=list(RUN.rglob('*'))+[ROOT/'STATUS.md',ROOT/'WORKLOG.md',ROOT/'LEARNED.md']
artifacts=[p for p in artifacts if p.is_file() and p.name!='receipts.json']
for p in artifacts: assert p.stat().st_size<20*1024*1024
assert json.loads((RUN/'PROGRESS.json').read_text())==json.loads((RUN/'PACKET_DELTA.json').read_text())
receipts={'run_id':RUN.name,'sources':[receipt(p) for p in source_files],
 'artifacts':[receipt(p) for p in artifacts],
 'validation':{'claim_fields_exact':True,'progress_fields_exact':True,'delta_identical':True,
 'every_artifact_below_20MB':True,'independent_review':False,'mirror_verified':False,
 'protocol_key_interpretation':'packet_ids (one primary ID, for compatibility) is descriptive; actual JSON key packet_ids per protocol compatibility contract'}}
save(RUN/'out/receipts.json',receipts)
print(json.dumps({'claims':1,'artifact_count':len(artifacts),'source_count':len(source_files),
 'protocol_fields':'PASS','report_sha256':receipt(RUN/'REPORT.md')['sha256'],
 'check_sha256':receipt(RUN/'out/check.json')['sha256']}))
