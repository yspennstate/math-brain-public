from datetime import datetime, timezone
import difflib
import hashlib
import json
from pathlib import Path
import sqlite3
import time
import urllib.request

base = Path(__file__).resolve().parent
stamp = datetime.now(timezone.utc).isoformat()
repo = Path('~/<private-repo>')
intake = repo / '06_math_research/probability_1000_intake_claude_20260907'
source_dir = base / 'sources'
source_dir.mkdir(exist_ok=True)
source_receipt = {'url': 'https://arxiv.org/pdf/0810.4221v2', 'version': '0810.4221v2, 2008-12-16', 'status': 'WEB_PRIMARY_ALREADY_READ', 'pdf_sha256': None, 'intake_reported_sha256': '17f13a871b84417a83514995c70d2ebf49f5464faeac9dd95e8c4d823b600658'}
pdf = source_dir / 'chatterjee_0810_4221v2.pdf'
try:
    if not pdf.exists():
        with urllib.request.urlopen(source_receipt['url'], timeout=20) as response:
            raw = response.read(2000001)
        if not raw.startswith(b'%PDF') or len(raw) > 2000000:
            raise ValueError('Not a bounded public primary PDF')
        pdf.write_bytes(raw)
    raw = pdf.read_bytes()
    source_receipt.update(status='PUBLIC_PRIMARY_PDF_SAVED', local_path=str(pdf), bytes=len(raw), pdf_sha256=hashlib.sha256(raw).hexdigest())
    source_receipt['matches_intake_digest'] = source_receipt['pdf_sha256'] == source_receipt['intake_reported_sha256']
except Exception as exc:
    source_receipt['download_error'] = f'{type(exc).__name__}: {exc}'

frozen = base / 'review_input'
frozen.mkdir(exist_ok=True)
peer_hashes = []
for name in ['STATEMENT.md', 'ATTEMPT.md', 'CLAIMS.jsonl']:
    origin = Path('~/brain_workers/w498') / name
    raw = origin.read_bytes()
    copied = frozen / ('w498_' + name)
    copied.write_bytes(raw)
    peer_hashes.append({'source': str(origin), 'snapshot': str(copied), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)})
(base / 'PEER_INPUT_HASHES.json').write_text(json.dumps(peer_hashes, indent=2) + '\n', encoding='utf-8')

target = None
target_line = None
with (intake / 'problems.jsonl').open(encoding='utf-8-sig') as incoming:
    for line_number, line in enumerate(incoming, 1):
        if 'C0120' not in line:
            continue
        candidate = json.loads(line)
        if candidate.get('problem_id') == 'C0120':
            target, target_line = candidate, (line_number, line.rstrip('\n\r'))
            break
assert target and target_line
corrected = dict(target)
corrected['statement'] = 'For iid standard Gaussian vertex weights on the planar lattice, let M_n be the maximum weight over all n-vertex up/right paths from the origin, with free endpoint and the origin counted. Improve the C n/log n variance upper bound beyond a logarithmic correction. The operational power goal is Var(M_n)<=C_epsilon n^(1-epsilon) for some fixed 0<epsilon<1 and all n>=2; this is a working formulation, not a literal quantifier in Section 12(3).'
corrected['status_search'] = 'Primary-source scope corrected on 2026-10-10: arXiv:0810.4221v2 Sections 1, 8, 12(3) concern a planar iid Gaussian ground-state maximum. Finite-temperature log Z, arbitrary disorder and general dimension require separate sources. Current openness UNKNOWN; no complete proof or novelty claim is made.'
(base / 'C0120_INTAKE_ORIGINAL.json').write_text(json.dumps(target, indent=2) + '\n', encoding='utf-8')
(base / 'C0120_INTAKE_CORRECTED.json').write_text(json.dumps(corrected, indent=2) + '\n', encoding='utf-8')
patch_dir = base / 'patches'
patch_dir.mkdir(exist_ok=True)
relative = '06_math_research/probability_1000_intake_claude_20260907/problems.jsonl'
line_no, old = target_line
new = json.dumps(corrected, ensure_ascii=False, sort_keys=True)
patch = f'--- a/{relative}\n+++ b/{relative}\n@@ -{line_no} +{line_no} @@\n-{old}\n+{new}\n'
(patch_dir / '01_C0120_source_scope.diff').write_text(patch, encoding='utf-8')

store_matches = []
export = Path('~/math-brain-build/export/population')
for name in ['nodes.jsonl', 'claims.jsonl']:
    count = 0
    with (export / name).open(encoding='utf-8-sig') as records:
        for line_no, line in enumerate(records, 1):
            low = line.lower()
            relevant = 'c0120' in low or ('gaussian' in low and 'polymer' in low and 'variance' in low) or 'gaussian-layer-mean' in low
            if not relevant:
                continue
            record = json.loads(line)
            # Store only this target's matched records, never the export.
            store_matches.append({'file': str(export / name), 'line': line_no, 'matched_row_sha256': hashlib.sha256(line.encode('utf-8')).hexdigest(), 'record': record})
            count += 1
            if count >= 5:
                break
