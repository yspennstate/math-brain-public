import requests,pathlib,concurrent.futures,xml.etree.ElementTree as E,json
jobs=[('berger_arxiv','https://export.arxiv.org/api/query',{'search_query':'ti:"Transience" AND au:"Berger"','max_results':20}),('berger_crossref','https://api.crossref.org/works',{'query.bibliographic':'Noam Berger Transience recurrence and critical behavior for long-range percolation','rows':3}),('schur_arxiv','https://export.arxiv.org/api/query',{'search_query':'all:"Kron reduction" AND all:"resistance"','max_results':10})]
def run(t):
 name,u,p=t
 try:
  r=requests.get(u,params=p,timeout=35);pathlib.Path('second_'+name+'.txt').write_text(r.text,encoding='utf8')
  with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n- Second attempt, 2026-10-12: '+name+' '+r.url+' HTTP '+str(r.status_code)+'; raw second_'+name+'.txt\n')
  if 'arxiv' in name:
   ns={'a':'http://www.w3.org/2005/Atom'};return name,[(e.findtext('a:title',namespaces=ns),e.findtext('a:id',namespaces=ns),e.findtext('a:summary',namespaces=ns)) for e in E.fromstring(r.text).findall('a:entry',ns)]
  return name,[(x.get('title'),x.get('DOI'),x.get('volume'),x.get('page'),x.get('published')) for x in r.json().get('message',{}).get('items',[])]
 except Exception as e:return name,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for r in ex.map(run,jobs):print(json.dumps(r,ensure_ascii=False))
