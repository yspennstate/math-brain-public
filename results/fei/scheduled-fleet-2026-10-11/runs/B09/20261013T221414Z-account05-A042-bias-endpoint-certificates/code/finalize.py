from pathlib import Path
import json,hashlib,datetime
root=Path(__file__).resolve().parents[1];agent=root.parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def write(name,obj):
 (root/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def claimhash(statement,hyp):
 return hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
team=Path(r'~\brain_workers\FEI100_20261011')
a43=team/'agents/A043/runs/20261012T012726Z-account05-A043-prime-gate-decomposition'
a41=team/'agents/A041/runs/20261013T215146Z-account05-A041-weighted-threshold-fei'
a45=team/'agents/A045/runs/20261013T212421Z-account05-A045-biased-realizability-referee'
sourceclaim=json.loads((a43/'CLAIMS.json').read_text())[0]
binary=next(c for c in json.loads((a41/'CLAIMS.json').read_text()) if c['claim_id']=='A042-SHARP-BINARY-PRIME-ENDPOINT')
assert binary['statement_sha256']=='e163ebefc916767a00214eea2d54e56e53c9666821565f612f15a7ef4f17d5e8'
statement=('For the sign majority-three gate under every independent interior Bernoulli product law, natural corrected entropy '
 'E=(ln2)Hplus satisfies E <= (4+ln4)(I-Var) - (ln4-1)P({1,2,3}). '
 'Its exact all-bias supremum Hplus/(I-Var) is 2+4/ln2, not attained in the interior, and approached at probabilities (1-t^3,t,t). '
 'The result is invariant under input permutations/reflections with reflected biases and output negation. '
 'At a unanimous deterministic vertex with rare deviations e,u,v, the ratio is 2+O(delta ln(1/delta)); '
 'at a mixed vertex represented by probabilities (1-e,u,v), the ratio is 2+(2/ln2)(1+uv/[e(u+v)+uv])+O(delta ln(1/delta)), '
 'where delta=max(e,u,v) and each absolute error is at most 400 delta ln(1/delta) for delta<=1/8, with no restriction on relative rates. '
 'Codimension-two fixed-interior-r edge formulas are (12)-(13) of REPORT.md; their remainders are uniform only on compact r-subintervals. '
 'All deterministic boundary functions are contracted before zero-deficit division. No arbitrary-arity prime or universal FEI theorem is established.')
hyp=['fixed genuine essential sign majority on three independent Bernoulli bits','interior probabilities 0<pi<1 for the global quotient','natural E and bit Hplus=E/ln2; spectral I, not unweighted physical pivotal expectation','T=P({1,2,3}) is the actual biased spectral triple mass','absolute corner error bound for 0<e,u,v<=1/8','fixed compact interior r domain for codimension-two edge remainders','input reflection changes its physical bias simultaneously','no extension of the special common-triple identity to higher arities assumed']
claim={'claim_id':'A042-SHARP-MAJORITY3-BIASED-ENDPOINT','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':claimhash(statement,hyp),
 'contributors':['A042/account05'],
 'proof_source':{'run_id':root.name,'path':'REPORT.md','locators':['Theorem (T), sections 1-3','independent-rate boundary certificate (7)-(13)'],'checker':'code/check_majority.py','output':'out/CHECK_OUTPUT.json'},
 'proof_dependencies':['actual majority Boolean truth table and finite-difference polynomial','Parseval for indicator-valued pivotal derivatives','elementary logarithm inequalities and explicit Taylor remainders'],
 'review_records':[],'status':'ANALYTIC_PROOF_EXACT_CHECKS; INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A041','A043','A044','A045','A084','A090','A091','B09','B20']}
write('CLAIMS.json',[claim,binary])
review={'reviewer':'A042/account05','claim_id':sourceclaim['claim_id'],'version':sourceclaim['version'],'original_statement_sha256':sourceclaim['statement_sha256'],
 'verdict':'PARTIAL_REVIEW_HOLDS','accepted_subresult':'majority prime test, normalized spectrum and (1-q^3,q,q) boundary limit including lower bound above 7 at q=1/8',
 'method':'independent centered-moment truth-table reconstruction over twelve source-path dyadic values plus all-rate analytic limit; source coefficients not assumed',
 'source':str(a43/'MAJORITY_BOUNDARY.md'),'new_local_proof':'REPORT.md sections 1 and 4','finite_certificate':'out/CHECK_OUTPUT.json',
 'not_reviewed':['complete n<=4 grid certificate','prime census','full bundled source claim'],'contributed_repair':False,
 'cap_handling':'consume queued boundary source and independently reviewed prior binary result, then finish the same endpoint packet with a fixed higher-prime theorem; no new broad universal candidate'}
