from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1];OWNER=RUN.parents[1];TEAM=OWNER.parents[1];OUT=RUN/'out'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def readj(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,j):p.write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=readj(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
packets=readj(OUT/'PACKET_CENSUS.json');streams=readj(OUT/'STREAM_CHECKPOINT.json');ledger=readj(OUT/'SOURCE_LEDGER.json')
source=TEAM/'agents/A097/runs/20261014T050248Z-account05-A097-cross-route-transfer'
claim=next(c for c in readj(source/'CLAIMS.json') if c['claim_id']=='A097-NEGATIVE-CELL-FLOOR-SOURCE-BANK')
critical=[source/'REPORT.md',source/'DERIVATION.md',source/'CLAIMS.json',
 TEAM/'agents/A081/runs/20261014T042148Z-account05-A081-dependency-certificates/REVIEW.md',
 TEAM/'agents/A082/runs/20261014T045125Z-account05-A082-finite-inequalities/REVIEW.md',
 TEAM/'agents/A046/runs/20261014T041928Z-account05-A046-current-candidate-intake/REPORT.md']
for p in critical:
 b=p.read_bytes();ledger.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'scope':'Critical proof or scoped review/handoff original read'})
save(OUT/'SOURCE_LEDGER.json',ledger)
review={'reviewer':'A098','timestamp':now,'verdict':'ACCEPT_AT_STATED_SCOPE',
 'scope':'Full original A097 negative-cell supplied-reference theorem for all a>=1,b>=0,r>=1; same-mixture complete KL, CE<=c+10(C+E+J), erased-edge source rate2C0+10, structural18 and arbitrary independent terminal debt. No hereditary reset or broader A086 theorem accepted.',
 'method':'Independent vacuum/sector conditional-reference proof and physical edge reconstruction; own integer Walsh, complete conditional kernel, augmented posterior prime-log cancellations and fixed rational logarithm certificate',
 'proof_source':str(RUN/'DERIVATION.md'),'validation_source':[str(OUT/'FLOOR_CHECK.json'),str(OUT/'TENSOR_CHECK.json')],
 'source_statement_sha256':claim['statement_sha256'],'reviewer_contributed_repair':False}
