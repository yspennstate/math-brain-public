"""Build the reproducible research package manifest; emit bounded JSON chunks for upload."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROOT_NAMES = ['README.md', 'PROVENANCE.md', 'DIRECTIONS.md', 'CLAIMS.json', 'AGENT_LEDGER.json']

def selected():
    paths = [ROOT / name for name in ROOT_NAMES]
    paths += sorted((ROOT / 'agents').glob('*.md'))
    paths += sorted((ROOT / 'agents').glob('*.tsv'))
    paths += sorted(p for p in (ROOT / 'research').rglob('*')
                    if p.is_file() and '__pycache__' not in p.parts and p.suffix in {'.md', '.json', '.py'})
    return sorted(set(paths))

def records(paths):
    out = []
    for path in paths:
        data = path.read_bytes()
        out.append({'path': path.relative_to(ROOT).as_posix(), 'bytes': len(data),
                    'sha256': hashlib.sha256(data).hexdigest(),
                    'git_blob_sha': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()})
    return out

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--emit-chunk', type=int)
    parser.add_argument('--chunk-bytes', type=int, default=50000)
    args = parser.parse_args()
    paths = selected()
    manifest = {'schema': 'codex-research-package-v1', 'files': records(paths),
                'worker_count': 30, 'manifest_excludes_itself': True}
    target = ROOT / 'MANIFEST.json'
    manifest_text = json.dumps(manifest, indent=2, ensure_ascii=False) + '\n'
    if args.emit_chunk is None:
        target.write_text(manifest_text)
    elif target.read_text() != manifest_text:
        raise SystemExit('Manifest stale: rebuild before emitting chunks')
    chunks = [[]]
    size = 0
    for path in paths + [target]:
        content = path.read_text()
        item = {'path': path.relative_to(ROOT).as_posix(), 'mode': '100644', 'type': 'blob', 'content': content}
        n = len(json.dumps(item, ensure_ascii=False).encode())
        if size and size + n > args.chunk_bytes:
            chunks.append([])
            size = 0
        chunks[-1].append(item)
        size += n
    if args.emit_chunk is None:
        print(json.dumps({'files': len(paths) + 1, 'bytes': sum(p.stat().st_size for p in paths + [target]),
                          'chunks': len(chunks), 'reports': len(list((ROOT / 'agents').glob('a[0-9][0-9].md')))}))
    else:
        print(json.dumps(chunks[args.emit_chunk], ensure_ascii=False))

if __name__ == '__main__':
    main()
