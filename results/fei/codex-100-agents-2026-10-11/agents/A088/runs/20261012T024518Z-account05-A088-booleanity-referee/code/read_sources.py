from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
TEAM=Path(r'~\brain_workers\FEI100_20261011')
REPORT=Path(r'~\mop_fei100\reports\fei-2026-10-11')
files=[TEAM/'BOARD.md',TEAM/'claude/B18/STREAM_NOTES.md',ROOT.parents[1]/'STATUS.md',REPORT/'EXECUTION_PROTOCOL.json',REPORT/'CLAIM_REGISTRY.json',REPORT/'OBSTRUCTION_REGISTRY.json',REPORT/'STREAM_NEXT_ACTIONS.json']
for i in [39,66,67,70,97]:
    d=TEAM/'agents'/('A%03d'%i)
    files+=list(d.glob('STATUS.md'))
    files+=[p for p in (d/'runs').rglob('*') if p.is_file() and p.suffix in ['.md','.json','.tex','.py'] and 'big' not in p.parts]
files += list((TEAM/'claude/B14').glob('STREAM_NOTES.md'))+list((TEAM/'claude/B08').glob('STREAM_NOTES.md'))
rows=[]
for p in files:
    raw=p.read_bytes()
    try: s=raw.decode('utf-8-sig');enc='utf-8-sig'
    except UnicodeDecodeError:s=raw.decode('cp1252');enc='cp1252'
    rows.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':enc,'lines':len(s.splitlines())})
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out/SOURCE_MANIFEST.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print(json.dumps({'loaded_files':len(rows),'scope':'Proof consultation is restricted to the locators in REPORT.md; hashes pin loaded bytes, not blanket acceptance.'}))
