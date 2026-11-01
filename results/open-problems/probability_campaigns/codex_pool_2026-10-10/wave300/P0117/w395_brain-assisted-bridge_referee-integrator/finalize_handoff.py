"""Record exact hashes and review states for the integration contact."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
files = {
    'report': root / 'REPORT.md',
    'source_status': root / 'SOURCE_STATUS.json',
    'attempt': root / 'ATTEMPT.md',
    'review_packet': root / 'REVIEW_PACKET.md',
    'claims': root / 'CLAIMS.jsonl',
    'result_rows': root / 'RESULT_ROWS.jsonl',
    'w395_bundle': root / 'draft_bundles' / 'bundle_001.json',
    'w395_bundle_diff': root / 'patches' / '01_p0117_fixed_label_gap_bundle.diff',
    'w395_hook_diff': root / 'patches' / '02_p0117_quantifier_hook.diff',
    'w394_current_bundle': Path('~/math-brain-inbox/w394/bundle_002.json'),
    'w394_referee_fix_diff': root / 'patches' / '03_w394_bundle_002_referee_fix.diff',
    'w394_referee_copy': root / 'reviewed_copies' / 'w394_bundle_002_referee_fix.json',
    'public_preprint_copy': root / 'source_openai_no_bigeodesics_2026-09-24.pdf',
}
out = {}
for key, path in files.items():
    data = path.read_bytes()
    out[key] = {'path': path.as_posix(), 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}
handoff = {
    'target': 'P0117',
    'agent': 'w395',
    'date': '2026-10-10',
    'integration_contact': 'codex-01a12190',
    'served_model_evidence': {'w395': 'UNKNOWN: this API session exposed no response-side served-model receipt', 'peer_authors': 'UNKNOWN to w395; integration contact must verify response-side records'},
    'source_status': 'A 2026-09-24 primary preprint claims moment-qualified resolution; mathematical proof and moment-free scope are unverified.',
    'scoped_verdicts': {'w393_L1_L2_L3_C1': 'KEEP partial', 'w394_C01_C05': 'KEEP partial', 'w394_C06': 'KEEP conditional', 'w392_zero_edge': 'KEEP boundary only', 'openai_preprint_Prop7_6': 'KEEP conditional final deduction; no verdict on full Theorem 1.1', 'w394_bundle_002': 'FIX two entry/edge lines before ingestion'},
    'remaining_gap': 'Simultaneous random-label Busemann control, half-plane transfer, union preservation, and positive mark density in the preprint remain unverified; peers have no divergent whole-event killing estimate.',
    'w395_bundle_states': {'prepared': True, 'submitted': False, 'reviewed': 'local source/logic audit; independent edge audit pending', 'ingested': False, 'retrievable': 'not measured after ingestion'},
    'artifacts': out,
}
(root / 'HANDOFF.json').write_text(json.dumps(handoff, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({'status': 'pass', 'artifacts_hashed': len(out), 'w394_bundle_sha256': out['w394_current_bundle']['sha256'], 'w394_fix_diff_sha256': out['w394_referee_fix_diff']['sha256'], 'w395_bundle_sha256': out['w395_bundle']['sha256']}))
