from pathlib import Path
import json,hashlib,datetime
run=Path(__file__).resolve().parents[1]
home=run.parents[1]
prior=run.parent/'20261022T221625Z-fleet03-A024-biased-child-stability'
protocol_path=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def read(p):return p.read_text(encoding='utf-8')
def write(p,s):
 with p.open('w',encoding='utf-8',newline='\n') as f:f.write(s)
def js(p,v):write(p,json.dumps(v,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=json.loads(read(protocol_path))
validation=json.loads(read(run/'out/VALIDATION.json'))
activation=json.loads(read(run/'out/ACTIVATION.json'))
multi=json.loads(read(run/'out/MULTI.json'))
pilot=json.loads(read(run/'out/PILOT.json'))
assert all(x['status']=='PASS' for x in [validation,activation,multi,pilot])
assert validation['descriptions']==18032 and pilot['descriptions']==624
assert activation['ordered_pairs']==64 and activation['one_query_prefixes']==224
assert multi['fixture_triples']==7 and multi['one_query_prefixes']==44
assert validation['checker_sha256']==sha(run/'code/check_repair.py')
assert multi['checker_sha256']==sha(run/'code/multi.py')
assert validation['prior_helper_sha256']==sha(prior/'code/check.py')
statement=('Retains v3 with its original prescribed-tree hypotheses. Adds: every uniform Boolean quadratic phase with at most one vertex flipped, and every fair physical restriction thereof, has a complete continuation with selected coordinate erasure B_i<=5 Inf_i. This extends to products on disjoint blocks. For an OR of any finite number of disjoint such products (and its AND/sign variants), after any physical stopping prefix there exists a complete continuation with B_i<=14 Inf_i at each selected actual query; additional K14-bad odd-face debit is exactly zero. Both full terminal entropies are retained and resolved with remaining influence, giving H<=17I for the complete class and H<=8I for each product. Earlier prefix debits are unchanged and not asserted bounded. This does not transfer a prescribed-tree Phi to a reordered tree. Arbitrary edit sets, arbitrary outer gates, universal net-price selection and full FEI remain open.')
claim={
 'claim_id':'A024-MIXED-FACE-ORDER-OBSTRUCTION','version':4,'exact_statement':statement,
 'hypotheses':['Finite disjoint physical blocks, uniform remaining physical bits, entropy in bits',
 'Each inner product factor is a degree-at-most-two F2 phase with no edit or a single vertex edit, with arbitrary affine coefficients and constant sign',
 'Physical adaptive prefix fixes only queried bits; no conditioning on unobserved inner outputs',
 'Outer gate is OR or sign-equivalent AND; arbitrary fan-in but disjoint inner supports',
 'Old booked debits retained; no reuse of old fixed-tree potential after changing component policy',
 'Entropy corollaries use B05 localized reduction with c_JS=2/ln2; all-dimensional pivot/transport proof given separately from finite checks'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A024'],'proof_source':str(run/'DERIVATION.md'),
 'proof_dependencies':['A024-MIXED-FACE-ORDER-OBSTRUCTION@3 (scalar binary-activation transport; reconstructed in DERIVATION.md)',
 'B05-ODDFACE-LOCALIZED-REDUCTION@1 (entropy corollary only; inherited conditional acceptance)'],
 'review_records':[{'kind':'author exact enumeration','status':'PASS','source':'out/VALIDATION.json','scope':'18032 quadratic/edit descriptions, 293842 exact assertions; finite domain only'},
 {'kind':'author full physical activation replay','status':'PASS','source':'out/ACTIVATION.json','scope':'64 pairs,224 arbitrary one-query prefixes,2555 exact assertions'},
 {'kind':'author full multi-input physical replay','status':'PASS','source':'out/MULTI.json','scope':'7 triples,44 prefixes,2632 exact assertions'},
 {'kind':'formal verification','status':'NOT_ATTEMPTED_RESOURCE_FLOOR','scope':'Observed available memory2076MB below Lean launch floor5500MB; no compiler started'},
 {'kind':'independent review','status':'PENDING','reviewers':['A087','A094']}],
 'status':'AUTHOR_PROOF_REVIEW_PENDING','supersedes':['A024-MIXED-FACE-ORDER-OBSTRUCTION@3'],
 'refutes':[], 'first_unproved_line':'For a general edit set after the quadratic part vanishes, no point-defect spectral bound or universally good continuation has been established.',
 'next_consumers':['A021','A023','A025','A028','A029','A087','A094','B05','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
js(run/'CLAIMS.json',[claim])
next_action='Test and prove a hereditary repair for a two-point or affine-subspace edit with full actual-prefix debit retained; identify exactly when the affine residual ceases to have an influence-paid erasure bound. A087/A094 reconstruct v4 before adoption.'
progress={
 'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B05','packet_id':'A024',
 'gap_id':'G-R-SELECT','attempt_id':'A024-stage18-hereditary-quadratic-policy-repair',
 'method':'Balanced physical quadratic derivatives, exact point-defect Fourier spectrum, character-shift invariant erasure, scalar binary-activation transport and full both-terminal telescoping',
 'mathematical_delta':'Dimension-free hereditary good-query repair for arbitrary-width quadratic single-point-edited product blocks; after arbitrary physical prefixes, OR/AND of arbitrary finite fan-in has zero further K14-bad debit. Old debits and both terminal entropies retained; old fixed-tree Phi not transferred.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'AUTHOR_PROOF_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':['A024-MIXED-FACE-ORDER-OBSTRUCTION@3','B05-ODDFACE-LOCALIZED-REDUCTION@1'],
 'claims_created_or_changed':['A024-MIXED-FACE-ORDER-OBSTRUCTION@4'],
 'source_artifacts':['DERIVATION.md','AUDIT.md','FROZEN_SPEC.md','MULTI_SPEC.md','out/PILOT.json','out/VALIDATION.json','out/ACTIVATION.json','out/MULTI.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['General-edit affine residual and universal net mixed-credit selection remain open','Independent A087/A094 review pending','No formal proof certificate; low-memory launch floor respected','Supervisor remote copy and mirror unverified','Brain self-care degraded: stale owner-model and state-of-mind sources; personal-context freshness unverified'],
 'packet_ids':['A024']}
expected={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
js(run/'PROGRESS.json',progress);js(run/'PACKET_DELTA.json',progress)
sources=[protocol_path,Path(r'BOARD.md'),Path(r'claude\B05\STREAM_NOTES.md'),prior/'DERIVATION.md',prior/'CLAIMS.json',prior/'PROGRESS.json',prior/'code/check.py',prior/'REPORT.md',prior/'out/SOURCE_RECEIPTS.json']
js(run/'out/SOURCE_RECEIPTS.json',{'fresh_read_scope':'Protocol complete, current BOARD orientation, B05 notes, own STATUS and prior proof/helper/claim; no new full-paper review',
 'inherited_intake':str(prior/'out/SOURCE_RECEIPTS.json'),'files':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources]})
total=validation['exact_assertions']+activation['exact_assertions']+multi['exact_assertions']
js(run/'out/EXECUTION_NOTES.json',{'brain_selfcare':'DEGRADED_UNVERIFIED: owner model/state-of-mind stale; no claim that these were refreshed',
 'formal_status':'Not attempted: observed2076MB available versus5500MB Lean launch floor',
 'compiler_started':False,'mathematical_assertion_failures':0,'stopped_processes':[], 'left_running':[],
 'nonmathematical_incidents':['UTF8 acknowledgement read gate, then read succeeded with explicit UTF8','One rejected context patch, corrected without altering sources'],
 'local_only':True,'remote_copy_verified':False})
head=protocol['required_per_run']['report_fields']
parts=[
 'Repair the remaining physical query policy after ANY already observed prefix for quadratic phases with one edited vertex, their disjoint products, and OR/AND of finitely many such products. Bits; uniform untouched physical inputs; arbitrary module width and fan-in. Establish B<=5d within a product and B<=14d for actual outer-gate queries, zero additional K14-bad odd-face debit, and both-terminal resolution. This is an author proof pending review, not full FEI.',
 'Fresh: execution protocol revision '+protocol['revision']+'; BOARD orientation snapshot2026-10-23; B05 STREAM_NOTES v2 (A024 target and localized reduction); own STATUS; v3 DERIVATION and exact-check helper SHA256 '+sha(prior/'code/check.py')+'. Prior campaign/registry/paper intake is inherited through the preceding SOURCE_RECEIPTS and REPORT, not reread in full this stage. Exact source paths/hashes are in out/SOURCE_RECEIPTS.json. Theorem locator: DERIVATION sections1-3; source B05-ODDFACE-LOCALIZED-REDUCTION@1 is only needed for the entropy corollary.',
 'Complete all-dimensional author derivation: DERIVATION.md. A surviving quadratic edge supplies an exactly-half-influential unedited pivot, robust to one vertex edit; after the quadratic part vanishes, character translation and the exact point-defect spectrum give B<=5d(1-d). Tensorization and the v3 R<=9rd transport give actual B<=14d with no variance denominator. Grouping all other inner blocks pays arbitrary OR fan-in with the SAME constant. After any prefix the continuation adds zero bad debit; the exact entropy/influence telescopes retain both terminal functions. The old prescribed-tree potential is not reused after reordering. First unsupported universal line: replacing the one-point affine residual by an arbitrary edit event and assuming the same hereditary good-query bound. AUDIT.md reconstructs the critical steps and limits.',
 f'Frozen specs: FROZEN_SPEC.md and MULTI_SPEC.md, saved before their respective jobs. Commands: python -X utf8 code/check_repair.py --pilot; python -X utf8 code/check_repair.py; python -X utf8 code/check_repair.py --activation; python -X utf8 code/multi.py (from this run). Pilot624 descriptions/9166 assertions, {pilot["runtime_seconds"]:.3f}s. Full18032 descriptions/{validation["exact_assertions"]} assertions, {validation["runtime_seconds"]:.3f}s. Activation64 pairs/224 prefixes/{activation["exact_assertions"]} assertions, {activation["runtime_seconds"]:.3f}s. Multi-input7 triples/44 prefixes/{multi["exact_assertions"]} assertions, {multi["runtime_seconds"]:.3f}s. All PASS; full validation total{total} excluding pilot. Integer Walsh, rational influences, prime-log vectors and rigorously bounded rational atanh sign certificates. Independent author character-sum lane checks16 spectra. No floating-point sign inference; runtimes only are floating point. No independent review or formal certificate claimed. No jobs expected over300MB; no heavy search or automatic dimension increase.',
 'v4 extends the existing candidate rather than opening a new broad claim. Scalar transport is reconstructed from v3; B05 localization remains an inherited dependency for H<=17I (product H<=8I). New downstream conclusion: old tensor-selector module-width growth does not force future rare logarithms when the continuation policy may be repaired. This does not price the original bad prefix, prove Phi_root<=CI, or transfer Phi to a changed component tree. An arbitrary outer gate and general edit sets remain outside scope. Physical restrictions keep inputs uniform; changed output means induce biased outer inputs only. FEI+ uses the product input-variance numerator, with no output-variance numerator; deterministic children are contracted.',
 next_action+' This targets the exact affine-residual bottleneck left by the new repair, rather than enlarging width in an already settled single-point family. No messages sent to reviewers; adoption remains pending.',
 'Four protocol artifacts, derivation/audit/specs, executable checkers and exact outputs saved locally in this immutable run. code/finish.py validates field sets, source hashes, output counts and statement digest; out/FINAL_RECEIPT.json records readback hashes. Rolling STATUS/WORKLOG/LEARNED updated locally. No publication, independent acceptance, remote mirror verification, or full-FEI resolution claimed. All computation completed; no process stopped or left running. Brain self-care remains degraded/unverified: owner-model and state-of-mind freshness are affected; fresh task instructions govern this stage.'
]
report='# A024 stage18: hereditary physical-query repair\n\n'+'\n\n'.join('## '+h+'\n\n'+b for h,b in zip(head,parts))
report+='\n\n**Universal bridge**: This moves C019 stopping-tree payment and C024 history transfer on the growing-module obstruction: after an arbitrary physical prefix, all remaining bad-node credit is exactly zero at K14 for arbitrary-width quadratic one-point-edited product inputs and arbitrary OR fan-in. It retains the SAME already-booked prefix debit and both complete terminal entropies, without renewing credit or reusing a changed-tree Phi. The universal gap is a good continuation for general affine edit residuals and a bound for earlier bad debit; full FEI stays OPEN. Testing the first two-point/subspace residual is the shortest next route because it attacks the precise one-point-only step that blocks extending this policy mechanism to general Boolean functions.\n'
write(run/'REPORT.md',report)
write(home/'STATUS.md','STATE: A024 v4 saved: hereditary quadratic/one-point product repair; OR any fan-in continuation K14-good after arbitrary prefix; 299029 exact assertions PASS; author proof/review pending, FEI OPEN.\nNEXT: Extend affine-residual repair to two-point/subspace edits with SAME prefix debit and both terminals; A087/A094 reconstruct v4; no changed-tree Phi transfer.\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (home/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:
 f.write('\n'+stamp+' | Stage18 '+run.name+': proved hereditary K5 repair for quadratic one-point-edited factors and products; transported to K14 actual OR/AND any fan-in after arbitrary physical prefix, zero further bad debit. Full exact checks:18032 descriptions293842 assertions,64 activation pairs224 prefixes2555 assertions,7 triples44 prefixes2632 assertions; pilot624/9166. Corrected strict numerical relaxation at constants. No old-tree Phi transfer or old-debit payment claimed. Review pending; FEI open. No jobs left running.\n')
with (home/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:
 f.write('\n'+stamp+' | Hereditary physical policy: nonaffine quadratic phase has an incident-coordinate pivot d_base=1/2; one edited vertex changes d by at most2^(1-D), hence d>=1/4 forD>=3 and B<=4d. Affine fallback has u=2^(1-D), B=2u(1-u)+L(1-u,u)<=5d(1-d), since character multiplication complements or preserves d while preserving erasure. Product factors tensorize; disjoint OR fan-in groups all other inputs into an arbitrary second child, so the v3 R<=9rd bound gives K14 independently of width/fan-in and after any fair physical prefix. This adds zero future bad debit but does not forgive old debit or transfer prescribed-tree Phi after reordering. General edit sets in the affine fallback remain the unsupported universal step.\n')
# Actual readback verification; receipt excludes itself to avoid a recursive hash.
for file in ['CLAIMS.json','PROGRESS.json','PACKET_DELTA.json']:
 json.loads(read(run/file))
assert json.loads(read(run/'PROGRESS.json'))==json.loads(read(run/'PACKET_DELTA.json'))
assert hashlib.sha256(json.loads(read(run/'CLAIMS.json'))[0]['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
assert all('## '+h in read(run/'REPORT.md') for h in head)
files=sorted(p for p in run.rglob('*') if p.is_file() and p.name!='FINAL_RECEIPT.json')
assert all(p.stat().st_size<20*1024*1024 for p in files)
receipt={'status':'PASS_LOCAL_READBACK','time_utc':stamp,'files':[{'path':str(p.relative_to(run)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],
 'rolling_files':[{'path':str(home/n),'sha256':sha(home/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],
 'full_validation_assertions':total,'independent_review':'PENDING','full_fei':'OPEN','left_running':[]}
js(run/'out/FINAL_RECEIPT.json',receipt)
print(json.dumps({'status':receipt['status'],'run_files':len(files),'full_assertions':total,'review':'PENDING','full_fei':'OPEN','left_running':[]}))
