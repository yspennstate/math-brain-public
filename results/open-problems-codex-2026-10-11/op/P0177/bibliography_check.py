import pathlib,json,urllib.request,urllib.parse,xml.etree.ElementTree as ET
c=json.loads(pathlib.Path('crossref.response').read_bytes())
for x in c['message']['items']:
 if x.get('DOI') in ['10.4064/cm8413-6-2021','10.7900/jot.2019mar23.2264']:
  print(json.dumps({k:x.get(k) for k in ['title','author','published','volume','issue','page','DOI','container-title']},ensure_ascii=False))
s=pathlib.Path('source.txt').read_text(encoding='utf8');i=s.rfind('Biane, P.');print(s[i:i+800])
r=ET.fromstring(pathlib.Path('arxiv_modes.response').read_bytes());ns={'a':'http://www.w3.org/2005/Atom'}
for e in r.findall('a:entry',ns):print(e.findtext('a:id','',ns),' '.join(e.findtext('a:title','',ns).split()),' '.join(e.findtext('a:summary','',ns).split())[:500])
u='https://api.openalex.org/works?filter='+urllib.parse.quote('cites:https://doi.org/10.30757/ALEA.v15-15')+'&per-page=100'
try:
 b=urllib.request.urlopen(u,timeout=30).read();pathlib.Path('openalex_citations_doi.response').write_bytes(b);result='OK '+str(len(b))
except Exception as e:result=repr(e)
with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n- OpenAlex DOI citation filter (2026-10-11): '+u+'\n  '+result+'\n')
print('OpenAlex citations DOI',result)
