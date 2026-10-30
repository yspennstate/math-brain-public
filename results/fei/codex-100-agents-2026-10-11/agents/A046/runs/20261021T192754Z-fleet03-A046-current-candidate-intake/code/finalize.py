from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,datetime

RUN=Path(__file__).resolve().parents[1]; HOME=RUN.parents[1]
RID=RUN.name; NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def iv(v):return tuple(map(Q,v))
r=read(RUN/'out/CODE7.json'); result=read(RUN/'out/RESULT.json')
checks=0
def ck(p):
 global checks
 assert p
 checks+=1

# Independently audit only saved exact records, not execution status strings.
for name in ['CODE7','CODE1','DICTATOR']:
 v=read(RUN/f'out/{name}.json')
 for law in [v['P'],*v['children_P']]:
  ck(sum(map(Q,law))==1)
 for key in ['R','B_old','B_new','K','TC','sigma','net_reset']:
  lo,hi=iv(v[key]);ck(lo<=hi)
source=Path(r'agents\A040\runs\20261021T164919Z-fleet03-A040-credit-insufficiency-tests')
mapping={'R':'residual','B_old':'inherited_full_bank','B_new':'product_full_bank','sigma':'signed_reset','TC':'TCmean','K':'K','net_reset':'conversion_debit'}
for ours,theirs in [('CODE7','NONFLAT'),('CODE1','PILOT'),('DICTATOR','DICTATOR')]:
 a=read(RUN/f'out/{ours}.json');b=read(source/f'out/{theirs}.json')
 for ka,kb in mapping.items():
  x,y=iv(a[ka]),iv(b[kb]);ck(max(x[0],y[0])<=min(x[1],y[1]))
ck(Q(r['U'])==Q(r['release'])+Q(r['full_retirement'])+Q(r['remaining_U_mean']))
ck(iv(r['revised_source_bank'])[0]>Q(1,800))
ck(iv(r['full_actual_payment_margin'])[0]>Q(1,800))
ck(iv(r['source_full_bank'])[1]<-Q(21,50))
ck(iv(r['specific_payment_margin'])[0]>Q(5,32))
for b in r['separator_continuation']:
 ck(iv(b['good_margin'])[0]>0);ck(iv(b['CE_price4_margin'])[1]<0)
 ck(iv(b['terminal_bank'])[0]>0);ck(iv(b['after_held_U'])[0]>0)
 for p in b['leaf_P']+b['leaf_references']:ck(sum(map(Q,p))==1)
save(RUN/'out/FINAL_AUDIT.json',{'status':'PASS','checks':checks,'method':'saved-record rational audit, source interval comparison against distinct 36-term checker, normalization and conservation','timestamp':NOW})

