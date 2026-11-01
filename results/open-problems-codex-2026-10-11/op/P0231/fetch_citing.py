import research_fetch as f, concurrent.futures as c, json, pymupdf
Q={'tree_paper':'https://arxiv.org/pdf/2606.24793',
 'stick_paper':'https://arxiv.org/pdf/2601.19546',
 'survey_metadata':'https://api.crossref.org/works/10.1016/j.cosrev.2025.100857',
 'citing_arxiv_metadata':'https://export.arxiv.org/api/query?id_list=2606.24793,2601.19546,2302.10795,2212.13235,2108.13014'}
with c.ThreadPoolExecutor(max_workers=4) as p: results=list(p.map(lambda kv:f.fetch(*kv),Q.items()))
(f.ROOT/'citing_fetch_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for key in ['tree_paper','stick_paper']:
 try:
  doc=pymupdf.open(stream=(f.ROOT/(key+'.txt')).read_bytes(),filetype='pdf')
  text='\n'.join(f'PDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc))
  (f.ROOT/(key+'_text.txt')).write_text(text,encoding='utf8')
  print(key,'pages',len(doc)); print(text[:6500])
 except Exception as e: print(key,repr(e))
print(json.dumps(results,indent=2))
