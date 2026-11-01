from pathlib import Path
import pymupdf,urllib.request,urllib.parse,xml.etree.ElementTree as E,json
r=Path(__file__).resolve().parent
for name,pages in [('CIK',[0,1,2,3,4]),('KRV',[54,55,56])]:
 doc=pymupdf.open(r/(name+'.pdf'))
 for i in pages:print('\n',name,'PDF PAGE',i+1,'\n',doc[i].get_text(),flush=True)
q='ti:"Universality of a double scaling limit near singular edge points"'
url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':q,'max_results':5})
try:
 with urllib.request.urlopen(url,timeout=30) as d:data=d.read()
 (r/'CV_search.xml').write_bytes(data)
 ns={'a':'http://www.w3.org/2005/Atom'}
 for e in E.fromstring(data).findall('a:entry',ns):
  id=e.find('a:id',ns).text.split('/abs/')[-1];print('CV ID',id,flush=True)
  with urllib.request.urlopen('https://arxiv.org/pdf/'+id,timeout=40) as d:pdf=d.read(12000000)
  (r/'CV.pdf').write_bytes(pdf);doc=pymupdf.open(stream=pdf,filetype='pdf')
  text='\n'.join('\nPDF PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(doc))
  (r/'CV.txt').write_text(text,encoding='utf8')
  for word in ['Theorem 1.7','Theorem 1.6','Theorem 1.5']:
   pos=text.find(word)
   if pos>=0:print(word,text[max(0,pos-1000):pos+4000],flush=True)
except Exception as e:print('CV SEARCH ERROR',e,flush=True)
(r/'targeted_search_log.json').write_text(json.dumps({'date':'2026-10-12','queries':[url,'https://arxiv.org/pdf/0901.2473','https://arxiv.org/pdf/1306.4832']},indent=2),encoding='utf8')
