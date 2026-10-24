"""Read the cited public primary PDF into w393; no credential or private input."""
from pathlib import Path
import urllib.request
import json

ROOT = Path(__file__).resolve().parent
URL = 'https://raw.githubusercontent.com/openai/math/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/main.pdf'
with urllib.request.urlopen(URL, timeout=30) as response:
    data = response.read(2_000_001)
if len(data) > 2_000_000 or not data.startswith(b'%PDF-'):
    raise RuntimeError('Expected a bounded PDF primary source.')
path = ROOT / 'source_no_bigeodesics_2026-09-24.pdf'
path.write_bytes(data)
receipt = {'url': URL, 'bytes': len(data), 'path': str(path), 'claim_validation': 'not a proof audit'}
(ROOT / 'new_source_receipt.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
try:
    import fitz
    with fitz.open(path) as document:
        text = '\n'.join(document.load_page(i).get_text() for i in range(min(2, len(document))))
except ImportError:
    from pypdf import PdfReader
    reader = PdfReader(path)
    text = '\n'.join(page.extract_text() or '' for page in reader.pages[:2])
(ROOT / 'new_source_first_two_pages.txt').write_text(text, encoding='utf-8')
print(json.dumps(receipt))
print(text[:14000])
