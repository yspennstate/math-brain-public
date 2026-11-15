"""Fetch primary-source PDFs into memory and save text only (no PDF files)."""
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    'biskup_1712.09972': '1712.09972',
    'biskup_louidor_1612.01424': '1612.01424',
    'aidekon_hu_shi_1710.00348': '1710.00348',
    'biskup_louidor_extremal_1606.00510': '1606.00510',
    'junnila_saksman_webb_imaginary_1806.02118': '1806.02118',
    'junnila_saksman_webb_decompositions_1808.06838': '1808.06838',
    'garban_holden_sepulveda_sun_1805.00864': '1805.00864',
    'berestycki_webb_wong_1701.03289': '1701.03289',
    'junnila_lambert_webb_2209.06548': '2209.06548',
    'lacoin_rhodes_vargas_1307.6117': '1307.6117',
    'aru_lupu_sepulveda_1805.09204': '1805.09204',
    'daviaud_math_0406609': 'math/0406609',
    'biskup_louidor_intermediate_final': 'https://www.math.ucla.edu/~biskup/PDFs/papers/GFF-intermediate-final-AIHP.pdf',
}

def fetch(name, aid):
    dest = ROOT / 'sources' / (name + '.txt')
    url = aid if aid.startswith('https://') else 'https://arxiv.org/pdf/' + aid
    if not dest.exists() or dest.stat().st_size < 1000:
        raw = subprocess.run(['curl', '-fsSL', '--max-time', '90', url],
                             capture_output=True, check=True).stdout
        assert raw.startswith(b'%PDF'), (name, raw[:100])
        txt = subprocess.run(['pdftotext', '-layout', '-', '-'], input=raw,
                             capture_output=True, check=True).stdout
        dest.write_bytes(txt)
    txt = dest.read_bytes()
    return dict(file=str(dest.relative_to(ROOT)), url=url,
                sha256_text=hashlib.sha256(txt).hexdigest(), bytes=len(txt),
                pages=txt.count(b'\x0c'))

if __name__ == '__main__':
    manifest = []
    for name, aid in SOURCES.items():
        try:
            item = fetch(name, aid)
            manifest.append(item)
            print(name, item['pages'], flush=True)
        except Exception as e:
            manifest.append(dict(file=name, error=str(e)))
            print(name, repr(e), flush=True)
        (ROOT/'sources'/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
