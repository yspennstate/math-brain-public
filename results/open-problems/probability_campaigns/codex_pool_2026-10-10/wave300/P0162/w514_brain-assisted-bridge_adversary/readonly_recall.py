"""Run named recall commands read-only, with a 60-second recall budget."""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def guard(event, args):
    if event == "open":
        path, mode, flags = args
        writing = (isinstance(mode,str) and any(c in mode for c in "wax+")) or (isinstance(flags,int) and flags & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND))
        if writing and isinstance(path,(str,bytes,os.PathLike)):
            resolved = Path(os.fsdecode(path)).resolve()
            if not resolved.is_relative_to(ROOT):
                raise PermissionError("w514 read-only recall forbids an external write")
    if event in ("os.remove","os.rmdir","os.rename","os.replace","os.mkdir"):
        for value in args[:2]:
            if isinstance(value,(str,bytes,os.PathLike)) and not Path(os.fsdecode(value)).resolve().is_relative_to(ROOT):
                raise PermissionError("w514 read-only recall forbids external mutation")
    if event == "sqlite3.connect":
        database = str(args[0])
        if database != ":memory:" and not (database.startswith("file:") and "mode=ro" in database):
            raise PermissionError("sqlite connections must use mode=ro")

def child(mode, query):
    sys.dont_write_bytecode = True
    sys.addaudithook(guard)
    if mode == "memory":
        import runpy
        sys.path.insert(0,"~/.claude/dreaming")
        sys.argv = ["brain.py","recall",query,"-n","3"]
        runpy.run_path("~/.claude/dreaming/brain.py",run_name="__main__")
    elif mode == "math":
        sys.path.insert(0,"~/math-brain-build/src")
        from math_brain.cli import main
        raise SystemExit(main(["recall","~/math-brain-build/local/population/brain.sqlite3",query,"--limit","8"]))
    else:
        raise ValueError(mode)

def main():
    mode, query = sys.argv[1:3]
    if "--child" in sys.argv:
        child(mode,query)
        return
    started = time.perf_counter()
    try:
        result = subprocess.run([sys.executable,"-B","-X","utf8",str(Path(__file__).resolve()),mode,query,"--child"],
                                capture_output=True,text=True,encoding="utf-8",timeout=60)
        record = {"mode":mode,"query":query,"returncode":result.returncode,
                  "stdout":result.stdout,"stderr":result.stderr,"timed_out":False}
    except subprocess.TimeoutExpired as exc:
        def decode(x):
            return x.decode("utf-8",errors="replace") if isinstance(x,bytes) else (x or "")
        record = {"mode":mode,"query":query,"returncode":None,"stdout":decode(exc.stdout),
                  "stderr":decode(exc.stderr),"timed_out":True}
    record["seconds"] = time.perf_counter()-started
    target = ROOT/("recall_"+mode+".json")
    target.write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in record.items() if k not in ("stdout","stderr")}))
    print(record["stdout"][:18000])
    print(record["stderr"][:2500])

if __name__ == "__main__":
    main()
