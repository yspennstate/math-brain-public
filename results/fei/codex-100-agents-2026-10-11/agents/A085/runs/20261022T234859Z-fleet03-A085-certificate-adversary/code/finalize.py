from pathlib import Path
import json,hashlib,datetime,subprocess,sys

R=Path(__file__).resolve().parents[1];OWN=R.parents[1]
HOME=Path(r'~');TEAM=HOME/'brain_workers/FEI100_20261011'
def get(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def put(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
protocol_path=HOME/'mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'
protocol=get(protocol_path);fields=protocol['required_per_run']
base=TEAM/'agents/A099/runs/20261022T231100Z-fleet03-A099-candidate-assembly'
dirs={
 'floor':TEAM/'agents/A097/runs/20261014T050248Z-fleet05-A097-cross-route-transfer',
 'active':TEAM/'agents/A096/runs/20261021T210221Z-fleet03-A096-live-gap-ledger',
 'control':TEAM/'agents/A097/runs/20261021T232544Z-fleet03-A097-cross-route-transfer',
 'dummy':TEAM/'agents/A073/runs/20261022T211534Z-fleet03-A073-certified-logarithms'}
ids={'floor':'A097-NEGATIVE-CELL-FLOOR-SOURCE-BANK','active':'A096-CANONICAL-ACTIVE-RESET-SAME-ANCESTOR','control':'A097-MIXED-ACTIVE-CONTROL-RESET-SAME-ANCESTOR','dummy':'A073-DUMMY-DATA-RESET-SAME-ANCESTOR'}
source_claims={k:next(c for c in get(d/'CLAIMS.json') if c['claim_id']==ids[k]) for k,d in dirs.items()}
prior=OWN/'runs/20261021T174013Z-fleet03-A085-certificate-adversary'

# Package the already pinned own arithmetic dependency; then verify the final portable source.
original=prior/'code/check_reset.py';local=R/'code/log_intervals.py';local.write_bytes(original.read_bytes())
checker=R/'code/check_exit.py';oldtext=checker.read_text(encoding='utf-8')
oldline="OLD=RUN.parents[1]/'runs/20261021T174013Z-fleet03-A085-certificate-adversary/code/check_reset.py'"
newtext=oldtext.replace(oldline,"OLD=Path(__file__).with_name('log_intervals.py')")
assert newtext!=oldtext or "OLD=Path(__file__).with_name('log_intervals.py')" in oldtext
if newtext!=oldtext:
 (R/'out/EXACT_EXIT_DISCOVERY.json').write_bytes((R/'out/EXACT_EXIT.json').read_bytes())
 checker.write_text(newtext,encoding='utf-8')
 put(R/'out/PACKAGING_AMENDMENT.json',{'reason':'Bundle byte-identical own logarithm/Fraction primitives so the saved run reproduces alone','old_checker_sha256':hashlib.sha256(oldtext.encode('utf-8')).hexdigest(),'new_checker_sha256':sha(checker),'helper_sha256':sha(local),'domain_changed':False,'mathematics_changed':False,'requires_final_source_recheck':True})
 z=subprocess.run([sys.executable,'-B','-X','utf8',str(checker)],capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
 put(R/'out/FINAL_SOURCE_RECHECK.json',{'exit_code':z.returncode,'stdout':z.stdout,'stderr':z.stderr})
 assert z.returncode==0,z.stderr
main=get(R/'out/EXACT_EXIT.json');pilot=get(R/'out/PILOT.json');lean=get(R/'out/LEAN_RECEIPT.json')
assert main['status']=='PASS' and main['transactions']==162 and main['roots']==27
assert main['helper_sha256']==sha(checker) and main['log_helper_sha256']==sha(local)
assert main['positive_after_active_prefix']>0
witness=get(R/'out/POSITIVE_RESET.json');assert witness['positive_signed_reset_certified'] and witness['prefix_active']>0

paths=[protocol_path,HOME/'AGENTS.md',TEAM/'BOARD.md',TEAM/'claude/B17/STREAM_NOTES.md',base/'REPORT.md',base/'CLAIMS.json',base/'STAGE7_ADDITIONS.tex',prior/'out/SOURCE_RECEIPTS.json',prior/'CLAIMS.json',TEAM/'agents/A092/runs/20261021T232000Z-fleet03-A092-counterexample-referee/PROOF.md',TEAM/'agents/A092/runs/20261021T232000Z-fleet03-A092-counterexample-referee/CLAIMS.json']
for d in dirs.values():
 paths.extend(d/n for n in ['CLAIMS.json','DERIVATION.md'] if (d/n).exists())
pins=[]
for p in paths:
 raw=p.read_bytes();raw.decode('utf-8-sig')
 pins.append({'path':str(p),'sha256':sha(p),'bytes':len(raw),'encoding':'utf-8-sig'})
put(R/'out/SOURCE_RECEIPTS.json',{'saved_at':now,'sources':pins,'baseline_intake':'Required campaign/supplement/paper intake is retained in the prior A085 source receipts; it is not newly re-audited or used as a theorem premise. Critical new proofs are the exact sources listed here.','prior_acceptance':'A092 independently accepted A085-ABSOLUTE-TV-RESET-OBSTRUCTION@1 unchanged; new stage does not rerun that family.'})

source_exit=next(c for c in get(base/'CLAIMS.json') if c['claim_id']=='A099-PRESCRIBED-EXIT-SOURCE-RESET')
review=json.loads(json.dumps(source_exit));review['review_records'].append({'reviewer':'A085','timestamp':now,'verdict':'HOLDS_AT_EXIT_CONVERSION_AND_CONDITIONAL_PROPAGATION_SCOPE','source':str(R/'PROOF.md'),'scope':'Original unqueried-exit source conversion/pure-source continuation and its propagation, relative to exact named upstream premises; not an integrated FEI-chain audit','source_statement_sha256':source_exit['statement_sha256'],'contributed_repair':False,'new_postquery_policy_is_separate':True})
review['status']='ONE_A085_SCOPED_REVIEW_UPSTREAM_PREMISES_RETAINED_INTEGRATED_AUDIT_OPEN'
statement=('For every supplied negative-cell source F=1-2A_a+2A_(a+b+r), a>=1,b>=0,r>=1,b+r>=2, with the normalized finite-cost original source c_raw<=C0 I(g), C0>=0, and canonical live-branch active/dummy/eligible-control histories, a retained non-active exit may execute one arbitrary unqueried active/dummy/control coordinate BEFORE its reset. Keep the outcome-one child on its complete actual inherited marginal. Reset only outcome zero to the source reference obtained by marginalizing the creating-parent supplied source over exactly the data coordinates physically removed at exit creation and this query, then calibrating ONCE to that final actual source vacuum; put point spectral mass on irrelevant controls, with explicit point law for a constant child. The complete exit erasure-plus-both-terminal bill is <c+11e/2, and its creating-parent transaction is <W+19e/4, W=c+10e(a+b+r), e=2^(1-a-b-r). Hence any collection of such exits, with all earlier debits and other complete terminals retained, remains paid by the SAME original (2C0+10)I(F_root)-12e_root. If all non-active exits use this policy the reserve is at least61e_root/4. Structural source retains rate18. Arbitrary finite subsequent no-reset continuations and untouched independent terminal costs are retained. This is a direct-final-calibration policy, not an assertion about a different intermediate-calibration target, repeated prescribed resets, arbitrary incoming profiles, extra channels/codes or universal initial reference pricing.')
hyp=['Finite uniform Boolean cube, bits and physical influence','Exact supplied negative-cell source and finite normalized source cost; source vacuum calibrated','Eligible creating non-active query (dummy b>=1 or control r>=2); current d>=2','No prior query or reset in the selected exit before this one inside query; all prior main debits retained','Only the stated direct original-source marginal followed by one FINAL calibration; complementary full inherited terminal unchanged']
claim={'claim_id':'A085-POSTQUERY-EXIT-DIRECT-SOURCE-RESET','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(json.dumps({'exact_statement':statement,'hypotheses':hyp},sort_keys=True,ensure_ascii=False).encode('utf-8')).hexdigest(),'contributors':['A085'],'proof_source':{'path':str(R/'PROOF.md'),'locators':'Sections1--4','checker':str(checker),'certificate':str(R/'out/EXACT_EXIT.json'),'positive_transaction':str(R/'out/POSITIVE_RESET.json')},'proof_dependencies':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256'],'source':str(dirs[k]/'CLAIMS.json'),'scope':'Exact supplied-source/canonical-history scope only'} for k,c in source_claims.items()],'review_records':[],'status':'ANALYTIC_AUTHOR_PROOF_EXACT_VALIDATION_INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A099','A096','A097','A073','A094','A050','B17','B20']}
assert set(claim)==set(review)==set(fields['claim_fields'])
put(R/'CLAIMS.json',[review,claim])
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B17','packet_id':'A085','gap_id':'C024-C019-INHERITED-REFERENCE-SAME-OWNER','attempt_id':'A085-stage7-postquery-exit-direct-source','method':'Analytic likelihood-floor and vacuum-mixture bounds; actual signed Boolean and complete-reference reconstruction with exact log expressions and outward dyadic signs','mathematical_delta':'A099 exit-source conversion scoped HOLDS; one actual A/D/C query INSIDE an exit before direct source reset paid at same original rate18 structurally, local< W+19e/4. Full FEI OPEN.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_AUDIT_HOLDS_NEW_THEOREM_REVIEW_PENDING_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256']} for c in source_claims.values()]+[{'claim_id':source_exit['claim_id'],'version':source_exit['version'],'statement_sha256':source_exit['statement_sha256']}],'claims_created_or_changed':[{'claim_id':review['claim_id'],'version':1,'change':'Scoped A085 review in local record only'},{'claim_id':claim['claim_id'],'version':1,'change':'New postquery direct-source policy author proof'}],'source_artifacts':['PROOF.md','TARGET.md','out/FROZEN_SPEC.json','code/check_exit.py','code/log_intervals.py','out/EXACT_EXIT.json','out/POSITIVE_RESET.json','out/SOURCE_RECEIPTS.json','out/LEAN_RECEIPT.json'],'next_consumers':claim['next_consumers'],'next_action':'A099/A094 independently audit the postquery direct-final-calibration theorem; A050/A094 supply a non-point correlation-preserving source with a paid analogue of the vacuum/singleton likelihood floor and test one actual reset against SAME U+r with both old terminals.','stagnant_substantive_attempts':0,'blockers':['Independent review of new extension pending','Generic non-point supplied source and absolute initial influence price remain open','Repeated prescribed reset is not covered','Core Lean held by fresh failed memory admission; no formal certification'],'packet_ids':['A085']}
expected={s.split(' (')[0] for s in fields['progress_fields']};assert set(progress)==expected
put(R/'PROGRESS.json',progress);put(R/'PACKET_DELTA.json',progress)

