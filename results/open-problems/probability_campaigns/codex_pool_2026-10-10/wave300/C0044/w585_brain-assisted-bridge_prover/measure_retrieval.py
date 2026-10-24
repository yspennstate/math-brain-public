"""Scoped paired replay with one draft bridge card; no live-store mutation."""
import json
import os
import sys
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
os.environ['MATH_BRAIN_SEMANTIC']='0'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
sys.dont_write_bytecode=True
sys.path.insert(0,'~/math-brain-build/src')
from math_brain.models import GraphNode, NodeKind
from math_brain.retrieval import retrieve

queries=[
    'directional transience zero one law environment seen particle uniform integrability',
    'RWRE quenched harmonic posterior martingale missing bridge',
    'incoming density Cesaro probability zero one strict ellipticity',
]
raw=json.loads((ROOT/'brain_selected_nodes.json').read_text(encoding='utf-8'))
nodes=[GraphNode(id=r['id'],kind=NodeKind(r['kind']),title=r['title'],body=r['body'],metadata=json.loads(r['metadata_json']),created_at=r['created_at']) for r in raw]
bundle=json.loads((ROOT/'bundle_001.json').read_text(encoding='utf-8'))
entry=next(e for e in bundle['entries'] if e['key']=='criterion')
extra=GraphNode(id='draft_w585_c0044_criterion',kind=NodeKind.CLAIM,title=entry['title'],body=entry['statement'],metadata={'claim_kind':'concept','truth_status':'unverified','logical_id':'math:'+entry['namespace']+':'+entry['logical_name']})
def usable(n):
    s=(n.title+' '+n.body).lower()
    return ('zero-one' in s or 'zero one' in s) and 'uniform' in s and 'integrab' in s and ('density' in s or 'densities' in s) and ('extra assumption' in s or 'additional assumption' in s)
start=time.monotonic(); records=[]
for arm,cards in [('before',nodes),('after_one_draft_card',nodes+[extra])]:
    for query in queries:
        result=retrieve(query,nodes=cards,edges=[],limit=3,min_support_score=0.0,min_margin=0.0)
        records.append({'arm':arm,'query':query,'usable_bridge_in_top3':any(usable(h.node) for h in result.hits),
                        'hits':[{'id':h.node.id,'title':h.node.title,'score':h.total_score} for h in result.hits]})
receipt={'command':'python -X utf8 ~/brain_workers/w585/measure_retrieval.py','selected_live_nodes':len(nodes),
         'added_draft_cards':1,'semantic_channel':'disabled in both arms; no model load','graph_edges_used':0,
         'metric':'top3 contains a zero-one density bridge explicitly declaring the extra UI assumption',
         'before_hits':sum(r['usable_bridge_in_top3'] for r in records if r['arm']=='before'),
         'after_hits':sum(r['usable_bridge_in_top3'] for r in records if r['arm']!='before'),
         'queries':len(queries),'seconds':time.monotonic()-start,'records':records,
         'limitation':'Task-scoped 14-card lexical replay, not whole-store recall or held-out evaluation; author-only draft after treatment.'}
(ROOT/'RETRIEVAL_MEASUREMENT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
