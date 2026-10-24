"""Read only the exact P0117 intake row; retrieve its primary public source."""
from pathlib import Path
import json
import importlib.util
import urllib.request

ROOT = Path(__file__).resolve().parent
INTAKE = Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/brain_bundle_C006p01.json')
data = json.loads(INTAKE.read_text(encoding='utf-8-sig'))
rows = [e for e in data.get('entries', []) if 'p0117' in json.dumps(e, ensure_ascii=False).lower()]
(ROOT / 'P0117_INTAKE_EXACT.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(rows, ensure_ascii=False, indent=2), flush=True)
print('PDF text readers:', {m: importlib.util.find_spec(m) is not None for m in ['pypdf', 'fitz', 'pdfplumber']}, flush=True)
url = 'https://arxiv.org/pdf/1511.03262'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'P0117-source-verification/1.0'})
    with urllib.request.urlopen(req, timeout=25) as response:
        blob = response.read(12000000)
    if not blob.startswith(b'%PDF'):
        raise ValueError('Response is not a PDF')
    (ROOT / 'ADH_1511.03262.pdf').write_bytes(blob)
    print('Retrieved primary PDF:', len(blob), 'bytes', flush=True)
except Exception as exc:
    print('PRIMARY_RETRIEVAL_UNAVAILABLE:', type(exc).__name__, str(exc), flush=True)
