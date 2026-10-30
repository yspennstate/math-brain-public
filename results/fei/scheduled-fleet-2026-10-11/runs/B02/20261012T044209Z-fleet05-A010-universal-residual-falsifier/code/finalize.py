from pathlib import Path
from fractions import Fraction as Q
import hashlib,json
RUN=Path(__file__).resolve().parents[1]; ROOT=RUN.parents[1]; OUT=RUN/'out'
OLD=ROOT/'runs/20261011T225444Z-fleet05-A010-universal-residual-falsifier'
def write(path,obj): path.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
consumers=['Claude/B02','A009','A086','A094']
source=Path('~/mop_fei100/reports/fei-2026-10-11/source_material/reductions/paper/forests.tex')
dep={'source':str(source),'sha256':digest(source),'locator':'partition-forest definition; eq:forestcost; eq:foresttarget; thm:posteriorforest','acceptance':'Source definition used directly; FEI implication conditional on source theorem'}
lead=Path('~/brain_workers/FEI100_20261011/claude/B02/runs/20261011T230200Z-claude-B02-single-gate-collapse')
leadclaims=json.loads((lead/'CLAIMS.json').read_text())['claims']
reviews=[]
for c in leadclaims[:2]:
    reviews.append({'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256'],'reviewer':'A010','verdict':'ACCEPT_AT_STATED_SCOPE','method':'Independent all-n specialization: exact one-root cancellation and adjacent-swap rank proof; L2 additionally reconstructed in 65536-mask independent Walsh census','proof_source':'REPORT.md; code/raw_rank.py; out/raw_rank_65536.json','dependency_scope':'Conditional on forests.tex posterior theorem; O1 not reviewed; no repair supplied'})
write(OUT/'reviews.json',reviews)

