from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,datetime
import search as s
r=s.RUN; results=json.loads((s.OUT/'results.json').read_text()); rows=results['rows']
expected=[{'n':1,'classes':2,'truth_tables':4},{'n':2,'classes':4,'truth_tables':16},{'n':3,'classes':14,'truth_tables':256},{'n':4,'classes':222,'truth_tables':65536}]
max_n=results['census'][-1]['n']
assert results['census']==expected[:max_n], 'Cannot claim a dimension without complete orbit census'
assert len(rows)==sum(x['classes']-1 for x in results['census'])
replay=json.loads((s.OUT/'replay.json').read_text())
upper=max(Q(x['ratio_hi']) for x in rows)
ceiling=Q((upper*1000000).__ceil__(),1000000)
assert all(Q(x['ratio_hi'])<=ceiling for x in rows)
top=rows[0]; lower=Q(top['ratio_lo'])
strict=[x for x in rows if Q(x['ratio_hi'])<lower]
tied=[x for x in rows if Q(x['ratio_hi'])>=lower]
summary={'finite_ceiling':str(ceiling),'top_ratio_interval':[str(lower),top['ratio_hi']],'top_row':top,'overlapping_top_rows':[{'n':x['n'],'truth':x['truth'],'representative':x['representative'],'ratio':x['ratio']} for x in tied],'strictly_separated_rows':len(strict),'census':results['census'],'rows':len(rows),'orientations':2*len(rows),'runtime_seconds':results['elapsed_seconds'],'max_interval_width':results['max_interval_width'],'replay_comparisons':replay['exact_comparisons']}
(s.OUT/'summary.json').write_text(json.dumps(summary,indent=2))
sources=[Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'),Path(r'~\mop_fei100\reports\fei-2026-10-11\source_material\reductions\paper\forests.tex'),Path(r'~\brain_workers\FEI100_20261011\claude\B02\STREAM_NOTES.md')]
sources+=list((r/'code').glob('*.py'))
hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
(s.OUT/'hashes.json').write_text(json.dumps(hashes,indent=2))
statement=f'Every Boolean sign on the uniform cube with 1<=n<={max_n} admits one of its two all-prime-implicant tables, one ordered cover per conjunction (transported from an NPN representative), and lambda=1/read, for which the complete conditioned posterior partition-forest residual R is at most ({ceiling}) I. Moreover for n<=2, in the class of all-prime-implicant tables with one complete support order per conjunction, optimizing BOTH orientations, EVERY positive packing weight and EVERY gate order, the maximum residual/influence infimum is exactly 3/10, attained by the two-bit point defect. Constants have R=I=0. No all-dimensional conclusion or weight-infimum lower bound for n=3,4 is asserted.'
hyp=['Uniform cube; normalized sign Fourier spectrum; entropy in bits','Exactly the partition forests of forests.tex with one root per source SCC','Permitted output orientation, transported prime supports and physical orders',f'Finite census: 1<=n<={max_n}; fixed global lambda=1/max coordinate read','Analytic infimum subclaim: n<=2; prime gates fixed by either orientation; one complete support order per gate; all admissible positive weights and all gate orders']
claim={'claim_id':'A010-PIJ-FINITE-TABLE-CEILING','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),'contributors':['A010'],'proof_source':{'report':'REPORT.md','code':['code/search.py','code/replay.py'],'certificate':['out/results.json','out/replay.json','out/summary.json','out/hashes.json']},'proof_dependencies':[{'source':str(sources[1]),'sha256':hashes[str(sources[1])],'locator':'eq:forestcost; definition of partition forests; thm:posteriorforest'}],'review_records':[],'status':'FINITE_CERTIFIED_AUTHOR_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['Claude/B02','A006','A009','A086','A094']}
boundary_statement='For any fixed finite ordered support table with positive pi, covering every positive-mass nonempty Fourier set, and any fixed positive packing vector mu, the complete optimal posterior partition-forest residual obeys R(t mu)=D log2(1/t)+O(1) as t decreases to zero, where D=sum_{A nonempty} P_f(A)(d_A-1) and d_A is the minimum number of supports covering A. In particular D>0 forces divergence to +infinity. The remainder depends on the fixed table and direction; no partial-boundary or all-lambda infimum claim follows.'
bhyp=['Fixed finite support/order table with pi_l>0 and every spectral A covered','Distinct partition forests; one root per source SCC; all used lambda_l positive','Fixed positive packing vector mu; 0<t<=1; bits; fixed finite Fourier law']
boundary=dict(claim)
boundary.update(claim_id='A010-PIJ-RADIAL-BOUNDARY',exact_statement=boundary_statement,hypotheses=bhyp,statement_sha256=hashlib.sha256(json.dumps({'statement':boundary_statement,'hypotheses':bhyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),proof_source={'report':'REPORT.md, weight-boundary handoff paragraph'},status='ANALYTICALLY_PROVED_AUTHOR_PENDING_INDEPENDENT_REVIEW')
old_claims=json.loads((r/'CLAIMS.json').read_text())
(s.OUT/'analytic_checkpoint_claims.json').write_text(json.dumps(old_claims,indent=2))
claim['supersedes']=['A010-PIJ-N2-INFIMUM-v1']
(r/'CLAIMS.json').write_text(json.dumps([claim,boundary],indent=2))
next_action='Use the P4 edge-DNF extremizer as a seed for unbounded-degree graph DNFs; derive posterior mass polynomials and certify all weight boundaries before claiming growth of the PI-J infimum. A086/A094 review the saved census and n<=2 proof.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':r.name,'stream':'B02','packet_id':'A010','gap_id':'G-J-COST','attempt_id':'A010-PIJ-CENSUS-1','method':'NPN census, integer Walsh and exact posterior forest mass with rational intervals; separate queue-trace replay','mathematical_delta':{'finite_ceiling':str(ceiling),'nonconstant_orbits':len(rows),'truth_tables':sum(x['truth_tables'] for x in results['census']),'top_n':top['n'],'top_truth':top['truth'],'all_lambda_infimum':'OPEN','full_FEI':'OPEN'},'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'FINITE_TABLE_UPPER_BOUND_CERTIFIED; UNIVERSAL_PIJ_AND_FEI_OPEN','claim_versions_used':['forests.tex source pin in out/hashes.json; thm:posteriorforest'],'claims_created_or_changed':['A010-PIJ-FINITE-TABLE-CEILING-v1'],'source_artifacts':['REPORT.md','SEARCH_SPEC.json','REPLAY_SPEC.json','code/search.py','code/replay.py','out/results.json','out/replay.json','out/summary.json','out/hashes.json'],'next_consumers':['Claude/B02','A006','A009','A086','A094'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Universal estimate and continuum lambda optimization unproved; independent-agent review pending'],'packet_ids':['A010']}
for name in ['PROGRESS.json','PACKET_DELTA.json']: (r/name).write_text(json.dumps(progress,indent=2))
progress['claims_created_or_changed'].append('A010-PIJ-RADIAL-BOUNDARY-v1')
progress['mathematical_delta']['weight_boundary']='Fixed positive rays: coefficient of log(1/t) equals E[(minimum cover number-1) 1_{A nonempty}]'
progress['mathematical_delta']['n_le_2_complete_weight_and_order_infimum']='Worst exact ratio 3/10; analytic proof includes both output orientations and limiting boundaries'
for name in ['PROGRESS.json','PACKET_DELTA.json']: (r/name).write_text(json.dumps(progress,indent=2))
report=(r/'REPORT.md').read_text()
report=report.replace('Pending final census and queue replay receipts.',f'Completed {len(rows)} nonconstant NPN classes ({2*len(rows)} output orientations), with orbit coverage of {sum(x["truth_tables"] for x in results["census"])} truth tables including constants. Counts by n are '+', '.join(f'{x["n"]}: {x["classes"]}' for x in results['census'])+f'. Certified R/I <= {ceiling} for a chosen admissible table for every nonconstant orbit. Largest recorded ratio midpoint is {top["ratio"]:.12f}, n={top["n"]}, selected truth integer={top["truth"]}, representative={top["representative"]}; the exact interval is in out/summary.json. {len(tied)} rows overlap the leading interval; {len(strict)} rows are strictly below its lower endpoint. Main runtime {results["elapsed_seconds"]:.3f} seconds. Separate queue growth exactly matched {replay["exact_comparisons"]} set/table mass-and-count checks involving {replay["distinct_runs_in_comparisons"]} distinct runs; replay runtime {replay["elapsed_seconds"]:.3f} seconds. This is a different enumeration within A010, not independent-agent acceptance.')
report=report.replace('Pending census extremizer:',f'Leading census extremizer n={top["n"]}, truth={top["truth"]}, prime gates={top["gates"]}:')
report=report.replace('Final result JSON, replay certificate, source hashes, CLAIMS.json, PROGRESS.json and PACKET_DELTA.json will be saved after validation.','Final result JSON, replay certificate, source hashes, CLAIMS.json, PROGRESS.json and PACKET_DELTA.json are saved. The finalizer checks each endpoint against the stated rational ceiling and writes the source/implementation SHA256 pins.')
report=report.replace('The quantitative finite delta will be recorded with the census;',f'The quantitative finite delta is the certified table ceiling R/I <= {ceiling} through {max_n} variables;')
if max_n<4:
    report=report.replace('This stage exhausts functions on 1<=n<=4 up to NPN symmetry','The frozen target was functions on 1<=n<=4 up to NPN symmetry; this completed certificate exhausts 1<=n<=3')
    report=report.replace('Completed '+str(len(rows))+' nonconstant', 'The full n<=4 job did not finish within its frozen shared-machine wall budget; no n=4 ceiling is claimed. A separate cheap n<=3 rerun supplies the durable finite certificate. Completed '+str(len(rows))+' nonconstant')
(r/'REPORT.md').write_text(report)
root=r.parents[1]
(root/'STATUS.md').write_text(f'STATE: A010 finite PI-J census certified R/I<={ceiling} through n={max_n} on {len(rows)} nonconstant NPN classes; n<=2 all-weight/order infimum closed at 3/10; review pending; full FEI OPEN.\nNEXT: {next_action}\n')
with (root/'WORKLOG.md').open('a') as f: f.write(f'\n2026-10-12: Completed PI-J census through n={max_n}: {len(rows)} nonconstant NPN classes, {2*len(rows)} orientations, finite table ceiling {ceiling}; exact queue replay {replay["exact_comparisons"]} comparisons. Saved protocol artifacts. No lambda-infimum obstruction found or claimed.\n')
with (root/'LEARNED.md').open('a') as f: f.write(f'\nFinite PI-J table upper bound through n={max_n}: R/I <= {ceiling}, {len(rows)} nonconstant NPN classes. Admissible orders are transported with the NPN symmetry, not assumed lexicographically invariant. Equal-attachment child labels contribute a factorial multiplicity of DISTINCT queue runs. Per-step dyadic enclosure reduces rational log-series cost without losing certification. Complete n<=2 all-weight/all-order/both-orientation prime-table infimum maximum is 3/10.\n')
protocol=json.loads(sources[0].read_text())['required_per_run']
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert set(claim)==set(protocol['claim_fields'])
assert set(boundary)==set(protocol['claim_fields'])
assert (r/'PROGRESS.json').read_bytes()==(r/'PACKET_DELTA.json').read_bytes()
for p in r.rglob('*'):
    if p.is_file(): assert p.stat().st_size<20_000_000,(p,p.stat().st_size)
print(json.dumps({k:v for k,v in summary.items() if k!='top_row'},indent=2))
