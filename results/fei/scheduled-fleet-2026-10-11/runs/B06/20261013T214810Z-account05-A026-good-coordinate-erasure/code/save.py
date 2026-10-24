import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
def dump(path,value):path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
BASE=AGENT.parents[1]
sources=[
 (BASE/'BOARD.md','stage-start complete read; refreshed header 2026-10-13 21:55 UTC'),
 (BASE/'claude/B06/STREAM_NOTES.md','v2; R2 and agent dispatch'),
 (AGENT/'runs/20261011T232716Z-account05-A026-good-coordinate-erasure/code/transitive.py','exact prime-log arithmetic and Walsh'),
 (AGENT/'runs/20261011T232716Z-account05-A026-good-coordinate-erasure/code/transitive_v2.py','outward interval implementation'),
]
other=BASE/'agents'
for who,run,files in [
 ('A003','20261012T005637Z-account05-A003-minimal-target-formulation',['REPORT.md','DERIVATION.md','CLAIMS.json']),
 ('A075','20261013T212622Z-account05-A075-search-to-theorem-bridge',['REPORT.md']),
 ('A057','20261012T003930Z-account05-A057-coherent-restriction-remainder',['REPORT.md','CLAIMS.json']),
 ('A063','20261011T222159Z-account05-A063-information-revelation',['REPORT.md'])]:
 for name in files:sources.append((other/who/'runs'/run/name,'read source; theorem locators in REPORT.md'))
