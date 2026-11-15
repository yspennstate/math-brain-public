import requests,json,datetime
from pathlib import Path
DOIS=['10.1007/s00030-025-01090-2','10.1088/1361-6544/abd613','10.1007/s00028-022-00786-7','10.1007/s40072-019-00134-w','10.1007/BF01084893','10.1007/978-3-319-22354-4','10.1007/s00440-023-01249-x','10.1007/s00220-023-04867-7','10.5802/crmath.833','10.1016/j.jfa.2010.05.012']
results=[]
for doi in DOIS:
    url='https://api.crossref.org/works/'+doi
    try:
        r=requests.get(url,timeout=15); r.raise_for_status(); m=r.json()['message']
        keys=('DOI','title','subtitle','author','container-title','volume','issue','page','article-number','published','published-online','published-print','URL')
        d={k:m[k] for k in keys if k in m};d['source_url']=url;results.append(d)
        print(doi,d.get('container-title'),d.get('volume'),d.get('page'),d.get('article-number'),flush=True)
    except Exception as e: results.append(dict(doi=doi,error=str(e)));print(doi,str(e),flush=True)
Path('sources/bibliography_metadata.txt').write_text('Crossref DOI metadata; independently retrieved '+datetime.datetime.now().astimezone().isoformat()+'\n'+json.dumps(results,indent=2,ensure_ascii=False)+'\n')
