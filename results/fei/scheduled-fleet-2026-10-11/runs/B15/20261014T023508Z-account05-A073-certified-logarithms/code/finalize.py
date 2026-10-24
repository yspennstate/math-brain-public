from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,copy
import exact as E
R=Path(__file__).resolve().parents[1];A=R.parents[1];TEAM=A.parent.parent
SRC=TEAM/'agents/A096/runs/20261014T013836Z-account05-A096-live-gap-ledger'
CANON=Path(r'~\mop_fei100\reports\fei-2026-10-11')
NOW=datetime.now(timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def write(p,v):p.write_text(json.dumps(E.serial(v),indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(c):return sha(json.dumps({k:c[k] for k in ['exact_statement','hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
summary=json.loads((R/'out/SUMMARY.json').read_text());pilot=json.loads((R/'out/PILOT.json').read_text())
assert summary['cases']==110 and summary['checks']==11720 and summary['status']==pilot['status']=='PASS'
lo,hi=E.log_bounds(F(7,5),12)
margin=(F(1,4)-hi/2,F(1,4)-lo/2)
U=7**128;V=(2**63)*(5**128)
assert 49<50 and U<V and margin[0]>F(1,256)
write(R/'out/UNIFORM_MARGIN.json',{'statement':'1/4-log2(7/5)/2 > 1/256',
 'integer_equivalence':'log2(7/5)<63/128 iff 7^128 < 2^63*5^128',
 'integer_left':U,'integer_right':V,'integer_difference':V-U,'sign':1,
 'margin_interval':margin,'margin_decimal':E.decimal_interval(margin,9),
 'margin_above_1_over_256':margin[0]-F(1,256),'precision_terms':12,'precision_refinements':0})

original=next(c for c in json.loads((SRC/'CLAIMS.json').read_text()) if c['claim_id']=='A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP')
accepted=copy.deepcopy(original)
accepted['review_records'].append({'reviewer':'A073','timestamp':NOW,'verdict':'ACCEPT_AT_FULL_STATED_SCOPE_NO_REPAIR',
 'method':'Independent character embedding and complete conditional likelihood reconstruction; own integer Walsh/physical flip/full joint KL checker; all labeled n<=2 and selected n3 subsets plus bent witnesses',
 'proof_source':str(R/'DERIVATION.md'),'locator':'Independent reconstruction section',
 'validation_source':str(R/'out/SUMMARY.json'),'reviewer_contributed_repair':False,
 'scope':'Original parity-substitution identities, exact binary sufficiency, all-even-d unbounded local deletion and bounded H/I witness. No universal payment theorem.'})
accepted['status']='INDEPENDENTLY_ACCEPTED_AT_FULL_STATED_SCOPE_BY_A073_LOCAL_ADOPTION_PENDING'
new={
 'claim_id':'A073-NONZERO-ERASURE-BINARY-REMAINDER','version':1,
 'exact_statement':'For every even integer d>=2, put delta=2^-d, t=2^(-d/2), b(y)=(-1)^(sum_j y_(2j-1)y_(2j)) on 0/1 labels, q(u,v)=-1 only at (1,1), and F_d=b(y)+1_(y=0)(q(u,v)-1). Every Fourier atom of F_d is positive. Each query i in {u,v} has e_i=delta/2 and positive true erasure. Retaining only the other pair coordinate gives complete derivative/reference laws (1/2,1/2) and (1-e_i,e_i). With N_+=(2^d+2^(d/2))/2,N_-=(2^d-2^(d/2))/2 and D0=sum_sigma N_sigma delta log2[(1-delta/2)/(1-sigma t+delta/2)], the full KL equals binary KL plus D0/2 and the influence-weighted quotient loss is L_i=e_i D0/2. Uniformly 0<L_i/e_i<=log2(7/5)/2<1/4-1/256, certified by 7^128<2^63*5^128. The two losses together are <delta/4 and <Inf_(y1)/10 if that physical reserve is dedicated only to these losses. Nevertheless M_i/e_i>d/2+3/4. Each core influence equals (1+delta)/2, I(F_d)=d/2+(d/2+1)delta, and H(F_d)/I(F_d)<=2+4/d<=4. No universal conditional partition, terminal payment, or FEI conclusion is asserted.',
 'hypotheses':['Actual uniform-cube Boolean signs; entropy and KL in bits; ordinary physical flip influence',
 'Even d>=2, the specified quadratic bent core and two-bit gate on disjoint physical coordinates',
 'Complete normalized reference laws including derivative-free mass; no reference conditioning on derivative support',
 'Dedicated reserve inequality is only a partial ledger for the two stated quotient losses; no other charges or free global reserve are asserted'],
 'statement_sha256':'','contributors':['A073'],'proof_source':{'path':str(R/'DERIVATION.md'),'locator':'Nonzero-erasure Boolean boundary family; Certified logarithms','validation':[str(R/'out/SUMMARY.json'),str(R/'out/UNIFORM_MARGIN.json')]},
 'proof_dependencies':[],'review_records':[],'status':'SCOPED_EXPLICIT_FAMILY_LEMMA_PROVED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A096','A001','A085','A099','B15','B20']}
new['statement_sha256']=digest(new)
claims=[accepted,new];write(R/'CLAIMS.json',claims)
write(R/'out/statement_hash_notes.json',{'definition':'sha256 UTF8 compact sorted-key JSON of exact_statement and hypotheses',
 'source_claim':{'recorded_preserved':original['statement_sha256'],'recomputed_envelope':digest(original),'note':'Historical identifier retained; source bytes and exact text independently pinned'},
 'new_claim':{'recorded':new['statement_sha256'],'recomputed_envelope':digest(new)}})
write(R/'out/ATTEMPTS.json',{'pilot':pilot,'main':summary,
 'diagnostic_correction':'First pilot passed but printed checks=0 because from-import copied an integer counter. Fixed reporting to exact.CHECKS; main was correct and unchanged-domain pilot rerun reports527. No arithmetic assertion failed.',
 'new_comparison':'MARGIN_SPEC frozen before single exact integer/fixed-N constant certificate; no function domain expansion',
 'precision_refinements':0,'peak_memory':'Not measured; frozen estimate80MB; no job expected above300MB'})

heads=json.loads((CANON/'EXECUTION_PROTOCOL.json').read_text())['required_per_run']
sections=[
('exact target, quantifiers, hypotheses and units',
'Independently review A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP@1 at its full stated scope, then extend its informative binary quotient to the explicit nonzero-erasure Boolean family F_d for every even d>=2. Use complete normalized reference laws and quantify the exact influence-weighted conditional remainder. Entropy/KL are in bits and influence is ordinary physical flip influence. This is a source-bound dependency review and narrow signed family lemma, not a renewed census.'),
('sources actually read, revisions and theorem locators',
'At stage start read BOARD supervisor snapshot2026-10-14 02:33 UTC, B15 STREAM_NOTES v2 dated2026-10-11 23:25, own STATUS/LEARNED, and full protocol2026-10-11-execution-v2. Read A096 current DERIVATION sections1-5, CLAIMS and checker source; independently reconstructed rather than importing or executing its code. Read A001 current REPORT, especially the complete-tail conditional-KL obstruction and tensor cancellation; it motivates preserving likelihood information rather than degree-only compression. The old B15 f5/f6 30-digit task is already completed in the preceding run. Its24 cyclic inputs remain unarchived, so no repeat search was dispatched. Earlier campaign sources/papers are context rather than premises of this proof. Byte receipts below identify current source snapshots.'),
('complete derivation or exact first unsupported line',
'DERIVATION.md reconstructs all A096 clauses by injective character embedding, direct complete likelihood ratios, exact conditional laws and the bent selector edge count. Verdict: HOLDS AT FULL STATED SCOPE, no repair. The new family replaces parity at one bent-core vertex by the actual two-bit gate negative only at11. Its four signed Fourier amplitudes are sigma*t-delta/2,delta/2,delta/2,-delta/2, so erasure is positive. The informative binary quotient has mu=(1/2,1/2),r=(1-e,e),e=delta/2. Full divergence equals binary divergence plus D0/2, with exact D0 in the derivation/claim. The conditional core likelihood is at most7/5 because (2-3t)(1-2t)>=0. Thus the lost weighted refund obeys0<L_i/e_i<=log2(7/5)/2<1/4-1/256. The strict final margin is the exact integer comparison7^128<2^63*5^128, independently enclosed with fixed12-term rational logarithms. Both row losses together are<delta/4; a dedicated1/10 fraction of one specified core influence also covers them once. This partial allocation makes no other charge against that reserve. The retained M_i/e_i still exceeds d/2+3/4. Total influence is d/2+(d/2+1)delta and H/I<=4, so this is no FEI disproof. The first unsupported universal line remains sum_i e_i D_i>=sum_i e_i log2(1/e_i)-K I for one absolute K and every Boolean f; arbitrary-row partition choice and nonoverlapping terminal-reserve ownership remain open.'),
('executed validation with domain, arithmetic, commands and outputs',
f'FROZEN_SPEC precedes computation. Exhaust all4 one-bit and16 two-bit labeled signs with all duplication subsets, and4 named three-bit signs with all subsets:104 cases. Add3 bent-selector and3 AND-point-gate cases d=2,4,6 for110 cases; no symmetry quotient. Maximum physical dimension8. Actual truth tables are checked by exact integer FWHT, signed inverse, Parseval, physical edge counts, complete row/joint normalization and exact prime-log cancellations. FixedN12 rational interval signs use proved positive tails; zero refinement. Each case flushes to JSONL. Pilot6 cases,527 checks,{pilot["runtime_seconds"]:.6f}s; main110 cases,11720 checks,{summary["runtime_seconds"]:.6f}s. First pilot counter display was corrected; no mathematical failure or main rerun. Commands: python -X utf8 runs/{R.name}/code/prepare.py; python -X utf8 runs/{R.name}/code/audit.py --pilot; python -X utf8 runs/{R.name}/code/audit.py. Main helper/code cap55s, estimated80MB RAM, not measured; no memok-required job. A separate MARGIN_SPEC precedes the one constant comparison performed by code/finalize.py. The outward L_i/e_i intervals at d=2,4,6 are (0.070399460,0.070399461), (0.021352095,0.021352096), (0.005561896,0.005561897). Their signs are already strict; no extra precision is needed.'),
('proof dependencies and changed downstream conclusions',
'A096@1 gains a local independent acceptance record without changes to its statement, hypotheses, contributor or recorded source hash. The additional explicit-family lemma is A073-NONZERO-ERASURE-BINARY-REMAINDER@1, pending independent review, proved directly with no unreviewed theorem dependencies. The proof uses elementary character orthogonality, finite KL chain rule/nonnegativity and rational log tails. The new scope is a controlled positive-erasure row and a quantitative conditional remainder payment; the original A096 zero-erasure claim was not repaired or extended under its identity. Historical source statement hash and separately computed canonical-envelope digest are both retained; new claim hash is defined in out/statement_hash_notes.json. No shared registry or outside source is modified, no broad universal candidate opened, and universal constants remain unchanged.'),
('one next mathematical action and independent reviewer',
'A096/A001 should test whether an actual signed Boolean conditional partition gives the same bounded within-cell likelihood ratio beyond this one-vertex gate, with the remainder charged once to a named available terminal reserve. The challenge is the still unbounded retained M_i/e_i, not the now certified small discarded remainder. A085 independently reconstructs the signed amplitudes and margin; A096/A001 review the new family lemma and reserve scope. Do not extrapolate from binary alphabet size or discard the residual KL. The missing old cyclic codes are a separate input blocker, not a reason to restart the census.'),
('actual persistence receipts or precise save blocker',
'Saved REPORT.md, exact-schema CLAIMS.json, PROGRESS.json and byte-identical PACKET_DELTA.json, both frozen specs, DERIVATION.md, all code, flushed cases, three complete AND-row witnesses and exact margin. STATUS is two lines, WORKLOG appends the stage and LEARNED records durable formulas. out/SCHEMA_CHECK.json and manifest.json provide readback/size/hash checks; source_receipts.json pins consulted source bytes. Largest file is checked below20MB. Only A073 is written. Supervisor adoption, independent review of the new lemma and mirror copy are unverified, not claimed.')]
report='# A073: informative binary quotient with positive erasure\n\n'+'\n\n'.join('## '+h+'\n\n'+b for h,b in sections)
report+='\n\n## Universal bridge\n\nThis stage moves C018 by independently accepting A096\'s exact correlated-partner ownership audit and extending the informative quotient to an actual positive-erasure row: the discarded conditional KL costs less than (1/4-1/256) times queried influence, with both row losses also covered once by a dedicated1/10 fraction of one core coordinate. The universal-constant improvement is zero. The surviving retained M_i/e_i grows at least d/2+3/4, and a general signed partition with a globally nonoverlapping available terminal reserve remains unproved. NEXT tests precisely that conditional partition/ownership condition, because the explicit exact decomposition distinguishes the small removable remainder from the true arbitrary-seed bill and therefore addresses the full C018/FEI bridge rather than another numerical class census.\n'
(R/'REPORT.md').write_text(report,encoding='utf-8')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B15','packet_id':'A073',
 'gap_id':'C018-HIGHER-ERASURE-SINGLE-BUDGET','attempt_id':'A073-STAGE4-INFORMATIVE-BINARY-POSITIVE-ERASURE',
 'method':'Independent source-claim reconstruction; exact signed Boolean complete-row quotient; integer margin and fixed rational intervals',
 'mathematical_delta':'A096 single-spectator claim independently accepted at full scope. New all-even-d positive-erasure family has exact conditional remainder0<L/e<1/4-1/256 and explicit single reserve allocation;110 finite cases/11720checks. Retained terminal price remains unbounded locally; FEI open.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'A096_REVIEW_ACCEPTED; NEW_SCOPED_LEMMA_PENDING_REVIEW; UNIVERSAL_FEI_OPEN',
 'claim_versions_used':['A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP@1 (independently reconstructed, no repair)'],
 'claims_created_or_changed':['A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP@1 local review added','A073-NONZERO-ERASURE-BINARY-REMAINDER@1 created'],
 'source_artifacts':['DERIVATION.md','FROZEN_SPEC.json','MARGIN_SPEC.json','code/audit.py','code/exact.py','out/SUMMARY.json','out/UNIFORM_MARGIN.json','out/AND_d2.json','out/AND_d4.json','out/AND_d6.json'],
 'next_consumers':['A096','A001','A085','A099','B15','B20'],
 'next_action':'Find and review a signed Boolean conditional partition with bounded within-cell likelihood ratio and a named available terminal reserve counted once; retain and pay the remaining core price.',
 'stagnant_substantive_attempts':0,'blockers':['No universal terminal-core KL payment or global reserve ownership theorem','Old cyclic24 inputs still unavailable; no new search dispatched','New scoped lemma independent review and supervisor/mirror adoption pending'],
 'packet_ids':['A073']}
write(R/'PROGRESS.json',progress);write(R/'PACKET_DELTA.json',progress)
paths=[CANON/'EXECUTION_PROTOCOL.json',TEAM/'BOARD.md',TEAM/'claude/B15/STREAM_NOTES.md',A/'STATUS.md',A/'LEARNED.md']
paths += [SRC/f for f in ['DERIVATION.md','REPORT.md','CLAIMS.json','code/check.py']]
paths += [TEAM/'agents/A001/runs/20261014T011101Z-account05-A001-quantifier-audit/REPORT.md',A/'runs/20261013T234148Z-account05-A073-certified-logarithms/code/review.py']
write(R/'out/source_receipts.json',[{'path':str(p),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in paths])
(A/'STATUS.md').write_text('STATE: A073 stage4 saved: A096 spectator claim independently HOLDS; positive-erasure binary remainder0<L/e<1/4-1/256 for all even d;110 cases/11720 exact checks; FEI OPEN.\nNEXT: A096/A001 generalize signed conditional partition with one available terminal reserve; A085 review A073 positive-erasure lemma; retained core M/e remains unbounded locally.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{NOW} Stage {R.name}: read new board/A096/A001. Independently accepted A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP@1 without repair. Changed parity mechanism to actual AND point-gate on bent core; proved positive-erasure informative quotient remainder e*D0/2<(1/4-1/256)e for all even d, with both losses coverable once from dedicated core fraction1/10. Retained M/e>d/2+3/4; H/I<=4. Pilot6/527 and main110/11720 exact checks; fixedN12, no refinement. Corrected initial imported counter display only. Saved new scoped claim pending A085/A096 review; universal payment open.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nStage20261014: A096 single-spectator ownership@1 independently HOLDS: parity duplication embeds p, adds sum_J e, removes sum_J M; dropping partner loses original M_i, retaining partner preserves KL exactly despite correlation. New F_d=b(y)+1_(y=0)(q_AND(u,v)-1), even d, has e_u=e_v=delta/2 and all Fourier masses positive. Binary mu=(1/2,1/2),r=(1-e,e); D_full=D_binary+D0/2, D0=sum N_sigma delta log2[(1-delta/2)/(1-sigma*t+delta/2)]. Likelihood bound7/5 follows (2-3t)(1-2t)>=0. Hence0<L/e<1/4-1/256, exact7^128<2^63*5^128; combined losses<delta/4<=Inf_y1/10 with that reserve dedicated only to these losses. Still M/e>d/2+3/4; H/I<=4. Positive erasure does not invalidate conditional quotient, and small lost remainder does not pay retained core price. Do not assume a globally free core reserve. Fixed12-term exact rational log enclosures settle all requested signs; no refinement.\n')
required=set(heads['progress_fields']);required.remove('packet_ids (one primary ID, for compatibility)');required.add('packet_ids')
assert set(progress)==required and all(set(c)==set(heads['claim_fields']) for c in claims)
assert all('## '+h in report for h in heads['report_fields'])
assert all(accepted[k]==original[k] for k in ['exact_statement','hypotheses','statement_sha256','contributors','version'])
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
assert len((A/'STATUS.md').read_text().splitlines())==2
write(R/'out/SCHEMA_CHECK.json',{'exact_protocol_fields':'PASS','delta_byte_equality':'PASS','status_two_lines':'PASS',
 'source_statement_unchanged':'PASS','new_claim_hash':'PASS','source_claim_acceptance':'LOCAL; shared adoption pending',
 'new_claim_review':'PENDING','saved_at':NOW})
manifest=[]
for p in R.rglob('*'):
 if p.is_file() and p.name!='manifest.json':
  raw=p.read_bytes();assert len(raw)<20_000_000
  manifest.append({'path':str(p.relative_to(R)),'bytes':len(raw),'sha256':sha(raw)})
write(R/'out/manifest.json',{'files':manifest,'saved_at':NOW,'mirror_verification':'UNVERIFIED'})
for e in manifest:assert sha((R/e['path']).read_bytes())==e['sha256']
print(json.dumps({'schema':'PASS','manifest_readback':'PASS','files':len(manifest),'max_bytes':max(x['bytes'] for x in manifest),
 'uniform_margin':E.decimal_interval(margin,9),'new_lemma_review':'PENDING','report':str(R/'REPORT.md')},default=str,indent=2))
