"""Run the named helper with all generated files restricted to this worker."""
import sys
sys.dont_write_bytecode=True
import json
import os
from pathlib import Path
ROOT=Path(__file__).resolve().parent
os.environ['LEAN_CHECK_DIR']=str(ROOT/'lean_receipts')
sys.path.insert(0,'~/.claude/dreaming')
import lean_check

for filename,target in [('c0033_key.lean','w340_dpp_atom_product'),('p0441_key.lean','w340_delayedoff_wait_identity')]:
    source=ROOT/filename
    raw=source.read_bytes()
    try:
        receipt=lean_check.check_source(raw,source_path=source,target=target,reviewed_sha256=lean_check.digest(raw),timeout=40,output_root=ROOT/'lean_receipts')
    except Exception as exc:
        receipt={'result':{'status':'SETUP_OR_RUNTIME_UNAVAILABLE'},'error':type(exc).__name__+': '+str(exc),'source_path':str(source),'target':target}
    (ROOT/(filename+'.receipt.json')).write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
    print(filename,json.dumps(receipt,ensure_ascii=False),flush=True)
