import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
def save(pid, slug, title, statement, proof, assumptions, limitation, label='proof', kind='lemma'):
    cards=json.loads((ROOT/'cards.json').read_text(encoding='utf-8'))
    targets=[c for c in cards if c['problem_id']==pid and c['kind']=='problem']
    assert len(targets)==1, (pid,len(targets))
    target=targets[0]
    rows=[json.loads(line) for line in (ROOT/'results.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
    previous=next((row for row in rows if row.get('slug')==slug),None)
    folder=ROOT/'proofs'
    folder.mkdir(exist_ok=True)
    file=folder/(slug+'.md')
    file.write_text(f'# {pid}: {title}\n\nLabel: {label}; author checked only. Independent audit: PENDING w347.\n\n{statement}\n\nAssumptions: '+ '; '.join(assumptions)+f'\n\n{proof}\n\nLimits: {limitation}\n\nExisting card: {target["logical_id"]}\nSource snapshot: {target["evidence_path"]}:{target["evidence_line"]}\n',encoding='utf-8')
    row={'row_id':previous['row_id'] if previous else f'S1.w345.{len(rows)+1:03d}','problem_id':pid,'slug':slug,'label':label,'kind':kind,'title':title,'statement':statement,'proof_text':proof if kind in ('lemma','theorem') else None,'assumptions':assumptions,'limitations':limitation,'proof_path':str(file).replace('\\','/'),'to_existing_logical':target['logical_id'],'target_key':target.get('draft_target_key'),'target_quote':target['statement'],'source_path':target['evidence_path'],'source_line':target['evidence_line'],'audit_status':'PENDING_W347'}
    if previous:
        rows=[row if old.get('slug')==slug else old for old in rows]
        (ROOT/'results.jsonl').write_text(''.join(json.dumps(item,ensure_ascii=False)+'\n' for item in rows),encoding='utf-8')
    else:
        with (ROOT/'results.jsonl').open('a',encoding='utf-8') as handle:
            handle.write(json.dumps(row,ensure_ascii=False)+'\n')
    print(row['row_id'],pid,slug)
