from pathlib import Path
from datetime import datetime,timezone
import json,hashlib

R=Path(__file__).resolve().parents[1]; HOME=R.parents[1]
SRC=HOME.parent/'A012'/'runs'/'20261021T212009Z-account03-A012-sparse-activation-accounting'
BASE=Path(r'~\mop_fei100');CTX=Path(r'context')
REPORTS=BASE/'reports'/'fei-2026-10-11';SUP=BASE/'research_pushes'/'2026-10-11-full-fei-100-agents'
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
now=datetime.now(timezone.utc).isoformat();run=R.name
results={n:load(R/'out'/n) for n in ('CONTINUUM_REPLAY.json','BOOLEAN_REPLAY.json','FOUR_BIT_BOUNDARY.json')}
assert all(x['status']=='PASS' for x in results.values())
count=sum(x['checks'] for x in results.values());assert count==42000
assert results['CONTINUUM_REPLAY.json']['leaves']==1326
assert results['CONTINUUM_REPLAY.json']['analytic_boxes']==384
assert results['BOOLEAN_REPLAY.json']['cases']==2048

sources=[REPORTS/n for n in ('EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex')]
sources += [SUP/n for n in ('CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md')]
sources += sorted((SUP/'sources').glob('*.md'))+sorted(CTX.glob('*.txt'))
sources += [HOME.parent.parent/'BOARD.md',HOME.parent.parent/'claude'/'B03'/'STREAM_NOTES.md']
sources += [SRC/n for n in ('REPORT.md','DERIVATION.md','CLAIMS.json','PROGRESS.json')]
sources += list((SRC/'code').glob('*.py'))+list((SRC/'out').glob('CONTINUUM_*.json'))
sources += [HOME/'runs'/'20261014T051241Z-account05-A013-representation-stability'/n for n in ('REPORT.md','DERIVATION.md','CLAIMS.json')]
receipts=[];excerpts=[]
for p in sources:
    raw=p.read_bytes()
    try:
        txt=raw.decode('utf-8-sig');decoding='strict UTF-8'
    except UnicodeDecodeError:
        # Archived PDF extractions are not all UTF-8. Preserve exact bytes/hash;
        # diagnostic excerpts alone use replacement, never a theorem premise.
        txt=raw.decode('utf-8-sig',errors='replace');decoding='non-UTF8 archive; display-only replacement; raw bytes unchanged'
    receipts.append(dict(path=str(p),bytes=len(raw),sha256=sha(raw),decoding=decoding))
    if p.suffix in ('.txt','.md','.tex') and 'CONTINUUM_' not in p.name:
        lines=txt.splitlines();hits=[(i+1,s) for i,s in enumerate(lines) if any(k in s.lower() for k in ('shared-data','proposition 8.6','selector','overlap','a013','universal','abstract'))]
        excerpts.append(dict(path=str(p),line_count=len(lines),selected_lines=hits[:16]))
dump(R/'out'/'SOURCE_RECEIPTS.json',receipts);dump(R/'out'/'SOURCE_EXCERPTS.json',excerpts)
dump(R/'out'/'LEAN_ADMISSION.json',dict(status='NOT_RUN_MEMORY_ADMISSION_REFUSED',command='python -X utf8 tools\\memok.py',observed_exit_code=1,observed_output='WAIT: physical free 1.7 GB (need 4.0), commit free 5.0 GB (need 8.0)',source='code/QuadraticChord.lean',meaning='Source only. No compiler pass or Lean-checked mathematics.'))
dump(R/'out'/'EXACT_RESULTS.json',dict(status='PASS',total_exact_assertions=count,results=results,lean='NOT_RUN_MEMORY_ADMISSION_REFUSED',full_FEI='OPEN'))

