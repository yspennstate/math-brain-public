from pathlib import Path
from urllib.request import Request,urlopen
from urllib.parse import urlencode
from hashlib import sha256
from datetime import datetime
import xml.etree.ElementTree as ET
import json
root=Path(__file__).resolve().parent.parent;at=datetime.now().astimezone().isoformat()
query='all:"random-cluster" AND (all:"negative correlation" OR all:Rayleigh) AND submittedDate:[202607170000 TO 202610152359]'
targets=[('https://export.arxiv.org/api/query?'+urlencode({'search_query':query,'max_results':12,'sortBy':'submittedDate','sortOrder':'descending'}),'t084_rc_recent_own.xml','Recent random-cluster negative-correlation metadata'),('https://api.semanticscholar.org/graph/v1/paper/ARXIV:2610.00549/citations?fields=title,year,externalIds&limit=25','t084_rc_citing_own.json','Papers citing closest Ciceksiz-Ravichandran source')]
records=[]
for url,name,title in targets:
    p=root/'papers'/name
    record={'url':url,'file':str(p.relative_to(root)),'title':title,'authors':['arXiv or Semantic Scholar metadata'],'year':2026,'what you used it for':'C021-C023 prior-work audit; bounded screen cannot establish priority','at':at}
    try:
        if p.exists():raw=p.read_bytes()
        else:
            with urlopen(Request(url,headers={'User-Agent':'ProbabilityAudit/1.0'}),timeout=25) as r:raw=r.read(2000001)
            assert len(raw)<=2000000
            p.write_bytes(raw)
        record.update(sha256=sha256(raw).hexdigest(),status='fetched')
        if name.endswith('.xml'):
            ns={'a':'http://www.w3.org/2005/Atom'}
            record['entries']=[{'title':e.findtext('a:title',default='',namespaces=ns).strip(),'id':e.findtext('a:id',default='',namespaces=ns),'published':e.findtext('a:published',default='',namespaces=ns)} for e in ET.fromstring(raw).findall('a:entry',ns)]
        else:record['citations']=json.loads(raw).get('data',[])
    except Exception as e:record.update(status='unavailable',error=type(e).__name__+': '+str(e)[:180])
    records.append(record)
    with (root/'SOURCES.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(record)+'\n')
paper=root/'papers/2610.00549v1.pdf'
records.append({'url':'https://arxiv.org/pdf/2610.00549v1','file':str(paper.relative_to(root)),'sha256':sha256(paper.read_bytes()).hexdigest(),'title':'Ciceksiz-Ravichandran primary source already fetched','used_locators':['Proposition3.4 printedp11','Lemma5.1 printedp27','Proposition5.7 printedpp32-33'],'scope':'Existing identity and injection architecture; source commonweight>=1, adjacent closingweight>=1, and disjoint cross>=2 plus outside incident>=1 restrictions.'})
(root/'checks/t084_rc_literature_own.json').write_text(json.dumps({'at':at,'priority':'unclear; no global novelty assertion','records':records},indent=2)+'\n',encoding='utf8')
slugs=['fk_below_one_is_not_monotone_in_the_edge_vector_and_the_upset_maxflow_2026_09_13','t084_kmn_forests_negatively_correlated_every_fugacity_2026_10_15','project_mistake_graph_catalog_2026_07_11']
with (root/'BRAIN_USE.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps({'at':at,'query':['random cluster complete graph q less than one negative edge correlation mistakes'],'top_ids':slugs,'used':slugs[:1],'helped':'partly','why':'The q<1 vector-parameter warning is relevant: these proofs must reapply exact weighted injection inequalities, not assert stochastic monotonicity. Other top hits are forest context or irrelevant.'})+'\n')
with (root/'ROUTES.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps({'at':at,'kind':'audit','target':'T084 target3 RC on Kn belowweight1','route':'Direct bridge deletion identity, exact weighted same/different-component injections, independent full-subset union-find and Fraction evaluator','status':'mathematical checks PASS; prior-work screen and final verdict recording'})+'\n')
print(json.dumps([{'file':r['file'],'status':r.get('status','primary source'),'entries':r.get('entries',[]),'citations':r.get('citations',[])} for r in records]))
