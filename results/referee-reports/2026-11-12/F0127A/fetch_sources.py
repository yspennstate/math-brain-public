#!/usr/bin/env python3
"""Fetch the primary papers examined; convert PDFs with pdftotext -layout."""
import hashlib
import json
import subprocess
import urllib.request
from pathlib import Path

SOURCES = {
    'kms': 'https://arxiv.org/pdf/1611.02460v4',
    'oliveira_peres': 'https://arxiv.org/pdf/1807.06858',
    'avena_capannoli_hazra_quattropani': 'https://arxiv.org/pdf/2308.01832v2',
    'avena_baldasso_hazra_hollander_quattropani': 'https://alea.impa.br/articles/v21/21-18.pdf',
}


def main():
    folder = Path('sources')
    folder.mkdir(exist_ok=True)
    manifest = {}
    for name, url in SOURCES.items():
        pdf = folder / (name+'.pdf')
        if not pdf.exists():
            request = urllib.request.Request(url, headers={'User-Agent': 'Research verification/1.0'})
            with urllib.request.urlopen(request, timeout=45) as response:
                pdf.write_bytes(response.read())
        data = pdf.read_bytes()
        if not data.startswith(b'%PDF'):
            raise ValueError(f'{name}: response is not a PDF')
        subprocess.run(['pdftotext', '-layout', str(pdf), str(folder/(name+'.txt'))], check=True)
        manifest[name] = dict(url=url, sha256=hashlib.sha256(data).hexdigest(), bytes=len(data))
        print(name, len(data), flush=True)
    (folder/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')


if __name__ == '__main__':
    main()
