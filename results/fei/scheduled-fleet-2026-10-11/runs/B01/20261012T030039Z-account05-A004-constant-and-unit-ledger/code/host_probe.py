import os,sys,time
print('HOST_PROBE_START pid='+str(os.getpid()),flush=True)
from pathlib import Path
p=Path(__file__).resolve().parents[1]
print('RUN_PATH '+str(p),flush=True)
print('OUT_FILES '+','.join(f.name for f in (p/'out').iterdir()),flush=True)
print('HELPER_EXISTS '+str((p/'code/ledger_arithmetic.py').exists()),flush=True)
print('HOST_PROBE_DONE',flush=True)
