import hashlib,json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,r'~\.claude\dreaming')
try:
 import lean_check
 src=(R/'code/SideCertificates.lean').read_bytes()
 result=lean_check.check_source(src,target='A019_sign_certificates',reviewed_sha256=hashlib.sha256(src).hexdigest(),timeout=45,source_path=str(R/'code/SideCertificates.lean'),output_root=str(R/'out/lean'),use_mathlib=False)
 (R/'out/LEAN_RESULT.json').write_text(json.dumps(result,indent=2,default=str),encoding='utf-8')
 print(str(result)[:2000])
except Exception as exc:
 result={'status':'UNVERIFIED','blocker':type(exc).__name__+': '+str(exc),'scope':'core arithmetic side certificates only; full entropy proof not formalized'}
 (R/'out/LEAN_RESULT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps(result))
