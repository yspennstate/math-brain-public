"""Run dependent worker-local preparation before the authorized draft submission."""
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parent
for script in ("record_audit.py", "make_deliverables.py", "submit_draft.py"):
    runpy.run_path(str(ROOT / script), run_name="__main__")
