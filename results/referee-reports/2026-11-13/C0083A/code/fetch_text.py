"""Fetch arXiv TeX sources only; never save PDFs or image members."""
import io
import gzip
import json
from pathlib import Path
import sys
import tarfile
import urllib.request

ROOT = Path(__file__).resolve().parents[1]

def fetch(identifier):
    url = 'https://arxiv.org/src/' + identifier
    with urllib.request.urlopen(url, timeout=60) as response:
        payload = response.read(16_000_000)
        content_type = response.headers.get('Content-Type', '')
    if payload.startswith(b'%PDF'):
        raise ValueError('Refusing a PDF response')
    target = ROOT / 'data' / 'sources' / identifier.replace('/', '_')
    target.mkdir(parents=True, exist_ok=True)
    files = []
    if payload.startswith(b'\x1f\x8b'):
        payload = gzip.decompress(payload)
    try:
        archive = tarfile.open(fileobj=io.BytesIO(payload), mode='r:')
    except tarfile.ReadError:
        if b'\\documentclass' not in payload and b'\\documentstyle' not in payload:
            raise ValueError('Response is neither a source tar nor a TeX document')
        (target / 'main.tex').write_bytes(payload)
        files.append('main.tex')
        archive = None
    if archive is not None:
        for member in archive:
            if not member.isfile() or Path(member.name).suffix.lower() not in {'.tex', '.bib', '.bbl', '.txt'}:
                continue
            name = Path(member.name)
            if name.is_absolute() or '..' in name.parts:
                raise ValueError('Unsafe archive member')
            destination = target / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(archive.extractfile(member).read())
            files.append(str(name))
        archive.close()
    (target / 'provenance.json').write_text(json.dumps({'url': url, 'content_type': content_type, 'files': files}, indent=2) + '\n')
    print(identifier, files)

if __name__ == '__main__':
    for identifier in sys.argv[1:]:
        fetch(identifier)
