"""Archive a stale proposal without changing anyone else's live code."""
import sys
sys.dont_write_bytecode = True
import hashlib
import json
from pathlib import Path

R = Path(__file__).resolve().parent
drift = json.loads((R/'review/LIVE_DRIFT_RECEIPT.json').read_text(encoding='utf-8'))
prov_path = R/'patches/01_provenance.json'
prov = json.loads(prov_path.read_text(encoding='utf-8'))
assert hashlib.sha256((R/'copies/brain_node_documents.py').read_bytes()).hexdigest() == prov['source_sha256'] == drift['old_sha256']
assert hashlib.sha256((R/'copies/brain_node_documents_resume.py').read_bytes()).hexdigest() == drift['current_sha256']
prov.update({'deployment':'superseded; do not apply', 'deployment_permitted':False,
             'observed_current_source_sha256':drift['current_sha256'],
             'reason':'Current live source adds a permission-aware verified snapshot path; the pinned baseline is stale.',
             'runtime_validation':'not run; three unchanged fresh gates declined admission',
             'evidence':'review/LIVE_DRIFT_RECEIPT.json; review/live_drift.diff'})
prov_path.write_text(json.dumps(prov, indent=2)+'\n', encoding='utf-8')

claims_path = R/'CLAIMS.jsonl'
claims = [json.loads(s) for s in claims_path.read_text(encoding='utf-8').splitlines() if s.strip()]
for c in claims:
    if c['id'] == 'w370-P0104-006':
        c['statement'] += ' The historical read-lock proposal is superseded: the current live code has a different permission-aware snapshot fallback.'
        c['source']['live_drift'] = 'review/LIVE_DRIFT_RECEIPT.json; review/live_drift.diff'
        c['remaining_gap'] = 'The current fallback has not been runtime-validated by this worker. Do not apply the archived patch; no speedup claim.'
    if c['id'] == 'w370-P0104-007':
        c['source']['live_drift'] = 'review/LIVE_DRIFT_RECEIPT.json'
        c['remaining_gap'] = 'Current live fallback runtime validation and draft integration remain outstanding. The worker patch is superseded; no repair speedup or FPP exponent claim follows.'
claims_path.write_text(''.join(json.dumps(c, ensure_ascii=False)+'\n' for c in claims), encoding='utf-8')

resume_path = R/'review/RESUME_RECEIPT.json'
resume = json.loads(resume_path.read_text(encoding='utf-8'))
resume['runtime_check']['code_status'] = 'superseded unvalidated proposal'
resume['live_source_drift'] = drift
resume['NEXT'] = 'Integrate independently checked math drafts; validate the current live fallback separately rather than apply the archived patch.'
resume_path.write_text(json.dumps(resume, indent=2)+'\n', encoding='utf-8')

notice = {'sent':False, 'scope':'Staged in w370 under the worker-folder and no-mesh-send restrictions.',
          'messages':[{'to':'w371','kind':'answer','text':'Accepted KEEP for claims 002/003/005; exact receipts saved in w370/review/REFEREE_VERDICTS.jsonl. The resumed CPU gate declined at 85.5%. The old code proposal is superseded by the live permission-aware snapshot path.'},
                      {'to':'claude-4a88bc43','kind':'done','text':'w370 math packet has three independent KEEP receipts. Old reader-lock diff is superseded: live source f326206c has a permission-aware fallback. Do not apply the old diff; no runtime speedup claimed. See w370/review/REVIEW_PACKET.md.'}]}
(R/'outbox/resume_peer_notices.json').write_text(json.dumps(notice, indent=2)+'\n', encoding='utf-8')

with (R/'ATTEMPT.md').open('a', encoding='utf-8') as f:
    f.write('\n2026-10-10 resume: The live source changed from the copied baseline and now has a permission-aware snapshot fallback. The historical read-lock diff is SUPERSEDED and must not be applied; live_drift.diff records the exact change. No end-to-end improvement was measured.\n\nNEXT: Bound the actual FPP Doob martingale cross and cubic sums relative to Var(T_n)^2 before asserting uniform kurtosis.\n')
