from pathlib import Path
import json

root=Path(__file__).resolve().parent
path=root/'CLAIMS.jsonl'
raw=path.read_text(encoding='utf-8')
backup=root/'CLAIMS.before_escape_repair.jsonl'
if not backup.exists():backup.write_text(raw,encoding='utf-8')

def repair(line):
    out=[];i=0;in_string=False;fixed=0
    while i<len(line):
        c=line[i]
        if c=='"':
            in_string=not in_string;out.append(c);i+=1;continue
        if in_string and c=='\\':
            nxt=line[i+1] if i+1<len(line) else ''
            if nxt and nxt in '"\\/bfnrt':
                out.extend([c,nxt]);i+=2;continue
            if nxt=='u' and i+5<len(line) and all(x in '0123456789abcdefABCDEF' for x in line[i+2:i+6]):
                out.append(line[i:i+6]);i+=6;continue
            out.append('\\\\');i+=1;fixed+=1;continue
        out.append(c);i+=1
    return ''.join(out),fixed

rows=[];fixes=0
for n,line in enumerate(raw.splitlines(),1):
    if not line.strip():continue
    try:row=json.loads(line)
    except json.JSONDecodeError:
        line,count=repair(line);row=json.loads(line);fixes+=count
    for field in ['id','statement','assumptions','source','proof_or_counterexample','independent_reviewer','remaining_gap','status']:
        if field not in row:raise ValueError((n,field))
    rows.append(row)
if len({r['id'] for r in rows})!=len(rows):raise ValueError('Duplicate claim id')
path.write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in rows),encoding='utf-8')
receipt={'rows_preserved':len(rows),'invalid_backslash_escapes_repaired':fixes,'status':'PASS_JSON_ROW_STRUCTURE_ONLY','mathematical_audit':False}
(root/'CLAIM_SERIALIZATION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
with (root/'STATUS.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-10 STUCK: two prepare runs found invalid mathematical backslash escapes in hand-written claim JSON. Switched to JSON-encoded rows with a character-preserving repair; all original rows retained in CLAIMS.before_escape_repair.jsonl. This is serialization validation, not mathematical review.\n')
print(json.dumps(receipt),flush=True)
