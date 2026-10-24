import json, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
BASE=AGENT.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
source34=BASE/'agents/A034/runs/20261014T055220Z-account05-A034-phase-energy-transfer'
claims34=json.loads((source34/'CLAIMS.json').read_text(encoding='utf-8'))
if isinstance(claims34,dict):claims34=claims34.get('claims',[])
claim34=next(c for c in claims34 if c['claim_id']=='A034-ALL-PRODUCT-ROW-PAYMENT')
fields=['claim_id','version','exact_statement','hypotheses','statement_sha256','contributors','proof_source','proof_dependencies','review_records','status','supersedes','refutes','first_unproved_line','next_consumers']
review={k:claim34[k] for k in fields}
review['review_records']=list(review['review_records'])+[dict(reviewer='A032',verdict='HOLDS_AT_STATED_SCOPE',source=str(ROOT/'REVIEW_A034.md'),method='Independent complete all-dimensional analytic reconstruction; no repair and no author code imported',registry_adoption='NOT_VERIFIED')]
review['status']='INDEPENDENTLY_RECONSTRUCTED_AT_STATED_SCOPE_LOCAL'
statement='For every Boolean g(z,Y) on the independent uniform physical cube, if every positive conditional squared Fourier law of S_Y given S_z=b is coordinate product, allowing arbitrary marginals, deterministic frequency coordinates and arbitrary signs, then every varying conditional marginal is fair; if both branches are positive their masses are exactly1/2. Consequently H(g)<=2I(g) sharply in every dimension, in bits and original physical influence. More generally every nonzero integer ternary physical row with product normalized squared spectrum has reduced dyadic norm numerator1 modulo4; thus no ternary product spectrum with norm3/8 is realizable by any signs in any dimension.'
claim=dict(claim_id='A032-PRODUCT-BRANCH-MASS-RIGIDITY',version=1,exact_statement=statement,
    hypotheses=['Actual Boolean g on independent uniform input; split one original physical frequency coordinate','All positive branch spectral laws coordinate product; deterministic labels and all signs allowed','Ternary norm clause assumes a nonzero row with values0,+/-1 and product normalized spectrum','Entropy bits; physical influence in original coordinates'],
    statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A032'],
    proof_source=dict(path=str(ROOT/'MASS_RIGIDITY.md'),sha256=sha(ROOT/'MASS_RIGIDITY.md'),validation=['out/validation.json','out/mass_congruence.json','out/ternary_obstruction.json','out/truth_tables.json']),
    proof_dependencies=[],review_records=[],status='PROVED_LOCAL_INDEPENDENT_REVIEW_PENDING',supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A079','A034','A033','A088','A094','B07-lead','B20'])
save(ROOT/'CLAIMS.json',[review,claim])
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=ROOT.name,stream='B07',packet_id='A032',
    gap_id='B07-nonproduct-frequency-branch-transfer',attempt_id='A032-stage6-mod4-complementary-mass-admission',
    method='Independent primitive integer norm reconstruction and all-dimensional modulo4 mass impossibility; exact stored-row and actual truth-table checks',
    mathematical_delta='All-product conditional theorem independently HOLDS; arbitrary product frequency branches of a Boolean gate are necessarily fair and equally weighted, hence sharp H<=2I. Requested nonfair/unequal two-product-branch extension is impossible. Nonfair standalone ternary rows do exist and force nonproduct complements.',
    deliverable_status='COMPLETE_LOCAL',mathematical_status='ARBITRARY_PRODUCT_BRANCH_INTERFACE_PROVED_LOCAL; INDEPENDENT_REVIEW_PENDING; NONPRODUCT_TRANSFER_AND_FULL_FEI_OPEN',
    claim_versions_used=['A034-ALL-PRODUCT-ROW-PAYMENT@1: independently reviewed','A034-SIGNED-ODD-MASK-ADMISSION@2: withdrawal consumed','A079 fair-branch endpoint BOUNDARY.md: independently reconstructed','A032-TWO-ADDRESS-N6-CERTIFICATE@1: stored catalogue only'],
    claims_created_or_changed=['A034-ALL-PRODUCT-ROW-PAYMENT@1: A032 HOLDS review','A032-PRODUCT-BRANCH-MASS-RIGIDITY@1'],
    source_artifacts=['MASS_RIGIDITY.md','REVIEW_A034.md','FROZEN_SPEC.json','RIGIDITY_SPEC.json','out/validation.json','out/truth_tables.json','out/mass_congruence.json','out/ternary_obstruction.json','out/ARTIFACT_RECEIPTS.json'],
    next_consumers=['A079','A034','A033','A088','A094','B07-lead','B20'],
    next_action='Pay the forced nonproduct complementary ternary branch with full signed branch/address Renyi gap and both terminal spectra from one original physical influence reserve; identify transfer to height-two rows.',
    stagnant_substantive_attempts=0,blockers=['General nonproduct complete-branch payment unproved','Height-two frequency branches can be half-integral; complementary norm congruence does not transfer','Independent review of new rigidity claim and remote adoption not verified'],packet_ids=['A032'])
