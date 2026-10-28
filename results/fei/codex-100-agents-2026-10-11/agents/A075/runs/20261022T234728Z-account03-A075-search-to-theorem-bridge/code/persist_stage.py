from pathlib import Path
from datetime import datetime, timezone
import json, hashlib

ROOT=Path(__file__).resolve().parents[1]
HOME_AGENT=ROOT.parent.parent
PEERS=HOME_AGENT.parent
OLD=ROOT.parent/'20261021T173628Z-account03-A075-search-to-theorem-bridge'
SOURCE=PEERS/'A089/runs/20261022T225420Z-account03-A089-repair-specialist'
def read(path):return json.loads(path.read_text(encoding='utf-8'))
def save(path,obj):path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def statement_hash(s,h):return hashlib.sha256(json.dumps({'statement':s,'hypotheses':h},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()

def main():
    stamp=datetime.now(timezone.utc).isoformat()
    analytic=read(ROOT/'out/DIAGONAL_ANALYTIC.json')
    finite=read(ROOT/'out/DIAGONAL_FINITE.json')
    review=read(ROOT/'out/REVIEW_SIGNED.json')
    assert len(finite['rows'])==6 and sum(r['states'] for r in finite['rows'])==35
    assert all(r['local_repair_feasible'] and r['all_preterminal_full_eligible'] and r['all_preterminal_D_nonnegative'] for r in finite['rows'])
    assert len(review['rows'])==18 and sum(r['negative'] for r in review['rows'])==2
    assert analytic['checks']>=341
    # Correct only a profile-count metadata typo, leaving the frozen search spec intact.
    save(ROOT/'out/SPEC_CORRECTIONS.json',{'original_spec_sha256':sha(ROOT/'out/FROZEN_SPEC.json'),'correction':'five fixed initial prefix profiles per n, not six; the 35 retained-state domain and every arithmetic/runtime constraint are unchanged','reason':'implementation computes r,a,b,c,z; d is not a separate initial profile'})
    source_paths=[
      PEERS.parent/'BOARD.md', PEERS.parent/'claude/B15/STREAM_NOTES.md',
      SOURCE/'REPORT.md',SOURCE/'CLAIMS.json',
      PEERS/'A072/runs/20261021T225156Z-account03-A072-exact-walsh-engine/REPORT.md',
      PEERS/'A074/runs/20261022T225155Z-account03-A074-independent-reproducer/REPORT.md',
      OLD/'REPORT.md',OLD/'PROOF.md',OLD/'CLAIMS.json',
      Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
    save(ROOT/'out/SOURCE_INVENTORY.json',{'saved_at':stamp,'sources':[{'path':str(p),'sha256':sha(p)} for p in source_paths],'intake_scope':'current board/lead/status and the listed peer reports read this stage; old campaign/paper intake preserved by previous run, not claimed as fresh rereading'})
    statement=(
      'For the actual uniform disjoint-block family F_n=J(g_n^6), g_n negative on {0,1,2}, J=-h(x xor1), h negative on {0,1,2,4,8,16,32,6,17,40}, keep the original rate4 two-query debit D0=(2e1+e2)U_b/((U_b+U_c)/2) after block0 original coordinates2=0,0=0. Formally continue padding queries3,4,... by D_(j+1)=2(D_j+e_j) in the zero child and zero in the full constant-selected-plus sibling Z. Then exactly R_j=S_j-D_j=S_Z+2^j(S_b-D0-S_Z). With p=3*2^-n, E=log2(e), A=24log2(3)-32/3-16E, and fixed remaining dimension d, R_(n,d)/p tends to K_d=A-2^(5-d)(2+E). K4<0<K5, while both full endpoint capacities and their net booked debits at d4 and d5 are eventually positive. Thus no such no-transfer policy can remain feasible uniformly through depth n-6. At the last d5-to-d4 row, with these bookings fixed, transfer a_n=-R_(n,4) from the untouched sibling Z is sufficient and minimal, leaves positive donor residual, preserves every label and earlier stopped terminal, and has root-weighted cost/p^2 tending to -(16/3)K4 in (13.8457460552,13.8457460553). Nonnegative net debit legality at every intermediate growing-depth ancestor for all n is not asserted. Complete exact chain certificates cover n=8,12,24 only; n=16,32,48 certify endpoints only. No universal FEI theorem.'
    )
    hypotheses=['uniform physical Boolean cube, six disjoint core blocks, base2 Fourier entropy and S=4I-H',
      'specified original two-query proportional debit, signed query excesses, every full terminal and old label retained',
      'd fixed before n tends to infinity; n>=d+2; prescribed continuation is algebraic, without assumed feasibility',
      'minimal last-row flow is among zero-mean sibling transfers with the prescribed debit labels fixed']
    own={'claim_id':'A075-GROWING-DEPTH-SAME-DEBIT-ENDPOINT','version':1,'exact_statement':statement,'hypotheses':hypotheses,
      'statement_sha256':statement_hash(statement,hypotheses),'contributors':['A075'],
      'proof_source':['PROOF.md sections1-5','code/diagonal.py','out/DIAGONAL_ANALYTIC.json','out/DIAGONAL_FINITE.json'],
      'proof_dependencies':['finite character orthogonality, exact physical pivotal identity and Shannon chain rule reconstructed in PROOF.md','own pinned sparse-core and rational log primitives listed in out/FROZEN_SPEC.json'],
      'review_records':[{'reviewer':'A075','independent_reviewer':False,'verdict':'AUTHOR_ALGEBRA_AND_EXACT_CERTIFICATES_CHECKED','scope':'exact telescoping, endpoint coefficient signs, independently simplified first-order closed form, and declared finite states'}],
      'status':'AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW','supersedes':[],
      'refutes':['Proposed uniform growing-depth payment by the unchanged all-to-zero no-transfer policy; not the scoped fixed-depth theorem'],
      'first_unproved_line':'Derive arbitrary inherited-history component admission after an exact subsidy has been received and its donor outgoing flow spent; all-dimensional intermediate net-debit legality also remains outside this endpoint theorem.',
      'next_consumers':['A072','A074','A089','A092','A085']}
    peer=read(SOURCE/'CLAIMS.json')[0]
    peer_original_hash=peer['statement_sha256']
    peer['statement_sha256']=statement_hash(peer['exact_statement'],peer['hypotheses'])
    peer['proof_source']=[str(SOURCE/'REPORT.md'),'PROOF.md section6','out/REVIEW_SIGNED.json']
    peer['review_records']=peer['review_records']+[{'reviewer':'A075','independent_reviewer':True,
      'verdict':'HOLDS_FOR_GENERIC_THEOREM_AND_18_TERMINAL_SIGNS_ONLY',
      'scope':'positive-weight support, sharp signed-capacity kernel including T=0/P=0; all18 actual physical full S signs via own original truth-core FWHT and physical edges. Four whole-history coupled policies/parked ancestry not newly accepted.',
      'source_declared_statement_sha256':peer_original_hash,
      'source_hash_convention':'source digest preserved separately; local claim digest canonical statement+hypotheses',
      'evidence':'out/REVIEW_SIGNED.json and PROOF.md section6'}]
    peer['status']='PARTIAL_INDEPENDENT_REVIEW_GENERIC_AND_TERMINAL_SIGNS'
    peer['first_unproved_line']='This independent review does not accept the four source historical coupled allocations or their parked2tau ancestry. The source universal admission gap remains open.'
    save(ROOT/'CLAIMS.json',[own,peer])
    previous=read(OLD/'PROGRESS.json')
    progress={
      'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B15','packet_id':'A075',
      'gap_id':previous.get('gap_id','G-R-MISMATCH'),'attempt_id':'A075-stage7-diagonal-inherited-credit',
      'method':'exact inherited-ledger telescoping, fixed-remaining-dimension limit, sharp fixed-booking sibling flow, independent physical-terminal reconstruction',
      'mathematical_delta':'Growing depth n-6 defeats unchanged no-transfer booking although fixed depth is eventually payable; last-row minimal root subsidy has exact positive p^2 coefficient. Independent review confirms A089 generic signed-capacity theorem and all18 full terminal signs, without promoting its historical policies to accepted.',
      'deliverable_status':'COMPLETE_LOCAL_SOURCE_AND_CERTIFICATES','mathematical_status':'RESTRICTED_ENDPOINT_PROOF_REVIEW_PENDING; FULL_FEI_OPEN',
      'claim_versions_used':['A075-FIXED-DEPTH-RARE-PADDING-SAME-DEBIT@1 (comparison, not a uniform premise)','A089-SIGNED-TERMINAL-COMMON-KERNEL-REPAIR@1 (partial independent reconstruction)'],
      'claims_created_or_changed':[own['claim_id']+'@1',peer['claim_id']+'@1 (partial review only)'],
      'source_artifacts':['PROOF.md','out/FROZEN_SPEC.json','out/DIAGONAL_ANALYTIC.json','out/DIAGONAL_FINITE.json','out/REVIEW_SIGNED.json','out/SOURCE_INVENTORY.json'],
      'next_consumers':['A072','A074','A089','A092'],
      'next_action':'A074/A092 review the fixed-d quantifier and original-debit identity; then expose a physical data bit in the subsidized terminal while carrying the same incoming subsidy and already spent donor flow.',
      'stagnant_substantive_attempts':0,
      'blockers':['No independent reviewer acceptance of the new endpoint theorem yet.','Universal component-level admission and all-dimensional intermediate nonnegative net-debit legality are unproved.','Brain self-care degraded: owner model/state-of-mind sources stale; not used as mathematical evidence.','Supervisor mirror not verified by this agent; no git authorized.'],
      'packet_ids':['A075']}
    save(ROOT/'PROGRESS.json',progress)
    (ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())
    report=f'''# A075 B15 stage7: inherited credit at growing depth

## exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. For the actual uniform Boolean F_n=J(g_n^6), entropy in bits and S=4I-H, retain the original rate4 two-query debit and every full terminal. The exact remaining-credit law is R_j=S_Z+2^j(S_b-D0-S_Z). At remaining dimension4, R/p tends to -2.59607738536; at dimension5 it tends to +0.846617655529. Thus uniform no-transfer continuation fails despite the earlier fixed-depth eventuality. The last untouched sibling pays the sharp prescribed-booking deficit with positive capacity left. Its root-weighted cost/p^2 tends to 13.8457460553. This is a local endpoint theorem, not all-dimensional admission.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL revision2026-10-11-execution-v2, current BOARD (B15 snapshot2026-10-22 23:50UTC), B15 STREAM_NOTES v2, own rolling status and prior stage6 proof; A072 saturated-donor report20261021T225156, A074 independent report20261022T225155, and A089 signed-terminal report/claim20261022T225420. Source hashes are in out/SOURCE_INVENTORY.json; copied own helpers are pinned in the frozen spec. Prior campaign/paper intake remains background, without claiming a fresh full rereading or using a new literature theorem. The owner-model and state-of-mind brain sources are stale; self-care is degraded/unverified and those personal-context notes are not mathematical evidence.

## complete derivation or exact first unsupported line

PROOF.md supplies the complete finite Walsh/occupied-spectrum chain rule, original debit, exact recurrence, its fixed-remaining-dimension asymptotics, independent closed-form first-order check, and sharp fixed-booking last-row transfer. Only fixed INITIAL profiles are expanded, so multiplying by 2^j for j=n-d-2 is justified with an explicit o(p) remainder; no uniform fixed-depth expansion is assumed. K4<0<K5 and A+K4>0 are rationally certified. Full S and D are both positive at the last parent and child eventually; the deficit is inherited-credit exhaustion, distinct from A089's negative S endpoints.

Scope restriction: all earlier FULL residuals are eventually positive by the exact monotone formula, but nonnegative NET debits at every growing-depth ancestor for all n are not proved. Three finite full chains certify them on their stated domain. The positive root transfer cost is forced only with the prescribed descendant bookings fixed: reassigning the new bookings through the full-capacity kernel gives zero flow here because both raw full children are positive. Thus the theorem refutes the specified routing, not all no-transfer policies. A089's negative full terminals, independently reconstructed here, force flow even with reassignment. First unsupported universal line: derive component-level admission under the next physical query after a subsidy is assigned, with donor flow already spent and all old labels retained. The source A089 generic signed theorem and all18 terminal signs are independently reconstructed; its four historical coupled policies/old parked ancestry are not newly accepted here.

## executed validation with domain, arithmetic, commands and outputs

Before searches, out/FROZEN_SPEC.json fixed n=8,12,24 complete zero chains and n=16,32,48 endpoints only:35 retained states, no symmetry reduction or automatic escalation. The pilot n8 completed in {read(ROOT/'out/DIAGONAL_PILOT.json')['seconds']:.3f}s. Full finite computation took {finite['seconds']:.3f}s with {finite['checks']} recorded helper predicates. All three full chains have nonnegative net bookings and positive full preterminal residuals; every final deficit is positive and exactly payable by its last untouched sibling. Endpoint-only jobs do not certify their omitted prefixes. A separate metadata correction records that five, not six, initial profiles are computed per n; no search domain changed.

code/diagonal.py --analytic records {analytic['checks']} helper predicates, exact rational coefficient cancellations and rigorous signs; code/review_signed.py reconstructs18 original truth-core restrictions with {review['checks']} helper predicates in {review['seconds']:.3f}s, including exactly two negative full capacities. Both use exact Fraction arithmetic and 192-bit directed rational logarithm enclosures with80 atanh terms and a proved remainder. Floating displays are diagnostic only. Predicate counters include interval primitive checks and are not counts of distinct theorems. Commands were python -B -X utf8 code/setup_stage.py, code/diagonal.py --pilot, code/diagonal.py --analytic, code/diagonal.py, code/review_signed.py, and code/persist_stage.py, using paths relative to this run. The analytic command was repeated only after adding the independent closed-form equality checks. Estimated memory<=150MB; no >300MB job, GPU, detached process or Lean compiler launched. Prior Lean timeout is preserved, not called verification.

## proof dependencies and changed downstream conclusions

No empirical absence of failures is promoted to a theorem. Exact character orthogonality, the finite Shannon chain rule and explicit core spectra are reconstructed in PROOF.md. A075 fixed-depth@1 remains valid in its stated order of quantifiers; the new endpoint result blocks its proposed uniform no-transfer extension. A089's generic signed allocation theorem and18 terminal signs receive scoped independent support, with the positive-weight-support convention preserved. Whole-history admission remains distinct. The new endpoint proof awaits A074/A092 independent acceptance.

## one next mathematical action and independent reviewer

NEXT: after A074/A092 check the exact original-debit diagonal law, expose a physical data bit in a subsidized terminal, carrying the SAME incoming subsidy and the donor's already spent outgoing flow. Derive the conditional admission inequality from component spectra, rather than assuming mean full S covers the debit. A089/A072 are the intended mathematical consumers. No messages or edits to their folders were made.

## actual persistence receipts or precise save blocker

All seven report fields, CLAIMS.json, byte-identical PROGRESS/PACKET_DELTA, proof, frozen specs, code and exact outputs are saved locally in this immutable run. out/PERSISTENCE.json records per-file hashes and sizes after schema and statement-hash checks. STATUS.md is two lines; dated WORKLOG and LEARNED entries record the result and scope. No active own computation remains at close. Supervisor GitHub/brain copying and independent acceptance are not asserted; the specific user order forbids this agent's git/brain writes. No checklist identifier was supplied for this stage, and no shared checklist was modified under the own-folder-only order.

## Universal bridge

This stage moves C019 stopping-tree payment from fixed-depth eventuality to an exact growing-depth inherited-credit obstruction and a sharp, positive-root-cost last-row sibling repair at unchanged rate4: the coefficient is Gamma4=-(16/3)K4 in (13.8457460552,13.8457460553), while the donor retains positive capacity. It also independently checks the signed-capacity theorem and18 actual full terminal signs supporting the nonlocal route. Universal component admission, legality of every growing-depth nonnegative net debit, and closure under further physical queries with donor flow already spent remain unproved. NEXT carries that exact subsidy into the next query, directly testing the missing history-sensitive payment mechanism instead of adding another isolated fixed-depth class result. Full FEI remains OPEN.
'''
    (ROOT/'REPORT.md').write_text(report,encoding='utf-8')
    (HOME_AGENT/'STATUS.md').write_text('STATE: A075 stage7 saved: growing-depth original-debit R/p tends K4=-2.596077; last unused sibling pays sharp root cost 13.845746*p^2; A089 generic+18 signs independently checked; new proof review pending; FEI OPEN.\nNEXT: A074/A092 audit diagonal quantifiers; query subsidized terminal carrying SAME incoming flow and spent donor flow. All-n intermediate nonnegative-debit legality remains outside endpoint theorem.\n',encoding='utf-8')
    with (HOME_AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
        f.write(f'\n## {stamp} stage7 ({ROOT.name})\nDerived exact remaining-credit telescoping R_j=S_Z+2^j Delta_n and fixed remaining-dimension K_d. K4<0<K5 defeats uniform unchanged no-transfer continuation. Proved sharp fixed-booking last-row sibling repair and root cost Gamma4; certified35 retained states (three full chains only), plus independent A089 generic theorem/18 full terminal signs. New theorem review pending. No claim of all-n intermediate net-debit legality or universal FEI. No own jobs left running; supervisor mirrors unverified.\n')
    with (HOME_AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
        f.write(f'\n## {stamp}: fixed depth does not control growing-depth inherited credit\nFor the unchanged two-query debit, Delta_n=S_b-D0-S_Z=-(128/3)(2+log2(e))*p^2+O(p^3(1+abs(log p))). Exact R_j=S_Z+2^j Delta_n allows j=n-d-2 without a uniform fixed-depth expansion. K_d=A-2^(5-d)(2+log2(e)); K4<0<K5. The last full child can have S>0 and still lack capacity because its original debit is larger. Its untouched sibling repairs the prescribed account with minimal incoming -R4 and root cost/p^2 -> -(16/3)K4=13.8457460552547..., leaving positive donor residual. This is not a proof that all ancestor net debits are nonnegative for all n. A089 signed-capacity minimum E(-s)_+ is valid on positive-weight support with nonnegative net debit;18 physical signs independently reproduced, historical policies not newly accepted.\n')
    protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
    fields=protocol['required_per_run']
    assert set(own)==set(fields['claim_fields']) and set(peer)==set(fields['claim_fields'])
    expected={x.split(' (')[0] for x in fields['progress_fields']}
    assert set(progress)==expected
    assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
    for claim in read(ROOT/'CLAIMS.json'):
        assert claim['statement_sha256']==statement_hash(claim['exact_statement'],claim['hypotheses'])
    for heading in fields['report_fields']:assert '## '+heading in report
    assert len((HOME_AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
    records=[]
    for path in sorted(ROOT.rglob('*')):
        if path.is_file() and path.name!='PERSISTENCE.json':
            assert path.stat().st_size<20*1024*1024
            records.append({'path':str(path.relative_to(ROOT)),'bytes':path.stat().st_size,'sha256':sha(path)})
    save(ROOT/'out/PERSISTENCE.json',{'saved_at':stamp,'schema_checks':'PASS','canonical_statement_hashes':'PASS','progress_delta_byte_identity':'PASS','files':records,'mirrors':'SUPERVISOR_PENDING_NOT_VERIFIED','independent_endpoint_review':'PENDING'})
    print(json.dumps({'saved':str(ROOT),'files':len(records),'retained_states':35,'peer_states':18,'analytic_checks':analytic['checks'],'finite_checks':finite['checks'],'review_checks':review['checks'],'claim_hash':own['statement_sha256'],'schema':'PASS'}))

if __name__=='__main__':main()
