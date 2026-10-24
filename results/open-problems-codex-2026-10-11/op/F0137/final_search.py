from research import fetch
import json,pathlib,urllib.parse,subprocess,xml.etree.ElementTree as ET
R=pathlib.Path(__file__).resolve().parent
r=fetch('openalex_direct_source.json','https://api.openalex.org/works/https://doi.org/10.5802/afst.1542')
if 'error' not in r:
 w=json.loads((R/'openalex_direct_source.json').read_text())['id']
 fetch('openalex_citing.json','https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:'+w,'per-page':100,'sort':'publication_date:desc'}))
else:
 # DOI-form citation filter is attempted, but no successful graph traversal is claimed if the service rejects it.
 fetch('openalex_citing_attempt.json','https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:https://doi.org/10.5802/afst.1542','per-page':100,'sort':'publication_date:desc'}))
paths=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True,encoding='utf8',timeout=90).stdout.splitlines()
hits=[p for p in paths if any(s in p.lower() for s in ['f0137','sabot_tournier','dirichlet'])]
(R/'repository_path_hits.json').write_text(json.dumps(hits,indent=2),encoding='utf8')
print('REPOSITORY_PATHS',json.dumps(hits[:35]),flush=True)
ns={'a':'http://www.w3.org/2005/Atom'}
for e in ET.parse(R/'arxiv_T.xml').findall('a:entry',ns):
 print('ARXIV',e.findtext('a:id',namespaces=ns),' '.join(e.findtext('a:title',namespaces=ns).split()),flush=True)
for x in json.loads((R/'github.json').read_text()).get('items',[]): print('GITHUB',x['full_name'],x.get('description'),flush=True)
