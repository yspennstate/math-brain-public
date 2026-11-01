from pathlib import Path
from fractions import Fraction as R
import json, hashlib, datetime, copy

ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
SHARED=AGENT.parents[1]
PROTOCOL=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
A075=SHARED/'agents/A075/runs/20261014T005346Z-fleet05-A075-search-to-theorem-bridge'
A072=SHARED/'agents/A072/runs/20261014T020611Z-fleet05-A072-exact-walsh-engine'
A080=SHARED/'agents/A080/runs/20261014T005622Z-fleet05-A080-universal-counterexample-standard'
PRIOR=AGENT/'runs/20261014T000747Z-fleet05-A084-continuum-parameters'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,o):p.write_text(json.dumps(o,indent=2),encoding='utf-8')
def hash_statement(c):
    return hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
def receipt(p):
    b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

protocol=read(PROTOCOL)
validation=read(ROOT/'out/VALIDATION.json')
assert validation['all_checks_passed'] and validation['exact_assertions']==8864
assert validation['physical_coefficient_checks']==8192
certificate_names=['LOW_Q_CERTIFICATE','COMPLEMENT_Q_CERTIFICATE','RARE_Q_LOWER','RARE_Q_UPPER','RARE_BIAS_CONTRACTION']
for name in certificate_names:
    cert=read(ROOT/'out'/(name+'.json'));leaves=cert['leaves']
    assert len(leaves)==32
    assert leaves[0]['box'][0]==cert['domain'][0] and leaves[-1]['box'][1]==cert['domain'][1]
    for a,b in zip(leaves,leaves[1:]):assert a['box'][1]==b['box'][0]
    for leaf in leaves:
        lower=min(map(R,leaf['Bernstein_coefficients']))
        assert lower>0 if cert['strict'] else lower>=0
sources=[PROTOCOL,SHARED/'BOARD.md',SHARED/'claude/B17/STREAM_NOTES.md',AGENT/'STATUS.md',
    A075/'REPORT.md',A075/'PROOF.md',A075/'CLAIMS.json',A075/'code/finalize.py',A072/'REPORT.md',A080/'REPORT.md',
    SHARED/'agents/A089/STATUS.md',PRIOR/'REPORT.md',PRIOR/'PROOF.md',PRIOR/'CLAIMS.json',PRIOR/'code/certify_continuum.py']
save(ROOT/'out/SOURCE_RECEIPTS.json',[dict(receipt(p),role='Read-only input; bytes at finalization, mutable board/status not an immutable historical snapshot') for p in sources])

source_claims=read(A075/'CLAIMS.json')
accepted=copy.deepcopy(next(c for c in source_claims if c['claim_id']=='A084-F6-CONTINUUM-ADMISSION'))
assert accepted['version']==1 and accepted['statement_sha256']==hash_statement(accepted)
assert accepted['statement_sha256']=='8d2b6527e00bd11aaf450db42698c225c13e55f4cad5106c53bfc1ccda5afa27'
assert accepted['exact_statement']==read(PRIOR/'CLAIMS.json')[0]['exact_statement']
accepted['status']='INDEPENDENT_ACCEPTANCE_BY_A075_CONSUMED_WITH_SOURCE_PROVENANCE'
precursor=next(c for c in source_claims if c['claim_id']=='A075-RARE-CORE-LOCALIZATION')
assert precursor['statement_sha256']==hashlib.sha256(precursor['exact_statement'].encode()).hexdigest()
assert precursor['statement_sha256']=='4a2c5d8837c0f46e95515ea964fee828e46ac32633ab16ed7ab3810f590a45fc'
save(ROOT/'out/SOURCE_HASH_CONVENTIONS.json',{'A075-RARE-CORE-LOCALIZATION@1':{'stored_hash':precursor['statement_sha256'],'verified_convention':'SHA256 of UTF8 exact_statement alone, as in source code/finalize.py','supplemental_statement_and_hypotheses_hash':hash_statement(precursor)},'A084-F6-CONTINUUM-ADMISSION@1':{'stored_hash':accepted['statement_sha256'],'verified_convention':'SHA256 canonical JSON of statement and hypotheses'},'source_statement_modified':False})

statement=('Let h be the six-bit Boolean sign negative exactly at binary indices {0,1,2,4,8,16,32,6,17,40}, a one bit denoting a negative input. '
    'For every nonconstant Boolean core g_0 on every finite uniform cube, define a finite-depth policy by orienting its minority output to -1, substituting six disjoint identical copies in that orientation when minority s<=7/32 and in its complement otherwise, and reorienting the output to its minority before the next level. '
    'For every finite depth d>=0, -2074/105<=H(g_d)/I(g_d)-H(g_0)/I(g_0)<=248/3, with true squared-spectrum entropy in bits and physical total influence. '
    'The moderate prefix alone has complete signed normalized entropy correction in [-314/21,200/3]. '
    'The exact identity H(g_(k+1))=Q_k H(g_k)+C_k, I(g_(k+1))=Q_k I(g_k), Q=12p(1-p)^3(2-p), C=H_p(h)-Q h2(4p(1-p)), retains the whole starting entropy, and every level correction C_k/(Q_k I(g_k)) is counted once. '
    'There is at most one low-moderate run and at most two complemented levels before the absorbing rare phase; no uniform number of low-moderate levels is required. '
    'These are additive composition bounds relative to the unknown starting ratio, not an absolute FEI constant or a physical restriction-tree payment, and do not price arbitrary alternating one-flip escape cycles.')
