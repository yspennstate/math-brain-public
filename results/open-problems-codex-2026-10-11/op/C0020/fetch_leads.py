exec(open('targeted_search.py',encoding='utf-8-sig').read().split('with concurrent.futures')[0])
Q={k:'https://arxiv.org/pdf/'+k for k in ['2606.32024','2408.12995','2408.08457','2609.15388','1708.03643']}
Q['openalex_doi']='https://api.openalex.org/works/doi:10.1017/cbo9781139924160'
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:rows=list(ex.map(lambda kv:f(*kv),Q.items()))
import pymupdf
for row in rows:
 k=row['service']
 if k!='openalex_doi' and 'status' in row:
  d=pymupdf.open(stream=(R/(k+'.response')).read_bytes(),filetype='pdf')
  (R/(k+'.txt')).write_text('\n'.join('=== PAGE '+str(i+1)+' ===\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
 if k=='openalex_doi' and 'status' in row:
  w=json.loads((R/(k+'.response')).read_text()); u='https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:'+w['id'].split('/')[-1],'per-page':200})
  rows.append(f('openalex_citing',u))
with (R/'search_log.jsonl').open('a',encoding='utf8') as o:
 for row in rows:o.write(json.dumps(row)+'\n');print(row)

