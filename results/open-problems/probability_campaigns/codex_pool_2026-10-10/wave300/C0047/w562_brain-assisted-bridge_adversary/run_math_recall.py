"""Run the deployed math-brain CLI with a budget and read-only store."""
import json
import os
import pathlib
import subprocess
import time

root=pathlib.Path(__file__).resolve().parent
env=os.environ.copy()
env["PYTHONPATH"]="~/math-brain-build/src"
env["PYTHONDONTWRITEBYTECODE"]="1"
cmd=["python","-X","utf8","-m","math_brain.cli","recall","~/math-brain-build/local/population/brain.sqlite3","Benjamini Schramm percolation spectral radius nonamenable generating set","--limit","6"]
start=time.perf_counter()
try:
    result=subprocess.run(cmd,env=env,capture_output=True,text=True,encoding="utf-8",errors="replace",timeout=60)
    record={"command":cmd,"elapsed_seconds":time.perf_counter()-start,"timeout":False,"returncode":result.returncode}
    stdout,stderr=result.stdout,result.stderr
except subprocess.TimeoutExpired as exc:
    record={"command":cmd,"elapsed_seconds":time.perf_counter()-start,"timeout":True,"returncode":None}
    def decode(v):return v.decode("utf-8",errors="replace") if isinstance(v,bytes) else v or ""
    stdout,stderr=decode(exc.stdout),decode(exc.stderr)
(root/"math_recall_output.json").write_text(stdout,encoding="utf-8")
(root/"math_recall_stderr.txt").write_text(stderr,encoding="utf-8")
(root/"math_recall_measurement.json").write_text(json.dumps(record,indent=2),encoding="utf-8")
print(json.dumps(record));print(stdout[:12000]);print(stderr[:1500])
