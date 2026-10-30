from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1]
RUN=R.name;stamp=datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
hist=read(R/'out/HISTORY.json');replay=read(R/'out/HISTORY_REPLAY.json');child=read(R/'out/CHILD_REVIEW.json')
assert hist['status']==replay['status']==child['status']=='PASS'
assert hist['positive_policies']==replay['positive']==30 and replay['negative']==214
checks=sum(x['assertions'] for x in (hist,replay,child))
sources=[Path('~/AGENTS.md'),Path('BOARD.md'),Path('claude/B03/STREAM_NOTES.md'),Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
S=Path('agents/A012/runs/20261023T053904Z-fleet03-A012-sparse-activation-accounting')
sources += [S/p for p in ['REPORT.md','DERIVATION.md','REFEREE_NOTES.md','CLAIMS.json','out/NEXT_TARGET.json','code/child_exact.py','code/fixtures.py','out/CHILD_author.json','out/CHILD_replay.json']]
save(R/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sources])
review_statement='The NEW increment of A012-DISJOINT-PRIVATE-MUX-ADMISSION@7 independently reconstructs: the separately semiconvex amplitude entropy has lower coordinate curvature -2/ln2, independent quotient-row rounding gives B_z<=4min(d,1-d)+(rhoG+rhoH)/ln2 for both actual means in one common affine Fourier coset of rank<=3; the full calibrated parent reference retains D_F=(D_G+D_H)/2. The variance bill is paid once from original child stock after old bookings. An independent direct-character-bitmask certificate covers all65536 four-bit Boolean children and proves nonconstant H<=4I-1/4, supporting the whole-private15/16-dominated reference allowance CE<=4I-1/8 and the bounded finite-node reserve. This scoped review accepts only the NEW transfer/source increment conditional on previously reviewed v6 and C005, not the earlier A013-credited full syntax chain or arbitrary history closure.'
history_statement='For the exact six-bit Boolean parent F, G,H and inherited normalized Q in A012 v7 out/NEXT_TARGET.json, rate K=4+2/ln2, old debit b=5/(4ln2), the original post-variance child reserve R=3-(H(G)+H(H))/2 pays the physical s0 query with marginal reference Qminus(T)=Q(T)+Q(T+s0). The signed draw is tau=K/8-[H(F)-H(Qminus)], and exact rational certificates give R-tau>1/4 bit while the separate unused original selector allowance A>1/2 bit remains untouched. Both complete daughter KLs and off-target reference masses are retained. These are expected-frontier accounts, not nonnegative per-daughter certificates. Querying s1 on both s0 outcomes with twice-marginalized ORIGINAL Q and the SAME retained b gives full remaining margin K/2-H(Qminus_s0_s1)-b<-15/64 bit, even after spending A. Of all244 adaptive stop/query policies on the three shared bits, exactly30 have positive and214 negative final expected margins, independently certified. This refutes unrestricted continuation of this particular fixed-reference/old-debit rule, not FEI or v7.'
common={'hypotheses':['uniform finite Boolean cubes; normalized Fourier spectrum and physical influence','all costs bits; K=4+2/ln2; no historical reference reset, no renewed variance bank'], 'contributors':['A013/fleet03'], 'proof_source':{'derivation':'DERIVATION.md','code':['code/history19.py','code/replay_history19.py','code/review_child19.py'],'outputs':['out/HISTORY.json','out/HISTORY_REPLAY.json','out/CHILD_REVIEW.json']},'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A012','A086','A094','B03','B20']}
claims=[]
for cid,statement,status,deps,reviews in [
 ('A013-SCOPED-REVIEW-A012-V7',review_statement,'HOLDS_NEW_V7_INCREMENT_ONLY',[{'claim_id':'A012-DISJOINT-PRIVATE-MUX-ADMISSION','version':7,'scope':'NEW variance transfer, finite-child source and one-use stock only'},{'claim_id':'A013-SCOPED-REVIEW-A012-V6','version':1,'scope':'previously independently reviewed NEW pure-child/quotient increment'},{'claim_id':'C005','version':'baseline','scope':'scalar JS conversion; conditional inherited premise'}],[{'reviewer':'A013','verdict':'HOLDS_NEW_V7_INCREMENT_ONLY','independence':'Independent convexity reconstruction; direct character bitmasks/complement classes, physical edges and128th-power logs; no v7 repair supplied. Earlier A013 contribution precludes full inherited-chain acceptance.'}]),
 ('A013-ORIGINAL-CHILD-BANK-PHYSICAL-QUERY',history_statement,'PROVED_EXACT_LOCAL_PENDING_INDEPENDENT_AGENT_REVIEW',[{'source':str(S/'out/NEXT_TARGET.json'),'scope':'material actual truth tables and inherited Q, independently recomputed; no acceptance of v7 is needed for finite arithmetic'}],[])
]:
 c=dict(common);c.update(claim_id=cid,version=1,exact_statement=statement,statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),proof_dependencies=deps,review_records=reviews,status=status)
 if cid.endswith('QUERY'):c['hypotheses']=common['hypotheses']+['ONLY the exact saved six-bit target and original booking; frontier statements are in expectation']
 claims.append(c)
