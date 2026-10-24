"""Fail-closed resource gate followed by the two small local checks, if allowed."""

import contextlib
import ctypes
import io
import json
import runpy
import time
from datetime import datetime, timezone
from pathlib import Path

import psutil


ROOT = Path(__file__).resolve().parent


class PerformanceInfo(ctypes.Structure):
    _fields_ = [("cb", ctypes.c_ulong)] + [
        (name, ctypes.c_size_t) for name in (
            "CommitTotal", "CommitLimit", "CommitPeak", "PhysicalTotal",
            "PhysicalAvailable", "SystemCache", "KernelTotal", "KernelPaged",
            "KernelNonpaged", "PageSize")
    ] + [(name, ctypes.c_ulong) for name in ("HandleCount", "ProcessCount", "ThreadCount")]


sample = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "cpu_percent": psutil.cpu_percent(interval=0.25),
    "available_memory_bytes": psutil.virtual_memory().available,
    "max_base_dimension": 8,
    "max_wall_seconds": 30,
    "gpu": False,
    "training": False,
}
info = PerformanceInfo()
info.cb = ctypes.sizeof(info)
api = ctypes.WinDLL("psapi").GetPerformanceInfo
api.argtypes = [ctypes.POINTER(PerformanceInfo), ctypes.c_ulong]
api.restype = ctypes.c_int
ok = bool(api(ctypes.byref(info), info.cb)) and info.CommitLimit > 0
sample["commit_telemetry_available"] = ok
if ok:
    sample["commit_percent"] = 100 * info.CommitTotal / info.CommitLimit
    sample["commit_headroom_bytes"] = (info.CommitLimit - info.CommitTotal) * info.PageSize
sample["allow"] = bool(
    ok and sample["cpu_percent"] < 85
    and sample["available_memory_bytes"] > 8 * 1024 ** 3
    and sample["commit_percent"] < 85
    and sample["commit_headroom_bytes"] > 16 * 1024 ** 3
)
sample["policy"] = "CPU <85%, physical headroom >8 GiB, commit <85%, commit headroom >16 GiB; fail closed"
(ROOT / "COMPUTE_GATE.json").write_text(json.dumps(sample, indent=2) + "\n", encoding="utf-8")
if not sample["allow"]:
    print("Fresh resource gate denied; no experiment run")
    raise SystemExit(2)

started = time.perf_counter()
buffer = io.StringIO()
with contextlib.redirect_stdout(buffer):
    runpy.run_path(str(ROOT / "check_proxy.py"), run_name="__main__")
    runpy.run_path(str(ROOT / "audit_split.py"), run_name="__main__")
elapsed = time.perf_counter() - started
assert elapsed < 30
(ROOT / "GATED_MEASUREMENT.txt").write_text(buffer.getvalue(), encoding="utf-8")
print(f"Fresh-gated checks passed in {elapsed:.6f} seconds")
