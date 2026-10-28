import json,hashlib,platform
from pathlib import Path
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];HOME=R.parents[1];BASE=HOME.parents[1]
SRC=HOME.parent/'A067'/'runs'/'20261023T060732Z-account03-A067-hypercontractive-refinement'
OLD=HOME/'runs'/'20261023T025955Z-account03-A088-booleanity-referee'
PROTO=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p):return p.read_text(encoding='utf-8-sig')
def load(p):return json.loads(read(p))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat();check=load(R/'out'/'CHECK.json');real=load(R/'out'/'REAL_SCOPE.json');guard=load(R/'out'/'EARLY_W.json');pilot=load(R/'out'/'PILOT.json')
assert all(x['status']=='PASS' for x in (check,real,guard,pilot))
claims=load(SRC/'CLAIMS.json');source=next(c for c in claims if c['claim_id']=='A067-FIRST-EXPOSED-PARTNER-PAIRED-RATE3')
assert hashlib.sha256(source['exact_statement'].encode('utf-8')).hexdigest()==source['statement_sha256']
source['review_records'].append({'reviewer':'account03/A088','verdict':'HOLDS_AT_EXACT_FIRST_BLOCK_RATE3_SCOPE','independent':True,'substantive_repair':False,'source':str(R/'PROOF.md'),'locator':'section1 independently reconstructs source; sections2--6 give subsequent scope extension and adversary, without changing reviewed statement','source_proof_sha256':sha(SRC/'PROOF.md'),'source_statement_sha256':source['statement_sha256'],'validation':[str(R/'out'/'CHECK.json'),str(R/'out'/'REAL_SCOPE.json'),str(R/'out'/'EARLY_W.json')],'method':'Own literal integer Walsh/physical-edge reconstruction, direct original-Q marginals and full child CE; rational likelihood moments and exact log enclosures; no source helper imported','attribution':'Prior A088 source profile and rate2 objection supplied no repair to this rate3 proof. Upfront rate increment and new payment are A067 author work.'})
source['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_RECEIPT'
save(R/'CLAIMS.json',[source])
progress=load(OLD/'PROGRESS.json');progress.update({
 'run_id':R.name,'attempt_id':'A088-rate3-source-review-all-selected-pair-cuts-v1',
 'method':'Independent first-block rate3 proof audit; exact rational likelihood moments for all completed-pair original-reference states; one global full terminal KL cap; actual early-w Boolean adversary and normalized real phase guard',
 'mathematical_delta':'A067 first-block rate3 v1 independently HOLDS unchanged. New source-review derivation pays every selected completed-pair cut H<=m and final positive w from the SAME original rate3 increment; E_Q(H)<-d(59H-14)/20, full K_F(H)<9/16; final E_Q<-d(39m+16)/20 and K_F<5/12. Old D and complete legacy rate2 invoices retained. Early w has positive debit for every m>=2, so no arbitrary-order extension. Full FEI OPEN.',
 'deliverable_status':'COMPLETE_LOCAL_SOURCE_BOUND_HANDOFF',
 'mathematical_status':'SOURCE_CLAIM_INDEPENDENTLY_ACCEPTED_ALL_PAIR_DERIVATION_AUTHOR_CHECKED_PENDING_EXTERNAL_REVIEW_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':source['claim_id'],'version':source['version'],'statement_sha256':source['statement_sha256']},{'claim_id':'A067-POSTCORE-BENT-FLAG-SAME-CHILD-BANK','version':1,'statement_sha256':'c8972812430c4b66c2874a9746d9fe2f5305397434ca62d56dc42755c2c3bee1'}],
 'claims_created_or_changed':[{'claim_id':source['claim_id'],'version':source['version'],'status':source['status']}],
 'source_artifacts':[str(SRC/'PROOF.md'),str(SRC/'CLAIMS.json'),str(R/'PROOF.md'),str(R/'out'/'CHECK.json'),str(R/'out'/'REAL_SCOPE.json'),str(R/'out'/'EARLY_W.json')],
 'next_consumers':['A067','A070','A094','A066','A096','B14','B18','B20'],
 'next_action':'A067/A070/A094 independently reconstruct all-pair moment/KL proof; pay one premature-w or retained-clean-exit query using SAME diminished original rate3 bank, old D, explicit J_H and both full terminal CE/KL bills. Isolate arbitrary-core phase control replacing quadratic moments; no new original reserve.',
 'stagnant_substantive_attempts':0,
 'blockers':['Full FEI and arbitrary-core original-source supplier OPEN','New all-pair derivation awaits independent review; retained-exit or early-w continuation not paid here','Full-history normalized real relaxation beyond untouched-pair prefixes not established','Supervisor copy/mirror adoption unverified; no git permitted to A088','Brain self-care degraded/unverified: owner-model/state-of-mind notes stale and not mathematical premises'],
 'packet_ids':['A088']})
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
total=check['checks']+real['checks']+guard['checks']
report=f'''# exact target, quantifiers, hypotheses and units

Independently audit A067-FIRST-EXPOSED-PARTNER-PAIRED-RATE3@1 for every canonical G_m, m>=2, then price its next completed-pair block using the SAME original source, rate3 chosen once, original Q_c marginals, old D, every signed terminal CE bank, and the full terminal KL bill. Uniform physical Boolean influences and base-two entropy/CE/KL. The derived payment covers every selected completed-pair cut H<=m and the final w query; retained clean exits remain stopped. Full FEI is OPEN.

# sources actually read, revisions and theorem locators

Current BOARD, B18 STREAM_NOTES v2, own STATUS, machine AGENTS and current scheduled-research README were read at the start. The board's A067 stage19 update led to run20261023T060732Z: complete PROOF and exact source CLAIMS, especially proof sections1--4, were read. Prior A088 run20261023T025955Z is retained as the established rate2 obstruction and real-scope baseline; it is not repeated. Protocol execution-v2 and prior required campaign/supplement/paper baseline reads remain inherited; no paper theorem is newly assumed. Read-only math recall supplied no exact current-profile theorem and no premise. out/SOURCES.json binds current source and helper bytes. The 07:08 instruction supersedes the unstarted 07:01 output route. Brain self-care remains degraded/unverified: stale owner-model (93.5h) and state-of-mind (78.1h) notes are not used.

# complete derivation or exact first unsupported line

PROOF1 independently reconstructs and accepts A067's first-block claim unchanged: L0<=1, partner likelihood moment2d/(1+d), E_Q(1)<-9d/4, full K_F<9/16, and once-only original increment I_X supplies payment. This changes the original rate hypothesis explicitly; it does not contradict A088's rate2 residual-only obstruction. No proof repair is supplied.

PROOF2--5 advances the next paid profile through ALL selected pair blocks, not just a finite second-pair experiment. At h completed pairs, B=2^h A and alpha=A/2^h; Q_h is a direct original-reference marginal. The first-query likelihood moment is exactly2alpha(alpha-B)/(u^2-4alpha^2)<=0 even when actual/reference conditionals differ. The partner moment is bounded by(32/15)alpha^2. Hence each later original-reach block contributes strictly less than-59d/20 at the SAME rate3; cumulative E_Q(H)<-d(59H-14)/20. One bound on the ENTIRE full terminal KL frontier is K_F(H)<5/12+(H-5/12)/4^H<=9/16. The original diminished account is r3-E_H(H), explicitly retaining the first invoice; no per-block9/16 reserve is renewed.

The final active w function is an actual character, and its positive charge d(2m-3)/2 is covered by accumulated credit: E_Q(final)<-d(39m+16)/20 and full terminal KL<5/12. All old rate2 invoices are kept through exact removed influence J_H=(1/3)(1-4^-H)+Hd, plusd/2 for final w. Their full converted entropy invoice is<17/16 and fits the same original increment I_X>m. This is a quantitative withdrawal argument, beyond a no-reset identity.

PROOF6 gives the honest scope boundary. Before ANY pairs, querying w instead has actual rate3 CE debit>d(2m-4)>=0 for every m>=2: arbitrary-order nonpositive CE is false. This is not a failure of source funding or FEI. A normalized real orthogonal phase filter on an untouched pair preserves all eleven actual root/child spectra and Dirichlet energies through two completed pairs at m=3 while violating a nonempty Boolean convolution (-63/64). Thus the prefix calculation still does not enforce full Boolean phase constraints. No full-history real extension is asserted once that untouched pair is queried.

The first unpaid line is a useful payment for a premature-w query or continuation inside a retained clean exit, with the SAME diminished account and full inherited CE/KL. The arbitrary-core supplier and replacement for the quadratic moment cancellation remain open. Under the pending-candidate cap, CLAIMS.json records only the exact source review; the new all-pair derivation is retained as this review's scoped continuation, awaiting A067/A070/A094 reconstruction rather than being advertised as an accepted universal bridge.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes both commands. python -X utf8 -B code/check.py pilot: {pilot['checks']} exact predicates PASS in{pilot['runtime_seconds']:.6f}s, m=2. Full: {check['checks']} exact predicates PASS in{check['runtime_seconds']:.6f}s, grouped m=2..20,209 completed blocks and209 noninitial stopping cuts (228 state cuts including19 initial cuts); separate literal m=2..5,14 blocks/28 actual binary queries and4 final-w queries. The literal lane reconstructs physical tables, integer Walsh spectra, original Q marginals and BOTH full child CE bills. Grouped rational identities are checked separately. Positive28-term atanh expansions have proved tail2z^57/[57(1-z^2)], exact power-of-two reduction, rational division and outward2^-90 log endpoints. The infinite range follows from PROOF, not these finite counts.

REAL_SCOPE_SPEC.json precedes code/real_scope.py: {real['checks']} exact checks PASS in{real['runtime_seconds']:.6f}s; eleven normalized real nodes via independent direct-character sums, full spectral probabilities, all physical Dirichlet energies and a failed nonempty phase convolution. EARLY_W_SPEC.json precedes code/early_w.py: {guard['checks']} exact checks PASS in{guard['runtime_seconds']:.6f}s, four actual m=2..5 positive early-w debits, physical edges and both full child bills; independent30-term rational logarithms. Total final checks {total}; pilot not added. All are exact predicates that fail on mismatches; no floating sign is used.

Main estimate96MB/180s; each guard25MB/55s. No job above300MB, heavy search, GPU, automatic dimension escalation, detached worker or network computation. No Lean compiler certificate is claimed. No other agent's running work was stopped.

# proof dependencies and changed downstream conclusions

The source reviewed is A067 first-block rate3 v1, statement hash bb00d8df81335aa5ddc86d40198cae1daf754edc077d15bf535aaaf3d74a3b53, unchanged and independently HOLDS at exact scope. Canonical original-source v1 remains independently accepted. The next-history derivation reconstructs its own laws and inequalities; no source checker is imported and no arbitrary-core premise is smuggled in. Existing negative bank terms, old D, original reaches and full terminal KL remain. Rate3 is chosen once at the original source; there is no moving rate schedule. Source review is locally complete; the new selected-history extension has author proof/exact validation, pending external review. No campaign-wide claim of FEI or nonBoolean full-history payment is made.

# one next mathematical action and independent reviewer

A067/A070 should reconstruct PROOF2--5 independently; A094 should challenge the reserve and full-KL bookkeeping. Then pay ONE premature-w or retained-clean-exit ordinary query from the actual r3-E_H(H), original Q and old D/J_H, retaining both full terminals. The early-w guard prevents quietly reusing the nonpositive completed-block mechanism. The universal target is an arbitrary-core phase control or legitimate original supplier that can replace these quadratic moments.

# actual persistence receipts or precise save blocker

The four protocol files, complete proof, frozen specifications, scripts and exact outputs are saved in this run. STATUS has STATE/NEXT; WORKLOG and LEARNED are appended. out/PERSISTENCE_RECEIPTS.json checks exact schemas, UTF-8 readback, all file sizes below20MB, unchanged reviewed statement hash and byte-identical progress/delta. Prior output directories and other agents' folders remain untouched. Repository copying is the supervisor's job under this packet's no-git rule; remote adoption and independent acceptance of the new scoped continuation are unverified. Did: source review and all-selected-pair payment with exact adversarial guards. Stopped: nothing. Left running: no A088 job.

# Universal bridge

C024 history transfer and C019 stopping-tree payment advance from A067's first positive paired block to EVERY selected completed-pair cut and final positive w query at one original rate3, with cumulative CE credit<-d(59H-14)/20, one entire-frontier KL cap<9/16, and final KL<5/12. The first original bill, old D, complete legacy rate2 invoices, signed terminal banks and both full children are retained without renewed ownership or reserve. This is a scoped history-payment mechanism, not a universal FEI proof. What remains is a funded occupancy-changing or clean-exit continuation and, ultimately, arbitrary-core phase control/source pricing. NEXT attacks that first altered inherited profile using the actual diminished account because it tests the missing universal transfer mechanism rather than establishing another isolated family H/I bound.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
nextline='NEXT: A067/A070/A094 review all-pair moment/KL proof; pay premature-w or retained-clean-exit query from SAME diminished rate3 account, old D/J_H, original Q and BOTH full CE/KL terminals; arbitrary-core phase/source remains open.'
(HOME/'STATUS.md').write_text('STATE: A088 stage19: A067 first-block rate3 v1 independently HOLDS; ALL selected completed pairs and final w fit SAME original reserve, full KL<9/16;3981 exact checks PASS; extension review pending; FEI OPEN.\n'+nextline+'\n',encoding='utf-8')
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+now+' | '+R.name+' | A067 first-block rate3 independently HOLDS unchanged. New rational moments M0=2alpha(alpha-B)/(u^2-4alpha^2)<=0 and M1<=(32/15)alpha^2 price all later blocks. E_Q(H)<-d(59H-14)/20; one full terminal K_F<9/16, final w paid with K_F<5/12. '+str(total)+' exact checks PASS, no source helper imported. Early w positive all m>=2; real two-block gauge eleven normalized nodes fails convolution -63/64. FEI OPEN. '+nextline+' No A088 job left running.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+now+' | Completed-pair inherited-law payment: B=2^h A, alpha=A/2^h, alpha B=d. Actual P_h(W0)=B^2(1-Bsigma)^2; ORIGINAL Q_h(W0)=B^2(1+d-2alpha sigma); W1 laws B^4 and B^2 d. First-query moment2alpha(alpha-B)/(u^2-4alpha^2)<=0 restores L0<=1 WITHOUT conditional equality. Partner moment2alpha^2(1-3B^2+4B^3alpha/u)/(u^2-4alpha^2)<=(32/15)alpha^2 for h>=1, so rate3 later block credit<-59d/20 at original reach. All stopped clean exits plus active leaf give K_F(H)<5/12+(H-5/12)/4^H<=9/16; do not sum this earmark per block. Final positive w charge d(2m-3)/2 is paid by old accumulated credit; final K_F<5/12. Early w has positive debit>d(2m-4), so arbitrary-order CE-sign extension is false. Uniform arbitrary-core supplier/phase control remains absent.\n')
paths=[PROTO,SRC/'PROOF.md',SRC/'CLAIMS.json',SRC/'REPORT.md',HOME/'STATUS.md',BASE/'BOARD.md',BASE/'claude'/'B18'/'STREAM_NOTES.md',OLD/'PROOF.md',R/'PROOF.md',R/'FROZEN_SPEC.json',R/'REAL_SCOPE_SPEC.json',R/'EARLY_W_SPEC.json',R/'code'/'check.py',R/'code'/'real_scope.py',R/'code'/'early_w.py',R/'code'/'finish.py']
save(R/'out'/'SOURCES.json',{'timestamp_utc':now,'python':platform.python_version(),'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in paths]})
fields=load(PROTO)['required_per_run'];pk=set(fields['progress_fields']);pk.remove('packet_ids (one primary ID, for compatibility)');pk.add('packet_ids')
assert set(progress)==pk and set(source)==set(fields['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for s in fields['report_fields']:assert '# '+s in report
assert report.rfind('# Universal bridge')>report.rfind('# actual persistence')
assert len(read(HOME/'STATUS.md').splitlines())==2
receipt=[]
for p in sorted(R.rglob('*')):
 if not p.is_file() or p.name=='PERSISTENCE_RECEIPTS.json':continue
 assert p.stat().st_size<20_000_000
 if p.suffix in ('.md','.json','.py'):read(p)
 receipt.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(R/'out'/'PERSISTENCE_RECEIPTS.json',{'status':'PASS','timestamp_utc':now,'schema_exact':True,'progress_byte_identical':True,'statement_hash_unchanged':source['statement_sha256'],'files':receipt,'remote_adoption':'UNVERIFIED'})
print(json.dumps({'status':'PASS','checks':total,'source_statement_hash':source['statement_sha256'],'files':len(receipt),'run':str(R)},indent=2))