report=f'''# A085: an actual query inside an exit before its prescribed reset

## exact target, quantifiers, hypotheses and units

Independently scope-check A099-PRESCRIBED-EXIT-SOURCE-RESET@1, then extend its saved NEXT to ONE actual active/dummy/control query already executed inside a retained exit. All a>=1,b>=0,r>=1,d=b+r>=2; supplied normalized finite-cost source; canonical live histories. Keep the SAME original quota, every old live/exit erasure debit and both complete terminal CE costs. Bits and ordinary uniform physical influence. The direct target marginalizes the creating-parent original source over removed data coordinates, then calibrates ONCE at the final child. It is explicitly different from intermediate exit-root calibration. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Current BOARD2026-10-22 23:50 UTC, own STATUS and B17 leadv2 were read at stage start. The old lead census audits are completed prior work; they are not rerun. The board and A09220261021T232000Z PROOF/CLAIMS supply unchanged independent acceptance of A085's previous full-support TV obstruction. Current critical sources are A09920261022T231100Z entire STAGE7_ADDITIONS, CLAIMS and REPORT; A09620261021T210221Z DERIVATION1--4; A09720261021T232544Z original mixed-reset derivation; A07320261022T211534Z source derivation; and the exact original A097 supplied floor/source claim. SOURCE_RECEIPTS pins bytes and exact original claim versions. Existing baseline protocol/campaign/supplement/four-paper intake remains in prior A085 source receipts, not a new blanket theorem audit. Current user deadline23 October14:49UTC supersedes older static dates. No other agent or campaign file was edited.

## complete derivation or exact first unsupported line

PROOF Sections1--4 derive gamma=(1-h)/(1+h/2), h=e/s<=1/2, and the actual complete exit likelihood floor. On occupied active labels Qoff>=gamma R, while Qoff(empty)>=mu^2; reference-only atoms remain. For an active query, its unchanged constant sibling's excess over the source comparison is <=(1-mu^2)(-log2 gamma)<11e. Concavity of log handles the whole vacuum/singleton mixture. Source disintegration, additional irrelevant-data marginalization and ONE final calibration pay the fresh other child. A1 uses the explicit constant point law, avoiding0/0. For an inactive query, actual erasure is zero and both children remain nonconstant; old-reference marginalization only lowers the inherited cost. In either case the whole exit-query bill is <c+11e/2 and the creating-parent substitution <W+19e/4. Thus the previous8e allowance pays it with no renewal. All-postquery exits leave >=61e_root/4; mixed retained exits still leave>=12e_root. A099 immediate exit-root conversions leave18e_root under a DIFFERENT policy, not a corrected estimate.

A099's original added exit conversion and conditional global propagation HOLD relative to their exact named upstream local/source premises, without repair. This is not acceptance of its entire integrated FEI candidate. New policy is a separate author proof, pending independent review. First unsupported universal line: a non-point supplied source with a suitably paid signed likelihood floor (or another prescribed reset after this transaction's actual debit), and an absolute influence-priced initial reference for arbitrary Boolean functions. Channel/code bills are outside this erasure-plus-CE ledger.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec precedes evaluation:27 root/reference pairs,162 transactions, dimensions<=6; pilot3 roots/30 transactions. Parameters a1,2,3;b0,1;r1,2;d>=2, matching/ascending/spiked supplied references, every proper active prefix length, each available non-active exit and one least-labelled coordinate of every available inside-query type. No reference-sensitive label symmetry is claimed. Analytic proof supplies other labels and all-parameter quantifiers.

Commands from this run: python -B -X utf8 code/check_exit.py --pilot; python -B -X utf8 code/check_exit.py; python -B -X utf8 code/finalize.py. Initial pilot failed on a tuple/exact-expression accumulator mismatch and supplies no certificate; initialization was repaired without domain change. Successful pilot:{pilot['assertions']} assertions/{pilot['transactions']} transactions PASS,{pilot['mathematical_seconds']:.6f}s. Final portable-source check:{main['assertions']} exact assertions/{main['transactions']} transactions PASS,{main['mathematical_seconds']:.6f}s. Pilot and discovery repetitions are not added to the final count. Packaging copies the byte-identical own log helper into code and changes only its import path; amendment, prior output and final-source rerun are saved.

Independent literal character sums and integer FWHT agree on every actual law; physical edges verify influence. Fraction arithmetic checks complete normalization, reference-only mass, likelihood floors, positive normalizers, final point boundary, old debits, both terminals, local bounds and original root quota. Exact rational-log expressions cancel algebraically BEFORE100-bit outward/40-term positive-atanh interval evaluation; zero signs are not inferred from interval overlap. There are{main['positive_resets']} certified positive signed resets,{main['positive_after_active_prefix']} after an earlier active debit. POSITIVE_RESET stores one full rational transaction at root{witness['root']}, prefix{witness['prefix_active']}, exit{witness['exit']}, inside query{witness['inside_query']}, with both incoming and final reference laws.

Fresh memok exited1: physical free3.6GB versus4GB required, commit free18.5GB versus8GB required. Lean was NOT launched; its saved integer reserve-step source is unverified. Mathematical rung is analytic proof plus exact finite certificates, pending independent review. Mathematical helper estimate100MB, observed peak unmeasured, frozen55s cap; no heavy search, GPU, background research process or automatic n increase. No process was stopped for resources.

## proof dependencies and changed downstream conclusions

Exact supplied floor/source-bank, canonical active reset and mixed/dummy source versions are pinned in CLAIMS. Original A099 statement/hypotheses/hash are preserved in its local scoped review; shared status is untouched. A099/A096/A097 may consume a concrete post-query exit transaction without a renewed source bank or omitted sibling. The source marginal must precede ONE final calibration: replacing it by a twice-calibrated target is not covered by the proof. The prior TV obstruction is consumed as independently accepted, not re-tested. Universal FEI constant improvement:zero. General source/reference pricing and repeated arbitrary-profile resets remain unpaid.

## one next mathematical action and independent reviewer

A099/A094 should independently reconstruct the new direct-source policy, especially the creating-dummy/inside-active order and a1 denominator guard. A050/A094 should then supply one correlation-preserving unequal-amplitude non-point source with an influence-paid analogue of the vacuum/singleton floor and price an actual post-query reset against SAME U+r with both full terminals. This removes the point-source hypothesis responsible for the cheap comparison, rather than proving another isolated class entropy bound.

## actual persistence receipts or precise save blocker

All four exact-schema protocol files, PROOF, frozen spec, portable code, exact outputs, positive rational witness, source pins, packaging/failure records and Lean admission noncertificate are saved locally. PERSISTENCE_RECEIPTS verifies exact field sets, hashes and20MB ceilings. STATUS has exactly two lines; WORKLOG and LEARNED are current. No git, mail, intentional brain write, trading access or other-agent mutation occurred. Required wake reported stale owner-model/state-of-mind notes (86h/71h); user was alerted and neither is a mathematical premise. Brain self-care remains degraded/unverified. Supervisor copying, canonical adoption, independent review and remote mirror verification remain unverified. No stage job is intentionally detached.

## Universal bridge

C019 stopping-tree payment and C024 history transfer advance by ONE actual active/dummy/control query inside a retained exit BEFORE its prescribed direct-source reset, with every old debit and both complete terminals retained. The new local coefficient19/4 fits the old8 allowance at unchanged original rate2C0+10 (18 structurally), and all-postquery exits retain>=61e_root/4 while mixed policies retain>=12e_root. Universal-constant improvement is zero: a paid generic non-point likelihood floor and an influence-priced initial reference remain open. NEXT targets that precise non-point replacement with the SAME remaining bank because the point-source vacuum/singleton comparison, not additional finite dimensions or probability precision, is the remaining restrictive hypothesis.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(OWN/'STATUS.md').write_text('STATE: A085 stage7 complete: post-query exit direct-source reset paid SAME rate18; local< W+19e/4, all-converted reserve>=61e_root/4;23978 exact checks; A099 exit conversion scoped HOLDS; new theorem review pending, FEI OPEN.\nNEXT: A099/A094 review direct-final calibration/a1 guard; A050/A094 supply non-point likelihood floor and pay one actual reset against SAME unused bank with all old debits and both terminals.\n',encoding='utf-8')
tag='2026-10-22T234859Z stage7 fleet03'
for name,text in [('WORKLOG.md',f'\n## {tag}\nConsumed A092 unchanged acceptance of prior TV obstruction. A099 exit conversion scoped HOLDS. Proved direct-source final-calibration reset after one actual A/D/C query inside an exit; full ledger<c+11e/2 locally, creating parent<W+19e/4, SAME original rate18. Final{main["assertions"]} exact assertions/162 transactions PASS;21 positive resets,9 after old active debit. One pilot initializer failure repaired without domain change; final portable source rechecked. Fresh memory admission held Lean; no compiler or detached job launched. Artifacts in {R.name}; universal generic source pricing OPEN.\n'),('LEARNED.md',f'\n## {tag}: query-before-reset exit payment\nFor a>=1,d=b+r>=2 supplied negative-cell source, h=e/s<=1/2 and gamma=(1-h)/(1+h/2), full inherited non-active exit obeys Qoff(T_active)>=gamma R(T_active),Qoff(empty)>=mu², with all reference-only mass retained. After ONE actual inside A/D/C query, reset only zero child to ORIGINAL-source direct marginal followed by ONE FINAL calibration; keep sibling inherited. Active constant sibling excess<= (1-mu²)(-log2 gamma)<11e by log concavity and Rj<=1-mu²; a1 uses explicit point. Whole exit cost<c+11e/2; creating parent<W+19e/4, fitting old8e. All such exits leave>=61e_root/4 at same original rate18; old immediate-conversion18e reserve refers to a different policy. Dummy creation/active query target must marginalize BEFORE calibrating: a twice-calibrated target is a different reference. No generic non-point or second-prescribed-reset claim follows.\n')]:
 p=OWN/name;old=p.read_text(encoding='utf-8') if p.exists() else ''
 if tag not in old:p.write_text(old+text,encoding='utf-8')

assert get(R/'PACKET_DELTA.json')==get(R/'PROGRESS.json')
assert len((OWN/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all(set(c)==set(fields['claim_fields']) for c in get(R/'CLAIMS.json'))
assert set(get(R/'PROGRESS.json'))==expected
assert (R/'REPORT.md').read_text(encoding='utf-8').rstrip().endswith('remaining restrictive hypothesis.')
artifacts=[]
for p in R.rglob('*'):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  assert p.stat().st_size<20*1024*1024
  artifacts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
put(R/'out/PERSISTENCE_RECEIPTS.json',{'status':'PASS','saved_at':now,'protocol_exact_fields':True,'no_file_above_20MB':True,'final_source_hash_matches_executed_checker':True,'source_original_statement_unchanged':review['exact_statement']==source_exit['exact_statement'] and review['hypotheses']==source_exit['hypotheses'] and review['statement_sha256']==source_exit['statement_sha256'],'artifacts':artifacts,'rolling':[{'path':str(OWN/x),'sha256':sha(OWN/x)} for x in ['STATUS.md','WORKLOG.md','LEARNED.md']],'independent_new_review':'PENDING','canonical_remote_save':'UNVERIFIED'})
print(json.dumps({'status':'PASS','assertions':main['assertions'],'transactions':main['transactions'],'positive_after_prior_active_debit':main['positive_after_active_prefix'],'lean':lean.get('status'),'run':str(R),'saved_files':len(artifacts)}))