sources.append((other/'A030/WORKLOG.md','current mechanism/plateau retirement'))
protocol=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
sources.append((protocol,'full read; execution-v2'))
dump(ROOT/'out/source_receipts.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'locator':loc} for p,loc in sources])
statement='For any even k>=4 and Boolean outer sign f(y,z_1,...,z_(3k)) with k background influences p(1/2+delta), 2k background influences p(1-sqrt(delta)+delta) and selector influence p delta, delta=2^-k,p=delta^2, encode each background by a fresh disjoint odd Majority_M, M=2k^2 2^(2k+2)+1, retaining y. At every actual restriction querying at most one physical bit per block and never y, every bit in an untouched block satisfies B_i/I_i<55/256 and I_i>I/(2d), d=3kM+1-q, q the number of queried blocks. For every adaptive prefix following this rule, cumulative erasure is <=(55/256)[I(root)-E I(leaf)] and H(root)<=E H(leaf)+(55/256+2/ln2)[I(root)-E I(leaf)]. The selector remains the unique maximum-influence coordinate throughout such histories and all influences are <1/4. Terminal entropy is retained; no terminal or universal FEI bound follows.'
hypotheses=['All finite uniform physical cubes; Boolean sign outer seed with exactly the stated influence types; entropy in bits.','Odd majority blocks fresh and mutually disjoint; at most one queried bit per block; no selector query.','Selection conclusions apply only when an untouched block exists; prefixes may stop earlier or when all 3k blocks are touched.']
claim={'claim_id':'A026-INTACT-ENCODER-BIASED-PREFIX','version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),'contributors':['A026'],'proof_source':{'run_id':ROOT.name,'path':'PROOF.md','locator':'sections 1-4','validation':['out/pilot_summary.json','out/main_summary.json','out/symbolic_checks.json']},'proof_dependencies':[{'source':'B06 STREAM_NOTES.md','version':'v2 2026-10-11 23:26Z','locator':'R2 influence telescope and JS bound; existing local proof, independent acceptance not asserted'},{'source':'A003-MAXIMUM-INFLUENCE-SELECTION-NOGO','version':1,'locator':'DERIVATION sections 2-4; source-conditional instantiation only, abstract influence-hypothesis statement independent of its review'},{'source':'A056-DISJOINT-COMPOSITION','version':2,'locator':'A057 stage2 CLAIMS reproduced accepted biased interface; special case directly reconstructed here'}],'review_records':[],'status':'SCOPED_AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A003','A056','A057','A087','A094','B06 lead','B20']}
dump(ROOT/'CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B06','packet_id':'A026','gap_id':'G-R-SELECT','attempt_id':'A026-stage3-intact-encoder-biased-prefix','method':'Actual physical rest packet concavity; induced product-density domination through one query per block; exact sliced-encoder signed corrections and rational/prime-log certificates.','mathematical_delta':'Pays a history-robust first-query-per-block prefix at erasure price 55/256 with G_(1/2) eligibility; actual bias retained. Arbitrary-rest intact-block majorant proved; terminal entropy and inherited sliced-encoder price remain explicit.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_PREFIX_PROVED_LOCALLY; SPECIFIC_B05_INSTANTIATION_SOURCE_CONDITIONAL; C018_C019_FULL_FEI_OPEN; REVIEW_PENDING','claim_versions_used':['B06 R2 v2 2026-10-11 23:26Z','A003-MAXIMUM-INFLUENCE-SELECTION-NOGO v1 (source-conditional instantiation)','A056-DISJOINT-COMPOSITION v2 (A057 local independent acceptance)'],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],'source_artifacts':['REPORT.md','PROOF.md','PILOT_SPEC.json','MAIN_SPEC.json','SYMBOLIC_SPEC.json','code/check.py','code/symbolic.py','out/pilot_rows.jsonl','out/main_rows.jsonl','out/pilot_summary.json','out/main_summary.json','out/symbolic_checks.json','out/source_receipts.json'],'next_consumers':claim['next_consumers'],'next_action':'Pay a second query in a touched majority block with one signed reserve, retaining inherited erasure and full terminal outer-core entropy; test arbitrary Boolean outer seeds.','stagnant_substantive_attempts':0,'blockers':['Universal lower derivative bound unavailable; intact-block scalar price contains log(1/delta).','Touched-block inherited erasure and terminal outer-core entropy lack a common influence payment.','Independent review and supervisor mirror pending.'],'packet_ids':['A026']}
dump(ROOT/'PROGRESS.json',progress);(ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())
stamp=datetime.now(timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: Stage3 saved: biased-history intact-majority prefix paid at B/I<55/256 with half-average eligibility; 2304 exact cases PASS; terminal entropy retained; full FEI OPEN, review pending.\nNEXT: A003/A087/A094 review prefix density and price; pay second-query sliced-majority inherited erasure with a signed reserve on arbitrary outer seeds.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as o:o.write('\n'+stamp+' | Stage3 '+ROOT.name+': consumed A003 induced-bias objection; proved actual-rest intact-block majorant and all-first-query prefix at 55/256 with G_(1/2) eligibility. Pilot 48 cases/112 identities, main 2304/10752 identities/1440 scalar signs, symbolic 3193 parameters+257 binomial checks PASS. Main 30.374s, estimated memory 100 MB; no heavy job. Paid prefix only; second query and terminal outer entropy remain unpaid.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as o:o.write('\nStage3 durable facts ('+ROOT.name+'):\n- Actual-rest odd balanced encoder: F=A+gD, delta=E D^2, gamma=ghat_i,d=I_i(g) gives B_i=sum Phi(Ahat^2,gamma^2 Dhat^2) and B_i/I_i<=(gamma^2/d)log2(e/(gamma^2 delta)). Histories outside intact g may be arbitrarily biased; histories inside invalidate balance.\n- For the specified B05 outer influence types and M=2k^2 2^(2k+2)+1, any adaptive at-most-one-query-per-block prefix preserves cheap intact bits at B_i/I_i<55/256 and I_i>I/(2d), while selector remains unique maximum. General proof uses q rho<3/32 density domination, not reused uniform outer spectra.\n- Sliced inner h: B_i(A+hD)=delta[B_i(h)-Phi(mu^2,gamma^2)]+sum Phi((Ahat+mu Dhat)^2,gamma^2 Dhat^2). Maj3 after first query has inherited B_i=1,d=1/2; omitting this charge is false.\n- Prefix theorem retains E H(leaf). All blocks touched is the first unpaid node, and arbitrary delta makes the scalar log(1/delta) unbounded. No universal C018/C019 or biased selector-erasure divergence is inferred.\n')
p=json.loads(protocol.read_text(encoding='utf-8-sig'))['required_per_run']
assert set(progress)=={x.split(' (')[0] for x in p['progress_fields']}
assert set(claim)==set(p['claim_fields'])
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
receipts=[]
for path in sorted(ROOT.rglob('*')):
 if path.is_file() and '__pycache__' not in str(path):
  assert path.stat().st_size<20*1024*1024
  receipts.append({'path':str(path.relative_to(ROOT)),'sha256':sha(path),'bytes':path.stat().st_size})
for path in [AGENT/'STATUS.md',AGENT/'WORKLOG.md',AGENT/'LEARNED.md']:
 receipts.append({'path':str(path),'sha256':sha(path),'bytes':path.stat().st_size})
dump(ROOT/'out/persistence_receipts.json',{'status':'PASS','schema_fields_exact':True,'progress_delta_byte_identical':True,'files':receipts,'mirror':'UNVERIFIED','independent_review':'PENDING','recorded_at':stamp})
print(json.dumps({'status':'PASS','files_receipted':len(receipts),'claim_fields':len(claim),'progress_fields':len(progress),'run_id':ROOT.name}))
