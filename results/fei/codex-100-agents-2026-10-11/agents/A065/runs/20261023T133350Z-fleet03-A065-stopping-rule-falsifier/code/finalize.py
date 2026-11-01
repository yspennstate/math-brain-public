from pathlib import Path
import json,hashlib,copy,datetime

ROOT=Path(__file__).resolve().parents[1]; OWN=ROOT.parents[1]; BASE=OWN.parents[1]
PROTOCOL=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
SOURCE=BASE/'agents/A087/runs/20261023T121304Z-fleet03-A087-restriction-referee'
PREV=OWN/'runs/20261023T112150Z-fleet03-A065-stopping-rule-falsifier'
def read(p):return json.loads(p.read_bytes().decode('utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,s):p.write_bytes(s.encode('utf-8'))
def js(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def append(p,s):
 raw=p.read_bytes() if p.exists() else b''; nl='\r\n' if b'\r\n' in raw else '\n'
 entry=s.replace('\r\n','\n').replace('\n',nl).encode('utf-8')
 if b'20261023T133350Z stage20' not in raw:p.write_bytes(raw+nl.encode()+entry+nl.encode())

protocol=read(PROTOCOL); spec=read(ROOT/'FROZEN_SPEC.json'); main=read(ROOT/'out/MAIN.json'); pilot=read(ROOT/'out/PILOT.json')
assert main['status']==pilot['status']=='PASS' and main['query_cases']==24 and main['physical_children']==48
assert main['actual_installation_continuations']==48 and main['reentry_cases']==18
assert len(main['nonzero_erasure_defect_cases'])==10 and main['seconds']<55
for name,digest in spec['helper_version'].items():assert sha(ROOT/'code'/name)==digest
source_claim=next(c for c in read(SOURCE/'CLAIMS.json') if c['claim_id']=='A087-PRODUCT-HISTORY-SIGNED-COCYCLE-INSTALLATION')
assert hashlib.sha256(source_claim['exact_statement'].encode()).hexdigest()==source_claim['statement_sha256']
assert sha(SOURCE/'PROOF.md')==source_claim['proof_source']['sha256']
claim=copy.deepcopy(source_claim)
claim['review_records'].append({'reviewer':'A065','verdict':'HOLDS_NEW_EXTENSION_AT_STATED_SCOPE_NO_REPAIR','proof':str(ROOT/'PROOF.md'),'proof_sha256':sha(ROOT/'PROOF.md'),'certificate':str(ROOT/'out/MAIN.json'),'independence_scope':'New implementation written without reading or running A087 code; direct Boolean Walsh reconstruction and two alternative outside-cell compressions. New all-history proof reconstructed from definitions.','limitation':'A065 originated selector-only baseline dependency and is credited there. This is NOT an independent full-chain review of the earlier A065 dependency; A094 full-chain review remains requested. No Lean check.'})
claim['status']='EXTENSION_RECONSTRUCTED_BASE_DEPENDENCY_AUTHOR_FULL_CHAIN_REVIEW_PENDING'
js(ROOT/'CLAIMS.json',[claim])

next_action='Attack a noncircular influence-priced ORIGINAL reference/owner supplier for an indecomposable Boolean core; keep the point-tensor A/I divergence as a compulsory admission guard, with signed E/O, old debits and full H+KL. A094 reviews the complete chain; do not spend another stage on already-paid product-history depth.'
source_paths=[PROTOCOL,BASE/'BOARD.md',BASE/'claude/B13/STREAM_NOTES.md',SOURCE/'PROOF.md',SOURCE/'CLAIMS.json',PREV/'PROOF.md',PREV/'CLAIMS.json',PREV/'code/exact.py',BASE/'agents/A061/runs/20261023T113614Z-fleet03-A061-entropy-process/REPORT.md',BASE/'agents/A062/runs/20261023T120607Z-fleet03-A062-influence-compensator/REPORT.md']
sources=[]
for p in source_paths:
 raw=p.read_bytes();sources.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)})
js(ROOT/'out/SOURCE_RECEIPTS.json',sources)
js(ROOT/'out/REVIEW_VERDICT.json',{'claim_id':claim['claim_id'],'version':1,'source_statement_sha256':claim['statement_sha256'],'new_extension_verdict':'HOLDS_NO_REPAIR','full_chain_independent_review':'PENDING_A094_A065_OWNS_BASE_DEPENDENCY','exact_primary_checks':main['total_checks'],'pilot_checks_excluded':pilot['total_checks'],'query_cases':24,'physical_children':48,'installed_continuations':48,'erasure_defect_cases':10,'erased_reference_reentry_cases':18,'universal_fei':'OPEN','first_unsupported_universal_line':next_action})

