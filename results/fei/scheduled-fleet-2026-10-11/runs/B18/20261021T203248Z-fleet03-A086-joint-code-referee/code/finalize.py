from pathlib import Path
import json, hashlib, datetime as dt
BASE=Path(__file__).resolve().parents[1]
OWN=BASE.parents[1]
SOURCE=OWN.parent/'A095'/'runs'/'20261021T180853Z-fleet03-A095-restricted-result-extraction'
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
RUN=BASE.name
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,value): p.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=read(PROTOCOL); results=read(BASE/'out'/'EXACT_RESULTS.json')
assert results['status']=='PASS' and results['assertions']==2373
assert results['helper_sha256']==sha(BASE/'code'/'check.py')
claim=read(SOURCE/'CLAIMS.json')[0]
canonical=json.dumps({'exact_statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False)
assert hashlib.sha256(canonical.encode('utf-8')).hexdigest()==claim['statement_sha256']
write(BASE/'out'/'STATEMENT_HASH_CONVENTION.json',{'convention':'SHA256 UTF8 canonical JSON of exact_statement and hypotheses; sorted keys, compact separators, ensure_ascii=False','source':str(SOURCE/'code'/'finalize.py')+':29','verified':True,'initial_validator_correction':'Plain exact_statement hashing is not this source convention; the initial finalizer stopped before creating protocol artifacts.'})
assert sha(SOURCE/'DERIVATION.md')==claim['proof_source']['sha256']
stamp=dt.datetime.now(dt.timezone.utc).isoformat()
lean=read(BASE/'out'/'LEAN_RECEIPT.json') if (BASE/'out'/'LEAN_RECEIPT.json').is_file() else {'status':'UNAVAILABLE'}
assert lean['status']!='SOURCE_PREPARED_NOT_CHECKED', 'wait for the formal attempt to finish'
review={'reviewer':'A086/fleet03','reviewed_at':stamp,'verdict':'HOLDS_AT_FULL_NAMED_SCOPE_WITHOUT_REPAIR','reconstruction':str(BASE/'RECONSTRUCTION.md'),'validation':str(BASE/'out'/'EXACT_RESULTS.json'),'checks':2373,'independence':'Direct character sums and literal physical edges; no author checker imported; all-policy influence dynamic program and complete reference policies','substantive_repair_supplied':False,'rung':'independently reconstructed analytic proof with exact finite validation; Lean status applies only to named arithmetic lemma','formal_arithmetic_status':lean['status']}
claim['review_records'].append(review)
claim['status']='INDEPENDENTLY_RECONSTRUCTED_AT_STATED_SCOPE'
claim['first_unproved_line']=None
write(BASE/'CLAIMS.json',[claim])
sourcepaths=[SOURCE/x for x in ['REPORT.md','DERIVATION.md','CLAIMS.json','PROGRESS.json','code/finalize.py']]
(BASE/'out'/'INPUT_STATUS.md').write_bytes((OWN/'STATUS.md').read_bytes())
sourcepaths+=[PROTOCOL,BASE/'out'/'INPUT_STATUS.md',OWN.parent.parent/'BOARD.md',OWN.parent.parent/'claude'/'B18'/'STREAM_NOTES.md']
receipts=[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sourcepaths if p.is_file()]
write(BASE/'out'/'CRITICAL_SOURCE_RECEIPTS.json',receipts)
sourceprogress=read(SOURCE/'PROGRESS.json')
progress={
 'protocol_revision':protocol['revision'],'run_id':RUN,'stream':'B18','packet_id':'A086',
 'gap_id':sourceprogress.get('gap_id','G-J-COST'),'attempt_id':'A086-stage17-A095-signed-profile-independent-review',
 'method':'Independent analytic reconstruction plus exact direct-character/physical-edge reference audit',
 'mathematical_delta':'A095@1 independently HOLDS for all w>=4,m>=0 and ALL adaptive wide-block histories at SAME rate4, retaining complete references and surplus>3/256. Product-compatible true-zero-fiber terminal extension checked; arbitrary reference/reset bridge remains OPEN.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_SOURCE_PROOF_ACCEPTED_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':claim['claim_id'],'version':1,'statement_sha256':claim['statement_sha256']}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'independent review only; source statement unchanged'}],
 'source_artifacts':[str(p) for p in sourcepaths if p.is_file()],
 'next_consumers':['A095','A094','A096','A097','B20'],
 'next_action':'A095/A094/A097: after one width-two query, specify the fresh descendant reference and pay reset plus complementary full terminal from the SAME unused ancestor capacity, retaining all old debits.',
 'stagnant_substantive_attempts':0,
 'blockers':['Full FEI: arbitrary influence-priced incoming reference or prescribed useful fresh reset remains unpaid.','Supervisor copying, canonical adoption and remote mirror verification are unverified.'],
 'packet_ids':['A086']}
write(BASE/'PROGRESS.json',progress); write(BASE/'PACKET_DELTA.json',progress)

