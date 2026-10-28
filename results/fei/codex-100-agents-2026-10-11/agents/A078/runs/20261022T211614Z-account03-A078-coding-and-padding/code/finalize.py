from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1];OUT=RUN/'out'
def write(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def jwrite(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
main=json.loads((OUT/'CHECK.json').read_text(encoding='utf-8'));ind=json.loads((OUT/'INDEPENDENT.json').read_text(encoding='utf-8'))
assert main['status']==ind['status']=='PASS'
source=Path('agents/A077/runs/20261021T230123Z-account03-A077-sparse-defect-towers')
up=json.loads((source/'CLAIMS.json').read_text(encoding='utf-8'))
uc=up if isinstance(up,list) else up.get('claims',[])
versions=[str(x.get('claim_id'))+'@'+str(x.get('version')) for x in uc]
source_manifest=[]
for p in [source/'PROOF.md',source/'CLAIMS.json',Path('BOARD.md'),Path('claude/B16/STREAM_NOTES.md')]:source_manifest.append({'path':str(p),'sha256':sha(p),'scope':'read source; the mean-sector input is A077 PROOF section6, collision bounds/first donor sections2 and8'})
jwrite(OUT/'SOURCE_MANIFEST.json',source_manifest)
write(RUN/'code/account_key.lean','import Mathlib\nexample (e B x0 x : ℝ) (hB : 4*e ≤ B) (h0 : x0 ≤ 0) (hx : -4*e ≤ x) : 0 ≤ B-x0+x := by linarith\nexample (B x0 xp xm : ℝ) : x0-(xp+xm)/2 + ((B-x0+xp)+(B-x0+xm))/2 = B := by ring\n')
jwrite(OUT/'LEAN_RECEIPT.json',{'status':'NOT_RUN_COMPUTE_ADMISSION','memok_exit':1,'memok_output':'WAIT: physical free 2.4 GB (need 4.0), commit free 8.2 GB (need 8.0)','intended_command':'python -X utf8 lean_check.py --stmt <account_key.lean examples>','source_sha256':sha(RUN/'code/account_key.lean'),'rung':'analytic proof and exact finite certificates; no Lean compilation or axiom acceptance claimed'})
statement='For every two-vertex Boolean wrapper with shared mass e=2^-d, every finite adaptive private stopping tree, and Xi as in PROOF.md, -4e<=Xi_v<=0 at every descendant. If B>=4e+Xi_o, K_v=B-Xi_o+Xi_v is nonnegative and Xi_o-E Xi_leaf+E K_leaf=B at every frontier. The A077 mean-sector inequality consequently yields PROOF(9) with both complete wrapper terminals and both inherited core entropy decrements. For original V=y*bent_k, even k>=4, S=e(3k/2+5); after preserved debits D0+4e, D0<=S-8e funds every further private continuation from the same original S, leaving at least S-D0-8e (at least3e when D0=0).'
claim={'claim_id':'A078-CODING-PADDING-SIGNED-CONTINUATION','version':1,'exact_statement':statement,'hypotheses':['uniform actual Boolean wrapper; fixed d>=1 and unchanged two shared vertices','finite adaptive PRIVATE physical-coordinate tree; stopping allowed','all inherited old debits preserved; B is the unused original-source budget','guarded donor clause uses original V=y times a quadratic bent sign on even k>=4 bits; added y influence included','entropy corollary uses A077 mean-sector inequality at its stated author-proof scope; arbitrary core and terminal FEI are not assumed'],'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A078'],'proof_source':str(RUN/'PROOF.md'),'proof_dependencies':{'collision_account':'self-contained PROOF(1)-(4); exact finite check and independent Bellman reproduction','entropy_corollary':versions,'source_locator':str(source/'PROOF.md')+' sections6-8; independent continuum review pending'},'review_records':[],'status':'AUTHOR_PROOF_EXACT_FINITE_CHECKS_INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A077','A028','A076','A092','A094']}
jwrite(RUN/'CLAIMS.json',[claim])
gap='G-R-MISMATCH'
prior=ROOT/'runs/20261014T053454Z-account05-A078-coding-and-padding/PROGRESS.json'
if prior.exists():gap=json.loads(prior.read_text(encoding='utf-8')).get('gap_id',gap)
progress={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B16','packet_id':'A078','gap_id':gap,'attempt_id':'A078-private-signed-continuation-1','method':'bounded signed Fourier collision account; exact actual-Boolean spectra and edge counts; independent Bellman all-policy reconstruction','mathematical_delta':'Extends the first 4e donor debit to EVERY further adaptive private stopping tree with one more total 4e allowance from the SAME original guarded-bent C5 surplus; at least3e remains for k>=4 with no other old debit. No child certificate renewed.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'RESTRICTED_ANALYTIC_HISTORY_THEOREM_REVIEW_PENDING; FULL_FEI_OPEN','claim_versions_used':versions,'claims_created_or_changed':[claim['claim_id']+'@1'],'source_artifacts':['PROOF.md','out/CHECK.json','out/INDEPENDENT.json','out/SOURCE_MANIFEST.json','out/LEAN_RECEIPT.json'],'next_consumers':claim['next_consumers'],'next_action':'Carry SAME original Xi/source account through one actual shared-coordinate exposure while retaining D0+4e and continuation debit, complete core bills and both wrapper terminals; independently review A077 mean-sector input.','stagnant_substantive_attempts':0,'blockers':['No general original-source donor eligibility; arbitrary W core entropy remains unpaid.','Shared queries change event geometry; no transfer theorem here.','Fresh memok exit1 prevented Lean execution.','Independent review, supervisor copy and remote mirror unverified.'],'packet_ids':['A078']}
for name in ['PROGRESS.json','PACKET_DELTA.json']:jwrite(RUN/name,progress)
report=f'''# A078: every further private collision uses one original donor

## exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. For every actual two-vertex Boolean wrapper and every finite adaptive PRIVATE stopping tree, the signed collision account in PROOF(2) pays the complete continuation from one original budget. No local constant pays the collision alone, as A077 already showed. This result instead uses its globally bounded signed range. Entropy is in bits and all influence counts physical uniform-cube flips. The guarded-bent clause includes its added y bit and arbitrary padding bits. The entropy-payment corollary retains the A077 mean-sector input at its stated author-proof scope.

## sources actually read, revisions and theorem locators

Read machine AGENTS, full execution protocol {protocol['revision']}, current BOARD (22 Oct21:26UTC), B16 lead notes v2, own rolling status/learned, prior substantive-run inventory, campaign README/CURRENT_STATUS and registry/routing outputs. Read A027 stage17 REPORT and DERIVATION, A028 stage5 REPORT/DERIVATION, and A077 stage6 PROOF sections1-9. Source hashes are in SOURCE_MANIFEST. A027 excludes controller interleaving; A028 reserve conservation alone does not fund signed entropy drift. These restrictions are preserved. Supplemental campaign/claim/counterexample/seed/mapping excerpts, both threshold and both percolation abstract/scope excerpts, and threshold38pp Proposition8.6 equations75-79 were inspected; no percolation or threshold theorem is needed for the new collision-account proof. Paper text exports decode as cp1252; this is recorded without alleging source corruption. Large registry outputs were truncated; no unseen entry is claimed as reviewed. The requested later campaign deadline governs over older snapshots.

The fresh required wake exited1 and reported OWNER ALERT REQUIRED NOW: attachment document-integrity/render and incident-ledger state-lock timeouts, disclosed before relying on affected notes. No mathematical premise is taken from those notes. The initial empty stage directory and startup limitation were checkpointed in out/STARTUP.md. Sixteen recorded invocations do not mean sixteen substantive local proofs; five older substantive REPORT files were found.

## complete derivation or exact first unsupported line

PROOF.md supplies the derivation. Binary entropy bounds give -4e<=Xi_v<=0 for every private descendant. For K_v=B-Xi_start+Xi_v, collision debit plus expected child K equals parent K EXACTLY, and K_v>=B-4e. Finite physical reach-weight telescoping proves the ALL-policy, ALL-prefix result. A077(12) then gives PROOF(9), retaining both actual full wrapper terminals, both inherited core entropy decrements, old mean reserve and the same source budget.

The actual guarded bent source has H(V)=k and I(V)=k/2+1, so S=e(3k/2+5)>=11e for even k>=4. Keep the first booked4e and any D0; if D0<=S-8e, every subsequent private tree costs at most one further4e total and leaves S-D0-8e. For D0=0 the guaranteed remainder is3e. The source split eH(V)+S=5eI(V) is booked ONCE. Later inherited V entropy decrements and its full terminal entropy telescope to that original entropy allocation; its surplus is not renewed at children. The theorem includes unequal correlated point-padding second splits and arbitrary later private orders.

First unsupported universal line: supply such a genuinely unused donor for arbitrary roots, pay arbitrary W entropy and transfer the same signed source/reference through a shared-coordinate query that changes the two-vertex geometry. A bounded collision account does not certify those core or terminal bills. The full mean-sector continuum estimate is an explicit upstream author-proof dependency pending independent review; the new account identity itself is self-contained.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC is written before the search. Main helper v1 checks all276 ordered controller pairs on n=0,1,2, every partial assignment, shared widths1,2, and eight actual guarded-bent/spike fixtures at k=2,4 and padding m=1,2. No symmetry quotient, automatic dimension increase, GPU or heavy job. k=2 is a boundary fixture and is not included in the k>=4 guaranteed3e claim. The static planned split count was corrected from directed-child count6208 to actual query count3104 BEFORE execution; the mathematical domain was unchanged.

Run python -X utf8 code/check.py from this run: {main['checks']} exact assertions PASS, {main['wrapper_states']} full wrapper states, {main['private_split_instances']} private splits, {main['runtime_seconds']:.3f}s. Integer direct Walsh and a separate FWHT agree; physical edges agree with spectral mean degree. Fraction prime-log identities and outward16-term atanh intervals verify the full spectrum, Xi range, original bank identity, mean-sector inequality and retained source debit. Every source-state and both child spectra are kept. This finite domain is not claimed to exhaust arbitrary dimensions.

Run python -X utf8 code/independent.py: {ind['exact_assertions']} exact assertions PASS over {ind['root_cases']} signed-character wrapper roots, {ind['distinct_Bellman_states']} distinct Bellman states, {ind['runtime_seconds']:.3f}s. This script imports no main helper and minimizes expected terminal Xi over EVERY adaptive stopping policy on its frozen three-bit character domain. It is an independent implementation by the same author, not an independent reviewer. The all-dimensional extension follows from PROOF(1)-(4), not sampling or the finite Bellman cases.

Fresh memok exited1: physical free2.4GB (need4.0), commit free8.2GB (need8.0). Accordingly no Lean/Mathlib job was started. code/account_key.lean records the intended nonnegative-account and exact averaging statements; LEAN_RECEIPT records NOT_RUN_COMPUTE_ADMISSION, not a compilation failure or a Lean proof. Rung: analytic collision-account proof plus exact finite certificates; upstream entropy corollary and independent review retain their explicit statuses. The compute snapshot reported memory pressure and low disk; no other work was killed or throttled. Estimated checker memory80MB and independent memory30MB; actual peaks unmeasured; both bounded pilots finished below55s.

## proof dependencies and changed downstream conclusions

This narrowly extends A078's existing coding/padding handoff and consumes A077's original donor; it opens no new broad universal candidate. A077's one-collision transfer can now retain its first4e debit and fund ALL further private continuations from one additional total4e, subject to D0<=S-8e. Repeatedly allocating4e per query is unnecessary. The source mean-sector statement is {versions!r}, PROOF section6; no independent acceptance is asserted for it. This stage does not change the earlier parity-code/activation-minimum results or the refutation of a universal local collision price.

## one next mathematical action and independent reviewer

Expose ONE actual shared coordinate on the saved guarded bent/point-padding family while carrying the SAME original S, old D0+4e and continuation account, both inherited core bills and both complete wrapper terminals. Derive the new normalization/source transfer rather than assigning another4e at the child. A092 is primary independent reviewer; A028/A094 should challenge source ownership and geometry transfer. These are saved handoff targets; no messages were sent.

## actual persistence receipts or precise save blocker

The four protocol products, PROOF, code, frozen specifications, completed check outputs, source hashes and Lean admission receipt are saved only inside A078. out/PERSISTENCE_RECEIPT.json validates exact protocol key sets, claim hash, byte-identical progress copies, two-line STATUS and file sizes. Independent review, supervisor copying, GitHub persistence and mirror verification remain unobserved. No git, email, brain write, shared-index mutation, trading action, detached job or process termination was performed.

## Universal bridge

C024 history transfer and C019 stopping-tree payment advance from one guarded private collision to EVERY finite adaptive private continuation, funded from the SAME original C5 bent surplus after preserving the first4e debit. One further4e TOTAL allowance leaves at least3e for even k>=4 with no other old debit; both terminal spectra and both inherited core entropy bills remain. The exact unpaid bridge is original-source eligibility and transfer across a shared-coordinate exposure, together with arbitrary terminal/core payment. NEXT attacks that geometry-changing source transfer directly, rather than another local-price sweep or another bounded-ratio class. Full FEI remains OPEN.
'''
write(RUN/'REPORT.md',report)
write(ROOT/'STATUS.md','STATE: Signed collision continuation saved: ALL adaptive private trees paid from SAME original bent donor after booked4e; at least3e remains; exact checks PASS; FEI OPEN, review pending.\nNEXT: A077/A028/A092/A094 review; carry SAME old debit and remaining Xi account through one shared query, with both full terminals and inherited core bills; no renewed donor.\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:f.write(f'\n{stamp} A078 signed continuation: main{main["checks"]} and independent{ind["exact_assertions"]} exact assertions PASS. One further4e pays every private stopping tree from the original guarded-bent donor after booked4e; guaranteed3e remains at k>=4,D0=0. Fresh memok1 blocked Lean. Shared geometry transfer and arbitrary core entropy remain open.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:f.write('\nSigned continuation: for fixed two-vertex shared geometry, Xi in[-4e,0] at EVERY private descendant. K_v=B-Xi_start+Xi_v pays ALL adaptive private collision decrements exactly; B>=4e suffices and leaves>=B-4e. After a booked4e, the original guarded-bent C5 surplus S=e(3k/2+5) pays the ENTIRE further private tree with one additional4e total if D0<=S-8e; at k>=4,D0=0 at least3e remains. Original core entropy budget and surplus are disjoint: eH(V)+S=5eI(V), never renew at children. Both full wrapper terminals and inherited controller decrements stay in the stopped identity. Shared queries alter geometry; arbitrary-source eligibility and arbitrary W entropy remain unpaid.\n')
req=protocol['required_per_run']
assert set(progress)==set(x.split(' (')[0] for x in req['progress_fields'])
assert set(claim)==set(req['claim_fields'])
assert all(x in report for x in req['report_fields'])
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((ROOT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[p for p in RUN.rglob('*') if p.is_file()]
assert all(p.stat().st_size<20_000_000 for p in files)
jwrite(OUT/'PERSISTENCE_RECEIPT.json',{'status':'PASS_LOCAL','timestamp':stamp,'protocol_keys':'exact','progress_delta':'byte_identical','claim_statement_sha256':claim['statement_sha256'],'files':[{ 'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],'remote':'unverified','independent_review':'pending'})
print(json.dumps({'local_persistence':'PASS','main_assertions':main['checks'],'independent_assertions':ind['exact_assertions'],'claim':claim['claim_id'],'sources':versions,'file_count':len(files)}),flush=True)
