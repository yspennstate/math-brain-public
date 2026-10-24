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
item=json.loads((ROOT/'github.raw').read_text(encoding='utf8'))['items'][0]
repo=item['full_name']; branch=item['default_branch']
data=fetch('github_tree','https://api.github.com/repos/'+repo+'/git/trees/'+branch+'?recursive=1')
if data:
    tree=json.loads(data)
    for entry in tree.get('tree',[]):
        path=entry['path']
        if entry['type']=='blob' and ('potts' in path.lower() or path.lower()=='readme.md'):
            print('LEAD FILE',path,flush=True)
            raw=fetch('github_'+path.replace('/','_').replace('.','_'),'https://raw.githubusercontent.com/'+repo+'/'+branch+'/'+path)
            if raw and len(raw)<100000: print(raw.decode('utf8','replace')[:14000],flush=True)
