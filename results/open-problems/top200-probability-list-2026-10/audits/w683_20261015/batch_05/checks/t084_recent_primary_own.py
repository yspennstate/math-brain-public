from pathlib import Path
from urllib.request import Request,urlopen
from hashlib import sha256
import json
for identifier,name,title,authors in [
 ('2609.26134','t084_gupta.pdf','Edges of the uniform random forest of K_n are pairwise negatively correlated for every n','Anish Gupta'),
 ('2610.00549','t084_ciceksiz_ravichandran.pdf','Negative Correlations for Forests and the q<1 Random Cluster Model','Recep Altar Ciceksiz; Mohan Ravichandran')]:
    url='https://arxiv.org/pdf/'+identifier
    with urlopen(Request(url,headers={'User-Agent':'ProbabilityAudit/1.0'}),timeout=40) as response:raw=response.read(5_000_001)
    assert len(raw)<5_000_000 and raw.startswith(b'%PDF')
    path=Path('papers')/name;path.write_bytes(raw)
    record={'url':url,'file':str(path),'sha256':sha256(raw).hexdigest(),'title':title,'authors':authors,'year':2026,'what you used it for':'Primary theorem-scope check: t=1 complete-graph forests and high-fugacity/random-cluster distinctions'}
    with Path('SOURCES.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(record)+'\n')
    print(name+' '+str(len(raw))+' '+record['sha256'])
