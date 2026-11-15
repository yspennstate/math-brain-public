import os, re, sys, json, hashlib
from pathlib import Path
from html.parser import HTMLParser
from fetch_sources import BASE, fetch, save_pdf
class Text(HTMLParser):
 def __init__(self): super().__init__(); self.out=[]; self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ('script','style','svg'): self.skip+=1
  if tag in ('p','div','section','h1','h2','h3','li','br'): self.out.append('\n')
 def handle_endtag(self,tag):
  if tag in ('script','style','svg'): self.skip=max(0,self.skip-1)
 def handle_data(self,s):
  if not self.skip: self.out.append(s)
 def text(self): return re.sub(r'\n[ \t]*\n(?:[ \t]*\n)+','\n\n',''.join(self.out))
PDFS={
 'kunisky_yu_published_CCC2023':'https://drops.dagstuhl.de/storage/00lipics/lipics-vol264-ccc2023/LIPIcs.CCC.2023.30/LIPIcs.CCC.2023.30.pdf',
 'wang_shen_kobzar':'https://yw3762.github.io/assets/pdf/paley.pdf',
 'kaplan_pohl_boche':'https://sampta2019.sciencesconf.org/267683/Kaplan.pdf',
 'bandeira_ten_lectures':'https://people.math.ethz.ch/~abandeira/TenLecturesFortyTwoProblems.pdf',
}
HTMLS={
 'bandeira_2013_blog':'https://afonsobandeira.wordpress.com/2013/12/04/deterministic-rip-matrices-a-new-cooperative-online-project/',
 'mixon_2026_blog':'https://dustingmixon.wordpress.com/2026/11/11/explicit-restricted-isometries-well-beyond-the-square-root-bottleneck/',
 'mixon_publications':'https://people.math.osu.edu/mixon.23/',
 'randomstrasse_html_v1':'https://arxiv.org/html/2603.29571v1'
}
for name,url in PDFS.items():
 try: save_pdf(name,url)
 except Exception as e: print('FAILED',name,repr(e),flush=True)
for name,url in HTMLS.items():
 try:
  raw,final,ct=fetch(url); parser=Text();parser.feed(raw.decode()); out=parser.text()
  (BASE/'sources'/f'{name}.txt').write_text('URL: '+url+'\n'+out)
  print(name,len(out),flush=True)
 except Exception as e: print('FAILED',name,repr(e),flush=True)
for p in (BASE/'sources').glob('*_metadata.txt'):
 raw=p.read_text()
 if '<html' not in raw: continue
 parser=Text();parser.feed(raw)
 # Preserve machine-readable bibliographic fields as plain text.
 metas=re.findall(r'<meta name="citation_([^"]+)" content="([^"]*)"',raw)
 p.write_text('\n'.join(k+': '+v for k,v in metas)+'\n'+parser.text())
