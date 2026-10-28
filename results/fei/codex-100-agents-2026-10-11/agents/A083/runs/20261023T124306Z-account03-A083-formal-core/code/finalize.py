from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
BASE=Path('~/brain_workers/FEI100_20261011')
def digest(b):return hashlib.sha256(b).hexdigest()
def save(name,x):(R/name).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
pr=json.loads(protocol.read_text(encoding='utf-8'))
res=json.loads((R/'out/RESULT.json').read_text(encoding='utf-8'))
formal=json.loads((R/'out/LEAN_RESULT.json').read_text(encoding='utf-8'))
assert res['status']=='PASS' and res['fixtures']==132 and res['proposed']==144 and res['checks']==16625
assert formal['checker_exit_code']==2 and 'SETUP_UNVERIFIED' in formal['stdout']
assert formal['source_sha256']==digest((R/'code/Orbit.lean').read_bytes())
peer=BASE/'agents/A066/runs/20261023T113807Z-account03-A066-semigroup-dissipation'
incoming=json.loads((peer/'CLAIMS.json').read_text(encoding='utf-8'))[0]
assert incoming['claim_id']=='A066-NONFLAT-DATA-RELEASE-AND-SOURCE-PAYMENT' and incoming['version']==4
assert digest(incoming['exact_statement'].encode('utf-8'))==incoming['statement_sha256']=='3d140b42344fef85bd4ed28b9a5fe58a976d1b24e505ec59be908102d235c802'
source_paths=[protocol,BASE/'BOARD.md',BASE/'claude/B17/STREAM_NOTES.md',peer/'DERIVATION.md',peer/'CLAIMS.json',
 BASE/'agents/A096/runs/20261023T115236Z-account03-A096-live-gap-ledger/DERIVATION.md',
 BASE/'agents/A096/runs/20261023T115236Z-account03-A096-live-gap-ledger/CLAIMS.json',
 A/'runs/20261023T070041Z-account03-A083-formal-core/PROOF.md',
 A/'runs/20261014T023633Z-account05-A083-formal-core/code/occupancy_check.py']
source_receipts=[]
for p in source_paths:
 b=p.read_bytes();b.decode('utf-8-sig');source_receipts.append({'path':str(p),'bytes':len(b),'sha256':digest(b)})
save('out/SOURCE_RECEIPTS.json',{'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sources':source_receipts,'scope':'Current bytes pinned; BOARD is a final readback snapshot. Earlier campaign/paper reads remain baseline provenance, not a fresh manuscript audit.'})
incoming['review_records'].append({'reviewer':'A083','disposition':'INDEPENDENTLY_RECONSTRUCTED_HOLDS_AT_STATED_SCOPE_UNCHANGED','time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_statement_sha256':incoming['statement_sha256'],'source_file_sha256':digest((peer/'DERIVATION.md').read_bytes()),'source':str(R/'REVIEW.md'),'method':'Independent direct Walsh and edge enumeration; full source/ghost/physical projection/current-reference/original-bank reconstruction; all stated analytic/group/heat and orbit-defect clauses reconstructed.132 admissible fixtures,16625 exact checks.','substantive_repair':False,'limits':'Necessity only for the supplied skewed reference and fixed two-invoice/old-booking policy. No arbitrary-core supplier, matched-nullspace payment, general T_G bound or Lean proof accepted.'})
incoming['status']='INDEPENDENTLY_RECONSTRUCTED_HOLDS_AT_STATED_SCOPE'
statement='On frequency labels Fin8 identified with F2^3 by binary expansion, let A have columns(2,4,7), equivalently table(0,2,4,6,7,5,3,1). For every label s, A^4(s)=s; for all a,b, A(a XOR b)=A(a) XOR A(b). It fixes0 and cycles1->2->4->7->1. Thus A is an invertible physical linear frequency map with the displayed four-cycle. The exact certificate exhausts all8 labels and64 XOR pairs. The supplied Lean target A083Stage20.structure_certificate is NOT kernel-verified: checker setup was refused for stale compute telemetry.'
finite={'claim_id':'A083-C4-PHYSICAL-ORBIT-CORE','version':1,'exact_statement':statement,
 'hypotheses':['Fin8 binary labels; XOR over F2^3','the explicit table and matrix columns as specified'],
 'statement_sha256':digest(statement.encode('utf-8')),'contributors':['A083; concrete map supplied by A066'],
 'proof_source':{'files':[str(R/'code/check.py'),str(R/'out/RESULT.json'),str(R/'REVIEW.md')],'formal_source':str(R/'code/Orbit.lean'),'formal_status':'SETUP_UNVERIFIED_STALE_TELEMETRY','formal_receipt':str(R/'out/LEAN_RESULT.json')},
 'proof_dependencies':['finite exhaustive evaluation of the explicit binary-linear map, independent of the incoming checker'],
 'review_records':[],'status':'EXACT_FINITE_CERTIFICATE_LEAN_UNVERIFIED','supersedes':[],'refutes':[],
 'first_unproved_line':None,'next_consumers':['A066','A096','A097','A092','B17']}