(base / 'STORE_MATCHES.json').write_text(json.dumps(store_matches, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

canonical = {'path': '~/math-brain-build/local/population/brain.sqlite3', 'mode': 'read-only', 'purpose': 'Target-scoped owner solved/retired-status check; no absence inference', 'matches': []}
try:
    connection = sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro', uri=True, timeout=5)
    try:
        for table in ['nodes', 'claims']:
            columns = [row[1] for row in connection.execute(f'PRAGMA table_info({table})')]
            text_cols = [col for col in ['id', 'node_id', 'logical_name', 'title', 'statement', 'text', 'payload_json', 'data_json'] if col in columns]
            if not text_cols:
                continue
            quoted = ','.join('"' + col + '"' for col in text_cols)
            predicates = ' OR '.join('lower(CAST("' + col + '" AS TEXT)) LIKE ?' for col in text_cols)
            rows = connection.execute(f'SELECT {quoted} FROM {table} WHERE {predicates} LIMIT 5', ['%c0120%'] * len(text_cols)).fetchall()
            canonical['matches'].extend({'table': table, 'record': dict(zip(text_cols, row))} for row in rows)
        canonical['status'] = 'SCOPED_READ_COMPLETED'
    finally:
        connection.close()
except Exception as exc:
    canonical['status'] = 'UNAVAILABLE'
    canonical['error'] = f'{type(exc).__name__}: {exc}'
(base / 'CANONICAL_STORE_CHECK.json').write_text(json.dumps(canonical, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

status = {
    'problem_id': 'C0120', 'checked_at_utc': stamp, 'primary_source': source_receipt,
    'locators': ['Section 1, printed p. 2: model and overlap', 'Section 8, printed pp. 37-38: maximum and Theorem 8.1', 'Section 12(3), printed p. 59: open question'],
    'source_quote': 'Improve the fluctuation exponent in directed polymers.',
    'exact_statement': 'iid N(0,1) vertex weights; all n-vertex up/right paths from the origin in Z_+^2; free endpoint; M_n=max_p sum_{v in p}g_v. The working power goal is Var(M_n)<=C n^(1-epsilon) for some 0<epsilon<1 and all n>=2.',
    'source_vs_operational_quantifier': 'Section 12(3) asks to improve the fluctuation exponent; the epsilon inequality is the task operationalization, not a verbatim formal quantifier.',
    'scope_correction': 'The cited source does not state the intake finite-temperature log Z or general-disorder/general-dimension formulation.',
    'historical_status': 'SOURCE_ASKS_OPEN_2008', 'current_openness': 'UNKNOWN', 'novelty': 'UNVERIFIED', 'parent_problem_solved': False,
    'prior_work': {'intake': str(intake / 'attempts.jsonl') + ':98, C0120-A001, quantitative overlap/conditional exponent route without a new proof', 'named_H_I_Lean': 'No direct C0120 match in bounded targeted searches; not evidence of absence', 'Team_O': 'No C0120 row in its named board', 'other_intakes': 'Only a dedup index hit in intake F; no additional theorem recovered', 'exports': str(base / 'STORE_MATCHES.json'), 'canonical_read_only': str(base / 'CANONICAL_STORE_CHECK.json'), 'recent_primary_search': 'Bounded 2025/2026 arXiv search returned related higher-dimensional/correlated/intermediate-disorder models and Graham 0909.1352; none verifies present openness of the exact planar Gaussian target'},
    'recall': {'status': 'TIMEOUT_60S', 'index_fallback': 'No relevant hit in targeted MEMORY.md grep', 'scar_read': 'perceptron_proof_open_gaps_fleet_2026_07_12'},
    'author_served_model_evidence': {'requested': 'gpt-6.1-sol / max / Fast', 'response_side_model': None, 'account_login': None, 'state': 'UNVERIFIED; requested settings and prompt metadata do not prove served identity'},
    'independent_reviewer': 'w500', 'review_state': 'AUTHOR_PROOF_PENDING_REFEREE_AND_PROVENANCE',
    'paired_input_hashes': str(base / 'PEER_INPUT_HASHES.json'), 'patch': str(patch_dir / '01_C0120_source_scope.diff'),
}
(base / 'SOURCE_STATUS.json').write_text(json.dumps(status, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({'primary_pdf': source_receipt, 'intake_target_line': line_no if False else target_line[0], 'matched_export_rows': len(store_matches), 'canonical_status': canonical['status'], 'peer_snapshots': len(peer_hashes)}, indent=2))
