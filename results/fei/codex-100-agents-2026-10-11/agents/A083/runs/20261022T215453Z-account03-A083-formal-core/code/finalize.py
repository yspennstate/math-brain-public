from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def dump(p,v):p.write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
result=read(R/'out/RESULT.json');assert result['status']=='PASS'
lean=read(R/'out/LEAN_RESULT.json');assert lean['status']=='NOT_RUN_ADMISSION_HELD'
protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
statement=('For F(x,a,b,y)=(-1)^a if x=0, otherwise 2y-1 if b=1 and +1 if b=0, '
 'and every real c in [3/4,13/16], let Q_c have empty mass 1/16 and nonempty mass 15/16 '
 'distributed as Bernoulli(8c/15,8c/15,4c/15,4c/15) conditioned nonempty. '
 'Along query b then query y only at b=1, transport Q_c by the SAME normalized spectral branch kernels. '
 'The complete source-erasure, outcome and reach-weighted full inherited terminal KL bill equals D(P_F||Q_c)<183/128 bits. '
 'For the fair initial fallback, the previously booked conditional C=-(1/2)log2(1-4c/15) partitions '
 'into untouched-terminal C/2 and second-query erasure C/2, without duplication. '
 'The original mean b-child surplus 4 mean I-mean H=3 pays this full bill plus continuation energy debit 1, '
 'while retaining all terminal entropies and reserve greater than 73/128 bits.')
