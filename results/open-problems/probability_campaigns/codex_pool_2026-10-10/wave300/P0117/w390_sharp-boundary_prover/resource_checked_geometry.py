"""Fresh, conservative local pressure gate followed immediately by tiny CPU checks."""
from __future__ import annotations

import ctypes
from ctypes import wintypes as wt
import datetime as dt
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
STATE = Path('~/.claude/compute/compute_state.json')


class MemoryStatus(ctypes.Structure):
    _fields_ = [('length', wt.DWORD), ('load', wt.DWORD)] + [
        (n, ctypes.c_ulonglong) for n in ('total_phys', 'avail_phys', 'total_page', 'avail_page',
                                         'total_virtual', 'avail_virtual', 'extended')]


def cpu_ticks():
    vals = [wt.FILETIME(), wt.FILETIME(), wt.FILETIME()]
    if not ctypes.windll.kernel32.GetSystemTimes(*(ctypes.byref(v) for v in vals)):
        raise OSError('GetSystemTimes failed')
    return [v.dwHighDateTime * 2 ** 32 + v.dwLowDateTime for v in vals]


def main():
    state = json.loads(STATE.read_text(encoding='utf-8-sig'))
    memory = MemoryStatus()
    memory.length = ctypes.sizeof(memory)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory)):
        raise OSError('GlobalMemoryStatusEx failed')
    t0 = cpu_ticks()
    time.sleep(.25)
    t1 = cpu_ticks()
    idle, kernel, user = [b - a for a, b in zip(t0, t1)]
    cpu = 100 * (1 - idle / max(1, kernel + user))
    age = time.time() - STATE.stat().st_mtime
    headroom_mb = memory.avail_page / 2 ** 20
    free_mb = memory.avail_phys / 2 ** 20
    effective_commit = state.get('commit_eff_used_pct', state.get('commit_used_pct'))
    permit = (age <= 60 and state.get('status', 'UNKNOWN') in {'ok', 'warn'}
              and not state.get('hung_windows') and cpu < 85 and headroom_mb >= 1024
              and free_mb >= 1024 and isinstance(effective_commit, (int, float))
              and effective_commit < 95)
    result = {'at_utc': dt.datetime.now(dt.timezone.utc).isoformat(), 'permit': permit,
              'governor_status': state.get('status'), 'governor_age_seconds': age,
              'live_cpu_pct': cpu, 'live_commit_headroom_mb': headroom_mb,
              'live_physical_free_mb': free_mb, 'effective_commit_used_pct': effective_commit,
              'hung_ui': bool(state.get('hung_windows')),
              'budget': 'One sequential deterministic graph check, <=3 CPU seconds, no GPU, no model, no subprocess worker pool.',
              'policy_source': '12_cognitive_architecture/compute_governor/COMPUTE_DOCTRINE.md'}
    receipt = ROOT / 'reports' / 'geometry_gate.json'
    receipt.write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2), flush=True)
    if not permit:
        print('CHECKS_DEFERRED: fresh local pressure gate did not permit computation; proof remains a written author proof.')
        return 2
    # Same foreground command; no process survives return. The verifier enforces receipt freshness.
    run = subprocess.run([sys.executable, '-X', 'utf8', str(ROOT / 'check_geometry.py'),
                          '--gate-receipt', str(receipt)], cwd=ROOT, timeout=30)
    return run.returncode


if __name__ == '__main__':
    raise SystemExit(main())
