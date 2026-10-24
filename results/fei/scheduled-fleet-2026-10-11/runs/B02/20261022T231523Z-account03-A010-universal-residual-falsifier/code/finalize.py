from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
B=Path(__file__).resolve().parents[1];AGENT=B.parents[1];SHARED=AGENT.parent.parent;O=B/'out';now=datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def put(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def js(p,x):put(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
check=read(O/'CHECK.json');verify=read(O/'VERIFY.json');review=read(O/'REVIEW_A006.json');lean=read(O/'LEAN.json')
assert check['status']==verify['status']==review['status']=='PASS'
assert (check['functions'],check['scalar_triples'],check['assertions'])==(40,6448,217218)
protocolpath=Path(r'~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json');protocol=read(protocolpath)
# This is the same explicit field schema extracted at stage opening.
claimfields=['claim_id','version','exact_statement','hypotheses','statement_sha256','contributors','proof_source','proof_dependencies','review_records','status','supersedes','refutes','first_unproved_line','next_consumers']
progressfields=['protocol_revision','run_id','stream','packet_id','gap_id','attempt_id','method','mathematical_delta','deliverable_status','mathematical_status','claim_versions_used','claims_created_or_changed','source_artifacts','next_consumers','next_action','stagnant_substantive_attempts','blockers','packet_ids']
used=[{'claim_id':'A008-ALL-BOOLEAN-IMPLICANT-ROOT-NORMALIZER-PAYMENT','version':1,'use':'width-two root substatement rederived; no private-leaf corollary'},{'claim_id':'A009-ONE-MISSING-EDGE-LEAFLESS-COMPLETE-CERTIFICATE','version':1,'use':'whole source reviewed unchanged; specific NEXT extended'},{'claim_id':'A006-ANCHORED-ROOT-PACKING-CERTIFICATES','version':1,'use':'whole finite-family lower-certificate and cost-enclosure review; not a premise of new complete-cost theorem'}]
consumers=['A006','A008','A009','A086','Claude/B02','B20']
common=['Uniform physical cube; cost in bits and actual Boolean squared Fourier spectrum','Both endpoint orders, width-two positive-edge prime table, original nonempty-conditioned all-partitions queue','A single globally fixed packing-feasible weight vector; all original root exclusions, selected subsets, counts, attachments and labels paid']
def claim(cid,statement,hypotheses,dependencies):
 h=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
 return dict(zip(claimfields,[cid,1,statement,hypotheses,h,['A010'],{'path':str(B/'GROWING_MATCHING.md'),'code':['code/check.py','code/verify.py'],'certificates':['out/CHECK.json','out/VERIFY.json']},dependencies,[{'reviewer':'A010','verdict':'AUTHOR_ALL_PARAMETER_DERIVATION_AND_SEPARATE_EXACT_REPLAY; NOT INDEPENDENT_AGENT_ACCEPTANCE','timestamp_utc':now,'formal_status':lean['status']}],'AUTHOR_PROOF_WITH_EXACT_FINITE_VALIDATION; INDEPENDENT_AGENT_REVIEW_PENDING',[],[],None,consumers]))
generic=claim('A010-GENERIC-WIDTH-TWO-FOREST-MASS','For every finite nonempty simple graph edge-prime table, both endpoint orders, and one common feasible weight 0<lambda<=1 with pi=1/4 and D=(1+lambda/4)^|E|-1, every nonempty output set A consisting of incident vertices admits a distinct actual source-SCC-rooted queue event with original probability at least (lambda/72)^|A|/D. This includes all root rarities and exclusions, block subsets, child counts, attachment compositions, fixed chronology and child labels. Any number of roots is allowed. Therefore the complete all-partitions output mass is at least this amount. This is a mass lower bound/cost upper bound, not a lower certificate for the variational infimum.',common+['Every selected output coordinate is incident to some table edge; positive common lambda'],[{'source':'forests.tex','use':'original queue probabilities and partition admissibility; locally reconstructed event'}])
matching=claim('A010-GROWING-DELETED-MATCHING-COMPLETE-COST','For all integers 2<=a<=b and 0<=k<=a, let G be K_(a,b) with k disjoint matching edges deleted and f_G its actual uniform Boolean edge DNF. On precisely its surviving positive edge primes, fix both endpoint orders, pi=1/4 and lambda_e=1/b. For the SAME original all-partitions queue, D=(1+1/(4b))^(ab-k)-1 and complete nonempty output cost C=sum_(A!=empty) fhat_G(A)^2 log2(1/Q_G(A)), there is an explicit distinct-run subfamily of complete cost less than1255I(f_G)/72<18I(f_G), hence the full queue cost and any variational infimum containing this admissible representation obey that upper bound. The result includes all root/leaf factors, arbitrary growing k, and the leafless subfamily a,b>=3. No added primes, private leaves, controller, sampled-set weights, optimal-weight claim, or arbitrary-deletion transfer is used.',common+['2<=a<=b; deleted edges are a matching of size0<=k<=a; lambda=1/b'],[{'claim_id':generic['claim_id'],'version':1},{'claim_id':used[0]['claim_id'],'version':1,'use':'only width-two root term, reconstructed in section4'}])
claims=[generic,matching];js(B/'CLAIMS.json',claims)
nextaction='Use the same generic width-two forest and derive exact weighted Fourier label payment for overlapping deleted neighborhoods (start degree-two deleted paths/cycles); distinguish complete original-reference cost from optimization gap and retain all positive global weights/posteriors in lower-certificate tests. A006/A009 review the new two claims.'
artifacts=['GROWING_MATCHING.md','REVIEW_A006.md','REVIEW_A009.md','FROZEN_SPEC.json','VERIFY_SPEC.json','REVIEW_SPEC.json','out/CHECK.json','out/VERIFY.json','out/REVIEW_A006.json','out/LEAN.json','out/SOURCES.json','out/RECEIPTS.json']
progress=dict(zip(progressfields,['2026-10-11-execution-v2',B.name,'B02','A010','G-J-COST','A010-growing-matching-complete-cost','Whole-source exact reviews; generic source-SCC width-two forest; exact Boolean weighted Fourier moments; rational logarithm and probability replay','Closed the growing-deleted-matching NEXT: unchanged-table complete cost<1255I/72<18I for every size. Generic width-two event pays arbitrary root count. Reconstructed A006201 dual certificates,5878 complete runs,67 cost/infimum enclosures. No variational-growth falsifier found.','COMPLETE_LOCAL_ARTIFACTS','SCOPED_AUTHOR_PROOF_AND_EXACT_CERTIFICATES; INDEPENDENT_AGENT_REVIEW_PENDING; FULL_FEI_OPEN; '+lean['status'],used,[{'claim_id':c['claim_id'],'version':1} for c in claims],artifacts,consumers,nextaction,0,['Universal complete original-reference payment remains unproved for overlapping deleted neighborhoods and arbitrary Boolean prime tables. New author proof has no independent-agent acceptance. Supervisor mirror/adoption not verified. Brain self-care degraded: model of Yitzchak and state-of-mind required sources stale; personal-state-dependent guidance unverified.'],['A010']]))
js(B/'PROGRESS.json',progress);js(B/'PACKET_DELTA.json',progress)
sourcepaths=[protocolpath,SHARED/'BOARD.md',SHARED/'claude/B02/STREAM_NOTES.md',Path(r'~/mop_fei100/reports/fei-2026-10-11/source_material/reductions/paper/forests.tex')]
for agent,run,names in [('A006','20261021T182437Z-account03-A006-posterior-forest-optimization',['PROOF.md','CLAIMS.json','out/CHECK.json','out/COST.json']),('A009','20261022T220926Z-account03-A009-fractional-incidence-optimization',['ONE_MISSING_EDGE.md','LEAFLESS_CERTIFICATE.md','CLAIMS.json']),('A008','20261021T234312Z-account03-A008-gate-label-compression',['ROOT_PAYMENT.md'])]:
 sourcepaths.extend(SHARED/'agents'/agent/'runs'/run/name for name in names)
sources=[]
for p in sourcepaths:
 assert p.exists(),p
 sources.append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'receipt_timestamp_utc':now})