claim={
 'claim_id':'A083-SAME-REFERENCE-Y-CONTINUATION','version':1,'exact_statement':statement,
 'hypotheses':['specified actual uniform-cube Boolean gate','3/4 <= c <= 13/16','bits; normalized finite KL',
 'same inherited reference through both queries; fair initial zero-row fallback for explicit C partition',
 'one original mean-child surplus dedicated only to this transaction; prior C booking retained'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A083; continuation proof and certificate','A038/A092 reached-gate provenance via A083 stage5'],
 'proof_source':['PROOF.md','code/continuation.py','code/continuation_v1.py (helper only; original main timed out)','out/RESULT.json'],
 'proof_dependencies':['finite KL chain rule and monotonicity of logarithm; reconstructed in PROOF.md',
 'exact Walsh/direct-character-sum identities checked in this run','prior A083 stage5 canonical-root identification only; all-c theorem does not need that identification'],
 'review_records':[],'status':'AUTHOR_PROOF_EXACT_CHECKED_REVIEW_PENDING','supersedes':[],'refutes':[],
 'first_unproved_line':None,'next_consumers':['A047','A092','A038','A039','A094','B17','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
dump(R/'CLAIMS.json',[claim])
next_action=('Replace the literal character (-1)^a by an arbitrary non-flat Boolean core h; derive the SAME-reference '
 'mixed-query residual in terms of its full inherited likelihood profile and H(h),I(h), without importing fresh banks '
 'or assuming FEI for h. A047/A092 independently reconstruct this finite continuation first.')
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B17','packet_id':'A083',
 'gap_id':'C024-PHYSICAL-REFERENCE-OWNED-RESERVE-COMPATIBILITY','attempt_id':'A083-stage17-same-reference-y-continuation',
 'method':'Finish prior partial transaction; exact finite Fourier/Bayes and old-debit identities; all-real analytic KL bound; Lean draft held by fresh admission',
 'mathematical_delta':'Prescribed b then active y history fully paid from SAME 3-bit mean-child owner including prior C, full quotient/erasure/outcome/terminal reference bills and 1-bit energy debit; reserve >73/128; arbitrary-core bridge unpaid',
 'deliverable_status':'COMPLETE_LOCALLY_SAVED','mathematical_status':'SCOPED_ANALYTIC_PROOF_EXACT_CHECKED_REVIEW_PENDING_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A083-REFERENCE-ONLY-MATCHING-AND-PAID-CONDITIONAL-BILL','version':1,'use':'same incoming reference and previously booked C; needed fixture algebra reconstructed'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['REPORT.md','PROOF.md','out/RESULT.json','out/FROZEN_SPEC.json','out/FROZEN_SPEC_V1_1.json','out/V1_ATTEMPT.json','out/SOURCE_RECEIPTS.json','out/LEAN_RESULT.json','out/MEMOK.json'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal arbitrary-core inherited-profile payment is unsupported','Independent review and supervisor/mirror adoption unverified','Fresh memok held Lean; current formal source UNCHECKED'],
 'packet_ids':['A083']}
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
headings=protocol['required_per_run']['report_fields']
paragraphs=[
 'A083 B17 resumed stage17 (sixth source-complete mathematical stage found locally). Finish the prior actual four-bit gate transaction: query b, then y only at b=1, with SAME inherited Q_c and old conditional debit C. Uniform independent bits, Boolean signs, entropy/KL in bits, all real 3/4<=c<=13/16. PROOF.md states every law and denominator. The complete finite-history bill is paid; full FEI remains OPEN. The owner\'s current deadline supersedes the old initial protocol dates; no schedule or clock is changed.',
 'Read the complete execution-v2 protocol and required campaign/control files, plan source, twelve supplement sources, all four manuscript text versions, BOARD and B17 notes v2, five prior A083 reports and stage5 proof/code. out/SOURCE_RECEIPTS.json records 37 orientation files and their actual hashes/encoding; out/SOURCE_READING.txt supplies line locators. A manuscript extraction failed strict UTF-8, then was explicitly read as cp1252; this is recorded, not blamed on source corruption. Later own run folders contained markers rather than a newer mathematical report. Lead scalar target was already completed in substantive stage2; dispatch resumes the productive stage5 gap. No new literature theorem is invoked.',
 'PROOF.md reconstructs the exact actual spectra, all-real D(P||Q_c)<183/128 bound, same-kernel two-step KL identity, C=C/2+C/2 partition, full terminal entropy and original-source ownership. The one extra rate-four energy debit is 1, so total including the already booked C is 1+D<311/128 of the original 3; reserve >73/128. The b=1 y query has full erased source support and fair kernel everywhere. The previously unpaid source erasure/outcome and retained quotient bills are included, with untouched b=0 and both y terminals retained. FIRST UNSUPPORTED UNIVERSAL LINE: the analogous arbitrary-core inherited-profile bill is payable from one genuinely unused ancestor source under an eligible policy, retaining full terminal seed entropy. No all-dimensional constant improves.',
 f'Frozen v1 targeted 51 rational histories plus 16 continuum boxes; it reached the interval checks then exceeded its 60-second guard, so it is TIMEOUT_UNRESOLVED, preserved as code/continuation_v1.py and out/V1_ATTEMPT.json. Frozen v1.1 changes method to an analytic all-real bound plus nine exact rational histories (three c values, all three initial fallbacks), no symmetry or dimension escalation. Executed python -X utf8 code/continuation.py: PASS in {result["seconds"]:.6f}s; {result["assertions"]} primary, {result["helper_assertions"]} transport-helper and {result["interval_helper_assertions"]} interval-helper assertions (distinct counters, not added to old-stage counts). Direct character sums independently match integer FWHT; physical-edge influences verify every terminal; reference normalization, conditional/full KL chains, old-booking partition and complete support are checked. Continuum signs use four exact integer power inequalities with analytic monotonic logarithms; finite samples are not the continuum proof. Estimate <100 MB; no heavy compiler launched. Fresh memok held formal admission: code/FairContinuation.lean is only an UNCHECKED draft, not a Lean result. out/LEAN_RESULT.json records the hold. No memory threshold was overridden.',
 'Only elementary finite KL and explicit gate spectra supply the new proof. The old stage5 reference/debit ownership is preserved, not independently accepted wholesale. The canonical root from that stage lies inside the proved all-real interval; the expanded normalized family needs no canonical-root uniqueness premise. This finishes that gate\'s previously partial transaction without extending A047\'s general matching theorem or asserting a universal profile bound. The scoped result is an author proof with exact validation, pending independent reconstruction. No remote adoption, mirror verification, public release or new theorem certification is claimed.',
 next_action+' This tests the unpaid universal interface rather than extending infrastructure or repeating an already closed census. Review should check especially the empty-atom +1/4 cross-entropy term, actual reach weights, and that C is included once.',
 'All research outputs are confined to this assigned A083 run. Four protocol files and rolling STATUS/WORKLOG/LEARNED are saved by code/finalize.py; exact field sets, claim statement digest, identical progress/delta, successful exact result and <20 MB per-file limits are checked. out/ARTIFACT_RECEIPTS.json binds local bytes. The only external state updates are the developer-required wake/checklist hooks; no git, email, brain writes, peer-folder mutation or deletion occurred. Supervisor copying, independent review and mirror persistence are unobserved.'
]
report='\n\n'.join('# '+h+'\n\n'+p for h,p in zip(headings,paragraphs))
report+='\n\nUniversal bridge: This stage moves C024 history transfer and C019 stopping-tree payment by finishing one previously partial inherited-reference transaction: the actual next y query, the untouched sibling, full quotient/erasure/outcome/terminal KL and the old conditional spend are all charged once to the SAME original 3-bit mean-child source, leaving >73/128 after an extra 1-bit energy debit. C018 and full FEI remain open. What remains is a dimension-independent inherited-profile/terminal-seed payment for arbitrary non-flat cores. NEXT derives that exact arbitrary-core residual; it is the shortest identified continuation because it directly removes the literal-character restriction instead of buying another fresh reference bank or adding an unrelated class estimate.\n'
(R/'REPORT.md').write_text(report,encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
(A/'STATUS.md').write_text('STATE: A083 stage17 complete locally: SAME-reference b then active-y full ledger paid from original3; D<183/128, reserve>73/128; 9 exact histories PASS; Lean admission HELD; FEI OPEN.\nNEXT: Derive arbitrary non-flat core inherited-profile residual with SAME old booking and both terminals; A047/A092 review finite continuation; no fresh bank.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+' Stage17: resumed stage5 rather than marker-only later runs. Proved full same-reference next-y finite history, D<183/128 and original-source reserve>73/128, retaining C once and all terminals. V1 hit 60s guard; analytic v1.1 +9 histories PASS in '+str(result['seconds'])+'s. Fresh memok refused Lean; no compiler launched. Independent review and arbitrary-core payment remain open.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+' Durable: At reached priority gate F=(-1)^a if x=0 else (2y-1 if b=1 else1), b=1 then y has full uniform erased law and fair channel: both actual leaf spectra uniform4. Old conditional C splits into untouched b=0 C/2 and y-erasure C/2; it is not a new spend. For all c in[3/4,13/16], complete same-reference KL tree bill D(P||Q_c)<183/128 from exact power inequalities, including the empty atom +1/4 cross-entropy term. Original mean child S4=3 pays full debt plus energy1 leaving>73/128; arbitrary-core counterpart is still unsupported. Compiler admission failure leaves formal source unchecked.\n')
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
assert '# '+headings[-1] in report and report.rstrip().split('\n')[-1].startswith('Universal bridge:')
files=[p for p in R.rglob('*') if p.is_file()]
assert all(p.stat().st_size<20_000_000 for p in files)
receipts=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files if p.name!='ARTIFACT_RECEIPTS.json']
for p in [R.parent/'20261014T053514Z-account05-A083-formal-core/code/reference_rows.py',R.parent/'20261014T023633Z-account05-A083-formal-core/code/occupancy_check.py']:
    receipts.append({'read_only_helper':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
dump(R/'out/ARTIFACT_RECEIPTS.json',{'saved_at_utc':stamp,'local_validation':'PASS','independent_review':'UNVERIFIED','mirror':'UNVERIFIED','files':receipts})
print(json.dumps({'status':'LOCAL_PACKAGE_PASS','protocol_files':4,'files_hashed':len(receipts),'claim':claim['claim_id'],'full_FEI':'OPEN','Lean':'NOT_RUN_ADMISSION_HELD'}))