fields=protocol['required_per_run']['report_fields']
paras=[
 'Independently reconstruct the NEW A087 all-physical-product-history signed correction and one-actual-tensor-installation theorem, including its exact two-module one-data booking. Fair physical outcomes, coherent kernels with fair source-zero extension, normalized supporting original references, bounded stopping, at most one actual installation, bits throughout. Scope is the stated theorem and exact finite policy class; full FEI remains OPEN. Saved NEXT was already closed by A087 and is consumed rather than repeated as a new A065 claim.',
 'Read BOARD dated 2026-10-23 13:38 UTC in B13 scope, B13 lead v2 (2026-10-11), own STATUS, current execution protocol 2026-10-11-execution-v2, A087 run20261023T121304Z PROOF sections3--6 and exact CLAIMS, own stage19 proof/helper, and latest A061/A062 report handoffs. Earlier campaign/paper baseline is inherited, not newly reread or used as a new dependency. Immutable source bytes and statement/proof hashes are checked in out/SOURCE_RECEIPTS.json. A087 supplied the mathematical extension; no A087 source code was read/imported/executed. Current owner deadline 2026-10-23 14:49 UTC supersedes the old protocol calendar.',
 'PROOF.md sections1--2 reconstruct the general signed cocycle and original2A potential; sections3--5 give a separate exact Boolean certificate of all24 data queries,48 fair children and48 actual post-installation continuations. Verdict HOLDS at stated scope, no repair: mean d_child=d+(E_local-E_global)+(O_local-O_global). Other-module erasure correction is rho log2(4/3), rho=(0,5/8,5/8,5/8,7/64,7/64); source re-entry alone does not imply a nonzero correction. Sharp pending booking is log2(32/29)/2<1/8, with no ordinary-query top-up when already nested. The first unpaid universal line is an influence-priced original reference/owner supplier for indecomposable cores: section6 proves the original marginal-product KL/I is unbounded on actual point-function tensor families.',
 f'Frozen FROZEN_SPEC.json preceded both runs: fixed two-module GF4 source, no symmetry omission, 4 pilot /24 main query cases, exact rational arithmetic and prime-log identities, 96-bit rigorous 32-term atanh-tail sign enclosures, estimated130MB and maximum55seconds, no dimension escalation. Commands: python -B -X utf8 code/review.py --pilot; python -B -X utf8 code/review.py. Pilot PASS {pilot["total_checks"]} checks in {pilot["seconds"]:.6f}s; excluded from primary count. Main PASS {main["total_checks"]} checks in {main["seconds"]:.6f}s. Direct integer character sums independently check every child spectrum against FWHT and physical edges. All24 queries and48 installed-reference continuations pass;18 queries have positive erased reference-only re-entry and10 have positive erasure correction. Full terminal H for both fair children is saved in every case. Exact outputs: out/PILOT.json, out/MAIN.json, out/REVIEW_VERDICT.json. No heavy search or memok-triggering job was run.',
 'Consumed A087-PRODUCT-HISTORY-SIGNED-COCYCLE-INSTALLATION@1, source statement hash e7c04ca466d3a6380f65185c2f2fdf5ddb0ef176ad2be3388eb61522a80dff92, and accepted selector-only A065-FIXED-PRODUCT-ROOT-ZERO-SECTOR-LINEAR-DEFICIT@1. No new broad candidate is opened. A065 contributed the earlier baseline dependency; this review independently reconstructs the NEW extension, supplies no repair, and is NOT counted as an independent full-chain review of that earlier A065 claim. A094 remains the full-chain reviewer. Downstream: use the erasure-aware cocycle beyond selector-only histories; the finite same-owner bound leaves>97/8 after the old quarter and A=5, while arbitrary physical product histories plus one installation use the general29S/92 remainder. Neither cap is an influence-priced universal owner theorem.',
 next_action,
 'All required protocol files, proof, frozen spec, code and exact outputs are locally saved. STATUS is two lines; WORKLOG/LEARNED append dated results preserving existing line endings. code/finalize.py rereads exact schema fieldsets, all source statement/proof hashes, frozen helper hashes, compatibility-copy identity, output case counts and SHA256/byte receipts for every saved file except the receipt file itself. No local save blocker. Supervisor archive, mirror, downstream use, public release and A094 full-chain acceptance remain unverified. Did: reconstructed and checked the A087 extension. Stopped: this declared finite stage. Left running: no research job.'
]
report='# A065 stage20: erasure-aware history repair reconstructed\n\n'+'\n\n'.join('## '+h+'\n\n'+p for h,p in zip(fields,paras))
report+='\n\n**Universal bridge:** C019 stopping-tree payment and C024 history transfer advance by a source-bound reconstruction of the repair to A065\'s last open boundary: arbitrary physical product histories require the SIGNED erasure difference as well as outcome difference, and one actual tensor installation is paid from supplied original2A. The complete finite24-query certificate confirms the sharper nested booking needs zero top-up and preserves the old account/full terminal H+KL. This closes that product-history mechanism, not full FEI. An influence-priced original reference/owner supplier for arbitrary indecomposable cores remains unpaid; the actual point-tensor initial-KL obstruction rules out the naive supplier. NEXT attacks that universal admission step, because another selector or ordinary depth would only revisit an already-funded class.\n'
write(ROOT/'REPORT.md',report)

