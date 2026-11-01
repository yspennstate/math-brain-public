from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];BASE=R.parents[3]
(R/'out').mkdir(exist_ok=True)
receipts=[]
paths=[BASE/'BOARD.md',BASE/'claude/B06/STREAM_NOTES.md',R.parents[1]/'STATUS.md',BASE/'agents/A029/LEARNED.md',BASE/'agents/A056/LEARNED.md']
for p in paths:
    s=p.read_text(encoding='utf-8');receipts.append(dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
    if p.name=='BOARD.md':
        lines=[x for x in s.splitlines() if any(x.startswith('- '+a+' |') for a in ('A028','A029','A056','A094','A096','A097'))]
        print('\n'.join(x[:600] for x in lines))
    elif p.parent.name in ('A029','A056'): print(str(p)+'\n'+'\n'.join(s.splitlines()[-12:])[:6500])
state=Path('~/.claude/compute/compute_state.json')
if state.exists():
    x=json.loads(state.read_text(encoding='utf-8-sig'));snap={k:x.get(k) for k in ('ts','status','mode','mem_avail_mb','commit_used_pct','disk_free_gb')}
    (R/'out/compute_snapshot.json').write_text(json.dumps(snap,indent=2)+'\n',encoding='utf-8',newline='');print(json.dumps(snap))
(R/'out/context_receipts.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8',newline='')
