from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
old=R.parent/'20261026T230945Z-fleet04-A084-continuum-parameters'
target=old/'out/FORMAL.json'
receipts=json.loads((old/'out/RECEIPTS.json').read_text(encoding='utf-8'))['artifacts']
expected=next(x['sha256'] for x in receipts if x['path'].replace('\\','/')=='out/FORMAL.json')
current=target.read_bytes()
if hashlib.sha256(current).hexdigest()!=expected:
 (R/'out/MISDIRECTED_FORMAL.json').write_bytes(current)
 original={'command':['python','-X','utf8','lean_check.py','--file',str(old/'code/row_transfer.lean'),'--target','A084_row_transfer','--reviewed-sha256','04e995a760656dadb57479b06d6270be1cf0f97c743d196484854201671a1af5'],'exit_code':2,'stdout':'SETUP_UNVERIFIED: Compute admission held (hung window or under 5500 MB free); no new compiler process\n','stderr':'','runtime_seconds':0.5241054000216536,'scope':'algebraic final transfer l<=k*b,b<=d,k>=0 implies l<=k*d; entropy monotonicity/derivatives are NOT formalized'}
 raw0=json.dumps(original,indent=2).encode('utf-8')
 candidates=[raw0,raw0.replace(b'\n',b'\r\n')]
 candidates += [x+b'\n' for x in candidates]+[x+b'\r\n' for x in candidates]
 raw=next((x for x in candidates if hashlib.sha256(x).hexdigest()==expected),None)
 assert raw is not None, 'Do not restore bytes unless original receipt verifies them'
 target.write_bytes(raw)
assert hashlib.sha256(target.read_bytes()).hexdigest()==expected
(R/'out/PRIOR_RECEIPT_RESTORED.json').write_text(json.dumps({'status':'BYTE_EXACT_PRIOR_RECEIPT_VERIFIED','sha256':expected,'misdirected_attempt_retained':'out/MISDIRECTED_FORMAL.json'},indent=2),encoding='utf-8')
helper=(old/'code/check.py').read_bytes();(R/'code/exact_arithmetic.py').write_bytes(helper)
print(json.dumps({'prior_receipt':'RESTORED_AND_VERIFIED','self_contained_arithmetic_sha256':hashlib.sha256(helper).hexdigest()}))
