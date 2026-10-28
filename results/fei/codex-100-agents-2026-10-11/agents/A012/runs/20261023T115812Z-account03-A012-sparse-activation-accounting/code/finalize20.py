from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json
R=Path(__file__).resolve().parents[1];BASE=R.parents[1]
ROOT=Path('~/brain_workers/FEI100_20261011')
SRC=R.parent/'20261023T053904Z-account03-A012-sparse-activation-accounting'
A13=ROOT/'agents/A013/runs/20261023T062458Z-account03-A013-representation-stability'
P=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,x):p.write_bytes((json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode('utf-8'))
def md(p,s):p.write_bytes(s.encode('utf-8'))
a=read(R/'out/PARTIAL.json');b=read(R/'out/REPLAY.json');assert a['status']==b['status']=='PASS'
consumers=['A013','A011','A058','A086','A094','B03','B20']
statement=('Refinement of A012 v7 with a paid partial-profile operation: for normalized finite laws P,Q with Q positive on supp(P), a fixed cell partition with profiles p,q, 0<t<1 and r=(1-t)q+t p, define R(x)=r_j Q(x)/q_j on cell j. This preserves every complete inherited conditional law and reference-only atom. Charging FULL c=D(R||Q)=D(r||q) gives exact net rebate CE(P,Q)-CE(P,R)-c=((1-t)/t)[D(r||q)+D(q||r)]>=0. At t=1/2 the rebate is symmetric KL. Under actual physical queries with marginal reference, signed draw tau=K Inf_i-gamma, K=4+2/ln2, admits this handoff iff weighted(tau-rebate) fits the SAME previously unused original stock after every old booking/conversion debit. For the saved v7 six-bit target, after s0 then s1 on all branches, q_empty=21/32, actual p_empty=(1/16,1,9/16,1), expected remaining I=1/2. Half-profile transport retains BOTH full terminal KLs and old5/(4ln2), charges the full new conversion, and leaves >1/128 bit; all real t in[1/2,5/8] leave >1/256 bit by exact endpoints and convexity. No variance reserve is renewed. Complete-reference shape is stable under physical marginalization; budget admission is conditional, not automatic. The old v7 admitted-function grammar is unchanged, so no opaque hidden core is newly admitted. After all three shared queries expected I=1/4 and K/4-5/(4ln2)=1-3/(4ln2)<-1/16 bit even with zero terminal/reference costs. Thus arbitrary-query closure with flat old booking against remaining influence is impossible under this policy; a genuine original-source liability transfer is still required. Full FEI remains OPEN.')
claim={
 'claim_id':'A012-DISJOINT-PRIVATE-MUX-ADMISSION','version':8,'exact_statement':statement,
 'hypotheses':['uniform Boolean signs and physical coordinates; costs bits, K=4+2/ln2',
 'supplied normalized complete reference and original source certificate; all terminal CE and all old bookings retained',
 'profiles use actual cofactor means; all conditional nonempty laws are inherited, no oracle true nonempty replacement',
 'each conversion pays FULL D(new||inherited) from the same account; earlier variance stock remains diminished',
 'expected frontier solvency is distinguished from per-branch solvency and universal representation existence',
 'finite target and old source/reference exactly as saved in v7; no new function-class admission'],
 'statement_sha256':sha256(statement.encode()).hexdigest(),
 'contributors':['A012/account03: new partial-profile charged transaction, continuum certificate and next reference-independent floor','A013: prior scoped v7 review, signed original-source query ledger and first-query payment','A003: previously established vacuum-ray physical-projection algebra; no novelty claim for it'],
 'proof_source':{'derivation':str(R/'DERIVATION.md'),'author':str(R/'out/PARTIAL.json'),'replay':str(R/'out/REPLAY.json'),'full_calibration_negative_control':str(R/'out/PROFILE.json'),'source_receipts':str(R/'out/SOURCE_RECEIPTS.json')},
 'proof_dependencies':[{'claim_id':'A012-DISJOINT-PRIVATE-MUX-ADMISSION','version':7,'scope':'existing admitted function grammar and original saved target; NEW v7 increment accepted at scoped A013 review, not universal old chain'},
 {'claim_id':'A013-SCOPED-REVIEW-A012-V7','version':1,'scope':'consumed independent review of NEW both-private variance/source increment'},
 {'claim_id':'A013-ORIGINAL-CHILD-BANK-PHYSICAL-QUERY','version':1,'scope':'signed query/source ledger and exact target; finite first-query and two-query failure independently recomputed here without requiring upstream general theorem'},
 {'claim_id':'A003-ORIGINAL-REFERENCE-VACUUM-RAY-ABSORPTION','version':'source-bound stage18; exact registry ID not assumed','scope':'credited prior algebra only; no proof reliance since needed ray identity is rederived in DERIVATION section2'}],
 'review_records':[{'reviewer':'A013','target_version':7,'result':'HOLDS_NEW_V7_INCREMENT_ONLY','source':str(A13/'REPORT.md')},{'reviewer':'A012 separate replay','target_version':8,'result':str(a['assertions']+b['assertions'])+' final saved assertions; own independent implementation is NOT independent-agent acceptance'}],
 'status':'AUTHOR_PROOF_AND_EXACT_REPLAY; NEW_V8_INDEPENDENT_AGENT_REVIEW_PENDING; FULL_FEI_OPEN',
 'supersedes':['A012-DISJOINT-PRIVATE-MUX-ADMISSION@7, incrementally; original artifact preserved'],
 'refutes':['universal continuation with unchanged old5/(4ln2) booking against remaining influence, even allowing arbitrary references, at all-three-shared-query frontier of this actual target'],
 'first_unproved_line':'Transfer/retire the physically owned original shared booking at the third query, recording its liability and all executed costs against ONE original source; a reference-only update cannot overcome the proved influence floor.',
 'next_consumers':consumers}
# Do not invent an exact upstream registry ID: the credited ray algebra is proved here.
claim['proof_dependencies']=claim['proof_dependencies'][:3]
write(R/'CLAIMS.json',[claim])
total=a['assertions']+b['assertions'];write(R/'out/EXACT_RESULTS.json',{'status':'PASS','assertions_final_outputs_once':total,'author_assertions':a['assertions'],'replay_assertions':b['assertions'],'full_calibration_pilot_assertions_separately_not_added':read(R/'out/PROFILE.json')['assertions'],'states_per_final_implementation':27,'continuum':'analytic convexity plus two exact endpoint signs, not a numerical grid','author_seconds':a['seconds'],'replay_seconds':b['seconds'],'max_estimated_MB':80,'no_Lean_claim':True})
next_action='A013/A086/A094 reconstruct v8. At the saved third-shared-query frontier, transfer the original shared5/(4ln2) liability to its actual owner/source while carrying the paid half-profile conversion and both full terminals; no booking deletion, reference reset or renewed variance stock.'
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B03','packet_id':'A012','gap_id':'C020-COMPLETE-REFERENCE-COLLIDING-CHILDREN','attempt_id':'A012-stage20-paid-partial-profile-handoff',
 'method':'exact KL Bregman transaction; full conditional nonempty transport; SAME diminished source and signed physical query ledger; continuum via convexity; integer-Walsh author and independent direct-character/integer-log replay',
 'mathematical_delta':'Consumes A013 scoped v7 acceptance and pays the actual failed second query by a half-profile handoff even charging FULL D(new||old); >1/128 bit remains, continuum[1/2,5/8]>1/256. Next all-shared frontier is reference-independently impossible with flat old booking/remaining influence.',
 'deliverable_status':'COMPLETE_LOCALLY','mathematical_status':'NEW_V8_PAID_HANDOFF_EXACT_AUTHOR_PROOF_PENDING_INDEPENDENT_AGENT_REVIEW; OLD_V7_NEW_INCREMENT_SCOPED_ACCEPTED; FULL_FEI_OPEN',
 'claim_versions_used':claim['proof_dependencies'],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':8,'change':'same-packet refinement; pays prescribed conditional profile handoff and exposes next reference-independent bookkeeping floor'}],
 'source_artifacts':[str(SRC/'out/NEXT_TARGET.json'),str(A13/'REPORT.md'),str(A13/'DERIVATION.md'),str(R/'DERIVATION.md'),str(R/'out/PARTIAL.json'),str(R/'out/REPLAY.json')],
 'next_consumers':consumers,'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['universal original-source booking transfer at the next physical query is not proved; arbitrary common quotient/cover existence and full FEI remain OPEN','new v8 independent-agent acceptance pending; supervisor mirror verification unobserved','checklist T-20261023-410 working update failed: checklist lock held too long; completion receipt will be recorded separately','brain self-care degraded/unverified: owner model98.4h, state83.0h, latest dream33.7h stale at wake; current owner context/personalization affected'],
 'packet_ids':['A012']}
