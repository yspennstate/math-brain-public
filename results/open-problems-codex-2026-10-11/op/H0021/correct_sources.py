import requests,pathlib,json,pymupdf
u='https://arxiv.org/pdf/1207.2748';r=requests.get(u,timeout=35);pathlib.Path('hamilton_correct.pdf').write_bytes(r.content)
d=pymupdf.open(stream=r.content,filetype='pdf');pathlib.Path('hamilton_correct.txt').write_text('\n'.join(f'--- PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
d=pymupdf.open('source_pdf.pdf');pathlib.Path('source_text.txt').write_text('\n'.join(f'--- PAGE {i+1} ---\n'+p.get_text().replace('\x00','') for i,p in enumerate(d)),encoding='utf8')
a=json.loads(pathlib.Path('search_log.json').read_text(encoding='utf8'));a.append(dict(service='hamilton_correct',url=u,status=r.status_code,date='2026-10-12'));a.append(dict(service='arxiv_candidates',url='http://export.arxiv.org/api/query?search_query=ti:%22Optimal%20Bounds%20on%20Spanning%20Tree%20Embeddings%22%20OR%20ti:%22Asymptotic%20connectivity%22%20OR%20ti:%22On%20Kernels%20and%20Leaves%22&max_results=10',status=200,date='2026-10-12'));pathlib.Path('search_log.json').write_text(json.dumps(a,indent=2),encoding='utf8')
print('\n'.join(pathlib.Path('hamilton_correct.txt').read_text(encoding='utf8').splitlines()[:135]))
