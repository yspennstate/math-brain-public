"""Build a content-addressed manifest and print Git tree entries for this package."""
from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]
def blob_sha(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def main():
    files = sorted(p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name != 'MANIFEST.json')
    records = []
    entries = []
    for p in files:
        data = p.read_bytes()
        rel = p.relative_to(ROOT).as_posix()
        records.append({'path': rel, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'git_blob': blob_sha(data)})
        entries.append({'path': rel, 'mode': '100644', 'type': 'blob', 'content': data.decode('utf-8')})
    manifest = {'format': 1, 'package': 'open-frontier-continuation-2026-10-24', 'files': records, 'excluded': ['MANIFEST.json (self-reference)']}
    text = json.dumps(manifest, ensure_ascii=False, indent=2) + '\n'
    (ROOT / 'MANIFEST.json').write_text(text)
    entries.append({'path':'MANIFEST.json','mode':'100644','type':'blob','content':text})
    print(json.dumps({'entries':entries, 'manifest':manifest, 'manifest_blob':blob_sha(text.encode())}, ensure_ascii=False))

if __name__ == '__main__':
    main()
