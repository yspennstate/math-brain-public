"""Reproduce saved paper texts without saving PDFs or images.

Run from the task directory. Requires the installed pdftotext executable.
URLs and expected output hashes are in data/sources_manifest.json.
"""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import urllib.request


def main():
    manifest = json.loads(Path('data/sources_manifest.json').read_text())
    for item in manifest:
        # PDF bytes live in memory and in an anonymous subprocess pipe only.
        blob = urllib.request.urlopen(item['url'], timeout=45).read(16_000_001)
        if len(blob) > 16_000_000 or not blob.startswith(b'%PDF'):
            raise ValueError('not a PDF within the 16 MB input cap')
        raw = subprocess.run(['pdftotext', '-layout', '-', '-'], input=blob,
                             capture_output=True, check=True).stdout
        text = re.sub(r'[\x00-\x08\x0b\x0e-\x1f\x7f]',
                      lambda m: f'[U+{ord(m[0]):04X}]', raw.decode('utf-8'))
        out = text.encode('utf-8')
        if hashlib.sha256(out).hexdigest() != item['text_sha256']:
            raise ValueError(f"changed source or pdftotext output: {item['name']}")
        Path('sources',item['name']+'.txt').write_bytes(out)
        print(item['name'])


if __name__ == '__main__':
    main()
