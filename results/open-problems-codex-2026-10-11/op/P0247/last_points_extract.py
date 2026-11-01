from pathlib import Path
import re,pymupdf
p=Path(__file__).parent;d=pymupdf.open(p/'bht_cover.pdf')
for i in [3,4,5,38,39,40]:
 t=' '.join(d[i].get_text().split())
 print('PDF PAGE',i+1,t,flush=True)
