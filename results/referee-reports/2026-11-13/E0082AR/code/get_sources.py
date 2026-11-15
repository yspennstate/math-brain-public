"""Independent source collection. PDF responses exist only in memory."""
import os
os.environ.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1')
import io, datetime, json, urllib.request
from pathlib import Path
from pypdf import PdfReader
items = {
 'pitman_tang_arxiv': 'https://arxiv.org/pdf/1411.0041v3',
 'pitman_tang_published': 'https://www.columbia.edu/~wt2319/Patterns.pdf?download=1',
 'shepp_1971': 'https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/First-passage-time_.pdf',
 'pitman_tang_slepian': 'https://arxiv.org/pdf/1411.0040',
 'ostaszewska_zajkowski': 'https://arxiv.org/pdf/1302.4859',
 'tang_thesis_2017': 'https://escholarship.org/content/qt51j6244c/qt51j6244c_noSplash_0d298bb720a71e482d931510dcf532d2.pdf',
 'pitman_tang_spans': 'https://arxiv.org/pdf/1506.02021',
 'pitman_tang_argmin': 'https://arxiv.org/pdf/1610.01524',
 'pozdnyakov_scan': 'https://vladimir-pozdnyakov.github.io/papers/scan.pdf',
 'li_1980': 'https://projecteuclid.org/journals/annals-of-probability/volume-8/issue-6/A-Martingale-Approach-to-the-Study-of-Occurrence-of-Sequence/10.1214/aop/1176994578.pdf',
 'noonan_zhigljavsky_linear': 'https://arxiv.org/pdf/1904.07227',
 'noonan_zhigljavsky_moving_sums': 'https://arxiv.org/pdf/1907.08201',
 'nielsen_1973': 'https://backend.orbit.dtu.dk/ws/files/4640102/PNielsen.pdf',
}
for name,url in items.items():
 if Path('sources',name+'.txt').exists(): continue
 try:
  req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
  raw=urllib.request.urlopen(req, timeout=45).read()
  assert raw.startswith(b'%PDF'), 'non-PDF response'
  doc=PdfReader(io.BytesIO(raw))
  text='Source: '+url+'\nRetrieved: '+datetime.datetime.now().isoformat()+'\n'
  for i,p in enumerate(doc.pages):
   text+='\n===== PDF PAGE '+str(i+1)+' =====\n'+p.extract_text(extraction_mode='layout')+'\n'
  Path('sources',name+'.txt').write_text(text)
  print(name,len(doc.pages),len(raw),len(text),flush=True)
 except Exception as e: print(name,type(e).__name__,str(e),flush=True)
