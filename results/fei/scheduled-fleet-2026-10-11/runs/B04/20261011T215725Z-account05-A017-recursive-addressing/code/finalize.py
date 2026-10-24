"""Local artifact serialization and protocol-schema verification, no shared writes."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

RUN = Path(__file__).resolve().parents[1]
AGENT = RUN.parents[1]
CANON = Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUPPLEMENT = Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
CONTEXT = Path(r'~\brain_workers\FEI100_20261011\context')
TEAM = AGENT.parents[1]
NOW = datetime.now(timezone.utc).isoformat()

def save(path,data):
    path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def file_receipt(path):
    blob = path.read_bytes()
    return dict(path=str(path),bytes=len(blob),sha256=hashlib.sha256(blob).hexdigest())

sources = [CANON/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md',
           'CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json',
           'STREAM_NEXT_ACTIONS.json','AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex']]
sources += [SUPPLEMENT/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md',
            'SEED_LEMMAS.md','NATIVE_MAPPING.md','baseline/current-threshold-paper.tex']]
sources += sorted((SUPPLEMENT/'sources').glob('*.md'))
sources += sorted(CONTEXT.glob('*.txt'))
sources += sorted((CANON/'runs').rglob('REPORT.md'))
sources += [TEAM/'BOARD.md']
receipts = []
for source in sources:
    # Full text decode used for ingestion and provenance, no source mutation.
    content = source.read_text(encoding='utf-8-sig',errors='replace')
    receipt = file_receipt(source)
    receipt['text_lines'] = len(content.splitlines())
    receipts.append(receipt)
save(RUN/'out'/'source_receipts.json',dict(created_utc=NOW,sources=receipts,
     stream_notes=dict(path=str(TEAM/'claude'/'B04'/'STREAM_NOTES.md'),exists=(TEAM/'claude'/'B04'/'STREAM_NOTES.md').exists()),
     scope='Full texts ingested; proof-critical Section 8 threshold excerpts and packet scope inspected; contextual sources are not theorem dependencies.'))

statement = ('For all n,a>=0, binary linear M:F2^n->F2^a and quadratic q:F2^n->F2, '
             'F(x,y)=(-1)^q(x)y_(Mx) on independent uniform physical controls and distinct data signs '
             'has 2^(2r+k) equal Fourier atoms, H(F)=2r+k, I(F)=1+(c+b)/2+d, '
             'and H(F)<=4(I(F)-1-d)<=4(I(F)-1). Here r=rank M, k=rank of the polar form '
             'restricted to ker M, c counts nonzero M columns, b counts zero M columns '
             'with nonzero polar row, and d counts zero M columns with zero polar row and '
             'linear q coefficient one. Under M_t=A_t M_(t-1)+B_t and q_t=q_(t-1)+p_t '
             'with quadratic p_t, Delta H_t=2 Delta r_t+Delta k_t and '
             'Delta I_t=(Delta c_t+Delta b_t)/2+Delta d_t, including arbitrary control reuse.')
hypotheses = ['uniform independent physical controls and data signs','entropy in bits',
              'distinct terminal states name distinct physical data coordinates',
              'q and every phase increment have degree at most two over F2',
              'all state update matrices fixed over F2; no selector freshness required between stages']
sh = hashlib.sha256(json.dumps(dict(statement=statement,hypotheses=hypotheses),sort_keys=True,separators=(',',':')).encode()).hexdigest()
claim = dict(claim_id='A017-QUADRATIC-REUSED-ADDRESSING-LEDGER',version=1,
             exact_statement=statement,hypotheses=hypotheses,statement_sha256=sh,
             contributors=['A017/account05'],
             proof_source=dict(path='RECURSIVE_ADDRESSING.tex',sha256=file_receipt(RUN/'RECURSIVE_ADDRESSING.tex')['sha256'],
                               locator='Rank and fiber-phase ledger theorem and Exact recursive addressing program'),
             proof_dependencies=[],review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
             supersedes=[],refutes=[],first_unproved_line=None,
             next_consumers=['A013','A030','A077','A008','A018','A058','A091','A090'])
save(RUN/'CLAIMS.json',[claim])
progress = dict(protocol_revision='2026-10-11-execution-v2',run_id=RUN.name,stream='B04',packet_id='A017',
                gap_id='FEI-B04-A017-INITIAL',attempt_id='A017-stage1-rank-fiber-phase',
                method='Exact signed-affine-fiber Walsh law, GF2 polar rank and physical edge derivatives',
                mathematical_delta='Closed exact H/I ledgers for reused linear-state addressing with quadratic phases; normalized terminal label code; cancellation tower and general nonquadratic fiber residual. Constant-four closure can also be recovered from baseline orthogonal-neighbor closure plus quadratic leaf bound; full FEI remains OPEN.',
                deliverable_status='LOCAL_ARTIFACT_COMPLETE_REVIEW_PENDING',
                mathematical_status='EXACT_RESTRICTED_LEDGER_AUTHOR_PROVED_FULL_FEI_OPEN',
                claim_versions_used=[],claims_created_or_changed=[dict(claim_id=claim['claim_id'],version=1)],
                source_artifacts=['REPORT.md','CLAIMS.json','RECURSIVE_ADDRESSING.tex','REUSE_CONDITIONS.json',
                                  'code/check.py','out/FROZEN_SPEC.json','out/FROZEN_SPEC_CORRECTION.json',
                                  'out/validation.json','out/source_receipts.json'],
                next_consumers=['A013','A030','A077','A008','A018','A058','A091','A090'],
                next_action='A091/A090 independently reconstruct the ledger; then test full conditional fiber entropy of a sparse nonquadratic Boolean perturbation with a nonreusing physical stopping-tree budget.',
                stagnant_substantive_attempts=0,
                blockers=['B04 STREAM_NOTES.md absent; no mathematical access blocker','Independent review and supervisor mirror/adoption pending'],
                packet_ids=['A017'])
save(RUN/'PROGRESS.json',progress)
save(RUN/'PACKET_DELTA.json',progress)
protocol = json.loads((CANON/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
assert set(claim) == set(protocol['required_per_run']['claim_fields'])
expected = set(protocol['required_per_run']['progress_fields'])
expected.remove('packet_ids (one primary ID, for compatibility)')
expected.add('packet_ids')
assert set(progress) == expected
report = (RUN/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:
    assert '## '+field in report
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge**:')
assert json.loads((RUN/'PROGRESS.json').read_text()) == json.loads((RUN/'PACKET_DELTA.json').read_text())
assert all(p.stat().st_size < 20*1024*1024 for p in RUN.rglob('*') if p.is_file())
save(RUN/'out'/'persistence_receipts.json',dict(created_utc=NOW,status='LOCAL_SAVE_VERIFIED',
     protocol_schema='exact report_fields, claim_fields and progress_fields verified',
     artifacts=[file_receipt(p) for p in sorted(RUN.rglob('*')) if p.is_file() and p.name!='persistence_receipts.json'],
     rolling_files=[file_receipt(AGENT/n) for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],
     mirror_status='NOT_VERIFIED; supervisor transfer pending',review_status='INDEPENDENT_REVIEW_PENDING'))
print(json.dumps(dict(status='LOCAL_SAVE_VERIFIED',source_count=len(receipts),claim_fields=len(claim),
                     progress_fields=len(progress),statement_sha256=sh,run=str(RUN)),indent=2))
