import sys,json,urllib.parse
sys.path.insert(0,'code')
from fetch_sources import fetch,BASE
DOIS={'BFMW':'10.1007/s00041-013-9293-2','BMM':'10.1093/imrn/rnv385','Satake':'10.1016/j.laa.2021.08.018','BDFKK':'10.1215/00127094-1384809','Mixon_chapter':'10.1007/978-3-319-16042-9_13','HBP':'10.1112/jlms/jdv009','Kunisky':'10.1080/10586458.2024.2400182','Zahl':'10.1017/S0305004121000256','Burgess1988':'10.1112/blms/20.6.589','Youssef':'10.1093/imrn/rnt172'}
for key,doi in DOIS.items():
 try:
  raw,_,_=fetch('https://api.crossref.org/works/'+doi);d=json.loads(raw)['message']
  fields={k:d.get(k) for k in ['DOI','title','author','container-title','volume','issue','page','published','published-print','published-online']}
  (BASE/'sources'/('bibliography_'+key+'.txt')).write_text(json.dumps(fields,ensure_ascii=False,indent=2))
  print(key,fields['title'],fields['volume'],fields['page'],flush=True)
 except Exception as e:print('FAILED',key,repr(e),flush=True)