runtime=results['runtime_seconds']
formaltext=(f"The bounded core-only Lean attempt has status {lean['status']}. Its exact target is only A086_padding_bound: for each natural m, 16m+37<=37*2^m. out/LEAN_RECEIPT.json records the source and available compiler/axiom evidence. This does not formally certify the entropy theorem.")
report=f'''# A086: A095 signed-profile history theorem independently holds

## exact target, quantifiers, hypotheses and units

Review A095-UNBOUNDED-WIDTH-SIGNED-PROFILE-HISTORY@1 without changing its statement. For every w>=4,m>=0, use g=h_w h_2, padding m, the fresh fair-selector all-zero edit, and exactly the prescribed support-completed source-spectrum reference. Every finite adaptive tree querying only previously unqueried wide-block coordinates satisfies CE_root<1005/256, E I_leaf>=63/64 and4 E I_leaf-E CE_leaf>3/256. Entropy and CE are in bits; influence is literal uniform-cube physical influence. No selector, narrow-block, padding or independent-terminal query or descendant reset is admitted. Product-compatible zero-fiber transport is required for the untouched terminal statement.

## sources actually read, revisions and theorem locators

Execution protocol2026-10-11-execution-v2 was read completely. BOARD and B18 STREAM_NOTES v2, A086 STATUS/WORKLOG/LEARNED and the current A095 REPORT, CLAIMS and DERIVATION1–4 determine the continuation. The B18 initial A003/A007/A008/A012 targets were already covered in A086's older WORKLOG; this run consumes the newer A095 dependency requested by the saved NEXT and current board. A095's source statement hash is {claim['statement_sha256']}; its DERIVATION hash is {sha(SOURCE/'DERIVATION.md')}. The current campaign indices, plan, supplement and four paper-text exports receive byte/encoding and relevant-locator intake in out/INTAKE_RECEIPTS.json. They are background rather than imported new proof premises. Explicit cp1252 fallback follows UTF-8 rejection for affected source exports; no source bytes are rewritten. Recent A086 run directories063415Z,104515Z,133315Z contain only.final locally; absent prior reports are not claimed as reread proofs. No outside paper, novelty or literature claim is made.

## complete derivation or exact first unsupported line

RECONSTRUCTION.md gives the independent complete derivation. Direct signed tensor sums recover A=2+2b log2 b+(2-q)(2w-2) and B=-8log2 b+2^(w+3)w-8w+8. Both support-completion mass and root CE are normalized exactly. Elementary log inequalities and the padding induction give CE_root<1005/256 uniformly. A literal destroyed-edge count gives E I_leaf=1+wq-Pi_g+delta(m-w-1+t); the unique edited-path leaf contributes at least(w-t)q original wide influence. Thus E I_leaf>=1-delta>=63/64 for EVERY adaptive stopping tree. Complete CE release is B_query+JS+conditional KL-mean log2 Z>=0 with both positive normalizers and all true-zero reference fibers retained. Telescoping yields surplus>3/256 from the SAME original bank. Independent untouched terminal costs add in full under the explicit compatible extension. The atom indexing is literal Fourier-mask indexing; no duplicate code witness, sampler termination or decoding assumption is silently substituted for the reference proof.

Verdict HOLDS at the full named scope, without substantive repair. The first unsupported universal line is an influence-priced arbitrary complete incoming reference or payment of a specified useful fresh descendant reset plus the complementary full terminal from unused SAME ancestor capacity. The source theorem proves neither. Rung: independently reconstructed analytic proof with exact finite checks. {formaltext}

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes search. Run python -B -X utf8 code/check.py pilot, then code/check.py from this run. The original pilot passes552 assertions. The final independent helper passes2373 assertions in{runtime:.3f} seconds on(w,m)=(4,0),(4,1),(5,0), with no symmetry reduction or dimension escalation. All405 labelled partial wide assignments and every next wide physical query are checked; dynamic programming minimizes remaining influence over ALL adaptive stopping policies. Three complete reference policies per root include reverse order, outcome-dependent order and branch stopping. Direct character sums, Fraction physical edges/normalizers and18-term rational atanh logarithm intervals rounded outward to96 binary fractional bits provide exact certification. Both nonunit normalizers and true-zero fibers occur. Original and edited remaining influence are independently enumerated and their exact debit identity is checked. A constant terminal with true spectrum(1,0), reference(1/3,2/3) demonstrates why globally fair fallback does not preserve terminal factorization, while product-compatible extension does. This challenges a hypothesis rather than repairing the source theorem.

An intermediate full run reaches2038 assertions before Python's integer-to-string limit prevents serialization of huge interval fractions; out/REPRESENTATION_LIMIT_FAILURE.json preserves that incomplete result. Outward rounding changes the representation while preserving certified enclosures; the final PASS is authoritative. Pilot and failed-run counts are not added. Estimated verifier memory100MB; peak memory is unmeasured. No mathematical search exceeds55 seconds internally. The core-only formal attempt uses fresh memok admission, and the multi-GB Mathlib route is excluded by the packet cap. No heavy search, GPU, detached job or new worker is started.

## proof dependencies and changed downstream conclusions

The source claim version and hash are unchanged; the local claim copy adds A086's independent review. Generic posterior transport and the point-path edge identity are rederived, not assumed from missing prior reports. The all-dimensional parameter quantifiers are supplied by the analytic argument, not by three finite roots. No full-FEI constant improves. A095/A094/A096/A097 may now use this reviewed wide-block history scope; a width-two query, different reference or fresh reset requires another payment. No shared registry or other agent's output is edited.

## one next mathematical action and independent reviewer

Expose one untouched width-two coordinate on this SAME account after a nontrivial wide history; prescribe the intended new descendant reference, retain old debits and the other full terminal, and price the signed reset from genuinely unused original capacity. A095/A094/A097 are the next consumers; A094 is the independent reviewer for any new reset payment. Further conservative no-reset telescoping would repeat an already paid mechanism.

## actual persistence receipts or precise save blocker

The four exact-field protocol artifacts, complete reconstruction, frozen spec, independent verifier, finite outputs, failure archive, source receipts, formal attempt and local persistence/schema receipts are saved in this assigned run. STATUS has two lines, and WORKLOG/LEARNED receive dated entries. All files are below20MB. The required wake surfaced stale owner-context notes; those notes are not mathematical premises. Shell startup and tool-host delays dominated elapsed wall time; verifier runtime is reported separately. Checklist/wake/formal tool bookkeeping are the required maintenance exceptions; research outputs stay in A086. No git, mail, brain research write, trading access, source mutation or other-agent mutation is performed. Supervisor copying, remote mirrors and canonical adoption are unverified.

## Universal bridge

This stage moves C020 whole-set reference cost through C024 history transfer and C019 stopping payment by independently accepting the ALL-width, ALL-padding, ALL-adaptive-wide-history supplied-reference rate4 theorem with surplus>3/256, one original owner and complete terminal debt. It adds a checked review rather than another isolated class theorem; universal constant improvement is zero. What remains is a useful specified fresh reset or arbitrary incoming reference paid from the SAME unused ancestor account. NEXT attacks the first untouched narrow-coordinate exposure with complementary terminals retained because automatic no-reset transport is already closed and cannot supply the missing universal FEI payment.
'''
(BASE/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
(OWN/'STATUS.md').write_text('STATE: Stage17 COMPLETE_LOCAL: A095 all-width/all-padding/ALL adaptive wide-block history independently HOLDS at SAME rate4;2373 exact checks PASS; full FEI OPEN.\nNEXT: A095/A094/A097 price one untouched width-two query and prescribed fresh descendant reset from SAME unused ancestor bank, retaining old debits and both complete terminals.\n',encoding='utf-8',newline='\n')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:
 f.write(f'\n{stamp} {RUN}: Independently reconstructed A095@1 signed profile, complete root normalizer, all-policy edited-path debit and finite CE telescoping. HOLDS without repair;2373 exact checks PASS/{runtime:.3f}s. Serialization failure archived then fixed by outward dyadic output. Core formal status {lean["status"]}; main entropy theorem not Lean-certified. Fresh-reset/source payment remains OPEN.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:
 f.write(f'\n{stamp}: A095@1 independent HOLDS: prescribed h_w*h2 edit, all w>=4,m>=0, ALL adaptive wide-only trees, CEroot<1005/256, mean I>=63/64, SAME-bank surplus>3/256. The unique edited all-zero path pays every lost wide edge; untouched h2 retains influence1. On independent-terminal true-zero fibers use product-compatible core posteriors; globally fair fallback can break terminal factorization (constant terminal P=(1,0), R=(1/3,2/3)). This is a scoped source/reference theorem, not an arbitrary reset payment.\n')

expected=set(protocol['required_per_run']['progress_fields']); expected.discard('packet_ids (one primary ID, for compatibility)'); expected.add('packet_ids')
assert set(progress)==expected
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert read(BASE/'PROGRESS.json')==read(BASE/'PACKET_DELTA.json')
assert len((OWN/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
write(BASE/'out'/'SCHEMA_VALIDATION.json',{'status':'PASS','claim_fields_exact':True,'progress_fields_exact':True,'delta_identical':True,'status_two_lines':True,'source_statement_and_proof_hash_verified':True})
manifest=[{'path':str(p.relative_to(BASE)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in BASE.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
assert all(x['bytes']<20*1024*1024 for x in manifest)
rolling=[{'path':str(OWN/x),'sha256':sha(OWN/x)} for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]
write(BASE/'out'/'PERSISTENCE_RECEIPTS.json',{'saved_at':stamp,'artifacts':manifest,'rolling':rolling,'remote_verification':'UNVERIFIED'})
print(json.dumps({'status':'COMPLETE_LOCAL','assertions':results['assertions'],'formal_arithmetic_status':lean['status'],'artifact_count':len(manifest),'source_statement_hash':claim['statement_sha256'],'full_fei':'OPEN'}))
