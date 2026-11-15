"""Independent source retrieval. PDF bytes pass only through memory and pipes."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
PAPERS = {
    '1705.04787v1': 'source_v1', '1705.04787v2': 'source_v2',
    '2108.05610': 'chen_hu_shi_2022', '1907.01601': 'chen_et_al_2021',
    '2006.06140': 'chen_shi_2020', '1811.08749': 'hu_mallein_pain',
    '1401.6919': 'derrida_retaux_2014', '2411.12189': 'li_zhang_scaling',
    '2411.13068': 'li_zhang_asymptotic', '2502.02991': 'alsmeyer_hu_mallein',
    '2005.10208': 'derrida_shi_review', '2306.12717': 'chen_hu_shi_dual',
    '2405.09741': 'chen_differentiability', '2609.11435': 'duquesne_shi_2026',
}

def fetch(url, target):
    req = urllib.request.Request(url, headers={'User-Agent': 'Independent mathematical referee source audit'})
    raw = urllib.request.urlopen(req, timeout=90).read()
    if not raw.startswith(b'%PDF'):
        raise ValueError(f'Not a PDF: {url}')
    run = subprocess.run(['pdftotext', '-layout', '-', '-'], input=raw, capture_output=True, check=True)
    text = run.stdout.decode('utf-8')
    meta = dict(url=url, retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                pdf_sha256=hashlib.sha256(raw).hexdigest(), pdf_bytes=len(raw),
                text_sha256=hashlib.sha256(run.stdout).hexdigest())
    (ROOT/'sources'/f'{target}.txt').write_text(text)
    return meta

if __name__ == '__main__':
    records = {}
    for aid, target in PAPERS.items():
        try:
            records[target] = fetch(f'https://arxiv.org/pdf/{aid}', target)
            print(target, records[target]['pdf_bytes'], flush=True)
        except Exception as e:
            records[target] = {'error': str(e)}
            print(target, str(e), flush=True)
        (ROOT/'sources'/'retrieval.json.txt').write_text(json.dumps(records, indent=2))
