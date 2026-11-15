"""Best-effort recall using the existing tool without shared writes or threads.

The external store is deliberately immutable/read-only; recent WAL-only records
may therefore be absent. Failure is recorded rather than relaxing the guard.
"""
import os
from pathlib import Path
import runpy
import sqlite3
import sys

ROOT = Path(__file__).resolve().parent
os.environ.update({
    "MATH_RECALL_SERVER_DISABLE":"1", "MATH_STRENGTH_NOLOG":"1",
    "MATH_STRENGTH_OFF":"1", "MATH_RECALL_FAST_ENCODER":"0",
    "MATH_BRAIN_SEMANTIC":"0", "MATH_RECALL_CACHE_DIR":str(ROOT/"recall_cache"),
    "MATH_RECALL_FAST_KEEP_MB":"64"})

original_connect = sqlite3.connect


def immutable_connect(database, *args, **kwargs):
    name = os.fsdecode(database)
    if name != ":memory:":
        if not name.startswith("file:"):
            name = Path(name).resolve().as_uri()
        name += ("&" if "?" in name else "?")+"mode=ro&immutable=1"
        kwargs["uri"] = True
    return original_connect(name, *args, **kwargs)


sqlite3.connect = immutable_connect

# Refuse encoder/background helper threads. This leaves the lexical tool path.
import threading


def no_thread(self):
    raise RuntimeError("Recall worker threads disabled by this session's resource rule")


threading.Thread.start = no_thread
script = Path(r"~\.claude\dreaming\math_recall.py")
sys.path.insert(0,str(script.parent))
sys.argv = [str(script),"strong log concavity total variation Wasserstein clipping",
            "--or","log concave sampling query complexity subpolynomial",
            "--or","T304 sampling oracle lower bound", "--limit","4"]
runpy.run_path(str(script),run_name="__main__")
