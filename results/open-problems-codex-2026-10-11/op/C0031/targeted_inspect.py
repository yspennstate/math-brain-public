import pathlib,json,xml.etree.ElementTree as E,urllib.request,urllib.parse
R=pathlib.Path(__file__).parent
ns={'a':'http://www.w3.org/2005/Atom'}
out=[]
for name in ['arxiv_broad.xml','arxiv_invertibility.xml']:
 for e in E.parse(R/name).findall('a:entry',ns):
  out.append('\n'+e.find('a:id',ns).text+' '+e.find('a:title',ns).text+'\n'+e.find('a:summary',ns).text)
for name in ['cr_invertibility.json','cr_almostsure.json']:
 for e in json.loads((R/name).read_text())['message']['items']:
  title=' '.join(e.get('title',[]))
  if any(w in title.lower() for w in ['matrix','matrices','singular','circular']):out.append(name+' '+title+' DOI '+e.get('DOI',''))
for e in json.loads((R/'semantic_retry.json').read_text()).get('data',[]):
 p=e['citingPaper'];title=p.get('title','')
 if any(w in title.lower() for w in ['heavy','singular','invertib','stable','levy','lévy']):out.append('CITING '+json.dumps(p,ensure_ascii=False))
(R/'targeted_literature.txt').write_text('\n'.join(out),encoding='utf8')
print('\n'.join(out),flush=True)
t=(R/'original.txt').read_text(encoding='utf8');print('ORIGINAL FIRST\n'+t[:17000],flush=True)
url='https://api.openalex.org/works/https://doi.org/10.1214/11-PS183'
try:
 with urllib.request.urlopen(url,timeout=40) as f:b=f.read()
 (R/'openalex_source_correct_doi.json').write_bytes(b)
 source=json.loads(b);source_id=source['id']
 url='https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:'+source_id,'per-page':100})
 with urllib.request.urlopen(url,timeout=40) as f:b=f.read()
 (R/'openalex_citing.json').write_bytes(b);status='OK'
except Exception as e:status='FAILED '+str(e)
(R/'openalex_citation_attempt.json').write_text(json.dumps({'url':url,'date':'2026-10-11','status':status,'coverage':'Citation list unavailable if source resolution fails'}),encoding='utf8')
print('OPENALEX CITING',status,flush=True)
