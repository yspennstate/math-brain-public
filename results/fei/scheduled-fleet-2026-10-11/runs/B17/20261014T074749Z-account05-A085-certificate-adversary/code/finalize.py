from pathlib import Path
from fractions import Fraction as Q
import datetime,hashlib,json
RUN=Path(__file__).resolve().parents[1];AGENT=RUN.parents[1];ROOT=AGENT.parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
protocol_path=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8-sig'));fields=protocol['required_per_run']
def dump(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
sources=[protocol_path,ROOT/'BOARD.md',ROOT/'claude/B17/STREAM_NOTES.md']
for agent,run,names in [
 ('A083','20261014T053514Z-account05-A083-formal-core',['REPORT.md','PROOF.md','CLAIMS.json']),
 ('A096','20261014T042803Z-account05-A096-live-gap-ledger',['DERIVATION.md','CLAIMS.json']),
 ('A050','20261014T063752Z-account05-A050-repair-with-scope',['REPORT.md','PROOF.md']),
 ('A073','20261014T053433Z-account05-A073-certified-logarithms',['CLAIMS.json'])]:
 sources.extend(ROOT/'agents'/agent/'runs'/run/name for name in names)
dump(RUN/'out/source_receipts.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p),'timestamp':now} for p in sources])
audit=json.loads((RUN/'out/audit.json').read_text());pilot=json.loads((RUN/'out/pilot.json').read_text());initial=json.loads((RUN/'out/audit_initial.json').read_text())
assert audit['status']=='PASS' and audit['checks']==137 and initial['checks']==134 and pilot['checks']==336
assert max(audit['elapsed_seconds'],pilot['elapsed_seconds'],initial['elapsed_seconds'])<55
r=audit['results'][0]
assert Q(r['unused_same_owner']['lower'])>Q(176,100)
assert Q(r['A050_booking_unchanged_owner_left']['lower'])>Q(173,100)
assert Q(r['A050_final_unpaid_quotient']['lower'])>0
assert r['old_S4']==r['consumed_influence_debit']+r['final_actual_S4']==3
dump(RUN/'CERTIFICATE_FAILURE.json',{
 'verdict':'COMPLETED_SCOPE_AND_SAME_OWNER_CHECK; ORIGINAL_SOURCE_CLAUSES_SURVIVE',
 'actual_Boolean_fixture':'F(x,a,b,y)=(-1)^a if x=0; else 2y-1 if b=1; else +1',
 'history':'b, then y only on b=1; fair declared ghost fallback; same canonical inherited reference',
 'scope_guard':'Old S4=3 equals consumed influence1 plus final S4=2; final2 is not a new bank',
 'first_booked_C':'out/true-canonical-root.json',
 'exact_KL_identity':'D_mean_b = reached_y_erasure + D_final = C/2+D_final',
 'conservative_A050_booking':'Keep C+C_y booked, add J=D_mean_b-C-C_y/2 once, no refund',
 'final_quotient':r['A050_final_unpaid_quotient'],
 'remaining_original_owner':r['A050_booking_unchanged_owner_left'],
 'failure_or_unproved_extension':'General non-flat mixed-history eligibility/available surplus and preceding source/outcome accounts are not established by this fixture',
 'existing_claim_refuted':False,'global_minimality_claimed':False,'full_FEI':'OPEN'})
dump(RUN/'out/review_verdict.json',{'source':'A083-REFERENCE-ONLY-MATCHING-AND-PAID-CONDITIONAL-BILL@1',
 'verdict':'HOLDS_CONCRETE_CANONICAL_PARTIAL_PAYMENT_CLAUSE_ONLY',
 'independent_method':'Direct physical characters and complete interval same-kernel transport',
 'unreviewed_source_bundle':'General graph/Lean kernel interpretation; no full-source acceptance',
 'additional_delta':'A050 saved conservative booking retained; remaining final quotient paid once from same final2 owner',
 'universal_scope':'OPEN'})
src073=sources[-1]
accepted=next(c for c in json.loads(src073.read_text()) if c['claim_id']=='A085-QUADRATIC-CONDITIONAL-REMAINDER-CERTIFICATE')
previous=next(c for c in json.loads((AGENT/'runs/20261014T034606Z-account05-A085-certificate-adversary/CLAIMS.json').read_text()) if c['claim_id']==accepted['claim_id'])
assert accepted['exact_statement']==previous['exact_statement'] and accepted['statement_sha256']==previous['statement_sha256']
statement=('On the actual four-bit canonical-occupancy priority fixture F(x,a,b,y)=(-1)^a if x=0, '
 'else 2y-1 if b=1, else +1, query b then y only in the b=1 child with fair source-zero fallback '
 'and the SAME inherited canonical reference. The positive occupancy normalizer solves '
 '1-c=(1-8c/15)^2(1-4c/15)^2. The actual old mean-child S4=3 splits exactly into consumed-influence debit1 '
 'and final actual S4=2. Let C=-(1/2)log2(1-4c/15), Dbar be the mean complete inherited b-child KL, '
 'and Dfinal the root-reached terminal KL. Then 1/8<C<3/16, Dbar<1, Dbar-C>0, '
 'and Dbar=C/2+Dfinal; half the already booked C moves to y-query erasure, without a second debit. '
 'All current terminal entropy and reference KL fit the same old owner, leaving 2-Dbar>176/100. '
 'For A050 conservative booking C+Cy, where Cy=(1/2)log2[(2-8c/15)^2/(4(1-8c/15))], '
 'the unpaid final quotient J=Dbar-C-Cy/2 is positive. Keeping every old conservative booking and adding J once '
 'spends Dbar+Cy/2 and leaves more than173/100 in the same final2 portion, with no refund or new bank. '
 'Preceding source-b erasure/outcome accounts and universal non-flat owner eligibility are not asserted paid.')
hyp=['Specified actual uniform-cube fixture, physical order x,a,b,y; bits and ordinary influence',
 'Complete canonical nonempty occupancy reference with empty atom1/16, mass15/16 and marginals(8/15,8/15,4/15,4/15)',
 'Same normalized coherent kernel and fair declared source-zero fallback at both queries; full reference-only support kept',
 'The old mean-child S4=3 is prespecified genuinely unused before the conditional transaction; no earlier history bank is reused',
 'Single specified history and owner; no arbitrary-core policy, full graph/Lean acceptance or universal FEI conclusion']
claim={'claim_id':'A085-CANONICAL-SAME-OWNER-QUOTIENT-CONTINUATION','version':1,'exact_statement':statement,'hypotheses':hyp,
 'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'contributors':['A085'],'proof_source':{'path':str(RUN/'PROOF.md'),'checker':str(RUN/'code/audit.py'),'certificate':str(RUN/'out/true-canonical-root.json')},
 'proof_dependencies':[],'review_records':[{'reviewer':'A083','verdict':'PENDING_PRIMARY'},{'reviewer':'A050','verdict':'PENDING_BOOKING_COMPATIBILITY'},{'reviewer':'A092','verdict':'PENDING_ALTERNATE'}],
 'status':'NARROW_LOCAL_CERTIFICATE_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
 'first_unproved_line':None,'next_consumers':['A083','A050','A038','A039','A047','A092','A096','B17','B20']}
for c in [accepted,claim]:assert set(c)==set(fields['claim_fields'])
dump(RUN/'CLAIMS.json',[accepted,claim])
progress={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B17','packet_id':'A085',
 'gap_id':'C024-C019-INHERITED-REFERENCE-SAME-OWNER','attempt_id':'A085-stage5-canonical-retained-quotient',
 'method':'Direct physical characters and exact same-kernel transport; rational canonical-root interval and complete current KL owner ledger',
 'mathematical_delta':'Canonical two-step retained quotient paid from SAME owner; A050 conservative booking untouched, >1.73 bits left; prior quadratic claim acceptance consumed',
 'deliverable_status':'COMPLETE_LOCAL_SAVE','mathematical_status':'SCOPED_CURRENT_TRANSACTION_CLOSED; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':['A083-REFERENCE-ONLY-MATCHING-AND-PAID-CONDITIONAL-BILL@1 (concrete clause reconstructed only)',
 'A085-QUADRATIC-CONDITIONAL-REMAINDER-CERTIFICATE@1 (A073 independent acceptance consumed)',
 'A050 stage5 support-complete likelihood-envelope repair (saved conservative booking, exact PROOF Section4)'],
 'claims_created_or_changed':[accepted['claim_id']+'@1 (external review consumed unchanged)',claim['claim_id']+'@1'],
 'source_artifacts':[str(p) for p in sources],'next_consumers':claim['next_consumers'],
 'next_action':'Carry SAME reference and booked C/R spends through a weak non-flat replacement data core, paying combined actual conditional/quotient/source costs from genuinely unused certified child surplus; A083/A050/A092 review',
 'stagnant_substantive_attempts':0,'blockers':['General unused-owner eligibility and preceding source/outcome debts remain unpaid','Review/shared adoption/remote mirrors unverified'],
 'packet_ids':['A085']}
assert set(progress)=={s.split(' (')[0] for s in fields['progress_fields']}
dump(RUN/'PROGRESS.json',progress);(RUN/'PACKET_DELTA.json').write_bytes((RUN/'PROGRESS.json').read_bytes())
(AGENT/'STATUS.md').write_text('STATE: A085 stage5 complete: canonical retained quotient paid from SAME owner; A050 conservative bookings unchanged, >1.73 bits left; 137 final checks PASS; prior quadratic claim independently accepted; FEI OPEN.\n'
 'NEXT: A083/A050/A092 review canonical transaction; test weak non-flat replacement data query with SAME complete reference, booked debits, actual unused child surplus and both full terminals.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n'+now+' — '+RUN.name+': consumed A083 canonical b/query and A050 saved conservative y-envelope booking. Direct physical/channel pilot two rational refs336 checks0.044116s; exact canonical interval initial134 checks1.393013s; newly frozen A050 compatibility recheck137 checks1.429482s unchanged domain/precision. Proved old S4=3=consumed1+final2, Dbar=C/2+Dfinal, R=Dbar-C>0; inherited quotient paid without renewal. Keeping A050 C+Cy booking and paying positive final quotient once leaves>1.73 bits, no refund. All current terminal laws retained; preceding source/outcome and arbitrary non-flat owner eligibility remain open. Prior quadratic claim A073 full-scope acceptance observed and preserved. Saved protocol files, receipts and rolling notes; new review pending.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n## '+now+' — Canonical inherited-quotient owner\n'
 'On four-bit priority gate, b then y only at b=1, old actual mean-child S4=3 partitions into consumed-influence1 and finalS4=2. Canonical c root ~0.793; C=-log2(1-4c/15)/2. Complete mean inherited b-child KL Dbar~0.2371; R=Dbar-C~0.0658. Exact full current identity Dbar=C/2+Dfinal moves half old conditional debt to reached y erasure without new debit. Same owner leaves>1.76 bits in exact accounting. A050 conservatively books C+Cy, Cy=log2[(2-theta)^2/(4(1-theta))]/2,theta=8c/15; final quotient J=Dbar-C-Cy/2>0. Keep booking untouched, addJ once, no refund: leftover>1.73. Canonical-root interval, not pilot endpoint overlap, certifies signs. Source-b erasure/outcome precede this owner and are not paid here. No universal availability of unused mean-child surplus is established. Prior quadratic A085@1 independently accepted by A073; no old-family precision rerun needed.\n')
report=(RUN/'REPORT.md').read_text()
assert all('## '+s in report for s in fields['report_fields']) and report.rsplit('## ',1)[1].startswith('Universal bridge\n')
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
dump(RUN/'out/validation.json',{'status':'PASS','timestamp':now,'protocol_fields':'EXACT','packet_delta':'BYTE_IDENTICAL','current_transaction':'CERTIFIED',
 'source_A083_review_scope':'CONCRETE_CANONICAL_CLAUSE_ONLY','A050_booking':'PRESERVED_WITHOUT_REFUND','counts':audit,'independent_review':'PENDING','full_FEI':'OPEN'})
files=[p for p in sorted(RUN.rglob('*')) if p.is_file() and p.name!='manifest.json'];assert all(p.stat().st_size<20*1024*1024 for p in files)
manifest=[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]
dump(RUN/'out/manifest.json',{'timestamp':now,'files':manifest,'maximum_bytes':max(p['bytes'] for p in manifest)})
assert all(sha(RUN/x['path'])==x['sha256'] for x in manifest)
print(json.dumps({'status':'PASS','files':len(manifest)+1,'maximum_bytes':max(p['bytes'] for p in manifest),'timestamp':now}))