write(R/'PROGRESS.json',progress);write(R/'PACKET_DELTA.json',progress)
report=f'''# A012 stage20: paid partial-profile handoff

## exact target, quantifiers, hypotheses and units

Continue the prescribed actual s0-then-s1 history of v7's six-bit both-private target with its ORIGINAL Q, old5/(4ln2) booking and SAME already diminished source. K=4+2/ln2; CE/KL/entropy in bits. New general identity holds for every finite supplied P,Q and fixed cell partition, but source admission remains conditional. The realized result is an expected frontier certificate, not separately nonnegative daughter stocks. Full FEI OPEN.

## sources actually read, revisions and theorem locators

Current BOARD (supervisor12:06UTC snapshot), full B03 notes v2, own STATUS, full machine AGENTS and execution protocol2026-10-11-execution-v2; A012 stage19 source target, source proof/fixture/source certificate excerpts and outputs; A013 stage19 REPORT, full DERIVATION, CLAIMS identifiers and history code. A003 LEARNED stages18/19 and A001 latest source/transaction notes were read as neighboring warnings/credited vacuum-ray algebra. The mathematical brain's read-only two-wording recall supplied no profile-transaction proof premise. Earlier campaign/paper intake is inherited from prior stages, not claimed freshly reread. Exact current source hashes are saved. Current user campaign deadline23Oct14:49UTC supersedes legacy protocol dates.

## complete derivation or exact first unsupported line

DERIVATION Sections1-4 proves the paid transaction. Set profile r_t=(1-t)q+t p and retain the WHOLE inherited conditional law in every cell. Charge c=D(R_t||Q), rather than treating conversion as free. Its exact net rebate is ((1-t)/t)[D(r_t||q)+D(q||r_t)]>=0. At t=1/2 this is symmetric KL. FULL calibration has zero net rebate under the same charge: the initial control correctly catches that failure.

For the actual four second-query histories, q_empty=21/32 and p_empty=(1/16,1,9/16,1). The half update gives reference empty masses(23/64,53/64,39/64,53/64). BOTH nonconstant full terminal conditional KLs and all off-support reference atoms remain. CONSTANT terminals also retain positive inherited CE; none is silently set to zero. Original variance reserve remains diminished. After the FULL new conversion debit, the SAME original account exceeds terminal CE+old booking by>1/128 bit. Every real t in[1/2,5/8] leaves>1/256 by convexity of CE+D and the exact endpoints.

The generic structural test is weighted signed query draws minus the exact rebate <=unused original stock, with all earlier booked costs retained. It is closed as a reference/certificate operation on already admitted functions, preserving inherited whole conditional shapes under physical marginalization; it does not assert automatically funded arbitrary histories or admit an opaque core. The v7 function-class hidden-core guard is unchanged.

FIRST universal unsupported line: at the THIRD shared query, transfer the old physical shared liability to a named original source. Actual expected I becomes1/4, while even zero future CE/conversion would give K/4-5/(4ln2)=1-3/(4ln2)<-1/16 bit. Thus no reference-only improvement can repair this flat-booking/remaining-influence policy. This is an accounting-policy obstruction, not a refutation of FEI or v7/v8.

## executed validation with domain, arithmetic, commands and outputs

Four frozen specs precede their respective jobs/addendum. Commands from A012: python -X utf8 runs/{R.name}/code/profile20.py; python -X utf8 runs/{R.name}/code/replay20.py. The first full-calibration pilot is retained in out/PROFILE.json as a negative control; final author uses the paid half update. All27 actual shared states are retained without symmetry reduction. Author: integer FWHT, rational direct physical-edge influence, exact prime-log identities and24-term rational atanh bounds with a proved remainder. Replay: independently reconstructed truth formula, direct character sums, spectral-energy influence,4096th-power integer binary-log bounds and20-term rational ln2 bounds. The final outputs contain {total} assertions ({a['assertions']} author + {b['assertions']} replay), counted once; earlier pilot {read(R/'out/PROFILE.json')['assertions']} predicates are reported separately. Final math runtimes {a['seconds']:.3f}s and {b['seconds']:.3f}s; estimates<=80MB and cutoffs50s. No>300MB search, GPU, automatic dimension increase, detached work or Lean check.

Replay verifies >1/128 at the half step, >1/256 at both continuum endpoints, positive retained conditional KL at BOTH nonconstant leaves, positive constant terminal CE, exact original source/reference reconstruction, A013's first-query remaining child bank>1/4 and untouched selector allowance>1/2, and the next reference-independent floor<-1/16. Own separate replay is not independent-agent acceptance of v8.

## proof dependencies and changed downstream conclusions

Consumes A013-SCOPED-REVIEW-A012-V7@1 at its stated NEW-increment scope and A013-ORIGINAL-CHILD-BANK-PHYSICAL-QUERY@1 for the exact signed ledger/target, independently checking the relevant finite facts here. Prior v7 artifacts remain intact. A003's vacuum-ray observation is credited and the needed algebra rederived; no uncertain registry identifier is invented. The new transaction closes the actual next-profile handoff that A013 left unpaid. Its third-query floor redirects the universal continuation toward original-liability ownership, not another spectrum/reference search. No independent acceptance of all older syntax-chain premises, universal quotient/cover existence, or full FEI is asserted.

## one next mathematical action and independent reviewer

{next_action} Exact next terminal data, current R, previous conversion debit and the reference-independent necessary source are saved in out/NEXT_TARGET.json. No external message was sent.

## actual persistence receipts or precise save blocker

All four protocol files, derivation, frozen specs, code and exact outputs are local in this run; rolling STATUS is two lines and WORKLOG/LEARNED receive dated entries. FINAL_VALIDATION checks exact schema keys, matching progress/packet copy, hashes and<20MB. Supervisor remote mirroring is UNOBSERVED and no git/brain write was performed. Checklist working T-20261023-410 failed with a shared lock; the final attempt receipt will be saved separately. Brain self-care is degraded/unverified: owner-model98.4h, state83.0h, latest dream33.7h stale at wake, affecting current owner context and personalization; not mathematical premises. All bounded math jobs have ended.

## Universal bridge

This moves C024 by paying the actual second interacting physical query through a conditional-profile handoff from the SAME diminished original source, with the full new conversion KL, both full terminals and old5/(4ln2) retained; the half-step leaves>1/128 bit and a continuum leaves>1/256. It consumes C020's scoped-reviewed v7 collision. Universal source/quotient existence and original-liability transfer remain open. The next all-shared frontier has a reference-independent>1/16-bit floor under unchanged booking, so transferring its named liability without deletion or bank renewal is the shortest route to a reusable universal witness step rather than another isolated class theorem.
'''
md(R/'REPORT.md',report)
from fractions import Fraction as F
states=a['states'];front=[states[str((x,y,-1))] for x in (0,1) for y in (0,1)]
write(R/'out/NEXT_TARGET.json',{'original_target':str(SRC/'out/NEXT_TARGET.json'),'frontier':'after s0,s1 with t=1/2 paid profile handoff; NEXT physical s2 on all four branches','old_booking_coefficient_1_over_ln2':'5/4','new_conversion_debit_prime_log_bits':a['frontier']['conversion_charge_D_R_Q'],'current_complete_terminals':front,'third_query_expected_I':'1/4','reference_independent_upper_bound_even_zero_new_costs_bits':b['third_query_any_reference_margin_upper_bound_bits'],'requirement':'Transfer old shared liability with explicit ownership and SAME original source. Keep all earlier costs including this full conversion, both whole terminal references and CE. No deletion or renewed stock.'})
sources=[P,ROOT/'BOARD.md',ROOT/'claude/B03/STREAM_NOTES.md',SRC/'out/NEXT_TARGET.json',SRC/'CLAIMS.json',A13/'REPORT.md',A13/'DERIVATION.md',A13/'CLAIMS.json',A13/'code/history19.py',ROOT/'agents/A003/LEARNED.md',ROOT/'agents/A001/LEARNED.md']
write(R/'out/SOURCE_RECEIPTS.json',{'read_at_stage':'2026-10-23 A012 stage20; hashes reflect final local observation','sources':[{'path':str(x),'sha256':sha256(x.read_bytes()).hexdigest(),'bytes':x.stat().st_size} for x in sources],'prior_full_campaign_paper_intake':'inherited stage history; not claimed freshly reread','brain_recall':'read-only two-wording query; no imported mathematical premise','remote_mirror':'UNOBSERVED'})
stamp=datetime.now(timezone.utc).isoformat()
md(BASE/'STATUS.md',f'STATE: A012 stage20 COMPLETE LOCALLY: v7 scoped HOLDS consumed; v8 second query PAID with FULL conversion KL, >1/128 bit left; all t[1/2,5/8]>1/256;{total} exact checks; FEI OPEN; v8 review pending.\nNEXT: A013/A086/A094 review paid half-profile handoff; transfer original old5/(4ln2) liability at third shared query, whose remaining-I floor<-1/16 even with zero CE; carry same diminished source and all conversion costs.\n')
def append(p,s):
 with p.open('a',encoding='utf-8',newline='') as f:f.write(s)
