from pathlib import Path
import json,hashlib,datetime,shutil
R=Path(__file__).resolve().parents[1];A=R.parents[1];B=A.parent
def read(p):return Path(p).read_text(encoding='utf-8-sig')
def write(p,s):Path(p).write_text(s,encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def js(p,x):write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
old=A/'runs/20261023T112820Z-account03-A001-quantifier-audit'
source=B/'A094/runs/20261023T131208Z-account03-A094-proof-chain-challenger'
older=B/'A094/runs/20261023T110024Z-account03-A094-proof-chain-challenger'
src95=B/'A095/runs/20261023T112654Z-account03-A095-restricted-result-extraction'
src86=B/'A086/runs/20261023T114749Z-account03-A086-joint-code-referee'
protocol=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
proto=json.loads(read(protocol));cert=json.loads(read(R/'out/CERTIFICATE.json'));pilot=json.loads(read(R/'out/PILOT.json'))
assert cert['status']=='PASS' and cert['profiles']==417 and cert['source_paths']==30
assert cert['runtime_seconds']<55 and pilot['runtime_seconds']<60
shutil.copyfile(old/'out/RECOVERED_GAP_MAP.json',R/'out/RECOVERED_GAP_MAP.json')
assert sha(old/'out/RECOVERED_GAP_MAP.json')==sha(R/'out/RECOVERED_GAP_MAP.json')
claim=next(x for x in json.loads(read(source/'CLAIMS.json')) if x['claim_id']=='A094-SMALL-PADDING-POSITIVE-SOURCE-PATH-PAYMENT')
assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
review={'reviewer':'A001/account03/B01','at':now,'verdict':'HOLDS_WITHOUT_REPAIR_AT_EXPLICIT_SCOPED_BOUNDARY','proof':str(R/'DERIVATION.md'),'validation':str(R/'out/CERTIFICATE.json'),'scope':'Full arbitrary-Boolean-source standalone small-padding conversion and physical source-path bounds; original-root owner corollary conditional on supplied7Ig/8 reserve. Rate-four corollary arithmetic/implication checked conditionally; its preceding actual two-reset baseline NOT independently reconstructed from original sources in this stage. Not full-chain acceptance.','independence':'Separate weighted Euclidean reconstruction, exact compressed-law checker, literal FWHT physical children, mass1/2 incoming source, all source orders through2bits, full signed identity and separate positive-booked bill; no negative reset credit reclaimed. Prior A001 exact log helper reused.','substantive_repair_supplied':False}
claim['review_records'].append(review);claim['status']='SCOPED_INDEPENDENT_RECONSTRUCTION_HOLDS_OWNER_INPUT_AND_RATE4_BASELINE_CONDITIONAL'
js(R/'CLAIMS.json',[claim]);js(R/'out/REVIEW.json',review)
sources=[protocol,B.parent/'BOARD.md',B.parent/'claude/B01/STREAM_NOTES.md',source/'DERIVATION.md',source/'CLAIMS.json',src95/'DERIVATION.md',src86/'RECONSTRUCTION.md',old/'DERIVATION.md',old/'code/helpers.py',old/'out/RECOVERED_GAP_MAP.json']
manifest=[{'path':str(p),'sha256':sha(p),'scope':'actually read this stage, or explicit carried baseline/helper as identified in REPORT'} for p in sources]
js(R/'out/SOURCES.json',manifest)
nextaction='A011/A094/A099: supply a noncircular absolute influence-priced ORIGINAL reference for arbitrary core, or a well-founded genuinely decreasing source-price mechanism; for C024 test required selector exposure from CURRENT depleted owner after source-first conversion, preserving all old U and both full terminals. A094 independently inspect this scoped review.'
delta='Independently reconstruct A094 small-padding exact-floor conversion and arbitrary supplied-core source-first continuation: Dfloor<C(u)epsilon, all positive bookings<=C(u)uIg, reserve>1613Ig/8192 conditional on original7Ig/8. 417 compressed Boolean profiles and30 full physical source-order paths with original source masses1 and1/2;5515 exact assertions. Prior quarter-profile compatibility gap closed for this precise prospective path, not arbitrary executed histories. Initial universal source remains FEI-equivalent.'
progress=dict(protocol_revision=proto['revision'],run_id=R.name,stream='B01',packet_id='A001',gap_id='C024-SOURCE-FIRST-EXACT-FLOOR-TO-C000-SUPPLIER',attempt_id='A001-20261023T134242Z-scoped-independent-review',method='Independent analytic reconstruction plus exact rational Fourier and positive-booking ledger certificates',mathematical_delta=delta,deliverable_status='COMPLETE_LOCAL_READBACK_PENDING',mathematical_status='SCOPED_REVIEW_HOLDS_CONDITIONAL_OWNER; FULL_FEI_OPEN',claim_versions_used=['A094-SMALL-PADDING-POSITIVE-SOURCE-PATH-PAYMENT@1','A094-LARGER-NONVANISHING-ALL-FRONTIER-ALLOWANCE@1','A001-CURRENT-SOURCE-QUANTIFIER-EQUIVALENCE@1'],claims_created_or_changed=['A094-SMALL-PADDING-POSITIVE-SOURCE-PATH-PAYMENT@1: scoped review record only, statement unchanged'],source_artifacts=manifest,next_consumers=['A094','A011','A086','A095','A099','B01','B20'],next_action=nextaction,stagnant_substantive_attempts=0,blockers=['Universal initial source supplier unpaid; supplied C0 is not produced by continuation.','Rate-four preceding baseline not independently reconstructed here; no full-chain acceptance.','No local mirror/publication verification; supervisor publication route only.','Brain self-care degraded: stale owner/state/dream notes; recurrence observer unverified.'],packet_ids=['A001'])
js(R/'PROGRESS.json',progress);shutil.copyfile(R/'PROGRESS.json',R/'PACKET_DELTA.json')
report=f'''# A001 quantifier audit — 2026-10-23 13:42 UTC stage

## exact target, quantifiers, hypotheses and units

Prove existence of ONE finite absolute C such that for EVERY n>=0 and EVERY Boolean f on the uniform cube, H(f)<=C I(f), with base-two spectral entropy and literal physical influence. Constants have H=I=0, but their references retain full CE. Full FEI is OPEN. This stage independently reviews a conditional universal source-first conversion theorem; no new broad candidate is opened.

## sources actually read, revisions and theorem locators

Stage intake: current BOARD (preserved as out/BOARD_START.md), B01 STREAM_NOTES v1, own STATUS, machine-wide AGENTS and the execution protocol. Source hashes and carried-source distinctions are in out/SOURCES.json. A094 run20261023T131208Z DERIVATION sections1-6 and the small-padding claim statement were read; A086 run20261023T114749Z RECONSTRUCTION independently accepts the original allowance. A095 completed run20261023T112654Z DERIVATION sections1-5 was read as a conditional explicit-family handoff/nested-chain theorem, without independently accepting its canonical-cost dependencies. New A095/A011 run folders were still incomplete when queried; missing files are not treated as read. The previous37-route recovered-manuscript inventory is copied BYTE IDENTICALLY; it is a carried baseline, not a new paper review.

## complete derivation or exact first unsupported line

DERIVATION sections1-4 reconstruct Dfloor<C(u)epsilon, C(u)=1/2+(5043/128)u for u=2^-m,m>=3, using actual joint point-edit spectra, complete target floor, Boolean coefficient granularity and chi-square. Physical source-query inheritance retains reference-only atoms and subprobability mass; every conversion is positively booked and every sibling/full terminal retained. Original physical reach times epsilon remains constant down the distinguished path. Cube minimum boundary then gives total positive booking<=C(u)u I_g<=5555I_g/8192. Given the separate original7I_g/8 allowance, remaining reserve is >1613I_g/8192. This is an EXACT prescribed floor handoff, stronger than the prior quarter-target likelihood floor in this precise prospective source-first regime.

Review HOLDS without repair for the standalone arbitrary-source conversion/path bound and conditionally for its original-owner corollary. The rate-four corollary arithmetic is checked, but its preceding two-reset baseline is not independently reconstructed from original sources here: no full-scope or full-chain acceptance is asserted. DERIVATION section5 gives the first unsupported universal line: obtain CE(P_g,R_g)<=C0 I_g for all dimensions/Boolean cores at ONE C0 without assuming FEI. That premise is exactly FEI(C0) by Gibbs and R_g=P_g. The output4C0+15 is not a source-price improvement. A separate supplied C_g for each example does not establish the uniform quantifier.

## executed validation with domain, arithmetic, commands and outputs

Frozen specification: out/FROZEN_SPEC.json, before the main job. Helper is SHA-pinned in the persistence receipt. All139 sign-normalized sources on0..3 bits, with m=3,5,8, give417 compressed exact profiles. Global sign is the only reduction. Physical source-query validation additionally uses all8 nonconstant sign-normalized sources through2 bits, every source order and original source masses1 and1/2, giving30 paths. Both signed telescoping identities and the larger positive-booked bill are checked, discarding negative reset credit, with old U=69I_g/8 and K31 retained. Constants/a0 endpoints remain in the profiles and reached source endpoints. Integer FWHT, Fraction arithmetic, exact prime-log vectors and rational outward atanh enclosures supply certificates; no floating sign evidence is used.

Commands: python -B -X utf8 code/audit.py --pilot; then python -B -X utf8 code/audit.py. Pilot: {pilot['exact_assertions']} assertions,9 profiles,{pilot['runtime_seconds']:.3f}s. Main: {cert['exact_assertions']} assertions,417 profiles,30 paths,{cert['runtime_seconds']:.3f}s, PASS. Pilot and main counts are separate. Estimated memory120MB; no >300MB job, heavy job, GPU or detached producer. Finite cases verify the implementation; DERIVATION supplies the all-dimensions analytic argument. The main exact certificate and the separate pilot are saved in out/.

## proof dependencies and changed downstream conclusions

The A094 statement SHA remains {claim['statement_sha256']}; CLAIMS.json adds only a scoped independent review record, with no substantive repair. Source-first physical continuation is compatible with the exact floor and supplied original source account. Earlier demands for such compatibility should not be repeated as an unsolved obligation in this regime. The original7Ig/8 reserve is a conditional input with A086 review, not a new initial supplier. A095's unbounded nested chain uses geometric original reach and a priced explicit-family source; simultaneous broad active branches and arbitrary new edits are outside it. No constant-tail reference normalization, fresh descendant C0 or full local FEI certificate is issued.

## one next mathematical action and independent reviewer

{nextaction}

## actual persistence receipts or precise save blocker

All research writes stay inside A001. Four protocol files, complete proof, frozen spec, executable checker, exact outputs, unchanged recovered gap map, source hashes, and rolling STATUS/WORKLOG/LEARNED are saved locally. out/PERSISTENCE_RECEIPT.json records actual readback/schema/hash checks. Mirror/public release are UNVERIFIED and remain supervisor work under the explicit no-git instruction. No external messages or research-brain writes occurred. Own computation has finished; nothing is left running for this stage. Brain self-care is degraded: owner-model/state/dream sources are stale and recurrence observer unverified; personal context continuity is affected, while mathematics is grounded in the cited current source files.

**Universal bridge:** C024 advances from an arbitrary quarter-target likelihood floor to an independently reconstructed EXACT prescribed floor handoff and physical source-first continuation for EVERY supplied Boolean core with m>=3, preserving the SAME original account, old U and both complete terminals, with reserve >1613Ig/8192. This closes a real conditional compatibility obligation, not the universal original-source price. C019/C020 still require an independently funded source or compatible broad-branch/selector continuation without renewed C0. The shortest NEXT is to supply a noncircular original reference price or a well-founded decreasing source mechanism, using current depleted-account structural tests where needed; another isolated product family cannot discharge the universal quantifier.
'''
write(R/'REPORT.md',report)
write(A/'STATUS.md','STATE: Stage saved: scoped independent A094 small-padding source-FIRST exact-floor payment HOLDS;417 profiles/30 paths/5515 exact checks;reserve>1613Ig/8192 conditional original owner;FEI OPEN.\nNEXT: '+nextaction+'\n')
for name,text in [('WORKLOG.md',f'\n[{now}] Stage {R.name}: {delta} Read A095 unbounded nested-chain conditional family proof; no full-chain acceptance. Main{cert["runtime_seconds"]:.3f}s. All own computations exited; mirror unverified. NEXT: {nextaction}\n'),('LEARNED.md','\n2026-10-23 13:42 stage: An actual prescribed exact-source floor for arbitrary supplied core can be installed along a SOURCE-FIRST path with m>=3, all positive costs <=(1/2+5043*2^-m/128)2^-m Ig, leaving>1613Ig/8192 from an original7Ig/8 reserve. Reference-only fibers and normalized child factors must be retained; signed bill and positive-booked bill are distinct. This fixes that compatibility gap, but does not price the source. K=4C0+15 preserves a supplied price rather than improving it; self-substitution is circular. Partial review must not be presented as acceptance of an unreconstructed rate-four baseline.\n')]:
 with (A/name).open('a',encoding='utf-8') as f:f.write(text)
required=proto['required_per_run'];expected={k.split(' (')[0] for k in required['progress_fields']}
assert set(progress)==expected
assert set(claim)==set(required['claim_fields'])
assert all(('## '+h) in read(R/'REPORT.md') for h in required['report_fields'])
assert len(read(A/'STATUS.md').splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
progress['deliverable_status']='COMPLETE_LOCAL_SCHEMA_HASH_READBACK_PASS'
js(R/'PROGRESS.json',progress);shutil.copyfile(R/'PROGRESS.json',R/'PACKET_DELTA.json')
artifacts=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']
assert all(p.stat().st_size<20*1024*1024 for p in artifacts)
receipt={'status':'PASS','at':now,'checks':['exact protocol schemas','unchanged reviewed statement SHA','417 profiles/30 paths/5515 exact assertions','source gap-map byte identity','progress/packet byte identity','two-line rolling status','report seven fields and final universal-bridge paragraph','UTF8 readback and file-size cap'],'artifacts':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in artifacts],'rolling_files':[{'path':str(A/n),'sha256':sha(A/n)} for n in ('STATUS.md','WORKLOG.md','LEARNED.md')],'publication':'UNVERIFIED_SUPERVISOR_ROUTE','own_computation':'ALL_EXITED','full_FEI':'OPEN'}
js(R/'out/PERSISTENCE_RECEIPT.json',receipt)
assert read(R/'REPORT.md').rstrip().split('\n')[-1].startswith('**Universal bridge:**')
print(json.dumps({'status':'PASS','artifacts':len(artifacts),'certificate_assertions':cert['exact_assertions'],'claim_statement_unchanged':True,'new_broad_claims':0,'full_FEI':'OPEN'}))
