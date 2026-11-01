from pathlib import Path
import urllib.request, urllib.parse, xml.etree.ElementTree as ET, json
root = Path(__file__).resolve().parent
url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': '(all:"symmetric" AND all:"heavy traffic") OR (all:"service disciplines" AND all:"heavy traffic")', 'max_results': 50})
try:
    with urllib.request.urlopen(url, timeout=45) as response:
        data = response.read()
    (root/'arxiv_broad.response').write_bytes(data)
    ns = {'a':'http://www.w3.org/2005/Atom'}
    results = [{'title':e.findtext('a:title',namespaces=ns), 'id':e.findtext('a:id',namespaces=ns), 'summary':e.findtext('a:summary',namespaces=ns)} for e in ET.fromstring(data).findall('a:entry',ns)]
    record = {'url':url,'entries':results}
except Exception as exc:
    record = {'url':url,'error':str(exc)}
(root/'broader_literature.json').write_text(json.dumps(record,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(record,ensure_ascii=False))
