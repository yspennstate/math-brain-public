import sys, urllib.request
from html.parser import HTMLParser
from pathlib import Path
class Text(HTMLParser):
 def __init__(self): super().__init__(); self.parts=[]; self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ('script','style'): self.skip+=1
  if tag in ('p','div','h1','h2','h3','li','br','section'): self.parts.append('\n')
 def handle_endtag(self,tag):
  if tag in ('script','style'): self.skip-=1
 def handle_data(self,s):
  if not self.skip: self.parts.append(s)
u,out=sys.argv[1:3]
r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=50).read().decode('utf-8','replace')
p=Text();p.feed(r)
s='\n'.join(l.strip() for l in ''.join(p.parts).splitlines() if l.strip())
Path(out).write_text('Source URL: '+u+'\n\n'+s)
print(out,len(s))