claims=read(source/'CLAIMS.json'); a040=claims[1]
actual=hashlib.sha256(a040['exact_statement'].encode('utf-8')).hexdigest()
ck(actual==a040['statement_sha256'])
a040['review_records'].append({'reviewer':'A046','verdict':'HOLDS_AT_FULL_STATED_SCOPE_WITHOUT_REPAIR','source':str(RUN/'PROOF.md'),'method':'independent activation coefficient derivation, direct character sums and rational intervals for all three stated fixtures; entire source 800-case census not rerun','repair_supplied':False,'reviewed_at':NOW})
a040['status']='INDEPENDENT_REVIEW_HOLDS_LOCALLY_BY_A046'
statement=('For the uniform Boolean sign F=1+[WUV OR S(U OR V)](g-1), four singleton controls, g=(-1,-1,-1,1,1,1,1,1), query core bit0 then S in both children, stop separator accounting. Carry the original full root-product reference Q with the actual common physical kernel (fair fallback on source-zero rows), then one explicit reset to full child product references R_b and no more resets through S. Retain the A046 v3 original U: Uroot=23/32,U0=3/4,U1=17/32,booked release5/64. Both S nodes are erasure-rate4-good but have full-reference drops exceeding4Inf. Their complete signed terminal accounts are positive. Retire 5/16 from U0 and17/32 from U1 at their original half reaches: total27/64, retaining mean7/32. The original root bank 4I-H-D(P||Q)-U is<-21/50; after this policy-certified retirement it exceeds1/800. The original B_new<-67/1000 and R>41/1000 reproduce A040. C_new=B_new+27/64 pays the complete actual node debit L=CEroot-mean CEchild+5/64-4Inf, with C_new-L>1/800; C_new-R>5/16 is a decomposition check, not a second spend. All four final full terminal laws/references and remaining reserve are retained. This is one exact fixed-policy transaction with no unspecified prior withdrawals; it supplies no arbitrary-history or universal FEI bound.')
new={'claim_id':'A046-PRESCRIBED-SEPARATOR-RESERVE-RETIREMENT','version':1,'exact_statement':statement,'hypotheses':['Uniform physical Boolean cube; bit entropy and KL.','Exactly stated singleton controller, code7 core and labelled physical queries; S is next after the first core query.','Original full product reference, actual common child kernel, all zero-source reference rows retained, strictly positive normalizers; one explicitly priced child-product reset only.','Original U ledger retained with explicit retirement and unchanged booked release; no additional unspecified prior debit is supplied or assumed paid.','Complete signed CE continuation and all terminal laws retained; R and L are not spent twice.'],'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A046'],'proof_source':{'run_id':RID,'files':['PROOF.md','code/certify.py','out/CODE7.json','out/RESULT.json','out/FINAL_AUDIT.json']},'proof_dependencies':[{'claim_id':'A040-ACTIVATION-CORE-QUERY-FULL-TERMINAL-BANK','version':1,'statement_sha256':actual,'status':'INDEPENDENT_REVIEW_HOLDS_BY_A046'},{'claim_id':'A046-SEPARATOR-LAYER-CUTOFF-RESERVE','version':3,'statement_sha256':claims[0]['statement_sha256'],'status':'INDEPENDENT_REVIEW_HOLDS_BY_A040'}],'review_records':[],'status':'EXACT_FINITE_CERTIFICATE_EXTERNAL_REVIEW_PENDING','supersedes':[],'refutes':['For this fixture, erasure B_S<4Inf_S suffices to pay the full-reference CE drop from that query influence alone.','Retiring only17/64 and paying isolated R establishes full original-root reference admission; the root account remains negative.'],'first_unproved_line':'A history-stable sufficient retirement condition before another active core query, with arbitrary earlier debits and both full terminal references, is not established.','next_consumers':['A040','A039','A047','A050','A087','A092','A094','B10','B20']}
save(RUN/'CLAIMS.json',[a040,new])

progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RID,'stream':'B10','packet_id':'A046','gap_id':'G-R-MISMATCH-SAME-OWNER-CORE-REFERENCE','attempt_id':'A046-stage7-prescribed-reserve-retirement','method':'Independent A040 review; direct-character rational interval fixture; explicit policy-dependent reserve retirement with root-admission and full signed CE telescope.','mathematical_delta':'A040 v1 independently HOLDS. For fixed code7 core/S continuation retire27/64 from original U, keep booked5/64 and held7/32; original full root account and complete actual core-node payment gain>1/800. Erasure-good/full-reference-good shortcut rejected.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'EXACT_FINITE_CERTIFICATE; NEW_REVIEW_PENDING; UNIVERSAL_HISTORY_AND_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':'A040-ACTIVATION-CORE-QUERY-FULL-TERMINAL-BANK','version':1},{'claim_id':'A046-SEPARATOR-LAYER-CUTOFF-RESERVE','version':3}],'claims_created_or_changed':[{'claim_id':a040['claim_id'],'version':1,'change':'independent unchanged acceptance'},{'claim_id':new['claim_id'],'version':1,'change':'new exact finite continuation certificate'}],'source_artifacts':[str(source/'PROOF.md'),str(source/'CLAIMS.json'),'out/SOURCE_MANIFEST.json','out/FROZEN_SPEC.json','out/ROOT_ADMISSION_SPEC.json','out/CODE7.json','out/FINAL_AUDIT.json'],'next_consumers':new['next_consumers'],'next_action':'A040/A092 independently reconstruct the source admission and complete CE telescope; then expose one further core query before S using the SAME original U/reference and explicit prior debit, proving retirement remains eligible or retaining its exact liability.','stagnant_substantive_attempts':0,'blockers':['No universal retirement/admission theorem; arbitrary-seed entropy remains unpaid.','New certificate independent external review and supervisor private-repository copying unverified.'],'packet_ids':['A046']}
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)

lean=RUN/'out/LEAN_RECEIPT.json'
lean_status='pending or not returned at report generation'
if lean.exists():
 try:
  obj=read(lean);lean_status=str(obj.get('result',{}).get('status',obj.get('status','UNVERIFIED')))
 except Exception:lean_status='receipt not parseable; no Lean certification claimed'