claims=[incoming,finite]
for c in claims:assert set(c)==set(pr['required_per_run']['claim_fields'])
save('CLAIMS.json',claims)
next_action='A097/A031 specify a useful mandatory reference class and actual residual source; test its compatible orbit conversion by T_G-R_G<=the SAME unused original bank after all old invoices/full terminals, or prove that conversion deferrable. A066/A096/A094 review. Do not search further optional matched-nullspace resets without a necessity premise.'
progress={'protocol_revision':pr['revision'],'run_id':R.name,'stream':'B17','packet_id':'A083',
 'gap_id':'C024-PHYSICAL-REFERENCE-OWNED-RESERVE-COMPATIBILITY','attempt_id':'A083-stage20-necessary-C4-review',
 'method':'Consume A066 v4 actual necessary supplied-source isospectral conversion; independent analytic reconstruction, exact Walsh/edge/current-reference/ghost/ancestor-account checks; minimal C4 formal target attempted without bypassing stale telemetry guard.',
 'mathematical_delta':'A066 v4 independently HOLDS unchanged: real paid t prefix, fixed original quota and old debit; C4 refund c-2 pays prescribed x with all full terminals, SAME final3K/2-9/4>=15/4. Necessity is policy-relative, current q is deliberately skewed; arbitrary-core pricing and general noninvariance defect remain open. Finite C4 structure exactly checked; Lean unverified.',
 'deliverable_status':'SAVED_LOCAL_SCHEMA_AND_HASH_VALIDATED','mathematical_status':'INCOMING_SUPPLIED_THEOREM_INDEPENDENTLY_ACCEPTED_FULL_FEI_OPEN',
 'claim_versions_used':['A066-NONFLAT-DATA-RELEASE-AND-SOURCE-PAYMENT@4','A096-ISOSPECTRAL-TARGET-GEOMETRIC-ACCOUNT@1 contextual, not a proof premise'],
 'claims_created_or_changed':['A066-NONFLAT-DATA-RELEASE-AND-SOURCE-PAYMENT@4 independent review appended, statement unchanged','A083-C4-PHYSICAL-ORBIT-CORE@1 exact finite certificate only'],
 'source_artifacts':[str(R/'REVIEW.md'),str(R/'out/RESULT.json'),str(R/'out/FIRST_FAILURE.json'),str(R/'out/LEAN_RESULT.json'),str(R/'out/SOURCE_RECEIPTS.json')],
 'next_consumers':['A066','A096','A097','A031','A094','B17','B20'],
 'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Kernel formal check SETUP_UNVERIFIED: telemetry stale despite fresh memok0; no compiler or axiom acceptance inferred.','Arbitrary-core influence-priced source and necessary compatible noninvariant conversion payment remain open.','Current q is not exact-matched P; refund is prepaid source mismatch, not creation of zero-energy credit.','Brain self-care degraded/unverified: personal model99.2h,state-of-mind83.8h,latest dream34.5h stale at wake; excluded as proof premises.','Supervisor mirror and downstream adoption unverified.'],
 'packet_ids':['A083']}
