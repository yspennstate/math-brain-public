from pathlib import Path
import hashlib,json
root=Path(r'~\brain_workers\FEI100_20261011')
p=root/'agents/A067/runs/20261021T224913Z-fleet03-A067-hypercontractive-refinement'
for name in ['DERIVATION.md','CLAIMS.json','REPORT.md','out/CHECK.json','out/LEAN.json']:
    f=p/name
    if f.exists():
        print('\nFILE',f,'SHA256',hashlib.sha256(f.read_bytes()).hexdigest())
        print(f.read_text(encoding='utf-8'))
print('\nOWN CHECKER INVENTORY')
for f in (root/'agents/A088/runs/20261014T053751Z-fleet05-A088-booleanity-referee/code').iterdir():print(f.name)
print('\nLEAN WRAPPER OPTIONS')
f=Path(r'lean_check.py')
print(f.read_text(encoding='utf-8')[:7000])
