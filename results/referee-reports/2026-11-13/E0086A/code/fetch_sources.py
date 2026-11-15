"""Fetch research PDFs in memory; retain only pdftotext output and metadata."""
import hashlib
import json
import pathlib
import subprocess
import urllib.request
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
ITEMS = [
    ('okada_2016_1606.03787', 'https://arxiv.org/pdf/1606.03787'),
    ('dprz_2001_thick', 'https://www.math.csi.cuny.edu/~rosen/64-erdos-taylor.pdf'),
    ('dprz_2004_cover', 'https://annals.math.princeton.edu/wp-content/uploads/annals-v160-n2-p02.pdf'),
    ('dprz_2006_late', 'https://arxiv.org/pdf/math/0303102'),
    ('dpr_2007_disc', 'https://www.math.csi.cuny.edu/~rosen/82-large-disc.pdf'),
    ('rosen_2005', 'https://arxiv.org/pdf/math/0503108'),
    ('jego_2020_thick', 'https://arxiv.org/pdf/1809.04369'),
    ('jego_2020_chaos', 'https://arxiv.org/pdf/1812.01903'),
    ('abe_cover', 'https://arxiv.org/pdf/1709.08151'),
    ('belius_kistler', 'https://arxiv.org/pdf/1405.0888'),
    ('belius_rosen_zeitouni', 'https://arxiv.org/pdf/1711.02845'),
    ('bass_rosen', 'https://arxiv.org/pdf/math/0607636'),
    ('comets_popov_vachkovskaia', 'https://arxiv.org/pdf/1502.03470'),
    ('okada_pairs', 'https://arxiv.org/pdf/1602.05641'),
    ('okada_late', 'https://arxiv.org/pdf/1605.01158'),
    ('csaki_foldes_revesz_maximal', 'https://www.math.csi.cuny.edu/~foldes/pdf/Maximallocal.pdf'),
    ('okada_inner', 'https://arxiv.org/pdf/1409.8368'),
    ('okada_sets', 'https://alea.math.cnrs.fr/articles/v16/16-42.pdf'),
    ('hao_li_okada_zheng', 'https://arxiv.org/pdf/2409.00995'),
    ('collin_popov_2026', 'https://arxiv.org/pdf/2610.26640'),
    ('lawler_limic', 'https://www.math.uchicago.edu/~lawler/srwbook.pdf'),
]

def main():
    manifest = []
    for name, url in ITEMS:
        target = ROOT / 'sources' / (name + '.txt')
        item = {'name': name, 'url': url, 'accessed_utc': datetime.now(timezone.utc).isoformat()}
        try:
            if not target.exists():
                request = urllib.request.Request(url, headers={'User-Agent': 'Research source verification'})
                raw = urllib.request.urlopen(request, timeout=45).read(16_000_000)
                if not raw.startswith(b'%PDF'):
                    raise ValueError('Response is not a PDF')
                result = subprocess.run(['pdftotext', '-layout', '-', '-'], input=raw,
                                        capture_output=True, check=True)
                target.write_bytes(result.stdout)
            text = target.read_bytes()
            item.update(status='ok', bytes=len(text), sha256=hashlib.sha256(text).hexdigest())
        except Exception as exc:
            item.update(status='failed', error=str(exc))
        manifest.append(item)
        (ROOT/'sources'/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
        print(name, item['status'], flush=True)

if __name__ == '__main__':
    main()
