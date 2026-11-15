"""Plain text web evidence, including LaTeX carried in image alt attributes."""
import re,sys,json,hashlib
from html.parser import HTMLParser
from datetime import datetime,timezone
from fetch_sources import fetch,BASE
class Plain(HTMLParser):
 def __init__(self):super().__init__();self.out=[];self.skip=0
 def handle_starttag(self,t,attrs):
  if t in ('script','style','svg'):self.skip+=1
  if t in ('p','div','br','h1','h2','h3','li'):self.out.append('\n')
  if t=='img':
   a=dict(attrs)
   if a.get('alt'):self.out.append(' '+a['alt']+' ')
 def handle_endtag(self,t):
  if t in ('script','style','svg'):self.skip=max(0,self.skip-1)
 def handle_data(self,s):
  if not self.skip:self.out.append(s)
urls={
 'bandeira_2013_blog':'https://afonsobandeira.wordpress.com/2013/12/04/deterministic-rip-matrices-a-new-cooperative-online-project/',
 'mixon_2026_blog':'https://dustingmixon.wordpress.com/2026/11/11/explicit-restricted-isometries-well-beyond-the-square-root-bottleneck/',
 'mixon_2014_blog':'https://dustingmixon.wordpress.com/2014/06/24/derandomizing-restricted-isometries-via-the-legendre-symbol/',
 'mixon_2019_blog':'https://dustingmixon.wordpress.com/2019/08/12/some-news-regarding-the-paley-graph/',
 'randomstrasse_original_blog':'https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/'
}
for name,url in urls.items():
 raw,final,ct=fetch(url);p=Plain();p.feed(raw.decode());out='URL: '+url+'\n'+re.sub(r'\n\s*\n(?:\s*\n)+','\n\n',''.join(p.out))
 (BASE/'sources'/f'{name}.txt').write_text(out)
 with (BASE/'data'/'web_sources.jsonl').open('a') as f:f.write(json.dumps({'name':name,'url':url,'retrieved_utc':datetime.now(timezone.utc).isoformat(),'response_sha256':hashlib.sha256(raw).hexdigest(),'text_sha256':hashlib.sha256(out.encode()).hexdigest()})+'\n')
 print(name,len(out),flush=True)
