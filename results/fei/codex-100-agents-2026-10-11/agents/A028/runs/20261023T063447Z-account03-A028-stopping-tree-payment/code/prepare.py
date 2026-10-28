from pathlib import Path
import shutil,json,hashlib
R=Path(__file__).resolve().parents[1];OLD=R.parent/'20261023T023055Z-account03-A028-stopping-tree-payment'
for src,dst in [('check.py','base.py'),('exact_helper.py','exact_helper.py')]:shutil.copyfile(OLD/'code'/src,R/'code'/dst)
paths=[Path('BOARD.md'),Path('claude/B06/STREAM_NOTES.md'),OLD/'REPORT.md',OLD/'out/DERIVATION.md',OLD/'CLAIMS.json',Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
receipt=[]
for p in paths:
    text=p.read_text(encoding='utf-8')
    receipt.append(dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
    if p.name=='BOARD.md':
        selected=[s for s in text.splitlines() if any(s.startswith('- '+a+' |') for a in ['A028','A029','A056','A096','A097'])]
        (R/'out/board_selected.txt').write_text('\n'.join(selected)+'\n',encoding='utf-8',newline='')
        print('\n'.join(s[:450] for s in selected))
compute=Path('~/.claude/compute/compute_state.json')
if compute.exists():
    x=json.loads(compute.read_text(encoding='utf-8-sig'))
    small={k:x.get(k) for k in ('ts','status','mode','cpu_pct','mem_avail_mb','commit_used_pct','disk_free_gb','hung_windows')}
    (R/'out/compute_snapshot.json').write_text(json.dumps(small,indent=2)+'\n',encoding='utf-8',newline='')
    print(json.dumps(small))
(R/'out/context_receipts.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='')
print('prior helpers copied; sources pinned')
