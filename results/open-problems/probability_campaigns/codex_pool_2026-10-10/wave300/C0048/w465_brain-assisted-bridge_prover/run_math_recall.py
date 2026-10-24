import sys
from run_bounded_recall import run

run("math_recall_corrected", [sys.executable, "-X", "utf8", "-c", "from math_brain.cli import main; raise SystemExit(main())", "recall", "~/math-brain-build/local/population/brain.sqlite3", "Potts nearest-neighbor discontinuity q 3 d 3 wired free critical", "--limit", "5", "--decision", "--skip-unknown-edges"], seconds=60, env_extra={"PYTHONPATH":"~/math-brain-build/src"})
