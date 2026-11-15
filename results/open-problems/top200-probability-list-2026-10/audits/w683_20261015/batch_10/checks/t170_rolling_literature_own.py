"""Bounded read-only primary-source discovery; no novelty inference from absence."""
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.parse import urlencode
from hashlib import sha256
from datetime import datetime
import xml.etree.ElementTree as ET
import json
root=Path(__file__).resolve().parents[1]
at=datetime.now().astimezone().isoformat()
queries=[('method','all:"first passage percolation" AND (all:"rolling window" OR all:"Markov chain" OR all:regeneration) AND (all:Dhar OR all:Eden OR all:anisotropy)'),('recent','all:"first passage percolation" AND (all:"Eden conjecture" OR all:anisotropy) AND submittedDate:[202607170000 TO 202610152359]')]
out=[]
for label,q in queries:
    url='https://export.arxiv.org/api/query?'+urlencode({'search_query':q,'max_results':12,'sortBy':'submittedDate','sortOrder':'descending'})
    p=root/f'papers/t170_rolling_{label}_own.xml'
    try:
        if not p.exists():
            with urlopen(Request(url,headers={'User-Agent':'ProbabilityResearchAudit/1.0'}),timeout=30) as response:
                raw=response.read(2_000_001)
            assert len(raw)<=2_000_000
            p.write_bytes(raw)
        raw=p.read_bytes(); tree=ET.fromstring(raw); ns={'a':'http://www.w3.org/2005/Atom'}
        entries=[{'title':' '.join(e.findtext('a:title','',ns).split()),'url':e.findtext('a:id','',ns),'published':e.findtext('a:published','',ns),'abstract':' '.join(e.findtext('a:summary','',ns).split())} for e in tree.findall('a:entry',ns)]
        row={'at':at,'url':url,'file':str(p.relative_to(root)),'sha256':sha256(raw).hexdigest(),'title':'Arxiv rolling-method discovery '+label,'authors':['arXiv metadata'],'year':2026,'what you used it for':'Bounded T170 D15/D14 novelty screen, not priority proof'}
        with (root/'SOURCES.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps(row)+'\n')
        out.append({'label':label,'query':q,'cap':12,'status':'fetched','entries':entries})
    except Exception as exc: out.append({'label':label,'query':q,'status':'unavailable','error':str(exc)})
receipt={'at':at,'queries':out,'prior_citation_screen':'checks/t170_d16_literature_own.json; same-day BP citation index and Kumar-Dhar primary source already checked','novelty':'unclear; no priority claim; finite metadata caps are not exhaustive','primary_shape_source':'BP1705.08143v2 introduction and Section2, previously checked; standard shape theorem hypotheses Exp(1) satisfy every finite moment and P(t=0)=0'}
(root/'checks/t170_rolling_literature_own.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
with (root/'BRAIN_USE.jsonl').open('a',encoding='utf-8') as f:
    f.write(json.dumps({'at':at,'query':['auditing Poisson graphical coupling regeneration FPP shape theorem mistakes'],'top_ids':['math_frontier_reviews_and_actual_ingestion_2026_10_15','three_kinds_of_label_defect_in_my_own_test_set_2026_08_22','fpp_ratio_is_bootstrap_shaped_mismatch_is_not_2026_08_15'],'used':[],'helped':'no','why':'Recall metadata did not supply the needed graphical coupling or regeneration lemma; no test-bank memory opened; prove the coupling directly.'})+'\n')
print(json.dumps([{'label':r['label'],'status':r['status'],'titles':[e['title'] for e in r.get('entries',[])]} for r in out]))