hypotheses=['Actual nonconstant Boolean core on an arbitrary finite uniform physical cube',
    'Fixed gate, identical copies on six disjoint blocks, and specified common orientation at each level',
    'Every depth is finite; all resulting influences are strictly positive',
    'Entropy in bits of the full squared Fourier spectrum, and true physical total influence',
    'No restriction to a finite bias grid or a finite dimension range; balanced tie may be oriented either way']
consumers=['A075','A071','A072','A089','A074','A092','A080','A090','A094','B15','B17','B20']
claim={'claim_id':'A084-F6-FULL-NORMALIZED-ENTROPY-BUDGET','version':1,
    'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':'','contributors':['A084'],
    'proof_source':{'proof':str(ROOT/'PROOF.md'),'report':str(ROOT/'REPORT.md'),
        'certificates':['out/'+name+'.json' for name in certificate_names],
        'validation':['out/VALIDATION.json','out/ALGEBRA.json','out/PHYSICAL_1.json','out/PHYSICAL_6.json','out/TRAJECTORY_FIXTURES.json']},
    'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_SOURCE_BOUND_PREFIX_COMPLETION_INDEPENDENT_REVIEW_PENDING',
    'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':consumers}
claim['statement_sha256']=hash_statement(claim)
claims=[accepted,claim]
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
save(ROOT/'CLAIMS.json',claims)
progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B17','packet_id':'A084',
    'gap_id':'G-R-SELECT','attempt_id':'A084-continuum-4',
    'method':'Source-bound completion of moderate-prefix bill: exact compact Bernstein estimates, scalar entropy thinning, geometric influence growth, two-complement bias decomposition and retained rare-tail reconstruction',
    'mathematical_delta':'Closes previously unpaid moderate-prefix normalized H/I correction in [-314/21,200/3]; complete all-depth common-policy correction in [-2074/105,248/3], uniformly over all core dimensions and real bias parameters. 160 exact polynomial boxes and 8864 assertions passed; consumes A075 independent acceptance of A084 continuum@1.',
    'deliverable_status':'ARTIFACT_COMPLETE_NEW_BUDGET_REVIEW_PENDING',
    'mathematical_status':'FULL_COMPOSITION_CORRECTION_BOUNDED_ABSOLUTE_TERMINAL_BOUND_AND_FEI_OPEN',
    'claim_versions_used':[{'claim_id':'A084-F6-CONTINUUM-ADMISSION','version':1,'statement_sha256':accepted['statement_sha256'],'role':'Unchanged external independent acceptance consumed; not required as an entropy-proof premise'},
        {'claim_id':'A075-RARE-CORE-LOCALIZATION','version':1,'statement_sha256':precursor['statement_sha256'],'hash_convention':'Source stores statement-only SHA256; supplemental hypotheses binding in out/SOURCE_HASH_CONVENTIONS.json','role':'Source-bound unpaid-prefix target and rare-tail entropy subchain reconstructed, not an unreviewed theorem premise'}],
    'claims_created_or_changed':[{'claim_id':accepted['claim_id'],'version':1,'change':'Source-pinned external review consumed, unchanged statement'}, {'claim_id':claim['claim_id'],'version':1}],
    'source_artifacts':['REPORT.md','PROOF.md','REVIEW.md','FROZEN_SPEC.json','code/verify.py','out/VALIDATION.json','out/ALGEBRA.json','out/LOW_Q_CERTIFICATE.json','out/COMPLEMENT_Q_CERTIFICATE.json','out/RARE_Q_LOWER.json','out/RARE_Q_UPPER.json','out/RARE_BIAS_CONTRACTION.json','out/PHYSICAL_1.json','out/PHYSICAL_6.json','out/TRAJECTORY_FIXTURES.json','out/THINNING_FIXTURES.json','out/SOURCE_RECEIPTS.json'],
    'next_consumers':consumers,
    'next_action':'Price or refute a complete actual one-flip escape/common-sign localization cycle with both signed terminal corrections and an exclusive retained-core slack, or bound the absolute localized rare-core E supremum. A075/A074/A092/A089 independently reconstruct the new moderate-prefix theorem.',
    'stagnant_substantive_attempts':0,
    'blockers':['No blocker in proved complete common-policy entropy budget; independent reconstruction pending.',
        'Absolute E or H/I bound for retained arbitrary-dimensional rare cores remains open.',
        'Repeated mixed-policy escape cycles have no single-use terminal slack or cancellation proved here.'],
    'packet_ids':['A084']}
