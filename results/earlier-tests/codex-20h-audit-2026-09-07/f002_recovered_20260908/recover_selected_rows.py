"""Recover only the authorized F002 row captures; never replay transcript code."""
import ast
import datetime as dt
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent / 'math-brain-20h-20260907'
TRANSCRIPT = Path.home() / '.codex/sessions/<ROLLOUT>'
DIGEST = '2dc1a24f5f9372bc'
LINE_HASHES = {
    8691: 'aed598506b8da3bc6723c4fe3a270aa4387e95f22ff1532677894f765fd68702',
    8152: '04b3e77541511cda086d37cbf6887e21d110b35f7d79a14901fb9e1a3f28550d',
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def captured_rows(record):
    rows = []
    for item in record['payload']['output']:
        if item.get('type') not in ('text', 'input_text'):
            continue
        try:
            envelope = json.loads(item['text'])
        except (ValueError, TypeError):
            continue
        text = envelope.get('output', '')
        if not isinstance(text, str):
            continue
        for line in text.splitlines():
            try:
                row = json.loads(line)
            except ValueError:
                continue
            if isinstance(row, dict) and row.get('digest') == DIGEST:
                rows.append((line, row))
    return rows


def main():
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    target = HERE / 'recovered03'
    target.mkdir(exist_ok=False)
    captures = {}
    pins = []
    with TRANSCRIPT.open(encoding='utf-8') as stream:
        for number, line in enumerate(stream, 1):
            if number not in LINE_HASHES:
                continue
            assert sha(line.encode('utf-8')) == LINE_HASHES[number], 'Target transcript line changed'
            record = json.loads(line)
            captures[number] = captured_rows(record)
            pins.append({'line': number, 'timestamp': record['timestamp'],
                         'normalized_line_sha256': LINE_HASHES[number],
                         'note': 'Hash of complete transcript line after universal newline decoding; raw transcript is not copied.'})
            if len(captures) == len(LINE_HASHES):
                break
    assert len(captures[8691]) == 2 and len(captures[8152]) == 1
    old, new = [pair[1] for pair in captures[8691]]
    assert 'proof_opt' not in old and 'proof_opt' in new
    assert captures[8152][0][1] == old, 'Independent earlier old-row tool capture differs'
    for name, pair in zip(['proofs.jsonl', 'proofs_v2.jsonl'], captures[8691]):
        # This is the exact JSON object string visible in historical tool output.
        # Original archive whitespace/newline bytes were not printed, so do not
        # call this an exact recovery of the old archive or snapshot file bytes.
        (target / (name + '.captured-row.json')).write_bytes((pair[0] + '\n').encode('utf-8'))
    computed = sha(re.sub(r'\s+', ' ', new['statement'] + '|' + ' '.join(new['steps'])).encode())[:16]
    assert computed == DIGEST
    assert old['accept'] is True and new['accept'] is True
    assert old['statement'] == new['statement'] and old['steps'] == new['steps']
    assert 'd=4,5' in new['statement'] and 'dimension four' in new['steps'][-1]
    assert new['proof_opt'].endswith('for $d=4$')
    extractor = (ROOT / 'bank_baseline/extract_proofs.py').read_bytes()
    assert sha(extractor) == '26df4ed150f1cca2523addcc8e4ad2abfd8847c858c917a4853bd3f58937152f'
    guard_path = ROOT / 'heading_scope_guard.py'
    spec = importlib.util.spec_from_file_location('f002_recovery_heading_guard', guard_path)
    guard = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = guard
    spec.loader.exec_module(guard)
    original = guard.load_original_predicate()
    assert original(new['proof_opt']) is False
    assert guard.assess(new, original)['status'] == 'QUALIFIED_HEADING_REQUIRES_SCOPE_REVIEW'
    assert guard.assess(old, original)['status'] == 'HEADING_METADATA_UNVERIFIED'
    assert guard.assess({'proof_opt': ''}, original)['status'] == 'NO_HEADING_SCOPE_FLAG'
    # A matching restricted statement is still sent for review: this predicate
    # does not itself decide semantic mismatch, validity, or falsity.
    matching = dict(new, statement='Let d=4. The claimed coupling holds.')
    assert guard.assess(matching, original)['status'] == 'QUALIFIED_HEADING_REQUIRES_SCOPE_REVIEW'
    changed = dict(new, statement=new['statement'].replace('d=4,5', 'd=4'))
    assert sha(re.sub(r'\s+', ' ', changed['statement'] + '|' + ' '.join(changed['steps'])).encode())[:16] != DIGEST
    (target / 'extract_proofs.frozen.py').write_bytes(extractor)
    (target / 'heading_scope_guard.py').write_bytes(guard_path.read_bytes())
    manifest = {
        'schema': 'f002_transcript_object_recovery.v1',
        'as_of': dt.datetime.now(dt.timezone.utc).isoformat(),
        'transcript': str(TRANSCRIPT), 'transcript_pins': pins,
        'row_digest': DIGEST, 'recomputed_digest_matches': True,
        'historical_archive_lines': {'proofs.jsonl': 2701, 'proofs_v2.jsonl': 2701},
        'recovery': {
            'complete_selected_row_objects': 'RECOVERED_FROM_HISTORICAL_TOOL_OUTPUT',
            'second_earlier_old_row_capture': 'EXACT_OBJECT_MATCH',
            'original_archive_or_snapshot_bytes': 'UNVERIFIED_NOT_RECOVERED',
            'original_report_sha256': '7113814b6188046a7c30586151525f89a4d3c3aa044521722cf0764fceddc22f',
            'original_report_bytes': 'NOT_RECOVERED',
            'full_original_archives': 'NOT_RECOVERED',
            'old_full_archive_hashes': 'NOT_RECOVERED',
            'frozen_extractor': 'EXACT_EXISTING_HASH_MATCH',
        },
        'reproduction': {
            'accepted_in_both': True, 'same_statement_and_steps': True,
            'claim_dimensions': [4, 5], 'explicit_proof_dimension': 4,
            'old_heading_flag': False, 'candidate': guard.assess(new, original),
            'legacy_missing_heading': guard.assess(old, original),
            'scope': 'Packaged proof scope only; no assertion that source theorem is false; no score, key, or solver-answer changes.',
        },
        'controls': {'earlier_capture_equal': True, 'digest_recomputed': True,
                     'tampered_statement_digest_changes': True,
                     'original_predicate_misses_qualifier': True,
                     'candidate_requests_review': True, 'missing_heading_withheld': True,
                     'ordinary_empty_heading_preserved': True,
                     'matching_qualified_pair_still_review_not_false': True},
        'artifact_pins': {p.name: sha(p.read_bytes()) for p in sorted(target.iterdir()) if p.is_file()},
        'canonical_writes': 0, 'independence': 'New recovery investigator; reused root-authored guard; no independent mathematical closure.',
        'brain_selfcare': 'Own wake remains degraded/unverified; correction-ingestion and stale orientation coverage not certified by this packet.',
    }
    (target / 'RECOVERY.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'output': str(target), 'sha256': sha((target/'RECOVERY.json').read_bytes()), 'controls': manifest['controls']}))


if __name__ == '__main__':
    main()