report=f'''# A013 stage17: scoped independent review of three-row stability

## exact target, quantifiers, hypotheses and units

Review the NEW v5 increment of A012-DISJOINT-PRIVATE-MUX-ADMISSION: every Boolean phase on three shared bits, three distinct edited rows, arbitrary correlated private events on an independent finite private cube, and a fresh physical selector. Verify B_z<4d at d>0, the complete surcharge Kd with K=4+2/ln2<7, both actual child references and one influence owner. Bits throughout. This consumes the new dependency rather than opening another broad candidate. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Execution protocol v2 read in full; BOARD snapshot2026-10-22 20:25 UTC, B03 lead notes v2 and own STATUS/LEARNED/WORKLOG; A012 stage17 REPORT, DERIVATION Sections1-6, CLAIMS@5 and both author arithmetic implementations; A013 stage5 proof and report. Campaign README/CURRENT_STATUS, claim/obstruction/packet/action indices, plan B03 contracts and supplemental seed/interface/control notes inspected at relevant locators. Threshold38pp Proposition8.6 shared-data identity read directly; other threshold/percolation versions and supplemental sources inspected for baseline context, with selected locators in SOURCE_EXCERPTS. Earlier paper intake is inherited; no new full-paper reading is asserted. A single read-only math-recall search returned weak neighboring controls, used as no theorem premise. SOURCE_RECEIPTS records source hashes. Older source snapshots end21Oct; the current user deadline23Oct14:49UTC governs. No web, git, mail, brain writes, or other-agent mutations.

## complete derivation or exact first unsupported line

DERIVATION Sections1-3 independently reconstruct the exact joint private-mass identity, Gibbs tangent, nonnegative quadratic coefficient, complete dyadic cover and normalized reference debt D_F=D_Hcal/2. All1,326 saved tangent boxes and384 analytic boxes are independently certified using outward binary-squaring logarithms, without importing source code. Both private correlation and off-support reference mass remain. Verdict HOLDS for the NEW v5 three-row collision/reference increment. Since A013 supplied earlier credited inputs, this is explicitly not independent full-chain acceptance of all inherited v1-v4 syntax or nonmember claims.

Section4 gives a checked scope control: four-bit quadratic bent phase versus its origin flip has d=1/16, B_z>4d and Delta_z>7d. This is an explicit instance of the existing bent obstruction, not a new full-FEI counterfamily. First unsupported line: arbitrary three-bit conditional means with four-to-eight independently varying rows reduce to at most three rows or obey a complete all-row tangent payment. For growing overlap, the four-bit witness already requires unused shared/terminal surplus rather than selector-only transfer at K<7.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede execution: FROZEN_SPEC and FROZEN_BOUNDARY. Commands: `python -X utf8 code/replay.py continuum`, `fixtures`, `boundary`. Exact total {count:,} assertions PASS: 15,113 continuum/classification/coverage checks; 26,880 actual Boolean/reference checks on2,048 six-bit parents with all256 phases and8 correlated-event triples (128 full calibrated-reference cases);7 four-bit boundary predicates. Binary logs use160-bit outward interval squaring and64-bit upper bounds, independent of both source atanh-series implementations. Fixtures use integer Walsh, Fraction probabilities and exact rational prime-log signatures. The continuum proof, rather than finite fixtures, supplies all-real probabilities and arbitrary private dimension. Minimum gap and observed run times are in EXACT_RESULTS.

All mathematical jobs have50s internal caps and estimated memory below80MB; no dimension escalation or GPU. Before a possible compiler job, memok exited1: physical free1.7GB versus4.0 required, commit free5.0GB versus8.0 required. Lean compilation was therefore not launched; saved QuadraticChord.lean is source only. No numerical or runtime failure is counted as proof. The UTF-8 hook initially held a command already specifying UTF-8; the exact command was retried with the required acknowledgment and then executed. All launched mathematical jobs have returned; no new persistent worker was created.

## proof dependencies and changed downstream conclusions

Uses A012@5 new theorem, its precisely scoped inherited@4 grammar interface, earlier A013 two-row/rare-moderate derivations, and C005 scalar JS only for converting B to Delta. New v5 collision and complete-reference increment independently HOLDS at that scope. This clears a review dependency for A012/A086/A094; it does not independently accept the complete earlier grammar chain, original queue contraction, free terminal debt, universal admission, or full FEI. The four-bit scope control forbids extending the SAME local constant without another source of payment. Physical gate count, labels and root density updates are explicit in DERIVATION Section3 and STABILITY_LEDGER.

## one next mathematical action and independent reviewer

Apply the dimension-free tangent/corner lemma to four-to-eight varying rows on the SAME three-bit shared cube, retaining both complete private references and the single selector owner. For growing width, price a selected actual query from unused shared/terminal surplus rather than the refuted local surcharge. A086/A094 independently audit the new scoped review and four-bit boundary; A012 consumes the reconstruction.

## actual persistence receipts or precise save blocker

The four protocol files, full derivation, independent script, frozen specs, exact outputs, source receipts, auxiliary Lean source and local persistence manifest are saved in this run. finalize.py checks exact protocol field sets, claim hashes, all PASS outputs, identical PACKET_DELTA and current two-line STATUS. Rolling WORKLOG/LEARNED append the result. All artifacts stay below20MB. Supervisor copying, remote mirror and downstream use are unobserved. No write outside A013 is part of this result package.

## Universal bridge

This stage advances C020 whole-set witness cost and C024 history transfer by independently validating the new all-probability three-row complete-reference transfer at unchanged K<7, with one physical influence owner and both terminal bills. It also fixes the next boundary: a four-shared-bit Boolean instance already has Delta>7d, so growing overlap must use genuinely unused shared/terminal surplus. The universal bridge remains open at arbitrary three-bit conditional profiles and then nonreused wider-overlap payment. NEXT attacks that exact missing admission statement with the now-validated tangent mechanism, rather than adding another isolated class or renaming FEI.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
statements=[
('A013-SCOPED-REVIEW-A012-V5', 'The NEW three-row collision and full-reference increment of A012-DISJOINT-PRIVATE-MUX-ADMISSION@5 holds: for all pure shared three-bit phases and three distinct row edits with arbitrary correlated private events, B_z<4d for d>0 (zero at d=0), and the normalized calibrated parent reference retains D_F=D_Hcal/2 and complete child debt. Independent binary-squaring logarithms certify the entire saved probability-cube cover. This is not independent acceptance of the earlier A013-credited grammar chain.', 'SCOPED_INDEPENDENT_RECONSTRUCTION_HOLDS_NEW_INCREMENT; FULL_CHAIN_NOT_INDEPENDENTLY_ACCEPTED'),
('A013-FOUR-SHARED-BIT-LOCAL-BOUNDARY', 'For c(s)=(-1)^(s0s1+s2s3), h=c with the origin sign flipped, and F=mux_z(c,h), d=1/16, B_z>4d and Delta_z=3+(9/64)log2(3)-(75/64)log2(5)>7d; I(F)=37/16. Thus the three-bit selector-only K<7 payment does not extend to four shared bits without another source of payment. This actual Boolean scope control instantiates the existing bent-edit obstruction and is not a counterexample to FEI.', 'EXACT_SCOPE_CONTROL_OF_EXISTING_OBSTRUCTION')]
claims=[]
for cid,stmt,status in statements:
    claims.append(dict(claim_id=cid,version=1,exact_statement=stmt,hypotheses=['finite uniform Boolean cubes; bit entropy','fresh selector; exact correlated private law; source theorem requires one pure shared child of width at most three','review scope is new v5 increment only; boundary instead has four shared bits'],statement_sha256=sha(stmt.encode('utf-8')),contributors=['A013/account03'],proof_source={'derivation':'DERIVATION.md','replay':'code/replay.py','outputs':'out/EXACT_RESULTS.json'},proof_dependencies=[{'claim_id':'A012-DISJOINT-PRIVATE-MUX-ADMISSION','version':5,'scope':'new increment reviewed; full inherited chain not accepted'},{'claim_id':'C005','version':'baseline','scope':'scalar JS only'}] if 'REVIEW' in cid else [],review_records=[{'reviewer':'A013','verdict':'HOLDS_NEW_V5_INCREMENT_ONLY','independence':'new algebra and binary logarithm implementation; earlier A013 credit excludes full-chain acceptance'}] if 'REVIEW' in cid else [],status=status,supersedes=[],refutes=['extension of selector-only Delta<=7d from three to four shared bits'] if 'BOUNDARY' in cid else [],first_unproved_line=None,next_consumers=['A012','A086','A094','B03','B20']))
dump(R/'CLAIMS.json',claims)
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=run,stream='B03',packet_id='A013',gap_id='G-LOWSEL-COLLISION',attempt_id='A013-stage17-scoped-review-three-row',method='Independent algebra; binary-logarithm continuum certificate replay; exact joint-private reference identities; actual four-shared-bit boundary control',mathematical_delta='NEW A012@5 three-row increment independently reconstructed at scoped level;42,000 exact assertions;Delta>7d for explicit four-shared-bit bent point edit; full FEI open',deliverable_status='COMPLETE_LOCAL',mathematical_status='SCOPED_PROOF_RECONSTRUCTED; UNIVERSAL_BRIDGE_OPEN; LEAN_NOT_RUN',claim_versions_used=['A012-DISJOINT-PRIVATE-MUX-ADMISSION@5 new increment; inherited@4 conditional','A013-TWO-ROW-ARBITRARY-EVENT-TRANSPORT@1 prior-input credit','C005 baseline scalar JS'],claims_created_or_changed=[x['claim_id']+'@1' for x in claims],source_artifacts=['DERIVATION.md','REPORT.md','code/replay.py','out/EXACT_RESULTS.json','out/SOURCE_RECEIPTS.json'],next_consumers=['A012','A086','A094','B03','B20'],next_action='Certify complete four-to-eight varying-row three-bit profiles with fixed joint private references and one selector owner; wider overlap needs unused shared/terminal surplus.',stagnant_substantive_attempts=0,blockers=['Full three-bit profile reduction/payment open','Lean compiler admission refused by memok exit1','No remote mirror or downstream-use receipt'],packet_ids=['A013'])
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
dump(R/'STABILITY_LEDGER.json',dict(gates='N_parent<=N_G+N_H; one selector literal incidence per cell',parent_density='pi_child/2 under fresh selector',physical_restriction='actual cofactor; discard contradictory cells, remove satisfied literals, recompute N and density',uniform_root_reference='r_j=pi_j/(N+pi_j); constants use vacuum',labels='full signed joint reference retained; D_F=D_Hcal/2, no independent factoring of private event labels',collision='B<4d only for certified three-bit rule; four-bit scope control Delta>7d',full_FEI='OPEN'))
status=HOME/'STATUS.md';(R/'out'/'INTAKE_STATUS.md').write_text(status.read_text(encoding='utf-8'),encoding='utf-8')
status.write_text('STATE: A013 stage17 saved: NEW A012 three-row v5 scoped HOLDS;42,000 exact checks;four-shared-bit Delta>7d boundary certified;Lean admission refused;FEI OPEN.\nNEXT: Pay complete four-to-eight varying-row three-bit profile with SAME joint private references/one selector owner;A086/A094 review scope;wider overlap needs unused shared/terminal surplus.\n',encoding='utf-8')
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} Stage17 {run}: independently reconstructed NEW A012@5 three-row continuum/reference increment only (earlier A013 inputs prevent full-chain independent acceptance);15,113 binary-log cover checks+26,880 exact Boolean/reference checks+7 four-bit scope predicates=42,000 PASS. Explicit four-shared-bit bent flip has Delta>7d, no FEI counterexample. memok exit1 withheld Lean compilation. Protocol files and rolling state saved locally; full three-bit all-row payment remains open.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage17: A012@5 NEW three-row arbitrary-correlated-event collision and complete-reference delta independently reconstructs at stated scope; do not count earlier A013-credited grammar as independent full-chain review. Saved cube1326 tangent+384 analytic boxes replay with binary interval-squaring logs (different from source atanh logs);42,000 exact predicates PASS. At four shared bits, c=(-1)^(s0s1+s2s3), h origin flip gives d=1/16 and Delta=3+9log2(3)/64-75log2(5)/64>7d, exactly 3^9*2^164>5^75; I=37/16. Thus width growth needs unused shared/terminal payment, not the three-bit local constant. Full all-row three-bit profile remains next. memok refused compiler admission: auxiliary Lean source is not Lean-checked.\n')
protocol=load(REPORTS/'EXECUTION_PROTOCOL.json')['required_per_run']
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert all(set(c)==set(protocol['claim_fields']) for c in claims)
assert load(R/'PROGRESS.json')==load(R/'PACKET_DELTA.json')
assert len(status.read_text(encoding='utf-8').splitlines())==2
for c in claims:assert c['statement_sha256']==sha(c['exact_statement'].encode('utf-8'))
files=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        raw=p.read_bytes();assert len(raw)<20_000_000;files.append(dict(path=str(p.relative_to(R)),bytes=len(raw),sha256=sha(raw)))
dump(R/'out'/'PERSISTENCE_RECEIPTS.json',dict(status='LOCAL_FILES_VALIDATED',at=now,total_assertions=count,files=files,mirror='UNOBSERVED',downstream_use='UNOBSERVED'))
print(json.dumps(dict(status='PASS',exact_assertions=count,protocol_fields='EXACT',claim_hashes='PASS',progress_delta='IDENTICAL',files=len(files),full_FEI='OPEN')))