assert set(progress)=={x.split(' (',1)[0] for x in protocol['required_per_run']['progress_fields']}
for name in ['PROGRESS.json','PACKET_DELTA.json']:save(ROOT/name,progress)
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rstrip().splitlines()[-1].startswith('**Universal bridge:**')
(AGENT/'STATUS.md').write_text('STATE: A084 stage4 complete: moderate prefix [-314/21,200/3], full all-depth common-policy H/I correction [-2074/105,248/3]; 160 exact boxes/8864 assertions PASS; stage3 accepted by A075, new review pending, FEI OPEN.\nNEXT: Price one actual one-flip escape/common-sign return cycle from exclusive terminal slack, retaining both signed corrections; absolute rare-core E remains open; A075/A074/A092/A089 review new budget.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp}: Stage4 read current board/B17/status and protocol. Consumed A075 external acceptance of unchanged stage3 continuum theorem. A080 actual rare core makes rare-high-E exclusion false, A075 already pays rare admission/tail, and A072 already pays one-flip escape: do not repeat them. Finished A075 explicitly unpaid moderate-prefix entropy bill instead. Derived thinning envelope, Q>=19/16 on low band, Qcomp>=1/9, at most one low run/two complemented steps, and geometric influence sum. Moderate correction [-314/21,200/3]; reconstruct rare tail to obtain full [-2074/105,248/3]. Pilot336 assertions 0.0609s; final8864 assertions (8192 actual physical coefficients) runtime {validation["runtime_seconds"]:.4f}s;160 exact Bernstein boxes. Replaced irrelevant pilot sanity assertion with exact seed-degree identity and reran; no expanded domain. A089 run-local status missing was resolved by reading rolling status. First finalizer halted before claim/rolling saves because it assumed all source hashes used statement-plus-hypotheses JSON. Source A075 code actually uses statement-only for its new claim; verified that exact convention and saved an additional hypotheses binding without changing its source. New proof pending independent review; no full A075 acceptance due contributor conflict and no complete erasure-loss audit. Save complete, FEI open.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage4 durable: Finite arbitrarily long common-sign matching-gate trajectories have a uniformly bounded FULL normalized entropy correction, not just rare tail: [-2074/105,248/3]. Scalar L(v)=q h2(v)+v h2(q)-h2(vq) is concave with zero endpoints, so C/(Q I) is between -h2(v)/I and (v/I)h2(q)/q. Low-moderate Q>=19/16 yields sum1/I<=38/3 by edge isoperimetry at its start. That prices unlimited residence near a fixed bias. The policy has at most one low run and two complemented steps, because b(1/2)=5/32 and a low crossing <=3/8 maps via b to7047/131072<1/16. Moderate correction [-314/21,200/3]; retained rare tail [-24/5,16] completes the bounds. A075 externally accepted stage3 continuum@1 unchanged. Rare high-E exclusion is refuted by A080 actual core; repeated ALTERNATING one-flip/common-sign cycles and absolute terminal E remain unpaid. Bounded correction retains an unknown starting ratio and cannot establish FEI.\n')
save(ROOT/'out/CHECKPOINT.json',{'state':'COMPLETE_AUTHOR_PROOF_CHECKED_LOCALLY','moderate_correction':['-314/21','200/3'],'all_depth_correction':['-2074/105','248/3'],'mathematical_checks':8864,'boxes':160,'prior_continuum_review':'A075 acceptance consumed unchanged','new_independent_review':'pending','full_FEI':'OPEN'})
assert read(ROOT/'PROGRESS.json')==read(ROOT/'PACKET_DELTA.json')
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
files=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json' and '__pycache__' not in p.parts:
        row=receipt(p);assert row['bytes']<20*1024*1024
        row['path']=str(p.relative_to(ROOT));files.append(row)
save(ROOT/'out/RECEIPTS.json',{'required_files_verified':['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json'],
    'schema_fields':'PASS','statement_hashes_verified':True,'compatibility_copy_verified':True,
    'certificates_coverage_and_signs':'160 boxes checked','exact_assertions':8864,
    'independent_review_new_claim':'pending','supervisor_copy':'pending','mirror_verification':'not performed',
    'rolling_files':[receipt(AGENT/f) for f in ['STATUS.md','WORKLOG.md','LEARNED.md']],
    'files':files})
for item in files:
    assert receipt(ROOT/item['path'])['sha256']==item['sha256']
print(json.dumps({'run':ROOT.name,'claim':claim['claim_id']+'@1','files_receipted':len(files),'readback':'PASS','new_independent_review':'pending','full_FEI':'OPEN'}),flush=True)