append(BASE/'WORKLOG.md',f'\n{stamp} Stage20 {R.name}: consumed A013 NEW-v7 review and actual first-query/second-deficit ledger. Full profile calibration plus full conversion canceled (negative control). Changed mechanism to partial half-profile: exact symmetric-KL rebate pays actual second query with >1/128 bit after ALL new/old debits; convexity yields real interval[1/2,5/8]>1/256. Author/replay {total} final assertions PASS, <=80MB estimates. Third-query E I=1/4 makes flat old booking impossible for ANY reference (floor<-1/16); next ownership transfer remains open. v8 independent-agent review and mirror unobserved; checklist working failed shared lock; no brain writes.\n')
append(BASE/'LEARNED.md',f'\n## Stage20 ({stamp}): partial profile update pays its own FULL conversion\n\nFor finite supplied P,Q and fixed cell profile p,q, set r=(1-t)q+t p and R|cell=Q|cell. Exact CE(P,Q)-CE(P,R)-D(R||Q)=((1-t)/t)[D(r||q)+D(q||r)]>=0 for0<t<1. Full calibration has ZERO net rebate under the same charge; partial calibration can strictly outperform it. At half-step rebate=Jeffreys(r,q), with every conditional KL/reference-only atom retained. This is reference arithmetic, not a universal influence-priced source theorem.\n\nActual v7 target after s0,s1: p_empty=(1/16,1,9/16,1), inherited q_empty=21/32, r_half=(23/64,53/64,39/64,53/64), remaining mean I=1/2. FULL conversion cost is paid; old5/(4ln2) and diminished original bank retained; >1/128 bit remains. CE+D convexity extends >1/256 margin to every real t in[1/2,5/8]. Constants still have positive CE, both nonconstant conditional terminal KLs positive. Final {total} assertions, independent numerical arithmetic paths, no independent-agent v8 acceptance yet.\n\nAfter exposing all3 shared bits mean I=1/4, but K/4-old=1-3/(4ln2)<-1/16 even with zero terminal cost. NO reference construction alone can solve flat-booking/remaining-I heredity at this frontier. Next must transfer the physically owned liability while retaining executed costs, not renew variance or erase old booking. Vacuum-ray shape closure does not imply budget solvency.\n')
proto=read(P)['required_per_run'];claimkeys=set(proto['claim_fields']);progresskeys={x.split(' (')[0] for x in proto['progress_fields']}
assert set(claim)==claimkeys;assert set(progress)==progresskeys
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
assert len((BASE/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all(x.stat().st_size<20_000_000 for x in R.rglob('*') if x.is_file())
receipt={'status':'PASS','protocol_keys':True,'statement_hash':claim['statement_sha256'],'final_assertions':total,'files':[{'path':str(x.relative_to(R)),'bytes':x.stat().st_size,'sha256':sha256(x.read_bytes()).hexdigest()} for x in sorted(R.rglob('*')) if x.is_file() and x.name!='FINAL_VALIDATION.json'],'remote_mirror':'UNOBSERVED','independent_agent_review':'PENDING_NEW_V8'}
write(R/'out/FINAL_VALIDATION.json',receipt)
print(json.dumps({'status':'PASS','assertions_final':total,'files_sealed':len(receipt['files']),'run':str(R)}))
