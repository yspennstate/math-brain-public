import research_fetch as f
import urllib.parse,json,xml.etree.ElementTree as ET
R=f.ROOT
url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'id_list':'2510.24562','max_results':1})
r=f.fetch(('arxiv_random_environment',url))
(R/'ledger_lead_log.json').write_text(json.dumps([r],indent=2),encoding='utf8');print(json.dumps(r))
p=R/'arxiv_random_environment.json';ns={'a':'http://www.w3.org/2005/Atom'}
if p.exists():
 for e in ET.fromstring(p.read_bytes()).findall('a:entry',ns):
  print(e.findtext('a:title',namespaces=ns));print([a.findtext('a:name',namespaces=ns) for a in e.findall('a:author',ns)]);print(e.findtext('a:summary',namespaces=ns))
