import json, pathlib

root=pathlib.Path(__file__).resolve().parent
receipt=json.loads((root/'PEER_REVIEW_RECEIPT.json').read_text(encoding='utf-8'))
rows=[]
for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines():
    if not line.strip(): continue
    row=json.loads(line)
    if row['claim_id'] in receipt['claims']:
        row['independent_reviewer']='w529 KEEP_SCOPED_AUXILIARIES; w530 referee pending'
        row['status']='independently checked proof'
        row['review_state']='One independent mathematical KEEP for the stated auxiliary; final referee review pending; account-distinctness UNKNOWN'
        row['independent_reviews']=[{'reviewer':'w529','verdict':'KEEP_SCOPED_AUXILIARIES','verdict_file':receipt['verdict_file'],'message_id':receipt['message_id']}]
    rows.append(row)
(root/'CLAIMS.jsonl').write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in rows)+'\n',encoding='utf-8')
life=json.loads((root/'BUNDLE_LIFECYCLE.json').read_text(encoding='utf-8'))
life['adversary_review']=receipt
life['referee_submission']={'message_id':receipt['referee_message_id'],'submitted':True,'verdict':'PENDING'}
life['reviewed_definition']='All required final mathematical reviews completed; six auxiliary claims already have a w529 KEEP.'
(root/'BUNDLE_LIFECYCLE.json').write_text(json.dumps(life,indent=2)+'\n',encoding='utf-8')
source=json.loads((root/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source['independent_review']='w529 KEEP for L1-L6; w530 final referee review PENDING; G remains unproved'
(root/'SOURCE_STATUS.json').write_text(json.dumps(source,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'independently_kept_auxiliaries':len(receipt['claims']),'final_referee':'PENDING','G':'UNPROVED'}))
