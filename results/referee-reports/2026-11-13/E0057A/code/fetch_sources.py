"""Fetch primary papers into plain text; never persist PDF bytes."""
import io, json, hashlib, os, sys, time
from pathlib import Path
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import requests
from pypdf import PdfReader
ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
 'bandeira_notes': 'https://people.math.ethz.ch/~abandeira/TenLecturesFortyTwoProblems.pdf',
 'perry_2019': 'https://web.math.princeton.edu/~amits/publications/MRA_SIMODS_Published.pdf',
 'brunel_2019': 'https://proceedings.mlr.press/v99/brunel19a/brunel19a.pdf',
 'optimal_rates': 'https://arxiv.org/pdf/1702.08546',
 'aperiodic': 'https://arxiv.org/pdf/1710.02793',
 'bispectrum': 'https://arxiv.org/pdf/1705.00641',
 'fan_sun_wang_wu': 'https://arxiv.org/pdf/2004.00041',
 'dihedral': 'https://arxiv.org/pdf/2107.05262',
}
def main():
 names = sys.argv[1:] or list(SOURCES)
 manifest_path = ROOT/'sources'/'manifest.json'
 manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
 for name in names:
  url = SOURCES.get(name, name.split('=',1)[-1])
  if '=' in name: name = name.split('=',1)[0]
  try:
   res = requests.get(url, timeout=90); res.raise_for_status()
   reader = PdfReader(io.BytesIO(res.content))
   text = '\n'.join(f'\n===== PDF PAGE {i+1} =====\n'+(p.extract_text(extraction_mode='layout') or '') for i,p in enumerate(reader.pages))
   (ROOT/'sources'/f'{name}.txt').write_text(f'SOURCE URL: {url}\nPDF SHA256: {hashlib.sha256(res.content).hexdigest()}\nExtracted {time.strftime("%Y-%m-%d %H:%M:%S %z")}\n'+text)
   manifest[name] = {'url':url,'pdf_sha256':hashlib.sha256(res.content).hexdigest(),'text_sha256':hashlib.sha256(text.encode()).hexdigest(),'pages':len(reader.pages),'retrieved':time.strftime('%Y-%m-%d %H:%M:%S %z')}
   manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
   print(name, len(reader.pages), 'pages',flush=True)
  except Exception as e: print(name, type(e).__name__,str(e),flush=True)
if __name__ == '__main__': main()
