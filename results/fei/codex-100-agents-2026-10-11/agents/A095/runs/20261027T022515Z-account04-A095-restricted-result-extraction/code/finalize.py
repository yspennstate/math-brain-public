from pathlib import Path
import json, hashlib, datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(name,obj):
 (R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
checks=[json.loads((R/'out'/('CHECK_'+m+'.json')).read_text(encoding='utf-8')) for m in ['compressed','20','21','30','31']]
assert all(x['status']=='PASS' for x in checks)
assert all(x['checker_sha256']==sha(R/'code/check.py') for x in checks)
summary={'status':'PASS','main_cases':sum(x['cases'] for x in checks),'compressed_laws':checks[0]['cases'],'histories':sum(x['cases'] for x in checks[1:]),'main_assertions':sum(x['assertions'] for x in checks),'frontiers':sum(x['frontiers'] for x in checks),'max_internal_seconds':max(x['seconds'] for x in checks),'pilot_excluded':True,'batches':[{k:v for k,v in x.items() if k!='records'} for x in checks]}
boundary=json.loads((R/'out/BOUNDARY.json').read_text(encoding='utf-8'));assert boundary['status']=='PASS' and boundary['code_sha256']==sha(R/'code/boundary.py')
summary['separate_boundary_assertions']=boundary['checks'];put('out/VALIDATION_SUMMARY.json',summary)
put('out/LEAN_RECEIPT.json',{'statement':'example (a e : Real) : (a-2*e)^4 = (a^2+4*e^2)*(a^2-8*e*a+20*e^2)-64*e^4 := by ring','status':'RUNTIME_UNVERIFIED','elapsed_seconds':120.4,'source_sha256':'723e1ce05858223e8c925a28211da7f4dfaba4e070da22aa932f3c05f086447f','translation_fidelity':'UNVERIFIED','claim':'No Lean certification, source/compiler trust receipt or axiom audit obtained.'})
root=Path('~'); campaign=root/'mop_fei100/reports/fei-2026-10-11';worker=root/'brain_workers/FEI100_20261011'
sources=[root/'AGENTS.md',worker/'BOARD.md',worker/'claude/B19/STREAM_NOTES.md']
sources += [campaign/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
supp=root/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
sources += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
sources += list((worker/'context').glob('*.txt'))
previous=A/'runs/20261023T134030Z-account03-A095-restricted-result-extraction'
sources += [previous/n for n in ['DERIVATION.md','REPORT.md','CLAIMS.json','PROGRESS.json','code/check.py']]
sources += [worker/'agents/A094/runs/20261026T232939Z-account04-A094-proof-chain-challenger/REPORT.md',worker/'agents/A086/runs/20261023T140222Z-account03-A086-joint-code-referee/REPORT.md']
receipts=[]
for p in sources:
 raw=p.read_bytes()
 try:s=raw.decode('utf-8');encoding='utf-8'
 except UnicodeDecodeError:s=raw.decode('cp1252');encoding='cp1252 explicit fallback after UTF8 rejection'
 receipts.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':encoding,'read_scope':'Protocol full; own stage20 proof/code full; coordination/current reports and selected contextual paper passages. Hash is a provenance receipt, not independent proof review.'})
put('out/SOURCE_RECEIPTS.json',receipts)
statement=('For every nonconstant Boolean g on a>=1 source bits, m>=2 padding bits, supplied reference R0 of mass in (0,1] and complete cost c<=C0 I(g), C0>=0, fix ORIGINAL K=4C0+15 and the actual point-selector root R0-floor lifted by its true selector kernel. Retain compatible old U<=(C0+37/8)I(g). Along the full-zero matching path, query any source prefix with exact-source point-selector floors, expose the selector at any depth d in [0,a], install data-only floors (A^2+4epsilon^2)/(1+4epsilon), finish all remaining source queries in any order, and then all padding queries down to a constant. Keep every actual inherited sibling, complete query release and full terminal. All positive new reset charges total<573I(g)/128; at every frontier K I(F)-U-Bfull>(C0/2+275/128)I(g)+4C0G>0, G=2^(-a-m)(a+m+1-d0). Original R0,C0,K and old bills do not renew. Key data-only floor chi2<=16u epsilon and D2<24u epsilon for u=2^-m<=1/4; the r=1,0 constant-source endpoints are separately paid. No arbitrary-core source supplier or off-path reset policy is asserted.')
hypotheses=['Uniform Boolean cube, normalized Walsh amplitudes, costs in bits, complete subprobability mass penalty retained','Edit point translated to zero and output-negated so g(0)=1; actual one-point reversal on source+padding+selector cube','Supplied ORIGINAL source and old debit are hypotheses; no executed padding-first history is undone','Only matching-path resets prescribed; all source bits before padding, arbitrary selector exposure depth and source orders; inherited-only off-path trees allowed','Both full physical terminals and complete CE query releases retained at every frontier']
cid='A095-TWO-PADDING-PAID-SELECTOR-EXPOSURE'
claim={'claim_id':cid,'version':2,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':hashlib.sha256(json.dumps({'exact_statement':statement,'hypotheses':hypotheses},sort_keys=True,ensure_ascii=False,separators=(',',':')).encode('utf-8')).hexdigest(),'contributors':['A095/account04'],'proof_source':{'path':str(R/'DERIVATION.md'),'sha256':sha(R/'DERIVATION.md'),'sections':'1-5'},'proof_dependencies':[{'claim_id':cid,'version':1,'source':str(previous/'DERIVATION.md'),'sha256':sha(previous/'DERIVATION.md'),'used':'Point-selector source-prefix floor sum and original root margin, sections1-4,6; supplied hypotheses retained; author proof with review pending'}],'review_records':[],'status':'ANALYTIC_AUTHOR_PROOF_EXACT_CASES_REVIEW_PENDING_NOT_LEAN_CHECKED','supersedes':[cid+'@1'],'refutes':[],'first_unproved_line':'None identified inside the stated conditional extension. Universal ORIGINAL influence-priced source, REQUIRED branching resets, and interacting new edits remain unpaid. Full FEI OPEN.','next_consumers':['A086','A094','A011','A081','A096','A097','A099']}
put('CLAIMS.json',[claim])
next_action='A086/A094 independently reconstruct exact division, r1/r0 endpoints and full ledger; then require and price ONE necessary off-path branch conversion or arbitrary-core INITIAL source from SAME original unused influence. Optional matching path is now paid through a constant.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B19','packet_id':'A095','gap_id':'C020-C024-SAME-OWNER-SIGNED-PROFILE','attempt_id':'A095-stage21-exact-cancellation-complete-matching-path','method':'Exact polynomial division retains zero-amplitude cancellation; reach-weighted geometric endpoint sum; SAME-original full complete-query-release ledger','mathematical_delta':'ONE data-only reset -> ALL remaining source resets and all padding resets to a constant; supplied SAME original K and old U; reserve>(C0/2+275/128)Ig+4C0G. No universal initial source or FEI resolution.','deliverable_status':'COMPLETE_LOCAL_REVIEW_PENDING','mathematical_status':'CONDITIONAL_HISTORY_TRANSFER_AUTHOR_PROOF_FULL_FEI_OPEN','claim_versions_used':[cid+'@1; sections1-4,6','A094 stage21 accounting objection as scope context, not a dependency theorem'],'claims_created_or_changed':[cid+'@2'],'source_artifacts':['DERIVATION.md','FROZEN_SPEC.json','code/check.py','code/boundary.py','out/VALIDATION_SUMMARY.json','out/SOURCE_RECEIPTS.json','out/LEAN_RECEIPT.json'],'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Independent review of new extension pending; no blanket acceptance of preceding unreviewed proof','Universal original influence-priced source and required branching/new-edit payment OPEN','Lean key-step attempt RUNTIME_UNVERIFIED; no formal claim','Supervisor mirror, adoption and downstream mathematical use unverified','Wake flagged stale owner/state/dream notes; excluded from proof premises'],'packet_ids':['A095']}
put('PROGRESS.json',progress);put('PACKET_DELTA.json',progress)
report=f'''# A095 stage21: exact cancellation pays the complete matching path

## exact target, quantifiers, hypotheses and units

Every nonconstant uniform Boolean source g on a>=1 bits, every m>=2 initial padding, any supplied original R0 with complete cost c<=C0Ig, mass in(0,1], C0>=0. Fix SAME original K=4C0+15 and retain old U<=(C0+37/8)Ig. Extend the exact source-first point-selector policy through any selector exposure depth, all remaining DATA-source resets, and padding down to dimension zero. Both complete terminals and all complete CE query releases remain. Bits; physical uniform influence. Full FEI OPEN.

## sources actually read, revisions and theorem locators

Full protocol2026-10-11-execution-v2; current BOARD/B19 notes, own rolling state and stage20 full DERIVATION/code. Campaign/index/plan/supplement accessed for scope and source navigation; selected theorem/scope passages in all four supplied paper versions were decoded explicitly as cp1252 after UTF8 rejection. No new paper audit, priority or literature claim. A086 stage21 and A094 stage21 REPORTs read; their actual physical-query KL warning governs the ledger distinction. Exact read-file pins are in out/SOURCE_RECEIPTS.json; hashes do not certify content. The current explicit resumed stage governs despite historical campaign end dates.

## complete derivation or exact first unsupported line

DERIVATION1 proves EXACT chi2=16e+48e^2-64e^4(1+4e)sum1/(A^2+4e^2). Zero-amplitude cancellation gives chi2<=16ue for m>=2, hence D2<24ue. Along the remaining source path reach*e=e_root/2, so ALL data-source resets cost<3Ig/4. Constant-source padding endpoint formula chi2=64e^3(1-e)/(1+4e^2), with separate r1 log2(3)<2 and r0 D0, pays ALL further padding resets for<3Ig/4. Add the inherited stage20 source-prefix bound381Ig/128: total new positive charges<573Ig/128. SAME original reserve after full U is>(C0/2+275/128)Ig+4C0G at EVERY frontier. The proof retains accumulated physical-query KL contraction inside Bfull; no negative reset or query credit is reissued. First unsupported universal line: an ORIGINAL O(I) arbitrary-core source, or payment of a REQUIRED off-path branching reset/new interacting edit. Completing this optional matching path does not establish necessity.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json saved before pilot. Commands: python -B -X utf8 code/check.py pilot, compressed,20,21,30,31 sequentially; then code/boundary.py. Pilot8 cases/514 assertions is excluded. Main ALL278 labelled sources a0..3 at m0,1,2,3,7,8 gives1668 compressed laws; four direct batches give480 complete original-owner histories and {summary['frontiers']} frontiers, all source prefixes, forward/reverse orders and two references including mass1/2. Main total {summary['main_assertions']} exact assertions PASS; separate9 boundary assertions PASS including literal C0=0 dictator and independent polynomial coefficient convolution. Fraction truth tables/spectra/chi-square/transport; rigorous rational atanh logarithms with proved tail and outward80-bit dyadic rounding. No floating signs or all-dimensional inference from samples. Maximum internal helper time {summary['max_internal_seconds']:.3f}s<55s; estimated180MB, peak unmeasured. No heavy, GPU, detached or >300MB search. Lean polynomial attempt returned RUNTIME_UNVERIFIED after120.4s, source hash recorded; no Lean/axiom certification is claimed. The mathematical rung is author proof with exact finite checks and independent review pending.

## proof dependencies and changed downstream conclusions

Version2 extends the existing A095 supplied-owner claim instead of opening a broad unrelated candidate. Its original source-prefix estimate/root margin is the explicit version1 dependency; that author's complete proof remains review pending. New division and endpoint sum are derived in full. A094's accounting objection does not invalidate the stronger Bfull identity used here. Global FEI constant improvement: zero. No silent source replacement or descendant influence certificate occurs.

## one next mathematical action and independent reviewer

{next_action}

## actual persistence receipts or precise save blocker

Four exact-schema protocol files, standalone extension proof, frozen spec, code, exact outputs and source/Lean receipts saved only inside A095. Rolling STATUS/WORKLOG/LEARNED updated. out/PERSISTENCE_RECEIPT.json records reread local hashes/schema checks. Each file<20MB. Supervisor mirror, external independent review, adoption and downstream use unverified. No git, mail, shared research source/brain edits, trading work, detached workers or process stops. Wake reported stale owner/state/dream sources and these were excluded from mathematical premises. Checklist outcomes are separately recorded, without claiming a lock failure succeeded.

## Universal bridge

C024 history transfer and C019/C020 complete-reference payment advance from ONE post-selector data-only reset to the ENTIRE remaining matching path, all source then padding queries through a constant, at unchanged original K=4C0+15 and FULL old U. Exact cancellation improves the data-floor estimate54e->24ue; full-ledger reserve becomes>(C0/2+275/128)Ig+4C0G. Universal FEI remains OPEN: the original arbitrary-core source and required branching/new-edit payment remain unpaid. NEXT tests a necessary branching conversion or that original source, because further optional matching-path extensions are now exhausted and cannot alone bridge full FEI.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(A/'STATUS.md').write_text('STATE: Stage21 saved: SAME supplied owner pays ENTIRE matching path after selector through all DATA-source/padding resets to constant; reserve>(C0/2+275/128)Ig+4C0G; exact checks PASS; review pending; FEI OPEN.\nNEXT: A086/A094 review zero-mask division/r1-r0/full Bfull; fund REQUIRED off-path branch/new edit or ORIGINAL arbitrary-core O(I) supplier from SAME unused owner; optional matching path exhausted.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} Stage21: exact zero-mask chi-square cancellation pays all remaining data-source and padding resets at SAME original owner; {summary["main_assertions"]} main+9 separate boundary checks PASS. Lean attempt RUNTIME_UNVERIFIED. Original supplier/required branching OPEN; no shared edits/process stops.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-27 stage21: For data-only point edit q=(A-2e)^2, R=(A²+4e²)/(1+4e), exact division gives chi2=16e+48e²-64e^4(1+4e)sum1/(A²+4e²). N<=u/e nonzero amplitudes gives chi2<=16ue+(-16+64u)e²<=16ue at m>=2; D<24ue. Entire remaining DATA-source path costs<3Ig/4. Constant-source padding chi2=64e³(1-e)/(1+4e²), r1 Dlog2(3),r0 D0; all further padding costs<3Ig/4. Together with old source-prefix381Ig/128, new positive total<573Ig/128; SAME K4C0+15 after FULL old U leaves>(C0/2+275/128)Ig+4C0G with ALL complete query releases/both terminals. No optional matching path remains unpaid; move to REQUIRED off-path branching/new edit or ORIGINAL supplier. Lean polynomial attempt unverified; analytic author proof, review pending.\n')
protocol=json.loads((campaign/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
pf=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(pf)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all(field in report for field in protocol['required_per_run']['report_fields'])
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']
assert all(p.stat().st_size<20_000_000 for p in files)
put('out/PERSISTENCE_RECEIPT.json',{'status':'PASS','schemas':'exact required field sets; REPORT fields present; progress/delta byte-identical','files':[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files],'remote_status':'UNVERIFIED','independent_review':'PENDING'})
print(json.dumps(summary,indent=2));print('SCHEMAS_AND_LOCAL_PERSISTENCE_PASS')
