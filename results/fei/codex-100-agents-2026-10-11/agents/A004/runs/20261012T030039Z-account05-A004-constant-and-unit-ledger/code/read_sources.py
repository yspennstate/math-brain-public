from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
TEAM=Path(r'~\brain_workers\FEI100_20261011')
CANON=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUPP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
def main():
    paths=[TEAM/'BOARD.md',TEAM/'claude/B01/STREAM_NOTES.md',TEAM/'claude/B05/STREAM_NOTES.md',TEAM/'claude/B20/STREAM_NOTES.md',CANON/'EXECUTION_PROTOCOL.json',SUPP/'sources/ERASURE_REDUCTION.md',SUPP/'sources/ERASURE_RIGIDITY.md']
    for packet in ['A002','A003','A024','A038','A086','A094']:
        reports=sorted((TEAM/'agents'/packet/'runs').glob('*/REPORT.md'))
        if reports:paths.append(reports[-1])
    paths+=list((TEAM/'claude/B01/runs').glob('*/CLAIMS.json'))
    paths+=list((TEAM/'claude/B20/runs').glob('*/CLAIMS.json'))
    folder=ROOT/'out/sources';folder.mkdir(exist_ok=True)
    manifest=[]
    for j,p in enumerate(paths):
        if not p.exists():print('MISSING '+str(p));continue
        data=p.read_bytes();text=data.decode('utf-8-sig',errors='replace')
        target=folder/(f'{j:02d}_'+p.name);target.write_bytes(data)
        manifest.append({'source':str(p),'snapshot':str(target.relative_to(ROOT)),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
        print('\nFILE '+str(p))
        if p.name=='EXECUTION_PROTOCOL.json':print(json.dumps(json.loads(text)['required_per_run'],indent=2))
        elif p.name=='BOARD.md':print('\n'.join(text.splitlines()[:18]))
        elif p.name=='CLAIMS.json':
            d=json.loads(text)
            print(json.dumps(d,ensure_ascii=False)[:12500])
        elif p.parent.name=='B05':print(text[:9000])
        elif p.name=='REPORT.md':
            lines=text.splitlines();hits=set()
            for i,line in enumerate(lines):
                if any(s.lower() in line.lower() for s in ['A004','nonempty','DTC','L_i','L =','erasure','normaliz','split','alias']):
                    hits.update(range(max(0,i-1),min(len(lines),i+3)))
            print('\n'.join(f'{i+1}: {lines[i]}' for i in sorted(hits))[:12000])
        else: print(text[:17000])
    (ROOT/'out/source_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':main()
