import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
path=ROOT/'evidence/lean_arithmetic_receipt.json'
data=path.read_bytes()
raw=data.decode('utf-16' if data.startswith((b'\xff\xfe',b'\xfe\xff')) else 'utf-8-sig').strip()
(ROOT/'evidence/lean_arithmetic_receipt.txt').write_text(raw+'\n',encoding='utf-8')
receipt={'status':'SETUP_UNVERIFIED','compiler_started':False,'lean_checked':False,'raw_output':raw,'scope':'Finite P0242 ratio arithmetic only; the stochastic lower bound was never submitted as a Lean theorem.'}
assert raw.startswith('SETUP_UNVERIFIED:')
path.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print('Lean receipt normalized from PowerShell UTF-16; no compiler started.')
