from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];HOME=ROOT.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=read(Path(r'math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
results={f:read(ROOT/'out'/f) for f in ['pair_validation.json','graph_validation.json','independent.json','structural.json']}
assert all(r['status']=='PASS' for r in results.values())
total=sum(r.get('exact_assertions',r.get('assertions',0)) for r in results.values())
write(ROOT/'out/RESULTS.json',{'status':'PASS','nonpilot_exact_assertions':total,'runs':results,'no_Lean_certificate':True,'independent_external_review':'PENDING','scope':'analytic exterior theorem; stopped assembly conditional on named internal local inputs'})
sources=[]
shared=Path(r'~/brain_workers/FEI100_20261011')
for agent,run in [('A059','20261023T034026Z-fleet03-A059-decomposition-depth'),('A060','20261023T042148Z-fleet03-A060-composition-sharpness'),('A091','20261023T053740Z-fleet03-A091-composition-referee')]:
 for name in ['PROOF.md','CLAIMS.json']:
  p=shared/'agents'/agent/'runs'/run/name;sources.append({'path':str(p),'sha256':sha(p),'scope':'read current proof and source claim version; only scoped local acceptance imported'})
for p in [HOME/'STATUS.md',ROOT.parent/'20261023T015026Z-fleet03-A057-coherent-restriction-remainder/PROOF.md',shared/'claude/B12/STREAM_NOTES.md']:
 sources.append({'path':str(p),'sha256':sha(p),'scope':'stage input or previous proof; rolling STATUS hash is pre-finalization'})
write(ROOT/'out/SOURCES.json',sources)
statement='For any finite uniform Boolean exterior b with a fixed partition into pairs, assume every two-bit slice of each pair has sign product -1 and b(0)=b(e_i)=+1 for every i. For F=b-C+Cg, C the zero-point mask and g an independent actual Boolean fallback, allocate ORIGINAL exterior ticket Eroot=4 I_ext(F). Each untouched pair retains4 times its ACTUAL pair influence; after its first queried bit allocate2 in EACH actual child for the remaining partner; after its second allocate0. Under arbitrary adaptive exterior queries and intervening internal queries with their own valid payments, this SAME account pays all exterior entropy decrements; at each exterior split the original fine U and internal Q are harmonic and the CURRENT fine R and density reserve S=phi(t)Var(g) release respectively t*sum p_j Var(h_j) and t Var(g). Both full terminals and all previous debits remain. Conditional on the named private-priority controller and signed-DATA inputs, the source W0=g,W1=F with no exterior before X satisfies Hroot<=P_root+E[Hleaf-P_leaf], P=U+R+Q+S+E, with original internal rates21/5 and source6 whenever c<=Eb<=1/4,m>=4. This includes all disjoint paired bent gates, interacting homogeneous quadratics with a fixed perfect matching meeting that source condition, and b=(-1)^(sum x_j y_j+P0(x)) for arbitrary P0 with P0(0)=P0(e_j)=0,k>=2. No generic root core/representation price or full FEI is claimed.'
claim={
 'claim_id':'A057-ORIGINAL-PAIR-CAPACITY-TRANSFER','version':1,'exact_statement':statement,
 'hypotheses':['Uniform independent exterior and internal cubes; actual Boolean signs; bits entropy.','Fixed original physical pair partition; every outside-fixed pair slice sign product -1; b positive at0 and all exterior unit vectors.','No exterior queries before source X; optional source exposure at arbitrary internal frontier.','For the combined source6 theorem require c<=Eb<=1/4 and m>=4; general exterior theorem has no bias hypothesis.','Combined internal stopping assembly additionally imports original fine private-priority/controller and signed-DATA local payments at their actual hypotheses.'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A057'],
 'proof_source':{'main':'PAIR_PROOF.md Sections1-4','generalization':['MATCHED_QUADRATIC.md','STRUCTURAL_LEMMA.md'],'validation':['out/pair_validation.json','out/graph_validation.json','out/independent.json','out/structural.json']},
 'proof_dependencies':[{'claim_version':'A059-SINGLETON-DENSITY-VARIANCE-TRANSFER@1','scope':'current density singleton tax, variance telescope, source allocation; A060/A091 accept only these local scopes'},{'claim_version':'A059-INTERRUPTED-PRIORITY-STOPPING-PAYMENT@2','scope':'private-controller erasure baseline; imported, not independently re-certified here'},{'claim_version':'A059-INTERLEAVED-BIASED-STOPPING-RESERVE@1','scope':'signed fine-DATA at arbitrary exterior wrappers; explicit conditional input'},{'claim_version':'A059-FREQUENT-EXTERIOR-FALLBACK-PAYMENT@1','scope':'hidden-source internal payment; scoped local review only'},'physical block-influence conservation; Boolean split decrement<=2'],
 'review_records':[{'reviewer':'A057','kind':'author analytic reconstruction plus separate direct-character implementation; NOT external independent acceptance','result':f'{total} nonpilot exact assertions PASS; all-policy conclusion by proof, not enumeration of policies'}],
 'status':'SELF_CONTAINED_EXTERIOR_PROOF_PENDING_REVIEW; MIXED_ASSEMBLY_CONDITIONAL','supersedes':[],
 'refutes':['UNCLAIMED_LOCAL_E4_TIMES_REMAINING_PARTNER_INFLUENCE_EXTENSION; see actual g=-1 partner controls and analytic ratio>=m-4'],
 'first_unproved_line':'For arbitrary exterior b, fund the first-query child pair/block allocations without the hereditary physical influence floor, from the SAME unused owner; arbitrary initial core/representation entropy and full FEI remain open.',
 'next_consumers':['A059','A060','A091','A087','A090','B12','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields']);write(ROOT/'CLAIMS.json',[claim])
progress={
 'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B12','packet_id':'A057','gap_id':'G-R-SELECT/ORIGINAL-EXTERIOR-PAIR-CONVERSION','attempt_id':'A057-stage19-original-pair-v1',
 'method':'Retain original physical pair capacity through its first query; reserve2 for its actual partner; current mean-variance density telescope; independent direct-character audit',
 'mathematical_delta':'All exterior/internal mixed continuations after source exposure paid from original exterior4I and unchanged source6/internal21/5; structural pair-slice lemma includes interacting quadratic and arbitrary-degree phase families. Canonical remaining-influence shortcut fails at actual isolated partner.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'EXTERIOR_ANALYTIC_PROOF_PENDING_REVIEW; MIXED_STOPPING_ASSEMBLY_CONDITIONAL; FULL_FEI_OPEN',
 'claim_versions_used':['A059-SINGLETON-DENSITY-VARIANCE-TRANSFER@1','A059-INTERRUPTED-PRIORITY-STOPPING-PAYMENT@2','A059-INTERLEAVED-BIASED-STOPPING-RESERVE@1','A059-FREQUENT-EXTERIOR-FALLBACK-PAYMENT@1','A060-SHARP-SINGLETON-VARIANCE-AND-EXTERIOR-SOURCE6-OBSTRUCTION@1','A091 stage19 scoped independent local reconstruction'],
 'claims_created_or_changed':['A057-ORIGINAL-PAIR-CAPACITY-TRANSFER@1'],
 'source_artifacts':['PAIR_PROOF.md','STRUCTURAL_LEMMA.md','MATCHED_QUADRATIC.md','PROOF.md','SPEC.json','PAIR_SPEC.json','GRAPH_SPEC.json','REPRO_SPEC.json','STRUCTURAL_SPEC.json','out/RESULTS.json','out/SOURCES.json','out/EXECUTION_NOTES.json'],
 'next_consumers':claim['next_consumers'],'next_action':'A091/A087 independently reconstruct original pair conversion and current density/fine-profile changes after actual internal debit; next generalize to a block lacking hereditary pair influence floor without renewed account or assumed initial entropy price.',
 'stagnant_substantive_attempts':0,
 'blockers':['external independent review pending','old internal controller/DATA dependency chain is explicit conditional input','universal initial core/representation price and non-pair block selection unpaid','supervisor mirror verification unavailable; no git used','brain self-care degraded/unverified: owner-model92.1h and state-of-mind76.7h stale; affected notes not used for task direction'],
 'packet_ids':['A057']}
fields=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(fields);write(ROOT/'PROGRESS.json',progress);write(ROOT/'PACKET_DELTA.json',progress)
notes={'pilot':'v1 intact-only pilot9036 assertions passed; v2 first launch retained known-false v1 D<=4d guard and failed there before its pair accounting check. Removed exactly that obsolete guard, retained partner negative controls, reran entire frozen v2 pilot/full domain. No pair-payment assertion failure.',
 'execution':'One anchor-edit command was blocked by acknowledgement hook; acknowledged and switched to a checked UTF-8 derivation file after a PowerShell quoting error. All seven anchors and generated Python compilation checked. No external files mutated by the rejected commands.',
 'resources':'Every mathematical helper frozen below100MB estimate, actual compute under180s; no >300MB job, no GPU, no detached job, no Lean compiler, no resource shedding.',
 'review_cap':'This is a targeted completion/repair of the existing stage18 exterior-ticket gap, not a new broad full-FEI candidate. One narrowly scoped conditional extension recorded.',
 'failed_shortcut':'Canonical E4-only partner extension fails at all tested m4,6,8,10,12; analytic ratio>=m-4 is unbounded. Pair account preserves first-query capacity instead of renewing current influence.'}
write(ROOT/'out/EXECUTION_NOTES.json',notes)
report=f'''# A057 stage19: original exterior pair capacity

## exact target, quantifiers, hypotheses and units

Price EVERY finite adaptive exterior/internal continuation after the optional source X exposure, including a first exterior query after nonzero internal debit, from the SAME diminished source, variance, fine and ORIGINAL exterior accounts. Entropy is bits. Self-contained exterior hypothesis: fixed physical pair partition, every outside-fixed pair slice has sign product-1, and b(0)=b(e_i)=+1. Combined source6 additionally assumes m>=4 and c<=Eb<=1/4. Internal private-priority/controller/DATA inputs remain explicit. Full FEI is OPEN.

## sources actually read, revisions and theorem locators

Current BOARD.md (06:06 UTC), B12 STREAM_NOTES v2, own stage18 STATUS/PROOF and protocol2026-10-11-execution-v2. A059 run20261023T034026Z PROOF Sections1-4 supplies NEW singleton-density/variance mechanism. A060 run20261023T042148Z Sections1-6 and A091 run20261023T053740Z Sections1-5 reconstruct its LOCAL transfer/variance/source budget and refute source6-only exterior funding. Their scoped review does not certify the older internal assembly chain. Exact source hashes: out/SOURCES.json. Older campaign/paper background was read in prior stages; this stage makes no new literature claim. Direct brain recall returned low-separation old FEI warnings, not a new mathematical dependency; stale owner/state notes were not used.

## complete derivation or exact first unsupported line

PAIR_PROOF.md is the main complete derivation. Allocate exterior4I_ext at the ORIGINAL ancestor. An untouched hereditary pair has actual total influence>=1, so its incoming capacity>=4. Its first query costs<=2 and allocates2 in EACH full child for the remaining physical partner. Its second costs<=2 and closes that same pair. Other untouched influences are harmonic; open2 accounts are constant through all other queries. At an exterior point-mask split t becomes2t or0; exact changes are drop U=drop Q=0, drop R=t*Vbar and drop S=t*Var(g), where S=phi(t)Var(g). This is the CURRENT diminished logarithmic reserve, not a renewed root allowance. All local edges telescope with all full H-P terminals. Source6 and internal21/5 retain their old scopes and old debits.

MATCHED_QUADRATIC.md proves arbitrary extra quadratic edges preserve the matched-pair floor. STRUCTURAL_LEMMA.md proves the actual physical slice criterion and arbitrary-degree family (-1)^(sum x_j*y_j+P(x)), P(0)=P(e_j)=0, with EXACT mean2^-k, so source6 is still valid. No flat-spectrum assumption is needed for the exterior lemma. The finite graph checks do NOT claim source6 for graphs of unsuitable bias.

Canonical4 times current remaining influence is FALSE at the isolated partner: actual g=-1 gives D/d>=m-4 after a zero outcome, and all five tested m4..12 have strict positive deficits. The new account pays from capacity reserved at the first bit. This diagnoses a LOCAL shortcut; it does not refute full original accounts or FEI. The first unsupported universal line is funding an analogous first-query block conversion when no hereditary pair influence floor is available, together with the arbitrary root core/representation price. The mixed stopping statement is conditional on the named older internal local inputs, rather than independently certified here.

## executed validation with domain, arithmetic, commands and outputs

Frozen SPEC/PAIR_SPEC/GRAPH_SPEC/REPRO_SPEC/STRUCTURAL_SPEC precede their jobs. Commands are python -X utf8 code/check_pair.py, code/check_graph.py, code/independent_repro.py --full, code/check_structural.py from this run (pilot flags saved separately). Integer Walsh and Fraction prime-log expressions use36-term rigorous atanh bounds; the separate reproduction uses DIRECT character sums, separate factorization and48-term enclosures. Nonpilot checks total **{total} exact assertions PASS**.

Pair main:5832 states,72 source cylinders,3888 internal and7776 exterior edges,338 positive internal-debit edges. Graph main:16 actual matched quadratic graphs,20736 states,27648 exterior edges. Separate direct reproduction includes972 exposed states and a complete mixed physical tree A,X,z0,y,z1,z2,z3 with positive old internal debits, keeping X=0 siblings. Structural check exhausts16 six-bit phases,768 physical pair slices and1024 direct Fourier amplitudes. These finite domains are evidence; the all-dimensional/all-policy quantifiers follow from the written local-edge proof. Detailed counts and measured compute runtimes are in out/RESULTS.json. Pilots are excluded from the reported total. No Lean certificate or independent external acceptance is claimed. The obsolete canonical guard failure and quoting correction are recorded in out/EXECUTION_NOTES.json.

## proof dependencies and changed downstream conclusions

Use A059-SINGLETON-DENSITY-VARIANCE-TRANSFER@1 for CURRENT singleton/variance accounting, replacing the larger stage18 influence-surrogate bill. Stage18's source-only surrogate obstruction remains correct; the new sufficient tax is smaller, as A059/A060/A091 explicitly explain. Self-contained new pair conversion requires only Boolean D<=2 and harmonic physical influence. Internal erasure baseline and signed-DATA payment remain explicit local imports, so older assembly review is not silently upgraded. This completes the previously unpaid EXTERIOR continuation at fixed original rate4 in the stated geometry, including interactions and partners. It neither pays arbitrary inherited core entropy nor proves FEI.

## one next mathematical action and independent reviewer

A091/A087 should reconstruct the same-owner pair transaction, changed current fine/variance profiles and the mixed positive-debit tree; A060 can challenge the isolated-partner ownership distinction. Then replace the hereditary pair floor by an influence-paid block admission for a genuine gate outside this slice criterion, preserving original unused funds, old bookings and BOTH full terminal bills. Repeating additional matched-pair examples is not the next mathematical action.

## actual persistence receipts or precise save blocker

Required JSON schemas, statement hash, identical PACKET_DELTA and all local artifact hashes are checked by code/finalize.py; out/PERSISTENCE.json records the readback. Rolling STATUS is exactly two lines; WORKLOG and LEARNED updated. Every file is under20MB; no big artifact or search beyond the frozen dimensions. Source trees remain read-only. No git or external messages used; supervisor mirroring/adoption is NOT_VERIFIED. Checklist closure receipt is saved separately when available. Brain self-care remains degraded/unverified because owner-model92.1h and state-of-mind76.7h notes were stale at wake; those notes were not task authority.

Universal bridge: C019 moves from internal-only stopping to ALL mixed exterior/internal continuations after source exposure under a physical hereditary-pair criterion, funded by ORIGINAL exterior4I plus unchanged source6/internal21/5 and SAME diminished fine/variance reserves. The exact t log(1/t) term survives every profile change; both full terminals and every old debit remain. What remains is arbitrary initial core/representation pricing, older internal dependency-chain review and a block admission beyond the pair influence floor. That admission is the shortest next route to full FEI because more examples within the proved hereditary-pair criterion would not address the missing universal payment.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert f'## {field}' in report
status='STATE: A057 stage19 original exterior4I pair conversion pays ALL mixed exterior/internal histories after source; structural criterion includes interacting/nonquadratic gates; '+str(total)+' exact checks PASS; assembly conditional; FEI OPEN.\nNEXT: A091/A087 audit SAME pair4->2->0 plus current U/R/variance; fund a genuine non-hereditary block conversion from original unused owner, both full terminals and old debits.\n'
(HOME/'STATUS.md').write_text(status,encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp} stage19 {ROOT.name}: original exterior pair capacity4I ->2 per open child ->0 pays ALL exterior/internal mixed policies after X, conditional on named internal inputs. Structural slice lemma covers matched quadratics and arbitrary-degree one-sided phases; source6 unchanged at stated bias. {total} exact nonpilot assertions PASS. Canonical remaining-influence partner shortcut fails; preserved analytic/finite controls. No external review or mirror claimed.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage19 durable: original pair allocation is NOT canonical current influence after first bit. Untouched actual pair influence>=1 funds4, first Boolean query<=2 reserves2 for BOTH full actual partner children, second query<=2 closes same owner. Other pair influences harmonic; open2 constant. At point-mask exposure, CURRENT phi(t)Var(g) releases t Var(g), fine R releases t Vbar, U/Q harmonic. Pair slice product-1 plus b positive at0 and unit vectors suffices without quadraticity. Family sum xj*yj+P(x), P0=P(ej)=0, has exact mean2^-k and arbitrary degree. Combined source6/internal21/5 ledger remains conditional on old internal inputs. Canonical partner rateK fails locally: g=-1 after first zero has D/d>=m-4. Root unused capacity, not a renewed rate at that partner, is the repair. Universal missing step: physical block admission without hereditary pair influence floor and arbitrary core/root price.\n')
assert len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20_000_000;files.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
write(ROOT/'out/PERSISTENCE.json',{'verified_at':stamp,'local_schemas':'PASS','statement_hash':'PASS','PACKET_DELTA_identical':read(ROOT/'PROGRESS.json')==read(ROOT/'PACKET_DELTA.json'),'files':files,'mirror':'NOT_VERIFIED; supervisor ownership','external_review':'PENDING','running_stage_jobs':'read execution receipts; no detached jobs launched'})
print(json.dumps({'status':'SAVED_AND_READBACK_VERIFIED','nonpilot_assertions':total,'files':len(files),'claim':claim['claim_id'],'external_review':'PENDING','full_FEI':'OPEN'}))
