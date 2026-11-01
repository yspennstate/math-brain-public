"""Seal reviewed source fragments; full web response remains private and unapproved."""
import ast
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


def write(name, value):
    if (HERE/name).exists():
        assert json.loads((HERE/name).read_text(encoding='utf-8')) == value
        return
    with (HERE/name).open('x', encoding='utf-8') as f:
        json.dump(value, f, indent=2)
        f.write('\n')


def main():
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    raw = (HERE/'primary_source_2608.23135v1.html').read_bytes()
    assert sha(raw) == 'd776336d0cb7d2cd4eae1aec8535a39b7d63a9f3e21f21e8fcfe15bc4ad3d855'
    soup = BeautifulSoup(raw, 'html.parser')
    oracle = json.loads((HERE/'PRIMARY_SCOPE_CHECK.json').read_text(encoding='utf-8'))
    for name, key in [('theorem', 'S1.Thmdfn3'), ('proof', 'S3.5')]:
        fragment = str(soup.find(id=key)).encode('utf-8')
        assert sha(fragment) == oracle[name+'_element_sha256']
        destination = HERE/('primary_'+name+'_fragment.html')
        if destination.exists():
            assert destination.read_bytes() == fragment
        else:
            with destination.open('xb') as f:
                f.write(fragment)
    write('PRIVATE_WEB_RESPONSE_SCAN_FINDING.json', {
        'file': 'primary_source_2608.23135v1.html', 'sha256': sha(raw),
        'source': 'Fresh public arXiv HTML response', 'category': 'long API key', 'count': 3,
        'disposition': 'Private retained response; not approved for publication. No matched strings were printed. Exact theorem/proof DOM fragments are separately scanned and pinned.',
        'scope': 'This is not a claim that detected strings are credentials or that an earlier exposed Git credential was rotated.',
    })
    p = Path.home()/'.claude/dreaming/scan_secrets.py'
    spec = importlib.util.spec_from_file_location('f002_scan_finish', p)
    scanner = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = scanner
    spec.loader.exec_module(scanner)
    files = sorted(x for x in HERE.rglob('*') if x.is_file()
                   and '__pycache__' not in x.parts and x.name != 'primary_source_2608.23135v1.html')
    assert scanner.main([str(x) for x in files]) == 0
    write('SECRET_SCAN_REVIEWED_FILES.json', {
        'status': 'REVIEWED_FILE_SET_CLEAN', 'count': len(files),
        'excluded_private_flagged_response': 'primary_source_2608.23135v1.html',
        'scanner_sha256': sha(p.read_bytes()),
        'files': [str(x.relative_to(HERE)) for x in files],
    })
    files.append(HERE/'SECRET_SCAN_REVIEWED_FILES.json')
    write('HANDOFF.json', {
        'schema': 'f002_recovery_handoff.v2', 'as_of': dt.datetime.now(dt.timezone.utc).isoformat(),
        'finding_id': 'MB20-F002', 'status': 'RECOVERY_EVIDENCE_STAGED',
        'pins': {str(x.relative_to(HERE)): sha(x.read_bytes()) for x in files},
        'private_excluded': {'primary_source_2608.23135v1.html': sha(raw)},
        'verified': ['Complete historical row objects at pinned transcript line 8691; old row corroborated by line 8152.',
                     'Digest recomputation and eight scope/predicate controls passed.',
                     'Fresh primary HTML theorem/proof elements independently corroborate the scope difference.',
                     'Frozen extractor exact baseline hash match; no live target writes.'],
        'unverified': ['Original report bytes, original selected-row snapshot bytes, full archives, and original full-archive hashes are not recovered.',
                       'Original report SHA 7113814b6188046a7c30586151525f89a4d3c3aa044521722cf0764fceddc22f cannot be reissued.',
                       'No whole-proof validity, score change, model efficacy, or formal audit closure certification.',
                       'Own brain self-care remains degraded/unverified for correction-ingestion and stale orientation coverage.'],
        'initial_missteps': ['Wrong native block type caused zero-capture assertion; preserved INITIAL_PARSER_FAILURE.json.',
                             'Earlier capture mislabeled v2 before comparison; actual old-row equality verified and parent explicitly corrected.',
                             'First full-response scan detected three key-like strings; full response is retained privately and excluded from the reviewed clean file set.',
                             'First HTML exploratory print hit console Unicode encoding; rerun with JSON ASCII output succeeded.'],
        'integration': 'Register a newly dated reproduction, supersede the missing old-report binding explicitly, use clean exact row captures and public DOM fragments as current evidence. Do not fabricate original report hash or full archives. Root owns canonical writes, node/reflex registration and independent-review disposition.',
        'search_scope': 'Specified transcript markers/lines, root scope writer/finalizer files, exact audit-path Git history, and filenames under root and September 7 audit paths. No global transcripts, mutation keys, locked/current35 inputs, or solver answers read.',
        'rollback': 'No live writes made; withdraw proposed integration if pins fail and preserve recovery evidence.',
    })
    print(json.dumps({'handoff': str(HERE/'HANDOFF.json'), 'sha256': sha((HERE/'HANDOFF.json').read_bytes()), 'reviewed_files': len(files)}))


if __name__ == '__main__':
    main()
