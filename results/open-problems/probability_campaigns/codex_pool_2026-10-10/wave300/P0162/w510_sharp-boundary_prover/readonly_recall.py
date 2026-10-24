"""Run the requested recall with a 60s timeout and deny persistent live writes."""
from __future__ import annotations
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
QUERY = "P0162 Fourier entropy influence sharp boundary proof mistakes"

CHILD = r'''
import os, pathlib, runpy, sys
root=pathlib.Path(sys.argv[1]).resolve()
brain=sys.argv[2]
query=sys.argv[3]
sys.dont_write_bytecode=True
def guard(event,args):
    if event=='open':
        path, mode, flags=args
        writing=(isinstance(mode,str) and any(c in mode for c in 'wax+')) or (isinstance(flags,int) and bool(flags & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC)))
        if writing and isinstance(path,(str,bytes,os.PathLike)):
            p=pathlib.Path(os.fsdecode(path)).resolve()
            if p!=root and root not in p.parents:
                raise PermissionError('w510 read-only recall denies live write')
    if event in ('os.remove','os.rmdir','os.rename','os.replace'):
        raise PermissionError('w510 read-only recall denies deletion or move')
    if event=='os.mkdir':
        p=pathlib.Path(os.fsdecode(args[0])).resolve()
        if p!=root and root not in p.parents:
            raise PermissionError('w510 read-only recall denies live mkdir')
    if event=='sqlite3.connect' and 'mode=ro' not in str(args[0]):
        raise PermissionError('w510 recall requires read-only SQLite URI')
    if event in ('subprocess.Popen','socket.connect'):
        raise PermissionError('w510 recall denies model helpers and network')
sys.addaudithook(guard)
sys.path.insert(0,str(pathlib.Path(brain).parent))
sys.argv=[brain,'recall',query]
runpy.run_path(brain,run_name='__main__')
'''

def main():
    started=time.perf_counter()
    env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONUTF8="1")
    command=[sys.executable,"-X","utf8","-c",CHILD,str(ROOT),"~/.claude/dreaming/brain.py",QUERY]
    receipt={"query":QUERY,"timeout_seconds":60,"live_write_policy":"denied by Python audit hook","network_and_helper_policy":"denied"}
    try:
        completed=subprocess.run(command,env=env,capture_output=True,text=True,encoding="utf-8",errors="replace",timeout=60)
        output=completed.stdout+completed.stderr
        receipt.update(state="returned",exit_code=completed.returncode)
    except subprocess.TimeoutExpired as exc:
        output="Recall timed out after 60 seconds. Use the named memory scar as fallback.\n"
        receipt.update(state="timeout",exit_code=None)
    receipt["wall_seconds"]=time.perf_counter()-started
    (ROOT/"RECALL_OUTPUT.txt").write_text(output,encoding="utf-8")
    (ROOT/"RECALL_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(receipt))
    print(output[:4500])

if __name__=="__main__":
    main()
