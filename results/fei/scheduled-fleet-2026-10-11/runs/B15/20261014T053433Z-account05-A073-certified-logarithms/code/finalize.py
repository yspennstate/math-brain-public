from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy
from fractions import Fraction as F
import exact as E
R=Path(__file__).resolve().parents[1];A=R.parents[1];TEAM=A.parent.parent
S=TEAM/'agents/A085/runs/20261014T034606Z-account05-A085-certificate-adversary'
N=TEAM/'agents/A096/runs/20261014T042803Z-account05-A096-live-gap-ledger'
CANON=Path(r'~\mop_fei100\reports\fei-2026-10-11')
now=datetime.now(timezone.utc).isoformat()
def sha(raw):return hashlib.sha256(raw).hexdigest()
def write(p,obj):p.write_text(json.dumps(E.serial(obj),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def digest(c):return sha(json.dumps({k:c[k] for k in ['exact_statement','hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
summary=json.loads((R/'out/SUMMARY.json').read_text());pilot=json.loads((R/'out/PILOT.json').read_text())
assert summary['checks']==2080 and summary['status']==pilot['status']=='PASS'
a,b=E.reduced_ln(F(2),24)
sharp=(1/(2*b),1/(2*a));reserve=(1/(40*b),1/(40*a))
margin=(F(3,80)-reserve[1],F(3,80)-reserve[0])
assert a>F(2,3) and b<1 and margin[0]>F(1,1000)
write(R/'out/CONSTANT_CERTIFICATE.json',{'ln2_interval':[a,b],
 'sharp_D0_over_delta_coefficient_interval':sharp,'sharp_coefficient_display':E.decimal_interval(sharp,9),
 'reserved_fraction_upper_bound_interval':reserve,'reserved_fraction_display':E.decimal_interval(reserve,9),
 'strict_margin_below_3_over_80_interval':margin,'margin_display':E.decimal_interval(margin,9),
 'certified_margin_lower_bound':'1/1000','new_rational_core_fraction':'3/80',
 'previous_fraction':'3/64','fraction_reduction':F(3,320),'precision_terms':24,'precision_refinements':0})
source=next(c for c in json.loads((S/'CLAIMS.json').read_text()) if c['claim_id']=='A085-QUADRATIC-CONDITIONAL-REMAINDER-CERTIFICATE')
review=copy.deepcopy(source)
review['review_records'].append({'reviewer':'A073','timestamp':now,'verdict':'ACCEPT_AT_FULL_STATED_SCOPE_NO_REPAIR',
 'method':'Independent complete signed-law reconstruction; Jensen curvature proof; own physical Walsh/edge/full joint checks and centered rational logarithm certificate; frozen binary64 negative-control reproduction',
 'proof_source':str(R/'DERIVATION.md'),'locator':'Sections1-3','validation_source':str(R/'out/SUMMARY.json'),
 'reviewer_contributed_repair':False,'scope':'All source analytic clauses for every even d>=2, dedicated remainder-only reserve and recorded formula-specific numerical minima on current platform; no universal terminal payment'})
review['status']='INDEPENDENTLY_ACCEPTED_AT_FULL_STATED_SCOPE_BY_A073_LOCAL_ADOPTION_PENDING'
new={'claim_id':'A073-CENTERED-JENSEN-SHARP-REMAINDER','version':1,
 'exact_statement':'For the actual specified bent-core/one-vertex AND2 family F_d at every even d>=2, delta=2^-d, the complete binary-quotient remainder satisfies 0<D0<delta/(2 ln2). The coefficient 1/(2 ln2) is asymptotically sharp since D0/delta tends to it as even d tends to infinity. The sum of the two influence-weighted losses is less than delta^2/(4 ln2), and is less than (3/80)Inf_(y1), with that one physical reserve dedicated only to these two losses. For any finite rational probability weights p_j and rational |x_j|<1 satisfying sum_j p_j x_j=0, J=-sum_j p_j ln(1+x_j) is enclosed by the centered degree-N polynomial sum_j p_j sum_(k=2..N)(-1)^k x_j^k/k with absolute error at most sum_j p_j |x_j|^(N+1)/[(N+1)(1-|x_j|)], for each integer N>=2. Taking p_sigma=(1+sigma sqrt(delta))/2 and x_sigma=(delta-sigma sqrt(delta))/(1-delta/2) gives J=(ln2)D0 and a positive scaled rational certificate at the frozen dimensions including d=104,538,1076 with N=24 and no refinement. No assertion of a globally available child bank, retained terminal payment or universal FEI bound is made.',
 'hypotheses':['Actual specified finite uniform-cube Boolean family; entropy/KL in bits and physical flip influence',
 'Every even d>=2; complete derivative/reference normalizers and no support conditioning',
 'Centered-series identity assumes nonnegative rational weights summing to one, exact centering, and |x_j|<1; it does not silently discard outside reference mass',
 'Dedicated3/80 core fraction pays only the two displayed remainder losses, with no other debit'],
 'statement_sha256':'','contributors':['A073'],'proof_source':{'path':str(R/'DERIVATION.md'),'locator':'Sections3-4','validation':[str(R/'out/SUMMARY.json'),str(R/'out/CONSTANT_CERTIFICATE.json')]},
 'proof_dependencies':[],'review_records':[],'status':'NARROW_CERTIFICATE_AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A085','A096','A001','A094','A099','B15','B20']}
new['statement_sha256']=digest(new);claims=[review,new];write(R/'CLAIMS.json',claims)
write(R/'out/STATEMENT_HASHES.json',{'definition':'SHA256 of UTF8 compact sorted JSON with exact_statement and hypotheses',
 'source_recorded_hash_preserved':source['statement_sha256'],'source_envelope_digest':digest(source),
 'source_note':'Historical source identifier preserved; full source bytes pinned separately; not silently recanonicalized',
 'new_recorded_digest':new['statement_sha256'],'new_recomputed_digest':digest(new)})
write(R/'out/REVIEW_VERDICT.json',{'source_claim':source['claim_id'],'version':1,'verdict':'HOLDS_AT_FULL_STATED_SCOPE_NO_REPAIR',
 'new_refinement':'Separate contributor claim, pending independent review','full_FEI':'OPEN',
 'finite_precision_refinements':0,'universal_constant_improvement':0})
proto=json.loads((CANON/'EXECUTION_PROTOCOL.json').read_text());fields=proto['required_per_run']
parts=[
('exact target, quantifiers, hypotheses and units',
'Independently review A085-QUADRATIC-CONDITIONAL-REMAINDER-CERTIFICATE@1 for every even d>=2 on the actual bent-core point-edited AND2 family. Certify tiny positive KL signs by rational centered logarithms, rather than comparing rounded near-equal logarithms. The separate sharper all-dimensional bound is D0<delta/(2ln2), asymptotically sharp in this family. All entropy/KL is in bits and influence is ordinary physical flip probability. The dedicated reserve pays these two quotient losses only; full FEI remains open.'),
('sources actually read, revisions and theorem locators',
'Read BOARD supervisor snapshot2026-10-14 05:31 UTC, B15 STREAM_NOTES v2 dated2026-10-11 23:25, own STATUS/LEARNED and full protocol execution-v2. Read A096 latest DERIVATION sections1-4 and CLAIMS, A090 latest REPORT and A001 latest REPORT, including their non-flat quotient/child-bank and repeated-owner obstructions. The board records A082 independent full-scope acceptance of the new A096 result, so no redundant review is claimed. A085 current REPORT, PROOF, CLAIMS and audit source were read in full; its primary A073 review remained pending. No upstream executable is imported or executed. Own previous exact helper is copied byte-for-byte. Earlier source campaign/papers remain context; elementary calculations here have no paper theorem premise. Source receipts pin the consulted versions. The old f5/f6 display assignment is complete and the cyclic24 codes remain unavailable; neither census nor old precision task is repeated.'),
('complete derivation or exact first unsupported line',
'DERIVATION.md supplies the complete independent reconstruction and new proof. A085@1 HOLDS at its full analytic and platform-scoped numerical scope, without repair. Complete laws give D_full=D_binary+D0/2 and L_pair=delta D0/2. The source lower bound follows from the variance of its two signed row amplitudes and strong concavity of ln; the source upper bound and reserve follow from the exact atanh identity and rational polynomial. The new centered certificate cancels the weighted linear term exactly before applying a degree24 log series with an absolute geometric tail. It certifies D0/delta in(0.721347520,0.721347521) at d=104,538,1076 despite the naive binary64 zero/underflow. The new analytic inequality atanh[t/(1+t^2/2)]<t follows by a positive entire-series expansion of(1+t^2/2)sinh(t)-t cosh(t). Thus D0<delta/(2ln2), with the limiting coefficient exactly attained asymptotically. Both losses cost less than delta^2/(4ln2), giving a dedicated3/80 core fraction instead of3/64. The reduction is3/320. The rigorous margin3/80-1/(40ln2) exceeds1/1000. The first unsupported universal line remains sum_i e_i D_i>=sum_i e_i log2(1/e_i)-K I for a finite absolute K. A sufficient signed partition, retained terminal charge and actual unspent child reserve must still be paid together for arbitrary cores.'),
('executed validation with domain, arithmetic, commands and outputs',
f'FROZEN_SPEC predates computation. Three actual physical cases d=2,4,6 (maximum dimension8) and eight compressed cases d=2,4,6,8,32,104,538,1076; no symmetry quotient beyond proved two-amplitude counts. The separate frozen negative control has540 even dimensions2..1080. Pilot: one physical plus two compressed cases,89 exact checks,{pilot["runtime_seconds"]:.6f}s. Main:3 physical/8 compressed/540 negative controls,2080 counted checks,{summary["runtime_seconds"]:.6f}s, all PASS. Integer Walsh, signed inverse, Parseval, actual flips, complete normalized joint/row laws and prime-log identities verify the physical source. Centered Fraction arithmetic plus the proved tail decides the compressed signs with fixedN24 and zero precision refinements. At d=2 the wider initial display interval already proves the sign, so it is intentionally not refined. Actual full fractions and rational margins are saved per dimension. The source-formula negative control first returns zero at104 and a squared atom zero at538; floats never decide mathematical positivity. Commands: python -X utf8 runs/{R.name}/code/prepare.py; python -X utf8 runs/{R.name}/code/audit.py --pilot; python -X utf8 runs/{R.name}/code/audit.py; python -X utf8 runs/{R.name}/code/finalize.py. Frozen RAM estimate80MB, unmeasured, cap55s per job. No job expected above300MB, no memok-triggering job, automatic dimension escalation, GPU or background process.'),
('proof dependencies and changed downstream conclusions',
'A085@1 receives an independent acceptance record while its original statement, hypotheses, contributor, version and historical hash remain unchanged. A073-CENTERED-JENSEN-SHARP-REMAINDER@1 is a separate narrow refinement pending independent review. There is no contributed repair or conflict of authorship on the reviewed source. The elementary positive-series proof and centered-tail identity have no unreviewed campaign dependency. Source hash conventions are recorded explicitly rather than silently altered. This closes the pending source certificate and makes tiny positive remainder checks robust without adaptive precision. No broad FEI candidate is opened; the improved remainder-only reserve is not a globally free terminal bank. The A096 price-five obstruction and A001 repeated-owner audit remain in force.'),
('one next mathematical action and independent reviewer',
'A096/A001 should provide one actual non-flat conditional query with its sufficient signed amplitude statistic, complete reference and retained terminal bill, together with a named genuinely unused child surplus. Apply the centered certificate only after checking exact normalization, centering and its ratio domain; otherwise retain a full likelihood partition instead of discarding unmatched mass. A085 reviews the new sharp envelope and centered-tail certificate; A094 is alternate. This handoff targets the unpaid signed terminal bill rather than another round of small-family precision.'),
('actual persistence receipts or precise save blocker',
'Saved the four protocol files, frozen spec, complete DERIVATION, own code, flushed case receipts, full rational intervals at every compressed dimension, complete physical audit summaries, numerical negative-control receipts and constant certificate. STATUS has exactly two lines; WORKLOG appends and LEARNED records the durable result. Exact schema, compatibility-copy equality, source-statement preservation, file sizes and SHA256 readback are checked in out/SCHEMA_CHECK.json and manifest.json. Only A073 was written. New-claim independent review, supervisor adoption and mirror verification are pending; none is claimed as completed. No local save blocker.')]
report='# A073: centered certified logarithms and quadratic-certificate review\n\n'+'\n\n'.join('## '+h+'\n\n'+v for h,v in parts)
report+='\n\n## Universal bridge\n\nThis stage moves C018 by closing A085\'s pending full-scope remainder-certificate review and providing a cancellation-safe exact sign method for tiny conditional KL, with positive certificates through d=1076. For the specified family the two-loss reserve improves from3/64 to3/80, a reduction of3/320, and the sharp linear remainder coefficient is1/(2ln2). The improvement to a universal FEI constant is zero. The retained terminal bill and an actually unused, globally exclusive child surplus for arbitrary non-flat conditional rows remain unproved. NEXT consumes a source-complete non-flat physical query with those two terminal debts and one named bank: exact small-remainder arithmetic can then validate the real missing payment rather than manufacture a free reserve or refine another isolated class display.\n'
(R/'REPORT.md').write_text(report,encoding='utf-8')
p={'protocol_revision':proto['revision'],'run_id':R.name,'stream':'B15','packet_id':'A073','gap_id':'C018-HIGHER-ERASURE-SINGLE-BUDGET',
 'attempt_id':'A073-STAGE5-CENTERED-JENSEN-CERTIFICATE',
 'method':'Independent source review; centered rational log polynomial and explicit tail; positive-series sharp envelope and one remainder reserve',
 'mathematical_delta':'A085 quadratic certificate independently HOLDS without repair. New D0<delta/(2ln2), asymptotically sharp; paired remainder reserve3/80 instead of3/64. Exact positive scaled signs at104,538,1076 with fixed24 terms.2080 checks PASS; universal payment unchanged.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'A085_REVIEW_ACCEPTED; NEW_NARROW_REFINEMENT_PENDING_REVIEW; FULL_FEI_OPEN',
 'claim_versions_used':['A085-QUADRATIC-CONDITIONAL-REMAINDER-CERTIFICATE@1 (independent reconstruction, no repair)',
 'A073-NONZERO-ERASURE-BINARY-REMAINDER@1 (own earlier family context; no reopening)'],
 'claims_created_or_changed':['A085-QUADRATIC-CONDITIONAL-REMAINDER-CERTIFICATE@1 local independent review added','A073-CENTERED-JENSEN-SHARP-REMAINDER@1 created'],
 'source_artifacts':['DERIVATION.md','FROZEN_SPEC.json','code/audit.py','out/SUMMARY.json','out/CONSTANT_CERTIFICATE.json','out/centered_d104.json','out/centered_d1076.json','out/NEGATIVE_CONTROL.json'],
 'next_consumers':['A085','A096','A001','A094','A099','B15','B20'],
 'next_action':'Certify one sourced non-flat physical conditional-row payment jointly with retained terminal debt and an actually unused named child surplus; keep complete reference and one owner.',
 'stagnant_substantive_attempts':0,'blockers':['Universal retained terminal-core payment and global child-bank ownership remain open',
 'New narrow refinement independent review and shared/mirror adoption pending','Original cyclic24 codes remain unarchived; no repeat census'],
 'packet_ids':['A073']}
write(R/'PROGRESS.json',p);write(R/'PACKET_DELTA.json',p)
sources=[CANON/'EXECUTION_PROTOCOL.json',TEAM/'BOARD.md',TEAM/'claude/B15/STREAM_NOTES.md',A/'STATUS.md',A/'LEARNED.md']
sources += [S/f for f in ['REPORT.md','PROOF.md','CLAIMS.json','code/audit.py']]
sources += [N/f for f in ['DERIVATION.md','CLAIMS.json']]
sources += [TEAM/'agents/A001/runs/20261014T035113Z-account05-A001-quantifier-audit/REPORT.md',TEAM/'agents/A090/runs/20261014T034626Z-account05-A090-independent-reconstruction/REPORT.md',A/'runs/20261014T023508Z-account05-A073-certified-logarithms/code/exact.py']
write(R/'out/source_receipts.json',[{'path':str(f),'bytes':f.stat().st_size,'sha256':sha(f.read_bytes())} for f in sources])
(A/'STATUS.md').write_text('STATE: A073 stage5 saved: A085 quadratic certificate independently HOLDS; sharp D0<delta/(2ln2), dedicated pair-loss fraction3/80; centered positives through d1076;2080 checks PASS; FEI OPEN.\nNEXT: A096/A001 source an actual non-flat signed conditional row with retained terminals and one unused child bank; A085/A094 review sharp-envelope and centered-log certificate; no further old-family precision.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{now} Stage {R.name}: read updated board and source-complete A096/A090/A001 context. A082 already reviewed non-flat A096, so consumed pending A085 review instead. Independently accepted A085 quadratic certificate without repair; reproduced source floating minima104/538. Developed exact centered log series at fixedN24, giving positive D0/delta intervals at104,538,1076 without refinement. Proved sharp upper coefficient1/(2ln2) by positive sinh/cosh series; dedicated pair remainder reserve improves3/64 to3/80, margin>1/1000. Pilot89 and main2080 checks PASS. All protocol/rolling artifacts saved; full FEI and actual available terminal bank remain open.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nStage20261014T053433: A085 quadratic remainder@1 independently HOLDS, including platform/formula-specific first falsezero104 and squared-atom underflow538. For p_sigma=(1+sigma*t)/2, x_sigma=(delta-sigma*t)/(1-delta/2), E x=0 exactly. Centered -E ln(1+x)=E sum_(k=2..N)(-1)^k x^k/k with absolute tail<=E |x|^(N+1)/[(N+1)(1-|x|)]; divide by delta before positive ln2 interval to avoid tiny cancellation. FixedN24 proves D0/delta in(0.721347520,0.721347521) at104,538,1076. Analytic atanh[t/(1+t^2/2)]<t follows coefficients k(2k-1)/(2k+1)!>0 in(1+t^2/2)sinh t-t cosh t. Thus0<D0<delta/(2ln2), sharp as delta->0, pairedloss<delta^2/(4ln2), dedicated core fraction3/80 instead of3/64. Only remainder is paid. Actual unused terminal-child bank is still not supplied, and retained M/e grows. Do not refine a display once sign is known; d2 interval may stay wide.\n')
req=set(fields['progress_fields']);req.remove('packet_ids (one primary ID, for compatibility)');req.add('packet_ids')
assert set(p)==req and all(set(c)==set(fields['claim_fields']) for c in claims)
assert all('## '+h in report for h in fields['report_fields'])
assert all(review[k]==source[k] for k in ['exact_statement','hypotheses','statement_sha256','contributors','version'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text().splitlines())==2
write(R/'out/SCHEMA_CHECK.json',{'exact_fields':'PASS','original_statement_preservation':'PASS','compatibility_copy':'PASS',
 'status_two_lines':'PASS','new_claim_hash':'PASS','refinements':0,'new_refinement_independent_review':'PENDING',
 'source_claim_independent_review':'HOLDS_NO_REPAIR','saved_at':now})
manifest=[]
for f in R.rglob('*'):
 if f.is_file() and f.name!='manifest.json':
  raw=f.read_bytes();assert len(raw)<20_000_000
  manifest.append({'path':str(f.relative_to(R)),'bytes':len(raw),'sha256':sha(raw)})
write(R/'out/manifest.json',{'files':manifest,'saved_at':now,'remote_adoption':'UNVERIFIED'})
for x in manifest:assert sha((R/x['path']).read_bytes())==x['sha256']
print(json.dumps({'schema':'PASS','manifest_readback':'PASS','files':len(manifest),'max_bytes':max(x['bytes'] for x in manifest),
 'reserve_margin':E.serial(E.decimal_interval(margin,9)),'review_verdict':'HOLDS_NO_REPAIR',
 'new_claim_review':'PENDING','report':str(R/'REPORT.md')},indent=2))
