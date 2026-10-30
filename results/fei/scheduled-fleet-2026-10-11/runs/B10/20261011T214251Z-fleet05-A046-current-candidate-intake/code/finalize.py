"""Persist and validate the A046 protocol package; no mathematical search."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

RUN = Path(__file__).resolve().parents[1]
AGENT = RUN.parents[1]
CAMPAIGN = Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUPPLEMENT = Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
TEAM = Path(r'~\brain_workers\FEI100_20261011')
protocol=json.loads((CAMPAIGN/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))

def save(name,obj):
    (RUN/name).write_text(json.dumps(obj,indent=2,ensure_ascii=True)+'\n',encoding='utf-8')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

statement=('For the actual Boolean sign g(x,y)=(-1)^(xy) on independent Bernoulli inputs '
           'with P(X=1)=p and fixed P(Y=1)=q in (0,1/2), and physical reveal A={X}, '
           'the Shannon spectral/physical-channel quantities satisfy '
           'J_A-M_A=4q(1-2q)*p*log2(1/p)+O_q(p) as p tends to zero. '
           'Consequently every scalar tau(p) such that J_A<=M_A+tau(p) for all finite '
           'actual Boolean signs under every interior product bias and every singleton '
           'block of bias p satisfies liminf_{p->0} tau(p)/(p*log2(1/p))>=1/2. '
           'In particular no universal O(p) tax is valid. This does not refute '
           'B09 Delta(p), prove its optimality, or disprove uniform-cube FEI.')
hypotheses=['actual two-bit AND sign, not an arbitrary normalized spectrum',
            'independent interior product biases p and q',
            'q fixed in (0,1/2) for the asymptotic; q=1/4 for the universal lower bound',
            'orthonormal biased Fourier basis including the empty coefficient',
            'physical reveal A={X} with actual branch probabilities',
            'M_A=H(S_A|S_B), J_A=I(Z;S_B), all entropy in bits']
claim={'claim_id':'A046-AND-ENDPOINT-TAX-NECESSITY','version':1,
       'exact_statement':statement,'hypotheses':hypotheses,
       'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
       'contributors':['fleet05/A046'],
       'proof_source':{'run_id':RUN.name,'path':'REPORT.md','locator':'complete derivation, steps 1-4','finite_checker':'code/exact_check.py'},
       'proof_dependencies':[], 'review_records':[],
       'status':'ANALYTICALLY_PROVED_PENDING_INDEPENDENT_REVIEW',
       'supersedes':[],
       'refutes':['universal scalar tax tau(p)=O(p) in biased singleton J_A<=M_A+tau(p)',
                  'universal tau(p)=c*p*log2(1/p)+O(p) with c<1/2'],
       'first_unproved_line':None,
       'next_consumers':['A047','A048','A071','A092','A087','B09','B19','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save('CLAIMS.json',[claim])

progress={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B10',
          'packet_id':'A046','gap_id':'G-BIASED-TAX','attempt_id':'A046-intake-1',
          'method':'source-bound candidate intake; actual two-bit AND endpoint lower bound; independent rational interval witness reconstruction',
          'mathematical_delta':'Complete frozen B09 v1 potential with exact quantifiers and retirement guards; proved AND endpoint excess coefficient 1/2, excluding every universal O(p) scalar tax. Four finite exact certificates passed. Full FEI remains OPEN.',
          'deliverable_status':'COMPLETE_LOCAL_PENDING_INDEPENDENT_REVIEW',
          'mathematical_status':'RESTRICTED_HELPER_OBSTRUCTION_PROVED; LIVE_CORE_PENDING_REVIEW; FULL_FEI_OPEN',
          'claim_versions_used':['B09-BIASED-BLOCK-UNCERTAINTY@1 (intake object only, not accepted premise)',
                                 'B09-TAXFREE-AND-COUNTEREXAMPLE-REPAIRED@1 (independently recertified)',
                                 'B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO@1 (scope/retirement guard)'],
          'claims_created_or_changed':['A046-AND-ENDPOINT-TAX-NECESSITY@1'],
          'source_artifacts':['REPORT.md','FROZEN_POTENTIAL.json','KNOWN_FALSIFIERS.md','SEARCH_SPEC.json',
                              'SOURCE_MANIFEST.json','code/exact_check.py','out/EXACT_CHECK.json'],
          'next_consumers':['A038','A047','A048','A071','A076','A092','A087','B09','B19','B20'],
          'next_action':'A092/A087 review intake and endpoint proof; A047 freeze a genuine coefficient-1/2 sharpness test on Boolean-realizable physical-child pairs. Retire intake until candidate revision or specific review objection.',
          'stagnant_substantive_attempts':0,
          'blockers':['B10 lead STREAM_NOTES.md absent at intake (nonblocking)',
                      'Original fixed-reserve definition/witness not present in inspected curated note; retrieve before proposing any occurrence-reserve repair',
                      'Independent review and supervisor copy/mirror receipts are not yet available'],
          'packet_ids':['A046']}
required_progress_keys={key.split(' (',1)[0] for key in protocol['required_per_run']['progress_fields']}
assert set(progress)==required_progress_keys
save('PROGRESS.json',progress)
save('PACKET_DELTA.json',progress)

paths=[]
for name in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json',
             'OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json',
             'AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex']:
    paths.append((CAMPAIGN/name,'protocol fully read; campaign navigation and packet-specific sections inspected'))
for path in (CAMPAIGN/'runs').rglob('REPORT.md'):
    paths.append((path,'original report inspected; B09 sections 0-9; B05/B19 no-go reconstruction'))
for name in ['REPORT.md','CHECK.py']:
    paths.append((CAMPAIGN/'verification'/'B09_interval_repair_20261011'/name,'repaired interval derivation/code inspected'))
paths.append((CAMPAIGN/'verification'/'plan_mathematical_audit_2026-10-11.md','correction records and obstruction source map inspected'))
for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','SOURCES.json']:
    paths.append((SUPPLEMENT/name,'supplement context, claims/controls and source catalog inspected'))
for path in (SUPPLEMENT/'sources').glob('*.md'):
    scope=('inspected relevant proof/source ledger' if path.name in {
        'BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','LOG_ALLOCATION_CURATED.md',
        'ROUTE_MAP_CURATED.md','GAMMA_ENDPOINT_LEDGER.md','ONE_BIT_ENDPOINT.md',
        'OVERLAPPING_PRODUCT_NOTE.md'} else 'cataloged; no theorem from this note used as a proof dependency')
    paths.append((path,scope))
for path in (TEAM/'context').glob('*.txt'):
    paths.append((path,'scope/context inspection; threshold 38pp sections 6.1/7; percolation 30pp introduction/section 3; earlier versions opening/scope, not whole-paper proof audit'))
paths.append((TEAM/'BOARD.md','stage-start supervisor snapshot read'))
manifest=[]
for path,scope in paths:
    raw=path.read_bytes()
    manifest.append({'path':str(path),'sha256':hashlib.sha256(raw).hexdigest(),
                     'bytes':len(raw),'inspection_scope':scope})
save('SOURCE_MANIFEST.json',{'sources':manifest,'missing_source':str(TEAM/'claude'/'B10'/'STREAM_NOTES.md'),
                             'external_network_retrieval':'NONE; endpoint proof self-contained, no literature priority claim'})

stamp=datetime.now(timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A046 intake complete locally; B09 potential frozen; AND endpoint forces tax coefficient >=1/2; four exact certificates PASS; independent review pending; full FEI OPEN.\nNEXT: A092/A087 review; A047 test a genuinely improved coefficient-1/2 tax on Boolean-realizable child pairs; reopen intake only for candidate revision or review objection.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as handle:
    handle.write(f'\n{stamp}: Saved frozen candidate, correction ledger and pre-computation SEARCH_SPEC. Independent Fraction checker passed four actual two-bit AND instances in 0.0078 arithmetic seconds. Completed analytic all-p endpoint proof: excess/(p log2(1/p)) -> 1/2 at q=1/4, repairing the unsupported B09 necessity inference without accepting its core. Wrote protocol artifacts and hashes; no shared-tree mutation, network retrieval, git, messaging or brain write. Review/mirror pending.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as handle:
    handle.write('\nCompleted analytic proof in stage-1 REPORT: fixed-q AND excess coefficient is 4q(1-2q)=1/2-8(q-1/4)^2. Universal scalar singleton tax must have liminf tau(p)/(p log2(1/p))>=1/2; O(p) is impossible. Exact existing Delta(p)=p log2((1-p)/p) for p<=1/2 has coefficient 1, so current helper survives. Optimal universal coefficient unresolved; core pending independent review.\nRange reduction of rational logarithms to [1,2) makes 24 atanh terms sufficient for these signs. Signed interval division must use four endpoint extrema; negative entropy weights reverse endpoints. Four values checked exactly after freezing the spec.\n')

headers=[line[2:] for line in (RUN/'REPORT.md').read_text(encoding='utf-8').splitlines() if line.startswith('# ')]
assert headers==protocol['required_per_run']['report_fields']
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert json.loads((RUN/'out'/'EXACT_CHECK.json').read_text())['status']=='PASS'
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
artifacts=[]
for path in RUN.rglob('*'):
    if path.is_file():
        assert path.stat().st_size<20_000_000
        artifacts.append({'path':str(path.relative_to(RUN)),'sha256':digest(path),'bytes':path.stat().st_size})
validation={'status':'PASS','validated_at_utc':stamp,'claim_field_keys_exact':True,
            'progress_field_keys_exact':True,'report_fields_exact':True,
            'protocol_label_normalization':'packet_ids (one primary ID, for compatibility) maps to literal JSON key packet_ids, as required by the user',
            'progress_delta_byte_identical':True,'statement_hash_convention':'protocol canonical JSON',
            'status_two_lines':True,'file_size_limit_pass':True,
            'source_manifest_count':len(manifest),'artifacts':artifacts,
            'independent_review':'PENDING','supervisor_copy':'NOT_OBSERVED','mirror_verification':'NOT_OBSERVED'}
save('out/VALIDATION.json',validation)
print(json.dumps({k:v for k,v in validation.items() if k!='artifacts'},indent=2))
