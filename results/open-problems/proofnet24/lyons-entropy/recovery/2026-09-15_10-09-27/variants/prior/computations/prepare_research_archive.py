"""Prepare an append-preserving research checkpoint and the final review bundle.

GitHub writes are deliberately external to this script. A current remote blob
inventory may be supplied at tmp/archived_blob_shas.json; already archived
numbered reports and their numbered computations must remain byte-identical.
"""
import argparse
import base64
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / 'tmp'


def git_blob_sha(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def collect(final=False):
    ledger = json.loads((ROOT / 'execution_ledger.json').read_text())
    agents = ledger['agents']
    numbers = [int(a['number']) for a in agents]
    if len(set(numbers)) != len(numbers) or sorted(numbers) != list(range(1, len(agents)+1)):
        raise ValueError('Agent numbers must be unique and contiguous')
    if len({a['task_name'] for a in agents}) != len(agents):
        raise ValueError('Actual agent task identities must be unique')
    if any(a['model'] != 'gpt-6-astra' or a['reasoning_effort'] != 'max' for a in agents):
        raise ValueError('Agent execution metadata does not match the requested configuration')
    done = {a['number'] for a in agents if a['status'] in ('completed', 'interrupted')}
    if final and (len(agents) != 100 or len(done) != 100):
        raise ValueError('Finalization requires exactly 100 actual launches, all resolved; interruptions remain explicit')
    files = {p.relative_to(ROOT).as_posix(): p for p in ROOT.glob('*.md')}
    for name in ('execution_ledger.json', 'sourcecache035_jamilov2016_provenance.json'):
        files[name] = ROOT / name
    for number in sorted(done):
        path = ROOT / 'agents' / (number + '.md')
        if not path.is_file() or path.stat().st_size < 100:
            raise ValueError('Missing substantive report: ' + str(path))
        files[path.relative_to(ROOT).as_posix()] = path
    for directory in ('computations', 'examples'):
        for path in (ROOT / directory).rglob('*'):
            if not path.is_file() or '__pycache__' in path.parts or path.suffix in ('.pyc', '.pyo'):
                continue
            rel = path.relative_to(ROOT).as_posix()
            first = path.relative_to(ROOT / directory).parts[0]
            match = re.match(r'^(\d{3})(?:_|\.)', first)
            if match and match.group(1) not in done:
                continue
            # All final numbered worker artifacts, including extensionless Lean
            # pins and licenses, are retained. No suffix allowlist can drop them.
            files[rel] = path
    if final:
        pdf = ROOT / 'output' / 'pdf' / 'proofs-and-counterexamples.pdf'
        if not pdf.is_file():
            raise ValueError('Final proof PDF must be built first')
        files['proofs-and-counterexamples.pdf'] = pdf
    return ledger, files


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--final', action='store_true')
    args = parser.parse_args()
    ledger, files = collect(args.final)
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d_%H-%M-%S')
    TMP.mkdir(exist_ok=True)
    remote_path = TMP / 'archived_blob_shas.json'
    remote = json.loads(remote_path.read_text()) if remote_path.exists() else {}
    entries, manifest = [], []
    for relative, path in sorted(files.items()):
        data = path.read_bytes()
        sha = git_blob_sha(data)
        manifest.append({'path': relative, 'bytes': len(data),
                         'sha256': hashlib.sha256(data).hexdigest(), 'git_blob_sha': sha})
        old = remote.get(relative)
        if old == sha:
            continue
        numbered = bool(re.match(r'^(agents/\d{3}\.md|computations/\d{3}(?:_|\.))', relative))
        if old and numbered:
            raise ValueError('Refusing to replace immutable archived worker bytes: ' + relative)
        try:
            content = data.decode('utf-8')
            body = {'content': content}
        except UnicodeDecodeError:
            # The calling GitHub orchestrator creates a base64 blob, then replaces
            # this preparation-only field with the returned Git blob SHA.
            body = {'binary_base64': base64.b64encode(data).decode('ascii')}
        # Root manuscripts remain append-only checkpoint snapshots until the
        # completed final packet installs its stable review index and sources.
        target = relative
        if '/' not in relative and not relative.startswith('sourcecache') and not args.final:
            target = 'checkpoints/' + stamp + '/' + relative
        entries.append({'path': target, 'mode': '100644', 'type': 'blob', **body})
    record = {'created_utc': stamp, 'final': args.final,
              'launched_agents': len(ledger['agents']),
              'completed_agents': sum(a['status'] == 'completed' for a in ledger['agents']),
              'interrupted_agents': sum(a['status'] == 'interrupted' for a in ledger['agents']),
              'files': manifest}
    record_name = 'ARCHIVE_MANIFEST.json' if args.final else 'checkpoints/' + stamp + '/ARCHIVE_MANIFEST.json'
    entries.append({'path': record_name, 'mode': '100644', 'type': 'blob',
                    'content': json.dumps(record, indent=2) + '\n'})
    serialized = json.dumps(entries, ensure_ascii=False)
    (TMP / 'checkpoint_entries.json').write_text(serialized)
    for path in TMP.glob('checkpoint_piece_*.json'):
        path.unlink()
    pieces = [serialized[i:i+18000] for i in range(0, len(serialized), 18000)]
    for i, piece in enumerate(pieces):
        (TMP / f'checkpoint_piece_{i:03d}.json').write_text(json.dumps(piece, ensure_ascii=False))
    for path in TMP.glob('checkpoint_chunk_*.json'):
        path.unlink()
    chunks, current, size = [], [], 0
    for entry in entries:
        amount = len(json.dumps(entry, ensure_ascii=False).encode())
        if current and size + amount > 24000:
            chunks.append(current)
            current, size = [], 0
        current.append(entry)
        size += amount
    if current:
        chunks.append(current)
    for i, chunk in enumerate(chunks):
        (TMP / f'checkpoint_chunk_{i:02d}.json').write_text(json.dumps(chunk, ensure_ascii=False))
    if args.final:
        out = ROOT / 'output'
        out.mkdir(exist_ok=True)
        zip_path = out / 'open-problem-research-2026-09-14.zip'
        with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as bundle:
            for relative, path in sorted(files.items()):
                bundle.write(path, relative)
            bundle.writestr('ARCHIVE_MANIFEST.json', json.dumps(record, indent=2) + '\n')
        print(json.dumps({'zip': str(zip_path), 'zip_bytes': zip_path.stat().st_size}))
    print(json.dumps({'checkpoint': stamp, 'entries': len(entries), 'chunks': len(chunks), 'pieces': len(pieces),
                      'bytes': sum(len(e.get('content', e.get('binary_base64', '')).encode()) for e in entries),
                      'launched': record['launched_agents'], 'completed': record['completed_agents']}))


if __name__ == '__main__':
    main()
