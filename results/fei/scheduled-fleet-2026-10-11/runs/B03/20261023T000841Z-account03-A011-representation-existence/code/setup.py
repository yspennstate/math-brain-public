from pathlib import Path
import json,hashlib,shutil
R=Path(__file__).resolve().parents[1];A=R.parents[1];(R/'out').mkdir(exist_ok=True)
old=A/'runs/20261014T074949Z-account05-A011-representation-existence/code/shared.py'
raw=old.read_bytes();(R/'code/shared.py').write_bytes(raw)
(R/'out/HELPER_PROVENANCE.json').write_text(json.dumps({'source':str(old),'sha256':hashlib.sha256(raw).hexdigest()},indent=2),encoding='utf-8')
paths=[Path('~/AGENTS.md'),Path('~/brain_workers/FEI100_20261011/BOARD.md'),Path('~/brain_workers/FEI100_20261011/claude/B03/STREAM_NOTES.md'),Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),A/'runs/20261021T182829Z-account03-A011-representation-existence/DERIVATION.md',A/'runs/20261021T182829Z-account03-A011-representation-existence/CLAIMS.json',A/'runs/20261014T074949Z-account05-A011-representation-existence/GENERAL_ENVELOPE.md']
receipts=[]
for p in paths:
 data=p.read_bytes();receipts.append({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
# Remove an abandoned overstrong intermediate inequality before any theorem is claimed.
f=R/'DERIVATION.md';txt=f.read_text(encoding='utf-8');start=txt.index('    K I(F)-L_a >= (C0+15/4)');end=txt.index('    K I(F)-L_a >= C0 I_g',start)
txt=txt[:start]+'''    K I(F)-L_a >= C0 I_g+K(C+J)>0.                      (11)

Indeed K(3/4)-2C0=C0+45/4 and15B_root<=45I_g/4 for a>=1, because B_root/I_g<=2^-q[1+q/a]<=(q+1)/2^q<=3/4. Thus the source entropy and complete source divergence are both retained, with the conservative final margin

'''+txt[end:];f.write_text(txt,encoding='utf-8')
print(json.dumps({'status':'SETUP_SAVED','source_files':len(receipts)}))
