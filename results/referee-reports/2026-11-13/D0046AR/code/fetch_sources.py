"""Fetch primary papers; PDFs exist in memory only. Output is plain text."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time
import requests

ROOT = Path(__file__).resolve().parents[1]
PAPERS = {
    'virag_1804.06953': '1804.06953',
    'holcomb_paquette_1707.02700': '1707.02700',
    'edelman_jeong_nissim_2411.01633v3': '2411.01633v3',
    'corwin_hammond_1108.2291': '1108.2291',
    'allez_guionnet_1206.1460': '1206.1460',
    'dumitriu_edelman_math-ph_0206043': 'math-ph/0206043',
    'li_1007.3905': '1007.3905',
    'yabuoku_2204.00736': '2204.00736',
    'landon_sosoe_yau_1609.09011': '1609.09011',
    'landon_2009.11176': '2009.11176',
    'gorin_xu_zhang_2411.10829': '2411.10829',
    'huang_zhang_2411.10586': '2411.10586',
    'assiotis_li_2609.26386': '2609.26386',
    'kwak_2610.35808': '2610.35808',
}

def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
    out = ROOT / 'sources'
    out.mkdir(exist_ok=True)
    (ROOT / 'data').mkdir(exist_ok=True)
    manifest = {}
    for name, aid in PAPERS.items():
        url = 'https://arxiv.org/pdf/' + aid
        try:
            response = requests.get(url, timeout=90)
            response.raise_for_status()
            raw = response.content
            if not raw.startswith(b'%PDF'):
                raise ValueError('Response is not PDF')
            # Poppler handles math fonts without embedding control-code glyphs.
            converted = subprocess.run(['pdftotext', '-layout', '-', '-'], input=raw,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            text = converted.stdout.decode('utf-8')
            pages = text.count('\f')
            (out / (name + '.txt')).write_text(text)
            manifest[name] = dict(url=url, pages=pages, pdf_sha256=hashlib.sha256(raw).hexdigest(), text_sha256=hashlib.sha256(text.encode()).hexdigest())
            print(name, pages, flush=True)
        except Exception as exc:
            manifest[name] = dict(url=url, error=str(exc))
            print(name, 'FAILED', str(exc), flush=True)
        (ROOT / 'data' / 'source_manifest.json').write_text(json.dumps(manifest, indent=2))
        time.sleep(0.2)

if __name__ == '__main__':
    main()
