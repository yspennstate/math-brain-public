from pathlib import Path
import hashlib, json, re

RUN=Path(__file__).resolve().parents[1]
ROOT=RUN.parents[1]
PROTOCOL_PATH=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(PROTOCOL_PATH.read_text(encoding='utf-8'))
required=protocol['required_per_run']
progress_fields=[s.split(' (')[0] for s in required['progress_fields']]
run_id=RUN.name

def save(path,value):
    path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

report=(RUN/'REPORT.md').read_text(encoding='utf-8')
headings=re.findall(r'^# (.+)$',report,re.M)
assert headings==required['report_fields'],(headings,required['report_fields'])
manifest=json.loads((RUN/'out'/'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
checks=json.loads((RUN/'out'/'EXACT_CHECK_n3.json').read_text(encoding='utf-8'))
assert checks['cases']==278 and checks['assertions']==7592 and checks['failures']==0
inventory=[]
for line in report.splitlines():
    if re.match(r'^\| (T\d\d|R\d\d|P\d\d) \|',line):
        cells=[s.strip() for s in line.strip('|').split('|')]
        assert len(cells)==4
        inventory.append(dict(route_id=cells[0],classification_and_scope=cells[1],source_locator=cells[2],first_unproved_implication=cells[3]))
assert len(inventory)==37,len(inventory)
save(RUN/'out'/'SUFFICIENT_CONDITIONS.json',inventory)
(RUN/'TARGET_QUANTIFIERS.md').write_text(report.split('# sources actually read, revisions and theorem locators')[0],encoding='utf-8')
save(RUN/'GAP_MAP.json',dict(
    target='exists C finite, forall n>=0, forall Boolean signs on the uniform n-cube: H2<=C I; constants H=I=0',
    source_manifest='out/SOURCE_MANIFEST.json',manuscript_routes=inventory,
    universal_unpaid_leaves=[
        dict(gap_id='G-J-COST',route_ids=['T07','R03','R04'],classification='ONE_WAY_SUFFICIENT',unpaid='Complete posterior residual <=K I with one global admissible representation/reference'),
        dict(gap_id='G-R-SELECT',route_ids=['R05','R06','R08'],classification='R06_EQUIVALENT_IN_FINITENESS; R05_AND_R08_SUFFICIENT',unpaid='A paid relevant split at every reached nonconstant function'),
        dict(gap_id='G-R-MISMATCH',route_ids=['R07'],classification='ONE_WAY_SUFFICIENT',unpaid='Entire actual-tree logarithmic mismatch/KL charge plus terminal entropy without budget reuse'),
        dict(gap_id='G-BOOLEANITY',classification='OPEN_MECHANISM',unpaid='Entropy payment from full signed Booleanity beyond refuted finite-prefix relaxations'),
        dict(gap_id='G-PHASE-COND',classification='FIXED_REALIZED_MARGINAL_WITH_ARBITRARY_DATA_TENSORS_IS_FEI_STRENGTH',unpaid='Conditional spectrum entropy; prove a structural exclusion of arbitrary tensor factors for an easier class'),
        dict(gap_id='G-BIASED-LTF',route_ids=['T15'],classification='OPEN_CLASS_EXTENSION',unpaid='Corrected biased weighted threshold FEI+; physical reuse is a separate universal gap'),
        dict(gap_id='G-LOWSEL-COLLISION',route_ids=['T18','T19'],classification='OPEN_CLASS_EXTENSION',unpaid='Collision payment when I_sel/a vanishes or selector coordinates are reused'),
        dict(gap_id='A001-DYADIC-GATE-POTENTIAL',route_ids=['R09'],classification='EXACT_EQUIVALENCE_AT_FIXED_C',unpaid='Construct nonnegative symmetric dyadic Gamma with all-gate inequality without assuming FEI'),
        dict(gap_id='A001-ACTUAL-HISTORY-TRANSFER',classification='FEI_EQUIVALENT_IN_FINITENESS_CONDITIONAL_ON_SOURCE_IDENTITIES',unpaid='Universal actual-source integrated path cost <=K I'),
        dict(gap_id='A001-WEIGHTED-REVEAL-LIFETIME',classification='INSUFFICIENT_ALONE',unpaid='Dimension-uniform weighted TC lifetime under prescribed policy plus separate entropy-transfer obligation')],
    review_packets=['A086','A094'],consumers=['A003','A004','A005','A081','A093','B20'],
    full_fei_status='OPEN'))

def claim(cid,statement,hypotheses,status,proof,deps,gap,consumers):
    result=dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=hypotheses,
        statement_sha256=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
        contributors=['A001/fleet05'],proof_source=proof,proof_dependencies=deps,review_records=[],
        status=status,supersedes=[],refutes=[],first_unproved_line=gap,next_consumers=consumers)
    assert set(result)==set(required['claim_fields'])
    return result

claims=[claim('A001-UNIVERSAL-QUANTIFIER-AND-GAP-MAP',
    'FEI is exists finite C, for every finite n and every Boolean sign f, H2(f)<=C I(f), including constants with H=I=0. The 37 inventoried manuscript interfaces separate proper-class theorems, one-way sufficient payments and proved equivalences; no audited interface establishes finiteness of C_FEI.',
    ['Uniform physical cube','Fourier entropy in bits','Source locators and byte pins in REPORT.md and out/SOURCE_MANIFEST.json','Recovered class proofs are not all independently reconstructed by this audit'],
    'SOURCE_BOUND_AUDIT_COMPLETE_PENDING_INDEPENDENT_REVIEW',
    {'path':'REPORT.md','inventory':'out/SUFFICIENT_CONDITIONS.json','manifest':'out/SOURCE_MANIFEST.json'},
    [{'source':entry['path'],'sha256':entry['sha256']} for entry in manifest if '/reductions/' in entry['path'].replace('\\','/') or entry['path'].endswith('threshold_paper_38pp.txt') or entry['path'].endswith('percolation_spectral_pivotal_entropy_30pp.txt')],
    'A dimension-independent payment for the universal posterior residual, hereditary erasure selection, gate potential, or actual-source history remains unpaid; see each route separately.',
    ['A003','A005','A006','A026','A041','A064','A086','A094','B20']),
    claim('A001-FIXED-BOOLEAN-MARGINAL-TENSOR-ADMISSION',
    'Fix any actual Boolean F0(X,Y0) on disjoint finite input groups and its X spectral marginal. Among Boolean functions with that fixed marginal and admitting fresh arbitrary data tensor factors, the optimal constant in H(S_Y|S_X)<=C I equals C_FEI as an extended-real supremum. Any fixed upper X-degree bound obeyed by F0 is preserved by the embedding.',
    ['F0 is an actual Boolean sign with normalized squared Fourier law','Fresh independent uniform data blocks are admitted without structural exclusion','Entropy in bits; I is full physical influence','The fixed marginal class has no constraint prohibiting tensoring F0 with an arbitrary Boolean seed'],
    'ANALYTIC_PROOF_COMPLETE_PENDING_INDEPENDENT_REVIEW',
    {'path':'REPORT.md','locator':'Fixed conditional marginal admission'},
    [{'source':'Disjoint tensor Fourier factorization','proof':'Explicit Hconditional=c0+tH(f), I=I(F0)+tI(f) in REPORT.md'}],
    None,['A005','A034','A079','A086','A094','B20'])]
save(RUN/'CLAIMS.json',claims)
progress=dict(protocol_revision=protocol['revision'],run_id=run_id,stream='B01',packet_id='A001',
    gap_id='G-J-COST',attempt_id='A001-QUANTIFIER-AUDIT-1',method='Source-bound theorem and quantifier inventory; analytic implication reconstruction; exact finite Walsh/log identity validation',
    mathematical_delta='Pinned 37 interfaces from threshold, reductions and geometric manuscripts; isolated first unpaid implications; reconstructed good-coordinate and dyadic gate-potential equivalences; proved general fixed-marginal tensor admission; exact checks passed for 278 Boolean truth tables.',
    deliverable_status='COMPLETE_LOCAL_PENDING_INDEPENDENT_REVIEW_AND_SUPERVISOR_ADOPTION',
    mathematical_status='BASELINE_AUDIT_COMPLETE; NARROW_TENSOR_ADMISSION_PROVED_PENDING_REVIEW; FULL_FEI_OPEN',
    claim_versions_used=['B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO@1 (scoped obstruction only)','B09-BIASED-BLOCK-UNCERTAINTY@1 (pending review; not an accepted proof dependency)','B09-TAXFREE-AND-COUNTEREXAMPLE-REPAIRED@1 (scoped obstruction only)'],
    claims_created_or_changed=[c['claim_id']+'@1' for c in claims],
    source_artifacts=[{'manifest':'out/SOURCE_MANIFEST.json','files':len(manifest)},'REPORT.md','out/SUFFICIENT_CONDITIONS.json','out/FROZEN_SPEC.json','out/EXACT_CHECK_n2.json','out/EXACT_CHECK_n3.json'],
    next_consumers=['A003','A005','A006','A026','A034','A041','A064','A086','A094','B20'],
    next_action='A003: freeze an admissible complete posterior-forest representation on a new low-selector-energy or rare-core family and compute every residual term. A086/A094: independently reconstruct quantifier directions and tensor admission.',
    stagnant_substantive_attempts=0,blockers=['B01 STREAM_NOTES.md absent at prescribed path; independent audit continues','Independent review and supervisor/mirror adoption not yet performed'],packet_ids=['A001'])
assert set(progress)==set(progress_fields)
save(RUN/'PROGRESS.json',progress); save(RUN/'PACKET_DELTA.json',progress)
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()

# Preserve the three durable rolling files and append this completed result once.
(ROOT/'STATUS.md').write_text('STATE: A001 quantifier audit complete locally; 37 routes pinned, 7,592 exact assertions passed; full FEI OPEN; review/adoption pending.\nNEXT: A086/A094 review implication graph and tensor admission; A003 compute complete posterior residual on a new low-energy family.\n',encoding='utf-8')
for name,entry in [
    ('WORKLOG.md','2026-10-12: Completed audit of 37 sufficient-condition/reduction interfaces. Exact exhaustive identity validation n<=3: 278 labelled Boolean functions, 7,592 assertions, no failures, about 40.17 seconds. Saved required protocol-shaped run files and input/output manifests. Full FEI remains open; no external acceptance/adoption claimed.\n'),
    ('LEARNED.md','Universal good-coordinate B_i<=K I_i is equivalent to FEI in finiteness, with forward coefficient K+2/ln2; optimal constants need not match. Delta_i selection is recorded as a sufficient hereditary route. The posterior residual is sufficient only, with complete global weights and actual distinct-run posterior cost.\nDyadic gate potential is an exact FEI(C) equivalence on finite uniform encoder probabilities; an all-real-bias extension is a separate obligation. For any actual Boolean base with fixed X spectral marginal, unrestricted fresh data tensors retain C_FEI in the conditional completion endpoint; prove exclusion of those tensors before claiming easier scope.\nPercolation local guards and pivotal entropy statements are lower bounds; only spatial occupancy plus arm estimates and influence comparison supply FEI upper bounds.\n')]:
    p=ROOT/name
    if entry not in p.read_text(encoding='utf-8'):
        with p.open('a',encoding='utf-8') as file: file.write(entry)

receipts=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and p.name not in ['ARTIFACT_RECEIPTS.json','FINAL_VALIDATION.json']:
        raw=p.read_bytes(); assert len(raw)<20*1024*1024
        receipts.append(dict(path=str(p.relative_to(RUN)),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()))
save(RUN/'out'/'ARTIFACT_RECEIPTS.json',receipts)
result=dict(report_fields='PASS',claim_fields='PASS',progress_fields='PASS',statement_hashes='PASS',compatibility_copy='BYTE_IDENTICAL',size_cap='PASS',inventory_routes=len(inventory),exact_assertions=checks['assertions'],source_files=len(manifest),saved_artifacts=len(receipts),independent_review='PENDING',supervisor_adoption='NOT_CLAIMED',full_fei='OPEN')
save(RUN/'out'/'FINAL_VALIDATION.json',result)
print(json.dumps(result))