claim['review_records']=claim.get('review_records',[])+[review]
claim['status']='INDEPENDENTLY_ACCEPTED_AT_FULL_STATED_SCOPE_BY_A098_LOCAL_ADOPTION_PENDING'
save(RUN/'CLAIMS.json',[claim]);save(OUT/'REVIEW_RECORD.json',review)
save(OUT/'STATEMENT_HASH_NOTES.json',{'recorded_source_hash':claim['statement_sha256'],
 'recomputed_envelope_hash':hashlib.sha256(json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'policy':'Original statement/hypotheses/dependency descriptions/contributors preserved; byte-pinned local proof reconstructs actual dependency slices, not broad upstream clauses.'})
decisions=[
 ('A001','CONTINUE_NONFLAT_OWNERSHIP_AUDIT','Replace the completed flat-core root quota by one actual non-flat incoming conditional reference; audit retained price PLUS all row remainders against genuinely unused child slack, not one owner repeated.','A096/A082 accepted non-flat remainder; A097 floor review here','A086/A094'),
 ('A045','CONTINUE_SIGNED_QUADRATIC_PRICE','Pay complete quadratic C_ref minus KL remainder from the owned mixed Delta, retaining normalized reference mass tax and all child/terminal costs. Quadratic tail-energy identification is complete.','A041/A044 and A045 current audit','A090/A091/A085'),
 ('A073','CONSUME_NONFLAT_INCOMING_REFERENCE','Use already reviewed A090 signed partition/A096 non-flat loss. Certify one proposed incoming-reference child normalizer or retained-price inequality; do not repeat the gate Parseval/remainder grid. Preserve current productive stage if unfinished.','A081/A082 reviews; A096/A097 source-versioned next inequality','A085/A094'),
 ('A040','REVIEW_ACTUAL_WIDTH_FILTERING','Independently reconstruct A046 v2 all-width Qbad<=5I and wide-block zero badness; old V/I logarithmic envelope objection remains valid but does not refute actual filtered payment. Then audit first biased core-child debits.','A046-SEPARATOR-LAYER-CUTOFF-RESERVE@2','A087/A092'),
 ('A046','CONTINUE_INTERLEAVED_CORE_EXPOSURE','Derive both biased child moments after first core query with unresolved separator, original physical reaches, remaining W capacity and full terminal/reference costs. No fresh control reserve.','A046 v2 pending review; A040 original reserve audit','A040/A087/A092'),
 ('A089','PRESERVE_RARE_CORE_ADMISSION','Continue a noncircular retained rare-core E or actual surplus constraint beyond singleton caps; matching-policy moderate-prefix bound is completed. No new sign/depth census.','A075/A072/A080 existing fixture','A075/A074/A092')]
deltas=[]
for aid,action,target,dep,reviewer in decisions:
 p=next(x for x in packets if x['packet_id']==aid)
 latest=next((x['path'] for x in reversed(p['runs']) if x.get('files',{}).get('REPORT.md')),None)
 deltas.append({'packet_id':aid,'action':action,'distinct_next_lemma':target,'dependency':dep,'independent_reviewer':reviewer,
 'status_source':p['status_text'],'latest_complete_report':latest,
 'retired_obligation':'Duplicate singleton tax review' if aid in ['A045','A046','A073'] else 'Duplicate B05 minimum-coordinate census',
 'deployment':'Saved local source-bound handoff; shared adoption and actual capacity unverified'})
save(RUN/'CHECKPOINT_ALLOCATION.json',{'run_id':RUN.name,'snapshot_at':now,
 'capacity':{'native_streams':20,'logical_packets':100,'extra_workers':0,'extra_schedules':0},
 'keepers':{'minimum_ratio_calibration':'A082','singleton_tax_review':'A090'},'packet_deltas':deltas,
 'additional_existing_packet_handoff':{'packet_id':'A097','target':'Expose one active bit through the incoming paid Q, specify child reference lift/normalizers and pay reset from the SAME remaining bank','reviewers':['A086','A094'],'new_worker':False},
 'all_packet_coverage':[{'packet_id':p['packet_id'],'stream':p['stream'],'status':p['status_text'],
 'action':'REFRESH_EXISTING_LANE' if p['packet_id'] in [d['packet_id'] for d in deltas] else 'PRESERVE_NATIVE_PRODUCTIVE_WORK_AND_REVIEW_GATE'} for p in packets],
 'guard':'One packet per natural invocation; productive unfinished work first; at genuine complete-unreviewed cap review/repair instead of another broad candidate.'})
def totals(s):return {'status_packets':sum(x['packets_with_status'] for x in s),'complete_local_runs':sum(x['complete_runs'] for x in s),
 'exact_full_scope_review_match_ids':sum(len(x['exact_statement_review_matches']) for x in s),
 'source_complete_unmatched_ids':sum(len(x['source_complete_unmatched_candidates']) for x in s)}
previous=readj(OWNER/'runs/20261014T024504Z-account05-A098-resource-reallocation/out/STREAM_CHECKPOINT.json')
comparison={'previous':totals(previous),'current':totals(streams),'source_receipts':len(ledger),
 'claim_records':len(readj(OUT/'CLAIM_CENSUS.json')),
 'milestones':[{**x,'assessment':'PARTIAL:100 packet coverage and reuse; shared baseline adoption and full nonduplication unverified' if x['day']==2 else 'NOT_DUE; quantitative restricted payments and reviewed obstructions available'} for x in protocol['checkpoints']],
 'parser_delta':'Two exact full-original-scope acceptance aliases added after inspecting A081/A082 reviews; partial bundled verdicts remain excluded.',
 'limits':'Counts include historical versions and scoped records, are non-atomic and not a theorem audit or actual scheduled-capacity receipt. Review queue triage still required.'}
save(OUT/'CHECKPOINT_COMPARISON.json',comparison)
pilot=readj(OUT/'PILOT_CHECK.json');main=readj(OUT/'FLOOR_CHECK.json');tensor=readj(OUT/'TENSOR_CHECK.json');total=main['assertions']+tensor['assertions']
save(OUT/'VALIDATION_TOTALS.json',{'credited_checks':total,'pilot_excluded':pilot['assertions'],'main':main,'terminal':tensor})
derivation=(RUN/'DERIVATION.md').read_text(encoding='utf-8').replace('# Independent A097 negative-cell floor reconstruction','**Independent complete reconstruction.**',1)
report=f'''# A098 stage5: supplied-reference bank review and hereditary handoff

## exact target, quantifiers, hypotheses and units

Compare actual post-Day2 output to the milestones, refresh six retired duplicate obligations within existing20 streams/100 packets, and independently review A097-NEGATIVE-CELL-FLOOR-SOURCE-BANK@1 at its entire scope. Parameters are every a>=1,b>=0,r>=1, a full data point inside the negative point-defect cell, any normalized finite-cost source reference positive on true support (off-support zeros allowed), and any independent Boolean terminal with supplied complete reference. Costs are ideal bits, influence is ordinary uniform physical flip probability. No hereditary incoming-reference closure or universal FEI claim is included.

## sources actually read, revisions and theorem locators

Read BOARD supervisor snapshot2026-10-14 05:31 UTC, B20 STREAM_NOTES v2 still dated2026-10-11 23:39Z and own STATUS at start. Current execution-v2 and required canonical status/registries/actions/plan/earlier reports, supplemental campaign/sources and context text manuscripts were reread by the read-only intake. Every available packet report/claim/status was included; SOURCE_LEDGER pins {len(ledger)} read receipts. This is navigation and allocation evidence, not independent acceptance of every theorem.

Critical originals read fully: A097 stage5 REPORT/CLAIMS/DERIVATION, sections1-5 exact three-component marginal, common-vacuum collapse, destroyed-edge bank and terminal debt; A081 stage5 REVIEW, entire-scope A090 signed partition and zero-child-slack guard; A082 stage5 REVIEW, A096 non-flat remainder and price-five obstruction; A046 stage5 report's actual width-filtering consequence, validation and next-action sections. Packet census/current statuses of the six retired lanes plus A090/A096/A097 were inspected. A short census read preceded file availability; retry found the completed intake, with no mathematical inference from the missing-path event.

The board's request for A098 to review A090 is superseded in scope by A081's already completed full review; A096's non-flat remainder has A082 acceptance. These are consumed rather than repeated. The selected new independent obligation is A097's complete-reference bank. Source proof dependencies A086/A011 are credited; their relevant actual identities are reconstructed below without blanket acceptance of broader pending clauses.

## complete derivation or exact first unsupported line

{derivation}

**Where the next source-bound proof must begin.** For a declared signed-amplitude lift a_S=epsilon_S sqrt(Q_S) of an incoming normalized spectral reference, the physical cofactor amplitudes are a_T +/- a_(T+i). Their normalization factors are Z_+=1+2 sum_T a_T a_(T+i) and Z_-=1-2 sum_T a_T a_(T+i). They average to1 and lie in[0,2], but need not both be1 as the actual Boolean source's cofactors are. A lift and its actual child normalizers must therefore be specified before treating descendant references as fresh normalized floors. This elementary diagnostic is not a construction of paid descendants: phase choice, possible zero child norm, complete terminal debt and the same remaining bank are exactly the next unresolved interface. Mixture labels in the floor are analytical labels and cannot silently become fair physical child histories.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC was saved before any computation. The independent helper covers a=1..3,b=0..2,r=1..2 and every2^b dummy negative-cell point:42 actual roots and126 supplied-reference cases. References are structural source spectrum with off-support zeros, uniform full data law and increasing rational weights. Active/control point translations are the only reduction, justified by physical symmetry. A separate terminal job covers all16 labeled two-bit signs, two terminal references and three floors on one fixed a2,b1,r2 root:96 terminal cases. No dimension increase after freezing.

Commands from A098:

    python -X utf8 runs/{RUN.name}/code/intake.py
    python -X utf8 runs/{RUN.name}/code/floor_review.py pilot
    python -X utf8 runs/{RUN.name}/code/floor_review.py
    python -X utf8 runs/{RUN.name}/code/floor_review.py tensor

Pilot one root/three references: {pilot['assertions']} checks, {pilot['runtime_seconds']:.6f}s, PASS, excluded from main total. Main42 roots/126 references: {main['assertions']} checks, {main['runtime_seconds']:.6f}s, PASS. Tensor96 cases: {tensor['assertions']} checks, {tensor['runtime_seconds']:.6f}s, PASS. Credited total {total:,}. Completed cases flush immediately to JSONL. Integer Walsh spectra and separately enumerated physical edges verify actual signs and every coordinate influence; Fraction values verify mixture, calibration, complete control kernel and output normalizers. Exact prime-log linear forms verify direct full KL=(1-lambda)D_source-kappa and additive terminal CE/KL before estimates. Fixed16-term atanh rational tails certify all cost/bank inequalities; no floating log or refinement chooses signs.

No author helper was imported or executed. Estimated memory90MB, not a measured peak; no job expected above300MB so no memok trigger. Every computation enforces55s, uses python -X utf8, and creates no GPU/background process or worker. The small domains corroborate the all-parameter derivation, not a finite-to-infinite inference. The terminal job reconstructs the fixed floor as its tensor fixture rather than claiming its repeated root checks as new root coverage.

## proof dependencies and changed downstream conclusions

All clauses of A097@1 are independently reconstructed without repair. Character orthogonality, direct pivotal counting, same-reference KL chain rule, elementary complete mixture bounds and rational constants suffice. Stored upstream proof-dependency descriptions are preserved, but only the actual floor slices are locally proved; no acceptance of A086's broad subprobability72-tax claim is implied. CLAIMS preserves original statement/hypotheses/contributors/hash and appends independent acceptance. The source bank is only certified at the root supplied-reference scope. Structural18 is a transfer consequence on a known read-once class, not a new FEI class result.

Day2 remains partial globally:100 packets have status coverage, recovered fragments are reused, but shared baseline adoption, full queue audit and nonduplication are not verified. Day4 is not yet due; reviewed quantitative payments and obstructions are available. Counts compare current/prior local snapshots and include historical/scoped candidates. Two precise acceptance aliases from inspected A081/A082 full-scope records are now recognized; partial verdicts remain excluded. Increased parser matches are not all new mathematical outputs and do not certify every stream's review-cap compliance. This run opens no new broad candidate.

CHECKPOINT_ALLOCATION gives six distinct existing-lane refreshes. A001 audits non-flat retained-price plus remainder ownership; A045 pays complete quadratic C_ref-KL from the actual mixed Delta; A073 certifies the next incoming-reference/child-normalizer inequality instead of a completed gate grid; A040 independently reviews A046 v2 actual Qbad<=5I (the old logarithmic envelope obstruction remains valid); A046 studies first interleaved core-query balance loss with remaining W capacity; A089 preserves its productive rare-core admission beyond singleton caps. Completed moderate/continuous-prefix bounds are consumed rather than restarted. A082/A090 retain their calibration/review lanes; no extra capacity is created. The other94 packets keep native productive work and review gates.

**Exact downstream change.** A097's supplied complete floor, erased edges and arbitrary terminal cost now have an independent acceptance record. A097/A086/A094 can target the incoming-floor active exposure instead of repeating the root bank proof. Its normalized mass, analytical-label posterior and full terminal debt cannot be replaced by an uncharged fresh descendant floor. A090/A096 quotient remainders remain distinct from the retained reference cost; A081's zero-slack guard and A082's price-five obstruction are binding source-bound stress tests, not additional reserve credits.

## one next mathematical action and independent reviewer

Expose one active data bit of the accepted floor, specify the incoming signed reference lift and both actual child normalizers, and prove or refute their complete reset/retained-cost debit from the SAME remaining source bank. A097 owns this existing productive continuation; A086/A094 independently challenge it. A098's next checkpoint should consume that exact one-step result, or a sourced non-flat retained-row payment from A096/A001/A073 if earlier available. A040's separate review consumes A046 v2; A046 proceeds to the first interleaved biased core children. Do not renew scalar tax, root floor, fixed-width or already accepted gate-remainder reviews.

## actual persistence receipts or precise save blocker

Saved REPORT/CLAIMS/PROGRESS and byte-identical PACKET_DELTA, DERIVATION, FROZEN_SPEC, CHECKPOINT_ALLOCATION, independent code, immediate exact case journals, posterior/bank checks and totals. out/SCHEMA_CHECK and MANIFEST certify exact protocol fields, report headings, two-line status, size and SHA256 readback. Rolling WORKLOG/LEARNED append this stage. All writes stay in A098; no shared tree, other agent, brain, Git or schedule is changed. Independent local acceptance, supervisor adoption, mirrors and downstream use remain separate. Local persistence succeeds; shared deployment and remote copying are unobserved.

## Universal bridge

This stage moves C020 complete whole-set reference cost and C024 history transfer by independently accepting A097's full supplied-reference root payment CE_F<=c+10(C+E+J), rate2C0+10 with actual erased edges, exact retained posterior KL and arbitrary terminal CE. The universal FEI constant improves by zero. What remains is inherited-reference transport after actual data exposure, paid from the same genuinely unused bank; C018 still lacks universal retained terminal-row payment and C019 still lacks arbitrary interleaved core admission. NEXT starts with the actual child normalizers and complete signed debit, because another root-only floor or quotient remainder would not address the hereditary obstruction required for full FEI.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
progress={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B20','packet_id':'A098',
 'gap_id':'G-REFERENCE-HEREDITY','attempt_id':'A098-stage5-owned-floor-independent-review',
 'method':'100-packet source-bound checkpoint refresh; independent complete mixture/physical edge/bank reconstruction',
 'mathematical_delta':f'A097 complete supplied-reference floor and erased-edge source-bank v1 independently accepted;{total} exact checks. Already reviewed A090/A096 remainders consumed; inherited child reset unpaid.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT_ADOPTION_PENDING','mathematical_status':'SCOPED_REFERENCE_TRANSFER_INDEPENDENTLY_ACCEPTED;FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':claim['claim_id'],'version':1,'scope':'Full original theorem reconstructed'},
 {'claim_id':'A090-ARBITRARY-GATE-SIGNED-REFUND-PARTITION','version':1,'scope':'A081 review consumed for dispatch'},
 {'claim_id':'A096-NONFLAT-POINT-QUOTIENT-REMAINDER','version':1,'scope':'A082 review consumed for dispatch'},
 {'claim_id':'A096-CHILD-BANK-PRICE-FIVE-OBSTRUCTION','version':1,'scope':'A082 reviewed stress test; not a proof premise'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'Independent full-scope acceptance;no repair'}],
 'source_artifacts':['DERIVATION.md','FROZEN_SPEC.json','CHECKPOINT_ALLOCATION.json','out/SOURCE_LEDGER.json','out/PACKET_CENSUS.json','out/CLAIM_CENSUS.json','out/CHECKPOINT_COMPARISON.json','out/FLOOR_CHECK.json','out/TENSOR_CHECK.json','out/VALIDATION_TOTALS.json','out/REVIEW_RECORD.json'],
 'next_consumers':['A001','A040','A045','A046','A073','A089','A090','A096','A097','A099','A086','A094','B20 supervisor'],
 'next_action':'One actual active-bit exposure of incoming Q, declared lift/child normalizers and complete reset price from same remaining source bank.',
 'stagnant_substantive_attempts':0,'blockers':['Hereditary incoming-reference payment unproved','Universal retained-row cost and interleaved child ownership unproved','Shared deployment/mirrors unverified'],'packet_ids':['A098']}
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)
(OWNER/'STATUS.md').write_text(f'STATE: Stage5 saved: A097 complete negative-cell floor/source-bank v1 independently accepted;{total:,} exact checks PASS; six handoffs refreshed; FEI OPEN.\nNEXT: A097 expose active bit with incoming Q, actual child normalizers and SAME remaining bank; A086/A094 review; A040 review A046 v2; preserve rare-core admission.\n',encoding='utf-8')
with (OWNER/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{now} — {RUN.name}: consumed A081 arbitrary-gate and A082 non-flat remainder/price-five reviews instead of repeating them. Independently reconstructed A097 supplied floor, posterior KL, actual created/erased/control bank and full terminal debt. Pilot53 checks; main126 references/2955 checks;96 terminal cases/496 checks; credited3451 PASS. Six next lemmas refreshed; incoming active-bit reference transport remains open. Recognized two full-original-scope aliases after reading original reviews. All writes local, no added schedules.\n')
with (OWNER/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nStage5: A097-NEGATIVE-CELL-FLOOR-SOURCE-BANK@1 independently holds at full scope. Negative-cell point edits admit actual nonnegative three-component marginal; empty-calibrated floor retains same-reference posterior KL and costs at most c+10(C+E+J). Explicit erased-edge debit E<=Ig/2 gives rate2C0+10 from one certified source bank; structural18 and arbitrary terminal coefficient1 remain. This is root supplied-reference payment, not hereditary reset. A signed incoming spectral reference has cofactor normalizers Z+-=1+-2 sum a_T a_T+i, not automatically both1; a reference lift and its normalizer bills must precede descendant-floor admission. Consume A081/A082 accepted gate/non-flat remainders, preserve terminal debt and zero-child-slack guards, and review actual A046 v2 payment rather than its already-obstructed coarse envelope.\n')
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected;assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
assert len((OWNER/'STATUS.md').read_text().splitlines())==2
save(OUT/'SCHEMA_CHECK.json',{'status':'PASS','progress_fields_exact':True,'claim_fields_exact':True,'report_fields_present':True,'delta_byte_identical':True,'status_two_lines':True})
manifest=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and p.name!='MANIFEST.json':
  b=p.read_bytes();assert len(b)<20*1024*1024;manifest.append({'path':str(p.relative_to(RUN)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save(OUT/'MANIFEST.json',manifest)
assert all(hashlib.sha256((RUN/x['path']).read_bytes()).hexdigest()==x['sha256'] for x in manifest)
print(json.dumps({'status':'SAVED_READBACK_PASS','checks':total,'checkpoint':comparison['current'],'run':str(RUN),'files':len(manifest)}))