assert set(progress)==set(x.split(' (')[0] for x in pr['required_per_run']['progress_fields'])
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
contents=[
 'Independently review A066-NONFLAT-DATA-RELEASE-AND-SOURCE-PAYMENT@4 and check its small decisive C4 physical-map core. For EVERY supplied finite Boolean core g, integerK>=4 and fixed normalized full Qg with Cg=CE(Pg,Qg)<=K I(g), the theorem concerns F=t*x*Maj3*g, its declared skewed original reference, fixed original quota and old debit. All quantities are bits; BOTH t branches and BOTH x outcomes, ghosts and complete terminal CE remain. The theorem independently HOLDS unchanged at this scope. No arbitrary-core supplier or full FEI resolution is claimed.',
 'Read BOARD snapshot12:27UTC, unchanged B17 STREAM_NOTES v2, own stage19 STATUS, execution-v2 protocol, A066 run20261023T113807Z DERIVATION/CLAIMS and A096 run20261023T115236Z DERIVATION/CLAIMS. Own earlier atanh helper is reused read-only with bytecode disabled. B17 scalar assignment already closed in earlier stages, so dispatch consumes the new useful source-payment dependency. out/SOURCE_RECEIPTS.json pins the actual source bytes and declared statement hash. Campaign/manuscript baseline remains earlier-stage provenance, not newly audited literature. This session ran its required wake and reported degraded personal/dream notes; those are not proof premises.',
 'REVIEW.md reconstructs the full theorem: Maj3 spectrum is uniform on{1,2,4,7}, I=3/2; the explicit XOR-linear C4 map cycles those labels. Original CE=Cg+c, c=9K/4-log2(1-3*2^(-3K))/4. With A=K(Ig+7/2) and permanent tau=K Ig-Cg+1/4, actual t invoiceK leaves S_t=5K/2-c-1/4>0. Literal x completion would leave3K/2-c-1/4<0. CURRENT reference orbit averaging first refunds c-2, then x leaves3K/2-9/4>=15/4. The exact equality2K+(Cg+2)+tau+S_final=A retains all old owners/terminals; there is no overdraft or renewed quota. The necessity claim is ONLY for this prescribed policy and original skewed profile. Generic orbit DeltaCE=-R_G+T_G and zero-boundary heat clauses also reconstruct. FIRST UNSUPPORTED UNIVERSAL LINE: obtain a useful mandatory compatible reference class and pay its actual T_G-R_G from unused original surplus, or price the arbitrary-core initial source. Matched-nullspace conversions are not funded by this nonmatched-source example.',
 f'Frozen out/FROZEN_SPEC.json precedes the initial check and same-domain correction: all16 labeled2bit cores plus8 named3bit cores, K4/5/8, matched/ghost references,144 proposed fixtures. Twelve constant-core ghost references violate CE<=K I and are explicitly excluded;132 admissible fixtures PASS16625 assertions in{res["seconds"]:.6f}s (<60s). Arithmetic is exact Fraction/prime-log with proved atanh bounds; independent direct Walsh/physical edges and all four signed branches; Python memory estimate<100MB. Command python -B -X utf8 {R}/code/check.py. First run FAIL at assertion80: local logs aliased a cached factor dictionary. out/FAILED_check_v1.py and FIRST_FAILURE.json preserve it; copying the mapping fixed the checker, with mathematical domain unchanged. Fresh memok passed twice. code/formal.py then received checker exit2 SETUP_UNVERIFIED for stale compute telemetry. out/LEAN_RESULT.json pins source/target/hash. NO kernel theorem, transitive axiom result or Lean success is claimed; no guard was bypassed.',
 'A066 v4 is independently accepted with no mathematical repair or contributor conflict. Its original statement SHA256 matches3d140b42344fef85bd4ed28b9a5fe58a976d1b24e505ec59be908102d235c802. The proof uses only the explicit supplied reference premise, disjoint spectral tensor identities, finite symmetry/convexity and exact ancestor algebra. The C4 finite certificate checks8 labels/64 XOR pairs; the Lean draft remains unverified. A096 geometric compression is context only and its normalizer is not dropped. No independent acceptance of that entire A096 claim is asserted. This stage clears the concrete invariant isospectral handoff in our prior NEXT, without transferring its prepaid source refund to arbitrary matched histories.',
 next_action+' The shortest next step is to identify a required compatible handoff and its real payer, rather than create another optional conversion or extend an already paid invariant class. The finite C4 formal target may be retried only after telemetry admission is genuinely healthy; the current mathematics does not depend on that retry.',
 'Four exact-schema protocol files, REVIEW.md, the frozen spec, corrected and failed checker sources, exact PASS, diagnostic, admission and formal-refusal records are saved. out/ARTIFACT_RECEIPTS.json hashes all other run files; finalizer validates schema keysets, peer statement/source binding, compatibility equality and20MB ceiling. Rolling STATUS/WORKLOG/LEARNED updated. Local durable save is verified; supervisor mirror and downstream use are unverified. No other work was stopped and no research job is left running. Brain self-care remains degraded/unverified: stale personal model/state-of-mind/latest dream affect personal-context and consolidation reliability; no affected note supports the proof.'
]
report='\n\n'.join('# '+h+'\n\n'+t for h,t in zip(pr['required_per_run']['report_fields'],contents))
report+='\n\nUniversal bridge: C024 and C019 gain an independent reconstruction of a necessary policy-relative isospectral source handoff: SAME original account after a genuine paid prefix and old debit retains at least15/4, with complete arbitrary supplied-core and terminal costs. The finite physical C4 core is exactly certified; kernel checking remains unverified. This improves no universal FEI constant and does not price an arbitrary initial source or general noninvariant defect. NEXT asks A097/A031 for the actual mandatory compatible class and prices T_G-R_G from its unused original owner, because this identifies the missing universal transport payment instead of adding another isolated favorable family.\n'
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A083 stage20 saved: A066 v4 necessary policy-relative isospectral C4 payment independently HOLDS, SAME old account >=15/4;132 fixtures/16625 exact checks PASS; cache bug preserved/fixed;Lean setup HELD stale telemetry;FEI OPEN.\nNEXT: A097/A031 specify mandatory compatible reference class; pay noninvariant T_G-R_G from SAME unused original source after old bills/full terminals or prove deferrable; A066/A096/A094 review.\n',encoding='utf-8')
stamp='2026-10-23 stage20 '+R.name
for name,text in {
 'WORKLOG.md':f'{stamp}: Consumed A066 v4 actual invariant isospectral handoff. Independently reconstructed source/orbit/heat/full-terminal/original-bank proof unchanged, exact final>=15/4. Initial checkerFAIL80 was cache-dictionary alias in local logs; failed source/diagnostic retained and copy fixed it. Same frozen domainPASS132 admissible/144 proposed,16625 assertions,{res["seconds"]:.6f}s. Fresh memok0 twice; formal checker SETUP_UNVERIFIED stale telemetry, no Lean pass. No governor restart or other process stop. NEXT mandatory compatible class and actual noninvariant defect payer; full FEI open.',
 'LEARNED.md':f'{stamp}: A066 v4 holds at SUPPLIED source scope, necessity relative to fixed K invoices and old tau. F=t*x*Maj3*g, original skewed Maj reference cost c in(9K/4,9K/4+1/4). After real t invoice, literal x overdraws; C4 CURRENT-reference averaging refunds c-2 BEFORE x, preserving exact Qg and final3K/2-9/4>=15/4. This is prepaid mismatch, not matched-nullspace energy. Map table0,2,4,6,7,5,3,1 is XOR-linear/order4; generic orbit cost=-R_G+T_G, so noninvariance still needs a payer. Copy cached prime-factor dictionaries before subtracting denominator exponents: aliasing factors(4096) corrupted repeated log terms and was caught by strict c bound. No helper file was changed. Kernel proof held for stale telemetry despite memok0; draft is not formal verification.'
}.items():
 p=A/name;s=p.read_text(encoding='utf-8') if p.exists() else ''
 if stamp not in s:p.write_text(s+'\n\n'+text+'\n',encoding='utf-8')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (R/'REPORT.md').read_text(encoding='utf-8').rstrip().splitlines()[-1].startswith('Universal bridge:')
receipts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
  b=p.read_bytes();assert len(b)<20_000_000;receipts.append({'path':str(p.relative_to(R)),'bytes':len(b),'sha256':digest(b)})
save('out/ARTIFACT_RECEIPTS.json',{'status':'PASS','artifacts':receipts,'mirror':'UNVERIFIED','kernel':'UNVERIFIED_STALE_TELEMETRY'})
print(json.dumps({'status':'PASS','protocol_files':4,'claims':len(claims),'artifacts':len(receipts),'incoming_review':'A066v4 HOLDS unchanged','formal':'UNVERIFIED','full_FEI':'OPEN'}))
