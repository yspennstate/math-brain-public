import requests,pathlib,pymupdf,concurrent.futures
ids=['math/0110296','1102.2950']
def run(i):
 name=i.replace('/','_');r=requests.get('https://arxiv.org/pdf/'+i,timeout=35);r.raise_for_status();pathlib.Path('second_'+name+'.pdf').write_bytes(r.content);d=pymupdf.open(stream=r.content,filetype='pdf');t='\n\n'.join('PDF PAGE '+str(j+1)+'\n'+p.get_text() for j,p in enumerate(d));pathlib.Path('second_'+name+'.txt').write_text(t,encoding='utf8');
 with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n- 2026-10-12 document fetch '+r.url+' HTTP '+str(r.status_code)+'; second_'+name+'.pdf/text\n')
 return i,t[:1200]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
 for r in ex.map(run,ids):print(r)