report=f'''# exact target, quantifiers, hypotheses and units

A046/B10 stage7 consumes A040's new full-reference result and freezes one prescribed continuation, not the retired singleton tax. Four independent fair controls have A=WUV OR S(U OR V). The exact three-bit core is (-1,-1,-1,1,1,1,1,1). Query core bit0, then the sole S bit in BOTH children, then stop separator accounting. All entropy/KL is bits and influence is physical. Full FEI remains OPEN.

The finite transaction pays the entire signed core-query/reference bill from the original two child accounts after an explicit retirement of unneeded separator reserves. The actual original-root reference account has margin >1/800. Both nonconstant core children, one child-product reset, the original reference-only rows and all four full terminal laws are retained. Independent review of the new transaction remains pending.

# sources actually read, revisions and theorem locators

Execution protocol 2026-10-11-execution-v2 read in full. BOARD and B10 notes v2, own STATUS/LEARNED/WORKLOG and the preceding substantive report were used for continuation; the rolling files preserve the six earlier substantive stages. BOARD's A040 stage6 supersedes the already-completed six-bit NEXT; the old B10 scalar-review instruction was completed in earlier stages. Current dispatch therefore consumes the new A040 objection rather than repeating that work. Campaign README/status/three registries/next actions/plan and supplemental campaign/claims/counterexamples/seed/mapping/source notes were read at relevant locators. out/SOURCE_MANIFEST.json pins whole-file bytes and identifies encoding; the four context paper texts were inspected, not independently reviewed, and no paper theorem is a dependency. The older status deadline is overtaken by the user's explicit current 23 October endpoint; no schedule was altered.

The substantive dependency is A040 run20261021T164919Z PROOF sections Complete original reference, Six-bit payment, and Failure of the first both-nonconstant extension, CLAIMS v1 hash {actual}. Its complete mathematical statement is copied unchanged with an independent A046 review. The source review also corrects the copied digest of A046 v3; copied actual digest and old source-declared digest remain distinct, and no old source was edited. Brain recall yielded no premise used. Wake warned of stale personal notes; the warning was reported and those notes were not relied on.

# complete derivation or exact first unsupported line

PROOF.md reconstructs the general activation entropy formula directly from finite coefficients and independently accepts A040 v1 without repair. Direct character sums reproduce its code1, code7 and dictator reference accounts.

For code7 the unchanged Uroot=23/32 splits into booked5/64 plus mean child U=41/64. The first partial candidate retired only17/64 and paid R, but failed full root admission because S_old=4I-H-D(P||Q)-U<-21/50. That partial result is preserved and rejected as a full source-payment claim.

The final fixed policy retires5/16 of child0 U and17/32 of child1 U at original half reaches. Thus total retirement=27/64 and held mean=7/32. The full source identity is 23/32=5/64+27/64+7/32. Source admission S_old+27/64>1/800 and the independently checked complete-node telescope C_new-L>1/800 hold at the SAME rate4 and original Q. C_new-R>5/16 is only the residual decomposition; it is not a second debit.

Both S nodes satisfy B<4Inf but their full-reference CE drops exceed4Inf. Their negative local signed price-four margins are paid from their corresponding retained terminal accounts. These terminal accounts are already inside the child source accounts and are never added again. Both restricted spectra, actual reference normalizers, four final law/reference pairs, physical influences and full cross-entropies are serialized.

First unsupported universal line: before another core query, show that retirement cannot create an unpaid future separator liability and remains affordable under arbitrary incoming debits/references. This fixed-policy certificate does not establish it, a width-independent full controller theorem, or FEI.

# executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json precedes the first three-root computation. ROOT_ADMISSION_SPEC.json precedes the corrected full-source admission computation, with unchanged finite family. No symmetry quotient, search, GPU, detached process or dimension increase. Maximum dimension7, estimated100MB. The independent helper uses integer direct character sums, Fraction, separate physical edge influence counts and 32-term rational atanh intervals, with a proved remainder and outward2^-110 log rounding. Source A040 uses a different FWHT/36-term implementation.

Command: python -X utf8 runs/{RID}/code/certify.py. Final run: {result['checks']} exact assertions PASS, {result['runtime_seconds']:.4f}s arithmetic runtime. Initial version passed967 assertions; full continuation version1174; final1182. These are successive checks of one fixed domain, not independent cases added together. The finalizer checks{checks} saved-record assertions, overlaps all three fixtures' seven source interval fields, verifies normalizations and source admission. The finalizer does not claim a fresh exhaustive n=3 search. Failed root admission is not counted as a proof of the initial proposed payment.

Compute state/interventions were read: the recorded state was ok, CPU80.3%, available memory11.7GB; no work was stopped. Fresh memok before the only possible >300MB formal check exited0; receipt in out/MEMOK.txt. Lean status at save: {lean_status}. It concerns only Rat conservation 46/64=5/64+27/64+7/32, never the entropy or policy proof. No repeated Lean job. See actual full receipt for target, toolchain and transitive axiom result; no broader Lean theorem is claimed.

# proof dependencies and changed downstream conclusions

A040-ACTIVATION-CORE-QUERY-FULL-TERMINAL-BANK@1 is independently accepted unchanged by A046. A046 v3 remains accepted by A040 at separator-only scope. The new claim depends on these earlier versions and the self-contained finite certificate, so no proof cycle is introduced. Retired tax-free/O(p), release-only and sole-B_new payment repairs remain false. A favorable net reset sign and an erasure-good separator still do not prove full terminal affordability. The substantive new substitution is an explicitly prescribed reserve retirement PLUS full root admission and signed continuation checks.

# one next mathematical action and independent reviewer

{progress['next_action']} The policy restriction and unused reserve must be justified again at that next history; no new rate, root bank or favorable net-reset shortcut is authorized.

# actual persistence receipts or precise save blocker

All four protocol files, PROOF.md, code, frozen specifications and exact outputs are local. STATUS has exactly two lines; WORKLOG and LEARNED append the result. Final local schema, equality, statement-hash and file-size checks are in out/RECEIPTS.json. All files are below20MB. Only A046 research outputs were changed; required runtime wake/checklist/formal-check helpers may maintain their own runtime receipts. No git, email, external messages, foreign research-folder mutation, brain write, trading access, GPU or detached job. Private repository/brain copying and independent acceptance of the new claim remain unverified.

## Universal bridge

This stage advances C019 stopping-tree payment and C024 history transfer by consuming the exact both-nonconstant code7 obstruction, identifying one policy-certified retirement from the SAME inherited separator bank, and paying the full original-reference core query with margin>1/800 while retaining all signed continuation and terminal costs. It improves the universal FEI constant by zero. The missing implication is history-stable admission of such a release before another active core query with arbitrary earlier debits. NEXT targets that admission directly, because it is what separates the paid finite transaction from a universal stopping-tree proof.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(HOME/'STATUS.md').write_text('STATE: A046 stage7 saved: A040 full-reference v1 independently HOLDS; code7 prescribed core/S continuation pays full original source after27/64 inherited-U retirement, margin>1/800;1182 exact checks PASS; new review pending, FEI OPEN.\nNEXT: A040/A092 review complete source/terminal ledger; allow one further core query before S with SAME U,Q and prior debit, proving retirement eligibility or keeping its actual liability.\n',encoding='utf-8')
if RID not in (HOME/'WORKLOG.md').read_text(encoding='utf-8-sig'):
 with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{NOW} — {RID}: consumed A040 v1 unchanged, reconstructed all-activation identity and three exact fixtures independently. Partial17/64 retirement paid R but root admission failed; final27/64 retirement certifies SAME original-Q full query margin>1/800. Both erasure-good S nodes have full CE drops>4Inf, retained with four terminal references. Main1182 exact assertions; saved-record/source audit{checks}. New review and universal history eligibility pending.\n')
if '2026-10-21 stage7:' not in (HOME/'LEARNED.md').read_text(encoding='utf-8-sig'):
 with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-21 stage7: code7 original U23/32, release5/64, childU=(3/4,17/32). Sole B_new is negative despite favorable sigma-E. Retiring only17/64 pays isolated R but leaves original root full-reference admission negative. Under prescribed core0 then S then stop, both S erasures are rate4-good; retire5/16 from child0 and17/32 from child1 at half reaches=27/64, retain mean7/32; root source and complete actual-node margins>1/800. Both S full CE drops exceed4Inf, so keep signed terminal telescope; erasure-goodness alone never pays the reference drop. R is part of full node debit, not a second spend. Policy-certified retirement does not extend to another earlier core query without a new liability proof.\n')

protocol=read(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))['required_per_run']
expected=set(x.split(' (')[0] for x in protocol['progress_fields']);ck(set(progress)==expected)
for c in [a040,new]:ck(set(c)==set(protocol['claim_fields']));ck(hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256'])
ck((RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes())
ck(len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2)
files=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  b=p.read_bytes();ck(len(b)<20_000_000);files.append({'path':str(p.relative_to(RUN)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save(RUN/'out/RECEIPTS.json',{'status':'PASS','timestamp':NOW,'finalizer_checks':checks,'files':files,'private_repository_copy':'UNVERIFIED','new_external_review':'PENDING','full_fei':'OPEN'})
print(json.dumps({'status':'PASS','finalizer_checks':checks,'files':len(files),'new_statement_sha256':new['statement_sha256'],'lean_status':lean_status}))
