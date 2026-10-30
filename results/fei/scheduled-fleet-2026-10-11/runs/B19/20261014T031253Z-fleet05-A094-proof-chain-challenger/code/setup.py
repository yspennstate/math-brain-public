from pathlib import Path
import hashlib,json
run=Path(__file__).resolve().parents[1]
src=run.parents[1]/'runs/20261014T001244Z-fleet05-A094-proof-chain-challenger/code/check.py'
dst=run/'code/arithmetic.py'
dst.write_bytes(src.read_bytes())
(run/'out/HELPER_PROVENANCE.json').write_text(json.dumps({'source':str(src),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'scope':'Own earlier exact Fraction/prime-log arithmetic only; no author checker imported; mathematical checker and rational-log enclosure rebuilt in current check.py'},indent=2)+'\n',encoding='utf-8')