def claim(cid,statement,hyp,code,cert,deps):
    return {'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),'contributors':['A010'],'proof_source':{'report':'REPORT.md','code':code,'certificate':cert},'proof_dependencies':deps,'review_records':[],'status':'FINITE_CERTIFIED_AUTHOR_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':consumers}

claims=[claim('A010-N4-PRIME-SINGLE-MENU-INFIMUM',
 'On uniform cubes with n<=4, the maximum over nonconstant Boolean f of the infimum of the posterior partition-forest residual R/I over the following menu is exactly (43+19 log2 3)/80: either one gate f or -f with one full relevant-support order, or exactly all prime implicants of either output side with one full support order per conjunction; in both cases optimize all positive global packing weights and the conditional law on distinct source-SCC partition forests. Constants have R=I=0. Equality occurs precisely on the 96 four-coordinate NPN images of OR(AND2,AND2). This is not the prime-only constant or an all-dimensional result.',
 ['Entropy in bits; gamma=6/5; R is eq:foresttarget without h2(v) or K_ref I','Menu contains no additional gates or multi-covers; full single order only','Positive global weights satisfy coordinate-incidence packing; limiting zero faces accounted for in infimum lower proof','Uniform cube; Boolean signs; 0<=n<=4'],
 ['code/single_compare.py','code/prime_poly.py','code/continuum.py','code/verify_continuum.py','code/raw_rank.py'],
 ['out/single_n4.json','out/prime_polynomials.json','out/continuum_summary.json','out/independent_check.json','out/raw_rank_65536.json'],[dep])]

rows=json.loads((OUT/'p4_candidates.json').read_text())['rows']; upper=min(Q(r['hi']) for r in rows)
oldrows=json.loads((OLD/'out/results.json').read_text())['rows']
others=[r for r in oldrows if not(r['n']==4 and r['representative']==863)]
assert all(Q(r['ratio_hi'])<Q(32,25) for r in others)
assert upper<Q(130101,100000)
summary=json.loads((OUT/'p4_continuum_summary.json').read_text()); check=json.loads((OUT/'p4_independent_check.json').read_text())
assert summary['tables']==check['tables']==16 and Q(check['minimum_independent_lower'])>=Q(32,25)
write(OUT/'pure_prime_bracket.json',{'lower':'32/25','upper':str(upper),'convenient_upper':'130101/100000','upper_table':{k:rows[0][k] for k in ['truth','gates','orders','lambda','hi']},'non_P4_orbits_checked':len(others),'maximum_other_chosen_table_upper':str(max(Q(r['ratio_hi']) for r in others)),'extremizer':'P4 NPN family','sharp_value':'OPEN','source':str(OLD/'out/results.json')})
claims.append(claim('A010-PIJ-N4-VARIATIONAL-BRACKET',
 'For the prime-only menu (exactly all primes of either Boolean output side, one full support order per conjunction, all positive global packing weights), the maximum through n<=4 of inf R/I is attained only in the P4 edge-DNF NPN class represented by truth863. Its value lies in [32/25,130101/100000]. The lower bound includes all 16 gate-order/orientation tables and all admissible weights and limiting zero faces; the upper comes from the rational table weights (7/8,7/8,1/8), orders ((2,1),(3,0),(2,3)) on supports (6,9,12). Every other NPN class has a certified chosen table below 32/25. The exact optimum and every all-dimensional claim remain open.',
 ['Uniform Boolean cube n<=4; bits; gamma=6/5','All-prime fixed gates; one full order per gate; either output side; globally fixed positive packing weights','Distinct partition forests with one root per source SCC; optimal conditional posterior','Use exact stage-1 orbit census and chosen-table certificate for the non-P4 upper comparisons'],
 ['code/p4.py','code/p4_continuum.py','code/p4_verify.py','code/verify_continuum.py'],
 ['out/p4_candidates.json','out/p4_continuum_summary.json','out/p4_independent_check.json','out/pure_prime_bracket.json'],
 [dep,{'claim_id':'A010-PIJ-FINITE-TABLE-CEILING','version':1,'statement_sha256':'be899b0fa23230ed244e93ec90e98d90ab0c5dc45feaf911e142ff8a50d93599','acceptance':'Author-checked certificate reused; independent-agent review pending','source':str(OLD/'CLAIMS.json')}]))
write(RUN/'CLAIMS.json',claims)

progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B02','packet_id':'A010','gap_id':'G-J-COST','attempt_id':'A010-BOUNDED-VARIATIONAL-2','method':'Exact one-gate rearrangement and raw Walsh census; multiaffine mass-ratio dyadic weight-domain cover; distinct queue and rational-log replay','mathematical_delta':{'menu_n_le_4_exact':'(43+19 log2 3)/80','menu_equality_truth_tables':96,'pure_prime_n_le_4_bracket':['32/25','130101/100000'],'pure_prime_extremizer':'P4 NPN class','pure_prime_all_orders':16,'pure_prime_certificate_nodes':summary['nodes'],'pure_prime_verified_leaves':check['verified_leaves'],'source_L1_L2':'Independent local acceptance at stated scope','sharp_prime_constant':'OPEN','universal_PIJ_and_FEI':'OPEN'},'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'FINITE_MENU_EXACT_AND_PRIME_INFIMUM_BRACKET_CERTIFIED; UNIVERSAL_OPEN; INDEPENDENT_AGENT_REVIEW_PENDING','claim_versions_used':[{'claim_id':r['claim_id'],'version':r['version'],'statement_sha256':r['statement_sha256'],'acceptance':'Independent local reconstruction in out/reviews.json'} for r in reviews]+[{'claim_id':'A010-PIJ-FINITE-TABLE-CEILING','version':1,'acceptance':'Author-checked source census reused; independent-agent review pending'},dep],'claims_created_or_changed':[c['claim_id']+'-v1' for c in claims],'source_artifacts':['REPORT.md','CLAIMS.json','out/reviews.json','out/hashes.json','out/independent_check.json','out/raw_rank_65536.json','out/p4_independent_check.json','out/pure_prime_bracket.json']+[p.name for p in sorted(RUN.glob('*SPEC.json'))],'next_consumers':consumers,'next_action':'Use the certified P4 prime-only infimum bottleneck to derive a growing high-read graph-DNF mass polynomial, and apply the multiaffine ratio bounds to ALL packing weights rather than one table; A086/A094 review both bounded certificates.','stagnant_substantive_attempts':0,'blockers':['Sharp P4 optimum unproved; growing-family universal lower bound unproved; independent-agent acceptance and supervisor mirror not verified'],'packet_ids':['A010']}
write(RUN/'PROGRESS.json',progress); write(RUN/'PACKET_DELTA.json',progress)

