import importlib.util,json,hashlib,time,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
source=root/'code/dual_core.lean'
helper=Path('lean_check.py')
sys.path.insert(0,str(helper.parent))
spec=importlib.util.spec_from_file_location('a058_lean_checker',helper)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
started=time.monotonic()
try:
    receipt=module.check_source(source.read_bytes(),target='a058_liquidation_exchange',reviewed_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),timeout=30,source_path=source,output_root=root/'out/lean',use_mathlib=False)
except (OSError,RuntimeError,ValueError,KeyError,TypeError) as exc:
    receipt={'status':'SETUP_UNVERIFIED','reason':str(exc)}
receipt['translation_scope']='Natural-number nonnegative-coefficient dual step. Clearing positive denominators gives the exact rational finite-certificate step. Does NOT certify real entropy optimality, Fourier identities, or universal FEI.'
receipt['helper_sha256']=hashlib.sha256(helper.read_bytes()).hexdigest()
receipt['elapsed_s']=time.monotonic()-started
(root/'out/LEAN.json').write_text(json.dumps(receipt,indent=2,default=str),encoding='utf-8')
print(json.dumps({'result':receipt.get('result',receipt.get('status')),'seconds':receipt['elapsed_s'],'translation_scope':receipt['translation_scope']},default=str))
