"""Fresh, conservative local resource gate. No services/process priorities changed.

Honors the governor's commit/physical critical thresholds and worker commit floor.
Only this bounded one-thread check is launched; no model, GPU, or network is used.
"""
import ctypes
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class MemoryStatus(ctypes.Structure):
    _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong),
                ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]


def main():
    gate = {"sampled_at_unix": time.time(), "permitted": False,
            "policy": "COMPUTE_DOCTRINE critical thresholds + worker GATE.json; no gate weakening",
            "planned_work": "one-thread small floating-point enumerations; no model/GPU/network"}
    try:
        memory = MemoryStatus()
        memory.dwLength = ctypes.sizeof(memory)
        if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory)):
            raise RuntimeError("GlobalMemoryStatusEx failed")
        state_path = Path("~/.claude/compute/compute_state.json")
        state = json.loads(state_path.read_text(encoding="utf-8-sig"))
        config = json.loads(Path("~/brain_workers/GATE.json").read_text())
        available_phys_gb = memory.ullAvailPhys / 2**30
        available_commit_gb = memory.ullAvailPageFile / 2**30
        commit_used_pct = 100 * (1 - memory.ullAvailPageFile / memory.ullTotalPageFile)
        age = time.time() - state_path.stat().st_mtime
        critical_reasons = []
        if available_phys_gb <= 4:
            critical_reasons.append("memory_physical_critical")
        if available_commit_gb <= max(8, config["commit_floor_gb"]) or commit_used_pct >= 90:
            critical_reasons.append("memory_commit_critical")
        if age > 60:
            critical_reasons.append("stale_governor")
        if state.get("status") in {"distress", "critical"} or state.get("mode") == "throttle":
            critical_reasons.append("governor_distress_or_throttle")
        if state.get("cpu_pct") is None or float(state["cpu_pct"]) >= 90:
            critical_reasons.append("cpu_saturation_or_missing_telemetry")
        gate.update({"available_physical_gb": available_phys_gb,
                     "available_commit_gb": available_commit_gb,
                     "commit_used_pct": commit_used_pct,
                     "governor_age_seconds": age,
                     "governor_status": state.get("status"),
                     "governor_mode": state.get("mode"), "cpu_pct": state.get("cpu_pct"),
                     "critical_reasons": critical_reasons,
                     "permitted": not critical_reasons, "sampled_at_unix": time.time()})
    except Exception as exc:
        gate["error"] = str(exc)
    (ROOT / "compute_gate.json").write_text(json.dumps(gate, indent=2), encoding="utf-8")
    with (ROOT / "RESOURCE_GATES.jsonl").open("a", encoding="utf-8") as out:
        out.write(json.dumps(gate) + "\n")
    print(json.dumps(gate), flush=True)
    if not gate["permitted"]:
        print("ENUMERATION_DEFERRED: resource gate refused; analytic proofs retained.", flush=True)
        return 3
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    run = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "verify_entropy_route.py"),
                          "--gate-receipt", str(ROOT / "compute_gate.json")],
                         cwd=ROOT, env=env, timeout=120,
                         creationflags=subprocess.CREATE_NO_WINDOW)
    return run.returncode


if __name__ == "__main__":
    raise SystemExit(main())
