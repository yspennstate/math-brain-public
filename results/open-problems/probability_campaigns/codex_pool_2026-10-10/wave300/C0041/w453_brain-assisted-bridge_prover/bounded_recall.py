"""Call the live read-only recall route with a 60-second in-process budget.

Only this worker's artifacts are written. Disable bytecode and the optional
live recall log. A timer exits this command; no persistent helper is launched.
"""
import os
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
os.environ["BRAIN_RECALL_LOG"] = "0"
sys.dont_write_bytecode = True
start = time.perf_counter()

def timed_out():
    print("TIMEOUT: 60-second recall budget exhausted", flush=True)
    os._exit(124)

timer = threading.Timer(60, timed_out)
timer.daemon = True
timer.start()
try:
    sys.path.insert(0, "~/.claude/dreaming")
    import brain
    brain.recall("C0041 uniformly elliptic iid RWRE directional transience ballisticity regeneration mistakes", n=3)
finally:
    timer.cancel()
    print(f"ELAPSED_SECONDS: {time.perf_counter() - start:.6f}", flush=True)
