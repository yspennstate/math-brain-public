from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p):return json.loads((R/p).read_text(encoding='utf-8'))
def put(p,o):(R/p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
main=read('out/EXACT_CHECK.json');audit=read('out/INDEPENDENT_AUDIT.json')
assert main['status']==audit['status']=='PASS'
statement=('For b=g tensor g on six uniform DATA bits, g=-1 only at000, delta=1/64, '
 'and every pair of balanced Boolean controllers a,c on the same arbitrary finite uniform cube, '
 'let F(0,z)=a(z),F(e0,z)=-c(z),F=b elsewhere and h(y,z)=a(z) or -c(z). '
 'With V the nonempty upper-set potential, W=V minus the marked singleton term, '
 'and Gmark the signed sum retaining W in both control children and V(a),V(c) at the mark query, '
 'GV(F)-2delta Gmark(h)<=321<256 I_DATA(F), and V(F)>=2delta W(h).')
gap=('A compatible influence-priced ORIGINAL marked source for arbitrary Boolean cores and required '
 'physical restrictions, with old debits and both full terminals retained, is not supplied. '
 'Unbalanced descendants and arbitrary tensor seeds are outside the new theorem.')
claim={
 'claim_id':'A021-SAME256-BALANCED-DEPENDENT-MARKED-PAIR','version':1,
 'exact_statement':statement,
 'hypotheses':['uniform finite cubes and base2 logarithms','fixed six-bit tensor seed g tensor g','adjacent DATA vertices0,e0','both controllers balanced; dependence arbitrary','original mark retained in both control outcomes; removed only at its own query'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A021'], 'proof_source':str(R/'PROOF.md'),
 'proof_dependencies':['elementary Walsh Parseval and physical restriction means; exact row factorization rederived in PROOF.md1; no unreviewed theorem used as a premise'],
 'review_records':[{'reviewer':'A021','verdict':'AUTHOR_PROOF_EXACT_CHECKS','main_assertions':main['assertions'],'separate_implementation_assertions':audit['assertions'],'independence':'different implementation, same author; independent-person review pending','lean':'RUNTIME_UNVERIFIED; no formal acceptance'}],
 'status':'AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW','supersedes':[], 'refutes':[],
 'first_unproved_line':None,'next_consumers':['A022','A025','A029','A087','A094']}
put('CLAIMS.json',[claim])
protocol=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B05','packet_id':'A021',
 'gap_id':'B05-ORIGINAL-MARKED-DEPENDENT-PAIR-PAYMENT','attempt_id':'A021-stage22-three-moment-curvature-and-signed-mark-cancellation',
 'method':'exact marked Fourier-sector factorization; correlation-aware three-moment Hessian; light-heavy Parseval; signed DATA/mark cancellation',
 'mathematical_delta':'Closes SAME256 root transfer for ALL balanced dependent controller pairs on the original six-bit adjacent-edit seed. Control remainder<=243; DATA remainder after signed mark<=78; total<=321<336. Source eligibility/hereditary arbitrary-core step remains open.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_AUTHOR_PROOF; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':['A021 prior 20261023T135142Z marked shared-controller repair (extended, not needed as a black box)','A022 stage11 ledger v10 adjacent-interface definitions (rederived)','A025 20261027T001552Z distinct-dependent family (context only)'],
 'claims_created_or_changed':[claim['claim_id']+'@1'],
 'source_artifacts':['PROOF.md','SEARCH_SPEC.json','AUDIT_SPEC.json','code/stage.py','code/audit.py','out/EXACT_CHECK.json','out/INDEPENDENT_AUDIT.json','out/SOURCE_RECEIPTS.json','out/LEAN_ATTEMPT.json'],
 'next_consumers':['A022','A025','A029','A087','A094'],
 'next_action':'Independently reconstruct the correlation-aware marked transfer; then retain this original mark through an unbalanced physical child or supply an arbitrary-core influence-priced original owner, without resetting old debt.',
 'stagnant_substantive_attempts':0,
 'blockers':[gap,'Independent-person mathematical review pending.','Brain wake stale personal-context sources; not used as mathematical premises.','Lean algebra attempt runtime-unverified; no formal certificate.','Supervisor copy and remote mirror unverified.'],
 'packet_ids':['A021']}
put('PROGRESS.json',progress);put('PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

{statement}

This repairs the prior stage's exact NEXT at balanced-root, fixed-seed scope: arbitrary distinct dependent controllers are now admitted. Full FEI remains OPEN. Rung: author proof with exact checks; independent-person review pending. Gmark is a signed marked transition, not unmarked GV(h).

# sources actually read, revisions and theorem locators

Current BOARD B05, B05 STREAM_NOTES v2, own STATUS and LEARNED, prior A021 PROOF Sections1--5 and BALANCED_COROLLARY, A022 stage11 PROOF Sections1--6 and REPORT, and A025 20261027T001552Z PROOF Sections1--5 were inspected. The original shared-controller repair and special a,a*w repair are extended, not re-counted as new results. B05's old remainder-sign objection is already repaired and is not repeated. Protocol fei-execution-protocol/2, revision {protocol['revision']}, was read. Source byte/hash/explicit-decoding receipts cover accessible requested campaign files, prior own reports, source texts and all four context paper texts; selected relevant excerpts are in out/SOURCE_EXCERPTS.json. Loading and hashing a full source is not represented as independent mathematical review of every theorem in it. The threshold/percolation papers are background, not proof premises. Read-only math recall returned generic FEI/restriction warnings, no theorem used here. No network premise, git, mail or external research write is used.

# complete derivation or exact first unsupported line

PROOF.md is self-contained at the new scope. The complete DATA marginal is affine in (Ea,Ec,Eac). Omitting Eac is invalid for dependent controllers. Nonempty-control rows factor into the SAME W(h), with a nonnegative remainder T. Along each light physical restriction path all denominators have floor delta^2; |T''|<110(u^2+v^2+w^2). Three Parseval sums pay at most165, and at most6 heavy controller coordinates pay at most78, so CONTROL drift after the marked source is <=243. The special DATA query contributes precisely the signed marked term R, which cancels its owner transition; all6 DATA remainders total<=78. Thus the full residual is <=321. Balance gives I_DATA>=21/16, hence rate256 pays at least336. Both actual physical outcomes remain throughout; no root singleton credit is renewed. The endpoint V(F)>=2delta W(h) follows from remainder nonnegativity.

First unsupported universal line: {gap} In particular the new theorem is not hereditary under arbitrary restrictions. No full FEI claim, arbitrary controller source payment, or all-seed transfer follows.

# executed validation with domain, arithmetic, commands and outputs

SEARCH_SPEC v1 was saved before the pilot, which passed800 assertions in8.1565s. SEARCH_SPEC v2 freezes the expanded40-fixture domain and helper hash before the final run. The final check covers ALL36 ordered balanced two-bit controller pairs, every physical output/controller coordinate and both outcomes,4 balanced three-bit guards including fractional correlations, constant restriction children, exact source-row identities and complete signed residuals. Fraction spectra and exact prime-log vectors supply equality checks;32-term rational atanh tails supply strict inequalities. Final result: {main['assertions']} counted assertions PASS in {main['seconds']:.4f}s, maximum dimension9. The pilot is subsumed, not added to this count.

AUDIT_SPEC was frozen before the separate implementation. Direct conditional DATA character sums independently reconstruct the moment mean/marginal formulas, sign-law feasibility and derivative denominator/ratio bounds on four3-bit pairs and45 sampled light paths, including endpoints. It imports no production helper. Result: {audit['assertions']} exact assertions PASS in {audit['seconds']:.4f}s. This is same-author different-representation corroboration, not independent-person acceptance. The all-dimensional result follows from the analytic compact-path bounds, not extrapolation from these samples. Hypotheses actually used are located in PROOF.md5; zero coefficients and degenerate correlations use explicit conventions and positive floors.

Commands: python -X utf8 code/stage.py orient; python -X utf8 code/stage.py check; python -X utf8 code/audit.py (from the run directory; the helper resolves paths). Jobs estimate30--60MB, with no dimension escalation, heavy search, GPU or detached research process. No >300MB job was planned, so memok admission was not triggered. Peak memory was not measured. The required algebra-only lean_check attempt returned RUNTIME_UNVERIFIED after120.5s, exceeding the research60s pilot limit; it was not repeated and certifies neither the algebra nor this theorem. Its source hash and exact status are saved in out/LEAN_ATTEMPT.json. No Lean acceptance is claimed.

# proof dependencies and changed downstream conclusions

The new proof reconstructs the relevant sector identities rather than adopting a whole unreviewed A022 bundle. A021's shared-controller and A025's special dependent-controller marked repairs now have an arbitrary balanced-pair extension at the SAME rate256 and original coefficient2delta. Their unmarked-owner counterfamilies remain valid. No prior claim is refuted. The signed marked query cancels DATA interference; replacing it by an absolute debit, dropping either child, or replacing W by unmarked V destroys the stated argument. Review-cap discipline is respected by completing the existing repair mechanism, without opening an unrelated universal candidate.

# one next mathematical action and independent reviewer

{progress['next_action']} A029/A087/A094 should independently reconstruct the complete dependency chain; A022/A025 consume the exact balanced scope only. A useful adversarial review is to derive the special DATA query through the two one-point children before reading Section4, then check its signed R against the retained marked transition. General unbalanced roots and arbitrary-seed floors are not silently inherited.

# actual persistence receipts or precise save blocker

All four protocol files, PROOF, both frozen specifications, code and exact outputs are local in this assigned run. CLAIMS uses exactly protocol claim_fields; PROGRESS/PACKET_DELTA use exactly progress_fields and are byte-identical with packet_ids=[A021]. out/ARTIFACT_CHECK.json checks schemas, hashes, nonempty files and20MB bounds. STATUS has two lines; WORKLOG and LEARNED append this result. Source trees and other agents' folders remain read-only. The required wake reported stale model/state/dream notes and was disclosed before using them; they are not premises. Shared checklist lifecycle is attempted through its prescribed hook and its local output retained; any failure is recorded as a coordination blocker, not mathematical success. No supervisor copy, remote mirror or independent review receipt is claimed. Saved at {now}.

**Universal bridge:** This moves C024 history transfer and C019 payment in B05's marked-GU formulation by removing the identical-controller/special-dependence hypothesis from the SAME256 six-bit adjacent-edit supplier: control changes cost at most243, signed DATA changes at most78, with total321 below the original336 allowance. What remains is a compatible influence-priced original marked source for arbitrary cores and unbalanced continuations, retaining old debits and both terminals. NEXT targets that missing admission/closure step because another balanced small class or a sharper local constant would not supply the universal FEI bridge.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A021 stage22 saved: ALL balanced dependent controller pairs satisfy SAME original marked256 transfer on adjacent six-bit seed; residual<=321<336; exact956+6454 PASS; author proof, review pending; FEI OPEN.\nNEXT: A029/A087/A094 reconstruct signed DATA/mark cancellation; A022/A025 extend ORIGINAL owner to unbalanced descendants/arbitrary cores with old debits and BOTH full terminals; no owner reset.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} Stage22: derived three-moment remainder (Ea,Ec,Eac), bounded correlation-aware control drift243 and signed DATA/mark remainder78, closing SAME256 for all balanced dependent pairs at fixed six-bit seed. Final exact956 plus separate direct moment6454 checks PASS; pilot800 subsumed. Lean algebra runtime-unverified120.5s (no certificate). Full FEI/source eligibility/unbalanced closure OPEN; independent-person review pending. Artifacts: {R.name}.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage22: SAME six-bit adjacent-pair seed and ALL balanced dependent controllers a,c: GV(F)<=2delta Gmark(h)+256 I_DATA(F), delta1/64. Keep W=V minus marked singleton in BOTH control outcomes; query mark to BOTH full V(a),V(c). Exact remainder T depends on Ea,Ec AND Eac. All light paths have positive p floor delta^2 and |Tsecond|<110(u^2+v^2+w^2); three Parseval sums plus at most6 heavy coordinates give243. DATA drift minus2delta R<=78; R is exactly marked query increment, so total321<336. This closes earlier arbitrary-balanced-pair NEXT, not unbalanced descendants, arbitrary seeds or universal original-owner eligibility. Never discard Eac or charge signed R by absolute value.\n')
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
manifest={}
for p in R.rglob('*'):
    if p.is_file() and p.name!='ARTIFACT_CHECK.json':
        b=p.read_bytes();assert 0<len(b)<20_000_000
        manifest[str(p.relative_to(R))]={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
put('out/ARTIFACT_CHECK.json',{'status':'PASS','at':now,'protocol_fields_exact':True,'progress_delta_identical':True,'claim_hash_valid':True,'rolling_status_two_lines':True,'files':manifest})
print(json.dumps({'status':'COMPLETE_LOCAL','claim':claim['claim_id'],'final_checks':main['assertions'],'audit_checks':audit['assertions'],'files':len(manifest),'full_FEI':'OPEN'}))
