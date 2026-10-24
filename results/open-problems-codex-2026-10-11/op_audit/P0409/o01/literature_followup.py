import concurrent.futures,json,pathlib,re,urllib.request
BASE=pathlib.Path(__file__).resolve().parent
urls={
 'arxiv_html_search':'https://arxiv.org/search/?query=ideal+Voronoi&searchtype=all&abstracts=show&order=-announced_date_first&size=50',
 'openalex_retry':'https://api.openalex.org/works?search=Ideal%20Poisson%20Voronoi&per_page=10',
 'crossref':'https://api.crossref.org/works?query=ideal%20Poisson%20Voronoi&rows=12',
 **{f'abstract_{i}':f'https://arxiv.org/abs/{i}' for i in ['2606.26049','2606.30517','2602.06906','2609.10007','2408.10009','2412.00822']}}
def fetch(item):
 name,url=item
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as r:data=r.read().decode('utf-8')
  (BASE/(name+'.txt')).write_text(data,encoding='utf-8')
  if name=='crossref':return name,[{'title':v.get('title'),'DOI':v.get('DOI')} for v in json.loads(data)['message']['items']]
  if name.startswith('abstract'):
   title=re.search(r'<title>(.*?)</title>',data,re.S)
   abstract=re.search(r'<blockquote[^>]*class="abstract[^>]*>(.*?)</blockquote>',data,re.S)
   return name,{'title':title.group(1) if title else None,'abstract':re.sub('<[^>]+>',' ',abstract.group(1)).strip() if abstract else None}
  return name,re.sub('<[^>]+>',' ',data)[:22000]
 except Exception as e:return name,repr(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:out=dict(pool.map(fetch,urls.items()))
(BASE/'literature_followup.json').write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(out,indent=2,ensure_ascii=False))
