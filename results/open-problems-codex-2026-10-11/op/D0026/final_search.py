import pathlib,urllib.request,urllib.parse,json,datetime,xml.etree.ElementTree as E
r=pathlib.Path(__file__).resolve().parent
q='cat:math.PR AND all:"kinetically constrained" AND submittedDate:[20251023 TO 20261011]'
u='https://export.arxiv.org/api/query?search_query='+urllib.parse.quote(q)+'&sortBy=submittedDate&sortOrder=descending&max_results=100'
rec={'service':'arxiv_exact_recent','query':q,'url':u,'date':datetime.datetime.now().isoformat()}
try:
 b=urllib.request.urlopen(u,timeout=45).read();(r/'arxiv_exact_recent.response').write_bytes(b)
 ns={'a':'http://www.w3.org/2005/Atom'};d=E.fromstring(b);es=d.findall('a:entry',ns)
 rec['entries']=len(es);rec['total']=d.findtext('{http://a9.com/-/spec/opensearch/1.1/}totalResults')
 print('total',rec['total'])
 for e in es:
  print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:summary',namespaces=ns))
except Exception as e:rec['error']=repr(e);print(repr(e))
(r/'exact_search_log.json').write_text(json.dumps(rec,indent=2),encoding='utf-8')

# Turn every saved request log into a readable journal, preserving failures.
records=[]
for name in ['search_log.json','followup_log.json','recent_log.json','exact_search_log.json']:
 data=json.loads((r/name).read_text(encoding='utf-8'))
 records.extend(data if isinstance(data,list) else [data])
lines=['\n\n## Full request journal\n']
for a in records:
 service=a.get('service',a.get('name','unknown'));query=a.get('query',urllib.parse.unquote(a['url']))
 outcome=a.get('error','HTTP success / raw response saved')
 lines.append(f"* {a['date']}: **{service}**; query `{query}`. URL: {a['url']}. Outcome: {outcome}.\n")
lines.append('\nA shell-inline attempt at the final exact-phrase query failed before issuing a request (Python quoting SyntaxError); final_search.py reruns it correctly.\n')
with (r/'LITERATURE.md').open('a',encoding='utf-8') as f:f.writelines(lines)
