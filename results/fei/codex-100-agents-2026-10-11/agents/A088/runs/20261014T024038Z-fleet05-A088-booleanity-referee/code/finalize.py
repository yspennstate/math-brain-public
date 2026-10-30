from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]; agents=A.parent; brain=agents.parent
run=R.name
proto=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
p=json.loads(proto.read_text(encoding='utf-8'))
s67=agents/'A067/runs/20261014T020120Z-fleet05-A067-hypercontractive-refinement'
s70=agents/'A070/runs/20261014T005025Z-fleet05-A070-analytic-route-referee'
targets=[(s67,'A067-TWO-SUBCUBE-COMPLETE-CELL-REFERENCE'),(s70,'A070-MASK-REFUND-BOOLEANITY-AND-EDGE-CONVERSION-AUDIT')]
records=[]
for src,name in targets:
    c=next(c for c in json.loads((src/'CLAIMS.json').read_text(encoding='utf-8')) if c['claim_id']==name)
    raw=hashlib.sha256(c['exact_statement'].encode()).hexdigest()
    can=hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert c['statement_sha256'] in (raw,can)
    c['review_records'].append({'reviewer':'fleet05/A088','verdict':'HOLDS_AT_FULL_STATED_SCOPE','independent':True,'substantive_repair':False,'review_source':str(R/'AUDIT.md'),'validation_source':str(R/'out/CHECK.json'),'method':'New explicit controller/cell partition, physical final spectra, exact reference cross entropy and direct independent resampling pairs; own prior arithmetic only; no other agent code','hash_convention':'raw statement' if c['statement_sha256']==raw else 'canonical statement+hypotheses','scope':'Original exact hypotheses preserved; normalized-real diagnostic failures and signed conversion guard are not Boolean FEI refutations','registry_adoption':'UNVERIFIED'})
    c['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_RECEIPT'
    assert set(c)==set(p['required_per_run']['claim_fields'])
    records.append(c)
def write(path,obj): path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
write(R/'CLAIMS.json',records)
full=json.loads((R/'out/CHECK.json').read_text()); pilot=json.loads((R/'out/PILOT.json').read_text()); real=json.loads((R/'out/REAL_SCOPE.json').read_text())
sources=[proto,brain/'BOARD.md',brain/'claude/B18/STREAM_NOTES.md',s67/'CLAIMS.json',s67/'DERIVATION.md',s67/'REPORT.md',s70/'CLAIMS.json',s70/'DERIVATION.md',A/'runs/20261013T234248Z-fleet05-A088-booleanity-referee/AUDIT.md',A/'runs/20261013T234248Z-fleet05-A088-booleanity-referee/code/check.py']
manifest=[]
for path in sources:
    data=path.read_bytes(); manifest.append({'path':str(path),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
write(R/'out/SOURCE_MANIFEST.json',manifest)
next_action='Audit one control-dependent two-core branch transfer using a single complete output/conditional KL reference: retain the A070 cancellation banks, both actual terminal entropies, and an explicitly exclusive child slack for the 2I_X reserve. A094/A070 independent review; A067/A069/A096 consume.'
progress={'protocol_revision':p['revision'],'run_id':run,'stream':'B18','packet_id':'A088','gap_id':'C019-EXCLUSIVE-TERMINAL-CORE-SLACK-FOR-SHARED-REFERENCE','attempt_id':'A088-stage4-new-cell-reference-audit','method':'Independent exact five-cell cross-entropy proof, physical Boolean edge payment, resampling versus edge conversion and normalized-real diagnostics','mathematical_delta':'A067 two-subcube complete reference v1 and A070 mask-refund/conversion audit v1 independently HOLDS; 14068 Boolean cases/349542 exact assertions; 499 normalized-real cases,8 ownership failures and actual real degree-one terminal counterexample. Same-C induction still needs exclusive 2I_X child surplus.','deliverable_status':'COMPLETE_LOCAL_SAVED_READ_BACK','mathematical_status':'TWO_SCOPED_THEOREMS_INDEPENDENTLY_ACCEPTED; FULL_FEI_OPEN','claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'role':'review target'} for c in records]+[{'claim_id':'A067-BOUNDED-FIBER-TWO-EVENT-ACCESS-RESERVE','version':1,'role':'previously accepted ownership/channel fragments only'},{'claim_id':'A067-LOCAL-BOOLEAN-GRANULARITY','version':1,'role':'previously accepted optional terminal certificate'}],'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'independent local acceptance receipt; source text/hash unchanged'} for c in records],'source_artifacts':[str(path) for path in sources],'next_consumers':['A067','A070','A069','A094','A096','B14','B18','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Unpaid exclusive retained-core surplus for universal recursion','Control-dependent source transfer unproved','Registry adoption and remote mirror unverified'],'packet_ids':['A088']}
assert set(progress)=={f.split(' (')[0] for f in p['required_per_run']['progress_fields']}
write(R/'PROGRESS.json',progress); write(R/'PACKET_DELTA.json',progress)
report=f'''# A088 stage 4: complete two-controller reference and Boolean payments

## exact target, quantifiers, hypotheses and units

Independent review of A067-TWO-SUBCUBE-COMPLETE-CELL-REFERENCE v1 and A070-MASK-REFUND-BOOLEANITY-AND-EDGE-CONVERSION-AUDIT v1. A067: every finite Boolean control-independent seed g(X), arbitrary core flags A,B, two globally fixed subcube controllers p,q on Z, and final XOR/union edit fibers of probability <=1/4 has Q_access<=K I_Z+2I_X, K=4+log2 5+2/ln2<19/2 (compatible K<9). All actual terminal entropies are retained; U-certified/degree-two leaves give the claimed full entropy bound. A070: exact arbitrary-K signed physical-influence conversion plus its normalized-real and actual Boolean cancellation obstructions. Bits throughout. Both verdicts HOLDS at the exact source scope, no repair. Full FEI OPEN.

## sources actually read, revisions and theorem locators

BOARD snapshot 2026-10-14 02:33 UTC, full file plus focused packet rows; B18 STREAM_NOTES v2 dated 2026-10-11 23:34 UTC; own stage-3 STATUS and accepted audit. The lead's old A066/A067 baseline is already closed; protocol dispatch consumes the new A067 result matching our previous NEXT. A067 run20261014T020120Z CLAIMS/DERIVATION Sections1-4/REPORT; A070 run20261014T005025Z exact CLAIMS and DERIVATION Sections2-3, with Section1 read as context. EXECUTION_PROTOCOL {p['revision']} read in full. Source hashes/byte sizes in out/SOURCE_MANIFEST.json. No other agent checker code used. Prior own exact arithmetic imported with immutable source pin.

## complete derivation or exact first unsupported line

AUDIT.md gives complete independent derivations. The signed row polynomial is flat on four compatible or five incompatible cells; one normalized complete law covers every nonempty control subset and every core row. Its cross entropy pays h2(alpha)+alpha log2 M plus cell cardinalities bounded by2I_Z. Boolean final-mask isoperimetry and final-edge ownership pay alpha<=I_Z and h2(alpha)<=2(I_X+I_Z). Add the already accepted real channel2I_Z/ln2. All actual leaves remain. Terminal U/degree-two corollaries and all-dimensional cell cardinality/phase cases are proved explicitly.

A070's refund/physical conversion is independently reconstructed from conditional-resampling disagreements and actual edge XOR. Its four-bit retained-core witness has banks49/2,14,-59/2, summing9; dropping source/mask banks is invalid. Real normalized product subadditivity fails by exact integer gap571100.

One source prose sentence incorrectly says the11 cell always has zero mass; this holds only in the incompatible case. The same source already proves the correct compatible pq term, and its theorem/reference do not rely on zero11 mass. This is documented without a substantive proof repair.

The strongest normalized-real seed relaxation preserves norm-one actual children and the entire flat-cell row algebra; eight admissible cases violate core ownership. The rational norm-one degree-one seed(4095+128x)/4097, empty edit, has U=0,H/I>10>K, refuting real terminal/degree-two extensions. No bare real access inequality failure was certified on the finite grid; its unrestricted extension remains undecided. None refutes Boolean FEI.

No unsupported line remains in either stated theorem. The universal continuation first needs an exclusive actual child surplus for the retained2I_X reserve: assuming only H(child)<=C I(child) yields K I_Z+(C+2)I_X, not a same-C induction. A control-dependent source also needs a common output reference retaining all signed banks; A070's g=q*y witness is outside A067's seed hypothesis.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs were written before each job. Main domain: all ordered two-bit controller pairs whose fixed-set union is the whole control block; all one-bit Boolean g,A,B; XOR/OR. Add eight explicit controller geometries at r=3,4,5 with all one-bit core flags/seeds, and three fixed r3 geometries with all two-bit core flags/seeds. No symmetry reduction or automatic dimension growth; maximum enumerated dimension6. Filter the final fiber cap, not individual edit caps. Full: {full['raw_inputs']} raw inputs, {full['valid_boolean_cases']} valid Boolean cases, {full['outside_cap_rejected']} outside-cap rejections, {full['exact_assertions']} exact assertions, runtime {full['runtime_seconds']:.4f}s. These are seed/domain/controller executions, not claimed distinct Boolean functions. Pilot128 inputs passed {pilot['exact_assertions']} assertions in {pilot['runtime_seconds']:.4f}s. Full frozen cap300s, pilot60s; no timing overrun.

Integer/rational Walsh spectra, actual physical derivatives, exact row-cell squared coefficient equality, normalized reference coverage, direct resampling-pair versus physical-edge refunds, and retained actual leaf U/entropy are independently checked. Cardinality payment is certified as |C|^|C|<=2^(2sum_C degree), with integer powers. Prime-log entropy maps cancel identities exactly; signs use24-term positive atanh enclosures with proved rational tails and outward2^-80 rounding. Floating point appears only in elapsed time. The analytic proof supplies all dimensions and controller widths.

Real diagnostic:1024 prescribed flag/mode/controller inputs, {real['valid_real_cases']} cap-admissible cases, {real['flat_cell_checks']} exact row-cell equalities, {real['real_ownership_failures']} ownership failures, no certified bare-Q failure, runtime {real['runtime_seconds']:.4f}s. First ownership witness has13/18<3/4. The rational terminal guard uses p=16384/16785409<1/1024 and ln2>842/1215, log2 5<5/2. Pilot repetitions are not added to primary assertion counts.

Commands:

    python -X utf8 runs/{run}/code/check.py pilot
    python -X utf8 runs/{run}/code/check.py full
    python -X utf8 runs/{run}/code/real_scope.py

Estimated memory <=100MB per job; >300MB memok gate not triggered. One mathematical job at a time, no GPU, daemon, windows, unrelated process termination or expanded large-core table.

## proof dependencies and changed downstream conclusions

A067 uses prior independently accepted bounded-fiber v1 only for channel/restriction/ownership fragments, with no cardinality hypothesis reapplied; its complete-cell reference is reconstructed here. Optional terminals use previously accepted local Boolean granularity v1. A070's new exact conversion claim is self-contained; no new acceptance of its broader A069 decoder chain is asserted. Original statement/hypotheses/hashes preserved with local independent review receipts; no coauthored repair or new broad candidate opened.

This independently closes the previous NEXT's two-fixed-controller label loss, including unequal widths, overlapping/incompatible assignments, XOR/OR cancellation and positive reference mass on unoccupied cells. It separates real-valued flat-cell algebra from genuine Boolean final influence and leaf payments. Shared reference and core reserve remain distinct: retaining both terminal costs does not justify spending the reserve recursively. Local acceptance is recorded; B20 adoption, supervisor copies and mirrors are unverified.

## one next mathematical action and independent reviewer

{next_action} This consumes the now-checked cancellation boundary and targets the actual unpaid reserve rather than repeating the completed large-fiber class proof. FullFEI requires a noncircular surplus/transfer, not another terminal U assumption.

## actual persistence receipts or precise save blocker

The four required protocol files, AUDIT, frozen specifications, code and exact outputs are confined to the prescribed A088 run. out/SAVE_RECEIPT.json records actual local artifact SHA256/size and readback checks; exact JSON field sets, unchanged source hashes and identical PROGRESS/PACKET_DELTA are verified. Rolling STATUS has two lines; WORKLOG appended and LEARNED updated. Every file below20MB. No other agent/shared tree/brain/git/mail/trading directory written. Local persistence complete; external propagation unverified.

## Universal bridge

C019 gains independent acceptance of a single complete five-cell reference removing the previous r/(r-log2 k) loss for two arbitrarily wide fixed subcube controllers: accessK<19/2 (compatibleK<9), one owned final-core reserve, all actual terminal costs retained. This closes the specified structured access gap but leaves the universal2I_X reserve and arbitrary terminal payment unclosed; same-C child induction alone yieldsC+2 on the core. NEXT tests a single source-compatible conditional reference with an exclusive signed child surplus on the already-certified cancellation witness, the shortest route to a reusable universal stopping-tree ledger rather than another isolated class census.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A088 stage4 complete locally: A067 two-subcube reference and A070 signed conversion HOLD;14068 Boolean cases/349542 exact assertions; real ownership/degree-one terminal extensions refuted; FEI OPEN.\nNEXT: Audit one control-dependent common-reference transfer with both terminal cores and exclusive child slack for2I_X; preserve A070 cancellation banks; A094/A070 review.\n',encoding='utf-8')
date=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{date} — {run}: independently accepted A067 complete five-cell two-controller access and A070 refund/conversion v1 without repair.35840 inputs/14068 cap-valid Boolean cases/349542 exact assertions; full78.3958s, pilot0.0183s. Real499 valid cases/7984 flat-cell equalities/8 ownership failures; rational degree-one U=0 seedH/I>10>K. The11-zero source sentence is only valid for incompatible assignments; actual proof handles compatible11. Universal same-C induction leaves2I_X unpaid; NEXT exclusive child-slack/shared-reference transfer. All files saved locally; remote adoption unverified.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage4: Two globally fixed subcube controllers admit a common complete four-cell compatible/five-cell incompatible Fourier reference; log-cardinality<=2conditional mean degree, so accessK<19/2 (<9 compatible) with one2I_X reserve. Independent A088 acceptance of A067 v1. The flat-cell row polynomial is general-real algebra; genuine Boolean steps are g²=1, final pivot probabilityp versus1-p, and leaf granularity. Real seedvalues(1,-1/3,5/3,1/3) can give13/18<3/4 ownership failure even with fixed controller geometry. Norm-one degree-one Fourier seed(4095/4097,128/4097) hasU=0,H/I>10 and refutes real terminal extensions. A070 cancellationg=q*y under fixed tree gives banks49/2,14,-59/2 totaling9; all source/mask banks and terminalcore must remain. A bare childH<=C I induction producesK I_Z+(C+2)I_X: exclusive reserve slack is still needed. Source prose11-zero remark is only incompatible; correct compatible proof already haspq and is accepted unchanged.\n')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text().splitlines())==2
receipt=[]
for path in sorted(R.rglob('*')):
    if path.is_file() and path.name!='SAVE_RECEIPT.json':
        data=path.read_bytes(); assert len(data)<20*1024*1024
        receipt.append({'path':str(path.relative_to(R)),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
write(R/'out/SAVE_RECEIPT.json',{'local_artifacts':receipt,'schema':'PASS','source_statement_hashes':'PASS','remote_mirror':'UNVERIFIED'})
print(json.dumps({'artifact_hashes':len(receipt),'claims':len(records),'schema':'PASS','source_hashes':'PASS','primary_boolean_assertions':full['exact_assertions']}))
