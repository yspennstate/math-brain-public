import urllib.request,json,pathlib,pymupdf
m=json.loads(pathlib.Path('kanda_metadata.json').read_text());u=m['locations'][0]['pdf_url']
r={'date':'2026-10-12','service_query':'kanda_original_pdf','url':u}
try:
 data=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'ResearchMath/1.0'}),timeout=35).read();pathlib.Path('kanda_original.pdf').write_bytes(data)
 d=pymupdf.open(stream=data,filetype='pdf');s='\n'.join(f'PDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(d));pathlib.Path('kanda_original.txt').write_text(s,encoding='utf8');r.update(status='ok',file='kanda_original.pdf');print(s[:12500])
except Exception as e:r['status']=str(e);print(r)
p=pathlib.Path('search_log.json');old=json.loads(p.read_text());p.write_text(json.dumps(old+[r],indent=2))
