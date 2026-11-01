from modular_search import fetch,R
import concurrent.futures,json
urls={
 'orientation_paper':'https://arxiv.org/pdf/2209.13175',
 'permutation_paper':'https://arxiv.org/pdf/1008.1736',
 'substitution_paper':'https://arxiv.org/pdf/1711.06511',
 'prime_paper':'https://arxiv.org/pdf/2609.08057',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:log=list(pool.map(fetch,urls.items()))
(R/'modular_pdf_log.json').write_text(json.dumps(log,indent=2),encoding='utf8')
for entry in log:
 print(json.dumps(entry));name=entry['name'];p=R/(name+'.raw')
 if p.exists():
  import pymupdf
  doc=pymupdf.open(stream=p.read_bytes(),filetype='pdf')
  pages=[page.get_text() for page in doc]
  (R/(name+'.txt')).write_text('\n'.join('--- PDF PAGE '+str(i+1)+' ---\n'+s for i,s in enumerate(pages)),encoding='utf8')
  for i,s in enumerate(pages):
   if any(t in s.lower() for t in ['gallai','exactly two','strong module','simple permutation','strong interval']):print(name,'PAGE',i+1,s[:10000])
