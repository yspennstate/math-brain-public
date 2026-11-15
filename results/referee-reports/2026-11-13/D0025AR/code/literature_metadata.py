import urllib.request,json,pathlib,datetime
root=pathlib.Path(__file__).resolve().parents[1]
urls={
 'semantic_sly':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1609.06589?fields=title,year,journal,publicationVenue,citationCount,citations.title,citations.year,citations.externalIds',
 'openalex_sly':'https://api.openalex.org/works/https://doi.org/10.48550/arXiv.1609.06589',
 'crossref_sly':'https://api.crossref.org/works?query.title=Note%20on%20the%20flux%20for%20TASEP%20with%20general%20disorder&rows=4',
}
for name,url in urls.items():
 try:
  raw=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mathematical referee source verification'}),timeout=45).read()
  data=json.loads(raw);(root/'data'/f'{name}.json').write_text(json.dumps({'url':url,'retrieved':datetime.datetime.now(datetime.timezone.utc).isoformat(),'response':data},indent=2))
  if name=='crossref_sly': print(name,[(x.get('title'),x.get('DOI')) for x in data['message']['items']])
  else: print(name,json.dumps(data)[:6500])
 except Exception as e:print(name,e)
