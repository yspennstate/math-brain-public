from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
run=Path(__file__).resolve().parents[1];agent=run.parents[1]
def write(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def dump(p,x):write(p,json.dumps(x,indent=2,ensure_ascii=True)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
p=json.loads((run/'out/CHECK_PILOT.json').read_text(encoding='utf-8'))
v=json.loads((run/'out/CHECK_FULL.json').read_text(encoding='utf-8'))
a=json.loads((run/'out/AUDIT.json').read_text(encoding='utf-8'))
spec=json.loads((run/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
auditspec=json.loads((run/'out/AUDIT_FROZEN_SPEC.json').read_text(encoding='utf-8'))
assert p['status']==v['status']==a['status']=='PASS'
assert spec['helper_sha256']==sha(run/'code/check.py')
assert auditspec['sha256']==sha(run/'code/audit.py')
statement=('For every integer K>=4, Boolean core g on a finite uniform cube and fixed normalized complete Qg of finite Cg=CE(Pg,Qg)<=K Ig, let F=t*x*Maj3(y)*g on independent physical bits. Put eps=2^(-3K), q(1)=1-3eps and q(2)=q(4)=q(7)=eps, zero elsewhere. The ORIGINAL source is delta_{t,x} tensor q tensor Qg, original quota A=K(Ig+7/2), and permanently booked old tau=K Ig-Cg+1/4. With c=9K/4-log2(1-3eps)/4, the actual t query costs K and leaves SAME bank S_t=5K/2-c-1/4>0. Prescribed x has influence1 but identical full child spectra/zero means, zero singleton and nonempty-overlap phase energy, zero entropy decrement, zero conditional/vacuum refund. Keeping its literal inherited source would leave3K/2-c-1/4<0, so a nonempty change is necessary for that SAME-rate whole-terminal completion. The actual physical C4 frequency map with columns(2,4,7) preserves the actual spectrum and cycles the four nonempty Maj3 labels. Averaging the CURRENT source over this orbit changes q to uniform4, retaining the exact Qg and returning c-2. Perform the average BEFORE x: all intermediate banks stay nonnegative; the full original ledger after both genuine queries is 2K+E terminal CE+tau+S_final=A, S_final=3K/2-9/4>=15/4. Both complete physical terminal bills are Cg+2. At g=1,K4 this is a fully priced all-relevant five-bit witness, with no reference-only occupied labels and old quarter retained. It is a necessary zero-energy source conversion paid by an original-reference refund, not an arbitrary positive target paid by nonexistent phase energy. No arbitrary-core source is supplied. The general finite-cost orbit defect identity is Delta CE=-R_G+T_G; T_G=0 here and remains unpaid generally. Semigroup means/boundaries and entropy are unchanged by both physical queries; fixed-function small/large-time integrability remains valid.')
claim={'claim_id':'A066-NONFLAT-DATA-RELEASE-AND-SOURCE-PAYMENT','version':4,'exact_statement':statement,'hypotheses':['Finite independent fair Boolean coordinates; integer K>=4','Fixed supplied complete core reference Qg with CE<=K Ig; no universal supplier assumed','Both actual t branches and both x outcomes, physical reaches and full terminal costs retained','Original A and old tau fixed before the prefix; C4 averaging precedes x invoice and keeps the exact Qg','Actual squared spectrum is invariant under the displayed C4; arbitrary source-only averaging is not free'],'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A066'],'proof_source':str(run/'DERIVATION.md'),'proof_dependencies':[],'review_records':[],'status':'ANALYTIC_AUTHOR_PROOF_EXACT_CERTIFICATES_REVIEW_PENDING','supersedes':[{'claim_id':'A066-NONFLAT-DATA-RELEASE-AND-SOURCE-PAYMENT','version':3,'scope':'Earlier profile bounds, literal-reference obstruction, calibration repair and boundary estimate remain at their original scopes. Adds a paid necessary zero-energy nonempty handoff after a genuine paid prefix; no prior theorem withdrawn.'}],'refutes':[],'first_unproved_line':'Bound noninvariant actual-source symmetry defect T_G by legitimate R_G plus SAME unused original bank, with actual compatible required handoff; arbitrary-core initial influence price remains unpaid.','next_consumers':['A096','A097','A068','A070','A085','A088','A094','A099']}
dump(run/'CLAIMS.json',[claim])
next_action='For a useful necessary isospectral handoff with NONINVARIANT actual spectrum, bound exact defect T_G=sum(P-PG)log2(Q/QG) by legitimate orbit refund R_G plus SAME unused ancestor bank; keep old tau/physical invoices/Qg and both full terminals. A096/A097/A068/A094 review the supplied-core transaction and temporal order.'
pr={'protocol_revision':'2026-10-11-execution-v2','run_id':run.name,'stream':'B14','packet_id':'A066','gap_id':'C019-C024-INHERITED-DATA-AND-TERMINAL-PAYMENT','attempt_id':'A066-stage10-necessary-isospectral-orbit-refund','method':'Consume A068 actual-invariant orbit mechanism and A096/A097 zero-energy frontier; construct and price mandatory nonempty repair after a real paid prefix, all-K exact algebra and independent physical certificates.','mathematical_delta':'Necessary zero-singleton/isospectral profile conversion paid at SAME original K>=4 with arbitrary supplied core, old tau and BOTH full terminals; c-2 refund pays next physical K invoice and leaves3K/2-9/4>=15/4. Exact nonuniform defect DeltaCE=-R_G+T_G isolates remaining universal step.','deliverable_status':'COMPLETE_LOCALLY_REVIEW_PENDING','mathematical_status':'SUPPLIED_CORE_ANALYTIC_PAYMENT_AND_EXACT_CERTIFICATES_FULL_FEI_OPEN','claim_versions_used':[],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':4}],'source_artifacts':[str(run/'DERIVATION.md'),str(run/'out/CHECK_FULL.json'),str(run/'out/AUDIT.json'),str(run/'out/SOURCES.json')],'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Arbitrary initial core reference is not influence-priced universally','Nonuniform useful orbit defect T_G and other wrapper compatibility requirements unpaid','Independent review/supervisor adoption/remote mirrors unverified','Brain self-care stale personal/dream notes; current exact task files used instead'],'packet_ids':['A066']}
dump(run/'PROGRESS.json',pr);dump(run/'PACKET_DELTA.json',pr)
report=f'''# A066 stage10: a necessary zero-energy handoff paid by the original source

## exact target, quantifiers, hypotheses and units

Pay ONE necessary conditional-NONEMPTY profile conversion at an isospectral zero-phase-energy query after a genuine already-paid prefix, keeping SAME original rate/source, old debit and both full terminal bills. Theorem: every integer K>=4, arbitrary Boolean core g with a SUPPLIED fixed complete Qg satisfying Cg<=K Ig, and physical F=t*x*Maj3*g. The original peaked four-label reference is fully priced explicitly. After paid t, literal x completion is insolvent despite DeltaH=0 and zero phase energy. Actual C4 source averaging BEFORE x returns c-2, pays that query and leaves **3K/2-9/4>=15/4**. K4,g1 is a fully priced five-bit example without a core assumption or occupied ghost mass. Units bits; heat boundary/area uses natural logs. This is a source transaction, not a new FEI class theorem or universal source supplier.

## sources actually read, revisions and theorem locators

Read BOARD(2026-10-23 11:35UTC), B14 STREAM_NOTES v2, own STATUS and preceding stage9 DERIVATION. Protocol 2026-10-11-execution-v2 was read completely. out/SOURCES.json records37 current source hashes: required baseline campaign protocol/registries/plan/supplement, supplied paper texts and current mathematical intake. Four PDF-extracted texts require the explicit cp1252 fallback already documented in stage9. No manuscript theorem is needed for this self-contained calculation. Source hashes identify read versions; this is not a fresh independent audit of every manuscript theorem.

A068 run20261023T065356Z REPORT: vacuum-only all-rate source no-go and ACTUAL-invariant orbit repair. A096 run20261023T053800Z REPORT: phase-energy supplied-source payment/parity obstruction. A097 run20261023T062140Z REPORT: sign-bin zero-singleton NONISOSPECTRAL payment, and NEXT asking for a NECESSARY isospectral zero-energy conversion. These changed the route: another vacuum-only counterexample would duplicate A068. We use its orbit mechanism on a genuinely necessary zero-energy conversion, with a real paid prefix and arbitrary supplied core unchanged. A097's coherent-controller formulas/Gram constants are not imported as a proof premise. B14's old heat/Maj/addressing tests were handled in previous stages, not restarted. No new external literature or brain-store theorem dependency.

## complete derivation or exact first unsupported line

DERIVATION sections1-5 prove every quantifier. The actual Maj3 spectrum is uniform on FOUR nonempty labels W=(1,2,4,7). The explicit physical invertible map A with columns(2,4,7) cycles these labels and leaves the actual spectrum invariant. The same old source's four-copy average becomes uniform on W, retaining Qg exactly; convexity proves the refund, and the actual cost changes from Cg+c to Cg+2.

With eps2^(-3K), **9K/4<c<9K/4+1/4**. Original A=K(Ig+7/2), fixed old tau=(K Ig-Cg)+1/4. After t invoice K the same original bank is5K/2-c-1/4>0. Prescribed x has zero singleton, zero nonempty products, isospectral children, zero entropy/CE/vacuum refunds, but still physical invoice K. Literal terminal completion would leave3K/2-c-1/4<0; all means and vacuum masses are zero so vacancy repair cannot help. The nonempty change is therefore necessary for that specified SAME-rate continuation. Averaging current source FIRST leaves5K/2-9/4 before x and3K/2-9/4 afterwards; no temporary overdraft or borrowed future credit occurs. Exact original-owner identity:2K+E full terminal CE+tau+S_final=A.

The zero entropy/heat debit is kept distinct from the physical influence tariff. No phase energy is fabricated; the actual reference-cost refund pays the required query. This does not show arbitrary prescribed positive-cost targets are free. For a noninvariant actual spectrum, the exact remaining defect is DeltaCE=-R_G+T_G, with T_G=sum(P-PG)log2(Q/QG). The dictator control shows orbit averaging can COST>1bit when this invariance is missing. First unsupported universal line: price this actual noninvariant defect from the legitimate R_G refund and SAME unused original owner, or construct an influence-priced arbitrary-core source.

All means here are zero and H remains H(g)+2 through both queries. Thus both heat areas are equal, signed empty boundary0, and the source refund has heat units ln2*(c-2). Fixed-function semigroup integrability at0 and infinity remains verified analytically; no universal pointwise integrable envelope or full FEI claim is inferred.

## executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json precedes the searched helper; v1 pilot is preserved, then v2 adds explicit pre-query solvency/erasure commutation and an adversarial noninvariance control on the SAME frozen core/rate inputs. V2 pilot: all6 labelled Boolean cores on d0,1,12 source cases,10 supplier-admitted and2 rejected, **{p['exact_assertions']} exact assertions PASS in{p['seconds']:.6f}s**. Full: all278 labelled cores d0..3, two supplied references(actual and half-uniform), rates4,5,8,16:2224 cases,2200 supplied and24 supplier-rejected. **{v['exact_assertions']} exact assertions PASS in{v['seconds']:.6f}s**, maximum physical truth dimension8. The rejected references fail Cg<=K Ig and are not admitted by the theorem. No symmetry quotient or automatic dimension increase.

Code/check.py recomputes complete physical integer FWHT spectra, independent edge influences, both actual prefix children and all four terminals, product-source support/normalization, zero phase products, actual orbit invariance, four original-source copies, exact complete CE identities, original old-debit cancellation, temporal order and every source bank. Every logarithmic sign is reduced to an EXACT rational power comparison after clearing rational exponents. No floating sign, log approximation or interval overlapping zero is a certificate. Saved rows give source states for each frozen rate at the no-core example. Counts are new-stage domains, not revisions to stage9's259078+31; pilot/rerun counts are not added.

Independent code/audit.py uses DIRECT physical character sums, not main FWHT/imports, on the all-relevant five-bit no-core witness; checks both prefix outcomes, all four terminals, and K4..32 orbit/coefficient bounds. Its separately frozen audit passed **{a['exact_assertions']} exact assertions in{a['seconds']:.6f}s**. This is independent AUTHOR-side representation, not an independent-agent acceptance. All-K extension follows analytic inequalities(1)-(7), not the finite K list.

Commands from A066: `python -X utf8 runs/{run.name}/code/check.py pilot`, same with `full`, then `python -X utf8 runs/{run.name}/code/audit.py`. Main and audit frozen maximum55s, enforced during verification; actual full runtime{v['seconds']:.6f}s stayed below it. Memory estimates150MB/30MB, actual peaks unmeasured; no >300MB job, GPU, detached job or compiler. No other running work stopped or throttled. The saved compute snapshot is timestamped13:57:59 local and was already stale; no current health claim or governor restart was based on it.

## proof dependencies and changed downstream conclusions

New theorem is reconstructed from product spectra, physical source permutation, convexity and elementary exact cost algebra; proof_dependencies=[] for this version. A068's general orbit principle is explicitly credited as the consumed mechanism, not called a new theorem or independent acceptance. A096/A097 remain valid at their supplied-source scopes; their arbitrary-core initial supplier and general nullspace targets are not declared solved. The present actual necessary isospectral handoff is paid even with phase energy exactly zero, by a different source owner/refund. Other A079/A050 wrapper compatibility requirements must be checked before inserting this source-level transaction there.

A066 v3's counterexample, literal-reference limits, boundary and calibration statements stay unchanged in their immutable run. This v4 extends the SAME bundled source-payment claim, avoiding another broad unreviewed candidate. Independent review and full FEI remain OPEN. No numerical controller constants or old assertion counts are revised.

## one next mathematical action and independent reviewer

{next_action} This is a source-bound request for later consumers, not a message sent, acceptance or downstream adoption. Removing actual uniform-orbit invariance, rather than buying more fixed-bank reset rounds, targets the surviving universal mechanism.

## actual persistence receipts or precise save blocker

The four exact-field protocol files, complete derivation, frozen source versions, code and outputs are saved within A066. out/RECEIPTS.json verifies hashes/sizes, statement hash, progress/delta identity, required fields, two-line STATUS and all artifacts below20MB. Rolling WORKLOG/LEARNED are appended. Supervisor copying, GitHub/mirror persistence and independent review remain unverified; no git/mail/shared-tree/other-agent/brain mutation or deletion. Current session wake was performed: brain self-care is degraded/unverified because owner-model/state-of-mind/latest dream are stale; those personal-context notes were not mathematical premises or current preferences.

## Universal bridge

C024 history transfer and C019 stopping-tree payment gain a necessary zero-energy CONDITIONAL-NONEMPTY handoff after a real paid prefix at the SAME original K for every integer K>=4, with arbitrary supplied core, both complete terminals and old debit retained. The exact refund c-2 pays the next invoice and leaves3K/2-9/4>=15/4, with no universal FEI constant improvement claimed. What remains is the actual noninvariant symmetry defect T_G and the arbitrary-core initial source price. NEXT targets T_G at a useful compatible handoff using the same diminished owner, because the present actual invariant sector is paid and additional symmetric fixed-bank cycles would not move the universal bridge.
'''
write(run/'REPORT.md',report)
status=f'STATE: A066 stage10 saved: necessary isospectral zero-energy nonempty handoff PAID by SAME-source C4 refund after real prefix; allK>=4, final3K/2-9/4; {v["exact_assertions"]}+{a["exact_assertions"]} exact checks PASS; review pending; FEI OPEN.\nNEXT: Bound actual noninvariant orbit defect T_G by legitimate R_G plus SAME unused ancestor bank, preserving old tau/physical invoices/Qg/full terminals; A096/A097/A068/A094 review necessary transaction.\n'
write(agent/'STATUS.md',status)
now=datetime.now(timezone.utc).isoformat()
work=f'\n{now} {run.name}: stage10 consumed A068 orbit and A096/A097 zero-energy frontier. F=t*x*Maj3*g, supplied Qg unchanged, old tau=KIg-Cg+1/4; t prefix paid then x literal completion insolvent. Actual C4 nonempty averaging BEFORE x refunds c-2 and leaves SAME original3K/2-9/4>=15/4 for ALL integerK>=4. Main {v["exact_assertions"]}, audit {a["exact_assertions"]} checks PASS; no noninvariant/initial supplier claim. NEXT: bound exact T_G defect, not more symmetric resets.\n'
learn=f'\n{now} {run.name}: Zero JS/phase/entropy debit does NOT remove a physical K*Inf invoice in a supplied-source ledger. Necessary zero-energy source handoff: F=t*x*Maj3*g, q_M=(1-3eps,eps,eps,eps),eps2^(-3K),K>=4. With same originalA=K(Ig+7/2),oldtau=KIg-CEg+1/4, paid t leaves5K/2-c-1/4>0 but literal x would leave3K/2-c-1/4<0. The ACTUAL invariant physical frequency C4 (columns2,4,7) averages q to uniform4, retaining Qg, giving refundc-2. Average BEFORE x to avoid overdraft; final3K/2-9/4>=15/4, all old/full terminals retained. General orbit conversion=-R_G+T_G with T_G=sum(P-PG)log(Q/QG); actual invariance givesT0, source-only symmetry is insufficient (dictator control costs>1bit). Arbitrary initial core supplier/nonuniform defect remain open.\n'
for name,entry in [('WORKLOG.md',work),('LEARNED.md',learn)]:
 q=agent/name;s=q.read_text(encoding='utf-8') if q.exists() else ''
 if run.name not in s:write(q,s+entry)
write(run/'CHECKPOINT.md','STATE: Stage10 v4 complete locally; necessary zero-energy orbit handoff paid from SAME owner; FEI OPEN.\nNEXT: '+next_action+'\n')
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
assert set(claim)==set(protocol['claim_fields'])
assert set(pr)=={s.split(' (')[0] for s in protocol['progress_fields']}
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert claim['statement_sha256']==hashlib.sha256(statement.encode('utf-8')).hexdigest()
assert all('## '+h in report for h in protocol['report_fields'])
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert len(status.splitlines())==2
files=[]
for q in sorted(run.rglob('*')):
 if q.is_file() and q.name!='RECEIPTS.json':
  assert q.stat().st_size<20*1024*1024
  files.append({'path':str(q),'bytes':q.stat().st_size,'sha256':sha(q)})
for q in [agent/'STATUS.md',agent/'WORKLOG.md',agent/'LEARNED.md']:files.append({'path':str(q),'bytes':q.stat().st_size,'sha256':sha(q)})
for row in files:
 q=Path(row['path']);assert q.stat().st_size==row['bytes'];assert sha(q)==row['sha256']
dump(run/'out/RECEIPTS.json',{'status':'PASS','timestamp':now,'schema':'exact field sets PASS','statement_sha256':claim['statement_sha256'],'files':files,'full_fei':'OPEN','independent_review':'PENDING','remote_mirror':'UNVERIFIED'})
print(json.dumps({'status':'PASS','main_assertions':v['exact_assertions'],'audit_assertions':a['exact_assertions'],'version':4,'files_hashed':len(files),'full_fei':'OPEN'}))
