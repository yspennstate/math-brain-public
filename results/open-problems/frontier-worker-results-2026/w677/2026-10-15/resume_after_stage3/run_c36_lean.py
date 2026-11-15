"""Use the existing pinned Lean checker, writing every artifact in this folder."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
root = Path(__file__).resolve().parent
module_path = Path('~/.claude/dreaming/lean_check.py')
sys.path.insert(0, str(module_path.parent))
spec = importlib.util.spec_from_file_location('task_lean_check', module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
source = root / 'C36Quartic.lean'
try:
    receipt = module.check_source(source.read_bytes(), source_path=source,
        target='C36.uniform_drift', output_root=root/'lean_checks'/'c36', timeout=90)
except (OSError, ValueError, RuntimeError, KeyError, TypeError, ImportError) as exc:
    receipt = {'status': 'SETUP_UNVERIFIED', 'reason': str(exc)}
receipt['requested_target'] = 'C36.uniform_drift'
receipt['source_sha256'] = hashlib.sha256(source.read_bytes()).hexdigest()
receipt['scope'] = 'Uniform quartic inequality only; no formalization of the stochastic coupling or full T4 obstruction.'
(root/'C36_LEAN_RECEIPT.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps({k:v for k,v in receipt.items() if k not in ['compiler_output','environment']}, default=str))
print(str(receipt.get('compiler_output', ''))[-2600:])
