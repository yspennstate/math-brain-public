from search import fetch,q,ROOT
import json,xml.etree.ElementTree as E
jobs=[
    ('second_arxiv','https://export.arxiv.org/api/query?search_query='+q('all:"random walks" AND all:"bounded index"')+'&max_results=30'),
    ('second_crossref','https://api.crossref.org/works?query='+q('random walks symmetric cyclic direct product random generators')+'&rows=15')]
results=[fetch(x) for x in jobs]
(ROOT/'second_search_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
try:
    root=E.fromstring((ROOT/'second_arxiv.raw').read_text());ns={'a':'http://www.w3.org/2005/Atom'}
    entries=[]
    for x in root.findall('a:entry',ns):
        entries.append({k:x.find('a:'+k,ns).text for k in ['id','title','summary']})
    (ROOT/'second_arxiv.json').write_text(json.dumps(entries,indent=2),encoding='utf-8')
    print(json.dumps(entries,indent=2))
except Exception as e:print('arxiv parse:',e)
try:
    j=json.loads((ROOT/'second_crossref.raw').read_text())['message']['items']
    print(json.dumps([{'title':x.get('title'),'doi':x.get('DOI')} for x in j],indent=2))
except Exception as e:print('crossref parse:',e)
