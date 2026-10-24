from pathlib import Path
import urllib.request,json
ROOT=Path(__file__).resolve().parent
def fetch(name,url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'ProbabilityResearch/1.0'}),timeout=35) as r: data=r.read(); status=r.status
        (ROOT/(name+'.raw')).write_bytes(data)
        result={'date':'2026-10-12','name':name,'url':url,'status':status,'bytes':len(data)}
    except Exception as e:
        result={'date':'2026-10-12','name':name,'url':url,'error':str(e)}; data=None
    with (ROOT/'search_log.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(result)+'\n')
    print(json.dumps(result),flush=True)
    return data
commit='fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb'
data=fetch('openai_tree','https://api.github.com/repos/openai/math/git/trees/'+commit+'?recursive=1')
if data:
    tree=json.loads(data)
    print('TREE truncated:',tree.get('truncated'),flush=True)
    for entry in tree.get('tree',[]):
        path=entry['path']
        if entry['type']=='blob' and 'Potts' in path and path.endswith(('.tex','.pdf','.md')):
            print('FILE',path,flush=True)
            # Retrieve manuscript and README; source subfiles listed but not all duplicated.
            if path.endswith(('.pdf','.md')) or path.rsplit('/',1)[-1] in ['main.tex','paper.tex']:
                fetch('openai_'+path.replace('/','_').replace('.','_'),'https://raw.githubusercontent.com/openai/math/'+commit+'/'+urllib.parse.quote(path))
for dirname in ['The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026','A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026']:
    directory='preprints/'+dirname
    data=fetch('openai_contents_'+dirname,'https://api.github.com/repos/openai/math/contents/'+directory+'?ref='+commit)
    if data:
        for entry in json.loads(data):
            if entry['type']=='file' and entry['name'].endswith(('.pdf','.tex','.md')):
                fetch('openai_direct_'+dirname+'_'+entry['name'].replace('.','_'),entry['download_url'])
import pymupdf
for p in ROOT.glob('openai_*_pdf.raw'):
    doc=pymupdf.open(p)
    p.with_suffix('.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+page.get_text() for i,page in enumerate(doc)),encoding='utf8')