save(R/'CLAIMS.json',claims)
next_action='Price an actual conditional nonempty-profile/reference handoff at the s0-then-s1 frontier that pays the >15/64-bit deficit using named unspent ORIGINAL source, retaining old5/(4ln2), both full terminals and all earlier debits. A012 construct; A086/A094 independently reconstruct. Flat unchanged-booking continuation with mere marginal Q is exactly obstructed.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN,'stream':'B03','packet_id':'A013','gap_id':'G-LOWSEL-COLLISION','attempt_id':'A013-stage19-v7-review-original-child-bank-history','method':'Independent semiconvex proof reconstruction, exact complement-class child certificate, dual arithmetic all-policy history replay and source-reserve reconciliation','mathematical_delta':'NEW v7 transfer/source scoped HOLDS. Saved physical s0 query paid from SAME post-variance child reserve, >1/4 bit remains and >1/2 original selector allowance untouched. Fixed next s1 query fails full account by>15/64 bit. All244 policies classified30 positive/214 negative.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_V7_REVIEW_HOLDS; EXACT_EXPECTED_HISTORY_STEP_PROVED; ARBITRARY_HISTORY_AND_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':'A012-DISJOINT-PRIVATE-MUX-ADMISSION','version':7,'scope':'NEW increment only'},{'claim_id':'A013-SCOPED-REVIEW-A012-V6','version':1},{'claim_id':'C005','version':'baseline'}],'claims_created_or_changed':[{'claim_id':x['claim_id'],'version':1,'status':x['status']} for x in claims],'source_artifacts':['DERIVATION.md','out/SOURCE_RECEIPTS.json','FROZEN_SPEC.json','FROZEN_REPLAY.json','out/HISTORY.json','out/HISTORY_REPLAY.json','out/CHILD_REVIEW.json'],'next_consumers':['A012','A086','A094','B03','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Universal common-rank3 representation and arbitrary diminished-bank history closure are unproved.','New finite-history theorem pending independent-agent review.','Mirror/supervisor copy unobserved.','Brain self-care degraded/unverified: stale owner model and state-of-mind notes; no mathematical premise uses them.'],'packet_ids':['A013']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
report=f'''# A013 stage19: inherited physical query paid after both-private variance conversion

## exact target, quantifiers, hypotheses and units

Independently review the NEW variance/source increment of A012 v7, then price its saved actual six-bit both-private parent's physical shared query s0 with original Q, old5/(4ln2) booking and SAME diminished child stock. K=4+2/ln2<7; entropy and ideal costs in bits. The new paid result is an EXPECTED frontier account for this exact target, not a nonnegative branchwise invariant or all-function history theorem. Full FEI OPEN.

## sources actually read, revisions and theorem locators

Current BOARD B03 and relevant review/history updates, full B03 STREAM_NOTES v2, own STATUS, machine AGENTS and full execution protocol2026-10-11-execution-v2; A012 stage19 run20261023T053904Z-fleet03-A012-sparse-activation-accounting REPORT, DERIVATION, REFEREE_NOTES, CLAIMS, saved NEXT_TARGET, child certificate code and outputs, and fixture construction excerpt. Earlier campaign/paper/full-chain intake is inherited from prior stages, not claimed reread. One read-only multiwording math recall supplied neighboring local-induction warnings, not a proof premise. Exact paths/hashes are in SOURCE_RECEIPTS. Current user campaign end23Oct14:49UTC supersedes legacy protocol dates. No off-scope film/mesh message changed the task.

## complete derivation or exact first unsupported line

DERIVATION Sections1-4 contains the proof. Independently differentiating the amplitude primitive shows ln2*(L_aa+2/ln2)=ln(m/|xy|)+a^2/m-ln2>=0; continuous first derivatives join diagonal singularities. Independent row rounding loses exactly(rhoG+rhoH)/ln2 and preserves expected disagreement, so the reviewed v6 pure bound gives the NEW v7 transfer. Full disjoint-private reference calibration preserves the average of BOTH child KLs. The independent four-bit source certificate supports nonconstant CE<=4I-1/8 and one-time variance payment after old shared bookings. Scoped HOLDS excludes the A013-credited older syntax/full-chain and any unpaid history claim.

For a physical query, original-reference marginalization decreases average CE by gamma>=0 and influence by Inf_i. The EXACT signed draw is tau=K Inf_i-gamma; the weighted draws telescope along adaptive trees. This applies the known CE projection mechanism to the same-rate historical ledger, without claiming a new general CE projection theorem.

For the actual saved target, Q=P_F and the private child mixture references equal P_child, independently checked. Original post-variance CHILD reserve R=3-(HG+HH)/2 is certified in(0.7233428955,0.7251930237) bits. The s0 query has influence1/8 and consumes between0.4628046501 and0.4636133660 bits. Hence R-tau>1/4 bit; the SEPARATE unused ORIGINAL selector allowance A>1/2 bit remains untouched. The old5/(4ln2) booking and both full daughter references/KLs survive. Daughter KLs are positive, about0.262 and0.326 bit, and their off-target reference masses are retained in the saved exact distributions.

The next fixed query s1 on BOTH s0 outcomes FAILS: even the full remaining original account is<-15/64 bit with twice-marginalized Q and unchanged old booking. ALL244 adaptive shared-bit stop/query policies have independently certified signs:30 positive and214 negative. No policy uses a free reference reset or a renewed variance reserve. This is a rule obstruction, not an FEI counterexample. FIRST universal unsupported line: a genuine conditional nonempty-profile handoff/reference conversion that pays this second-query deficit from named original source, with both full terminals and the old debit retained.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede every math job. Commands: python -X utf8 code/history19.py; python -X utf8 code/review_child19.py; python -X utf8 code/replay_history19.py, run from this run directory (or with the corresponding prefixed path from A013). Child review uses32768 complement classes covering65536 actual four-bit functions, direct character bitmasks, direct physical edges and128th-power integer logs; minimum certified4I-H=1207/4096>1/4. Complete spectral/energy histograms match BOTH A012 implementations. No pair enumeration is claimed.

History author covers27 actual partial assignments and244 policy trees using rational28-term atanh logs and rigorous tails. Replay computes character sums and leaf-weighted policy bills independently, verifies exact prime-log telescoping, and signs with4096th-power integer binary-log intervals plus a20-term rational ln2 bound. Both full private and cofactor distributions are used. Replay also proves the stronger<-15/64 obstruction and explicit>1/4 retained child bank. A final rerun follows the additional off-target-mass fields/stronger sign assertion. There are {checks} assertions in the final saved outputs; this counts the FINAL output of each job once, not cumulative reruns. Observed math times: child{child['seconds']:.3f}s, history{hist['seconds']:.3f}s, replay{replay['seconds']:.3f}s. Each estimate<=80MB and cutoff50s; no>300MB job, compiler, GPU, new dimension, detached process or visible window. No Lean check is claimed.

## proof dependencies and changed downstream conclusions

NEW v7 scoped acceptance consumes the already reviewed v6 increment and conditional baseline C005; it does not reopen older A013-credited chain claims. The NEW finite historical theorem instead recomputes the saved actual Boolean target, spectra, influences and Q directly and does not require accepting any general v7 theorem. It closes A012's specified first physical query while showing the exact next inherited-reference frontier is NOT automatically covered by the remaining margin. Existing universal FEI/cover gaps stay OPEN.

## one next mathematical action and independent reviewer

{next_action} The exact target, all distributions, old booking, original bank split and next-policy witness are available in HISTORY_REPLAY and NEXT_TARGET. No external message was sent.

## actual persistence receipts or precise save blocker

All four protocol files, DERIVATION, both frozen specs, scripts and exact outputs are local under this A013 run. STATUS is two lines; WORKLOG and LEARNED append dated findings. FINAL_VALIDATION checks exact schema keys, statement hashes, matching packet/progress data, source/output hashes and the<20MB rule. Supervisor copying/GitHub ingestion is unobserved. No brain data was written. Brain self-care remains degraded/unverified (owner-model92.5h and state-of-mind77.1h stale at stage wake), affecting current owner context/personalization; these are not mathematical premises. Operational checklist status is recorded separately if available. All bounded mathematical jobs have ended.

## Universal bridge

This moves C020 by independently reconstructing NEW v7's both-private variance/source conversion and C024 by paying the saved actual s0 query from the SAME already diminished child reserve, leaving>1/4 bit and preserving>1/2 bit of original selector allowance. It also pinpoints an exact>15/64-bit failure at the next fixed interacting query. Universal quotient existence, conditional original-source handoff and arbitrary history closure remain open. NEXT targets that actual second-query deficit, the shortest path to making the paid collision a reusable universal witness step instead of adding another isolated class result.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A013 stage19 saved: NEW A012 v7 scoped HOLDS; SAME post-variance child bank pays s0, >1/4 bit remains and >1/2 original selector allowance untouched; next s1 fails by>15/64; exact checks PASS; FEI OPEN.\nNEXT: Pay actual conditional nonempty-profile handoff/reference conversion at s0-then-s1 with ORIGINAL Q, old5/(4ln2), both full terminals and SAME source; A012/A086/A094 review; no renewed variance bank.\n',encoding='utf-8')
log=f'\n{stamp} stage19 ({RUN}): NEW A012 v7 semiconvex variance/source increment independently HOLDS at scoped level; independent character/complement review covers65536 child functions, minimum4I-H>=1207/4096. Actual s0 query paid from original post-variance child R with>1/4 bit left, original selector A>1/2 untouched. Exact s0-then-s1 continuation has margin<-15/64; all244 policies classify30 positive/214 negative. Final saved math assertions={checks}. No broad history closure or full FEI claimed; A086/A094 review pending.\n'
with (A/'WORKLOG.md').open('a',encoding='utf-8') as h:h.write(log)
lesson=f'''\n{stamp} durable stage19 facts: For any physical query and normalized inherited Fourier Q, gamma=CE_parent-averageCE_child with marginal Qminus>=0; the exact SAME-rate draw is K Inf_i-gamma. Adaptive reach-weighted draws telescope, preserving full KL and old expected debits. This is an accounting identity, not a universal payment bound. For A012 v7 saved actual target, R=3-(HG+HH)/2 is ORIGINAL child bank AFTER variance payment. s0 draws<1/2 bit, leaving>1/4 and separate selector allowance>1/2 untouched. Querying s1 on both outcomes then fails full account by>15/64 with unchanged old5/(4ln2) and marginal reference; never infer arbitrary history closure or a branchwise nonnegative bank from a positive first expected margin. Both s0 daughter KLs remain positive and charged. NEW v7 semiconvex transfer/source is scoped HOLDS; older A013-credited full syntax is excluded from independent acceptance.\n'''
with (A/'LEARNED.md').open('a',encoding='utf-8') as h:h.write(lesson)
# Validate protocol schemas, actual artifacts, hashes and report headings.
protocol=read(sources[3]);pf=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
cf=protocol['required_per_run']['claim_fields']
assert set(progress)==set(pf)
for c in claims:
 assert set(c)==set(cf)
 assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
for heading in protocol['required_per_run']['report_fields']:assert '## '+heading in report
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[p for p in R.rglob('*') if p.is_file() and p.name!='FINAL_VALIDATION.json']
assert all(p.stat().st_size<20_000_000 for p in files)
save(R/'out/FINAL_VALIDATION.json',{'status':'PASS','timestamp':stamp,'checks_in_final_math_outputs':checks,'files':[{'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in files],'schema':'exact protocol key sets and statement hashes checked','rolling_files':'STATUS exact2 lines; WORKLOG/LEARNED appended','mirror':'UNOBSERVED'})
print(json.dumps({'status':'PASS','math_assertions':checks,'local_files':len(files),'max_file_bytes':max(p.stat().st_size for p in files),'run':str(R)}))
