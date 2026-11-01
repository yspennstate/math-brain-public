import pathlib,urllib.request,urllib.parse,xml.etree.ElementTree as E,json
R=pathlib.Path(__file__).parent
params={'search_query':'all:"invertibility" AND au:Jain','max_results':30,'sortBy':'submittedDate','sortOrder':'descending'}
url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode(params)
try:
 with urllib.request.urlopen(url,timeout=40) as f:b=f.read()
 (R/'arxiv_jain.xml').write_bytes(b);status='OK'
 ns={'a':'http://www.w3.org/2005/Atom'}
 for e in E.fromstring(b).findall('a:entry',ns):print(e.find('a:id',ns).text,e.find('a:title',ns).text,e.find('a:summary',ns).text,flush=True)
except Exception as e:status=str(e)
(R/'final_lead_log.json').write_text(json.dumps({'url':url,'date':'2026-10-11','query':params['search_query'],'status':status},indent=2),encoding='utf8')
