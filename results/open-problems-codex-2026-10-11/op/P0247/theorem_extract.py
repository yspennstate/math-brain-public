from pathlib import Path
import pymupdf
p=Path(__file__).parent
for name,pages in [('bht_cover',[3,4,5,38,39,40]),('wired_planar',[0,1,2])]:
 d=pymupdf.open(p/(name+'.pdf'))
 for i in pages:print(name,'PDF PAGE',i+1,d[i].get_text())