previous=read(PREV/'PROGRESS.json')
progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B13','packet_id':'A065','gap_id':previous['gap_id'],'attempt_id':'A065-stage20-A087-erasure-aware-extension-reconstruction','method':'Independent new-extension proof reconstruction, exact Boolean two-orientation compressed-spectrum certificate, source-bound no-repair review','mathematical_delta':'A087 extension HOLDS at stated scope: signed erasure-aware all-history cocycle and one-installation2A cap; sharp finite booking unchanged,24 data queries/48 children/48 installed continuations; no new claim or FEI closure. Base dependency originated A065, so independent full-chain review remains pending.','deliverable_status':'COMPLETE_LOCAL_SAVED_AND_READBACK_VERIFIED','mathematical_status':'STATED_EXTENSION_RECONSTRUCTED_NO_REPAIR; FULL_CHAIN_REVIEW_PENDING; UNIVERSAL_OWNER_AND_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':claim['claim_id'],'version':1},{'claim_id':'A065-FIXED-PRODUCT-ROOT-ZERO-SECTOR-LINEAR-DEFICIT','version':1}],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'local source-bound reconstruction review only; source claim and shared registries untouched'}],'source_artifacts':sources,'next_consumers':['A061','A062','A064','A087','A094','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Universal noncircular influence-priced original-owner supplier is not established.','Independent full-chain A094 acceptance and supervisor archive/mirror unverified.'],'packet_ids':['A065']}
js(ROOT/'PROGRESS.json',progress);js(ROOT/'PACKET_DELTA.json',progress)
write(OWN/'STATUS.md','STATE: Stage20: A087 erasure-aware product-history extension reconstructed, no repair;369295 exact checks/24 queries/48 installed continuations; sharp reserve<1/8; full-chain A094 review pending; FEI OPEN.\nNEXT: Influence-priced ORIGINAL reference/owner for an indecomposable core, with point-tensor admission guard and signed E/O/full H+KL; stop extending already-paid product histories; A094 full-chain review.\n')
append(OWN/'WORKLOG.md','## 20261023T133350Z stage20 (2026-10-23 UTC)\nSaved NEXT already closed by A087 run20261023T121304Z. Reconstructed new all-history cocycle/one-installation2A proof without repair; wrote independent GF4 Boolean source, raw Walsh checks and both outside-cell compressions, never read/ran A087 code. Main369295 exact checks PASS in14.0484771s:24 ordinary queries,48 children,48 actual installed-reference continuations;18 erased reference-only re-entries,10 positive erasure corrections. Sharp booking log2(32/29)/2<1/8 unchanged by one data query; same old account/full H retained. A065 owns baseline dependency so not counted as independent full-chain review; A094 needed. No universal owner or FEI closure. Fresh wake degraded: model100h/state84.6h/dream35.3h; warned owner, did not repair unrelated brain state. All research jobs ended; artifacts saved locally only.')
append(OWN/'LEARNED.md','## 20261023T133350Z stage20 durable reconstruction\nFor a physical product with original supporting tensor reference, global K minus sum of separately transported local Ks evolves by BOTH signed erasure and outcome differences. Re-entry does not itself force erasure difference: selected GF4 module queries cancel it, other-module data has rho log2(4/3), rho=(0,5/8,5/8,5/8,7/64,7/64). One actual tensor installation plus inherited continuation is funded by supplied original2A; a second installation is not included. On exact two-module selector/one-data policy, sharp extra booking log2(32/29)/2<1/8 needs no nested top-up. This new A087 extension was reconstructed without source repair,369295 checks; own earlier baseline is not independently reviewed by its author. Initial actual product KL/I diverges on point tensors (I=m, KL>=m^2-5m-2), so universal influence-priced reference/owner admission is still the relevant frontier; additional paid product-history depth cannot fix it.')

# Exact schema and actual persistence checks, not a claim of remote acceptance.
cf=set(protocol['required_per_run']['claim_fields']);pf={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert all(set(c)==cf for c in read(ROOT/'CLAIMS.json'))
assert set(read(ROOT/'PROGRESS.json'))==pf
assert read(ROOT/'PROGRESS.json')==read(ROOT/'PACKET_DELTA.json')
assert [x[3:] for x in report.splitlines() if x.startswith('## ')]==fields
assert report.split('\n\n')[-1].startswith('**Universal bridge:**')
assert len((OWN/'STATUS.md').read_text().splitlines())==2
receipts=[]
paths=sorted(p for p in ROOT.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json')+[OWN/n for n in ('STATUS.md','WORKLOG.md','LEARNED.md')]
for p in paths:
 raw=p.read_bytes();assert len(raw)<20*1024*1024
 receipts.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)})
js(ROOT/'out/PERSISTENCE_RECEIPTS.json',{'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'receipts':receipts,'schema':'PASS','frozen_hashes':'PASS','claim_source_hashes':'PASS','compatibility_identity':'PASS','remote_acceptance':'UNVERIFIED'})
for r in receipts:
 p=Path(r['path']);assert sha(p)==r['sha256'] and p.stat().st_size==r['bytes']
print(json.dumps({'status':'PASS','saved_files_verified':len(receipts),'protocol_files':4,'source_claim_hash':claim['statement_sha256'],'main_checks':main['total_checks'],'no_research_jobs_left_running':True,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}))