save(ROOT/'PROGRESS.json',progress);save(ROOT/'PACKET_DELTA.json',progress)
(AGENT/'STATUS.md').write_text('STATE: Stage6 complete: all-product conditional A034 independently HOLDS; arbitrary product frequency branches necessarily fair/equal mass, sharp H<=2I; exact mod4 phase-impossibility and actual32-sign witness saved; new review pending; FEI OPEN.\nNEXT: A079/A034/A088/A094 review mass rigidity; pay forced nonproduct complement with both full spectra and signed branch/address gap from SAME physical reserve; transfer to half-integral height-two rows.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-14 stage6 (20261014T105923Z): Read updated board/lead/status. Consumed A034 all-product proof and withdrawal; independently reconstructed HOLDS. Started height-one norm payment, then found stronger mod4 rigidity: product ternary norms have odd numerator1 mod4; complementary masses force half/half and no nonfair marginals. Full arbitrary-product branch theorem H<=2I sharp, proof local pending review. Frozen exact audits:45088 stored rows inspected,5392 ternary (3584 nonfair standalone);2048 dyadic masses onlyhalf complementary; actual32-sign product/nonproduct5/8,3/8 fixture, I17/8. Runs0.3002s/0.1369s, integer/Fraction, below300MB estimate. Saved protocol artifacts and receipts. General nonproduct/height-two transfer and FEI remain OPEN.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-14 stage6 durable result: A nonzero ternary integer row with product squared spectrum has dyadic squared norm whose reduced odd numerator is1 modulo4. Primitive coprime pair norms have odd part1 mod4 and scale is a power2. Two such positive masses summing1 must equal1/2, which also forces all branch marginals fair. Therefore any actual Boolean g whose two conditional physical frequency branches are product already belongs to the fair-branch class and has sharp H<=2I. This is an all-dimensional phase-impossibility certificate: a product ternary branch of mass3/8 has no signing. Standalone nonfair ternary product rows DO exist (3584 stored examples on four bits, N1,m3,mass5/8); their complements must be nonproduct. Do not confuse standalone row rigidity with paired admission, or extend the congruence to half-integral branches of height-two rows. A034 all-product conditional theorem independently HOLDS; withdrawn coupled-gcd is unused.\n')
protocol=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
schema=json.loads(protocol.read_text(encoding='utf-8'))['required_per_run']
assert all(set(c)==set(schema['claim_fields']) for c in json.loads((ROOT/'CLAIMS.json').read_text()))
expected=set(schema['progress_fields']); expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
assert json.loads((ROOT/'PROGRESS.json').read_text())==json.loads((ROOT/'PACKET_DELTA.json').read_text())
report=(ROOT/'REPORT.md').read_text()
assert all('# '+s in report for s in schema['report_fields']) and '# Universal bridge' in report
files=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
sources=[protocol,BASE/'BOARD.md',BASE/'claude/B07/STREAM_NOTES.md',source34/'PROOF.md',source34/'CLAIMS.json',BASE/'agents/A079/runs/20261014T060856Z-account05-A079-correlated-auxiliaries/BOUNDARY.md',BASE/'agents/A079/runs/20261014T060856Z-account05-A079-correlated-auxiliaries/REPORT.md']
receipt=dict(status='PASS',schema_fields_exact=True,compatibility_copy_equal=True,report_headings_complete=True,
    all_files_under20MB=True,artifacts={str(p.relative_to(ROOT)):dict(sha256=sha(p),bytes=p.stat().st_size) for p in files},
    rolling={p.name:sha(p) for p in [AGENT/'STATUS.md',AGENT/'WORKLOG.md',AGENT/'LEARNED.md']},
    source_sha256={str(p):sha(p) for p in sources},remote_adoption='NOT_VERIFIED',independent_rigidity_review='PENDING')
save(ROOT/'out/ARTIFACT_RECEIPTS.json',receipt)
print(json.dumps(dict(status='PASS',protocol_claims=len([review,claim]),artifact_count=len(files),statement_sha256=claim['statement_sha256'],proof_sha256=claim['proof_source']['sha256']),indent=2))
