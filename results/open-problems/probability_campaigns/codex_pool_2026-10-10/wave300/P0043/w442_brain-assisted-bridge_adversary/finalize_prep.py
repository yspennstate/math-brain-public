import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
correction=json.loads((ROOT/'SOURCE_CORRECTION.json').read_text(encoding='utf-8'))
claims=[json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
if not any(row['claim_id']==correction['claim_id'] for row in claims):
    claims.append(correction)
(ROOT/'CLAIMS.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in claims),encoding='utf-8')
bundle=json.loads((ROOT/'DRAFT_BUNDLE.json').read_text(encoding='utf-8'))
gap=next(row for row in bundle['entries'] if row['key']=='exploration-gap')
gap['statement']='Source comparison, still draft material: arXiv:2304.12110v3, Definition 4 and Lemma 7, requires finite E and a nonanticipating exploration with deterministic first edge. For every positive-probability complete transcript, the same q bounds conditional next-edge opening after every prefix. Marginals do not suffice. An infinite-cluster application needs those history-uniform bounds, a percolating comparison object and a justified limit argument. The unverified harvested fragment omits the global finite-graph and exploration definitions.'
extra={'key':'clean-exploration-hypotheses','namespace':'probability.percolation.audit',
       'logical_name':'finite-exploration-domination-full-hypotheses-draft-w442','kind':'concept',
       'title':'Finite exploration domination with complete hypotheses (draft correction)',
       'statement':'Draft source correction awaiting referee w443: '+correction['statement'],
       'proof_text':None,'assumptions':correction['assumptions'],
       'domain':'Bernoulli bond percolation / source hypothesis audit',
       'source':{'source_id':'owner:P0043:w442:C004-source-audit',
                 'url':'~/brain_workers/w442/BRIDGE_COMPARISON.md',
                 'revision':'draft-pending-independent-referee-2026-10-10',
                 'license':'owner-own-work (campaign source correction; primary source attributed)',
                 'excerpt':None}}
if not any(row['key']==extra['key'] for row in bundle['entries']):
    bundle['entries'].append(extra)
relation={'from_key':extra['key'],'to_existing_logical':correction['source']['stored_logical_id'],
          'kind':'cites','rationale':'Primary Definition 4 supplies finite E and nonanticipating exploration with deterministic first edge. Lemma 7 supplies the history-uniform conditional q bound. These global definitions are absent from the standalone stored fragment.'}
if not any(row['from_key']==extra['key'] for row in bundle['relations']):
    bundle['relations'].append(relation)
(ROOT/'DRAFT_BUNDLE.json').write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
by_key={row['key']:row for row in bundle['entries']}
card=json.loads((ROOT/'BRIDGE_CARD.json').read_text(encoding='utf-8'))['hits'][0]
edges=[]
for row in bundle['relations']:
    target=by_key[row['to_key']]['statement'] if 'to_key' in row else card['body']
    edges.append({**row,'from_quote':by_key[row['from_key']]['statement'],'to_quote':target,
                  'status':'draft','independent_reviewer':'w443 (pending)'})
(ROOT/'EDGES.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in edges),encoding='utf-8')
source=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
if not any(row.get('url')==correction['source']['url'] for row in source['primary_sources']):
    source['primary_sources'].append({'url':correction['source']['url'],'locator':correction['source']['locator'],
                                    'checked':'finite graph and nonanticipating exploration definitions plus all conditional quantifiers checked in primary source; C004 still awaits referee',
                                    'mathematical_proof_receipt':False})
(ROOT/'SOURCE_STATUS.json').write_text(json.dumps(source,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
test=ROOT/'validate_delivery.py'
content=test.read_text(encoding='utf-8').replace('assert len(claims)==3 and','assert len(claims)==4 and')
test.write_text(content,encoding='utf-8')
print(json.dumps({'claims':len(claims),'draft_entries':len(bundle['entries']),'draft_relations':len(bundle['relations'])}))
