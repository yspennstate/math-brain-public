"""Independent HTML scope corroboration and safe recovery packet sealing."""
import datetime as dt
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def write(name, data):
    with (HERE / name).open('x', encoding='utf-8') as stream:
        json.dump(data, stream, indent=2)
        stream.write('\n')


def main():
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    raw = (HERE / 'primary_source_2608.23135v1.html').read_bytes()
    assert sha(raw) == 'd776336d0cb7d2cd4eae1aec8535a39b7d63a9f3e21f21e8fcfe15bc4ad3d855'
    assert len(raw) == 941920 and raw.rstrip().endswith(b'</html>')
    soup = BeautifulSoup(raw, 'html.parser')
    theorem = soup.find(id='S1.Thmdfn3')
    proof = soup.find(id='S3.5')
    assert theorem is not None and proof is not None
    claim_text = theorem.get_text(' ', strip=True)
    proof_text = proof.get_text(' ', strip=True)
    assert 'd=4,5' in claim_text
    assert 'for d = 4 d=4' in proof_text[:70]
    assert 'in dimension four' in proof_text
    assert 'Proposition 3.4' in proof_text
    old = json.loads((HERE / 'recovered03/proofs.jsonl.captured-row.json').read_text(encoding='utf-8'))
    new = json.loads((HERE / 'recovered03/proofs_v2.jsonl.captured-row.json').read_text(encoding='utf-8'))
    assert {key for key in set(old) | set(new) if old.get(key) != new.get(key)} == {'proof_opt'}
    assert old['accept'] is True and new['accept'] is True
    write('PRIMARY_SCOPE_CHECK.json', {
        'as_of': dt.datetime.now(dt.timezone.utc).isoformat(),
        'source_url': 'https://arxiv.org/html/2608.23135v1',
        'source_sha256': sha(raw),
        'theorem_element_id': 'S1.Thmdfn3', 'proof_element_id': 'S3.5',
        'theorem_element_sha256': sha(str(theorem).encode()),
        'proof_element_sha256': sha(str(proof).encode()),
        'claim_dimensions': [4, 5], 'selected_proof_explicit_dimension': 4,
        'old_new_difference_only_proof_opt': True,
        'observation': 'The retrieved full public HTML independently corroborates the selected excerpt scope. The source paper discusses dimension five elsewhere; no theorem-falsity claim is made.',
        'bound_control': 'The download cap was 8,000,001 bytes with rejection above 8,000,000. Received 941,920 bytes, ending in the HTML closing tag. This is not a proof of full original archive recovery.',
        'transcript_capture_completeness': 'Both captured row strings parse as complete JSON objects and fit below the original 7,800-character output cap. Raw archive whitespace/newline bytes were not captured.',
        'independence': 'Direct HTML element scope comparison does not invoke the root-authored heading guard. It is scope corroboration, not whole-proof verification.',
    })
    scanner_path = Path.home() / '.claude/dreaming/scan_secrets.py'
    spec = importlib.util.spec_from_file_location('f002_secret_scan', scanner_path)
    scanner = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = scanner
    spec.loader.exec_module(scanner)
    paths = sorted(p for p in HERE.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    result = scanner.main([str(p) for p in paths])
    if result != 0:
        raise RuntimeError('Secret scanner did not pass')
    write('SECRET_SCAN.json', {'result': 'CLEAN', 'files': len(paths), 'scanner_sha256': sha(scanner_path.read_bytes())})
    paths = sorted(p for p in HERE.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    write('HANDOFF.json', {
        'schema': 'f002_recovery_handoff.v1', 'as_of': dt.datetime.now(dt.timezone.utc).isoformat(),
        'finding_id': 'MB20-F002', 'status': 'RECOVERY_EVIDENCE_STAGED',
        'pins': {str(p.relative_to(HERE)): sha(p.read_bytes()) for p in paths},
        'verified': ['Both complete historical selected row objects recovered from exact pinned transcript locations.',
                     'Earlier independent capture equals the old row; both later rows differ only in proof_opt.',
                     'Digest recomputation and eight scope/predicate controls passed.',
                     'Fresh independently fetched public HTML corroborates wider theorem and dimension-four selected proof.',
                     'Existing frozen extractor matches original baseline SHA-256.'],
        'unverified': ['Original report bytes and original selected-row snapshot bytes are not recovered.',
                       'Full historical archives and their hashes are not recovered.',
                       'Exact original report SHA 7113814b6188046a7c30586151525f89a4d3c3aa044521722cf0764fceddc22f cannot be reissued.',
                       'This does not certify whole-proof validity, efficacy, scores, or audit closure.',
                       'Own brain self-care remains degraded/unverified for correction-ingestion and stale orientation coverage.'],
        'known_recovery_missteps_preserved': ['INITIAL_PARSER_FAILURE.json', 'EARLIER_CAPTURE_CORRECTION.json'],
        'integration': 'Root may register a freshly dated reproduction using these current pins and explicitly supersede the missing-report binding. Do not copy recovered objects into canonical full archives or label the new report as the old hash. Preserve missing-original history. Root owns canonical writes and audit/node/reflex/independent-review integration.',
        'rollback': 'No live writes made. Withdraw the proposed new report/packet if its pins fail; preserve recovery artifacts as evidence.',
        'search_scope': 'Only specified transcript markers/lines, root scope writer/finalizer files, exact audit-path Git history, and filenames under the specified root and September 7 audit directories. No global transcript sweep, mutation keys, locked/current35 inputs, or solver answers read.',
    })
    print(json.dumps({'handoff': str(HERE/'HANDOFF.json'), 'sha256': sha((HERE/'HANDOFF.json').read_bytes()), 'files_pinned': len(paths)}))


if __name__ == '__main__':
    main()