js(O/'SOURCES.json',sources)
report=f'''# A010: universal residual falsifier, growing deleted matching

## exact target, quantifiers, hypotheses and units

For every2<=a<=b and0<=k<=a, pay the complete SAME original-reference cost on the actual edge DNF K_(a,b) minus a k-edge matching. Result: C<1255I/72<18I, with global lambda=1/b, both endpoint orders, and the unchanged surviving prime table. GROWING_MATCHING.md states all conventions and proves the bound. A second all-size lemma gives original queue mass >=(lambda/72)^|A|/D for any width-two graph output on incident vertices. Costs are bits; all physical variables are uniform independent bits. No universal FEI closure or growing variational-infimum counterexample is claimed.

## sources actually read, revisions and theorem locators

Reread current BOARD.md, B02 STREAM_NOTES.md, own STATUS.md, and execution-v2 protocol; earlier campaign packet/paper context remains read-only. Mathematical queue source: forests.tex, original conditioned root/count/subset/attachment construction. Whole current source reviews: A006 anchored-root-packing stage20261021T182437Z (PROOF.md sections1-5, saved complete certificates and cost enclosures); A009 stage20261022T220926Z (ONE_MISSING_EDGE.md and its entire LEAFLESS_CERTIFICATE.md calibration); A008 stage20261021T234312Z ROOT_PAYMENT.md, width-two root substatement only. Exact paths and byte hashes at finalization are in out/SOURCES.json. Source conventions for statement hashes differ; no false corruption diagnosis is made.

## complete derivation or exact first unsupported line

GROWING_MATCHING.md sections1-5 contain the entire all-parameter argument. Assign coordinates to actual incident primes, form disjoint owned blocks, and take a source-SCC-rooted breadth-first forest. The exact count/composition inequality pays every arbitrary-root event by (lambda/72)^|A|. Actual one-sided neighbor sums remove most label cost. Exact physical spectrum and weighted moments give R log(b/a)<=(50/9)I and M log b<=(9/2)I, with I=I0+2k(a+b-4)2^(-a-b)>=I0; no quadratic coefficientwise loss in k is used. Cube-cut/implicant-fiber packing reconstructs the same root payment<9I/8. Finally log72<25/4, so total<1255I/72. The first unsupported universal line is analogous spectral label payment for arbitrarily overlapping deleted neighborhoods or arbitrary Boolean prime tables. A selected-run mass lower bound transfers to a full-family COST UPPER bound; it does not transfer a restricted-family variational LOWER bound.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede each search. Run commands from this directory: python -X utf8 code/check.py --pilot; python -X utf8 code/check.py; python -X utf8 code/verify.py; python -X utf8 code/review.py. Pilot:10 actual functions,5706 assertions,0.217s. Full check:40 actual functions2<=a<=b<=5, all0<=k<=a,12496 truth entries, every nonempty Fourier set,6448 scalar triples through b=32,217218 exact assertions,13.412s. Independent no-helper-import replay:10 functions,390 histories,462 singleton-label choices,270 cube subsets,6476 assertions,0.552s. Whole A006 replay:67 graphs,201 rational dual support certificates,5878 reconstructed complete runs,67 complete-cost and variational enclosures,5786 assertions,2.532s. Arithmetic is integer/Fraction, with proved atanh-series logarithm remainders. These finite checks support the explicit proof and do not replace its quantifiers. Lean key count-ratio attempt: {lean['status']}; no Lean verification of the complete theorem is asserted. All searches used at most80MB by frozen estimate; no heavy job or dimension escalation. Before the formal setup attempt, memok exited0 (4.6GB physical and20.1GB commit free).

## proof dependencies and changed downstream conclusions

The generic forest uses original queue mechanics, locally reconstructed. The complete theorem additionally uses the A008 root substatement, rederived here, and exact Boolean moment identities. A009's whole one-missing-edge statement and undamaged calibration hold unchanged; its growing-matching NEXT is now closed by an author proof pending independent-agent review. A006's anchored/lifted cuts, finite dual gaps and COMPLETE cost enclosures hold unchanged; its separator is inadmissible at the hub, not a Boolean counterexample. Its upstream A010 cap authorship is disclosed. The new upper bound rules out unbounded variational cost on this matching-deletion family within any representation class containing our admissible reference; it says nothing about infima over unrelated restricted representation classes. All-weight lower-certificate conclusions remain scoped to their complete saved families.

## one next mathematical action and independent reviewer

{nextaction} The generic forest removes the arbitrary-root combinatorial obstacle, so the next work should price spectral occupation rather than add another root-law relaxation. New claims require independent A006/A009 mathematical review; no external acceptance is fabricated.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and compatibility PACKET_DELTA.json are written locally with the protocol's exact fields; code, frozen specs, proofs, source reviews and exact outputs are retained. out/RECEIPTS.json records file SHA256 values and sizes, and out/FINAL_VALIDATION.json records schema/readback checks. STATUS.md is exactly two lines; WORKLOG.md and LEARNED.md are appended. All research writes stay inside A010. Supervisor mirroring and shared-registry adoption are unverified; no git operation is authorized. No computation is left running by this stage. Brain self-care is degraded/unverified: required model-of-Yitzchak and state-of-mind sources are stale, so personal-state-dependent guidance remains unverified; mathematical certificates are local computations independent of those notes.

Universal bridge: This stage advances C020 / PI-J whole-set witness cost from one deleted edge to an arbitrarily growing deleted matching, with complete original-reference payment<1255I/72<18I and a reusable arbitrary-root width-two event bound. It does not close the universal bridge: overlapping neighborhoods and arbitrary Boolean prime tables still lack spectral label payment. Deriving their weighted moments on the same physical function and unchanged prime table is the shortest next route toward full FEI because the queue event construction already works; another finite relaxation-gap improvement would not pay that remaining bill.
'''
put(B/'REPORT.md',report)
put(AGENT/'STATUS.md','STATE: A010 saved: all-size original-reference C<1255I/72<18I for K_ab minus any matching;217218 full-check assertions,6476 independent replay assertions; A006 whole67-cost review PASS; new independent-agent review pending; FEI OPEN.\nNEXT: A006/A009 review generic width-two forest and matching payment; derive exact weighted spectral label payment for overlapping deleted paths/cycles on the same actual prime table.\n')
entry=f'\n{now} stage {B.name}: Closed growing-deleted-matching NEXT with original-reference complete cost<1255I/72<18I for all sizes; generic width-two source-SCC forest pays arbitrary roots. Full40-function/6448-triple exact check217218 assertions; independent390-event replay6476 assertions. Whole A006 review201 duals/5878 runs/67 cost enclosures passes5786 assertions; whole A009 construction/calibration reviewed unchanged. Formal count step {lean["status"]}. New claims independent-agent review pending; arbitrary overlapping deletions and full FEI open. Only local persistence; brain self-care degraded/unverified.\n'
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write(entry)
lesson='\n'+now+' — Growing matching lesson: use owned blocks of sizes1/2 and a source-SCC-rooted forest; every original event factor gives numerator >=(lambda/72)^degree, regardless of root count. For K_ab minus k matching edges, q=u+v+(k-1)uv and I=I0+2k(a+b-4)uv; true mixed weighted Fourier moment is linear in k, not quadratic. Exact moments plus unchanged root payment yield complete C<1255I/72<18I. One explicit admissible upper bound excludes variational growth for classes containing it, but cannot provide lower bounds. Arbitrarily overlapping missing neighborhoods are the next unpaid spectral step. See '+str(B/'GROWING_MATCHING.md')+'.\n'
with (AGENT/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:f.write(lesson)
assert read(B/'PROGRESS.json')==read(B/'PACKET_DELTA.json')
for c in read(B/'CLAIMS.json'):
 assert set(c)==set(claimfields)
 assert c['statement_sha256']==hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
assert set(progress)==set(progressfields)
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipts=[]
for p in sorted(B.rglob('*')):
 if not p.is_file() or p.name in ('RECEIPTS.json','FINAL_VALIDATION.json'):continue
 raw=p.read_bytes();assert len(raw)<20*1024*1024
 if p.suffix in ('.json','.md','.py','.lean'):raw.decode('utf-8')
 receipts.append({'path':str(p.relative_to(B)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
js(O/'RECEIPTS.json',receipts)
js(O/'FINAL_VALIDATION.json',{'status':'PASS','timestamp_utc':now,'exact_claim_fields':True,'exact_progress_fields':True,'compatibility_equal':True,'claim_hashes_checked':len(claims),'all_files_under20MB':True,'utf8_readback':True,'two_line_status':True,'artifact_receipts':len(receipts),'formal_status':lean['status'],'independent_agent_acceptance':False,'full_FEI':'OPEN','remote_mirroring':'UNVERIFIED'})
print(json.dumps({'status':'PASS','claims':len(claims),'artifacts':len(receipts),'report_bytes':(B/'REPORT.md').stat().st_size,'formal_status':lean['status']}))
