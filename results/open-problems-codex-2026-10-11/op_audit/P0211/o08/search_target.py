from pathlib import Path
import urllib.request, urllib.parse, xml.etree.ElementTree as ET, json
import fitz
ROOT=Path(__file__).resolve().parent
q='all:fragmentation AND (all:Aldous OR all:"linear polymers" OR all:"relaxation time")'
url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':q,'max_results':40})
log=[]
try:
 data=urllib.request.urlopen(url,timeout=45).read()
 (ROOT/'arxiv_target.xml').write_bytes(data)
 log.append({'url':url,'status':'OK'})
 ns={'a':'http://www.w3.org/2005/Atom'}
 for e in ET.fromstring(data).findall('a:entry',ns):
  print(e.find('a:id',ns).text,' '.join(e.find('a:title',ns).text.split()),' '.join(e.find('a:summary',ns).text.split())[:1200])
except Exception as e: log.append({'url':url,'status':str(e)})
url='https://arxiv.org/pdf/1609.00697'
try:
 data=urllib.request.urlopen(url,timeout=45).read(); (ROOT/'survey.pdf').write_bytes(data)
 doc=fitz.open(stream=data,filetype='pdf')
 (ROOT/'survey.pdf.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
 log.append({'url':url,'status':'OK'})
except Exception as e: log.append({'url':url,'status':str(e)})
(ROOT/'target_fetch_results.json').write_text(json.dumps(log,indent=2),encoding='utf-8')
print(log)
