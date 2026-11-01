import json
from pathlib import Path

root=Path(__file__).resolve().parent
source=json.loads((root/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
store=json.loads((root/'READ_ONLY_STORE_RECEIPT.json').read_text(encoding='utf-8'))
summaries=[]
for row in store.get('matches',[]):
    metadata=json.loads(row.get('metadata_json') or '{}')
    summaries.append({'id':row['id'],'title':row['title'],
                      'claim_kind':metadata.get('claim_kind'),
                      'truth_status':metadata.get('truth_status'),
                      'logical_id':metadata.get('logical_id')})
source['local_checks']['owner_solved_retired']={
    'receipt':'READ_ONLY_STORE_RECEIPT.json','status':store['status'],
    'exact_nodes':summaries,
    'conclusion':'The two exact population nodes are unverified concepts; neither is a verified solved/retired certificate. This check is not an exhaustive owner-work search.'}
source['current_openness']='UNKNOWN'
(root/'SOURCE_STATUS.json').write_text(json.dumps(source,indent=2),encoding='utf-8')
claims=[json.loads(line) for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
for row in claims:
    if row['id']=='w472-C0052-001':
        row['source']['established_input']='Jiang-Newman 2210.03602 equations (25)-(27), and Hadamard factorization; primary formula verified'
    if row['id']=='w472-C0052-000':
        row['remaining_gap']='Exact primary statement now verified in SOURCE_STATUS.json; current openness remains uncertified.'
(root/'CLAIMS.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in claims),encoding='utf-8')
print(json.dumps({'exact_nodes':summaries,'current_openness':source['current_openness']},ensure_ascii=False))
