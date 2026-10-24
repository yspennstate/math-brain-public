import ctypes
import json
import shutil
import sys
import time
from pathlib import Path

sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent

class MemoryStatus(ctypes.Structure):
    _fields_=[('length',ctypes.c_ulong),('load',ctypes.c_ulong),
              ('total_phys',ctypes.c_ulonglong),('avail_phys',ctypes.c_ulonglong),
              ('total_page',ctypes.c_ulonglong),('avail_page',ctypes.c_ulonglong),
              ('total_virtual',ctypes.c_ulonglong),('avail_virtual',ctypes.c_ulonglong),
              ('avail_extended',ctypes.c_ulonglong)]

state_path=Path('~/.claude/compute/compute_state.json')
state=json.loads(state_path.read_text(encoding='utf-8-sig'))
now=time.time()
age=now-state_path.stat().st_mtime
mem=MemoryStatus()
mem.length=ctypes.sizeof(mem)
if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem)):
    raise SystemExit('Direct memory telemetry failed; no computation admitted.')
gb=1024**3
critical={'memory_physical_critical','memory_commit_critical','disk_critical',
          'process_critical','ui_freeze','starvation'}
reasons=state.get('reasons',[])
commit_headroom=(state.get('commit_limit_mb',0)-state.get('commit_used_mb',0))/1024
disk=shutil.disk_usage(ROOT).free/gb
allowed=(0<=age<=60 and state.get('status') in ('ok','warn') and
         not critical.intersection(reasons) and mem.avail_phys/gb>=3 and
         commit_headroom>=3 and disk>=5)
receipt={'checked_epoch':now,'state_timestamp':state.get('ts'),
         'state_file_age_seconds':age,'status':state.get('status'),'reasons':reasons,
         'cpu_pct_reported':state.get('cpu_pct'),'physical_free_gib':mem.avail_phys/gb,
         'commit_headroom_gib':commit_headroom,'disk_free_gib':disk,
         'allow_small_check':allowed,'scope':'One foreground stdlib arithmetic check; no GPU, no model, no background worker; <=2 CPU seconds.',
         'policy_source':'12_cognitive_architecture/compute_governor/COMPUTE_DOCTRINE.md (live-state and direct checks; no distress override).'}
(ROOT/'evidence').mkdir(exist_ok=True)
receipt_path=ROOT/'evidence'/'compute_gate.json'
receipt_path.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
if not allowed:
    print(json.dumps(receipt,indent=2))
    raise SystemExit('Small computation held by fresh gate.')
import verify_packet
sys.argv=['verify_packet.py','--gate-receipt',str(receipt_path)]
verify_packet.main()
