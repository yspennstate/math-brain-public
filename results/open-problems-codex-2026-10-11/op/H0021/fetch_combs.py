import requests,pathlib,json,pymupdf
u='https://arxiv.org/pdf/1405.6560';r=requests.get(u,timeout=40);pathlib.Path('montgomery_combs.pdf').write_bytes(r.content)
a=json.loads(pathlib.Path('second_search_log.json').read_text(encoding='utf8'));a.append(dict(date='2026-10-12',service='arxiv_montgomery_combs_pdf',url=u,status=r.status_code,bytes=len(r.content)));pathlib.Path('second_search_log.json').write_text(json.dumps(a,indent=2),encoding='utf8')
d=pymupdf.open(stream=r.content,filetype='pdf');s='\n'.join(f'--- PAGE {i+1} ---\n'+x.get_text().replace('\x00','') for i,x in enumerate(d));pathlib.Path('montgomery_combs.txt').write_text(s,encoding='utf8');print('\n'.join(s.splitlines()[:160]))
