from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy

ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
TEAM=AGENT.parents[1]
LEAD=TEAM/'claude/B04/runs/20261011T224500Z-claude-B04-sharp-selector-debt'
PROTOCOL=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
stamp=datetime.now(timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def readj(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,obj):(ROOT/p).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
protocol=readj(PROTOCOL);pilot=readj(ROOT/'out/PILOT.json');census=readj(ROOT/'out/CENSUS.json');bent=readj(ROOT/'out/BENT.json');failure=readj(ROOT/'out/LOW_PRECISION_FAILURE.json')
assert pilot['pilot']['status']=='PASS' and census['census']['status']=='PASS' and bent['bent']['status']=='PASS'
assert failure['m']==40 and failure['grid_bits']==80

# Preserve the exact initial helper that produced the saved pilot/census.
current=(ROOT/'code/check_lead.py').read_text(encoding='utf8')
initial=current.replace("BITS=96 if '--bits96' in sys.argv else 80\nSCALE=1<<BITS",'SCALE=1<<80')
initial=initial.replace("  gl,gh=grid(upper,2*d)\n  if gl<=0:\n   (ROOT/'out/LOW_PRECISION_FAILURE.json').write_text(json.dumps({'m':m,'grid_bits':BITS,'natural_sharp_gap_interval':[str(gl/SCALE),str(gh/SCALE)],'meaning':'This interval does not establish the strict sign; not a mathematical counterexample. Census already persisted.'},indent=2)+'\\n',encoding='utf8')\n  ck(gl>0)","  gl,gh=grid(upper,2*d);ck(gl>0)")
initial=initial.replace("elif '--bent-only' in sys.argv:\n result['bent']=bent();name='BENT.json'\n",'')
initialbytes=initial.encode('utf8')
assert sha(initialbytes)==census['code_sha256']==pilot['code_sha256']
(ROOT/'code/check_lead_census_original.py').write_bytes(initialbytes)

original=readj(LEAD/'CLAIMS.json')
targets=['B04-SEL-LOG-SHARP','B04-BENT-SPLICE-SHARP','B04-NODE-BOUNDARY']
claims=[];reviews=[]
proofloc={'B04-SEL-LOG-SHARP':'REPORT.md section 1','B04-BENT-SPLICE-SHARP':'REPORT.md section 2','B04-NODE-BOUNDARY':'REPORT.md section 3'}
for target in targets:
 source=next(c for c in original['claims'] if c['claim_id']==target)
 claim=copy.deepcopy(source)
 computed=sha(claim['exact_statement'].encode('utf8'))
 announced=claim['statement_sha256']
 claim['statement_sha256']=computed
 review={'reviewer':'A018','date_utc':stamp,'independent':True,'verdict':'HOLDS_AT_STATED_SCOPE','proof_reconstruction':proofloc[target],'implementation':'Independent Python integer Walsh/direct sums and rational outward logs; no imported lead code','source_statement_sha256_announced':announced,'statement_utf8_sha256_recomputed':computed,'source_hash_matches_utf8_statement':announced==computed,'mathematical_repair_supplied':False,'scope_note':'Bent sharpness is asymptotic on the displayed actual Boolean family, not exact pointwise optimization; standard zero-mass convention retained' if 'BENT' in target else 'Universal analytic statement plus independent exact finite certificate'}
 claim['review_records'].append(review)
 claim['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A018'
 claim['proof_source']=proofloc[target]+'; original lead claim and independently reconstructed proof, with exact certificates in out/'
 claim['first_unproved_line']=None
 assert set(claim)==set(protocol['required_per_run']['claim_fields'])
 claims.append(claim);reviews.append({'claim_id':target,'version':claim['version'],**review})
save('CLAIMS.json',{'claims':claims})
save('out/REVIEW_RECORDS.json',{'reviews':reviews,'full_fei':'OPEN','adoption_by_shared_registry':False})

nextaction='Reconstruct a spectator-free exact-bad-node boundary bill on a shared-data-coordinate two-level splice (A016/A017 fixtures), assigning disjoint downstream deficit reserves and retaining terminal H; A090/A091 challenge the three independently reconstructed lead versions.'
progress={
 'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B04','packet_id':'A018',
 'gap_id':'G-LOWSEL-COLLISION','attempt_id':'A018-stage2-independent-sharp-boundary-review',
 'method':'Independent analytic reconstruction, integer/direct Walsh census and outward rational-log certification; exact rational asymptotic coefficients and explicit remainder',
 'mathematical_delta':'Independently accepts B04-SEL-LOG-SHARP@1, B04-BENT-SPLICE-SHARP@1 and B04-NODE-BOUNDARY@1 at stated scope. All 262144 n=4 nodes have ratio <81/100; 20 bent histogram cases and three actual tensor fixtures certified. Universal cumulative bad-node boundary payment remains open.',
 'deliverable_status':'COMPLETE_LOCAL_READBACK_VERIFIED',
 'mathematical_status':'THREE_LOCAL_LEAD_CLAIMS_INDEPENDENTLY_ACCEPTED_AT_SCOPE; UNIVERSAL_FEI_OPEN',
 'claim_versions_used':['A018-COLLISION-BLOCK-INTERFACE@1 (lead HOLDS)','B04-SEL-LOG-SHARP@1','B04-BENT-SPLICE-SHARP@1','B04-NODE-BOUNDARY@1'],
 'claims_created_or_changed':[target+'@1: append independent A018 HOLDS review; exact statement unchanged' for target in targets],
 'source_artifacts':['REPORT.md','CLAIMS.json','code/check_lead.py','code/check_lead_census_original.py','out/FROZEN_SPEC.json','out/PILOT.json','out/CENSUS.json','out/BENT.json','out/LOW_PRECISION_FAILURE.json','out/PRECISION_AMENDMENT.json','out/REVIEW_RECORDS.json'],
 'next_consumers':['A016','A017','A019','A020','A027','A090','A091','B04 lead','B05','B06','B20'],
 'next_action':nextaction,'stagnant_substantive_attempts':0,
 'blockers':['No universal nonreusing adaptive boundary/terminal payment supplied','Supervisor registry adoption and mirror verification pending'],
 'packet_ids':['A018']
}
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)

paths=[PROTOCOL,TEAM/'BOARD.md',TEAM/'claude/B04/STREAM_NOTES.md',LEAD/'CLAIMS.json',LEAD/'code/verify2.py',LEAD/'REPORT.md',AGENT/'runs/20261011T221538Z-fleet05-A018-shared-data-collision-law/REPORT.md',AGENT/'runs/20261011T221538Z-fleet05-A018-shared-data-collision-law/CLAIMS.json']
sources=[]
for p in paths:
 if p.exists():
  b=p.read_bytes();sources.append({'path':str(p),'bytes':len(b),'sha256':sha(b),'access':'READ_ONLY'})
 else:sources.append({'path':str(p),'status':'ABSENT'})
save('out/SOURCE_RECEIPTS.json',{'recorded_at_utc':stamp,'sources':sources,'source_scopes':'REPORT.md source section; no source is modified'})

(AGENT/'STATUS.md').write_text('STATE: A018 stage 2 independently accepts B04 selector-log, bent-sharpness and node-boundary v1 claims; 262144 n=4 nodes certified <81/100; full FEI OPEN; supervisor adoption pending.\nNEXT: A090/A091 challenge; reconstruct spectator-free bad-node boundary payment on a shared-coordinate two-level splice with single-use downstream reserves and terminal H retained.\n',encoding='utf8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf8') as f:
 f.write(f'\n{stamp} | Stage 2: followed B04 lead v2 review assignment rather than repeating stage-1 identity or A019 translations. Three independent analytic verdicts HOLDS at stated scope. Pilot: 6463 assertions, 1082 block cases/804 nodes, {pilot["elapsed_seconds"]:.3f}s. Complete n=4 singleton census: 65536 tables/262144 nodes, rational ratio cap 81/100, exact direct Walsh and physical derivative checks; saved before later sign failure. Bent m=40 strict gap unresolved on 80-bit grid; saved failure, refined only bent calculations to96 bits. All20 bent histograms and3 tensor fixtures PASS, {bent["assertions"]} assertions in{bent["elapsed_seconds"]:.3f}s. Derived exact -19/6 and8/3 natural-unit coefficients with a uniform analytic remainder. No full-FEI or nonreusing cumulative boundary theorem claimed. All run files/readbacks saved locally.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf8') as f:
 f.write('''
## Stage 2: independently reviewed selector/boundary debt

B04 lead v2 has independently reconstructed A018 stage1 and directs an audit of its selector-log, bent-sharpness and node-boundary claims. All three exact v1 statements HOLDS at scope by A018 reconstruction. Statement text is unchanged; review records preserve announced source hashes and recomputed UTF-8 hashes (which differ), and local statement hashes use the latter. Supervisor adoption is pending. No need to restart these baselines.

For any fresh a-bit multiplexer with s=I_sel, exact B_W<=a h2(s/a) follows from conditional entropy<=sum marginal bit entropies and concavity. Together with posterior M_W, Delta<=min(a,2s/ln2)+a h2(s/a)<=s log2(e^3 a/s). Zero selectors/influence use continuous zero conventions. The logarithm is unavoidable to first order on actual bent splices.

Bent splice: delta=2^-m, u=sqrt(delta), branch coefficient signs have multiplicities (2^m+e2^(m/2))/2. Parent sectors have coefficients eu-delta and delta. The exact closed formula in REPORT section2 agrees with independent integer histograms. Delta=m delta+(3delta-19delta^2/6-61delta^3/30+...)/ln2. Envelope gap=(8delta^2/3+28delta^3/15+...)/ln2. For m>=4 the remainder through delta^2 has natural-unit magnitude <=(512/3)delta^3. Sharpness is an asymptotic family statement, not a fixed-(s,a) extremal theorem.

For one coordinate, D=(g-h)/2 is trinary and d=E D^2=Inf_i(f). Use I(D)=sum|T|Dhat(T)^2, not trinary disagreement influence. Its support A has I(D)>=I(1_A). Indicator-specific product entropy gives d ln(1/d)<=2ln2 I(1_A), so Delta_i<=3d/ln2+2I(D). I(D)=sum_(S contains i)(|S|-1)fhat(S)^2. Bent point derivative has I(D)=m delta/2 and Delta/node-bound tends to1.

Exact review data: pilot6463 assertions/1082 block cases n<=3, full65536 n=4 tables and262144 physical singleton nodes (1024 have zero influence). All nonzero boundary ratios have rational upper endpoint below81/100. Largest interval witness mask7,i0 has d=1/8, I(D)=3/16 and Delta_nat=(768ln2-200ln5-72ln3)/256. This is a proved cap, not an exact argmax classification. Histograms m=2,4,...,40 plus direct m<=8 and tensor(2,2),(2,3),(4,2) certified. Preserve the initial helper's exact source hash in code/check_lead_census_original.py.

Precision lesson: strict m40 envelope gap is O(delta^2)=O(2^-80); an80-bit grid cannot necessarily sign it after cancellation of large prime logs. Preserve inconclusive bounds and refine only the relevant subjob. A96-bit grid with the same36-term rational atanh tails settled every required sign. No failed theorem is inferred from an enclosure crossing zero.

Universal gap: select a certified physical stopping tree and pay sum_(exact B_v>K d_v) pi_v 2I(D_v)<=K'I(root) using the same physical reserve once and retaining terminal H. Root majority can have exact B=0; h2(d) must not define badness. A016 tensor-spectator overcharge makes blind derivative-energy pricing unsuitable. Next use a spectator-free shared-coordinate two-level splice and A017 incompatible phase-gradient fixtures, keeping actual downstream deficits.
''')

receipts=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  b=p.read_bytes();assert len(b)<20*1024*1024
  if p.suffix=='.json':json.loads(b.decode('utf-8-sig'))
  receipts.append({'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':sha(b),'readback':'PASS'})
for name in ('STATUS.md','WORKLOG.md','LEARNED.md'):
 p=AGENT/name;b=p.read_bytes();receipts.append({'path':str(p),'bytes':len(b),'sha256':sha(b),'readback':'PASS'})
assert len((AGENT/'STATUS.md').read_text(encoding='utf8').splitlines())==2
assert readj(ROOT/'PROGRESS.json')==readj(ROOT/'PACKET_DELTA.json')
save('out/PERSISTENCE_RECEIPTS.json',{'date_utc':stamp,'local_persistence':'VERIFIED_READBACK','schema':'PASS; exact claim/progress fields; protocol annotation stripped from packet_ids; statement hashes checked; all JSON parse; STATUS two lines; per-file limit checked','initial_checker_source_hash_reconstructed':sha(initialbytes),'artifacts':receipts,'supervisor_adoption':False,'mirror_verified':False,'full_fei':'OPEN'})
print(json.dumps({'status':'PERSISTED','review_verdicts':len(reviews),'artifact_receipts':len(receipts),'source_hash_match':'PASS','full_fei':'OPEN'},indent=2))