write('out/REVIEW_SCOPE.json',{'A043_boundary':review,'A042_binary_review_consumed':{'claim_id':binary['claim_id'],'version':binary['version'],'statement_sha256':binary['statement_sha256'],'review_source':str(a41/'REVIEW_BINARY.md'),'scope':'full binary and genuine read-once claim; original review record preserved in local CLAIMS.json','contributor_repair':False}})
checks=json.loads((root/'out/CHECK_OUTPUT.json').read_text())
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':root.name,'stream':'B09','packet_id':'A042','gap_id':'G-BIASED-LTF','attempt_id':'A042-majority-prime-endpoint-3',
 'method':'degree-resolved singleton Parseval credit; common-triple payment of pair normalization; full all-bias inequality; rate-independent boundary expansion with explicit error; source-bound partial review',
 'mathematical_delta':'Closed exact majority-three corrected ratio supremum 2+4/ln2 over all biases, with favorable triple mass remainder and all deterministic boundary strata. Reconstructed A043 boundary source; consumed A041 independent binary acceptance. No new universal candidate.',
 'deliverable_status':'COMPLETE_LOCAL_SAVED','mathematical_status':'FIXED_PRIME_CONTINUUM_CLOSED_BY_AUTHOR; REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':sourceclaim['claim_id'],'version':1,'use':'named majority boundary independently reconstructed; grid not accepted','statement_sha256':sourceclaim['statement_sha256']},{'claim_id':binary['claim_id'],'version':1,'use':'reviewed binary face limits and optional disjoint closure','status':'A041 INDEPENDENT_REVIEW_HOLDS consumed','statement_sha256':binary['statement_sha256']}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'new narrow all-bias prime endpoint certificate'},{'claim_id':binary['claim_id'],'version':1,'change':'independent acceptance consumed; original statement/version unchanged'},{'claim_id':sourceclaim['claim_id'],'version':1,'change':'partial boundary review HOLDS; bundled grid status unchanged'}],
 'source_artifacts':['REPORT.md','code/check_majority.py','out/FROZEN_SPEC.json','out/CHECK_OUTPUT.json','out/ENDPOINT_MAP.json','out/REVIEW_SCOPE.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'A090/A091 independently reconstruct singleton 4D-2T credit and common-triple pair bound. A041/A043 test degree-resolved credit on next actual non-majority prime or mixed-sector coefficient process, isolating the replacement for common triple identity.',
 'stagnant_substantive_attempts':0,'blockers':[],'packet_ids':['A042']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
write('out/ENDPOINT_MAP.json',{'gate':'2*1[x1+x2+x3>=2]-1','all_bias_bound_nats':'E <= (4+ln4)D - (ln4-1)P123','sharp_supremum_bits':'2+4/ln2','unanimous_vertex':{'ratio':'2+error','max_absolute_error_bits':'400 delta ln(1/delta)'},
 'mixed_vertex':{'physical_probabilities':['1-e','u','v'],'S':'e(u+v)+uv','lambda':'uv/S','ratio_bits':'2+(2/ln2)(1+lambda)+error','max_absolute_error_bits':'400 delta ln(1/delta)','domain':'0<e,u,v<=1/8; delta=max(e,u,v)','cluster_interval_bits':['2+2/ln2','2+4/ln2']},
 'same_deterministic_edge':{'physical_probabilities':['e','d','r'],'leading_ratio_bits':'2+2A(r)/ln2','error':'O_r((e+d)ln(1/(e+d)))'},
 'opposite_deterministic_edge':{'physical_probabilities':['1-e','d','r'],'theta':'e/(e+d)','leading_ratio_bits':'2+(2/ln2)[1+theta A(r)+(1-theta)A(1-r)]','error':'O_r((e+d)ln(1/(e+d)))'},
 'edge_scope':'r in fixed compact subinterval of (0,1); joint r endpoint instead uses corner bound','A':'A(r)=r ln(1/r)/(1-r)','contraction':'face -> AND2/OR2 with positive remaining deficit; edge -> constant/literal with E=D=0; do not assign limiting quotient to zero deficit',
 'full_FEI':'OPEN'})
protocolpath=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
sources=[team/'BOARD.md',team/'claude/B09/STREAM_NOTES.md',protocolpath,a43/'REPORT.md',a43/'MAJORITY_BOUNDARY.md',a43/'CLAIMS.json',a41/'REPORT.md',a41/'REVIEW_BINARY.md',a41/'CLAIMS.json',a45/'CLAIMS.json',agent/'runs/20261012T002547Z-account05-A042-bias-endpoint-certificates/REPORT.md']
receipts=[]
for p in sources:
 raw=p.read_bytes();receipts.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
write('out/SOURCE_RECEIPTS.json',{'at':now,'files':receipts,'scope':'report-listed locators inspected; review scopes explicitly limited; no all-paper or all-grid audit claimed'})
protocol=json.loads(protocolpath.read_text(encoding='utf-8-sig'))
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
for c in (claim,binary):
 assert set(c)==set(protocol['required_per_run']['claim_fields'])
 assert c['statement_sha256']==claimhash(c['exact_statement'],c['hypotheses'])
assert (root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes()
report=(root/'REPORT.md').read_text()
for heading in protocol['required_per_run']['report_fields']:assert '## '+heading in report
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
assert checks['assertions_passed']==7783
write('out/VALIDATION.json',{'protocol_schemas':'PASS','claim_statement_hashes':'PASS','compatibility_delta':'PASS','report_fields':'PASS','source_boundary_review':'PARTIAL_HOLDS; grid not adopted','exact_assertions_passed':7783,'new_theorem_independent_review':'PENDING'})
(agent/'STATUS.md').write_text('STATE: A042 stage 3 saved: sharp majority3 all-bias supremum 2+4/ln2, triple-atom remainder and independent-rate boundary map; 7,783 exact checks; A043 boundary HOLDS; FEI OPEN.\nNEXT: A090/A091 review common-triple/singleton credit; A041/A043 test that credit on next non-majority prime or mixed-sector process, isolating its missing shared normalization payment.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n'+now+' | Stage 3: read updated board, stale-but-applicable B09 v2, A043 majority source and A041 binary review. Reconstructed A043 boundary at partial scope. Derived global sharp majority3 E<=(4+ln4)D-(ln4-1)P123, plus complete independent-rate vertex/edge map and absolute corner error400 delta ln(1/delta). Frozen 729 grid+12 source+128 corner+6 edge cases passed 7783 exact checks in1.302s. Saved required protocol files and review receipts; new independent review/mirror pending.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n# '+now+' majority-three shared triple payment\n'
 '- Majority c_i=p_j+p_k-2p_jp_k, c_ij=(1-2p_k)/2, c_123=-1/2; pair mass B, triple T, D=B+2T.\n'
 '- Preserve degree credit: E_single<=2 sum vi ci(1-ci)=4B+6T=4D-2T nats. Pair entropy<=ln4 Pij+T, and Etriple=ln4 T; hence E<=(4+ln4)D-(ln4-1)T globally. Exact sharp bit constant2+4/ln2 attained as limit on actual prime (1-t^3,t,t).\n'
 '- At rare e,u,v unanimous corners Hplus/D->2. At mixed corner (1-e,u,v), ratio=2+(2/ln2)(1+uv/[e(u+v)+uv])+error; error<=400 delta ln(1/delta), delta=max(e,u,v)<=1/8, independent rates. Oscillating mixture parameter can mean no ratio limit.\n'
 '- Opposite deterministic edge with remaining r has leading ratio2+(2/ln2)[1+theta A(r)+(1-theta)A(1-r)], theta=e/(e+d); same-sign edge gives2+2A(r)/ln2. Edge remainders uniform only for r in compact interior intervals; use corner proof when r moves to boundary.\n'
 '- A043 grid-and-boundary claim reviewed only for majority coefficients/prime/source path; grid not replayed. A041 full independent acceptance of binary A042 claim consumed at unchanged hash.\n'
 '- Higher-arity gap is replacing the single common triple payment with an all-degree owned normalization/reference, preserving the degree-resolved singleton credit; naive repetition of closed binary or one-bit-tax baselines does not supply it.\n')
manifest=[]
for p in sorted(root.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  raw=p.read_bytes();assert len(raw)<20_000_000
  manifest.append({'path':str(p.relative_to(root)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
write('out/PERSISTENCE_RECEIPTS.json',{'at':now,'local_files':manifest,'independent_review':'PENDING','supervisor_copy':'PENDING','brain_ingestion':'PENDING','mirror_verification':'NOT_CLAIMED'})
print(json.dumps({'saved_run':str(root),'files':len(manifest),'new_claim':claim['claim_id'],'exact_assertions':7783,'schemas':'PASS','A043_review':'PARTIAL_BOUNDARY_HOLDS'},indent=2))
