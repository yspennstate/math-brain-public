from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]; O=R/'out'; O.mkdir(exist_ok=True)
ROOT=R.parents[3]
receipts=[]
def consume(p,show=False):
    raw=p.read_bytes(); text=raw.decode('utf-8-sig')
    receipts.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
    if show: print('\nFILE',p,'\n',text)
    return text
for p in [ROOT/'BOARD.md',ROOT/'claude/B18/STREAM_NOTES.md',R.parents[1]/'STATUS.md']:
    text=consume(p)
    if p.name=='BOARD.md':
        for line in text.splitlines():
            if any(line.startswith('- '+a+' |') for a in ['A086','A094','A095','A096','A097','A011']): print(line)
for a in ['A095','A094','A097','A096','A011']:
    candidates=[p for p in (ROOT/'agents'/a/'runs').iterdir() if p.is_dir() and (p/'REPORT.md').is_file()]
    p=max(candidates,key=lambda x:x.name)
    print('LATEST',a,p,'FILES',[x.name for x in p.iterdir() if x.is_file()])
    if a=='A095':
        consume(p/'REPORT.md',True)
        consume(p/'CLAIMS.json',True)
        (O/'TARGET_PATH.txt').write_text(str(p),encoding='utf-8')
(O/'INTAKE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