report = '''P0104 is not solved. Current global openness is UNKNOWN. I saved an
independent abstract obstruction, then audited the paired conditional proof.
w371 independently kept my rare-event counterexample, conditional variance
bridge and interval correction: review/REFEREE_VERDICTS.jsonl records the
exact decisions. Uniform lattice kurtosis and nondegenerate n^(1/3) weak
scaling remain unproved.

The counterexample has weak n^(1/3) scaling and an exponential tail at
sqrt(n/log n), but variance exponent 3/8. It shows why the larger-scale
concentration theorem cannot replace moment control. The correction is
Var(X)>=epsilon L^2/4 under a uniform closed-interval probability deficit;
it does not restate the cited paper's theorem.

Measurement command:
    python -X utf8 ~/brain_workers/w370/readonly_recall.py
The guarded recall timed out after 60.756 seconds, with 40 blocked
write-lock open attempts across bundles. This is a read-only access
failure, not an unguarded latency benchmark or proof of retry delay.

Runtime check command:
    python -X utf8 ~/brain_workers/w370/test_read_lock.py
Three unchanged gates declined admission at CPU 80.9%, 88.4% and 85.5%
against the 75% cap; RAM cleared the 2 GiB minimum each time. No fixture
tests ran. There is no measured reader-lock improvement or speedup.

The live source changed while this task ran: the saved baseline starts
cc0f2cdf and the observed current source starts f326206c. The exact diff
adds a permission-aware verified snapshot fallback. The worker did not
make that live change. My earlier read-lock proposal is SUPERSEDED.

Apply line: DO NOT APPLY patches/01_readonly_attachment_lock.diff; its
pinned baseline is stale. Keep it as a historical proposal. Validate the
current live fallback separately before making performance or concurrency
claims. See patches/01_STATUS.md and review/LIVE_DRIFT_RECEIPT.json.

Seven claim rows, five typed draft entries and four supported relations
are saved. The three math claims are independently checked; draft nodes
remain concepts. Submission, full bundle review, ingestion and
retrievability remain false. Structural/AST results are recorded in
validation_receipt.json and are separate from mathematical and runtime
checks. Bundle, hook, progress rows and peer acknowledgments are staged
inside w370 under the worker-folder restriction.

Review: review/REVIEW_PACKET.md, SOURCE_STATUS.json, CLAIMS.jsonl,
AUDIT_w369.md and INDEPENDENT_BRIDGE.md.

NEXT: Integrate the checked mathematical drafts and validate the current
live fallback. The next proof obligation is to bound the actual FPP Doob
cross and cubic sums relative to Var(T_n)^2 before asserting uniform
kurtosis.
'''
(R/'REPORT.md').write_text(report, encoding='utf-8')

packet = '''# w370 P0104 review packet

For w371 and claude-4a88bc43. Current global openness UNKNOWN; P0104 is
not solved by this work.

1. w371 KEEP: claim 002, the exact abstract 3/8 rare-event sequence in
   INDEPENDENT_BRIDGE.md. The all-parameter tail bound and divergent
   standardized fourth moment were independently reproduced. It is not
   an iid lattice FPP construction.
2. w371 KEEP: claim 003, the conditional bridge under uniform centered
   kurtosis and nondegenerate weak scaling, including arbitrary centers
   by symmetrization. Both lattice inputs remain unproved.
3. w371 KEEP: claim 005, the uniform interval premise implying
   Var(X)>=epsilon L^2/4. This corrects only a categorical inference on
   the recalled card. It does not reassert the paper theorem.
4. Review drafts/bundle_001.json and EDGES.jsonl for integration using
   review/REFEREE_VERDICTS.jsonl. New result nodes remain concepts with
   proof_text null. Full bundle/edge admission, submission, ingestion
   and retrievability have not been certified.
5. The historical reader-lock proposal is SUPERSEDED. Do not apply
   patches/01_readonly_attachment_lock.diff. The observed live code has
   a permission-aware snapshot fallback; review/live_drift.diff and
   review/LIVE_DRIFT_RECEIPT.json preserve the exact difference.

The old synthetic test command is preserved for reference:

    python -X utf8 ~/brain_workers/w370/test_read_lock.py

Three unchanged admission gates rejected tests at CPU 80.9%, 88.4% and
85.5%; no fixture test ran. Retain the fixed 75% CPU / 2 GiB RAM limits
and 20-second test budget for any subsequent runtime validation. The
archived test compares historical copies and does not validate the new
live fallback. No end-to-end recall improvement is claimed.

validation_receipt.json records schema/AST checks and the observed source
hashes. Those checks do not establish lock behavior, concurrency or a
mathematical theorem. No formal checker ran. All worker writes remain
under w370; outbox/ contains staged notices and progress rows.

NEXT: Integrate the independently checked mathematical drafts and
validate the current live fallback separately. For P0104, bound actual
Doob cross and cubic sums relative to Var(T_n)^2; the conditional bridge
does not supply that estimate.
'''
(R/'review/REVIEW_PACKET.md').write_text(packet, encoding='utf-8')
print(json.dumps({'proposal':'superseded','deployment_permitted':False,'live_file_modified':False,'math_claims':'w371 KEEP 002/003/005'}))
