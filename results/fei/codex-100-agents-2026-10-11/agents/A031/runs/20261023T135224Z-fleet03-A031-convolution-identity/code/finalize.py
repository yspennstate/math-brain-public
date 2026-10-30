from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).resolve().parent.parent;A=R.parent.parent;ROOT=A.parent.parent
def rd(p):return p.read_text(encoding='utf-8')
def load(p):return json.loads(rd(p))
def save(p,s):p.write_text(s,encoding='utf-8')
def js(p,o):save(p,json.dumps(o,ensure_ascii=False,indent=2)+'\n')
sha=lambda b:hashlib.sha256(b).hexdigest()
stamp=datetime.now(timezone.utc).isoformat()
ck=load(R/'out/CHECK.json');pilot=load(R/'out/PILOT.json');rep=load(R/'out/REPRODUCE.json')
assert ck['status']==rep['status']==pilot['status']=='PASS'
assert ck['cases']==15360 and rep['transport_cases']==2161 and rep['weighted_CS_cases']==29241
peers={
'A033':ROOT/'agents/A033/runs/20261023T123045Z-fleet03-A033-derivative-hierarchy',
'A035':ROOT/'agents/A035/runs/20261023T132111Z-fleet03-A035-signed-cancellation-countersearch',
'A097':ROOT/'agents/A097/runs/20261023T121505Z-fleet03-A097-cross-route-transfer'}
claims=[];used=[];sources=[]
snap=R/'out/source_snapshots';snap.mkdir(exist_ok=True)
for who,folder in peers.items():
 for name in ['CLAIMS.json','DERIVATION.md' if who!='A097' else 'PROOF.md']:
  p=folder/name;data=p.read_bytes();target=snap/(who+'_'+name);target.write_bytes(data)
  sources.append({'source':str(p),'snapshot':target.relative_to(R).as_posix(),'sha256':sha(data)})
 if who=='A097':continue
 c=next(c for c in load(folder/'CLAIMS.json') if c['claim_id'].startswith(who+'-'))
 assert sha(c['exact_statement'].encode('utf-8'))==c['statement_sha256']
 c['review_records'].append({'reviewer':'A031','status':'HOLDS_NO_REPAIR_AT_STATED_SCOPE','source_statement_sha256':c['statement_sha256'],'source_proof_sha256':sha((folder/'DERIVATION.md').read_bytes()),'artifacts':['DERIVATION.md section1','out/REVIEW_'+who+'.json','code/reproduce.py'],'scope':'Independent chain-rule equality reconstruction and actual Boolean witness/global optimum. No arbitrary-core source or universal class necessity imported.'})
 c['status']='INDEPENDENT_SCOPED_REVIEW_HOLDS_NO_REPAIR'
 claims.append(c);used.append({'claim_id':c['claim_id'],'version':c['version']})
old_id='A031-SHARP-COMPATIBLE-PROFILE-GHOST-CAPACITY'
prev=next(c for c in load(A/'runs/20261023T113108Z-fleet03-A031-convolution-identity/CLAIMS.json') if c['claim_id']==old_id)
review_copy=next(c for c in load(peers['A033']/'CLAIMS.json') if c['claim_id']==old_id)
assert prev['statement_sha256']==review_copy['statement_sha256']
ack={'claim_id':old_id,'version':1,'statement_sha256':prev['statement_sha256'],'source':str(peers['A033']/'REVIEW_A031.md'),'review_records':review_copy['review_records'],'statement_binding':'MATCHES_CURRENT_PRIOR_RUN','verdict':'ACKNOWLEDGED_SCOPED_HOLDS'}
js(R/'out/PREVIOUS_REVIEW_ACKNOWLEDGED.json',ack)
save(snap/'A033_REVIEW_A031.md',rd(peers['A033']/'REVIEW_A031.md'))
sources.append({'source':str(peers['A033']/'REVIEW_A031.md'),'snapshot':'out/source_snapshots/A033_REVIEW_A031.md','sha256':sha((snap/'A033_REVIEW_A031.md').read_bytes())})
for label,p in [('B07_STREAM_NOTES',ROOT/'claude/B07/STREAM_NOTES.md'),('EXECUTION_PROTOCOL',Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))]:
 data=p.read_bytes();target=snap/(label+p.suffix);target.write_bytes(data);sources.append({'source':str(p),'snapshot':target.relative_to(R).as_posix(),'sha256':sha(data)})