report=(RUN/'REPORT.md').read_text(encoding='utf-8')
report=report.replace('Later optional pure-prime tests must be distinguished explicitly from this closed menu theorem.', 'The separate pure-prime bracket below addresses that infimum without identifying its sharp value.')
insert='''**Pure-prime continuation: whole-domain P4 lower bound.** The rational grid only supplies a chosen-table upper bound: on truth863, gates with masks 6,9,12, orders (2,1),(3,0),(2,3), weights (7/8,7/8,1/8), the certified upper endpoint is below 130101/100000 (midpoint 1.3010094884). Independently of this search, p4_continuum.py covers ALL weights, both output orientations, and all 16 full gate-order tables with the same multiaffine-ratio argument. p4_verify.py reconstructs all spectral polynomials by the separate queue algorithm, verifies a prefix-free complete dyadic cover, and uses its separate rational logarithm/fifth-root bounds. Every table has R/I>=32/25. This is a lower bound on the variational infimum, not a failure of one representation. The source-bound stage-1 chosen-table intervals for every OTHER NPN class are strictly below 32/25, as rechecked exactly in out/pure_prime_bracket.json. Consequently the pure-prime n<=4 worst infimum belongs precisely to the P4 NPN class and lies in [32/25,130101/100000]. Its sharp value remains unproved. P4 has read two, so repeating bounded-degree paths cannot itself give an unbounded route obstruction; the next growing family must have increasing read or a different unpaid mechanism.

'''
report=report.replace('## executed validation with domain, arithmetic, commands and outputs',insert+'## executed validation with domain, arithmetic, commands and outputs')
report=report.replace('The prime-only n<=4 sharp infimum constant is not established by the menu result','The prime-only n<=4 sharp infimum constant is not established')
report=report.replace('CLAIMS/PROGRESS/PACKET_DELTA and hash receipts will be finalized after the last scoped computation.', 'CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are finalized; out/reviews.json records source-bound L1/L2 review, and out/hashes.json pins code, source inputs and run artifacts. The finalizer checks exact protocol field sets, claim statement digests, output sizes and compatibility-copy equality.')
report=report.replace('Frozen specifications SEARCH_SPEC.json, POLYNOMIAL_SPEC.json, CONTINUUM_SPEC.json, VERIFY_SPEC.json and RAW_CENSUS_SPEC.json', 'Frozen specifications SEARCH_SPEC.json, POLYNOMIAL_SPEC.json, CONTINUUM_SPEC.json, VERIFY_SPEC.json, RAW_CENSUS_SPEC.json, P4_SPEC.json and P4_CONTINUUM_SPEC.json')
report=report.replace('Apply the multiaffine ratio certificate to the prime-only P4 bottleneck, retaining all orders and partial-zero faces, then use its actual prime-support pattern for a growing high-read family.', 'Use the certified prime-only P4 bottleneck to derive a growing high-read graph-DNF posterior mass polynomial, retaining all packing weights, orders and partial-zero faces.')
report=report.replace('Prime-only and all-dimensional PI-J remain open. NEXT targets the remaining prime-only bottleneck with a certificate over its full weight domain,', 'The prime-only four-bit worst infimum is additionally located in [32/25,130101/100000] with all weights/orders certified on P4; its sharp value and all-dimensional PI-J remain open. NEXT transports the unpaid P4 pattern to a growing high-read graph family with a certificate over its full weight domain,')
report=report.replace('No runtime cap was exceeded.',f"No runtime cap was exceeded. P4 generator pilot: {json.loads((OUT/'p4_continuum_pilot.json').read_text())['elapsed_seconds']:.4f} s; full P4 cover: {summary['elapsed_seconds']:.4f} s, {summary['nodes']} nodes; distinct P4 checker: {check['elapsed_seconds']:.4f} s, {check['verified_leaves']} leaves, {check['exact_polynomial_matches']} polynomial matches. Commands: code/p4.py; code/p4_continuum.py pilot then full; code/p4_verify.py pilot then full. Exact brackets and all leaves are saved in out/p4_*.json.")
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(ROOT/'STATUS.md').write_text('STATE: A010 stage2 exact n<=4 prime-plus-single menu constant certified; pure-prime worst P4 infimum in [32/25,130101/100000] over all weights/orders; FEI OPEN.\nNEXT: Transport P4 unpaid pattern to growing high-read graph DNFs; A086/A094 review full-domain menu and pure-prime certificates.\n',encoding='utf-8')
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n2026-10-12 stage2 continuation: P4 all-weights/order/orientation lower R/I>=32/25 certified, {summary["nodes"]} cover nodes and {check["verified_leaves"]} replayed leaves; rational table upper<130101/100000. All other n<=4 NPN classes have chosen tables below32/25: true prime-only worst infimum is P4, sharp value OPEN. Protocol outputs and review/hash receipts finalized.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nP4 now has a true prime-only variational lower certificate: every positive packing weight, all 16 full-order/orientation tables and zero faces have R/I>=32/25; a rational (7/8,7/8,1/8) table gives R/I<130101/100000. Every other n<=4 NPN class has chosen-table upper<32/25, so P4 is the worst prime-only family through four variables. Sharp optimum is open; read-two repetition cannot show unbounded growth.\n')

protocol=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'); fields=json.loads(protocol.read_text())['required_per_run']
expected=set(fields['progress_fields']); expected.remove('packet_ids (one primary ID, for compatibility)'); expected.add('packet_ids')
assert set(progress)==expected
for c in claims: assert set(c)==set(fields['claim_fields'])
for name in fields['report_fields']: assert '## '+name in report
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
files=[p for p in RUN.rglob('*') if p.is_file() and '__pycache__' not in str(p) and p.name not in ['hashes.json','persistence_check.json']]
assert all(p.stat().st_size<20_000_000 for p in files)
sourcefiles=[protocol,source,lead/'CLAIMS.json',lead/'REPORT.md',OLD/'out/results.json',OLD/'CLAIMS.json']
write(OUT/'hashes.json',{'source_inputs':{str(p):digest(p) for p in sourcefiles},'run_artifacts':{str(p.relative_to(RUN)):digest(p) for p in files}})
write(OUT/'persistence_check.json',{'protocol_fields':'exact sets checked','compatibility_copy':'byte-identical','claim_digests':'SHA256 canonical statement/hypotheses','maximum_file_bytes':max(p.stat().st_size for p in files),'files_hashed':len(files),'writes':'A010 only','independent_agent_review':'PENDING','supervisor_mirror':'UNVERIFIED'})
print(json.dumps({'claims':[c['claim_id'] for c in claims],'pure_prime_bracket':['32/25','130101/100000'],'all_protocol_checks':'PASS','files_hashed':len(files)},indent=2))