sources.append({'source':str(ROOT/'BOARD.md'),'snapshot':'out/BOARD_READ.md','sha256':sha((R/'out/BOARD_READ.md').read_bytes()),'revision':'2026-10-23 13:48 UTC snapshot; live board may advance'})
js(R/'out/SOURCES.json',sources)
newid='A031-QUANTITATIVE-FINE-COMPATIBILITY-TARIFF'
statement=('Let p+,p- be complete finite child laws absolutely continuous with respect to a complete inherited mean m, '
'and let prescribed normalized block profiles r+,r- average to pi(m), with finite coarse KL. '
'Let M be the minimum mean KL over complete references R_tau of profiles r_tau and full mean m, and L the mean coarse KL. '
'On each doubly occupied block set a_tau=p_tau(block), kappa_tau=p_tau(.|block), '
'e=r+*kappa+ + r-*kappa- -2m, W=r+^2/a+ + r-^2/a-. '
'On each singly occupied block define o=sum(r_tau*kappa_tau-2m)_+. Then '
'(M-L)*ln(2)>=Phi=sum_double ||e||_1^2/(4W)+sum_single a_tau*o^2/r_tau^2. '
'Phi>0 iff a fine attainability test fails; wholly actual-zero blocks contribute zero and all ghosts remain. '
'The common multiplier1 is optimal even for actual positive-influence Boolean child spectra: f=x*h2 with h2 the two-bit point defect, '
'one block and inherited m=((1+2s)/4,(1+2s)/4,(1-2s)/4,(1-2s)/4), 0<s<1/2, '
'has M*ln2=-ln(1-4s^2)/2, Phi=2s^2 and their ratio tends to1. Its FULL transaction is exactly0, '
'since JS=occupancy=0 and old marginal KL=M. For any declared finite complete adaptive tree with current references '
'and these class constraints, define the original margin A=W-U-CE(P_root,Q_root), with W the owner and U all old debits. Payment requires '
'sum reach*(L+Phi/ln2-JS-D(actual_marginal||inherited_m)-actual_occupancy_KL)<=A; negative terms must be retained. '
'This is generic reference geometry applied to actual Boolean witnesses, not an initial Boolean admission bound or universal necessity claim.')
first='A model/policy-required class and noncircular influence-priced unused ORIGINAL payer for arbitrary Boolean cores remain unproved; neither this fixed-mean class nor the floor class is universally forced.'
claims.append({'claim_id':newid,'version':1,'exact_statement':statement,'hypotheses':['Finite complete normalized laws, both physical children and all reference-only atoms retained.','Full-mean compatibility and prescribed profiles are explicit additional obligations; finite coarse KL.','Bits for M,L,JS,KL; Phi is in natural-log units.','Tree corollary retains every old debit, actual reach and negative credit; no positive-part replacement or renewed bank.'], 'statement_sha256':sha(statement.encode('utf-8')),'contributors':['fleet03/A031'],'proof_source':{'path':'DERIVATION.md','sha256':sha((R/'DERIVATION.md').read_bytes())},'proof_dependencies':['KL conditional chain rule and elementary log-sum/Pinsker, proved locally.','Triangle and weighted Cauchy-Schwarz on within-block reference errors.','Actual Boolean signed child identities and full convolution; checked directly.','Existing A033/A035 criteria independently reconstructed, not assumed as an initial source.'],'review_records':[{'reviewer':'A031 author','status':'ANALYTIC_PROOF_AND_EXACT_CERTIFICATES_PASS_EXTERNAL_REVIEW_PENDING','artifacts':['out/CHECK.json','out/REPRODUCE.json'],'independence':'Two implementations by same author; external peer review remains pending.'}],'status':'AUTHOR_PROVED_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['Any larger uniform multiplier on Phi under the stated general inherited-mean hypotheses, even on actual Boolean splits.'],'first_unproved_line':first,'next_consumers':['A033','A035','A094','A096','A097','B07 Claude lead']})
js(R/'CLAIMS.json',claims)
pr={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B07','packet_id':'A031','gap_id':'C024-required-fine-reference-class-and-original-payer','attempt_id':'stage21-quantitative-fine-tariff','method':'Consume two new fine-attainability dependencies; reconstruct their exact Boolean optimizers; derive explicit quantitative gap by conditional KL, mass overflow and weighted L1; actual Boolean sharpness; same-owner dual test.','mathematical_delta':'Replaces strict/nonquantitative fine separation by explicit dimension-free Phi with optimal common constant; preserves old-KL/JS cancellation; two scoped peer reviews completed and previous ghost theorem acceptance acknowledged.','deliverable_status':'LOCAL_COMPLETE_PENDING_SUPERVISOR_COPY','mathematical_status':'SCOPED_AUTHOR_PROOF_EXACTLY_CHECKED_NEW_THEOREM_REVIEW_PENDING; FULL_FEI_OPEN','claim_versions_used':used+[{'claim_id':old_id,'version':1,'use':'A033 acceptance acknowledged, not a logical premise of new bound'}],'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version']} for c in claims],'source_artifacts':['DERIVATION.md','out/CHECK.json','out/PILOT.json','out/REPRODUCE.json','out/TRANSPORT_CERTIFICATES.json','out/REVIEW_A033.json','out/REVIEW_A035.json','out/PREVIOUS_REVIEW_ACKNOWLEDGED.json','out/SOURCES.json'],'next_consumers':['A033','A035','A094','A096','A097','B07 Claude lead'],'next_action':'Instantiate a model-required class; use the fixed-mean quantitative dual only if that compatibility is actually required, otherwise use the correct floor-class minimum. Pay full M-JS-oldKL-occupancy from one actual unused original allowance or price arbitrary-core initial source.','stagnant_substantive_attempts':0,'blockers':[first,'New quantitative theorem external peer review pending; same-author reproduction is not external review.','Supervisor publication unverified.','Brain self-care degraded: model100.3h/state84.9h/dream35.6h stale at fresh wake; personal-context freshness affected.'],'packet_ids':['A031']}
js(R/'PROGRESS.json',pr);js(R/'PACKET_DELTA.json',pr)
report=f'''# A031 stage21: quantitative fine-compatibility tariff

## exact target, quantifiers, hypotheses and units

Full FEI is OPEN. For arbitrary finite complete child laws and supplied inherited mean, quantify the minimum fine KL in excess of the coarse invoice under explicitly declared pointwise-mean and block-profile constraints. Theorem: (M-L)ln2>=Phi, with Phi the sum of doubly occupied mismatch terms ||e||1^2/(4W) and singly occupied overflow terms a*o^2/r^2. All terms, zeros and quantifiers are in CLAIMS.json and DERIVATION section2. The common coefficient is optimal even on actual positive-influence Boolean splits. This is generic reference transfer; it is not the lead's still-open F^4=1 initial-admission target.

## sources actually read, revisions and theorem locators

Execution protocol v2 in full; current BOARD snapshot13:48 UTC, B07 STREAM_NOTES v2, own STATUS/LEARNED/prior stage20. A033 run20261023T123045Z DERIVATION1-3 and REVIEW_A031; A035 run20261023T132111Z DERIVATION1-4; A097 run20261023T121505Z PROOF1-5. The latter differs from its older DERIVATION filename; intake corrected to the actual current PROOF. A098 already reviews that declared-floor payment, so no duplicate full-chain review is claimed here. out/SOURCES.json binds retained snapshots, including the immutable board read; no new claim relies on a fresh audit of the older threshold/percolation papers.

## complete derivation or exact first unsupported line

DERIVATION gives the complete proof. Subtract the coarse KL by its exact chain rule. Conditional Pinsker bounds the remaining mean KL by (1/4)sum a*||E||1^2/r^2 in natural-log units. For two occupied children E++E-=-e, and weighted Cauchy-Schwarz gives the explicit mismatch term. For one occupied child a componentwise capacity violation forces removal and replacement of o mass, so ||E||1>=2o. Thus Phi is positive exactly on A035's obstruction set, including ghosts; no compactness-only quantitative inference is used.

Sharpness is the actual Boolean f=x*point-defect2. With one block and a slight inherited-mean tilt, exact Mln2=-ln(1-4s^2)/2 and Phi=2s^2 have ratio tending to1 by elementary integral bounds. The FULL CE transaction is zero, because old marginal KL equals M and JS/occupancy vanish. Positive Phi is not an unpaid invoice. A033's boundary optimizer and A035's rational interior KKT optimizer independently HOLD, with their stated negative complete net bills and no repair. Their equality criteria are generic and full-mean compatibility is an extra obligation. A097's event-floor class does not impose that mean constraint, so these are distinct admissibility problems.

The same-owner tree dual test retains negative credits: a proposed unused original allowance A must be at least the reached sum of L+Phi/ln2-JS-old marginal KL-actual occupancy KL for the declared current references. This is a necessary test for that policy, not a universal requirement.

First unsupported universal line: {first}

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede search: out/FROZEN_SPEC.json and out/INDEPENDENT_SPEC.json. Commands use the explicit current run directory and python -X utf8; no dimension escalation or floating mathematical test.

* code/check_gap.py --pilot: {pilot['cases']} cases, {pilot['checks']} checks, {pilot['seconds']:.3f}s; PASS.
* code/check_gap.py: ALL256 labelled three-bit tables at fixed physical query0, all15 remaining-label partitions,2 inherited means,2 compatible templates and2 candidate fine laws per case: {ck['cases']} cases, {ck['strict_fine_gap_cases']} strict fine-gap cases, {ck['checks']} checks, {ck['seconds']:.3f}s; PASS. Full signed Walsh convolution and signed physical child identities checked. Exact Fraction prime-log forms with40-term atanh intervals and proved tails establish each comparison.
* code/reproduce.py: independent direct character sums, exact KKT and integer-power witness signs, full incoming-reference occupancy check; {rep['transport_cases']} exact three-cell transport fixtures and {rep['weighted_CS_cases']} weighted L1 certificates; {rep['checks']} checks, {rep['seconds']:.3f}s; PASS. Four rational sharpness parameters retained. No source helper imported. Same author, not external peer review.

out/TRANSPORT_CERTIFICATES.json contains explicit finite box/kink-vertex transport attainers; outputs include both peer reviews and exact source-statement-bound acknowledgement of A033's acceptance of our previous ghost theorem. Independent natural-log lower certificates exceed the new witness Phi values1/108 and1/12. Proofs, not the finite census, establish all finite dimensions and the sharp limiting constant.

Estimated memory80MB primary/20MB independent; no job expected above300MB, no heavy or GPU job, no detached launch, no formal Lean claim. Governor ts stayed13:57:59 across reads more than30s apart; no service restart or shared configuration change. Personal wake is degraded/unverified: model100.3h,state84.9h,dream35.6h stale; personal-context freshness is affected and not used as mathematics.

## proof dependencies and changed downstream conclusions

A033-NONISOSPECTRAL-COMPATIBILITY-ATTAINMENT@1 and A035-MISMATCHED-MEAN-FINE-ATTAINABILITY@1 now have independent A031 scoped reconstructions without repair. A033's prior acceptance binds the current stage20 statement hash; acknowledged in out/PREVIOUS_REVIEW_ACKNOWLEDGED.json. The NEW theorem is author-proved with exact certificates and awaits independent peer review. It improves strict fine separation to an explicit optimal-scale tariff and tree dual. Initial Boolean source, universally mandatory constraints and full FEI remain unproved. Signs are combined into actual children before any norm inequality; original signed Booleanity is tested on actual witnesses, not replaced by generic normalization.

## one next mathematical action and independent reviewer

A096/A097 should instantiate a reference class actually required by a surviving policy, with its incoming full law and actual unused original allowance. Apply the fixed-mean dual only if full-mean compatibility is part of that policy; otherwise price the appropriate floor class. Compare the complete reached bill after JS, old KL and occupancy, retaining all siblings and old bookings. Independent reviewer requested for the new bound/sharpness: A033 or A035, with A094 for the whole account. No message sent; handoff is in these artifacts for the supervisor.

## actual persistence receipts or precise save blocker

Four protocol files, complete derivation, both scripts, frozen specs, exact receipts, source snapshots and transport certificates saved. Rolling STATUS/WORKLOG/LEARNED updated. out/MANIFEST.json and out/READBACK.json give final hash/field/limit verification. No git, brain writes, shared-tree mutation, service changes or other-agent file writes. Supervisor copy and remote verification remain pending. Scoped theorem completion is distinct from full FEI, external review and publication.

**Universal bridge:** C024 moves from a qualitative fine-compatibility failure to the explicit quantitative tariff Phi, positive exactly on the full obstruction set, with optimal common constant even for actual Boolean splits. C019 gains the reached same-owner dual inequality with every negative JS/old-KL/occupancy credit retained. What remains is a policy-required class and actual noncircular original payer for arbitrary cores; neither a fixed-mean constraint nor a declared floor alone supplies them. Testing those real constraints against the complete dual is the shortest route to full FEI because it can certify unavoidable whole-policy expenditure, while another optional profile or isolated source family cannot.
'''
save(R/'REPORT.md',report)
save(R/'out/CHECKPOINT.md',f'{stamp}: Stage21 mathematical work complete locally. Two peer criteria HOLD; explicit quantitative fine tariff proved with optimal common constant and actual Boolean zero-net sharpness. Primary15360 cases and independent2161 transport/29241 CS fixtures PASS. External new-bound review, universal supplier/class and supervisor copy pending. NEXT: instantiate genuinely required constraints and pay full net from one original allowance.\n')
save(A/'STATUS.md','STATE: Stage21 saved: A033/A035 fine criteria independently HOLD; explicit quantitative fine tariff with optimal Boolean sharpness proved/exactly checked; prior ghost theorem accepted; FEI open.\nNEXT: A033/A035 review tariff; A096/A097 instantiate REQUIRED class and actual unused original payer, retaining JS/old KL/occupancy/all terminals; F^4=1 initial admission remains open.\n')
marker='## Stage21 (2026-10-23 13:52 UTC)'
for name,body in [('WORKLOG.md',f'''Consumed current A033/A035 fine criteria and A097 declared-floor scope; independently reconstructed both fine witnesses/global optima without repair. Derived (M-L)ln2>=Phi from conditional Pinsker, double-block mismatch and single-block overflow, including all ghosts. Optimal common constant proved by actual f=x*point-defect2 with oldKL=M and COMPLETE net0. Primary {ck['cases']} cases/{ck['checks']} checks and independent {rep['checks']} checks PASS. No new initial source/class necessity proved; new theorem peer review pending. Source intake initially selected old A097 DERIVATION by filename; corrected to latest PROOF before deriving any downstream conclusion. No failed mathematical search. Saved {R.name}.'''),('LEARNED.md','''For arbitrary inherited mean m and declared compatible profiles, the sharp criterion has a quantitative lower bound: (M-L)ln2>=sum_double ||r+kappa+ + r-kappa- -2m||1^2/[4(r+^2/a+ +r-^2/a-)]+sum_single a*o^2/r^2, o=sum(r*kappa-2m)_+. It is positive iff a fine equality/capacity test fails. Generic geometry, NOT F^4=1 admission. The common constant1 is optimal even on actual Boolean f=x*point-defect2: inherited m=(1+2s,1+2s,1-2s,1-2s)/4, one block; Mln2=-ln(1-4s^2)/2, Phi=2s^2, but oldKL=M so full net0. Never turn positive fine tariff into an unpaid charge by dropping JS/oldKL/occupancy. A097 floor class has NO pointwise mean condition; do not import one silently. A033/A035 v1 independently HOLD; previous A031 ghost theorem accepted with exact statement-hash match. New tariff proof/reproduction saved in stage21, peer review pending.''')]:
 p=A/name;t=rd(p)
 if marker not in t:save(p,t+'\n'+marker+'\n'+body+'\n')
# Final readback is separate from the mathematical checks.
proto=load(snap/'EXECUTION_PROTOCOL.json')['required_per_run'];passed=[]
assert set(pr)=={x.split(' (')[0] for x in proto['progress_fields']};passed.append('progress fieldset exact')
assert load(R/'PACKET_DELTA.json')==load(R/'PROGRESS.json');passed.append('packet copy exact')
for c in load(R/'CLAIMS.json'):
 assert set(c)==set(proto['claim_fields'])
 assert sha(c['exact_statement'].encode('utf-8'))==c['statement_sha256']
passed.append('claim fields and statement hashes exact')
for h in proto['report_fields']:assert '## '+h in rd(R/'REPORT.md')
assert rd(R/'REPORT.md').rstrip().split('\n\n')[-1].startswith('**Universal bridge:**');passed.append('report fields and final bridge')
assert len(rd(A/'STATUS.md').splitlines())==2;passed.append('two-line rolling status')
for s in sources:assert sha((R/s['snapshot']).read_bytes())==s['sha256']
passed.append('source snapshot hashes match')
manifest=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name not in ['MANIFEST.json','READBACK.json'] and '__pycache__' not in p.parts:
  assert p.stat().st_size<20_000_000;manifest.append({'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())})
js(R/'out/MANIFEST.json',{'created_utc':stamp,'artifacts':manifest})
for m in load(R/'out/MANIFEST.json')['artifacts']:assert sha((R/m['path']).read_bytes())==m['sha256']
passed.append('artifact limits and manifest readback')
js(R/'out/READBACK.json',{'status':'PASS','checks':passed,'new_claim_peer_review':'PENDING','full_FEI':'OPEN','supervisor_copy':'PENDING'})
print(json.dumps({'status':'PASS','run':R.name,'claims':len(claims),'readback_checks':len(passed),'artifacts':len(manifest),'primary_checks':ck['checks'],'independent_checks':rep['checks'],'full_FEI':'OPEN'}))
